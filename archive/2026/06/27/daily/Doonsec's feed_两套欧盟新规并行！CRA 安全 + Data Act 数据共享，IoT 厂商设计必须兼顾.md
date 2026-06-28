---
title: 两套欧盟新规并行！CRA 安全 + Data Act 数据共享，IoT 厂商设计必须兼顾
url: https://mp.weixin.qq.com/s/hKEYXtXBE3WFuLQvkNnSiw
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:12:20.505396
---

# 两套欧盟新规并行！CRA 安全 + Data Act 数据共享，IoT 厂商设计必须兼顾

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/U5ROicHxZUzoNX4Sq9wKkBhfzXgIKHsiardf10JFiaey81g5cHkGykibpcCN4G87uRibVljA540N5BsN6XKsiceM4ml3Iria5ic5LEAgfELfv5ricKVg/0?wx_fmt=jpeg)

# 两套欧盟新规并行！CRA 安全 + Data Act 数据共享，IoT 厂商设计必须兼顾

原创

GTG-Hardy
GTG-Hardy

GTG网络安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/U5ROicHxZUzqV15sPJj9BowBS3RGUbV8DgibQ0lj62bSn994YQj2gpazMmnZKoaJHYyuhlYe1vecDmK8bUYiaJIekC8exHFKe62gTicibCqgOQs0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/U5ROicHxZUzoK1cGFF1aPa1t0FIK48zGZCkBBbH3S6vPwd877yWen4rTMlWJ1CGa3Y0rISfKFvNNhA4PgJkpGibhVDcQt3PyTgvrQVog21u8o/640?wx_fmt=png&from=appmsg)

做智能家居、工业物联网、车载设备的出海企业注意，除 CRA 网络弹性法案外，欧盟《数据法案》（Data Act）早已在 2025 年 9 月生效。很多企业分开做两套合规，出现接口开放但无安全防护、加密完善却无法提供用户数据的矛盾设计。

欧盟 CRA 官方 FAQ 2.9 专门厘清两套法规边界、产品设计要求、风险评估联动规则，今天一次性讲清如何一套硬件 / 软件同时满足两套强制要求。

**一**

**CRA和Data Act管完全两件事，**

**只是IoT产品会双重约束**

1. CRA：管住设备底层网络安全（上市门槛）

定位：所有带联网软硬件的强制准入法规

核心义务：出厂无高危漏洞、默认安全配置、5 年安全补丁、漏洞上报、CE 合格评定

目标：防止黑客入侵设备、劫持系统、横向渗透

2. Data Act：管住设备产生的数据流通（数据公平）

定位：规范联网设备运行数据的访问权法规

核心义务：用户可免费、标准化调取设备运行、诊断、工况数据，厂商不能锁死数据、不能设置高额数据提取费用

目标：打破设备厂商数据垄断，激活工业、消费数据流通

重叠覆盖产品（必须双合规）

智能家电、工业 PLC、物联网传感器、智能农机、车载终端、共享设备

仅适用 CRA：路由器、交换机、纯工控服务器

仅适用 Data Act：无实体硬件纯云端 SaaS 数据服务

**二**

**核心合规红线：**

**数据共享风险必须写入CRA风险评估**

根据官方 2.9.2 原文，厂商开展 CRA 全生命周期网络安全风险评估时，必须把 Data Act 强制对外数据开放场景纳入风险分析。

典型风险场景

为满足用户数据调取需求，设备开放 API、本地数据接口、云端数据通道，这些接口会成为黑客攻击入口，存在越权读取、数据篡改、远程控制风险。

厂商合法缓冲机制（两大刹车条款）

如果开放数据接口会带来重大网络安全风险，或涉及企业核心商业秘密，厂商可依法限制数据共享，同时在技术文档留存完整佐证材料：

1. 安全刹车：数据开放会引发设备被入侵、系统瘫痪；
2. 商业秘密刹车：算法、核心工艺、自研控制逻辑属于商业秘密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzoZSWM0OR0DXtXSh178q6iaoIVvcvjaK3NbgTR8ib67cBUpPgXZjqxeTVdPS0Poc3Ld7Ms3DcQ2MumKaaHMsa7KMQNHMrpB8NgRg/640?wx_fmt=png&from=appmsg)

文档必备内容

1. 设备哪些数据需对外提供（Data Act 要求）；
2. 数据接口存在的攻击路径、安全隐患；
3. 配套防护手段：接口鉴权、传输加密、访问日志、权限分级；
4. 启用数据限制刹车的判定依据与管控方案。

**三**

**不用两套产品架构！**

**一套设计兼顾安全与数据开发**

很多厂商误区：要同时满足两套法规，必须开发两套设备版本，一套封闭保安全、一套开放给用户取数。FAQ 2.9.3 明确澄清：法规不强制厂商重新独立设计产品，无需两套硬件 / 固件。

正确落地思路：在同一套产品内分层设计：

1. 对外标准化数据接口（满足 Data Act 免费、机器可读输出要求）；
2. 接口配套身份校验、传输加密、访问审计、超时阻断等安全能力（满足 CRA 默认安全要求）；一套软硬件同时实现数据可流通、攻击难入侵。

新旧产品区分要求

1. 2027.12.11 前投放市场存量设备：无重大改版不用重做全套 CRA，但 Data Act 数据开放义务照常履行；
2. 2027 年底后新上市产品：研发阶段同步融合两套法规需求，一次设计完成双合规。

**四**

**3个极易踩坑合规误区**

误区 1：做好 CRA 加密防护，就能拒绝用户调取设备数据

错！CRA 只约束安全层面，不能豁免 Data Act 数据开放法定义务，仅能凭安全 / 商业秘密刹车有限限制。

误区 2：设备只做数据开放接口，不用评估接口安全风险

错！未将数据通道风险写入 CRA 技术文档，市场监管核查会直接判定产品不合规，要求整改下架。

误区 3：两套法规分开设计两套产品版本

错！官方明确无需两套独立架构，分层接口 + 安全管控即可同时达标，额外增加研发与库存成本。

**五**

**IoT厂商落地行动清单**

1. 产品立项同步梳理 Data Act 要求输出的全部设备数据清单；
2. 在 CRA 网络安全风险评估新增「外部数据接口专项风险章节」；
3. 统一接口标准，兼顾机器可读输出 + 鉴权加密安全防护；
4. 整理安全、商业秘密刹车使用判定标准，归档备查；
5. 存量设备升级固件时，同步补齐合规数据接口与安全防护模块。

**六**

**总结**

1. CRA 管设备网络安全准入，Data Act 管设备数据开放权利，IoT 联网产品需双重合规；
2. 数据对外接口带来的攻击风险，必须完整记录在 CRA 技术文档；
3. 无需两套产品架构，单一软硬件分层设计可同时满足两套法规；
4. 2025 年 Data Act 已全面实施，2027 年底 CRA 全面落地，提前同步设计规避双重整改成本。

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzrFq6dDz44ibAOoMGXCYPzM5UTF24BoeULIdH1I7TCkfaTw9jcTkMkI60MO7yxMz2EwQPzNxL1eJ4ic16Vt45QCPtXFCkZtLrlA4/640?wx_fmt=png&from=appmsg)

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