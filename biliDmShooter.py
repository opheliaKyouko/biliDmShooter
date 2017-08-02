import requests
import json
import random
import pymysql
from multiprocessing.dummy import Pool as ThreadPool
import sys
import datetime
import time
from imp import reload
from bs4 import BeautifulSoup
import re

class dmShooter:
    postLink = "https://interface.bilibili.com/dmpost?cid=21044350&aid=12802603&pid=1&ct=1"
    #postLink = "https://interface.bilibili.com/dmpost?cid=8217915&aid=5058980&pid=1&ct=1"

    heads = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '176',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'UM_distinctid=15ad5656ae42d0-02ada8b094b9d9-3e64430f-100200-15ad5656ae52d4; pgv_pvi=419131392; fts=1489638879; sid=k6hzui35; rpdid=oqqwsmxilxdopqlxsqkpw; buvid3=0F551A78-75F9-4CD3-9E27-2598B45EE73239886infoc; _ga=GA1.2.2104182693.1490083328; tma=136533283.65841841.1495978582031.1495978582031.1495978582031.1; tmd=3.136533283.65841841.1495978582031.; _qddaz=QD.3ztoxi.vgiiwi.j0xek9q5; HTML5PlayerCRC32=3539211364; finger=81df3ec0; uTZ=-480; LIVE_BUVID=1bfcfc4d0cacfaf0db3855dcdf0e40b0; LIVE_BUVID__ckMd5=f5e763c5273bbcfd; DedeUserID=808545; DedeUserID__ckMd5=d7d91faef040e5db;SESSDATA=a07e0577%2C1503501203%2C98e0ace7;  bili_jct=9f179a962285670f35d1c2392aa2d330; user_face=http%3A%2F%2Fi1.hdslb.com%2Fbfs%2Fface%2F5e6ea7566bcc776d55288b9aa1bc2dd5c1263fd6.jpg; pgv_si=s214607872; purl_token=bilibili_1501596868; biliMzIsnew=1; biliMzTs=null; _cnt_pm=0; _cnt_notify=0; _dfcaptcha=928df88e465df5117e998f4cf8a62407',
        'Host': 'interface.bilibili.com',
        'Origin': 'https://www.bilibili.com',
        'Referer': 'https://www.bilibili.com/video/av12802603/?from=search&seid=8780256231569288628',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    params = {
        'fontsize': '25',
        'pool': '0',
        'mode': '4',
        'color': '16777215',
        'rnd': '1501590340951250',
        'message': '23333',
        'playTime': '1636.963084',
        'cid': '21044350',
        # 'cid': '8217915',
        'date': '2017-08-01 20:48:56',
        'csrf': '9f179a962285670f35d1c2392aa2d330'
    }

    def __init__(self):
        self.session = requests.session()

    def postDm(self, videoTime, dmText):
        #get current time
        sendDate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        self.params['date'] = str(sendDate)
        self.params['playTime'] = videoTime
        self.params['message'] = dmText

        rndNum = random.randint(1501597969253783, 1501597969263783)
        self.params['rnd'] = str(rndNum)
        print (str(sendDate),videoTime,str(rndNum),dmText)
        jscontent = requests.session().post(self.postLink, headers=self.heads, data=self.params).text
        return jscontent

class userData:
    def __init__(self):
        self.cookie = ''
        self.aid = ''
        self.cid = ''
        self.csrf = ''
        self.mid = ''
        pass

    def getVideoId(self,html):
        htmlList = html.split("\n")
        for lineItem in htmlList:
            if ('cid' and 'aid' in lineItem):
                # '<div id='player_placeholder' class='player'></div><script type='text/javascript'>EmbedPlayer('player', "//static.hdslb.com/play.swf", "cid=21014825&aid=12783044&pre_ad=");</script>
                #lineItem = r"cid=12345&aid"
                pattenStr = r"cid=(\d+)&aid=(\d+)&pre"
                patten = re.compile(pattenStr)
                idList = patten.findall(lineItem)[0]
                self.cid = idList[0]
                self.aid = idList[1]
                print ("get cid = %s,and aid = %s" % (self.cid,self.aid))
                return True
        else:
            print("get video data fail")
            return False

    def getCookie(self,webCookie):

        pass


if __name__ == '__main__':

    uData = userData()

    #input website
    #biliLink = "https://www.bilibili.com/video/av12775565/"
    biliLink = input("please input your bilibili video link:")
    htm =requests.get(biliLink)
    if(uData.getVideoId(htm.text) == False):
        print("exit because of network fault")
        exit(1)

    #input cookie
    webCookie = input("please input your cookie:")
    uData.getCookie(webCookie)

    assFileNmae = input("please input your ass file name:" )





"""
    dmShooter = dmShooter()
    file_object = open(assFileNmae,'r+',encoding='UTF-8')

    assLines = file_object.readlines()

    for lintItem in assLines:
        if lintItem.count('Dialogue') == 1:
            time.sleep(5.0+random.random())
            currentLine = (lintItem.split('\n')[0]).split(",")
            timeMarkList = currentLine[1].split(':')
            timeMark = float(timeMarkList[0])*3600+float(timeMarkList[1])*60+float(timeMarkList[2])
           # print(currentLine[1],'%6f'% timeMark, currentLine[9])
            postText = dmShooter.postDm('%6f'% timeMark, currentLine[9])
            print(postText)
        else:
            continue

"""