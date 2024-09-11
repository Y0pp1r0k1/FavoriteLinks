import customtkinter as CTK
import random


#ウィンドウの作成
def sentMail() :
    sentMailWindow = CTK.CTkToplevel()
    sentMailWindow.geometry("400x500")
    sentMailWindow.geometry("+690+330")
    sentMailWindow.title("Sent Mail")
    sentMailWindow.lift()
    sentMailWindow.focus_force()
    sentMailWindow.attributes("-topmost", True)



    #メールに送るランダムな6桁の数字の制作
    randomNumbers = [random.randint(0, 9) for i in range(6)]
    randomNumbersList = "".join(map(str,randomNumbers))
    print(randomNumbersList)

    #スペースづくり
    noneSpace = CTK.CTkLabel(sentMailWindow, text="")
    noneSpace.grid(column=0, row=0)

    #パスワードを入れる場所のタイトルとテキスト
    sentMailTitle = CTK.CTkLabel(sentMailWindow, text="Entry to set password", font=("游ゴシック", 15))
    sentMailTitle.grid(column=1, row=1, padx=30, pady=20, sticky=CTK.W)

    setPassword = CTK.CTkEntry(sentMailWindow, font=("游ゴシック", 13), border_width=0)
    setPassword.grid(column=1, row=2, padx=60)

    #送られたきたコードを入力する場所の制作
    enterTheCodeLabel = CTK.CTkLabel(sentMailWindow, text="Enter the 4 digit code. code is in your mailbox", font=("游ゴシック", 13))
    enterTheCodeLabel.grid(column=1, row=3, padx=30, pady=30, sticky=CTK.W)

    entryTheCode = CTK.CTkEntry(sentMailWindow, font=("游ゴシック", 13), border_width=0)
    entryTheCode.grid(column=1, row=4, padx=60, sticky=CTK.N)


#Test only
#sentMail()