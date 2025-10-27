---
title: “蓝屏事件”阴魂不散，微软安全更新导致Linux系统无法启动
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546571&idx=3&sn=998ed56697d8b4692164f8da9c9fe4a5&chksm=fa93800acde4091cf1d6d85596f294d17a3944f50ae577ddbd9cfd944f46bdcf1255bc944d06&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-24
fetch_date: 2025-10-06T18:05:39.819931
---

# “蓝屏事件”阴魂不散，微软安全更新导致Linux系统无法启动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mxzrSiaf7o2PBUQUCuN4LWojXHj9RC9zibRgqbOYGWDBZdLibicxxBP7j0RvjIpoYgDVVavyoDo15KUQ/0?wx_fmt=jpeg)

# “蓝屏事件”阴魂不散，微软安全更新导致Linux系统无法启动

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mxzrSiaf7o2PBUQUCuN4LWokEvibqkibLhZEZKKfRyUh3DB9IIZUibOLbLvJ33cGPgPxTRwhffHAcuMA/640?wx_fmt=png&from=appmsg)

最近，众多Linux用户报告称他们的设备在尝试启动时，收到了一条神秘的错误消息：“系统出了严重问题。”这起事件的罪魁祸首是微软在月度安全更新中发布的一个补丁，用于修复一个存在已久的GRUB漏洞。

这次更新却导致了Linux和Windows双系统设备的启动问题，引发大量用户投诉和抱怨。

**Linux/Windows双系统“躺枪”**

新发现的漏洞编号为CVE-2022-2601，最早于2022年被发现，其漏洞评分高达8.6分（满分10分）。该漏洞允许攻击者绕过安全启动机制，进而可能在启动过程中加载恶意软件。尽管该漏洞早在两年前便已被披露，但微软却迟至本月才发布补丁。然而，这次修复的副作用让许多Linux用户措手不及。

**多款Linux发行版受影响**

此次更新对运行双系统的设备带来了严重影响，特别是那些同时运行Windows和Linux的用户。用户报告称，当他们尝试加载Linux系统时，收到如下错误信息：“验证shim SBAT数据失败：安全策略违规。”相关的讨论和支持论坛瞬间被用户抱怨的声音所淹没，受影响的发行版包括Debian、Ubuntu、Linux Mint、Zorin OS和Puppy Linux等。

微软发布的公告原本声称该更新仅适用于运行Windows的设备，且不会影响双系统设备。然而，事实证明，许多运行较新版本Linux的设备同样受到了影响，包括Ubuntu 24.04和Debian 12.6.0等最新发行版。

**用户自救解决方案**

面对微软的沉默，受影响的用户不得不自行寻找解决办法。最直接的方法是进入EFI面板并关闭安全启动功能。然而，对于注重设备安全性的用户而言，这一选项可能并不可行。另一种临时解决方案是删除微软推送的SBAT策略，这能够让用户保留部分安全启动的保护功能，同时避免由于CVE-2022-2601漏洞而导致的攻击风险。

具体步骤包括：

1. 禁用安全启动
2. 登录Ubuntu系统并打开终端
3. 使用命令删除SBAT策略：

Select all

sudo mokutil --set-sbat-policy delete

1. 重启并重新登录Ubuntu以更新SBAT策略
2. 再次重启并在BIOS中重新启用安全启动

**安全启动的局限性**

此次事件暴露了Windows安全启动机制的诸多问题。尽管安全启动旨在保护操作系统免受恶意软件的威胁，但近年来，研究人员已经发现了至少四个漏洞，足以破坏这一安全机制。最近的一次漏洞利用甚至影响了超过200款设备型号，证明了安全启动机制的脆弱性。

安全分析师Will Dormann指出：“尽管安全启动的初衷是让Windows的启动更加安全，但它似乎正逐渐暴露出越来越多的缺陷，无法完全兑现其应有的安全保障。”这一观点也得到了业界的广泛认同，安全启动的复杂性和微软在这一机制中的核心角色，使得任何漏洞都可能给Windows设备带来致命的安全隐患。

**参考链接：**

https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2022-2601

原文来源：GoUpSec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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