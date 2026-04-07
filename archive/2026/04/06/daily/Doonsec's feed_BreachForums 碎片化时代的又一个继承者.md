---
title: BreachForums 碎片化时代的又一个继承者
url: https://mp.weixin.qq.com/s/s9bYzFZ65ishpKXNFdnu7w
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:28:33.010250
---

# BreachForums 碎片化时代的又一个继承者

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAgVHdCoyRcZCjcTA79qIyq6G0N9lW6ozib7CqJmwIG8gVkyuibz9qfnKUTSPlia6H9BuvHnicYkUkqRDsfHU4KMzdAric04PEse60pU/0?wx_fmt=jpeg)

# BreachForums 碎片化时代的又一个继承者

原创

独眼情报
独眼情报

独眼情报

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAgKLYgrOWGYNChbRlKj1vdxDX6bJ7aAlOk9iaphMZ8YDadnqDMJrvbw9uwEibovXDwwVFFYZeWRjWIYe7vhhatVrIKwjjPuCliaVs/640?wx_fmt=png&from=appmsg)

2026 年 4 月 5 日，一个名为 PwnForums 的英文网络犯罪论坛正式上线，域名为 ████.██，同时提供 Tor 隐藏服务入口。管理员「John」在公告板块发布了一条欢迎帖。

这条轻描淡写的开场白背后，是一个体量惊人的数据迁移：论坛上线不到 24 小时，已显示拥有 339,506 名注册用户、78,676 个帖子主题、807,417 条帖子。这些数字不可能在一天内有机增长，可以确定来自对breachforums论坛数据库的批量导入。

## 技术与运营画像

PwnForums 的技术架构和运营模式呈现出鲜明的 BreachForums 克隆特征：

**基础设施层面**，论坛采用 MyBB 开源论坛软件搭建——这正是 BreachForums 各个历史版本一贯使用的框架。域名注册在 .st（圣多美和普林西比）顶级域下，与 BreachForums 在 2025 年使用的 breach-forums.st 域名属同一顶级域。论坛设置了 PGP 签名的 Warrant Canary（执法机构透明声明），下次更新截止日期为 2026 年 4 月 18 日，PGP 指纹为 AE97AB876347317D64B460656DA7866D332B11B7。

**板块结构上**，PwnForums 几乎是 BreachForums 的像素级复刻：

| 板块类别 | 核心子板块 | 与 BreachForums 对应关系 |
| --- | --- | --- |
| General | Announcements、Introductions、World News、The Lounge | 完全一致 |
| Leaks | Databases、Stealer Logs、Combolists、Cracked Accounts | 完全一致 |
| Marketplace | Services、Sellers Place、Buyers Place、Scam Reports | 完全一致 |
| Cracking | Cracking Discussion、Configs、Proxies、Hash Cracking | 完全一致 |
| Programming | Malware Development、Reverse Engineering、Exploit & POCs | 完全一致 |

**管理团队**极度精简，仅由两名管理员构成：「John」和「Insane」。John 的账号创建于 2023 年 6 月，帖子数仅为 1 条，但声望值高达 80，持有「GOD」荣誉标识。

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgzmibHCdrVQsHeuXTJ69C799jX6t39vHFMpkPMBicFmOhiaj1tjTDboJQJfUVxEa3QQ1p51QEavhXlTdJIzvDh13edqTXgSOvicPA/640?wx_fmt=png&from=appmsg)

## 生态位分析：2026 论坛战争的产物

要理解 PwnForums 的出现，必须把它放进 2026 年英文网络犯罪论坛生态的混战格局中看。

当前暗网论坛圈正经历一场被称为「2026 论坛战争」的内斗。核心参与方包括：由 Indra 和 N/A 运营的原版 BreachForums，以及由 HasanBroker 创建的竞争版本（被分析师称为「NotBreachForums」）。HasanBroker 自称与 2025 年 2 月被捕的前 BreachForums 管理员 IntelBroker（真名 Kai West）关系密切，从 2025 年 4 月开始筹建自己的版本，2026 年 1 月正式上线。

这场战争的关键转折点在于 2026 年 1 月 9 日，一个自称「James」的人在以 ShinyHunters 命名的网站上泄露了 BreachForums 完整用户数据库——323,986 条记录，包括用户名、邮箱、IP 地址和 Argon2 哈希密码。据分析，泄露源于论坛恢复过程中数据库备份被意外暴露。「James」同时发表了一篇戏剧性的 23 章宣言，自称是网络犯罪圈的「精神导师」，点名了包括 Dorian Dali、Nahyl Ojeda 在内的多个涉嫌参与 BreachForums 和 ShinyHunters 运营的个人。

此后，HasanBroker 与一个自称 LAPSUS$ 的组织联手攻击原版 BreachForums，据称成功窃取了论坛数据库并向自己的平台导入了 30 万用户。而原版 BreachForums 不仅遭受持续的 DDoS 攻击和内部分裂，其首页甚至一度出现出售论坛的广告。

PwnForums 正是在这种「九龙夺嫡」式的混乱中杀入市场的。它的策略很明确：不参与 BreachForums 的品牌之争，而是启用一个全新名称，同时通过批量导入老版BreachForums论坛用户数据和内容来制造「成熟社区」的假象。

## 风险研判

**对安全研究人员的意义**：PwnForums 的出现印证了一个趋势——英文数据泄露论坛正在从「一家独大」走向「军阀割据」。研判认为，BreachForums 品牌的反复被查封、被泄露、被争夺，正在加速这种碎片化。对于威胁情报分析师而言，这意味着监控工作量的显著增加——同一份泄露数据可能同时出现在三到五个竞争论坛上。

**论坛可信度存疑**：PwnForums 存在多个红旗信号。第一，管理团队极度不透明，仅两名管理员且无公开历史记录可验证身份。第二，339,000 名用户的来源就是来自老版BreachForums 数据库，那意味着论坛运营者可能拥有这些用户的明文邮箱和 IP 地址。第三，论坛提供 Escrow（担保交易）服务，但在缺乏信誉积累的前提下，担保方的可信度本身就是一个问号。

**蜜罐可能性**：BreachForums 生态系统的历史充斥着蜜罐指控。2025 年 8 月，ShinyHunters 曾公开声称 BreachForums 已被法国执法机构 BL2C 和美国 FBI 控制，成为记录用户活动的蜜罐。 2026 年 3 月又公开宣称任何 breachforums 论坛的克隆论坛都是假的。在这种环境下，任何新论坛——尤其是批量导入用户的新论坛——都无法排除类似的可能性。当然，目前没有任何证据表明 PwnForums 是执法蜜罐，这一判断仅作为风险维度列出，「待证实」。

## 与历史克隆论坛的对比

PwnForums 不是第一个试图从 BreachForums 废墟中崛起的平台。

2023 年 3 月 BreachForums 首次被查封后，PwnedForums（注意拼写差异）迅速上线，由化名 Sinistery 的人运营，但在不到一周后因内部分歧而关闭。同期还出现了 kkksecforum 等更短命的克隆。2024 年 5 月第二次查封后，USDoD 宣布创建 Breach Nation，ShinyHunters 则通过 Jacuzzi 2.0 等 Telegram 渠道重新聚拢用户。2025 年的混乱更加剧烈：breached.fi、breachforums.uk、breachforums.af、breachforums.info 等域名如雨后春笋般涌现，大多被威胁情报社区评估为诈骗或低可信度平台。

PwnForums 与这些前辈的不同之处在于：它有意回避了「BreachForums」的品牌，选择建立独立身份。这既可能是为了规避与 BreachForums 品牌争夺相关的风险，也可能是从过往克隆论坛的快速失败中汲取了教训。

## 小结

PwnForums 是 BreachForums 品牌持续崩解的最新产物。在原版论坛反复遭受查封、泄露和内斗的 2026 年，这种碎片化几乎是必然的演化方向。对于一个刚上线不到 24 小时的论坛，它的规模数据显然是人造的，而非有机生长的社区。它能否在这个充满猜忌、背刺和执法压力的生态中存活下来，取决于它能否做到其前辈们始终未能做到的事：赢得信任。

而在网络犯罪的地下世界里，信任恰恰是最稀缺的货币。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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