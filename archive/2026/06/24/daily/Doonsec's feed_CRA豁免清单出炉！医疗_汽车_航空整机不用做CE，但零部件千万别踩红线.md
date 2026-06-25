---
title: CRA豁免清单出炉！医疗/汽车/航空整机不用做CE，但零部件千万别踩红线
url: https://mp.weixin.qq.com/s/DkqM2lrEFyCO28IGL5tvGg
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:35.175402
---

# CRA豁免清单出炉！医疗/汽车/航空整机不用做CE，但零部件千万别踩红线

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U5ROicHxZUzp8wtWIIjCvaBdnWVsgEwhGWMX5An9ZrVVRTRshZ0WA23PUhvZaRmWRNDyn9Jb9Qm4emTM37uD9DXlsNB59EYicCy7CXSbw2ShA/0?wx_fmt=jpeg)

# CRA豁免清单出炉！医疗/汽车/航空整机不用做CE，但零部件千万别踩红线

原创

GTG-Hardy
GTG-Hardy

GTG网络安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/U5ROicHxZUzpGpJn4CprafeJTic67ay95KgSDINiaaoxvavC2vpcxQwl5vTvgq6x8E1EWjpxn4pMPF1nODXBlu90Q6AYv0qHemQWqFAambTYsY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzrKTTRuOOo8SMsto62734GrVLRGNaKkaJgoNyWeuBLjmAmib6Lvamibmg5D70BrSwaMTDB9RW4TnddPaWwnbXoR0fB5XYXLpoOicE/640?wx_fmt=png&from=appmsg)

不少医疗、车载、船舶、航空设备出海企业有个大疑问：我们产品已有行业专项合规认证，2027 年 CRA 全面落地后，还要额外做全套网络安全评估、CE 标识吗？

欧盟官方 FAQ 1.9 给出权威豁免规则，四大行业整机可免于 CRA 管控，但分立零部件单独销售不享受豁免，90% 供应链企业都在这里踩坑，轻则整改，重则产品下架、高额罚款。

今天结合法案原文与官方解读，一次性分清豁免边界、例外场景、企业自查方法。

**一**

**立法底层逻辑：**

**行业专项法规优先，避免双重合规**

欧盟出台 CRA 作为横向通用数字产品网络安全法规，但医疗、汽车、民航、海事等高风险领域，早已出台配套专项法规，内部已完整覆盖设备网络安全、漏洞修复、软件更新全生命周期要求。

为减轻企业重复认证负担，CRA 第 2 条明确：已受专项欧盟法规完整监管的整机产品，直接豁免 CRA 全部义务，无需重复开展 CRA 合格评定、技术文档搭建。

**二**

**官方明确5大类可豁免整机产品**

**（FAQ1.9原文清单）**

![](https://mmbiz.qpic.cn/mmbiz_png/U5ROicHxZUzpmuRHlKfWbuPQKhI10C5kcicicvQKLicp3qh02nndSXNzADpcZCKdACM8AknEEqColDq9D94Go6J3KORBic08CGEWXoKPOoHNHLMA/640?wx_fmt=png&from=appmsg)

1. 医疗器械 & 体外诊断设备

适用法规：(EU) 2017/745 MDR、(EU) 2017/746 IVDR覆盖：医用监护设备、手术器械、诊断分析仪、医用软件、可穿戴医疗监测设备等整套医疗产品。规则：完成 MDR/IVDR 认证整机，不受 CRA 约束。

2. 机动车、配套整车系统及专用部件

适用法规：(EU) 2019/2144 机动车型式批准法规覆盖乘用车、商用车、车载车机、电控单元、整车配套系统；补充：三轮 / 四轮机动车同样豁免；唯一例外：人力脚踏 L1e 两轮电动车，不在豁免范围内，必须遵守 CRA。

3. 取得 EASA 认证民航整机与机载成套设备

适用法规：(EU) 2018/1139 欧盟民航基础条例覆盖民航客机、通航飞机、经过 EASA 认证机载软硬件；边界区分：开放式消费类无人机、未单独航空认证机载组件，不享受豁免。

4. 海事船舶成套设备

适用指令：2014/90/EU 海事设备指令船舶导航、通信、控制整套海事设备，遵循海事法规即可，无需 CRA 合规。

5. 纯国防、国家安全专属设备（补充联动 FAQ1.8）

仅专门为国防、涉密场景研发改造产品豁免；普通军民两用通用电脑、工控、路由器，依旧适用 CRA。

**三**

**致命红线：**

**豁免仅针对整机，单独售卖零部件无豁免**

这是整条 FAQ 最核心、最容易忽略的约束条件，也是供应链厂商高频违规点：

即便零部件最终用于医疗 / 汽车 / 航空 / 船舶整机，只要单独投放欧盟市场、独立销售，就不属于行业专项法规管控范畴，必须完整执行 CRA 全部要求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzr5U67I3GPpG4Aibg3QaSib7uVMvYkSl0WX1Iws2zWbd8MmZ2QWpkNhPs89uG6JYRu890Ev9l1QT6Xc6eYn0u2RC2YnohAmHuOeY/640?wx_fmt=png&from=appmsg)

举 3 个典型踩坑案例

1. 车载芯片厂商单独向多家车企售卖车载 MCU 芯片，芯片未纳入整车型式认证流程。判定：芯片独立上市，必须完成 CRA 风险评估、CE 标识、漏洞管理体系。
2. 医用传感器供应商单独销售数字化医用传感器，医院 / 设备厂商采购后集成进医疗设备。判定：分立组件单独流通，受 CRA 监管。
3. 机载固件服务商单独售卖飞机通用嵌入式软件，不随整机配套认证。判定：软件独立投放市场，需要 CRA 全套合规。

补充备件特殊规则

一对一替换原厂、不改变产品数字功能的同款备件，可豁免；若备件新增联网、数据处理功能，则不再享受豁免。

**四**

**4个高频误区，出海企业一定要避开**

误区 1：只要是车载 / 医疗配件，全都不用做 CRA

错！区分销售模式：随整机配套供货、不单独售卖→豁免；单独上架分销、对外零售→强制 CRA。

误区 2：开放式消费无人机属于航空豁免范畴

错！仅取得 EASA 航空认证的专业机载设备豁免，普通娱乐、商用开放式无人机无航空认证，适用 CRA。

误区 3：脚踏两轮电动车也能享受机动车豁免

错！法规明确 L1e 脚踏类两轮电动车排除在机动车豁免名单之外，必须遵循 CRA。

误区 4：整机豁免 = 不用管网络安全

错！只是免除 CRA 义务，企业仍需严格遵守 MDR、汽车型式认证、EASA 等行业法规内的网络安全、漏洞更新强制条款，行业监管机构会单独核查。

**五**

**企业快速自查三步法（直接落地使用）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzrU0gDz4EAhErH2OKG5gnczrYT6GicUSOTWVspXChZEglzRT4WUFpTg0zsYpTXHMTnOibro1MzDyYpiaOG3auI6T6lX1JelLeUqEs/640?wx_fmt=png&from=appmsg)

1.判断产品品类：是否属于医疗 / 机动车 / 民航认证整机 / 海事成套设备？

2.判断销售模式：产品是否单独在欧盟市场售卖、独立流通？

· 整机成套销售、不拆分组件：享受 CRA 豁免；

· 芯片、固件、传感器、软件单独供货：必须 CRA 合规；

3.特殊品类校验：脚踏电动车、消费无人机、军民两用通用设备，无豁免。

**六**

**不同厂商落地行动建议**

整机设备厂商（医疗 / 车载 / 航空 / 船舶）

1. 留存全套行业认证证书、型式批准文件，证明整机合规资质；
2. 梳理上游供应链，明确区分配套集成零部件、独立售卖零部件，要求独立组件供应商提供 CRA 合规材料；
3. 内部台账区分整机与分立组件，避免两类产品合规混淆。

零部件 / 软件供应商（芯片、固件、传感器）

1. 无论下游客户属于哪个行业，只要产品单独销往欧盟，提前启动 CRA 风险评估；
2. 建立组件漏洞响应、长期安全支持机制，准备 CE 标识、符合性声明；
3. 区分供货模式：专供整机厂配套、不单独流通，可与客户书面留存集成证明，降低核查风险。

![](https://mmbiz.qpic.cn/mmbiz_png/U5ROicHxZUzo3WFLmolpO9lelKN1P8BFgP1icyKzgBOMS5K19iavTvcM6vv508JBhUL6QlrnaD6y0GuaTiazUoDIwiaAaibtp3xjmPyIc0wMwxdDw/640?wx_fmt=png&from=appmsg)

1. 医疗、机动车、EASA 认证民航、海事成套整机，可豁免 CRA 全套合规要求；
2. 分立芯片、软件、传感器等组件只要单独上市销售，不享受行业豁免，必须落地 CRA；
3. 脚踏两轮电动车、开放式消费无人机、通用军民两用产品，无豁免；
4. 豁免不代表免除网络安全责任，仍需遵守对应行业法规安全条款；
5. 供应链企业是监管重点，单独售卖零部件极易因遗漏 CRA 整改产生损失。

欧盟数字安全监管持续细化，分清整机与组件的豁免边界，才能合理控制认证成本，规避市场处罚风险。

**广测电磁：全球数字安全合规优选伙伴**

**别让合规只停留在“拿证”。**

面对欧盟 CRA网络弹性法案、AI法案及 GDPR/CCPA/数据法案等严苛监管，凭借CNAS(L18872)+A2LA(6947.01)双资质及前360/深信服核心网络安全专家团队，为您提供真正的“实战级”防护。

**🏆 为什么GTG能为您降本避险？**

* 拒绝模板：不只给报告，我们提供定制化漏洞修复方案，确保产品真安全。
* 极致省心：代写核心文档，免除繁琐填表，让合规效率提升70%。
* 全域覆盖：从消费电子到汽车、工控、医疗，一站式解决全球隐私与数据安全难题。

您的全球合规通行证，从这里开始。

**[👉 立即咨询 CRA / AI法案 / 隐私合规]**

更多相关内容

欢迎关注视频号**“GTG网络安全实验室”**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzrP38LQm0Ew4Yv2aIAWoqAs810WiavVWvibTrYN9ho4Gj1a4Heja7Rr9rCxro15xhuORvMOKY7BzEhw4bIHMgACNGDVbC1dDjtIM/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nU5v4aGBAyTCxIBHVZGhicPLY9XcpAMrBicsiaXF1ERvicoRgK6vx53LwYgdT5XnNziah1Mdmib8RsvVic7hrVm5fEI7Q/0?wx_fmt=png)

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