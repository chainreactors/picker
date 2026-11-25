---
title: V2X 信任体系里的证书、假名与撤销
url: https://mp.weixin.qq.com/s/WRajGLF3vcGV6IUzTjDMWQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:41:42.663630
---

# V2X 信任体系里的证书、假名与撤销

# V2X 信任体系里的证书、假名与撤销

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB995ym51yuiaz6UL4C02FAq637ia0w2GiaMZ1NeOTbZsFia0oXMWjkiatyNdibc3tWmRVo9GcFVPnLmf3HcbwDyar3YhWkLDt0DZ4SY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

车云通信里，双方可以先握手、再协商、还能查在线状态；车路协同不行。一辆车在路口以广播方式发出「我要刹车」「前方有障碍」，周围几十个接收者没有会话、没有回连、也不该知道这辆车是谁。于是 V2X 把公钥基础设施推到了一个很极端的角落：既要让陌生人立刻验证消息，又要让同一辆车不被长期追踪，还要能在发现它撒谎时把它从系统里摘出去。这三件事互相拉扯，构成了车路协同安全最核心、也最容易被低估的一层。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDZJicFt0YM4OzRLiafNY6XVoroIQsOjCRR0b3Sp4XBZVB8arUBo3iaNhjuhuKoxubwXV9x6cOt82dTnso9YibJFceiaXMTyyJscJs0/640?wx_fmt=png&from=appmsg)

图 1｜V2X 路侧单元 RSU 设备

**一、先把信任拆成三问**

车路协同的消息大多是广播：发送方不指定接收者，接收方也无法事先与对方建立连接。基础安全消息、协同感知消息、信号灯相位与配时、路侧预警，走的都是这种「先发后验」的路径。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDvVTlygAOcAGPxn02IJ54GLJKWrKHBfB9jrzUA7tOWPjHePyNkPdj2A5ektNrjrV5qkZXnltlROScrtBrV8NIUH8HvYkDLycQ/640?wx_fmt=png&from=appmsg)

第一问和第二问靠密码学解决，第三问靠一整套证书治理解决。很多项目把精力放在「签名验签跑通」，真正的工程量却在第三问：让一辆车在保护隐私的同时，仍然可以被追责。

**二、消息级安全：签名不加密，权限写进证书**

V2X 安全消息通常只签不密——内容是给周围所有交通参与者看的，机密性不是首要目标，来源可信与完整性才是。IEEE 1609.2 定义了安全消息格式与证书用法，欧洲 ETSI C-ITS 在此基础上扩展出 CAM、DENM 一类消息；国内 C-V2X 走 PC5 直连，消息签名普遍使用国密 SM2 / SM3，并遵循 YD/T 3957—2021、GB/T 45112—2024 一类安全证书管理系统技术要求。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaC8kkrGVZ6fdvSN5qtG9nR3wxjibaYFUJGIgX99XIib3thOTA3zUTFzeic6FcUMRvjv59tHibK5swLeFmwKMCVLRP3NGwCxUhBZ0hQ/640?wx_fmt=jpeg&from=appmsg)

图 2｜C-V2X PC5 直连通信示意

证书里不只有公钥，还写着权限。PSID / ITS-AID 一类标识限定了「这个证书能签哪类应用消息」，有效期通常很短。接收方验证时，要同时完成证书链回溯、签发者匹配、有效期检查、权限核对与撤销状态检查——任何一步通过但其余步骤被跳过，都会留下「假通过」的口子。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBEibfe1WU28tJu7ETFrdQibAicZpDYTQXxSiaHl8HRf7KXbbiaOS99KyCWzOWG48vxRjF7cxYUdyNdDe2VUGna35HGcKKEdkMl1cFE/640?wx_fmt=png&from=appmsg)

**三、三套信任域，长得不一样但逻辑相同**

全球并没有一张统一的 V2X 证书体系，而是几个并行的信任域。它们角色名称不同，拆开看都是「根 → 注册 → 授权 → 端实体 → 撤销」这条链。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBdibdvtAtVPjCNomaRSD6rArH68qfxpJaOsdTxs0rCrLdSYuH5obwdLaKQfwLkTxNSMib7MJK9vm9N5Z9jGria02FL2lMAgKicazI/640?wx_fmt=png&from=appmsg)

欧洲那条链最能说明「治理」与「运行」为什么要分开：CPA 决定哪些根 CA 可被信任，TLM 把批准的根 CA 收进签名的欧洲证书信任列表 ECTL，CPOC 负责收集与分发；Root CA 再给 EA、AA 发证，EA 发长期注册凭证，AA 基于 EA 的校验发短期的 Authorization Ticket。接收方之所以能信一张 AT，是因为它背后有一条从 CPA 一路下来的信任链，而不是因为那张证书本身看起来正规。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDiabhV90a9kgrmfjXCb0Tj1VRSFRA3A0IjRqq3LE7LqkY5C38OyibI9mYohCLJVqhTCtKEToapBXPndDfHm3dOpicV0RppAVlbJE/640?wx_fmt=png&from=appmsg)

图 3｜V2X 安全证书管理系统架构

**四、假名证书：可验证，但不可长期追踪**

如果一辆车始终用同一张证书签名，路边几个接收点就能把它的轨迹串起来。解法是发一堆短期假名证书，按时间或距离轮换，让外部观察者难以把两次签名关联到同一辆车。

难点在于「一次要发很多张，又不能让发证方知道它们属于谁」。SCMS 用蝴蝶密钥扩张：端实体生成一对「毛虫密钥」，注册机构用扩展函数派生出多个「茧公钥」，授权 CA 再生成「蝴蝶公钥」并签发一批假名证书；只有持有原始私钥的端实体能导出对应私钥。同时，两个独立的链接机构各生成部分链接值，组合后嵌进证书——平时谁也看不出这些证书属于同一辆车，一旦需要撤销，误行为管理机构发布链接种子，所有终端就能自行算出该设备当前及未来的全部链接值并拒收，且不会反向暴露撤销之前的轨迹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAv3d4cgS4A4M5BFJjqA2Ew5cR2tZ2qQiaTOmDHWQ4S0IdIPYVLWR5R55F9ia0cv31Aq35icU4OUiaKygSsI2eCiaILY26OJRJ07H7s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaB994BiaicSNFYN5jZknfPvI1TCIJicrMPEeD4iceKSWu8at72TL6QwkbOCZFdXUV9kn7XSqlYzWTZAphYNMPxMuuBK52ibWUtUBEQs/640?wx_fmt=jpeg&from=appmsg)

图 4｜PKI 信任链层级示意

**五、撤销：整个体系最难的一段**

发证书是批量操作，撤销却是广播信道里的实时难题。IEEE 1609.2 工作组把撤销归纳成三条路：一是什么都不做，只停止给该设备发新证，等现有证书自然到期；二是把证书标识写进 CRL 并分发给所有可能收到它消息的终端；三是用假名证书激活码 ACPC 在发送侧控制证书可用性。

第一条最省事，但设备可能继续作恶一年以上；第二条最及时，代价是 CRL 会随长期运营与批量泄露持续膨胀，终端每次验签都要查表，存储和分发都成负担；第三条把负担从接收侧挪到发送侧，只依赖广播、不需要交互连接，但需要 1609.2.1 一类机制配套。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCnLSyg63WJy6oGDaTb1tGbj1AuHXUh55GicM1yjdMsmGBNqcujWrDmCiavsFtAAiaQ8ficsaIMBiaqxicueU2qn8gFpxXjTTWFial2gY/640?wx_fmt=png&from=appmsg)

误行为管理是另一半。单车本地检测出「消息里的位置与速度对不上」「同一时刻自相矛盾」，会生成报告；MA 汇总多个报告、关联到同一设备，确认持续异常后才触发撤销。这里故意设了门槛：传感器故障与蓄意作恶在单条消息上很难区分，因此系统设计成「持续异常」才撤销，而不是一条报告就拉黑。CRL 通常还要区分全量与增量，路侧单元离线时得有明确的降级策略，不能默认「查不到就放行」。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBgmvyUFCwl5GkL0iaCM7aegsibvXxrucSLyL5BIjbxtlfm41IGvoZWLtd6VZLAR0YR4NV96yFammJgibiaMIiaodHGJOL7TmX9TZ6A/640?wx_fmt=png&from=appmsg)

图 5｜硬件安全模块 HSM

**六、跨域互认：根证书列表才是那张通行证**

一辆车跨省、跨国产线、跨运营商部署时，真正决定它能不能被验证的，不是自己那张证书，而是接收方信任列表里有没有签发它的根。国内由工信部车联网安全信任根管理平台与中国信通院建立的可信根证书列表 TRCL，实现多厂商 CA 平台跨域互认；欧洲靠 TLM 签发、CPOC 分发的 ECTL；美国靠 SCMS 生态里的链验证与信任锚。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAm2GwOsuQrGlfZraQHR9s98qL1pzbxa3Ah1Seyngh3uibWMNwdtkXj4SOWFpcVib7OGxKyXEmxonIj76qyY570gAfze9tl1zXrU/640?wx_fmt=png&from=appmsg)

图 6｜车路协同路口

这带来一类很实际的集成故障：证书本身完全合法，但接收方的信任列表没更新、或者两边的证书策略不一致——有效期上限、算法、撤销流程、权限字段定义对不上，整车厂与供应商就会在现场看到「验不过但说不清为什么」。因此证书策略（CP/CPS）、有效期、密钥保护、撤销程序，应该写进供应商合同并定期审计，而不是等路侧联调时再对齐。

**七、几处容易被误读的地方**

各信任域是并行推进的体系，标准规定了机制，部署范围却取决于各地的落地节奏，把标准文本等同于全行业强制采用并不成立。行业层面也缺少可核验的统一覆盖率、装车量与证书签发量，任何百分比都找不到共同分母。现行消息签名仍基于椭圆曲线或国密 SM2；后量子签名在广播信道上的体积与拥塞开销仍是开放问题，尚无成熟的量产后量子 V2X 规范。误行为检测在论文与原型里已有不少结果，但那些是实验网络或台架环境下的结论，不能直接搬成量产车队的实测表现。

**八、工程侧验收清单**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDlX1UUaPD2v0JbAep4qvrHHeFDicU6hZX5vDsicib8sLibP9lDcEw2YgKaM24micficjXCeoyT7Y86De7kjoTqiciaV8niah3jDKmtiaUzw/640?wx_fmt=png&from=appmsg)

V2X 最危险的漏洞从来不是「验签失败导致系统崩溃」，而是「本该拒绝的消息被静默接受」。证书、假名、撤销、互认这四层，本质上都是在给同一个问题补证据：当一条广播消息说「前方有危险」时，接收方凭什么相信它，又在什么时候必须不再相信它。

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

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247502093&idx=1&sn=ec4b373a33ca04d79afbb0b0b880bd4e&chksm=e9278dd6de5004c01bdd83ad0dd89c...