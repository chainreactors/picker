---
title: OpenClaw 近期安全漏洞修复汇总报告
url: https://mp.weixin.qq.com/s/4TcTXcWzqB0owLgQ9QiwRA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:28:53.619544
---

# OpenClaw 近期安全漏洞修复汇总报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jHUbrwW0VwWKTJSX6TiaIUqmvYAVt9919R6gfvUFWojia1ra0icjb0iaK4MicLOFs4yMH3T1lUpmhBeFEyLmTicZjqcVgfccGicO2WCibQXBSRapQibU/0?wx_fmt=jpeg)

# OpenClaw 近期安全漏洞修复汇总报告

腾讯安全威胁情报中心

![]()

在小说阅读器中沉浸阅读

近日，腾讯安全科恩实验室针对热门开源 AI 智能体框架 OpenClaw 的安全性进行了专项分析。根据对该项目 GitHub 仓库近期提交（Commit）记录及版本迭代信息的深度回溯，我们发现其在 2026.3.22 之前的版本中存在多项涉及插件执行、权限提升及鉴权绕过的系统性安全缺陷。
需要特别说明的是，目前所有已发现的风险点均已在官方最新版本 2026.3.24 中得到完整修复。本次披露的信息并非 0day 漏洞，而是基于社区已公开代码变更的追溯性审计结果。由于 OpenClaw 在国内开发者及 AI 自动化领域的普及度极高，为防止旧版本用户遭受供应链攻击或远程提权风险，我们整理了本篇报告，旨在为用户提供清晰的漏洞原理说明及切实可行的加固指引。

分析对象：OpenClaw `2026.3.22 beta.1` / `2026.3.22` / `2026.3.23` / `2026.3.24`

**整体风险等级**：**严重**，含多项可被远程利用的鉴权绕过与代码执行路径

**推荐行动**：立即升级至 `2026.3.24` 或更高版本

---

## 01 漏洞概览

![图片](https://mmecoa.qpic.cn/mmecoa_png/4EHqib0vXQFicbKOlA1YVIUw2P030RjUFD3ibxBQLLsX50nsdU7HEvX5TbqtSnfly0k3GAtyQAWw3bStBQeeeGT8yBjS3ib0U4YM59F21CLic60M/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=0)

**总结**：攻击者可通过克隆含恶意插件的仓库、伪造 WebSocket 权限声明、重放设备配对码或匿名访问 Canvas 路由等方式，在未修复版本上实现权限提升乃至代码执行。

---

## 02 风险主线速览

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/4EHqib0vXQFibRzILaI9byC4GV4CsKjkAUlMNIibR2p3WxedpCicUACHsa0lkSBap9oXZo7IBGvOg5Maq8GwTYBejFTbj3JvW2QNPQvsiaKmqkE4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=1)

---

## 03 普通用户安全防护建议

### 立即行动

**将 OpenClaw 升级至 `2026.3.24` 或更高版本。**

* 如果你使用的是桌面客户端，打开应用后检查"关于"页面的版本号，低于 `2026.3.24` 即需更新。
* 如果你是自托管部署，拉取最新镜像或包后重启服务。

### 我是否受影响？

根据你的使用场景自查：

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/4EHqib0vXQF8A4pia76WNBRVAgxcfTQ5TMOzE77LvuQ7ysuzT00nhXK4GrSGPkwGYO9ibtQVMfHc8f1pIyFEWNupt23ntQe9NegvZRugQv8t7E/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=2)

### 临时缓解措施（无法立即升级时）

如果你暂时无法升级，可采取以下措施降低风险：

1. **禁用工作区插件自动发现**：在设置中关闭"自动加载工作区插件"选项，避免克隆仓库时隐式执行插件。
2. **不要打开来源不明的工作区**：在升级前，避免克隆或打开陌生人分享的 OpenClaw 工作区。
3. **限制 Gateway 端口访问**：如果你是自托管用户，通过防火墙规则将 Gateway 端口限制为仅内网可访问，避免 Canvas 路由被公网匿名访问。
4. **停用 Webhook 集成**：如果你使用了 Webhook 集成，在升级前可临时停用，以避免 pre-auth 请求被解析。
5. **不要分享 setup code**：在升级前，避免生成或分享设备配对码，防止被重放利用。

### 自托管用户特别提示

* **网络隔离**：建议将 OpenClaw Gateway 部署在内网，通过反向代理（如 Nginx）统一处理外部流量，并在代理层添加访问控制。
* **日志审计**：检查 Gateway 访问日志，关注来自非预期 IP 的 Canvas 路由请求（`/canvas/`）和异常的 WebSocket 连接。
* **定期更新**：OpenClaw 安全修复频率较高，建议订阅官方 Release 通知，保持版本在最新稳定版的一个小版本内。

---

## 04 漏洞技术分析

以下选取部分严重和高危漏洞进行分析：

### 4.1 插件供应链执行：克隆仓库即运行恶意代码

**风险等级**：严重

**影响版本**：version <= `2026.3.13`

**攻击场景**：攻击者在公开 Git 仓库中放置一个包含恶意插件的 OpenClaw 工作区。受害者克隆该仓库后，旧版本 OpenClaw 会自动发现并加载工作区内的插件，无需用户任何确认操作，恶意代码即在受害者机器上执行。

**技术根因**（`src/plugins/config-state.ts`）

漏洞前态（`2026.3.13`）：非 bundled 插件在没有显式 allow/deny 时，直接返回启用状态，工作区来源插件具备"被发现即启用"的风险。

修复后（`2026.3.22-beta.1`）：workspace origin 被单独拉出来做 deny-by-default，只有显式允许或明确启用时才会装载执行。

**修复效果**：工作区插件从"默认启用"改为"默认禁用"，彻底切断"克隆即执行"的攻击链。

---

### 4.2 WebSocket 权限提升：共享 Token 自声明 Scope

**风险等级**：严重

**影响版本**：version <= `2026.3.13`

**攻击场景**：攻击者持有一个低权限的共享 token，在建立 WebSocket 连接时，在连接参数中自行声明 `operator` 级别的 scope。旧版本在 `sharedAuthOk` 为真时不会清除这些自声明的 scope，攻击者因此获得超出其实际权限的操作能力。

**技术根因**（`src/gateway/server/ws-connection/message-handler.ts`）

漏洞前态：只要 `sharedAuthOk` 为真，客户端自声明的 scopes 就可能被保留，`clearUnboundScopes` 函数在此条件下不执行清除。

修复后：scope 保留变成显式 allow path——`clearUnboundScopes` 无条件清空 scopes，仅在设备身份明确且鉴权决策为 allow 时才通过独立条件分支保留，无设备身份时一律清除。

**修复效果**：在无设备身份场景下，scope 保留变成显式 allow path，而不是 shared auth 默认保留。

---

### 4.3 Setup Code 重放与权限放大

**风险等级**：严重

**影响版本**：version <= `2026.3.13`

**攻击场景**：攻击者截获或猜测到一个设备配对 setup code，在审批完成前多次重放该 code，并在重放时声明比原始签发时更高的 role/scope，从而获得超出预期的设备权限。旧版本的 setup code 可被多次消费，且不校验 role/scope 是否与签发时一致。

**技术根因**（`src/infra/device-bootstrap.ts`）

修复后（`2026.3.22-beta.1`）引入了两层保护：将兑换时请求的 role/scope profile 与签发时持久化的 profile 做严格比对，不一致则直接拒绝；校验通过后在返回成功前立即删除 token 记录，确保一次性消费。

**修复效果**：

* **权限绑定**：兑换时必须与签发时的 role/scope profile 完全一致，无法在兑换时升级权限。
* **一次性消费**：成功前即删除记录，阻止重放与审批前放权。

---

### 4.4 Shell Wrapper Allowlist 绕过

**风险等级**：高危

**影响版本**：version <= `2026.3.22`

**攻击场景**：攻击者构造一个包含 `$0` 引用的 shell 命令，使其通过 exec approvals 的 allowlist 检查，但实际执行时携带额外的 shell 操作（如管道、eval、换行拆分的 exec）。旧版本的正则匹配过于宽松，无法区分合法的 positional carrier 与混杂恶意操作的 payload。

**技术根因**（`src/infra/exec-approvals-allowlist.ts`）

漏洞前态（`2026.3.22`）：仅用宽松正则检查命令中是否包含 `$0`，无法可靠区分真正的 direct carrier 与混杂恶意操作的 payload。

修复后（`2026.3.23`）：引入严格的 `isDirectShellPositionalCarrierInvocation` 函数，通过精确的正则模式只允许形如 `$0 $@`、`exec -- $0 $@` 的标准 positional carrier 形式命中 allowlist 绑定，其余形式一律拒绝。

**修复效果**：拒绝 single-quoted 的 `$0`/`$n` carrier 形式和换行拆分的 `exec` carrier，只接受合法的 `exec --` carrier 形式。

---

### 4.5 Canvas 匿名访问与非管理员 Session Reset

**风险等级**：高危

**影响版本**：version <= `2026.3.22`

**攻击场景 A（Canvas 匿名访问）**：攻击者通过本地回环地址或直连方式访问 Canvas 路由，旧版本将本地直连请求视为可信并直接放行，无需任何认证凭据。

**攻击场景 B（非管理员 Session Reset）**：持有较低写权限的调用者发送 session reset/new 命令，旧版本不检查调用者是否具备 `operator.admin` scope，导致任意低权限用户可重置他人会话。

**技术根因**（`src/gateway/server/http-auth.ts` 和 `src/gateway/server-methods/agent.ts`）

Canvas 路由漏洞前态：`isLocalDirectRequest` 判断为本地直连时直接返回放行结果，绕过所有鉴权逻辑。

修复后：删除"本地直连即放行"捷径，所有 Canvas 请求统一进入 bearer token / capability 鉴权链，路径格式异常时直接返回未授权。

Session Reset 修复后：新增 `resolveCanResetSessionFromClient` 函数，将 reset/new 权限收归为仅 owner（即持有 `operator.admin` scope 的调用者）可执行，并在命令处理路径中强制校验，权限不足时返回明确的缺少 `operator.admin` scope 错误。

**修复效果**：Canvas 路由必须经过完整鉴权链；session reset/new 被收归为 owner 专属操作，非 `operator.admin` 调用者会收到明确的权限不足错误。

---

### 4.6 沙箱媒体路径逃逸：`mediaUrl`/`fileUrl` 别名绕过

**风险等级**：高危

**影响版本**：version <= `2026.3.23`

**攻击场景**：OpenClaw 对出站工具和消息动作中的媒体访问路径设有媒体根目录（media-root）限制，以防止代理访问沙箱外的本地文件。旧版本在校验路径时仅检查 `url` 字段，而出站动作同时支持 `mediaUrl` 和 `fileUrl` 作为别名字段。攻击者通过在出站工具调用或消息动作中使用 `mediaUrl`/`fileUrl` 字段替代 `url` 字段，可绕过媒体根目录限制，访问沙箱外的任意本地文件路径，实现沙箱逃逸。

**技术根因**（`src/media/dispatch.ts`）

漏洞前态：路径校验仅覆盖 `url` 字段，`mediaUrl` 和 `fileUrl` 别名字段未经媒体根目录检查即被直接使用，攻击者可通过别名字段绕过限制。

修复后（`2026.3.24`）：先将三个字段按优先级合并为最终路径，再统一执行媒体根目录校验，消除别名绕过路径。

**修复效果**：出站工具和消息动作中的所有媒体路径别名均受媒体根目录限制约束，`workspaceOnly` 模式下的沙箱代理无法通过别名字段访问沙箱外文件。

---

### 4.7 其他修复摘要

**Webhook 前置鉴权缺失（高危）**：Webhook 入口在旧版本中先读取并解析请求体，再校验签名，导致未鉴权请求也能触发 body 解析，形成 pre-auth 慢请求 DoS 面。修复后，所有 Webhook 入口将签名校验前置，鉴权失败立即断开连接（`Connection: close`）。

**远程媒体错误体泄露（高危）**：旧版本在媒体下载失败时使用 `res.text()` 整体读取错误响应体，攻击者可通过构造异常大的错误体或 slow body 造成内存放大，同时错误体中的敏感内容（如内部路径、凭据片段）更容易进入日志。修复后，错误体读取被限制在 8KB 上限和超时约束内。

**Diagnostics 缓存追踪凭据泄露（中危）**：旧版本在生成诊断缓存追踪 JSONL 文件时，未对输出字段进行过滤，凭据相关字段（如 API key 片段、token 值）可能随诊断日志落盘，在日志被共享或上传时造成凭据泄露。修复后（`2026.3.23`），JSONL 输出在写入前会剥离所有凭据字段，仅保留非敏感诊断字段与图像编辑元数据（`src/infra/diagnostics/cache-trace.ts`）。

---

## 05 版本发布时间线与升级路径

### 发布时间线

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/4EHqib0vXQFibkqBk4v8PX82vTtUYPLl6zlHZjdLopGyIdemCZlrdlusibffQD9JlQialDEVfvUuPib4U7o39C3eLQsaOLAj5yTqwUJyRv8hM1Ls/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=3)

### 版本关系说明

* `2026.3.22-beta.1` 已具备本轮核心安全补丁，`2026.3.22` 是其稳定版发布，继承了 `beta.1` 的主要安全修复，但仍存在部分安全问题（Canvas 匿名访问、非管理员 session reset、shell-wrapper allowlist 绕过），在 `2026.3.23` 中修复。
* `2026.3.23` 额外修补了 Canvas 匿名访问、非管理员 session reset、shell-wrapper positional carrier allowlist 绕过以及 Diagnostics 缓存追踪凭据泄露四个问题。
* `2026.3.24` 是**当前最新完整修复版本**，进一步修补了沙箱媒体路径逃逸（`mediaUrl`/`fileUrl` 别名绕过）和 skill 安装器元数据注入与 URL 协议滥用两个新发现的安全问题。

### 推荐升级路径

**任意旧版本 → 直接升级至 `2026.3.24`（推荐）**

无需经过中间版本，直接升级至 `2026.3.24` 即可获得本轮所有安全修复。

---

## 06 参考链接

* OpenClaw GitHub Releases：https://github.com/openclaw/openclaw/releases
* OpenClaw CHANGELOG：仓库根目录 `CHANGELOG.md`
* 本报告分析的关键文件：

+ `src/plugins/config-state.ts`
+ `src/infra/device-bootstrap.ts`
+ `extensions/telegram/src/webhook.ts`
+ `src/gateway/server/ws-connection/message-handler.ts`
+ `src/media/fetch.ts`
+ `src/infra/exec-approvals-allowlist.ts`
+ `src/gateway/server/http-auth.ts`
+ `src/gateway/server-methods/agent.ts`
+ `src/infra/diagnostics/cache-trace.ts`
+ `src/media/dispatch.ts`
+ `src/skills/installer.ts`
+ `src/control-ui/markdown-preview.ts`

**针对OpenClaw安全风险，腾讯推出多场景安全防护矩阵：**

**本地个人：**

> 腾讯电脑管家 18.0 版本提供「龙虾管家-AI安全沙箱」，无需复杂配置、一键即可为 “龙虾” 开启隔离运行环境，并通过AI实时运行保护和漏洞防护，实现 “龙虾” 的全流程防护。

**本地企业：**

> 腾讯iOA提供 “威胁源头——执行过程——数据出口” 全链路龙虾防护

**云端部署**：

> Lighthouse原生安全 Lighthouse与腾讯云ClawPro...