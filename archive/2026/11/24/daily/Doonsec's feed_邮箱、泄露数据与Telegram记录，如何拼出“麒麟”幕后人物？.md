---
title: 邮箱、泄露数据与Telegram记录，如何拼出“麒麟”幕后人物？
url: https://mp.weixin.qq.com/s/AzC1QSwyWeK_3U-ru9yMQQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:44:41.753019
---

# 邮箱、泄露数据与Telegram记录，如何拼出“麒麟”幕后人物？

# 邮箱、泄露数据与Telegram记录，如何拼出“麒麟”幕后人物？

原创

Owllntel
Owllntel

猫头鹰OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

勒索软件麒麟背后的操盘手到底是谁？2026 年 11 月，一份名为《Who Runs Qilin? Identifying Haise》的调查材料公开，披露了一条完整的溯源链条。调查人员梳理暗网论坛遗留痕迹，通过用户名匹配、邮箱反查、泄露数据检索、聊天记录解析，把散落在各个地下平台的账号线索串在一起，最终锁定一名俄罗斯籍男子。

勒索软件麒麟（Qilin）是一个采用“勒索软件即服务”（RaaS）模式运营的网络犯罪组织，通过向附属攻击者提供勒索软件工具和基础设施，招募成员实施网络攻击，并从赎金收益中分成。其活动涉及企业网络入侵、数据窃取和系统加密。

Haise是麒麟幕后管理者的人员所使用的网络化名，调查人员最终将这一化名与俄罗斯籍男子Alexey Mikhailovich Yakovtsev联系起来。RAMP等网络犯罪地下论坛则是其发布招募信息、寻找攻击合作人员的重要渠道。由于Haise长期以匿名账号活跃于地下平台，调查人员首先从麒麟曾经开展招募活动的RAMP论坛入手，追查其留下的账号记录。

# 突破口：从 RAMP 论坛审核记录挖出关联账号

整个追查工作，始于 Haise 在俄语犯罪地下市场 RAMP 论坛留下的记录。麒麟早期就在这个平台发布勒索合作信息、招募攻击附属人员，论坛注册资料、审核存档和私信内容，成了追查核心人员的起点。

美国联邦调查局在 2026 年 1 月查封 RAMP，调查团队拿到平台留存的历史注册和私信数据，开始梳理账号之间的联系。在 2022 年 6 月两份审核记录里，Haise 先后和 Exploit 论坛账号 Alexbigboss44、XSS 配置文件所用用户名： Rjun 产生交集，调查范围就此打开，不再局限于 Haise 这一个麒麟管理账号。

这一步主要依靠用户名关联比对：研究人员收集 Haise 在不同论坛使用的昵称，对照注册时间、审核记录、资料和联系方式寻找重合点。但单单依靠用户名无法确认归属，团队继续深挖关联账号主页，寻找邮箱这类可以跨平台检索的关键信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWxrDtmiauESKs8RJibfIM53SHjzdVbejPKdD3bDTqicVWHXHkHF410n8S5vsYSfB1Td3feXWngXztN2zAIMh5WBBV0NUGibes0RekM/640?wx_fmt=png&from=appmsg)

一条邮箱串起多个地下论坛身份

调查重心转向 XSS 配置文件对应的用户名 Rjun。资料显示，Rjun 曾在 BHF 论坛的个人资料中留下邮箱：mail30a@mail.ru。工作人员拿这个邮箱检索 Zloy 论坛历史数据库，查到账号 rjun123 同样使用该邮箱注册。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWzDRLNU7FfHlNmicfPicf24UicRvxV6AVTdqMkNJ6MvOoZXqBW7KU4rz8FOpdhwBKHsR7UC7nF6MuGGQFKSiaT8F0HrLyicicqeF2BlM/640?wx_fmt=png&from=appmsg)

相比于可以随意更换的用户名，邮箱是稳定的跨平台溯源标识。团队拿着这个邮箱检索多个地下论坛存档，收集所有绑定该邮箱的账号，核对账号活动轨迹。

Intel 471 的历史数据补充证明，这一邮箱还关联 Darkmarket、Verified、Zloy 等多个地下市场账号。

线索链路：Rjun（XSS 配置文件用户名）→BHF 主页登记邮箱→匹配 Zloy 账号 rjun123→延伸 Darkmarket、Verified 等平台账号记录。

至此，调查跳出单一论坛，以邮箱作为检索枢纽，追踪同一联系方式在各个黑产平台的注册与活动记录。

# 泄露数据库落地真实身份信息

在关联多个地下论坛账号后，调查人员将邮箱地址mail-30a@mail.ru作为检索标识，利用一些身份情报平台对历史泄露数据进行反向检索，并将命中记录与俄罗斯政务服务门户网站Gosuslugi的泄露数据进行交叉比对。检索结果显示，该邮箱出现在Gosuslugi相关泄露记录中，关联姓名为Alexey Mikhailovich Yakovtsev，出生日期为1990年8月18日，相关身份资料指向俄罗斯圣彼得堡。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SmpxklM1IWxRicrou3fhFnp6q6KQEC35hlZK5gA01KRjrnaAcz4mMPGgzp1kicqzMUrY3Hw6k1LcXusbE1YJoZiaCeampDic43nZPXI7HSXeLDY/640?wx_fmt=png&from=appmsg)

链路：mail30a@mail.ru → Gosuslugi 泄露记录 → 对应自然人信息。

之后团队再通过关联手机号、其他邮箱、Telegram 账号交叉校验信息。2026 年 11 月 11 日，KrebsOnSecurity 发布报道，复盘了这条从匿名账号到真实身份的追踪过程。真实身份不是由单条记录直接确定，而是论坛邮箱、泄露库个人资料、通信账号多方信息互相印证后得出。

# 5000 余条 Telegram 消息，还原完整黑产活动时间线

论坛资料和泄露数据负责把匿名账号和真人绑定，而数千条 Telegram 历史消息，完整记录了 Haise 长年的黑产活动细节。 相关账号活跃时段为 2018 年 9 月至 2024 年 7 月，群组公开消息总量超 5000 条，内容覆盖黑产技术交流、招人、恶意工具交易、勒索项目运营。调查人员整理消息时间、话题、群组和互动对象，勾勒出他在地下网络的活动轨迹。

2023 年 4 月，账号发布招募公告，寻找熟悉 Windows、Linux、ARM、NAS、VMware ESXi 环境的技术人员。同年 7 至 8 月，群组内多次讨论 Linux、ESXi 勒索源码、ESXi 内核原理、绕过 CrowdStrike 防护的技术。7 月 10 日，他询问 ESXi 勒索软件的 Linux 源码；8 月 1 日，向群成员请教 ESXi 内核相关技术难点，能看出其深耕虚拟化服务器、安全绕过、勒索程序开发方向。

他还持续关注中文黑产社群。2023 年 5 月 14 日，Haise 在 Ralf Hacker Public Chat 群组询问有没有类似 RAMP 的中文论坛；时隔一年多，2024 年 7 月 28 日，又在 Ransomware Developers 群组提出相同问题，寻找同类平台。RAMP 主打勒索附属招募和业务合作，两次提问，说明他一直在留意中文地下社群，寻找潜在合作渠道。

![](https://mmbiz.qpic.cn/mmbiz_png/SmpxklM1IWwj8elUcfbjROWPAT9FEeZ0lOAzxZH3DBchD22GdBJrXjJn4Diar58ZH5H4JUic5YicPs37cjPIibqBSSickf49oWribIAKic54CMhnY4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/SmpxklM1IWxOrQ9lAMgXjoN3M7A1icN7xemL09jIticCibSX8DQYA8f2540VAG3RiaCDK4pAfRNJLGMdtLmU03ibDPVjKibW988dvmWFnaAsuzjib0/640?wx_fmt=png&from=appmsg)

这些聊天内容和麒麟当时的业务高度契合。2023 年 2 月，麒麟就在 RAMP 放出招募广告，工具支持 ChaCha20、AES、RSA4096 加密，具备多种加密模式。Telegram 里讨论的 Linux、ESXi、安全规避技术，正好匹配麒麟的开发和攻击需求。 2024 年 7 月底，Haise 所在的 Cobalt Strikers 群组传出消息，麒麟与 RansomHub 被纳入 Scattered Spider 攻击工具体系，同期群组内也出现麒麟招募广告，群组与时间线互相印证，把该账号的活动和麒麟业务推广绑定。

追溯更早的痕迹，Flashpoint 的数据显示，Haise 早年大量收购 Facebook 日志、Google Ads 账号，用来开展广告和博彩欺诈，同时做流量交易、黑资源中介。IntelHawk 的记录也体现了他的身份演变：从最初倒卖账号流量，慢慢涉足恶意软件、僵尸网络、黑产支付基础设施，最后深度参与麒麟勒索运营。

五千多条消息串联起他完整的黑产路径：账号流量倒卖→恶意程序与僵尸网络相关业务→参与麒麟勒索软件运营，招募人员、搜集工具资源、对接地下市场的所有行为，都留下了时间痕迹。

真正发挥作用的并非某一条孤立线索，而是多个平台留下的信息相互印证。从论坛用户名到注册邮箱，从历史泄露数据到Telegram通信记录，原本分散在不同平台上的网络痕迹逐渐指向同一身份。Haise长期使用的匿名账号，也正是在这些信息的交叉比对中，与现实中的个人资料建立起联系。对于活跃于地下网络的犯罪团伙而言，账号之间看似独立的注册信息和活动记录，往往会在长期使用中留下可以追溯的关联。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/biarWYvQqiaDic4snvC23OLhiaMAjLibbsp65I4VAh9Wtkq9VEtls6dEpuHbQAdNcdqwHkUGtpylW3dr0lzWwPTjR7g/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过