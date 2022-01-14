#!/usr/bin/env sh

DIR=$(dirname "$0")
cd "$DIR"

. ../scripts/functions.sh

SOURCE="$(realpath .)"
DESTINATION="$(realpath ~)"

info "Configuring zsh …"

find . -name ".z*" | while read fn; do
  symlink "$SOURCE/$fn" "$DESTINATION/$fn"
done

set_zsh_shell() {
  if grep --quiet zsh <<< "$SHELL"; then
    success "ZSH shell is already set up."
  else
    substep_info "Adding zsh executable to /etc/shells"
    if grep --fixed-strings --line-regexp --quiet $(which zsh) /etc/shells; then
      substep_success "ZSH executable already exists in /etc/shells."
    else
      if sudo bash -c "echo $(which zsh) >> /etc/shells"; then
        substep_success "ZSH executable added to /etc/shells."
      else
        substep_error "Failed adding ZSH executable to /etc/shells."
        return 1
      fi
    fi

    if chsh -s $(which zsh); then
      substep_success "Changed shell to zsh"
    else
      substep_error "Failed changing shell to zsh"
      return 2
    fi

  fi
}

if set_zsh_shell; then
  success "Successfully set up ZSH as the default shell."
else
  error "Failed setting up ZSH shell."
fi

success "Finished configuring zsh."
