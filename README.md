# Geson-anko.github.io

GesonAnko の個人サイト。Hugo + Blowfish テーマで構築。

## 必要なもの

- Docker / Docker Compose
- [just](https://github.com/casey/just)

## セットアップ

```bash
# コンテナをビルドして起動
just up

# コンテナ内で初期セットアップ（pre-commit, submodule）
just shell
just setup
```

http://localhost:1313 でプレビューできます。

## コマンド一覧

| コマンド                | 説明                                      |
| ----------------------- | ----------------------------------------- |
| `just up`               | 開発サーバー起動                          |
| `just down`             | コンテナ停止                              |
| `just rebuild`          | コンテナ再ビルド＆再起動                  |
| `just build`            | 本番ビルド（minify）                      |
| `just new blog/my-post` | 新規記事作成                              |
| `just shell`            | コンテナ内シェル                          |
| `just tmux`             | コンテナ内 tmux                           |
| `just claude`           | コンテナ内 Claude Code                    |
| `just format`           | Prettier でフォーマット                   |
| `just lint`             | pre-commit 全ファイルチェック             |
| `just setup`            | pre-commit インストール＆submodule 初期化 |

## 記事の書き方

```bash
just new blog/my-new-post
```

`content/blog/my-new-post/index.md` が生成されます。front matter の `draft: true` を `false` に変えると公開されます。画像は同じフォルダに置けば記事から参照できます。

## ディレクトリ構成

```
content/
  _index.md          # トップページ
  about.md           # プロフィール
  blog/_index.md     # ブログ一覧
  projects/_index.md # プロジェクト一覧
config/_default/     # Hugo / Blowfish 設定
static/              # 画像・PDF・静的ファイル
themes/blowfish/     # テーマ（git submodule）
```

## デプロイ

`main` ブランチへの push で GitHub Actions が自動ビルド＆GitHub Pages にデプロイします。
