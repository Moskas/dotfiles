import os
import subprocess
from typing import List  # noqa: F401

from libqtile import hook

#from libqtile.extension.dmenu import DmenuRun
from libqtile.extension.window_list import WindowList
#from libqtile.extension.command_set import CommandSet
# import layout objects
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating

# import widgets and bars
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen, KeyChord
from libqtile.lazy import lazy
from bar_top import bar
from bottom_bar import bottom_bar

# import color palette
#from colors import gruvbox
from colors import *
# set mod key "windows/meta" key
mod = "mod4"
# set default terminal
terminal = "alacritty"

keys = [
    # Launch applications
    KeyChord([mod],"w",[
        Key([],"w", lazy.spawn('qutebrowser')),
        Key([],"e", lazy.spawn('emacs')),
        Key([],"d", lazy.spawn('discord')),
        Key([],"s", lazy.spawn('steam')),
    ]),
    #Key([mod], "e", lazy.spawn('alacritty -e ranger -r ~'),desc="Launch nnn in home directory"),
    Key([mod], "o", lazy.spawn('flatpak run com.obsproject.Studio'), desc="Launch OBS"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # rofi shortcuts
    Key([mod], "d", lazy.spawn("rofi -show drun")),
        KeyChord([mod], "s",[
            Key([],"e", lazy.spawn("rofi -show emoji")),
            Key([],"q", lazy.spawn("rofi -show p -modi p:rofi-power-menu -width 20 -lines 6")),
            Key([],"w", lazy.spawn("rofi -show window")),
            Key([],"c", lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort")),
            Key([],"p", lazy.spawn("/home/moskas/.scripts/rofi-pulse")),
            Key([],"b", lazy.spawn("rofi-bluetooth")),
            Key([],"j", lazy.spawn("rofi-wifi-menu")),
            Key([],"m", lazy.spawn("rofi-mpd -l")),
        ]),

    Key([mod],"l",lazy.spawn("betterlockscreen -l")),


    # screenshot shortcuts
    Key(["control"],"Print", lazy.spawn("flameshot gui -c")),
    Key([],"Print", lazy.spawn("flameshot screen -c")),

    # media keys
    Key([],"XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2000")),
    Key([],"XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2000")),
    Key([],"XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # brightness keys
    Key([],"XF86MonBrightnessUp",lazy.spawn('xbacklight -inc 10')),
    Key([],"XF86MonBrightnessDown",lazy.spawn('xbacklight -dec 10')),

    # Command prompt
    # Key([mod], "p", lazy.spawncmd(),
    #     desc="Spawn a command using a prompt widget"),

    # DmenuRun
#    Key([mod, "shift"], 'd', lazy.run_extension(DmenuRun(
#        font="MesloLGS NF",
#        fontsize="13",
#        dmenu_command="dmenu_run",
#        dmenu_prompt=" ",
#        dmenu_height=10,
#        dmenu_lines=15,
#        background=gruvbox['bg'],
#        foreground=gruvbox['fg'],
#        selected_foreground=gruvbox['dark-blue'],
#        selected_background=gruvbox['bg'],
#    ))),

    Key([mod, "shift"], 'w', lazy.run_extension(WindowList(
        all_groups=True,
        font="MesloLGS NF",
        fontsize="13",
        dmenu_prompt=" ",
        dmenu_height=10,
        # dmenu_lines=15,
        background=gruvbox['bg'],
        foreground=gruvbox['fg'],
        selected_foreground=gruvbox['dark-blue'],
        selected_background=gruvbox['bg'],
    ))),

    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode"),

    # Keybindings for resizing windows in MonadTall layout
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "control"], "space", lazy.layout.flip()),

    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = [
    Group('1', label="一", matches=[
          Match(wm_class='firefox'), Match(wm_class='brave'), Match(wm_class='qutebrowser')], layout="columns"),
    Group('2', label="二", matches=[Match(wm_class='emacs'),Match(wm_class='code')],layout="columns"),
    Group('3', label="三", matches=[Match(wm_class='discord')], layout="columns"),
    Group('4', label="四", layout="columns"),
    Group('5', label="五", matches=[Match(wm_class="obs")], layout="columns"),
    Group('6', label="六", layout="columns"),
    Group('7', label="七", matches=[Match(wm_class='steam')],layout="columns"),
    Group('8', label="八", layout="columns"),
    Group('9', label="九",matches=[Match(wm_class="Spotify")],layout="columns"),
    Group('0',label="零",layout="monadtall"),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'alacritty', width=0.4, height=0.7, x=0.3, y=0.1, opacity=0.9),
#    DropDown('discord', 'discord', width=0.4,
#             height=0.6, x=0.3, y=0.1, opacity=1), SHAME
    DropDown('mixer', 'alacritty -o font.size=8 -e pulsemixer', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('music', 'alacritty -e ncmpc', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('bitwarden', 'bitwarden-desktop',
             width=0.4, height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('ranger', 'alacritty -e ranger ~', width=0.4, height=0.7, x=0.3, y=0.1, opacity=0.9),

]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["mod1"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
#    Key(["mod1"], "2", lazy.group['scratchpad'].dropdown_toggle('discord')),
    Key(["mod1"], "2", lazy.group['scratchpad'].dropdown_toggle('music')),
    Key(["mod1"], "3", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key(["mod1"], "4", lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key(["mod1"], "9", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
])

layouts = [
    Stack(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['blue'],
        border_width=2,
        num_stacks=1,
        margin=5,
    ),
    MonadTall(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['blue'],
        margin=5,
        border_width=2,
        single_border_width=2,
        single_margin=5,
    ),
    Columns(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['blue'],
        border_width=2,
        border_normal_stack=gruvbox['dark-gray'],
        border_focus_stack=gruvbox['cyan'],
        border_on_single=2,
        margin=5,
        margin_on_single=5,
    )
]

floating_layout = Floating(
    border_normal=gruvbox['dark-gray'],
    border_focus=gruvbox['dark-blue'],
    border_width=3,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry

        Match(title="Android Emulator - pixel5:5554"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom"),
        Match(wm_class="bitwarden"),
        Match(wm_class="nemo"),
    ])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
widget_defaults = dict(
#    font='TerminessTTF Nerd Font',
#    font='MesloLGS NF',
    fontsize=13,
#    padding=10,
    foreground=gruvbox['fg'],
)

extension_defaults = widget_defaults.copy()

screens = [Screen(top=bar,bottom=bottom_bar
)]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "kittywm"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
