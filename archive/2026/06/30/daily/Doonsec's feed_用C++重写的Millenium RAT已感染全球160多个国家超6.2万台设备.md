---
title: 用C++重写的Millenium RAT已感染全球160多个国家超6.2万台设备
url: https://mp.weixin.qq.com/s/Lgk-hy8BSTtK9tQl6e2l4A
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:21:01.829991
---

# 用C++重写的Millenium RAT已感染全球160多个国家超6.2万台设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0DhE86cYj1arVcOqRjUTMOhZq14Pl4xRkITiajgTERMp0xVzHByHTZkks1h2bmlJuj3hnwqMC6rjxvicjZrDzE106cKjTy9ia3PE/0?wx_fmt=jpeg)

# 用C++重写的Millenium RAT已感染全球160多个国家超6.2万台设备

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX2iaTY92K53fsAnkwOqibJwFibibTQyEiaMrmqxapyG0ricZ70iaPjvwmbalqrgvPHXdXODDEePT3sYMflib7ldynb76PxSPTnicWfAsHbY/640?wx_fmt=gif)

![图片](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1e2DgnxictRLY8GQU0TiaQtGR1bqzF2mO4icU9rjUsOFlwPXSnF2kTqALpyDqVK7BNDaFaUUZkfCnmClvT6lO4cicboeeiaMabcPP4/640?wx_fmt=png)

一款名为Millenium RAT的远程访问木马正在全球范围内悄然传播，其感染规模令人震惊。目前已有超过160个国家的6.2万台设备遭到入侵，且感染速度未见减缓迹象。

仅2026年第一季度就有超过3.9万台设备被感染，表明攻击活动正在持续扩大。该恶意软件最初由CYFIRMA在2023年11月的威胁报告中披露，当时版本号为2.4。如今已升级至第4版，技术架构完全重构，攻击能力显著增强，主要针对全球Windows设备。

Part01

攻击组织与传播模式

Group-IB分析师将这一活跃攻击活动归因于名为"Y2K Operators"的黑客组织。该恶意软件的开发者使用"shinyenigma"作为代号，在地下论坛和GitHub等平台公开推广。

![图片](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1Rm0gjmf702iaibp5lo16APE4Pib0m67m8mdGy1Bia5Q3WV1P0vicZ3I3tCrzsyhl4ehCJHvfO9R74dJuhYfW05drfZfD13ZrdJ0WI/640?wx_fmt=png)

Group-IB向网络安全新闻(CSN)提供的报告显示，该工具以"恶意软件即服务"(Malware-as-a-Service)形式出售，首月费用50美元，续费10美元，或支付90美元获得终身使用权。

Part02

技术架构升级

第4版最重大的变化是从.NET完全重写为原生C++，消除了对受害者设备上.NET框架的依赖，大幅提升了隐蔽性。该木马通过Telegram Bot API与攻击者通信，将命令控制流量伪装成普通网络活动，无需专用服务器。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cA87SRC7aSNK45jiaB8RUmWowiamro0q3aZGYxZyiatic9dZMR6gxsQOk1RPwkg4YjuJES4N7HnEc9J5QFrUksv8gm1utXbH2600/640?wx_fmt=png)

执行后，RAT会从嵌入式文件资源加载加密配置，包含Telegram机器人令牌、聊天ID、持久化设置和键盘记录选项。数据采用Base64编码，并通过自定义XOR算法保护，额外添加随机数据以改变文件哈希值，规避基于签名的检测。

Part03

多样化攻击能力

该RAT功能全面，可窃取浏览器凭据和Cookie、截取屏幕和摄像头图像、录制音频、记录键盘输入、获取Telegram和Discord会话数据，以及加密受害者文件。所有命令都通过Telegram下发，无需专用服务器。持久化机制通过将有效载荷复制到%APPDATA%并添加注册表自启动项实现。

恶意软件还尝试通过标准Windows UAC提示进行权限提升，依赖用户授权。所有功能都基于标准Windows API调用，未使用0Day漏洞，完全依赖用户信任实施攻击。

Part04

社会工程传播手段

Y2K Operators完全依赖欺骗手段传播Millenium RAT。文件被伪装成信用卡生成器、加密货币余额检查器、黑客工具包、破解软件和游戏实用程序。文件名经过精心设计，诱使目标立即打开，广泛撒网以覆盖尽可能多的受害者类型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2wIcqlaArk7RDxIblJbofJZ2bXg67DwoARYxxCOibuJjAJpY877vnnCTlSLTxyyK1rGtgHNLsiax1sR8AF89XTiapxiaJ9esRPcR0/640?wx_fmt=png)

攻击者甚至会将已知RAT和漏洞利用工具植入后门后重新分发。潜在攻击者下载看似可用的工具后反而被感染。在某次攻击活动中，受害者收到伪装成PDF的快捷方式，触发PowerShell静默运行，在获取RAT有效载荷的同时下载诱饵文档，并在前台打开文档作为掩护。

感染后，有效载荷会伪装成svchost.exe、MsEdgeUpdate.exe和Microsoft Antivirus.exe等常见进程。安全专家建议用户将意外的UAC提示视为可疑行为，避免运行不可信来源的文件，日常使用非管理员账户，保持系统补丁更新，并启用多因素认证以降低凭证被盗风险。

Part05

入侵指标(IoCs)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1T6HEoNTaao3GRSyY6Yu7NBL4fmxqCCV1rnIuhpxIMk4gDld6QIQCgGFica6FZeuDH2JgLVyibksEISO4aGsYVBKR3m5FXsVp5g/640?wx_fmt=png&from=appmsg)

注：IP地址和域名已进行无害化处理(如使用[.]代替.)，防止意外解析或超链接。仅在MISP、VirusTotal或SIEM等受控威胁情报平台中可恢复原始格式。

参考来源：

Millenium RAT Rewritten in C++ Infects 62,000+ Devices Across 160 Countries

https://cybersecuritynews.com/millenium-rat-rewritten-in-c/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2hnMwPwS6lmzbFHf7S8ibkCSGSF9zbd12puFsqvAeRIjLV7b95iaBhzib3wR12ia2WNVDpNOZvF8yaZcGaQ3kXTL8YePjicoGiajOTg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340988&idx=1&sn=0937f2692c838e2a62e89dde8d9dbe41&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3BRs1SIg3pvHw9PNmLlib6c3rX0W3PemrBoDibgBD3WXIWDcs94DXZpBy9YuU36icJ4NHEE98mUbqcOYyicrZBiblxE3uy64Zibo1PY/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0UGcrYtIkSYDEgbDkib0yMF23VlKQibpJyRnibia1cD3no5XF7Je0Sic98ytMyvbY9LhO8tKoxBlnibsAXh8CnBTYoAxLReujuqjomI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

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