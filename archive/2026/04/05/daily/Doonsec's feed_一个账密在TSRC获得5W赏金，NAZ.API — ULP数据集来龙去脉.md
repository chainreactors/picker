---
title: 一个账密在TSRC获得5W赏金，NAZ.API — ULP数据集来龙去脉
url: https://mp.weixin.qq.com/s/N4lvdX460UMQLDxt5_eItQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:38:27.984603
---

# 一个账密在TSRC获得5W赏金，NAZ.API — ULP数据集来龙去脉

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8KeKfUH0uliaO7knUv7TbOG6kwVPiblHOwK1pcib4ZtgOBXyLgibEaecuRcRzHR7KrlpsuxYmKhfdDbiaVt8ZcOukrGkWZkhGsoBsEd1LW0fPtCs/0?wx_fmt=jpeg)

# 一个账密在TSRC获得5W赏金，NAZ.API — ULP数据集来龙去脉

AI安全工坊

![]()

在小说阅读器中沉浸阅读

编者荐语：

潜藏在大众视角下的攻防打法，提的人不多可以借鉴学习一下，做甲方的朋友可以做个威胁风控，目前全球网络还持续存在这样的泄露。

以下文章来源于增长Hack Alice
，作者Alice007

![](http://wx.qlogo.cn/mmhead/LTpwfH82rickKWM8ldPlseDVQ5ynY8EkU68hYPnkUSUTArqBdIwMN1iaiaI486atpXwJ6q0uCzkfibo/0)

**增长Hack Alice**
.

从黑客到增长黑客，研究利用技术变现的流量玩法。关注我，发现更多技术变现的流量玩法。

## 一个账密在 TSRC 获得 5W 赏金，NAZ.API — U L P 数据集来龙去脉

### 一、 前言

直接上图，不吹牛逼。

![](https://mmbiz.qpic.cn/mmbiz_png/8KeKfUH0uljELAqkXKzMdZYFyAJIF0qDOOGiaeSxs9s9aavHruYUoadib5LJ1rzZvCwPS5y2gvQaIaribZkoHew2gDH50RMK4v2HWqzc17B4gA/640?wx_fmt=png&from=appmsg)

漏洞奖励+现金奖励，这个漏洞仅仅只是登录了一个账号密码而已。

![](https://mmbiz.qpic.cn/mmbiz_png/8KeKfUH0ulia93VqOrU1B8vz0F76hLq9b8aXAicPEuPyes1ic5yNqWdm2Azug5xhc0LQ6vuLJqK1iaEWVVZNicuAl3HDoba5tYzLCdYSXKHJJicoU/640?wx_fmt=png&from=appmsg)

那段时间，每天就是看着群里几位黑阔嘎嘎狗叫，又登进这，又登进去那。粗略的统计下，哥几个单单这种密码登录，提交SRC的漏洞收益就有6位数。做到这个收益一点都不难，仅仅只是早发现，早提交而已。本篇文章就讲述下怎么发现这份数据集，以及延伸的一些搞钱玩法。

### 二、 数据来源

我应该算国内第一批发现这些数据集的人了，因为我和朋友去SRC各种提交漏洞的时候，各家审核都是蒙的，一直追问账号密码咋来的。当时2-3个月内提交的漏洞一个重复的都没有，几乎各大SRC都没有幸免，被薅了个遍。以至于后面都知道很多审核也在通过这种思路提别家SRC的漏洞。

有兴趣的可以看看这篇老外的文章：
https://www.troyhunt.com/inside-the-massive-naz-api-credential-stuffing-list/

当时我还在甲方工作，期间做了很多数据防泄露和威胁情报相关的工作。偶然一次在逛黑客论坛时候，发现了一篇引流贴。说发现了一个百亿级的数据库，可以在线查询。

![](https://mmbiz.qpic.cn/mmbiz_png/8KeKfUH0uliaZMEoTLKkf3UHaDNMia9TwAAHwbiatCYbPBQfbxyicUvzNUrMSYJtcgtK1icVTIqdpbe06X0VGmL0AnVv2pKNS3s9xGJnYjFsJ42Q/640?wx_fmt=png&from=appmsg)

地址：
https://search.illicit.services/

![](https://mmbiz.qpic.cn/mmbiz_png/8KeKfUH0ulj8h66ibrJqzEdlbrJiaB4qhsib0rFv8riac7nRYV3EqXwLu37qImvSpj6XGfyear3IJXFCob595Yia4ZU26zNjYXmaomIpuqiccRKibw/640?wx_fmt=png&from=appmsg)

他可以根据 First Name, Last Name, Email, Username, Password, Domain 进行查询。于是我查了下公司的域名，花了十几 U 买了结果。

发现大多数账密来源都是来自于这个 `naz.api` 的组，并且大多数账号密码都可以登录。完全没有修改。实效性非常强。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8KeKfUH0ulhNqWcbndoV8hxfC4RPt4ThicL44Y6lhtbDHfSXxR1D1ymhiaVvic9LbVbCglWcaLcSjHjOfr4qXQflgHbBtmvntmvFtoKYGRNrcs/640?wx_fmt=png&from=appmsg)

但没用几天，刚把公司资产排查完。这个站就关了，作者说有人用它做坏事。

具体自行看✈，作者直接就把这套大数据查询的代码开源出来了，说你们要玩自己搭。
https://t.me/illsvc

https://github.com/MiyakoYakota/search.0t.rocks

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8KeKfUH0ulhmrt9R2c9xxeWibHCiaYqcSoKgImeqnKSVJgGMEZMYObZSIAia2hxW7nyEggNI1mDK7ZibvEOOEnAb6CQKQCEiaqlE1rrxfl9CBhiaY/640?wx_fmt=png&from=appmsg)

他关了以后，我就到处找这个 NAZ.API 的数据集，因为我知道，找到它就等于找到钱。

皇天不负有心人。终于有一天被我在 Breach Forums 里找到了，就是那个被 FBI 端了的论坛。我用了 8 积分，30块，买了它。然后就和几位“国际黑阔”开始了 SRC 捡钱之旅。很多系统，常规信息收集方法，一点找到的可能性都没有。（纯无特征的IP）账密登进去之后，直接乱杀。

逆推过来，就发现：**挖洞的本质还是信息收集+账号权限。剩下的部分真的是放两把米在键盘上，鸡都能啄两注入出来。**

### 三、 玩法分享

1. **内网账号 + Host碰撞：**

   很多甲方内部都没有做过全量的 Host 碰撞测试，或者业务上下线流程不规范。把内网域名账号密码提出来，再把该公司的公网 IP 全部收集下来进行碰撞。当场就进内网核心系统了。
2. **HVV项目：**

   通过收集供应商的系统账号密码。Get Shell后下源码，再回去打靶标。
3. **特定系统打击：**

   搜索 URL 路径，找某些特定的系统/组件，直接打一片。
4. **横向扩展：**

   通过搜索同样的密码，发现其他账号。
5. **内网无感渗透：**

   进内网后，直接登内网核心系统，全程无感信息收集。
6. **黑产变现案例 1：**

   某俄罗斯黑客团队通过撞库某个带信用卡信息的网站，一个月内赚了25W 刀。
7. **黑产变现案例 2：**

   FJ佬撞库某支付网站，用别人的账号来做跑分。
8. **黑产变现案例 3：**

   数据在tg上卖，国外正规的公司也收集这类信息做成saas服务，一年卖几千欧。
9. WordPress 变现：

   自动化撞库后台 + 自动化插入 JS 窃取信用卡代码（一张18-25刀）。那B黑客一个月卖了11w刀的卡。
10. **上下游扩展：**

    例如我登了某些安全公司的 XX 账号。一堆没公布的 0day POC。
11. **高价值资产：**

    服务商（域名/服务器/机房）、API、虚拟卡、代理、广告账户等等，都是钱啊！！！

很多玩法和思路不能细说了，在公众号这个平台，只可意会，图都没法放太多。只恨当时自己还没开窍，没往流量变现这方面去思考，就知道盯个B SRC。回过头来看，啥也不是，其他跑通哪个方向不比提这点漏洞赚的多。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8RWa5pyic1Xob8V1UxQjOHLAx5qbkPJ2gibKpIQpRw4ogjL6jE9xIxc26o12ZRTBvPaLQNjxXDAO5g/0?wx_fmt=png)

AI安全工坊

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8RWa5pyic1Xob8V1UxQjOHLAx5qbkPJ2gibKpIQpRw4ogjL6jE9xIxc26o12ZRTBvPaLQNjxXDAO5g/0?wx_fmt=png)

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