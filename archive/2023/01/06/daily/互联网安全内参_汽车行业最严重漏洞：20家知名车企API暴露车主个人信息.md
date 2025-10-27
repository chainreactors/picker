---
title: 汽车行业最严重漏洞：20家知名车企API暴露车主个人信息
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507433&idx=2&sn=48d9a0f7de6244cd2971a24b1dc2e153&chksm=ebfa9ac9dc8d13df0d5ef10c5b9dd578bb67739a207c6b380d751a77288b3ff62468067a93f6&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-01-06
fetch_date: 2025-10-04T03:10:16.128523
---

# 汽车行业最严重漏洞：20家知名车企API暴露车主个人信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7uroibd0o10MLBicrZoMPzJErSbj9u43XqrUvnlc0CSgbPm69pM05hZERZdV4catibjXqnibQelLjLklQ/0?wx_fmt=jpeg)

# 汽车行业最严重漏洞：20家知名车企API暴露车主个人信息

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZrxppzOe1rWASVibEC6Fm1qSficxpKfQzEbcFRBRDibcRkvw9CHQRqXt3OzYwJvh3g6bgfAM24b1dGQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZrxppzOe1rWASVibEC6Fm1qPcFFWpJxckkicVjNYqrM9deg1cvgCGUFibSdK2xeX21SaxHl71j5xxPw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

近日安全研究人员Sam Curry披露了近20家知名汽车制造商在线服务中的API安全漏洞，这些漏洞可能允许黑客执行恶意活动，包括从解锁、启动、跟踪汽车到窃取客户个人信息。这可能是汽车行业迄今披露的影响最为广泛，也最为严重的安全漏洞。

受漏洞影响的知名品牌包括宝马、劳斯莱斯、梅赛德斯-奔驰、法拉利、保时捷、捷豹、路虎、福特、起亚、本田、英菲尼迪、日产、讴歌、现代、丰田和捷尼赛思。

这些漏洞还影响了汽车技术品牌Spireon和Reviver以及流媒体服务SiriusXM。

Sam Curry领导的一组研究人员此前在2022年11月曾首次披露现代、捷尼赛思、本田、讴歌、日产、因菲尼迪和SiriusXM存在此类API漏洞。

当时，Curry披露了黑客如何利用这些漏洞来解锁和启动汽车，但并未公布漏洞细节，在90天的漏洞披露静默期结束后，该团队发布了一篇详细介绍这些API漏洞的博客文章（链接在文末）。

Curry透露，存在漏洞的汽车厂商已修复该报告中提出的所有安全问题，因此现在黑客已经无法再利用这些漏洞。

**奔驰内部门户：从源代码到客户信息全暴露**

在宝马和奔驰公司的系统发现的API漏洞最为严重，两家企业内部网络SSO（单点登录）都存在漏洞，使攻击者能够访问其内部系统，分析师可以访问奔驰的多个私有GitHub实例、Mattermost上的内部聊天频道、服务器、Jenkins和AWS实例、连接到客户汽车的XENTRY系统等等，具体如下：

* 通过配置不当的SSO访问数百个任务关键型内部应用程序，包括...
* SSO后面的多个Github实例
* 公司范围内的内部聊天工具，攻击者能够加入几乎任何频道
* SonarQube、Jenkins、misc.build servers
* 用于管理AWS实例的内部云部署服务
* 车辆内部相关接口
* 在多个系统上远程执行代码
* 内存泄漏导致员工/客户PII泄露、帐户访问

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZrxppzOe1rWASVibEC6Fm1qibTpVHCjPOD6nb4fHicyZ5uyvFib4Cqb0Uia7x6lhTaZh7p8PFcXIPhdLA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**宝马、劳斯莱斯：经销商门户洞开**

对于宝马，研究人员可以访问其内部经销商门户，查询任何汽车的VINs，并检索包含敏感车主详细信息的销售文件。此外，研究者可以利用SSO漏洞以任何员工或经销商的身份登录，并访问仅供内部使用的应用程序。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZrxppzOe1rWASVibEC6Fm1qCcDDbkPKZ7lxkbWAuHjJYDStZXPw2ZveFibUVckkjyS9WvAibExtCt8w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

*在宝马门户网站访问车辆详细信息*

**知名车企车主个人信息暴露无遗**

利用其他API漏洞，研究人员可以访问起亚、本田、英菲尼迪、日产、讴歌、奔驰、现代、捷尼赛思、宝马、劳斯莱斯、法拉利、福特、保时捷和丰田汽车的所有者的PII（个人身份信息）。

对于超豪华汽车的车主，个人信息泄露尤其危险。研究者可以访问的豪华车主个人信息包括销售信息、汽车定位信息和客户地址等。

例如法拉利的漏洞让攻击者可以零交互接管任何法拉利车主个人账户。原因是法拉利在其CMS上的SSO实施暴露了后端API路由，并使得从JavaScript脚本中提取凭据成为可能。

攻击者可利用这些漏洞访问、修改或删除任何法拉利客户帐户，管理其车辆配置文件或将自己设置为车主。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZrxppzOe1rWASVibEC6Fm1qZn1oyy7vpH5WQWfAXC1NgMovUZb8EjTZU53rctiahf3fHcTRrcoASPw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**黑客可实时跟踪车辆**

披露的漏洞还可能允许黑客实时跟踪汽车，引入潜在的物理风险并威胁数百万车主的隐私。

例如，保时捷的远程信息处理系统存在漏洞，使攻击者能够检索车辆位置并发送命令。

GPS跟踪解决方案Spireon也容易受到汽车位置泄露的影响，殃及使用其服务的1550万辆汽车，攻击者甚至可以完全管理访问其远程管理面板，远程解锁汽车，启动发动机或禁用启动器。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZrxppzOe1rWASVibEC6Fm1qWib2XzNeU3R4YWZccC25YbDiclMylXbDzhKn1MhrzN12lkeeBsDdia2nQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

第三个存在位置泄露问题的企业是Reviver，这是一家数字车牌制造商，容易受到未经身份验证的远程访问其管理面板的攻击，该面板可能使任何人都可以访问车辆的GPS数据和用户记录，甚至更改汽车的牌号信息。

攻击者可以在管理面板中将目标车辆标记为“被盗”，这将自动通知警方，使车主/司机面临不必要的麻烦和风险。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZrxppzOe1rWASVibEC6Fm1qicIEkqibIY6c7qUib0aPv0P7ibicjM0fTTIwHGvxrYL4eHfnBkArSGX4IWw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

*远程修改车牌号码*

**专家建议车主应尽量减少暴露个人信息**

车主可以通过最大限度减少存储在车辆或汽车APP中的个人信息来保护自己免受此类漏洞的影响。

将车载远程信息处理设置为最高私密等级，并阅读汽车厂家的隐私政策以了解其数据的使用方式也很重要。

安全专家还建议车主在购买二手车时，确保先前车主的帐户已被删除。如果可能的话，使用强密码并为汽车应用程序和服务的登录设置双因素身份验证。

参考链接：

*https://samcurry.net/web-hackers-vs-the-auto-industry/*

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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