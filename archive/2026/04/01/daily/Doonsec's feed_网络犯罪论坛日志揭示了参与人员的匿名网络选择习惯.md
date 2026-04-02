---
title: 网络犯罪论坛日志揭示了参与人员的匿名网络选择习惯
url: https://mp.weixin.qq.com/s/ZnwaRAM33KFu1GOAH2AXIA
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:21:24.720347
---

# 网络犯罪论坛日志揭示了参与人员的匿名网络选择习惯

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoWR5KggA5CWaAsGvjQ41YvtfVjjUp0GNmtVJelzWDkOHsoRXpMHiaZyHhvgqnaBvOjtgURAOyuicOJcsibEhpweCFKibibbWZuicXWk/0?wx_fmt=jpeg)

# 网络犯罪论坛日志揭示了参与人员的匿名网络选择习惯

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

一般威胁行为者登录系统时，绝不会使用真实 IP 地址。相反，他们会通过虚拟专用网络（VPN）、代理服务器和匿名网络转发流量

境外安全机构通过分析2026 年 1 月来自头部英文网络犯罪交易平台 BreachForums 的数据泄露库，其中包含了威胁行为者的 IP 地址信息。

这项分析能够帮助威胁情报公司针对高风险登录行为做出有据可依的决策，同时明确如何通过管控措施，限制来自高风险 VPN 服务或匿名网络的登录请求。

攻击者一般都会担心，一旦执法部门获取了服务提供商认可的搜查令或传票，其使用的 IP 地址可能会关联到现实身份，这就迫使他们转向边缘网络服务：

承诺不留存日志的 VPN 服务、匿名代理，以及所谓的 “防弹网络”（[防弹主机 Bulletproof Hosting 是什么？](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451183741&idx=1&sn=5b391d8ec9c54118a506acf428087718&scene=21#wechat_redirect)）。

威胁行为者对身份隐匿的需求，不仅体现在发起攻击的阶段，也包括他们登录网络犯罪论坛和交易平台时。

BreachForums 基于 MyBB 开源论坛软件搭建，底层采用 MySQL 数据库。用户数据库包含多个字段，包括注册邮箱、哈希密码、用户注册论坛时的 IP 地址，以及用户最后一次访问的 IP 地址。完整数据字段如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpWwDASYVzicmM2QwRT7vdBWK1clz8BibdOW9oM4dZxumwNeFdUReJ9icGfgMqIYaABH7gic6M5sZiba26kRezansFzhdblJytjcAHI/640?wx_fmt=png&from=appmsg)

该数据库包含近 32.4 万条记录。其中约 235208 条记录的 “regip”（注册 IP，即账户注册时使用的 IP 地址）和 “lastip”（最后一次登录 IP）字段值均为 127.0.0.9。

该 IP 地址为本地主机 / 环回路由保留地址，这一现象十分异常,其原因可能是论坛配置错误导致日志失准，也可能是人为刻意设置。但仍有超过 88700 条 IP 记录的 “lastip” 值并非 127.0.0.9。

针对这些 IP 地址及其对应的自治系统号（ASN）展开分析，可以探明2026年的新时代犯罪人员和黑客论坛参与者的网络习性。

登录 BreachForums 的用户身份各异，并非只有网络犯罪人员，执法人员和网络威胁情报从业者同样在一旁盯着。

这意味着无法断定这些论坛 IP 地址全部属于威胁行为者，因为执法部门和 CTI 研究人员也可能使用同类服务来伪装身份。

尽管如此，这种混合使用的特性反而进一步说明：

来自这些 ASN、IP 和代理的请求，来自 “正常” 用户的概率极低，封禁这些地址触发误报的可能性也极小。

### 头部自治系统（ASN）榜单

###

下表列出了 BreachForums 数据中出现频次最高的 ASN，上榜并不意味着对相关企业或机构的声誉进行诋毁。

合法服务被恶意行为者滥用是行业常态。

同时，大型网络服务商和数据中心持有的网段，可能会将部分地址租赁给小型服务商（例如 VPN 或代理服务提供商）。

而防弹主机服务商这类小型网络运营商，会频繁更换网段和网络接入供应商，以此规避关停，保护其犯罪客户免受滥用投诉。

尽管如此，这份数据仍能反映特定时间节点的网络活动快照。

CDNEXT, GB：

该 ASN（AS212238）由英国 DataCamp Limited 运营，是一家大型内容分发网络（CDN）和网络服务提供商，在本次 BreachForums 数据中出现的 IP 数量最多。其在全球多地部署了大量网络节点，包括美国、英国、荷兰。

TORSERVERS-NET, DE：

这是由德国数字基本权利协会运营的小型 ASN（AS60729），对应网段 185.220.101.0/24，包含洋葱路由（Tor）的中继节点。Tor 是一个匿名网络平台，通过全球中继节点网络加密浏览流量，大幅提升溯源用户真实 IP 地址的难度。（相关阅读：[Tor 匿名网络的“美国印记”：政府招标项目资金占比从53%降到35%](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184312&idx=1&sn=c555fe3244d85515ad22a896402d459b&scene=21#wechat_redirect)）

M247, RO：

M247 Global 是一家大型主机托管和云基础设施服务商。

CLOUDFLARNET：

Cloudflare 是一家聚焦安全与性能的大型 CDN 和云网络服务商。

CYBEROLOGY-AS, NL：

该 ASN（AS215125）自称为 “网络学教会”，将自身定位为 “倡导（线上）自由、权利与隐私的宗/教组织”。其总部位于荷兰，在小型 IPv4 网段 192.42.11.0/24 上运营 Tor 中继节点。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp9LdeCFWTSBTX2CxXqyDWn3dYfEAFutNgp0Ys7bkWt8Rb3XzXdCtPicZjKdacKq1CiabHc8TIPawicYVvC1RbyqtuDWrIxRxPo0I/640?wx_fmt=png&from=appmsg)

以上为 BreachForums 泄露数据中出现频次 TOP10 的 ASN

###

### VPN 与代理服务使用情况

###

登录 BreachForums 的威胁行为者，所使用的 IP 地址分属各类 VPN、代理服务及私有网络。

尽管 BreachForums 数据中约 75% 的 IP 地址无法公网路由，仍有超过 3.5 万个 IP 可完成情报富集。

不出所料，与 Tor 匿名系统相关的 IP 在 TOP10 服务中占比超 42%；排名第二的是 Mullvad VPN，其后依次为 Proton VPN、Nord VPN。住宅代理服务（常被用于绕过地理定位限制、实施凭证填充等攻击）在结果中未出现显著占比。

TOP10 VPN 与代理服务使用情况如下：

| 排名 | 服务运营商 | 占比（%） |
| --- | --- | --- |
| 1 | TOR\_PROXY | 42.7 |
| 2 | MULLVAD\_VPN | 13.3 |
| 3 | PROTON\_VPN | 12 |
| 4 | NORD\_VPN | 9.4 |
| 5 | WARP\_VPN | 7.3 |
| 6 | OXYLABS\_PROXY | 5.6 |
| 7 | ICLOUD\_RELAY\_PROXY | 3 |
| 8 | EXPRESS\_VPN | 2.7 |
| 9 | OPERA\_VPN | 2.5 |
| 10 | SURFSHARK\_VPN | 2.4 |

###

### 电子邮箱域名分布

在线服务商通常会向新注册用户的邮箱发送验证邮件，以确认地址有效性，但这个版本的BreachForums 并未执行该流程。

这意味着数据库中的邮箱地址甚至可能并非真实存在。在网络犯罪论坛中，无需提供真实邮箱存在显著优势：若邮箱地址不存在，其服务商就无法向执法部门提供相关数据或元数据；同时，BreachForums 注册者也可能使用他人的邮箱地址作为误导手段。

BreachForums 数据共包含 323986 条记录，其中约 2.7 万条记录包含无效邮箱、无邮箱，或 null@null.com 这类无效地址。绝大多数注册者使用 Gmail 邮箱，占比约 81%；约 14.3% 的邮箱域名来自主打隐私的加密邮箱服务 Protonmail；排名第三的是Onionmail.org，占比约 1.6%，该服务基于 Tor 网络运行，不留存个人数据与 IP 地址；第四位是 Cock.li，注册账户数比第五位的 Yahoo 多出约 100 个。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDr1TSJxTlm0bHZAg2kft2KeZyO3ONTCaboUVM5aYkfahL2go8Pz5Tajl3LHHngrulXdr5OzgGt9kWHMnaNPxXEgkuItQjicdjVs/640?wx_fmt=png&from=appmsg)

Gmail 是 BreachForums 威胁行为者注册使用最多的邮箱域名，但这个版本的论坛并未执行邮箱验证流程。

从数据中抽取了 16044 个邮箱地址样本，通过数据泄露通知服务 Have I Been Pwned，核查这些地址是否还出现在其他过往泄露事件中。

这一核查无法证明邮箱地址真实注册过，但若某地址出现在其他泄露事件中，则其真实存在的概率更高。

在 16044 个样本邮箱地址中，有 10200 个地址仅出现在本次 “BreachForums2025” 泄露数据中，其中 7515 个为 Gmail 地址。这表明 BreachForums 注册者遵循了论坛管理员的建议，使用 “一次性” 邮箱地址，即仅用于单一用途、不绑定其他账户的邮箱。剩余 5844 个账户出现在其他与信息窃取恶意软件日志相关的大型数据泄露事件中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoiaojlHbiaPFEVnfWfKgiaWtKv7ORHVJzFnxAy8rLIOKHNDeQUz2ykVWSd4KSick0eSQSwtts3nRI0IREuu0YGxTyzrMkPm4cHtVg/640?wx_fmt=png&from=appmsg)

该图表展示了 Have I Been Pwned 平台核查到的、同时出现在其他泄露事件中的 BreachForums 邮箱地址分布，基本是很烂大街的密码库表。

BreachForums 泄露数据，揭示了威胁行为者登录犯罪论坛时的服务选择偏好。可以推测，绝大多数用户的选择，都反映了其对自身操作安全的一定认知。

使用 VPN 和匿名网络，并不代表所有使用者都在从事恶意活动，但这类网络，正是那些利用地下市场、恶意软件活动窃取的凭证实施账户劫持的攻击者，最常使用的网络类型。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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