---
title: Windows语音识别转文字
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247488029&idx=1&sn=57497e714e9e6f353f2f8e781bff9108&chksm=fab2d122cdc558348f2b2fe98c622247ddc543731ed04b8d5b13022f4d5441df9d0a5984b396&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2025-03-02
fetch_date: 2025-10-06T21:57:26.893875
---

# Windows语音识别转文字

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPMO2ngic7aAHhyf7Nzpia3icKc7whgBVb9jIDyFjPydQWnoiceCzX3PMH86ARic1RnWib2c4zvHS23kmqUQ/0?wx_fmt=jpeg)

# Windows语音识别转文字

原创

沈沉舟

青衣十三楼飞花堂

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPMO2ngic7aAHhyf7Nzpia3icKcw3S2ptBW5aDyDz7O1qrUcnNXdU72jic5GEibiaa0JnhL9WQuia2icXSzLJg/640?wx_fmt=png&from=appmsg)

☆ 背景介绍

有时会在别人说点啥时用录音笔、手机APP等录制音频，事后导出音频文件，重新播放内容，手工整理文字。记者采访，肯定有这需求。需求量大的群体，肯定有TA们专业解决方案。

普通人生活中遇上此需求的不多，但也不是绝对没有。女科学家觉得我特能扯淡，好几次在我正满嘴跑火车之际说：“停，等我录一下…(掏手机)…你接着说…”。她这手机录音导出来是m4a后缀，当时来不及找现成的语音识别转文字工具，她就倍速听录音，根据关键字手工摘录要点。

若录音不涉及隐私，有很多云端解决方案，剪映好像就是云端方案。干网络安全这行，无法接受隐私数据上云。我不是搞媒体的，也不会AI相关编程，需要一个小白式傻瓜化工具，本地离线使用。

还真有，github上的Buzz，是对OpenAI Whisper的离线封装版，缓存相应模型文件后，使用时不要求必须联网；T14笔记本也能跑。

☆ Buzz

```
https://github.com/chidiwilliams/buzz
```

OpenAI Whisper是通用语音识别引擎，自己布署使用Whisper，对普通用户有难度。Buzz对之进行离线封装，提供Windows版安装包，简化布署与使用过程。

1) 安装

下载Buzz-1.2.0-windows.exe，有1.51GB。安装目录在

```
C:\Program Files (x86)\Buzz\
```

占用空间5.03GB。Buzz是Python开发的，安装目录下\_internal子目录有Python 3.11解释引擎。

2) 最简用法

```
set http_proxy=socks5h://<ip>:<port>
set https_proxy=socks5h://<ip>:<port>
"C:\Program Files (x86)\Buzz\Buzz.exe"
```

设代理是防止GFW干扰模型文件的下载过程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPMO2ngic7aAHhyf7Nzpia3icKcEgF6K6q6ia5iaDmPet6HfVQ4WpUMvRoFc5VyIVZEEywhRNjbdvX7hQdg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPMO2ngic7aAHhyf7Nzpia3icKcl7WcGeKrltibqgUGpACE0ozicgeeryvLXqLB773nddgdnyOoicW914tJA/640?wx_fmt=png&from=appmsg)

"Import File"本来有快捷键Ctrl-O，但Windows中实测不灵，BUG。语音识别结束时会在some.m4a所在目录生成相应的txt、srt文件；文件名有模板，可修改。

初次测试Buzz推荐用"Whisper+Small"。使用某些模型时会崩溃，那就换个模型重试。

2.1) 测试数据

some.m4a大概5m26s，是段两人之间日常对话。各种模型耗时如下:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPMO2ngic7aAHhyf7Nzpia3icKcaiccMY4W4o8JLTcf0LrxQEjgibpRszBwGsv0ia2K8neOU2VD4iapaI9r5A/640?wx_fmt=png&from=appmsg)

这种事不能简单看耗时，还得看语音识别效果，上面只是记录耗时参照系。

我觉得"Whisper+Small"、"Whisper+Large-V3-Turbo"够用了。

☆ Win10/11自带语音听写功能 (不推荐)

```
VB-CABLE Virtual Audio Device
https://vb-audio.com/Cable/
```

非LTSB版Win10/11自带语音听写功能，能识别来自麦克风的音频输入，并自动转成文字输出到某种文本域中，比如打开的记事本。但我们想要的场景是，一边播放音频，一边根据前者自动听写到文本域中；音频输入不用麦克风，而是来自播放器的音频输出。这种需求一般可用第三方软件配合解决，目前没有原生解决方案。

安装虚拟音频设备VB-CABLE，它同时提供虚拟的CABLE Output与CABLE Input设备，所有来自CABLE Input的音频流直接转发到CABLE Output，有点像内录线。稳妥起见，安装结束后重启OS。

实测将输入设备设为"立体声混音"，并不适用此场景，必须装VB-CABLE。

参照下图调整音频相关设置:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPMO2ngic7aAHhyf7Nzpia3icKcmht6dYK7icBVaREKm68PMIXEQDftIXxcXO2BXuCC6vSWHZUxBaRxP7A/640?wx_fmt=png&from=appmsg)

假设需要播放中文音频，在桌面右下角托盘区将输入法调成某种中文输入法，比如微软五笔、微软拼音什么的，都可以，不要调成ENG美式键盘；但中文输入法本身可停留在英文输入状态，这个无所谓。若托盘区是ENG美式键盘，将来听写中文音频时各种幺蛾子。

Win+H呼叫自带语音听写功能，会在屏幕正上方出现提示横幅，其左侧有个麦克风图标，点击它，可启用或停止听写功能。通过麦克风色调变化，可看出启用、停止状态。

打开记事本或其他文本处理软件，播放音频，启用听写功能。正上方横幅有一些提示信息，比如正在初始化、正在聆听等等。鼠标焦点要放在记事本中，一切正常的话，慢慢地其中就会出现与所播放音频对应的文字，即自动听写。

听写时勿将焦点从记事本移开，这算是大限制。我用虚拟机规避，这样Guest中不失焦，Host中随便干啥。

Win10的语音听写能力很一般，并不推荐；据说Win11好一些，未实测。

(完整版本看TXT)

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