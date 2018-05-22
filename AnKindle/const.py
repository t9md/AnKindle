# -*- coding: utf-8 -*-
# Created: 3/27/2018
# Project : AnKindle
import os

from .libs import six

__version__ = "0.6.21"
HAS_SET_UP = False
ADDON_CD = 1016931132
DEBUG = False
ONLINE_DOC_URL = "https://github.com/upday7/AnKindle/blob/master/docs/DOC.md"
DEFAULT_TEMPLATE = six.ensure_str(os.path.join(os.path.dirname(__file__), u"resource", u"AnKindle.apkg"))
CLIPPINGS_DEFAULT_TEMPLATE_NAME = u"AnKindleClipping-Default"
CLIPPINGS_DEFUALT_TEMPLATE = six.ensure_str(os.path.join(os.path.dirname(__file__), u"resource",
                                                         CLIPPINGS_DEFAULT_TEMPLATE_NAME + ".apkg"))
CLIPPING_DEFAULT_MODULE_NAMES = ["AnKindleClipping-Basic", "AnKindleClipping-Cloze"]
SQL_SELECT_WORDS = """
SELECT
  ws.id,
  ws.word,
  ws.stem,
  ws.lang,
  datetime(ws.timestamp * 0.001, 'unixepoch', 'localtime') added_tm,
  lus.usage,
  bi.title,
  bi.authors
FROM words AS ws LEFT JOIN lookups AS lus ON ws.id = lus.word_key
  LEFT JOIN book_info AS bi ON lus.book_key = bi.id
"""

MUST_IMPLEMENT_FIELDS = (
    "STEM", "WORD", "LANG", "CREATION_TM", "USAGE", "TITLE", "AUTHORS", "ID"
)
