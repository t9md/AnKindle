# -*- coding: utf-8 -*-
# Created: 3/27/2018
# Project : AnKindle

import os

from anki.db import DB
from anki.utils import isWin
from aqt import mw
# noinspection SqlResolve
from aqt.utils import getFile
from .config import Config
from .const import DEBUG
from .lang import _trans


class KindleDB(DB):
    def __init__(self, fpath=None, force_select=False):
        """

        :param fpath: db or txt
        :param force_select:
        """
        self._fpath = fpath

        if force_select:
            self.db = self.search_db(force_select)
        else:
            if fpath and os.path.isfile(fpath):
                self.db = fpath
            else:
                self.db = self.search_db()

        if self.is_format_db:
            Config.last_used_db_path = self.db
            super(KindleDB, self).__init__(self.db)
        else:
            Config.last_used_clips_path = self.db

    @property
    def is_format_db(self):
        return self._fpath.upper().endswith(".DB")

    @property
    def is_available(self):
        try:
            return os.path.isfile(self.db)
        except TypeError:
            return False

    def create_clippings_db(self):
        pass

    def search_db(self, force_select_db=False):
        if isWin:
            allDisks = ['A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:',
                        'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:',
                        'R:', 'S:',
                        'T:',
                        'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']

        else:
            allDisks = [os.path.join(os.path.sep, "Dev/Kindle"),
                        os.path.join(os.path.sep, "Volumes/Kindle"),
                        os.path.join(os.path.sep, "mnt/Kindle")]
        if DEBUG or force_select_db:
            allDisks = []
        for disk in allDisks:
            if self.is_format_db:
                kindle_db = os.path.join(disk + os.path.sep + "system" + os.path.sep
                                         + "vocabulary" + os.path.sep + "vocab.db")
            else:
                kindle_db = os.path.join(disk + os.path.sep + "documents" + os.path.sep
                                         + "My Clippings.txt")

            if os.path.isfile(kindle_db):
                return kindle_db
        if force_select_db:
            if self.is_format_db:
                kindle_db = getFile(mw, _trans("GET KINDLE DB"),
                                    lambda x: x, ("Kindle Vocab Db(*.db)"),
                                    os.path.dirname(
                                        Config.last_used_db_path if
                                        os.path.isdir(os.path.dirname(Config.last_used_db_path)) else __file__
                                    )
                                    )
            else:
                kindle_db = getFile(mw, _trans("GET KINDLE CLIPPINGS"),
                                    lambda x: x, ("Kindle Clippings (*.txt)"),
                                    os.path.dirname(
                                        Config.last_used_db_path if
                                        os.path.isdir(os.path.dirname(Config.last_used_clips_path))
                                        else __file__
                                    )
                                    )
            return kindle_db

    def get_vocab(self, only_new):
        """

        :return: list of [id,word, ste, lang, added_tm,usage,title,authors]
        """
        return self.execute(
            """
            SELECT
              ws.id,
              ws.word,
              ws.stem,
              ifnull(dict.langin,ws.lang) as lang,
              datetime(ws.timestamp * 0.001, 'unixepoch', 'localtime') added_tm,
              lus.usage,
              bi.title,
              bi.authors,
              ws.CATEGORY
            FROM words AS ws
              LEFT JOIN lookups AS lus ON ws.id = lus.word_key
              left join DICT_INFO as dict on lus.dict_key = dict.id
              LEFT JOIN book_info AS bi ON lus.book_key = bi.id
            
            {}
            
            """.format("WHERE ws.CATEGORY = 0" if only_new else "")
        )

    def update_word_mature(self, word_id, category):
        self.execute(
            """
            update words set category = ? where id = ?

            """, category, word_id
        )
        self.commit()
