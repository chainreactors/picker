---
title: 假冒Mullvad VPN分发Powershell-Loader恶意软件
url: https://mp.weixin.qq.com/s/bY2f1w4KPHvwOBc81TICfQ
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:01:14.391777
---

# 假冒Mullvad VPN分发Powershell-Loader恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8kp4vzLDGiareMF6rNQLoDC6XAKySkJR9kCxDEaBzEpeLDsfHpyBsTa6PZ14QQYercYaVnKy2wTibWKEwiaZVFiaSoDNq8KCVOn3cY/0?wx_fmt=jpeg)

# 假冒Mullvad VPN分发Powershell-Loader恶意软件

原创

忍者
忍者

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

当前有一个恶意活动正在通过假冒VPN下载网站执行，伪装成合法服务。攻击者通过冒充知名的VPN提供商**Mullvad VPN**，分发签名的Powershell-loader恶意软件。恶意载荷通过钓鱼域名**mullvad-vpn[.]us[.]org**进行分发，用户被重定向到**mullvad-download[.]org**。该恶意网站与合法的Mullvad VPN官网非常相似，旨在欺骗用户下载被感染的安装程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8lRgW8QviceNicDenS3iccpDVFjOj4qsWL8vopxEfBeMZk8c4HHxqSS7K4XElN1RcqJMcMx7Blx3QG3orKeiatn6CDepdpiaIUDvsrA/640?wx_fmt=png&from=appmsg)

#### 恶意软件详情

####

该恶意软件样本被发现由**Xiamen Quanlian Information Technology Co., Ltd.**通过**Sectigo**证书进行签名。这一点非常重要，因为它表明攻击者采取了额外的措施，获取了一个合法的证书，以绕过Windows Defender SmartScreen等安全措施，这些安全措施通常会错误地标记未签名的可执行文件。

该文件是一个Windows可执行文件（**Install Mullvad VPN.exe**），一旦执行，就会触发从**metrics.msft17[.]com/run/XYaR5gFi**下载并执行一个被混淆的Powershell脚本。该Powershell脚本被精心设计，通过高级混淆技术避免被传统的安全软件检测到。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8nR7mRFcwxHz5VL1WmVzwuibVoic9rFPMBV9CSJicHIXNrNrLicmvJCmQ4ibxEao9OyHl0dpIyyUtic3XlDcGdaFlGicL3ynnJpcVgXvw/640?wx_fmt=png&from=appmsg)

#### 恶意软件行为与C2基础设施

####

一旦执行，恶意软件会与位于**events[.]ms709[.]com**的命令与控制（C2）服务器进行通信。这些C2通信采用了高度编码的形式，进一步增加了分析和检测的难度。

该恶意软件还依赖多个网页域名来促进其载荷的交付和持久性机制：

* **metrics.msft17[.]com**

  托管恶意的Powershell代码。
* **events.ms709[.]com**

  作为主要的僵尸网络C2服务器，允许远程控制并窃取敏感数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8m4IjFd954VfiavyWwv5tMCFz7gM2q5A4hjp6BD5LdWtPx0IgWv2VJFjB7tT0OpeGNicX6GZEicIfqYibIEVhbkcNVz79ZCzXWhDtM/640?wx_fmt=png&from=appmsg)

#### 恶意软件分析

####

为了深入了解恶意软件的能力和策略，进行了详细的引爆分析，并在**Any.Run**沙箱环境中观察到以下行为：

* **混淆的Powershell执行**

  恶意软件运行一个混淆的Powershell脚本，负责下载额外的载荷。
* **C2通信**

  恶意软件与远程服务器进行通信（通过编码的数据），以接收命令或窃取数据。
* **持久性机制**

  恶意软件试图在感染的计算机上维持持久性，确保即使重启后仍能继续运行。

#### 对用户和组织的影响

####

这种类型的恶意软件尤其危险，原因如下：

**VPN服务的合法性**

恶意软件伪装成一个可信赖的服务**Mullvad VPN**，使得攻击者更容易欺骗用户下载受感染的可执行文件。

**签名恶意软件**

恶意软件使用合法证书进行签名，进一步复杂化了检测工作，因为许多终端保护解决方案会忽略具有有效证书签名的文件。

**C2通信**

感染主机与C2服务器之间的编码通信使得传统的网络安全解决方案难以识别攻击并阻止恶意流量。

####

#### 结论

####

这一威胁展示了攻击者如何通过社会工程和技术手段绕过安全防御。假冒的Mullvad VPN网站是一个例子，说明了攻击者如何利用用户对受欢迎的隐私保护服务的信任。通过保持警惕并实施强有力的安全措施，个人和组织可以减少受到此类攻击的风险。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

Khan安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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