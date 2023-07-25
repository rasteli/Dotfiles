import os

from .colors import get_colors
from libqtile import widget
from libqtile.lazy import lazy

terminal = "alacritty"
colors = get_colors()

def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.Image(
            filename="~/.config/qtile/icons/python.png",
            scale="False",
            mouse_callbacks={"Button1": lazy.spawn("dmenu_run -h 25")},
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            font="mononoki",
            fontsize=15,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[8],
            inactive=colors[2],
            rounded=False,
            disable_drag=False,
            highlight_color=colors[0],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.Sep(linewidth=0, padding=30, foreground=colors[2], background=colors[0]),
        widget.WindowName(
            fontsize=13,
            foreground=colors[6],
            background=colors[0],
            padding=0,
            max_chars=50,
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.TextBox(
            text="",
            background=colors[0],
            foreground=colors[4],
            padding=0, fontsize=51
        ),
        widget.TextBox(
            text=" ",
            padding=2,
            foreground=colors[2],
            background=colors[4],
            fontsize=15,
        ),
        widget.TextBox(
            text=f"{os.uname()[2]}",
            foreground=colors[2],
            background=colors[4]
        ),
        widget.TextBox(
            text="",
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=51
        ),
        widget.Net(
            interface="enp3s0",
            format="{down} {up}",
            foreground=colors[2],
            background=colors[5],
            padding=5,
        ),
        widget.TextBox(
            text="",
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=51
        ),
        widget.TextBox(
            text=" ",
            padding=2,
            foreground=colors[2],
            background=colors[4],
            fontsize=15,
        ),
        widget.DF(
            visible_on_warn=False,
            foreground=colors[2],
            background=colors[4],
            threshold=90,
            padding=5,
            format="{uf}G free",
        ),
        widget.TextBox(
            text="",
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=51
        ),
        widget.TextBox(
            text=" ",
            padding=2,
            foreground=colors[2],
            background=colors[5],
            fontsize=14,
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="{updates} Updates",
            foreground=colors[2],
            mouse_callbacks={"Button1": lazy.spawn(terminal + " -e sudo pacman -Syu")},
            background=colors[5],
            no_update_string="N/A updates"
        ),
        # widget.TextBox(
        # text = '',
        # background = colors[5],
        # foreground = colors[4],
        # padding = 0,
        # fontsize = 51
        # ),
        # widget.TextBox(
        # text = " ",
        # foreground = colors[2],
        # background = colors[4],
        # padding = 0,
        # fontsize = 14
        # ),
        # widget.Memory(
        # foreground = colors[2],
        # background = colors[4],
        # mouse_callbacks = {'Button1': lazy.spawn(terminal + ' -e htop')},
        # padding = 5
        # ),
        widget.TextBox(
            text="",
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=51
        ),
        widget.TextBox(
            text="  Vol:",
            foreground=colors[2],
            background=colors[4],
            padding=0
        ),
        widget.PulseVolume(
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        widget.TextBox(
            text="",
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=51
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[0],
            background=colors[5],
            padding=0,
            scale=0.7,
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[5],
            padding=5
        ),
        widget.TextBox(
            text="",
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=51
        ),
        widget.TextBox(
            text=" ",
            padding=2,
            foreground=colors[2],
            background=colors[4],
            fontsize=14,
        ),
        widget.Clock(
            foreground=colors[2],
            background=colors[4],
            format="%A, %B %d - %H:%M "
        ),
        widget.TextBox(
            text="",
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=51
        ),
        widget.Systray(background=colors[5], padding=5),
        widget.Sep(linewidth=0, background=colors[5]),
    ]
    return widgets_list
