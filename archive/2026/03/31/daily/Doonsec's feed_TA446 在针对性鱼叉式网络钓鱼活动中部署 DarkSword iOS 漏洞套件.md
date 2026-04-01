---
title: TA446 在针对性鱼叉式网络钓鱼活动中部署 DarkSword iOS 漏洞套件
url: https://mp.weixin.qq.com/s/hvxxw4AzXAQo-HAZuBZZ7g
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:19.688278
---

# TA446 在针对性鱼叉式网络钓鱼活动中部署 DarkSword iOS 漏洞套件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADsibX0gpJic4ZVibeIwiccJSTHXrLq5UnM3Y2T2rbCfHzAKJHfldhdicFx6PibaIK2HXsgXhqES1mYPm2We1Ixs3FkVhicexJ7xmE4WT5A/0?wx_fmt=jpeg)

# TA446 在针对性鱼叉式网络钓鱼活动中部署 DarkSword iOS 漏洞套件

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs8gQibZWD4siaQRMMT0jL7MnwrzzB4PvxdI6nVyGxKiajXmTJwpAwDA8DMFcjEjgW2dKZQZLic68cwTZBOj7Gadicrpe6DyqxPnia1BQ/640?wx_fmt=jpeg&from=appmsg)

Proofpoint披露了一项针对性的电子邮件活动细节，这些活动中与俄罗斯有关联的威胁行为者利用最近披露的DarkSword漏洞套件针对iOS设备。

这一活动被高度确定归因于俄罗斯国家支持的威胁组织TA446，该组织也被更广泛的网络安全社区追踪，名称包括Callisto、COLDRIVER和星暴（前称SEABORGIUM）。该机构被评估为隶属于俄罗斯联邦安全局（FSB）。

该黑客组织以发动鱼叉式钓鱼活动而闻名，旨在从目标那里获取凭证信息。然而，过去一年中，该威胁行为者发起的攻击针对受害者的WhatsApp账户，并利用各种自定义恶意软件家族窃取敏感数据。

Proofpoint和Malfors指出的最新活动涉及利用伪造的“讨论邀请”邮件，伪造大西洋理事会，通过DarkSword漏洞套件传播数据挖掘恶意软件GHOSTBLADE。这些邮件由被攻破的发件人于2026年3月26日发送。邮件收件人之一是俄罗斯著名反对派政治家、反腐基金会政治主任列昂尼德·沃尔科夫。

据称，Proofpoint的安全工具触发的自动分析被重定向到一份无害的诱饵PDF文档，这很可能是因为服务器端的过滤机制只引导iPhone浏览器访问该漏洞工具包。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs8rBTOH9urAPdN5kUtkgnLaEFhHgWI6iaQAhdRoPpamAEUIwt0HVlybus6cdzYvyjKVjl9ybACxlspRLW8jnzAYwZql4OicjCVKA/640?wx_fmt=jpeg&from=appmsg)

Proofpoint表示：“我们此前并未观察到TA446会针对用户的iCloud账户或苹果设备，但泄露的DarkSword iOS漏洞利用工具包的采用，使该行为者能够针对iOS设备进行攻击。”

这家企业安全公司还指出，过去两周该威胁行为方的邮件量“显著增加”，并补充说，这些攻击导致通过密码保护的ZIP文件部署了一个名为MAYBEROBOT的已知后门。

该组织使用DarkSword的事实也得到了证据，一台上传到VirusTotal的DarkSword加载器中提到了“escofiringbijou[.”。“com”，这是归因于威胁行为者的第二阶段域名。

一项 urlscan.io 结果显示，TA446控制的域曾为DarkSword漏洞套件服务，包括初始重定向器、漏洞加载器、远程代码执行以及指针认证码（PAC）绕过组件。然而，没有证据表明沙盒逃脱曾被实施。

据怀疑，TA446正在将DarkSword漏洞工具包重新利用用于凭证收集和情报收集，Proofpoint指出，邮件活动中的目标“比平时更广泛”，涵盖了政府、智库、高等教育、金融和法律实体。

这反过来又引发了威胁行为者利用DarkSword新能力作为对更广泛目标的机会主义行动的一部分。

Proofpoint的威胁研究员Greg Lesnewisch告诉《黑客新闻》，这次攻击很可能利用了DarkSword的泄露版本，该版本直接从UNC6353的一个水源中获取并上传到GitHub，并且“TA446使用的是UNC6353之前使用的同一版本的漏洞工具包。”目前尚不清楚这些攻击是否成功。然而，Proofpoint表示，所有针对其客户的消息都被屏蔽了。

此举正值苹果开始向运行旧版iOS和iPad的iPhone和iPad发送锁屏通知，提醒用户网络攻击并敦促他们安装更新以阻挡威胁。这一不同寻常的举措表明，苹果已将其视为足够广泛的威胁，需要用户立即关注。

苹果的警告也与GitHub上新版本DarkSword泄露同时发生，引发了人们对其可能民主化国家级漏洞利用的担忧，从而从根本上改变移动威胁格局。

Lookout首席研究员贾斯汀·阿尔布雷希特表示，泄露的即插即用版本甚至允许不熟练的威胁行为者部署先进的iOS间谍工具包，将其变成商品恶意软件。

“DarkSword驳斥了普遍认为iPhone免疫网络威胁，高级移动攻击仅用于针对政府和高级官员的定点行动，”Albrecht补充道。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

HackSee安全生活

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