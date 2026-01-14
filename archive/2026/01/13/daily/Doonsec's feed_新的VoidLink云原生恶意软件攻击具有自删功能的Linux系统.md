---
title: 新的VoidLink云原生恶意软件攻击具有自删功能的Linux系统
url: https://mp.weixin.qq.com/s/PLal_IkP17XEh6wROmhpXg
source: Doonsec's feed
date: 2026-01-13
fetch_date: 2026-01-14T03:34:02.655365
---

# 新的VoidLink云原生恶意软件攻击具有自删功能的Linux系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dzJiaU8Wt1qwd5micNeuJRweZcicvcEvh9JtibMc5EwtJicIR24lg7b7DLLHrHiaSJBEqZdUpCjvD4aDAIspLT0qtouQ/0?wx_fmt=jpeg)

# 新的VoidLink云原生恶意软件攻击具有自删功能的Linux系统

原创

O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qwd5micNeuJRweZcicvcEvh9JKqmVa47yTacluEb4ibRUqvbb5ELhovFv7SHosQVYUb79o6hcsyEh5zQ/640?wx_fmt=png&from=appmsg)

一种名为VoidLink的新型云端恶意软件框架已出现，针对Linux系统，具备先进的规避技术和自删功能。

该恶意软件采用Zig编程语言编写，代表了威胁行为者处理云基础设施攻击方式的重大转变。

VoidLink以其识别AWS、GCP、Azure、阿里巴巴和腾讯等主要云环境的能力而脱颖而出，并根据每个平台定制其行为。

该框架可以检测其运行在Kubernetes或Docker容器中，并据此调整策略。

Check Point 研究人员于2025年12月发现了此前未知的 Linux 恶意软件，发现了包含多个调试符号和开发伪影的样本。

这些样本似乎来自讲中文的开发环境，表明该框架仍在积极开发中，而非成品。

该恶意软件针对管理云基础设施的软件工程师和管理员，可能为间谍或供应链攻击打开大门。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qwd5micNeuJRweZcicvcEvh9JiaLALE75IedcBV9rzbG3XCly5Hs33xYMDRiazjpn70ObON5b1tK2ric1Q/640?wx_fmt=png&from=appmsg)

该框架包含37个以上的插件，分为侦察、凭证采集、横向移动和持久化等类别。

这些插件作为目标文件工作，运行时加载并直接在内存中执行，类似于 Cobalt Strike 的 Beacon 对象文件。

VoidLink 从云环境和版本控制系统（如 Git）收集凭证，使攻击者能够访问敏感的开发资源和云基础设施机密。

## **自适应隐形与自我删除机制**

VoidLink以自适应隐身为核心防御机制。恶意软件启动时会扫描已安装的安全产品和内核加固技术，包括Linux终端检测和响应系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qwd5micNeuJRweZcicvcEvh9JgBSAicedPgk9pd30N0ibK3eHiah3b9UWdAUlTx8IvDUfc8oXCFiasrMFLg/640?wx_fmt=png&from=appmsg)

然后计算环境风险评分，并选择最佳规避策略。在高风险且有主动监控的环境中，VoidLink 会放慢运行速度，更谨慎地执行任务以避免被发现。

该框架根据检测到的内核版本部署不同类型的rootkit。

对于4.0版本以下的内核，它采用LD\_PRELOAD技术。对于支持eBPF的内核版本5.5及以上，它部署基于eBPF的rootkit。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qwd5micNeuJRweZcicvcEvh9JDpDxuvqicW9umW5D5ibkkl2MrztAva9W0QOagVhrPqgu28xw3y1sPibIg/640?wx_fmt=png&from=appmsg)

对于4.0及以上的内核，它安装可加载的内核模块。这些rootkit隐藏进程、文件、网络套接字，甚至rootkit模块本身，不被系统管理员和安全工具发现。

VoidLink 包含自修改代码，可在运行时解密受保护区域，并在未使用时加密。

这种技术帮助恶意软件躲避查找可疑代码模式的内存扫描器。该框架不断执行运行时完整性检查，以检测安全工具可能引入的钩子和补丁。

如果VoidLink检测到任何篡改或调试尝试，会立即触发自删除机制，清除感染系统中的所有痕迹，阻止取证分析。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

O安全研究员

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

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