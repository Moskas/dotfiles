from libqtile.bar import Bar

from colorschemes.gruvbox_dark import colors

from libqtile.widget.textbox import TextBox
from libqtile.widget.spacer import Spacer
from libqtile.widget.open_weather import OpenWeather
from libqtile.widget.crypto_ticker import CryptoTicker
from libqtile.widget.stock_ticker import StockTicker
from libqtile.widget import Mpd2
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.bluetooth import Bluetooth


bottom_bar = Bar([
    CheckUpdates(
        #bachground=colors['blue'],
        colour_have_updates=colors['red'],
        colour_no_updates=colors['fg'],
        display_format=' {updates}',
        distro = "Arch",
        execute='alacritty -e /usr/bin/paru -Syyu',
        no_update_string = '',
        update_interval='60'
    ),
    OpenWeather(
#        mousecallbacks={lazy.spawn("xdg.open https://google.com")},
#        font='Hack',
        location='Wrocław,PL',
        #bachground=colors['blue'],
        language='PL',
        format='{location_city}: {main_temp} °{units_temperature} | {icon} | {sunrise} {sunset} | {wind_speed} m/s {wind_direction}'
    ),

#    Bluetooth(
#        #bachground=colors['dark-blue'],
#    ),
#    DF(
#        #bachground=colors['fg'],
#        partition='/',
#        measure='G',
#        format='{p} ({uf}{m}|{r:.0f}%)'
#    ),


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
    TextBox('💰'),
#    StockTicker(
#        #bachground=colors['red'],
#        apikey='',
#        market='USD',
#        symbol='INTC'
#    ),
#    CryptoTicker(
#        #bachground=colors['green'],
#        crypto='ETH',
#        currency='PLN',
#        symbol='zł',
#        format='{crypto} {amount:.2f}{symbol}'
#    ),
#    CryptoTicker(
#        #bachground=colors['yellow'],
#        crypto='BTC',
#        currency='PLN',
#        symbol='zł',
#        format='{crypto} {amount:.2f}{symbol}'
#    ),
#    CryptoTicker(
#        #bachground=colors['blue'],
#        crypto='USDC',
#        currency='PLN',
#        symbol='zł',
#        format='{crypto} {amount:.2f}{symbol}'
#    ),
],
    margin=[0, 0, 0, 0],
    #border_width=[2,0,0,0],
    border_color=[colors['blue'],colors['blue'],colors['blue'],colors['blue']],
    background=colors['bg'],
    opacity=1,
    size=24,
)
