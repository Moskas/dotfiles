#              _       _
#             | |     | |
#   __ _ _   _| |_ ___| |__  _ __ _____      _____  ___ _ __
#  / _` | | | | __/ _ \ '_ \| '__/ _ \ \ /\ / / __|/ _ \ '__|
# | (_| | |_| | ||  __/ |_) | | | (_) \ V  V /\__ \  __/ |
#  \__, |\__,_|\__\___|_.__/|_|  \___/ \_/\_/ |___/\___|_|
#     | |
#     |_|


config.load_autoconfig()

import subprocess
import os
from qutebrowser.api import interceptor

c.tabs.background = True
c.new_instance_open_target = "window"
# c.url.start_pages(https://www.google.com)
c.url.searchengines = {"DEFAULT": "https://google.com/search?={}"}
c.downloads.position = "bottom"
c.statusbar.show = "in-mode"
c.tabs.show = "multiple"
# c.spellcheck.languages = ["en-US"]
# Fonts
c.fonts.web.family.sans_serif = '"JetBrainsMono NF"'
c.fonts.web.family.standard = '"JetBrainsMono NF"'
c.fonts.web.family.fixed = '"JetBrainsMono NF"'
c.fonts.contextmenu = '10pt "JetBrainsMono NF"'
c.fonts.completion.entry = '10pt "JetBrainsMono NF"'
c.fonts.completion.category = '10pt "JetBrainsMono NF"'
c.fonts.prompts = '12pt "JetBrainsMono NF"'
c.fonts.hints = '10pt "JetBrainsMono NF"'
c.fonts.statusbar = '12pt "JetBrainsMono NF"'
c.fonts.tabs.selected = '10pt "JetBrainsMono NF"'
c.fonts.tabs.unselected = '10pt "JetBrainsMono NF"'
c.fonts.completion.entry = '12pt "JetBrainsMono NF"'

# Behaviour
c.tabs.new_position.related = "next"  # open new tab next to the focused
c.fileselect.multiple_files.command = ["kitty", "-e", "-ranger", "--choosefiles"]

# Adblock
c.content.blocking.whitelist = ["https://www.ethicalads.io"]

# Keybinds
config.bind("W", "hint links spawn --detach mpv {hint-url}")
config.bind("W", "hint links spawn --detach mpv {hint-url}")
config.bind("ci", "hint inputs")
config.bind("Di", "hint images spawn --detach wget {hint-url}")  # download image
config.bind(
    "Dd", "hint links spawn --detach wget {hint-url}"
)  # download the content of link
config.bind(
    "St", "hint links spawn --detach streamlink {hint-url} best"
)  # open stream with streamlink (I'm not using it anymore tbh)
config.bind("Y", "hint links spawn yt-dlp {hint-url}")
config.bind("ce", "config-edit")  # open config in editor
config.bind(
    "B", "spawn --userscript qute-bitwarden"
)  # open rbw and fill login/password
config.bind("yl", "hint all spawn yank")  # yank the selected link
config.bind("<Shift-Left>", "tab-prev")
config.bind("<Shift-Down>", "back")
config.bind("<Shift-Up>", "forward")
config.bind("<Shift-Right>", "tab-next")
config.bind("<Shift-K>", "tab-next")
config.bind("<Shift-J>", "tab-prev")
# Enable force reloading as shortcut
config.bind("<Ctrl-r>", "reload -f")
# Unbind closing tab with d
config.unbind("d")
config.unbind("D")

config.bind("<Ctrl-h>", "tab-prev")
config.bind("<Ctrl-l>", "tab-next")

# Editor
c.editor.command = ["emacs", "{}"]

# Colorscheme
# config.source("gruvbox.py")


# ====================== xresources ======================= {{{
# taken from https://qutebrowser.org/doc/help/configuring.html
def read_xresources(prefix):
    """
    read settings from xresources
    """
    props = {}
    x = subprocess.run(["xrdb", "-query"], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split("\n")
    for line in filter(lambda l: l.startswith(prefix), lines):
        prop, _, value = line.partition(":\t")
        props[prop] = value
    return props


xresources = read_xresources("*")

c.colors.statusbar.normal.bg = xresources["*background"]
c.colors.statusbar.command.bg = xresources["*background"]
c.colors.statusbar.command.fg = xresources["*foreground"]
c.colors.statusbar.normal.fg = xresources["*foreground"]
c.statusbar.show = "in-mode"

c.colors.tabs.even.bg = xresources["*background"]
c.colors.tabs.odd.bg = xresources["*background"]
c.colors.tabs.even.fg = xresources["*foreground"]
c.colors.tabs.odd.fg = xresources["*foreground"]
c.colors.tabs.selected.even.bg = xresources["*color4"]
c.colors.tabs.selected.even.fg = xresources["*background"]
c.colors.tabs.selected.odd.bg = xresources["*color4"]
c.colors.tabs.selected.odd.fg = xresources["*background"]
c.colors.tabs.pinned.odd.bg = xresources["*color12"]
c.colors.tabs.pinned.odd.fg = xresources["*background"]
c.colors.tabs.pinned.even.bg = xresources["*color12"]
c.colors.tabs.pinned.even.fg = xresources["*background"]
c.colors.hints.bg = xresources["*background"]
c.colors.hints.fg = xresources["*foreground"]
c.hints.border = "1px solid #fbf1c7"

c.colors.webpage.bg = xresources["*foreground"]

# change title format
c.tabs.title.format = "{audio}{current_title}"
# fonts
c.fonts.web.size.default = 16

c.colors.tabs.indicator.stop = xresources["*color14"]
c.colors.completion.odd.bg = xresources["*background"]
c.colors.completion.even.bg = xresources["*background"]
c.colors.completion.fg = xresources["*foreground"]
c.colors.completion.category.bg = xresources["*background"]
c.colors.completion.category.fg = xresources["*foreground"]
c.colors.completion.item.selected.bg = xresources["*background"]
c.colors.completion.item.selected.fg = xresources["*foreground"]

c.qt.args = ["blink-settings=darkMode=4"]
# c.colors.webpage.prefers_color_scheme_dark = True
c.colors.webpage.darkmode.enabled = False

# yomichad setup
for mode in ["normal", "caret"]:
    config.bind("gs", "spawn --userscript yomichad --names", mode=mode)
    config.bind("gS", "spawn --userscript yomichad --prefix-search", mode=mode)
