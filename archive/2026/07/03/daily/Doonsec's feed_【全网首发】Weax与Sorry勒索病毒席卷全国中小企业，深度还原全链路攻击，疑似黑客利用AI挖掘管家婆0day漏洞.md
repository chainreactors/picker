---
title: 【全网首发】Weax与Sorry勒索病毒席卷全国中小企业，深度还原全链路攻击，疑似黑客利用AI挖掘管家婆0day漏洞
url: https://mp.weixin.qq.com/s/kA9sgBnLcko08dWljqAcgg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:42:12.490338
---

# 【全网首发】Weax与Sorry勒索病毒席卷全国中小企业，深度还原全链路攻击，疑似黑客利用AI挖掘管家婆0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/887OLfia3YQZHyCs5mIbibf3srJqOByqFdxriavIMic6VONtYe0vzuTLqHQQyIfQAN3VoWUNB1LFG8a17H0WFgaicticJibaeopbuTRzvtebk7hXCQ/0?wx_fmt=jpeg)

# 【全网首发】Weax与Sorry勒索病毒席卷全国中小企业，深度还原全链路攻击，疑似黑客利用AI挖掘管家婆0day漏洞

原创

州弟学安全
州弟学安全

solar应急响应团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/DxUXemrrntp3gibjPSCHmSEpdPDqfBcXT5e151v5AJSbV5JtaALLzQe0I1Jibbet7rTia8icjmgo5r4hpY3IMpYPIw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

依托 **Solar 安全运营响应团队**的日常实战沉淀，我们会定期分享在安全运营中处置的典型应急响应事件，涵盖**银狐木马、APT 攻击、勒索病毒**等各类主流威胁。

作为专业的应急响应中心，Solar 致力于为复杂多变的安全事件提供从深度溯源到闭环处置的全流程支持。针对银狐、APT 等具有高隐蔽性的威胁，我们不仅聚焦于对其攻击行为的深度剖析，更致力于还原其完整的活动链路，并同步输出切实可行的**清除闭环操作方案**。

**突发危机干预通道：**若您的核心资产正面临加密锁定或数据勒索风险，请通过文末二维码联系我们。我们提供全天候紧急介入服务，协助您快速切断攻击链路，全力挽回业务损失。

## 写在前面

本文首发于**Solar应急响应团队-「州弟学安全」**，转载请务必注明出处。

此前，我们发布的[【万字首发】零安全设备零日志环境下的极限溯源，疑似国内黑产组织的.sorry1变种勒索病毒攻击链全拆解](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247510444&idx=1&sn=1a0f1607848c4cdc3e6fa96efe352311&scene=21#wechat_redirect)受到了业内广泛关注；关于Weaxor家族（Rox、Weax、Roxeaw）的往期分析文章，也收获了不错的反响，感兴趣的读者可以翻看历史文章。

最近一段时间，`.weax`与`.sorry`两个勒索病毒在国内中小企业圈里反复作案。Solar应急响应团队接连处置了多起相关事件，把这些案例放在一起对比，发现了一个高度一致的共同点：**受害者无一例外都部署了"管家婆"系列管理软件（管家婆辉煌Ⅱ/TOP+等）。**

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQa6yucl2l2R1cphVj7IPLaiaNPEeokfM2WtKvayHr5qDRSibTPlaHF3WqZ4ouP8HwJQMeVwwEOhiaaUGN9tC0nbKsfp87Ed5RMFLI/640?wx_fmt=png&from=appmsg)

Weaxor家族将文件加密为`.weax`后缀

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYyb7rcAuLBgSDvUdESyMrVKgf6XQAib2lHTYZXWLcUg4S1D1Qz9LKM6XnZaRCxSQHMcpI5rwkOSlPKL2jNyYLEPDrviaR2nibkjw/640?wx_fmt=png&from=appmsg)

Tellyouthepass将文件加密为`.sorry`后缀

奇怪的是，这些受害者的环境里：

* **SQL Server 的 1433 端口并没有对公网开放**；
* 数据库账号**也不是弱口令**（sa 密码复杂度足够）；
* 边界设备、Web 应用上**找不到明显的入侵痕迹**；
* 可偏偏就是被加密了，而且**加密发生前 SQL Server 日志里干干净净，没有任何爆破、任何异常登录**。

一个"没开数据库端口、没弱口令、没 Web 漏洞"的内网，是怎么被勒索病毒从公网打进来的？这是本篇要回答的核心问题。

经过深度的逆向分析与活机验证，并通过其它渠道交叉确认，我们最终把入口锁定在了管家婆几乎默认对外开放的211端口上，一个被绝大多数运维忽视、却能让攻击者在完全不需要任何口令、不需要加密狗、不需要客户端的情况下，可导致以 SQL Server 服务身份执行系统级操作，实际权限需以现场服务账户为准的未授权远程代码执行（RCE）漏洞。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYuKtYiajEcIsYI6dvv1ojQia0RuenNTJRhTqHGjovHwt0CRxUdp1Y4qs7sptW2zXY2VIUy27F3mkdBBjjuo3UgK09o6SZ3Fhbf0/640?wx_fmt=png&from=appmsg)

通过多渠道验证，漏洞利用入口确认为211端口

更致命的是，这个漏洞**不产生任何登录日志**，传统的安全设备和日志审计对它几乎无效，这正好解释了为什么受害者环境里"没有任何攻击痕迹"。

本文将从零开始，完整还原**排查、逆向、抓包、靶场验证**的全过程，每一步都给出可复现的操作与截图，供同行复测与防守参考。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/887OLfia3YQbhia5Vl1S7ONB5R1ic7ll5qm8ibkrL6erbDQic9tys7D8fftT350x1pGQhoRpbjia6jMNaYQmehFGfl2hZmD2JeCL5XVkOvI1Fq608/640?wx_fmt=jpeg&from=appmsg)

本文整体攻击链路概览

**值得警惕的是，截至本文发布时，这两个家族的攻击目标正在进一步扩展。** 此前**Weaxor**和**Telyouthepass**主要利用HW（护网）期间的1day和Nday漏洞实施攻击，但近期态势发生了明显变化，两个家族开始将矛头指向**管家婆物联通、管家婆ERP**等更多产品线，且基本上都是以0day漏洞作为突破口。这种攻击面的快速转移和武器化速度，与以往的攻击模式形成了强烈反差。

管家婆系列软件在互联网上可以直接下载安装包，任何人都能轻易获取目标程序。从软件公开下载到漏洞被武器化投入实战，这个周期被压缩得极短。结合此次攻击目标快速扩展、0day漏洞接连出现的特点，我们不得不提出一个严肃的假设：**勒索组织可能正在借助****AI****辅助进行自动化漏洞审计，大幅缩短了从"发现漏洞"到"勒索变现"的时间线。**这不再是传统的"漏洞挖掘-分析利用-传播攻击"线性流程，而可能演变成AI驱动的批量审计、快速武器化、精准投放的闭环模式。

## 一、线索汇聚：两起案例的共同点

### 1.1 案例A：Tellyouthepass家族（某制造业务系统，加密后缀`.sorry`）

第一起案例是一家制造业开发公司被`.sorry`加密。在其磁盘镜像里提取到了服务端程序包`XXXserver.rar`，解压后发现一个关键文件：`ScktSrvr.exe`（路径`hs_extract\ScktSrvr.exe`，680960字节），这是后续逆向的核心样本之一。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQb4ZaLicibBJ1kRaSzlQ3wIJ8gWBu9lVlfg7573sia3gEhGXjH8ybgNlUQibGk3oHsLygDO5wJuYeic4dm5VYNibXkTRDKnZoSXBH0Og/640?wx_fmt=png&from=appmsg)

解压`XXXserver.rar`后的目录列表，`ScktSrvr.exe`高亮标注

这台机器对公网开放的端口里，**211端口（TCP）处于监听状态**，而且加密发生后仍然存活；而1433（SQL Server）并未对公网放行。

### 1.2 案例B：Weaxor家族（某企业ERP，加密后缀`.weax`）

第二起案例是`.weax`病毒作案。我们拿到了这台机器的SQL Server默认追踪日志（`log_*.trc`），里面有一条铁证级的记录：

```
2026-06-26 19:47:59.30  spid56  Configuration option 'Ole Automation Procedures' changed from 0 to 1
LoginName = sa   （经 .Net SqlClient）
```

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQaN8If7BiaPXwicwjkQ9UUIqYZMqdbmut2pXkYhtJlE1otfVbEXH5H4o84diaa511mToNOEjGfw6SjNg85JygibyaiaibiaOCyU1ib92ok/640?wx_fmt=png&from=appmsg)

受害者SQL默认trace`log_105.trc`中`Ole Automation Procedures changed from 0 to 1`的记录（使用`fn_trace_gettable`或日志查看器打开）

这条记录说明：**攻击者在加密前一天，用****`sa`****身份开启了 SQL Server 的 OLE Automation Procedures**（这是后续执行 OS 命令的前置动作）。但问题是：`sa` 是怎么被拿到的？1433 又没开。

### 1.3 共同点收敛

把两起案例并排放：

| 维度 | 案例A（.sorry） | 案例B（.weax） |
| --- | --- | --- |
| 行业 | 制造业开发公司 | 企业ERP |
| 加密后缀 | .sorry | .weax |
| 1433端口开放 | 否 | 否 |
| 数据库弱口令 | 否 | 否 |
| Web漏洞痕迹 | 无 | 无 |
| 211端口开放 | 是 | 是 |
| 管家婆部署 | 否 | 是 |

线索全部指向同一个东西：**那个开着的 211 端口**。它不是 Web 端口、不是数据库端口，它是管家婆客户端连服务端用的**应用层 socket 端口**。在 1433 不暴露的前提下，唯一能让`sa` 在本地被执行的路径，就是经这个 211 端口：**借管家婆应用自身的****`sa`****连接，绕过数据库端口的封堵**。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQY0fov5Y0aM3sz1EZMq0MN4jAYcsPRNjtHYHNh5535D9IprGOsJFgoIdoObGTkvOeiapDqUPa4dDibfiaC95SJlRYCgSoV6ZzKm6w/640?wx_fmt=png&from=appmsg)

目标地址211端口可达性确认

研究方向由此明确：**搞清楚211端口背后这个程序是什么、协议是什么、能不能在无凭据的情况下执行任意操作。**

## 二、管家婆是什么，211端口又是什么

### 2.1 下载管家婆安装包，本地搭建

为了可控地复现，我们在本地下载了一份**管家婆辉煌ⅡTOP+15**的安装包，并在一台干净的Windows Server上完成安装（服务端+数据库+客户端）。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQaKQU9mxnldNuDN6btzATjBmhqccCXajIVnrBI59aQPBqUq7cNpeyRQHg4CnfNBQ5YQWBQc6q6zZvdao6e6LEqnK9e5YYRpHJo/640?wx_fmt=png&from=appmsg)

管家婆辉煌ⅡTOP+15安装过程截图（安装向导/安装完成界面）

安装完成后，`C:\GRASP TOP+\`目录列表如下，`scktsrvr.exe`与`GraspSvr.exe`高亮标注，这两个文件是本文的主角：

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbN6ptwy4C2hrLlR8P16ia4WmoEcTx196BmDloeCM41YIznQRFt7qYACaw93GXX3iaQwibrtytibIVvtiaqvEkljWMJrfqPyYic34dlI/640?wx_fmt=png&from=appmsg)

`C:\GRASP TOP+\`目录列表，`scktsrvr.exe`与`GraspSvr.exe`高亮标注

安装完毕后，用客户端`GraspNet.EXE`登录服务端、进入一个测试账套，确认整套环境正常工作。

靶场拓扑如下：

![img](https://mmbiz.qpic.cn/sz_mmbiz_jpg/887OLfia3YQZ82U3NXkCbERo56YJxOmgMb7Wjtc8eh08oQ2YtxMyggK0bRkTtYzPU7iciaWY0srSsjjqUoKptIGicicDomNLGyZT6yaxzBxxIras/640?wx_fmt=jpeg&from=appmsg)

靶场进程截图：任务管理器或PowerShell`Get-Process scktsrvr,GraspSvr,sqlservr`显示三者运行中及路径

### 2.2 211 端口的真身：`scktsrvr.exe`

我们顺着 211 端口找到了对应的进程：`C:\GRASPⅡTOP+\scktsrvr.exe`。

**`scktsrvr.exe`****到底是什么？** 这里用大白话解释一下，方便不熟悉 Delphi 技术栈的同学理解：

管家婆这类软件是典型的**C/S（客户端/服务端）两层半架构**。你在前台操作的客户端（`GraspNet.EXE`），并不直接连数据库，而是先连到服务端的一个"中间程序"；这个中间程序再统一去连数据库、并把结果回传给客户端。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/887OLfia3YQZX2TKJ43ungWD3ln6ZEx2VI1qIrJn1u1b8yicuYcrDPwsdiceyVwwItXsLttPH6X5DnAaolgrgTdiaqMdooUP7qWXte821cVtSv8/640?wx_fmt=jpeg&from=appmsg)

中间件逻辑运行示意图：客户端→scktsrvr.exe→GraspSvr.exe→SQL Server

`scktsrvr.exe` 扮演的就是这个"数据中转站 / 中间件"**的角色，它来自 Borland/Delphi 的技术体系，正式名称叫**Borland Socket Server**（或 Delphi Socket Server），是 Delphi 开发的多层应用（MIDAS / DataSnap 架构）里专门用来**在客户端和服务端之间搬运数据的 socket 传输层程序。

可以把它通俗地理解成：

> **它是管家婆客户端和服务端之间的"快递中转站"，客户端把要查的数据、要执行的指令打包发给它（211 端口），它转交给服务端的业务程序（GraspSvr），业务程序再去数据库取数/写数，原路返回。**

这个"快递中转站"用的是一个叫**MIDAS** 的私有二进制协议（不是 HTTP）。理解这一点非常关键，因为它决定了后面两件事：

### 2.3 为什么传统防御对它无效

**第一，它不是 Web 漏洞。** 211 端口上跑的不是 HTTP，是 MIDAS 私有二进制协议。WAF、Web 日志、URL 审计统统看不到它：它根本不在 Web 这条管道里。

**第二，它默认不产生登录日志。** 我们在逆向时确认：`scktsrvr` 的连接建立阶段**没有任何应用层认证**（注册表里的鉴权拦截器`InterceptGUID` 是空的），握手成功也不会像 SQL Server 那样写一条登录记录。也就是说，攻击者连上来、握个手、调几个方法，**全程在操作系统和应用日志里留不下任何"谁连进来了"的痕迹**。

这就完美解释了之前的悖论：**受害者环境没有痕迹，不是因为没被打，是因为这条管道压根不记日志。**

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbDls80zUwZZH0WpyWowwDdo4ia42LHBRTk31dmhGACI58t0bj9jnhh5X1qpX8YTDcF3ibHf3UxC08FLv2cqncicIIdwnMb4h1LF8/640?wx_fmt=png&from=appmsg)

注册表`HKLM\SOFTWARE\WOW6432Node\Borland\Socket Server`的内容：`InterceptGUID`值为空（无鉴权拦截器）

既然它是私有协议、又不记日志，那想搞清楚它到底怎么工作、有没有漏洞，就只能靠**两条路**：

1. **静态逆向**：把`scktsrvr.exe`（以及它拉起的业务程序`GraspSvr.exe`）丢进 IDA，看协议是怎么解析的、有没有鉴权；
2. **动态抓包**：搭一个中间人（MITM），让真实的管家婆客户端从中间过一遍，把协议的真实字节抓下来对照。

后面的方向，我们就分别走这两条路。

## 三、逆向 scktsrvr.exe：协议与漏洞点

我们把靶机上`C:\GRASPⅡTOP+\scktsrvr.exe`（与受害者同款，文件版本 7.0.4.453）拷贝出来，放进**IDA Pro**。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYOtbrOIHharibHiaY4aWwfuxZPJUEKj1aPFrSgGtXsyesn1dP4Ke1LqcQhAicNoRHLZLBLA6YddplRAmGHU3I9xJ8Xul8eBicmXKY/640?wx_fmt=png&from=appmsg)

IDA Pro成功载入`scktsrvr.exe`程序

### 3.1 第一个发现：握手阶段没有任何认证

在逆向协议之前，我们先确认了一个最关键的前提：**这个服务要不要登录？**

`scktsrvr` 的运行参数读自注册表`HKLM\SOFTWARE\WOW6432Node\Bor...