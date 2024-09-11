import customtkinter as CTK
import CTkDefs as defs

from settings.AutoStart   import autoStart
from settings.buttonColor import bColor
from settings.windowColor import wColor 
from settings.fontSize    import fSize
from settings.information import info


def settingWindow() :

    settingWindow = CTK.CTkToplevel() 
    settingWindow.geometry("720x480")
    settingWindow.geometry("+640+280")
    settingWindow.title("設定")
    settingWindow.focus_force()
    settingWindow.attributes("-topmost", True)


    defs.buttonDef("setWindowColor", settingWindow, "Change the window color", 0, 0, 20, 5, wColor())

    defs.buttonDef("setButtonColor", settingWindow, "Change the button color", 1, 0, 20, 5, bColor())

    defs.buttonDef("setFontSize", settingWindow, "Change the font size", 2, 0, 20, 5, fSize())

    defs.buttonDef("autoStart", settingWindow, "Witch the how to start", 3, 0, 20, 5, autoStart())

    defs.buttonDef("showInformation", settingWindow, "Show the app information", 4, 0, 20, 5, info())