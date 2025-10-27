---
title: 语音识别之CapsWriter-Offline
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247488038&idx=1&sn=480b88fe17c90325cd85a475f523bc3a&chksm=fab2d119cdc5580f45c0ba010c14d7584e3dd0eac87da3559543e0bdca4c94df80d328b9e349&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2025-03-03
fetch_date: 2025-10-06T21:56:36.634848
---

# 语音识别之CapsWriter-Offline

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPOo0mJ3ZDWpW4zofsy7TjdSqdozG7HyicORqJ3Iyd2hUVy9kGsFcqHzSoIIt7CWD19tcT7jTtBdPyg/0?wx_fmt=jpeg)

# 语音识别之CapsWriter-Offline

原创

沈沉舟

青衣十三楼飞花堂

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOo0mJ3ZDWpW4zofsy7TjdSibay7ib7gwUEwUvjudf66SyGrSdaa9Fh9iaxsicRubvvbStsTySeDtqhUw/640?wx_fmt=png&from=appmsg)

☆ CapsWriter-Offline

```
https://github.com/HaujetZhao/CapsWriter-Offline
```

网友在公众号上一篇的评论区提到CapsWriter-Offline，中英文识别快速、准确，资源占用低，完全离线使用，有效保护隐私。我试了，很强大，快速、准确、省资源，以后就用它了，推荐。缺点是，不太适合特别小白的用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPOo0mJ3ZDWpW4zofsy7TjdSEMZc6PEQGV8vI233U4icRmT0tYg0XGZE9VsLWIYsWmzPwA4O6DmrNqQ/640?wx_fmt=jpeg&from=appmsg)

1) 下载

假设是Win10/11，从github releases下载如下文件:

```
CapsWriter-Offline-Windows-64bit.zip
models.zip
```

这就是全部，合起来大概1.16GB，比Buzz小太多。GFW对github的干扰有些迷，大多数时候不挂线路直接可达，下载飞快；偶有干扰时，过会儿再试，比挂线路快。

2) 部署

假设将CapsWriter-Offline-Windows-64bit.zip展开到

```
X:\Green\CapsWriter-Offline\
```

将models.zip展开到

```
X:\Green\CapsWriter-Offline\models\
```

部署就这么简单。

3) 修改config.py

根据个人喜好做些修改

X:\Green\CapsWriter-Offline\config.py

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOo0mJ3ZDWpW4zofsy7TjdSb0pROYMedn3XanruvzFkhIPKnengtfNvl85Iu6xJnhvZ5IjbYgzamw/640?wx_fmt=png&from=appmsg)

config.py中有许多参数，比如start\_server.exe侦听、start\_client.exe连接的IP与端口，语音识别保存文本时是否同步保存音频文件，是否启用keyword.txt，等等。这些参数都有注释，解释其基本含义。

上例hot\_kwd设为False，也可直接修改

```
X:\Green\CapsWriter-Offline\keywords.txt
```

缺省有三个关键词，用#号注释掉。

4) 启动服务端

双击start\_server.exe即可，也可在cmd中执行

```
start "" X:\Green\CapsWriter-Offline\start_server.exe
```

耐心等待服务端启动完成，有提示，比如:

```
模块加载完成
语音模型载入完成
标点模型载入完成
模型加载耗时 61.79s
开始服务
```

5) 启动客户端

待服务端启动完成后再启动客户端，双击start\_client.exe即可，也可在cmd中执行

```
start "" X:\Green\CapsWriter-Offline\start_client.exe
```

若提示"连接成功"，即可使用客户端。

6) 录音并语音识别

假设焦点位于start\_client.exe

缺省长按CapsLock键启用录音，提示"开始录音"，要求输入设备是麦克风。长按CapsLock的同时，正常说话，中英混杂无所谓。

松开CapsLock键停止录音并完成语音识别；该热键可通过config.py中shortcut参数修改，但小白不大可能正确指定其他按键。start\_client.exe"识别结果"行会显示文字。

只有客户端启动的情况下，上述热键才可用，单启动服务端不行。

6.1) paste = True

缺省config.py中有个参数

```
paste = True
```

其效果是，停止录音并完成语音识别时，将文字先写入剪贴板，再模拟Ctrl-V。

长按CapsLock是全局热键，焦点离开start\_client.exe时热键仍生效。假设焦点在记事本之类的文本处理软件中时长按CapsLock开始录音；之后松开CapsLock停止录音，记事本中会自动粘贴语音识别所得文字。这种类似于Win10/11的"Win+H"功能，但准确、高效得多。

6.2) save\_audio = True

除了剪贴板中文字，若config.py中save\_audio为True，则有其他文件对应语音识别结果。

比如录音时，我说，我就试试你能不能保存音频，然后得到如下目录与文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOo0mJ3ZDWpW4zofsy7TjdSLmZYCuRkqf6ycTAUS5Y4WfOyL7QnqkhsrNPiaQ6WPvczA2EmL4lAFicA/640?wx_fmt=png&from=appmsg)

今天是2025年3月2日，如下文件是语音识别的文字版

```
X:\Green\CapsWriter-Offline\2025\03\02.md
```

如下文件是录音音频

```
X:\Green\CapsWriter-Offline\2025\03\assets\(20250302-185611)我就试试你能不能保存音频.mp3
```

mp3的文件名受config.py中audio\_name\_len参数影响，缺省为20，取语音识别结果的前多少个字置于mp3文件名中。

save\_audio为False时，不会生成2025目录，没有上述文件。

7) 从音频文件到文本文件

假设有some.m4a或其他格式音视频文件，将之拖放到start\_client.exe上，会自动启动客户端对some.m4a进行语音识别，输出相应结果。比"Buzz Whisper Small"快多了。

假设输入是

```
X:\path\some.m4a
```

则输出是

```
X:\path\some.json
X:\path\some.merge.txt
X:\path\some.srt
X:\path\some.txt
```

两个txt是纯文字版，格式有差别，srt带时间戳，自己打开一看就明白。json的用途后面再说。

也可命令行操作

```
X:\Green\CapsWriter-Offline\start_client.exe X:\path\some.m4a
```

需指定some.m4a绝对路径

7.1) 修正语音识别结果

假设手工修正some.txt，将之拖放到start\_client.exe上，会自动根据some.txt找到some.json，二者结合，同步修正some.srt。

也可命令行操作

```
X:\Green\CapsWriter-Offline\start_client.exe X:\path\some.txt
```

此功能只根据txt修正srt，不同步修正merge.txt。好像有点鸡肋，srt也是文本文件，可直接手工修正srt，不需要先txt再srt。

8) 热词

有三个热词表

```
X:\Green\CapsWriter-Offline\

hot-en.txt
hot-zh.txt
hot-rule.txt
```

热词的作用是，识别到相应发音，按热词表中内容进行规范化输出，比如WiFi、IP的大小写，听到赫兹时固定输出Hz，等等。

config.py中有参数决定是否启动这些热词表、是否区分声调，一般不需要改。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过