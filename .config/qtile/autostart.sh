#!/bin/sh

#~/.fehbg &
feh --bg-scale --randomize /home/moskas/.config/wallpapers/gruvbox/**
setxkbmap pl &
redshift -l manual &
#nm-applet &
#mictray &
#pasystray &
dunst &
#deadd-notification-center &
picom --experimental-backends --backend glx &

# Random apps
discord &

# Rival 3 mouse sensitivity
rivalcfg -s 800 
