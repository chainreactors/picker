---
title: 易笺 – TXT 小说阅读器[Web]
url: https://buaq.net/go-172699.html
source: unSafe.sh - 不安全
date: 2023-07-23
fetch_date: 2025-10-04T11:51:27.528538
---

# 易笺 – TXT 小说阅读器[Web]

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

![](https://8aqnet.cdn.bcebos.com/3e73f0d84c15628a94c2d37b300071be.jpg)

易笺 – TXT 小说阅读器[Web]

*2023-7-22 15:46:0
Author: [www.appinn.com(查看原文)](/jump-172699.htm)
阅读量:31
收藏*

---

![易笺 - TXT 小说阅读器[Web] 1](https://static1.appinn.com/images/202307/appinn-feature-images-2023-07-21t223327-227.jpg!o "易笺 - TXT 小说阅读器[Web] 1")

献上一个这两天自己写的一个非常简洁的网页，没有任何设置，纯粹是为了阅读。

好吧，原来想的是开发一款能看200MB+日志文件的阅读器，结果写着写着就成了看小说的了……

来自[**发现频道**](https://meta.appinn.net/c/faxian/10)，@henryxrl 同学的自荐：<https://meta.appinn.net/t/topic/45732>

![易笺 - TXT 小说阅读器[Web] 2](https://static1.appinn.com/images/202307/appinn-2023-07-21-22-36-092x.jpg!o "易笺 - TXT 小说阅读器[Web] 2")

## 为啥又双叒叕要开发一个txt阅读器？

1. 百兆文件秒开（毕竟原本就是为了看日志的），支持自动识别文件编码（我在国外系统是英文，打开中文小说简直是痛苦）
2. 中英文小说名、作者名自动识别
   * 《书名》作者：作者名.txt
   * Bookname by author.txt
3. 标题正则自动识别 —— 自信的说，标题抓取几乎很少有超过易笺的了，看官们可以自行和别的阅读器对比
4. 支持自动抓取小说中的脚注（下方有视频演示，支持的脚注格式可以参考我修改的《逍遥游》[百度网盘｜提取码: qehd 1](https://pan.baidu.com/s/1p8WAzB8dMWW7WH6Acf3Ulw?pwd=qehd)）
5. 支持英文小说以及英文标题抓取
6. 界面语言随着拖进来的文件而改变（中英自动切换，别的语言咱也不会……）
7. 自动去除文字中的一些广告，目前只对塞班和知轩藏书的小说进行了优化
8. 自动制作扉页，显示识别出的标题名和作者名，再戳上一个藏书章（中英文藏书章是不同的哦！藏书章纯粹是为了好玩儿，看官要是不喜欢我可以拿掉）
9. 颜值高，颜值高，颜值高（至少我自己觉得好看hhh）
10. **【之前忘记提了】每本txt都会自动储存阅读进度，精确到每一行！**

## 图文示例

1. 拖拽动画

2. 拖拽（或双击）打开文件。示例用的是55MB的《极品全能高手》——这是我能找到的最大的小说文件了，如果有更大的，欢迎提供。

3. 秒开后就是主界面啦！左侧目录栏，右侧正文，右侧底部有翻页按键。目录栏默认只现实当前位置的章节名，鼠标移动到目录栏上方后会显示完整的目录。

4. 小说脚注示例

5. 英文小说示例（每个章节第一个词的第一个字母自动下沉）

易笺一共用了三种字体，分别是：

1. 霞鹜文楷（免费商用， 内嵌）：UI，脚注，以及所有英文字体
2. 黄令东齐伋复刻体（免费商用，内嵌）：中文标题
3. 方正宋刻本秀楷\_GBK（个人使用免费，无法内嵌，需个人安装）：中文正文

强烈建议自行安装“方正宋刻本秀楷\_GBK”字体，因为真的很好看！一旦安装，易笺会自动识别。如果没有安装，中文正文会用霞鹜文楷代替。

## 获取

临时host在自己的服务器的一台虚拟机里，小水管，勿滥用，求别hack我～ 哪位大佬愿意帮忙host请联系我！！

* [https://txt.xrl.app](https://txt.xrl.app/)（直接用）
* [Github](https://github.com/henryxrl/SimpleTextReader)

---

文章来源: https://www.appinn.com/txt-xrl-app/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)