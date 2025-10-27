---
title: 【安全圈】黑客利用第三方SaaS服务成功入侵美国财政部系统
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067069&idx=3&sn=bd0876c49c1d286c84408344ea9a8bc8&chksm=f36e78bdc419f1abc5a9eeea0d3b371b020c63cc85d3ee2cfe748cedf2bfd63ac4dad00f6412&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-02
fetch_date: 2025-10-06T20:09:15.643607
---

# 【安全圈】黑客利用第三方SaaS服务成功入侵美国财政部系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhu91q2gWUzXUMq6yvzz9lWziagqLukZvqZhfLiadTF1mufpWA0mOPR3bNAPKcrFoEpFCCrOibdYVbkQ/0?wx_fmt=jpeg)

# 【安全圈】黑客利用第三方SaaS服务成功入侵美国财政部系统

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

根据美国财政部本周一向国会议员发出的一封信，财政部透露，网络安全公司 BeyondTrust 于 12 月 8 日通知其发现一名黑客利用被盗的安全密钥成功入侵财政部系统。黑客通过远程访问权限控制了员工工作站并获取了其中的机密文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhu91q2gWUzXUMq6yvzz9lWL6LBr6ibrSDr2vK3cutXmichb6PAsiccOSeIWJrvXic06auIb0sZH9utAA/640?wx_fmt=jpeg&from=appmsg)

BeyondTrust 是一家专注于特权访问管理（PAM）和安全远程访问解决方案的网络安全公司，其 SaaS 产品被广泛应用于政府机构、科技企业、零售商、医疗机构、能源和公用事业提供商，以及银行业等领域。

财政部助理部长 Aditi Hardikar 在信中表示：“根据目前的调查结果，这起事件可归因于高级持续威胁（APT）行为者。”然而，财政部并未详细说明受影响的工作站数量或泄露文档的具体类型，也未明确攻击发生的具体时间。

财政部补充称，受感染的服务已被下线，目前没有迹象表明攻击者仍然能够访问财政部的信息资源。根据财政部政策，APT 行为导致的入侵被视为重大网络安全事件。

### **BeyondTrust的漏洞利用与财政部受影响情况**

本月早些时候，BeyondTrust遭遇黑客攻击，其远程支持 SaaS 平台的部分实例被入侵。黑客通过盗取的 API 密钥重置了本地应用程序帐户的密码，从而获得了系统的高级权限。

BeyondTrust在调查后确认了两个0day漏洞——CVE-2024-12356 和 CVE-2024-12686。这些漏洞使攻击者能够侵入并控制远程支持 SaaS 实例。由于财政部是受影响实例的用户之一，黑客得以通过该平台远程访问财政部的设备并窃取文档。

在发现违规行为后，BeyondTrust迅速采取措施，关闭了所有受影响的实例并撤销了被盗的 API 密钥。

### **政府协同应对措施**

目前，美国财政部正在与联邦调查局（FBI）和美国网络安全与基础设施安全局（CISA）合作，全面调查并解决此次入侵事件。财政部表示，将继续采取措施确保其系统的安全性，并防止类似事件再次发生。

***END***

阅读推荐

[【安全圈】日本航空公司遭网络攻击导致全球瘫痪](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=1&sn=3ae632fb4839dc14720917aa26fe469c&scene=21#wechat_redirect)

[【安全圈】Linux 系统岌岌可危：GStreamer 漏洞威胁数百万用户](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=2&sn=6bf70d067d0bebdf78e4045b13df4439&scene=21#wechat_redirect)

[【安全圈】严重漏洞使大量Four-Faith路由器面临远程利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=3&sn=852cf568ead351f59557241b2af12032&scene=21#wechat_redirect)

[【安全圈】老旧D-Link路由器成了僵尸网络的武器](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=4&sn=02e788cd1d37c6ecc9e6e4b8820b6a00&scene=21#wechat_redirect)

[【安全圈】大众集团80万电动汽车车主个人数据被泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=1&sn=6603384db2288a2926a144a8eac4bf06&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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