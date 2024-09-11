import customtkinter as ctk
import os
from pathlib import Path

import CustomLinkDefs as CLD
from signInWindow import signIn
from signUpWindow import signUp
from Notes import NotesWindow
from settingHome import settingWindow
from Custom import customWindow

#ウィンドウの設定
root = ctk.CTk()
root.title("Favorite Links and App")
root.geometry("1280x720")
root.geometry("+300+160")

#アイコンの設定


#アプリを起動したUserのIDを取得する処理
UserName = os.getlogin()

#main
def main():

    #アイコンの設定
    #appdir = Path(__file__).parent 
    #iconfile = appdir / "icon.ico"
    #root.iconbitmap(iconfile)

    #サインイン
    signIn = ctk.CTkButton(root, text="Sign In", font=("游ゴシック", 10), state="disable")
    signIn.place(x=1100, y=20)
    #signIn.bind("<Button-1>", lambda e:signIn())
        #完成したら元に戻す

    signIn.bind("<Button-1>", lambda e:NotesWindow())
        #SignInWindowが完成したら消す


    #サインアップ
    signUp = ctk.CTkButton(root, text="Sign Up", font=("游ゴシック", 10), state="disable")
    signUp.place(x=1100, y=70)
    #signUp.bind("<Button-1>", lambda e:signUp())
        #完成したら元に戻す

    signUp.bind("<Button-1>", lambda e:NotesWindow())
        #SignInWindowが完成したら消す


    #設定
    setting = ctk.CTkButton(root, text="Setting", font=("游ゴシック", 10), state="disable")
    setting.place(x=1100, y=660)
    #setting.bind("<Button-1>", lambda e:settingWindow())
        #settingHomeが完成したら元に戻す

    setting.bind("<Button-1>", lambda e:NotesWindow())
        #settingHomeが完成したら消す

    #カスタムリンク
    custom = ctk.CTkButton(root, text="Custom link", font=("游ゴシック", 10), state="disable")
    custom.place(x=1100, y=620)
    #custom.bind("<Button-1>", lambda e:customWindow())

    custom.bind("<Button-1>", lambda e:NotesWindow())

    #タイトルの追加 SNS
    CLD.TitleContent(root,"SNS", "SNS", 20, 20)

    #X
    CLD.linkContent1(root, "X", "X(旧Twitter)", 40, 45, "https://twitter.com")

    #HoyoLab
    CLD.linkContent1(root, "HoyoLab", "HoyoLab", 40, 65, "https://www.hoyolab.com")

    #TikTok
    CLD.linkContent1(root, "TikTok", "TikTok", 40, 85, "https://www.tiktok.com")


    
    #コミュニケーションサービス
    CLD.TitleContent(root,"communicationService", "コミュニケーションサービス", 20, 110)

    #Discord　Web
    CLD.linkContent1(root, "DiscordWeb", "Discord(Web版)", 40, 135, "https://discord.com/channels/@me")

    #Discord app
    CLD.AppContent(root, "DiscordApp", "Discord(App版)", 40, 155, rf"C:\Users\{UserName}\AppData\Local\Discord\Update.exe --processStart Discord.exe")

    #LINE web
    CLD.AppContent(root, "LINEWeb", "LINE(Web版)", 40, 175, rf"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #LINE app
    CLD.AppContent(root, "LINEApp", "LINE(App版)", 40, 195, rf"C:\Users\{UserName}\AppData\Local\LINE\bin\LineLauncher.exe")

    #Slack Web
    CLD.linkContent1(root, "SlackWeb", "Slack(Web版)", 40, 215, "https://app.slack.com/client")

    #Slack app
    CLD.AppContent(root, "SlackApp", "Slack(App版)", 40, 235, rf"C:\Users\{UserName}\AppData\Local\slack\slack.exe")



    #プログラミング系 Site
    CLD.TitleContent(root, "programmingSite", "プログラミング Site", 20, 260)

    #GitHub
    CLD.linkContent1(root, "GitHub", "GitHub", 40, 285, "https://github.com")

    #Progate
    CLD.linkContent1(root, "Progate", "Progate", 40, 305, "https://prog-8.com/")

    #Python-izm
    CLD.linkContent1(root, "Python-izm", "Python-izm", 40, 325, "https://www.python-izm.com")

    #Qiita
    CLD.linkContent1(root, "Qiita", "Qiita", 40, 345, "https://qiita.com")

    #WebColorCode
    CLD.linkContent1(root, "WebColorCode", "Web色見本", 40, 365, "https://www.colordic.org/")



    #プログラミング系　App
    CLD.TitleContent(root,"programmingApp", "プログラミング App", 20, 390)

    #Blender 
    CLD.AppContent(root, "Blender", "Blender", 40, 415, rf"C:\Program Files\Blender Foundation\Blender 4.0\blender-launcher.exe")

    #VisualStudioCode
    CLD.AppContent(root, "VisualStudioCode", "VisualStudioCode", 40, 435, rf"C:\Users\ys082\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    #Unity hub
    CLD.AppContent(root, "Unity", "Unity", 40, 455, rf"C:\Program Files\Unity Hub\Unity Hub.exe")



    #動画配信サービス
    CLD.TitleContent(root,"VideoService", "動画配信サービス", 20, 480)

    #Youtube 
    CLD.linkContent1(root, "Youtube", "Youtube", 40, 505, "https://www.youtube.com")

    #Twitch
    CLD.linkContent1(root, "Twitch", "Twitch", 40, 525, "https://www.twitch.tv")

    #TVer 
    CLD.linkContent1(root, "TVer", "TVer", 40, 545, "https://tver.jp")

    #Amazon Prime
    CLD.linkContent1(root, "PrimeVideo", "PrimeVideo", 40, 565, "https://www.amazon.co.jp/gp/video/storefront/ref=atv_hm_hom_legacy_redirect?contentId=IncludedwithPrime&contentType=merch&merchId=IncludedwithPrime")

    #Hulu
    CLD.linkContent1(root, "Hulu", "Hulu", 40, 585, "https://www.hulu.jp")

    #Netflix
    CLD.linkContent1(root, "Netflix", "Netflix", 40, 605, "https://www.netflix.com/jp/")



    #ブラウザ
    CLD.TitleContent(root,"browser", "ブラウザ", 20, 630)

    #Chrome
    CLD.AppContent(root, "Chrome", "Chrome", 40, 655, rf"C:\Program Files\Google\Chrome\Application\chrome.exe")

    #Edge
    CLD.AppContent(root, "Edge", "Edge", 40, 675, rf"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

    

    #便利系サイト
    CLD.TitleContent(root, "convenientSite", "便利系サイト", 300, 20)

    #unlimited:waifu2x
    CLD.linkContent1(root, "unlimited:waifu2x", "unlimited:waifu2x", 320, 45, "https://unlimited.waifu2x.net/#google_vignette")

    #URL Shortener
    CLD.linkContent1(root, "URLShortener", "URL Shorttener", 320, 65, "https://tinyurl.com/app")



    #ゲーム　Site
    CLD.TitleContent(root, "gamesSite", "ゲームリンク Site", 300, 90)

    #GenshinBuildCard
    CLD.linkContent1(root, "GenshinBuildCard", "GenshinBuildCard", 320, 115, "https://artifacter.neody.land/ja-JP/genshin/")

    #HSRBuildCard
    CLD.linkContent1(root, "HSRBuildCard", "HSRBuildCard", 320, 135, "https://artifacter.neody.land/ja-JP/hsr/")

    #VALORANTTracker
    CLD.linkContent1(root, "VALORANTTracker", "VALORANTTracker", 320, 155, "https://tracker.gg/valorant/")



    #ゲーム　App
    CLD.TitleContent(root,"gamesApp", "ゲーム App", 300, 180)

    #GenshinImpact
    CLD.AppContent(root, "GenshinImpact", "GenshinImpact", 320, 205, rf"C:\Windows\system32\schtasks.exe /run /tn GenshinImpact")

    #Houkai:StarRail
    CLD.AppContent(root, "Houkai:StarRail", "Houkai:StarRail", 320, 225, rf"C:\Windows\system32\schtasks.exe /run /tn HoukaiStarRail")

    #VALORANT 
    CLD.AppContent(root, "VALORANT", "VALORANT", 320, 245, rf"C:\Riot Games\Riot Client\RiotClientServices.exe --launch-product=valorant --launch-patchline=live")

    #OW2
    CLD.AppContent(root, "OverWatch2", "OverWatch2", 320, 265, rf"C:\Program Files (x86)\Steam\steamapps\common\Overwatch\Overwatch.exe")

    #ApexLegends
    CLD.AppContent(root, "ApexLegends", "ApexLegends", 320, 285, rf"C:\Program Files (x86)\Steam\steamapps\common\Apex Legends\r5apex.exe")

    #osu!
    CLD.AppContent(root, "osu!", "osu! (classic)", 320, 305, rf"C:\Users\{UserName}\AppData\Local\osu!\osu!.exe")

    #AimLabs
    CLD.AppContent(root, "AimLabs", "AimLabs", 320, 325, rf"C:\program Files (x86)\steam\steamapps\common\Aim Lab\AimLab_tb.exe")

    CLD.AppContent(root, "XDefiant", "XDefiant", 320, 345, rf"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\games\XDefiant\XDefiant.exe")


    
    #ゲームランチャー
    CLD.TitleContent(root, "gamesLauncher", "ゲームランチャー", 300, 370)

    #Steam 
    CLD.AppContent(root, "Steam", "Steam", 320, 395, rf"C:\Program Files (x86)\Steam\steam.exe")

    #RiotGames
    CLD.AppContent(root, "Riot Client", "Riot Client", 320, 415, rf"C:\Riot Games\Riot Client\RiotClientServices.exe")

    #Ubisoft
    CLD.AppContent(root, "Ubisoft", "Ubisoft", 320, 435, rf"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\UbisoftConnect.exe")

    #EpicGamesLauncher
    CLD.AppContent(root, "EpicGames", "EpicGames", 320, 455, rf"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe")



    #ウィンドウの実行
    root.mainloop()

NotesWindow()

#main関数の呼び出し
main()

