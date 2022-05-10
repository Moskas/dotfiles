#!/bin/bash

# Getting .config from dotfiles
cp -r .config ~

# Installing doom-emacs config
cp -r .doom.d ~
cp -r .emacs.d ~

./.emacs.d/bin/doom install
./.emacs.d/bin/doom sync -u

# Creating temporary folder for cloning
mkdir ~/.temp
cd ~/.temp
# Install Kröhnkite from main repo
git clone https://github.com/esjeon/krohnkite.git --depth 1
cd krohnkite && make install
cd ~/.temp

# Install spacevim with install script
curl -sLf https://spacevim.org/install.sh | bash

