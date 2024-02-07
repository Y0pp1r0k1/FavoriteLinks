import tkinter as tk
import sys 
import os
import defs

#ウィンドウの設定
root = tk.Tk()
root.title("お気に入りのリンク集")
root.geometry("1280x720")

#アイコンの設定
def temp_path(relative_path):
    try:
        #Retrieve Temp Path
        base_path = sys._MEIPASS
    except Exception:
        #Retrieve Current Path Then Error 
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

logo=temp_path('./myicon.ico')
root.iconbitmap(default=logo)

#アプリを起動したUserのIDを取得する処理
UserName = os.getlogin()

def main():
    
    #タイトルの追加 SNS
    defs.TitleContent(root, "SNS", "SNS", 20, 20)

    #X
    defs.LinkContent(root, "X", "X(旧Twitter)", 30, 45, "https://twitter.com")

    #Hoyolab
    defs.LinkContent(root, "HoyoLab", "HoyoLab", 30, 65, "https://www.hoyolab.com")

    #TikTok
    defs.LinkContent(root, "TikTok", "TikTok", 30, 85, "https://www.tiktok.com")


    
    #コミュニケーションサービス
    defs.TitleContent(root, "communicationService", "コミュニケーションサービス", 20, 110)

    #Discord　Web
    defs.LinkContent(root, "DiscordWeb", "Discord(Web版)", 30, 135, "https://discord.com/channels/@me")

    #Discord app
    defs.AppContent(root, "DiscordApp", "Discord(App版)", 30, 155, rf"C:\Users\{UserName}\AppData\Local\Discord\Update.exe --processStart Discord.exe")

    #LINE web
    defs.AppContent(root, "LINEWeb", "LINE(Web版)", 30, 175, rf"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #LINE app
    defs.AppContent(root, "LINEApp", "LINE(App版)", 30, 195, rf"C:\Users\{UserName}\AppData\Local\LINE\bin\LineLauncher.exe")

    #Slack Web
    defs.LinkContent(root, "SlackWeb", "Slack(Web版)", 30, 215, "https://app.slack.com/client")

    #Slack app
    defs.AppContent(root, "SlackApp", "Slack(App版)", 30, 235, rf"C:\Users\{UserName}\AppData\Local\slack\slack.exe")



    #プログラミング系
    defs.TitleContent(root, "programming", "プログラミング", 20, 260)

    #GitHub
    defs.LinkContent(root, "GitHub", "GitHub", 30, 285, "https://github.com")

    #Progate
    defs.LinkContent(root, "Progate", "Progate", 30, 305, "https://prog-8.com/")

    #Python-izm
    defs.LinkContent(root, "Python-izm", "Python-izm", 30, 325, "https://www.python-izm.com")

    #Qiita
    defs.LinkContent(root, "Qiita", "Qiita", 30, 345, "https://qiita.com")



    #動画配信サービス
    defs.TitleContent(root, "VideoService", "動画配信サービス", 20, 370)

    #Youtube 
    defs.LinkContent(root, "Youtube", "Youtube", 30, 395, "https://www.youtube.com")

    #Twitch
    defs.LinkContent(root, "Twitch", "Twitch", 30, 415, "https://www.twitch.tv")

    #TVer 
    defs.LinkContent(root, "TVer", "TVer", 30, 435, "https://tver.jp")



    #ブラウザ
    defs.TitleContent(root, "browser", "ブラウザ", 20, 460)

    #Chrome
    defs.AppContent(root, "Chrome", "Chrome", 30, 480, rf"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #Edge
    defs.AppContent(root, "Edge", "Edge", 30, 500, rf"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")


#main関数の呼び出し
main()

#ウィンドウの実行
root.mainloop()
root.quit()
