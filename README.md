# biliDmShooter
字幕君有福了，从此告别暂停发歌词弹幕。只需要输入b站视频网址，页面cookie，以及ass字幕文件名，即可自动发动弹幕到b站指定视频

# dependence
python 3.4.2，以及 python requests库

# 使用方法
1，把歌词ass文件存放到biliDmShooter.py同一路径下(这里我准备了Vsinger2017演唱会的ass文件)
2，命令行下，执行“python D:\python\biliDmShooter\biliDmShooter.py”
3，按照提醒输入视频的链接，例如
“https://www.bilibili.com/video/av12802603/”
“https://www.bilibili.com/video/av6002357/index_2.html”
(目前只支持普通视频，拜年祭，活动视频暂时不支持)

4，(额，这一步稍复杂，确保你是登录的)1在上一步链接所在的网页，进入浏览器-->工具-->开发者工具页面
                                2在网页播放器中发射一条弹幕
                                3在下面的开发者工具中，在左侧找到名为dmpost?=cid=*****的请求名，在右侧Headers中找到Request Headers中的字段，一般都是“UM_distinctid=”开头的一大坨字符串，复制从“UM_distinctid=”开始的整个字段
                                4这段cookie复制到程序中

5，输入文件夹中的字幕名，例如这里输入VSinger_2017.ass
6，按下回车，然后泡杯茶睡觉打游戏，脚本将自动把你的字幕发送到视频中(5~6秒一发)

 



