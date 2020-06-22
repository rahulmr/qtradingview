"""
QTradingView

Usage:
  qtradingview [--debug]
  qtradingview -h | --help
  qtradingview -v | --version


Options:
  -h --help     Show this screen.
  -v --version  Show version.
  --debug       Execute in debug mode.
"""

__version__ = '0.11.0'

import os
import sys
import docopt

from app.context import ContextoApp


# ─── MAIN ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = docopt.docopt(__doc__, version=__version__)
    appctx = ContextoApp(args)
    appctx.app.installTranslator(appctx.app_language)
    appctx.app.installTranslator(appctx.system_language)
    exit_code = appctx.run()
    sys.exit(exit_code)
