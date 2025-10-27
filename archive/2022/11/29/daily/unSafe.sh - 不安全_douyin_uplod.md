---
title: douyin_uplod
url: https://buaq.net/go-137604.html
source: unSafe.sh - 不安全
date: 2022-11-29
fetch_date: 2025-10-03T23:57:08.717234
---

# douyin_uplod

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

douyin\_uplod

从0自动生成发布视频，解决你不知道发什么视频的烦恼。demo的实例是每天5点20分，单号生成并发送舔狗日记，双号生成并发送心灵鸡汤。你们可以根据自己的需求修改下。示例
*2022-11-28 18:51:29
Author: [github.com(查看原文)](/jump-137604.htm)
阅读量:36
收藏*

---

* 从0自动生成发布视频，解决你不知道发什么视频的烦恼。
* demo的实例是每天5点20分，单号生成并发送舔狗日记，双号生成并发送心灵鸡汤。你们可以根据自己的需求修改下。
* 示例[抖音号](https://v.douyin.com/rA1gERo/)

1. 使用apscheduler开启计划任务，每天x点x分运行
2. 通过自定义的文字以及背景音乐合成音频【使用了微软语音合成】
3. 通过音频和临时视频片段合成视频【使用了ffmpeg】
4. 通过playwright发布合成的视频

* python
* playwright
* ffmpeg
* apscheduler

* 微软[azure注册](https://azure.microsoft.com/zh-cn/products/cognitive-services/text-to-speech/)
* 没有海外卡的同学，淘宝搜索`微软azure注册`
* 准备至少2个临时视频片段，最好可以循环重复的静音视频
* 安装python
* 安装playwright、ffmpeg、apscheduler，执行以下命令
* 下载[ffmpeg](https://ffmpeg.org/download.html)

```
pip install apscheduler
pip install ffmpy
pip install playwright
python -m playwright install
```

* 然后通过playwright把cookie文件保存下来，执行以下命令，扫码登录完成后即可

```
playwright codegen www.douyin.com --save-storage=cookie.json
```

* ffmpeg需要添加到环境变量，如不添加需要修改`ffmpeg.exe`目录`ctrl+左键点击ffmpeg`进入，把`executable='ffmpeg.exe'`修改成你`下载ffmpeg`的目录

```
def __init__(
        self, executable=r'E:\ffmpeg\ffmpeg-5.0.1-essentials_build\bin\ffmpeg.exe', global_options=None, inputs=None, outputs=None
    )
```

* qq交流群：916790180
* 本源码只是出于学习交流的目的，非法使用发送不良视频等与作者无关

文章来源: https://github.com/y35uishere/douyin\_uplod
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)