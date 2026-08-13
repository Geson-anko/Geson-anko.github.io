---
name: do-on-worktree
description: Git worktreeを使って主作業ツリーのbranch・index・未コミット変更を動かさず、隔離した作業ディレクトリと専用`codex/` branchでサブタスクを実行する。worktreeでの作業、メイン作業を邪魔しない並行作業、隔離したサブタスク、別worktreeへのエージェント委譲を依頼されたときに使う。
---

# Run a subtask in an isolated worktree

主作業ツリーをforegroundとして保持し、サブタスクの調査・編集・検証を別worktreeへ隔離する。

## Choose the worktree mode

- ChatGPTデスクトップアプリで独立chatを開始できる場合は、組み込みの **Worktree** を優先する。作業をLocalへ移すときは **Hand off** を使う。
- 現在のthreadからサブエージェントへ委譲する場合は、親エージェントが手動Git worktreeを作成し、サブエージェントへ絶対pathを渡す。
- 読み取り専用の短い調査にはworktreeを作らず、通常のsubagentまたは並列tool callで十分か先に判断する。

## Protect the primary worktree

- 開始前のprimary worktreeのpath、branch、HEAD、`git status --short`を記録する。
- primary worktreeでcheckout、switch、reset、stash、commit、mergeを行わない。
- primaryに未コミット変更があっても、自動でstashまたはcommitしない。
- 手動worktreeはcommit済みrefを基点にする。primaryの未コミット変更がサブタスクに必要なら停止し、基点の作り方をユーザーへ確認する。
- 同じbranchを複数worktreeへcheckoutしない。各サブタスクに固有branchと固有pathを割り当てる。
- ignored file、secret、dependency directory、build cacheを無断でcopyしない。アプリ管理worktreeで必要なignored fileだけを共有するときは、内容を確認して `.worktreeinclude` を使う。

## Inspect before creation

リポジトリルートで次を確認する。

```bash
git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
git status --short
git worktree list --porcelain
```

基点はユーザー指定ref、指定がなければ現在の `HEAD` commitにする。編集を伴うサブタスクのbranchは `codex/worktree/<YYYYMMDD>/<slug>` とし、local branchと既存worktreeで未使用か確認する。

## Create a manual worktree

1. `mktemp -d`で `/tmp` 配下にタスク固有の空directoryを作り、返された絶対pathを記録する。
2. 記録した空directoryだけを `rmdir` し、Gitがworktree directoryを作成できる状態にする。
3. 編集を伴う場合は専用branchで追加する。

   ```bash
   git worktree add -b codex/worktree/<YYYYMMDD>/<slug> <absolute-worktree-path> <base-ref>
   ```

4. 読み取り・検証だけでbranchが不要な場合はdetached worktreeを使う。

   ```bash
   git worktree add --detach <absolute-worktree-path> <base-ref>
   ```

5. 作成後にworktree自身の状態を確認する。

   ```bash
   git -C <absolute-worktree-path> status --short
   git -C <absolute-worktree-path> branch --show-current
   git worktree list --porcelain
   ```

作成直後の `status --short` をbaselineとして保存する。出力が空でなければサブタスクを開始しない。特にGit LFSのpointer不整合やcheckout filterでtracked fileがmodified扱いになる場合は、自動修正・stage・commitせず、対象fileと原因を報告する。

submoduleが必要なタスクだけ、worktree内で次を実行する。

```bash
git -C <absolute-worktree-path> submodule update --init --recursive
```

## Delegate the subtask

サブエージェントへ次を明示する。

- worktreeの絶対pathと専用branch
- 具体的な目的、成功条件、検証command
- 所有するfileまたはdirectory
- すべてのcommandでworktree pathを `workdir` として使うこと
- primary worktreeへ移動・編集しないこと
- 他エージェントの変更をrevertしないこと
- worktreeのremove、branchのdelete、primaryへの統合を行わないこと
- 最後に変更file、検証結果、未解決事項、commitの有無を返すこと

サブエージェントのdefault cwdがprimaryを指す可能性を前提にし、prompt内のpathだけでなく各tool callの `workdir` も確認する。書き込みタスクには明確な所有範囲を割り当て、同じfileを複数エージェントへ渡さない。

## Review the isolated result

親エージェントがworktree内の結果を検査する。

```bash
git -C <absolute-worktree-path> status --short
git -C <absolute-worktree-path> diff --check
git -C <absolute-worktree-path> diff --stat
git -C <absolute-worktree-path> log -5 --oneline
```

- 検証はworktree内で実行し、primaryのserver、container、port、cacheと競合しないようにする。
- primaryのbranch、HEAD、statusを再確認する。ユーザーが同時にprimaryを変更していた場合は、その状態を保持して差分だけ報告する。
- commit、push、cherry-pick、mergeは、それぞれユーザーの依頼範囲に含まれる場合だけ実行する。

## Integrate or preserve the result

- アプリ管理worktreeからLocalへ移す場合は **Hand off** を優先する。
- 手動worktreeの変更を統合する場合は、まずworktree側で検証済みcommitを作成し、そのcommit hashを報告する。
- primaryへのcherry-pickまたはmergeは明示的に依頼された場合だけ行う。primaryに未コミット変更がある場合は先に競合リスクを報告する。
- 同じbranchをprimaryでcheckoutしたい場合は、先にworktree側をdetached HEADまたは別branchへ移すか、worktreeを安全にremoveする。
- 統合を依頼されていない場合は、worktree path、branch、HEAD、clean/dirty状態を報告して残す。

## Clean up safely

worktreeの削除は、ユーザーがcleanupを依頼し、変更が不要またはcommitで保存済みと確認できた場合だけ行う。

```bash
git -C <absolute-worktree-path> status --short
git worktree remove <absolute-worktree-path>
git worktree prune --dry-run
```

- dirty worktreeへ原則として `--force`を使わない。例外は、この実行で作成した直後かつサブタスク未実行で、保存したbaseline以外の変更が一切ない一時worktreeを取り消す場合だけとする。対象pathとdiffを再確認してからremoveする。
- worktree directoryを `rm -rf`で削除しない。
- branchはworktreeとは別の成果物として扱い、削除を明示的に依頼されるまで残す。
- cleanup失敗時はGit metadataを手作業で消さず、pathと `git worktree list --porcelain` の状態を報告する。
