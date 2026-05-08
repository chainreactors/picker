---
title: Axon泰瑟枪与执法记录仪的蓝牙安全性问题
url: https://mp.weixin.qq.com/s/K-cSpM1A5zEO48CHEfxDPA
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:49:47.900861
---

# Axon泰瑟枪与执法记录仪的蓝牙安全性问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDopBTbIWC3RAhO9KtPgcMqENshia1Ofyial6vgCseyxaZqQJZ4Xzez1JG6ia6JjGATmiatseBtTBACmYyztJRmxRyCibJHJU5cb9sMU/0?wx_fmt=jpeg)

# Axon泰瑟枪与执法记录仪的蓝牙安全性问题

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

当一个穿着深色连帽衫的人走向澳大利亚某个警察局时，他的手机开始不断震动。

“一，二，三……” 他数着屏幕上弹出的通知。每一条通知都代表一名被检测到的警察，屏幕上清晰显示着他们的精确坐标。

“…… 七，八，九，十。”

这不是什么高科技间谍活动。这是任何一个拥有普通智能手机或笔记本电脑的人都能做到的事情。全球执法巨头 Axon 生产的蓝牙泰瑟枪和随身执法记录仪，正在让全球数千名警察变成行走的位置信标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr0CW5I4lu5YM6lHC5CUPGYC8jH0n6Byw0Ft87HU597B9bXdibHC9sssfkrUeOJbRhXvbhd49NBUqFOh5pEBGpCZY0renOvhHgA/640?wx_fmt=png&from=appmsg)

##

这个漏洞的发现者是一位不愿透露姓名的独立安全研究员。

他最初只是在自己的手机上记录周围的蓝牙设备，却意外发现了大量标注为执法记录仪和泰瑟枪的设备信号。

“我只是在记录手机上的蓝牙设备日志，然后就看到执法记录仪和泰瑟枪不断出现，当时我就觉得这有点不对劲。” 他说。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpN5ictUZqma256vciag5nrPqw8JDMxrkFnNLphsWvictSq31js4mEvjp4VP0jYhBnwQMcO3rasen02cj93SErlZEOYb9h9g5nSoE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpRyNGKVUiaibGIZVFiazyvbKlRlzqUibRiaOsjwSPvicYnhibEvr9ExfVnZAkZlylCkHB1QxnIeicgjv1SWY2hT0bUGBOVFAOBzGZDbhs/640?wx_fmt=png&from=appmsg)

他随后开发了自己的POC软件，证实任何人都可以通过 Axon 蓝牙设备分配的固定公开MAC地址定位并追踪佩戴这些设备的警察。

“你可以在相当远的距离外追踪这些警用设备。软件会发出一个小警报，提示‘检测到警察’。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqVw4j4kXv5ia6AV0CWibTtJ73nTDkIIGjH4UcfnKr2nEyJEEDCEzUwasYuuld1YDIHwTHHbFxmicFsKlaibib9H5jkDaNu5KHjgnfY/640?wx_fmt=png&from=appmsg)

更令人担忧的是，这种能力已经完全公开化。

在安卓应用商店中，已经有多个公开可用的应用可以实现相同的功能。

当这些应用检测到附近的 Axon 设备时，会立即向用户推送通知，并显示设备的纬度、经度、型号和序列号。

在墨尔本的实地测试中，研究人员使用其中一款公开应用，不仅能检测到乘坐警车返回警察局的警员，还能持续追踪那些换乘无标记车辆离开的警员，直到他们完全离开视觉范围。研究人员自己开发的软件，有效探测距离更是达到了 400 米。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqo0siaTWmonmU3rianRt77ZrXH30HmCHMNWhwXV73rrwQTe8VBRvczbwxFmAGW1TxLPVpic1aw7qCaBV3EyWGbNqMto0MNXkZGyk/640?wx_fmt=png&from=appmsg)

每一个使用蓝牙技术的设备都拥有一个全球唯一的硬件标识符MAC地址。

在早期的蓝牙技术中，这个地址是固定不变的，任何人都可以通过扫描周围的蓝牙信号获取设备的MAC地址，并以此持续追踪该设备的位置。

为了解决这个严重的隐私问题，现代智能手机操作系统都内置了 MAC 地址随机化功能。以苹果 iPhone 为例，手机会定期随机生成一个临时的 MAC 地址用于蓝牙通信，使得第三方无法通过固定标识符追踪设备的位置。

然而，作为全球最大的警用装备供应商，Axon 却没有在其产品中实现这一标准的隐私保护功能。该公司生产的所有蓝牙版泰瑟枪和执法记录仪，都使用固定不变的 MAC address 进行广播。

这意味着，只要有人记录下某个 Axon 设备的 MAC 地址，就可以在任何时间、任何地点持续追踪该设备的位置，进而追踪佩戴该设备的警察。

研究人员指出，犯罪分子可以使用数十个廉价的小型蓝牙扫描单元，在一个郊区或城镇的关键位置进行部署。这些单元可以组成一个实时监控网络，在地图上持续追踪所有佩戴 Axon 设备的警察。

“它可以被用来伏击警察、袭击警察、逃避警察追捕。有组织犯罪团伙完全可以利用这个系统。本质上，这个漏洞已经可以被武器化。”

对于便衣警察、战术单位成员以及那些需要将设备带回家的警员来说，这个风险尤为致命。犯罪分子不仅可以提前发现警方的突袭行动，还可以追踪警员的个人行踪，对警员及其家人的人身安全构成直接威胁。

这个漏洞已经不是什么行业秘密。其他黑客已经在网上分享了详细的利用教程。美国边境巡逻队在去年就已经被告知停止在野外使用 Axon 执法记录仪，并启动了相关调查。

早在 2024 年，这位安全研究员就已经向澳大利亚所有州和地区的警察机构、警察部长、联邦警察以及国家安全机构发送了警告邮件。

在给维多利亚警方的邮件中，他明确写道：“我正在向警方提出一个潜在的严重网络安全问题。我开发的软件仅使用笔记本电脑或手机，就能在 400 米外检测到警察的存在。你们的新型 Axon 泰瑟枪让整个警队实际上都佩戴着广播自己位置的信标。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpPddMvj38I9USaJxXH88D9unn9YgogCWgrrsKqoa70P3ciaPnKR8paFscU75XCrKrFbn92wFWw6h5WlP4EwAffYkKtqO3JO8ZM/640?wx_fmt=png&from=appmsg)

他警告警方，通过合适的硬件，有组织犯罪分子可以建立一个简单的系统，实时追踪警察的位置，甚至可以在数公里外发现警方的突袭行动。

Axon 公司确实在其网站的产品设置中，通过一个免责声明承认了这个漏洞，或者用他们的话说是 “安全考虑”。在其信任与安全页面的小字部分，

Axon 警告其警察客户，“Axon 相机的蓝牙和 Wi-Fi 无线电信号通常可以被检测到”。

声明还指出，“在部署 Axon 相机进行可能因检测导致意外结果的行动之前，应考虑操作安全因素”。

Axon 同时承认，其所谓的 Stealth Mode（隐身模式）并不能禁用设备的无线电信号发射。

当被问及为什么公司不直接修复这个问题时，安全研究员给出了一个令人不安的答案。这是一个硬件级别的漏洞。

“这些设备的设计方式决定了它们无法通过补丁或软件更新来修复这个问题。整个系统必须从头开始重新设计。因此，如果他们被迫召回这些设备，他们将陷入非常糟糕的境地。”

Axon 在 2023 年表示正在开发 “改进措施以解决追踪问题”，但是并没有解决。

附录:

Axon 泰瑟枪是全球应用最广泛的传导能量武器（Conducted Energy Weapon, CEW），由美国 Axon Enterprise 公司（原 Taser International）研发生产。它通过发射带电探针干扰人体神经系统实现非致命制服，现已成为全球 18000 多个执法机构的标准装备，同时也引发了关于安全性、隐私权和行业垄断的持续争议。

目前公司市值约 320 亿美元，在全球传导能量武器市场拥有绝对垄断地位，业务覆盖泰瑟枪、执法记录仪、无人机、AI 分析工具和云存储服务等多个领域。

泰瑟枪与普通电击器的本质区别在于其工作机制。普通电击器仅通过接触放电产生疼痛，而泰瑟枪通过以下步骤实现神经肌肉失能（Neuromuscular Incapacitation, NMI）：

1. **探针发射**

   扣动扳机后，压缩氮气将两个带倒钩的金属探针以约 60 米 / 秒的速度射出，探针通过细绝缘铜线与主机连接
2. **电路形成**

   探针穿透衣物或皮肤后，在目标体内形成闭合电路
3. **神经干扰**

   主机释放高压（最高 50000 伏）但低电流（平均约 2 毫安）的脉冲信号，直接干扰外周神经系统的电信号传导
4. **肌肉失控**

   脉冲信号强制肌肉产生不受控制的收缩，使目标瞬间失去行动能力，持续时间通常为 5 秒

这种机制使泰瑟枪能够在不造成严重永久性伤害的情况下快速制服暴力人员，被认为是介于徒手控制和致命武器之间的重要中间力量选项。

部分型号还具备 Drive Stun（驱动电击）模式，即在不发射探针的情况下，直接将设备接触目标皮肤放电。该模式主要用于疼痛顺从，而非完全失能，也是争议最大的功能之一。

### 现役主力型号

* **TASER 7（2018 年）**

  目前全球部署最广泛的型号，也是澳大利亚大多数州警方的标准装备

  双发射击能力，支持快速重新装填

  采用 Rapid Arc 技术，提升了探针接触不良时的有效性

  首次集成蓝牙功能，可与 Axon 执法记录仪联动，实现拔枪自动录像

  最大射程 7.6 米，使用可充电数字电源弹匣（DPM）
* **TASER 10（2023 年）**

  Axon 最新一代旗舰产品，被称为非致命技术的重大飞跃

  单弹匣可发射 10 个独立瞄准的探针，理论制服成功率达 98%

  最大射程提升至 13.5 米，几乎是 T7 的两倍

  具备 IP67 级防水防尘能力，适应各种恶劣环境

  采用更低电压设计，进一步降低健康风险

Axon 泰瑟枪已被全球超过 18000 个执法机构采用，包括美国 90% 以上的地方警察局和澳大利亚所有州及地区的警察部队。澳大利亚政府与 Axon 签订了价值数亿澳元的长期合同，涵盖泰瑟枪、执法记录仪和云存储服务。

Axon 的核心商业模式已经从单纯的硬件销售转变为 硬件 + 订阅 + 服务 的综合模式：

硬件销售：泰瑟枪和执法记录仪等设备

订阅服务：Evidence云存储平台，用于存储和管理执法视频证据

增值服务：AI 视频分析、案件管理系统、培训服务等

这种模式形成了极强的客户锁定效应。一旦执法机构接入 Axon 的生态系统，更换供应商的成本极高，这也是 Axon 能够维持垄断地位的关键原因之一。

请禁止你大胆的想法。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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