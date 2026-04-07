---
title: eCapture V2 来了，AI Agent 是主要重构者
url: https://mp.weixin.qq.com/s/0E3_6UkDjgr4PUhzTXkrbw
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:25:02.031023
---

# eCapture V2 来了，AI Agent 是主要重构者

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/arjmNWXmn5VP9tnUzmo3ZicGRSvJVGmMZRl3IRN6RXEeuE9AyDfYicvAMfycgtl3icichsicOTP1usVGw29Y5NRm0ZNDMJDcUbKtAc2sxJfo2C8Q/0?wx_fmt=jpeg)

# eCapture V2 来了，AI Agent 是主要重构者

原创

CFC4N
CFC4N

榫卯江湖

![]()

在小说阅读器中沉浸阅读

> 写这篇文章的时候，eCapture 已经发布到 v2.2.1 了。从 v2.0.0 到现在，短短三个月内经历了 5 个版本迭代。 趁着版本刚稳，笔者来认真梳理一下 v2 系列到底做了哪些事——不只是给用户看的 Feature，还有架构层面那些"没有功劳只有苦劳"的内功修炼。

---

## 一、先说结论

v2 系列最核心的变化可以用一句话概括：\*\*把整个项目从"能用"变成了"可以持续演进"\*\*。

表面上，你可能感知到的是：GoTLS 支持连接四元组了，pcap 写入更稳了，Android 的兼容性更好了。

但水面以下，是整个内部架构的推倒重建——原来杂乱的 `user/` 目录彻底删掉了，所有 8 个 Probe 被重新实现，工厂模式、观察者模式、模板方法模式，该用的设计模式全用上了。

---

## 第一部分：面向用户

### 1. GoTLS 终于有四元组了

很多同学用 eCapture 抓 Go 应用的 TLS 流量，一直有个痛点：抓到的明文没有连接信息，不知道这条流量来自哪个 IP、哪个端口。

v2.0.1 和 v2.1.0 里，@zenyanle 接连贡献了两个 PR（#947, #960），给 GoTLS Probe 加上了从 `tls.Conn` 里提取 fd、进而获取连接四元组的能力。

现在抓到的 GoTLS 明文，连接的源/目 IP 和端口都有了。对于要做流量审计或安全分析的同学，这个功能很关键。

### 2. pcap 写入更可靠了

v2.0.0 引入了缓冲 pcapng 写入，带上了接口元数据；v2.2.0 修掉了一个 `Close()` 里的竞态条件——之前在高并发场景下，DSB keylog 写入会出现数据乱序或丢失的情况。

现在写 pcap 文件，序列化保证了，关闭时也不会丢尾巴了。

### 3. Android 支持更成熟

* BoringSSL Android 16 的 offset 更新（#885）
* Android 模拟器的 DNS 解析问题修复（#957）
* Android e2e PCAP 模式自动探测活跃网络接口（#976）
* Build tag 从 `androidgki` 统一改名为 `ecap_android`（#930）

对于在 Android 上用 eCapture 做流量分析的同学，v2 系列的稳定性比 v1 强了不止一个量级。

### 4. 重新支持 `--cgroup_path` 参数

v2.0.0 的大重构里，`tls` 子命令的 `--cgroup_path` 参数被不小心砍掉了。v2.2.1 把它恢复了（#975）。

用 cgroup 做隔离抓包的同学，可以放心升级了。

### 5. 全覆盖的 E2E 测试体系

v2.0.0 里加入了 72+ 个 E2E 测试场景，覆盖了 bash、tls、gnutls、gotls 全部模块，以及 pcap/keylog/text 三种抓包模式。

这意味着每次发版前，核心路径都会被自动验证一遍。用户升级时踩到"老功能突然坏了"这种坑的概率，大幅降低。

---

## 第二部分：面向开发者

> Warning：以下是面向 eCapture 开发者或想给项目贡献代码的同学的内容，只是日常使用的话可以不用往下看。

### 1. 架构重构：`user/` 目录彻底消失了

v1 时代，所有 Probe 的代码都堆在 `user/` 目录下，随着支持的协议越来越多，这个目录越来越难维护——命名不统一、接口不一致、职责边界模糊。

v2.0.0 用 7 个 Phase 完成了完整的迁移：

![](https://mmbiz.qpic.cn/mmbiz_png/arjmNWXmn5UJKpJibP1z4hGRqaIKgvPma18yyskThiaCrGMUvLwASlMsyUyeFveKPPzicLStYDPkLaSgriaWD5lxyNVicP8RUJ7SAM9HOPsnKJIQ/640?wx_fmt=png&from=appmsg)

所有 8 个 Probe（Bash、Zsh、MySQL、Postgres、OpenSSL、GnuTLS、NSPR、GoTLS）完成了标准化迁移。每个 Probe 现在都有统一的文件结构：

```
internal/probe/<name>/
    config.go      # 配置，嵌入 BaseConfig，实现 Validate()
    event.go       # 事件结构，实现 DecodeFromBytes()
    register.go    # init() 里调用 factory.RegisterProbe()
    <name>_probe.go # 嵌入 BaseProbe，实现 Initialize/Start/Stop/Close
```

### 2. 核心设计模式

v2 引入了三个设计模式，彻底解耦了各个组件：

![](https://mmbiz.qpic.cn/mmbiz_png/arjmNWXmn5WiaK87dicmjcWsDnpgdjYVTfUN7efFibAVUn7g79cqQUA4nHf7uCVYs58JuIFTLoQSdWwrJpAd3GaCicPXcWaOoQ41wByvmcFCBtY/640?wx_fmt=png&from=appmsg)

* **工厂模式**：每个 Probe 在 `register.go` 的 `init()` 里自注册，CLI 命令通过 `factory.NewProbe()` 创建实例，互不依赖。
* **模板方法模式**：`BaseProbe` 实现公共流程，子 Probe 只需覆写差异化逻辑。
* **观察者模式**：事件通过 `EventDispatcher` 分发，Output Writer（file/pcap/keylog/websocket）作为订阅者，彼此完全解耦。

### 3. 事件流转全链路

从 eBPF 内核态抓到数据，到最终写入文件或推送到远端，完整路径如下：

![](https://mmbiz.qpic.cn/mmbiz_png/arjmNWXmn5VqgRKefiandMqhLeyicSxhRpGXrDXbTQ8g7iciae1LzXoCG7WCR0wwxuLibwqyTicnjOENKG2gBHjHg62UfLqKXyyA1TUkbIurOuUr0/640?wx_fmt=png&from=appmsg)

这个链路在 v2 里被完整地标准化了。之前 v1 里部分 Probe 是直接写文件，绕过了 Dispatcher，导致远端推送（ecaptureQ 模式）下数据丢失——这个 Bug 在 v2.1.0 的 #964 里修掉了。

### 4. 破坏性变更备忘

如果你有基于 eCapture 源码开发的二次开发代码，升级 v2 需要注意以下几点：

| 变更项 | v1 | v2 |
| --- | --- | --- |
| Probe 代码位置 | `user/` | `internal/probe/` |
| Build tag（Android） | `androidgki` | `ecap_android` |
| eBPF bytecode 目录 | 项目根 | `ebpfassets/` |
| Probe 注册方式 | 手动初始化 | `init()` 自注册 + Factory |

---

## 更丰富的官方文档

V2.0.0 里，官方网站也做了重构。

![](https://mmbiz.qpic.cn/mmbiz_png/arjmNWXmn5Xz2iazlZklR2MOjNicAlexNTzOQDZBFhC98xAKqsiamiaWiaGL03J0JP2PSIyZOWWF5a8gF2VNGEicPbkjPywERCvS5FfyaS2S1miblE/640?wx_fmt=png&from=appmsg)

除了官网首页，使用文档也经历了大幅度的扩充和重构，分为概述、架构设计、捕获模块、输出格式、开发指南等多个章节，覆盖了从用户入门到开发者贡献的全流程。![](https://mmbiz.qpic.cn/sz_mmbiz_png/arjmNWXmn5Vmf2TdaEqhIAUiawu3IP0BIyl4d55yX745dqqfTYCJVlCM1GIckY1vWy9t4zCZUh9JvSeGoW6kh0DhfVoRQibiats9S30OW5gmgM/640?wx_fmt=png&from=appmsg)

---

## 番外：AI Agent 写了多少代码？

最近 AI Agent 是个大热词，笔者被问到最多的问题就是：eCapture v2 里，到底有多少代码是 AI 写的？

说个实际数据。从 v2.0.0 到 v2.2.1，GitHub 上合并了约 **37 个 PR**，分布如下：

| 贡献者 | PR 数量 | 占比 |
| --- | --- | --- |
| @Copilot（GitHub Copilot AI Agent） | 13 | **~35%** |
| @cfc4n（笔者） | 21 | ~57% |
| 社区贡献者（@zenyanle、@Carl Chen 等） | 3 | ~8% |

v2.0.0 那次大重构是 AI 参与度最高的版本：8 个 Probe 的标准化迁移、E2E 测试框架搭建，10 个 PR 直接由 @Copilot 提交，占当版 PR 总量的近 \*\*45%\*\*。

再看代码行数。说实话，这个数字笔者自己都没料到会这么极端。**v2 系列 90% 的代码是 AI 写的**，笔者的角色更像产品经理加 Code Reviewer。

| 贡献者 | 新增行数 | 删除行数 | 新增占比 |
| --- | --- | --- | --- |
| @Copilot（AI Agent） | 28,426 | 10,392 | **~90%** |
| @cfc4n（笔者） | 2,097 | 781 | ~7% |
| 社区贡献者 | 1,082 | 96 | ~3% |

但聪明的同学一定想问：AI 是怎么知道该做什么的？

答案是：**每一个 AI PR 背后，都对应着笔者写的一个详细 Issue**。任务描述写得越清楚，AI 出活越靠谱；描述含糊的，烂 PR 照样打回去重写。那段时间的工作流，基本是"笔者当产品经理+Code Reviewer，AI 当执行工程师"。

AI Agent 擅长的是**模式清晰、重复度高**的任务——比如"按照这个标准模板，把剩余 6 个 Probe 全部重构一遍"，这种活交给 AI 效率极高。但涉及 eBPF 内核行为的细节、并发竞态的根因分析，还是得靠人来兜底。

v2 这次实践下来，笔者的感受是：**AI Agent 不是替代开发者，而是把开发者从重复劳动里解放出来，让人能把精力放在真正需要判断力的地方**。

---

## 最后

v2 是一次迟到很久的重构。老实说，v1 时代的 `user/` 目录，笔者自己看着都头疼。这次借着 AI Coding Agent 的帮助，总算把欠的技术债还掉了大半。

后面 v2.x 的迭代重心会放在功能上——更多 TLS 库版本支持、更丰富的过滤能力、更完善的远端推送协议。架构的活算是告一段落了。

有问题欢迎到 GitHub 提 Issue，PR 更欢迎。

* GitHub: https://github.com/gojue/ecapture[1]
* 官网: https://ecapture.cc[2]

参考资料

[1]

https://github.com/gojue/ecapture: *https://github.com/gojue/ecapture*

[2]

https://ecapture.cc: *https://ecapture.cc*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHsLicJBSCn3XGk8WbSqyUDAQp9Gh8QjlFv4FFbGo5e8L2k4tDTXa0sYGIKfVEQibnufpIibQD7EOoWQw/0?wx_fmt=png)

榫卯江湖

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IjnZ9ic9bGHsLicJBSCn3XGk8WbSqyUDAQp9Gh8QjlFv4FFbGo5e8L2k4tDTXa0sYGIKfVEQibnufpIibQD7EOoWQw/0?wx_fmt=png)

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