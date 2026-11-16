---
title: 「蔚来」的数据安全课：225 万美元的勒索邮件，和一张没人签字的后台权限表
url: https://mp.weixin.qq.com/s/EMxfhjJW0-n-_xsekZrrhQ
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:44:25.421504
---

# 「蔚来」的数据安全课：225 万美元的勒索邮件，和一张没人签字的后台权限表

# 「蔚来」的数据安全课：225 万美元的勒索邮件，和一张没人签字的后台权限表

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCpMaDYVGMMtuR3fmy750iaicCKDagwQOrg64LEaCmsteVt9oP58YVs2DKiaaBP7Ls7WrHegrKtLib2VwklnMT6yamPZTbdJSEmSX8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

这一期我们讲回中国车企，讲一次没有碰到方向盘、也没有让任何一辆车失控的事件：它破的是「后台能查到，就等于有权查」。

**一、能确认的节点，与不能反推的架构**

**两处必须按住的推断：**其一，ET7 发布时公开材料明确的是 Aquila、Adam、四颗 Orin 与 1016 TOPS，**「NT2.0」是后续行业资料的归类口径，不是发布当天的官方术语**；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDpxDnjPqU3MF0anwvhYg6OG81NnwiawzRjOiaT0MR2oVb6xvSGwUcohOVMkdFnE5XFgSS8RekmDEaABWjpG8zfzk7kvF8Exagco/640?wx_fmt=png&from=appmsg)

其二，这些材料能证明该年代推进了高算力集中式平台，**推不出「使用了某一 AUTOSAR AP 版本」「部署了 SOME/IP」或「全网 TSN」。**本刊未取得蔚来量产车型的 ECU 通信矩阵或官方架构白皮书，因此全篇不写「行业首个」「算力第一」一类无来源排名，也不把架构名称当作安全结论。

**二、2022 年 12 月：一条勒索邮件，与一份上市公司公告**

2022 年 12 月 20 日，蔚来首席信息安全科学家、信息安全委员会负责人卢龙在蔚来官方社区发布《关于数据安全事件的声明》：公司于 **12 月 11 日**收到外部邮件，对方声称拥有蔚来内部数据，并以泄露数据勒索 225 万美元等额比特币；收到邮件当天成立专项小组进行调查与应对，**并第一时间向有关监管部门报告；经初步调查，被窃取数据为 2021 年 8 月之前的部分用户基本信息和车辆销售信息。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAcbh597byQ2Gam5G915QlCKl7oWicTXy31rPd25ht2h5RmQ6K55bkYRgIyE5WJsRpLjFf32kNJL5ywX49H11rt8ibfPa30gzaic0/640?wx_fmt=jpeg&from=appmsg)

图 1｜蔚来《关于数据安全事件的声明》公开截图

来源／图片性质：蔚来官方社区声明截图经媒体转载，图内可核 12-11 勒索邮件、225 万美元等额比特币、当日成立专项小组并向监管报告、2021 年 8 月前部分用户基本信息与车辆销售信息；为企业单方声明，非第三方取证报告

同日晚，蔚来创始人、董事长、首席执行官李斌在官方社区致歉：「保护好用户信息安全是我们的责任，我们没有做好，向大家深表歉意，会对此次事件给用户带来的损失承担责任……我们不会与不法行为妥协」。12 月 21 日，蔚来在港交所发布《内幕消息 就数据泄露作出回应》公告，再次确认 2021 年 8 月之前部分中国用户信息及车辆销售数据在网上被第三方违法出售，说明已在中国发布公开声明、提供专门热线及邮箱，承诺对用户损失承担责任，并表示持续与相关政府部门合作调查、采取必要措施控制潜在损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA6weqvh5vg9Fot8aOj2A0I5IbqXO9wicoLhJWFkH4nwBHjGRQrjVMtHVyL6OMwL0EgefIaQEDBkzGlv7kQAwOeyDOsRam2n2ia0/640?wx_fmt=png&from=appmsg)

图 2｜李斌在蔚来官方社区致歉的公开截图

来源／图片性质：蔚来官方社区回应截图经媒体转载；截图可证明企业公开致歉与承诺，不能证明攻击路径、数据量、根因或整改结果

这条链上能确认的是「勒索邮件 → 数据被第三方出售 → 企业公开声明 → 上市公司公告 → 致歉与承诺」，不是「车辆被攻破」。企业同日补充说明称，本次事件不涉及车辆使用中产生的数据（如行车轨迹、座舱数据），也不影响车辆的驾乘或远程控制；这是**蔚来单方技术口径**，不是独立机构复现结论。

**三、四条边界，一条都不能省**

**第一，网传出售目录不是企业审计结果，而且数字互相冲突。** 事件后网络流传一份明码标价的出售目录，媒体转述涉及员工数据、车主身份证、用户地址、注册用户、订单、退单、贷款信息等类别。但不同媒体对同一类别的条数转述不一致——例如车主身份证数据，证券时报、中国网河南写 39.9 万条，澎湃新闻写**3.99 万条**。本刊一个具体条数都不采用：这既不是企业公布的影响范围，也没有独立取证报告支撑，更不该被写成「蔚来确认泄露 XXX 万条」。企业初步调查给出的范围只有一句话：2021 年 8 月之前的部分用户基本信息和车辆销售信息。

**第二，企业口径与第三方判断要分开**。 中国汽车工业协会秘书长助理兼技术部部长王耀当时对媒体表示，以其个人初步判断「这次不是因技术问题导致的数据泄露」「目前看，对于蔚来汽车用户来说，不会出现系统性大规模数据泄露，也不会引发车辆端安全问题」；另有互联网安全技术人员对媒体推测「应该是对蔚来汽车 APP 后台数据库攻击而获取的信息」。**前者是协会人士个人初步判断，后者是第三方推测，两者都不是监管结论或取证报告，**正文不作事实引用。

**第三，本期未检索到的，就写「未检索到」**。 截至本期检索，未找到监管立案、行政处罚、整改验收的公开文件，也未找到与本事件对应的 CVE 编号或召回编号。这不等于「不存在」，更不等于「企业无需整改」。

**第四，勒索不等于中央计算平台有漏洞**。 数据泄露与数据被出售，和「某量产车可被远程控制」是两个命题。把两者写成因果，就是把一次后台数据安全事件包装成车辆安全事件——这既不准确，也会让真正的工程命题（**权限、分级、审计）**被漏掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDmJKQ2QYy8y4kbC6t5RQX4u6v4Lf9YB71eaz7rvBraLicVrdPAWIUviaxJxhdQBYiaFJuy9jGROwgpYNgbfIEmArKsROTRGJ7fibQ/640?wx_fmt=png&from=appmsg)

图 3｜2022 年 12 月：一条勒索邮件，与它留下的证据边界

来源／图片性质：谈思实验室编辑部绘制，依据蔚来官方声明、港交所公告与多家权威媒体交叉整理；图内已标注企业口径、媒体转述与待核实项，非事件取证图

**四、修好的是什么，公开材料能证明什么**

事件后的公开材料里，能看到蔚来参考 **UN R155 与 ISO/SAE 21434**搭建车辆网络安全管理体系：由整车生命周期网络安全管理办法、安全管理方针、风险管理办法、安全测试与验证管理办法、事件及漏洞管理、合作伙伴管理六部分组成；以 V 模型为参考，在概念阶段识别网络安全目标与需求、设计阶段做 TARA、开发阶段落实安全编码、测试验证阶段做需求验证与渗透测试、生产阶段审核生产控制与一致性计划、运维阶段定义事件响应与漏洞监控、报废阶段清除敏感数据。企业文章还提到云侧防火墙、严格访问控制、故障转移与异地灾备，APN / 加密 / 专线通信，自研 PKI，数据脱敏、加密、假名化、最小权限与冷热备份，以及 IDS/IPS 与日志审计。

**请把属性读准**：这些是**企业工程实践自述**，不是监管对本事件的整改验收，也不构成对 2022 年事件根因的官方说明；同一材料提到的 DEF CON Car Hacking Village 夺旗赛夺冠、世界智能驾驶挑战赛信息安全挑战赛第一名，只能说明竞赛表现，不能证明产品安全。本刊同样不把「事后排查与强化」写成「同类风险已消除」。

真正可迁移的工程判断是：一**次后台数据事件，检验的是「谁能查、查了什么、能不能被证明」**，而不是检验车端防火墙。

**五、从后台权限表，到本期技术研究室的四层链**

把这道题接到本期 B 块的框架里，就是一张分层的权限图。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDdYN0XO3BWMxQiajWZ2qFK7IYqHqO6Z2Ty0NpOicwxQicNVb4UmjK5pLaiab30bcEoibMjiaibdNaicJ80HF5Lk96ibH8oJHDCJlNjlVTQ/640?wx_fmt=png&from=appmsg)

图 4｜勒索之后真正要回答的：谁、凭什么、查了哪类数据、能不能被证明来源／图片性质：谈思实验室编辑部绘制示意图，非蔚来官方架构图或整改报告

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA5KuhBduOAllpGGyYic84C1NxMInHBicibGKTQpfERhYDOwVzNoGg2zNo2HtiaymJyUfzCsXMXzdwhXhunkgA8lSkZJxGPNK1wbBo/640?wx_fmt=png&from=appmsg)

**三句不能混淆的判断**：SOME/IP-SD 白名单只保护 SOME/IP 这一层绑定，不能替代应用层 Grant；gPTP / TSN 决定「什么时候发、占哪条队列」，不决定「谁有权查」；OTA 之后既要回归功能，也要回归权限矩阵、Grant 差分与异常访问基线。

合规衔接上，本期新闻篇那份《汽车数据安全要求（征求意见稿）》拟的是**车端默认不收集、未激活功能不调权限、拒绝后不反复索权；蔚来这道题问的是后台默认谁能查。**一头管采集，一头管访问，合起来才是「数据全生命周期」。ISO/SAE 21434 的 TARA 应把「后台服务 — 数据库 — 运维账号 — 审计日志 — 跨域网关」画成连续攻击路径；UN R155 的 CSMS 与 GB 44495 的外部连接 / 通信安全域，要求的是持续监测、响应、供应商接口与证据留痕，而不是一份事后的声明。

**六、给不同角色的清单**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAIdkw4wR746YO98NdsuWCQp1m45pKicztY0Zmmn2P3Sib9QicU5icWrBDoaYY4ib4d9TRs5soQVUtD36R69RBkc5y1ic7gicbxNo5dPo/640?wx_fmt=png&from=appmsg)

**七、六期，六种边界**

11-10 的 Jeep，破的是「车内总线不可达」；11-11 CARIAD 的数据集，破的是「云上数据关联不到人」；11-12 那根 USB 线，破的是「机械锁芯就是授权」；11-13 从浏览器到 CAN 的链，破的是「进了车机等于进了受信网络」；11-14 的 220 万辆车门，破的是「连上了服务端就等于官方」；今天这封勒索邮件，破的是「后台能查到，就等于有权查」。

六期合起来还是同一句工程命题：**谁、凭什么身份、在什么条件下、能对什么服务、什么数据或什么执行机构做什么操作，并且能不能被证明。** 差别只在于：越往后走，「能被证明」这四个字越不依赖一段声明，而越来越依赖一张有人签字、会被定期复核、且在 OTA 之后仍然成立的表。

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

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247502093&idx=1&sn=ec4b373a33ca04d79afbb0b0b880bd4e&chksm=e9278dd6de5004c01bdd83ad0dd89c3549c7ae2ceb362959dbcb159324b2593d70bce78d82a9&scene=21#wechat_redirect)

[汽车数据安全合规重点分析](http://mp.weixin.qq.com/s?__...