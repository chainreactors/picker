---
title: 从公告到入侵不足十小时：Marimo Python Notebook 预授权 RCE 事件研判
url: https://mp.weixin.qq.com/s/Z61tvmg8WaRkL2h3m60eUA
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:45:37.076980
---

# 从公告到入侵不足十小时：Marimo Python Notebook 预授权 RCE 事件研判

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAgyHu4JqKsnOTKbRasxQYX7mDBYT1612PGQXVYWiaxTK2ia1l9Fg1F1HkMQ6p13p0K6icBDhWQdOqToibmqBYdGkAa8crgFQLG14hs/0?wx_fmt=jpeg)

# 从公告到入侵不足十小时：Marimo Python Notebook 预授权 RCE 事件研判

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAia4pLGG3Go2n1D8IkicYqfCFu6Cx51mZuGptqjib825hEczcEPKw7Tj5lAuHUEB5QkdATvrcl1yqNibfbvLbJIGMC1n0wRzCHPeec/640?wx_fmt=png&from=appmsg)

**成稿时间：** 2026年4月11日
**分析原型：** 威胁通告型 · 兼事件溯源型
**置信度总体评级：** 高（核心事实多源交叉验证，含一手公告、厂商蜜罐数据及独立安全研究机构）

## 长话短说

2026年4月8日21:50（UTC），Marimo 开源 Python Notebook 的维护团队发布了安全公告 GHSA-2679-6mx9-h9xc，披露了一枚 CVSS v4.0 评分 9.3 的关键预授权远程代码执行（RCE，Remote Code Execution）漏洞，编号正式确认为 **CVE-2026-39987**。

**核心结论：**

1. **攻击门槛极低。** 该漏洞不需要任何凭证、令牌或社会工程，一条 WebSocket 连接即可获得目标主机的完整交互式 root shell。
2. **武器化速度创新低。** 公告发布后仅 **9小时41分钟**，Sysdig 威胁研究团队（TRT）的蜜罐节点即记录到首次在野利用；从初始访问到完成凭证窃取的完整操作，耗时不足三分钟。期间无任何公开概念验证（PoC）代码存在。
3. **目标不分大小。** Marimo 拥有约两万 GitHub Stars，远不及 Langflow（14.5万）或 n8n（7.5万）的量级，但攻击者依然在数小时内完成了武器化。这意味着威胁行为者正在**广谱监控**漏洞公告源，而非只盯头部目标。
4. **CVE 缺位无法作为防护借口。** 公告发布时尚未分配 CVE 编号，依赖 CVE 扫描的防御体系对此类情况完全失效。
5. **立即行动项：** 将 Marimo 升级至 0.23.0 或以上版本；所有曾公开暴露实例的环境变量、AWS 密钥、API 令牌须视为已泄露并立即轮换。

## 一、漏洞机制：一个被遗漏的鉴权调用

### 1.1 项目背景

Marimo 是 Jupyter 的新一代替代品，以「响应式执行」为设计核心——改变一个单元格的输出，其他依赖它的单元格会自动重新运行。它将 Notebook 存储为纯 Python 文件，并可将其部署为可交互的 Web 应用，使用 Starlette 框架构建后端服务，默认监听 2718 端口。其协作功能设计本身鼓励将编辑模式的服务端暴露于网络，这在安全上构成了结构性风险——Notebook 环境往往存储着数据库连接串、云凭据、API Key 等高价值数据。

截至漏洞公告发布时，Marimo 在 GitHub 上有约两万颗 Stars，活跃于数据科学和研究领域社区。

### 1.2 技术根因

漏洞位于 `marimo/_server/api/endpoints/terminal.py` 第340至356行。应用内置一个基于 WebSocket 的终端功能（`/terminal/ws`），允许用户在浏览器中直接操作 PTY（伪终端）Shell。

以下是受影响端点的核心逻辑（依据官方公告）：

```
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    app_state = AppState(websocket)
    if app_state.mode != SessionMode.EDIT:
        await websocket.close(...)
        return
    if not supports_terminal():
        await websocket.close(...)
        return
    # 此处完全没有认证检查
    await websocket.accept()
    # ...
    child_pid, fd = pty.fork()  # 直接创建 PTY Shell
```

问题在于：当 WebSocket 连接建立时，代码只检查当前运行模式和平台是否支持终端功能，随即调用 `websocket.accept()` 并执行 `pty.fork()` 创建子进程——整个流程中，没有任何鉴权调用。

对比同一应用中正确实现认证的 `/ws` 端点（`ws_endpoint.py`）：

```
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    app_state = AppState(websocket)
    validator = WebSocketConnectionValidator(websocket, app_state)
    if not await validator.validate_auth():  # 正确的认证检查
        return
```

两个端点的差异一目了然：`/ws` 调用了 `validate_auth()`，`/terminal/ws` 没有。一个守门，一个洞开，漏洞由此产生。

Marimo 使用 Starlette 的 `AuthenticationMiddleware`，但该中间件对未认证的 WebSocket 连接只会标记 `UnauthenticatedUser` 状态，并不主动断开连接。实际的鉴权拦截依赖各端点通过 `@requires()` 装饰器或 `validate_auth()` 显式调用来实现——`/terminal/ws` 两者都没有，使中间件的防护形同虚设。这意味着**即使整个 Marimo 实例已启用认证，该端点依然对所有人开放**。

据 Endor Labs 的独立分析，Marimo 在默认 Docker 部署配置下，进程以 root 权限运行——攻击者获得的不只是普通用户 Shell，而是容器内的完整 root 权限。

### 1.3 攻击链

完整攻击链仅需以下步骤，没有需要构造的复杂 Payload，没有竞争条件，没有任何技术门槛：

| 步骤 | 动作 | 说明 |
| --- | --- | --- |
| 1 | 向 `ws://TARGET:2718/terminal/ws` 发起 WebSocket 连接 | 无需任何认证令牌 |
| 2 | 服务端 `websocket.accept()` 直接接受连接 | 跳过所有认证逻辑 |
| 3 | `pty.fork()` 创建 PTY 子进程 | 生成交互式 Shell |
| 4 | 攻击者获得持续性交互终端 | 可实时键入命令、查看输出，体验与 SSH 无异 |
| 5 | 默认 Docker 部署以 root 运行 | 权限最大化 |

### 1.4 漏洞基本信息

| 字段 | 内容 |
| --- | --- |
| CVE 编号 | CVE-2026-39987 |
| GitHub 公告 | GHSA-2679-6mx9-h9xc |
| CVSS v4.0 评分 | 9.3（Critical） |
| CWE 类型 | CWE-306（关键功能缺失鉴权） |
| 受影响版本 | Marimo ≤ 0.20.4 |
| 修复版本 | Marimo 0.23.0（PR #9098） |
| 修复 Commit | `c24d4806398f30be6b12acd6c60d1d7c68cfd12a` |
| 公告发布时间 | 2026-04-08 21:50 UTC |
| 漏洞报告者 | GitHub 用户 @q1uf6ng |
| 首次在野利用 | 2026-04-09 07:31 UTC |

修复方案是在 `/terminal/ws` 端点中添加与 `/ws` 端点一致的认证验证逻辑。Marimo 官方同时建议将终端功能改为显式启用，而非默认开启。

## 二、攻击时间线

以下时间线基于 Sysdig TRT 蜜罐节点记录与 GitHub 官方公告交叉验证，所有时间均为 UTC。Sysdig TRT 在 GCP europe-west1-b 区域等多个云厂商节点部署了运行漏洞版本 Marimo 的蜜罐实例，记录了全部四次攻击会话。

| 时间（UTC） | 事件 |
| --- | --- |
| 04-08 21:50 | 官方安全公告 GHSA-2679-6mx9-h9xc 在 GitHub 发布 |
| 04-08 ～22:xx | Sysdig TRT 在多家云服务商部署运行漏洞版本的蜜罐节点 |
| 04-09 07:31 | 来自 IP 49.207.56.74 的首次利用请求抵达蜜罐（攻击窗口：9小时41分钟） |
| 04-09 07:33 | 攻击者重新连接，开始手动文件系统侦察 |
| 04-09 07:43 | 攻击者发起凭证收割，成功读取 `.env` 文件 |
| 04-09 07:45 | 攻击者执行 `exit` 退出，第一轮操作完成（从建立 shell 到完成凭证窃取不足3分钟） |
| 04-09 08:57 | 攻击者二次回访，重新运行 PoC 验证脚本并再次读取 `.env` |
| 04-09 09:04 | 第二轮会话结束 |
| 04-10 | The Hacker News 等权威垂直媒体跟进报道 |

---

## 三、在野攻击行为还原

### 阶段一：PoC 验证（07:31 UTC，持续约9秒）

攻击者连接蜜罐的 `/terminal/ws` 端点后，立即执行了一组带有结构性标记的验证命令：

```
echo '---POC-START---'
id
echo '---POC-END---'
```

`---POC-START---` 和 `---POC-END---` 这类定界符是自动化脚本的典型特征——攻击者在用脚本确认代码执行成功后，才会决定是否投入人工时间做后续手工操作。整个会话持续9秒，随即断开。

### 阶段二：手动侦察（07:33 UTC）

两分钟后攻击者重连，开始手工探索文件系统：依次执行 `pwd`、`whoami`、`ls`，确认所处目录为 `/app/marimo`，目录中包含 `logs`、`data`、`.env`、`docker-compose.yml` 等文件。随后尝试 `cd ../`、`cd logs`、`cd ~/.ssh` 等目录遍历，并运行了 `ipaddr`（应为 `ip addr` 的误输入）来枚举网络接口。

操作节奏和误输入表明这是人工操作，而非进一步的自动化脚本驱动。

### 阶段三：凭证窃取（07:43 UTC，耗时不足3分钟）

这是整个操作中效率最高的一节。攻击者重连后直接定向 `cat .env`，蜜罐返回了预置的仿真凭据：

```
AWS_DEFAULT_REGION=us-east-1
AWS_ACCESS_KEY_ID=AKIA01FB...
```

随后攻击者按顺序读取目录中的每一个文件——`data`、`docker-compose.yml`、`celerybeat-schedule`、`marimo`、`logs`——并专门搜索 SSH 密钥（`ls ~/.ssh`）。07:45 UTC，攻击者执行 `exit` 主动退出。

在真实生产环境中，`.env` 文件通常包含数据库连接字符串、云服务商密钥、第三方 API 令牌。据 Endor Labs 分析，Notebook 类工具的部署环境往往还与 AI/ML 编排平台、LLM 前端、内部代码仓库共处同一主机——一次成功的 shell 访问，可能意味着对整个宿主机攻击面的敞开。

### 阶段四：确认回访（08:57 UTC）

约70分钟后，攻击者第四次返回，重新执行 PoC 验证脚本并再次读取 `.env`，还执行了 `history` 命令——这一细节**研判**说明攻击者在核查是否有其他竞争者已经访问过同一目标，与人工操作的「检查工作列表、确认战果」习惯一致。

## 四、攻击者侧写

从上述行为模式可以形成以下初步侧写：

**已验证特征（L1）：**

* 攻击者使用了带定界符的结构化 PoC 脚本，说明有一定的工程化程度
* 攻击者在约90分钟内发起了四次独立会话，会话间存在有序停顿
* 攻击目标高度聚焦：优先寻找 `.env` 文件和 SSH 密钥，未尝试安装持久化机制或挖矿程序

**研判（L2）：**

* 攻击模式为「脚本化 PoC + 人工跟进」——PoC 生成阶段可能有工具辅助（含 AI 辅助），后渗透阶段转为人工操作。论据：PoC 的结构化标记字符串与后续阶段的命令误输入、逐步探索之间存在明显的行为差异，指向混合模式而非全自动扫描器。
* 攻击者当前证据不足以将其归因至任何已知 APT 组织或犯罪团伙，亦无证据表明此次攻击是某个大规模扫描行动的组成部分。初步判断为个人或小型团队，具备基本的漏洞武器化能力和云凭据变现意识。

**待证实（L3）：**

* 源 IP 49.207.56.74 地理位置标注为印度，但该 IP 可能是 VPN 出口节点或代理层，Sysdig TRT 原文明确指出此点，**不宜直接用于归因**。
* 攻击者在非蜜罐环境中采集的凭据是否已被用于后续攻击（如横向访问 AWS 账户），目前尚无公开信息确认。蜜罐返回的是虚假凭据，因此无法从该维度观测后续行为。

## 五、武器化速度的结构性根因

这一事件的核心价值不仅在于漏洞本身，更在于它揭示了一个持续加速的趋势。

Zero Day Clock 项目对83,000余枚 CVE 的统计数据显示：2018年，漏洞从披露到被利用的中位时间为771天；到2023年，已有44%的被利用漏洞在披露后24小时内完成武器化。VulnCheck 发布的《2026年漏洞利用态势》报告则指出，**2025年，已知被利用漏洞中有28.96%在 CVE 公开当天或之前就已被武器化**，这一数字较2024年的23.6%进一步上升。

Marimo 的案例将这一趋势推进了一步：**无 PoC、无 CVE 编号、目标知名度低——三重「保护因素」同时失效，武器化时间压缩至不足10小时。** 背后有几个结构性原因：

**公告本身即武器化说明书。** GHSA-2679-6mx9-h9xc 明确写明了受影响的端点路径（`/terminal/ws`）、缺失鉴权的代码位置，以及完整的 PoC Python 脚本。安全公告设计上是为防御者准备的，但在攻击者眼中，这份文档的价值等同于一份带注释的入侵教程。事实上，该漏洞本身极为简单，PoC 代码的核心逻辑不超过十行 Python——即使没有 AI 辅助，一个有经验的 Web 安全研究员也可以在30分钟内手写出可用的攻击工具。

**WebSocket 终端提供的是持久交互访问，而非一次性命令注入。** 传统 RCE 漏洞每次执行一条命令需要重新构造 Payload；WebSocket 终端是一个持续的双向通道，攻击者操作体验接近 SSH 远程登录，可以实时看到输出、实时调整命令。这显著降低了后渗透阶段的复杂度，将凭证窃取的时间压缩到了不足三分钟。

**Notebook 类工具是天然的凭证聚合点。** 数据科学和 ML 工程师的工作流天然涉及数据库连接串、云厂商密钥、API 令牌，这些信息往往以明文形式存在于 `.env` 或配置文件中。此外，此类工具经常由研究团队在常规安全审查流程之外独立部署，且往往配置了宽泛的云账户权限。

## 六、与近期同类事件的横向对比

| 漏洞 | 目标规模（GitHub Stars） | 公告到首次在野利用 | 是否有公开 PoC |
| --- | --- | --- | --- |
| CVE-2026-33017（Langflow） | ～145,000 | ～20小时 | 否 |
| **CVE-2026-39987（Marimo）** | **～20,000** | **9小时41分钟** | **无** |

Langflow 案例此前已被安全社区广泛关注，彼时的「20小时」已被认为是高风险信号。Marimo 以不到一半的时间完成了相同的武器化路径，且目标知名度仅为 Langflow 的约七分之一。

**研判（L2）：** 这一数据背离了「知名度越高、越早被攻击」的传统认知，指向一个更具威胁性的现实：攻击者的监控范围已全面覆盖漏洞公告订阅源，而非仅盯高知名度目标。Sysdig TRT 提出，AI 辅助漏洞分析的角色正在这一加速趋势中扮演重要角色，攻击者可能正在使用 AI 工具解析安全公告、自动构建可用漏洞利用程序。该判断目前属于合理推断，尚无直接技术证据（如工具指纹、错误输出特征）证实。

这一案例对防御方最深远的启示并非「赶快打补丁」——那是已经显而易见的操作——而是**「依赖 CVE 驱动的漏洞管理流程已不足以应对当前威胁节奏」**。CVE-2026-39987 在被积极利用时尚未在 NVD 入库，依赖 CVE 扫描的安全工具对此次事件全程静默。

## 七、防御建议（可操作）

**立即行动（24小时内完成）：**

1. **将 Marimo 升级至 0.23.0 或以上版本**（`pip install --upgrade marimo`）。补丁通过 PR #9098 合并，核心变更是在 `/terminal/ws` 端点加入与 `/ws` 一致的 `validate_auth()` 调用。
2. **视所有曾公开暴露的 Marimo 实例的凭证为已泄露**，立即轮换以下内容——不论是否有明确的被攻击证据：AWS / GCP / Azure 访问密钥、数据库密码、第三方 API 令牌、SSH 私钥、`.env` 文件中的所有敏感变量。
3. 检查 `/terminal/ws` 的访问日志，寻找非预期的 WebSocket 连接来源。合法使用场景应仅...