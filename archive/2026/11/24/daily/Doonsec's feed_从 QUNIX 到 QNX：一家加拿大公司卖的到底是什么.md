---
title: 从 QUNIX 到 QNX：一家加拿大公司卖的到底是什么
url: https://mp.weixin.qq.com/s/91bzNcTHLISmf3256i_o0w
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:41:45.075813
---

# 从 QUNIX 到 QNX：一家加拿大公司卖的到底是什么

# 从 QUNIX 到 QNX：一家加拿大公司卖的到底是什么

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB995ym51yuiaz6UL4C02FAq637ia0w2GiaMZ1NeOTbZsFia0oXMWjkiatyNdibc3tWmRVo9GcFVPnLmf3HcbwDyar3YhWkLDt0DZ4SY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

1980 年，两个滑铁卢大学的学生把一门实时操作系统课程作业做成了一家公司。四十多年后，这套系统跑在大量量产车的仪表、座舱与辅助驾驶域里，主打的卖点一直是「一个组件坏了，车不会跟着坏」。2021 年 8 月，一个 C 运行时库里的整数溢出把它推到了美国网络安全主管部门的公告里。这篇文章讲 QNX：它真正卖的是什么，那次技术危机暴露了什么，以及为什么功能安全认证与网络安全免疫从来不是一回事。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCtGNorNQZIXxRqSNGeZfhtlnbPJsyVRYR4ibE7YUUjO1qfR70JRs7DoQOBs00je5jqaQiaM9XwNqVsEdFtptPNVsErsyO8AvR84/640?wx_fmt=jpeg&from=appmsg)

图 1｜QNX 品牌标识

**一、从 QUNIX 到 QNX**

1980 年，Gordon Bell 与 Dan Dodge 在加拿大创立 Quantum Software Systems，把课程里那个实时微内核雏形做成了 QUNIX（Quick UNIX），1982 年发布在 Intel 8088 上，1984 年为避开商标问题改名 QNX。此后公司转向 POSIX 兼容，重写内核，2001 年前后形成 QNX Neutrino，并成为 Eclipse 联盟的早期成员。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBNibHbeafgfD1FSB7wWZYNWxl94BfwvtvkJzwhOT7jAlh8GMGRicEceURo3NLCUlVbOOPstP44ADd69eDt8FicrqF07M2c7w9iaibU/640?wx_fmt=png&from=appmsg)

两次转手很能说明它的位置。哈曼看中的是车载信息娱乐与远程信息处理；RIM 收购后曾把它用于 PlayBook 与 BlackBerry 10，手机业务退潮后，QNX 又回到车载与安全关键嵌入式系统。它始终不是面向消费者的品牌，而是藏在座舱与仪表背后的基础软件。

**二、卖的不是功能，是「隔离」**

QNX Neutrino 的微内核只保留调度、进程间通信、同步与中断这几件最基础的事；文件系统、网络协议栈、设备驱动、图形界面都作为用户态进程运行，通过消息传递交互。这样一来，一个驱动崩溃可以被单独重启，不会把整个内核拖下水；自适应分区再给安全关键组件留出确定的 CPU 预算，避免被娱乐域的任务饿死。

这套结构天然适合「混合关键性」：仪表上的告警灯属于安全关键功能，中控屏上的导航与媒体不是，两者可以跑在同一颗芯片上却彼此隔离。QNX OS for Safety 由 TÜV Rheinland 评估，可作为符合 ISO 26262 ASIL D 的合规项用于数字仪表与 ADAS；QNX Hypervisor 2.0 之后，还能让 Linux 与 QNX 在同一 SoC 上各管一摊。对整车厂与 Tier 1 来说，买的是「一个域出问题不扩散」的架构保证，而不是某个具体功能。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAxkbRsBK9uLfjN5QtQSIVN6LHyVoQFakoAM9PuQ4sMDY5xv4dGLhtJClwh79fUHLibJIgWTA63qMcRXounKPiaDYQlfso9KZ0l4/640?wx_fmt=png&from=appmsg)

图 2｜QNX 数字座舱界面

**三、2021 年那次技术危机**

2021 年 8 月 17 日，黑莓公开披露 QNX 受 BadAlloc 系列漏洞影响，编号 CVE-2021-22156：C 运行时库 `calloc()` 存在整数溢出，攻击者若能控制分配参数并影响分配后的内存访问，可能造成拒绝服务或任意代码执行；当受影响设备暴露在网络可达面时，可被远程利用。所有依赖该 C 运行时库的 QNX 程序都在影响范围内，涉及 QNX SDP 6.5.0SP1 及更早版本、QNX OS for Safety 1.0.1 及更早、QNX OS for Medical 1.1 及更早，以及 QNX CAR Development Platform 2.0RR 等多条产品线。

美国网络安全主管部门随后发布安全公告与 ICS 公告，建议尽快修补；公告同时说明，当时尚未发现该漏洞被公开利用。修补路径也不像手机 App 那样点一下就完成：整车厂与 Tier 1 需要向黑莓获取补丁或补丁代码，部分自研 RTOS 分支要自行开发与测试补丁；RTOS 的软件更新常常需要设备停机，甚至到现场物理更换集成存储器。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBlZknXFtTt9xbicG8JG8rhv25qaKmvy32yuFv27xXicGFzRRP9lG3VDsMJrk2KzH2SYiazpXZibeia3yjgzXo11Fe0IJkQswLDVAFA/640?wx_fmt=png&from=appmsg)

换句话说，隔离设计挡的是「一个组件坏掉拖垮全车」，挡不住「一个合法进程里的 C 库被恶意输入打穿」。这是两套完全不同的失效模型。

**四、功能安全认证不等于网络安全免疫**

把这两张表放在一起，行业里最常见的一个误读就清楚了：ASIL D 证明的是系统在随机硬件失效与系统性失效下达到功能安全目标，它的输入假设里没有「有人故意构造越界参数」；网络安全面对的恰恰是蓄意输入、可被远程触达的接口与长期存在的软件物料清单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCtXI7ZZ6K6AOs686ZIvqC5MQTFqGJ7IoDLD1TL9QkYsqT1MSvZP4EpW5CtkvmSDXdwsUljrXu9ia9xGLtpu6GVXDx1SW1xrZ6Q/640?wx_fmt=png&from=appmsg)

一次 libc 补丁之所以麻烦，正因为它同时踩中两条线：改了 C 库，就要重新走功能安全相关的验证与工具链确认；不改，又留下一个可被远程触达的内存破坏入口。安全认证给了「这套配置是可信的」结论，但没有给「这套依赖永远不会被打穿」的承诺。

**五、把数据变成可管控的资产**

2020 年 12 月，黑莓与 AWS 公布联合开发车载数据平台 BlackBerry IVY：平台运行在车端嵌入式系统里，由云端远程管理与配置，把不同供应商、不同车型各自为政的传感器数据做归一化，在车端边缘与云端分别生成可用信息。它强调支持多操作系统与多云部署，由整车厂拥有数据并控制「谁能访问、访问到什么粒度」。

这个产品线的意义不在功能列表，而在它把问题从「系统稳不稳」推进到「数据谁能碰」：车端先做本地处理与权限判定，只把必要的输出交给上层应用，访问行为可被审计。对数据安全负责人来说，这正好补上了微内核架构不覆盖的那一层——隔离解决的是进程之间不互相干扰，权限与审计解决的是数据不被越权读取。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCicRcicYKCfxKziaxIa2u3dcY3VO4OzbQdDCSrZe4cyWVHPGzoVbr8GYtXTrMBSyIv7CvyLzbJDTJdIrHQ3KJBrYsQJgDE36tsJs/640?wx_fmt=png&from=appmsg)

图 6｜QNX 数字仪表盘界面

**六、把边界放平**

两条界线都要留住。微内核隔离、安全认证与边缘数据平台是真实能力，但不等于整车安全，任何认证都不覆盖网络安全全貌，企业自述的市场地位也不宜当作客观结论。另一方面，那次漏洞是 C 运行时库的实现缺陷，不是「QNX 被攻破」、不是车辆被远程控制，公告当时也没有公开的在野利用报告；整车是否受影响，取决于具体版本、是否暴露在可达接口、以及补丁有没有被集成进量产分支。

QNX 是基础软件层。诊断口是否收敛、网关是否做写入鉴权、OTA 是否验签、SecOC 有没有启用、密钥是否落在 HSM 里——这些集成侧决定，才把「一个可靠的 RTOS」变成「一台可举证的车」。

**七、留给工程侧的五条**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBktvyhZXOfvoY8FEwmrjxtF0TTvrIUX1cCUCynDU8UkXkcEqxDZ54TCplvaVPGaicgYGtZrWskEGHibkIx6Eibsagd4jJMGPI7f4/640?wx_fmt=png&from=appmsg)

一个 1980 年的微内核，靠「把东西拆开、互不影响」活了四十多年；2021 年那次公告提醒的是，拆得再干净，也得有人盯住每一行仍在同一个进程里运行的 C 代码。基础软件给的是地基，不是整栋楼的安全证明。

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

[汽车数据安全合规重点分析](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519068&idx=1&sn=78c66e13bd8798afd46c766b8f18abe7&chksm=e927cf87de504691c816f78b55daf93bdfb72fc1cb870d926de8b471eb3e1be61058498327b1&scene=21#wechat_redirect)

[浅析汽车芯片信息安全之安全启动](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247512151&idx=1&sn=7fabbeeec206ce615a5a3c574bed4c43&chksm=e927f48cde507d9ab6bfd4b8389b5eafea37586707682bfe60f294feb54e1c36cb07bad4d26d&scene=21#wechat_redirect)

[域集中式架构的汽车车载通信安全方案探究](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519952&idx=2&sn=709860de942501f20e923d15330ced9a&chksm=e927ca0bde50431df0b47ad1a2da63bf98ee637c9c00482145fbdb8755851b61421357aab4bf&scene=21#wechat_redirect)

[系统安全架构之车辆网络安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247520446&idx=1&sn=27e10e455264cecb2a1b49d91484d036&chksm=e927d465de505d73c59a6fb4cb066c7c7d07a96ef49a841ffe598c23d28be545c5874dec7de4&scene=21#wechat_redirect)

[车联网中的隐私保...