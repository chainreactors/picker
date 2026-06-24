---
title: WhatsApp VBScript活动使用假文档安装ManageEngine RMM工具
url: https://mp.weixin.qq.com/s/fmTQDlM7lNoFi763yARXQA
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:03:02.735401
---

# WhatsApp VBScript活动使用假文档安装ManageEngine RMM工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs8jCysRl1VlQIQiaztRkVhVvic9oKrJGvKUaaDonWprJ6ibrdj4fTlSTtbkqG39eBiaa2k0BN75z3qkFh98nHdxWggPoyXc2F9hxlQ/0?wx_fmt=jpeg)

# WhatsApp VBScript活动使用假文档安装ManageEngine RMM工具

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs8FmDmb8wtFXPVfqp3B8833TqibgrkhkTYKjD9bSCOLcXMUia2FgYgwD30PjLcI3ElhNv0z1QhuNj6cNQNSDscbOfej0jc5huico8/640?wx_fmt=jpeg&from=appmsg)

通过WhatsApp发送的直接消息被用来传播恶意的Visual Basic Script （VBScript）文件，导致安装合法的远程监控和管理（RMM）软件。

根据卡巴斯基的调查结果，活跃的攻击活动针对的是马来西亚、巴西、印度、墨西哥、新加坡、英国、西班牙、台湾、澳大利亚、俄罗斯和越南的WhatsApp Desktop和WhatsApp Web用户。据报道，受害者最集中的地区是马来西亚。

安全研究员法里德·拉齐说：“黑客利用具有欺骗性的文件名伪装成商业和财务文件，说服收件人下载并执行附件。”一旦执行，VBScript启动一个多阶段的感染链，最终导致安装合法的远程监控和管理（RMM）软件，使远程访问受害者的系统。

人们怀疑，该行动背后的威胁行为者设法秘密访问了几个WhatsApp账户，然后将其用作在其联系人之间传播VBScript文件的媒介。也就是说，这些账户究竟是如何被入侵的尚不清楚。

严重混淆的VBScript文件被伪装成看似无害的商业和财务文件，使用诸如“财务报告。vbs”或“账户报表。vbs”之类的名称；有些文件还以其他语言命名，如葡萄牙语、法语、德语和马来语，反映了该活动的全球性质

“此外，VBScript样本包含大量注释和元数据，旨在模仿合法的微软Windows Update组件，”卡巴斯基解释说。许多评论都是用中文写的，包括对Windows Update模块、证书验证、系统完整性检查和部署相关功能的参考。

使用“WScript.exe”启动VBScript文件，然后获取并运行下一阶段攻击所需的附加VBScript组件。值得注意的是，感染链的行为略有不同，这取决于受害者是使用WhatsApp Web还是WhatsApp Desktop应用程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs8L3BGfw0PlwDISzUjBqvLfYUgfibdnj0icXYD4wfw8W2qF4pTBFCMcWiaicYqXIhicup1ZHQuibnPns9YpAsVUtBKtqAQ3PniaQsibuIg/640?wx_fmt=jpeg&from=appmsg)

在前一种情况下，攻击依赖于用户将文件下载到他们的系统，然后从下载的文件夹或通过浏览器的下载历史打开它，假设它是一个合法的文档。在WhatsApp Desktop中，恶意软件直接在应用程序中执行，进程树显示与客户端应用程序相关的后台进程“WhatsApp. root .exe”负责生成“WScript.exe”。

VBScript的主要目标是从远程服务器下载两个次要的VBScript有效负载，其中一个试图篡改Windows用户账户控制（UAC）行为，而另一个下载并执行包含ManageEngine RMM Central安装包的ZIP文件。

该活动仍未确定原因，然而，这家俄罗斯网络安全公司表示，它发现基础设施与先前与Gh0st RAT和ValleyRAT相关的活动有重叠（"202.61.160[.]201"）。

卡巴斯基说：“用户在通过WhatsApp收到意外附件时应保持谨慎，即使这些附件似乎来自已知联系人。”脚本和可执行文件类型，如VBS、VBE、EXE、BAT、CMD、JS和PS1，除非其合法性已被独立验证，否则不应打开。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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