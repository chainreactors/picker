---
title: Bitbucket 工件文件可能泄露明文身份验证机密
url: https://www.4hou.com/posts/L1NX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-14
fetch_date: 2025-10-06T16:55:25.649163
---

# Bitbucket 工件文件可能泄露明文身份验证机密

Bitbucket 工件文件可能泄露明文身份验证机密 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Bitbucket 工件文件可能泄露明文身份验证机密

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-06-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)181414

收藏

导语：威胁分子使用 Atlassian Bitbucket 工件文件以明文形式泄露的身份验证密钥来破坏 AWS 帐户。

威胁分子使用 Atlassian Bitbucket 工件文件以明文形式泄露的身份验证密钥来破坏 AWS 帐户。

Mandiant 率先发现该问题，他当时正在调查最近曝光的 Amazon Web Services (AWS) 机密，威胁分子利用这些机密来访问 AWS。

尽管该问题是在调查中发现的，但它说明了之前被认为是安全的数据可以以纯文本形式泄露到公共存储库。

**BitBucket 的安全变量**

Bitbucket 是一个与 Git 兼容的基于 Web 的版本控制存储库和托管服务，由 Atlassian 运行，为开发人员提供代码管理和协作平台。

Bitbucket Pipelines 是一种集成的持续交付/部署 (CI/CD) 服务，可自动执行构建、测试和部署流程。系统管理员通常将 Pipelines 直接链接到 AWS，以便快速部署应用程序并使用 AWS CLI、开发工具包和其他 AWS 工具访问资源。

为了促进这种自动化，Bitbucket 允许开发人员将敏感信息（例如 AWS 身份验证密钥）存储在“安全变量”中，以便在代码中轻松使用这些变量，而无需将密钥暴露给其他人。

![111.webp (1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240523/1716456973335924.jpg "1716456712205418.jpg")

在 Bitbucket 中存储安全变量

当变量在 BitBucket 中设置为安全时，它们将以加密形式存储，以防止在 Bitbucket 环境中公开暴露其值。

Bitbucket 文档解释说：“您可以保护变量，这意味着它可以在您的脚本中使用，但其值将隐藏在构建日志中（参见下面的示例）。如果想编辑安全变量，只能为其赋予新值或删除它。安全变量以加密值的形式存储。”

然而，Mandiant 发现，在管道运行期间生成的工件文件可能包含敏感信息，包括纯文本形式的安全变量。由于开发人员可能不知道这些秘密在工件文件中暴露，因此源代码可能会发布到公共存储库，威胁者可以从中窃取它们。

**明文形式的秘密**

工件在 bitbucket-pipelines.yml 配置文件中定义，用于指定 Bitbucket 项目的 CI/CD 流程。

这些文件中的指令之一是 artifacts:，用于指定导出到工件的变量、文件和目录，以便在构建和测试过程的进一步步骤中保留和使用。开发人员通常使用 printenv 命令将所有环境文件存储在文本文件中，然后将其传递给工件对象以供构建过程中的后续步骤使用。

![222.webp (1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240523/1716456973141068.jpg "1716456792166832.jpg")

将所有环境变量导出到工件文件

但是，这样做将导致“安全变量”以明文形式而不是以加密形式导出到工件文件。如果这些工件文件随后存储在公共位置，威胁分子只需打开文本文件并以明文形式查看所有变量，即可轻松窃取可用于窃取数据或执行其他恶意活动的身份验证机密。

![33.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240523/1716456974556522.jpg "1716456886204175.jpg")

以纯文本形式泄露机密的文本文件

报告中写道：“Mandiant 发现，开发团队在 Web 应用程序源代码中使用 Bitbucket 工件进行故障排除，但开发团队并不知道，这些工件包含密钥的纯文本值。这导致密钥暴露在公共互联网上，随后被攻击者利用，获得未经授权的访问权限。”

Mandiant 认为，另一种可能性是错误配置定义 CI/CD 管道的“bitbucket-pipelines.yml”文件，将安全变量包含在日志或工件中。当管道脚本出于调试目的记录环境变量时，它们可能会无意中记录敏感信息，而且由于这些日志通常存储在可访问的位置，因此再次存在密钥暴露的风险。

**缓解技巧**

Mandiant 提醒开发人员，Bitbucket 并非为管理机密而设计，建议使用专用的、专门的产品来实现此目的。还建议开发人员仔细检查工件，以确保生成的文件中不包含任何纯文本机密。

最后，建议在整个管道生命周期中部署代码扫描，以捕获秘密暴露事件并在代码到达生产之前将其删除。

文章翻译自：https://thecyberexpress.com/bitbucket-artifacts-could-expose-aws-secrets/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?qPQwPIWm)

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