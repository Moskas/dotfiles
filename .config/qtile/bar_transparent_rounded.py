from libqtile.bar import Bar

from libqtile.widget.textbox import TextBox
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.cpu import CPU
from libqtile.widget.battery import Battery
from libqtile.widget.memory import Memory
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer
from libqtile.widget.volume import Volume

from libqtile.widget.wlan import Wlan
from libqtile.widget.backlight import Backlight
from libqtile.widget.sensors import ThermalSensor
#from libqtile.widget.pacman import pacman
#from libqtile.widget.BitcoinTicker import *

from colors import gruvbox
from unicodes import left_half_circle, right_half_circle

bar = Bar([
#    left_half_circle(gruvbox['blue']),
#    BitcoinTicker(
#        background=gruvbox['fg'],
#        currency='PLN',
#        format='BTC Buy: {buy}, Sell: {sell}',
#    ),
    TextBox(
        '',
        background=gruvbox['dark-blue'],
        fontsize=20,
    ),
    WindowCount(
        text_format='缾 {num}',
        background=gruvbox['magenta'],
        show_zero=True
    ),
    CurrentLayout(
        background=gruvbox['blue'],
    ),
#    right_half_circle(gruvbox['blue']),
    GroupBox(
        disable_drag=True,
        active=gruvbox['fg'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['yellow'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg'],
        padding=10
    ),


    # Prompt(foreground=gruvbox['fg']),

    WindowName(
        foreground=gruvbox['fg'],
        background=gruvbox['bg']),


#    Spacer(length=100),
#    left_half_circle(gruvbox['fg']),
    Systray(
        padding=10,
        icon_size=16,
        # background='#00000000'
        background=gruvbox['gray'],
    ),
    TextBox(' ',background=gruvbox['gray']),
#    right_half_circle(gruvbox['fg']),
#    Spacer(length=10),
    Battery(
        format='{percent:2.0%} {char}',
        background=gruvbox['yellow'],
        charge_char='',
        discharge_char='',
#        font='MesloLGS NF',
        font='Hack',
    ),
    TextBox(' ',background=gruvbox['dark-blue'],fontsize=16,),
    CPU(
        format='{load_percent}%',
        background=gruvbox['dark-blue'],
        padding=5,
    ),
    ThermalSensor(
        format='{sensor} ',
        background=gruvbox['dark-blue'],
#        padding=100,
    ),
#    Spacer(length=10),

    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['blue']),
#    Spacer(length=5),
    Volume(
        background=gruvbox['dark-yellow'],
        padding=10,
    ),

#    Spacer(length=5),
    Clock(
        background=gruvbox['fg'],
        format=' %Y-%m-%d %a %H:%M %p',
    mouse_callbacks={'Button1':lambda:lazy.spawn("alacritty -e khal calendar")}
    ),
    Wlan(
        format=' {essid} {percent:2.0%}',
        max_chars=6,
        background=gruvbox['green'],
        mouse_callbacks={'Button1':lambda:qtile.cmd_spawn("alacritty -e nmcli")}
    ),
#   TODO fix brightness % not changing with xbacklight commands
#    Backlight(
#        backlight_name='nvidia_0',
#        brightness_file='/sys/class/backlight/nvidia_0/brightness',
#        max_brightness_file='/sys/class/backlight/nvidia_0/max_brightness',
#        step=10,
#        format='{percent}',
#        background=gruvbox['yellow'],
#        update_interval=0.2,
#    ),
],

    margin=[0, 0, 0, 0],
    background=gruvbox['bg'],
    opacity=1,
    size=25,
)
