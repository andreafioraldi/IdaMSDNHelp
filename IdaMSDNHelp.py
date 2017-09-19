__author__ = "Andrea Fioraldi"
__copyright__ = "Copyright 2017, Andrea Fioraldi"
__license__ = "MIT"
__email__ = "andreafioraldi@gmail.com"

import idaapi
import webbrowser

MENU_PATH = 'Edit/Other'
class IdaMSDNHelpPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_KEEP
    comment = ""

    help = "IdaMSDNHelp: MSDN Help for IDA Pro"
    wanted_name = "IDA MSDN Help"
    wanted_hotkey = "Alt-R"

    def init(self):
        r = idaapi.add_menu_item(MENU_PATH, 'Open MSDN Search', '', 1, self.openHelp, tuple())
        if r is None:
            idaapi.msg("IdaMSDNHelp: add menu failed!\n")
        idaapi.msg("IdaMSDNHelp: initialized, opening webbrowser with '%s' command\n" % webbrowser.get().name)
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        self.query()

    def term(self):
        idaapi.msg("IdaMSDNHelp: terminated\n")

    def openHelp(self):
        webbrowser.open("https://social.msdn.microsoft.com/search/en-US")

    def query(self):
        func = idaapi.get_highlighted_identifier()
        url = "https://social.msdn.microsoft.com/search/en-US?query=" + func
        webbrowser.open(url)

def PLUGIN_ENTRY():
    return IdaMSDNHelpPlugin()

