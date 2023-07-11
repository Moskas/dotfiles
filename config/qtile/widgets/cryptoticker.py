from libqtile import bar
from libqtile.widget import base


class RextBox(base._TextBox):
    """A flexible textbox that can be updated from bound keys, scripts, and qshell."""

    defaults = [
        ("font", "sans", "Text font"),
        ("fontsize", None, "Font pixel size. Calculated if None."),
        ("fontshadow", None, "font shadow color, default is None(no shadow)"),
        ("padding", None, "Padding left and right. Calculated if None."),
        ("foreground", "#ffffff", "Foreground colour."),
        ("coin", "bitcoin", "Cryptocurrency symbol"),
        ("fiat", "usd", "Fiat currency"),
    ]  # type: list[tuple[str, Any, str]]

    def __init__(self, text="", coin="", width=bar.CALCULATED, **config):
        self.coin = "bitcoin"
        base._TextBox.__init__(
            self, text=text + coin, width=width, coin=coin, fiat="usd", **config
        )

    def cmd_update(self, text):
        """Update the text in a TextBox widget"""
        self.update(text)

    def cmd_get(self):
        """Retrieve the text in a TextBox widget"""
        return self.text + self.coin
