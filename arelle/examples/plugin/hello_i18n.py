# -*- coding: utf-8 -*-
from arelle import PluginManager
from random import randint
import sys
'''
Hello dolly is a simple "Hello world" to demonstrate how plugins
are written for Arelle
'''

LYRICS =  ["I said hello, dolly,......well, hello, dolly", \
            "It's so nice to have you back where you belong ", \
            "You're lookin' swell, dolly.......i can tell, dolly ", \
            "You're still glowin'...you're still crowin'...you're still goin' strong ", \
            "I feel that room swayin'......while the band's playin' ", \
            "One of your old favourite songs from way back when ", \
            "So..... take her wrap, fellas.......find her an empty lap, fellas ", \
            "Dolly'll never go away again" 
            ]

def randomLyric():
    ''' A random lyrics.'''
    return LYRICS[randint(0, len(LYRICS))]
        
def menuEntender(cntlr, menu):
    menu.add_cascade(label="Hello i18n", underline=0, command=lambda: menuCommand(cntlr) )

def menuCommand(cntlr):
    i10L_world = _("Hello World");
    cntlr.addToLog(i10L_world)
    import tkinter
    tkinter.messagebox.showinfo(_("Prints 'Hello World'"), i10L_world, parent=cntlr.parent)            

'''
   Do not use _( ) in pluginInfo itself (it is applied later, after loading
'''
__pluginInfo__ = {
    'name': 'Hello i18n',
    'version': '0.9',
    'description': '''Minimal plugin that demonstrates i18n internationalization by localized gettext.''',
    'localeURL': "locale",
    'localeDomain': 'hello_i18n',
    'license': 'Apache-2',
    'author': 'R\u00e9gis D\u00e9camps',
    'copyright': '(c) Copyright 2012 Mark V Systems Limited, All rights reserved.',
    # classes of mount points (required)
    'CntlrWinMain.Menu.Tools': menuEntender
}