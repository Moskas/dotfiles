from libqtile.bar import Bar
from libqtile.widget.prompt import Prompt
from libqtile.widget.textbox import TextBox
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget import CPU
from libqtile.widget import NvidiaSensors 
#from libqtile.widget.battery import Battery
from libqtile.widget.memory import Memory
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer
from libqtile.widget.volume import Volume

from libqtile.widget.wlan import Wlan
from libqtile.widget.sensors import ThermalSensor
#from libqtile.widget.open_weather import OpenWeather

from colors import gruvbox

bar = Bar([
#    OpenWeather(
#        location='Wrocław,PL',
#        background=gruvbox['fg']
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


    Prompt(foreground=gruvbox['fg']),

    WindowName(
        foreground=gruvbox['fg'],
        background=gruvbox['bg'],
    ),

    Systray(
        padding=10,
        icon_size=16,
        background=gruvbox['gray'],
    ),
    TextBox(' ',background=gruvbox['gray'],width=8),
#    This isn't needed on PC (Most likely it will stop qtile from launching)
#    Battery(
#        format='{percent:2.0%} {char}',
#        background=gruvbox['yellow'],
#        charge_char='',
#        discharge_char='',
#        font='MesloLGS NF',
#        font='Hack',
#    ),
    TextBox('',background=gruvbox['dark-blue'],fontsize=16,),
    CPU(
        format='{load_percent}%',
        background=gruvbox['dark-blue'],
        padding=0,
    ),
    TextBox('',background=gruvbox['dark-blue'],width=8),
    ThermalSensor(
        format='{sensor}',
        background=gruvbox['dark-red'],
#        padding=100,
    ),
    NvidiaSensors(
        background=gruvbox['green'],
        format='{temp}°C'
    ),
#    Spacer(length=10),

    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['blue']),
#    Spacer(length=5),
    Volume(
        fmt='Vol:{}',
        font='MesloLGS NF',
        background=gruvbox['dark-yellow'],
        padding=10,
        step=5,
    ),

#    Spacer(length=5),
    Clock(
        background=gruvbox['fg'],
        format=' %a %H:%M:%S',
    ),
#    Wlan(
#        format=' {essid} {percent:2.0%}',
#        max_chars=6,
#        background=gruvbox['green'],
#        mouse_callbacks={'Button1':lambda:qtile.cmd_spawn("alacritty -e nmcli")}
#    ),
],

    margin=[0, 0, 0, 0],
#    border_width=[0,0,2,0],
#    border_color=[gruvbox['blue'],gruvbox['blue'],gruvbox['blue'],gruvbox['blue']],
    background=gruvbox['bg'],
    opacity=1,
    size=25,
)
