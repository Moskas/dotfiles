from libqtile.bar import Bar
from libqtile.widget import (
    Prompt,
    GroupBox,
    CurrentLayout,
    WindowCount,
    WindowName,
#CPU,
#    NvidiaSensors,
    Battery,
#    Memory,
    Systray,
    Clock,
#    Spacer,
    Volume,
#   Wlan,
#    sensors,
    TextBox
)
from colors import gruvbox

import cpuinfo
if cpuinfo.get_cpu_info()['vendor_id_raw'] == 'GenuineIntel':
    vendor = gruvbox['blue']
else:
    vendor = gruvbox['red']

bar = Bar([
    TextBox(
        '',
        foreground=gruvbox['blue'],
        #background=gruvbox['dark-blue'],
        fontsize=20,
    ),
    WindowCount(
        text_format='缾 {num}',
        #background=gruvbox['magenta'],
        show_zero=True
    ),
    CurrentLayout(
        #background=gruvbox['blue'],
    ),
    GroupBox(
        disable_drag=True,
        active=gruvbox['fg'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['yellow'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        #background=gruvbox['bg'],
        padding=10
    ),


    Prompt(foreground=gruvbox['fg']),

    WindowName(
        foreground=gruvbox['fg'],
        #background=gruvbox['bg'],
        max_chars=20,
        format='{name}'
    ),

    Systray(
        padding=10,
        icon_size=16,
        #background=gruvbox['gray'],
    ),
    TextBox(' ',
            #background=gruvbox['gray'],
            width=8
    ),
#    This isn't needed on PC (Most likely it will stop qtile from launching)
    Battery(
        format='{percent:2.0%} {char}',
        full_char='👌',
        empty_char=':(',
        #background=gruvbox['green'],
        low_background=gruvbox['red'],
        charge_char='',
        discharge_char='',
#        font='MesloLGS NF',
#        font='Hack',
    ),
#    TextBox('',#background=gruvbox['dark-blue'],fontsize=16,),
#    CPU(
#        format='{load_percent}%',
#        #background=gruvbox['dark-blue'],
#        padding=0,
#    ),
#    TextBox('',#background=gruvbox['dark-blue'],width=8),
#    ThermalSensor(
#        foreground=gruvbox['bg'],
#        format='{sensor}',
#        #background=vendor,
#        padding=100,
#    ),
#    NvidiaSensors(
#        foreground=gruvbox['bg'],
#        #background=gruvbox['green'],
#        format='{temp}°C'
#    ),
#    Spacer(length=10),
#    Memory(
#        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
#        #background=gruvbox['blue']),
#    Spacer(length=5),
    Volume(
        fmt='Vol:{}',
        font='MesloLGS NF',
        #background=gruvbox['dark-yellow'],
        padding=10,
        step=5,
    ),
    Clock(
        #background=gruvbox['fg'],
        format=' %a %H:%M:%S',
    ),
#    Wlan(
#        format=' {essid} {percent:2.0%}',
#        max_chars=6,
#        #background=gruvbox['green'],
#        mouse_callbacks={'Button1':lambda:qtile.cmd_spawn("alacritty -e nmcli")}
#    ),
],

    margin=[0, 0, 0, 0],
#   border_width=[0,0,2,0],
#   border_color=[gruvbox['blue'],gruvbox['blue'],gruvbox['blue'],gruvbox['blue']],
    background=gruvbox['bg'],
    foreground=gruvbox['fg'],
    opacity=1,
    size=25,
)
