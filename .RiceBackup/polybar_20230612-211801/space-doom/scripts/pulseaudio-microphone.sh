#!/bin/sh

s1="#135"
s2="#136"

status() {
  MUTED=$(pactl list sources | awk "/Source $s1/,/Source $s2/" | awk '/Mute/ {print $2; exit}')

  if [ "$MUTED" = "yes" ]; then
    echo "%{F$red}  Muted%{F-}"
  else
   	echo "%{F$primary}%{F-}  %{F$fore}$(pactl list sources | awk "/Source $s1/,/Source $s2/" | awk -F '/' '/Volume/ {print $2; exit}' | tr -d ' ')%{F-}"
  fi
}

listen() {
    status

    LANG=EN; pactl subscribe | while read -r event; do
        if echo "$event" | grep -q "source" || echo "$event" | grep -q "server"; then
            status
        fi
    done
}

toggle() {
  MUTED=$(pactl list sources | awk "/Source $s1/,/Source $s2/" | awk '/Mute/ {print $2; exit}')
  DEFAULT_SOURCE=$(pactl list sources | awk "/Source $s1/,/Source $s2/" | awk '/Name/ {print $2; exit}')

  if [ "$MUTED" = "yes" ]; then
      pactl set-source-mute "$DEFAULT_SOURCE" 0
  else
      pactl set-source-mute "$DEFAULT_SOURCE" 1
  fi
}

increase() {
  DEFAULT_SOURCE=$(pactl list sources | awk "/Source $s1/,/Source $s2/" | awk '/Name/ {print $2; exit}')
  pactl set-source-volume "$DEFAULT_SOURCE" +5%
}

decrease() {
  DEFAULT_SOURCE=$(pactl list sources | awk "/Source $s1/,/Source $s2/" | awk '/Name/ {print $2; exit}')
  pactl set-source-volume "$DEFAULT_SOURCE" -5%
}

case "$1" in
    --toggle)
        toggle
        ;;
    --increase)
        increase
        ;;
    --decrease)
        decrease
        ;;
    *)
        listen
        ;;
esac
