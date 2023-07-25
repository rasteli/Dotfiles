#!/usr/bin/env bash

killall -q volctl

dunst &
volctl &
setxkbmap br &
nitrogen --restore &
/usr/bin/emacs --daemon &
pulsemixer --set-volume 100 &
picom --config ~/.config/picom/picom.conf -b &
