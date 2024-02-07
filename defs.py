import tkinter as tk
import webbrowser
import subprocess


#タイトルの追加を簡単に記述するための関数
def TitleContent(root, title, text, x, y) :

    title = tk.Label(root, text=text, font=("游ゴシック", 11))
    title.place(x=x, y=y)


#リンク(Web版など)を簡単に記述するために作った関数
def LinkContent(root, title, text, x, y, url) : 

    title = tk.Label(root, text="・" + text, fg="blue", font=("游ゴシック", 10))
    title.place(x=x, y=y)
    title.bind("<Button-1>", lambda e:link_click(url))


#アプリ(App版など)を簡単に記述するために作った関数
def AppContent( root, title, text, x, y, exeUrl) :

    title = tk.Label(root, text="・" + text, fg="blue", font=("游ゴシック", 10))
    title.place(x=x, y=y)
    title.bind("<Button-1>", lambda e:app_click(exeUrl))


#リンクがクリックされた時に実行される処理
def link_click(url) :
    webbrowser.open_new(url)


#App版のリンクをクリックしたときに実行される処理
def app_click(exeUrl) :
    subprocess.Popen(exeUrl)

    