#!/bin/sh

if lsof /dev/video0 >/dev/null 2>&1; then
    camera=""
fi

if pacmd list-sources 2>&1 | grep -q RUNNING; then
    mic=""
fi

if [[ -n "$camera" && -n "$mic" ]]; then
	echo " $camera $mic"
elif [[ -n "$camera" ]]; then
	echo " $camera"
elif [[ -n "$mic" ]]; then
	echo " $mic"
else
	echo ""
fi
