---
title: Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器
url: https://www.4hou.com/posts/om3A
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-12
fetch_date: 2026-01-13T03:26:08.691316
---

# Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器

Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9260

收藏

导语：这一漏洞可被滥用于泄露存储在实例中的密钥、将敏感文件注入工作流、伪造会话Cookie以绕过身份验证，甚至执行任意命令。

研究人员最新发现，一项被命名为Ni8mare的最高严重级漏洞，允许远程未授权攻击者完全接管本地部署的N8N工作流自动化平台。

该安全漏洞编号为CVE-2026-21858，CVSS评分高达10分。据研究人员称，目前互联网上存在超过10万台易受攻击的N8N服务器。

N8N是一款开源工作流自动化工具，用户可通过可视化编辑器将各类应用、API及服务连接成复杂的工作流。它主要用于任务自动化，并支持与人工智能及大语言模型服务的集成。

该工具在npm上的周下载量超过5万次，在Docker Hub上的拉取量更是突破1亿次。作为AI领域的热门工具，它常被用于编排LLM调用、构建AI智能体（Agent）和检索增强生成（RAG）流水线，以及自动化数据摄入与检索。

**Ni8mare漏洞技术细节**

Ni8mare漏洞允许攻击者通过执行特定的基于表单的工作流，访问底层服务器上的文件。

N8N开发者表示：“存在漏洞的工作流可能会授予未授权远程攻击者访问权限。这可能导致存储在系统上的敏感信息泄露，并且根据部署配置和工作流的使用情况，可能会导致进一步的入侵。”

研究人员于2025年11月发现了该漏洞并向N8N官方报告。他们指出，该漏洞源于N8N在解析数据时存在的 内容类型混淆问题。

N8N使用两个不同的函数来处理传入数据，具体取决于Webhook中配置的content-type头部信息——Webhook是通过监听特定消息来触发工作流事件的组件。

当Webhook请求被标记为multipart/form-data时，N8N会将其视为文件上传，并使用特殊的上传解析器，将文件保存在随机生成的临时位置。

这意味着用户无法控制文件的最终存放路径，从而防范了路径遍历攻击。然而，对于所有其他内容类型，N8N则使用标准解析器。

攻击者可以通过设置不同的内容类型（例如 application/json）来绕过上传解析器。在这种情况下，N8N仍会处理与文件相关的字段，但不会验证请求中是否真的包含有效的文件上传。这使得攻击者能够完全控制文件元数据，包括文件路径。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260108/1767858263158015.png "1767858229205269.png")

存在缺陷的解析器逻辑

研究员解释：由于调用该函数时未验证内容类型是否为 multipart/form-data，所以可以控制整个req.body.files对象。这意味着我们控制了 filepath`参数——因此，无需复制上传的文件，而是可以复制系统中的任何本地文件。

这使得攻击者能够从N8N实例中读取任意文件，通过将内部文件添加到工作流的知识库中，从而泄露敏感信息。

这一漏洞可被滥用于泄露存储在实例中的密钥、将敏感文件注入工作流、伪造会话Cookie以绕过身份验证，甚至执行任意命令。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260108/1767858271162189.png "1767858271162189.png")

触发 Ni8mare (CVE-2026-21858) 访问数据库

N8N通常存储着API密钥、OAuth令牌、数据库凭证、云存储访问权限、CI/CD密钥及业务数据，使其成为企业的核心自动化枢纽。

N8N开发者表示，目前针对Ni8mare漏洞尚无官方临时缓解措施，但建议限制或禁用可公开访问的Webhook和表单端点。且强烈建议用户立即更新至N8N 1.121.0版本或更高版本。

文章来源自：https://www.bleepingcomputer.com/news/security/max-severity-ni8mare-flaw-lets-hackers-hijack-n8n-servers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Uj3WrIn6)

#### 你可能感兴趣的

* [![]()

  Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)
* [![]()

  WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)
* [![]()

  MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)
* [![]()

  漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)
* [![]()

  黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)
* [![]()

  新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)
  2026-01-12 12:00:00
* [WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)
  2026-01-04 12:00:00
* [MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)
  2025-12-31 12:00:00
* [漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)
  2025-12-30 10:29:10

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Ni8mare高危漏洞来袭 黑客可远程劫持n8n服务器](https://www.4hou.com/posts/om3A)

  胡金鱼
* [WebRAT恶意软件借GitHub伪造漏洞利用程序传播](https://www.4hou.com/posts/Bvw2)

  胡金鱼
* [MongoBleed高危漏洞遭在野利用 8万台MongoDB服务器暴露风险](https://www.4hou.com/posts/OGNB)

  胡金鱼
* [漏洞预警 | MongoDB 存在未授权内存泄露漏洞（CVE-2025-14847）](https://www.4hou.com/posts/QXPM)

  盛邦安全
* [黑客利用 Gladinet CentreStack 加密漏洞发起远程代码执行攻击](https://www.4hou.com/posts/XPN8)

  胡金鱼
* [新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)

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