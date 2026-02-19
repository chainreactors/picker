---
title: 0APT勒索软件组织声称已造成200组织被攻击但未能交付任何真实数据
url: https://mp.weixin.qq.com/s/wwELvC4pTx3ZmmuJ95HjlA
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:16:48.502615
---

# 0APT勒索软件组织声称已造成200组织被攻击但未能交付任何真实数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zdwoicOrrJb1lckcV2gibyTHh5P86iaJNC813KEFS2QTCw1T2N6EUNHKXYrIeSXCfnXypBKQm02xdbl0e4ibFeaUEHygk2PuBvWibSRMFpbfpSdQ/0?wx_fmt=jpeg)

# 0APT勒索软件组织声称已造成200组织被攻击但未能交付任何真实数据

原创

ZM
ZM

暗镜

![]()

在小说阅读器中沉浸阅读

2026 年 1 月下旬，一种名为 0APT 的新型勒索软件在暗网上出现，声称在第一周内就攻击了 200 多个组织。

该组织在一个个性化的 TOR 域名上建立了一个专业的泄露数据网站，并以“勒索软件即服务”的名义进行营销，以招募附属机构。

安全研究人员很快发现，几乎所有声称的受害者都是捏造的，根本没有真正的被盗数据。此次行动似乎旨在欺骗那些有志于从事网络犯罪的人，而不是敲诈合法机构。

0APT 组织构建了复杂的架构，包括一个由 NGINX 服务器驱动的数据泄露网站、一个功能齐全的 RaaS 面板以及用于谈判的聊天系统。

每个受害者名单都显示了据称包含数GB企业数据的文件树。当研究人员尝试下载这些文件时，他们发现文件大小异常庞大，超过4GB，而这些文件树原本应该只有几KB。

下载在五分钟后自动终止。《渡鸦档案》分析师认为这是蓄意欺骗，旨在制造成功入侵的假象，而没有提供真实信息。

包括 GuidePoint Security、Halcyon 和 SOCRadar 在内的多家网络安全公司进行了调查，但没有发现任何证据表明所列组织遭受了实际的数据泄露。

![](https://mmbiz.qpic.cn/mmbiz_png/zdwoicOrrJb0MhlQlOhgzhpAqpPFic177TPPqP7Fz9JnDkABSERzITJZicGl9kVQWdvZTdEZjG32icV8UW991ickoCnaYiaMEswJ9VFCoXDTz6jCA/640?wx_fmt=png&from=appmsg)

一些声称受到伤害的机构，例如 Epworth HealthCare，公开表示他们没有找到任何妥协方案。

研究人员发现，0APT组织列出了一些虚构实体，例如受DC漫画启发而创作的“大都会市政府”。该组织的认领率远超已知的勒索软件组织，报告显示，短短两天内就新增了91名受害者。

## **RaaS 小组欺骗策略**

当研究人员访问RaaS面板时，此次行动的真正目的才得以揭晓。该平台允许关联方每个账户生成五个勒索软件样本，支持Windows、Linux和macOS系统。

使用 Rust 编译的 Windows 可执行文件大小为 5.6MB，而 Linux 二进制文件大小为 1.3MB。这些样本使用了包括 AES256、Salsa20/ChaCha 以及与 AI 生成代码相关的罕见 Speck 密码在内的加密算法。

一些声称受到伤害的机构，例如 Epworth HealthCare，公开表示他们没有找到任何妥协方案。

研究人员发现，0APT组织列出了一些虚构实体，例如受DC漫画启发而创作的“大都会市政府”。该组织的认领率远超已知的勒索软件组织，报告显示，短短两天内就新增了91名受害者。

该行动通过醒目的“加入 RAAS”通知招募合作伙伴，向误以为自己加入了一个成功的生态系统的网络犯罪分子收取费用。

据报道，一名演员诈骗了感兴趣的犯罪分子至少 85,000 美元。该小组提供支付跟踪、谈判聊天、管理支持和技术文档等功能。

虽然该恶意软件在执行时会发挥作用，但整个受害者名单都是经过精心设计的，目的是为了吸引付费推广者。

安全团队应在回应赎金要求之前，通过官方渠道确认安全漏洞声明。

如果没有真正的赎金信、加密文件或直接沟通，泄露网站的列表应被视为可能捏造的。

建议各组织密切关注 0APT 入侵指标，因为功能性勒索软件二进制文件仍在流通。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

暗镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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