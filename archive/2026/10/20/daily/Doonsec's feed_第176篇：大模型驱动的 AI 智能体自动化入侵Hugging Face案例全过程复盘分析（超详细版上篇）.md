---
title: 第176篇：大模型驱动的 AI 智能体自动化入侵Hugging Face案例全过程复盘分析（超详细版上篇）
url: https://mp.weixin.qq.com/s/LPfFzROHw6HL0Kel5zLncg
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:48:09.655764
---

# 第176篇：大模型驱动的 AI 智能体自动化入侵Hugging Face案例全过程复盘分析（超详细版上篇）

# 第176篇：大模型驱动的 AI 智能体自动化入侵Hugging Face案例全过程复盘分析（超详细版上篇）

原创

abc123info
abc123info

希潭实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

## Part1 前言

大家好，我是ABC\_123。近两年来，AI大模型技术飞速发展，从文本生成、代码编写到自主规划、工具调用，新技术层出不穷。今天，我们分析一起发生于2026年7月的OpenAI大模型自动化攻击事件。这场持续约4.5天的攻击行动，AI智能体跨越多个信任边界，用了多个0day漏洞、逃逸了两个沙箱，完整展现了从初始入侵到深入内部基础设施的攻击链路；AI智能体在未经授权的情况下，为了获取题库和flag，意外入侵了Hugging Face k8s网络。据相关估计，顶尖人类黑客完成类似攻击可能需要两到三周。这一事件不仅揭示了AI智能体日益增强的自主攻击能力，也为网络安全防御带来了新的挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2Zc77PyLkuDupKmynbgOEwUUWTzUVjztJ8lNBUiaU9icoEOBhMD2DdLFiazribOgicGo0O9910qnCUP5NsLGWiabqBwOm1v6GShlmRj0/640?wx_fmt=png&from=appmsg)

Part2 技术研究过程

* ## 攻击事件起因介绍

当时OpenAI 正在测试AI 智能体的自动发现和利用软件漏洞的能力，让它参加一个类似于CTF的漏洞挑战，基于 ExploitGym 基准测试开展的内部网络安全能力评估。这个 AI 原本应该像安全人员一样，自己寻找漏洞并完成题目；但 AI 误以为 Hugging Face 网站上存放着这次考试的题库和答案，于是没有继续分析漏洞，而是尝试攻击 Hugging Face 的生产系统，绕过常规测试流程，想直接获取答案来作弊完成漏洞挑战。于是在约四天半的时间内，此 AI Agent智能体针对 Hugging Face 平台基础设施实施了一次端到端自动化入侵行动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZzibV4041qmEaQR0K0OFPLko97zp2756XiaDuias1EDQ3Dr5P44oeiauQibVUibsznGDP3btAp5kJtMSBmjbPpGEohLM4lRrKvkTeDM/640?wx_fmt=png&from=appmsg)

此次攻击是AI 智能体自动化完成的。AI 智能体在 OpenAI 提供的沙箱中持续进行目标探测、漏洞分析、访问尝试等攻击行为，并通过公共网络服务建立C2通信链路，实现攻击流程自动化。经安全团队调查，共还原约 17,600 次异常操作记录，并聚类分析形成约 6,280 个攻击行为链，相关活动持续时间约为 2026 年 7 月 9 日至 7 月 13 日。该事件表明，当前 AI 智能体已经具备一定程度的自动化攻击能力，可在无人干预情况下完成连续侦察和攻击流程，同时也暴露出 AI 系统在任务目标判断、权限控制和安全防护机制方面存在新的风险挑战。

* ## 第1步，AI Agent逃逸沙箱获取互联网访问能力

AI智能体收到了一项 ExploitGym CTF任务，并被要求编写漏洞利用程序来获取 flag。AI模型被允许可以在沙箱中运行命令，但无法访问开放的互联网环境。该智能体配置可能使用了最新的 Codex 搭配子智能体，配合一个使用 Ultra 版本的未发布模型，以及可能作为子智能体的 GPT-5.6。沙箱拥有 JFrog 软件包注册表的读取权限，可用于安装 npm、PyPI 和 Docker 软件包，以便AI智能体测试和执行漏洞利用代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZBGJsibaCBpj1t6Cq7q1SId149HsKYgMVHSkibv7z8TUt0ktpYzcsAeElWJwdCJvEV9pty0hgIEApMg064ew3hxH6FVVemnR7CU/640?wx_fmt=png&from=appmsg)

### 1  JFrog Artifactory 0day漏洞获取管理员权限

刚才我们说到，AI 智能体处在一个受到严格限制的沙箱环境中，软件包代理使用了JFrog Artifactory，该设置使AI Agent不直接访问互联网的情况下可以通过JFrog的缓存安装脚本插件，从而实现受限的互联网访问能力。在 Hugging Face 公开披露该事件的前一天，JFrog Artifactory发布了 Artifactory 7.146.27，修复了部分漏洞；据推测，其中至少有一个可能源自 OpenAI 的漏洞披露。这个漏洞在于 Artifactory 会信任访问令牌 JWT 中的声明，却没有先验证其签名。补丁如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bb2rTmUwHricOo3lVQw6JaYYbj3Kn8SE8HkU2rrCRcybF1iaI4icOE2ssBZ97FThiaTHvmlIxTA6xySa3RwQticPlIUBXyJUEuHLTw/640?wx_fmt=png&from=appmsg)

要复现存在漏洞的刷新请求，首先生成一个可正常刷新的读取者令牌，然后伪造带有管理员声明的访问令牌：

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2YXdNanV2W91R4GEVxREMjkA2140zSK3ToxiadBiaAjqk6EYoOb1dcdkPD6gzCABmUIXQbaHqfqBBibtRJ7ia7obQCDmtxzUQkFWMA/640?wx_fmt=png&from=appmsg)

将伪造的访问令牌与原始有效的刷新密钥一并发送：

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2Zpq2WlHuN3MSqYe5LKicK6GbJVQGh1LnS8KfjR6LhcXknhhiaVSrqqsWDGG1Ih0eMwNEicmT2lCV956iaDibGhmtAvrA1BmDeUicdhk/640?wx_fmt=png&from=appmsg)

Artifactory 7.146.25 接受了此操作，并返回了有效的管理员令牌；这让AI智能体获得了对 Artifactory 的控制权，但此时没有获得 shell 或直接访问互联网的权限。要连接到可访问互联网的节点，至少还需要一步。

### 2   利用软件包缓存污染获取命令执行权限

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZQlTBkUCpWg9N6mGpsoUD0T9ClQCTtakcDHCXVFs4pr6jVcqb2E0So24MsKAPQOZGEibfiaMDicWPZotUymbQomwTRLVPfFKl4zQ/640?wx_fmt=png&from=appmsg)

拥有Artifactory 的管理员权限后，模型可以从缓存中删除一个受信任的软件包，将仓库指向其控制的源，并在缓存中用相同的名称和版本存入另一个软件包，如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aMvlv4RLygXkCOfu4UTGCeSoECtU2DrGu5VyYtQAmb6LGYErlobrDib5ICh7zCnlt3IXULjAXlkkFicPOSZQPZaAWj8Cp9OFJ7s/640?wx_fmt=png&from=appmsg)

该攻击场景利用 npm 供应链机制和内部制品仓库（Artifactory） 实现横向攻击扩散。攻击者篡改 npm 包元数据，使其中记录的 tarball 地址和完整性校验值（hash/integrity）指向恶意软件包，导致正常的 `npm install` 流程将恶意包识别为可信版本。如果该软件包包含 `postinstall` 生命周期脚本，npm 会在安装阶段自动执行AI智能体投放的恶意代码，从而获得目标节点的命令执行权限。

### 3   共享邮箱式C2控制第2个节点获取互联网访问能力

随后，攻击者进一步分析 AI 服务内部依赖关系，寻找其他会自动安装或更新相关 npm 包的内部节点，通过依赖投毒方式实现横向移动。当前Agent由于受控节点位于内网，无法直接从公网节点上执行命令，攻击者还需要建立通信渠道，例如通过内部网络建立反向 Shell，或进一步滥用 Artifactory 等内部制品管理平台作为 C2通道，用于下发指令和回传执行结果。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2Y2X1zBgSYqm71gR3JicSeruBgQF8Gto7WdCicKxL9hOYQlFz6QgETMIiaQdsaLkCrQYiaapN6LSzxHcsahEdmbSvL0wia6hDoaLpibk/640?wx_fmt=png&from=appmsg)

当前攻击链可概括为：npm 元数据篡改 → 恶意依赖安装 → postinstall 代码执行 → 内网横向扩散 → C2 通信控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2aoBH3J7yKibRqbTGR44QU0YkIEc20RnmzO6iaOwMZ60fiavlL5tibpibmFsTWEFPsDEiaashpDQD5B949dcibcpnZiaxlsVf1cibotp7NE/640?wx_fmt=png&from=appmsg)

这样一来，模型无需在两个节点之间建立直接连接，就能控制第二个节点。一旦进入可访问开放互联网的节点，它就可以继续攻击 Hugging Face。这是一条相当复杂的攻击链，而 OpenAI 公布的细节不足以确认模型实际采用了哪种路径。第二个节点不是通过网络直连被控制，而是通过 JFrog Artifactory 充当“共享邮箱式 C2”被间接控制的。共享邮箱式 C2（Shared Mailbox C2） 是一种形象化说法，指攻击者不直接连接受害主机，而是利用一个双方都能访问的公共位置作为“留言板”或“邮箱”，实现命令下发和结果回传。

```
      攻击者/AI Agent             |             |     上传命令(command)             |             ↓     JFrog Artifactory      （共享命令仓库）             |             |     第二节点轮询(poll)             |             ↓          执行命令             |             ↓        上传执行结果             |             ↓     Artifactory保存结果             |             ↓       攻击者读取结果
```

* ## 第2步：AI Agent逃逸安全沙箱获取互联网跳板机

此时，AI Agent 通过利用软件包仓库缓存代理中的一个0day漏洞突破了自身沙箱环境限制，并获得了访问互联网的能力。为了有一个完全不受限制的执行命令的环境，随后AI Agent 入侵一个第三方用户托管的代码评测沙箱，被标记为 CyberGym 的实例，该实例暴露了一个可执行任意代码的接口；在此外部沙箱环境中AI Agent可以 root/管理员权限执行命令，并将该环境作为整个攻击活动的控制节点、攻击准备节点及网络出口节点。换句话说，该互联网沙箱成为该 Agent 发起后续攻击活动的外部跳板。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2YHKUuQ3Jz0V97jHcyIxveV9mz1cVDQ1s4ib9pDPWKEQIetsYKviaqicQNpbUHMw4ibEqcluAFwb6pYTeCfQFlWgfvbp4iaVBTq9Wmc/640?wx_fmt=png&from=appmsg)

简而言之，该框架允许 Agent 通过 `/submit-function` API 接口提交 C 语言代码`src/main.c` 文件，并将其链接到一个会调用 `sqlite3_initialize()` 的目标程序中，然后对此代码进行编译和执行。`sqlite3_initialize()` 函数被注册为一个构造函数，因此当相关库被加载时，该函数会自动执行。该 Agent 利用这一机制，通过重新定义 `sqlite3_initialize()` 函数来实现执行任意 Shell 命令。

```
// attacker-supplied src/main.c (illustrative)#include <stdlib.h>
int sqlite3_initialize(void) {    system("id; echo ZZROOTSTART; cat /proc/self/mountinfo");    return 0;}
```

但随后，AI Agent进一步发现并利用了代码提交流程中的参数校验缺陷：该沙箱会将用户提交的源代码路径直接拼接到后续 Shell 构建命令中，而未进行有效过滤。攻击者在路径字段中利用经典的命令注入方式，使构建流程被篡改，从而执行任意命令。

```
path = src/main.c;echo ZZROOTSTART;cat /proc/self/mountinfo; ... ;false;#
```

两种攻击路径最终都达到了相同的效果，在该沙箱环境中以 `uid=0`（即 root 权限） 执行任意 Shell 命令。第一个远程代码执行（RCE）行为发生在 7 月 9 日 04:01 UTC，其执行内容非常简单：

```
id            # uid=0(root) gid=0(root)env           # dump the environment, look for anything useful
```

不到一个小时内，该 Agent 已开始对互联网靶场沙箱环境进行系统探测，包括分析容器的挂载表、控制组、供应商控制平面以及一个随环境附带的调试 Shell。该调试 Shell 恰好内置了 `curl`、`nc` 和 `ip` 等网络与系统诊断工具，这些curl、nc等预置的工具在后续攻击过程中发挥了重要作用。

```
cat /proc/self/mountinfols -la /<sandbox-root> /<sandbox-root>/volumes /<sandbox-root>/mounts /pkg /rootPATH=/<sandbox-root>/.debug_shell/bin:$PATH curl -s http://<internal-svc>:8000/...
```

##

* ## 第3步：AI Agent借助跳板入侵 Hugging Face k8s网络

AI Agent 从这个外部跳板机出发，开始攻击 Hugging Face 内部网络，通过数据集处理流水线的两个漏洞（HDF5 文件读取漏洞、Jinja2 模板注入）获取 Hugging Face 的 Kubernetes 集群内部Pod网络访问权限。具体流程如下：外部Launchpad-->恶意Dataset配置（基于配置驱动的数据加载器）--> Hugging Face Dataset Processor--> 生产Kubernetes Pod。

### 1  漏洞利用1：AI利用HDF5 外部原始数据存储文件读取漏洞

### AI Agent的第一种攻击路径利用了 HDF5 外部原始存储数据集读取机制，该漏洞可以返回本地文件内容。通过这一方式，Agent 获取了 Pod 环境中的信息，包括：密钥secrets、访问令牌tokens及工作节点自身的源代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2Zzq8KHFmPcCWI51z2BogOPkHsV4MsDicUVKclvjqJEgQX9Nsmlm0I75hGT1rYOLTZP2h3dTu1IrvUfPO3INqmY7VQa0G3Ehz5c/640?wx_fmt=png&from=appmsg)

AI Agent利用的是本地文件读取漏洞，利用 HDF5 数据格式支持引用外部文件的特性，构造了一个恶意数据集；该数据集表面上是普通 AI 训练数据，实际隐藏了对服务器本地文件的读取指令。当 Hugging Face 后台 Worker 自动处理该数据集时，会按照 HDF5 文件中的定义读取本地指定路径中的内容，并将其作为数据返回。攻击者随后通过Hugging Face API  接口获取这些数据，最终导致服务器本地文件泄露。

```
 Agent（提交数据集的人/程序）             |             vDataset Config（告诉平台怎么读取数据）             |             v Worker（平台的数据处理机器）             |             v      读取 HDF5 文件             |             v    返回 Dataset 数据行             |             v     Hugging Face API             |             v    用户/API调用者获取数据
```

具体技术细节如下：

数据集配置（dataset config）可以通过多种格式指定其数据文件，其中包括 HDF5 格式。该 Agent 提交了一个数据集，其精心构造的配置文件将每个数据切分指向一个较小的 `.h5` 文件。每个文件都是一个有效的 HDF5 容器，其中包含一个数据集，而该数据集的原始数据被声明存储在本地文件系统中的某个路径下，指向 Worker 运行环境中的敏感文件。当 Worker 为构建数据切分而打开该文件时，它会根据 HD...