---
title: Node.js 的远程命令执行漏洞，不在你的业务代码里，在压缩库里
url: https://mp.weixin.qq.com/s/oZxv5QAZofxAE_kAAw7-bg
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:00:50.916230
---

# Node.js 的远程命令执行漏洞，不在你的业务代码里，在压缩库里

# Node.js 的远程命令执行漏洞，不在你的业务代码里，在压缩库里

原创

网络安全透视镜
网络安全透视镜

网络安全透视镜

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

QUOTE

这次出问题的地方，是几乎所有 Node.js 服务都会用到的 压缩库 。

—— CVE-2026-111497 事件观察

核心事实速览

| 项目 | 内容 |
| --- | --- |
| 漏洞编号 | CVE-2026-111497 |
| 缺陷类型 | Google Brotli 解码器越界写（内存破坏） |
| 评级口径 | Google CVSS v4.0 判 9.2 严重；Node.js 判高危；Red Hat 判 8.1 重要 |
| 报告方 | OpenAI Codex Security 的 Khai Tran 与 Sylvie Mayer |
| 修复方 | Matteo Collina 与 Antoine du Hamel |
| 披露日期 | 2026 年 10 月 21 日，同批修复 10 个漏洞 |
| 在野利用 | 截至 10 月 24 日无公开报告，CISA 于 10 月 23 日记为 none |
| 波及范围 | Node.js、Bun、Python Brotli 与 brotlicffi、Envoy、Istio、cdxgen |

2026 年 10 月 21 日，Node.js 项目发布了一次覆盖 22.x、24.x、26.x 三条受支持分支的安全更新，共修复 10 个漏洞。其中编号 CVE-2026-111497 被列为高危，官方公告写明：一旦应用解压了攻击者可控的 Brotli 数据，攻击者即可 破坏进程内存 ，进而导致崩溃、内存泄露或远程代码执行。

两天后，Imperva 威胁研究团队公开了名为 Node2Shell 的概念验证。在使用官方 Node.js 24.22.0 Linux arm64 镜像的新鲜容器中，研究人员 未借助调试器或定制编译 ，通过构造的 Brotli 数据让目标进程执行了随数据携带的代码。同样的输入在修复版 24.22.1 上被直接拒绝。

缺陷的影响范围不限于 Node.js。问题出在 Google Brotli 库的 C 代码 里，而各产品各自打包了一份副本，凡是复用这份解码器的软件——包括 Bun、Python 的 Brotli 与 brotlicffi 包、启用 Brotli 解压的 Envoy 与 Istio 代理，以及 cdxgen 的独立二进制——都被列入影响范围。

截至 10 月 24 日，公开渠道尚未出现该漏洞的 在野利用报告 。CISA 在 10 月 23 日的评估中把利用情况记为 none、自动化程度记为 no；Red Hat 则表示，目前没有可靠的公开 PoC 能复现代码执行。

Imperva 的测试有几处空白：只测了 24.22.0 这一个补丁版本，只测了 arm64 一种架构，路径也集中在 HTTP 两侧。为此我在自己的环境里用 Node.js 24.9.0 （x86\_64）独立复现了一遍，从 worker record 反序列化的方向打进，具体过程见第 04 章。需要先说明的是，这是 本地实验环境 中的验证，不构成在野利用的证据，也不改变厂商尚未公开 PoC 的现状。

本文看点

01

修复进入源码后的八个月

02

换一个版本和架构再复现

03

影响范围更大，扫描却可能漏掉

01

TIMELINE

### 从源码到发版：修复的八个月空窗

1.1 谁发现的，谁修的

Node.js 官方公告把报告方记为 OpenAI Codex Security 的 Khai Tran 与 Sylvie Mayer，把修复方记为维护者 Matteo Collina 与 Antoine du Hamel。上游 Google Brotli 在同一天发布了 1.0.10、1.1.1、1.2.1 三个版本，变更日志里只有一行 SECURITY 条目，写的就是这个编号。

公告同时点名了 20.x 及更早版本 已经结束生命周期，不会获得这次修复，这类部署只能迁移到受支持的分支。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPrWAialmKwzxAgvkA1DmG8WoJO6Wz8LumdF8vxO3Dlt7u4lYZlbXC55Ac4UIIyz2EjxHL4VHXecIuUQjJyNicyGNnJ5fRmofh0cg/640?wx_fmt=png&from=appmsg)

— Node.js 官方公告原文（截图）

1.2 修复进入源码后的八个月

这次事件里比较特殊的是时间差。据 The Hacker News 报道， 2026 年 2 月 27 日 关闭该缺陷的改动就已经进入 Brotli 的源码，但此后没有任何新版本携带它，直到 10 月 21 日 才随安全版本一同发布。OpenAI 对此的解释是：

REFERENCE

「was actually fixed in the Brotli source code in February, but it wasn't known at the time that it gave rise to a security vulnerability and there was no more recent release of Brotli.」

—— OpenAI

换句话说，修复代码当时就在源码里，但一直没有新版本把它带出去。从补丁进入源码到漏洞公开，中间将近八个月。

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPqQxR2A5fgLjGJia16Xa8nZ5Up8JCvMLs6WUmTvtagKQ6LS4tKB5vNP5ibjYbeyJmPHu2PzXcIPvp9eNOdvia0uicrxicQyCXytst0c/640?wx_fmt=png&from=appmsg)

— 从补丁入库到正式披露的关键节点（自制图）

1.3 同一个编号，三种评分口径

编号 CVE-2026-111497 的授权方是 Google， CVSS v4.0 打 9.2 判为严重；Node.js 官方把它定级为高危，但没有给出数值；Red Hat 给出的是 8.1 重要 。三套口径并列摆在这里，本身并不矛盾，但会直接影响各方推动修复的优先级排序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPrC51pfrThlrEUTTf8XtKSN8ucRUaiaO8Ikr6eUn6QLHF67HFWNqA9MOKTNQ8joKN1b2pZoXLCOF3Gr5aGIiakEHfdicHKweibk0ng/640?wx_fmt=png&from=appmsg)

— 三家厂商对同一漏洞的严重程度评分对比（自制图）

02

ROOT CAUSE

### 漏洞原理：被误判的「块切换」

2.1 八字节缓冲区上的越界写

按 Aikido 安全团队的定位，缺陷位于解码器的 DecodeBlockTypeAndLength() 函数。攻击者可以构造一个在单个块类型耗尽后要求切换 Huffman 树、但切换无法完成的 Brotli 流。旧版本解码器无法区分两种状态：

1

输入本身是格式非法的，应该直接终止；

2

流只是还没读完，解码器需要更多输入。

被误判成后者之后， 流式解码器持续向八字节的内部缓冲区追加数据 ，最终写过了缓冲区边界。问题出在状态机上：解码算法本身没有算错，是状态机在非法状态下继续推进了。修复版本改为返回 BROTLI\_DECODER\_ERROR\_FORMAT\_BLOCK\_SWITCH (-17) ，在安全路径与快速路径上同时停止解码。

2.2 两条可达路径，一个共享的原生解码器

一个 Node.js 服务可能在 HTTP 交互的任意一侧碰到 Brotli 数据：读取别人发来的压缩响应，或者解压别人发来的请求体。两条路径最终都通向 Node.js 自带的那份原生解码器，缺陷就在这个 共享路径 上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPr8Vicv1eVdZmAia4nQbsXXiaQFggwHhIQFD11PhMCOjDicj1GicpticicVNj81NBBfPd4n6l9DAqOsw82UKrEJj3yc8rUo2yPxrUBjyo/640?wx_fmt=png&from=appmsg)

— 两条路径汇入同一个解码器（Imperva 官方技术图）

响应侧比较好理解：Node.js 内置的 fetch() 读到带 Content-Encoding: br 的响应时会自动解码。请求侧需要中间件配合， Express 5 与 body-parser 2 的各类 body parser 在挂到路由上之后会解压 Brotli 请求体； 裸 Node.js HTTP 服务器不会自己解压 ，必须有中间件或显式调用。

2.3 客户端同样会中招

这个漏洞对客户端和服务器一视同仁。OpenAI 在披露中明确指出， 未打补丁的客户端也会被拿下 ，一个典型例子就是带 curl --compressed 的调用：

REFERENCE

「an unpatched server that accepts compressed input could be taken over by a malicious client, and an unpatched client that accepts compressed input (such as "curl --compressed") could be taken over by a malicious server.」

—— OpenAI

这段描述顺带解释了为什么只从 Accept-Encoding 里去掉 br 不算防护手段：客户端的声明只是建议，服务器可以无视它直接返回 Brotli。要在解码前主动拒绝 br 才有效。

03

PROOF OF CONCEPT

### Node2Shell：官方镜像上的代码执行

3.1 Imperva 的验证方法与结果

Imperva 的做法本身不复杂，值得注意的是它避开了容易被质疑的简化手段。团队在 全新拉起的官方容器 里运行官方 Node.js 24.22.0 镜像， 不用调试器、不用插桩二进制 ，测试应用里也没有任何创建标记文件的代码。收到构造的 Brotli 数据之后，标记文件出现了。

这一点比截图更有说服力：标记文件是 数据携带的代码自己创建的 ，不是研究者事先放进去的。相同的输入在 24.22.1 上被拒绝，没有产生标记，服务进程也保持运行。

| 攻击路径 | 实测版本 | 24.22.0 | 24.22.1 |
| --- | --- | --- | --- |
| 消费 HTTP 响应 | Node.js 内置 fetch() | 代码执行，生成标记 | 输入被拒绝 |
| 解析请求体 | Express 5.0.0–5.3.0 | raw() 与 json() 均执行 | 拒绝，服务未崩 |
| 解析请求体 | body-parser 2.0.0–2.3.0 | raw() 与 json() 均执行 | 拒绝，服务未崩 |

— Imperva 实测矩阵（整理自官方博客）

3.2 这次复现证明了什么，又没证明什么

Imperva 自己的表述比较克制： 并非每次尝试都成功 ，代码执行在其 Linux arm64 环境下需要多次尝试才能复现； 其他架构、22.x 与 26.x 分支都没测 ，Express 与 body-parser 也不是每个中间版本都逐一验证过。内存消毒器只用于解释成因，代码执行验证本身不需要它。概念验证至今未公开。这几处空白在第 04 章的本地复现中得到了部分补充。

3.3 与更早那个公开 PoC 的差别

10 月 22 日出现的首个公开 PoC 只能在 刻意削弱的测试构建 上达成代码执行；作者在标准构建上得到的是崩溃与有限的进程内存读取，并明确表示没能在正常构建上完成攻击。Imperva 的工作把证据推进到了 未经修改的官方构建 ，但覆盖面仍然止步于单一架构与一组中间件版本。

04

REPRODUCTION

### 自己动手：换一个版本和架构

4.1 为什么再做一次复现

Imperva 的验证留下了三处明确的空白：只测了 24.22.0 这一个补丁版本，只测了 arm64 一种架构，触发路径也限定在 HTTP 交互的请求体与响应两侧。这几个问题还是有意义的：漏洞影响多宽的版本区间、在哪些架构上成立、是否只能从 HTTP 侧进入，目前都还没有答案。

为补上这几处空白，我在自己的测试环境里用 Node.js 24.9.0 （x86\_64）做了一次独立复现。这个版本比官方修复版 24.22.1 早了好几个补丁号，也和 Imperva 测过的 24.22.0 不是同一个版本。走的也不是 HTTP 侧：工具的 profile 名称 node-24.9.0-worker-record-rce-bookworm-x86\_64 里的 worker-record 表明这次是从 worker record 反序列化的方向进入的。

4.2 复现过程

...bash

python poc.py --profile node-24.9.0-worker-record-rce-bookworm-x86\_64 \

　　--timeout 30 --callback-bind 0.0.0.0 \

　　--callback-host host.docker.internal

— 复现命令

几个参数值得说明： --profile 指定目标版本、架构与利用链， --timeout 30 是单次尝试的上限， --callback-bind 与 --callback-host 用来指定被测进程回连的通道，回连是判定利用成功的依据。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/m3tfzlbEQPr2u5ic8rszV3za1BJNFYYGJ6QlKicZL1MbjeQppUSAc2XxibHwSRRX5icbSRtQjS7GbuqYibibF5dxEl1JRIFsqXnIkiakJ1jFELNjDQ/640?wx_fmt=gif&from=appmsg)

GIF 动图 本地复现全过程：命令执行到 PASS 输出

这里的判定标准值得说明一下。输出里的 PASS: RCE verified by fresh id output 表示验证不是靠崩溃或者读出一段内存蒙混过去的，而是 确实执行了命令并回传了输出 。

4.3 输出里几个关键字段

terminal

PASS: RCE verified by fresh id output through the declared interface

profile=node-24.9.0-worker-record-rce-bookworm-x86\_64

callback\_peer=127.0.0.1

proof\_token=CVE111497\_e51cd5ac435b0ff028a676f10e0cb87a

proof\_command=id

proof\_stdout=uid=1000(node) gid=1000(node) groups=1000(node)

输出里有几个字段值得说明。 proof\_token 把这次验证与该 CVE 编号绑定， proof\_command 与 proof\_stdout 是一对——执行的命令是 id ，返回的 uid=1000(node) gid=1000(node) groups=1000(node) 说明代码确实在 以 node 用户身份运行的真实进程里 执行，不是沙箱或桩程序伪造的结果。回连对端是 127.0.0.1 ，属于容器内的本地通道。

4.4 补充了哪些信息，仍有哪些未覆盖

补上的部分有三处。版本上， 24.9.0 比修复版 24.22.1 早了多个补丁号，说明这不是最近几个补丁才出现的问题。架构上， x86\_64 补上了 arm64 之外的样本。路径上， worker record 这个方向说明进入点不止 HTTP 两侧。三处合起来看，这个现象不限于单个构建。

边界也需要说明：这次只覆盖了 一组版本、架构与路径的组合 ，其余版本、架构与利用链仍未验证；工具与 PoC 未公开；执行的代码拿到的是 uid 1000 的普通用户权限，不是 root ；也没有在 Bun、Python、Envoy、Istio 上重复这一过程。这是本地实验环境中的复现， 不构成任何在野利用的证据 。

05

BLAST RADIUS

### 影响面：从 Node.js 到 Python 与网格代理

5.1 受影响软件与修复版本

因为缺陷在共享的 C 代码里，而每个产品 各自捆绑一份副本 ，所以没有任何一次统一的升级能覆盖全部产品，必须逐个软件去更新自己那份。下面是 OpenAI 披露页与各厂商公告汇总的运行时与代理部分。

| 产品 | 受影响版本 | 修复版本 |
| --- | --- | --- |
| Google Brotli | 1.0.3 至 1.2.0 | 1.0.10 / 1.1.1 / 1.2.1 |
| Node.js | 22.x / 24.x / 26.x 修复前版本 | 22.23.4 / 24.22.1 / 26.12.1 |
| Node.js 20.x 及更早 | 全部版本 | 已 EOL，需迁移分支 |
| Bun | 1.4.3 及更早 | 1.4.4 |
| Envoy | 1.39.2 / 1.38.5 / 1.37.7 / 1.36.11 | 1.40.0 / 1.39.3 / 1.38.6 / 1.37.8 |
| Istio | 1.31.0–1.31.1 / 1.30.0–1.30.5 / 1.29.0–1.29.8 | 1.31.2 / 1.30.6 / 1.29.9 |

— 运行时与代理的受影响版本对照

5.2 语言绑定与工具链

| 产品 | 受影响版本 | 修复版本 |
| --- | --- | --- |
| Python Brotli | 1.2.0 及更早 | 1.2.1（PYSEC-2026-4322） |
| Python brotlicffi | 1.2.0.x | 1.2.1.0（PYSEC-2026-4323） |
| cdxgen | 13.4.0 / 12.8.8 及更早 | 13.5.0 / 12.8.9 |

— Py...