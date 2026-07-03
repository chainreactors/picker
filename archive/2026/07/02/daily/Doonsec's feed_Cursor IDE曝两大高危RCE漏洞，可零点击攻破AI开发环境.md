---
title: Cursor IDE曝两大高危RCE漏洞，可零点击攻破AI开发环境
url: https://mp.weixin.qq.com/s/rqIj9J1ORa8Ik6Zj0Hy_vA
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:46:18.223666
---

# Cursor IDE曝两大高危RCE漏洞，可零点击攻破AI开发环境

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0bsgZMIT2CgCGLJq3XbSDyOUdsibHKtfqJEyE6sYWbJx1wnrmLTLk63EtqicRCFhic4ibOKNNOYBP2WE6UU5344tdPLQnq9ccF5ibo/0?wx_fmt=jpeg)

# Cursor IDE曝两大高危RCE漏洞，可零点击攻破AI开发环境

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX1eMydabvJ803jQUcvEnQ3zAXTwOtFdOZG71zOlW6B9kZ1eJT0V9pKibbApCtu8QGKmsXdzY3QLD88ktcnQREx4tyOxqaZ9VX5I/640?wx_fmt=gif)

![文章配图](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2r7JHl5wJ2IyeX4tdibEXbIW9R080ghmp1IyAIYaoPxs94PewCbPUAPDXIZZ2Yrwv90J9urArlDyxktl6JnHVorBxSzMREiaXbk/640?wx_fmt=png)

在超过半数财富500强企业使用的AI开发环境Cursor IDE中，发现两个关键远程代码执行（RCE）漏洞。Cato AI实验室披露了这两个被命名为"DuneSlide"的漏洞（CVE-2026-50548和CVE-2026-50549），CVSS严重性评分均为9.8分，攻击者可借此完全突破Cursor的沙箱防护。

这些漏洞表明，提示注入攻击的影响范围已不仅限于操纵大语言模型（LLM）输出，还能触及传统代码路径——这些路径此前从未被视为攻击面的一部分。漏洞利用可使威胁行为者覆写关键系统文件（如cursorsandbox二进制文件），将沙箱终端命令转化为完全不受限的RCE，进而同时危害本地机器和连接的SaaS工作区。

这两个漏洞的触发均无需任何用户权限或主动交互，受害者只需发出一个看似无害的提示，该提示会无意中从未受信任来源（如MCP服务器响应或被污染的网页搜索结果）加载攻击者控制的内容。

Cursor 2.x版本会在沙箱内自动运行Agent终端命令而无需用户批准，这种设计本意是减少批准疲劳，同时限制简单提示注入可能造成的危害升级。

Part01

漏洞一：工作目录操纵

CVE-2026-50548源于Cursor沙箱对命令工作目录授予写入权限的机制。由于working\_directory是run\_terminal\_cmd工具中一个可选的、由LLM控制的参数，提示注入可引导Agent将其设置为攻击者指定的项目根目录之外的路径。

这使得攻击者能够写入敏感位置，包括/Applications/Cursor.app/Contents/Resources/app/resources/helpers/cursorsandbox处的cursorsandbox辅助程序，或~/.zshrc和~/Library/LaunchAgents等文件，从而解除同一注入中后续命令的沙箱限制。

Part02

漏洞二：符号链接规范化绕过

CVE-2026-50549是Cursor路径解析逻辑中的一个独立缺陷。提示注入可引导Agent在项目目录内创建指向外部文件的符号链接；当Cursor的规范化步骤失败时（例如目标不存在或缺乏读取权限），Agent会回退到信任原始的、未经验证的符号链接路径。

这绕过了越界写入检查，使攻击者能够通过符号链接覆写相同的cursorsandbox辅助程序，在无需任何用户交互的情况下实现特权RCE。

DuneSlide事件表明，当参数验证和路径解析的边缘情况仍可通过提示注入被利用时，仅靠沙箱无法约束自主编码Agent的行为。Cato AI实验室表示正在对其他流行编码Agent持续进行负责任的漏洞披露，指出需要系统性、架构级的防御措施而非零散补丁来确保AI驱动开发工具的安全性。

参考来源：

Critical Cursor IDE RCE Vulnerabilities Enable Prompt Injection in Zero-Click

https://cybersecuritynews.com/cursor-ide-rce-vulnerabilities/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

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