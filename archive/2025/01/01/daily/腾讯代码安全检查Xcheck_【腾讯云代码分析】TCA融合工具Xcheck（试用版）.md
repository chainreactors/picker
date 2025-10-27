---
title: 【腾讯云代码分析】TCA融合工具Xcheck（试用版）
url: https://mp.weixin.qq.com/s?__biz=Mzg2ODQ3ODE1NA==&mid=2247486404&idx=1&sn=c5dbb0295f59014dd2229566a8670655&chksm=ceaaf661f9dd7f779b7e6afdb7cba2382ff2e4eaa5178a3e7b7d47eb96b9b70e39a16cbfec65&scene=58&subscene=0#rd
source: 腾讯代码安全检查Xcheck
date: 2025-01-01
fetch_date: 2025-10-06T20:07:58.209506
---

# 【腾讯云代码分析】TCA融合工具Xcheck（试用版）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8SDYbMEObOIuh5LjEbGE4HaibJfS2LWDEL3b1ibh6vPaXpog2SLTYlianNZ2v0pyLHduBygicYiaOlZYHI2YGIWyrew/0?wx_fmt=jpeg)

# 【腾讯云代码分析】TCA融合工具Xcheck（试用版）

原创

腾讯云代码分析

腾讯代码安全检查Xcheck

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wl5fxRNUSKiaoCK7j6treg7xfJhppNTSZOoSzpDTEibraPImqqNA7vWiaMfZ0ESQia2LkdicckqgDol89xOYWCVsUaw/640?wx_fmt=other&from=appmsg&wxfrom=10005&wx_lazy=1&wx_co=1&tp=webp)

官网地址：（点击最下方【阅读原文】可直达）https://tca.tencent.com/

官网介绍：https://cloud.tencent.com/product/tcap
官方开源：https://github.com/Tencent/CodeAnalysis

国内镜像：https://git.code.tencent.com/Tencent\_Open\_Source/CodeAnalysis

## TCA介绍

▼

腾讯云代码分析于 2013 年从个别独立代码分析工具开始，持续逐步迭代强化，至今发展成集众多分析工具的云原生、分布式、高性能的代码综合分析跟踪子系统，支持三十余种编程语言的分析。

代码分析是运用词法分析、语法分析、控制流、数据流分析等技术，对代码进行综合分析，查找代码中的规范性、结构性、安全漏洞等问题，进而输出代码的详细分析报告，帮助项目持续跟踪管理项目代码质量。

腾讯云代码分析可以“左移”至CI门禁或本地桌面，从而尽早以低成本、高效率发现代码问题，减少修复成本，缩短修复时间。

## TCA优势

▼

腾讯云代码分析拥有稳定可靠的架构，采用云原生的微服务架构，支持资源弹性调度。它还采用分布式客户端模式，可以自适应优化分析效率。此外，腾讯云代码分析还国产化ARM64适配支持信创。它采用服务分层设计，支持灵活扩展适配，并具备高效的数据存储能力，可以支持大规模的并发分析。

腾讯云代码分析支持对接业内常见的Git/SVN/Perforce仓库，并开放了标准化的API，可以快速对接主流的**CI和DevOps**平台。它还支持**GitHub action和Jenkins**插件的快速接入。

同时支持**248款工具和2500+高价值规则（总量超2.5万规则）**，可以轻松扫描各种类型的代码。用户可以接入自定义工具和规则，可以根据自身业务定义业务逻辑规则，也可以集成自研工具和商业工具，以满足项目的需求。

目前，腾讯云代码分析覆盖了业内主流的**33门语言**，并支持自动识别语言，同时也支持扫描多种框架。

## 使用说明

▼

在方案页面，TCA官方体验分析方案内可以看到Xcheck安全规则包已启用。进入官方方案->选择分析的代码库->启动分析。

提示：Xcheck安全规则包目前只支持在官方体验分析方案中试用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wl5fxRNUSKg3eWfy0Tma2BJwVzUSFBRicsOgWV2gfYm9Hult06xC8s3TuwKfQMDkMh7YPIwxBJZviaxMgaqVibnZg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wl5fxRNUSKg3eWfy0Tma2BJwVzUSFBRicmGMzQsvjqA9ycMgtp9hLhrFNia40fI85tticHoB8JCGTqFicXicWJX79Hg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Wl5fxRNUSKg3eWfy0Tma2BJwVzUSFBRicdHAhV3JOBRKhxxvWibwJA9jicJ2YtMfX4G6h7HicSl9xr18UvicW9gribqQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8SDYbMEObOKQggbPaYBLjrib2bNEVB70UM8dnDUJnQ57A2qQe4qzomIxAUiczA3vGVcmHjOWibicWqcwksIvMfYM9Q/0?wx_fmt=png)

腾讯代码安全检查Xcheck

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8SDYbMEObOKQggbPaYBLjrib2bNEVB70UM8dnDUJnQ57A2qQe4qzomIxAUiczA3vGVcmHjOWibicWqcwksIvMfYM9Q/0?wx_fmt=png)

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