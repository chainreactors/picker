---
title: 大众80万用户数据泄露，工信部预警SafePay病毒 | 一周特辑
url: https://mp.weixin.qq.com/s?__biz=MzAwNTgyODU3NQ==&mid=2651130203&idx=1&sn=cf7af82f0381e4261d07bd511a68c140&chksm=80e713ebb7909afd5d7107cc20927c0776c8801c26ff5aa049fb23dd2b78d2e11e2b33295202&scene=58&subscene=0#rd
source: 威努特安全网络
date: 2025-01-05
fetch_date: 2025-10-06T20:08:14.539234
---

# 大众80万用户数据泄露，工信部预警SafePay病毒 | 一周特辑

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vEkwp3V9UtuzK7wTQxc9bnCH1n1TUHl9bmGkp4PjQ7VEjPyHr8BpNmgBbUCbatULa5M9oUrXT7OibvWwnS5DvNA/0?wx_fmt=jpeg)

# 大众80万用户数据泄露，工信部预警SafePay病毒 | 一周特辑

威努特安全网络

![](https://mmbiz.qpic.cn/mmbiz_gif/vEkwp3V9UtuzK7wTQxc9bnCH1n1TUHl97icwlX58dVXHPqyNXTysBibt0GEXlMib55yKLMYia0EFciampJofLLHJicaQ/640?wx_fmt=gif&from=appmsg)

**工信部发布关于防范**

**SafePay勒索病毒的风险提示**

近日，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）监测到一种名为SafePay的新型勒索病毒，其通过数据窃取和文件加密双重勒索机制开展攻击，可能导致数据泄露、业务中断等安全风险。

SafePay勒索病毒与LockBit勒索病毒密切相关，并深度借鉴INC和ALPHV/BlackCat等勒索病毒攻击策略。在数据窃取阶段，SafePay利用已知漏洞或弱口令实施攻击入侵，成功感染目标终端后，通过WinRAR、FileZilla等工具归档、盗取目标文件。在加密部署阶段，SafePay通过远程桌面协议（RDP）访问目标终端，利用PowerShell脚本实施文件加密、禁用恢复和删除卷影副本，对加密文件添加“.safepay”扩展名，并留下名为“readme\_safepay.txt”的勒索文件。在攻击过程中，SafePay会通过COM对象技术绕过用户账户控制（UAC）和提升权限，采用禁用Windows Defender、字符串混淆、线程创建、重复安装卸载工具等机制规避检测。

工信部建议相关单位及用户立即组织排查，加强RDP等远程访问的安全管理，使用强密码和多因素身份验证，实施全盘病毒查杀，及时修复已知安全漏洞，谨慎警惕来源不明的文件，定期备份重要数据，防范网络攻击风险。

**大众汽车泄露了80万用户数据**

大众汽车集团上个月发生了一起数据泄露事件，泄漏了其旗下品牌大约 800,000 名电动汽车车主的敏感个人信息，包括大众、奥迪、西雅特和斯柯达。

德国出版物 Speigel 报道，该漏洞是由于亚马逊云存储系统配置错误，该系统由软件子公司 Cariad 管理。据报道，该组织连续数月将个人和位置数据在网上公开访问，从而引发了泄露事件。

此次泄露中暴露的数据包括车辆位置信息，例如电动汽车的开关时间，以及车主的位置数据、电子邮件地址、电话号码和家庭住址。各种各样的人受到了此次泄露的影响，包括至少两名德国政治家和汉堡警方。虽然大多数受影响的车辆位于德国，但 Spiegel 聘请的研究人员还发现了位于挪威、瑞典、英国、荷兰、法国、比利时和丹麦的汽车详细信息。

Cariad 报告说，它迅速采取行动解决了这个问题，并在得知该事件的同一天关闭了访问权限。

**黑客入侵并窃取 ZAGG 客户的信用卡**

ZAGG 是一家消费电子配件制造商，以其移动配件而闻名。近日，ZAGG通知客户，在黑客入侵了该公司的电子商务提供商 BigCommerce 提供的第三方应用程序后，他们的信用卡数据已暴露给未经授权的个人。

根据发送给受影响个人的信件，攻击者破坏了 BigCommerce 提供的 FreshClicks 应用程序，并注入了窃取购物者信用卡详细信息的恶意代码：“我们了解到，一个不明身份的行为者向 FreshClick 应用程序注入了恶意代码，该代码旨在抓取在 2024 年 10 月 26 日至 2024 年 11 月 7 日期间某些客户线上交易结账过程中输入的信用卡数据。”

由于这次数据泄露，攻击者窃取了属于 zagg.com 购物者的姓名、地址和支付卡数据。针对此次事件，ZAGG 实施了补救措施，通知了联邦执法部门和监管机构，并安排受影响的个人通过 Experian 获得为期 12 个月的免费信用监控服务。ZAGG 尚未透露有多少客户受到此次安全漏洞的影响。

**拉斯维加斯报告网络攻击**

拉斯维加斯官员周二表示，网络攻击攻破了该市的计算机系统，但目前尚不清楚是否有任何敏感数据受到损害。

市政府发言人大卫·里格尔曼 （David Riggleman） 告诉《拉斯维加斯评论杂志》（Las Vegas Review-Journal），市政府官员在凌晨 4 点 30 分左右接到违规警报。里格尔曼说，该市的信息技术部门迅速做出反应，并正在采取“广泛措施”来保护该系统。

里格尔曼周二下午表示，该市仍在评估是否有任何城市或公共数据被访问。他说，拉斯维加斯将在一两天内更多地了解泄露的范围。

**新的网络攻击利用双击来入侵账户**

一种称为“DoubleClickjacking”的点击劫持攻击的新变体允许攻击者通过双击来诱骗用户授权敏感操作，同时绕过针对这些类型攻击的现有保护措施。

点击劫持，也称为 UI 补救，是指威胁行为者创建恶意网页，诱骗访问者点击隐藏或伪装的网页元素。这些攻击的工作原理是将隐藏 iframe 中的合法网页覆盖在攻击者创建的网页上。

多年来，Web 浏览器开发人员引入了防止大多数此类攻击的新功能，例如不允许跨站点发送 cookie 或对网站是否可以进行 iframe 引入安全限制（X-Frame-Options 或 Frame-ancestors）。但此类攻击仍然层出不穷并持续威胁用户的网络安全。

**Cyberhaven Chrome 扩展程序**

**遭黑客攻击**

网络安全公司 Cyberhaven 的 Chrome 扩展程序遭到入侵似乎是更广泛活动的一部分，而真正的目的是发动窃取用户数据的供应链攻击。在过去一年半中，该公司至少有 29 个扩展程序受到攻击。

作为 Cyberhaven 事件的一部分，威胁行为者获得了该公司 Chrome Web Store 管理员账户的访问权限，并发布了包含恶意代码的新版本扩展程序。该攻击于 12 月 25 日被发现，随后被该公司撤下并替换为不包含恶意代码的新版本。

但在此期间，恶意扩展程序还是被分发给启用了自动更新功能的用户，使他们面临敏感信息被盗的风险。恶意代码可能会窃取 Facebook 访问令牌、用户 ID 和账户信息。

**Palo Alto Networks 修补了**

**被用于 DoS 攻击的防火墙漏洞**

Palo Alto Networks 上周晚些时候通知客户，它已经修补了一个0day漏洞，该漏洞被用来对其防火墙发起拒绝服务 （DoS） 攻击。该安全漏洞被跟踪为 CVE-2024-3393，它影响了在 Palo Alto Networks 防火墙上运行的 PAN-OS 软件的 DNS 安全功能。该漏洞允许未经身份验证的攻击者通过数据平面发送特制数据包，从而导致防火墙重新启动。

威胁组织在攻击中利用 Palo Alto 防火墙漏洞的情况并不少见。在最近一次被安全公司跟踪为 Operation Lunar Peek 的活动中，恶意行为者利用两个 PAN-OS 零日漏洞入侵了大量防火墙。

**四信工业路由器漏洞被攻击利用**

漏洞情报公司 VulnCheck 警告说，已观察到威胁行为者利用 Four-Faith 工业路由器中的漏洞来部署反向 shell。被利用的缺陷被跟踪为 CVE-2024-12856（CVSS 评分为 7.2），被描述为可以远程利用但需要身份验证的操作系统命令注入问题。受影响的设备包括运行固件版本 2.0 的 Four-Faith 路由器型号 F3x24 和 F3x36。

根据 VulnCheck 的说法，已观察到攻击者使用 HTTP 上的 POST 请求修改系统时间参数。也有人在 2024 年 11 月观察到了第一批利用 CVE-2024-12856 的攻击，这些攻击至少来自两个不同的 IP 地址。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UtuzK7wTQxc9bnCH1n1TUHl9lvLRGC6LiaeICmUY28W2jUKNs258icmPmibBVSdIxNYOoibL1JhMwEvYdw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/vEkwp3V9UtuzK7wTQxc9bnCH1n1TUHl9ao0iaypUcMrBbtsDiaW96olVXia0UJbC34QyEtQALp3J84p9tR1yk4rQA/640?wx_fmt=jpeg&from=appmsg)

渠道合作咨询   田先生 15611262709

稿件合作   微信:shushu12121

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9Utvy3S0ykmxlskz7ythOsDsm6zNNibia3qASGEZwDcBXVAwThSasvpoWbn2NSVHiaFicF6G1G3HkrOarBA/0?wx_fmt=png)

威努特安全网络

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9Utvy3S0ykmxlskz7ythOsDsm6zNNibia3qASGEZwDcBXVAwThSasvpoWbn2NSVHiaFicF6G1G3HkrOarBA/0?wx_fmt=png)

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