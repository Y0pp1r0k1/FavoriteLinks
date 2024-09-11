import customtkinter as CTK

def customWindow() :

    customWindow = CTK.CTkToplevel()
    customWindow.title("リンクのカスタム")
    customWindow.geometry("1280x720")
    customWindow.geometry("+250+200")
    customWindow.focus_force()
    customWindow.attributes("-topmost", True)