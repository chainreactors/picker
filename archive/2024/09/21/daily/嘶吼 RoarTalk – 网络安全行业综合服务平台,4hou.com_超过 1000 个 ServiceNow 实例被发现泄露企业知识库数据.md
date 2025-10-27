---
title: 超过 1000 个 ServiceNow 实例被发现泄露企业知识库数据
url: https://www.4hou.com/posts/XP5k
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-21
fetch_date: 2025-10-06T18:25:02.600507
---

# 超过 1000 个 ServiceNow 实例被发现泄露企业知识库数据

超过 1000 个 ServiceNow 实例被发现泄露企业知识库数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 超过 1000 个 ServiceNow 实例被发现泄露企业知识库数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-09-20 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)102074

收藏

导语：在 2023 年发布有关 ServiceNow 数据泄露的报告后，该公司推出了一项安全更新，引入了新的 ACL，以防止未经身份验证访问客户数据。

超过 1,000 个配置错误的 ServiceNow 企业实例被发现将包含敏感公司信息的知识库 (KB) 文章暴露给外部用户和潜在威胁者。暴露的信息包括个人身份信息 、内部系统详细信息、用户凭据、实时生产系统的访问令牌以及取决于知识库主题的其他重要信息。

尽管 ServiceNow 在 2023 年的更新明确旨在改进访问控制列表 (ACL)，但这仍然是一个重大问题。

**公开的知识库文章**

ServiceNow 是一个基于云的软件平台，企业使用它来管理跨不同部门和流程的数字工作流。它是一个完整的解决方案，包含 IT 服务和 IT 运营管理、人力资源任务、客户服务管理、安全工具集成和知识库。

知识库功能充当文章存储库，用户可以在其中共享操作指南、常见问题解答和其他内部程序，供有权查看这些内容的用户使用。但是，由于许多此类文章并非公开发布，因此它们可能包含有关组织的敏感信息。

在 2023 年发布有关 ServiceNow 数据泄露的报告后，该公司推出了一项安全更新，引入了新的 ACL，以防止未经身份验证访问客户数据。然而，AppOmni 表示，大多数 ServiceNow 知识库使用的是用户标准权限系统而不是 ACL，这使得更新的用处不大。

此外，一些面向公众的、暴露客户信息的小部件没有收到 2023 ACL 更新，并继续允许未经身份验证的访问。因此，Costello 表示，面向公众的 ServiceNow 小部件上配置错误的访问控制仍可用于查询知识库中的数据，而无需任何身份验证。

AppOmni 在发布的新报告中表示：“受影响的企业认为这些实例本质上是敏感的，例如 PII、内部系统详细信息以及实时生产系统的有效凭证/令牌。”使用 Burp Suite 等工具，恶意分子可以向易受攻击的端点发送大量 HTTP 请求，以暴力破解知识库文章编号。

研究人员解释说，知识库文章 ID 以 KBXXXXXXX 格式递增，因此威胁者可以通过从 KB0000001 开始递增 KB 编号来暴力破解 ServiceNow 实例，直到找到一个无意中暴露的实例。

AppOmni 开发了一个概念验证攻击，以说明外部如何在没有身份验证的情况下访问 ServiceNow 实例、捕获用于 HTTP 请求的令牌、查询公共小部件以检索 KB 文章，以及暴力破解所有托管文章的 ID。

![screen.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240918/1726647465143286.png "1726646046206089.png")

示例请求（左）和令牌拦截（右）

**阻止未经授权的访问**

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

文章翻译自：https://www.bleepingcomputer.com/news/security/over-1-000-servicenow-instances-found-leaking-corporate-kb-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4uqbKnld)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)