---
title: 一根 USB 线与 830 万辆车：Kia Boyz 与现代、起亚的防盗课
url: https://mp.weixin.qq.com/s/cpHbpGj3kE5WDIIs6e32nQ
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:59:28.984984
---

# 一根 USB 线与 830 万辆车：Kia Boyz 与现代、起亚的防盗课

# 一根 USB 线与 830 万辆车：Kia Boyz 与现代、起亚的防盗课

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCpMaDYVGMMtuR3fmy750iaicCKDagwQOrg64LEaCmsteVt9oP58YVs2DKiaaBP7Ls7WrHegrKtLib2VwklnMT6yamPZTbdJSEmSX8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

**一、2021 年，密尔沃基的一段视频**

2021 年前后，美国威斯康星州密尔沃基一群自称「Kia Boyz」的青少年在 TikTok、YouTube 上传教学视频：拆开转向柱护罩，露出点火锁芯，用一根 USB-A 线（或螺丝刀）插入并转动点火开关，几十秒就能把车开走。2022 年这套手法以「Kia Challenge」之名在社交平台扩散，多地警方随后报告现代、起亚车辆盗窃激增。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDO0AW5lEEgQPpolEvtttjmTftluibTibdBhzujWInNnSwqz1TqibkpZTYibfbVTdSSeeXuFKV3avAkA3ZKzAp3oDDbbzFK4KDYuqo/640?wx_fmt=png&from=appmsg)

图 1｜起亚 Soul 车型外观

来源／图片性质：公开车型图片，仅作品牌车型形态示意；图示为较新年款，不属于本文所述 2011—2021 年款机械钥匙点火车型范围

**先划范围**：受影响的是**美国市场**、配备**传统机械钥匙点火**、且**未配备发动机防盗锁止器（engine immobilizer）**的部分年款车型。媒体与诉讼口径主要指向 2011—2021 年款起亚、2015—2021 年款现代；加拿大市场、较新车型、按钮式点火或已配 immobilizer 的车型不在此范围。不是「全部现代/起亚车型」——具体配置因车型、年款、销售市场而异。

**二、被省略的那道认证**

发动机防盗锁止器的通用原理并不复杂：钥匙内的应答器（transponder）与 ECU 之间做**挑战响应认证**——ECU 发出随机挑战，钥匙用与车辆配对的密钥计算应答，验证通过才允许点火与喷油；部分实现用滚动码抵御重放。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDNt7dKLOmFJynRAxWMZVu3S3j1uvUEDaWicE1DToibzB7q3iblhzTlHFYlGfyefzXrj0ibiaFw4tjZ8ibIpriaKrFuVpMrWdtXvicw6OU/640?wx_fmt=png&from=appmsg)

图 2｜发动机电子防盗系统组成示意

来源／图片性质：公开教材/技术资料图，谈思实验室整理；为通用技术原理示意，非涉事车型具体电路

在只有机械锁芯、没有这道电子关卡的车上，锁芯被机械转动就等同于「授权通过」。USB 线在这里不是电子工具，只是一根形状刚好能插进去、能带动锁芯转动的物理杠杆——**据公开披露**，拆护罩、转锁芯即可接通点火与起动机电路。这条机械细节未找到厂商或监管机构对技术细节的正式确认，属公开披露一致口径，本刊按「据披露」表述。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD20viaic7dk40SU7FibanmiaKiblTVb43If24tgPPZqBG8CyWOKcvrJQLvzyEnfPscrsBBKy9JsYJQbcR1TmOAMiblMpSxa5N1OXAhQ/640?wx_fmt=jpeg&from=appmsg)

图 3｜immobilizer 钥匙—ECU 挑战响应通用原理

来源／图片性质：公开技术原理图；说明 challenge / response / counter-challenge 机制，非涉事车型实现

配置差异是有数据支撑的。IIHS 下属公路损失数据研究所（HLDI）的统计：2011 年款车型中，电子 immobilizer 在现代/起亚美国车型上的标配率仅 **17%**，其他品牌为 **92%**；到 2022 年款升至 **84%**，其他品牌为 **96%**；到 2023 年，现代与起亚全系车型才实现标配。另有媒体转述 HLDI 的 2015 年款口径为 26% vs 96%，统计年款不同，两组数字不可混用。NHTSA 估计受影响车辆约 **380 万辆现代（2016—2021 年款）+ 450 万辆起亚（2011—2020 年款）**——这是车辆数，不是盗窃数。

**这组数字能证明的是「配置差异确实存在」，不自动导出「企业有责」的法律结论。** 后者是诉讼争议，不是本刊能下的判断。

**三、从社交平台到公共安全事件**

公开报道与警方数据里，几组数字值得放在一起看，**但全部要带口径**：

* NHTSA 估计该趋势关联**至少 14 起车祸、8 人死亡**（截至 2023 年 2 月 14 日的下限估计）；
* 明尼阿波利斯警方口径：与两品牌盗窃相关的 5 起凶杀、265 起车辆事故（单一城市/州）；
* 洛杉矶 2022 年现代/起亚盗窃案增加约 85%、占全市被盗车辆 20%（单一城市）；
* 圣路易斯 2022 年 3958 辆相关车辆被盗、同比增 1450%（单一城市）；
* HLDI：2023 年下半年 2003—2023 年款现代/起亚车型的整体盗窃索赔频率，是 2020 年上半年的 11 倍以上；破坏行为索赔频率为同期 5 倍于其他品牌。

**量纲警示**：车辆数、车主数、和解金额、各城市逐年盗窃数、每千辆索赔频率是五类不同指标，不能相加、不能互相替代。「失窃率约为整体两倍」是比例口径，不等于「现代/起亚占了全美被盗车辆的一半」。

**四、补救、监管与一条容易写错的事实**

**2023 年 2 月**，现代与起亚宣布为美国市场约 830 万辆未配防盗装置的车辆提供免费软件升级（企业口径）。升级逻辑按企业说明为：要求钥匙必须插入点火开关才能启动、警报时长从 30 秒延长至 1 分钟、配发窗贴标识；对无法安装软件升级的车型，提供最高**300 美元**用于购买方向盘锁等装置，并通过 120 多个美国执法机构免费发放方向盘锁。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCQVegp08lyn1J8fGk5xPj2uG0kMASc0jQ1mQRuwcibWfoZV8QuV3kWc7V51IP4RHRwoeL6SDU2QdJE2ChzgtkNKPJXfI0Gicmas/640?wx_fmt=jpeg&from=appmsg)

图 4｜现代/起亚车主加装的方向盘锁

来源／图片性质：公开媒体图片，仅作防盗装置形态示意，非涉事车辆实拍

HLDI 后续实测给了这组补救措施一个可量化的评价：截至 2023 年 12 月，数据库中已完成升级的现代占符合条件车辆的 30%、起亚占 28%；**完成升级车辆的整车盗窃索赔频率下降 64%，整体盗窃索赔频率下降 53%**。据两家企业口径，到 2024 年 7 月中约 60% 符合条件车辆完成升级。局限同样清楚：升级仅在使用遥控钥匙锁车时激活，很多车主习惯按门把手上的按钮；破坏行为索赔反而上升 61%（多为未遂盗窃造成的车窗、车门与转向柱损伤）；对已被盗或已被物理破坏的车辆无效；部分无警报系统的配置根本不适用软件升级。

**2023 年 5 月 18 日**，双方律师宣布以**2 亿美元**就消费者集体诉讼达成和解，覆盖约 900 万名美国车主（车主人数，非车辆数），其中含消费者实际损失补偿；对无法升级的车辆提供防盗装置补偿。这是已落地事实。

**这里是最容易写错的一环：**830 万辆的软件升级**并非召回**。2023 年 4 月 20 日，17 个州与哥伦比亚特区总检察长联名致信 **NHTSA 要求全国召回**；据 NBC 获得的 NHTSA 回函及多家媒体转述，NHTSA 于 **2023 年 6 月**拒绝了该（含 18 州）召回请愿，理由是联邦安全标准并未强制要求安装 immobilizer，该问题不构成需要召回的安全缺陷或标准不符。因此准确表述是「NHTSA 推动企业实施软件升级，但**未启动正式召回**」；「要求召回」不等于「已决定召回」。企业关于「符合联邦法律、装置非强制标配、召回不合适也不必要」的回应是**单方法律立场**，不是监管结论，本刊不以其为「企业无责」背书。

**2025 年 12 月**还有一次收束：据康涅狄格州总检察长 William Tong 公布的协议内容（经媒体转述），由康州、明尼苏达、新罕布什尔牵头、三十余州加入的多州和解达成——现代与起亚须为未来在美国销售的所有车型标配行业标准的发动机防盗锁止器，并向符合条件车主免费提供锌合金加固点火锁芯保护器，另设消费者赔偿与州调查费用。这项协议把「安全配置是否应按市场差分」从争议推向了可执行的承诺；本刊未取得州总检察长官网原文，标注为公告经媒体转述。

**五、四条必须保留的边界**

* **配置差异争议客观存在，但责任归属未由本刊判定**：诉讼方主张「成本削减决策」，企业主张「符合联邦法律」；IIHS 的装配率数据是统计事实，不自动成为法律结论。
* **软件升级有效但不彻底：**HLDI 的 -64% / -53% 是分组对比结果，同时伴随破坏索赔上升、覆盖率不足、依赖用户正确锁车方式。
* **监管状态要写准**：未启动正式召回；多州和解与消费者集体诉讼和解是两条不同轨道。
* **未决部分不写成定论**：部分城市公共危害诉讼仍在进行；2026 年 9 月美国第九巡回上诉法院就保险公司诉韩国母公司管辖权案推翻驳回、发回重审，属进行中程序，不代表最终裁决。

**六、自然落到安全技术：物理入口与车端身份认证**

这起事件的价值，不在于追责某个零件的缺席，而在于它把一条最朴素的权限链暴露得非常完整：

**物理钥匙 → 锁芯机械转动 → 点火开关 → 起动机/喷油授权。** 链路上每一节点的「信任来自哪里」都应在 TARA 里显式建模。若身份认证节点缺失，**物理可达即等同于授权通过**——攻击门槛极低、工具极易获取、影响却是「可启动并开走车辆」，风险评级不可能低。

由此引出四条工程命题：

**1. 车端身份认证：**钥匙—ECU 采用挑战响应（可叠加滚动码），密钥不可从固件提取，应由 HSM/SE 或安全存储保护；算法与密钥不得硬编码在诊断仪或量产固件中——这正是本期技术研究室讨论 0x27 时的同一类错误。

**2. 点火链路与诊断链路隔离：**机械接口不应能旁路电子认证；诊断总线与动力/底盘控制总线做网关隔离，诊断服务与点火授权分权，避免「诊断权限横向到物理控制」。

**3. 物理接口最小化暴露：**OBD 口、诊断口、锁芯机械接口都是物理可达面，需在 TARA 中把「物理可达 + 无认证」作为独立攻击路径评估；GB 44495 的外部连接安全对 TBOX、WiFi、USB 等外部通道已有要求，纯机械接口同样需要被建模。

**4. 配置一致性：**IIHS 的 96% vs 26%（2015 年款媒体口径）与跨市场配置差异，把「安全配置不应因市场、价位、销售区域而差分」变成一条可讨论的工程原则——注意这是本刊归纳的命题，不是监管条文。

**七、给不同角色的清单**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB2aZd3yyvu3CHPe8WKic6blBLeRr1CDDhx7GtXX0bX7fwR7sDs5lVKYpdj9BPzVWibJ28A20nl8LsbfbKe6SUgcyVS8ZNjO2Ge8/640?wx_fmt=png&from=appmsg)

图5 | 谈思实验室整理制表

**八、结尾：三期，三种边界**

11 月 10 日那辆 Jeep，破的是「车内总线不可达」；11 月 11 日 CARIAD 的数据集，破的是「云上数据关联不到人」；今天这根 USB 线，破的是「机械锁芯就是授权」。三者的工程命题其实是同一句：**谁、凭什么身份、在什么条件下，能对什么总线、什么数据或什么执行机构做什么操作，并且能不能被证明。**

差别只在于，前两道边界写在固件和 IAM 策略里，第三道曾经根本没写。

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

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3...