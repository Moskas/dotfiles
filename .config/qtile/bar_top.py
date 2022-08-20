from libqtile.bar import Bar
from libqtile.widget import (
    Notify,
    Prompt,
    GroupBox,
    CurrentLayout,
    CurrentLayoutIcon,
    WindowCount,
    WindowName,
    OpenWeather,
    Systray,
    Clock,
    Volume,
    TextBox,
    Spacer,
    Mpd2,
    WidgetBox
)
#from colors import colors
from config import colors
#from .config import colors
#import cpuinfo
#if cpuinfo.get_cpu_info()['vendor_id_raw'] == 'GenuineIntel':
#    vendor = colors['blue']
#else:
#    vendor = colors['red']

bar = Bar([
    TextBox(
        '',
        foreground=colors['blue'],
        #background=colors['dark-blue'],
        fontsize=20,
    ),
    WindowCount(
        text_format='缾 {num}',
        #background=colors['magenta'],
        show_zero=True
    ),
    CurrentLayoutIcon(
        padding=5,
        scale=0.6,
    ),
#    CurrentLayout(),
    GroupBox(
        disable_drag=True,
        active=colors['fg'],
        inactive=colors['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=colors['cyan'],
        borderwidth=0,
        highlight_color=colors['bg'],
        #background=colors['bg'],
        padding=10
    ),
    Spacer(),
        Mpd2(
        #bachground=colors['fg'],
        status_format='{play_status} {artist} - {title}',
        font='Hack',
        play_states={'pause': '', 'play': '', 'stop': ''},
        prepare_status={'consume': 'c', 'random': 'z', 'repeat': 'r', 'single': '1', 'updating_db': 'U'},
        scroll=True,
        #width=40
    ),

    Spacer(),
#   Prompt(foreground=colors['fg']),

#    WindowName(
#        foreground=colors['fg'],
#        #background=colors['bg'],
#        max_chars=20,
#        format='{name}'
#    ),
    Notify(
        action=True,
        fmt='{}'
    ),
    WidgetBox(
        widgets=[
        OpenWeather(
        location='Wrocław,PL',
        language='PL',
        format='{location_city}: {main_temp} °{units_temperature} | {icon} | {sunrise} {sunset} | {wind_speed} m/s {wind_direction}'
    ),

        ],
        text_closed='',
        text_open='',
        close_button_location='right'
    ),

    Systray(
        padding=10,
        icon_size=16,
        #background=colors['gray'],
    ),
    TextBox(' ',
#            #background=colors['gray'],
#            width=8
    ),
#    This isn't needed on PC (Most likely it will stop qtile from launching)
#    Battery(
#        format='{percent:2.0%} {char}',
#        full_char='👌',
#        empty_char=':(',
#        #background=colors['green'],
#        low_background=colors['red'],
#        charge_char='',
#        discharge_char='',
#        font='MesloLGS NF',
#        font='Hack',
#    ),
#    TextBox('',#background=colors['dark-blue'],fontsize=16,),
#    CPU(
#        format='{load_percent}%',
#        #background=colors['dark-blue'],
#        padding=0,
#    ),
#    TextBox('',#background=colors['dark-blue'],width=8),
#    ThermalSensor(
#        foreground=colors['bg'],
#        format='{sensor}',
#        #background=vendor,
#        padding=100,
#    ),
#    NvidiaSensors(
#        foreground=colors['bg'],
#        #background=colors['green'],
#        format='{temp}°C'
#    ),
#    Spacer(length=10),
#    Memory(
#        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
#        #background=colors['blue']),
#    Spacer(length=5),
#    Volume(
#        fmt='Vol:{}',
#        font='MesloLGS NF',
#        #background=colors['dark-yellow'],
#        padding=10,
#        step=5,
#    ),
    Clock(
        #background=colors['fg'],
        format=' %a %H:%M:%S',
    ),
#    Wlan(
#        format=' {essid} {percent:2.0%}',
#        max_chars=6,
#        #background=colors['green'],
#        mouse_callbacks={'Button1':lambda:qtile.cmd_spawn("alacritty -e nmcli")}
#    ),
],

    margin=[0, 0, 0, 0],
#   border_width=[0,0,2,0],
#   border_color=[colors['blue'],gruvbox['blue'],gruvbox['blue'],gruvbox['blue']],
    background=colors['bg'],
    foreground=colors['fg'],
    opacity=1,
    size=25,
)
