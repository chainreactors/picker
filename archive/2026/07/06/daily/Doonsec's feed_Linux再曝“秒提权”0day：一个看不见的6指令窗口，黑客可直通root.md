---
title: Linux再曝“秒提权”0day：一个看不见的6指令窗口，黑客可直通root
url: https://mp.weixin.qq.com/s/pe93aMfUEkVVs0j6cqeSfg
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:02:53.631348
---

# Linux再曝“秒提权”0day：一个看不见的6指令窗口，黑客可直通root

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1udnWEPoelo5DU7WtAGkJs5UZUXKrX1KDYT0JgcumsvTK2w0fOWicNKYBdndHkA3OPTfusS8OfMgCiaGxHCDwcbcgQsvgicwYXec/0?wx_fmt=jpeg)

# Linux再曝“秒提权”0day：一个看不见的6指令窗口，黑客可直通root

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，安全研究人员公开披露了一起 Linux 内核 epoll 子系统漏洞，代号 “Bad Epoll”（CVE-2026-46242）。

该漏洞属于 Use-After-Free 竞态条件问题，在特定条件下，受影响系统中的本地低权限进程可能借此提升至 root 权限。其潜在影响面包括使用受影响内核版本且尚未修复的 Linux 桌面、服务器以及部分 Android 设备。目前上游内核和主流发行版已陆续发布修复补丁，建议相关系统尽快完成内核更新并重启生效。

需要注意的是，该漏洞并非远程直接利用漏洞，攻击者通常需要先具备本地代码执行能力，或将其作为其他漏洞链的一环使用。研究人员已经构造出稳定利用链，在 kernelCTF 测试目标环境中可达到接近 99% 的提权成功率，但截至公开报道时，尚未看到大规模野外利用证据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3D55954fMtNmQPjdCkOX11nA7G2L36A8UHwS60TXIWpxFO1mOWgLURP7jClWGJFE7Uytzd888fPygM1JytUBHSHQFkuv9xAzE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K3KjDBcLTAKNFXP39FiaTO3NjOMdmh4gGMkCgDYWSszs7kpESjq549uibFibRgic42PnQUjDapCHt17t1iaVia7kCAL3b80H8bslknmo/640?wx_fmt=gif&from=appmsg)

*素材来源：thehackernews*

**#01**

漏洞核心：epoll中的“并发死亡窗口”

epoll 是 Linux 内核中非常基础的机制，用于高效管理大量文件描述符（如网络连接、IO事件），几乎所有服务器程序、浏览器、系统服务都依赖它运行。

这次的“Bad Epoll”，本质是一类经典但危险的内核问题：

Use-After-Free（释放后使用）竞态条件漏洞

在特定并发场景下，内核中两个不同路径会几乎同时访问同一对象：

* 一方释放内存（free）
* 另一方仍在写入该内存

短暂的冲突窗口中，内存结构被破坏，从而为攻击者提供“篡改内核数据”的机会。

但真正让这个漏洞变得可怕的，是它的触发窗口：

仅约6条CPU指令的时间差

也就是说，随机触发几乎不可能成功，属于典型“拼时间”的竞态漏洞。

**#02**

攻击难点：极小窗口 + 极低命中率

传统来看，这类漏洞通常“难发现、难利用、难稳定复现”。

Bad Epoll 同样具备三个典型特征：

* 时间窗口极短（6指令级别）
* 不稳定、容易崩溃
* 依赖复杂调度时序

但研究人员通过精心设计的攻击链，使其具备：

* 自动重试机制
* 竞争窗口放大技巧
* 稳定触发内核内存破坏路径

最终实现了在测试环境中接近 **99%成功率的提权效果。**

**#03**

危险升级：可绕过沙箱，影响Android

该漏洞的危险性不仅在于“提权”，还在于攻击面扩大：

**可从浏览器沙箱触发**

研究显示，该漏洞在某些情况下可以从 Chrome renderer 沙箱内部发起攻击。

这意味着：

* 用户只需访问恶意网页
* 即可能成为攻击入口

**影响Android设备**

由于Android同样基于Linux内核，该漏洞可能影响移动设备安全。

不过部分旧内核版本（如6.1系）暂未受影响。

**#04**

漏洞来源：一次“修补引发的连锁问题”

更值得注意的是，该漏洞被认为源自 2023年的一次epoll相关修改。

这类情况在内核开发中并不罕见：

* 修复一个竞态问题
* 却引入新的释放路径
* 形成“兄弟级漏洞”

Bad Epoll 正是这种“修复副作用”的典型案例之一。甚至有研究者指出，AI安全模型在审计代码时曾发现过同源问题的另一变体，但未能捕捉到这一“隐藏分支”。

目前该漏洞情况如下：

* CVE编号：CVE-2026-46242
* 已有PoC（概念验证）公开
* 未发现大规模野外利用
* Google kernelCTF已收录研究
* 修复补丁已发布（建议尽快更新）

受影响版本主要为：

* Linux 6.4及以上内核部分版本
* 多数未更新补丁的服务器系统
* 部分Android设备

**#05**

风险总结：内核竞态仍是“最难防线”

Bad Epoll 再次提醒一个现实问题：

Linux内核最危险的漏洞类型，不是逻辑错误，而是“时间问题”。

竞态条件的特点决定了它：

* 难以静态分析发现
* 难以在测试中稳定复现
* 难以彻底根除

这也是为什么它能在多年之后，仍不断演化出新的提权漏洞。

从 Dirty COW 到 Dirty Pipe，再到 Bad Epoll，Linux内核提权漏洞始终在重复一个模式：

“只要时间窗口足够短，系统就可能被撕开一道口子。”

而这一次，仅仅6条指令的差距，就可能决定一台机器是否彻底失守。

*资讯来源：thehackernews*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K32lDv6vZa3ylrnicA6t2oAibbLu8AL00icFiczP2NLUia6W4VMeJYIOYFuyOetAAbdjYgDgibViaZpCo9RFy8t4MMkcia5xcTxdF4s90M/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K2Cr1oP6hO99f5TbjGqcHPx7R4DjrGYJLmtU7xJ6T5db5uicXBWiaTt1k5KrtnTURGHqhe5K6rrNq8VibUnrru29S8NEUkEPric2w8/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K0OicbYt5wxAibbbeLKEc7a6ib152aGmLeP8WfpWKNR3yEl95v2664oQqmJKOiaPm4zn30kwHZlkibiaibdF6XuTt0e5bnPff13dor6fk/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K3YTgotLDEKnDQ9pBx5yWozbrKn7yMahlJicqLaQfibMzYiclI4YCJ05XfS5x5lnib2YJnFSsCSc6AD7VnYAuQzqSWKWZn6tsndmvc/640?wx_fmt=gif&from=appmsg)

**球在看**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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