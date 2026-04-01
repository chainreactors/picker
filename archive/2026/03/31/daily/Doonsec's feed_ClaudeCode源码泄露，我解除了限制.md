---
title: ClaudeCode源码泄露，我解除了限制
url: https://mp.weixin.qq.com/s/v7-WjsSL8T7Fj8Bn7nqHGw
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:21.895399
---

# ClaudeCode源码泄露，我解除了限制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GVAVvm742xNmWsC64a04CSlRLlJsGiaRtg3gRtwStg3H32AjVlteozWJdlM6XLphU1QtuLTPBm06XWxRjSdMhdFQmJgbiardpJhlFH0rpYspg/0?wx_fmt=jpeg)

# ClaudeCode源码泄露，我解除了限制

原创

Taoing
Taoing

Ms08067安全实验室

![]()

在小说阅读器中沉浸阅读

## 一、前言

> 2026年3月31日，发现`Anthropic`的`Claude Code CLI`工具通过`source map`文件暴露了完整源代码。这一发现迅速引发技术社区关注。
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xOZlxvgqeR2jYV3EzibnAYNBPicXFojXib4qrrvrwAD68tqvHO8GicRicC4icNjNJjgyDOzybCfpvqicRGXEKmsDtgGknhS3IH7RsV7cs/640?wx_fmt=png&from=appmsg)

---

> 本次泄露的核心价值不在于代码本身,`Claude Code`作为客户端工具，其大部分逻辑本就可通过反编译获取,而在于它完整暴露了`Anthropic`的安全控制架构、提示词工程策略以及权限边界设计。对于安全研究人员而言，这是一份难得一见的商业级`AI Agent`安全实现参考样本。
>
> ![图像](https://mmbiz.qpic.cn/mmbiz_jpg/GVAVvm742xP6fnspqjW71ajl06ZcHC6eY1mHHXfUICibqbF2XPzqPlakeibbssAjAdVXEy7Sw3em6ZiagvVrv0ib5aPdsIib5ia6JhAg0ibAickljrA/640?wx_fmt=jpeg&from=appmsg)

---

## 二、源码恢复工程的技术路径

![](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xOuBGtwtnKE75PDCTvic3oR3yH7EicsZkj1ibBHD2xyMf191BfblaPicTl3wflICaBujXq4wX5QtibV8WVEATv19EXULt3nIsiaPe9dU/640?wx_fmt=png&from=appmsg)

泄露的源码并非原始开发仓库，而是基于已发布包中的`cli.js`与`cli.js.map`进行反推恢复。这种恢复方式在技术上具有以下特点：

### 2.1 恢复方法

```
ounter(line原始产物 → Source Map解析 → TypeScript源码重构 → 工程化还原
```

* **构建工具**：esbuild重新打包，替代官方原始构建链
* **运行时环境**：Bun（非Node.js）
* **UI框架**：React + Ink（终端渲染框架）
* **架构模式**：模块化工具架构，支持懒加载与动态发现

### 2.2 工程结构

恢复后的代码库呈现典型的分层架构：

| 层级 | 核心模块 | 功能定位 |
| --- | --- | --- |
| 入口层 | `src/entrypoints/` , `src/bootstrap/` | 启动分流、全局状态初始化 |
| 交互层 | `src/components/` , `src/ink/`, `src/screens/` | 终端UI渲染、事件处理 |
| 业务层 | `src/services/` , `src/tools/`, `src/tasks/` | API调用、工具实现、任务执行 |
| 基础设施 | `src/utils/` , `src/constants/`, `src/state/` | 配置管理、权限控制、状态容器 |

---

## 三、安全限制机制解构

### 3.1 提示词级安全边界

泄露代码中最受关注的安全控制点位于`src/constants/cyberRiskInstruction.ts`。该文件定义了一个系统级指令常量，被注入到所有对话模式的系统提示词中。

**原始指令内容（泄露版本）**：

```
ounter(lineexport const CYBER_RISK_INSTRUCTION = `IMPORTANT: Assist with authorized security testing, defensive security, CTF challenges, and educational contexts. Refuse requests for destructive techniques, DoS attacks, mass targeting, supply chain compromise, or detection evasion for malicious purposes. Dual-use security tools (C2 frameworks, credential testing, exploit development) require clear authorization context: pentesting engagements, CTF competitions, security research, or defensive use cases.`
```

该指令在`src/constants/prompts.ts`中被注入到两个关键位置：

* **普通模式**：`getSimpleIntroSection()`函数（第182行）
* **自主代理模式**：Proactive模块的系统提示词模板（第474行）

### 3.2 安全策略的层级设计

Claude Code的安全架构并非单一依赖提示词控制，而是采用多层防御：

```
┌─────────────────────────────────────────────────────────────┐│  Layer 1: 系统提示词控制 (System Prompt)                      ││  - CYBER_RISK_INSTRUCTION (网络安全限制)                      ││  - URL生成限制、提示词注入检测、OWASP防护                        │├─────────────────────────────────────────────────────────────┤│  Layer 2: 权限系统 (Permission System)                        ││  - 危险命令模式匹配                                           ││  - 权限检查流程                                               ││  - 自动模式分类器 (yoloClassifier)                            │├─────────────────────────────────────────────────────────────┤│  Layer 3: 工具级安全检查 (Tool-Level Security)                ││  - PowerShell AST安全分析                                     ││  - Bash破坏性命令警告                                         ││  - 沙箱文件系统隔离                                           │├─────────────────────────────────────────────────────────────┤│  Layer 4: 输入清理 (Input Sanitization)                       ││  - Unicode隐藏字符攻击防护                                     │└─────────────────────────────────────────────────────────────┘
```

### 3.3 权限系统的实现细节

权限控制核心位于`src/utils/permissions/`目录：

| 模块 | 功能 |
| --- | --- |
| `dangerousPatterns.ts` | 定义危险命令的正则匹配模式 |
| `permissions.ts` | 权限检查主流程 |
| `yoloClassifier.ts` | 自动模式ML分类器 |

权限级别枚举：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineenum PermissionLevel {  ALWAYS_ALLOW = "always_allow",  // 持久化授权  ALLOW_ONCE = "allow_once",      // 单次授权  DENY = "deny",                  // 拒绝  ASK = "ask"                     // 需要用户确认（默认）}
```

---

## 四、安全限制移除的技术分析

GitHub仓库`Ta0ing/claude-code_evil`展示了如何通过最小化修改绕过提示词级安全控制。

项目地址：https://github.com/Ta0ing/claude-code\_evil

### 4.1 修改点

**文件**：`src/constants/cyberRiskInstruction.ts`

**修改前**：

```
ounter(lineexport const CYBER_RISK_INSTRUCTION = `IMPORTANT: Assist with authorized security testing...`
```

**修改后**：

```
ounter(lineexport const CYBER_RISK_INSTRUCTION = ``
```

### 4.2 移除限制

修改仅移除了提示词层面的安全边界，其他安全机制仍然生效：

| 安全机制 | 状态 | 说明 |
| --- | --- | --- |
| URL生成限制 | ✅ 生效 | `prompts.ts` 第183行 |
| 提示词注入检测 | ✅ 生效 | `prompts.ts` 第191行 |
| OWASP安全漏洞防护 | ✅ 生效 | `prompts.ts` 第234行 |
| 敏感操作确认 | ✅ 生效 | `prompts.ts` 第255-266行 |
| 危险命令模式匹配 | ✅ 生效 | `dangerousPatterns.ts` |
| Bash/PowerShell安全分析 | ✅ 生效 | 工具级检查 |
| 沙箱隔离 | ✅ 生效 | `sandbox-adapter.ts` |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GVAVvm742xPks3PFuEmEELGicqrOjEDicxPoJxsNRT0DHCKhEtYYC8B7h6icewaR77z1pwNM5EWNW6ziagP5udx3qbGvSGVkkkdpnotwRpmrvrA/640?wx_fmt=jpeg&from=appmsg)

***扫码进入AI交流群***

![](https://mmbiz.qpic.cn/mmbiz_gif/XWPpvP3nWaibHp52zxWlNtN3nVGMLmSA8icwk6kn0UEgUS0697juarl0r7m7wB4FoyBZ2Zu30nUbsrHic6m9yUPsw/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/GVAVvm742xMfOfkwAdk1uFO2pPnvSNSqlvEPficysriaTGMQHdH36vXMcZKh22bWXytgOebMV8LO2z2QjNesgMic60LSgu6bmOslUwVJs6GfGE/640?wx_fmt=jpeg)

****—  关于我们  —****

镇江刺掌信息科技有限公司成立于2020年，公司旗下MS08067安全实验室，专注于网络安全领域教育、培训、认证产品及服务提供商。近两年，线上培训人数近10万人次，培养网络安全人才近6000名。

公司被认定为国家高新技术企业、国家科技型中小企业、江苏省创新性中小企业、江苏省民营科技企业、江苏省软件企业。并荣获机械工业出版社“年度最佳合作伙伴”、电子工业出版社-博文视点“优秀合作伙伴”、镇江市企业发展服务中心优质合作伙伴、镇江市网络安全应急支撑服务单位等荣誉称号。

![图片](https://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWaibvYpHN9LYFOebXFfldqqPibeicFj6KbfoI2xNya3Q5pgAeGPolfhjIlCsdt9TC19DE1CQ41loqtCAA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=2)

```
![图片](https://mmbiz.qpic.cn/mmbiz_png/ddqrZtAEBOj4xTcIKUfImvRJW3QEEJCaNqRTwr9WEqXjnoaQ54wf9BbUE3HqNN7PIOxTDRNRb3e6bsJlSZP6Yw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn55VMON4QdPLRem0HgglfDI6V20Pn5QiaW92aZBNoCAUbs5wzNqGSgnyBseeDYpF3UXjjIl1qwzvyg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

如果喜欢我们

![图片](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn55VMON4QdPLRem0HgglfDI6V20Pn5QiaW92aZBNoCAUbs5wzNqGSgnyBseeDYpF3UXjjIl1qwzvyg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=5)

欢迎 在看丨留言丨分享至朋友圈 三连
```

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/XWPpvP3nWa90pEp3iaRLqIghzI7eJdSJLep6zBaRDKVC6ibGLOlT9TqriaVck7icnvExOuMOCFhVAyVcyJ0JucvrnQ/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=6)

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWa9xKtQcyickhdgvJx9bWxpSjSqS4AwI7o804CbiazVQqTnMibp7ZC6fyxmJ7kgfMyA2rHgHkShs3M7bA/0?wx_fmt=png)

Ms08067安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWa9xKtQcyickhdgvJx9bWxpSjSqS4AwI7o804CbiazVQqTnMibp7ZC6fyxmJ7kgfMyA2rHgHkShs3M7bA/0?wx_fmt=png)

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