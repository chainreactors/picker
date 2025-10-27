---
title: 最新网络钓鱼活动利用损坏的 Word 文档来规避检测
url: https://www.4hou.com/posts/vwRL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-14
fetch_date: 2025-10-06T19:37:34.456729
---

# 最新网络钓鱼活动利用损坏的 Word 文档来规避检测

最新网络钓鱼活动利用损坏的 Word 文档来规避检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 最新网络钓鱼活动利用损坏的 Word 文档来规避检测

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-12-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113451

收藏

导语：如果收到来自未知发件人的电子邮件，尤其是包含附件的电子邮件，应立即将其删除或在打开之前与网络管理员确认。

新出现的网络钓鱼攻击滥用 Microsoft 的 Word 文件恢复功能，将损坏的 Word 文档作为电子邮件附件发送，使它们能够绕过安全软件，但仍可由应用程序恢复。

威胁者不断寻找新方法来绕过电子邮件安全软件并将网络钓鱼电子邮件放入目标的收件箱中。恶意软件狩猎公司 Any.Run 发现了一种新的网络钓鱼活动，利用故意损坏的 Word 文档作为电子邮件中的附件。

![email-phishing.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241202/1733129042135451.png "1733128899161252.png")

这些附件使用广泛的主题，几乎全部围绕员工福利和奖金。打开附件时，Word 将检测到文件已损坏，并指出它在文件中“发现不可读的内容”，询问您是否要恢复它。

![corrupted-word-doc-attachment.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241202/1733129043321444.png "1733128877794840.png")

这些网络钓鱼文档的损坏方式很容易恢复，并显示一个文档，告诉目标扫描二维码以检索文档。如下所示，这些文档都带有目标公司的徽标，例如下面所示的示例：

![word-document.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241202/1733129049187866.png "1733128944167297.png")修复后的Word文档

扫描二维码会将用户带到一个冒充 Microsoft 登录名的钓鱼网站，试图窃取用户的凭据。

![phishing-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241202/1733129050164672.png "1733128999515560.png")

网络钓鱼页面窃取 Microsoft 凭据

虽然这种网络钓鱼攻击的最终目标并不新鲜，但它使用损坏的 Word 文档是一种逃避检测的新策略。尽管这些文件在操作系统中可以成功运行，但由于未能对其文件类型应用正确的程序，大多数安全解决方案仍然无法检测到它们。

它们已上传到 VirusTotal，但所有防病毒解决方案都返回“干净”或“未找到项目”，因为它们无法正确分析该文件。因此，这些附件相当成功地实现了他们的目标。

从附件来看，几乎所有附件在 VirusTotal 上的检测量都是零 [1,2,3,4]，只有一些 [1] 由 2 个供应商检测到。同时，这也可能是由于文档中没有添加恶意代码，仅显示二维码所致。一般规则仍然适用于保护用户免受网络钓鱼攻击。

如果收到来自未知发件人的电子邮件，尤其是包含附件的电子邮件，应立即将其删除或在打开之前与网络管理员确认。

文章翻译自：https://www.bleepingcomputer.com/news/security/novel-phishing-campaign-uses-corrupted-word-documents-to-evade-security/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?nTQh6ry3)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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