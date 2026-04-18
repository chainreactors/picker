---
title: Cross-Signed 驱动程序已死？未必如此
url: https://mp.weixin.qq.com/s/FkyPZd1KeLEUIPkspfCVgA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:25:44.071298
---

# Cross-Signed 驱动程序已死？未必如此

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSiaZtEvibRicMgwWFkyeBEcaBHDSibgLHwGWJq14rPwtby6SpW2iciaVianfOffxzpbUSDeS67RQNqZ6UcrTqQySmfiaibluU17wZ5JVHas/0?wx_fmt=jpeg)

# Cross-Signed 驱动程序已死？未必如此

Michael Haag
Michael Haag

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://www.magicsword.io/blog/microsoft-is-killing-cross-signed-drivers | Michael Haag |

微软将于 2026 年 4 月起撤销对 cross-signed kernel drivers 的信任。影响不容小觑：LOLDrivers 目录中有 81.7% 的驱动程序属于 cross-signed 类型。然而，策略并非即时强制执行——系统会先进入 evaluation mode，只要有一个旧版驱动程序未能通过检查，该阶段便会重置，导致许多组织可能始终无法进入真正的 enforcement 阶段。更值得警惕的是，Living Off the Land 攻击 (LOLBins、LOLRMM) 完全不受此策略影响，因此防范 Living off the Land 攻击依然至关重要。

2026 年 3 月 26 日，微软宣布将撤销对所有通过已废弃 cross-signed 根程序签名的 kernel drivers 的信任。自 2026 年 4 月的 Windows 更新起，只有通过 Windows Hardware Compatibility Program (WHCP) 认证、或列入微软白名单的驱动程序，才能在 Windows 11 24H2+ 及 Windows Server 2025 上默认加载。

这是一步有实质意义的举措，毋庸置疑。应当承认：微软正在关上一扇自 2000 年代初便一直洞开的大门。彼时，第三方 certificate authorities 几乎可以在审查极为有限的情况下随意颁发 kernel-mode 签名证书，对所签代码的安全性毫无保障。该程序于 2021 年正式废弃，所有相关证书也已相继过期。

但过期不等于失效。微软无法简单地吊销这些证书——一旦吊销，企业赖以维持硬件兼容性、工业控制系统及业务系统正常运转的数百万个合法旧版驱动程序将随之瘫痪。证书虽已过期，Windows 却仍然信任它们用于内核加载。这正是漏洞所在。

攻击者对此心知肚明。Scattered Spider 组织利用 cross-signed 证书加载了 POORTRY——一个专门用于终止 EDR 进程的自定义 kernel driver，这是一种经典的 BYOVD (Bring Your Own Vulnerable Driver) 攻击手法，曾在 2023 年多起高调赌场入侵事件 中被实际部署。Cuba ransomware 的幕后操纵者则申请了合法的代码签名证书，直接签署自己的 kernel drivers，借此禁用安全工具。BlackByte ransomware 则持续滥用 RTCore64.sys——MSI Afterburner 附带的一个存在漏洞的驱动程序——绕过 HVCI、禁用内核回调。

问题来了：这次举措真的能解决恶意驱动程序问题吗？

我们去探了个究竟。

## LOLDrivers 数据揭示了什么

LOLDrivers 项目由我们团队维护，专门收录攻击者实际滥用的存在漏洞及恶意驱动程序。这是目前同类数据集中最为全面的公开资源：**共 509 条驱动程序记录，涵盖 1,983 个独立驱动程序样本**。这些系统驱动程序均来自真实入侵场景，被真实威胁行为者用于终止 EDR、提升权限，以及在内核层面建立持久立足点——典型的 Living Off the Land 手法。

重点来了。

![LOLDrivers 代码签名分析：所有 LOLDrivers 样本中的 81.7% (1,983 个中的 1,620 个) 由参与 cross-signing 程序的第三方 certificate authorities 签名](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShv4bHOf12J0JjUFY1k8347RITYytqxHcoFRpkibVy3GV5Awj6UToblVURqGicAiaMibfyDvqCrianbG6x3YdTPAx9nT8YuXakb49mA/640?wx_fmt=png&from=appmsg)

LOLDrivers 代码签名分析：所有 LOLDrivers 样本中的 81.7% (1,983 个中的 1,620 个) 由参与 cross-signing 程序的第三方 certificate authorities 签名

**所有 LOLDrivers 样本中的 81.7%——1,983 个中的 1,620 个——均由参与 cross-signing 程序的第三方 certificate authorities 签名。**VeriSign/Symantec 独占 1,045 个样本，GlobalSign 412 个，DigiCert 287 个。仅有 6% 的样本携带纯 WHCP (Microsoft 认证) 签名。

理论上，微软新的内核信任策略应当能在 enforcement mode 生效的系统上，使绝大部分 LOLDrivers 目录失去作用。一旦 enforcement 正式启动，这 1,620 个已知被滥用的驱动程序样本将统统无法加载。

从账面数据来看，这对防御方是一次巨大的胜利。**但账面数据和生产现实，是两回事。**

## 陷阱：评估模式与重置循环

公告中有这样一段话，每一位防御者都应该逐字细读：

> **"若在评估期间，任何 cross-signed 驱动程序经审计后被认定无法通过新的内核信任策略，则该策略不会激活，系统继续保持评估状态，评估期随即重置。系统将一直维持评估模式，直到阻碍策略启用的驱动程序不再被审计为止。"**

再读一遍，慢慢消化。

系统收到 2026 年 4 月更新后，并不会直接进入强制执行状态，而是先进入 **evaluation mode**。内核会在 3 个启动会话（服务器版为 2 个）内，累计监控 100 小时的驱动程序加载情况。若该窗口内加载的所有驱动程序均合规，强制执行正式生效。但若有哪怕一个不合规的 cross-signed 驱动程序被加载——无论是某家外围设备厂商的老旧驱动、某款小众工控驱动，还是一个旧打印机驱动——评估期就会**完全重置**。系统重回 evaluation mode，旧版驱动如常加载，防护永远无法激活。

Microsoft 这样设计自有道理——企业机队不能一夜之间全部变砖，兼容性必须放在首位。但现实的问题是：只要某个组织的环境中存在哪怕一个不合规的旧版驱动，系统就可能无限期地停留在评估模式。唯一的解决方案是部署 Custom Kernel Signers，而这需要拥有 Secure Boot PK/KEK 的完整控制权，并全新安装操作系统。对于大多数拥有数千个端点、硬件环境多样、IT 团队本就捉襟见肘的企业而言，这条路几乎行不通。

对于那些硬件机队复杂、历史遗留依赖众多的大型企业而言？那个"单一旧版驱动"的存在几乎板上钉钉。

## 风险暴露的数据透视

用 LOLDrivers 的数据来量化这一问题：

| 指标 | 数量 |
| --- | --- |
| 驱动程序样本总数 | 1983 |
| Cross-signed（受新策略影响） | 1,620 (81.7%) |
| 即便启用 HVCI 仍能加载 | 421 (21.2%) |
| 持有有效签名的恶意驱动程序 | 302（恶意样本的 93.2%） |
| 可绕过 HVCI 的恶意驱动程序 | 恶意样本的 44.7% |

最后那个数字才是核心所在。威胁行为者挑选驱动程序从来不是随机为之——他们专门筛选能够规避现有防护的驱动。LOLDrivers 目录中，近半数恶意驱动程序样本都能绕过 HVCI。攻击者深知哪些驱动可以成功加载，在什么环境配置下，面对哪些已启用的防护手段——选择从来都是蓄意为之。

更关键的一点在于：**如果因为评估模式中存在单个旧版驱动，强制执行始终无法生效，那么全部 1,620 个 cross-signed 样本将持续可加载。**防护只存在于纸面，而非真实的端点之上。

## 这一措施的盲区：Living Off the Land

即便 enforcement mode 已在系统上激活，Microsoft 的内核信任策略依然有一类攻击无法触及：**Living Off the Land**。

拦截 cross-signed 驱动程序，确实能阻止不受信任的代码进入内核——这一点无疑是有价值的。然而，当今最主流的攻击手法压根不需要加载自定义 kernel driver。攻击者长于就地取材：调用已签名的 Microsoft 原生二进制文件、原生脚本引擎，以及每一份 Windows 系统自带的内置工具。

2026 年 CrowdStrike 全球威胁报告指出，82% 的初始入侵访问实现了无恶意软件化，这进一步凸显了对抗无恶意软件攻击策略的紧迫性。Red Canary 威胁检测报告则年复一年地印证着同一事实：`certutil`、`mshta`、`wscript.exe`、`regsvr32`、`rundll32`始终稳居 LOLBins 滥用排行榜前列。原因很简单——它们是操作系统的原生组成部分，不可能被移除。

Microsoft 的驱动程序信任更新对上述手法毫无制约。enforcement mode 不会判断 `certutil`是否正在下载恶意载荷，也不会检测 `mshta`是否正在从远程服务器执行 HTA——这本就不是它的设计职责。但正是这些技术，在真实攻击场景中被用于投放勒索软件、建立 C2 通道、以及窃取数据。

拦截恶意驱动程序，是防御体系的一层。拦截对合法工具的滥用，是另一层。

防御者两者都需要。

## 这片"土地"远未清净

Microsoft 的这一举措值得肯定。撤销对 cross-signed 驱动程序的信任，切实针对了一个有据可查的攻击面——而这一类别占据了 LOLDrivers 目录的 81.7%。这毫无疑问意义重大。

但强制执行能否生效，取决于 evaluation mode 能否顺利完成。一个旧版驱动程序就能重置计时器。HVCI 并非万能，421 个已知恶意样本在其启用状态下依然可以加载。而 Living Off the Land 整个攻击面，更是毫发未动。

**明天落地您端点上的攻击者，不会等您的 evaluation 期限跑完。**

**cross-signed 驱动程序的问题确实存在，Microsoft 也在积极应对。但攻击面远不止驱动程序，真正的端点攻击面收缩需要的不只是 kernel 信任策略。它涵盖每一个签名二进制文件、每一个脚本引擎、每一个随 Windows 附带或后续安装的远程管理工具。那才是这片仍待"耕耘"的土地。**

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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