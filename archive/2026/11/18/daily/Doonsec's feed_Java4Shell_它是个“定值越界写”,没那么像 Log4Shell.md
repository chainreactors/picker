---
title: Java4Shell:它是个“定值越界写”,没那么像 Log4Shell
url: https://mp.weixin.qq.com/s/byR8VGLT5Nc_S9glYe90ug
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:38:35.553701
---

# Java4Shell:它是个“定值越界写”,没那么像 Log4Shell

# Java4Shell:它是个“定值越界写”,没那么像 Log4Shell

原创

MessFeel
MessFeel

MessFreeSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Java4Shell(CVE-2026-114938)昨天披露,对标 Log4Shell,说是核弹级。漏洞是真的,认证前就能触发,该修。但把 Calif 的披露原文和几家分析对齐看一遍,它的利用原语比名字弱不少。下面讲几个被炒作盖过去的技术点。

## 这个洞是什么:能挑写到哪,挑不了写什么

漏洞在 HotSpot 的 Base64 解码器里,具体是 x86-64 上用 AVX-512 VBMI 指令写的那段优化汇编。解码一个带 padding 的短尾部时(`=`、`==`、`X=`、`X==`、`XY=`、`===` 这几种形态),输出长度算错,向量 store 把本该几个字节的写变成写满 64 字节,越界写到堆上。

关键在越界写进去的是什么。按 Calif 的描述,一个 50 字节的数组从 offset 48 开始写 64 字节,越界 62 字节;其中第 0 字节完全可控,第 1 字节可控 4 bit,剩下的不可控,offset 48 到 63 恒为 `0x9a`。Calif 自己的结论是:越界写只有落点可控(“Only the landing position of the out-of-bounds write is controllable”)。

也就是说,攻击者能挑这段越界写落在哪,但几乎挑不了写进去的内容,大部分是固定值。这类定值越界写做稳定 RCE 很吃力:你只能把固定的字节砸到某个关键结构上碰运气,不能像任意写那样直接改指针、改长度。这就是 Calif 说“没有通用利用、每个产品都得单独构造链路”的技术原因,也是它大多数时候的结果是进程崩溃、而不是拿到执行权限的原因。

拿它和 Log4Shell 比:Log4Shell 是往会被记录的地方塞一个 `${jndi:...}` 字符串,直接触发外连,利用门槛接近于零。Java4Shell 是一个要为每个目标单独排内存布局的弱原语。两个都叫 4Shell,利用难度不在一个档。

![图1　越界写只有落点可控、内容基本是固定值，这决定了它偏崩溃、难 RCE](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCOfmDhE56Hgicu9wvibNQsWe1t9YY1QWkSwjKBKHLia53iaOMtvDXdpX97HF1FaziaQ2sTxr4KDbh9cSpngNz7mvicy4n0YcCojPQpM/640?from=appmsg)

图1　越界写只有落点可控、内容基本是固定值，这决定了它偏崩溃、难 RCE

## 旧版 Java 反而安全,因为这段优化是新加的

受影响的是 Java 17.0.6 以后,以及 21、25、27;Java 8、11 和 17.0.0 到 17.0.5 不受影响。原因不是旧版打了补丁,是那段出问题的 AVX-512 解码汇编本来就不在旧版里,它是 17.0.6 时从 JDK 18 backport 进来的(这条目前主要见于 Endor 的分析)。

这给出一个反直觉的结论:跟着升到现代 LTS 的人踩中了,守在 8、11 的人反而没事。往一般里说,为性能手写的 SIMD intrinsic 是一类特殊代码:它绕开 Java 正常的边界检查直接操作内存,写得懂、审得了的人少,测试覆盖通常也薄。JVM 里这类拿底层不安全换性能的优化只会越来越多(Base64、各类向量化、Vector API),每加一处,就多一处同样性质的攻击面。

## 它挑 CPU,也能反过来打客户端

要走到那段汇编,CPU 得支持 AVX-512 VBMI,也就是 Intel Ice Lake 以后、AMD Zen 4 以后。ARM 全部不受影响,包括云上的 Graviton 和 Apple Silicon;Skylake、Cascade Lake 这类老 Xeon 也不受影响。此外还要 JIT 把解码器编成热路径、输入超过阈值(Java 17 要 129 字符以上,21/25/27 据 Endor 是 65 字符以上)。所以不少机群其实不在范围里。

一个容易漏的方向:Calif 提到一个由 samczsun 给出的客户端利用,一个 Java 程序主动用 TLS 连到恶意服务器,也可能被打。面不只是你对外的服务,还包括你主动连出去的那些 Java 客户端,爬虫、webhook 回调、服务间调用都算。

![图2　只有带 AVX-512 VBMI 的 x86 CPU 才在范围里，ARM 和老 Xeon 不受影响](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMC4XgsCm2LRjUxNFDTeH31x2iacMMBNLAfia723Via1bSnxPoaSYv1EDrTYyWYicHVYxPFhGabxkSs8WKmE2214UTV48zNp3adich2U/640?from=appmsg)

图2　只有带 AVX-512 VBMI 的 x86 CPU 才在范围里，ARM 和老 Xeon 不受影响

## 产品级 RCE 的真实状态

Calif 原文用的词是 demonstrated:在 Keycloak、Jira、Confluence、Artifactory、Jenkins、PingFederate 的默认配置上做到了 pre-auth RCE,另有一批需要认证的,比如 Kafka、Solr、Elasticsearch。但他们明确说武器化链条压着不放,公开的 PoC 只有一个证明越界写的 `Base64Trigger` 类,会打印 REPRODUCED,不演示 RCE。页面有演示视频,但外部拿不到可复现的产品级 PoC,也没有第三方独立复现过。

所以现在的状态是:披露方说自己做到了,我倾向于信,但你手里能亲自验证的只有“能触发越界写”这一步。再加上没有在野利用、没进 CISA KEV,它的紧迫度和一个已经满天飞 exploit 的洞不一样。

![图3　产品级 RCE 目前只有 Calif 一家“演示过”，武器化链条未公开、无第三方复现](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMBZBIaRbqjJGa4fYXELM34VocWAX1QUj8kD3INvfF1icN3L8MmKP9XZl9r22ghJ8LmChicgXsaeZAqwY97uupG1rSKGzZ9R0fduA/640?from=appmsg)

图3　产品级 RCE 目前只有 Calif 一家“演示过”，武器化链条未公开、无第三方复现

## 我更在意的,是它被挖出来的方式

Calif 的 Quang Luong 写,他让 Codex 去盯这几块代码,一小时找到漏洞,再两小时写出第一个可用利用,token 成本不到 200 美元,后面多数产品的链路几乎是 AI 自动接出来的。

过去能审 HotSpot 手写汇编 intrinsic 的人很少,要同时懂 x86 SIMD、Base64 编码和 JVM 内部。门槛高,所以这类代码长期没什么人系统地看。AI 在这里的作用不是让漏洞凭空变多,是让这类过去靠“没人看得懂”而事实上无人审计的角落,第一次被成规模地看了一遍。顺着这个逻辑,接下来更可能接连出问题的,是 JIT、GC、intrinsic、JNI 边界这些又底层、又少人懂的地方。这比“又出一个 Java 漏洞”更值得提前准备。

![图4　从库到框架再到 JVM 汇编，漏洞的位置在往更底层走](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMDlQpdiaCTW0juibvY8aibXTQticvCVaEtId8z0Wbt9A8WE1P1RO6ohEW8qRrxLBCq5XpkrXN8GCuToosZRzUw5264osYL9YwUldW8/640?from=appmsg)

图4　从库到框架再到 JVM 汇编，漏洞的位置在往更底层走

## 实操:怎么判断和缓解

2. 判断在不在范围:在机器上查 CPU flag 有没有 `avx512f`、`avx512bw`、`avx512vbmi`、`bmi2` 这四个,查运行时 `java -version` 是不是 17.0.6 以后、21、25、27。是查运行时,不是查 pom.xml,JDK 版本不写在依赖里。
4. 容器单独查:镜像里自带的 JDK 跟着镜像走,不随宿主 OS 更新。可能宿主补丁全打了、依赖全绿,容器里那个 JDK 还在漏。
6. 没补丁时缓解:加 `-XX:-UseBASE64Intrinsics` 关掉这段优化。Calif 也给了 `-XX:UseAVX=2`,但更重,而且 ARM 上会让 JVM 起不来。另外只有 basic 和 URL 解码受影响,MIME 解码走标量路径不受影响(据 Endor),实在改不动可以先确认入口用的是哪种。
8. 打补丁认具体 build,比如 Amazon Corretto 17.0.21.1.2。

这漏洞本身大概率很快修完、过阵子没人再提。今天更该动手的,是查清楚自己哪些 Java 跑在带 AVX-512 的机器上、哪些在容器里没跟着更新。这两件事比争论它够不够核弹有用。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nBEAXTaIuYiakqwmQlIeWQ9ZbB12BtJzcwa1sL64JXogjggNfsgZqLHVNxUhKTlqf6bATcs6kwDk9RyssibnnI0g/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过