repodir() {
  repo_base=~/dev
  repo_path=$(find "$repo_base" -mindepth 2 -maxdepth 2 -type d -name "*$1*" | head -n 1)
  if [[ -z "$1" || -z "$repo_path" ]]; then
    repo_path="$repo_base"
  fi
  echo "$repo_path"
}

repo() {
  repo_path=$(repodir "$1")
  echo "$repo_path"
  cd "$repo_path" || return
}
