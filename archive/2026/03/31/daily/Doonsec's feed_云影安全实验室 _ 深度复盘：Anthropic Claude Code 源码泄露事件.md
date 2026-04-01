---
title: 云影安全实验室 | 深度复盘：Anthropic Claude Code 源码泄露事件
url: https://mp.weixin.qq.com/s/4mKVw6M6rvOgP6BciZlIig
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:13.904894
---

# 云影安全实验室 | 深度复盘：Anthropic Claude Code 源码泄露事件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/G4YmHKUJpT9IeYznOibNdgU3dsQibHZiaQT6FEvrmVhibJYvIlCCvHtXQ2NzhDbTLU88wribAUzMFTJTmAA9s398dkiaCaw6ibwJUPLk2g1516bEfY/0?wx_fmt=jpeg)

# 云影安全实验室 | 深度复盘：Anthropic Claude Code 源码泄露事件

原创

SchneiderGrace
SchneiderGrace

云影安全实验室

![]()

在小说阅读器中沉浸阅读

**大家好，这里是云影安全实验室（Yunying Security Lab），我是Schneider。**

今天（2026年3月31日），Anthropic 再次用实际行动给我们上了一课：**顶级 AI 公司也会在最基础的 DevSecOps 环节翻车**。

## 事件核心：一次“教科书级”的 npm 打包失误

Anthropic 官方 npm 包 `@anthropic-ai/claude-code`（v2.1.88）中，**意外打包了 59.7MB 的 `cli.js.map` source map 文件**。

这个 `.map` 文件不仅包含源码映射，还**完整嵌入了 `sourcesContent`** —— 直接就是原始 TypeScript 源码。任何开发者只需一行命令：

```
npm install @anthropic-ai/claude-code
```

即可下载，然后一键还原完整代码。

### 泄露规模

* **约 1900+ 个文件**
* **51.2 万行 TypeScript 代码**
* 涵盖前端 UI、工具调用系统、权限控制、Agent 运行时、记忆模块等**完整架构**

研究员 **Chaofan Shou** 在 X 上率先公开披露，随后社区迅速镜像，多个 GitHub 仓库已公开传播。

这已经是 Anthropic **近期第二次**类似泄露（上一次是 Claude Mythos 内部文档）。连续犯低级错误，值得所有 AI 基础设施团队高度警惕。

## 安全视角：这不是小失误，是严重供应链风险

### 1. 知识产权与商业机密全面暴露

泄露的不仅仅是代码，还有大量**未发布 feature flags** 和内部核心逻辑：

* **KAIROS 模式**：全天候贾维斯式智能助手，支持 Webhook、社交软件远程控制等
* **DAEMON 守护进程**：终端关闭后仍可后台持续运行
* **AGENT\_TRIGGERS**、**MONITOR\_TOOL**、**memdir** 记忆系统、**cost-tracker** 等
* Ink React Terminal UI 框架、多层权限控制、并行工具调用机制

这些内容对竞争对手和安全研究者而言是**极高价值情报**。

### 2. 供应链攻击潜在放大

npm 包被广泛依赖，一旦被恶意植入后门或被下游项目直接 fork，风险将通过整个 AI 工具链快速扩散。幸好本次是“纯源码泄露”，暂未发现恶意植入，但**下一次呢**？

### 3. 配置管理与发布流程的双重失败

典型问题包括：

* 未正确配置 `.npmignore` 或 `files` 字段
* Source map 未在生产发布时剥离
* 云存储（R2）链接直接暴露在 map 文件中

这暴露了 Anthropic 在 CI/CD 安全管控上的明显薄弱环节。

## 对开发者和企业的安全启示

### 对于开发者/团队：

* **永远不要相信官方 npm 包的“干净性”** —— 定期审计依赖中的 `.map`、`.d.ts` 等辅助文件
* 生产环境构建时严格分离 source map，推荐使用 `source-map-exclude` 等工具
* Fork 开源/泄露代码时，必须做好**代码审查 + 安全扫描**（推荐 Semgrep + Trivy）
* AI Agent 类工具权限极高，使用前必须进行沙箱隔离和行为监控

### 对于 AI 公司/大模型团队：

* 加强发布流水线安全门禁（SCA + SAST + 手动代码审查）
* 敏感项目建议采用私有 registry + 严格访问控制
* 泄露后快速响应很重要，但**预防永远优于事后撤回**

## 云影安全实验室观点

这次事件再次证明：在 AI 军备竞赛中，**工程安全和运维安全才是真正的护城河**。模型参数再强，底层系统如果漏洞百出，优势也会瞬间归零。

云影安全实验室将继续跟踪本次泄露代码的安全分析，重点包括：

* 权限控制机制强度
* Agent 执行沙箱实现
* 潜在的后门/远程控制风险点

---

**你怎么看这次泄露？**

* 是单纯的打包失误，还是暴露了更深层的 DevSecOps 文化问题？
* 对 AI Agent 安全落地有哪些新思考？

欢迎在评论区理性讨论。**点赞 + 在看**，我们会持续输出高质量网安干货。

**关注公众号「云影安全实验室」**，一起守护 AI 时代的数字边界。

**关注公众号发送0331**获取Claude Code 源码泄露下载地址

---

**声明**：本文基于公开信息与安全研究整理，仅供学习与参考，**严禁用于非法用途**。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/tgtBX9Q56BUkpHau2qCpWKbGqVyeuKfR2bMfd9L6ZyNPBmNwvydyN2iaVDAQrDViag1xHrlqqxaranmJc0tJOO6g/0?wx_fmt=png)

云影安全实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/tgtBX9Q56BUkpHau2qCpWKbGqVyeuKfR2bMfd9L6ZyNPBmNwvydyN2iaVDAQrDViag1xHrlqqxaranmJc0tJOO6g/0?wx_fmt=png)

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