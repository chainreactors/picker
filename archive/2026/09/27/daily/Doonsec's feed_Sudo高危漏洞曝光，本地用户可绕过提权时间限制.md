---
title: Sudo高危漏洞曝光，本地用户可绕过提权时间限制
url: https://mp.weixin.qq.com/s/CS57XQOTfIm840aeoW8_OQ
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:54:08.497026
---

# Sudo高危漏洞曝光，本地用户可绕过提权时间限制

# Sudo高危漏洞曝光，本地用户可绕过提权时间限制

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX2SDiaYiaNnOJpwgP2GLtxRHytvY6hQ3A5sia01ZY4TL3YJ3bt1dCBhTic49CXFOYPnPvVeylBfBrZlic0bUbD06nBE05ib9yRz4jtMA/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX02JlnXR5icib6MM1KTVjduGMAcJJyawR8E3IZTHCofG15pDwJfLnia3AWdUxyXHbS0QfS7M3eNvfNt2f9Myh8KEGRJFQRVsAtuZk/640?wx_fmt=png)

Sudo存在一处高危安全漏洞，本地攻击者可利用该漏洞绕过基于时间的访问限制，以高权限执行命令。该漏洞编号为CVE-2026-96512，影响1.8.20至1.9.17p2版本的Sudo，根源是程序对TZ环境变量的处理机制存在缺陷。

Sudo是Linux平台广泛使用的权限管理工具，允许授权用户以其他用户身份（通常为root）执行命令。管理员可通过sudoers规则限制高权限命令的允许执行时段，这类规则支持NOTBEFORE和NOTAFTER条件，分别禁止用户在指定日期前、访问窗口过期后执行对应命令。

漏洞的触发逻辑在于，Sudo的parse\_gentime()函数处理未显式指定时区的时间戳时，会依赖mktime()函数和环境变量中的TZ值完成计算，未对该用户可控变量做安全隔离。由于Sudo是setuid-root程序，启动时会直接继承调用用户的环境变量，本地用户可在执行Sudo命令前，预先设置经过特殊构造的时区值。

如果用户设置极端的POSIX时区偏移值（例如TZ=XXX24），可让Sudo对授权时间的判断前后偏移约25小时。这种偏移会让已过期的NOTAFTER规则被判定为有效，或让尚未到生效时间的NOTBEFORE规则被提前放行。

Part01

漏洞可突破临时授权限制

该漏洞无法绕过密码认证或PAM（可插拔认证模块）机制。攻击者要成功利用，需满足两个前提：一是拥有本地系统的合法认证账号，二是账号已配置带时间访问限制的Sudo权限。

如果管理员通过时间窗口配置敏感命令的临时访问权限，该漏洞就会打破这层安全控制，让攻击者在允许的时间范围外提升权限。受影响的时间授权功能最早在Sudo 1.8.20版本中引入。

Red Hat将该漏洞评级为高危，明确指出如果系统运行存在漏洞的Sudo版本，且配置的NOTBEFORE或NOTAFTER规则未显式指定时区信息，就会面临风险。独立安全研究员Ermenson Junior于2026年8月28日上报了该漏洞。

Part02

建议及时排查加固

Sudo上游维护者Todd Miller于2026年8月29日向项目主分支提交了修复补丁。补丁会在Sudo设置时区时，从运行环境中移除用户可控的TZ变量，避免mktime()函数重复调用时读取攻击者构造的时区值。截至漏洞公开时，该修复尚未集成到已发布的Sudo 1.9.18版本中。

企业和组织应首先排查内部运行Sudo 1.8.20至1.9.17p2版本的系统，检查sudoers策略中配置的NOTBEFORE、NOTAFTER规则条目，待厂商发布更新后第一时间安装修复。

管理员配置时间限制的授权规则时，应尽可能使用显式UTC时间戳或时区偏移值，减少时间计算过程中的歧义，进一步降低风险。

参考来源：

Sudo Security Vulnerability Lets Attackers Escalate Privileges

https://cybersecuritynews.com/sudo-security-vulnerability/

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