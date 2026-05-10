---
title: 130万次下载的神库爆严重漏洞！Node.js沙箱逃逸PoC已公开，你的代码还在裸奔？
url: https://mp.weixin.qq.com/s/M7K5dxFQO5-F8FA7V3E8_Q
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:31:56.116577
---

# 130万次下载的神库爆严重漏洞！Node.js沙箱逃逸PoC已公开，你的代码还在裸奔？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SNiaibgtopgk8iaCNJ7YBIdDOMzgDwBDHRzL4TToostLCuNiaa4C4EvRNWx6xJVqvtTS2gNmkKJhYGqn3hdXlKWNkib3hexDicRYVT2TxJx6xC8mw/0?wx_fmt=jpeg)

# 130万次下载的神库爆严重漏洞！Node.js沙箱逃逸PoC已公开，你的代码还在裸奔？

原创

RCS-TEAM安全团队
RCS-TEAM安全团队

RCS-TEAM

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![文章封面](https://mmbiz.qpic.cn/mmbiz_png/SNiaibgtopgk9neic9icsuyjvCSRfnHciby0ukzVoPKfqia4cJ9VTPUYQW1SMXMwic5ahC139R3TCf3icowKWHVadud1PYmeRrBFhF67ZyUJ9Xia0kls/640?from=appmsg)

# 130万次下载的神库爆严重漏洞！Node.js沙箱逃逸PoC已公开，你的代码还在裸奔？

> 一个被全球开发者依赖了多年的沙箱库，被证明根本关不住恶意代码。PoC已经摆在GitHub上了，你还没升级？

---

## 事情是这样的

5月6号，BleepingComputer爆了一条消息：**vm2**——这个每周下载量超过130万次的Node.js沙箱库——被发现存在一个**Critical级别的沙箱逃逸漏洞**，CVE编号 **CVE-2026-26956**。

什么叫沙箱逃逸？简单说就是：你以为把不可信代码关进了笼子里，实际上它一脚就把笼门踹开了，直接在你的服务器上跑任意代码。

更吓人的是，**PoC exploit代码已经公开**，攻击者不需要什么高超技巧，照着PoC就能打。

---

## vm2是什么？为什么它这么重要？

vm2是一个Node.js的开源沙箱库，专门用来**在受限环境中运行不可信的JavaScript代码**。

它的工作方式是把用户提交的代码隔离在一个沙箱里，阻止访问 `process`、文件系统这些敏感的Node.js API。

你想想哪些场景会用到它：

▪**在线代码编辑器**（比如CodeSandbox、StackBlitz这类平台）

▪**SaaS应用**中执行用户上传的脚本

▪**自动化测试工具**中运行第三方代码

▪**Serverless函数**执行环境

全球**每周130万次下载**，说明有多少项目把vm2当安全底线在用。

---

## 漏洞原理：WebAssembly成了"后门"

这个漏洞的根因很有意思——**WebAssembly的异常处理机制**绕过了vm2的JavaScript层安全防线。

vm2原本的安全设计是：

①用JavaScript级别的保护来防止来自宿主环境的错误

②用Bridge Proxies来包裹跨上下文的对象

③全部跑在JavaScript层

但问题出在：**WebAssembly异常处理可以在V8引擎底层拦截JavaScript错误**，直接跳过vm2的JS层防护。

攻击者只需要：

①触发一个精心构造的 `TypeError`（通过 `Symbol` 到字符串的转换）

②导致宿主侧的错误对象泄露回沙箱

③这个错误对象没有被vm2清理，直接暴露了宿主环境

④沙箱逃逸，任意代码执行

**一句话总结：vm2的JS层防护被WebAssembly从底层绕过了。**

---

## 受影响范围

▪**vm2 3.10.4** 已确认受影响

▪更早版本**很可能也受影响**（官方没有排除）

▪需要运行在 **Node.js 25** 环境下（已在 Node.js 25.6.1 上验证）

▪需要启用 **WebAssembly异常处理** 和 **JSTag支持**

虽然看起来条件有点苛刻，但注意两点：

①**PoC已公开**，攻击者会想办法让环境满足条件

②很多在线平台默认就启用了这些特性

③即使你当前没升级Node.js 25，PoC的存在意味着漏洞细节已经完全暴露，未来可能有更多变种

---

## 怎么检查你的项目？

### 第一步：检查是否用了vm2

在项目根目录跑：

```
# 检查package.json grep "vm2" package.json  # 检查node_modulesls node_modules | grep vm2  # 全局搜索 find . -name "package.json" -exec grep -l "vm2" {} \;
```

### 第二步：检查版本

```
npm ls vm2
```

如果版本 ≤ 3.10.4，**立刻升级**。

### 第三步：检查Node.js版本

```
node -v
```

如果你跑在 Node.js 25 上且用了vm2，风险等级直接拉满。

---

## 修复方案

### 方案一：升级vm2（推荐）

```
npm update vm2 # 或 yarn upgrade vm2
```

关注vm2官方GitHub仓库，等待修复版本发布。目前 maintainer 已经确认了漏洞，修复补丁应该很快。

### 方案二：临时缓解措施

如果暂时不能升级，做以下操作降低风险：

```
# 1. 禁用WebAssembly异常处理（启动Node时加参数） node --no-wasm-eh node your-app.js  # 2. 不要在生产环境用Node.js 25# 降级到 LTS 版本（Node.js 22 LTS） nvm use 22  # 3. 在沙箱外层加一层防护# 用Docker容器隔离，即使沙箱逃逸也跑不出容器 docker run --read-only --memory=256m --cpus=0.5 your-app
```

### 方案三：考虑替代方案

如果vm2长期不修复，或者你的场景对安全要求极高，考虑换用：

| 替代方案 | 特点 | 适用场景 |
| --- | --- | --- |
| **isolated-vm** | 基于V8 isolate，性能更好 | 高性能沙箱需求 |
| **Node.js Worker Threads** | 原生线程隔离 | 简单隔离场景 |
| **Docker容器** | 操作系统级隔离 | 最高安全要求 |
| **Firecracker microVM** | 硬件级隔离 | 多租户SaaS平台 |

---

## 给开发者的5条建议

**1. 别把vm2当唯一防线**

vm2是最后一道防线，不是唯一防线。你的代码应该有多层防护：输入验证 → 权限控制 → 沙箱 → 容器隔离。

**2. 定期审计依赖**

```
# 检查已知漏洞 npm audit  # 更严格的检查 npm audit --audit-level=critical
```

把 `npm audit` 加到CI/CD流程里，每次提交自动检查。

**3. 用npm的overrides锁定安全版本**

```
{"overrides":{"vm2":"^3.10.5"}}
```

这样即使间接依赖引入了旧版本，也会被强制覆盖。

**4. 监控vm2的GitHub仓库**

https://github.com/patriksimek/vm2

关注Issues和Releases，有安全更新第一时间知道。

**5. 生产环境别用最新版Node.js**

Node.js 25 是最新主线版本，不是LTS。生产环境老老实实用LTS版本（目前是Node.js 22），减少未知风险。

---

## 这个漏洞告诉我们什么？

**沙箱从来不是绝对安全的。**

vm2的维护者花了多年时间构建JavaScript层的防护，结果被WebAssembly一个底层特性直接绕过了。这跟当年Java Applet沙箱、Flash沙箱被绕过是一个道理——**只要攻击面够大，总能找到突破口。**

对于安全团队来说，这意味着：

▪不要相信任何单一的沙箱机制

▪纵深防御（Defense in Depth）不是口号，是保命手段

▪依赖供应链安全（Supply Chain Security）越来越重要，一个npm包出事，下游几百万项目跟着遭殃

---

## 写在最后

这个漏洞目前影响的主要是Node.js 25环境，但PoC公开意味着攻击者随时可能找到更多利用方式。

**不管你现在用的是什么版本，第一件事：检查你的项目有没有依赖vm2。**

如果有，赶紧升级。如果没有，也看看有没有类似的沙箱库在裸奔。

网络安全这行，永远比攻击者快一步，才能睡得着觉。

---

*信息来源：BleepingComputer 2026-05-06 报道、vm2官方安全公告*
*CVE编号：CVE-2026-26956*
*本文链接：数据织梦·每日安全速递*

SECURITY · RCS-TEAM

关注 RCS-TEAM 安全团队

聚焦安全研究、漏洞分析、攻防技术与行业观察
         持续输出高质量安全内容

长按识别二维码，立即关注

COMMUNITY · SECURITY GROUP

加入 RCS-TEAM 安全交流群

想继续交流漏洞分析、攻防实践和文章里的细节补充，欢迎扫码进群。

           群内会不定期分享复现思路、工具经验和最新讨论。

           扫码即可加入交流，二维码失效可在后台回复「加群」。

实战问题、漏洞思路、工具踩坑都可以在群里继续聊
         也欢迎直接反馈你想看的后续选题

![RCS-TEAM安全交流群二维码](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SNiaibgtopgk8gRNmfdHlsmCZvU0XuyeAFqUJhRD3zqNnE82jOdHRlI7GDDwlfsRacGSGCuwCtfCzw8Xk76Qa6eicOH5vsSsKvnicnOoHQgU2EU/640?from=appmsg)

扫码加入交流群

若二维码失效或群满，请在后台回复「加群」

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/nUHbLcGPue4pUAAI1y5TIkP75j0BcQiczZZbrQ4U8ibKSCHKppbGmdlDgol2FfO2JMTOJbBibsl8Fbia8PvibnoTNWQ/0?wx_fmt=png)

RCS-TEAM

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nUHbLcGPue4pUAAI1y5TIkP75j0BcQiczZZbrQ4U8ibKSCHKppbGmdlDgol2FfO2JMTOJbBibsl8Fbia8PvibnoTNWQ/0?wx_fmt=png)

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