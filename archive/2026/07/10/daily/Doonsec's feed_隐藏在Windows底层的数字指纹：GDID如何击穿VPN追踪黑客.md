---
title: 隐藏在Windows底层的数字指纹：GDID如何击穿VPN追踪黑客
url: https://mp.weixin.qq.com/s/lQSxsT4RHccfe8CHtD58PA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:39.448198
---

# 隐藏在Windows底层的数字指纹：GDID如何击穿VPN追踪黑客

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2FnicQlnblCz5ceusibibicpAvSKqQMrKzkC7tQgy3tmLm0Lib9X1Q4AFQn93FicckViayQmvqXOKnILHpJuTDHaUTsk5Nttse12lwAc/0?wx_fmt=jpeg)

# 隐藏在Windows底层的数字指纹：GDID如何击穿VPN追踪黑客

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3pFvgq8l6rGuTAHv0nMeHWPEp0NtCmaHWl8tjb6iatwEAHrR099IWyIpOm999uwick4pVA3C9GJjIjiaicjUKYU9tu8R7t4myaJm0/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3B21x2K2fcLcPBettsIkPYiaDib9ljYKbLMw2pPlicGUicKuvAbKC3IoFO1Bcib0HBSfLPbhDhwOUtRn1UVQzXuNB6eqPe84TYj2kM/640?wx_fmt=png&from=appmsg)

2026年4月，一名19岁男子携带两块2TB硬盘和一张飞往日本的机票出现在赫尔辛基机场。他最终未能成行。芬兰警方根据国际刑警组织的红色通缉令将其拦下。同年7月，美国检察官公布了一份联邦起诉书，确认此人为彼得·斯托克斯，据称是“散落蜘蛛”（Scattered Spider）黑客组织的成员。该组织因涉嫌于2025年5月入侵一家美国奢侈珠宝零售商的系统并勒索800万美元而被通缉。

彼得·斯托克斯为什么会落网？正是微软向FBI提供了追踪斯托克斯Windows电脑跨越VPN、代理服务器和三个国家行踪的方法。这个工具叫做**全局设备标识符（GDID）**，除了少数企业文档页面外，大多数Windows用户在此案曝光之前从未听说过这个词。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2uIGpNibt9E7oXmibX8XR8P9sj2pp3OaaXHmsrENH7qCdfZ5WtZ50oHiaselchOsny7kicKheo0hbkcicBoB4MHMGMBgzTvia2sY2Xk/640?wx_fmt=jpeg&from=appmsg)

Part01

## GDID 是什么？

投诉中引用了一位微软代表的话，他将 GDID 描述为*“一种持久的设备级标识符，旨在跨某些微软服务和场景，唯一地标识设备上的 Windows 操作系统安装”。*

**全球设备 ID (GDID) 是一个永久性的唯一数字指纹，当您安装 Windows 或登录 Microsoft 帐户时，Microsoft 会自动将其分配给您的计算机。**

微软利用它来管理软件许可和Windows应用商店应用，但由于它会将你在该计算机上的所有在线活动与单一身份关联起来，执法部门可以利用它在互联网上追踪设备的真正所有者。

它能经受住 Windows 更新的考验，但无法经受住全新安装的考验。微软在投诉中的脚注也承认，“一个微软用户在一个账户的生命周期内可能拥有多个 GDID”。

微软解释了GDID的作用，但并未说明它在Windows系统中的具体位置。为此，独立研究人员不得不进行逆向工程，因为微软在Azure Monitor交付优化报告参考文档中仅发布了一句话关于GDID的内容，其中名为GlobalDeviceId的列仅被描述为“Microsoft全局设备标识符。这是Microsoft内部使用的标识符。”

Part02

## Windows如何生成GDID

## 真正的链条是从微软账户服务开始的。

##

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX29jsJMF6LWJFicrZ3JIYjfNkVq5nUb8VicEia5ia1bQ9k68kHdj91NFcS4ALd48eBtOFiaCkToj9Kzvraor3aagLGtX1MUeicq9xCIc/640?wx_fmt=jpeg&from=appmsg)

##

当 Windows 使用 Microsoft 帐户配置设备时，名为 wlidsvc 的系统服务会与 login.live.com 通信，并在服务器的 SOAP 响应中获取 Microsoft 所称的设备 PUID（Passport 唯一标识符）。该 ID 由服务器分配，Windows 不会在您的电脑上进行本地计算。它接收的是一个字符串并将其存储。

PUID（用户标识符）以纯文本形式存储在注册表单元 HKCU\SOFTWARE\Microsoft\IdentityCRL\ExtendedProperties 下，值为 LID。连接设备平台会读取该 PUID 并将其注册到 Microsoft 的设备目录服务中。该服务是 Microsoft 所有跨设备功能背后的身份图谱。

注册后，PUID 前面会添加一个小写字母 g，并以 g:decimal 的形式写入。每次您的电脑进行点对点数据共享或下载更新数据时，交付优化都会将该值以 UCDOStatus.GlobalDeviceId 的形式回传给 Microsoft 服务器。

也就是说，使用微软帐户登录 Windows，服务器会为您的 Windows 安装分配一个永久 ID 号。Windows 会将此 ID 号存储在本地，多个后台服务会读取它，同时你的电脑向微软上报的活动信息中也会附带这条标记数据。

重新安装 Windows 后，你会得到一个新的号码，但微软自己的记录完全有理由将新号码通过同一个帐户、OneDrive 和激活历史记录与旧号码关联起来，这与 Stokes 的情况非常相似。

Part03

## FBI如何利用GDID抓获斯托克斯

斯托克斯被抓是因为他所有操作都使用同一台 Windows 设备，而 GDID 事后将所有数据拼接了起来。

Scattered Spider 成员使用 Google Voice 号码致电这家珠宝零售商的 IT 服务台，冒充被锁在系统外的员工，诱骗支持人员重置了三个账户，其中两个账户拥有管理员权限。之后，他们安装了一款名为 ngrok 的隧道工具，绕过了零售商的网络防御，并使用 ngrok 和另一款名为 Teleport 的工具将大约 77 GB 的数据迁移到了亚马逊云存储。

他们试图部署勒索软件但失败了，随后发送了一封主题为“重要：我们窃取了数据，请立即联系”的勒索邮件。他们索要 800 万美元的加密货币赎金。零售商拒绝了他们的要求，承担了大约 200 万美元的清理费用，然后继续进行其他攻击。

调查人员随后传唤了 ngrok，发现攻击中使用的账户创建于 2025 年 5 月 12 日 19:21 UTC，注册地址为托管服务提供商 Tzulo 运营的 VPN 代理 IP 地址。该 IP 地址是死路一条。VPN 代理通常会这样做。但 GDID 的构造方式不同。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3LpuXDkiaOUn59d9nKjicgWkYM36Z5CicLp28EUzxXNEc7UNkl5arLZzAVNf4ge6rHpMA7tQdVbOWCiaclpezPibMz23ticvPjOdHqM/640?wx_fmt=png&from=appmsg)

微软的记录显示，就在同一分钟，一台GDID为g:6755467234350028的Windows设备访问了ngrok注册页面。三小时后，同一GDID通过与注册ngrok账户时相同的Tzulo代理地址访问了该零售商的网站。这使得FBI掌握了该设备的信息，而该设备不会像VPN出口节点那样轮换使用。

调查由此进入了串联线索的阶段。调查人员掌握了该设备使用过的所有IP地址的时间线后，将其与检察官此前怀疑属于斯托克斯的已知账户登录信息进行交叉比对：

* **2024年6月4日，** GDID的设备使用了位于爱沙尼亚塔林的IP地址，而斯托克斯就居住在那里。四分钟前，同一个IP地址登录了他的Snapchat账户；大约80分钟后，又登录了他的Facebook账户。
* **2024年11月17日和18日**，同一台设备出现在纽约的一个IP地址上，该地址与斯托克斯的一个苹果账户和他的Snapchat账户的登录记录相符。几周后，**11月26**日，同一台设备访问了纽约帝国酒店的网站，这与斯托克斯的另一次已确认的行程相吻合。就在前一天，他发布了一张Snapchat照片，调查人员将照片中的地毯和墙纸等细节与帝国酒店套房的公开宣传照片进行了比对。
* **2025年2月2日**，该设备出现在一个位于泰国的IP地址上，再次与他的苹果和Snapchat账号匹配。前一天，斯托克斯在Snapchat上发布了一张照片，标题为“曼谷华尔道夫酒店”。
* **2025年1月8日**，同一台设备（此时已恢复使用爱沙尼亚IP地址）登录了手机游戏《Growtopia》。此前一天，该IP地址曾访问过斯托克斯的一个苹果账户，两分钟后又访问了一个与该《Growtopia》登录关联的育碧账户。

当然，单独来看，这些活动似乎都没什么可疑之处。真正令人怀疑的是，同一个GDID和同一个Windows物理安装，在长达八个月的时间里，在四个国家反复出现，而且出现的时间点都与调查人员已知的斯托克斯账户完全一致。

Part04

## 事件仍令隐私研究人员担忧

根据司法部的数据，斯托克斯和“散落蜘蛛”组织的其他成员被指控犯有100多起企业入侵罪行，并支付了超过1亿美元的赎金。这套系统在这里发挥了预期作用。

令研究人员感到不安的是此案揭示的其他一切。知名恶意软件研究员科斯汀·雷乌 (Costin Raiu) 在“三友难题”(Three Buddy Problem) 播客节目中提出疑问：其他平台上存在多少此类问题？这些问题是否与硬件存在更持久的关联？另一位安全研究员马修·希基 (Matthew Hickey) 则将 Windows 称为“监控软件”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NuOonpsW017D9dS3hdkHXdfrDkyM5vxDicuDh43KK6L3UDUW2SAibo5ylxwWRmib34SvmemLW31RbdhHmLBHoiagSyd21I2mo0RQ/640?wx_fmt=png&from=appmsg)

两件事可以佐证这一点：

1. 没有同意屏幕。登录 Microsoft 帐户时，系统会自动分配一个 GDID。苹果的广告标识符需要应用跟踪透明度提示和可见的重置步骤；安卓的广告标识符也一样。GDID 既没有这些提示，也没有重置步骤，而且重新安装 Windows 只会获得一个新的 GDID，微软仍然可以将其恢复到同一个帐户。

2. 接下来是激活问题。微软激活脚本背后的团队 Massgrave 指出，Windows 安装程序会将硬件信息发送给微软，并接收返回的标识符，这些标识符之后会用于应用商店访问和许可：“如果不破坏激活和 UWP 应用，就无法阻止 Windows 获取 GDID。” 任何在更换主板后丢失许可证的人都已经遇到过类似的情况。

所有主流操作系统都会保留一些持久的设备身份信息，而且所有厂商都可能被传唤。但微软的不同之处在于其可视性和控制力，而Windows在这两方面都逊于苹果和谷歌的平台。

Part05

具体建议

重装系统并非人们通常认为的解决方法。虽然你会获得一个新的 GDID，但如果你登录的是同一个微软账户，微软完全有理由将其与你之前的活动关联起来。以下几点或许更有帮助：

* 请使用本地帐户而非 Microsoft 帐户，但我们也意识到，现在要绕过 Microsoft 帐户登录有多么困难。幸运的是，微软正在努力简化这一过程。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0PeT4RvPFO4wEzco9Ej6PnK2kUgahdaSCwKGZiacFAia2JicIRWNPM5k2a3EtOQu4JEaoqkCHOicPv8Ir5j5yhaA6VQPKacts5bME/640?wx_fmt=png&from=appmsg)

* 关闭“活动历史记录”，方法是：**“设置”>“隐私和安全”>“活动历史记录”**。此设置还会启用“手机连接”和“跨设备连续性”功能，这可能会带来一些不便。
* **在“设置”>“隐私和安全”>“诊断和反馈”**下，关闭可选的诊断数据。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1wSicc9nS7Sh2tESdJiajzBbeWHibBjGcoaxYMDKZWvgK195GPfRS7IVgJ6ptoCkKPVEagCydGcXiaDrjVhqjQKLMlsVvMk79RuXE/640?wx_fmt=png&from=appmsg)

* 请参阅指南，了解如何从 Windows 11 中移除不需要的 AI 功能和后台服务。
* 对于新闻报道、社会活动或家庭暴力案件，请避免使用 Windows 系统，而应使用通过 Tor 路由的 Linux 系统，而不是商业 VPN。GDID 并不关心你使用哪个 VPN，它只关心你使用的是同一个 Windows 系统。

Part05

## 最后

一个十几岁的少年吹嘘自己戴着拼出“黑地球”字样的钻石项链，并以此勒索珠宝店，整整三十五页的案卷记录着这一切，无论微软的遥测数据在案件侦破中扮演了什么角色，都很难让人对他产生同情。

但这并不意味着GDID就是合理的。所有销售软件的公司都使用某种形式的GDID，而将持久设备身份信息集成到激活和反欺诈系统中也是合情合理的。

在像这样的联邦法院诉讼之前，大多数人甚至从未听说过GDID这个术语。微软在Azure Monitor参考表中只用一句话提到了它，而这个参考表是为提取更新报告的企业IT管理员准备的，而不是为大约16亿使用电脑生成这些数据的普通用户准备的。

你或许技术娴熟，能够关闭活动历史记录、选择本地帐户并删除所有可选的遥测数据，但这都无法改变标识符存在的事实，也无法改变它实际上对应着你的微软帐户而非你本人的事实。微软直到法院强制要求后才向公众披露此事。

参考来源：

# You can’t fully disable Microsoft’s GDID Windows 11 tracker, but these settings limit what it captures

https://www.windowslatest.com/2026/07/10/you-cant-fully-disable-microsofts-gdid-windows-11-tracker-but-these-settings-limit-what-it-captures/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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