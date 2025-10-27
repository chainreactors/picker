---
title: 超过 1000 个 ServiceNow 实例被发现泄露企业知识库数据
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578057&idx=1&sn=84dde8a7f93f3836923c97e32435b7ea&chksm=e91461f3de63e8e521d8e3bcc39ba5062c02cd270c2634165e63a416aaae8f2d20a8ce6e7fdb&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-09-21
fetch_date: 2025-10-06T18:28:23.661018
---

# 超过 1000 个 ServiceNow 实例被发现泄露企业知识库数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibUqLQtqY0H7MicX93K48J7Dqo1EzerF9GazgjMsaJC6A1jGH8WeRpW2SoeLiaKcQwMTVWm2e8XX2ibA/0?wx_fmt=jpeg)

# 超过 1000 个 ServiceNow 实例被发现泄露企业知识库数据

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

超过 1,000 个配置错误的 ServiceNow 企业实例被发现将包含敏感公司信息的知识库 (KB) 文章暴露给外部用户和潜在威胁者。暴露的信息包括个人身份信息 、内部系统详细信息、用户凭据、实时生产系统的访问令牌以及取决于知识库主题的其他重要信息。

尽管 ServiceNow 在 2023 年的更新明确旨在改进访问控制列表 (ACL)，但这仍然是一个重大问题。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibUqLQtqY0H7MicX93K48J7DficsJHHcCf5yahickhzz1I3fgcnvRURnibKTvT9BIEeA5N7HbdarHricQQ/640?wx_fmt=png&from=appmsg)公开的知识库文章

ServiceNow 是一个基于云的软件平台，企业使用它来管理跨不同部门和流程的数字工作流。它是一个完整的解决方案，包含 IT 服务和 IT 运营管理、人力资源任务、客户服务管理、安全工具集成和知识库。

知识库功能充当文章存储库，用户可以在其中共享操作指南、常见问题解答和其他内部程序，供有权查看这些内容的用户使用。但是，由于许多此类文章并非公开发布，因此它们可能包含有关组织的敏感信息。

在 2023 年发布有关 ServiceNow 数据泄露的报告后，该公司推出了一项安全更新，引入了新的 ACL，以防止未经身份验证访问客户数据。然而，AppOmni 表示，大多数 ServiceNow 知识库使用的是用户标准权限系统而不是 ACL，这使得更新的用处不大。

此外，一些面向公众的、暴露客户信息的小部件没有收到 2023 ACL 更新，并继续允许未经身份验证的访问。因此，Costello 表示，面向公众的 ServiceNow 小部件上配置错误的访问控制仍可用于查询知识库中的数据，而无需任何身份验证。

AppOmni 在发布的新报告中表示：“受影响的企业认为这些实例本质上是敏感的，例如 PII、内部系统详细信息以及实时生产系统的有效凭证/令牌。”使用 Burp Suite 等工具，恶意分子可以向易受攻击的端点发送大量 HTTP 请求，以暴力破解知识库文章编号。

研究人员解释说，知识库文章 ID 以 KBXXXXXXX 格式递增，因此威胁者可以通过从 KB0000001 开始递增 KB 编号来暴力破解 ServiceNow 实例，直到找到一个无意中暴露的实例。

AppOmni 开发了一个概念验证攻击，以说明外部如何在没有身份验证的情况下访问 ServiceNow 实例、捕获用于 HTTP 请求的令牌、查询公共小部件以检索 KB 文章，以及暴力破解所有托管文章的 ID。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibUqLQtqY0H7MicX93K48J7DzZZJJQ1K4MR8qJRwI9PVGFwX91PNtX2fCICl583yq0RhSciaC04UlYA/640?wx_fmt=png&from=appmsg)

示例请求（左）和令牌拦截（右）

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibUqLQtqY0H7MicX93K48J7DficsJHHcCf5yahickhzz1I3fgcnvRURnibKTvT9BIEeA5N7HbdarHricQQ/640?wx_fmt=png&from=appmsg)阻止未经授权的访问

AppOmni 建议 SecureNow 管理员通过设置适当的“用户标准”（可以读取/不能读取）来保护 KB 文章，阻止所有未经授权的用户。

“任何用户”或“访客用户”等标准会导致配置无法保护文章免受任意外部访问。如果没有明确需要公开访问知识库，管理员应将其关闭，以防止文章在互联网上被访问。

研究人员还强调了特定的安全属性，即使在配置错误的情况下，也可以保护数据免遭未经授权的访问。这些是：

**·**glide.knowman.block\_access\_with\_no\_user\_criteria（True）：确保如果未为 KB 文章设置用户标准，则自动拒绝经过身份验证和未经身份验证的用户访问。

**·**glide.knowman.apply\_article\_read\_criteria（True）：要求用户对单个文章具有明确的“可以阅读”访问权限，即使他们对整个 KB 具有“可以贡献”访问权限。

**·**glide.knowman.show\_unpublished（False）：阻止用户查看草稿或未发布的文章，其中可能包含敏感的未审核信息。

**·**glide.knowman.section.view\_roles.draft（管理员）：定义可以查看草稿状态的知识库文章的角色列表。

**·**glide.knowman.section.view\_roles.review（管理员）：定义可以查看审核状态的知识库文章的角色列表。

**·**glide.knowman.section.view\_roles.stagesAndRoles（管理员）：定义可以查看自定义状态的知识库文章的角色列表。

最后，建议激活 ServiceNow 预先构建的开箱即用 (OOB) 规则，该规则会自动将来宾用户添加到新创建的知识库的“无法读取”列表中，要求管理员在需要时专门授予他们访问权限。

参考及来源：https://www.bleepingcomputer.com/news/security/over-1-000-servicenow-instances-found-leaking-corporate-kb-data/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibUqLQtqY0H7MicX93K48J7D3lEtYLYCMpsrEaWasTC6Avibm72NSDLA8sgoEyEkgNb2J0mmBpMQsHA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibUqLQtqY0H7MicX93K48J7DYI1MrhVlSrplg82sic94K3fnzq5siaNqlhEib9R7VxicsIBc1MLibtXAlOA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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