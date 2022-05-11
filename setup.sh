#!/bin/bash

# Creating temporary folder for cloning
mkdir ~/.temp
function temp() {
cd ~/.temp;
}
# Installing software with pacman and aur helper
sudo pacman -S git neovim emacs rust curl wget zathura zathura-pdf-mupdf zsh

git clone https://aur.archlinux.org/paru.git
cd paru && makepkg -s -i

temp

# Install Kröhnkite from main repo
git clone https://github.com/esjeon/krohnkite.git --depth 1
cd krohnkite && make install

temp

# Install spacevim with install script
curl -sLf https://spacevim.org/install.sh | bash

# Install ohmyzsh from official script
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Getting .config from dotfiles
cd ~/dotfiles/  # I will most likely run it from user home directory so no need for special path
cp -r .config ~

# Installing doom-emacs config
cp -r .doom.d ~
cp -r .emacs.d ~

./$HOME/.emacs.d/bin/doom install
./$HOME/.emacs.d/bin/doom sync -u
