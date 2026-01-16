---
title: 第152篇：希水涵Web日志分析工具（ABC_123原创）| 识别攻击行为，生成可视化报告
url: https://mp.weixin.qq.com/s/wblUHH-crmZ9oCtRtVvPhQ
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:26:00.592480
---

# 第152篇：希水涵Web日志分析工具（ABC_123原创）| 识别攻击行为，生成可视化报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcsib8Ioc7wKl2hpg9cjNuslaibt7Mw0IhUO9OlwWpYDNFCxnOGfRKM2TA/0?wx_fmt=jpeg)

# 第152篇：希水涵Web日志分析工具（ABC\_123原创）| 识别攻击行为，生成可视化报告

原创

abc123info
abc123info

希潭实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

Part1 前言

大家好，我是ABC\_123。最近我在家里集中精力，把多年前写的 Web 日志分析工具重新梳理并完善一下。该工具从 2017 年开始编写，期间一直断断续续地修改和新增功能，最近终于抽出时间系统性地更新优化，整理出了一个相对完整可用的版本，分享给大家使用。文末有下载地址，如果在使用过程中有任何建议、遇到 Bug 欢迎反馈。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450Dq1Q8s4COc7InkMO0jIGjiaGho1fcJicpibWB4vzvIM1wAib9TiakVECbIM5S0mHCTTeGJJibWtCe25vXw/640?wx_fmt=jpeg&from=appmsg)

Part2 技术研究过程

首先看一下软件界面，该界面可以指定日志所在目录，然后提供了部分选项，点击"分析日志"按钮，即可开始分析日志并生成日志分析报告。界面支持配置默认主机名、开启自动识别日志类型，并可按需配置日志分片大小（默认300MB）与日志编码（如 GB2312），以适配不同格式与大体量日志文件的处理需求。在分析内容方面，工具支持多种筛选策略：可选择"分析全部URL"、"仅分析带参数"，或"不带参数的URL"；同时可按资源类型过滤，例如"分析全部扩展名URL"、"仅分析动态URL（过滤图片、html、js、css）"，或"仅分析指定后缀（如`php/asp/jsp`）"。此外，状态码统计也支持全量分析、仅分析200状态码或指定状态码（如 `404,502`），便于针对异常访问进行定位。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcywo5HKrgUiammiaC121K4sDVDgKussYGypzxzOMicWgUycibtz5FEPWtxg/640?wx_fmt=png&from=appmsg)

分析完成后，该软件会在当前程序的 result 目录下生成一份 HTML 可视化报告。报告首页以仪表盘形式汇总 Web日志的整体态势：左侧展示漏洞攻击类型分布饼图，下方提供攻击目标雷达图；中间区域集中呈现Web日志的核心指标，包括总访问数、PV/UV、独立 IP 数、总消耗流量、漏洞攻击数、攻击 IP 数、攻击种类、错误访问数及日志文件大小等；底部通过攻击曲线图展示攻击随时间的变化趋势，便于快速定位风险高发时段并开展溯源与处置。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcd33yJBf6n5FMGHAgyWLCxm5rJItE4Ula6CsqhGrH7bTQk3W9YrqMmA/640?wx_fmt=png&from=appmsg)

全站请求数量曲线图：用于展示在统计时间范围内各时间点的请求量变化情况。通过曲线的波动可以快速识别访问高峰与低谷，判断是否存在突发流量、集中扫描或异常请求激增等现象，为定位异常时段提供依据。

**全站请求流量曲线图**：用于展示全站流量消耗随时间的变化趋势，单位以 GB 计。该图能够直观反映带宽占用情况，辅助判断大流量下载、资源盗刷、恶意刷接口或攻击引起的流量异常，从而为后续限流、封禁与资源调度提供参考。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcH85PyaTSGbbcYeFd5jOKPNQtKTE3Pp8DQChZbNLH8ELJgaCa25rVmA/640?wx_fmt=png&from=appmsg)

**状态码分析**：以表格 + 环形图展示 2xx / 3xx / 4xx / 5xx 的次数与占比，用于快速判断访问是否正常、错误请求是否集中。

攻击行为统计：汇总各类攻击行为及命中次数，如 SQL 注入、XSS、WebShell、SSRF/文件包含、框架漏洞探测等，便于定位主要风险点。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcZyZichRys7qS1nianGQlmgj2elwdO567uicE3d3rHJmicqib8HCoQ2ZiaGRQ/640?wx_fmt=png&from=appmsg)

报告还提供了攻击来源与恶意 IP 统计模块：

攻击 IP 分布：按国家/地区汇总攻击来源及数量，便于快速识别高风险区域。

**恶意 IP 列表**：展示攻击次数最高的 IP，并标注归属地、攻击类型及占比，用于溯源分析与封禁处置。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYc2UAbrZmH4ibhMTgs2XNHMlUiac5JSV10G4vVZ9DiaS09Bgz95GdU4HYXQ/640?wx_fmt=png&from=appmsg)

该页面为 IP流量分析（TOP200），用于统计访问量和带宽消耗最高的 IP。 表格按 IP展示其访问次数、访问占比、归属国家/地区、流量消耗及流量占比，便于快速定位高频访问源和异常大流量 IP，为限流、封禁和溯源提供依据。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYck2tcPyV9rnPHa49zNrkInhjdGAsDf7eQS5VBticqZT1YIWZSHVXGiczA/640?wx_fmt=png&from=appmsg)

该页面为国外IP流量分析（TOP200），用于筛选并统计来自境外的高频访问源。 报告中展示国外 IP 的访问次数、访问占比、归属地区、流量消耗及流量占比，便于识别异常境外流量、可疑扫描来源，并为封禁策略与访问控制提供参考。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcnGks1Y8rztvZTN5IOT6voic8P9LHic6yNwozGwGGDuWxbCP93STj8AXQ/640?wx_fmt=png&from=appmsg)

静态资源POST请求访问分析（TOP200）：统计对静态资源发起 POST 请求的 URL、访问次数、流量占比及响应码。由于静态资源通常不应使用 POST 方法，该模块可用于识别异常请求或潜在攻击尝试。

漏洞攻击列表：汇总检测到的漏洞利用行为（如 Nginx 解析漏洞 TOP10），展示对应的 Host、攻击 IP、攻击 URL、命中次数、响应码与时间，便于快速定位漏洞探测与攻击来源。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcwzASBvHEeE7oB4oWzZf3kJcCe8SwYJyJChficpl02VHH02jBkia18T8Q/640?wx_fmt=png&from=appmsg)

该页面主要用于统计站点的热门访问资源，包含两类 TOP200 排行：

页面访问分析（TOP200）：按页面 URL 统计访问次数、访问占比、独立 IP 数、流量消耗及响应码，用于识别访问最集中的业务入口和高流量页面。

静态资源访问分析（TOP200）：统计图片、JS、CSS 等静态资源的访问次数与流量占比，便于发现高消耗资源及异常访问情况。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcTVotoMQxMKEricv8qpeyqicZFYzDIAY0WQE1D1D0JpXDFkv2d3qZ9wqQ/640?wx_fmt=png&from=appmsg)

该模块为死链404访问分析（TOP200），用于统计返回 404 Not Found 的高频 URL。表格展示每个死链的访问次数、独立 IP 数、流量消耗及占比，便于排查无效链接、资源缺失或被扫描探测的路径，并为修复跳转、补全资源或封禁恶意请求提供依据。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcSh8Q93Sqyr16yY4vxqNYttiaaBASIlW8dnMlanJk4UQMd6npkNrwgWw/640?wx_fmt=png&from=appmsg)

该模块为访问来源URL分析（TOP200），用于统计 Referer（来源地址）的访问情况。 表格展示各来源 URL 的访问次数、访问占比、独立 IP 数及引流页面数，便于识别主要入口来源、异常外链引流或可疑跳转来源。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYc1wF0megdIlWnVr8UsRuaMeFdxUHq4gmm2Sxz43bEKiciaGwZu5fqJwiaw/640?wx_fmt=png&from=appmsg)

搜索引擎爬虫分析：统计来自 Baidu、Google、Bing、Sogou 等搜索引擎爬虫的访问次数、占比及流量消耗，用于评估爬虫抓取强度与带宽影响。

搜索关键词分析（TOP200）：汇总搜索引擎带来的关键词访问情况，展示关键词的出现次数、独立 IP、首次/最后出现时间及搜索来源链接，用于分析主要检索入口与流量来源。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcBPASC4pFGlxnmc904WoyEmVaFyW6RglYTcBbvPI0L4D4s4Xk9z2aEQ/640?wx_fmt=png&from=appmsg)

该模块为地域访问分布分析，用于统计不同国家/地区的访问情况。 表格展示各地区的访问用户数、用户占比、访问总次数及流量总量，便于识别主要访问来源区域，并辅助发现异常地域流量或可疑集中访问行为。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcPCCPlzQX8f1DibkwCiaeMEkXhlMcfFzD6u9tdFCmvtSa19GlVZKNy7QQ/640?wx_fmt=png&from=appmsg)

该模块为操作系统使用分析，用于统计访客使用的终端系统分布。 表格展示各操作系统的访问用户数、占比、访问总次数与流量消耗，并通过柱状条直观对比占比情况，便于了解主流访问终端及异常系统访问特征。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcgyp8TvOCp6Rmcx4g3D36VDLRR58LxmkWcibYPb9nea7ict5HkDX7ItJw/640?wx_fmt=png&from=appmsg)

该模块为浏览器使用情况分析，用于统计访客浏览器类型分布。 表格展示各浏览器的访问用户数、占比、访问总次数及流量消耗，并以柱状条对比浏览器占比，便于了解主流访问终端及可疑 UA（如 Unknown）访问情况。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AxCsGhaZgn4ibAdpUEWjkYcvxNPS3qVjCID4AGJOJwH5sgAP8cfUaKuA9ibwvCc361cYSIlweET2Lw/640?wx_fmt=png&from=appmsg)

Part3 总结

1.  工具支持一键导入日志文件/目录，自动识别日志类型，并可配置主机名、编码与分片大小，适配大体量日志快速解析。

2.  提供多维筛选功能，可按 URL 类型（全量/带参/不带参）、资源类型（动态/指定后缀）及状态码范围进行精确分析，便于聚焦异常行为。

3.  分析过程可视化展示，实时输出 GeoIP 初始化、分片处理进度与资源占用情况，确保分析过程透明可控，方便排障与溯源。

4.  关注公众号"希潭实验室"，回复关键字"log"，即可得到软件的下载地址。大家有好的建议，欢迎给我留言。为了便于技术交流，现已建立微信群"希水涵-信安技术交流群"，欢迎您的加入。

![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BeLRQeD27sD8qRPk8ghs8roXm8dhJxYetsiczLFOnPFHEk33HxXc3AicDSQE4J7wHfD42oAKrFRsJQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**OR 2332887682#qq.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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