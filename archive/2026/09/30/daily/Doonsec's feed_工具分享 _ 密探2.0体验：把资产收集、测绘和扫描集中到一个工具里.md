---
title: 工具分享 | 密探2.0体验：把资产收集、测绘和扫描集中到一个工具里
url: https://mp.weixin.qq.com/s/DW1LmnCFS6ECJSI1AYqiiQ
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:56:18.026382
---

# 工具分享 | 密探2.0体验：把资产收集、测绘和扫描集中到一个工具里

# 工具分享 | 密探2.0体验：把资产收集、测绘和扫描集中到一个工具里

原创

小安Air
小安Air

小安数记pro

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**前言：新漏洞频发，攻击手段日新月异。这里是小安数记pro。专注网络安全领域，日常更新分享，带你穿透技术迷雾。左上角点击关注，你的支持是小编创作的最大动力。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A4gKXH0hLyBHR4vfqicpmicGbiaZFcT0QXiaia0aUy7F99CjC8feIzeOejCfu5H1BRgbdMyiallrQJkArX03eUb4sQoA/640?wx_fmt=png&from=appmsg)

由于公众号推送机制调整，现在只有**常读和星标**的公众号才会显示大图推送。防止大家找不到，收不到及时咨询，建议大家将小安数记pro按照上面图片设置为星标，之后就可以及时收到咨询！！！

**免责声明**

> 本平台所有内容（包括技术文章、工具及方法）仅供网络安全从业人员在合法授权环境下进行学习与研究，严禁用于任何非法用途。使用者需在自有或完全授权的环境中操作，并对自身行为承担全部责任。因使用本平台内容导致的任何损失，本平台不承担责任。我们保留随时更新本声明的权利，不另行通知，持续使用即视为接受修改内容。请务必遵守法律法规，共同维护健康的网络安全研究环境。本文仅展示本人自己使用推荐和分享感受，并不做任何商业行为。作者只负责分享自己实践过程。

首先感谢kkbo(虎哥)，最近拿到了一枚 **密探 2.0 VIP 激活码**，正好趁这个机会，把这个工具实际装起来体验了一下。之前其实也听过“密探”这个工具，不过这次真正打开 2.0 版本之后，第一感觉还是比较明显的：

**它已经不只是单纯的信息收集工具了。**

从项目定位来看，密探 2.0 更像是把资产信息收集、空间测绘、指纹识别、扫描、一些安全分析工具，以及现在比较热门的 AI/MCP 能力整合到了一起。

所以这篇不准备把所有功能都介绍一遍，主要就当成一次简单的工具体验，聊聊我自己简单实际使用下来觉得比较值得关注的几个地方。

## 01 先说说密探2.0是什么

官方介绍中明确提到，新版本采用 **Rust + Tauri** 开发，并针对项目管理、资产收集、漏洞检测以及 AI/MCP 等方向进行了扩展。从目前的功能导航来看，密探 2.0 大致可以分成几块：

**1.主体查询**

包括主体查询、批量主体、ICP备案查询、IP 归属、搜索语法、敏感信息等。

**2.空间测绘**

整合了包括 FOFA、Hunter、Quake、ZoomEye、Censys、Shodan、零零信安等在内的多个测绘能力。

**3.Fuzz / 扫描**

包括指纹识别、JSFinder、目录扫描、子域名爆破、端口扫描、POC 扫描、Swagger 等。

**4.工具箱**

包括 SessionKey、Heapdump、小程序相关功能、密码本、社工字典、编码解码、数据处理等。

**5.云安全**

涉及 OSS、云主机以及一些常见云平台相关检测能力。

另外还有武器库、代理池，以及目前比较有意思的 **AI 渗透、MCP、AI 助手、代码审计**等功能。

简单理解就是：以前可能需要开好几个工具，现在尝试把其中很多工作集中到一个界面里完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkUia8JJc4Qd2CuUzTpOeQx1Cict9ulWj9a7x8OdvpI9GhleLibcTXvA1M5HhkRMrBibH6EFMeKMmneF7G8iczSakUicRbyTuGdtpia7E0/640?wx_fmt=png&from=appmsg)

# 02

# 第一感觉：界面确实比以前更“工具化”了

我这次主要体验的是 V2.0.1 版本。比较直观的一个变化，就是整个软件的功能入口非常多。打开以后，可以明显看到它不是传统那种“一个工具只负责一件事”的设计。而是按照实际安全工作的流程，把功能拆成了几个模块。

例如：

```
主体查询 → 资产测绘 → 指纹识别 → 端口扫描 → 目录 / 子域名 → 漏洞检测 → 后续分析
```

这种组织方式其实比较适合做资产梳理。尤其是刚接触安全测试的朋友，面对大量工具的时候经常会遇到一个问题：我到底先用哪个？

而这种“一站式工具”的优势就在于，至少可以先把基础流程跑起来。

# 03

# 一站式功能体验：项目管理、测绘、扫描与 AI/MCP

密探 2.0 里面有不少功能，我这次主要关注了项目管理、聚合测绘、断点续扫、Heapdump、小程序分析以及 AI/MCP。

**3.1 项目管理**。

这个功能看起来没有端口扫描、POC 扫描那么直观，但实际使用中比较实用。不同测试项目的数据可以单独保存，资产测绘、子域名、端口和指纹等结果也能按照项目进行归类。

对于需要长期维护资产信息的人来说，这样可以避免不同项目的数据混在一起，也不用每次都从零开始。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkV0HoINsgZngvxfWjFpYLdG2MGfYefvsmHUezsicxaUOKmRQb6oPW8tMPejzmkLFGsAic3yCTSvCQ5Y8ZmtYnH1JQXVu97hTx2fY/640?wx_fmt=png&from=appmsg)

**3.2 聚合测绘**。

密探 2.0 集成了多个测绘平台，可以减少在不同平台之间来回切换的麻烦。同时，工具还提供了测绘语法转换功能，对于不熟悉其他平台搜索语法的人来说，使用起来会方便一些。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkXBibN6IEWruWppwyrHlOUIibPlQAkciaiaHy8VjZJa0xsc9fkOVgqc57bZ7nObicbGDD5FB75KuNhw6TXcOGsAn6gTjZf1Puexb2JU/640?wx_fmt=png&from=appmsg)

**3.3 断点续扫**。

子域名、端口、目录、指纹和 POC 等扫描任务，有时候运行时间比较长。如果中途需要暂停，之后可以继续之前的任务，不需要每次重新开始。

这个功能虽然看起来比较简单，但对于持续进行资产梳理的人来说，还是比较实用的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkW2q5fia7AOS7ZFXQ4QBWGmibX9ZcfQrWR7fYdNWnMEk5clKoNicox9SpUm4s7micAFLZsJQ4HE0LyspzZNMkdz5uBDRiaE2kmZ7jb8/640?wx_fmt=png&from=appmsg)

**3.4Heapdump 分析**和**小程序分析**功能。

Heapdump 分析主要用于解析 Java 内存转储文件，尝试提取其中可能存在的数据库连接信息、SQL、IP、JWT Token 等内容。小程序分析则可以对小程序进行解包，并提取其中的 API、URL、AK/SK 等信息。

这些功能能够帮助我们从内存文件、小程序和 API 等角度了解业务可能暴露的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkU7ib6L11SINLNNLD13GuxCS8Zoibf8Buv1CA25Viab4SSTOQeNQphwLzyBfBu8oE8nduJBKFSrvJV3NgBxBVgGDttRm5dOUCXmBo/640?wx_fmt=png&from=appmsg)

**3.5 AI + MCP**

简单来说，MCP 可以让 AI 客户端调用密探中的部分功能。以前需要手动打开工具、填写参数、等待结果，现在可以尝试通过自然语言让 AI Agent 调用相关能力。

目前这部分还需要继续体验，但从方向上来看，还是比较有意思的。以后如果能够把资产查询、测绘、扫描和分析等功能串联起来，可能会进一步提高工作效率。这些内容需要自己手工配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkWF8IJZYfr8WzsqaUVRpibshXS8Biapr8kVxOicO8ia3XW4JxxMkIdMzXeJCv1qVCEs3ILMpUPREqof3WIGI9sGpYR0Uqr1iaTibN3eo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkWDzYux0Ic1oHVMZT61XcKxUzRJZU8QC0bR3yqMd0IUQWicrEUre1vvaEz2aTxvh52JnssSYgrhmyzmTflgLrtgPMGSPzZKfskg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkUYQNSBbg3fHWribWKicibwsiblAauvZOgo1eGdSTgykOhKTQoPWQvU64haRk7bS9yJJkYWvX3T6H4aw81QnTHg3Pbic6fic93iagXGho/640?wx_fmt=png&from=appmsg)

当然，以上功能都应该在合法授权的环境中使用。测绘能力越强，越需要注意目标范围和授权边界。

3.6 武器库

还有很多的武器进行分类后，供大家进行使用，需要大家手工配置。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkWKwdBDo3jibheJdV7MUYiaqp7NczyoFDvqsV4Wg6UpylPHvxH4KuPw8ib3ZkvFIsGm9a1SpC0xT6pUofZXprLUNWia0LTVrrA6S1E/640?wx_fmt=png&from=appmsg)

# 04

# 下载与安装

# 下载地址：https://github.com/kkbo8005/mitan/releases/tag/2.0.1#/，下载完成后选择自己电脑对应的安装包安装即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkVSoaibnnQvVzmyjhr6oSBEKw5Mr97mR9QtHScJl9mtSpNic2VOcibCIickKngnbP7fGkaGR5BuQhbEHxoG5ZleicfPrKgGr6muClsk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkU8vEIlABqGialFPOZLwc7LiaQHOeRbsmYAd0tPWVWBuXQ5oIVpf1OJTDVLGaW3MISo6mlJh8YUYR3vMWiaKRmuFVKOLEeR0xvNCI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkUtvtBAibFgiad3lVR3EOpxiaUovicxeFrRQTLdckia02KGghqwX6kKI3OEMRVGJ490jv3BZPbEsiaYXASysuPy9K4XQrSvJ0DiaiacAB4/640?wx_fmt=png&from=appmsg)

# 05

# 使用感受

#

这次并没有把密探 2.0 的所有功能都完整跑一遍，所以这里也不做“全功能测评”。

单纯从第一次使用的体验来看，我觉得它比较适合下面几类人：

**第一类：刚开始接触网络安全工具的人。**

因为很多常见功能已经集中在了一起，可以减少工具切换。

**第二类：平时需要做资产梳理的人。**

主体查询、空间测绘、子域名、端口、指纹等能力组合起来还是比较方便的。

**第三类：喜欢研究 AI + 安全的人。**

MCP 这一部分目前比较值得继续折腾。

当然，真正做项目的时候，还是需要结合自己的经验和一些 如（Burp、Nmap、各类测绘平台、漏洞验证等）工具以及自己编写的脚本一起使用。

所以我更倾向于把密探理解成：方便大家进行操作的一个完整的安全工作台。

# 06

# 总结

现在安全工具越来越多。以前大家比的是：谁的扫描更快、字典更多、POC 更多。现在开始慢慢加入：项目管理、数据关联、自动化、AI、MCP。

这其实是一个挺明显的趋势。而密探 2.0 这次让我比较关注的，也不是某一个具体扫描功能，而是它正在尝试把：（资产 → 测绘 → 扫描 → 分析 → AI）这些东西连接起来。所以这篇就先当成一次简单的“开箱体验”。后面有机会，我还会继续折腾一下它的 **MCP + AI** 部分，看看把它接入 AI 客户端之后，实际使用起来到底怎么样。

提醒：密探 2.0 本身属于安全测试类工具。无论是资产测绘、端口扫描、目录扫描还是漏洞检测，都建议只在自己拥有、明确获得授权，或者专门搭建的靶场环境中进行测试。工具本身不会替你解决授权问题。技术没有问题，用错地方才会出现问题。

**再次强调，能力越大，责任越大。希望我们都能用技术去守护，而不是破坏。记得给小编点个“赞”留个关注！！！**

> ⚠️ 郑重声明：所有内容均用于合法安全研究，请务必在授权环境下进行测试。做个白帽子，很酷。
> 📮 欢迎交流讨论评论。如果觉得有用，不妨点个“关注”和 “赞”支持一下。

每一次技术解读、每一篇实战记录，都源于大量时间的测试、验证与梳理。如果这份指南为您打开了新的思路，或为您节省了宝贵的时间，不妨给小编进行简单的打赏，支持更多深度内容的诞生。您的每一次点赞、在看、分享，都是我们持续分享的动力；而直接的赞赏，则是对原创内容最温暖的鼓励。

让我们一起，用技术观察世界，用分享传递价值。

感谢您的阅读与支持！

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/A4gKXH0hLyCe2Q4gcyXQPHnqU5YggpSQ0m5iaaro6s7jIDzvEnx8fJWfd2SPPdPXLq44aspBGXtGgAibbENDVfeg/0?wx_fmt=png)

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