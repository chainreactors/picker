---
title: 从单车到车路云网：治理升级、L2 强标与一条「假召回」短信
url: https://mp.weixin.qq.com/s/2M54bpzQ6aRhpJTnORXL8A
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:59:23.607816
---

# 从单车到车路云网：治理升级、L2 强标与一条「假召回」短信

# 从单车到车路云网：治理升级、L2 强标与一条「假召回」短信

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCpMaDYVGMMtuR3fmy750iaicCKDagwQOrg64LEaCmsteVt9oP58YVs2DKiaaBP7Ls7WrHegrKtLib2VwklnMT6yamPZTbdJSEmSX8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

11 月上旬一条能报出车架号的假召回短信，又把国内治理体系最容易被忽略的一面：车主数据流转，摆到了台面上。

**一、三个新特征：监管给「缺陷」重新划了边界**

2026 世界智能网联汽车大会（10 月 22 日）政策法规论坛上，国家市场监督管理总局质量发展局**二级巡视员李常青**提出智能网联汽车质量安全的三个新特征：

* 风险形态从「有形硬件」扩展到「无形软件」，软件缺陷多发与软件迭代常态化叠加，**OTA 成为风险管控新变量**；
* 缺陷特征从「显性可复现」转向「无形、数字化、难复现」，传统缺陷判定与试验验证手段面临挑战；
* 安全边界从「单车产品」延伸到**「车、路、云、网」协同的系统生态**，质量安全成为贯穿整车、芯片、算法、通信、数据的系统性命题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDeomzSQ8f9PCTNspMrFq4fNthmBbT3jC5W10mCuykUdLPrjJAkVn6AkiaynMdCdyU2gicXZv4nfEibcrk8w3P3mYgPRC5WhdCibFw/640?wx_fmt=png&from=appmsg)

图 1｜车路云一体化系统架构示意来源

来源／图片性质：公开技术架构图，谈思实验室整理；为技术示意，非监管官方原图

同一场发言还披露了今年 1—9 月召回 617 次、涉及车辆 2039.38 万辆，其中经监管部门调查约谈后推动的召回 1452.68 万辆（占 71.23%）。**这里必须标一处口径差异：**中证网将该统计表述为「新能源汽车召回」，央广网、OFweek 等转述为「智能网联汽车召回」，数字一致但统计对象名称不同。本刊按「同一场大会发言披露的召回数据」引用，不代监管重新定义统计范围；71.23% 一项目前仅见于媒体转述，属单一来源口径。论坛上「坚决防止追求热点、缺少场景验证的『激进式创新』上车」的表态，同样是媒体对发言的转述，不是法规条文。

对安全工程师来说，这三句话不是务虚。它意味着 TARA 里的资产清单要包含云端服务与算法模型，缺陷验证要覆盖「难复现」的时序与状态组合，OTA 的每一次版本变更都要能回答「这次升级是否改变了已批准车型的安全假设」。

**二、标准与地方立法：一边迭代指南，一边先行先试**

**国家层面，**工信部装备工业一司司长郭守刚在同一论坛表示，我国持续迭代《国家车联网产业标准体系建设指南》，**最新版本已公开征求意见**。注意状态：是「公开征求意见」，不等于已发布、已批准、已实施；截至本期截点，最新版本号与征求意见截止日期未取得可核验的官方公告，本刊不作补充。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCUe31wGDTv1Gk5prgNQRhTzdUicRSzusGtR44AsyR29Kvjpqjs9iaQMv7swnkbYzLQNAd1h7vh10DlBN2FJ19gltLqiaRdztMNoY/640?wx_fmt=jpeg&from=appmsg)

图 2｜智能网联汽车标准体系架构示意来源

来源／图片性质：公开技术资料图，谈思实验室整理；为体系框架示意，非现行标准清单

更硬的一条是 **GB 47955—2026《智能网联汽车 组合驾驶辅助系统安全要求》：**由工信部组织制定并归口，国家市场监督管理总局、国家标准化管理委员会于 2026 年 6 月 27 日批准发布，拟自 **2027 年 1 月 1 日**起正式实施，是我国首个针对 L2 级组合驾驶辅助的强制性国家标准。标准按基础单车道、基础多车道、领航驾驶辅助三类产品分别提出安全要求，从功能要求、数据记录、车辆制造商安全保障三个维度设基线，并构建场地试验、道路试验、文件检验相结合的多层级评价方法。新华社同期披露，2026 年以来我国搭载组合驾驶辅助功能的乘用车新车市场渗透率达 70%，其中领航辅助（NOA）车型渗透率超过 30%。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDxaWMTciaV2ibltQg3UKVnxAaU2f75puJCiaoUXCdKY0tt6l2ldQwKtRCEtwzd26bQFyYaJ1jIT3YtjZv6TZTNrg3u83NI6o3ib9k/640?wx_fmt=jpeg&from=appmsg)

图 3｜GB 47955《智能网联汽车 组合驾驶辅助系统安全要求》报批稿

来源／图片性质：公开标准报批稿封面，仅作标准主题示意；封面标注「报批稿」且标准号为占位符，非正式发布文本

**地方层面**，天津与浙江给出了两种样本。《天津市促进智能网联汽车发展条例》由天津市十八届人大常委会第二十二次会议于 **2025 年 11 月 28 日**通过并公布，**自 2026 年 1 月 1 日起施行**，共 6 章 43 条；条例明确市工信部门管产业促进与道路测试、市交通运输部门管商业化应用试点、市公安部门负责登记号牌与职责范围内网络数据安全监管、市网信部门统筹网络安全与网络数据安全。天津政务网 2026 年 1 月 10 日披露，全市已开放智能网联汽车测试道路 **5389 公里**。

**这里纠一个常见错：**央广网 10 月 24 日报道写作「2025 年正式施行的《天津市促进智能网联汽车发展条例》」，与法规原文（2026-01-01 施行）不符。以国家法律法规数据库与天津人大公告为准，应写「2025 年 11 月通过、2026 年 1 月施行」。另据 2024 年底官方口径，当时开放测试道路 2103 公里（含 491 公里高速）、发放测试牌照 51 项——与 5389 公里是不同时点的两组数字，不可混用。

浙江则按「事前准入—事中在线监测—事后应急处置」构建全链条监管：杭州率先出台智能网联汽车测试与应用促进条例，嘉兴、湖州 2026 年相继推出地方性法规，全省智能网联汽车**测试总里程突破 745 万公里。**这三市法规的具体名称、公布日期与 745 万公里的统计截止时点，目前仅见央广网对论坛发言的转述，本刊标注为**媒体转述、待官方文件核验；**745 万公里是累计行驶里程，不是开放道路长度，也不是牌照张数。

**三、L3 首批准入：是「附条件」，不是「全国上路」**

工信部第 401 批《公告》对两款搭载 L3 级有条件自动驾驶功能的产品作出**附条件许可**，被媒体称为我国首批获准入许可的 L3 产品：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAKsHwXQhibosmUXLclRDkLrXvWKkb8AVtiaq6oMJYky6AtIzcVaXaWdxJhQR1g2DKUPk3wFcmIhCMd9K99L5H0vcKaGsibUxtwX4/640?wx_fmt=png&from=appmsg)

图 4｜谈思实验室整理制表

工信部表述为两家企业「已完成并通过产品测试与安全评估」，由上述主体在**限定区域内**开展上路通行试点。写方案、做汇报时别把「首批 L3 准入」简写成「L3 可全国上路」——功能、车速、路段、运营主体四个限定都在公告里。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDgEFtoVvoYx2GicicuVuiadOxX5Gibvgo9KdXUPSGUYR5ibB55ibKHz9JTMkVdZP6z4kwFgNMnjEH4Omj76rUVWZ3hiadxb8ptoEHH3o/640?wx_fmt=jpeg&from=appmsg)

图 5｜首批 L3 准入相关媒体宣传海报

来源／图片性质：媒体制作海报，非监管公告；图中「仅 2 台合法上路」等标题为媒体表述，准入范围以工信部第 401 批《公告》为准

全国口径还有一组常被引用的数字：累计发放测试示范牌照超**2 万张**、开放测试示范道路超 **5.7 万公里**、累计测试里程突破 **2.2 亿公里**、车路云一体化设备 6 万余台套、乘用车新车 L2 搭载率超 70%。它们由工信部大会口径经行业媒体与中新网转述，本刊标注为**官方口径经媒体转述**（未取得工信部官网独立原文页）。再提醒一次量纲：张数、道路长度、行驶里程、设备台套、百分比是五类不同指标，不可相加，也不宜互作比例。

**四、11 月上旬的一条落地案例：能报出车架号的「假召回」**

11 月 5—6 日，理想汽车法务部、大众汽车（中国）、宝马中国、沃尔沃，以及丰田中国、一汽丰田、广汽丰田等先后发布声明或客服回应：近期大量传播的「高田气囊召回」短信与所附「红头文件」**均非官方发布**，属冒用企业及监管部门名义的电信诈骗。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCubGApj3g3cWTBxEdacm4GLpSnYrcibVkVGGIoYLXeJLrnDcmG3Y8MB6f5yhRlCxrfIyQyItnoEicGJ4icsvRAVg9oO3tKXvwibiaI/640?wx_fmt=jpeg&from=appmsg)

图 6｜被企业标注「假」的召回诈骗短信

来源／图片性质：企业辟谣声明配图，经媒体转载；图中个人信息已作打码处理

公开报道归纳的共性手法是：以「气囊召回」「2 小时内办理」「逾期取消质保」制造紧迫感，附伪造印章文件、非官方网址或二维码，诱导填写个人与车辆信息；部分短信能精准报出车主姓名、车牌号甚至车架号后六位。极目新闻记者实测一条涉诈链接，页面仅设简单滑动验证、无企业资质与官方联系方式，域名无工信部 ICP 备案、服务器在境外。各家给出的核验入口一致：凭 17 位车架号在市场监管总局缺陷产品召回技术中心官方渠道或品牌官方 App / 客服 / 授权经销商查询；正规召回免费，不索要银行卡号、验证码，不要求转账或开启屏幕共享。

**事实边界要写清：**以上均为**企业单方声明与媒体报道**，不是「已证实某车企车主信息泄露」。媒体关于「诈骗精准度反映车主数据流转链条存在风险」的分析，属于行业推断，非监管认定；受骗车主数量、涉案金额、信息泄露的具体环节均未披露。截至 11 月 9 日，记者查询市场监管总局及缺陷产品管理中心官方渠道未见针对此事的专门提示，公安部刑侦局与深圳、郑州等地反诈中心已发布预警。这条线索本刊只点到为止，不与 11 月 10 日已展开的数据出境制度重复。

不过它和今天的主题确实连得上：当召回本身变成 OTA 与软件缺陷的高频动作，「召回通知」就成了攻击者最好用的社会工程外壳。治理边界从车、路、云、网一路延伸，最后落在车主手机上——而这一端往往不在整车的威胁模型里。

**五、本期三条结论**

* **监管定义变了**：缺陷从「可复现的硬件问题」扩展到「难复现的软件与系统生态问题」，验证手段与证据组织必须跟着改。
* **节点别记混**：GB 47955—2026 是 2027 年 1 月 1 日实施，与 GB 44495/44496 的 2026 年 7 月 1 日公告准入节点不是同一件事；天津条例是 2026 年 1 月 1 日施行，不是 2025 年。
* **数据面别漏**：从云端配置到车主手机，安全边界的末端常常是最弱的一环；「能报出车架号」的精准诈骗，值得放进车企的数据流转审计范围，而不只是发一份辟谣声明。

**来源：综合网络资讯整理**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAgMtYBvxP2sDlfLAwoYib8145dMuTYZVJicxeicYLHeLoLWHibwZOxZKBcEFdvDzVLDUxffphYZ209H0Iy8LeZicYic10LYFWtDYGfM/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc65297027a878544a9e796e09cf6&scene=21#wechat_redirect)

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3128e4eaa74d6727dd46&scene=21#wechat_redirect)

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247502093&idx=1&sn=ec4b373a33ca04d79afbb0b0b880bd4e&chksm=e9278dd6de5004c01bdd83ad0dd89c3549c7ae2ceb3629...