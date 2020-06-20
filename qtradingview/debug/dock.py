import logging
import coloredlogs

from pathlib import Path
import os
from PyQt5 import QtWidgets, uic
# from ui.dock_debug_Ui import Ui_DockDebug

Ui_DockDebug, QtBaseClass = uic.loadUiType("qtradingview/ui/dock_debug.ui")


class DockDebug(QtWidgets.QDockWidget, Ui_DockDebug):

    def __init__(self, parent):
        QtWidgets.QDockWidget.__init__(self, parent)
        Ui_DockDebug.__init__(self)
        self.setupUi(self)
        #
        self.mw = parent
        #
        self.setVisible(self.mw.actionDebug.isChecked())


# ─── QLOGGER CLASS ──────────────────────────────────────────────────────────────

class Qlogger(logging.Handler):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        log_mode = logging.INFO
        if self.parent.ctx.debug:
            log_mode = logging.DEBUG
        coloredlogs.install(level=log_mode)
        self.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    def emit(self, record):
        msg = self.format(record)
        self.parent.dock_debug.edit_logger.append(msg)

# ────────────────────────────────────────────────────────────────────────────────