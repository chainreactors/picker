---
title: 钓鱼揭秘 | 微软云服务网络钓鱼技术分析
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490947&idx=1&sn=d8a02c07b0fdc8552385c1d368297586&chksm=c187dd92f6f0548402c3403123e4d1fa6cf75b7127f3ea693b353fa58561f5e7bb22e484c7e4&scene=58&subscene=0#rd
source: M01NTeam
date: 2023-03-09
fetch_date: 2025-10-04T09:02:12.893449
---

# 钓鱼揭秘 | 微软云服务网络钓鱼技术分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbPoko3y1oG4oweW75rEu3IMwKwKycuhRwnk3ica8hOOvibBX69oaicziaHsHKmQ1XCM6q65Lh4LMvNng/0?wx_fmt=jpeg)

# 钓鱼揭秘 | 微软云服务网络钓鱼技术分析

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTH0o5pTAO8jdqnibfx5ttzeyzVJRTatfuSibA1rn51P4j6jrFUXOX3Crbw/640?wx_fmt=gif)

**背景**

随着云化服务的普及，网络钓鱼攻击技术也趋于云化，我们需要对此保持高度警惕。尤其是当攻击者利用云服务和知名品牌的名字进行攻击时，由于云服务的高信誉度，传统的防御产品很难精准有效地拦截这种攻击，因此我们必须保持警觉。

本文将对黑客利用微软云服务进行网络钓鱼攻击的技术进行探讨，这些被利用的云服务包括：OneNote、OneDrive、Forms等。请阅读本文，以更好地保护自己的系统和网络安全，避免成为网络钓鱼的受害者。需要注意的是，这种滥用行为并非通过漏洞或入侵微软云服务实现，而是利用微软云服务的正常功能进行的攻击。

**01**：托管恶意文件

OneDrive是一种云存储服务，用户可以使用OneDrive来存储文档、照片、视频、音频等文件类型，OneDrive还可以与其他微软服务如Office 365集成，让用户能够在云端轻松地创建、编辑和共享文档。

利用OneDrive的存储功能和链接分享功能，我们可以方便的托管恶意文件，并且使用微软提供的域名“1drv.ms”进行投递，如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTH5Bia8gzQCWbfz1Qbw0hjAYg73h05XLA7a4zSH5bibaBsDPAzXMCqic5ew/640?wx_fmt=jpeg)

**图：使用OneDrive托管恶意文件**

OneNote是微软的笔记应用，具备强大的内容编辑器和网页剪藏功能，并且在OneDrive上进行了集成，用户可以创建自己的笔记，并将它们共享给其他人。我们可以通过利用OneNote进行诱导性内容托管，包括“敏感的话术文字”、“恶意链接”和“恶意文件”等，最终将这些内容托管在“onedrive.live.com”域名上，并通过该域名进行访问，具体内容和演示请参见下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHFUBYicW5qzXfdB9MtC19ibCLAmDdYM0AEbQTWnB7sse9dzPfsxH3sAkg/640?wx_fmt=jpeg)

**图：使用OneNote托管诱导内容和恶意链接**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHsMRAXyj73gj2sVpicE6WrkO4sRy5gceSfkI5qCdssOSMAuAgXCetkPw/640?wx_fmt=jpeg)

**图：使用OneNote托管诱导内容和恶意附件**

利用OneDrive的附件插入功能，我们还可以轻松捕获该附件文件的下载直链，然后在任意场景下通过“onenote.officeapps.live.com”域名进行投递。如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHh1Qwlf8Ek1SF5KibUSdon8gZlouvgGRXGKx5gk2yj1t3q1ktCJc5sicg/640?wx_fmt=png)

**图：获取OneNote附件的下载直链**

**02**：发送恶意邮件

OneDrive的邮件分享功能可以帮助用户将文件或文件夹通过邮件发送给其他人，选择要分享的文件或文件夹，然后单击“分享”按钮。接下来，可以选择“通过电子邮件邀请”选项，输入收件人的电子邮件地址，并添加一条消息来描述这个分享链接。

使用OneDrive的邮件分享功能，用户可以定制化“描述文字”、“发件人姓名”，最终通过微软的邮件服务发送邮件。这些邮件看起来来自微软，实际上包含恶意文件和恶意链接。如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHzJhqEAMB0sxoakWtT2JZz7lj7hZBUxyV9QQbmc3y81kO8BGrDFK9QQ/640?wx_fmt=jpeg)

**图：使用OneDrive发送恶意压缩包邮件**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHicgnhXNTx2Nics8nCXSTrtrOJnDC4MSkgECNdRup6gtmvrUA1gtY8hiaw/640?wx_fmt=jpeg)

**图：使用OneDrive发送恶意链接邮件**

**03**：创建钓鱼表单

微软Forms是一种在线调查和问卷工具，可以帮助用户轻松地创建各种类型的表单，包括：问答题目、选择题、分页、分段和主题，并可以选择多种样式和布局。同时，微软Forms还提供了数据分析和报告功能，可以帮助用户轻松地分析回答结果。

借助微软Forms，用户可以快速创建一个定制化的钓鱼表单。用户可以自由设计表单的“背景图片”、“文字内容”、“输入问题”等，以达到欺骗受害者的目的。这些表单将被托管在"forms.office.com"域名下，可以方便地记录目标的输入内容，从而实现个人或组织的攻击行为。如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHic1UBVgpMLbn2xq47OKN5KIWIQD5kFrrnicFdu0pP39KXjWHWwm1Rn9Q/640?wx_fmt=jpeg)

**图：创建定制化的Forms钓鱼表单**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTH8fIeGX2mcC3y5ibz1SElqNBZaDyJRysjHa8RMXdhibV8QGbwfbDibGaFA/640?wx_fmt=jpeg)

**图：Forms钓鱼表单结果回收**

写在最后

在滥用微软云服务进行网络钓鱼攻击方面，微软已经采取了一系列措施来保护用户。微软的云服务包括高级威胁防护、多因素身份验证等功能，可以帮助用户识别并阻止这种攻击。尽管微软云服务的安全功能越来越强大，但是攻击者也在不断改进其攻击手段。因此，用户和企业应该时刻保持警惕，注意验证所有不明来历的邮件和链接，并在下载和安装任何软件之前进行彻底的安全检查。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTH1b78spyGicmH6omxSIsEvMmxxl8qry0k35yuJunaBq93yeGGj1PfXRg/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHTJricAdx0AjSnFNpZxnOVooMcSO6gvDnhOkAFMfYAI2R7VyKPBGiaIPg/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbaqeVUKxZJ9ibNwJmEuCicTHvkg61O4zRwz4dlSmXuzmY0bDmmInKEm5KacwTTQI9ibWCMY9SODDiaMg/640?wx_fmt=png)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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