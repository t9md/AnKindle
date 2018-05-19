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
    "GET KINDLE CLIPPINGS": {'zh_CN': u'请手动选择 My Clippings.txt，。', 'en': u'Please select Kindle clippings file.'},
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
    "WIN UPDATE": {'zh_CN': u'请按照以下步骤更新AnKindle：\n\n1. 菜单 - 工具 - 打开插件文件夹。\n'
                            u'2. 退出Anki。\n'
                            u'3. 删掉AnKindle文件夹和anKindle.py。\n'
                            u'4. 用代码重装AnKindle。',
                   'en': u'Please follow below steps to upgrade AnKindle：\n\n1. Menu - Tools - Open Add-on Folder.\n'
                         u'2. Exit Anki.\n'
                         u'3. delete "AnKindle" folder and "anKindle.py" file.\n'
                         u'4. Re-Install AnKindle via the code.'},
    # region Clippings
    "SHOW VOCAB IMPORT": {'zh_CN': u'生词导入', 'en': u'Import Vocab'},
    "MY CLIPPINGS NOT AVAILABLE": {'zh_CN': u'无法读取‘My Clippings.txt’。', 'en': u'“My Clippings.txt” unavailable.'},
    "SHOW CLIPPING IMPORT": {'zh_CN': u'标注导入', 'en': u'Import Clippings'},
    "SELECT MY CLIPPINGS TXT": {'zh_CN': u'Kindle没有接入电脑或者无法定位文件\n\n请手动选择 “My Clippings.txt”。',
                                'en': u'Kindle is not adapted to machine or file cannot be found\n\nPlease select "My Clippings.txt".'},
    "INCOMPLETE CLIPPINGS": {'zh_CN': u'待导入', 'en': u'In Queue'},
    "COMPLETED CLIPPINGS": {'zh_CN': u'已完成', 'en': u'Completed'},
    "CLIPPING": {'zh_CN': u'标注', 'en': u'Clipping'},
    "REMARK": {'zh_CN': u'笔记', 'en': u'Remark'},
    "BOOK": {'zh_CN': u'书名', 'en': u'Book'},
    "AUTHOR": {'zh_CN': u'作者', 'en': u'Author'},
    "MARK AS": {'zh_CN': u'标记为', 'en': u'Mark as'},
    "AUTO FILL": {'zh_CN': u'自动填充', 'en': u'Auto Fill'},
    "ADD QUICK SET MENU": {'zh_CN': u'添加快捷菜单', 'en': u'Add Quick Menu'},
    "QUICK MENU NAME": {'zh_CN': u'快捷菜单名', 'en': u'Quick Menu Name'},
    "INVALID QUICK MENU SETTING": {'zh_CN': u'菜单名不为空<br>',
                                   'en': u'Menu must have value'},

    # endregion

    # region Config
    "CONFIGURATION": {'zh_CN': u'设置', 'en': "Configuration"},
    "QUICK FILL TAGS": {'zh_CN': u'快捷填充标签', 'en': "Quick Filling Tags"},
    "UPGRADE TO PLUS": {'zh_CN': u"解锁高级功能", 'en': "Ankindle Plus"},
    "REGISTER PLUS": {'zh_CN': u"输入解锁密码", 'en': "Enter SN"},

    # endregion
    # upgrade notice
    "UPGRADE SUGGESTION": {'zh_CN': u"""
    <p>AnKindle Plus：</p>
    <p>- 为您的所有Kindle标注制作Anki读书卡片！（点击菜单中“标注导入”进行试用）</p><br>
    <p>是否前往商店购买解锁密码？（即将访问淘宝页面）</p><br>
    """, 'en': """
    <p><b>AnKindle Plus：<b></p>
    <p>Create Anki cards for all your Kindle clippings!</p>
    <p>Purchase an SN for unlocking features?</p><br>
    """},

    "UPGRADE SUGGESTION MORE CLIPPINGS": {'zh_CN': u"""
    <p>基础版只支持10条标注的制作，是否升级为 AnKindle Plus 解锁？</p><br>
    """, 'en': """
    <p>Basic edition support only 10 clippings, upgrade to AnKindle Plus?</p>
    """}
}


def _trans(key):
    return getTrans(key, trans)
