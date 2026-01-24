---
title: 以色列Cellebrite设备取证手机后遗留的痕迹特征
url: https://mp.weixin.qq.com/s/Vmyg6dtYir7NppiRfIREKw
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:24:11.457176
---

# 以色列Cellebrite设备取证手机后遗留的痕迹特征

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dJPrPaEiblOWo418YVCBtkLhiaXANicYxQjeNAeNiayLK6ChVjn6DyLzjMA/0?wx_fmt=jpeg)

# 以色列Cellebrite设备取证手机后遗留的痕迹特征

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

Cellebrite DI Ltd.（简称 Cellebrite）是一家全球领先的数字情报（Digital Intelligence）和数字取证解决方案提供商，总部位于以色列佩塔提克瓦（Petah Tikva），成立于1999年。

主要业务和产品Cellebrite 提供端到端的数字调查平台（Case-to-Closure Platform），覆盖数据收集、审查、分析和管理全流程。

UFED（Universal Forensic Extraction Device）为行业标准移动取证工具，能从各种智能手机、平板等设备中合法提取数据，支持iOS、安卓等系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dBWwOKlTTevLILbZQmnUnhxyGLGw52wfm5uP5bzkNopsOn0LyrOqNFg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dYEamsotIJose43hNm08uwmqtxlN8icfDVWKd9A1ibg6SIGlejwEBdbsg/640?wx_fmt=png&from=appmsg)

Physical Analyzer：用于深度审查和分析提取的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dOchgicvw2ura38sJyDjnUsCYEEh5AsSJ12A6RhMAwScvSrn06ypNgLw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dOAZNbrVH4A6p1KBQZdKDcGlSYzYplQricZZcqKgc2lpTlDOFmBQias8Q/640?wx_fmt=png&from=appmsg)

Inseyets：AI驱动的调查解决方案。

Responder、Digital Collector、Pathfinder 等工具，支持实时采集、远程收集和案件管理。

企业级产品如 Endpoint Inspector，用于企业端点数据管理。

可以说境外各行各业都有使用该设备进行取证分析的情况存在，行业主要为公共安全（Public Safety）、企业（Enterprise）以及联邦/国防三大类。截至2025年最新公开数据，公司全球客户超过7,000家，技术每年支持超过150万次合法授权调查，收入90%以上来自政府和公共部门机构，大部分为执法行动。

黑鸟通过外部消息，总结关于Cellebrite取证手机设备后遗留的痕迹特征如下。

首先需要提及情况：2024 年末，苹果在 iOS 18 中引入了一项安全功能，该功能允许 iPhone 在连续 3 天（或 72 小时）无活动后自动重启，将手机状态从 AFU（高级无操作模式）切换到 BFU（基本无操作模式）。类似的可选功能于2025 年 4 月在 Android 手机上推出，对应 Google Play 服务版本 25.16。

当iphone被脸部解锁后，该Cellebrite设备可以通过未知手法，获取到iphone的解锁密码。

取证记录显示，该设备在进行Cellebrite数据提取的前一天重启过，因此在提取数据之前处于首次解锁前（BFU）状态。

BFU是指设备重启后尚未解锁的状态。与首次解锁后（AFU）状态相比，设备处于BFU状态时，其内容加密更加安全。

特征1：

iPhone 通过 USB 连接到Cellebrite设备时，该设备使用

HostID 9016926980658937761372207 和 SystemBUID 30313996-42072961236303456 进行自我识别。

这两个特征，分别出现在Cellebrite 数字签名的 DLL 文件中，包括“CellebriteMobileAgent/iPhoneLib.dll”。

handle\_pair: Pair message: {

PairRecord =     {

DeviceCertificate = [..]

HostCertificate = [..]

HostID = 9016926980658937761372207;

ProtocolVersion = 2;

RootCertificate = [..]

SystemBUID = “30313996-42072961236303456”;

};

Request = Pair;

}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dlJicSl35NpDicJD4A5AeMUHXUr7rBcokRH0g5ia4Dwmp9hLUejXVz001w/640?wx_fmt=png&from=appmsg)

特征2

Cellebrite设备取证存在公开的checkm8漏洞的iphone时，这部 iPhone 的崩溃日志显示，一个名为mnm 的进程曾在该设备上运行。

手机显然是从 RAM 磁盘启动的，这表明安全启动已被绕过，可能就是通过checkm8实现的。

崩溃日志显示， mnm进程有一个名为“com.cellebrite.bruteforce”的调度队列。

“24”：{...，“procname”：“mnm”，...，“dispatch\_queue\_label”：“com.cellebrite.bruteforce”，...}

手机上还设置了几个以“mnm-”开头的NVRAM变量（NVRAM变量可用于在文件系统之外保存设备重启后的状态），因此进程名*mnm或以“mnm-”开头的NVRAM变量大概率是由Cellebrite的工具设置的。*

特征3

Cellebrite取证的安卓设备的取证记录时，会安装了一个名为 com.client.appA 的软件包。

START DELETE PACKAGE: observer{██████████}
pkg{com.client.appA}, user{█}, caller{█} flags{█}
START INSTALL PACKAGE: observer{██████████}
stagedDir{/data/app██████████.tmp}
stagedCid{null}
pkg{com.client.appA}
Request from{null}

package=com.client.appA totalTimeUsed=”00:24″ lastTimeUsed=██████████
totalTimeVisible=”00:26″ lastTimeVisible=██████████
lastTimeComponentUsed=██████████ totalTimeFS=”00:00″ lastTimeFS=”1970-01-01 02:00:00″ appLaunchCount=2 fgServiceLaunchCount=0

该软件包随后不久被删除，该软件包名称出现在Cellebrite 公司数字签名的 DLL 文件中，

例如“CellebriteMobileAgent\CellewiseLib.dll”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dsuzzJvYxveEUg7ZLrhuoBJIjbK7LsKKzvibiacjunD3lTzXoj8Dekiblw/640?wx_fmt=png&from=appmsg)

还有一些其他资料，后续看情况不定期分享。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dc9vJxBLPJiaJj8XbPORamjQ1Ljnz6CU61ulCt59T6UqsIuoWZ8gC7xQ/640?wx_fmt=png&from=appmsg)

iOS 系统封锁记录

主机 ID：9016926980658937761372207

系统版本：30313996-42072961236303456

iOS崩溃日志

进程名称：mnm

 服务名称：com.cellebrite.bruteforce

Android 软件包

软件包 ID：com.client.appA

更多实时情报可扫码查阅

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpfjZtYHvnDwWrjlgr6wic9dfibOE7aPT48DIgWdp1VCHicRYPV8TtbMHHBx7EOlUVpbBDdT06NpLsHA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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