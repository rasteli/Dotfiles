# Launch the bar
launch_bars() {
    eww -c ${rice_dir}/src/eww daemon &
		polybar -q ryan-bar -c ${rice_dir}/config.ini &
}

launch_bars
