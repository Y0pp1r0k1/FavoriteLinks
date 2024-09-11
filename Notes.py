import customtkinter as CTK
import CustomLinkDefs as CLD
import CTkDefs as defs
 

def NotesWindow() :

    #ウィンドウの制作
    NotesWindow = CTK.CTkToplevel()
    NotesWindow.title("お知らせ")
    NotesWindow.geometry("700x500")
    NotesWindow.geometry("+750+280")
    NotesWindow.focus_force()
    NotesWindow.attributes("-topmost", True)


    #アイコンの設定
    logo = CLD.temp_path("./data/icon.ico")
    NotesWindow.iconbitmap(default=logo)

    #注意事項のテキストたち
    defs.labelDef("label", NotesWindow, "重要なお知らせ", 0, 0, CTK.W, "HGS創英角ゴシックUB", 25, 10, 10)

    defs.labelDef("label", NotesWindow, "この度は当アプリをご利用いただきありがとうございます。突然ですが、お知らせになります。", 1, 0, CTK.W, "游ゴシック", 15, 20, 5)
    
    defs.labelDef("label", NotesWindow, "現在、このアプリは制作進行中であり、未実装の機能を一時的に使用不可能な状態にしています。", 2, 0, CTK.W, "游ゴシック", 15, 20, 5)
    
    defs.labelDef("label", NotesWindow, "以下のものが使用不可能な機能になります。", 3, 0, CTK.W, "游ゴシック", 15, 20, 5)
    
    defs.labelDef("label", NotesWindow, "○ 使用不可能な機能一覧", 4, 0, CTK.W, "游ゴシック", 15, 20, 5)
    
    defs.labelDef("label", NotesWindow, "● ユーザー機能全般", 5, 0, CTK.W, "游ゴシック", 15, 50, 5)

    defs.labelDef("label", NotesWindow, "● 設定", 6, 0, CTK.W, "游ゴシック", 15, 50, 5)

    defs.labelDef("label", NotesWindow, "● リンクのカスタム機能", 7, 0, CTK.W, "游ゴシック", 15, 50, 5)

    defs.labelDef("label", NotesWindow, "これらの機能は今後実装していく予定です。ご理解の程、よろしくお願い致します", 8, 0, CTK.W, "游ゴシック", 15, 30, 5)
    
    defs.labelDef("label", NotesWindow, "最新情報や更新情報は以下のリンクから確認可能です。ぜひご覧ください。", 9, 0, CTK.W, "游ゴシック", 15, 30, 5)

    CLD.linkContent2("link", NotesWindow, "GitHub : https://github.com/Y0pp1r0k1/FavoriteLinks", 10, 0, 200, 5, "https://github.com/Y0pp1r0k1/FavoriteLinks")   
    
    defs.labelDef("label", NotesWindow, "アプリバージョン　Ver 2.0 / 2.0最終アップデート日 2024/7/15", 11, 0, CTK.W, "游ゴシック", 15, 250, 5)

    #閉じるボタン
    Button = CTK.CTkButton(NotesWindow, text="Close")
    Button.grid(row=12, column=0, padx=(300, 0))
    Button.bind("<Button-1>", lambda e:close())

    def close() :
        NotesWindow.destroy()
 
 



