# -*- coding: utf-8 -*-
# Created: 3/27/2018
# Project : AnKindle
import os

from PyQt5.QtGui import QIcon
from aqt import QAction, QMenu
from aqt import mw
from aqt.importing import importFile

from .const import MUST_IMPLEMENT_FIELDS, DEFAULT_TEMPLATE
from .gui import Window
from .lang import _trans


def _try_ext_module():
    try:
        from . import AnKindlePro
        if not AnKindlePro:
            return False
        return True
    except ImportError:
        try:
            import AnKindlePro
            if not AnKindlePro:
                return False
        except:
            pass
    return False


try:
    from . import AnKindlePro
except ImportError:
    try:
        import AnKindlePro
    except:
        pass


class ActionShow(QAction):
    def __init__(self, parent):
        super(ActionShow, self).__init__(parent)
        self.setText(_trans("AnKindle"))


class AnKindleAddon:

    def __init__(self):
        self.on_start()
        # variables
        self.main_menu = None
        self.action_show_vocab_dialog = None
        self.action_show_clipping_dialog = None
        # self.main_menu_action = None

        if not self.avl_col_model_names:
            importFile(mw, DEFAULT_TEMPLATE)

    def perform_hooks(self, func):
        # func('reviewCleanup', self.on_review_cleanup)
        func('profileLoaded', self.on_profile_loaded)
        # func('afterStateChange', self.after_anki_state_change)

    def on_profile_loaded(self):
        self.init_menu()

    def on_start(self):
        if self.ext_available:
            AnKindlePro.start_ankindle_pro()

    def init_menu(self):
        # init actions

        if not self.main_menu:
            self.main_menu = QMenu(_trans("AnKindle"), mw.form.menuTools, )
            mw.form.menuTools.addMenu(self.main_menu)

            self.action_show_vocab_dialog = QAction(_trans("SHOW VOCAB IMPORT"), self.main_menu)
            self.action_show_vocab_dialog.triggered.connect(self.on_show_vocab_dialog)
            self.main_menu.addAction(self.action_show_vocab_dialog)

            self.action_show_clipping_dialog = QAction(_trans("SHOW CLIPPING IMPORT"), self.main_menu)
            self.action_show_clipping_dialog.triggered.connect(self.on_show_clipping_dialog)
            self.main_menu.addAction(self.action_show_clipping_dialog)

            # self.action_show_clipping_dialog.setEnabled(self.ext_unlocked)
            if not self.ext_unlocked:
                self.action_show_clipping_dialog.setIcon(QIcon(
                    os.path.join(os.path.dirname(__file__), "resource", "lock.png")
                ))

    @property
    def ext_available(self):
        return _try_ext_module()

    @property
    def ext_unlocked(self):
        if self.ext_available:
            return AnKindlePro.Verification.Unlocked()
        return False

    def on_show_clipping_dialog(self):
        pass  # todo add lock

    def on_show_vocab_dialog(self):
        self.vocab_dlg = Window(mw, self.avl_col_model_names, self.avl_decks, )
        self.vocab_dlg.exec_()

    def avl_col_model_names(self):
        _ = []
        for mid, m_values in self.collection.models.models.items():
            if not set([f.lower() for f in MUST_IMPLEMENT_FIELDS]).difference(
                    set([f[u'name'] for f in m_values[u'flds']])):
                _.append(mid)
        return [v for k, v in self.collection.models.models.items() if k in _]

    def avl_decks(self):
        _ = []
        for did, d_values in self.collection.decks.decks.items():
            _.append(did)
        return [v for k, v in self.collection.decks.decks.items() if k in _]

    @property
    def collection(self):
        """

        :rtype: _Collection
        """

        return mw.col


# region Main Entry
from anki.hooks import addHook


def start():
    if const.HAS_SET_UP:
        return
    rr = AnKindleAddon()
    rr.perform_hooks(addHook)
    const.HAS_SET_UP = True


addHook("profileLoaded", start)
# endregion
