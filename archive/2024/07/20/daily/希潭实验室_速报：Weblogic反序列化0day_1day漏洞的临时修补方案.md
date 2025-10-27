---
title: 速报：Weblogic反序列化0day/1day漏洞的临时修补方案
url: https://mp.weixin.qq.com/s?__biz=MzkzMjI1NjI3Ng==&mid=2247486840&idx=1&sn=be8331018c1a11e0bf21444b2365e557&chksm=c25fc203f5284b157bd91c21145a2fe23c3c456d1e42ecacd468e4839c1c0dbad1c202412f8d&scene=58&subscene=0#rd
source: 希潭实验室
date: 2024-07-20
fetch_date: 2025-10-06T17:44:12.062262
---

# 速报：Weblogic反序列化0day/1day漏洞的临时修补方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450AJmeo5U5SYiaKBJXQHcfpkjCMCsYRtfwG18pBMElXn0mZO0ps8k7wXSCVHWaLKQzWdEuRZFSZSceQ/0?wx_fmt=jpeg)

# 速报：Weblogic反序列化0day/1day漏洞的临时修补方案

原创

abc123info

希潭实验室

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

##

## **Part1 前言**

**大家好，我是ABC\_123**。一年一度的大考就要开始了，坊间传闻weblogic中间件爆出了0day或者1day漏洞，这里ABC\_123给大家提供一个临时的漏洞修补方案。

## **Part2 研究过程**

最近几年的weblogic反序列化漏洞都与T3和IIOP协议相关，所以还是建议禁用T3和IIOP协议，但是网上很多禁用方法不对，ABC\_123给大家介绍一下正确操作方法。

* **禁用T3协议过程**

进入weblogic的后台之后，选择“安全”—“筛选器”，在“连接筛选器规则”输入

**weblogic.security.net.ConnectionFilterImpl**

连接筛选器规则中输入:

**127.0.0.1 \* \* allow t3 t3s**

**0.0.0.0/0 \* \* deny t3 t3s**

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AJmeo5U5SYiaKBJXQHcfpkjv7p0tKVpu3TRVU9decqW68wIQjyzDMbFWPtEBKTUqUR5nbfaichDo9Q/640?wx_fmt=png&from=appmsg)

最后重启weblogic项目。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AJmeo5U5SYiaKBJXQHcfpkjrCqhlRrI4ZrIglYyicO0F3hP49EOaod13dJsh6wC6AtQYU0ExzCrFjQ/640?wx_fmt=png&from=appmsg)

经过测试，10.x版本的weblogic禁用T3需要重启，否则不会生效；12.x版本不需要重启，点击“保存”即可立即生效。

* **禁用IIOP协议过程**

进入weblogic的后台之后，选择“base\_domain”—“环境”—“服务器”，然后在对应服务器设置中选择 “协议”—“IIOP” 选项卡，**取消 “启用IIOP” 前面的勾选**，然后重启weblogic项目。

##

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AJmeo5U5SYiaKBJXQHcfpkjg5Pbta2iaomE2MKxX4yflFib0RfO59wqLexgI2EKRrpH2HVSTMn94DGA/640?wx_fmt=png&from=appmsg)

经过ABC\_123测试，几乎所有版本的weblogic，彻底禁用IIOP协议需要重启，否则即使点击了“保存”，也不会生效。禁用T3、IIOP协议之后，红队工具检测如下，提示filter blocked Socket。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AJmeo5U5SYiaKBJXQHcfpkjCpkUeuTX6Oj3tjdeErlRW0prfGmRFWjJibcdyPIvxC7fAjKwjy7VgMg/640?wx_fmt=png&from=appmsg)

* ## **其它修复方法**

借助安全设备、防火墙策略屏蔽T3及IIOP协议；也可以在Weblogic前面放置一个Nginx，只对HTTP协议进行转发，对T3协议及IIOP协议不进行转发，但是这种方法只能杜绝外网攻击，无法杜绝内网横向中对于Weblogic反序列化漏洞的利用。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**公众号专注于网络安全技术，包括安全咨询、APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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