# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from typing import List  # noqa: F401

from bars.powerline import *
from bars.colors import get_colors

from libqtile.lazy import lazy
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])

@hook.subscribe.client_new
def client_new(client):
    wm_class = client.get_wm_class()[1]

    if wm_class == 'Godot':
        client.togroup("III")

# Mod keys
mod = "mod4"
alt = "mod1"

# Default apps
launcher = "dmenu"
browser = "librewolf"
terminal = "alacritty"
# editor = f"{alacritty} -e nvim"
editor = "emacsclient -c -a 'emacs'"

# Path to menu scripts
home = "/home/rasteli"
menu_path = f'{home}/.local/bin'

colors = get_colors()

### KEYS_START
keys = [
    # GET HELP
    Key([mod, "shift"], "slash", lazy.spawn(f'{home}/.config/qtile/keybindings')),

    # QTILE
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # WINDOW MOVEMENT
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),

    # WINDOW RESIZING
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    #### entering Windows mode! To get out, press ESC
    KeyChord([mod], "r", [
        Key([], "g", lazy.layout.grow()),
        Key([], "s", lazy.layout.shrink()),
        Key([], "n", lazy.layout.normalize()),
        Key([], "m", lazy.layout.maximize())],
        mode="Windows"
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "control"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # MODIFY LAYOUTS
    Key([mod], "f", lazy.window.toggle_floating(), desc="Put the focused window to/from floating mode."),
    Key([mod], "space", lazy.window.toggle_fullscreen(), desc="Put the focused window to/from fullscreen mode."),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # USEFUL PROGRAMS
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -g 5 -l 20 -p 'RUN'"), desc="Launches dmenu."),

    Key([mod], "b", lazy.spawn(browser), desc="Launch default browser."),
    Key([mod, alt], "h", lazy.spawn(f"{terminal} -e htop"), desc="Launch htop."),
    Key([mod, alt], "n", lazy.spawn(f"{terminal} -e sudo ncdu /"), desc="Launch ncdu."),
    Key([mod, alt], "f", lazy.spawn(f"{terminal} -e ranger"), desc="Launch ranger file manager."),
    Key([mod, alt], "Return", lazy.spawn(f"{editor}"), desc="Launch default editor."),

    # PULSEAUDIO
    Key([mod, alt], "a", lazy.spawn(f"{terminal} -e pulsemixer"), desc="Launches pulsemixer."),
    Key([mod, alt], "m", lazy.spawn("pulsemixer --toggle-mute"), desc="Sets volume to/from 0 from/to 100."),

    # MENU SCRIPTS
    Key([mod], "End", lazy.spawn(f"{menu_path}/menu/menu-power-dmenu")),
    KeyChord([mod],"p", [
        Key([], "a", lazy.spawn(f"{menu_path}/menu/menu-ambience -l {launcher}")),
        Key([], "b", lazy.spawn(f"{menu_path}/menu/menu-bin -l {launcher}")),
        Key([], "c", lazy.spawn(f"{menu_path}/menu/menu-editconf -l {launcher}")),
        Key([], "d", lazy.spawn(f"{menu_path}/menu/menu-download -l {launcher}")),
        Key([], "f", lazy.spawn(f"{menu_path}/menu/menu-fontviewer -l {launcher}")),
        Key([], "h", lazy.spawn(f"{menu_path}/hubmenu -l {launcher}")),
        Key([], "i", lazy.spawn(f"{menu_path}/menu/menu-misc -l {launcher}")),
        Key([], "k", lazy.spawn(f"{menu_path}/menu/menu-kill -l {launcher}")),
        Key([], "m", lazy.spawn(f"{menu_path}/menu/menu-mtp -l {launcher}")),
        Key([], "o", lazy.spawn(f"{menu_path}/menu/menu-bookmarks -l {launcher}")),
        Key([], "p", lazy.spawn(f'{menu_path}/menu/menu-passmenu --type -l 15 -p ">" '),),
        Key([], "s", lazy.spawn(f"{menu_path}/menu/menu-websearch -l {launcher}")),
        Key([], "t", lazy.spawn(f"{menu_path}/menu/menu-alacritty-theme -l {launcher}"), ),
        Key([], "v", lazy.spawn(f"{menu_path}/menu/menu-vm -l {launcher}")),
        Key([], "z", lazy.spawn(f"{menu_path}/menu/menu-zathura -l {launcher}")),
        Key(["shift"], "t", lazy.spawn(f"{menu_path}/menu/menu-theme -l {launcher}"))]
    )
]
### KEYS_END

groups = [
    Group("I", layout="monadtall"),
    Group("II", layout="monadtall"),
    Group("III", layout="monadtall"),
    Group("IV", layout="monadtall"),
    Group("V", layout="monadtall"),
    Group("VI", layout="monadtall"),
    Group("VII", layout="monadtall"),
    Group("VIII", layout="monadtall"),
    Group("IX", layout="monadtall"),
]

for index, grp in enumerate(groups):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], str(index + 1), lazy.group[grp.name].toscreen(),
                desc="Switch to group {}".format(grp.name)),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], str(index + 1), lazy.window.togroup(grp.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(grp.name))
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

window_gap = 6
border_focus_color = colors[6][0]
border_normal_color = colors[5][0]

layout_options = {
    "margin": window_gap,
    "border_focus": border_focus_color,
    "border_normal": border_normal_color,
}

layouts = [
    layout.Max(),
    layout.Zoomy(),
    ###############################################
    # layout.Stack(num_stacks=2),
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d']),
    # Try more layouts by unleashing below layouts.
    ###############################################
    layout.Bsp(**layout_options),
    ###############################################
    layout.Tile(**layout_options),
    ###############################################
    layout.Matrix(**layout_options),
    ###############################################
    layout.MonadTall(**layout_options),
    ###############################################
    layout.MonadWide(**layout_options),
    ###############################################
    # layout.RatioTile(**layout_options),
    ###############################################
    # layout.VerticalTile(**layout_options),
    ###############################################
    layout.TreeTab(
        active_bg=colors[6][0],
        active_fg=colors[0][0],
        inactive_bg=colors[1][0],
        inactive_fg=colors[2][0],
        bg_color=colors[0][0],
    ),
    ###############################################
    layout.Floating(border_focus="", border_normal=""),
]

widget_defaults = dict(font="mononoki", fontsize=12, padding=2, background=colors[2])

extension_defaults = widget_defaults.copy()
widgets = init_widgets_list()

screens = [
    Screen(top=bar.Bar(widgets, opacity=1.0, size=24))
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=border_focus_color,
    border_normal=border_normal_color,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(title="pinentry"),                # GPG key password entry
        Match(title="branchdialog"),            # gitk

        Match(wm_class="Yad"),                  # YAD
        Match(wm_class="Godot"),
        Match(wm_class="Steam"),
        Match(wm_class="Lutris"),               # Lutris
        Match(wm_class="maketag"),              # gitk
        Match(wm_class="makebranch"),           # gitk
        Match(wm_class="ssh-askpass"),          # ssh-askpass
        Match(wm_class="confirmreset"),         # gitk
        Match(wm_class="Pinentry-gtk-2"),       # Tutanota keyring prompt
        Match(wm_class="epicgameslauncher.exe") # Epic Games Launcher
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
