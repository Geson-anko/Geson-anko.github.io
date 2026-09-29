---
name: blender-mcp
description: "Blender MCP 経由で実 Blender を起動・操作し、ブログ記事用の画像（ビューポートのキャプチャやレンダリング）を撮ってページバンドルへ保存する。`just blender` での GUI + MCP サーバー起動、MCP / BlenderMCP アドオンのセットアップ、画像の保存先と形式、同時 1 インスタンス制約。Triggers: 'blender', 'Blender MCP', 'Blender を起動', 'Blender で撮って', 'スクリーンショット', 'ビューポート', 'レンダリング', '3D モデルの画像', '記事に Blender の画像'."
---

# Blender MCP で記事用の画像を撮る

Claude から実 Blender を操作し、記事の図版になる画像を作って `content/blog/<slug>/` のページバンドルへ保存するための手順。

## セットアップ

### 1. MCP サーバー（repo 側 / コミット済み）

[.mcp.json](../../../.mcp.json) が `uvx mcp-for-blender` を stdio サーバー `blender` として登録している。`DISABLE_TELEMETRY=true` で upstream のテレメトリを止めている。

`.claude/settings.json` の `enabledMcpjsonServers: ["blender"]` により、サーバー自体は承認プロンプトなしで有効になる。個々の MCP ツール呼び出しは allow に入れていないので、実行時に承認を求められる。`uvx` が PATH に必要。`.mcp.json` を反映するため、初回は Claude Code を再起動する。

### 2. BlenderMCP アドオン（Blender 側 / マシンごとに 1 回）

```bash
uvx mcp-for-blender install-addon
```

Blender の **Edit → Preferences → Add-ons** で **Interface: MCP for Blender** が入っていることを確認する。有効化は `just blender` が行う。古い `addon.py` を手で入れてある場合もそのまま使えるが、サーバーとの版ずれで警告が出たら上のコマンドで更新する。

## 起動

```bash
just blender                       # 空のシーンで起動
just blender path/to/scene.blend   # 既存ファイルを開いて起動
```

[tools/launch_blender.py](../../../tools/launch_blender.py) が BlenderMCP アドオンを有効化し、MCP サーバーまで立ち上げる。N パネルの接続ボタンを手で押す必要はない。

- `just blender` は Blender が終了するまでブロックするので、**Claude から実行するときは Bash の `run_in_background` で走らせる**。
- MCP は background モードでは使えない。必ず GUI で起動する。
- 起動ログに `[just blender] WARNING:` が出たらアドオン未導入。セットアップ 2 を行う。
- `just claude`（Docker コンテナ内の Claude Code）からはホストの Blender に届かない。ホストの Claude Code から使う。

## 画像を撮る

1. `get_scene_info` でシーンの状態を把握する。
2. 構図を決めたら `get_viewport_screenshot` で Claude 自身が見た目を確認する。このツールの画像は一時ファイルなので、記事には使わない。
3. 記事に載せる画像は `execute_blender_code` で **ページバンドルの絶対パスへ PNG で書き出す**。

   ```python
   import bpy

   scene = bpy.context.scene
   scene.render.image_settings.file_format = "PNG"
   scene.render.resolution_x = 1600
   scene.render.resolution_y = 900
   scene.render.resolution_percentage = 100
   scene.render.filepath = "/abs/path/to/content/blog/<slug>/model-overview.png"

   # 最終品質のレンダリング（アクティブカメラから）
   bpy.ops.render.render(write_still=True)
   ```

   ビューポートの見た目（ワイヤーフレームや編集中の表示）をそのまま載せたい場合は、3D ビューの context で `bpy.ops.render.opengl(write_still=True)` を使う。

   ```python
   area = next(a for a in bpy.context.screen.areas if a.type == "VIEW_3D")
   region = next(r for r in area.regions if r.type == "WINDOW")
   with bpy.context.temp_override(area=area, region=region):
       bpy.ops.render.opengl(write_still=True)
   ```

4. 書き出したファイルを Read で開いて確認し、記事から相対パスで参照する。

### 画像の規約

- ファイル名は既存記事に合わせて英小文字のケバブケース（例: `mold-split-wireframe.png`）。
- 色空間は sRGB にする。Blender の PNG 出力は通常 sRGB だが、`sips -g space <file>` で確認できる。
- 画像は Git LFS 管理（`.gitattributes`）。追加した画像だけを明示的に stage する。

## 制約と注意

- **MCP サーバーは同時 1 インスタンスのみ**（既定ポート 9876）。複数の Claude セッションや worktree、他リポジトリの Blender MCP と同時に使わない。
- MCP から実行した Python は Blender のシーンやユーザー設定を変えうる。保存したい作業ファイルは複製してから開き、破壊的な操作の前には何をするか一言説明する。
- Blender のロケールが日本語だと、`primitive_cube_add` などで作るオブジェクト名が `立方体` になる。名前でオブジェクトを引くときは注意する。

## うまくいかないとき

| 症状                   | 原因と対処                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| MCP ツールが見えない   | Claude Code を再起動する。`/mcp` で `blender` が connected か確認する                              |
| MCP サーバーが立たない | 起動ログの `[just blender] WARNING:` を確認する。アドオン名が違う場合は `BLENDER_MCP_ADDON=<名前>` |
| ポートが埋まっている   | 他の Blender / MCP が残っている。`lsof -nP -iTCP:9876 -sTCP:LISTEN` で確認して落とす               |
| 画像が真っ黒・空       | カメラやライトが無い。`render.opengl` はビューポート表示を、`render.render` はカメラ視点を使う     |
