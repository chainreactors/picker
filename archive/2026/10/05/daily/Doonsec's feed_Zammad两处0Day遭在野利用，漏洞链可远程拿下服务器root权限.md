---
title: Zammad两处0Day遭在野利用，漏洞链可远程拿下服务器root权限
url: https://mp.weixin.qq.com/s/w4snj5AUdAivTBdf-dU1Kg
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:38.331778
---

# Zammad两处0Day遭在野利用，漏洞链可远程拿下服务器root权限

# Zammad两处0Day遭在野利用，漏洞链可远程拿下服务器root权限

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3kgNmOtD2a8MjJ8K1lEgx4foIV1UdhVCa3JOOFJS454SXkX0IQu0ESYBT1OQVJBicLV6jBRicXic4tLTHAuMI5do37DticWxhUWNM/640?wx_fmt=gif)

![Zammad 0Day漏洞遭在野利用，可远程执行代码获取root权限](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1f9FYNmaTQJic6RaNLJ1lsoPYByMqjKltibHrclAyzdkuERD533CyaDz5rSdtvqgoib8WDDSdvvGBNcGAqeLV9FJB6xnao4Lyu74/640?wx_fmt=jpeg)

Part01

Zammad两0Day细节披露

Zammad存在两个严重0Day漏洞，据报攻击者已利用其入侵荷兰漏洞披露研究所（DIVD）。这些漏洞可导致会话劫持，允许攻击者以Zammad服务用户身份执行远程命令，还可能进一步实现root权限提升。

两个漏洞分别编号为CVE-2026-102489和CVE-2026-102490。DIVD在调查自身环境遭遇的一起独立入侵事件时发现了相关问题，随后以DIVD-2026-00015为案例号发布了研究结果。

2026年9月21日，攻击者利用CVE-2026-102489入侵DIVD。这是一个会话劫持漏洞，影响Zammad 6.3.0至6.5.4版本，攻击者可借此以Zammad用户身份执行远程代码。DIVD指出，该漏洞同样存在于Zammad 7.0.0至7.1.3版本中，但受环境条件限制，攻击者无法在这些版本中完成利用。

第二个漏洞CVE-2026-102490属于本地权限提升漏洞，影响所有Zammad版本，覆盖从1.5.0到7.1.0-alpha的所有构建版本。如果攻击者已经获取本地zammad用户的访问权限，就可以利用该漏洞将权限提升至root级别，完全控制受影响的服务器。

Part02

漏洞组合形成完整攻击链

这两个漏洞可以组合成高危害攻击链。远程攻击者可先利用会话劫持漏洞，以Zammad服务账号身份执行命令，再借助本地提权漏洞获取root级访问权限。

一旦获取root权限，威胁行为者就能完全掌控服务器数据：既可以篡改工单内容、访问客户支持工单、窃取邮件附件，也能随意修改用户账号。攻击者还可以在服务器中植入持久化后门，为后续横向移动渗透企业内网铺路。

DIVD表示，研究人员在9月22日至23日完成了漏洞分析与复现，并于9月24日将所有发现同步给Zammad官方。

9月26日，DIVD开始扫描公网上可公开访问的Zammad实例，识别出存在漏洞的资产后逐一通知所有者。该机构同时发布了有限度的漏洞披露公告，称Zammad官方正在开发修复补丁。

![DIVD在DIVD-2026-00015调查中发现关联DIVD-2026-00014的Zammad漏洞](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX02HpSrSVaXN6RGWX7qpy0ZqA2uJeDEiaEwLKbmf9kqcU19Cs45hOQXfGBLpgIbOMHkN4x03quVYgIJkmyGoxQ8t1lmfgz5HK1c/640?wx_fmt=jpeg)

Part03

官方发布安全建议

运行Zammad的安全团队应当将这两个漏洞列为最高优先级的应急响应事件。DIVD建议用户升级到Zammad 7版本，或者在修复完成前将受影响实例下线。

但管理员需要注意，本地提权漏洞同样影响7.x版本，包括最新的alpha构建版本。

企业应当检查Zammad日志，排查是否存在可疑会话、异常管理员操作、非正常命令执行，以及Zammad账号相关的变更记录。DIVD已经发布了一款IOC日志检查脚本，帮助管理员识别潜在的入侵痕迹。

由于攻击者在漏洞公开披露前就已展开在野利用，仅安装补丁可能无法清除攻击者留下的持久化访问权限。如果企业检测到可疑活动，应第一时间隔离受影响服务器，轮换所有凭证与密钥，核查账号变更情况。同时还要检查系统计划任务与服务项，开展完整的取证调查。

参考来源：

Zammad 0-Day Vulnerabilities Exploited to Gain Remote Code Execution and Root Access

https://cybersecuritynews.com/zammad-0-day-vulnerabilities-exploited/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bRSnFgE3WPnpU3s0eVp7QdRn9fI63ymmlhTHpsMBL2VnRMPZQy9DhvZasynJV1ia534sF84uxxKKulzDlBibjrQ7ylDiaickrCIY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651347479&idx=1&sn=1cf9c858a30d0b7af06d196002bd2913&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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