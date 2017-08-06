import requests
import random
import time
import re

class postDmData:
    def __init__(self):
        self.cookie = ''
        self.aid = ''
        self.cid = ''
        self.csrf = ''
        self.uid = ''
        pass

    def getVideoId(self,html):
        htmlList = html.split("\n")
        linenum = 0
        for lineItem in htmlList:
            if ('cid' in lineItem) and ('aid' in lineItem):
                linenum += 1
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
        self.cookie = webCookie

        pattenCsrfStr = r"bili_jct=(.+?);"
        findCsrfList =  re.findall(pattenCsrfStr, webCookie)

        pattenUidStr = r"DedeUserID=(.+?);"
        findUidList = re.findall(pattenUidStr, webCookie)

        if len(findCsrfList) != 0 and len(findUidList):
            self.csrf = findCsrfList[0]
            self.uid = findUidList[0]
            print("get uid = %s,and token = %s" % (self.uid, self.csrf))
            return True
        else:
            print("get user data fail")
            return False


class dmShooter:
    postLink = "https://interface.bilibili.com/dmpost?cid=21044350&aid=12802603&pid=1&ct=1"

    heads = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '176',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'UM_distinctid=123-12-23-23-23; pgv_pvi=; fts=123; sid=123; rpdid=123; buvid3=; _ga=8; tma=1.1; tmd=31.; _qddaz=QD.xek9q5; HTML5PlayerCRC32=56757; finger=54764576; uTZ=-76; LIVE_BUVID=46577; LIVE_BUVID__ckMd5=456; DedeUserID=123456; DedeUserID__ckMd5=233333;SESSDATA=123456;  bili_jct=123456; user_face=123456; pgv_si=123456; purl_token=123456; biliMzIsnew=1; biliMzTs=null; _cnt_pm=0; _cnt_notify=0; _dfcaptcha=123456',
        'Host': 'interface.bilibili.com',
        'Origin': 'https://www.bilibili.com',
        'Referer': 'https://www.bilibili.com',
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
        'date': '2017-08-01 20:48:56',
        'csrf': '9f179a962285670f35d1c2392aa2d330'
    }

    def __init__(self, postDmData):
        self.postDmData = postDmData
        self.session = requests.session()

    def postDm(self, videoTime, dmText):
        #get current time
        sendDate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        #set post Link
        self.postLink="https://interface.bilibili.com/dmpost?cid=%s&aid=%s&pid=1&ct=1"%(self.postDmData.cid,self.postDmData.aid)

        self.params['date'] = str(sendDate)
        self.params['playTime'] = videoTime
        self.params['message'] = dmText
        self.params['csrf'] = self.postDmData.csrf
        self.params['cid'] = self.postDmData.cid
        self.heads['Cookie'] = self.postDmData.cookie
        rndNum = random.randint(1501597969253783, 1501617969263783)
        self.params['rnd'] = str(rndNum)

        print (str(sendDate),videoTime,str(rndNum),dmText)
        jscontent = requests.session().post(self.postLink, headers=self.heads, data=self.params).text
        return jscontent


if __name__ == '__main__':

    dmData = postDmData()

    #input website
    #biliLink = "https://www.bilibili.com/video/av12802603/"
    biliLink = input("please input your bilibili video link:")

    htm = ""
    try:
        htm =requests.get(biliLink)
    except requests.exceptions.SSLError:
        print("exit because of SSL error")
        exit(1)
    except requests.exceptions.ConnectionError:
        print("exit because of network connectionError")
        exit(1)
    except requests.exceptions.MissingSchema:
        print("exit because of url entry error")
        exit(1)



    if(dmData.getVideoId(htm.text) == False):
        print("exit because of web page fault")
        exit(1)

    #input cookie
    webCookie = input("please input your cookie:")
    dmData.getCookie(webCookie)

    assFileNmae = input("please input your ass file name:" )

    dmShooter = dmShooter(dmData)

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