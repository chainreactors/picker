---
title: 打电话偷数据：Com 系钓鱼团伙的高调窃案，与伪装成 Chrome 的扩展 C2
url: https://mp.weixin.qq.com/s/cDUA0O2d2_0cQ7OnomIAyA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:46:12.406117
---

# 打电话偷数据：Com 系钓鱼团伙的高调窃案，与伪装成 Chrome 的扩展 C2

# 打电话偷数据：Com 系钓鱼团伙的高调窃案，与伪装成 Chrome 的扩展 C2

Unit 42
Unit 42

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 原文：https://unit42.paloaltonetworks.com/com-affiliate-vishing-attacks/
> 作者：Unit 42（Palo Alto Networks）
> 发布时间：2026-11-20
> 翻译模型：GLM-5.3
> 质量评分：★★★½（3.5/5） ｜ 标签：凭据访问 · 持久化 · 检测基础设施

**AI 摘要**：Unit 42 盘点 2026 年 8 月以来 Com 系（The Com）关联团伙的持续性 vishing 攻击浪潮：冒充内部 IT 支持诱导员工访问按目标组织定制的 AiTM 代理子域，实时截获凭据与 MFA 会话后数分钟内注册攻击者自己的 MFA 设备（多个集群复用同一台名为 Pixel 10a 的设备），再用 python-httpx、Microsoft Graph SDK 等脚本化外传 Microsoft 365 邮箱、OneDrive 与 SharePoint 数据，最后经 Teams 和邮件发勒索信并指向 Tor 谈判站。技术增量在一个伪装成「Google Chrome」的恶意扩展（经 Developer Mode 侧载，不上架 Chrome Web Store）：全局键盘记录、跨站窃取 localStorage/sessionStorage 与 IndexedDB、扫描页面 QR 码截获登录/MFA token、串流摄像头，并通过 chrome.debugger（Chrome DevTools Protocol）实现截图、输入事件派发、剪贴板窃取与远程导航的完整 C2 模块。全文附 7 个活动集群对照表、56 个钓鱼 FQDN 与域名注册模式表，受害行业从金融服务转向医疗，澳大利亚目标占比 10 月升至约 13%。

Unit 42 这篇是 Com 系 (The Com，一个以英语圈年轻人为主的松散网络犯罪联盟，成员团伙间共享基础设施与作业手法，以 vishing 和数据勒索闻名) 活动的季度性情报盘点，叙事和产品段占了不少篇幅，但中间埋着一块真正的硬货：那个伪装成「Google Chrome」的恶意扩展。它把 chrome.debugger（CDP）变成了完整的 C2 通道——截图、键盘鼠标输入、剪贴板、远程导航全在浏览器进程内完成，和本仓库已译的《受害者的浏览器就是 C2：Falcon 框架与 OneDrive 后门 Antino》正好对读：Falcon 是往网页里注入 JS implant，这个是把 C2 长进扩展 API 里，都让受害者的浏览器替攻击者干活。扩展窃取这条线，还可与 TAG-150 攻击链篇里 66 个钱包/密码管理器扩展的定向窃取对照——不上架官方商店、诱导侧载是共同路线。此外，Table 2 的域名注册模式表（TLD、连字符格式、认证关键词）和 56 个 FQDN 清单是给蓝队的现成狩猎素材，Pixel 10a 设备名复用则是跨账户聚类归因的廉价信号。想看社会工程全链的读者按顺序读即可，只想要技术细节的读者可以直接跳「恶意浏览器扩展」一节。

---

## 执行摘要

近几个月，Unit 42 持续跟踪并响应了多波由 Com 系关联威胁行为体实施的 vishing（语音钓鱼）攻击。这些攻击导致了数据窃取和勒索企图，目标是金融服务、医疗和法律服务等数据密集型行业，受害组织主要位于美国、英国和澳大利亚。

对这批广泛活动的归因包括：

* 具名 actor，如 Bling Libra（又名 ShinyHunters）
* 活动集群 CL-CRI-1116（又名 Redact，前称 BlackFile）、CL-CRI-1147（又名 Pink）、CL-CRI-1182（又名 Falcon）、CL-CRI-1192（又名 Helix）
* 新发现的 CL-CRI-1264（又名 Vortex）和 CL-CRI-1274（又名 Cinder），与 Google 跟踪的 UNC6671 活动存在重叠

本文内容包括：

* 我们基于独特遥测分析和事件响应项目，对 2026 年 8 月以来 Com 系关联威胁活动的持续观察
* 我们跟踪的各个具名 actor 和活动集群，包括此前未披露的独特观察
* 受害者画像洞察
* 攻击者战术、技术与程序 (TTP) 梳理
* 展望 2027 年的可能动向

Palo Alto Networks 客户可通过下列产品与服务获得针对上述威胁的更好防护：Advanced WildFire、Advanced URL Filtering、Advanced DNS Security、Advanced IP Defense、Cortex XDR 与 XSIAM、Cortex Agentic Endpoint Security、Prisma Browser、Device Security、Idira Identity and Access Management (IAM)、Idira Identity Threat Detection and Response (ITDR)、Idira Secure Web Sessions (SWS)。组织还可通过 Unit 42 Threat Intel Services 及其 Deep and Dark Web Service 获取定制对手情报、分析师直接咨询和专项暴露面追踪。如认为自身可能已被入侵或有紧急事项，请联系 Unit 42 事件响应团队。

| **相关 Unit 42 主题** | **勒索** 、**Vishing**、**社会工程**、**Bling Libra**、**浏览器扩展** |
| --- | --- |

## 背景

自 2026 年初以来，我们响应了多起数据窃取和勒索企图，归因于 Bling Libra 及其他 Com 系关联威胁行为体。攻击者常用剧本的更多细节见本文「战术、技术与程序」一节。

我们使用威胁组织和活动集群命名规范来跟踪这些活动，见表 1。

| **Actor/集群** | **别名** | **首次观察** | **TOX ID** | **基础设施观察** |
| --- | --- | --- | --- | --- |
| Bling Libra | ShinyHunters | 2019 | 固定 | NiceNIC + Cloudflare；以 report/claims 为主题的域名 |
| CL-CRI-1116 | Redact（前称 BlackFile） | 2026 年 1 月 | 多个 | NiceNIC + Cloudflare |
| CL-CRI-1147 | Pink | 2026 年 5 月 | 多个 | NiceNIC + Cloudflare |
| CL-CRI-1182 | Falcon | 2026 年中 | 固定 | NiceNIC + Cloudflare |
| CL-CRI-1192 | Helix | 2026 年 6 月 | 多个 | NiceNIC + Cloudflare |
| CL-CRI-1264 | Vortex | 2026 年 9 月 | 固定 | Cnobin + Cloudflare |
| CL-CRI-1274 | Cinder | 2026 年 9 月 | 固定 | Internet Domain Service BS Corp + DDoS-Guard |

表 1. Com 系具名 actor 与活动集群的区分。

## 最新观察

### 新兴活动集群 CL-CRI-1264 (Vortex)

2026 年 9 月，我们识别出一个新的活动集群，跟踪编号 CL-CRI-1264。攻击者的手法大体遵循 Com 系关联威胁行为体的通用剧本，但有几个特征把它和其他集群区分开来：最显著的是，我们观察到该活动主要针对医疗、制药和其他医疗类组织。

与 CL-CRI-1264 关联的攻击者通过 vishing 建立初始访问——冒充内部 IT 支持，把员工引导到针对每个目标组织定制的子域服务器上。这些服务器充当 AiTM (adversary-in-the-middle) 代理，把用户凭据和多因素认证 (MFA) 批准实时转发给攻击者。攻击者既针对员工的公司工作站，也针对其个人移动设备。

我们观察到 CL-CRI-1264 背后的攻击者在完成认证后的几分钟内就注册未授权 MFA 设备以建立持久化。在多起案例中，攻击者在多个失陷账户间复用了同一台名为 Pixel 10a 的设备。他们还使用 Python 脚本 (python-httpx User Agent) 自动化数据外传，目标是 Microsoft 365 邮箱、OneDrive 和 SharePoint 内容。

外传完成后，攻击者直接向受害组织员工发送 Microsoft Teams 消息，声称已窃取数据，并引导收件人访问一个 Tor 托管的谈判网站。

### 新兴活动集群 CL-CRI-1274 (Cinder)

2026 年 9 月，我们识别出另一个新活动集群，跟踪编号 CL-CRI-1274。与本报告所述的其他活动类似，攻击者以 vishing 获取初始访问，并通过重放持久的「keep me signed in」会话 token 避免再次触发 Duo MFA 验证，随后从代理基础设施重放同一会话 token。

接着，他们通过 python-requests (python-requests/2.34.2) 和 Microsoft Graph 软件开发工具包 (SDK) 进行脚本化访问，从受害者的 SharePoint 和 OneDrive 环境收集并外传数据。之后，攻击者利用一个失陷账户通过邮件和 Microsoft Teams 在组织内部发送勒索消息，最终引导收件人访问 Tor 托管的谈判网站。

### 恶意浏览器扩展

在一起归因于另一个活动集群 CL-CRI-1192（Google 将其跟踪为 UNC6671）的调查中，我们识别出一个恶意浏览器扩展https://www.virustotal.com/gui/file/ea8d30c42e758559e78bd1fe97f8849011beb7f24c7f092a066a5a62fa7fbe6f (manifest 版本 1.6.111)，名为 Google Chrome。

该扩展不在 Chrome Web Store 上，从攻击者控制的服务器 oskeysetup[.]com 下载，需要受害者手动在 Developer Mode 下侧载安装。把扩展命名为 Google Chrome 有助于伪装浏览器内置的警告横幅 (Google Chrome started debugging this browser)，使其在扩展活动时不被察觉。

该域名的注册信息与 Google 和 ReliaQuest 此前披露的攻击者基础设施高度相似，关联到我们跟踪为 CL-CRI-1192 的活动。

这个浏览器扩展执行多项恶意操作：

* 安装全局键盘记录器
* 窃取所有站点的 local/session storage 和 IndexedDB 数据
* 收割认证 cookie（针对 Microsoft 和 Google 账户）
* 扫描页面上的 QR 码以截获登录/MFA token
* 串流摄像头画面

此外，该浏览器扩展还通过 Chrome DevTools Protocol (chrome.debugger) 实现了一个完整的命令与控制 (C2) 远程控制模块，允许操作者执行以下操作：

* 隐蔽截图
* 派发输入事件
* 窃取剪贴板内容
* 远程导航站点

我们以该文件为线索追查，又识别出另一个同样伪装成 Google Chrome 的浏览器扩展https://www.virustotal.com/gui/file/930898e8b65e9cf4e2595ac4092042a707cca8922751e723ad8b86260655154a (版本 1.6.112)，它与同一台 C2 服务器通信，两个文件共享同一个硬编码 API key。

我们以中等置信度评估：CL-CRI-1192 关联的攻击者开发这个恶意浏览器扩展，是为了给运行 Chromium 系浏览器（如 Google Chrome 和 Microsoft Edge）的台式机和笔记本提供另一种提取凭据的手段。该扩展也可能被共享给其他 Com 系攻击者使用，不过我们目前没有证据支持这一点。

我们感谢 Kevin Pham 在 2026 年 9 月的一篇 write-up 中对这个浏览器扩展的详尽调查。

## 受害者画像

我们的遥测显示，Com 系关联威胁行为体的持续攻击活动自 2026 年 8 月前后显著加速。受害者有共同画像：持有大量高影响企业数据，一旦暴露会带来严重的监管、法律或市场后果。金融服务、医疗和法律组织是主要目标，但活动也横跨其他行业。

攻击者不是泛泛地针对普通邮箱，而是系统性地寻找对高价值文件、文档和数据库负责的个人或系统。这些攻击聚焦于：

* **法律与公司战略：**

  攻击者瞄准合伙人通信、事务所战略、高管薪酬和待签合同，并明确威胁公开客户协议和机密案件材料。
* **金融与投资记录：**

  攻击者优先窃取私募投资组合、交易管线和大型云数据仓库，偶尔一次性外传数千万条客户关系管理 (CRM) 和招聘记录。
* **医疗与生命科学：**

  攻击者瞄准包含患者记录和专有研究的云数据平台。为最大化施压，攻击者在内部聊天频道广播勒索通知，并威胁向监管机构举报。

最受针对的组织普遍具有分布式员工队伍、集中式单点登录 (SSO) 和广泛的云协作平台，且绝大多数位于英语国家。我们观察到攻击者反复攻击同一组织，有时在失败数周后卷土重来。

### 谁在被盯上：行业与国家

我们对 Com 相关活动关联域名的监控显示，其目标在 2026 年 9 月初从金融服务转向医疗。图 1 显示，2026 年 8 月这些攻击者针对金融服务组织的频率约为医疗组织的两倍，但 9 月医疗超过了金融服务——大约就在我们首次观察到 CL-CRI-1264 活动的时候。2026 年 10 月，医疗与金融服务并列成为最受针对的行业。攻击者也经常针对建筑、高科技、交通运输与物流组织。

![图 1：各行业组织遭受攻击数量随时间变化的折线图，行业包括医疗、金融服务、建筑、高科技、交通运输与物流、专业与法律服务、制造、制药与生命科学、保险、房地产，9 月上中旬出现明显峰值](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqVHnOhFWNwpeUoBmCL7qlbLPVRJTCxiaNgaicVp9b1xR4jRnPnE8GkLDsq5ibAK3HVycibwER9XJ2u2YcALFibrWxbNuZ6Bj3kJzEOk/640?wx_fmt=png&from=appmsg)

图 1. 2026 年 8 月至 10 月子域中受针对组织的行业分布。

图 2 显示，2026 年 8 月至 10 月间，大多数受针对组织位于美国。但我们观察到自 2026 年 9 月下旬起对澳大利亚组织的攻击增加。澳大利亚组织在 8 月和 9 月占观察到的子域不到 1%，10 月升至约 13%。澳大利亚现在是第二大受针对地区。

![图 2：标题为 Top Targeted Geographies by Percentage Share (Aug - Oct 2026) 的堆叠柱状图，三个月各一根柱，按国家分段；美国 8 月占 95.3%、9 月 91.9%、10 月 76.2%，澳大利亚 10 月升至 13.0%，其余为英国、加拿大、瑞士和其他](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqXmOZMAibGjzH99wY9q34DgicwIicjBRGIMlw2icvK6n6M3dMGQYTfWoIAlwszSYiaH88wONmiayH6vvqzyYcLvzPA28nlmfAFAeiawFs/640?wx_fmt=png&from=appmsg)

图 2. 2026 年 8 月至 10 月子域中受针对组织的国家分布。

## 战术、技术与程序

### 基础设施与工具

Com 系关联威胁行为体的一个关键特征，是使用伪装成 SSO 门户、IT 支持页面和 passkey 配置服务的 apex domain（注册的裸域）。这些域名常托管短生命周期的子域来冒充目标组织，例如 {company}.mfaregister[.]com。我们积极跟踪这些基础设施，对已识别域名进行威胁狩猎，并在我们的 GitHub 仓库以 Timely Threat Intelligence (TTI) 形式发布关键发现。

在 Com 系关联的各案例中，我们发现其托管基础设施、攻击链和受害者画像存在相似性。某些案例中，这些攻击者还共享工具，例如 Doko's Panel——一个由操作者控制的 AiTM 钓鱼 kit。

正如 Push Security 此前报告的，该 kit 的部分针对 Okta 的变体把面板默认的 backend.php handler 替换为改名的端点 api\_FyekIDWY.php。我们在多个与 Com 系案例关联的域名上观察到这个端点。

在至少一起金融服务案例中，遥测记录了从凭据输入到 MFA 数字匹配 (number-match) 提示的完整 AiTM 序列，表明会话可能已被成功截获，如图 3 所示。

![图 3：凭据与 MFA 截获流程图，涉及三方——受害者、中间人代理、操作者；序列包括落地页诱饵、钓鱼 kit 激活、用户名提交、密码提交、MFA 挑战，最后一步是把已认证会话转发给操作者；流程使用 Cloudflare 前置的钓鱼 kit，组件包括 Evilginx2 kit 与 Doko's Panel](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqV87lD87YHnrnBGBPvr0yEEiciamcZ6SjZPS7uVuXbJiaDCVSbLe6NbxnxghCMCeYeicg6KiaRib9H3NTKGBt8WvzfCe1eJeE0TYvp0E/640?wx_fmt=png&from=appmsg)

图 3. 一次观察到攻击的流程图。

与 Com 系基础设施特征一致的域名，也出现在使用不同技术攻击受害者的活动中。例如，Microsoft 在其 passkey 主题社会工程研究中报告过 oskeyregister[.]com。

在该报告基础上，我们识别出遵循 connec...