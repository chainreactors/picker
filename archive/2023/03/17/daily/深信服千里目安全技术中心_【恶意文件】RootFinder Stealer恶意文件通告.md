---
title: 【恶意文件】RootFinder Stealer恶意文件通告
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247517938&idx=1&sn=a95b899133066f51de0e7f0e0ee1411d&chksm=ce460de2f93184f4574567099f2eea438034ae81aeee19c370503c510bc5a6e383f66f037cff&scene=58&subscene=0#rd
source: 深信服千里目安全技术中心
date: 2023-03-17
fetch_date: 2025-10-04T09:53:14.693765
---

# 【恶意文件】RootFinder Stealer恶意文件通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSrd0kvt0u8VPnKKrh8Nkh9yZ4qNsCTJfVBAIpibmp76RsIOiaZBYensMA/0?wx_fmt=jpeg)

# 【恶意文件】RootFinder Stealer恶意文件通告

深盾研究实验室

深信服千里目安全技术中心

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSh2w6RbsAlvZ7sytEfrhibiclsS9txicZ539RA2RH8lNH8yqZI4TSY1meQ/640?wx_fmt=gif)

**恶意家族名称：**

RootFinder

**威胁类型：**

信息窃取

**简单描述：**

RootFinder 是一款基于 .NET 的窃密工具，该程序使用了 .NET Reactor进行多次混淆，运行时可以窃取主机信息和数十款浏览器的敏感信息、FTP账号密码等数据。

**恶意文件分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHStIwMkC51Qf5VlQCujrO26g6HLmrQLdC6IavPRAWuyrxBia4tjMgLT7Q/640?wx_fmt=gif)

**恶意事件描述**

近日，深信服深盾终端实验室在运营工作中捕获到一款新型信息窃取病毒，该病毒由 .NET 语言编写，套用了开源软件 StormKitty 的部分代码。经过分析发现该病毒功能尚不完善且手法相对简单，该窃密程序已在黑客论坛售卖，后续可能还会持续更新。

大多数计算机感染源于用户打开恶意电子邮件附件、点击有害链接或从不可信的来源下载文件。攻击者还使用特洛伊木马、虚假安装程序、虚假软件更新和类似方法来诱导用户并感染他们的计算机。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHStIwMkC51Qf5VlQCujrO26g6HLmrQLdC6IavPRAWuyrxBia4tjMgLT7Q/640?wx_fmt=gif)

**恶意事件分析**

**MITRE ATT&CK**

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSqP2NnT7wSk2ugCmhrlOQc9zQvWLqziaCYPYNL996bfeuianBG5YDXjvw/640?wx_fmt=png)

**解混淆**

首先查看文件的信息，发现是.NET写的32位程序，拖进dnspy发现存在混淆，使用de4dot经过多次解混淆之后查看该文件：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSYkS61dlSPNg2Ea3eRMsAJ4zibdzkvY21tZjkhXrrZrtUtVvCyKuryrQ/640?wx_fmt=png)

**收集ARP信息**

首先通过cmd执行arp -a命令收集主机arp信息

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHS9LscvT4ZAyKKwK6H7zSEcBic4kgNibniaPMXqZo3uHS528ajicAiaSl6JdQ/640?wx_fmt=png)

**收集FileZilla信息**

通过读取 recentservers.xml 和 sitemanager.xml 两个文件的内容获取ftp服务器账号密码。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSRJicibG6Iz6lQabX4AlL4oVkVZChxSvVibsqDHiaUSNSOBMxtrA3azkl2A/640?wx_fmt=png)

之后将收集到的信息写入到C:\Wondows\Hosts.txt中。

**收集主机信息**

使用通过WMI接口获取计算机CPU和显卡信息，之后与主机名，用户名进行拼接计算MD5：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSACn4d8Wx7wluM40ySARDpA1Wia6KhCIjQNSQUxRNSAqeEaJXBQZibYrQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHS1RLDVpibiaUJ6kzLZqbzQr3RkyzicZ1OIxs98LzED6mPyTsln88icRtRcg/640?wx_fmt=png)

收集主机反病毒软件信息

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSO1lSeRWYVp6n19mFAONwNQcREAyGicyNExM2sjpjehr72YVibibGdGlOQ/640?wx_fmt=png)

此外还包括：系统语言、公网IP、系统时间、操作系统和系统版本、内存大小、磁盘系列号、BIOS信息、MAC地址、子网扫描、内网IP。

**收集浏览器信息**

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSh44R61Ojx8N355Av2RDAw9ZkjicXv7VO66a64EDqyxlpMTgCTEE7JQg/640?wx_fmt=png)

包括Opera、Google Chrome、MapleStudio ChromePlus、Iridium、7Start、CentBrower、Chedot、Vivaldi、Kometa、Element Browser、Epic Privacy Brower、uCozMedia、Chromium、Sleipnir、Citrio、Coowon、liebao、QIP Surf、Orbitum、Comodo、Amigo、Torch、Yandex、360Browser、Maxthon3、K-Melon、Sputnik、Nichrome、CocCoc、Uran、Chromodo、Atom、Brave-Browser、Edge，FireFox、WaterFox、Thunderbird、IceGragon、Cyberfox、BlackHaw、Pale Moon等众多浏览器保存的账号密码、cookie、搜索历史、信用卡等信息，此时收集到的信息将被保存到C:\Windows目录下的众多txt中。

**发送数据**

收集到的信息将以明文的形式发送到 Telegram 机器人中：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSyRtjQwzHpiafx16niaWTsTfZgIriciczziaJZNrIia4iaqZnHTBtgH5ia55jZg/640?wx_fmt=png)

文件同样会被使用POST的方式发向Telegram，随后删除保存的txt文件

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSic8NicSlkntJByBKoAcmeLtGzqEBYfs4fYY3EGouVt7hrSUy0yU0MPGQ/640?wx_fmt=png)

病毒运营者自述可以获取游戏客户端（Steam，Minecraft）账号，但在分析调试的时候暂未发现相关代码调用。

**解决方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHStIwMkC51Qf5VlQCujrO26g6HLmrQLdC6IavPRAWuyrxBia4tjMgLT7Q/640?wx_fmt=gif)

**深信服解决方案**

**【深信服终端检测响应平台EDR】**已支持查杀拦截此次事件使用的病毒文件，请更新软件（如有定制请先咨询售后再更新版本）和病毒库至最新版本，并接入深信服安全云脑，及时查杀新威胁；

**【深信服安全运营服务】**通过以“人机共智”的服务模式帮助用户快速提高安全能力。针对此类威胁，安全运营服务提供安全设备策略检查、安全威胁检查等服务，确保第一时间检测风险以及更新策略，防范此类威胁。

![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5wZEaGcnWo3bJdhyj6bGMHSia5cEqk5t6aJJA21Vo7IicX43SWyJjCrrFMoWNE3PlDJIhbVE64eNdYQ/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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