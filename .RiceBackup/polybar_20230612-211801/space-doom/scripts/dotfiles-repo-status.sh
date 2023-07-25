#!/bin/sh

status=$(git --git-dir=$HOME/dotfiles/ --work-tree=$HOME status -sb | grep -v '^#' | wc -l)

if [[ "$status" -gt 0 ]]; then
  echo "%{F$primary}%{T6}%{T-}%{F-}  %{F$fore}$status%{F-}"
else
  echo "%{F$primary}%{T6}%{T-}%{F-}  %{F$fore}None%{F-}"
fi
