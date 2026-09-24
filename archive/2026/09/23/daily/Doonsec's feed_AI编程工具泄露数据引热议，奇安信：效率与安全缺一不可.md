---
title: AI编程工具泄露数据引热议，奇安信：效率与安全缺一不可
url: https://mp.weixin.qq.com/s/27YWv8dQEQ2_mKeR5CkG9g
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:00:23.389241
---

# AI编程工具泄露数据引热议，奇安信：效率与安全缺一不可

# AI编程工具泄露数据引热议，奇安信：效率与安全缺一不可

奇安信集团

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一个313MB的加密包，揭开了一场信任危机。

近日，某大模型公司旗下AI编程工具被开发者曝出：在用户登录状态下，该工具会后台静默打包整个项目工作区——包括完整Git历史、LFS大文件缓存、reflog等敏感文件——本地加密后上传至云端。加密使用的RSA公钥由服务端下发，私钥只存在云端，用户本人无法解包。更关键的是，这一上传机制默认常开，客户端界面中没有任何开关能将其关闭。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mSqhDgeKrPAicdlOMGiaTcVlsPj8mY4FgfaKLq1eRxQsXzympNyjw0sVMQjk7C6qI4V8wxBvXxmg6FKgH5CjPUCvUz63TeOby1utGwv5RWTNc/640?from=appmsg)

事件曝光后，该企业迅速致歉并完成整改。但由此引发了一场研发效率和安全治理如何平衡的热烈讨论。奇安信安全专家认为，在AI编码工具实现研发提效的同时，安全是不可失守的底线。换句话说，AI研发不能只追求代码生成速度，效率与安全必须同步建设。

![](https://mmbiz.qpic.cn/mmbiz_png/34bX0ofe9LJUj831WdFzgc71DrH4ZdXgrTARtsx2FYUl04d2ibVxfOhqrBtuoLVd3zDCJDtibXfFIdicEWp7uZ0PQ/640)

这不是孤例：AI编程工具的安全隐患正在集中爆发

2025年7月，Replit的编程Agent在用户明确指示冻结代码更改的情况下，仍删除了生产数据库；2026年2月，Check Point披露Claude Code的配置漏洞可能导致API凭据泄露；2026年7月，Wiz披露Cursor等工具存在权限问题，用户以为批准的是一次文件修改，实际却可能触及工作区之外的敏感文件。

这些事件指向同一个问题：当AI编程工具从“补全”走向“自主执行”，从“单文件”走向“全项目”，权限边界和数据流向的设计，正在成为企业安全的新短板。

浙江大学网络空间安全学院副教授张秉晟指出，用户“主动过度放权”是普遍现象，但“如何既安全又不过多干预用户隐私，仍具有挑战性”。网络安全正高级工程师袁博则强调：“Git历史记录的信息量更大更全，非法获取Git历史数据的危害性显然更大，数据泄露造成的影响将远超当前代码。”

一个看似“技术优化”的功能，实际上可能是在用户不知情、无法控制的情况下，将企业核心资产的整体副本送往云端。

![](https://mmbiz.qpic.cn/mmbiz_png/34bX0ofe9LJUj831WdFzgc71DrH4ZdXgrTARtsx2FYUl04d2ibVxfOhqrBtuoLVd3zDCJDtibXfFIdicEWp7uZ0PQ/640)

谁来守住AI编程工具的权限边界？

这场争议的核心，是一个被很多人混淆的技术边界问题。

AI编程工具要帮助用户理解和修改项目，确实需要读取代码。但“读取”和“上传”是两回事。读取若发生在本地或企业内网受控环境中，数据始终在企业安全边界内，风险是可控的；一旦上传云端，企业就失去了对存储位置、保留周期、使用方式、共享对象的掌控。

更值得警惕的是，Git不只是一份“当前代码”的档案，它保存着过去的版本、被删除的文件和修改痕迹。已删除的密钥、历史版本的敏感配置、开发者的提交习惯，都可能藏在Git历史中。

![](https://mmbiz.qpic.cn/mmbiz_png/34bX0ofe9LJUj831WdFzgc71DrH4ZdXgrTARtsx2FYUl04d2ibVxfOhqrBtuoLVd3zDCJDtibXfFIdicEWp7uZ0PQ/640)

奇安信：AI研发不能只追求代码生成速度

就在这一事件发酵的同一天，9月20日，第28届中国国际软件博览会在郑州开幕。奇安信集团董事长齐向东在主旨演讲中指出：“智能体的深入应用，让安全成为一道‘必答题’。”

齐向东强调，智能体重构软件，重构的不只是代码，更是企业的生产方式、权限结构和责任链条。他提出的核心原则是：把智能体画在圈里，管好“手脚”。具体要落地部署圈、连接圈、权限圈、数据圈、审计圈——工作智能体统一上云不装终端，所有连接走AI安全网关，权限绑定到人、最小必要、可撤销可复审，数据不落地、边界清晰，全程留痕、先留痕再放权。

奇安信AI原生研发平台QAgent Fabric的理念，正是这一原则在AI研发场景的落地实践：把AI智能体纳入企业现有研发体系，以统一入口承载研发智能体，连接项目上下文和研发工具链，通过可信模型、权限控制、隔离执行、过程审计以及质量与安全门禁，让AI在可控、可追溯的前提下完成从需求到交付的研发闭环。

![](https://mmbiz.qpic.cn/mmbiz_png/mSqhDgeKrPCpW1bq6VTSQ0yibycf3rNoibUylB8nV9c9T64ossrxvuPzfSAOhd3zJMLS7arcjLINMH2yaXGAHicskr6FHiaXeszpyt8SozfCribk/640?from=appmsg)

正如奇安信安全专家所强调的，随着智能体具备读取代码、修改文件、执行命令和调用工具的能力，风险已经从传统的内容安全，延伸到代码、数据、权限和执行环境安全。效率与安全必须同步建设。

为此，奇安信还推出了智能体安全管理平台，它以“看得见、管得住、防得住、说得清”为核心价值，通过智能体安全插件自动发现企业自建、商业获取、私自安装的各类智能体资产，通过AI安全网关统一管控连接行为，通过智能体安全管理平台汇聚研判，形成“发现—研判—定位—处置—优化”的完整闭环。没有留痕就不给授权，没有审计就不能扩大使用范围。

![](https://mmbiz.qpic.cn/mmbiz_png/mSqhDgeKrPCblO2d8EuIYZkEGXSicqTOeico2DGLqhEmmI2O2K3QJQv5BPDI52NZicju6aicU46oktYS9LUcpRKeo1xMP4fdK3dULB71vKwRzEk/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/34bX0ofe9LJUj831WdFzgc71DrH4ZdXgrTARtsx2FYUl04d2ibVxfOhqrBtuoLVd3zDCJDtibXfFIdicEWp7uZ0PQ/640)

AI编程工具，效率的前提是安全和信任

企业选择这类工具时，应该追问的不仅是“模型强不强”“补全快不快”，而是更根本的四个问题：

* 边界在哪——它能访问哪些目录、执行哪些命令、访问哪些网络域名；
* 上限在哪——一次任务的时间、token、花费有没有硬上限；
* 痕迹在哪——它做过的每一步，事后能不能查；
* 数据在哪——数据存在本地还是云端，是否出境，保留多久，谁能访问。

AI编程工具的效率红利是真实的，但效率的前提是信任。当AI从“辅助工具”变成“数字员工”，企业敢把代码、数据、流程交给它，前提是先把它的“手脚”管起来。没有安全作为底座，再快的代码生成速度，也如同在流沙上建高楼，效率虽然提升，但隐患随时爆发。

正如齐向东第28届软博会的演讲主题：智能体重构软件，效率要提上来、风险要管得住。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarwCHGK4V5d5pFicUo1yED6dkswm0BfC0ncqh9D2G8Rvuelo3qdHlWFv4KMF78FsOIEKiaJrgmdIlJw/0?wx_fmt=png)

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