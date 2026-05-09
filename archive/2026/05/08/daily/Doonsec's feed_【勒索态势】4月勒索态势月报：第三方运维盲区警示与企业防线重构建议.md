---
title: 【勒索态势】4月勒索态势月报：第三方运维盲区警示与企业防线重构建议
url: https://mp.weixin.qq.com/s/YAiDqB1oRSpU9oWAV_eyeQ
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:07:17.297046
---

# 【勒索态势】4月勒索态势月报：第三方运维盲区警示与企业防线重构建议

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/887OLfia3YQY6oic8anuofx4ZtGeV67iaMBY8zictSic0tic8Iggw7LSIWarSQHZQXzeV8LRx3ibf5YJBibJEYUm6VU8Nibbwo8QzJwjAKfbxEwnZvia4/0?wx_fmt=jpeg)

# 【勒索态势】4月勒索态势月报：第三方运维盲区警示与企业防线重构建议

原创

solarsec
solarsec

solar应急响应团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/DxUXemrrntp3gibjPSCHmSEpdPDqfBcXT5e151v5AJSbV5JtaALLzQe0I1Jibbet7rTia8icjmgo5r4hpY3IMpYPIw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

依托 **Solar 安全运营响应团队**的日常实战沉淀，我们会定期分享在安全运营中处置的典型应急响应事件，涵盖**银狐木马、APT 攻击、勒索病毒**等各类主流威胁。

作为专业的应急响应中心，Solar 致力于为复杂多变的安全事件提供从深度溯源到闭环处置的全流程支持。针对银狐、APT 等具有高隐蔽性的威胁，我们不仅聚焦于对其攻击行为的深度剖析，更致力于还原其完整的活动链路，并同步输出切实可行的**清除闭环操作方案**。

**突发危机干预通道：**若您的核心资产正面临加密锁定或数据勒索风险，请通过文末二维码联系我们。我们提供全天候紧急介入服务，协助您快速切断攻击链路，全力挽回业务损失。

结合全球公开威胁情报与 Solar 应急响应团队的一线实战处置数据，我们对4月份的勒索软件活动轨迹进行了全面的梳理与归因分析。

4月份，勒索攻击在目标选择、利用手段以及家族活跃度上呈现出明显的演进趋势，特别是针对企业核心供应链环节的渗透正在加剧。本文将从宏观数据洞察、国内入侵途径分析以及典型实战案例复盘三个维度，为您还原真实的威胁全貌，并提供体系化的安全整改建议。

## 一、全球与国内勒索攻击宏观态势剖析

### 1.1 全球活跃数据与受害区域分布

根据4月份监测数据，2026年4月份全球勒索攻击事件共确认为 **927 起**，其中涉及中国企业的攻击为 **95 起**。

从地域分布来看，当前可观测的受害目标高度集中。美国占比最高达到 34.62%，依然是公开情报中最主要的受害区域。这一数据特征与美国企业数字化程度高、数据资产价值大、公开披露机制相对完善密切相关，同时勒索组织也更倾向于在暗网数据泄露站点（DLS）优先公开这类企业的信息以施加压力。

**中国受害目标占比 10.44% 位居全球第二**。需要说明的是，这部分国内数据不仅包含了公开威胁情报，还深度结合了 Solar 应急响应团队在实战应急处置过程中掌握的真实案例。由于部分勒索组织并未建立暗网泄露平台或隐瞒了部分受害者，全球公开数据本身存在一定的统计缺口，而结合一线实战数据，能更客观、立体地反映当前国内企业面临的真实防御压力。![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZjoicBWqcmicYMJDXctQ8iaThE3eo47faTuibERMK5dxLT6I84CLlW8WB5krAVuC43fOkhGA9VJvhh7VczWMTbBCNOGUT475tjiaqU/640?wx_fmt=png&from=appmsg)

4月全球勒索攻击受害国家分布饼状图

### 1.2 头部家族活跃度与行业受灾分布

本期全球勒索活动呈现出“头部高度活跃，长尾持续分散”的显著特征。排名前列的勒索组织中，**Qilin 发动了 99 次攻击，以 11.80% 的占比位居首位**。TheGentlemen 以 10.25% 紧随其后，DragonForce（7.75%）与 APT73（7.39%）同样保持着高强度的攻击频率。此外，Akira、CoinbaseCartel、IncRansom 以及 LockBit5 等家族的数据表现相近，表明多支勒索团队均具备成熟且持续的攻击能力。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYZSricXW7NmZ0Wa3Xib4sZDE8yHW8MGmHrWzbtKnLY0ibeicq4xHghHibzxs3kbTObXI9Z4Bvg0SsC8p7qbp2kUsFruDENfH5AXFqw/640?wx_fmt=png&from=appmsg)

4月全球活跃勒索家族占比饼状图

在行业覆盖上，商业服务、制造业、消费服务、医疗与科技行业首当其冲。其中，商业服务行业成为重灾区，占比高达 20.26%。商业服务类企业通常涉及广泛的客户资料、供应链协作系统和外部数据接口，一旦系统失陷，极易造成业务中断与机密数据泄露的双重连锁反应，因此被攻击者视为极具“勒索变现”价值的高优先级目标。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYpdDWvETuWxsItBIe6zrzvndN9yibwkZzuxvJHiaufYTqSqic3g0hGLk4BkjodPrMDGicHkTm12kSiaoialuhQ6dUmq4zRicibSwrF4yM/640?wx_fmt=png&from=appmsg)

4月全球勒索攻击受害行业分布饼状图

## 二、国内实战处置数据与威胁演进趋势

### 2.1 国内高频家族与变种演变

4月份，Solar 应急响应团队共赴一线处置各类网络安全事件 **88 起**。在勒索软件分类中，TellYouThePass 家族的活跃度占据绝对主导，共处置 28 起，占总事件数的 31.82%，持续稳居国内勒索家族攻击榜首。紧随其后的是 Weaxor 家族，以 22 起（占比 25.00%）的规模保持高频活跃。

在实战排查中我们捕捉到了一个值得警惕的信号，4月份 Weaxor 家族出现了一起疑似变种案例。该变种的加密后缀依然保留为 `.rox`，但增加了对受害文件名的乱码化处理逻辑。Solar 团队目前已成功提取该变种加密器，正围绕其底层的密钥生成机制与文件命名规则展开深度的逆向工程分析。

整体而言，4月份国内的态势相较上月更加分散，共波及 21 个不同的勒索家族。除上述两大头部家族外，GodDamn、Asclepius、Woodpecker 等长尾家族的活跃度也在快速上升。这提醒我们在日常防护中，不能仅依据单一的家族特征或文件后缀构建防线，而是需要建立覆盖多家族变种的动态防御体系。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYdicINhBWibtcUT2tQia8UcAnzEibDath4T1WAoa0yj5UcheIUnLL1ib2MtIsV0N4KEEIg8aiaRBKkVqfKJNV1tLxicqSePG9GLccJlY/640?wx_fmt=png&from=appmsg)

4月国内TOP勒索家族分布饼状图

### 2.2 国内受害企业画像与入侵途径归因

4月份的受害目标高度集中在信息技术（14.77%）与制造业（13.64%）两大领域。在地域分布上，北京、广东、江苏、河南、浙江等地出现频率较高。这反映出经济活跃、业务系统庞杂且公网资产暴露面较大的区域，依然是攻击者自动化扫描与定点渗透的核心区域。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZ4zB5Ix8hQn9Jfld34OzxeIzSdsx2A4p9C9a3ibMOhuUTxria7x17vJQlibyMvDZYicVYFoDibOmb2BoLcMaMDB3fQeiaXS36nrhhyI/640?wx_fmt=png&from=appmsg)

4月国内受害企业行业分布饼状图

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYick0dgxlCZHTaCic8icMkIXD3mFp8QUK0Dq1SZLXgKH7wUMcVeRb6qfHANE7vIQpuUVj82QGrH37976Y4e0s9SZ0hk81iav1W2rU/640?wx_fmt=png&from=appmsg)

4月国内受害企业地域分布饼状图

深入剖析这 88 起安全事件的入侵途径，我们发现企业防线的突破口主要集中在以下三个薄弱环节

* **ERP/OA 历史漏洞利用（占比 65.38%）：**这是4月份最核心的失陷入口。攻击者频繁利用金蝶、用友等企业级管理系统的历史已知漏洞进行大范围的扫描与渗透。特别是在 TellYouThePass（`.sorry`勒索病毒） 的相关案例中，攻击活动往往精准踩准周末休息时段发起。结合其漏洞利用偏好与作案时间，不排除其背后有极其熟悉国内政企网络架构的攻击者主导或参与。
* **RDP 弱口令爆破（占比 19.23%）：**服务器远程桌面（RDP）公网暴露叠加口令强度不足，依然是企业防线失守的重灾区。缺乏多因素认证（MFA）和源 IP 访问限制，使得自动化爆破脚本得以轻易得手。
* **数据库暴露与弱口令（占比 11.54%）：**数据库端口违规映射至公网或存在默认口令，为攻击者提供了直接获取核心数据的捷径。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQbNSFLkRCxY3uplBQAsG5aLTQVm70fkKPyqNuNuWgfPYy76BF03oAtIPXhCnCXlxmA08yt7qeIgLvicrK3wNAXyvSuEKG4cSbUw/640?wx_fmt=png&from=appmsg)

4月国内勒索攻击入侵途径分布饼状图

## 三、典型案例深度复盘 供应链隐患引发的内网渗透

在近期的应急响应实战中，Solar应急响应团队协助某大型制造企业处置了一起由 Beast（别名 Monster）勒索家族变种引发的严重业务停摆事件。

通过对系统底层日志和网络流量的深度溯源，我们发现攻击者并未动用复杂的高级零日漏洞，而是精准捕捉到了企业在供应链管理中的安全盲区。第三方运维人员为图操作便利，违规部署了免费版的内网穿透工具（花生壳）并在维护结束后未及时关闭通道，这一行为等同于在企业坚固的外网防火墙上开了一扇“后门”。

### 3.1.1 攻击时间线全貌

取证发现，第三方运维人员违规使用了免费版的内网穿透工具（花生壳）进行远程维护，且在维护结束后未关闭穿透策略。这一管理疏漏，为攻击者提供了机会。以下是完整还原的黑客攻击与运维人员操作交错的时间路线图：

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQbZopve6ibrcCiaj7sVWEbMzDX4c5xPWZv2VsvnQdJphBOUibKryc2LbYaeTqjbZV8OibtKmZ7BzUmJLzRHt0vUnn08bhhVa1XM12E/640?wx_fmt=png&from=appmsg)

**黑客入侵与第三方运维违规操作交错的完整时间路线图**

|  |  |  |
| --- | --- | --- |
| 攻击阶段 | 时间节点 | 行为溯源记录 |
| 攻击未开始 | 2026/3/18 21:21 | 第三方运维使用花生壳远程登录 |
| 2026/3/18 21:35 | 第三方运维注销，未关闭穿透策略 |
| 攻击开始 | 2026/3/19 6:40 | 黑客利用花生壳暴露端口进行口令爆破 |
| 2026/3/19 7:00 | 口令爆破成功，但自动化爆破脚本未停止 |
| 2026/3/19 9:42 | 第三方运维使用花生壳远程登录 |
| 2026/3/19 11:46 | 第三方运维注销 |
| 2026/3/19 14:24 | 第三方运维使用花生壳远程登录 |
| 2026/3/19 15:54 | 第三方运维注销 |
| 2026/3/19 15:59 | 第三方运维使用花生壳远程登录 |
| 2026/3/19 16:06 | 第三方运维注销 |
| 2026/3/19 16:27 | 第三方运维使用花生壳远程登录 |
| 2026/3/19 16:30 | 第三方运维注销 |
| 2026/3/19 16:41 | 第三方运维使用花生壳远程登录 |
| 2026/3/19 16:41 | 第三方运维注销，仍未关闭穿透策略 |
| 2026/3/19 23:51 | 黑客爆破行为正式结束 |
| 2026/3/20 1:38 | 黑客利用花生壳第一次登录 |
| 2026/3/20 1:40 | 黑客注销 |
| 2026/3/20 3:29 | 黑客利用花生壳第二次登录 |
| 2026/3/20 3:30 | 黑客修改系统 Administrator 密码 |
| 2026/3/20 3:34 | 黑客注销 |
| 2026/3/20 3:42 | 黑客利用花生壳第三次登录 |
| 横向攻击 | 2026/3/20 3:56 | 黑客使用 netscan 进行横向攻击探测 |
| 2026/3/20 5:49 | 攻击结束，系统日志显示所有横向攻击失败 |
| 投放加密器 | 2026/3/20 6:10 | 投放 svchost.com 病毒程序 |
| 2026/3/20 7:07 | 投放核心加密器文件 |
| 2026/3/20 7:08 | 运行加密器并退出登录 |
| 故障发现 | 2026/3/20 9:48 | 本地管理员发现异常，但本地登录失败 |

### 3.1.2 初始打点与口令爆破攻击

安全日志提取分析显示，攻击者在探测到穿透端口后，随即发起了自动化攻击。

2026年3月19日 06:40:28，黑客使用 IP（溯源标记为：IP1）针对服务器暴露在公网的接口，开始进行持续性的口令爆破。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZEU4SvjibibwI7OfmXVVybnUabqD1icbPViciarAaVDWYibSLic6SslLpzqnCsu17Rd0zRia4ibK2epjCgicYRL8FGPaqlVNp6PiaXaCD03c/640?wx_fmt=png&from=appmsg)

**Windows安全日志（Event ID 4625）记录的高频口令爆破攻击起始动作**

由于企业账号体系存在弱口令问题，2026年3月19日 07:00:15，攻击者爆破成功，并于 07:00:17 短暂注销登录退出。值得注意的是，尽管已经成功获取凭据，但攻击者的自动化爆破程序并未立即停止，爆破行为依旧在系统后台持续，直到当晚的 23:51:49 才彻底结束。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZ4lNFRSTMFnjX0YQx59zuUUBEGYicZqWtkicj2PibUPXibEib7wRw1qWgBibXROvf9zoGQyQhMyDSoOPDPJeOAgJDawsPPfbyibNzYIA/640?wx_fmt=png&from=appmsg)

**Windows安全日志（Event ID 4624）记录的口令爆破成功及异常登录事件**

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZMWtPP5NneWibA6dbI8ibuguEhqM42REiar0NibLjZ3fiad2mTHIX5k1ROIErnVibia5gpcshe63RGRGFHsarNwOyZqTrDzPG6ep6xuY/640?wx_fmt=png&from=appmsg)

**攻击者获取凭据后的短暂停留与注销操作日志**

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZuv2IIvdQZia8fWaILDanNBcmMByI58d3fzDpzmOMFrjOQlgIvTRqkkerUbRBc66QIibjX6TJiahl24C9XFic6EicsDLpQa1iaLp5Ls/640?wx_fmt=png&from=appmsg)

**自动化口令爆破脚本行为彻底结束的时间节点审计**

### 3.1.3 权限接管与取证盲区

次日凌晨，攻击者开始利用获取的凭据正式潜入系统进行活动。

2026年3月20日 01:38:31，黑客更换设备（溯源标记为主机2），通过花生壳连接首次进入到服务器中。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQanoDFGcBdywia1ib1uQR8dWJRKaHfJLGpsopq0CibpFae4mPCicqiafx9KgZDq3ibJbTfcTs46cvllO4FFFvUJXfeY3WNtD8WGQwKA4/640?wx_fmt=png&from=appmsg)

**攻击者首次利用获取凭据通过内网穿透通道登录系统的审计记录**

在此排查环节中，团队遇到了由于第三方工具管理不规范带来的阻力。花生壳控制台因为使用的是免费版本，平台端没有提供详尽的访问日志记录能力，仅存留简单的流量统计记录（数据显示 20 号全天整体消耗流量仅为 44.49MB）。这也为后续追溯攻击者更加明确的网络特征增加了难度。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQaf5HvoQhibbENVHdjBr4KREkZWrwUvXu6dgic41m56W8zicl6VicBoyMnaOw3Q7fdfqQxqT8tibN1icTlOLxbvNeHlYXE9Dk2VcevibI/640?wx_fmt=png&from=appmsg)

**免费版内网穿透工具仅存留的粗粒度流量消耗记录（缺失源IP与会话详情）**

短暂探查后，2026年3月20日 01:40:48，黑客注销账户退出远程控制。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYbamE4ITYgXspVo0k4e5Ytsd0wqib3B8cYSiatzSx1hWIr0oebLBBSyUd5uHRltQyiboEP9gA8pH11Q1eJFOQN3xKibgYicx0klgZI/640?wx_fmt=png&from=appmsg)

**攻...