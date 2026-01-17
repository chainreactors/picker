---
title: AI代码驱动的MonetaStealer窃密软件正瞄准macOS用户
url: https://mp.weixin.qq.com/s/tkK7Ob3Qj8IDWFlHcUcQww
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:26:06.040117
---

# AI代码驱动的MonetaStealer窃密软件正瞄准macOS用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EmicqFmoHrFJhE0olONerj9xvcVQL8Z4O8KVTQuB7Tic3kPibD5LIsciaOS97ISthUkOyLeAFUB5vlZg/0?wx_fmt=jpeg)

# AI代码驱动的MonetaStealer窃密软件正瞄准macOS用户

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

安全研究人员于2026年1月6日首次发现一种名为MonetaStealer的新型信息窃取恶意软件，该软件正通过伪装文件和社交工程手段，积极针对macOS用户发起攻击。该恶意软件伪装成名为“Portfolio\_Review.exe”的Windows可执行文件，实则是一个Mach-O二进制文件，对经常接收来自候选人或合作方作品集文件的专业人士构成显著威胁。

MonetaStealer旨在从受感染的macOS系统中窃取敏感信息，包括浏览器密码、加密货币钱包数据、Wi-Fi凭证、SSH密钥和财务文档。其代码包含专门的系统检查（`if sys.platform != 'darwin'`），确保仅在苹果设备上执行。

此次威胁的特别之处在于其高度依赖机器学习工具生成的代码。研究人员认为，这表明该恶意软件仍处于早期开发阶段。尽管功能尚未完善，但其在发现时于VirusTotal上的检测率为零，能够躲避大多数安全解决方案的检测。

分析显示，恶意载荷隐藏于PyInstaller编译的二进制文件中，主文件为`portfolio\_app.pyc`。这个基于Python的恶意软件将其恶意逻辑嵌入到可绕过基本静态文件扫描的压缩CArchive结构中。反编译代码中发现了俄语注释且未做混淆处理，表明开发者优先考虑了功能而非隐蔽性。执行时，软件会显示“PROFESSIONAL MACOS STEALER v2.0”横幅，并通过打印语句跟踪其各个数据窃取模块的进度。

针对Chrome浏览器的数据窃取

MonetaStealer通过创建SQLite数据库的临时副本来绕过文件锁，专门窃取Google Chrome浏览器数据。它执行命令`security find-generic-password -w -a "Chrome"`来检索存储在macOS钥匙串中的Base64主密钥，这是解密保存的密码所必需的。此操作会触发系统提示，要求用户输入钥匙串密码，可能引起警觉。一旦获得访问权限，恶意软件便通过特定的SQL命令查询登录凭证、会话Cookie和浏览历史记录。

其Cookie窃取模块采用关键词过滤，通过搜索Cookie主机名中的“bank”、“crypto”、“exchange”、“paypal”等术语来识别高价值目标。这种针对性方法使其能够优先窃取金融和加密货币平台的会话信息。同时，该软件还通过从Chrome的历史记录数据库中提取URL、页面标题和访问频率来窃取浏览历史，这些信息可能暴露用户兴趣、常访问服务以及后续攻击的潜在目标。

所有收集到的浏览器数据都被结构化存储到恶意软件的内部字典中，以便后续通过一个ID为“8384579537”、名为“b746\_mac\_collector\_bot”的Telegram机器人进行外传。目前，该威胁持续活跃，macOS用户需对来源不明的文件保持高度警惕。

资讯来源：cybersecuritynews

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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