---
title: HTB-Redeemer：Redis 基础知识分享
url: https://mp.weixin.qq.com/s/iqySqOIOmYkeddCjMYQpKA
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:01:49.275090
---

# HTB-Redeemer：Redis 基础知识分享

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/v7ntTxZACkWExvYIaxXUrLoCVnPXevwsM903enmSFjDI0mQxzP84g0pG6joAtbssq0bpjnFyRhpxfxaricsqsxSIrwGGeXtnYtQvTmuCRibuw/0?wx_fmt=jpeg)

# HTB-Redeemer：Redis 基础知识分享

原创

小安Air
小安Air

小安数记pro

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**前言：新漏洞频发，攻击手段日新月异。这里是小安数记pro。专注网络安全领域，日常更新分享，带你穿透技术迷雾。左上角点击关注，你的支持是小编创作的最大动力。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A4gKXH0hLyBHR4vfqicpmicGbiaZFcT0QXiaia0aUy7F99CjC8feIzeOejCfu5H1BRgbdMyiallrQJkArX03eUb4sQoA/640?wx_fmt=png&from=appmsg)

由于公众号推送机制调整，现在只有**常读和星标**的公众号才会显示大图推送。防止大家找不到，收不到及时咨询，建议大家将小安数记pro按照上面图片设置为星标，之后就可以及时收到咨询！！！

**免责声明**

> 本平台所有内容（包括技术文章、工具及方法）仅供网络安全从业人员在合法授权环境下进行学习与研究，严禁用于任何非法用途。使用者需在自有或完全授权的环境中操作，并对自身行为承担全部责任。因使用本平台内容导致的任何损失，本平台不承担责任。我们保留随时更新本声明的权利，不另行通知，持续使用即视为接受修改内容。请务必遵守法律法规，共同维护健康的网络安全研究环境。本文仅展示本人自己使用推荐和分享感受，并不做任何商业行为。作者只负责分享自己实践过程。

# 一.介绍

## 1.1 机器信息

Redeemer 是一个非常简单的 Linux 机器，它探索了 Redis 数据库服务器的枚举和利用，同时展示了 redis-cli 命令行实用程序和与 Redis 服务交互的基本命令。

1.2 什么是Redis数据库服务器

Redis 是一个基于内存的高性能键值数据库服务器，主打极快的读写速度，支持字符串、哈希、列表、集合等多种数据结构，既能当缓存扛高并发、减轻数据库压力，也能做计数器、排行榜、分布式锁等，通过 RDB/AOF 机制把内存数据持久化到磁盘，配合主从复制、哨兵和集群模式实现高可用，是互联网系统里最常用的“加速外挂”。

它属于**缓存中间件 / 数据存储中间件**，也常被归进**NoSQL 中间件**一类。泛指应用和底层（数据库、操作系统等）之间的"中间层组件"。Redis 的位置是**架在应用和关系型数据库之间**的那一层——应用先查 Redis，命中就直接返回，没命中再去 MySQL 这类磁盘库取，顺便回写 Redis。所以它最标准的标签是**缓存中间件**；但因为它本身也能持久化、能独立当库用，所以也有人叫它**内存数据中间件**或**NoSQL 中间件**。**Redis 管“快”和“热”，MySQL 管“稳”和“全”**。

The CLI：命令行界面（CLI）是一种功能强大的工具，它能够让你全面访问 Redis 的数据及其各项功能。如果您正在开发一款需要与之进行交互的软件或工具，则需考虑其功能特性。

数据库：该数据库存储在服务器内存中，以便实现快速数据访问。Redis还会记录其中的内容以不同的间隔将数据库转存到磁盘上，以便将其作为备份保存，以备不时之需。

# 二.靶场信息

* 目标：Redeemer
* ip：10.129.122.34
* 本机ip：10.10.17.121
* 操作系统：linux

# 三.过程

### 1 测试一下连通性

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkXZSzDcLpBZ3FXfDnjh14eian4VibVCs5gJO5pp1fPHS3VpUibvxwTJZ41owicc8zB1vykCq9QbQoYgRNG8zb6dIicicHs5nVb12rGGk/640?wx_fmt=png&from=appmsg)

### 2 端口扫描

#### 2.1接着使用Rustscan进行端口扫描

```
rustscan -a 10.129.122.34
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkWbcP2bf2aN1q1FFPfuib1oTpFpKFQ3YJrlQNibtozd6eLCbwibmT1gjkEQ3CtgGicianUO7M0YibXLKQnt9KTfxib3O92yI8o0kPuODY/640?wx_fmt=png&from=appmsg)

发现一个可用tcp端口6379

#### 2.2使用nmap进行端口扫描

```
nmap -Pn -sC -sV 10.129.122.34
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkVErIrHricFBlibol0ibUXtU6Z8dXxBXOicUrowUnYpMOSuzmC1ic3Xic3LalRp0wkjJ3Nmc9jlzX3GPGjneK5uUfBkB13yYoErOLg2g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkWSEtxV6Q1QCRicNT2pGxzticu5Gh7E0h8uHbC4SXLZbnLSMBprq9EmcpuSBHgkAxqDO023ZULxVEZvkeZibhaDIyNPd0DsEhUtQE/640?wx_fmt=png&from=appmsg)

所以由此可知，6379对应的默认服务是：Redis

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkX6X6EsK7yaCaE8lodzQvnadRe2L5C7YzBlNMtPQc4Jkdkru7hurKQky9smkN7URr6goviczCfHtkFX2epiaJNrXLqqKTvxSI0x0/640?wx_fmt=png&from=appmsg)

根据上面对于Redis的介绍可知，Redis是内存数据库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkWKHLP05nRhP5yXBvCUHjP6aibhyGQZiatg5jRSR5Dmh3SibBbibFAE0prQVPyW7LibeFRxhNH4IaLmIru6kyQz1O8nPPT5OgHwdswE/640?wx_fmt=png&from=appmsg)

 用于与 Redis 服务器交互的命令行工具是 ‌**redis-cli**‌。‌‌

* **名称**

  ‌：redis-cli（Redis Command Line Interface）
* ‌**来源**‌：Redis 官方提供
* ‌**用途**‌：连接 Redis 服务器、执行命令、管理数据及监控状态
* ‌**基本用法**‌：直接运行 `redis-cli` 连接本地默认端口（6379）；支持 `-h`（主机）、`-p`（端口）、`-a`（密码）等参数连接远程或受保护实例。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkXhnOqXg0wicayPibLI2IXCCkUMxWZRAQujvU8kgu9fCBoQKpFbmS9ib33GOgydd8icpbOdn8bib2GiaHsUfG74acXiauiaDzeluZYUeSE/640?wx_fmt=png&from=appmsg)

想知道在 Redis 命令行工具中，使用哪个标志来指定主机，我们可以使用下面指令，来找到主机名是使用 -h。

```
redis-cli --help
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkWQzVsxquiaWUVIs7F2iaaoHBkaZd6jT8ia2kEibcLhfaOOEBDuor0c4RrQDgTxibI6dOhkghGGCjF5U1QGtlQ0GpqMhCms39y9cZ2U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkW9LxmnbyhiccowkyTuSKaWnLyaG4jX3tJHNP41wpeASDA06IfGqWSStzoyCjjI8NRQbbSqH3Bg9cRp2jp5z2maQjkibrCkibwbns/640?wx_fmt=png&from=appmsg)

连接到 Redis 服务器后，使用 ‌`INFO`‌ 命令获取服务器的信息和统计信息 。‌‌

* **基本用法**

  ‌：输入 `INFO` 可返回所有维度的完整信息（默认等同于 `INFO all`）。
* ‌**指定维度**‌：支持添加参数仅获取特定部分，如 `INFO server`（常规信息）、`INFO memory`（内存）、`INFO stats`（统计）、`INFO clients`（客户端）、`INFO replication`（复制）、`INFO cpu`（CPU）等。
* ‌**组合查询**‌：可同时指定多个参数，例如 `INFO server memory` 获取服务器常规及内存信息 。‌‌

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkUTDibEcZzMnf6MrneMF5t3MgZ4ELOmm6w1UWPoh0M2eWzGsnP21viaiaBoxmhsEoNJqohM0tqPJFibMH8fic1jJIIHxStFHog19SUY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkXnQyH4V6RxAhHbLjIicHSNRk9COmxUMKsyjIwj4icVAV2d9bES4gnNlTTEfUGPgfV4kR4dficib21DCcWjwyicVISSdnBOEjeGb95E/640?wx_fmt=png&from=appmsg)

目标机器上使用的 Redis 服务器版本：**如果你只是想查看 Redis 客户端版本**，请在操作系统终端使用 `redis-cli -v`或`redis-cli -version`。**如果你已经在 Redis 交互环境中，想查看 Redis 服务器的版本信息**，可以输入：`INFO server`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkXK2IQOdSKNdib8lhaVHBGvtvBlyDaurVDhwv0JaS41VKEJd97TKYjmPQhWE2guG9Phq81ibicRL7MH0WlFn7Imqz1a7UAukdpLyE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkU4XOhCOqFTCBZ0FtCldJUVGa4QTD5VR8qU9oXMLwZJ8dTBSzhGq8GW3rTfx2Eqsia6sFpWX2I4zHwNLDwSUuvZetJ3hufGybkM/640?wx_fmt=png&from=appmsg)

8.在 Redis 中，使用 `SELECT` 命令来选择所需的数据库。

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkWotm4aThO3TXtYUFkq6EP9tpVlhRbfg0vnhU2ojBibNxT7x1p4d6PiaMhAVERhXIkT4fKJY9l2DI752JOv2qSCibu9SQpyllKh70/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkVJZ26ZTDlILHkHJrWBdllAH6v9jMiboGtODAVAibHOIQsbl1dZibsz8bD15CLcLRGbQ2B3CvAiaOpdA8ZA9v0BkGrlKiaPL2icYdia5U/640?wx_fmt=png&from=appmsg)

9.要查看 Redis 中索引为 0 的数据库中有多少个键：

**1.先切换到数据库 0**（如果当前不在该库）：

```
SELECT 0
```

**2.然后执行**`DBSIZE`**命令**，它会返回当前数据库的键总数：

```
DBSIZE
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkXONFzIRs1dpzcyzRrstbbqBT8oWj5SfTQ6ibSZeBya4l3MA0gianDEQ9iaNKylcKHhkfX7WKHVxvqJxbOh7QHP5cQUbbdmcjxAKY/640?wx_fmt=png&from=appmsg)

另一种方式：不切换数据库，直接查看所有数据库的键数量

使用 `INFO keyspace`命令，可以一次性看到每个数据库的键数统计：

```
INFO keyspace
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkUGWiceAZNeqBSXGibh3p9dXmw8Db9x1exTJLMXhMLicFlebnJbBPAaEgicicTcpHsvmxuGOAja0gfPYHYgicFZVmgc44TYgbQ72XMia8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkUzYzkv1SPD9wMnv8cb0LItNpyYlXp9UWCNXllW67JFqADtx6USQZ0OiaDb43m4eS3plBlysFICtVufBGxmLUZQpicgshgjLUYQ0/640?wx_fmt=png&from=appmsg)

在 Redis 中，可以使用 `KEYS` 命令来获取当前数据库中匹配指定模式的所有键。

**基本用法**：

```
KEYS pattern
```

* 若要获取**所有键**，使用通配符 `*`：

```
KEYS *
```

![](https://mmbiz.qpic.cn/mmbiz_png/v7ntTxZACkWwem20FkzOyp3OsVB1EYFHbDiaJzsqM1v8xNjNKLqMibmunYHH7aEKlGoBzOSRKiaBL752tkkwj252KBeRP68X2riaR3LkMvUY1pk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkXiaJEzdxmL86pQianphHcaFa9hwLozgNuZfhsumSnwZ4aFPK9Ns0Q41Y4lsRT34ibUHxH0ictGdlibYObYMAvRCWAGUc6LjQicTksxE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkWgS3hZDk772Y4PkexficLm0DJflkQeMALUmCn06Bodn1uICHFvCBRcpXibezUNa8Ub2Vl0IuDWAr2HApGe2Wf1wsYhyhupe08lk/640?wx_fmt=png&from=appmsg)

拿到flag：03e1d2b376c37ab3f5319922053953eb

![](https://mmbiz.qpic.cn/sz_mmbiz_png/v7ntTxZACkVyrRtd60DagU5gfxoMRVZUZT2dvY8DaaKiamoDVSLQAXbCWCial2vQ6rBicxv3OnqVPrtTnpicgv3GegJbl80HTgu2FwrFndsUm5I/640?wx_fmt=png&from=appmsg)

通过完成 Redeemer 靶机，我们学习了 Redis 服务的基本原理及常见的枚举流程。从端口扫描识别 Redis 服务开始，到使用 `redis-cli` 连接目标、查看服务器信息、切换数据库、统计键数量以及读取键值数据，完整体验了 Redis 的基础交互过程。同时也了解到，当 Redis 配置不当（如未开启认证、暴露在公网等）时，可能会导致敏感数据泄露，因此在实际生产环境中应合理配置访问控制、身份认证及网络隔离等安全措施，避免因错误配置带来安全风险。

本次分享的目的并不是单纯完成靶机，而是希望大家能够对 Redis 有一个基础而全面的认识，了解 Redis 的工作原理、主要作用以及在实际渗透测试和日常运维中的应用场景，为后续学习数据库安全和中间件安全打下基础。

**再次强调，能力越大，责任越大。希望我们都能用技术去守护，而不是破坏。记得给小编点个“赞”留个关注！！！**

> ⚠️ 郑重声明：所有内容均用于合法安全研究，请务必在授权环境下进行测试。做个白帽子，很酷。
> 📮 欢迎交流讨论评论。如果觉得有用，不妨点个“关注”和 “赞”支持一下。

每一次技术解读、每一篇实战记录，都源于大量时间的测试、验证与梳理。如果这份指南为您打开了新的思路，或为您节省了宝贵的时间，不妨给小编进行简单的打赏，支持更多深度内容的诞生。您的每一次点赞、在看、分享，都是我们持续分享的动力；而直接的赞赏，则是对原创内容最温暖的鼓励。

让我们一起，用技术观察世界，用分享传递价值。

感谢您的阅读与支持！

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
...