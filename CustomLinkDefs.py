import customtkinter as ctk
import webbrowser
import subprocess
import os
import sys

#main.py用
#タイトルの追加を簡単に記述するための関数
def TitleContent(root, title, text, x, y) :

    title = ctk.CTkLabel(root, text=text, font=("游ゴシック", 15))
    title.place(x=x, y=y)


#リンク(Web版など)を簡単に記述するための関数 place版
def linkContent1(root, name, text, x, y, url) : 

    name = ctk.CTkLabel(root, text=text, font=("游ゴシック", 13), text_color="blue")
    name.place(x=x, y=y)
    name.bind("<Button-1>", lambda e:link_click(url))

def linkContent2(name, root, text, row, column, padx, pady, url) : 

    name = ctk.CTkLabel(root, text=text, font=("游ゴシック", 13), text_color="blue")
    name.grid(row=row, column=column, padx=padx, pady=pady)
    name.bind("<Button-1>", lambda e:link_click(url))


#アプリ(App版など)を簡単に記述するための関数
def AppContent(root, title, text, x, y, exeUrl) :

    title = ctk.CTkLabel(root, text=text, font=("游ゴシック", 13), text_color="blue")
    title.place(x=x, y=y)
    title.bind("<Button-1>", lambda e:app_click(exeUrl))


#リンクがクリックされた時に実行される処理
def link_click(url) :
    webbrowser.open_new(url)


#App版のリンクをクリックしたときに実行される処理
def app_click(exeUrl) :
    subprocess.Popen(exeUrl)


#アイコンの指定用関数
def temp_path(relative_path):

    try:
        #アプリのパスの取得
        base_path = sys._MEIPASS
    except Exception:
        #アプリのパスに "." を追加
        base_path = os.path.abspath(".")

        #アプリのパス、 ".", "relative_path"(アイコンの画像) を結合
    return os.path.join(base_path, relative_path)


    """"

        ファイルのアイコンを指定するなら必ずこれを記述する

            import CustomLinkDefs as CLD


            logo=CLD.temp_path("./data/icon.ico")
            (ウィンドウの名前).iconbitmap(default=logo)

    """