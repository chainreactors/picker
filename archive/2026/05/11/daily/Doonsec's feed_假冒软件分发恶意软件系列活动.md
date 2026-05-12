---
title: 假冒软件分发恶意软件系列活动
url: https://mp.weixin.qq.com/s/PN2NFs_otqoliyt9r2TIiQ
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:32:31.392213
---

# 假冒软件分发恶意软件系列活动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J7CSmJcRR8k4d5zwIpcX14QBXLdic0vnKia5rHu9aVTaqA6BzqVkDs49LVUVvP7ibZLo308QKibKjq46salic5iclpqGfBeAGhxrkTzwhNynMvp5M/0?wx_fmt=jpeg)

# 假冒软件分发恶意软件系列活动

原创

忍者
忍者

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#### 概述

####

近期，一系列恶意活动正在通过伪装成知名软件下载页面来传播恶意软件。攻击者通过创建多个假的软件网站，伪装成广泛使用的工具，如**KeePassXC**、**Cyberduck**、**Joplin**、**WinSCP**、**Amazon S3浏览器**、**EmEditor**和**Putty**等，诱使用户下载含有恶意负载的程序。这些伪装网站使用了多个恶意域名，并通过合法证书进行签名，从而绕过安全软件的检测。

#### 恶意域名

以下是本次恶意活动涉及的部分伪装域名，攻击者通过这些域名提供恶意软件下载链接

* **winscp-download[.]us[.]org**
* **winscp-setup[.]net**
* **winscp-app[.]org**
* **mullvad-vpn[.]us[.]org**
* **mullvad-download[.]org**
* **mullvad-download[.]it[.]com**
* **winscp-downloads[.]com**
* **s3-browser[.]quest**
* **s3-browser-download[.]blog**
* **em-editor[.]co[.]com**
* **joplin-download[.]com**
* **joplin-desktop[.]app**
* **emeditor-download[.]co[.]com**
* **cyberduck[.]info**
* **cyber-duck[.]co[.]com**
* **filezilla-project[.]us[.]com**
* **putty-setup[.]us[.]com**
* **cyberduck-ftp[.]com**
* **cyberduck-download[.]org**
* **winscp-ftps[.]com**

#### 恶意软件签名

####

这次攻击活动还涉及到使用了恶意签名的证书，特别是来自\*\*"Shenzhen Xingzhongxing Electronic Technology Co., Ltd."**的证书，这些证书由**Sectigo\*\*签发。恶意软件的签名通过合法证书的使用使得传统的安全防护手段难以识别其恶意性质。

#### 恶意样本与技术

####

在一些已分析的恶意软件样本中，例如**KeePassXC**的伪装版本，攻击者通过伪装网站引诱用户下载恶意文件。这些恶意文件会利用Powershell脚本或其他脚本语言来执行恶意操作，包括但不限于

* **下载并执行其他恶意载荷**

  这些文件通常会通过与远程服务器（C2）通信下载额外的恶意代码。
* **绕过安全防护**

  恶意文件使用了混淆技术，以躲避常见的反病毒和安全防护工具。
* **获取控制权限**

  恶意软件会尝试在被感染的计算机上建立持久化机制，使攻击者能够持续控制目标系统。

**假冒的KeePassXC下载页面**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8nR7Vgzelczbpgjd3AMIjvZU49PGpQokgrWe90fAexXAmybRdhpj7H34fFyojhFJw5ict9d1xo8WLdqArQR9Pv91LfGWQuTpWh0/640?wx_fmt=png&from=appmsg)

**假冒的Cyberduck下载页面**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8kyEOEu4xgZAWw0uSvjTtgYNnBCXf92GwpCbnEAof3aFBrIKykD8CCKErxICX3hrMTeWd70BZ2KibuUcN8sUnJMkchDogZA9SKI/640?wx_fmt=png&from=appmsg)

#### 恶意活动分析

####

此次攻击的主要策略是通过虚假的软件网站引诱用户下载恶意程序。攻击者伪装成流行的开源软件和工具，如**KeePassXC**、**Cyberduck**、**Joplin**等，利用用户对这些程序的信任性，成功诱导用户下载安装恶意软件。这些恶意软件往往是经过精心设计和签名的，利用合法证书来掩盖其恶意行为。

攻击者通过在这些伪装网站上提供看似无害的下载链接，实际上是在分发经过签名的恶意软件，进而导致数据泄露、远程控制或系统破坏等安全问题。

#### 建议与防范措施

####

1. **下载来源验证**

   用户应始终从官方渠道下载软件，确保下载链接的安全性。尤其是针对知名软件，应当特别留意任何偏离官方网站的网址。
2. **使用反病毒软件**

   确保所有终端设备都配备更新的反病毒和反恶意软件工具，并且能够有效检测到新型的恶意代码。
3. **网络监控**

   组织应加强网络监控，尤其是对于与未知或可疑域名的通信，及时识别并阻断恶意流量。
4. **提高用户安全意识**

   加强对员工或用户的安全意识培训，教育他们如何识别伪造的软件下载网站，避免受骗。

#### 结论

####

这次恶意软件分发活动展示了攻击者如何利用伪装技术绕过传统的安全防护。通过伪造知名软件的官方网站，攻击者能够轻松诱骗用户下载恶意文件。为了有效抵御此类威胁，用户和组织需要采取适当的安全措施，确保所有软件下载源的可靠性，并定期进行安全审计和监控。

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