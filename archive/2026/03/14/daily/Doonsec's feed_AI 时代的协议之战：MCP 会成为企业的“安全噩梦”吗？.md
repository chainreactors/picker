---
title: AI 时代的协议之战：MCP 会成为企业的“安全噩梦”吗？
url: https://mp.weixin.qq.com/s/CH6UeltLrNaEfdWJrmUr9w
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:27:38.167820
---

# AI 时代的协议之战：MCP 会成为企业的“安全噩梦”吗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PIWj1VguNosUgFepMjYFTn9qD22tFkyMffia5pqqUhLvhXePjykOtu7LS1TRdsRich0GGduTQLCibFoUz4aia9dPquDPktNjbictdR99ibZTKGhXk/0?wx_fmt=jpeg)

# AI 时代的协议之战：MCP 会成为企业的“安全噩梦”吗？

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器中沉浸阅读

### 前言

当我们在为 AI 代理（AI Agents）能够自主读取文档、调用 API、甚至编写代码而欢呼时，一个潜伏在底层的影子正悄然逼近。最近，知名安全机构 **Doyensec** 发布了一篇名为《The MCP AuthN/Z Nightmare》的技术深度博客，直指当前大火的 **Model Context Protocol (MCP)** 在身份验证与授权（AuthN/AuthZ）上的“噩梦级”隐患。

---

## 1. 事件背景：当 AI 拥有了“手脚”

随着 Anthropic 推出 MCP 协议，AI 模型正式告别了“空中楼阁”时代。开发者们疯狂地为自己的 LLM 接入各种本地或远程工具。然而，安全总是滞后于效率。Doyensec 的研究指出，MCP 在企业级远程部署中，由于标准碎片化和信任链条的复杂性，正面临前所未有的安全挑战。

## 2. 什么是 MCP？它解决了什么？

**Model Context Protocol (MCP)** 是由 Anthropic 主导的一项开放协议，旨在标准化 AI 模型与数据源（如 GitHub、Google Drive、Slack、数据库等）之间的连接。

* **解决的问题：** 以前每个 AI 工具都要单独写集成代码，现在只需通过 MCP，一个 Server 即可对接多个 Client（如 Claude Desktop、IDE 等）。
* **核心用途：** 它让 AI 具备了**上下文感知**和**工具执行**能力。简单来说，MCP 就是 AI 的“通用串行总线（USB）”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PIWj1VguNovds3nianpiaGajQTH9cdicfP8mtILibvWOW7rYrsrbjpF9LbhhL1LWXhGKicwsxBmloyl171EOXOYWUXt7hrjOk4353FIOFbBMwPRE/640?wx_fmt=jpeg&from=appmsg)

---

## 3. 核心概念：JAG 与其架构

在企业级场景下，如何证明“我是我”且“我有权让 AI 这么干”？Doyensec 重点剖析了 **JAG (Identity Assertion JWT Authorization Grant)** 方案。

### JAG 架构简述

JAG 试图利用企业现有的身份提供商（IdP，如 Okta）来为 AI 代理背书：

1. **身份断言：** 客户端向 IdP 申请一个证明用户身份的 JWT（即 JAG ID）。
2. **授权兑换：** 客户端拿着 JAG ID 去向 MCP 授权服务器换取 Access Token。
3. **资源调用：** 最终通过 Token 调用后端的工具（如删除服务器文件）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNov9M3M7dZYl6X1COllMiaI5IwURzZrdU4H148UXxicpVVj03KbsQ348JUYHBlkNyxCPdFYhLMdo6gN0DueuFvMwrdfxicWBwUBw5Q/640?wx_fmt=png&from=appmsg)

---

## 4. MCP 的安全“噩梦”：详细风险场景

Doyensec 警告称，JAG 架构虽然看起来逻辑通顺，但在 MCP 的非确定性场景下，存在以下致命风险：

### A. 访问失效的“盲区”

* **风险：** 目前协议未定义如何撤销已颁发的 Token。
* **场景：** 如果一个 AI 代理被黑客通过“提示词注入”控制，开始疯狂删除数据库，管理员竟然\*\*没有一个统一的“断路器”\*\*来瞬间切断该代理的权限。

### B. LLM 的权限“盲盒”

* **风险：** 代理可以在用户不知情的情况下，自主请求高危权限。
* **场景：** 用户只是让 AI “总结最近的邮件”，AI 却在后台利用 JAG 自动申请了 `gmail:delete` 权限。由于没有弹出确认框（Scope Consent），用户在完全无感的情况下，资产可能已被清空。

### C. 资源标识符注入 (Resource Injection)

* **风险：** 缺乏严格的命名空间校验。
* **场景：** 攻击者可能利用一个低安全级别服务器的 Token，去尝试访问高安全级别的资源。如果授权服务器没分清 `Server-A` 和 `Server-B` 的边界，就会发生“身份混淆”。

### D. 令牌重放与放大攻击

* **风险：** 单个 JAG ID 若能铸造多个 Token，其泄露后的破坏力将呈几何倍数增长。

---

## 5. 破局之道：如何构建安全的 MCP 生态？

面对这些“噩梦”，我们不能因噎废食，而应重塑信任模型。Doyensec 与安全专家给出了以下建议：

1. **采用 mTLS 和证书授权：** 放弃脆弱的纯 JWT 传递，改用 **双向 TLS (mTLS)** 这种确定性更高的身份绑定方式。
2. **引入“人类确认”环节：** 对于涉及数据修改、删除、外传等高危操作，必须强制引入 **Human-in-the-loop**，不能让 AI 自主决定。
3. **严格的命名空间隔离：** 在企业内部强制执行 Scope 的命名规范，防止不同 MCP Server 之间的权限穿透。
4. **建立全局撤销机制：** 开发者应实现即时的 Token 撤销接口，确保在发现异常行为时能秒级响应。
5. **协议最小化原则：** 不要试图把整个 SSO 体系塞进 MCP，而应追求减少隐式信任，让每一条指令都可审计、可回溯。

---

### 结语

MCP 的出现是 AI 迈向自动化的里程碑，但安全绝不能成为其牺牲品。正如 Doyensec 所言：“复杂性是安全的敌人。”在 AI 代理接管我们屏幕的今天，构建一个透明、受控的授权链条，比追求极致的自动化更为重要。

### 参考

* **官方博客链接：** https://blog.doyensec.com/2026/03/05/mcp-nightmare.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

APT-101

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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