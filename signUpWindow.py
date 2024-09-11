import customtkinter as CTK
import tkinter as tk
import sentMail

def signUp() :
    #登録ウィンドウの設定
    signUpWindow = CTK.CTkToplevel()
    signUpWindow.geometry("400x500")
    signUpWindow.geometry("+690+330")
    signUpWindow.title("新規登録")
    signUpWindow.lift()
    signUpWindow.focus_force()
    signUpWindow.attributes("-topmost", True)

    #Space作成
    noneSpace = CTK.CTkLabel(signUpWindow, text="")
    noneSpace.grid(column=0, row=0, padx=20)

    #メールアドレスの入力場所
    MailAddressTitle = CTK.CTkLabel(signUpWindow, text="MailAddress", font=("游ゴシック", 15))
    MailAddressTitle.grid(column=1, row=1)

    MailAddressText = CTK.CTkEntry(signUpWindow, width=180, border_width=0)
    MailAddressText.grid(column=2, row=2, sticky=tk.W, pady=20)

    #キャンセルボタン
    cancelButton = CTK.CTkButton(signUpWindow, text="Cancel", width=10)
    cancelButton.bind("<Button-1>", lambda e:close())
    cancelButton.grid(column=2, row=5, sticky=tk.E)

    #Nextボタン
    NextButton = CTK.CTkButton(signUpWindow, text="Next", width=10)
    NextButton.bind("<Button-1>", lambda e:MailAddressGet())
    NextButton.bind("<Button-1>", lambda e:sentMail.sentMail(), "+")
    NextButton.bind("<Button-1>", lambda e:close(), "+")
    NextButton.grid(column=3, row=5, padx=20, pady=20)

    def close() :
        signUpWindow.destroy()

    def MailAddressGet() :
        MailAddressGet = MailAddressText.get()
        print(MailAddressGet)