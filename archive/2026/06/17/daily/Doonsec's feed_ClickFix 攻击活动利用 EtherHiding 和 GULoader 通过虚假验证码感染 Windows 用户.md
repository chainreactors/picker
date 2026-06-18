---
title: ClickFix 攻击活动利用 EtherHiding 和 GULoader 通过虚假验证码感染 Windows 用户
url: https://mp.weixin.qq.com/s/mDLjhKNvdf4ixwXMZBS1hw
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:47:49.705060
---

# ClickFix 攻击活动利用 EtherHiding 和 GULoader 通过虚假验证码感染 Windows 用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7POBlia58XpnHQqjDILicz7bia9FHZkAPkiblMnSTyXukFIrueMTpIsZCA9aKj9RhGaDZZriaNTLZUdgH51fokCQnKawVSrxEPUBD80/0?wx_fmt=jpeg)

# ClickFix 攻击活动利用 EtherHiding 和 GULoader 通过虚假验证码感染 Windows 用户

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一种新的网络攻击活动正通过虚假的 CAPTCHA 页面针对 Windows 用户，结合三种技术绕过标准安全防御而不引起警报。

该攻击活动最早于 2026 年 4 月被发现，它始于一个被入侵的欧洲小型企业网站，最终目的是将基于内存的恶意软件下载器 GULoader 加载到受害者的计算机上。

这种攻击的危险之处在于它能自然地融入正常的浏览活动中，从而欺骗用户和自动化安全工具。

该攻击的目标是通过谷歌搜索访问看似合法网站的用户，不涉及钓鱼邮件或可疑链接。

网站功能一切正常，产品页面、联系表单和地图等都运行良好。隐藏在网站 WordPress 后台的恶意代码静静等待，一旦满足特定条件就会激活。

Sicuranext 的分析师发现了此次入侵事件，并记录了完整的攻击路径。根据 Sicuranext向网络安全新闻 (CSN) 分享的报告，此次攻击活动整合了一个被入侵的 WordPress 网站、一种名为 EtherHiding 的基于区块链的有效载荷方法、一种名为 ClickFix 的社会工程攻击手段，以及一个归因于 GULoader 的远程加载器。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NtBSCnapkOWuFsbfSWwAvvX5Wb0HFvIGUcqLuAHOM9oC500uE0kBicPFoqER4eQa8mTS1BTjc2vS5xUMYRa7kG5jXJY5nlxxgQ/640?wx_fmt=png&from=appmsg)

每一层攻击都伪装成合法攻击，使得大多数传统防御机制没有理由介入。受感染的网站仅针对Windows桌面浏览器。

任何通过手机或安全扫描仪访问的人都会看到一个完全干净的页面，从而对网站所有者、搜索引擎和自动监控器隐藏了攻击。

只有真正的 Windows 用户在桌面上才会触发有效载荷，因此通过例行检查很难发现这种攻击活动。

在此次事件中，行为检测在GULoader加载完成前不到300毫秒就阻止了攻击。尽管如此，此次攻击活动仍然险些得逞，并暴露了组织在防御此类威胁方面存在的真正漏洞。

## **ClickFix Campaign 使用 EtherHiding 和 GULoader**

攻击从受害者访问被入侵页面的那一刻就开始了。两秒钟内，注入的 JavaScript 代码会悄无声息地连接到 BNB 智能链测试网（一个免费的公共区块链），以获取存储在智能合约中的恶意载荷。

这种被称为 EtherHiding 的技术很难被阻止，因为请求会通过 Cloudflare 等受信任的提供商传输，而且区块链数据无法通过滥用报告删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7MhtQ3IYFficY3iavMDXo4tYwOUVRr0VKsLC31SP1tgtmlRqkR5SHicyicWvx1FW9BVR4kYYt2kzJtyzUrRcibE4ibczK11cdQBvtuKw/640?wx_fmt=png&from=appmsg)

一旦成功获取，恶意程序会在合法页面上显示一个伪造的 reCAPTCHA 验证码叠加层。该叠加层会提示用户按下 Win+R、Ctrl+V 和 Enter 键，这些快捷键会打开 Windows 运行对话框并粘贴命令。

用户不知道的是，剪贴板已经通过浏览器内置功能加载了一条恶意指令，而受害者却误以为这是例行检查，并自愿运行了该指令。

该命令调用 rundll32.exe，这是一个受信任的、经过签名的 Windows 工具，并将其指向攻击者通过 UNC 路径托管的远程 DLL 文件。由于 rundll32.exe 是经过 Microsoft 签名的二进制文件，因此它会在没有任何警告的情况下清除 SmartScreen。

该 DLL 直接加载到内存中，不会将文件写入磁盘，也不会显示任何提示，从而绕过了在执行前扫描文件的防病毒工具。

## **GULoader 交付和行为检测**

根据威胁情报报告，本次攻击活动中的 C2 域名 autum-path[.]vo8xalon[.]in[.]net 归因于 GULoader。

GULoader 是一种基于 shellcode 的加载器，完全运行在内存中，通常用于投放 Lumma 和 Vidar 等信息窃取程序以及 Remcos 和 AgentTesla 等远程访问工具。成功执行可能导致凭证被盗或受害者计算机被完全远程控制。

针对 rundll32.exe 的行为规则，如果其参数异常且调用了基于序号的函数，则会在 300 毫秒内标记并终止该进程。

事件后检查确认未生成任何子进程，未发生数据泄露或横向移动。为安全起见，已重置用户凭据并结束所有活动会话。

建议安全团队阻止端口 445 上的出站 SMB 流量，并考虑在不需要 WebDAV 的工作站上禁用 WebClient 服务。

强烈建议监控浏览器进程对区块链 RPC 域的 DNS 查询。此外，搜索 Windows 运行对话框历史记录中的 rundll32 或 UNC 路径条目也有助于及早发现安全漏洞。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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