---
title: 黑客冒充 Google Ads 中的 Node.js 安装程序来部署信息窃取恶意软件
url: https://mp.weixin.qq.com/s/Itqrg6g-oeZgbzIAq9cOkw
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:47.486701
---

# 黑客冒充 Google Ads 中的 Node.js 安装程序来部署信息窃取恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MicLnbuUAxyjDIibG0KUfjVpMTRWBVp3vTlfHibJiboy9t1Pej6Mrof84Xd4ZAWgPWgRUOZpwuRYtgNHam9JvorCAiaTjzEErgtW98/0?wx_fmt=jpeg)

# 黑客冒充 Google Ads 中的 Node.js 安装程序来部署信息窃取恶意软件

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

黑客利用虚假的谷歌广告来推送一种全新的恶意软件加载器，该加载器伪装成流行的 Node.js 安装程序。

该活动一直积极针对美国的 Windows 用户，只需点击一次看似合法的赞助搜索结果，就会悄悄地将危险的信息窃取程序植入他们的电脑。

此次攻击利用了数百万用户每天都会做的一件事：在线搜索软件并信任搜索结果排名靠前的部分。攻击者搭建了一个恶意登录页面，使其看起来像是官方的Node.js平台。

当受害者点击赞助广告时，他们会被悄悄地通过中间域名重定向到合法的云文件共享服务，下载托管在云文件共享服务上的恶意 Windows 批处理脚本，这使得安全工具更难将其标记出来。

Elastic Security Labs 的研究人员发现了这一活跃的网络攻击活动，并确认其目标是他们自己的一位客户。

Elastic Security Labs 在一份与网络安全新闻 (CSN) 分享的报告中表示，该加载器（现名为 OXLOADER）此前未曾公开记录，并且在静态防病毒引擎和自动化沙箱环境中的检测率都非常低。

该活动通过谷歌广告进行，恶意广告商账户注册时使用了与乌克兰相关的已验证姓名。

该广告最后一次出现是在 2026 年 4 月 23 日，到 2026 年 5 月 14 日，谷歌已完全删除了该广告商及其所有相关广告系列。

此次攻击尤其令人担忧的是，攻击者能够如此无缝地融入受信任的平台，在不引起警报的情况下投放恶意载荷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7OLaoMiaVHIAAKYOh55iclKy7c2v7UZhYxVdsiaTR8EH671cuGsWANmeicpUHOXia3HWicwXx20Vp58PFuqrmAheESmm9B5B9YkcfdDA/640?wx_fmt=png&from=appmsg)

通过该链传递的最终有效载荷是一个名为 CASTLESTEALER 的信息窃取程序，它是一种基于 .NET 的恶意软件，能够从受感染的系统中窃取敏感数据。

安全团队应格外谨慎地对待开发者工具的赞助搜索结果，确保终端行为检测处于激活状态，而不是仅仅设置为监控模式，并且始终直接在官方供应商网站上验证软件下载。

# 黑客在谷歌广告中冒充Node.js安装程序

当用户搜索 Node.js 安装程序并点击广告链接时，感染链就开始了。该点击会将受害者引导至一个伪造的登录页面，该页面旨在模仿真实的 Node.js 环境。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7Puq7PRLeAhKZL2ag6pibML2OqWicEwXOVibrDaJV3EA2XSdeU0EMAQQHq81tfZZawEQN7eqcXIq7N6hsvoWzhvicUQ2IHJCc2s2Qg/640?wx_fmt=png&from=appmsg)

从那里，通过中间域重定向，将批处理脚本传递到 Storj，这是一个合法的云存储服务，威胁行为者故意滥用该服务来绕过基于信誉的过滤。

该批处理脚本更进一步，显示了一个逼真的虚假软件安装向导，让受害者没有任何理由怀疑存在任何问题。

在这个界面背后，它会使用 PowerShell 静默下载下一阶段的可执行文件，并触发 Windows 用户账户控制提示以获取提升的系统访问权限。整个过程旨在模拟常规软件安装体验。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7Prb8jg8PeD5YicFg7nPm9jlCwdGdHZOlV0FD7zjVuXYKyibxZPH6pX8Pa5ia22nwmfAqOVVJjibGFuG2JcHiclHbZXDibnvUVGicQ7ok/640?wx_fmt=png&from=appmsg)

2026 年 5 月 13 日，又发现了 OXLOADER 的第二个变种，这次它伪装成 Node.js 安装程序二进制文件而不是 API Monitor，尽管其底层加载机制完全相同。

研究人员注意到，该文件的文件名中保留了“node”一词，这很可能是为了保持该活动一直以来所依赖的诱饵主题。

# OXLOADER 如何逃避检测

OXLOADER 的核心功能之一就是规避。在执行任何有意义的操作之前，它会运行五项独立的检查，以确认自身并非运行在沙箱或虚拟机中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PiavdGznk80xiaG2pUhFRbHTVOQFqtw7oxgeo69iaYF3Ohg3FwibsHfF81ES2AVy8wWdCHMjZibicsT6WUcsYtuPg2IHzzJHcpuDgXI/640?wx_fmt=png&from=appmsg)

这些检查包括：至少三个 CPU 核心、至少 3 GB 物理内存、20 Hz 以上的显示刷新率，以及验证系统是否位于独联体地区或配置为俄语。

该加载器还使用了复杂的混淆技术，可以破坏标准的二进制分析工具，使逆向工程变得缓慢而困难。

它将恶意代码隐藏在 Windows 的 .reloc 段中，而合法程序永远不会使用该段来存放可执行指令，并且它使用自修改解密例程将自身解包到内存中。

最终的有效载荷 CASTLESTEALER 完全通过名为 DonutLoader 的开源 shellcode 生成器在内存中交付，几乎不会在磁盘上留下任何痕迹。

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