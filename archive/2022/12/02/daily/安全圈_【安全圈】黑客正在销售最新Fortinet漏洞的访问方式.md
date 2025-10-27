---
title: 【安全圈】黑客正在销售最新Fortinet漏洞的访问方式
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652026116&idx=4&sn=732180dc0d04439122b38983b1496ac7&chksm=f36f9944c418105244f8b19679a11b5c658f7f64a1c33db06c728bbd66676ba0e684838bb494&scene=58&subscene=0#rd
source: 安全圈
date: 2022-12-02
fetch_date: 2025-10-04T00:18:04.498456
---

# 【安全圈】黑客正在销售最新Fortinet漏洞的访问方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAByywNys94kaH5sqGyiaC9xibxnLGyCcHB8lRKcic6jpGypb7CmPrfUq9g/0?wx_fmt=jpeg)

# 【安全圈】黑客正在销售最新Fortinet漏洞的访问方式

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAib1svM50ppMoI1q5WiafHthfeLK5U1oZup9icyDPnia6MicatveFtibaG79g/640?wx_fmt=jpeg)

**关键词**

Fortinet

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAPGKTZpKv2j2CyQcBUQpeuS2j7qzKVrVrlFrnhJowY6r9hS04wjVY5A/640?wx_fmt=jpeg)

安全厂商发现，稍早发现的Fortinet网络设备软件漏洞已经有黑客公开销售访问的方法。

10月间Fortinet修补了零时差漏洞CVE-2022-40684，它是HTTP/HTTPS管理接口的验证绕过漏洞，可被远程滥用，风险值列为9.6，属于重大风险。这项漏洞影响多项产品，包括FortiOS、FortiProxy和FortiSwitchManager。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAnF2IgqMKic7ZRrgAOBkibvwz8icw6v2CWO7ib5SxA9sibjljSGqfs5v2PrQ/640?wx_fmt=jpeg)

Fortinet当时提醒用户应尽快更新，因为公开前已经遭到滥用。如今专门监控暗网上犯罪活动及漏洞情报的厂商Cyble发现，俄罗斯地下网络论坛上，已经有人公开发布消息，以销售访问Fortinet VPN设备的凭证资讯。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAMM0d6Q9h892mmicZ9OJgnJL1ibFyLp4GxPZb8hLnG475hrkkhibdRSyGg/640?wx_fmt=jpeg)

图片来源／Cyble

Cyble发现的是“多个”未授权FortiOS设备的访问资讯，包括网址、管理员用户的SSH Key。分析这些访问资讯显示，攻击者企图将公开密钥加入到受害企业管理员账号中，借此冒充管理员访问Fortinet设备。

根据资料，这些受害企业用的都是过时版本的FortiOS。研究人员相信，发布广告的攻击者应该是对CVE-2022-40684发动攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAFbMELfp9gSibiaqStVp3rPnGccfAjAJVNX8DddV4xZ9pH3x6tpJk3bDQ/640?wx_fmt=jpeg)

图片来源／Cyble

通过冒充Fortinet管理员，攻击者可修改管理SSH密钥、添加本机用户、修改网络配置变更流量路径、下载系统配置资讯、抓取封包截取其他敏感系统或网络资讯，再于暗网销售。

Cyble研究人员指出，针对Fortinet执行实例的攻击行动，从10月17日起就持续至今。这个时间点大约等同Fortinet第一波悄悄发通知用户更新软件的时间。

研究人员呼吁用户尽快安装修补程序，因为网络上已公开的概念验证（PoC）程序及自动化工具，让攻击者在漏洞公布几天之内就能发动攻击。

来源：十轮网

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAwL9kicakIzxHhgHqEjbLbmlHvu3Bpbic8LaLIhqpWUttB0Gqkk5MqzuA/640?wx_fmt=jpeg)

# [【安全圈】应对挑战！元宇宙可能成为 2023 年网络攻击的主要途径](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652025972&idx=1&sn=cfd884abb5e3cff179335b50d5ae4257&chksm=f36f9834c41811223cb03635656355deb905e0bbd1ffecd465c1d8c5c8c49f2ec0e3ac8983bd&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSA53Ze5jYAPN0ziapYZJrlnkd3NtbGlQESPXaP0hb9tPj148OViac0U1pQ/640?wx_fmt=jpeg)

# [【安全圈】以威胁国家安全为由，美国禁止销售中兴、海康威视等电信和监控设备](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652025972&idx=2&sn=de6f5b320d1bb645cf46765afd15e72d&chksm=f36f9834c41811227599b505a054256c6c54bd53a64ffe1640df99aa5e5f685b166cbc07d982&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAmXyvUCX17HIorpmFE0ooiabBbr2QmINq3lx2Ro3iaCKbb209AJUVgiaTw/640?wx_fmt=jpeg)

# [【安全圈】宏碁电脑存在驱动程序漏洞，启动过程中可部署恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652025972&idx=3&sn=78efb6a0d35bca6db75a1112c7b97976&chksm=f36f9834c4181122f57ef00f80ef6cfcfdf4687b239883c7e2a98f741b92bc78ec8108e3d1b5&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgU7AQyHMBto7BXAPaYHNSAVQb4juM2yhB7iaMu6skKY12c1WLqp2QYy1ZKibj008VHEkjSIWMSSYEg/640?wx_fmt=jpeg)

# [【安全圈】新攻击利用Windows安全绕过 0 day 漏洞投放恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652025972&idx=4&sn=d652e648e5bb3117ca53f7bf0aa96cb1&chksm=f36f9834c41811225ffaef84ae60e9f5b6e8d6752f864fa26a5717d7a745bdc621faadd67446&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

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