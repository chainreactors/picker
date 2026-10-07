---
title: 苹果将收紧macOS全磁盘访问权限，防范AI Agent隐私风险
url: https://mp.weixin.qq.com/s/QAYmRYItaWpc127qwXconA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:51.534162
---

# 苹果将收紧macOS全磁盘访问权限，防范AI Agent隐私风险

# 苹果将收紧macOS全磁盘访问权限，防范AI Agent隐私风险

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3NG4YmuCbAYMWMhEcWxBegOqFTabrSfiaPohhsojodsTS7Oics9O2GjnYHiaAjVCBTqM0Rb9nnXyeeuhEt99UGQFA7W4HaVtwVOk/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2CRsiaxdficQMF2u6zMkcnPDpm4MiaicXwFgMeiaTJHD2D8SWEQDrexHfem1NqZISQnkCLRQa3LicmR5jma5JNwBn5VpVU8fG1s1pIA/640?wx_fmt=png&from=appmsg)

苹果计划为macOS的全磁盘访问权限增设更严格的管控机制。该公司警告称，随着AI Agent能力不断增强，这项高权限可能暴露用户最核心的隐私数据；调整落地后，用户在为应用开放这一宽泛权限前，必须完成更审慎的确认操作。

全磁盘访问权限的设计初衷，是让受信任的Mac工具（以备份软件为主）在必要时绕过常规隐私限制运行。但这项权限允许应用读取Mac本地所有文件，包括邮件、信息、Safari、家庭App、时间机器备份中的数据，以及部分系统设置内容。

根据苹果当前的规则指引，官方已将全磁盘访问列为高风险权限。用户必须手动进入macOS设置的“隐私与安全性”板块添加应用，才能为其开放该权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2PmGcLib44DMFj5pSibJiblbmajvOrGm8cB2UMxZibCvqQR6KBTxvoA8x5gpsnwBKteYLFWgic7m5wgNP8ZM52Lrg6SfF3FP4XJsBM/640?wx_fmt=png&from=appmsg)

Part01

全磁盘访问存在滥用风险

苹果指出，部分开发者对全磁盘访问权限的使用方式，可能导致用户完全不清楚应用能获取多少数据。这种风险的影响范围不只是设备本地存储的文档。

获得权限的应用可以访问邮件、私人聊天记录、浏览历史，以及其他各类个人数据，这些数据在正常情况下受macOS安全机制保护。如果是通讯类工具获得权限，隐私影响还会波及对话中的其他参与方。

AI Agent的普及应用让这一问题进一步恶化。和执行单一明确任务的普通应用不同，AI Agent会从多个来源读取信息并完成整合处理，再基于分析结果采取后续行动。

如果开放全磁盘访问权限，AI Agent就能获取大量个人或企业数据。苹果表示，随着这类工具能力不断增强、自主行动程度不断提升，相关风险还会大幅升高。

Part02

新管控强化知情确认环节

目前苹果尚未公布这套新增管控机制的具体设计、上线时间，以及支持的macOS版本。但从官方表述来看，苹果不再希望用户通过简单的开关完成授权，而是要让用户在开启权限前，清晰了解权限对应的访问范围。

这次调整不会取消备份、安全、恢复类合法工具的全磁盘访问权限。其核心目标是让用户主动确认这项特殊权限的授权，避免用户在快速走完应用安装流程时，未加留意就开放了这项高风险权限。

Part03

建议用户排查现有授权

对于Mac用户来说，当前可以立即采取的防护措施，是检查已获得全磁盘访问权限的应用列表。用户只需打开系统设置，选择“隐私与安全性”板块，再进入“全磁盘访问”页面就可以查看。

对于不再使用、或是没有明确需求读取全系统数据的工具，要及时移除其权限。这一点对桌面AI助手、浏览器扩展、系统清理工具以及通讯类应用格外关键。

这次调整也回应了业界对macOS透明、同意与控制（TCC）保护机制缺陷的普遍担忧。Cyber Security News近期曾报道过macOS TCC绕过漏洞，以及AI Agent实施勒索软件活动的风险持续攀升。

苹果这次计划推出的更新表明，随着AI软件对用户设备的访问权限不断加深，完善的权限设计正在成为核心安全管控手段。

参考来源：

Apple Tightens macOS Full Disk Access as AI Agents Become More Powerful

https://cybersecuritynews.com/apple-tightens-macos-full-disk-access/

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