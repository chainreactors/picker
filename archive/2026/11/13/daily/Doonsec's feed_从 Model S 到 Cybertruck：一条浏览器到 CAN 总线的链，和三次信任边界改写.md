---
title: 从 Model S 到 Cybertruck：一条浏览器到 CAN 总线的链，和三次信任边界改写
url: https://mp.weixin.qq.com/s/qdjq3C9Kjsp2ig08TmdFrQ
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:15:55.668562
---

# 从 Model S 到 Cybertruck：一条浏览器到 CAN 总线的链，和三次信任边界改写

# 从 Model S 到 Cybertruck：一条浏览器到 CAN 总线的链，和三次信任边界改写

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCpMaDYVGMMtuR3fmy750iaicCKDagwQOrg64LEaCmsteVt9oP58YVs2DKiaaBP7Ls7WrHegrKtLib2VwklnMT6yamPZTbdJSEmSX8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

当座舱大屏、网关和动力总线被串进同一条链，OTA 既是修复通道，也是新的信任假设。我们讲特斯拉，但不替它下结论——只把研究披露、监管公告、企业回应与第三方拆解分层摆开。

**一、四个时间节点，先把能确认的和不能确认的分开**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBpuB5EmkFCn7xBNTs3lbX9tuukj7ianfjNLO5oErfJI7Pyxs1OC3vKs88qklwUpoHicjwRlXQMo3GsJsSvNZayRHqTbTSdqzvQs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCzvOrs931icCWTK5oZGLvCqQ1DHsFrQlYZ9H7icuNbtIm3v9xicQTsOdoYS19o1oyTw3wuTBznAzyLgowRibiaDp3JQyZZWJK1x0Pw/640?wx_fmt=jpeg&from=appmsg)

图 1｜2012 年特斯拉 Model S 的 17 英寸竖式中控屏

来源／图片性质：媒体 / 行业研报配图（含原出处水印），非 Tesla 官方图库；仅作车型形态与交互形态示意

**必须提前说清：**具体 E/E 架构图、CAN 域划分、区域控制器数量与以太网速率，多数来自 Munro 等第三方拆解、券商与行业媒体整理。本刊本次**未取得 Tesla 官方架构白皮书**，因此下文涉及架构拓扑的表述一律标注为「第三方拆解 / 行业分析」，不写成企业公告。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaBBsk8zkO5am08UuLynyiaG30Mk2Lv2EWYmKJNQV1kClcIgmxtOBB1xss8q0UJ4Q8mo3U6N3SMjA8H3iaMHheMIQcyAUsXX6GXe4/640?wx_fmt=jpeg&from=appmsg)

图 2｜2017 年 Model 3 内饰与 15 英寸横向中控屏

来源／图片性质：媒体配图，非官方图库；与 Model S 的 17 英寸竖屏形成交互形态对照

把三代节点连起来看，不是「越来越先进」，而是**信任边界被三次重画**：2012 年大屏把座舱与车控拉近；2017 年前后代码签名与网关成为修复主通道，网关同时变成判决点；2023 年区域化把功能收敛到少数控制器，节点少了，单点失陷的影响面却可能变大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBJ8Gc5RWmaFPV7HXzqwJWCqlic64pD5z4ddhjCKZ8cyAtQsltey14ctKjNziaaLRg8TwHXCksbhT2gBokicibrOSwkVunpIpGZFFE/640?wx_fmt=png&from=appmsg)

图 3｜从 Model S 到 Cybertruck：架构在收敛，信任边界在重画

来源／图片性质：谈思实验室编辑部绘制示意图；时间节点由权威媒体交叉，第三行拓扑为第三方拆解推断，非企业官方架构文档

**二、2016：从浏览器到 CAN 总线，一条完整的链**

2016 年 9 月，腾讯科恩实验室公布对 Model S 的无物理接触远程攻击研究。公开演示里，研究人员在约 10 米外用笔记本，通过 Wi-Fi / 蜂窝网络进入车机 Web 浏览器，最终向 CAN 总线发送消息：驻车状态下可开天窗、点亮转向灯、调节电动座椅、使中控触屏失效、无钥匙解锁车门；行驶状态下可折叠后视镜、打开后备箱、控制雨刮，并触发制动——**研究者特别指出，这种制动不点亮刹车灯，高速场景下容易造成追尾。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD96icGBpjPpJEjiaYSZoWVWZdTu9MZrbnfBjFSkdI5XMuGcvDTGdXxOzDAXoL9X52KSdCamoUh4bypMl0W4pr40QqLVsPTNNiawU/640?wx_fmt=png&from=appmsg)

图 4｜2016 年科恩实验室披露的跨域攻击链、两次 OTA 修复与硬件信任根提醒

来源／图片性质：谈思实验室编辑部绘制，依据 CISA 公告、科恩实验室公开说明与会议报道整理，非厂商架构图

比演示更硬的是监管一手材料。CISA（当时 ICS-CERT）发布**ICSA-16-341-01「Tesla Gateway ECU Vulnerability」**：腾讯科恩实验室发现 Gateway ECU 漏洞，影响**所有低于 v7.1（2.36.31）且启用 Web 浏览器功能**的固件；攻击者经浏览器利用**网关 ECU 的固件校验缺陷**向 CAN 总线发送消息；编号 **CVE-2016-9337**，CVSS v3 基础分 6.8，归类命令注入（CWE-77）；公告明确**「无已知公开利用代码专门针对该漏洞」**，并指出构造可用利用链难度高，需要浏览器入侵、本地提权与定制固件。Tesla 于 **2016 年 9 月 18 日**发布 OTA 固件更新。

**这几条限定一个都不能丢**：特定固件版本、浏览器功能启用、复杂利用链、研究者演示环境。把它们简化成「2016 年特斯拉全系可被远程控制」，是把研究结论写成了无来源断言。环球网转述 Tesla 表示在接到报告后 10 天内展开软件升级，**属企业口径**；同年 Tesla 官网公开致谢科恩实验室、后者进入 Security Researcher Hall of Fame，由央广网与海外网交叉确认——但公开材料不足以支持「行业首个漏洞赏金计划」「行业首个名人堂」这类排名表述，本刊不写。

**三、2017：代码签名之后，网关成了新的判决点**

科恩实验室官网的一手说明写得很清楚：2017 年再次发现多个高危漏洞，实现驻车模式与行驶模式下对车辆的无物理接触远程操控；2017 年 6 月底按负责任披露流程把全部技术细节报告 Tesla 美国产品安全团队；Tesla 快速确认漏洞有效性与危害，并于 7 月初通过 FOTA 推送修复固件；实验室提醒车主确认已升级到**8.1（17.26.0）或以上**。演示中的「灯光秀」涉及多个 ECU 的远程协同操控。

技术媒体的复盘补上了关键一环：2016 年 9 月事件后，Tesla 为 FOTA 包引入**代码签名**校验；2017 年 Black Hat USA 的 FREE-FALL 研究（刘陵、杜越丰、聂森）展示了绕过代码签名、实现任意 CAN 帧远程注入的完整链路。新华网 2017 年 7 月 31 日的报道同样记录两次修复版本：v7.1（2.36.31）与 v8.1（17.26.0+）。

所以这一年的工程含义不是「签名没用」，而是：**网关从转发器变成了判决点，判决点本身也就成了攻击目标。**签名回答「刷进去的是什么」，网关回答「谁被允许发起」——这两个问题在本刊第 03 期讲刷写权限链时已经拆过，2017 年的案例把它们放到了同一条真实攻击链上。

**四、2023：OTA 覆盖不到的硬件信任根**

Black Hat 2023 上，柏林工业大学研究者（含 Christian Werling）公开了针对 Tesla 基于 AMD 的 MCU-Z 信息娱乐系统的研究：用**电压故障**注入攻击 AMD Secure Processor（ASP，系统信任根）的早期启动代码，获得 recovery 与 production Linux 的 root shell，并可提取**TPM 保护的车辆证明密钥**——该密钥被 Tesla 用于服务网络中的车辆认证与硬件平台完整性校验，研究者称可迁移到另一辆车、用于车辆 ID 冒充。工具成本被描述为烙铁加约 100 美元电子元件（如 Teensy 4.0 板）。

**证据分层要写足：**

* Tesla 的回应由研究者向媒体转述——后座加热解锁的 PoC 基于旧固件版本，新版本中该配置项更新需 Tesla 有效签名，且由**网关检查并强制执行**；若要解锁仍需另一个针对网关的软件或硬件利用。这是企业回应经转述，不是监管结论。
* 研究者同时称，密钥提取攻击在当时的最新软件更新中仍然有效；并明确澄清部分媒体所称「可解锁 FSD」**不属实。**
* 该研究为会议披露与负责任披露，**无召回、无监管公告**，本刊不写成「量产车已被实际攻击」。

它给本期主题补上了最后一块：**OTA 能修软件逻辑，修不了已出厂的硬件信任根**。代码签名可以约束「未经授权的固件运行」，但保证不了签名之前的源码、编译链、第三方依赖组件与调试接口没有缺陷——这也正是本期新闻篇里 SBOM 与软件缺陷管理要解决的问题。

**五、中立收束：三组事实对照，不写公关稿也不写指责**

**第一组，能力是真实的**。 两次披露都形成了「研究者报告 → 企业确认 → OTA / FOTA 推送修复版本」的公开协同路径，修复时间以天到周计。这在 2016 年的汽车行业并不常见。

**第二组，能力有边界**。 OTA 依赖车辆在线、目标版本、安装成功与足够存储；长期离线车辆、非目标市场、跳过版本、升级失败或未被覆盖的硬件信任根，都不能凭「已发布 OTA」推定已修复。Tesla 关于影响范围的回应（据新华网 2017 年报道转述，企业称未发现顾客受到攻击）属于企业单方口径，与 CISA 公告「无已知公开利用」也不是同一件事——后者是 2016 年公告时点的状态描述。

**第三组，架构不是安全结论**。 48V 降低的是线束截面、连接器热负荷与配电损耗；以太网提供的是带宽。**两者都不等于「更抗网络攻击」**。区域控制器把功能集中到少数 ECU，若网关对所有子网使用同一套路由规则，一个合法诊断身份可能访问更多目标；反之，若每个区域控制器只开放必要 VLAN、目标地址与服务码，并维护独立凭证、会话、审计与回滚，集中化也能缩小爆炸半径。风险方向取决于隔离与控制粒度，不取决于架构名称。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBX2s0mVHVWo22q74JiazROAUH5FsHAqqFicAwfsollEBTIicEneY6mibBNOKYhJ0GBF1Nf18d25Ajqibpqj1iakoAsuialRKH2nIK9nI/640?wx_fmt=png&from=appmsg)

图 5｜Cybertruck 外观

来源／图片性质：公开媒体图片，非 Tesla 官方新闻图库；仅作车型形态示意，不代表本文对架构细节的事实认定

我们把企业单方口径、第三方拆解、会议披露、监管公告与媒体转述分成五类归档，因为它们的证据强度不同，不能相互替代。公开资料里常见的「全球首套量产 48V」「全车以太网」等表述，多出自拆解者或行业分析，本刊按第三方推断处理，不作事实断言。

**六、自然落到本期技术主线：诊断口 IP 化之后**

2016 年那条链与本期技术研究室共享同一个因果：**外部入口 → 车机 → 网关 → CAN / ECU。**车机一旦进入受信网络，就必须重新做一次身份认证与权限决策，不能沿用「物理接触即可信」的旧模型。

于是四件事被串成同一条证据链：

* **DoIP 车辆发现与路由激活**：收到车辆通告不等于对方已认证；路由激活成功不等于任意目标 ECU 可达（第 04 期核心）。
* **证****书、VLAN 与目标 ECU 白名单**：2023 年 Tesla 回应里「由网关检查并强制执行签名」，正是网关作为判决点的工程表述；把它做成可审计规则，才谈得上诊断防火墙。
* **UDS 会话与服务限流**：0x27 解锁后最小权限、会话超时重新上锁、Bootloader 与应用独立密钥（第 03 期）。
* **SBOM 与 OTA 回归：**区域化以后，一张攻击图要同时覆盖交换机、区域控制器、ECU、诊断仪证书、签名密钥、SBOM 构建产物与日志；ISO/SAE 21434 的 TARA、GB 44495 外部连接 / 通信安全域、UN R155 CSMS，都要求把「OTA 后策略是否漂移」写进验证记录。

**七、给不同角色的清单**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAYbuvwVmKrmRC17lX7DKkabxMYJYRPFaYougmapKr1k2EYxy4usQ9xNQzJfISWwYBDqOyn69A4Ca0ou2b8FgMNzRPibjWMtFj4/640?wx_fmt=png&from=appmsg)

**八、四期，四种边界**

11 月 10 日的 Jeep，破的是「车内总线不可达」；11 日 CARIAD 的数据集，破的是「云上数据关联不到人」；12 日那根 USB 线，破的是「机械锁芯就是授权」；今天这条从浏览器到 CAN 总线的链，破的是「进了车机就等于进了受信网络」。

四期合起来其实还是同一句工程命题：**谁、凭什么身份、在什么条件下，能对什么总线、什么数据或什么执行机构做什么操作，并且能不能被证明。** 差别只在于，这条链每往前走一代，能做证明的地方就多一层，需要证明的东西也多一层。

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

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz...