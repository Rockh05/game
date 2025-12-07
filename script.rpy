# 遊戲腳本位於此檔案。

# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define me = Character("主角")
define yo = Character("學姊")
define Unknow=Character("???")

transform shake:
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0

# 遊戲從這裡開始。

label start:
    show scene1 with fade
    "夏天的那個午後，草地上還留著太陽的餘溫。一切都柔和得像夢。"
    "那時候的我們，都還好年輕。"
    #---------------------------------------------------ch2
    show scene2
    "我是一個路痴，常常在十字路口面臨多條岔路。"
    "天我漫無目的地亂走，一個轉角"
    show yo smile with fade
    "我看見了學姊。"
    "世界像突然按下慢速播放，每一個畫面都能被凍結分析。"
    hide yo smlie
    show me shock
    me "欸……學姊？那是  她離我，只有一步之遙。"
    me "學姊！請問……這附近怎麼走？"
    hide me shock
    with fade
    show yo smile at right
    show me shy  at left
    yo "啊，我認得妳。妳是一年○班吧？"
    yo "來，我帶妳去。"
    scene  scene2 with dissolve
    "學姊伸手，牽住了主角的手。"
    scene  black with fade
    "我的注意力全在她身上。"
    "我卻連她的班級、學號、名字都不知道。"
    "學姊……！為什麼我什麼都不知道！"
    #---------------------------------------------------ch3
    scene scene3 with fade
    "我們女校有個潛規則——直屬學姊制度。"
    "但我的直屬學姊在高一下休學了。"
    "雖然有點落寞……"
    "但我把所有心力都投入排球。"
    "同學、學姊們的陪伴，沖淡了那份孤單。"
    #---------------------------------------------------ch4
    scene scene4 with fade
    "比賽開始，學姊來看我了。"
    "我們的眼神對上那一瞬間，心跳加速。"
    show scene4 at shake
    show me hurt at left
    "後半場我為救球摔得太用力──"
    "手肘破皮，膝蓋滲血。"
    scene scene5 with fade
    show me shy at left
    me "謝謝……"
    "【學姊（作勢要拍傷口）】"
    show yo smile at right
    yo "痛不痛？"
    show scene3
    hide me shy
    show me shock at left
    me "會、會會會！！"
    yo "下次小心一點啦。沒看過妳這麼拚命的打法。"
    "【動作】學姊伸手、摸主角的頭。"
    scene black
    "溫暖的觸感，讓我差點想哭。"
    scene scene5
    show me shy at left
    show me smile at right
    me "謝謝學姊……"
    yo "妳不要一直說謝謝。"
    show scene5 at shake
    hide me shy
    show me shock at left
    show yo smile at right
    yo "還沒吸收藥效，別亂動。"
    #---------------------------------------ch5

    return