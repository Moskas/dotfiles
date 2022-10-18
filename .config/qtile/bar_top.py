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
    WidgetBox,
)

from colorschemes.gruvbox_dark import colors

bar = Bar(
    [
        TextBox(
            "",
            width=40,
            foreground=colors["blue"],
            background=colors["fg1"],
            fontsize=20,
        ),
        # WindowCount(
        #    text_format='缾 {num}',
        #    #background=colors['magenta'],
        #    show_zero=True
        # ),
        # CurrentLayoutIcon(
        #    padding=5,
        #    scale=0.6,
        # ),
        GroupBox(
            fontsize=17,
            disable_drag=True,
            hide_unused=False,
            active=colors["fg4"],
            inactive=colors["fg1"],
            highlight_method="line",
            block_highlight_text_color=colors["yellow"],
            borderwidth=0,
            highlight_color=colors["bg"],
            # background=colors['fg1'],
            padding=10,
        ),
        Spacer(),
        Mpd2(
            # width=800,
            background=colors["fg1"],
            # color_progress=[colors['fg']],
            status_format="{play_status}   {artist} - {title}",
            play_states={"pause": "", "play": "", "stop": ""},
            prepare_status={
                "consume": "c",
                "random": "z",
                "repeat": "r",
                "single": "1",
                "updating_db": "U",
            },
            # scroll=True,
        ),
        Spacer(),
        Notify(action=True, fmt="{}"),
        Systray(
            background=colors["fg1"],
            padding=10,
            icon_size=16,
            # background=colors['gray'],
        ),
        Clock(
            background=colors["fg1"],
            format="  %a %H:%M:%S",
        ),
    ],
    margin=[0, 0, 0, 0],
    #   border_width=[0,0,2,0],
    #   border_color=[colors['blue'],gruvbox['blue'],gruvbox['blue'],gruvbox['blue']],
    background=colors["bg"],
    foreground=colors["fg"],
    opacity=1,
    size=25,
)
