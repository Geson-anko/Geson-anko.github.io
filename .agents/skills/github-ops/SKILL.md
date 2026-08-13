---
name: github-ops
description: GitHub CLIを使って現在のリポジトリの認証確認、作業ブランチのpush、Pull Requestの作成・確認・レビュー、Issue操作を安全に行う。`gh auth`、`git push`、`gh pr`、`gh issue`、PR作成・送信・レビュー、Issue作成を依頼されたときに使う。
---

# GitHub operations

GitHubへの読み書きを、リポジトリのGit規約とユーザーの承認範囲に沿って実行する。

## Guardrails

- 読み取り、push、PR作成、Issue更新など、ユーザーが依頼した操作だけを行う。
- `main`へ直接pushしない。作業ブランチには `codex/` prefixを使う。
- `git push --force`を使わない。`--force-with-lease`も、ユーザーが履歴書き換えを明示的に依頼し、安全性を確認できる場合に限る。
- PRのmerge/close、release作成、repository設定変更、secret操作は明示的な依頼なしに行わない。
- token、`.env`の内容、認証ファイルを出力・commit・PR本文へ掲載しない。
- 外部状態を変更する直前に、repository、branch、PRまたはIssue番号を再確認する。

## Check environment and authentication

リポジトリルートで次を確認する。

```bash
gh --version
gh auth status
git remote -v
git branch --show-current
git status --short
```

コンテナ内のCodexは、ホストからread-onlyで共有された `~/.config/gh` を使う。認証が無い、期限切れ、またはscope不足の場合は、tokenを要求せず、ユーザーにホスト側で `gh auth login` を実行してもらう。

## Prepare and push a branch

現在地が `main` で、ユーザーが変更のcommitまたはpushを依頼した場合は、`main`から作業ブランチを作る。

```bash
git switch -c codex/<type>/<YYYYMMDD>/<short-slug> main
```

push前に対象commitと差分を確認する。

```bash
git log --oneline origin/main..HEAD
git diff --stat origin/main...HEAD
```

初回pushは現在のbranch名を重複指定しない。

```bash
git push -u origin HEAD
```

2回目以降は `git push` を使う。remoteから拒否された場合はforceせず、`$merge-main` で最新の `origin/main` を取り込む。

## Create a pull request

1. `git status --short` が意図した状態か確認する。
2. `git log origin/main..HEAD --oneline` と `git diff origin/main...HEAD` からPRの全変更を把握する。
3. 実際に実行した検証と未実施項目を整理する。成功していない検証を成功済みと書かない。
4. shell展開事故を避けるためPR本文を一時ファイルへ作成し、`--body-file`で渡す。
5. `gh pr create`後に返されたURLとbase/headを確認する。

PR本文は次の最小構成にする。

```markdown
## Summary

- <変更点>

## Validation

- <実行した検証と結果>
- <未実施なら理由>
```

作成コマンド:

```bash
gh pr create --base main --title "<type>(<scope>): <description>" --body-file <body-file>
```

作業途中なら `--draft` を付ける。PRを作成した時点で止め、mergeはユーザーへ委ねる。

## Inspect or review pull requests

```bash
gh pr list
gh pr view <number> --comments
gh pr diff <number>
gh pr checks <number>
```

CI待機を明示的に依頼された場合だけ `gh pr checks <number> --watch` を使う。レビュー投稿はユーザーの依頼内容に応じて次を使う。

```bash
gh pr review <number> --comment --body "<comment>"
gh pr review <number> --approve
gh pr review <number> --request-changes --body "<reason>"
```

## Work with issues

```bash
gh issue list --state open
gh issue view <number> --comments
gh issue create --title "<title>" --body-file <body-file>
gh issue comment <number> --body "<comment>"
gh issue close <number> --comment "<reason>"
```

Issueの作成・コメント・closeはそれぞれ外部書き込みとして扱い、ユーザーが依頼した操作だけを実行する。

## Draft locally before external writes

ネットワーク操作の前に、必要なら次からtitleとbodyを作る。

```bash
git log origin/main..HEAD --format="%s"
git diff --stat origin/main...HEAD
git diff origin/main...HEAD
```

認証・権限・CI失敗時は回避策でガードを無効化せず、`gh auth status`、PR checks、失敗ログを確認して根本原因を報告する。
