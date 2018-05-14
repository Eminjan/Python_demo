#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:Eminjan
#@Time  :2018/5/14 21:31

import requests
import itchat

def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents,translation

def send_news():

    try:
        # 登陆你的微信账号，会弹出登录二维码，扫描就可
        itchat.auto_login(hotReload=True)
        # 获取你对应的好友备注
        my_firend = itchat.search_friends(name="Arzu学妹")
        ArzuXueMei = my_firend[0]["UserName"]
        # 获取金山字典的内容
        message1 = str(get_news()[0])
        content = str(get_news()[1][17:])
        message2 = str(content)
        message3 = "Test Program"

        # 发送消息
        itchat.send(message1,toUserName=ArzuXueMei)
        itchat.send(message2,toUserName=ArzuXueMei)
        itchat.send(message3,toUserName=ArzuXueMei)


    except:
        message4 = u"今天最爱你的人出现了 bug /(ㄒoㄒ)/~~"
        itchat.send(message4, toUserName=ArzuXueMei)

def main():
    send_news()

if __name__ == '__main__':
    main()