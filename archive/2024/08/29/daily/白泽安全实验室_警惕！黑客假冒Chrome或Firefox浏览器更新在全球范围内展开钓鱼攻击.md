---
title: 警惕！黑客假冒Chrome或Firefox浏览器更新在全球范围内展开钓鱼攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492295&idx=1&sn=8226c6aa935bbfea48f569ea6ad95a83&chksm=e90dc8edde7a41fb3885ae82897c0de2ea698ffee44d2885ce704185d81486e3283cfca4af3a&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-08-29
fetch_date: 2025-10-06T18:06:02.212078
---

# 警惕！黑客假冒Chrome或Firefox浏览器更新在全球范围内展开钓鱼攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 警惕！黑客假冒Chrome或Firefox浏览器更新在全球范围内展开钓鱼攻击

BaizeSec

白泽安全实验室

**事件概述：**

近期，网络安全厂商AhnLab发现并分析一种新型恶意木马程序代码后，确认了伪装成浏览器更新的恶意木马程序正在向不特定的大量用户传播。该恶意木马程序通过受感染的网站传播，如果用户访问受感染的网站，就会加载恶意脚本。恶意脚本会生成Chrome或Firefox等浏览器更新窗口，并引导用户直接下载恶意文件并执行。这一行为正在全球范围内迅速传播，对用户的网络安全构成严重威胁。

**攻击过程分析：**

该恶意木马的传播主要通过感染的网站进行。用户在不知情的情况下访问这些网站，恶意脚本随即被加载。这些脚本模仿Chrome或Firefox等主流浏览器的更新提示，诱使用户点击并下载伪装的更新文件。这些文件可能具有EXE、ZIP、APPX等格式，而最新的变种甚至使用了VHD（虚拟硬盘）格式。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPoI3mibB2MOtyljW6Xx59PmfVTawRuXtnicmLh0ch7qhxJut43HRjq6YnMoyGK37720zUuNXQd4a9g/640?wx_fmt=png&from=appmsg)图 1 攻击示意图

下载的VHD文件是磁盘映像文件，当用户执行该文件时，它将以虚拟驱动器的形式挂载并运行。VHD内部包含一个恶意的LNK（快捷方式）文件，该文件利用PowerShell命令执行无文件（FileLess）攻击，即直接在内存中执行恶意代码，而不在磁盘上留下可追踪的文件痕迹。

在VHD内部，攻击者放置了一个名为MOC.hta的文件，该文件同样采用无文件技术，通过PowerShell执行，进一步加载和执行恶意代码。此外，攻击者还使用了名为Cloud.bat的脚本，该脚本从外部资源库下载并执行其他恶意组件，增加了攻击的隐蔽性和复杂性。

攻击者还在这一过程中利用了外部资源库，这种利用正常服务进行恶意代码传播的策略正在增加。攻击者通过这种方式可以更有效地规避传统的安全检测机制，实现长期潜伏和控制。

**安全防护建议：**

为了提高网络安全防护，建议用户采取以下措施：

* 定期更新操作系统和浏览器至最新版本，以修复已知的安全漏洞。
* 使用可靠的安全软件，并保持其更新，以检测和阻止恶意代码。
* 对下载的文件进行彻底的病毒扫描，特别是在执行之前。
* 增强对钓鱼攻击的警惕性，避免点击不明链接或下载来源不明的文件。

**附件：Ioc指标**

MD5

1369fd10f66d0ab867aab559253b01e4

5714c27e55d82b9ff9d92c04eee9570e

7ed0b7e22f568d2eedaf956ba831d0a6

URL

https[:]//bitbucket[.]org/shakespeare1/center/downloads/BrowserUpdater[.]vhd

https[:]//bitbucket[.]org/shakespeare1/gna/downloads/Lwrctogck[.]dat

https[:]//github[.]com/BrowserCompanyLLC/-12/releases/download/semtag/Cloud[.]bat

https[:]//github[.]com/BrowserCompanyLLC/-12/releases/download/semtag/MOC[.]hta

https[:]//redr[.]me/g3boil/

参考链接：

https://asec.ahnlab.com/ko/82620/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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