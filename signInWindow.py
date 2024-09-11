import tkinter as tk
import customtkinter as CTK
from pathlib import Path

import csv 
import CustomLinkDefs as CLD


def signIn() :
    #ログインウィンドウの設定
    signInWindow = CTK.CTkToplevel()
    signInWindow.title("ログイン")
    signInWindow.geometry("400x500")
    signInWindow.geometry("+690+330")
    signInWindow.focus_force()
    signInWindow.attributes("-topmost", True)

    
    #ウィンドウの編集
    noneSpace = CTK.CTkLabel(signInWindow, text="")
    noneSpace.grid(column=0, row=0)

    #ユーザーネームの入力場所
    UserNameTitle = CTK.CTkLabel(signInWindow, text="UserName", font=("游ゴシック", 15))
    UserNameTitle.grid(column=1, row=1)

    UserNameText = CTK.CTkEntry(signInWindow, width=180, border_width=0)
    UserNameText.grid(column=2, row=2, sticky=tk.W, pady=20)

    #パスワードの入力場所
    passwordTitle = CTK.CTkLabel(signInWindow, text="Password", width=120, font=("游ゴシック", 15))
    passwordTitle.grid(column=1, row=3)

    passwordText = CTK.CTkEntry(signInWindow, width=180, border_width=0, show="●", font=("游ゴシック", 13))
    passwordText.grid(column=2, row=4, sticky=tk.W, pady=20)

    #パスワードの表示切替ボタン
    passwordShowButton = CTK.CTkButton(signInWindow, text="Show", width=50)
    passwordShowButton.grid(column=3, row=4)
    #passwordの表示関数をここに指定する

    #キャンセルボタン
    cancelButton = CTK.CTkButton(signInWindow, text="Cancel", width=10)
    cancelButton.bind("<Button-1>", lambda e:close())
    cancelButton.grid(column=2, row=5, sticky=tk.E)

    #ログインボタン
    signInButton = CTK.CTkButton(signInWindow, text="Sign In", width=10)
    signInButton.bind("<Button-1>", lambda e:userNameGet())
    signInButton.bind("<Button-1>", lambda e:passwordGet(), "+")
    signInButton.bind("<Button-1>", lambda e:csvOpen(), "+")
    signInButton.bind("<Button-1>", lambda e:close(), "+")
    signInButton.grid(column=3, row=5, padx=20, pady=20)
    

    def passwordGet() :
        PasswordGet = passwordText.get()
        print(PasswordGet)

    def userNameGet() :
        UserNameGet = UserNameText.get()
        print(UserNameGet)

    def close() :
        signInWindow.destroy()

    def csvOpen() : 
        with open ("data/data.csv") as f:
        
            reader = csv.reader(f)
            for line in reader :
                print(line)

