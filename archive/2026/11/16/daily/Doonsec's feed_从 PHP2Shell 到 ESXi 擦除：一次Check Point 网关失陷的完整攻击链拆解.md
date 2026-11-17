---
title: 从 PHP2Shell 到 ESXi 擦除：一次Check Point 网关失陷的完整攻击链拆解
url: https://mp.weixin.qq.com/s/J7f_HxW_rSbM10kwt73QgA
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:55:32.015944
---

# 从 PHP2Shell 到 ESXi 擦除：一次Check Point 网关失陷的完整攻击链拆解

# 从 PHP2Shell 到 ESXi 擦除：一次Check Point 网关失陷的完整攻击链拆解

原创

极客零零七
极客零零七

极客零零七

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

10 月底开始，针对 **Check Point Security Gateway** 的真实攻击给很多企业提了个醒：边界设备一旦被打穿，后果远不只是“防火墙被控”这么简单。

根据 Check Point 的披露，攻击者先利用 **PHP2Shell** 漏洞链拿下暴露在外的 **Mobile Access** 门户，再结合此前未公开的 **Gaia OS 本地提权漏洞 CVE-2026-123039** 获取 root，随后在网关上植入 **TSGA 后门** 与网络组件 **TSProxy**，最后通过 SSH 横向进入 **VMware ESXi**，投递名为 **destroy\_v6** 的擦除工具，覆盖并删除文件，还留下了 `DREAM_ANNEXATION.txt` 文本文件。首波攻击从 2026 年 10 月 30 日开始，主要针对以色列组织；11 月 2 日后又出现了面向多国目标的第二波活动，不过后者暂未观察到同样的破坏行为。

这起事件最值得看的是它完整展示了一条现实中的高价值攻击路径，在这条攻击链里，真正危险的不是单点漏洞，而是“边界设备的地位”。

**互联网暴露的边界入口 → 设备本地提权 → 持久化与日志干扰 → 内网侦察 → 直达虚拟化平台 → 破坏性载荷投递**。

![](https://mmbiz.qpic.cn/mmbiz_png/L7VicJKsiaibFABeGCD8Dic5Pdx58FWT3jtbTdZNkP9Qk2a25wGRI3xgziawXVODGIOOOkicWxwjib2Dr6qTfvZGNB0JAKdJE96L6y1iaaMdqK5gxXY/640?wx_fmt=png&from=appmsg)

很多团队仍把安全网关视为“防守方设备”，默认它比普通 Linux 主机更安全。但从攻击者视角看，网关恰恰是理想的跳板之一：

* 它天然位于 **内外网交界处**
* 它通常拥有 **高权限网络可达性**
* 它经常保存 **管理凭据、证书、配置与日志**
* 企业对它的 **EDR、主机检测和文件完整性监控** 往往最弱

所以这次事件的关键在于：**边界设备一旦失陷，攻击者拿到的不是一台普通主机，而是一个天然具备横向条件的战略支点。**

## 初始访问：PHP2Shell 如何把 Mobile Access 门户变成入口

已确认被利用的两个漏洞编号为： **CVE-2026-109618**、**CVE-2026-109619。**

Check Point 的公告将其归为 **PHP2Shell** 相关问题，影响 **Mobile Access** 门户，能够导致 **未授权远程代码执行（RCE）**。公开资料已经确认，这组问题可用于初始入侵，但当前披露并没有给出足够细化的利用细节。从防守角度理解其风险并不难：  当安全网关把基于 PHP 的门户直接暴露到互联网，而底层解析链路又存在可执行能力时，攻击者就能在**无需有效账户**的情况下，把 Web 请求转成设备上的代码执行。这一步完成后，攻击者拿到的通常还不是 root，而是受限上下文中的执行能力。

但对边界设备来说，这已经足够危险。后续只要存在本地提权点，就很容易从“Web 入口”升级为“系统级控制”。

## 本地提权：Gaia OS 的 IPC 缺陷补上了最后一块拼图

接在 RCE 之后被利用的是 **CVE-2026-123039**。  Check Point 表示，这是一个影响 **Gaia OS DynamicCLI IPC 接口** 的本地提权漏洞，CVSS 评分 **7.8**，可被攻击者用于将权限提升至 **root**。

这一步很关键。很多真实入侵并不会止步于 WebShell，而是一定会继续寻找从应用层进入系统控制面的通路。对安全设备来说，**管理接口、守护进程、IPC 通信、配置同步机制** 往往比普通业务服务器更复杂，也更容易成为提权桥梁。当前披露已经明确指出，攻击者确实利用该 IPC 缺陷完成提权，但尚未公开完整利用原理。

但从整条攻击链的意义看，这一步完成后，攻击面已经发生了质变：

* 可以读写更多系统路径
* 可以植入更稳固的持久化组件
* 可以访问和窃取网关配置
* 可以篡改、删除或污染日志
* 可以把网关当作内网代理或跳板继续推进

换句话说，**RCE 解决的是“进来”，LPE 解决的是“站稳并接管”。**

## TSGA 后门：这不是一次“打一枪就走”的利用

Check Point Research 将落地组件描述为一个名为 **`slot_CPconfigdaemon`** 的后门，以及配套网络组件 **TSProxy**。已公开功能包括：加密远程访问、配置窃取、日志篡改或清理能力、更隐蔽的持久通信。这些特征说明，攻击者的目标不是单纯验证漏洞，而是希望长期保有这台网关的控制权。这里有两个尤其值得企业注意的信号。

### 1. 命名伪装明显贴近系统组件

`slot_CPconfigdaemon` 这种命名方式，本身就带有很强的伪装意图。它试图在运维或排障人员眼里，看起来像某个正常的配置守护进程。边界设备上本来就有大量厂商自带服务，攻击者只要命名足够“像”，就能显著提高驻留时间。

### 2. 后门的价值不只在远控，更在于“掩盖后续动作”

如果一个入侵样本同时具备 **配置读取** 和 **日志篡改** 能力，那么它带来的风险就不只是留一个 shell。对调查方来说，最麻烦的不是确认攻击发生过，而是很难准确还原：

* 攻击者什么时候进来的
* 使用了哪些管理凭据
* 从网关 pivot 到了哪些内网资产
* 哪些日志已经被删除或修改

这也是为什么不少厂商在应对此类边界设备失陷时，最终给出的建议不是“删掉恶意文件即可”，而是 **重建设备并轮换相关凭据与证书**。

## 横向移动：为什么最终受害的是 ESXi

根据 Check Point Research，攻击者在网关内部使用了名为 **gogo** 的工具扫描内部网络，随后通过 **SSH** 横向到 **VMware ESXi** 主机，并使用 **`vpxuser`** 账户进行访问。

首先，攻击者显然没有满足于控制网关本身，而是把它当作靠近核心基础设施的侦察点。其次，ESXi 之所以成为高价值目标，是因为它位于大量业务虚拟机之下。攻击一台普通业务服务器，影响的是一个系统；攻击一台虚拟化宿主机，影响的可能是一整组生产服务。

关于 `vpxuser` 的使用，公开资料确认了该账户被用于 SSH 渗透 ESXi，但**并未完整披露攻击者是如何获得相关访问条件的**。这可能涉及现有凭据、配置暴露，或其他中间环节。可以确定的是，边界网关失陷后，攻击者确实把访问范围推进到了虚拟化层。这一步给企业的提醒很直接：
**不要假设边界设备只能“看到”内网，它往往还能“进入”内网。**

## 破坏阶段：destroy\_v6 对 ESXi 文件执行零写入后删除

在破坏阶段，攻击者部署了 **destroy\_v6**。根据公开描述，该工具会对文件进行**零写入覆盖**，随后删除，并留下带有政治信息的 `DREAM_ANNEXATION.txt` 文件。

![](https://mmbiz.qpic.cn/mmbiz_png/L7VicJKsiaibFBAPPH865PQ1JBfBSveZaXjuwPmsQCObrd9JfqdIGZkm1XicQqPmS6LouOBarGJszmkY400xFBNOjz2CLTGBQCFK5bf46WVcpiaQ/640?wx_fmt=png&from=appmsg)

这已经不同于单纯勒索或数据窃取，更接近一种**具备明确破坏意图的数据摧毁行为**。尤其是在 ESXi 场景下，一旦宿主机上的关键文件、虚拟机文件或相关配置被破坏，恢复复杂度会迅速上升：

* 受影响的可能不是单个业务，而是整台宿主机上的多个 VM
* 即使有备份，恢复顺序、依赖关系和停机窗口也更复杂
* 如果攻击在破坏前已经完成日志清理，事后溯源会更加困难

需要区分的是，Check Point 观察到 11月2日后的第二波攻击面向更多国际目标，但**尚未看到同样的破坏性行为**。这意味着，“漏洞被用于入侵”与“漏洞被用于擦除数据”仍然是两个层次，不能把所有扫描和利用都直接等同于最终破坏。

## 防御与处置建议

如果环境中存在 Check Point Security Gateway，尤其启用了 **Mobile Access** 门户，建议优先做四件事。

### 1. 立即核查补丁状态

重点确认是否已部署厂商在 10 月 23 日发布的 **Jumbo Hotfix**，受影响版本包含公开提及的 **R81.20、R82.00、R82.10、R82.20** 等。具体修复范围仍以 Check Point 官方公告为准。

### 2. 把“是否被控”与“是否已修补”分开处理

补丁只能防止继续被打，不能证明系统未被植入。
应重点排查以下线索：

* 是否存在 **`slot_CPconfigdaemon`**
* 是否发现 **TSProxy** 或异常网络转发行为
* 是否出现 **`destroy_v6`**
* 是否留有 **`DREAM_ANNEXATION.txt`**
* 是否存在与 **gogo** 相关的扫描痕迹
* Web 目录或临时目录中是否有异常 PHP 文件，例如报告中提到的可疑痕迹名 **`upload_progress_pwn`**

### 3. 一旦确认失陷，优先重建，而不是“就地清理”

如果 root 已被获取，且后门具备日志篡改能力，那么更稳妥的策略通常是：

* 隔离设备
* 保留取证镜像和配置证据
* 重建网关
* 轮换管理员口令、SSH 密钥、API 密钥、证书及相关凭据
* 审计从网关可达的高价值资产，尤其是 **ESXi、备份系统、身份系统**

### 4. 重新设计边界设备的管理面信任关系

至少应检查：

* 网关是否可直接 SSH 到 ESXi
* ESXi 是否暴露给过宽的管理网段
* 关键虚拟化、备份与身份基础设施是否做了**管理面分段**
* 是否有独立于设备本地日志之外的 **远程集中日志留存**

## 写在最后

这次事件的警示其实很直接：**边界设备不是“防守方的豁免区”，而是攻击者最喜欢的入口之一。**

从 **PHP2Shell** 到 **Gaia OS 本地提权**，再到 **TSGA 持久化、TSProxy 隐蔽通信、ESXi 擦除**，整条链路几乎把现代企业最怕的几个环节串在了一起：入口暴露、补丁滞后、设备高权限、管理面互信、虚拟化平台承压。

如果企业还把防火墙、VPN 网关、安全接入设备当成“只要能跑就别动”的黑盒，那么攻击者迟早会把它们变成进入核心基础设施的踏板。真正有效的策略，不是事后惊讶于“怎么连网关都能被打”，而是默认：**任何暴露在公网的边界设备，都必须被当作高危、可失陷、需要持续监测的关键主机来管理。**

---

> 关注「极客零零七」，每周实战攻防干货。
> 回复「提权」获取 Windows + Linux 提权速查表 · 回复「AD 攻击」获取 AD 域攻击手册

## 参考资料

* https://blog.checkpoint.com/security/security-advisory-active-exploitation-of-php2shell-and-local-privilege-escalation?noamp=mobile&utm\_source=openai[https://blog.checkpoint.com/security/security-advisory-active-exploitation-of-php2shell-and-local-privilege-escalation?noamp=mobile
* https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway
* https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper
* https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过