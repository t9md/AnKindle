# -*- coding:utf-8 -*-

from .kkLib import getTrans

_style = u"""
<style>

* {
    font-family: 'Microsoft YaHei UI', Consolas, serif;
}

</style>

"""

trans = {
    'ANKINDLE': {'zh_CN': u'AnKindle', 'en': u'AnKindle'},
    'NOTE TYPE': {'zh_CN': u'保存为笔记类型', 'en': u'Note Type'},
    'DECK TYPE': {'zh_CN': u'保存到记忆库', 'en': u'Deck Name'},
    'MDX TYPE': {'zh_CN': u'查询MDX字典', 'en': u'MDX Dict'},
    'SELECT MODEL': {'zh_CN': u'保存为笔记类型', 'en': u'Choose Note Type'},
    'SELECT DECK': {'zh_CN': u'保存到记忆库', 'en': u'Choose Deck'},
    'SELECT MDX': {'zh_CN': u'（可选） 选择MDX字典', 'en': u'(Optional) MDX Dict'},
    'CREATED AND DUPLICATES': {'zh_CN': u'新建：%s 张卡片。\n重复：%s 张卡片。',
                               'en': u'Created: %s cards.\nDuplicates: %s cards.'},
    'NONE': {'zh_CN': u'无', 'en': u'None'},
    'CANNOT FIND KINDLE VOLUME': {'zh_CN': u'** 无法找到 Kindle 数据库 **', 'en': u'** Missing Kindle DB **'},
    'USING DB': {'zh_CN': u'读取%s', 'en': u'Reading %s'},
    'HELP': {'zh_CN': u'帮助', 'en': u'Help'},
    'IMPORT': {'zh_CN': u'导入设置', 'en': u'Import Config'},
    'SELECT KINDLE DB': {'zh_CN': u'重新选择Kindle数据库文件', 'en': u'Re-select Kindle database file'},
    'ONLY NEW WORDS': {'zh_CN': u'仅新词', 'en': u'New Word'},
    'ONE CLICK IMPORT': {'zh_CN': u'一键导入', 'en': u'One-Click-Import'},
    'GET KINDLE DB': {'zh_CN': u'请手动选择Kindle数据库，。', 'en': u'Please select Kindle vocab database.'},
    'IMPORTING': {'zh_CN': u'正在导入生词', 'en': u'Importing'},
    # 'SELECT ORIG LANG': {'zh_CN': u'选择生词语言类型:', 'en': u'Language of words:'},
    'MANDATORY': {'zh_CN': u'<b>必选：</b>', 'en': u'<b>Mandatory:</b>'},
    'ALERT FOR MISSING MDX': {'zh_CN': u'您没有选择MDX文件，单词释义信息将不会被导入，确认继续吗？',
                              'en': u'None of MDX dictionaries are selected, '
                                    u'explanations will be lost in your imports. Confirm to continue?'},
    'OPTIONAL': {'zh_CN': u'<b>可选：</b>', 'en': u'<b>Optional:</b>'},
    'USE LATEST TEMPLATE': {'zh_CN': u'默认配套模板', 'en': u'Default Card Template'},
    'LANGUAGE': {'zh_CN': u'生词语言类型:', 'en': u'Language: '},
    'MORE_DOC': {'zh_CN': u'更多模板与教程', 'en': u'More Templates & Documentation'},
    'MATURE': {'zh_CN': u'已掌握', 'en': u'Mature'},
    'NEW WORDS': {'zh_CN': u'新词', 'en': u'New'},
    'MDX MEMORY ERROR': {'zh_CN': u'无法读取MDX词典内容，请更换词典文件。',
                         'en': u'Memory error when loading MDX, please switch ' u'another MDX file.'},
    'REFRESH': {'zh_CN': u'刷新', 'en': u'Refresh'},
    'MARK MATURE': {'zh_CN': u'标记为已掌握', 'en': u'Mark Mature'},
    'MARK NEW': {'zh_CN': u'标记为新词', 'en': u'Mark New'},

    'MDX TYPE ERROR': {'zh_CN': u'无法读取MDX词典内容，请更换词典文件。', 'en': u'Type error when loading MDX, please switch '
                                                               u'another MDX file.'},
    "ENSURE USB": {'zh_CN': u'请确保Kindle已经接入电脑。',
                   'en': u'Please ensure Kindle has been adapted to your machine.'},
    "USER DEFINED TEMPLATE ALERT": {'zh_CN': u"""
    <p>您当前没有使用任何AnKindle的模板，<b>插件将自动使用默认模板</b>。</p>
    <p>关于如何制作和使用自定义用于的AnKindle的模板，请参考【帮助】文档或者【知乎】搜索AnKindle。</p>
    """, 'en': u"""
    <p>There's no available AnKindle models，<b>add-on will use default template for importing</b>。</p>
    <p>Please refer to [Help] docs for customizing template for your Kindle vocab.</p>
    """},
    "ANKINDLE WORDS PREVIEW": {'zh_CN': u'生词预览',
                               'en': u'Words Preview'},

    # region preview window
    'WORD': {'zh_CN': u'单词', 'en': u'Word'},
    'STEM': {'zh_CN': u'原型', 'en': u'Stem'},
    'ADDED_TM': {'zh_CN': u'添加日期', 'en': u'Created'},
    'USAGE': {'zh_CN': u'原句', 'en': u'Usage'},
    'TITLE': {'zh_CN': u'书籍', 'en': u'Title'},
    'AUTHORS': {'zh_CN': u'作者', 'en': u'Author(s)'},

    # endregion
}


def _trans(key):
    return getTrans(key, trans)
