---
title: OpenClaw最新完整漏洞，实时可查！（附高危列表）
url: https://mp.weixin.qq.com/s/57V-86JPnQDLzuv8kgV0VA
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:06:05.904961
---

# OpenClaw最新完整漏洞，实时可查！（附高危列表）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T4OSm0sXdEMVyU1mic2mDF7F62lHU0taM1cZm8SV5jnzJtoIvnf0iaBQicUyqGJicRiauuCpBWwP0B1WxNBbB9SYSDeqn9GCg4icmicO9DmA4WVH6I/0?wx_fmt=jpeg)

# OpenClaw最新完整漏洞，实时可查！（附高危列表）

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器中沉浸阅读

据媒体报道，由于OpenClaw智能体项目集中爆发漏洞太多（Github直接发布漏洞安全通告），导致CVE编号机构已来不及编号，存在较大的风险盲区。

为此，微步在线漏洞情报已对全网OpenClaw漏洞进行覆盖，并实时收录更新。用户当前通过微步安全情报社区X及下一代威胁情报平台NGTIP即可查询最新完整OpenClaw漏洞情报。此外，针对近期OpenClaw漏洞攻击情况，微步情报局也进行梳理，供各位师傅参考：

整体漏洞分布：

截至2026年3月19日，根据微步情报局统计，并基于漏洞VPT（Vulnerability Prioritization and Threat）评估模型，从威胁情报、攻击热度等不同维度综合评估，OpenClaw漏洞不同危险等级占比如下：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/KJ5kFuz2K97pSjtvqSE8ibhuv1qMPaVCNrOBNOsOZVn94ibLcFPI05WHqUxpjcBsZpXicnXKO64NzbibX3g3P2YcicfMCtCib94LshSIHnPYCCq20/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

当前，OpenClaw大多数漏洞被评定为低风险，此类漏洞实际利用价值较低或利用条件比较苛刻，仅有3个高风险漏洞（XVE-2026-2113、XVE-2026-7112、XVE-2026-7922），存在公开POC且能稳定复现，需重点关注。

此外，存在部分VPT评估低风险但CVSS高危/严重的漏洞，这类漏洞虽然技术危害较高，但由于利用条件苛刻或缺乏公开利用代码，实际威胁较低，建议结合微步VPT评估模型和CVSS综合判断漏洞优先级。

漏洞类型分布：

基于微步漏洞情报局统计与分析，OpenClaw漏洞攻击主要呈以下分布:

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K96Md8iaBVJwEZa639PoyEPNicOrMb9JftdAuhwePkvtmaTz5E8f8DzgQA04HKgicx74qjb3oxvV0sIEeFXib1csdPkwVyd1Zico7DVE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

其中，命令注入最多，占比高达21%，显示自托管类AI助手在Shell执行、文件处理、插件/扩展加载上存在明显的设计缺陷。紧随其后的，则是未授权访问和权限提升类漏洞，表明当前AI智能体访问控制机制存在较多缺陷。

需要注意的是，大多数漏洞仅影响特定部署，例如启用插件、暴露Webhook，共享主机，默认环回绑定+认证令牌可降低远程利用概率。

OpenClaw版本漏洞情况：

2026年2月到3月期间，是OpenClaw漏洞修复的高峰期，其2026.2.14版是漏洞修复最多的版本，达到38个漏洞，该版本进行了大规模的安全加固。其次则是OpenClaw 2026.2.22版，修复漏洞数33个。

以下为按版本号排序的各版本漏洞修复统计（截止20260313版本）：

|  |  |  |
| --- | --- | --- |
| **版本** | **修复漏洞数** | **累计修复** |
| 2026.1.5 | 1 | 1 |
| 2026.1.20 | 1 | 2 |
| 2026.1.29 | 3 | 5 |
| 2026.1.30 | 2 | 7 |
| 2026.2.1 | 4 | 11 |
| 2026.2.2 | 9 | 20 |
| 2026.2.3 | 2 | 22 |
| 2026.2.6 | 2 | 24 |
| 2026.2.12 | 7 | 31 |
| 2026.2.13 | 7 | 38 |
| 2026.2.14 | 38 | 76 |
| 2026.2.15 | 9 | 85 |
| 2026.2.17 | 7 | 92 |
| 2026.2.19 | 19 | 111 |
| 2026.2.21 | 18 | 129 |
| 2026.2.22 | 33 | 162 |
| 2026.2.23 | 15 | 177 |
| 2026.2.24 | 12 | 189 |
| 2026.2.25 | 18 | 207 |
| 2026.2.26 | 15 | 222 |
| 2026.3.1 | 11 | 233 |
| 2026.3.2 | 11 | 244 |
| 2026.3.7 | 10 | 254 |
| 2026.3.8 | 3 | 257 |
| 2026.3.11 | 17 | 274 |
| 2026.3.12 | 8 | 282 |
| 2026.3.13 | 4 | 286 |

安全建议：

当前，OpenClaw整体安全风险集中于提示词注入攻击、供应链攻击（恶意Skills/插件）、配置不当导致的未授权访问、工具权限滥用、Webhook 与沙箱边界等方面。虽然OpenClaw漏洞整体数量较多，但影响主要为较早期版本，随着整体安全态势持续改善，最新版本已大幅收敛漏洞面。

针对OpenClaw可能存在的风险，建议所有用户：

1、定期更新。关注OpenClaw漏洞信息，重点关注高风险（公开POC或在野利用行为）漏洞，及时升级到最新版本。

2、启用认证机制，避免未授权访问。

3、网络隔离。将OpenClaw网关部署在受保护的网络环境中。

4、最小权限原则。限制Docker容器权限，避免沙箱逃逸。对所有外部输入（包括 WebSocket、API请求）进行严格的访问控制限制。

5、结合官方SECURITY.md信任模型配置部署，未来需持续关注插件扩展与Webhook模块的安全边界。

附OpenClaw高危漏洞统计：

有公开 POC：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K965EaNuia3HzOdrpMO4Wsfs8CvMiaZJcwoIaicWqDCSoLtdfjja61BKw4BEcoPqIM93q7EXwNnU2ePJD0Z2rzPF6fS6Cpr5H5YHsU/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

CVSS 严重级别漏洞清单，共11个严重级别漏洞：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K94XAkdDdVash72cPlec7jdCOuibsBRibicTfmjoI7KicFqcT8210qXEKibLCeXvglA21AQRpiaiaBn80tIaT6dRoHKsmothBZCjQUP9k8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

上述漏洞虽然官方评级较高，但由于没有公开PoC/在野利用行为，风险较为可控。

欢迎扫码试用

↓↓↓

![图片](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=7)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

微步在线研究响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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