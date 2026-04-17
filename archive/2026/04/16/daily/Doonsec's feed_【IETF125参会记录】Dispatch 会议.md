---
title: 【IETF125参会记录】Dispatch 会议
url: https://mp.weixin.qq.com/s/y-5mhOPRZVqXMi1xERZeRQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:43:36.791130
---

# 【IETF125参会记录】Dispatch 会议

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kGhLgo0BUA78ZPo0gFhACnkh8OlUYRnkeqaOXdhEnbylKROjfy2u4vibuYiasx8tzRriblzXiaBR5eEC1nibTOOMPiankRkzoGf98LHlCuYiaZoPzA/0?wx_fmt=jpeg)

# 【IETF125参会记录】Dispatch 会议

原创

crackme.net
crackme.net

crackme安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

参会日期：2026-3-16 星期一
参会时间：09:00 - 11:00
参会地点：Grand Ballroom 3
会议领域：ART（应用与实时）
会议名称：Dispatch

~~别问为啥现在才发，因为我懒，想起来还有个公众号的时候已经是一个月后了~~

# Dispatch 工作组

![](https://mmbiz.qpic.cn/mmbiz_jpg/kGhLgo0BUA5VdtzkIHX6IPVpjA6ggvIoYqlLtiadwbqQw56o4I5yG5WW5o9vE16Yd4icNk4mW5rwAKhnntO08pTic1E3vE5LkcSQ9wSYicSiaqWY/640?wx_fmt=jpeg&from=appmsg)

Dispatch 工作组属于应用与实时领域（ART），不负责制定具体的草案与标准，而是评估新的草案，并为其找到合适的工作组。所以，参加这个工作组的会议，可以了解到可能即将标准化的新协议。

在本次会议中，共举行了 10 个草案报告，我将选择和自身专业相近的报告进行简要解析

# The 'donau' URI scheme for validation of donation statements

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA7vMzc7aiaO48d7qkpdricOwHh39sFe36meMC6tCRSeFUjwx9jjYJpLib62MjGlyxztvGKKSzgnonsNh4V2PJ6EHIbscdvYLXYfYI/640?wx_fmt=png&from=appmsg)

https://datatracker.ietf.org/doc/draft-grothoff-donau/

该草案定义了一种统一的 URI 格式，能让捐款者向税务局证明其捐款行为，同时保护捐款者的隐私（不让税务局知道捐款者捐给了哪家慈善机构）。底层密码学原语并不复杂，仅仅涉及简单的签名操作

该草案中，分为三个主要角色：

* • 捐款者：进行了捐款行为，并希望获取税务减免同时保持匿名性
* • 慈善机构：接收捐款，并签署捐款证明
* • 验证器：由税务局运行，用于验证捐款证明的真伪

捐款与纳税流程如下：

1. 1. 捐款者通过某种隐私协议向慈善机构捐款（Donau 解决“税务申报环节的隐私”，而不是“支付环节的隐私”，所以应该使用哪种匿名支付方式是用户的事情）
2. 2. 慈善机构的对这笔捐款进行数字签名，并生成一个 URI（本协议的核心）

```
donau://<服务器地址>?year=<年份>&id=<加盐哈希的捐款者ID>&salt=<盐值>[&total=<金额>&sig=<算法>:<签名>]
```

1. 3. 捐款者将签名后的 URI 发送给税务局，税务局验证签名

# Consolidated Parameters Part for Multipart/Form-Data

![](https://mmbiz.qpic.cn/mmbiz_png/kGhLgo0BUA4h3OPdSy55lsXPVQty5CVBkahpg7P74XVKqVj3wSQxtazQ2cdbo8D7ZRFXMae5xLCAdy7xdUTibgLf4As4jHxsic2C3UHgAvtjY/640?wx_fmt=png&from=appmsg)

https://datatracker.ietf.org/doc/draft-motiwala-consolidated-multipart-params/

根据现有的 HTML 标准，当提交包含文件上传的表单时，必须使用 `multipart/form-data` 编码，每一个表单字段都会被封装成一个独立的 MIME 部分，当表单中包含大量文本字段时开销巨大（传输一个仅含 20 字节数据的文本字段，可能需要约 100 字节的额外开销，膨胀了 4-6 倍）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA5t8La3TjGg7JIIvBTqXiaQKUoicMEHX6RJoOSOEXhgJAyhQDpwOPpPraXstMAwj2BuSjtuY94M6wcecDMEias5fMRnQdkpJl96e4/640?wx_fmt=png&from=appmsg)

该草案提出了一种名为 `Consolidated Parameters`（合并参数）的操作模式，用于优化 `multipart/form-data` 请求的开销，核心原理如下：

* • 原有的文件上传部分保持不变
* • 文本字段使用 URL 编码后，合并到一个 MIME 部分中，并将该部分的 `Content-Type` 设置为 `application/x-www-form-urlencoded`

![](https://mmbiz.qpic.cn/mmbiz_png/kGhLgo0BUA5Sickiaerx3m19PlUyOTsHHice1WWCiazNzyzuF3QOiaciadLGHNawynnJDHBd8pURASjoK3KialfDXSsNV5JEibszKnRpJk97P3gpuM0/640?wx_fmt=png&from=appmsg)

该草案实现简单，不对现有标准进行修改，兼容性强。如果服务器不支持这种优化，它会将这个合并的 MIME 部分视为一个普通的 URL 编码的文本字段，仍可以通过现有的解析逻辑手动提取数据，不会导致请求失败

# Security protocols that optimized for non-web and PQC

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA4kmM6CUJnkbXwLFasgTm2kEopTE6EFKian0BWuuw66oItd6oufwJlUEibsXtwsMJrXicKocnZvtmJSg7Lib0EXE7VHW4EHzd0aPVo/640?wx_fmt=png&from=appmsg)

此次报告主要讨论了如何利用消息层安全（MLS）的连续密钥协议（CKA）来在计算资源受限环境中（物联网、工控系统等）实现前向安全、妥协后安全和抗量子安全的密钥管理，同时显著降低计算和带宽开销，并支持异步通信。

为了实现计算资源受限环境中的通信加密，新的密钥管理机制必须（MUST）和应该（SHOULD）满足的要求如下所示：

**必须满足（MUST）**

* • 支持第 3 层和第 4 层（网络层和传输层）
* • 异步密钥更新
* • 后量子密码学（PQC）
* • 前向安全（FS）
* • 妥协后安全（PCS）
* • 可形式化分析的安全性

**应该满足（SHOULD）**

* • 异步通信支持
* • 支持群组（多播）和点对点（单播）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA4vJgicYctcia1Uxrdo6jFHfk4hTvRkg5eXFs5GBhs8ca2iahWz4kg7WHUCznria18SWmTtv1hSUxwc52ku0vDTywmmlyr3WoocnpU/640?wx_fmt=png&from=appmsg)

为了实现这些要求，MLS 的 CKA 密钥管理机制是极佳的设计。在 CKA 中，只需进行一次初始会话建立，之后即可进行异步密钥更新，且能将后量子算法的大开销分摊到每条消息中，降低整体加密开销

以 TLS 为例，报告提出了两种将 MLS 的密钥管理机制应用于现有协议的方法

1. 1. 作为 TLS 握手的扩展来引入 MLS 密钥管理，随后继续使用标准的 TLS 记录协议（参考草案：`draft-housley-tls-using-mls-handshake`）
2. 2. 在独立端口上运行 MLS 握手，建立连接后再接管 TLS 记录协议（参考草案：`draft-kohbrok-mls-tls`）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA6Xyu1y2GSwhQAM2l0FmziaYRNlfOZo27AfaGCzOJ6riaBwRwEAsUqbelpmXNucTL0uNAhFicpKseDPQC4hmVz5ml60645MaZ4vRw/640?wx_fmt=png&from=appmsg)

X3DH 密钥交换算法、双棘轮加密算法及 MLS 协议将在公众号以后的文章中详解（不得不佩服，Signal 的算法设计的是真的优秀，以致于成为了行业标杆，不仅被标准化为 MLS 协议，还被现在更多的端到端加密即时通信软件借鉴）

# Well-Known URI registration policy

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA4KiaZ3jnSEavyNjOHCahBdDIsRsmjAgB1hhtCyZ7PIcaStTM2VR4kNicTUicaqXMgZJbpN2Hkic4hXI3tRWgh4o0B84Sia4aEOCb1Y/640?wx_fmt=png&from=appmsg)

这次报告讨论了当前知名 URI 注册机制面临的问题，并提出了可能的改进方案

目前的知名 URI 的管理依据是 RFC 8615，注册时需基于一位或多位专家的建议，注册命名规范如下：

* • 必须符合 RFC 3986 中的 `segment-nz` 格式（即不能包含 `/` 字符）
* • 名称应精确对应特定应用，不鼓励抢注通用术语（例如，谷歌需要为自己的 AI 应用注册知名 URI，应该选择 `google-ai` 而不仅仅是 `ai`）

尽管有上述规则，但依然出现了一些令人担忧的趋势：

* • 命名空间是人类可读的，因此某些“短小精炼”的名称（`ai`）比其他名称（`some-company-ai`）更具吸引力，这导致了抢注滥用行为的时有发生
* • 最新的修订版有意限制了专家的裁量权，试图接近“先到先得”（FCFS）的注册模式
* • 越来越多的抢注滥用行为发生，抢注者往往缺乏社区讨论或共识的证据，引用的规范质量存疑。这种做法消耗了宝贵的命名资源，并可能给不成熟的协议带来误导性的“合法性”

![](https://mmbiz.qpic.cn/mmbiz_png/kGhLgo0BUA4KRpEfWYic7XvuIXqP4r5zJ4LuiadsydHkaxcibwRx4fTw4RlB5y2daoMOweX5JxsgawicpbjzeazkZKEE7CYDibQddXKtzslHJdaY/640?wx_fmt=png&from=appmsg)

报告列举了几个近期的典型“抢注”案例，说明问题的严重性：

* • 某人请求注册 `agents.txt`, `agents.json`, `agent.txt`, `agent.json`, `ai.txt`

+ • 规范仅存在于个人 GitHub 仓库
+ • 单一贡献者
+ • 其中 `ai.txt` 可能与某个工作组现有的工作冲突
+ • 没有任何更广泛的社区参与迹象

* • 某人请求注册 `agent.json`

+ • 规范位于某个组织的 GitHub 仓库，但该组织可能只有一名贡献者
+ • 网站托管在 GitHub Pages 上
+ • 同样缺乏社区参与

* • 某人请求注册 `ai`

+ • 规范位于一个两人的 GitHub 仓库（两人同姓）
+ • 除了他们与案例 A 的提案者有过交流外，无其他社区参与

之所以经常发生抢注滥用行为，可能存在以下几种原因：

* • 抢注者似乎混淆了“注册”（Registration）和“标准化”（Standardisation）的区别，存在一种“只要注册了，大家就会来用”的心态（投机主义）
* • GitHub + Markdown + AI 的搭配使得创建协议草案的门槛极低
* • 尽管 RFC 8615 提到了防止抢注，但并未直接解决这种利用低门槛进行投机性注册的问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA7mkg9cict6kOEia23fpPZzziagpUVwgg0Meq31S0tBRtGxPyr2cdXURw2Slw1wDIOcK4UMVHrAQSswiaD7fibwJiazsChm0PHctgchc/640?wx_fmt=png&from=appmsg)

为了解决此问题，本报告提出了一些可能的解决方案供讨论：

* • 加强注册审查，允许专家拒绝那些有吸引力的名称的请求，除非它们已经经过了一定程度的社区共识
* • 强制在名称前加随机数字（例如 `/.well-known/2462356-foo`），但这会破坏人类可读性
* • 建立一个限制较少的子空间（例如 `/.well-known/adhoc/foo`），进行“临时注册”

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f2j8DeXVicRQ9KGpr3vDNkdIwyasHFEWCmJibCSicITuAqbVgkygYicev0lUCVEj7B2XfSpnEhs6o7mVylZW5gzorA/0?wx_fmt=png)

crackme安全实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f2j8DeXVicRQ9KGpr3vDNkdIwyasHFEWCmJibCSicITuAqbVgkygYicev0lUCVEj7B2XfSpnEhs6o7mVylZW5gzorA/0?wx_fmt=png)

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