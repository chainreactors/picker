---
title: C2 藏进 Yggdrasil 网状网：ESET 拆解 MythicRatatoskr 后门与 Sandworm 破坏收尾
url: https://mp.weixin.qq.com/s/zJvw36k9c7c-nsgiR4OIoQ
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:02:13.456364
---

# C2 藏进 Yggdrasil 网状网：ESET 拆解 MythicRatatoskr 后门与 Sandworm 破坏收尾

# C2 藏进 Yggdrasil 网状网：ESET 拆解 MythicRatatoskr 后门与 Sandworm 破坏收尾

ESET
ESET

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 原文：https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/
> 作者：Anton Cherepanov、Peter Strýček（ESET Research）
> 发布时间：2026-10-22
> 翻译模型：GLM-5.3
> 质量评分：★★★★★（5/5） ｜ 标签：国家级 APT 全链路 · 持久化 · 检测基础设施

**AI 摘要**：ESET 披露此前未记录的 Go 后门 MythicRatatoskr——把 C&C 服务器藏进 Yggdrasil 去中心化 mesh 网络里，从内嵌的 32 个公共 peer 中随机挑 3 个入网，再走 443 端口 HTTPS 通信；配置文件用 AES-256-CFB 加密（密钥硬编码）。时间线：2025-07-16 UAC-0099 以带恶意附件的鱼叉邮件攻入一家乌克兰粮食物流企业（MATCHWOK 执行链），次日部署该后门；2025-09-17 访问权移交 Sandworm，经 AD 组策略下发 SDelete 完成数据抹除。二进制中留有 Linux 变体的迹象，且这是首例有公开记录的国家级行为者滥用 Yggdrasil。

「C2 寄生」是本仓库反复出现的主题：GSocket 把 Linux C2 挂在公共中继上，Turla 的 Cereal 让受害者的 Exchange 自己当 C2，Falcon 把浏览器变成 C2，ShadowCloud 的 GitDoor 住进 GitHub issue。这次 ESET 拆解的 MythicRatatoskr，宿主换成了 Yggdrasil——一张去中心化 mesh 覆盖网，C&C 只是网中一个普通节点。文章的看点有三处：后门本体的一手拆解，配置结构、12 条命令、硬编码密钥全部落在表里；基础设施侧怎么溯源——公开地图过期了，ESET 自己生成了网络的 spanning tree 地图去定位 C&C；以及「初始访问组＋破坏组」的分工在俄系阵营如何落地。这条 C2 寄生线，文末译者补充里又过了一遍。

![MythicRatatoskr 后门 (原文头图)](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqXmhCqQu8AibTPib5oepjmiay138q0UVD1xxHoqfV03XxMeSUSnPnCHHE9tQibGut7pcwT4ibVOqMxUPK0sf18SyNtpcfrIABURuzfI/640?wx_fmt=jpeg&from=appmsg)

## 执行摘要

本报告分析的行动中，UAC-0099 于 2025 年 7 月 16 日获得初始访问权，随后把访问权移交给 Sandworm，后者在 2025 年 9 月 17 日执行了数据抹除攻击。报告的焦点是 MythicRatatoskr 后门，其独特之处在于用 Yggdrasil mesh 网络与藏在这张网里的 C&C 服务器通信。

我们于 2026 年 9 月 18 日在 LABSconhttps://www.labscon.io/、2026 年 10 月 16 日在 Virus Bulletin 会议https://www.virusbulletin.com/conference/vb2026/programme/上公布了关于 MythicRatatoskr 的发现。

> **本文要点：**
>
> * 2025 年 7 月 16 日，UAC-0099 通过一封带恶意附件的鱼叉邮件攻入乌克兰一家粮食物流公司，触发 MATCHWOK 后门的执行链。
> * 一天后，攻击者部署了 MythicRatatoskr，一个此前没有公开记录的后门，与藏身 Yggdrasil mesh 网络内的 C&C 服务器通信。我们在别处没有见到该后门出现，且有迹象表明可能还存在 Linux 变体。
> * Yggdrasil 是一个去中心化 mesh 网络，实现了实验性路由方案，节点之间的 IPv6 通信受端到端保护。
> * 最终，UAC-0099 把访问权移交给 Sandworm，后者执行了数据抹除攻击。

## 俄系阵营行为者之间的协作

本报告记录的移交并非孤立现象。如前所述，Sandworm 被归因于 GRU 第 74455 部队，而 UAC-0099 的攻击目标让我们评估该组织与俄罗斯利益一致。

2025 年早些时候，我们发现同属俄系阵营的 Gamaredon 与另一个俄系威胁行为者 Turla 展开合作，相关发现记录在我们的博文 Gamaredon X Turla collabhttps://www.welivesecurity.com/en/eset-research/gamaredon-x-turla-collab/里。这两个组织都与俄罗斯联邦安全局（FSB）有牵连。这类协作说明，俄系组织之间有可能协同开展网络间谍行动，目的多半是放大作战效果。更早之前，Gamaredon 还与我们发现并命名的 InvisiMolehttps://www.welivesecurity.com/2020/06/18/digging-up-invisimole-hidden-arsenal/合作过。放在这样的背景下，UAC-0099 向 Sandworm 的移交，就涉事双方而言不算常见，但作为一种模式已经不再让人意外。

## 入侵过程概览

根据 ESET 遥测，事件经过如下：2025 年 7 月 16 日 06:59，目标组织中一台机器执行了名为 pdfopentask 的计划任务。该任务从 %temp%\temporarydoc.txt 执行了一个 PowerShell 载荷。

一分钟后，MATCHBOIL 落地。MATCHBOIL 是一个下载器，本次从 https://egyptanimals[.]com/animals/photoalbum 下载了 MATCHWOK 后门（C&C：https://uztickets[.]com）。次日 09:28，一个新的二进制文件被投递到这台机器：MythicRatatoskr 后门。由于时间衔接紧密，我们高度确信是 MATCHWOK 执行链导致了 MythicRatatoskr 的部署。遥测进一步显示，随后又有更多 MythicRatatoskr 样本被部署到组织内的其他机器上，这次用的是 OpenSSH SFTP 服务器。

再往后，ESET 遥测在部分机器上检测到 SOCKS5 服务器，其中一个样本是用 WinRAR 从一个来源不明的压缩包里解出来的。我们认为这个 SOCKS5 服务器就是用 MythicRatatoskr 部署的。

大约两个月后的 2025 年 9 月 17 日，我们在受害的粮食物流公司检测到数据抹除活动。攻击通过 Active Directory 组策略部署 SDelete 工具来执行——这是 Sandworm 的标准战术、技术与程序（TTP），我们在 ESET 遥测中已经见过很多次。

因此我们评估，UAC-0099 可以为 Sandworm 充当初始访问的角色。

本文重点分析 MythicRatatoskr 后门、承载其 C&C 服务器的 Yggdrasil 网络，以及配套的 SOCKS5 服务器。MATCHBOIL 和 MATCHWOK 的早期版本已由 CERT-UA 在其预警https://cert.gov.ua/article/6284949中分析过，MATCHBOIL 及其演化另见我们的博文 MATCHBOIL: New tricks, same old evil intentionshttps://www.welivesecurity.com/en/eset-research/matchboil-new-tricks-same-old-evil-intentions/，所以这两个工具不在本文展开。

## 世界树上的松鼠

Yggdrasil 一词出自北欧神话，指一棵连接宇宙各界的圣树。树里住着一只名叫 Ratatoskr 的松鼠，在树顶与树根之间来回传话。鉴于这个后门扮演的正是穿梭于 Yggdrasil 网络中的信使角色，我们把它命名为 MythicRatatoskr。

更技术性地讲，Yggdrasil 是一个去中心化 mesh 网络：设备彼此直连，没有中心枢纽，在互联网之上搭起一层加密的 IPv6 覆盖网，让参与节点交换端到端受保护的流量。合法用户用这类 mesh 换取连接韧性，也拿它做研究和爱好者组网。因为没有任何单一服务器在运营这张网，它健壮、难以破坏——这些特性同样招攻击者喜欢。需要说明的是，Yggdrasil 并不以匿名性为目标。

## 归因

入侵后的执行链依赖已归因于 UAC-0099 的已知恶意软件——MATCHBOIL 下载器和 MATCHWOK 后门——因此我们高度确信，把攻击的这一阶段归因于 UAC-0099。两个月后观察到的数据抹除活动，依据所涉 TTP，我们同样高度确信地归因于 Sandworm。

此外，我们高度确信 UAC-0099 在入侵期间的某个时点把访问权移交给了 Sandworm，只是还无法确定 MythicRatatoskr 后门主要由 UAC-0099 操作，还是由 Sandworm 操作。

## UAC-0099 档案

UAC-0099 是一个网络间谍组织，目标清一色在乌克兰：政府机构、金融机构和媒体。基于其攻击目标，我们中等确信该组织与俄罗斯利益一致。UAC-0099 可以为 Sandworm 充当初始访问中介，后者是最以在乌克兰搞破坏性攻击闻名的俄系组织。

该组织至少从 2022 年开始活跃，2023 年 6 月由 CERT-UAhttps://cert.gov.ua/article/4818341首次报告。除 MATCHBOIL 外，该组织通常还会部署 LONEPAGE——一个 PowerShell 下载器，因 C&C URL 里带有 page 一词得名。

## Sandworm 档案

Sandworm 是搞破坏性攻击的俄系威胁组织。它最出名的战果是 2015 年 12 月和 2016 年 12 月对乌克兰能源公司的攻击https://www.welivesecurity.com/2022/03/21/sandworm-tale-disruption-told-anew/，两次都造成了停电。2017 年 6 月，Sandworm 发动 NotPetya 数据抹除攻击，通过攻陷乌克兰会计软件 M.E.Doc 走供应链向量。2018 年 2 月，Sandworm 对 2018 年平昌冬奥会的组织方发动 Olympic Destroyer 数据抹除攻击。

Sandworm 会用 Industroyerhttps://www.welivesecurity.com/2017/06/12/industroyer-biggest-threat-industrial-control-systems-since-stuxnet/这类先进恶意软件——它能通过工业控制协议与能源公司的设备通信。2022 年 4 月，CERT-UA 挫败了一起针对乌克兰能源公司的攻击，Sandworm 当时试图部署该恶意软件的新变体 Industroyer2https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/。

自 2022 年 2 月以来，Sandworm 在乌克兰一直很活跃，不断对战略性组织部署数据擦除器。

2020 年 10 月，美国司法部公布对六名俄罗斯黑客的起诉书https://www.justice.gov/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and，指控他们准备并实施了多起 Sandworm 攻击。如前所述，该组织通常被归因于 GRU 第 74455 部队。

## 入侵链

### 初始访问与执行

根据 ESET 遥测，初始访问经由一封带恶意附件的鱼叉邮件获得——这一发现与 CERT-UA 博文一致。我们评估，接下来是 MATCHWOK 后门执行链（CERT-UA 博文已有记录）导致了 MythicRatatoskr 的执行——这是一个通过 Yggdrasil 网络与 C&C 服务器通信的后门。再往后，攻击者可能用 MythicRatatoskr 投递了 SOCKS5 服务器。

### 持久化

MATCHBOIL 通过在注册表键 HKCU\Software\Microsoft\Windows\CurrentVersion\Run\ 下添加注册表值 UpdateMonitor 来持久化 MATCHWOK，数据指向落地的 MATCHWOK 路径。

MythicRatatoskr 以名为 ieupdate 的 Windows 服务启动。

### 收集与外传

check-in 时，MythicRatatoskr 向 C&C 服务器发送当前用户名、主机名和本地网络设置。此外，操作者可以用 MythicRatatoskr 把文件和屏幕截图外传到 C&C 服务器，走的是经 Yggdrasil mesh 网络路由的 HTTPS。数据在外传前不做暂存。

## 工具集

### MythicRatatoskr

MythicRatatoskr 是用 Go 写的后门，靠 Yggdrasil 网络（见「网络协议」一节）连接它的 C&C 服务器。如前所述，后门以北欧神话里的松鼠 Ratatoskr 命名——它在 Yggdrasil 这棵连接宇宙各界的圣树上，于树顶与树根之间传话。对一个在 Yggdrasil 网络里搬运数据的后门来说，我们觉得这个类比很贴切。二进制中的迹象表明，开发始于 2024 年 12 月到 2025 年 2 月之间的某个时间点。

二进制里留下的函数名——混用大驼峰（CheckInAgent）和蛇形命名（agent\_run）——要么说明代码是从别的项目合并来的，要么说明作者命名不讲究。关键函数负责服务注册与 Yggdrasil 网络初始化（main、runService），check-in 与信标（agent\_run、init\_agent、CheckInAgent），配置处理（saveConfig、Encrypt、Decrypt），命令轮询与分发（getTasks、doTask），以及后门命令本身（upload、download、screencat、shell、manageProxy 等）。

部分样本还带 10 分钟的启动延迟，多半是为了避免一执行就连上 Yggdrasil 网络，借以规避检测。

#### 主机痕迹

表 1 列出我们分析中观察到的 MythicRatatoskr 主机痕迹。注意 krbtman.exe 的文件名冲突：在有些机器上它是 MythicRatatoskr，在另一些机器上是 SOCKS5 服务器。

**表 1. 与 MythicRatatoskr 相关的主机痕迹**

| 名称 | 值 |
| --- | --- |
| 安装路径 | C:\windows\system32\updater.exe |
|  | C:\Windows\system32\krbtman.exe |
|  | C:\windows\system32\windowsdefendersvc.exe |
|  | %localappdata%\Microsoft\OneDrive\OneDriveLiveUpdater.exe |
|  | c:\program files (x86)\microsoft.net\adomd.net\110\applicationasphost.exe |
|  | C:\OFFICE2010\Utilities\Act64.exe |
|  | %userprofile%\Downloads\WindowsDefenderSvc.exe |
|  | %userprofile%\Downloads\ieupdate.exe |
|  | %userprofile%\Downloads\ie.exe |
|  | %userprofile%\AppData\Local\Internet Explorer\ieupdate.exe |
|  | %userprofile%\AppData\Local\ieupdate.exe |
| 配置路径 | C:\Windows\Temp.updatecache |
|  | C:\Windows\system32.updatecache |
|  | %LocalAppData%/Temp/.crond (分析者注：正斜杠是攻击者的笔误) |
| 服务名称 | ieupdate |

#### 持久化

根据从受害机器拿到的 Windows 事件日志，updater.exe 和 WindowsDefenderSvc.exe 是作为 Windows 服务启动的，因而很可能就是靠服务持久化的。

#### 网络协议

与 C&C 服务器通信时，MythicRatatoskr 依赖 Yggdrasil 网络——一个仍处于 alpha 状态的去中心化 mesh 网络，实现实验性路由方案。网络中每个节点生成自己的 Ed25519 密钥对，peer 之间的 IPv6 通信因此有端到端保护。IPv6 地址由公钥派生，落在 200::/7 子网范围内，该网段 2004 年已被 IETF 废弃。匿名性不在项目目标之列。这个话题我们在「网络基础设施」一节展开。

yggdrasil-go 仓库已经提供加入 Yggdrasil 网络所需的类型和方法。还有另一个项目 yggstack，让 Yggdrasil 网络经由用户态的网络栈通信。好处是不需要创建隧道接口——在用户没有创建它的权限，或者系统不支持这种接口时，这本来会是个麻烦。MythicRatatoskr 的代码基于 yggstack，这让恶意软件可以移植。

往 Yggdrasil 配置里添加至少一个公共 peer，就能加入那张公开可用的网络。MythicRatatoskr 内嵌一个 base64 编码的 blob，里面是 URI 格式的公共 peer 清单，清单上大多数 peer 至今仍在运行。MythicRatatoskr 从硬编码清...