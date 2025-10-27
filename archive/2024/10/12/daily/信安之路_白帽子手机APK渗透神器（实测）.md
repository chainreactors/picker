---
title: 白帽子手机APK渗透神器（实测）
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247499572&idx=1&sn=43143b099d2f087c89f67f1119add3c4&chksm=ec1dcf1cdb6a460ac37d43a36a67fb1997f7e4f74503a60df7767a2db2d8149b539f56ddd83c&scene=58&subscene=0#rd
source: 信安之路
date: 2024-10-12
fetch_date: 2025-10-06T18:53:13.400814
---

# 白帽子手机APK渗透神器（实测）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jZhT1UzHfaTTia6mHmgqqDNY7FuQrO9reGtv0xx7XnibB4Q75xu897diayOzF9rBKYUSftqxweGVdM4VYInmnQPgA/0?wx_fmt=jpeg)

# 白帽子手机APK渗透神器（实测）

呆猫

信安之路

**“** 对于不熟悉手机APK反编译的白帽子，还有熟悉但就是懒得去反编译的各种帽子，我觉得摸瓜应该能满足你了。想要APK里的域名、URL接口信息都有，通用的加壳、插件信息也都有，想要的Word版报告也有。**”**

话说，第一次听到摸瓜应该是两年前了，当时觉得就是用开源框架搭的，没什么特别，网站还动不动就挂了。

今天突然一个00后小兄弟居然跟我提起来了，说用的人很多，我当时一愣，啊这个网站还活着。。瞬间激起了我这个老年人的求知欲望。

说实话，测试了一下还是挺佩服网站管理员的。APK在线反编译是个耗计算资源和存储的苦力活，能把网站坚持做这么久，技术改进了不少，有几个点超出了我的预期，运营模式也摸索出来点了，精神还是值得佩服。

01

—

APK分析

* **官方给的能力**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jZhT1UzHfaTTia6mHmgqqDNY7FuQrO9rekicVjxxzQITGTdp5eibdjiaiaTJZWcmyhN3mBDVPelZaepN3nm2mNduictQ/640?wx_fmt=png&from=appmsg)

* **实测结果**

实测了一下，分析速度1-3分钟，貌似有好几个分析引擎，藏在各种生僻的java文件、so库、静态文件里的域名和后台接口基本都能提出来，常见的加壳类型和插件也都有。

感觉不止静态分析，可能还用了沙箱。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jZhT1UzHfaTTia6mHmgqqDNY7FuQrO9reJKjASkrelGmmyMaDXgx5kZSAPiaxv7lGU9E9ITSO4ibNj9hkBjMTUiaxA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jZhT1UzHfaTTia6mHmgqqDNY7FuQrO9reL3vmnIFWZnYenGGyYK6q7H0eSYnicd0jZMWZXmeV9es67GM5zn99n3A/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jZhT1UzHfaTTia6mHmgqqDNY7FuQrO9reTvqzKIBNJNAOWJQUpZjfYCdonvPQvic7ZGYzgHpSLiaFsyJFTALDVA3A/640?wx_fmt=png&from=appmsg)

02

—

APK搜索

目测网站每天的APK上传量几百个，看网上有说总量到几十万个了，不好说。当然注册用户上传的咱也看不到。

搜索可以用它站内的搜库功能，我觉得搜包名和文件名比较有意思，能发现一些意想不到的。当然也可以使用Google、Bing搜，具体怎么搜就不说了。

* **站内搜索**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jZhT1UzHfaTTia6mHmgqqDNY7FuQrO9reSxYFiaINl23kZG1aRvHYegmB6OURH5RE4eu4HPoF9cgZSotAKMb2u1g/640?wx_fmt=png&from=appmsg)

* **外网搜索**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jZhT1UzHfaTTia6mHmgqqDNY7FuQrO9re2qcCRIoQGzCKODAbvk0k2UmZBG721SaPqUn3ic8pZb0ibzrs5b1typlQ/640?wx_fmt=png&from=appmsg)

03

—

APK报告

要我说，这是网站最良心的地方，就是能给你导出来一个有模有样的word报告，你可以随便拿来改，这对于白帽子来说，可真是救了命了。

要知道，宁可搞10个站，也绝对不会向一篇报告低头的，这个和年龄无关。

* **导出Word报告**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jZhT1UzHfaTTia6mHmgqqDNY7FuQrO9reVR5tKiamHSrLgF5PWYYquLubPibskckVkx6DpYfibibtgy1cOfh7pGOPIA/640?wx_fmt=png&from=appmsg)

写在最后，网站其他的一些功能没列出来，可以自行测测。好的东西还是值得大家多传播、点赞的。

贴上摸瓜的网址：**https://mogua.co**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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