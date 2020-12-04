## これは何

current directory の git branch を表示。
space で選択、削除出来るツール

## 使い方

適当なところで `git clone` する。

自分は zsh を使っているので、 `.zshrc` に alias を追加

```
alias clean_local="python ~/projects/cli-tool/clean_local.py"
```

以後 `clean_local` で branch 一覧が表示されるので、消したい branch を space で選択 → enter で削除。
