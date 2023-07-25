#!/bin/sh

echo_bell() {
	if [ "$(dunstctl is-paused)" = "true" ]; then
		echo ""
	else
		echo ""
	fi
}

case "$1" in
	--toggle)
		dunstctl set-paused toggle
		;;
	*)
		echo_bell ;;
esac
