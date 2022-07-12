from libqtile.bar import Bar

from colors import gruvbox

from libqtile.widget.textbox import TextBox
from libqtile.widget.spacer import Spacer
from libqtile.widget.open_weather import OpenWeather
from libqtile.widget.crypto_ticker import CryptoTicker
from libqtile.widget import Mpd2
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.bluetooth import Bluetooth
#from libqtile.widget.df import DF

#from pycoingecko import CoinGeckoAPI
#xmr = CoinGeckoAPI().get_price(ids=['monero'],vs_currencies='pln')

bottom_bar = Bar([
    CheckUpdates(
        background=gruvbox['blue'],
        colour_have_updates=gruvbox['red'],
        colour_no_updates=gruvbox['fg'],
        display_format=' {updates}',
        distro = "Arch",
        execute='alacritty -e sudo /usr/bin/pacman -Syu',
        no_update_string = '',
        update_interval='60'
    ),
    OpenWeather(
#        font='Hack',
        location='Wrocław,PL',
        background=gruvbox['blue'],
        language='PL',
        format='{location_city}: {main_temp} °{units_temperature} | {icon} | {sunrise} {sunset} | {wind_speed} m/s {wind_direction}'
    ),
    Bluetooth(
        background=gruvbox['dark-blue'],
    ),
#    DF(
#        background=gruvbox['fg'],
#        partition='/',
#        measure='G',
#        format='{p} ({uf}{m}|{r:.0f}%)'
#    ),


    Spacer(),
    Mpd2(
        background=gruvbox['fg'],
        status_format='{play_status} {artist} - {title}',
        font='Hack',
        play_states={'pause': '', 'play': '', 'stop': ''},
        prepare_status={'consume': 'c', 'random': 'z', 'repeat': 'r', 'single': '1', 'updating_db': 'U'},
        scroll=True,
        #width=40
    ),
    Spacer(),
    TextBox('💰'),
    CryptoTicker(
        background=gruvbox['green'],
        crypto='ETH',
        currency='PLN',
        symbol='zł',
        format='{crypto} {amount:.2f}{symbol}'
    ),
    CryptoTicker(
        background=gruvbox['yellow'],
        crypto='BTC',
        currency='PLN',
        symbol='zł',
        format='{crypto} {amount:.2f}{symbol}'
    ),
    CryptoTicker(
        background=gruvbox['dark-blue'],
        crypto='USDC',
        currency='PLN',
        symbol='zł',
        format='{crypto} {amount:.2f}{symbol}'
    ),
],
    margin=[0, 0, 0, 0],
    #border_width=[2,0,0,0],
    border_color=[gruvbox['blue'],gruvbox['blue'],gruvbox['blue'],gruvbox['blue']],
    background=gruvbox['bg'],
    opacity=1,
    size=24,
)
