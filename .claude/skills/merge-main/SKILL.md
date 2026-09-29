---
name: merge-main
description: Pull Request作成前に最新の`origin/main`を作業ブランチへmergeし、競合を安全に解消して検証する。PR前のmain最新化、mainへの追従、merge main、sync main、コンフリクト解決を依頼されたときに使う。
---

# Merge latest main before a pull request

作業ブランチのcommit hashを書き換えず、最新の `origin/main` をmergeで取り込む。rebaseは既定で使わない。

## Preconditions

```bash
git status --short
git branch --show-current
git remote get-url origin
```

- working treeに未コミット変更がある場合は止まり、内容を報告する。ユーザーの変更を自動でcommitまたはstashしない。
- 現在のbranchが `main` の場合はmergeしない。対象の作業ブランチを確認する。
- merge進行中、rebase進行中、またはcherry-pick進行中なら、新しい操作を始めず現在の状態を報告する。

## Sync main

1. 最新のremote tracking branchを取得する。

   ```bash
   git fetch origin main
   ```

2. 作業ブランチに未反映のmain側commitを確認する。

   ```bash
   git log HEAD..origin/main --oneline
   ```

3. 出力が空ならmergeせず検証へ進む。commitがある場合だけmergeする。

   ```bash
   git merge origin/main
   ```

4. merge後に `git status --short` と `git log --oneline --decorate -10` で結果を確認する。

## Resolve conflicts

```bash
git status
git diff --name-only --diff-filter=U
```

- 各conflictの両側の意図と周辺コードを読み、必要な意味を両方保持する。
- `--ours`、`--theirs`、一括checkoutで機械的に上書きしない。
- 判断で公開内容や動作が変わる競合は、選択肢と影響を示してユーザーへ確認する。
- conflict markerを解消したファイルだけをstageする。
- 全競合解消後に `git diff --check` と `rg -n '^(<<<<<<<|=======|>>>>>>>)'` を実行する。
- 続行するなら `git merge --continue`、中断を依頼された場合だけ `git merge --abort` を使う。

## Validate the merged result

変更種別に応じて、少なくとも次を実行する。

```bash
pre-commit run --all-files
docker compose run --rm --entrypoint hugo hugo --minify --destination /tmp/geson-anko-site
```

Dockerを利用できない場合は、実行済みの静的検査と未実施のHugoビルドを明記する。mergeで新たな差分が生じた場合は、その理由と含めるべきcommitを報告する。

## Finish

pushまで依頼されている場合だけ、検証成功後に作業ブランチをpushする。

```bash
git push
```

upstreamが無ければ `git push -u origin HEAD` を使う。PR作成は [github-ops](../github-ops/SKILL.md) に従う。merge方式では通常force-pushは不要であり、使わない。
