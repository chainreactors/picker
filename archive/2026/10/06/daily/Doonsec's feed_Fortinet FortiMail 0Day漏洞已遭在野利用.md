---
title: Fortinet FortiMail 0Day漏洞已遭在野利用
url: https://mp.weixin.qq.com/s/pXkmblBE0cENUmCi9lM0oA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:56.944676
---

# Fortinet FortiMail 0Day漏洞已遭在野利用

# Fortinet FortiMail 0Day漏洞已遭在野利用

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1k2fMJcgOiayjEeibeJHyatHP90HFjVyceohVDrRy3wcYNWgJxOYH5qibqAoibFz8cWI84smlswom2AZxIQibcH6U2MTKicYngia6DPA/640?wx_fmt=gif)

![CISA将Fortinet FortiMail 0Day漏洞纳入KEV目录，该漏洞已遭在野利用](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3ibJ4yLfDDcNhhzt8HnImdzvWuo45nYPJrdZ2QwgSkUlU900libSicIIibmN0BqVx4Dde8asCaZ8Y4iaYH33dCxoBibV9F34xicjYZzI/640?wx_fmt=jpeg)

CISA已将Fortinet FortiMail的一处严重漏洞（CVE-2026-104286）纳入已知被利用漏洞（KEV）目录，原因是已有证据显示该漏洞正遭在野利用。

Part01

漏洞属路径遍历类型

该漏洞影响Fortinet FortiMail。这款邮件安全产品通常部署在网络边界，用于过滤恶意邮件，保护企业内部消息系统。

未授权远程攻击者可向存在漏洞的FortiMail设备发送特制HTTP或HTTPS请求，利用该漏洞发起攻击。攻击成功后，攻击者能够向设备底层系统写入任意文件。

CVE-2026-104286属于路径遍历漏洞，成因是空字节处理不当。攻击者可借此篡改文件路径，访问或写入预期目录之外的文件。

空字节处理缺陷可帮助攻击者绕过输入验证机制。这类机制通常基于文件名或扩展名做校验，一旦系统对空字节的处理逻辑存在问题，校验就会失效。该漏洞对应CWE-22、CWE-158两类缺陷。

Part02

CISA明确修复时限

CISA在2026年10月1日正式将该漏洞录入KEV目录，要求联邦民事行政部门机构在2026年10月4日前完成修复。

各机构需按照第26-04号约束性操作指令（BOD 26-04）的要求，应用厂商推荐的缓解措施。该指令会根据风险等级对安全更新任务进行优先级排序，优先处置高风险漏洞。

Part03

漏洞可致设备持久被控

CISA在KEV条目中未将该漏洞与已知勒索软件活动关联。但面向互联网暴露的邮件安全设备一旦被攻破，攻击者就能获得高价值的初始访问权限。

攻击者获得任意文件写入权限后，可根据设备配置与文件权限，投放恶意文件、篡改系统配置、建立持久化访问，或为后续入侵活动铺路。

CISA同时依据BOD 26-04明确要求，各机构必须针对该漏洞开展取证排查。使用FortiMail的组织应全面梳理所有对外暴露的设备，确认是否受漏洞影响。

相关方需及时应用Fortinet官方指定的缓解措施或安全更新。安全团队还要检查日志中是否存在可疑的HTTP/HTTPS请求，排查系统内的异常文件、非预期配置变更、未授权账号与异常出站流量。

如果暂无有效缓解措施，CISA建议相关方遵循对应云服务安全指引，或停止使用受影响版本的产品。组织应优先处置面向公网可访问的FortiMail部署，这类设备暴露在互联网上，更易遭到攻击者的无差别扫描与利用。

参考来源：

CISA Adds Fortinet FortiMail 0-day Vulnerability to KEV Following Active Exploitation

https://cybersecuritynews.com/fortinet-fortimail-0-day-vulnerability-exploitation/

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