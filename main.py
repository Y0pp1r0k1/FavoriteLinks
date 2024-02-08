import tkinter as tk
import sys 
import os
import defs

#ウィンドウの設定
root = tk.Tk()
root.title("Favorite Links and App")
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

    #WebColorCode
    defs.LinkContent(root, "WebColorCode", "Web色見本", 30, 365, "https://www.colordic.org/")



    #動画配信サービス
    defs.TitleContent(root, "VideoService", "動画配信サービス", 20, 390)

    #Youtube 
    defs.LinkContent(root, "Youtube", "Youtube", 30, 415, "https://www.youtube.com")

    #Twitch
    defs.LinkContent(root, "Twitch", "Twitch", 30, 435, "https://www.twitch.tv")

    #TVer 
    defs.LinkContent(root, "TVer", "TVer", 30, 455, "https://tver.jp")



    #ブラウザ
    defs.TitleContent(root, "browser", "ブラウザ", 20, 480)

    #Chrome
    defs.AppContent(root, "Chrome", "Chrome", 30, 505, rf"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #Edge
    defs.AppContent(root, "Edge", "Edge", 30, 525, rf"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

    

    #便利系サイト
    defs.TitleContent(root, "convenientSite", "便利系サイト", 300, 20)

    #unlimited:waifu2x
    defs.LinkContent(root, "unlimited:waifu2x", "unlimited:waifu2x", 310, 45, "https://unlimited.waifu2x.net/#google_vignette")

    #URL Shortener
    defs.LinkContent(root, "URLShortener", "URL Shorttener", 310, 65, "https://tinyurl.com/app")



    #ゲーム　Site
    defs.TitleContent(root, "gamesSite", "ゲームリンク（手助け的な）", 300, 90)

    #GenshinBuildCard
    defs.LinkContent(root, "GenshinBuildCard", "GenshinBuildCard", 310, 115, "https://artifacter.neody.land/ja-JP/genshin/generate?uid=855760492")

    #HSRBuildCard
    defs.LinkContent(root, "HSRBuildCard", "HSRBuildCard", 310, 135, "https://artifacter.neody.land/ja-JP/hsr/generate?uid=800099957")



    #ゲーム　App
    defs.TitleContent(root, "gamesApp", "ゲーム（アプリ）", 300, 165)


#main関数の呼び出し
main()

#ウィンドウの実行
root.mainloop()

#ウィンドウを閉じる
root.quit()
