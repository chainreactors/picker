---
title: 一周安全事件回顾：银行资金、航司数据接连失守，第三方接入风险该如何管控？
url: https://mp.weixin.qq.com/s/epgR0PDWFS7G-VUzzmXjag
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:12:06.589376
---

# 一周安全事件回顾：银行资金、航司数据接连失守，第三方接入风险该如何管控？

# 一周安全事件回顾：银行资金、航司数据接连失守，第三方接入风险该如何管控？

奇安信集团

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本周两起重大安全事件，再次揭开大型机构供应链安全的深层隐患：服务可以外包，风险却不会随之转移。供应商掌握的系统权限与敏感数据，正成为核心业务防线的重要薄弱环节。法国大型银行因服务商平台遭入侵，攻击者进一步渗透内部系统并盗转巨额资金；亚洲六大航空公司则因共同IT服务商遭攻击，接连发生旅客信息泄露。前者表明第三方接入风险可能直达核心资金交易，后者凸显单点失陷引发跨机构连锁风险的破坏力。对大型政企而言，供应商安全不能止于资质审查和合同约束，更须掌握其实际接入范围、系统权限及数据流向。建议开展第三方接入专项排查，严格落实最小权限与访问隔离，完善独立审计、异常阻断及供应商失陷后的快速隔离机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mSqhDgeKrPA7P9LNsoHgpLPINZbiaOOOzSbCtgGgBEpicHZYC6Z19d6EibtquohBERAfyeaE5HCf2kKllkopK0chTzfrx9xXyVOj329IcLn1U8/640?wx_fmt=jpeg)

01

[法国一大型银行内部系统被黑，近10亿元遭转账窃取](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516847&idx=1&sn=2f9053c7890e76efcecdad5958b9702b&scene=21&token=625325701&lang=zh_CN#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jiathHTJL5U3sCaezEJIh7Zf6iaibKvMwOSBL1MnzHPQUpc8erdaaUoAbXu80BrR9icRBktfUps2A7nXWhB7oOOeHzGWnib1HO9H0ia6Y3NXtiaLyI/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

11月5日安全内参消息，法国大型银行Crédit Mutuel Arkéa披露遭遇一起网络安全事件。此前有研究员爆料，黑客从该行窃取了约1.33亿美元（约合人民币8.87亿元）。该行发布声明称，攻击者“通过服务供应商平台”入侵了集团内部系统，此次攻击手法“高度复杂”，并非人为失误。该行表示：“攻击者利用Crédit Mutuel Arkéa自身的账户，向其他银行机构转账。随后，这些资金可能通过专业平台兑换成加密货币。”部分兑换后的资产已被冻结，多方正努力追回其余资金。该行强调，客户账户没有被访问，客户资产也不会受到此次事件影响。

02

[因IT供应商遭入侵，亚洲六大航空龙头发生数据泄露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516847&idx=2&sn=ff96f9a983ca1ec061dde008daffee99&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jiathHTJL5U3sCaezEJIh7Zf6iaibKvMwOSBL1MnzHPQUpc8erdaaUoAbXu80BrR9icRBktfUps2A7nXWhB7oOOeHzGWnib1HO9H0ia6Y3NXtiaLyI/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

11月5日安全内参消息，亚洲多家大型航空公司陆续披露，由于西班牙IT服务商艾玛迪斯（Amadeus）近日遭到网络攻击，导致客户数据发生泄露。艾玛迪斯旗下某个存储旅行预订信息的系统存在安全漏洞，可被用于访问部分预订信息。日本航空、国泰航空、大韩航空、韩亚航空、新加坡航空和马来西亚航空相继确认遭遇数据泄露。日本航空表示，约9.2万名客户的信息被窃取。新加坡航空称，约4.6万条记录被访问。国泰航空则表示，黑客窃取了约5.3万条记录，其中包括预订编号、乘客姓名和航班信息，部分记录还包含护照及其他旅行证件信息、常旅客会员号码和电子邮箱地址。

03

[AI访问权限遭盗用，多家企业损失近千万元](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516839&idx=1&sn=54681ced91facf0a2a4791d94785af28&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jiathHTJL5U3sCaezEJIh7Zf6iaibKvMwOSBL1MnzHPQUpc8erdaaUoAbXu80BrR9icRBktfUps2A7nXWhB7oOOeHzGWnib1HO9H0ia6Y3NXtiaLyI/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

11月4日安全内参消息，谷歌Mandiant团队日前发布报告披露，大模型劫持攻击（LLMJacking）日渐增多，犯罪分子滥用企业AI资源，已发现多起滥用案例和专业分工黑产。报告举例称，有受害企业每日损失10万美元，累计损失逾百万美元；有攻击者利用窃取的API密钥转售给某些第三方中转站，8小时内就发起了超50万次调用。前几天谷歌旗下Wiz公司也发文称，近一个月来AI密钥盗用攻击猖獗，已发生9起AI服务明星平台失陷事件，如Railway、OpenCode、Warp等。用户应积极关注相关事件和采购订阅账单，避免滥用损失。

04

[冷藏系统再遭篡改变“烤箱”，欧洲上百家超市大量食品变质损坏](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516828&idx=1&sn=844104d1602e97c720d746cd7588664e&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jiathHTJL5U3sCaezEJIh7Zf6iaibKvMwOSBL1MnzHPQUpc8erdaaUoAbXu80BrR9icRBktfUps2A7nXWhB7oOOeHzGWnib1HO9H0ia6Y3NXtiaLyI/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

11月3日安全内参消息，“烤箱”攻击再现欧洲，比利时、瑞典、爱尔兰等多国上百家超市的冷藏系统被黑，温度被远程调至50摄氏度，致使大量食品变质损坏。多方消息显示，丹麦丹佛斯、比利时谷轮等公司的设备均为攻击目标。设备安装公司Sabcobel称，受影响的设备需要做硬件改造才能修复相关漏洞。此次攻击和上个月针对法国700家超市的攻击如出一辙，都是针对老旧控制设备，欧洲网络安全机构对此类持续增长的网络攻击事件表示担忧。

05

[国内群晖NAS设备遭勒索攻击，官方建议尽快排查更新](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516811&idx=1&sn=8ec8e6aac1f429accbd887ba2446ebc3&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/jiathHTJL5U3sCaezEJIh7Zf6iaibKvMwOSBL1MnzHPQUpc8erdaaUoAbXu80BrR9icRBktfUps2A7nXWhB7oOOeHzGWnib1HO9H0ia6Y3NXtiaLyI/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

10月31日安全内参消息，国内外陆续出现多起群晖（Synology）NAS设备遭受勒索软件攻击的事件，部分用户的文件被恶意加密，并被要求支付赎金才能恢复数据。国外Reddit、BleepingComputer社区，国内Linux DO、V2EX等社区及公众号均有用户发帖表示遭受了勒索攻击，也有安全厂商应急团队接到相关事件处置。部分受害设备中的文件被加密并添加.L0CK3D后缀，同时出现名为read-me3.txt的勒索信，相关攻击被认为与C3RB3R（Cerber）勒索软件有关。群晖官方公众号日前发布安全公告，确认攻击者正在利用旧版系统中已修复的安全漏洞（群晖安全公告：Synology-SA-24:20）实施攻击，提醒用户尽快检查并更新系统。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarwCHGK4V5d5pFicUo1yED6dkswm0BfC0ncqh9D2G8Rvuelo3qdHlWFv4KMF78FsOIEKiaJrgmdIlJw/0?wx_fmt=png)

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