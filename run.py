import lianzhong_api #line:1
import requests ,time ,os ,random ,re ,json #line:2
from base64 import b64decode #line:3
from selenium .webdriver .chrome .options import Options #line:4
from selenium .webdriver import ActionChains #line:5
from selenium import webdriver #line:6
from selenium .webdriver .support .wait import WebDriverWait #line:7
from selenium .webdriver .support import expected_conditions as EC #line:8
from selenium .webdriver .common .by import By #line:9
import cv2 as cv #line:10
TG_BOT_TOKEN =''#line:11
TG_USER_ID =''#line:12

if  "TG_USER_ID"in os .environ and os .environ ["TG_USER_ID"]:#line:13
        TG_BOT_TOKEN ='1698539466:AAHqZNARtVq2MJiFQIcygSxEjVDGpOJjY5k'#line:14
        TG_USER_ID =os .environ ["TG_USER_ID"]#line:15
        print ("Telegram 推送打开")#line:16
def get_email ():#line:17
    OO000O0O0OO0OOOOO =random .randint (11 ,999 )#line:18
    O000OO000O000O000 =random .randint (0 ,200 )#line:19
    OO0000O0000O00O00 ='varytmp+{}uu{}d@gmail.com'.format (OO000O0O0OO0OOOOO ,O000OO000O000O000 )#line:20
    return OO0000O0000O00O00 #line:21
def p_main (OOOOOO00O00OOO0O0 ,O0O000OO000OOOO0O ,OO0O0OO000O0O0000 ):#line:22
            OO000O0OO0000OO0O ='https://jc88.me/account/regist?userid='+OO0O0OO000O0O0000 #line:23
            O0O00OOOOOOO0O000 =get_email ()#line:24
            print (O0O00OOOOOOO0O000 )#line:25
            O0O0O00O0O00OO0O0 =Options ()#line:26
            O0O0O00O0O00OO0O0 =webdriver .ChromeOptions ()#line:27
            O0O0O00O0O00OO0O0 .add_argument ('--headless')#line:29
            O0O0O00O0O00OO0O0 .add_argument ('--disable-gpu')#line:30
            O0O0O00O0O00OO0O0 .add_argument ("--no-sandbox")#line:32
            O0O00O000000O00OO =webdriver .Chrome (options =O0O0O00O0O00OO0O0 )#line:33
            O0O00O000000O00OO .get (OO000O0OO0000OO0O )#line:35
            O0O00O000000O00OO .implicitly_wait (10 )#line:36
            time .sleep (1 )#line:37
            O0O00O000000O00OO .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[1]/div[2]/div/span/span/input').send_keys (O0O00OOOOOOO0O000 )#line:40
            O0OOO0O000O000000 =O0O00O000000O00OO .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/span/img').get_attribute ('src')#line:45
            O0OOO0O000O000000 =O0OOO0O000O000000 .split (",")[-1 ]#line:47
            O0OOO0O000O000000 =O0OOO0O000O000000 .replace ("%0A",'\n')#line:48
            O000O0OOOOOO0000O =b64decode (O0OOO0O000O000000 )#line:49
            with open ('./captcha.gif','wb')as O00O0OO0000OOO0OO :#line:50
                O00O0OO0000OOO0OO .write (O000O0OOOOOO0000O )#line:51
                O00O0OO0000OOO0OO .close ()#line:52
            time .sleep (2 )#line:53
            O00OOOOOO00OO0000 ='./captcha.gif'#line:55
            O0O0OOOO000000O00 =lianzhong_api .main (OOOOOO00O00OOO0O0 ,O0O000OO000OOOO0O ,O00OOOOOO00OO0000 ,'http://v1-http-api.jsdama.com/api.php?mod=php&act=upload','','','1008','8dc962b56f1968a844450834ef91bfd0')#line:57
            O000OOO000000O000 =O0O0OOOO000000O00 .json ()['data']['val']#line:59
            OOO00O0OO0000O000 =O0O0OOOO000000O00 .json ()['data']['id']#line:60
            print ('图片已识别:'+O000OOO000000O000 )#line:61
            O0O00O000000O00OO .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/input').send_keys (O000OOO000000O000 )#line:64
            time .sleep (1 )#line:66
            O0O00O000000O00OO .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/span/button').click ()#line:68
            time .sleep (10 )#line:70
            os .remove (O00OOOOOO00OO0000 )#line:72
            OOOO00OOOOOOOO0O0 =get_num (O0O00OOOOOOO0O000 )#line:74
            print (OOOO00OOOOOOOO0O0 )#line:75
            print ('验证码已识别：'+OOOO00OOOOOOOO0O0 [0 ])#line:76
            O0O00O000000O00OO .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/input').send_keys (OOOO00OOOOOOOO0O0 [0 ])#line:79
            O0O00O000000O00OO .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/form/div[4]/div[2]/div/span/span/input').send_keys ('qwer1234')#line:83
            time .sleep (1 )#line:85
            O0O00O000000O00OO .find_element_by_xpath ('//*[@id="app"]/section/main/div/div/div[2]/div/p[1]/button').click ()#line:86
            print ('正在点击注册完成！')#line:87
            time .sleep (2 )#line:88
            tx_code (O0O00O000000O00OO )#line:89
            time .sleep (4 )#line:90
            if O0O00O000000O00OO .current_url =='https://jc88.me/home':#line:91
                telegram_bot ("p88",'邀请成功！')#line:92
                O0O00O000000O00OO .quit ()#line:93
            else :#line:94
                telegram_bot ("P88",'邀请失败！')#line:95
                print ('邀请失败！')#line:96
def telegram_bot (OO0O0OOOOO00O0O00 ,O00000O0O000OOOO0 ):#line:97
    print ("\n")#line:98
    OO0OO00OOOOO0O0OO =TG_BOT_TOKEN #line:99
    O0000OOO00OOO000O =TG_USER_ID #line:100
    if "TG_USER_ID"in os .environ :#line:101
        OO0OO00OOOOO0O0OO ='1698539466:AAHqZNARtVq2MJiFQIcygSxEjVDGpOJjY5k'#line:102
        O0000OOO00OOO000O =os .environ ["TG_USER_ID"]#line:103
    if not OO0OO00OOOOO0O0OO or not O0000OOO00OOO000O :#line:104
        print ("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")#line:105
        return #line:106
    print ("Telegram 推送开始")#line:107
    O0000O0O0OO0O0000 ={"chat_id":O0000OOO00OOO000O ,"text":OO0O0OOOOO00O0O00 +'\n\n'+O00000O0O000OOOO0 ,"disable_web_page_preview":"true"}#line:109
    O00OOOO00OO0O0O00 =requests .post (url ='https://api.telegram.org/bot%s/sendMessage'%(OO0OO00OOOOO0O0OO ),data =O0000O0O0OO0O0000 )#line:111
    print (O00OOOO00OO0O0O00 .text )#line:112
def get_num (O00O0OO0OOO00OO00 ):#line:113
    global Driver #line:114
    OO00000OO0OO00000 ={'Cookie':'csrf_gmailnator_cookie=9283eccf4672e233327c1d07cbde2fbe; __gads=ID=808c92a03a3667c7-2268f1463cc6007d:T=1614844196:RT=1614845007:S=ALNI_MaEB-hZfUPTo6kHkEmOBLzPe4nqTQ; cto_bundle=AGHOXV9XSVpTNzY3TlRHbldjMDY5RFhQTlU4Y2J1cUpIWGNLVU0xa3ZiWGRKV1duNHo5cXpJYSUyQm5mZ0ROVDJBRFlIa211cG85JTJCOElMV0ZGQUIzVCUyRjg4NTdQZmZSSW9xMzZmMVY5dXdXeDViUUFYeG51SWNibEhqZGxqWGU5NjBQZHpxMg; _ga=GA1.2.1618068840.1614844229; _gid=GA1.2.103981802.1614844229; ci_session=15d382f04f7b998cecd0f9158bfe3db2c8f32629; __cfduid=d1f9a21dd34e5060cfd24ea55f37149961614844181'}#line:117
    O00O000OO0OOOO00O ={'csrf_gmailnator_token':'9283eccf4672e233327c1d07cbde2fbe','action':'LoadMailList','Email_address':O00O0OO0OOO00OO00 }#line:119
    try :#line:120
        OOO0O0OOO0000O000 =requests .post (url ='https://www.gmailnator.com/mailbox/mailboxquery',data =O00O000OO0OOOO00O ,headers =OO00000OO0OO00000 ).text #line:121
        O000O00000O000OO0 =re .findall (r'(?<=messageid\\/#).+(?=\\">\\n\\t\\t\\t\\t\\t<table class=\\"message_container)',OOO0O0OOO0000O000 )[0 ]#line:122
        OOO00O0O00O00OO0O ={'csrf_gmailnator_token':'9283eccf4672e233327c1d07cbde2fbe','action':'get_message','message_id':O000O00000O000OO0 ,'email':'varytmp'}#line:124
        O00OO0OO00000O00O =requests .post (url ='https://www.gmailnator.com/mailbox/get_single_message/',headers =OO00000OO0OO00000 ,data =OOO00O0O00O00OO0O ).json ()#line:125
        O0O0O000OOOOOOOO0 =O00OO0OO00000O00O ['content']#line:127
        O0OOOO0O00OO000O0 =re .findall (r'(?<=验证码为 <b>).+(?=</b>，有效)',O0O0O000OOOOOOOO0 )#line:129
        return O0OOOO0O00OO000O0 #line:130
    except Exception as O00O0O0000OO00OO0 :#line:131
        print (O00O0O0000OO00OO0 )#line:132
def tx_code (O0O0O000O00OOOO0O ):#line:133
    ""#line:134
    O0O0O000O00OOOO0O .implicitly_wait (10 )#line:135
    O0O0O000O00OOOO0O .switch_to .frame ("tcaptcha_iframe")#line:136
    time .sleep (0.5 )#line:138
    O0OOO0OO0O0OO0OO0 =O0O0O000O00OOOO0O .find_element_by_xpath ('//img[@id="slideBg"]').get_attribute ('src')#line:139
    print (O0OOO0OO0O0OO0OO0 )#line:140
    if save_img (O0OOO0OO0O0OO0OO0 ):#line:141
        O0OOO0O00OOO00000 =get_pos ()#line:142
        O0000O0OO00OOOOO0 =get_track (O0OOO0O00OOO00000 )#line:143
        time .sleep (0.5 )#line:144
        OO0OO0O00OOO0O0OO =O0O0O000O00OOOO0O .find_element_by_xpath ('// *[ @ id = "tcaptcha_drag_thumb"]')#line:145
        ActionChains (O0O0O000O00OOOO0O ).click_and_hold (on_element =OO0OO0O00OOO0O0OO ).perform ()#line:146
        time .sleep (0.2 )#line:147
        print ('轨迹',O0000O0OO00OOOOO0 )#line:148
        for OO0OOO0OOOOOO0OO0 in O0000O0OO00OOOOO0 :#line:149
            ActionChains (O0O0O000O00OOOO0O ).move_by_offset (xoffset =OO0OOO0OOOOOO0OO0 ,yoffset =0 ).perform ()#line:150
        time .sleep (1 )#line:151
        ActionChains (O0O0O000O00OOOO0O ).release (on_element =OO0OO0O00OOO0O0OO ).perform ()#line:152
        time .sleep (5 )#line:153
        return True #line:155
    else :#line:156
        print ('缺口图片捕获失败')#line:157
        return False #line:158
def save_img (OOOO00OO00OO00O00 ):#line:160
    ""#line:161
    try :#line:162
        O00OOO0OO00OOO00O =requests .get (OOOO00OO00OO00O00 ).content #line:163
        with open ('bg.jpeg','wb')as OOOOO00OOO0O0O000 :#line:164
            OOOOO00OOO0O0O000 .write (O00OOO0OO00OOO00O )#line:165
        return True #line:166
    except :#line:167
        return False #line:168
def get_pos ():#line:171
    ""#line:174
    OOOOO000000000OO0 =cv .imread ('bg.jpeg')#line:175
    OOOO0O0OO00O0O0O0 =cv .GaussianBlur (OOOOO000000000OO0 ,(5 ,5 ),0 )#line:176
    OOO0O0000000000O0 =cv .Canny (OOOO0O0OO00O0O0O0 ,200 ,400 )#line:177
    O00OOO0OO0000OOOO ,O0O00O0O0OOO0OO0O =cv .findContours (OOO0O0000000000O0 ,cv .RETR_EXTERNAL ,cv .CHAIN_APPROX_SIMPLE )#line:178
    for OO00OO0OO0000OOOO ,OOOOOOOOO00O0O00O in enumerate (O00OOO0OO0000OOOO ):#line:179
        O0O00O00OOO0O0OOO =cv .moments (OOOOOOOOO00O0O00O )#line:180
        if O0O00O00OOO0O0OOO ['m00']==0 :#line:181
            OO000000000O0OOOO =O0000O0OOO000000O =0 #line:182
        else :#line:183
            OO000000000O0OOOO ,O0000O0OOO000000O =O0O00O00OOO0O0OOO ['m10']/O0O00O00OOO0O0OOO ['m00'],O0O00O00OOO0O0OOO ['m01']/O0O00O00OOO0O0OOO ['m00']#line:184
        if 6000 <cv .contourArea (OOOOOOOOO00O0O00O )<8000 and 370 <cv .arcLength (OOOOOOOOO00O0O00O ,True )<390 :#line:185
            if OO000000000O0OOOO <400 :#line:186
                continue #line:187
            O0O0OO00000OO0OO0 ,O0OO000O0O0O00O00 ,OOOO0000OO00000OO ,OOO000OOO0O000OO0 =cv .boundingRect (OOOOOOOOO00O0O00O )#line:188
            cv .rectangle (OOOOO000000000OO0 ,(O0O0OO00000OO0OO0 ,O0OO000O0O0O00O00 ),(O0O0OO00000OO0OO0 +OOOO0000OO00000OO ,O0OO000O0O0O00O00 +OOO000OOO0O000OO0 ),(0 ,0 ,255 ),2 )#line:189
            print ('【缺口识别】 {x}px'.format (x =O0O0OO00000OO0OO0 /2 ))#line:191
            return O0O0OO00000OO0OO0 /2 #line:192
    return 0 #line:193
def get_track (O000OO0O0OOOO0000 ):#line:196
    ""#line:198
    O000OO0O0OOOO0000 -=37 #line:199
    OOO00OOO00O0O0OOO =0 #line:201
    OOO0O0OOOO0OO00OO =0.2 #line:203
    OO000O0OOOOOO00OO =[]#line:205
    OOO0OOOOOOOOO0OOO =0 #line:207
    O00OOO00O000O0OO0 =O000OO0O0OOOO0000 *7 /8 #line:209
    O000OO0O0OOOO0000 +=10 #line:211
    while OOO0OOOOOOOOO0OOO <O000OO0O0OOOO0000 :#line:213
        if OOO0OOOOOOOOO0OOO <O00OOO00O000O0OO0 :#line:214
            O00OOOOOOO00000OO =random .randint (2 ,4 )#line:216
        else :#line:217
            O00OOOOOOO00000OO =-random .randint (3 ,5 )#line:218
        OOO00O00O0O00OOOO =OOO00OOO00O0O0OOO #line:221
        OOOOOO00O00O0O0O0 =OOO00O00O0O00OOOO *OOO0O0OOOO0OO00OO +0.5 *O00OOOOOOO00000OO *(OOO0O0OOOO0OO00OO **2 )#line:223
        OOO0OOOOOOOOO0OOO +=OOOOOO00O00O0O0O0 #line:225
        OO000O0OOOOOO00OO .append (round (OOOOOO00O00O0O0O0 ))#line:227
        OOO00OOO00O0O0OOO =OOO00O00O0O00OOOO +O00OOOOOOO00000OO *OOO0O0OOOO0OO00OO #line:230
    for OO0O0O0O00OO0O000 in range (4 ):#line:233
        OO000O0OOOOOO00OO .append (-random .randint (2 ,3 ))#line:234
    for OO0O0O0O00OO0O000 in range (4 ):#line:235
        OO000O0OOOOOO00OO .append (-random .randint (1 ,3 ))#line:236
    return OO000O0OOOOOO00OO #line:237
def move_to (O00OO0O00O0OOO000 ):#line:239
    ""#line:240
    pass #line:241
def main ():#line:244
    OOOO000OOO0O00OO0 =os .environ ["USER"]#line:245
    O0000OOOOOO0O0O00 =os .environ ["PASSWORD"]#line:246
    O00OO0O0OOOO0O0O0 =os .environ ["INVITECODE"]#line:247
    O0OOOO0OO0OO0O00O =lianzhong_api .get_points (OOOO000OOO0O00OO0 ,O0000OOOOOO0O0O00 )#line:248
    O0OOOO0OO0OO0O00O =O0OOOO0OO0OO0O00O .json ()['data']#line:249
    
    print ('剩余点数：'+str (O0OOOO0OO0OO0O00O ))#line:250
    if  "START"in os .environ and os .environ ["START"]=='584UYTH888':#line:13
        if int (O0OOOO0OO0OO0O00O )<=2 :#line:251
                print ('点数不足！！')#line:252
                time .sleep (5 )#line:253
                telegram_bot ("p++",'点数不足！')#line:254
                exit ()#line:255
        else :#line:256
                print ('start')#line:257
                p_main (OOOO000OOO0O00OO0 ,O0000OOOOOO0O0O00 ,O00OO0O0OOOO0O0O0 )#line:258
    else:
        print('没有启动码!')
        telegram_bot ("P88",'没有启动码!')
if __name__ =='__main__':#line:261
    main ()
