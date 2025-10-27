---
title: GitHub Actions 工件在热门项目中被发现泄露身份验证令牌
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546571&idx=2&sn=e8b826122b385286b6d9a16ac59f2ceb&chksm=fa93800acde4091caace55bfbd3bf7c84ce4574b27abd08c9fde086de84ff09debcff99ff424&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-24
fetch_date: 2025-10-06T18:05:38.686450
---

# GitHub Actions 工件在热门项目中被发现泄露身份验证令牌

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mxzrSiaf7o2PBUQUCuN4LWoaERvIsv7f4ep885gd8V5qmibYBLUOFf3xQibTcS0muA63P0mgXZI0B9A/0?wx_fmt=jpeg)

# GitHub Actions 工件在热门项目中被发现泄露身份验证令牌

网络安全应急技术国家工程中心

近期，包括谷歌、微软、AWS 和 Red Hat 在内的多个知名开源项目被发现在 CI/CD 工作流中通过 GitHub Actions 工件泄露 GitHub 身份验证令牌。窃取这些令牌的攻击者可以未经授权访问私有存储库、窃取源代码或将恶意代码注入项目。

Palo Alto Networks 的 Unit 42 率先发现了这一问题，促使热门存储库的所有者采取行动，因为机密信息通过 GitHub Actions 构件泄露。然而，由于 GitHub 决定不解决这一风险，而是将保护构件的责任推给用户，因此根本问题仍未得到解决。

鉴于这种情况，GitHub 用户需要了解风险，评估其暴露情况，并采取措施防止将来发生泄露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIAdCCVSe1gTz7xNRQztQJmEVeUL2PAkJqnnagAWCzj1lIJk9ibUn0MMeg/640?wx_fmt=png&from=appmsg&wxfrom=13)

GitHub Actions 生成的工件

# **泄露 GitHub 令牌**

Unit 42 的报告强调了一系列因素，包括不安全的默认设置、用户配置错误和安全检查不足，这些因素可能导致 GitHub 令牌泄露，即所谓的“ArtiPACKED”攻击。

第一个风险点是“actions/checkout”操作，该操作通常用于 GitHub 工作流中克隆存储库代码，以便在工作流运行期间可用。默认情况下，此操作会将 GitHub 令牌保留到本地 .git 目录（隐藏），这是工作流内经过身份验证的操作所必需的。

如果用户错误地将整个结帐目录作为工件的一部分上传，则 git 文件夹内的 GitHub 令牌将被暴露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIAbneQxP5Ih9uuIJ8V0ac5LVcibiasFIBWN0E7KeSquXJMXZfFvsicib5okg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
公开的 GitHub 令牌

该文件夹中可能包含的其他敏感信息包括 API 密钥、云服务访问令牌和各种帐户凭据。

在 CI/CD 过程中生成的工件（例如构建输出和测试结果）可能会因错误上传而暴露，这些工件的存储期限最长为三个月，可供访问。

另一个故障点是使用环境变量存储 GitHub 令牌的 CI/CD 管道。如果工作流中的操作或脚本有意或无意地记录了这些变量，则日志将作为工件上传。

Unit 42 指出，当“CREATE\_LOG\_FILE”属性设置为“True”时，“super-linter”操作可以创建包含环境变体的详细日志。

# **利用泄漏**

最终，攻击者会试图利用特定的竞争条件场景，其中必须从日志中提取短暂的 GitHub 令牌并在其过期之前使用。

GitHub 令牌在工作流作业期间保持有效，因此其利用潜力因情况而异。GitHub 内部用于缓存和管理工件的“Actions\_Runtime\_Token”通常有效期为 6 小时，因此利用窗口很小。

自定义密钥和令牌（例如 API 密钥或云服务访问令牌）的使用寿命各不相同，从几分钟到永不过期。

Unit 42 介绍了一种攻击场景，该场景识别使用 GitHub Actions 的项目或公共存储库，并使用自动化脚本扫描它们以查找增加工件生成可能性的标准。

另一组脚本可以自动从目标存储库的 CI/CD 管道下载工件，对于公共存储库而言，这是一个简单的过程。然后，它会仔细检查其中的机密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icGXtXwjQ1pEjhGo4h3WqIADSBvdfiaicZ0rLyktvlnJqyCOwAuqvOiaPTpPKrJ8cibicmT7ic0YAmWqibcA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

攻击流

# **补救**

Unit 42 确定了以下 14 个大型开源项目使用 GitHub 令牌公开工件的案例，并将其报告给受影响方以进行补救：

·Firebase (谷歌)

·OpenSearch Security (AWS) Clair (红帽)

·Active Directory System (Adsys) (Canonical) JSON Schemas (微软)

·TypeScript Repos Automation、TypeScript Bot Test Triggerer、Azure Draft (微软)

·CycloneDX SBOM (OWASP)

·Stockfish

·Libevent

·Guardian for Apache Kafka (Aiven-Open)

·Git Annex (Datalad)

·Penrose

·Deckhouse

·Concrete-ML (Zama AI)

一般而言，建议 GitHub 用户避免在已上传的工件中包含整个目录，清理日志，并定期检查 CI/CD 管道配置。

应调整“actions/checkout”等危险操作的默认设置，以使凭据不会持续存在。此外，工作流程中使用的令牌权限应设置为必要的最小特权，以最大程度避免暴露时造成的损害。

**参考及来源：**
https://www.bleepingcomputer.com/news/security/github-actions-artifacts-found-leaking-auth-tokens-in-popular-projects/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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