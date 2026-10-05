---
title: 一款面向现代 Web 安全研究的轻量级渗透测试平台——Caido
url: https://mp.weixin.qq.com/s/3XN9keflBwF2UJL3GCZ8Gw
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:53:46.797629
---

# 一款面向现代 Web 安全研究的轻量级渗透测试平台——Caido

# 一款面向现代 Web 安全研究的轻量级渗透测试平台——Caido

原创

wolfsec
wolfsec

风铃Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

声明：仅用于授权测试，用户滥用造成的一切后果和作者无关 请遵守法律法规！出于对安全考量本公众号发布的所有文章中的工具均建议放在虚拟机中运行！【无需回复关键字，文中第二部分0x02获取工具】

**0x01 工具简介**

Caido 是一款轻量级的 Web 安全审计与渗透测试工具，旨在帮助安全研究人员和渗透测试人员更加高效地发现和验证 Web 应用漏洞。 它提供 HTTP 代理、请求拦截、流量分析、请求重放、自动化测试等功能，可用于手工安全测试和漏洞研究。 相比传统 Web 安全测试工具，Caido 注重高性能、简洁易用以及可扩展性，支持通过插件和工作流增强测试能力。 该工具常被用于 Bug Bounty、安全评估以及 Web 应用渗透测试场景。Caido 是一款面向现代 Web 安全研究的轻量级渗透测试平台，通过高性能代理、HTTPQL 流量查询、自动化工作流和可扩展插件体系，帮助安全人员更高效地完成 Web 应用漏洞分析与安全评估。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsqsP3HkricnOFEt2X7xEX8IsU0jZuZsFACh7AEzUok7SluePicbwTsx6u7Zl1tqxEdqKpJPntL0uUnNMGpLiacxfrFpAia33jaxSM/640?wx_fmt=png&from=appmsg)

**0x02 工具使用**

##### Sitemap（站点地图）

当你通过 Caido 代理目标流量时，所访问的域名、子域名以及其中包含的资源会自动被收集，并在 `Sitemap` 界面中以层级化的树状结构进行展示。该功能以直观的可视化方式呈现目标站点的目录结构和资源分布，帮助安全测试人员快速了解目标 Web 应用的整体架构与文件组织情况。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZluQ7J9aZQRsfuu4kS6zu7KeQ0VXlMFSGT9gMeZNicibXrGo0nDHcnT2T45rMpp139FYoxqmytp53EJJxxz6SbcT531emaIflotibY/640?wx_fmt=png&from=appmsg)

##### Workflows（工作流）

在 `Workflows` 界面中，你可以构建由多个步骤组成的自动化流程，用于执行特定操作或数据转换。通过工作流功能，可以将重复性的测试任务进行自动化处理，并根据需求选择立即执行、手动触发或周期性运行，从而提高安全测试过程中的效率与灵活性。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlv01HnXdYr8wCT7mEQLthH2ONsIHPZuVVNIz1on8qjs46UG2ChNDRGB6FVeCIBuoCKtiazabuplDtLXcDdU5BECpvTpJKGFJU4U/640?wx_fmt=png&from=appmsg)

##### Search（搜索）

`Search` 界面提供了一个集中化的数据表，用于展示所有经过 Caido 代理捕获或由 Caido 生成的 HTTP 请求及其对应响应内容。通过该功能，用户可以快速检索、筛选和分析历史流量数据，方便在 Web 安全测试过程中定位目标请求、发现潜在问题并进行进一步分析。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZltHh3LRHEIc03bjJqNbmCJL1yCYqYHuHaHNfSia9k3aTAlZnjMicvjsYaeWmzbpdRyRBndyiaeZqheBalHZ60JibHNbYpib2NeCkqxc/640?wx_fmt=png&from=appmsg)

##### Environment（环境变量）

`Environment` 界面允许用户定义和管理变量集合，并将这些变量动态插入到 HTTP 请求中。通过环境配置功能，用户可以在不同测试场景之间快速切换上下文，例如切换目标环境、认证信息或请求参数，从而提高安全测试过程中的灵活性与效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsibf3UajDJwsSAemGskouhFRibPIdMfofEf1iakcibqnL1VIoGbarBdTELrF12tk6azOLLVhYdZLw4Aqa58XnFib6Fke4X2xa8IAEg/640?wx_fmt=png&from=appmsg)

##### Plugins（插件）

`Plugins` 界面允许用户在 Caido 中安装和管理插件包，以扩展平台的功能和能力。通过插件系统，用户可以根据自身安全测试需求进行高度定制，例如添加自动化检测、流量分析、数据处理等功能，从而打造更加符合个人工作流程的测试环境。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZluT27RNb9dib9okThQOlnZILia0nFLCia15pURqK3ZdzOiaveCtLGFraLFCmcicRSQS93X9KJ9Jib3xXbSClgia5VO90CS72hvu0lIh20/640?wx_fmt=png&from=appmsg)

**0x03 下载链接**

```
后台回复：20261004获取下载链接
```

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HmibOdP6ibKTOYNXKuEdbPFJKnX0Z54TIaWXmS6apnB5FYRgZVtWlzvTJK3lQzuxEHTa5kCSibf2eXZw/0?wx_fmt=png)

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