# Repository guidance

## Project

- GesonAnko の個人サイト。Hugo と Blowfish テーマで構築する。
- ユーザーへの説明と作業結果は原則として日本語で返す。

## Development principles

### Think before editing

- 調査で解決できる不明点は先に確認し、重要な仮定・曖昧さ・トレードオフを明示する。
- 複数の解釈が結果を大きく変える場合は、独断で決めずユーザーへ確認する。
- 実装前に、変更内容と検証方法を対応づける。複数ステップなら短い計画にする。

### Prefer the smallest solution

- 要求された問題を解く最小限の変更に留め、投機的な機能・抽象化・設定項目を追加しない。
- 既存の規約とスタイルを優先し、周辺コードや文書をついでに整理しない。
- diff の各行がユーザーの要求へ直接トレースできる状態を保つ。

### Make surgical changes

- 無関係な未コミット変更を保持し、明示的な依頼なしに書き換え・削除・stashしない。
- 自分の変更で不要になったものだけ片付ける。既存のdead codeは指摘に留める。
- 生成物やsubmoduleを直接編集せず、正規の入力または生成コマンドを使う。

### Work toward verifiable outcomes

- バグ修正は可能なら再現方法または失敗する検証を先に確立する。
- 実装・修正・リファクタリング後は関連する検査を実行し、成功するまで安全な範囲で反復する。
- 実行できない検証は、理由と未検証範囲を最終報告へ明記する。

## Structure

- `content/`: Markdown のサイトコンテンツ。ブログ記事は `content/blog/<slug>/index.md` と同じページバンドル内の画像で構成する。
- `config/_default/`: Hugo と Blowfish の設定。
- `static/`: そのまま配信する画像や PDF。
- `themes/blowfish/`: Git submodule。明示的に依頼されない限りテーマ本体を変更しない。
- `public/` と `resources/`: 生成物。直接編集しない。
- `.agents/skills/`: タスク発火型のCodex共有スキル。
- `.codex/`: プロジェクト設定とカスタムエージェント。

## Workflow

- 既存の `justfile` を作業コマンドの正本として使う。
- 開発サーバーは `just up`、本番ビルドは `just build`、新規記事は `just new blog/<slug>` で操作する。
- Markdown、TOML、YAML、JSON の変更後は、変更ファイルを対象にPrettierまたはpre-commitを実行する。
- サイトの表示や設定に影響する変更後は、出力先を一時ディレクトリへ変更したHugo本番ビルドで検証する。Dockerを利用できない場合は未実施として報告する。

## Git workflow

- `main` に直接commitまたはpushしない。作業ブランチは `main` から `codex/<種別>/<YYYYMMDD>/<slug>` 形式で作成する。
- 種別は `feature`、`fix`、`refactor`、`docs`、`chore` を使う。
- commitメッセージは `<type>(<scope>): <description>` を基本とする。scopeは `content`、`config`、`theme`、`ci`、`docs`、`tooling` など変更範囲を表す語にする。
- force-push、PRのmerge/close、release作成、repository設定変更は、ユーザーの明示的な依頼なしに実行しない。
- push、PR、Issue操作には `$github-ops`、PR前のmain同期には `$merge-main` を使う。

## Parallel work

- 独立した複数処理では `$maximize-parallels` に従い、読み取りや検証を安全な範囲で並列化する。
- サブエージェントは、ユーザーが並列作業を依頼した場合、または適用中のスキルが明示的に要求する場合にのみ使う。
- 並列編集ではファイル所有範囲を重複させず、親エージェントが結果と検証を統合する。
- 利用可能なカスタムエージェントは `implementation-planner`、`code-implementer`、`code-refactorer`、`project-documenter`。各エージェントの責務外へ変更を広げない。
