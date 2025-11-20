# Dotfiles

These dotfiles are a fork of the dotfiles by [Rosco Kalis](https://github.com/rkalis/dotfiles).

For more information about dotfiles, he wrote the following blogposts on his blog:
* [Dotfiles: automating macOS system configuration](https://kalis.me/dotfiles-automating-macos-system-configuration/)
* [Increasing development productivity with repository management](https://kalis.me/increasing-development-productivity-repository-management/)
* [Set up a Hyper Key with Hammerspoon on macOS](https://kalis.me/setup-hyper-key-hammerspoon-macos/)

These files have been adapted to my use case.

## Usage
1. Restore your safely backed up ssh keys to `~/.ssh/`
    1. Alternatively, generate new ssh keys, and add these to your GitHub account
2. Install Homebrew and git

  ```bash
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  brew install git
  ```
3. Clone this repository

  ```
  git clone git@github.com:xeophin/dotfiles.git
  ```
4. Run the `bootstrap.sh` script
    1. Alternatively, only run the `setup.sh` scripts in specific subfolders if you don't need everything

## Customisation
I strongly encourage you to play around with the configurations, and add or remove features.
If you would like to use these dotfiles for yourself, I'd recommend changing at least the following:

#### Git
* The .gitconfig file includes my [user] config, replace these with your own user name and email

#### OSX
* At the top of the setup.sh file, my computer name is set, replace this with your own computer name

####  Packages
This folder is a collection of the programs and utilities I use frequently. These lists can easily be amended to your liking.

#### Repos
This folder is a collection of my own repos, some of which are even private. The existing lists can easily be edited or replaced by custom lists.

## Contents

### Root (/)
* bootstrap.sh - Calls all setup.sh scripts

### User Bin (bin/)
* setup.sh - Symlinks the other contents of the folder to `~/bin/`
* imgcat - A utility to display images inline in iTerm 2
* sethidden - A shell script which takes command line arguments to show or hide hidden files
* togglehidden - A shell script that toggles between showing and hiding hidden files

### Color Sync Profiles (colorSync/)
Contains commonly used ColorSync profiles used in Europe (and the newspaper production).

* setup.sh – Symlinks the color profiles to `~/Library/ColorSync/Profiles/`


### Duti (duti/)
* setup.sh - Sets the defaults set up in the different files
* app.package.id - Contains all extensions for the specified program

On the lookout for the bundle ID of an application?

```sh
osascript -e 'id of app "App Name"'
```

### Editor Config (editorconfig/)

* setup.sh – Symlinks the `.editorconfig` file to `~/`
* .editorconfig – The root .editorconfig. Yes, I set it to use tabs. At least for now.

### Git (git/)
* setup.sh - Symlinks all git files to `~/`
* .gitignore_global - Contains global gitignores, such as OS-specific files and several compiled files
* .gitconfig - Sets several global Git variables

### Keyboard Layouts (keyboard-layouts/)
Contains my prefered keyboard layouts ([Deutsch Dvorak Typ II für Mac OS X](http://halibrand.de/dvorak/), as well as my bastardisation of it)

* setup.sh – Symlinks the Keyboard Layouts to `/Library/Keyboard Layouts/`)

### macOS Preferences (macos/)
* setup.sh - Executes a long list of commands pertaining to macOS Preferences

### Packages (packages/)
* setup.sh - Installs the contents of the .list files and the Brewfile

### Python (python/)
* setup.sh - Currently empty, since I don't use Python that often

### Raycast (raycast/)

* script-commands – Script commands to be used with [Raycast](https://www.raycast.com/). Currently empty, requires Raycast to be configured to point here.

### Repositories (repos/)
* setup.sh - Clones the repositories in the .list files at the corresponding locations

### Helper Scripts (scripts/)
* functions.sh - Contains helper functions for symlinking files and printing progress messages

### Services (services/)
Various scripts and workflows that by 

* setup.sh – are being symlinked to `~/Library/Services/`

### Vim (vim/)
* setup.sh - Symlinks all vim files to `~/`
* .vimrc - Basic Vim configuration

### Visual Studio Code (vscode/)
* setup.sh - Symlinks the settings.json file to `~/Library/Application Support/Code/User`
* settings.json - Contains user settings for Visual Studio Code

### Zsh (zsh/)

Configuration and Setup for [Zsh](https://www.zsh.org/).

* setup.sh – Symlinks the `.z*` files to `~/`
* .zprofile – `PATH` support for `pyenv`
* .zsh_alias – Aliases to make working with Zsh faster
* .zsh_plugins.txt – Plugins that should be loaded using the plugin manager [Antibody](https://getantibody.github.io/)
* .zshrc – Zsh Config