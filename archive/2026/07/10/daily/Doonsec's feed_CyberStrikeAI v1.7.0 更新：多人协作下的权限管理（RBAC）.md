---
title: CyberStrikeAI v1.7.0 更新：多人协作下的权限管理（RBAC）
url: https://mp.weixin.qq.com/s/NrBPAaVwu93ztjQ_K69tWw
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:56:47.439030
---

# CyberStrikeAI v1.7.0 更新：多人协作下的权限管理（RBAC）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ufQ2xnAD33tAicOm0PMFlAS5r8jaLiaic9QtVUCRyhQhZ7t6luwh4D52TC23wnrETFzYHK5icEM5Y5rmhL6ItChEMgfHkqa542WcHVVsu61grico/0?wx_fmt=jpeg)

# CyberStrikeAI v1.7.0 更新：多人协作下的权限管理（RBAC）

原创

学安全也就图一乐
学安全也就图一乐

低调学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> v1.6 更适合个人或小团队快速用起来：单账号、配置简单、功能面已经比较全。
> 一旦要放进**多人协作的实验室、安全团队或甲方运营环境**，共享密码和「全员同等权限」就不够用了——
> **v1.7.0 的重点，是把平台 RBAC 接到 API、Agent、MCP、后台任务和机器人的执行链路上。**

---

## 一、为什么 v1.7.0 要推 RBAC？

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33sasnryI41bY9C07oQLR8mYYEwtTopbUkuicrhaXpgw4k89RXvI91YpVVzNMcjkjQyb8Xcw5DtbnSIEU4gSglkSia8XoAbGlANmM/640?wx_fmt=png&from=appmsg)

CyberStrikeAI 不是普通的聊天机器人。它能做的事包括：

* 调用 **安全工具** 与自定义 MCP
* 跑 **单 Agent / Deep / Plan-Execute / Supervisor** 多代理编排
* 操作 **WebShell、内置 C2、批量任务、工作流**
* 在 **企业微信 / 钉钉 / 飞书 / 个人微信 / Telegram** 等 IM 里远程指挥

这里其实有两个常见误区，也是 v1.7.0 要补 RBAC 的原因：

1. **能登录 ≠ 能做所有事**
   以前大家共用一个密码，谁登进来谁就是「管理员」：能删别人的对话、能调 C2/WebShell、能改全局配置。
   多人协作时，更合理的是：实习生能看指定项目，但不能删数据；操作员能跑 Agent，但不能改系统配置——**登录只证明「你是谁」，RBAC 才决定「你能干什么」。**
2. **页面上看不见按钮 ≠ 真的安全**
   如果只在前端把「删除」「终端」等按钮藏起来，懂一点技术的人仍可直接调 API。
   v1.7.0 会在**服务端**对每次 API、Agent 工具调用、机器人消息做权限校验；前端隐藏只是减少误点，**真正的拦截发生在服务端。**

v1.7.0 引入的**平台 RBAC（Role-Based Access Control）**，目标很直接：

1. **多用户**：每人独立账号，告别「全站一个密码」
2. **最小权限**：按岗位给权限，而不是全员 admin
3. **数据隔离**：项目、对话、漏洞、WebShell、C2 等资源按归属与授权可见
4. **全链路 enforcement**：不只管 Web 页面，还管 **API、Agent 工具调用、MCP、后台任务、机器人消息**

一句话总结：**RBAC 管的是「平台授权边界」，不是 Agent 的测试风格。**

---

## 二、先分清两种「角色」——这是上手 RBAC 的第一关

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33stetQdeWaZZYDVnJA9c4xVACUruUkk2XicEjYedqD4tm83JaibYnhq9jRneH8iaqDxClkaphbnAd3pGtrjUUd58T8sxPXBPMicPJY/640?wx_fmt=png&from=appmsg)

很多人第一次用会懵：CyberStrikeAI 里本来就有「渗透测试」「CTF」「Web 扫描」等**角色**，现在又来一套 RBAC **角色**，有什么区别？

| 概念 | 在哪里配 | 决定什么 |
| --- | --- | --- |
| **平台角色（RBAC Role）** | 左侧 **平台权限** | 用户能访问哪些功能、哪些数据 |
| **AI 测试角色（Agent Role）** | 左侧 **角色** / `roles/*.yaml` | Agent 的提示词、测试方法、可选工具集合 |

**关键原则：**

* 选了「渗透测试」AI 角色，**不会**自动获得 C2、WebShell、终端等权限
* 给了 `agent:execute`，**不会**自动改变 Agent 的系统提示词
* 前者是**安全边界**，后者是**测试策略**

团队落地时可以这样记：**按人的职责配平台 RBAC 角色**（谁能看、谁能改、谁能执行）；**按任务类型选 AI 测试角色**（渗透、CTF、信息收集等测试风格）。

---

## 三、RBAC 到底怎么生效？不是「看不见」就算安全

v1.7.0 的授权模型是**服务端强制校验**，前端隐藏按钮只是体验优化。

一次操作要同时满足：

```
有效账号
  + 路由/工具所需 permission（如 project:read）
  + 该 permission 对应的 scope（all / assigned / own）
  + 目标资源的 owner / 显式授权 / 父资源继承
  + 全局对象的额外限制
```

**处理链路（简化版）：**

1. 登录后签发 Bearer Token，会话里带上用户、角色、权限和**逐权限 Scope**
2. HTTP 中间件把 API 路由映射为权限，例如 `GET /api/projects` → `project:read`
3. 带资源 ID 的请求继续校验：是不是 owner？有没有被显式授权？父项目是否已授权？
4. Agent 启动时把不可变 Principal 写入执行上下文
5. 内置 MCP 工具按**工具名 + 参数里的资源 ID** 再查一遍
6. 拒绝会写入 RBAC / 审计日志，方便复盘「谁越权了、越在哪」

所以：**别指望改前端、猜 API 路径能绕过；真正的拒绝发生在服务端。**

---

## 四、开箱即用的四个平台角色

v1.7.0 内置四个系统角色，升级时会按当前版本权限目录自动对齐，避免旧版本残留脏权限：

| 角色 | Scope | 适合谁 |
| --- | --- | --- |
| **admin** 管理员 | `all` | 平台 Owner、实验室负责人 |
| **operator** 操作员 | `assigned` | 日常攻防、项目内测试人员 |
| **auditor** 审计员 | `all` （只读） | 合规审计、复盘、只看不改 |
| **viewer** 只读用户 | `assigned` （只读） | 外包/实习生、甲方对接人 |

**注意：**

* 系统角色不可编辑，需要微调就**复制思路建自定义角色**
* 没分配任何角色的账号能登录，但基本没有业务权限——别拿「空角色」当正式岗位

---

## 五、权限与 Scope：比「能不能点」更细的一层

### 5.1 权限怎么命名？

采用 `模块:动作`，常见动作：

* `read`：查看、列表、导出
* `write`：创建、更新、执行
* `delete`：删除
* `execute`：跑 Agent、终端、工作流等

覆盖模块包括：对话、项目、漏洞、WebShell、C2、MCP、知识库、Skills、工作流、终端、审计、机器人、FOFA、攻击链等 **30+ 模块**。完整目录见 Web 端 **平台权限**，或 API `GET /api/rbac/metadata`。

### 5.2 几个容易踩坑的特殊权限

| 权限 | 说明 |
| --- | --- |
| `agent:execute` | 能跑 Agent，**不自动**包含本机文件/Shell |
| `agent:local-execute` | 本地执行兜底权限，只给可信操作员 |
| `mcp:external:execute` | 调外部 MCP，当前还要求 Scope 为 `all` |
| `robot:write` | 管机器人配置；聊天本身走绑定用户/服务账号的业务权限 |

**RBAC 允许调用 ≠ 可以跳过 HITL。** 高危工具仍建议配合人机协同审批。

### 5.3 三种 Scope

| Scope | 含义 | 典型场景 |
| --- | --- | --- |
| `all` | 该权限覆盖的全部资源 | 管理员、全局审计 |
| `assigned` | 仅管理员显式授权的资源 + 支持的父资源继承 | 项目组成员 |
| `own` | 以本人创建/归属为主 | 个人工作区、机器人独立身份 |

多角色时权限取**并集**；**同一权限**的 Scope 取最宽：`all > assigned > own`。

但有个细节：**全局读取不会把写权限放大成全局写。** 服务端按 `ScopeFor(permission)` 逐项判断，不能只看用户「最宽总 Scope」。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33ssIzW0nmvXXMxXZdpj8Xq8bS3ocSvA1jTX8OWy6tshfTnFasyldT2sZvibaOPHsrDPMtuZ0zpF9ya9qk5AaDFdSs1NtS0h4Fvg/640?wx_fmt=png&from=appmsg)

### 5.4 哪些东西是「全局对象」？

即使你有 `write`，若 Scope 不是 `all`，仍可能改不了这些进程级共享配置：

* AI 测试角色、Skills、Markdown Agents
* 外部 MCP 配置、机器人配置、工作流定义
* 知识库写操作（搜索除外）、HITL 全局策略、C2 Profile 等

这是 v1 的设计取舍：**先把执行链路和数据资源管住，全局定义的细粒度分权还在演进。**

---

## 六、资源授权：项目授权一次，对话/漏洞往往跟着走

在 **平台权限 → 成员详情 → 资源授权** 里，可以给用户分配：

* 项目 `project`
* 对话 `conversation`
* 漏洞 `vulnerability`
* WebShell `webshell`
* 批量任务 `batch_task`
* C2 Listener `c2_listener`

**继承关系（实用）：**

* 授权项目 → 通常可访问该项目下对话、漏洞
* 对话 → 消息、过程详情、攻击链
* C2 Listener → Session → Task / 文件 / 事件

批量授权单次最多 **100** 个资源；重复授权会自动跳过。

---

## 七、Web 端怎么用？三步搭好团队权限

### 7.1 创建成员

1. 管理员登录 → 左侧 **平台权限**
2. 点击 **添加成员**：用户名、显示名、密码（至少 8 位）、启用状态
3. 分配一个或多个平台角色
4. 若角色 Scope 是 `assigned`，继续在 **资源授权** 里勾选项目等资源
5. 让用户重新登录，在右上角用户菜单确认角色、权限数、Scope

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33srsHu88sz5WAzgGLavprwQZEGAgiadyNRqlqn0zsj2jh6CpeW7nvfjul4gU8X7dKmEA5KQmbrNK8OT3mSwxj14J8w4dqhOunnQ/640?wx_fmt=png&from=appmsg)

### 7.2 创建自定义角色

1. **新建角色** → 写清岗位名和说明（如「红队一线」「甲方只读」）
2. 选 `all` / `assigned` / `own`
3. **只勾岗位真正需要的权限**——宁可少给，后续再加
4. 先用测试账号验证：列表、详情、写操作、删操作、Agent 调工具
5. 再批量分给正式用户

### 7.3 权限变更何时生效？

* 改用户角色/密码/启用状态 → **该用户现有会话立即作废**，需重新登录
* 改/删自定义角色 → **全站会话作废**，所有人重登
* 机器人 → **每条消息实时**重新解析绑定用户权限，下一条就生效
* 后台批量任务 → 按任务 owner 重新解析 Principal，不依赖创建时的前端状态

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sZALeD5HBjfTCqTfibuA84YiaKicYRd4xdko0bxIjEOAVzeQzzRiaEeccgsU0y4CtaXiaqrtuYLicQv9WoNwdtrI8VMaR9q1QXjuOw4/640?wx_fmt=png&from=appmsg)

---

## 八、典型落地场景

### 场景 A：安全实验室多人协作

* **队长**：`admin` 或自定义 `all` 管理角色
* **队员**：`operator` + `assigned`，只授权当前攻防项目
* **复盘同学**：`auditor`，`all` 只读，能看全站但不能改
* **实习生**：`viewer` + `assigned`，只看指定项目对话和漏洞

配合 **项目管理 + 攻击链 + 事实黑板**，不同人看到同一项目的不同切面，但改不了别人的 C2/WebShell。

### 场景 B：甲方安全运营「能用但不能乱动」

* 给 `agent:execute` + `chat:read/write` + `vulnerability:read/write`
* **不给**`agent:local-execute`、`terminal:execute`、`c2:write`
* HITL 默认人工审批，审计 Agent 用小模型降本

Agent 能帮忙分析、记录漏洞，但很难在平台里直接执行破坏性本机命令。

### 场景 C：机器人值班号

建一个专用 RBAC 用户：

```
Scope: own（独立工作区）或 assigned（指定项目）
agent:execute
chat:read / chat:write
按需增加 project、vulnerability、knowledge 等
```

**不要用 admin 当机器人账号**，除非你真的想让白名单里每个人都拥有完整权限并共享全部数据。

### 场景 D：红队项目制

* 每个项目一个 `assigned` 操作员组
* WebShell、C2 Listener 按项目显式授权
* 项目结束：禁用账号 → 撤销机器人绑定 → 撤销资源授权

审计日志里可追踪 `rbac/access_denied`、角色变更、机器人服务账号执行。

---

## 九、机器人 + RBAC：IM 里也能按人分权

v1.7.0 把机器人纳入同一套 RBAC。**平台 Token/签名只证明「消息来自钉钉/飞书」；真正决定能干什么的是 CyberStrikeAI 身份。**

支持平台：个人微信、企业微信、钉钉、飞书、Telegram、Slack、Discord、QQ 机器人。

### 9.1 两种业务鉴权模式

| 场景 | 推荐模式 | 效果 |
| --- | --- | --- |
| 企微/飞书/钉钉等多人共用机器人 | `user_binding` 逐用户绑定 | 每人绑自己的 Web 账号，数据隔离 |
| 个人微信、单人专属、固定自动化入口 | `service_account` 专用服务账号 | 白名单发送者共用指定 RBAC 用户 |

**机器人对话最低权限：**

```
agent:execute
chat:read
chat:write
```

删对话要 `chat:delete`；用项目、WebShell、C2、外部 MCP 等还要各自权限。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vjjjMuDYrh4xw4055062YQgGDVGrOicglicd78Qj5nibSJIM54coEz46l3vtNeibtBvp1gGmnQKyLSMNxuiaSVa0icROABH01iaJsuXs/640?wx_fmt=png&from=appmsg)

### 9.2 逐用户绑定（默认，多人团队首选）

**管理员：**

1. 系统设置 → 机器人设置 → 选平台
2. 业务鉴权策略选 **逐用户绑定**
3. 应用配置

**每位使用者：**

1. Web 右上角头像 → **绑定机器人账号** → 生成绑定码（5 分钟有效）
2. 在机器人里发送：`绑定 7C6E-BD4C`（以页面显示为准）
3. 发送 `身份` 或 `whoami`，确认「鉴权状态：已授权」且实际身份是自己

绑定码一次性、哈希存储；过期需重新生成。可 `解绑` 或在 Web 端撤销。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33skMWAHreRAoGKTCvt1u6IR4omibIFkmrmv81kkRUhsH7kpl9yplq3VibdmqxFfnYZqSodicVNcplOe6MSD6LJJszAkDbQdvmbeDc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33vQr3GtIy8smnKPribQD0CXdNyfFPW27pNgmkfm9bEWUpNltotAVRmNzoKO9Qib6umsas6iaKz47RX7ldOTqknaeR0eIiabViakFz3M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33sLWUGzmLibf39TqHAUBrHjgT1vhTjNycpMgxNe8yWOId4uFTsYEZIa5eJNk1yL6YG03RvACIQ53axUyT67EOaVKnwqVdRZH4kI/640?wx_fmt=jpeg&from=appmsg)

### 9.3 专用服务账号（个人微信 / 单人 bot）

1. 机器人连上平台后，先发送 `身份`，复制完整 **发送者 ID**（个人微信常形如 `...