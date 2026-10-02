---
title: Agent Harness 实战：Session 隔离（会话隔离）
url: https://mp.weixin.qq.com/s/covMvWQTY9raqfmILl4T8Q
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:42:41.338312
---

# Agent Harness 实战：Session 隔离（会话隔离）

# Agent Harness 实战：Session 隔离（会话隔离）

原创

Z
Z

威胁情报Z分析

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、为什么必须做 Session 隔离

##

1. **上下文污染**

   多用户共用同一个 Agent 实例，A 的对话历史被 B 看到，模型会混在一起，答非所问。
2. **文件 / 数据泄露**

   Agent 写代码、生成文件，不隔离会跨会话读取别人的文件。
3. **工具状态串扰**

   工具的变量、数据库连接、缓存跨会话残留，导致逻辑错乱。
4. **安全爆炸半径**

   恶意 Agent 沙箱逃逸，仅影响当前 Session，不会横向渗透其他会话。
5. **故障隔离**

   一个会话死循环、内存溢出，不会拖垮其他会话。

> 核心原则：**一个 Session = 一套独立上下文 + 独立 Workspace + 独立沙箱环境**；Harness 编排层无状态，状态全部存在 Session 存储中。

二、Session 完整生命周期流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXukr2vuNGDelzicxMwzDdKkM9YwY9hIVJzlgEle2icnmFcqTsVS8o5wAEc9WLeREDSxjq4iaqNnIiaW7VQPPndUB9Y4Wd7j8kZiaiaGmk/640?wx_fmt=png&from=appmsg)

三、隔离等级

| 隔离等级 | 隔离范围 | 实现方式 | 适用场景 | 风险 |
| --- | --- | --- | --- | --- |
| 软隔离（上下文隔离） | 仅对话上下文隔离，工具 / 文件共享 | 内存 / Redis 按 SessionID 隔离对话历史，共用工具进程 | 简单对话 Agent，无文件操作 | 高，文件、工具状态串扰 |
| 工作区隔离 | 上下文 + 独立目录 | 每个 Session 分配独立 workdir 目录，进程共享 | 轻量代码执行 | 进程内存、网络可跨会话泄露 |
| 容器级隔离（推荐生产） | 上下文 + 独立文件系统 + 网络 Namespace | 每个 Session 启动独立短期容器 / Pod | 代码解释器、多租户 Agent | 中等，容器逃逸风险 |
| MicroVM 强隔离 | 独立轻量虚拟机 | Firecracker 等 microVM | 高安全场景，不可信 Agent | 成本高，冷启动慢 |

工程最佳实践：**上下文隔离是基础，沙箱环境隔离是安全底线**。仅做上下文隔离，不隔离文件 / 网络，不能称为完整 Session 隔离。

四、实战关键组件拆解

### 1. Session 存储（Append-only 事件日志）

###

Session 不是简单聊天记录，是**只追加事件日志**：用户消息、模型推理、工具调用、工具返回、状态快照全部作为事件追加写入，不修改旧记录。

* 存储：Redis（活跃会话）+ 对象存储 / 数据库（持久审计日志）
* 主键：`session_id`，全局唯一，绑定用户身份
* 好处：Harness 任意实例崩溃，只要拿到 session\_id，重放事件日志即可恢复 Agent 状态

### 2. Harness 编排层（无状态）

###

职责：

* Session 生命周期管理：Create / Resume / Heartbeat / Destroy
* 权限校验：每个 Session 绑定权限策略
* 沙箱调度：为 session\_id 分配沙箱实例，绑定生命周期
* 上下文压缩：在 token 超限的时候做阶梯压缩，**不破坏 ReAct 推理链**

> 禁止：Harness 进程内存里保存会话状态。

### 3. 每 Session 独立 Sandbox

###

隔离项：

* 文件系统：独立根目录，会话销毁直接删除，无残留
* 网络：独立网络命名空间，防火墙策略，仅允许白名单出站
* 工具注册表：每个沙箱内工具实例独立，变量、缓存不共享
* 用户身份：低权限用户账号运行 Agent 进程，禁止宿主机高权限访问

###

### 4. 身份与访问控制

###

* 所有 Session 绑定 user\_id/tenant\_id；跨 session 不能读取其他 session\_id 的事件日志
* 沙箱凭证注入：**凭证按会话注入，沙箱本身不持久保存密钥**，会话销毁密钥失效

五、极简实战伪代码

```
# 1. 创建新会话session_id = harness.create_session(user_id="u1001")# 自动生成append-only事件日志，分配独立sandboxsandbox = harness.spawn_sandbox(session_id=session_id)# 2. 用户消息，写入当前session事件harness.append_event(session_id, {"type":"user_msg", "content":"写一个python脚本"})# 3. Harness加载本session事件，组装上下文调用LLMctx = harness.load_context(session_id)llm_resp = llm.call(ctx)# 4. 如果是工具调用，仅在本session的sandbox执行if llm_resp.tool_call:    result = sandbox.exec_tool(llm_resp.tool_call)    harness.append_event(session_id, {"type":"tool_result", "data":result})# 5. 会话结束，销毁沙箱，事件日志保留审计harness.destroy_sandbox(session_id)# session日志持久化保存，沙箱文件全部销毁
```

## 六、常见踩坑点

##

1. ❌ 只隔离对话历史，**文件目录全局共享**：工具产生的文件跨会话泄露。
2. ❌ 共用工具实例，全局变量：A 会话修改工具全局变量，B 会话直接受影响。
3. ❌ Session 日志直接修改（不是 append-only）：Agent 崩溃后无法恢复推理链。
4. ❌ 沙箱复用：多个 session 复用同一个容器，残留文件、环境变量。
5. ❌ 上下文粗暴截断：直接删除早期消息，ReAct 推理链断裂，Agent 陷入重复调用工具死循环。正确做法：阶梯式上下文压缩，保留系统 prompt 与关键推理链路。

##

## 六、可观测设计（Session 隔离配套）

##

每个事件日志自动埋点：

* session\_id、user\_id、事件类型、token 消耗、耗时
* 沙箱资源指标：CPU / 内存 / 网络 IO
* 审计日志：所有工具调用、文件读写、网络访问，按 session 维度检索

## 七、扩展思考

##

Session 隔离 ≠ 多 Agent 隔离。

* Session 隔离：**同一个 Agent 模板，多个独立会话实例**，用户对话隔离。
* Supervisor 多 Agent：一个会话内部，再拆分多个子 Agent 协同，子 Agent 共享同一个 Session 沙箱。

如果你需要，我可以继续输出：

1. 完整可直接放进 PPT 的中文版本（带排版）
2. K8s 部署 YAML：每个 Session 创建短期 Pod 实现容器级隔离
3. 压测方案：并发多 Session 场景下 Harness + 沙箱的性能测试脚本
4. 上下文压缩完整实现代码（解决长会话 token 超限）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBkc5vFwntXsAd8nDxmDyBf0Z76ENz1lEx3EmN3upgBOvJOHKylGVwXH7KCZSXduJAuoib2MvH9Hyww/0?wx_fmt=png)

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
在看
，轻点两下取消在看
分享
留言
收藏
听过