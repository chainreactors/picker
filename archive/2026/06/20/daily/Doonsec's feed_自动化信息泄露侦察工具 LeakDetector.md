---
title: 自动化信息泄露侦察工具 LeakDetector
url: https://mp.weixin.qq.com/s/tvpAH_6X8LpQcdRl_lpNiQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:45:40.078817
---

# 自动化信息泄露侦察工具 LeakDetector

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVkDw2oJtNKqHus1ZEqs6Z2icvhczFIDfhfZia7ficz49KARVfZv1zWzF5tYFJZec3rUtic43K83ga7bpTyN0VWReIMYjKU360Nsltg/0?wx_fmt=jpeg)

# 自动化信息泄露侦察工具 LeakDetector

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 731，阅读大约需 4 分钟

## 前言

**LeakDetector** 是一款专为红队渗透测试人员和安全研究员设计的**自动化信息泄露侦察工具**。它基于 Bing 搜索引擎的高级语法（Dork），结合 Playwright 浏览器自动化技术，能够高效、精准地发现互联网上由于配置不当、运维疏忽或系统漏洞而暴露的敏感信息。

项目地址：https://github.com/cbbzx12/LeakDetector

* • 未开源
* • 可运行在 Windows、linux、MacOS

![10cb1b34a0d50940a1ea2e1c5571eb84.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVm5YYQF8ic896VG5D5fibia5ibU76bQpkKxic1MsrYlYoSnhLVXSjTt8kVK8QEbF7rknxhcGjSNOMYhbEv3icQCMicU4xY1fxCPj4jib6Q/640?from=appmsg "null")

10cb1b34a0d50940a1ea2e1c5571eb84.png

下载地址：https://github.com/cbbzx12/LeakDetector/releases/tag/v1.2

![227ce9ccdac050255f8055f2cd3a5099.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl0HHBjgKaxibiczdySibCsYmlAO1vCia3m0J2IiaVQicqibw5L41oaSouhJMZic1gm6IbWsbd30FgDTdI4pSOlAVcDU4zLDjIFDNUfctw/640?from=appmsg "null")

227ce9ccdac050255f8055f2cd3a5099.png

与传统脚本不同，LeakDetector 引入了**智能抗反爬机制**和**深度内容分析引擎**，支持从数千个结果中自动筛选出高价值的敏感文件（如 Excel 通讯录、身份证名单、API 密钥配置等），并自动生成可视化的审计报告。

![dc43150101c9f0d50942c5a11f2df980.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnicYjqicW431A3ib0cTpfXXoGEWsl3wAO2JQGTXxNmyP6wl47jEYypJSKtHcPicwZliaf1yNMKVjuSrrXI9ML9Z7kBKx38wXNiceqmY/640?from=appmsg "null")

dc43150101c9f0d50942c5a11f2df980.png

## 侦察策略详解 (Dork Strategies)

LeakDetector 将搜索语法分为 6 个优先级，用户可根据场景选择：

| 级别 | 策略名称 | 描述 | 典型语法示例 |
| --- | --- | --- | --- |
| **P1** | **基础设施 & API** | **[必跑]** 核心配置与接口暴露，杀伤力最大。 | `inurl:swagger` , `inurl:actuator/env`, `filename:pom.xml` |
| **P2** | **精准文件泄露** | **[高危]** 针对 Excel/PDF 的精准打击，提取 PII。 | `filetype:xlsx "通讯录"` , `filetype:xlsx "身份证"` |
| **P3** | **后台与 OA** | 企业级后台入口、SSO 认证、OA 系统。 | `inurl:login` , `inurl:seeyon` (致远), `inurl:weaver` (泛微) |
| **P4** | **行业特征 (Edu/Gov)** | 针对学校/政府的特有敏感词。 | `"教务系统"` , `"录取名单"`, `"中标公告"`, `filetype:xlsx "学号"` |
| **P5** | **漏洞技术细节** | SQL 注入报错、Webshell、上传点、源码泄露。 | `inurl:php?id=` , `intext:"sql syntax near"`, `ext:sql` |
| **P6** | **运维与云设施** | DevOps 平台、VPN 入口、云存储密钥。 | `inurl:jenkins` , `filename:id_rsa`, `filename:web.config` |

## 核心特性 (Key Features)

### 1. 多维度 Dork 侦察策略

内置经过实战验证的六层侦察策略 (P1-P6)，覆盖从基础设施到敏感数据的全方位检测：

* • **API & 配置泄露**: 自动发现 Swagger UI, Spring Boot Actuator, `.env`, `application.yml` 等关键配置。
* • **精准文件挖掘**: 专注于 `xlsx`, `docx`, `pdf` 等文档，智能识别包含"身份证"、"手机号"、"工资表"等敏感词的文件。
* • **后台与组件识别**: 快速定位 OA 系统 (泛微/致远)、后台管理入口、Jenkins/GitLab 等运维平台。
* • **漏洞特征探测**: 识别 SQL 注入报错页面、文件上传入口、Webshell 残留等高危特征。

### 2. 智能浏览器引擎 (Smart Browser Engine)

集成 **Playwright** 浏览器内核，彻底解决传统爬虫面临的难题：

* • **自动/手动绕过验证码**: 支持检测 Bing 的 Turnstile/ReCAPTCHA 验证，支持在 GUI 中自动暂停并引导用户手动过验证，**彻底解决 IP 封禁导致的无结果问题**。
* • **动态渲染抓取**: 能够处理依赖 JavaScript 加载的搜索结果，获取比纯 HTTP 请求更完整的数据。

等等

## 总结

项目地址：https://github.com/cbbzx12/LeakDetector

类似的工具还有：
Fir-Fetch https://github.com/11firefly11/Fir-Fetch

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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