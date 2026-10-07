---
title: ShinyHunters勒索组织被FBI拘留事件技术溯源分析
url: https://mp.weixin.qq.com/s/bAJhVEr16AuEOF1qDxNtHQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:45.255226
---

# ShinyHunters勒索组织被FBI拘留事件技术溯源分析

# ShinyHunters勒索组织被FBI拘留事件技术溯源分析

原创

暗网分析师
暗网分析师

开源情报技术研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 9 月，使用 ShinyHunters 名义的人声称打进 FBI 招聘相关系统，并拿出一份部分可核对的人员样本。随后荷兰和约旦各有一名已被公开点名的人被拘。这不是一次把“谁偷了 FBI、核心网已瓦解”证完的行动。牌子下面至少有三代人，FBI 的入口和全量数据仍然只是声称。

# 两套手法，不要并成一次入侵

Salesforce 和电信客户数据这条线有受害方证实。2025 年下半年到 2026 年初，对方用语音钓鱼把员工骗去批准登录或安装恶意版 Data Loader，再滥用 OAuth 从客户自己的 Salesforce 里拖数据。Odido 属于这一类：2026 年 2 月 7 日至 8 日，荷兰运营商确认客户联络系统被打，约 620 万人。没有证据表明这场用了 PeopleSoft 漏洞。

PeopleSoft 是另一条线。CVE-2026-35273 是真的，Mandiant 把它记在 UNC6240，也就是他们追踪的 ShinyHunters 簇。这是 PeopleSoft Environment Management Hub 上的服务端请求伪造，Oracle 评定可远程利用，CVSS 9.8。2026 年 5 月 27 日到 6 月 9 日，它被当作零日，主要打高校，大约 100 家机构、300 个端点。9 月 25 日 Mandiant 又报告第二波：把路径写成 /%50SEMHUB/，用 URL 编码绕过只匹配字面量 /PSEMHUB/ 的防火墙规则。已点名的受害方包括诺丁汉大学、美国保险监管机构 NAIC 和日产。

FBI 这场不能直接接上这个编号。9 月 22 日对方对媒体说，前一天刚发现 PeopleSoft 上另一个零日，当晚就用在 FBI，随后进了 AWS GovCloud，并点名人力资源、Medlink 和刑事司法系统。FBI 只承认 FBIjobs.gov 有未授权活动，入口是局内系统还是支撑招聘站的第三方仍未确定。招聘站和 Special Agent Applicant Portal 确实下线，篡改截图来自对方。GovCloud 横向移动没有独立证据。

# 人是怎么被盯上的

Rey 的链在拘留之前十个月已经公开。2025 年 11 月，Krebs 写 Scattered LAPSUS$ Hunters 的三个 Telegram 管理员，只点出一个。突破口是他自己的截图：用户名 @wristmug 的图里露出一串密码，这串密码复用到一个 Proton 邮箱。SpyCloud 里该邮箱有 2024 年初的信息窃取日志，机器是安曼一台共用 Windows，多个用户同一姓 Khader。Krebs 写信给其父之后，本人私信确认，姓名是 Saif al-Din Khader，当时 15 岁。角色来自信道权限：Hellcat 泄露站、后期 BreachForums、ShinySp1d3r 的发布者。9 月 29 日约旦拘留、以及他在带 FBI 看设备，是路透消息源的说法。约旦官方只证实扣了一个与美国黑客案有关的人，没有点名。FBI 不按姓名证实。

Pepijn van der Stap 不是靠字符画认出来的。荷兰警方公报只说 24 岁、阿姆斯特丹、9 月 15 日被拘，涉嫌参加与 ShinyHunters 有关的犯罪组织，另案涉嫌在境外煽动两起谋杀，还押至少 90 天。姓名是 Neo Security 的 Benjamin Korper 向路透确认的，CBS 和 Krebs 的消息源一致。他 2023 年因数据盗窃和勒索被定罪，承认用过 Umbreon，约 2025 年 12 月出狱后做进攻安全。招聘站篡改页上的 Umbreon 字符画，被消息源解读成把视线引向已经在押的人，因为两人在争这块牌子。这是动机推断。组织随后说他与自己没有关系，并称荷兰警方无能。警方也澄清，这场逮捕不是 Odido 案。FBI 招聘站声明是 9 月 22 日，他当时已经在押。

另外两名 Telegram 管理员没有被点名。2020 到 2021 年那一代是另一案：Sébastien Raoult，马甲 Sezyo Kaizen，2024 年在西雅图被判三年。法国报道还点过 Abdel-Hakim El-Ahmadi 和 Gabriel Bildstein，两人未被引渡。2025 年 6 月巴黎检察官称拘捕四名 BreachForums 嫌疑人，姓名没有公布。

# 泄露了什么，核实到哪一层

FBI 样本是部分真实，全量库没有证实。对方给了约 5000 人的样本，字段包括姓名、住址、电话、出生日期、社保号、岗位，部分有配偶信息。路透拿社保号对征信记录，并和 District 4 Labs 的历史泄露库比对，至少 10 条对得上，其中包括 Kash Patel 的可核对字段。一名知情者说部分岗位描述也吻合。这证明样本里有真实人员信息，证明不了数据来自 PeopleSoft 或 GovCloud，也证明不了 2 到 3 TB、医疗记录和刑事司法库。对方没有要赎金，要求七天内撤回 FBI 5 月那份劝受害者不要付款的通报。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TEBBMzxzv79ibbJL0UiaZhowrpEOC2OQyZWpf8dPPNOxNib56qImcCo3DA2ickq5aBL0UuF0K1okVYrlS11lSwylibg/0?wx_fmt=png)

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