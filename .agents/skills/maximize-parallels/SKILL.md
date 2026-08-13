---
name: maximize-parallels
description: 複数の独立したファイル読み取り、検索、コマンド、検証、またはサブタスクを、依存関係と共有状態を確認して安全に並列実行する。複数ファイルの調査、複数角度の検索、独立テスト、並列エージェント、作業の高速化を依頼されたとき、または複数の独立処理へ着手するときに使う。
---

# Maximize safe parallelism

独立した処理を同じ実行フェーズにまとめ、依存関係がある境界だけで待つ。速度より整合性を優先し、共有状態へ同時に書き込まない。

## Decide whether work is independent

次の条件をすべて満たす処理だけを並列化する。

1. 一方の出力が他方の入力にならない。
2. 同じファイル、branch、container、cache、port、DB行などのmutable stateへ同時に書き込まない。
3. 利用するtoolに排他制約または単独呼び出し制約がない。
4. 複数処理が同時に承認を要求しても、ユーザーを混乱させない。

1つでも満たさない場合は逐次実行する。

## Plan execution waves

1. 各処理の入力、出力、副作用を1行ずつ整理する。
2. 出力から入力への依存関係を結ぶ。
3. 依存のない処理を1つのwaveにまとめる。
4. wave内を並列実行し、全結果を確認してから次のwaveへ進む。
5. 失敗した処理だけを再試行し、成功済み処理を不要に繰り返さない。

## Parallelize tool calls

並列化しやすい例:

- 読むファイルが事前に決まっている複数のread。
- `rg`による異なる検索語や対象範囲の調査。
- 相互に書き込まない `git status`、`git log`、設定検査。
- 出力先やcacheを共有しない独立したテスト。

Codexの複数 `exec_command` は、同じorchestration call内で `Promise.all` を使って並列化できる。各commandの `workdir` を明示し、`cd` による暗黙の状態共有を避ける。

次は逐次実行する。

- readした内容を使うedit、生成物を使う検証、SHAを使う後続Git操作。
- 同じファイルへの複数edit。
- checkout、merge、rebase、stash、commitなど同じworking treeを変更するGit操作。
- 同じCompose project、container、port、出力先を使うDockerまたはE2E操作。
- 同じformatterやbuild cacheへ書き込む可能性がある検証。

`web__run`のように単独実行が要求されるtoolは他のtoolと並列にしない。tool固有の説明を常に優先する。

## Use subagents selectively

サブエージェントは、ユーザーが並列作業を依頼した場合、またはこのスキルを明示的に使う場合に、まとまった独立タスクへ使う。数個のreadや短いcommandだけのために起動しない。

- 1エージェントにつき具体的で境界の明確な責務を1つ割り当てる。
- 書き込みを伴う場合は所有するファイルまたはディレクトリを明示し、他エージェントの変更をrevertしないよう伝える。
- shared filesystemを前提に、同じファイルを複数エージェントへ割り当てない。
- 書き込みを主作業ツリーから完全に隔離する必要がある場合は `$do-on-worktree` を使う。
- 読み取り調査、レビュー、ログ分析は並列化しやすい。書き込み作業はconflictコストを考慮する。
- collaboration toolは直接呼び出し、`functions.exec` 内から呼ばない。
- runtimeのconcurrency上限を超えない。親エージェントは結果の統合と最終検証を担当する。

このリポジトリでは、計画を `implementation-planner`、実装を `code-implementer`、挙動不変の整理を `code-refactorer`、文書作業を `project-documenter` に割り当てる。工程に依存がある場合は、計画、実装、リファクタ、文書化の順序を保つ。

## Recover from unsafe parallelism

予期しない競合、lock、port競合、または相互依存が見つかったら、追加の並列処理を止める。現在の状態を読み直し、所有範囲を分割するか逐次実行へ切り替える。ユーザーの既存変更をreset、checkout、stashして解消しない。
