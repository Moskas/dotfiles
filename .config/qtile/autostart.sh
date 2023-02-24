#!/bin/sh

xrandr --output DP-0 --mode 1920x1080 --rate 143.98
feh --bg-fill --randomize /home/moskas/.config/wallpapers/gruvbox/** &
openrgb -p red & 
betterlockscreen -u ~/.config/wallpapers/gruvbox/**/* 
setxkbmap pl &
dunst &
#picom --experimental-backends --backend glx & # OBSOLETE
picom &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# Random apps
discord &
nicotine &

# Rival 3 mouse sensitivity
rivalcfg -s 800 
# Easyeffects
#easyeffects --gapplication-service &

# SSHFS for local NAS
sshfs -o ~/.ssh/optiplex moskas@optiplex.home:~ ~/nas
