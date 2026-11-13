---
title: 黑客都在用什么渗透平台？
url: https://mp.weixin.qq.com/s/Sd-gMfdsr8NiqgwFnbRJSQ
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:22.715864
---

# 黑客都在用什么渗透平台？

# 黑客都在用什么渗透平台？

原创

安妮
安妮

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6P08EEHNoEpoOYsSVYV9a2CiarjaPHgiakVODRHG5OAWlg3CE2fJXDgay4r0CuQqb9Zoe5MX2SfdGEcIhY8HRQ43YYFhvxfICtEE/640?from=appmsg)
> **导语**：这个秋天刷屏的入侵，技术上并不高明，它们只是快。微软说 Storm-0940 用 ARTEX 打了 2250 多个租户，CrowdStrike 跟的 VAPOR PANDA 横跨 200 多家机构。RST Cloud 顺手数了一遍公网上裸露的 AI 渗透控制台：1341 个。

## 一、要的是节奏，不是技术

这个秋天刷屏的入侵事件并不高明。它们快。

微软披露，ConnectWise 被攻破之后，Storm-0940 用 ARTEX 尝试登录超过 2250 个租户。在多起由 ARTEX 驱动的攻击里，这位攻击者从初次锁定目标到拿到云上高权限只用了三个小时。另外，微软还观察到一场针对八家机构、327 个账号的密码喷洒行动，但没有发现一次成功登录。

CrowdStrike 从 10 月 17 日起开始追踪 VAPOR PANDA，同样用 ARTEX，横跨 200 多家机构。

有一个被 VULONE 研究过的 Cairn 操作者，跑了 66 个针对政府目标的项目，覆盖四个国家，烧掉大约 367 亿 token。

这些行动都不需要新漏洞。他们需要的只是一个编排器：拿到目标，拆成任务，派给 LLM agent，然后昼夜不停地跑下去。三个开源项目现在干的正是这件事——Cairn、ARTEX 和 PentAGI。

而且它们很好找。2026 年 11 月 2 日，我们在 Shodan 和 Netlas 上交叉验证并去重，数到这三个框架超过 1300 个暴露在互联网上的控制台。很多属于测试人员。有些不是，而从外面看，这些控制台长得一模一样。

## 二、这三个框架是什么

|  | Cairn | ARTEX | PentAGI |
| --- | --- | --- | --- |
| 上游 | oritera/Cairn | Autumn-27/ARTEX（2026 年 10 月隐藏） | VXControl |
| 技术栈 | Python、uvicorn、Alpine.js | Next.js + nginx | React SPA、自签 TLS |
| 默认端口 | 8000 | 8787 | 8443 |
| 默认认证 | 无 | 部分主机有 HTTP Basic（realm "ARTEX"） | 登录页，默认口令 |
| 许可 / 模式 | 开源 | AGPL，有 fork | 开源 + 商业版 |
| 衍生项目 | VulnFlow IoT、"Zero"、WorkerAnt | ScopeWeaver、BaaRai ARTEX、ARTEX v2、韩文版、AegisLoop | 改名版（"AI Pentest"、"Specter"） |

三个框架都会自己规划、调用工具、读输出、决定下一步，中间没人参与。操作者设定目标和规则，框架负责节奏。

有登录页不等于适合暴露在公网。很多 ARTEX 主机会回一个 HTTP Basic 认证挑战（realm "ARTEX"），PentAGI 会弹登录页并要求首次使用改掉默认口令，Cairn 干脆什么都没有。但我们的扫描不需要认证就读到了每个控制台的标题、页面正文、证书和 favicon，所以本文统计到的控制台无论如何都在公网上可达；而没有防护、或者还挂着默认口令的面板，正是 NorForge 看到被黑吃黑的那批。

## 三、Cobalt Strike 的老路

这条路我们见过。Cobalt Strike 原本是给红队用的，后来成了犯罪团伙和国家级入侵里最常见的后渗透框架。AI 框架走的是同一条路，只是更快。

**双用途是默认设定。** 红队、CTF 选手、研究人员、黑产团伙、国家级行为体，跑的是同一份代码。公开报道里权重偏向中国关联的行为体，但那只是他们最显眼，不是只有他们。

**fork 会自我繁殖。** ARTEX 有一个备用镜像（mhtsec）、一个通用名下的镜像的镜像（kutukam/autonomous-pentest-agent）、一个英韩双语 fork（cskwork/scopeweaver，约 770 星、660 次 fork），以及一个英文翻译版（BaaRai/ARTEX，约 320 星、170 次 fork）。BaaRai 那个 fork 加了一个浏览器扩展，能截取操作者已认证的会话，这样 agent 在 MFA 提示一次之后就能复用登录态。

**下架没用。** 2026 年 10 月，ARTEX 的作者在收到滥用报告后隐藏了原始仓库。这改变了谁在维护 ARTEX，没改变谁能用它。改名的镜像搜名字搜不到，就像改了品牌的控制台搜标题搜不到。

## 四、它们是怎么被用的

**Cairn：一个端点，一条接管路径。** ReliaQuest 追踪了一起由 Cairn 驱动的入侵——从单个暴露在外的 Spring Batch 端点一路走到服务器接管，数据以 1800 字节一块外传。攻击者自己的 Cairn 面板就架在攻击源 IP 上。

**Cairn：靠刷额度打政府。** VULONE 描述了一个跟中国有关、以牟利为目的的操作者，用 Cairn 在越南、台湾、印尼、印度的政府网络上跑了 66 个项目。操作者的提示词里有一条规则，强制 payload 只能用 ASCII；LLM 的账单则是靠刷 CodeBuddy 额度付的。

**ARTEX：爆发式请求、探测标记和被污染的日志。** 谷歌威胁情报团队看到 ARTEX 活动以 2 到 25 秒的间隔成串爆发，命令行里带 ArtexProbe 标记，还有 MySQL 日志投毒和 491 个 webhook.site 回调地址。GTIG 还点名了 ScopeWeaver 和一个"ARTEX PRO"变种。

**ARTEX：VAPOR PANDA。** CrowdStrike 报告 VAPOR PANDA 用 ARTEX 打 200 多家机构，操作指令用【人类指令】标签标记。这个行为体会专门找没装 EDR agent 的主机，拿到之后再部署 BLOODALCHEMY。

**ARTEX：Storm-0940。** 微软在 ConnectWise 供应链被攻破之后，把 Storm-0940 和 ARTEX 联系起来。ARTEX 驱动了对 2250 多个租户的登录尝试和 Microsoft Graph 侦察，在多起入侵里，从初次锁定目标到拿到云上高权限不超过三小时。另外一场针对八家机构的密码喷洒行动没有产生任何成功登录。

**猎人也成了猎物。** NorForge 记录了两个集群，AIA0009 和 AIA0010，劫持暴露在外的 Cairn 面板，偷走 API key 和 SSH key，还顺手部署了 Poseidon。敞开着的框架控制台，本身就是个目标。

## 五、狩猎指南

### 互联网暴露面

每个框架都不止一种特征能找。从弱到强依次是：标题 → 端口 → favicon → 证书 → 页面/模板代码。

下面这些默认指纹很好改，公开出来不损失什么；在意被找到的操作者早就改过了。它们是给还没开始找的防守方当起点的。

| 框架 | 起始指纹 | 说明 |
| --- | --- | --- |
| Cairn | Shodan `product:"Cairn"`；标题 `Cairn` 配合 `server: uvicorn` | 单看标题噪音很大，见下文 |
| ARTEX | 标题 `ARTEX — 自主渗透测试控制台` | 破折号（U+2014）很关键 |
| ARTEX | HTTP Basic auth realm `ARTEX`（`WWW-Authenticate` 头） | 与标题无关；控制台藏在 Basic auth 后面时只能靠它 |
| ARTEX | 标题 `ARTEX: Autonomous Penetration Testing Console`、`Agent Security Workbench` | 英文版、v2 |
| PentAGI | 证书签发者 CN `PentAGI CA` | 默认自签证书 |
| PentAGI | Favicon：Shodan `http.favicon.hash:-1596753120`，Netlas SHA-256 `2a620e3c5f7b49dfc6f5278352607f7931f8c38ef9d4689908af65538dd95366` | Shodan 用 MurmurHash3，Netlas 用 SHA-256 |
| 全部 | 默认端口：Cairn 8000、ARTEX 8787、PentAGI 8443 | 约三分之一的控制台跑在别的端口上 |

![Shodan 内置的 Cairn 产品过滤器](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Pbs14YDrdyUricLjoLeianrcTc3nUDHaZmtjzxHdCZbVzqvH6ss1aKhJ0ibVFeSGgxbxGiaHlM670JWiarXNBR3ciaPBniaMNb23wlxY/640?from=appmsg "Shodan 内置的 Cairn 产品过滤器")

*图：Shodan 内置的 Cairn 产品过滤器只匹配原始配置（来源：RST Cloud）*

![Shodan 上 ARTEX 默认标题的暴露主机](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Ps74tx8Hp4mXmS7NTZicVjhA3pooewFQlSkDQwEpAHwwUbdIEZ2qkqTvUsfk9licGRh8ttBiaf8ibtcIKIxCNvxicPl6Grgw0icD2iaE/640?from=appmsg "Shodan 上 ARTEX 默认标题的暴露主机")

*图：Shodan 上按 ARTEX 默认标题搜索，813 个暴露服务（2026 年 11 月 1 日）（来源：RST Cloud）*

![ARTEX v2 英文版控制台](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MQh6hsQkOyhJqf0ADRUKt8klPvcRibO5icMFy07JiaNk0enVztj3PxER1iaSEYxRdJMtINcgqCy9Tx33A6wewiaMoA73yfJPZRD7cs/640?from=appmsg "ARTEX v2 英文版控制台")

*图：英文版 "ARTEX v2 · Agent Security Workbench"，按默认标题搜索是搜不到的（来源：RST Cloud）*

![Netlas 上 PentAGI 的默认证书签发者](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Oxpe2Zfc22kjQy4llpLibwImyTLrIJgSerQOHhfqWfibbFRrorjMwciczU3J15noW8VKJhq9CKJjUrxTuC6ICQ6NLkeLcz4iagSRQ/640?from=appmsg "Netlas 上 PentAGI 的默认证书签发者")

*图：Netlas 上 PentAGI 的默认证书签发者，PentAGI 最强的单一指纹（来源：RST Cloud）*

![Netlas 上按 favicon 哈希定位的 PentAGI](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NcLWorPdbfTKezZ3TwrSAWiac3kgUEUOUqeQatntiamBAxAp6pVtJhy4hchWHV6Pvd793Acqq6FicDdFU9E8egwNib6HLOYBaiaV2Y/640?from=appmsg "Netlas 上按 favicon 哈希定位的 PentAGI")

*图：Netlas 上按 favicon 哈希找 PentAGI；favicon 常常没被索引，所以这个数是低估（来源：RST Cloud）*

真正耐用的指纹藏在页面代码里，我们故意不公开。这些字符串取自各框架的数据模型函数和特征明显的 UI 元素，fork 就算改了应用名也会继承。VulnFlow IoT、Zero 和 ScopeWeaver 就是靠它们翻出来的。把确切字符串印出来，等于直接告诉 fork 作者该改哪里。

RST Cloud 追踪暴露在外的 Cairn、ARTEX 和 PentAGI 控制台，包括改名版和 fork，通过 RST Threat Feed 交付给客户。

### 三个教训

**只看标题就是噪音。**`title:"Cairn"` 返回 407 台主机，只有 56 台是 Cairn，其余是度假民宿、一家登山公司、一家装修改造公司，还有 Amazon S3 上一个无关应用。做法是：先用互不相关的特征做召回，再用某个家族特有的标记做精确过滤，最后按 IP 去重。

**通用框架字符串是过滤器，不是指纹。** Next.js、Vite、Tailwind 的类名和内部结构出现在成千上万个无关应用里。只有在某个框架特有特征已经命中之后，才用它们来收窄结果。

| 变化形式 | 靠什么抓到 |
| --- | --- |
| 默认安装 | 标题或产品搜索 |
| 改了标题 | 正文或模板字符串 |
| 改了品牌的 fork（VulnFlow、ScopeWeaver、ARTEX v2） | 衍生版共享的框架代码 |
| 非标准端口 | 全端口定向扫描 |
| 自带证书 | 标题 / favicon 取并集 |

**fork 比改名更隐蔽。** 搜 Cairn 的模板代码，能翻出标题叫 VulnFlow IoT、WorkerAnt、Zero 和 cf作战平台的控制台，这些搜"Cairn"标题一个都找不到。其中一些（比如 VulnFlow IoT）其实是基于 Cairn 做的独立产品，不是改了名字的复制品。

![按模板代码翻出的 Cairn 衍生控制台](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PJf3ic3wqyACK3hbj1ianK8ct9iblsyVrWZrsUvia3ErV42IYRd8pyaB0Hf7Ikuumu8RS59juWNVqYRA7ia5Elx6GDiaHJ4VY1icBouA/640?from=appmsg "按模板代码翻出的 Cairn 衍生控制台")

*图：搜 Cairn 的模板代码，能翻出标题搜索漏掉的改名 fork（来源：RST Cloud）*

### 受害端遥测

静态标记最好查，也最好被 fork 删掉。行为不会随着模型、提示词和品牌一起变，所以要更看重行为。

静态标记（ARTEX）：

* 名为 `artex-probe-*` 的文件，名为 `ArtexProbe` 的账号。
* 命令行、云角色名和工作目录里出现 `artx` 或 `artex`（比如 `C:\ProgramData\artx5v\`）。
* 对轮换的 webhook.site URL 的回调，GTIG 数到 491 个。

行为特征：

* **机器节奏。** 命令或请求每隔几秒就到达一次，全天候，没有人类的停顿。ARTEX 的爆发间隔是 2 到 25 秒。
* **自我纠错的 payload。** 一串近乎相同的命令，每一条都在修正上一条的报错。人类很少这么快、这么干净地重试。
* **机器格式的输出。** 脚本打印竖线分隔的结果、明确的退出码或 banner，还有一边扔一边写、注释里还解释自己思路的一次性代码。
* **固定大小的外传。** 输出以统一大小分块离开（ReliaQuest 那个案子是约 1800 字节），常常用顺序命名的任务或带偏移量的文件。

云与身份：

* 一次新登录之后几分钟内出现 Microsoft Graph 枚举，以及大量账号上的成串失败登录（喷洒），哪怕一次都没成功。
* Graph 和登录日志里出现 `python-requests` 或 `Python-urllib` 的 User-Agent。
* 服务主体登录之后给自己授予角色。
* 成串的权限试算和部署校验调用，后面并没有真正的部署动作。

定向选择：

* 优先挑没有 EDR agent 的主机。

### 框架反被黑

Cairn 出厂就没有认证。NorForge 展示了接下来会发生什么：别的攻击者接管面板，偷走操作者的 LLM API key 和 SSH key，再把这套基础设施掉过头来打它的主人。如果你是合法拿这些工具做测试，把它们放在 VPN 或者带认证的反向代理后面，控制台端口永远别暴露。

## 六、互联网上是什么样子

### 暴露的控制台（2026 年 11 月 2 日）

| 框架 | 已验证主机 | 仅 Shodan | 仅 Netlas | 两者都有 |
| --- | --- | --- | --- | --- |
| Cairn | 56 | 25 | 16 | 15 |
| ARTEX | 834 | 754 | 28 | 52 |
| PentAGI | 459 | 242 | 59 | 158 |
| 合计（去重 IP） | 1,341 |  |  |  |

作为对比，单 Censys 一家就标出 1261 台带 ARTEX 软件标签的主机、506 个 PentAGI 控制台和 30 个 Cairn 控制台（2026 年 11 月 2 日），加起来接近 1800。我们没法和自己的数据去重，所以没算进总数。

### 部署在哪

| 框架 | 主要托管国家 | 默认端口占比 |
| --- | --- | --- |
| Cairn | 美国 21%、中国 14%、荷兰 12%、伊朗 7% | 95% 在 8000 |
| ARTEX | 美国 55%、中国 14%、中国香港 9%、日本 6% | 65% 在 8787 |
| PentAGI | 美国 43%、中国香港 11%、中国 11%、德国 7% | 69% 在 8443 |

托管集中度很高。大约 300 个 ARTEX 控制台（超过总数三分之一）挤在同一个网络（AS54600），还有大约 90 个 PentAGI 控制台在另一个（AS398823）。这两个段在 WHOIS 里都登记给 Cogent，但 Cogent 自己的网络并没有...