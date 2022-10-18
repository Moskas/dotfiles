#!/bin/sh

xrandr --output DP-0 -s 1920x1080 -r 143.98 --primary
feh --bg-scale --randomize /home/moskas/.config/wallpapers/gruvbox/**
setxkbmap pl &
redshift
dunst &
picom --experimental-backends --backend glx &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# Random apps
discord &

# Rival 3 mouse sensitivity
rivalcfg -s 800 
