---
title: 黑客滥用Outlook邮箱隐藏Linux后门，南亚成重点攻击目标
url: https://mp.weixin.qq.com/s/CV9MPQwA0rUaT3LF0PmD2Q
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:33:28.847457
---

# 黑客滥用Outlook邮箱隐藏Linux后门，南亚成重点攻击目标

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1lM6xgp4iaHvG9PD4eX7r0KzoqptKV9UT3xSHthK1odKabN5509fYPY6WVVj1ibJP02CkibMeiaVEM0KoUXuGZWxoFFeh1aiaIqhm8/0?wx_fmt=jpeg)

# 黑客滥用Outlook邮箱隐藏Linux后门，南亚成重点攻击目标

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3ibEpw1pDgh4Ifz7PaAicfB5FHXHdc5ic1X6oq5y6Ph1Ua4I06OvlyxhKNvSMh0QuibvboZ0eBal8xYmPgQOicm1YJG2CmHVRFZnWs/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****攻击手法分析****

一个疑似国家背景的黑客组织开发出利用微软Outlook邮箱隐藏恶意活动的新技术，使常规安全工具难以检测其攻击行为。自2021年起活跃的Harvester APT组织（被认定具有国家背景）近期升级了其GoGra后门程序，推出Linux版本。该恶意软件通过合法的Microsoft Graph API和真实Outlook邮箱建立隐蔽命令控制（C2）通道，借助受信任的微软云基础设施绕过传统边界防御——这些防御机制通常不会将正常邮件流量标记为可疑。

**Part02**

## ****攻击目标与特征****

此次攻击活动以间谍目的为主，非经济利益驱动。VirusTotal平台最早收到的恶意样本提交记录显示，受害目标主要位于印度和阿富汗，表明南亚地区仍是该组织的重点攻击区域。攻击者还使用了包含当地文化元素名称的诱饵文档，体现出高度定制化的定向攻击策略。历史数据显示，Harvester长期专注于南亚地区的间谍活动，此次攻击延续了该模式。

**Part03**

## ****技术演进与感染链****

赛门铁克与Carbon Black分析师确认，这款Linux恶意软件是Harvester已知Windows间谍活动的扩展版本。研究人员发现新旧版本存在显著代码相似性，证实该组织正在积极发展跨平台攻击能力。攻击者通过社交工程手段诱导受害者打开伪装成PDF文档（如"TheExternalAffairesMinister.pdf"）的Linux ELF二进制文件，触发后台静默感染流程，并建立持久化机制确保系统重启后仍能运行。

**Part04**

## ****微软基础设施滥用机制****

该后门最具技术突破性的特征在于将合法微软云服务转化为隐蔽通信渠道。感染初期，Go加载器会释放约5.9MB的i386可执行文件至"~/.config/systemd/user/userservice"路径。为实现持久化，恶意软件伪装成合法的Conky系统监视工具，创建systemd用户单元和XDG自启动项。核心载荷包含明文存储的Azure AD应用凭证（租户ID、客户端ID和客户端密钥），使其能直接向微软请求OAuth2令牌，并通过名为"Zomato Pizza"的Outlook邮箱文件夹建立通信（每2秒轮询指令）。

**Part05**

## ****防御建议****

攻击者发送的指令邮件主题以"Input"开头，恶意程序会解密经过AES-CBC加密的base64编码邮件正文，通过/bin/bash执行命令后，将结果加密并通过主题为"Output"的回复邮件传回。完成通信后，后门会发送HTTP DELETE请求清除原始指令邮件，几乎不留痕迹。建议Linux系统用户重点检查以下异常迹象：

* 自启动项和systemd用户单元中的可疑服务（特别是仿冒Conky的工具）
* 非常规终端的OAuth2令牌请求和Microsoft Graph API活动
* 用户目录下带有虚假扩展名的ELF二进制文件
* 非标准进程在"~/.config/systemd/user/"路径的写入操作 企业应封锁未经批准的Azure AD应用凭证以降低此类滥用风险。

**参考来源：**

Hackers Use Outlook Mailboxes to Hide Linux GoGra Backdoor Communications

https://cybersecuritynews.com/hackers-use-outlook-mailboxes/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NlibR8DpnkZguk1so3ThwkXScRIP7SKicZdaVeLa1eMHdfLgFsOaFCP6qt2JaDlnDPzLe5MJBV1micoP6YM0SG5C9X1ibsshUiccM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337140&idx=1&sn=134af642d92b85fc1076a8c83c09945c&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bKq2xLKwFuy1Yl63ibm7kJUCW7hP4uRIhllVu6icLPkYcerZIx5264cbnPu5uCLCpb0ic16Gm32GC3B6ou34yFia9Nm4YJTGU4iag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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