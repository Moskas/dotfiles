import os
import subprocess
from typing import List

from libqtile import hook

# from libqtile.extension.window_list import WindowList
# from libqtile.extension.command_set import CommandSet
# import layout objects
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall, MonadThreeCol, MonadWide
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating

# import widgets and bars
from libqtile.config import (
    Click,
    Drag,
    DropDown,
    Group,
    Key,
    Match,
    ScratchPad,
    Screen,
    KeyChord,
)
from libqtile.lazy import lazy
from bar_top import bar

# from bottom_bar import bottom_bar


from colorschemes.gruvbox_dark import colors


# set mod key "windows/meta" key
mod = "mod4"
# set default terminal
terminal = "alacritty"

keys = [
    # Launch applications
    KeyChord(
        [mod],
        "w",
        [
            Key([], "w", lazy.spawn("qutebrowser")),
            Key([], "e", lazy.spawn("emacs")),
            Key([], "d", lazy.spawn("discord")),
            Key([], "s", lazy.spawn("steam")),
        ],
    ),
    Key([mod], "o", lazy.spawn("flatpak run com.obsproject.Studio"), desc="Launch OBS"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # rofi shortcuts
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    KeyChord(
        [mod],
        "s",
        [
            Key([], "s", lazy.spawn("rofi-ttv")),
            Key([], "a", lazy.spawn("bwmenu")),
            Key([], "e", lazy.spawn("rofi -show emoji")),
            Key(
                [],
                "q",
                lazy.spawn("rofi -show p -modi p:rofi-power-menu -width 20 -lines 6"),
            ),
            Key([], "w", lazy.spawn("rofi -show window")),
            Key(
                [],
                "c",
                lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort"),
            ),
            Key([], "p", lazy.spawn("/home/moskas/.scripts/rofi-pulse")),
            Key([], "b", lazy.spawn("rofi-bluetooth")),
            Key([], "j", lazy.spawn("rofi-wifi-menu")),
            Key([], "m", lazy.spawn("rofi-mpd -l")),
        ],
    ),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window")),
    Key([mod], "l", lazy.spawn("betterlockscreen -l")),
    # screenshot shortcuts
    Key(["control"], "Print", lazy.spawn("flameshot gui -c")),
    Key([], "Print", lazy.spawn("flameshot screen -c")),
    # media keys
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2000"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2000"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen mode"),
    Key(
        [mod, "shift"],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode",
    ),
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
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = [
    Group(
        "1",
        label="爵",
        matches=[
            Match(wm_class="firefox"),
            Match(wm_class="brave-browser"),
            Match(wm_class="qutebrowser"),
        ],
        layout="stack",
    ),
    Group(
        "2",
        label="ﭮ",
        matches=[Match(wm_class="discord"), Match(wm_class="signal")],
        layout="stack",
    ),
    Group(
        "3",
        label="",
        matches=[
            Match(wm_class="emacs"),
            Match(wm_class="jetbrains-fleet"),
            Match(wm_class="neovide"),
        ],
        layout="columns",
    ),
    Group("4", label="", matches=[Match(wm_class="Zathura")], layout="monadthreecol"),
    Group("5", label="", matches=[Match(wm_class="Steam")], layout="columns"),
    Group(
        "6",
        label="",
        matches=[Match(wm_class="obs"), Match(wm_class="sxiv")],
        layout="columns",
    ),
    Group("7", label="", layout="columns"),
    Group("8", label="", layout="columns"),
    Group("9", label="ﱮ", layout="columns"),
    Group(
        "0",
        label="",
        matches=[Match(wm_class="Spotify"), Match(wm_class="mpdevil")],
        layout="stack",
    ),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

# Append scratchpad with dropdowns to groups
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term", "alacritty", width=0.6, height=0.7, x=0.2, y=0.0, opacity=0.9
            ),
            DropDown(
                "pixel",
                "alacritty -e scrcpy -b 30M -w -S --max-fps=90",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.0,
                opacity=0.9,
            ),
            DropDown(
                "stock",
                "alacritty -e tickrs",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.0,
                opacity=0.9,
            ),
            DropDown(
                "mixer",
                "alacritty -e pulsemixer",
                width=0.4,
                height=0.2,
                x=0.3,
                y=0,
                opacity=0.9,
            ),
            DropDown(
                "music",
                "alacritty -e ncmpcpp",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.0,
                opacity=0.9,
            ),
            DropDown(
                "bitwarden",
                "bitwarden-desktop",
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=1,
            ),
            DropDown(
                "ranger",
                "alacritty -e ranger /home/moskas/",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.0,
                opacity=0.9,
            ),
        ],
    )
)
# extend keys list with keybinding for scratchpad
keys.extend(
    [
        Key(["mod1"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key(["mod1", "shift"], "1", lazy.group["scratchpad"].dropdown_toggle("stock")),
        Key(["mod1", "shift"], "2", lazy.group["scratchpad"].dropdown_toggle("pixel")),
        Key(["mod1"], "2", lazy.group["scratchpad"].dropdown_toggle("music")),
        Key(["mod1"], "3", lazy.group["scratchpad"].dropdown_toggle("mixer")),
        Key(["mod1"], "4", lazy.group["scratchpad"].dropdown_toggle("ranger")),
        Key(["mod1"], "9", lazy.group["scratchpad"].dropdown_toggle("bitwarden")),
    ]
)

layouts = [
    Stack(
        border_normal=colors["dark-gray"],
        border_focus=colors["blue"],
        border_width=2,
        num_stacks=1,
        margin=5,
    ),
    MonadTall(
        border_normal=colors["dark-gray"],
        border_focus=colors["blue"],
        margin=5,
        border_width=2,
        single_border_width=2,
        single_margin=5,
    ),
    MonadThreeCol(
        border_normal=colors["dark-gray"],
        border_focus=colors["blue"],
        margin=5,
        border_width=2,
        single_border_width=2,
        single_margin=5,
        new_client_position="bottom",
    ),
    Columns(
        border_normal=colors["dark-gray"],
        border_focus=colors["blue"],
        border_width=2,
        border_normal_stack=colors["dark-gray"],
        border_focus_stack=colors["cyan"],
        border_on_single=2,
        margin=2,
        margin_on_single=5,
    ),
]

floating_layout = Floating(
    border_normal=colors["dark-gray"],
    border_focus=colors["dark-blue"],
    border_width=3,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Android Emulator - pixel5:5554"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom"),
        Match(wm_class="bitwarden"),
        Match(wm_class="nemo"),
    ],
)

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
widget_defaults = dict(
    #    font='MesloLGS NF',
    fontsize=13,
    foreground=colors["fg"],
)

extension_defaults = widget_defaults.copy()

screens = [Screen(top=bar)]  # ,bottom=bottom_bar)]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ""
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "kittywm"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])
