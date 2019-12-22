set -x -g LS_COLORS "di=38;5;27:fi=38;5;7:ln=38;5;51:pi=40;38;5;11:so=38;5;13:or=38;5;197:mi=38;5;161:ex=38;5;9:"

set -x -g TERM "xterm-256color"

# Use en_GB as the message language, but keep everything in swiss german
set -x -g LANG en_GB.UTF-8
set -x -g LC_CTYPE de_CH.UTF-8
set -x -g LC_COLLATE de_CH.UTF-8
set -x -g LC_MONETARY de_CH.UTF-8
set -x -g LC_NUMERIC de_CH.UTF-8
set -x -g LC_TIME de_CH.UTF-8

# Coreutils bin and man folders
set -x -g PATH (brew --prefix coreutils)/libexec/gnubin $PATH
# set -x -g MANPATH (brew --prefix coreutils)/libexec/gnuman $MANPATH

# Findutils bin and man folders
set -x -g PATH (brew --prefix findutils)/libexec/bin $PATH
# set -x -g MANPATH (brew --prefix findutils)/libexec/gnuman $MANPATH

# Pipenv completions
eval (pipenv --completion)

# personal config
set -g fish_user_paths "/usr/local/sbin" $fish_user_paths
set -g fish_user_paths "$HOME/.local/bin" $fish_user_paths

# Set up pyenv for LEDE
set -x PYENV_ROOT "$HOME/.pyenv"

status --is-interactive; and source (pyenv init -|psub)

# Set up powerline
set fish_function_path $fish_function_path (brew --prefix)/lib/python3.7/site-packages/powerline/bindings/fish
powerline-setup

# Add alias file
source  "$HOME/.config/fish/alias.fish"
thefuck --alias | source
set -g fish_user_paths "/usr/local/opt/mongodb@3.6/bin" $fish_user_paths

# Add itch.io butler
set -g fish_user_paths "$HOME/Library/Application Support/itch/apps/butler" $fish_user_paths