---
title: 【安全圈】知名开源监控系统Zabbix存在SQL 注入漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=1&sn=ac63bf158d1e3e33b69fbab49a5ae214&chksm=f36e7e19c419f70fbbf339ed9443f3c6144f86fd4c2767b6093fa54e3cdac6dd1a3c287d74d2&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-04
fetch_date: 2025-10-06T19:39:04.909579
---

# 【安全圈】知名开源监控系统Zabbix存在SQL 注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljNjbcFCaXKEbVibCkASomibX7blpzegQDkWfWUalwq2FgnialAmUC5tH0WIBjS2Qw6esfn2Gk5vSAuQ/0?wx_fmt=jpeg)

# 【安全圈】知名开源监控系统Zabbix存在SQL 注入漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

Zabbix 存在 SQL 注入漏洞（CVE-2024-42327），该漏洞是由于在 Zabbix前端的CUser类中的addRelatedObjects函数未对输入数据进行充分验证和转义，导致具有API访问权限的恶意用户可以通过user.get API传递特制输入触发SQL注入攻击，进而利用该漏洞实现权限提升或访问敏感数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljNjbcFCaXKEbVibCkASomibXTTdDI4rumBvMAvC7mNzPumFiaf15Niag56ljI7fmLIEJficicUWItYiaAcw/640?wx_fmt=jpeg&from=appmsg)

Zabbix是一个基于WEB界面的提供分布式系统监视以及网络监视功能的企业级开源监控解决方案，可以用来监控服务器、硬件、网络等。

该漏洞位于user.get API端点，任何具有API访问权限的非管理员用户均可利用，包括默认的“用户”角色。利用这一漏洞，攻击者可以通过操控特定的API调用，注入恶意SQL代码，从而获得未授权的访问和控制权限，进而完全控制Zabbix实例，导致敏感监控数据和连接系统的泄露。

Qualys公司对于该漏洞进行分析，指出利用这个漏洞可能允许攻击者提升权限并获得对易受攻击的Zabbix服务器的完全控制，且目前已经发现，有超过83000个暴露在互联网上的Zabbix服务器。

漏洞具体信息如下：

### 漏洞等级

高危

### 受影响版本

目前受影响的Zabbix版本：

6.0.0 <= Zabbix < 6.0.32rc1

6.4.0 <= Zabbix < 6.4.17rc1

Zabbix 7.0.0

### 修复方案

目前官方已发布新版本修复该漏洞，建议受影响用户升级到Zabbix 6.0.32rc1、Zabbix 6.4.17rc1、Zabbix 7.0.1rc1或更高版本。官网地址：https://www.zabbix.com/download

尽管关于CVE-2024-42327的咨询仅在上周发布，但包含该问题补丁的版本6.0.32rc1、6.4.17rc1和7.0.1rc1已于7月发布。这些修补版本还解决了另外一个漏洞，编号为CVE-2024-36466（CVSS评分为8.8）。该漏洞存在认证绕过问题，可能允许攻击者签署伪造的zbx\_session cookie并以管理员权限登录。

Zabbix版本7.0.1rc1还修复了CVE-2024-36462，这是一个不受控制的资源消耗漏洞，可能允许攻击者造成拒绝服务（DoS）状态。目前没有发现该漏洞被公开利用的情况，强烈建议用户尽快安全最新版本，以修复上述漏洞。

参考来源：https://www.securityweek.com/critical-vulnerability-found-in-zabbix-network-monitoring-tool/

***END***

阅读推荐

[【安全圈】知名科技公司员工举报公司高管系美国间谍？公司回应，疑点重重](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=1&sn=be6fcf97a8eeb2bc8145ab42b1be777c&scene=21#wechat_redirect)

[【安全圈】摄像头贴很有必要，黑客可不激活指示器而调用摄像头](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=2&sn=7f9d672677e1dcb0f7e67405da112ae9&scene=21#wechat_redirect)

[【安全圈】新型钓鱼工具包能让“菜鸟”轻松发动攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=3&sn=35d457660d9cc1755f262a4e5f6fe6b4&scene=21#wechat_redirect)

[【安全圈】损坏的Word钓鱼文件可以绕过微软安全防护？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=4&sn=4a3ea073cc936b52c057d059b24874a6&scene=21#wechat_redirect)

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

阅读原文

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