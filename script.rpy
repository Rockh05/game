# 遊戲腳本位於此檔案。

# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define me = Character("我")
define yo = Character("學姊")
define Unknow=Character("???")
define ml = Character("小莫")
define qing = Character("阿青")

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
    "後半場我為救球摔得太用力——"
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
    
    jump ch5

label ch5:
    scene black with dissolve
    window hide
    show text "{size=48}{color=#FFFFFF}失去聯繫的幾週{/color}{/size}":
        xalign 0.8
        yalign 0.8
    with fade
    with Pause(1.5)
    
    scene black with fade
    with Pause(0.5)
    window show

    "後來幾個星期，我再也沒遇到學姊。"
    "不是刻意......但似乎也不意外。"
    "我的食指還留著些微被握過的觸感。"
    "我知道學姊在等——"
    "這次輪到我去找她。"
    "傷口逐漸結痂、脫落。"
    "天冷了。冬天快來了。"

    window hide
    with Pause(0.5)

    jump ch6

label ch6:
    scene black with dissolve
    window hide
    show text "{size=48}{color=#FFFFFF}世界與我們{/color}{/size}":
        xalign 0.8
        yalign 0.8
    with fade
    with Pause(1.5)

    scene bg daytop with fade
    with Pause(0.5)

    with None
    show me idle:
        xalign 0.8
        yalign 1.0
    show yo smile:
        xalign 0.2
        yalign 1.0
    with dissolve

    window show
    me "「學姊......妳喜歡女生嗎？」"
    show yo bigsmile:
        xalign 0.2
        yalign 1.0
    yo "「喜歡啊。」"
    yo "「就算全世界反對，也會不顧一切的那種喜歡。」"
    show me sadsmile:
        xalign 0.8
        yalign 1.0
    "就算全世界反對也無效的......喜歡。"
    yo "「只是世界的力量很強大。」"
    yo "「希望世界變好，或是我們變強。」"
    me "「我們......？」"
    show yo laugh:
        xalign 0.2
        yalign 1.0
    yo "「對啊，我們。不管妳喜不喜歡女生——」"
    yo "「妳會站在我這邊的吧？」"
    show me jishin:
        xalign 0.8
        yalign 1.0
    me "「會！我一定會。」"
    "學姊用手輕輕掠過我脖子上的髮絲。"
    show yo smile:
        xalign 0.2
        yalign 1.0
    yo "「你的長髮很可愛，短髮應該會變很帥。」"
    show me sadsmile:
        xalign 0.8
        yalign 1.0
    "我感到坐立難安，學姊靠的太近了。"
    yo "「我告訴妳怎麼判斷妳喜不喜歡女生。」"
    show me idle:
        xalign 0.8
        yalign 1.0
    me "「什麼？」"
    yo "「親我一下。」"
    me "「為什麼？！」"
    show yo bigsmile:
        xalign 0.2
        yalign 1.0
    yo "「輔導老師說的啦。」"
    yo "「女校可能會有『假性性傾向』。」"
    yo "「只要妳不想跟對方更親密，那就只是同儕壓力。」"
    yo "「所以親我一下，就知道妳是不是真的喜歡女生。」"
    show yo laugh:
        xalign 0.2
        yalign 1.0
    yo "「我願意當試驗品！」"
    me "「我不要為了實驗奪走妳的初吻啦。」"
    show yo sad:
        xalign 0.2
        yalign 1.0
    yo "「沒差，我的初吻已經不在了。」"
    me "「什——！？」"
    show yo angry:
        xalign 0.2
        yalign 1.0
    "學姊急忙捂住我的嘴。"
    yo "「噓！被教官發現我們在頂樓會被記警告啦。」"
    "此時，上課鐘聲響起。"
    "我們像在跳一個微妙的舞步。"
    "彼此靠近，卻又不跨過那條線。"

    window hide
    with Pause(0.5)

    jump ch7

label ch7:
    scene black with dissolve
    show text "{size=48}{color=#FFFFFF}晚餐與生日的夜晚{/color}{/size}":
        xalign 0.8
        yalign 0.8
    with fade
    with Pause(1.5)

    scene bg school with fade
    with Pause(0.5)

    with None
    show me idle:
        xalign 0.4
        yalign 1.0
    show yo smile:
        xalign 0.6
        yalign 1.0
    with dissolve

    yo "「欸，妳今天晚上有事嗎？」"
    me "「沒有。」"
    yo "「陪我吃飯。」"
    me "「好啊。妳不用趕回家？」"
    yo "「門禁取消一次。」"
    show me sadsmile:
        xalign 0.4
        yalign 1.0
    me "「行吧，妳想吃什麼？」"
    show yo laugh:
        xalign 0.6
        yalign 1.0
    yo "「麥當勞！大麥克套餐、薯條可樂都加大！」"
    me "「那我們放學後校門口見？」"
    show yo smile:
        xalign 0.6
        yalign 1.0
    yo "「阿對了，可以拜託妳買嗎？我有點事，晚點頂樓會合。」"
    "她把頭靠在我肩膀，我完全不敢動。"
    window hide

    scene black with fade
    with Pause(0.5)
    window show
    "晚上，校舍頂樓。"
    window hide

    scene bg nighttop with fade
    with Pause(0.5)

    with None
    show me idle with dissolve

    window show
    "我提著食物上樓時，學姊已經布置好一塊空地。"
    "正方形的格紋布上，放著一塊小蛋糕，蛋糕上還有幾根點燃的蠟燭。"
    hide me idle with dissolve

    with None
    show me idle:
        xalign 0.8
        yalign 1.0
    show yo laugh:
        xalign 0.2
        yalign 1.0
    with dissolve

    yo "「祝妳生日快樂！」"
    yo "「就算全世界都忘記，我也會記得。」"
    show me sadsmile:
        xalign 0.8
        yalign 1.0
    me "「可是......我生日是明天。」"
    show yo smile:
        xalign 0.2
        yalign 1.0
    yo "「有人規定不能偷跑嗎？」"
    yo "「快許願，吹蠟燭！」"
    "我猶豫了會，才閉上眼睛，在心中默念願望。"
    "這或許是我人生中第一個「圓形」的生日蛋糕。"

    window hide
    with Pause(0.5)

    jump ch8

label ch8:
    scene black with dissolve
    show text "{size=48}{color=#FFFFFF}真正的直屬學姊{/color}{/size}":
        xalign 0.8
        yalign 0.8
    with fade
    with Pause(1.5)

    scene bg school with fade
    with Pause(0.5)
    show ml idle with dissolve
    window show
    "小莫——我失聯已久的直屬學姊回來了。"
    "她是傳說級的中性學姊。"
    "關於她的病，謠言很多。"
    "這天，班上同學傳了張紙條給我。"
    "上面寫著「妳的直屬學姊小莫剛來過。她說很抱歉沒有照顧妳。」"
    "紙條尾端還提到——「聽說小遊常常去找妳。」"
    "小遊？常常來找我？"
    "我的高一前半，學姊就是全部。"
    "難道說..."
    window hide
    with Pause(0.5)
    jump ch9
    
label ch9:
    scene black with dissolve
    show text "{size=48}{color=#FFFFFF}球場上的邂逅{/color}{/size}":
        xalign 0.8
        yalign 0.8
    with fade
    with Pause(1.5)

    scene bg field with fade
    with Pause(0.5)

    with None
    show me idle:
        xalign 0.8
        yalign 1.0
    show ml bigsmile:
        xalign 0.2
        yalign 1.0
    with dissolve

    window show
    ml "「學妹，可以跟你們一起打嗎？」"
    "身邊的同學歡呼著學姊的出現。"
    "我不知為何，下意識想要遠離她。"
    show me annoy:
        xalign 0.8
        yalign 1.0
    me "「我不舒服......我想去保健室......」"
    me "我心虛地說。"
    qing "打一場啦！要是被老師知道你翹課，後果會很慘喔！。"
    "比賽很是激烈，小莫的球技幾乎壓著人打。"
    "最後她們班獲勝。"

    window hide
    with Pause(0.5)

    jump ch10

label ch10:
    scene black with dissolve
    show text "{size=48}{color=#FFFFFF}泳池邊的重逢{/color}{/size}":
        xalign 0.8
        yalign 0.8
    with fade
    with Pause(1.5)

    scene bg swim with fade
    with Pause(0.5)
    
    show me idle with dissolve

    window show
    "我去找掉到泳池的球，結果遇見了一位熟悉的人。"

    with None
    show me idle:
        xalign 0.8
        yalign 1.0
    show yo sad:
        xalign 0.2
        yalign 1.0
    with dissolve

    yo "「好久不見。」"
    me "「小莫呢？」"
    yo "「還在打球。」"
    "學姊舉起了呼拉圈。"
    show yo smile:
        xalign 0.2
        yalign 1.0
    yo "「我來試試看能不能把球勾回來。」"
    "她開始在水面上揮舞著呼拉圈，畫面十分滑稽。"
    show me laugh:
        xalign 0.8
        yalign 1.0
    me "「這不是夜市套圈圈啦！」"
    show yo laugh:
        xalign 0.2
        yalign 1.0
    yo "「欸妳笑了欸！」學姊興奮的說。"
    with None
    hide me laygh
    hide yo laugh
    with dissolve
    "幾分鐘後，呼拉圈、浮板全飄在水面上，現場混亂的像是剛舉辦完泳池派對。"
    with None
    show me sadsmile:
        xalign 0.8
        yalign 1.0
    show yo bigsmile:
        xalign 0.2
        yalign 1.0
    with dissolve
    yo "「我下去撿好了。」"
    me "「不要啦！天氣很冷！」"
    "不知為何，她的話觸動了我心中的某個開關。"
    "猶豫片刻後..."
    "撲通！"
    "我領先學姊跳進了泳池裡。"
    "我在水池中緩緩移動，把球帶回陸地。"
    "學姊看著狼狽的我，趕緊把我拉了上岸。"
    "我們對視了一下子，她的眼神透漏著一些情緒。"

    with None
    show me annoy:
        xalign 0.8
        yalign 1.0
    show yo sad:
        xalign 0.2
        yalign 1.0
    with dissolve

    yo "「妳最近怎麼都不來找我？」"
    me "「妳才沒有來找我。」我賭氣的說。"
    yo "「我覺得妳在生氣......才不敢來。」"
    me "「我不知道妳在幹嘛......不知道妳在想什麼。」"
    "語畢，兩人陷入了一段沉默。"
    yo "「是因為小莫？」"
    "我沉默了一會。"
    yo "「我跟小莫......已經分開了。」"
    show me idle:
        xalign 0.8
        yalign 1.0
    me "「所以她就是妳的初吻？」我驚呼道。"
    "換學姊沉默了一會。"
    yo "「去沖熱水澡，我幫妳拿衣服。」"
    "學姊轉身準備離開。"
    "我輕輕的拉了她的衣角。"
    show me sadsmile:
        xalign 0.8
        yalign 1.0
    me "「可以......重新開始嗎？」"
    "學姊轉過身來。"
    yo "「誰跟誰？」"
    me "「我們。」"
    show yo smile:
        xalign 0.2
        yalign 1.0
    "聽聞，學姊蹲下來伸出手，輕撥開我髮絲間的落葉，淺笑著說道。"
    yo "「妳好，我姓游。」"
    "我握住她的手。"
    me "「游小姐妳好......我不諳水性。」"

    window hide
    with Pause(0.5)
    jump end

label end:
    scene black with dissolve
    show text "{size=32}{color=#FFFFFF}未完待續...{/color}{/size}":
        xalign 0.8
        yalign 0.8
    with fade
    with Pause(2.0)

    return