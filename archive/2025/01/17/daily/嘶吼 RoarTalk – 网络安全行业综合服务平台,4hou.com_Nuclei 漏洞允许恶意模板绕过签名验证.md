---
title: Nuclei 漏洞允许恶意模板绕过签名验证
url: https://www.4hou.com/posts/xyjP
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-17
fetch_date: 2025-10-06T20:08:29.246655
---

# Nuclei 漏洞允许恶意模板绕过签名验证

Nuclei 漏洞允许恶意模板绕过签名验证 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Nuclei 漏洞允许恶意模板绕过签名验证

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-01-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)86722

收藏

导语：YAML 模板还包括一个代码协议，可用于在扩展模板功能的设备上本地执行命令或脚本。

最新发现开源漏洞扫描器 Nuclei 中现已修复的漏洞可能允许攻击者绕过签名验证，同时将恶意代码潜入在本地系统上执行的模板中。

Nuclei 是 ProjectDiscovery 创建的一款流行的开源漏洞扫描程序，可扫描网站是否存在漏洞和其他弱点。该项目使用基于模板的扫描系统，该系统包含 10,000 多个 YAML 模板，可扫描网站是否存在已知漏洞、错误配置、暴露的配置文件、Webshell 和后门。

YAML 模板还包括一个代码协议，可用于在扩展模板功能的设备上本地执行命令或脚本。每个模板都使用摘要哈希进行“签名”，Nuclei 使用摘要哈希来验证模板是否未被修改以包含恶意代码。该摘要哈希以以下形式添加到模板的底部：

```
# digest:
```

**漏洞绕过 Nuclei 签名验证**

Wiz 研究人员发现了一个名为 CVE-2024-43405 的新 Nuclei 漏洞，即使模板被修改为包含恶意代码，该漏洞也会绕过 Nuclei 的签名验证。

该问题是由基于 Go 正则表达式的签名验证以及 YAML 解析器在验证签名时处理换行符的方式引起的。当验证签名时，Go 的验证逻辑将 \r 视为同一行的一部分。

但是，YAML 解析器将其解释为换行符。这种不匹配允许攻击者注入绕过验证但在 YAML 解析器处理时仍会执行的恶意内容。另一个问题是 Nuclei 如何处理多个 #digest: 签名行，因为该过程仅检查模板中第一次出现的 #digest:，而忽略模板中稍后发现的任何其他内容。

可以通过在包含恶意“代码”部分的初始有效摘要之后添加额外的恶意“#digest:”有效负载来利用此漏洞，然后在使用模板时注入并执行该有效负载。

Wiz 研究员解释说：“有了关于不匹配换行符解释的见解，我们制作了一个模板，利用 Go 的正则表达式实现和 YAML 解析器之间的差异。通过使用 \r 作为换行符，可以在模板中包含第二个 # 摘要：行，该行可以逃避签名验证过程，但由 YAML 解释器解析并执行。”

![1735840138-code-diagram[1].webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250106/1736133402175511.png "1736133248764845.png")

不同解析器如何解析 Nuclei 模板的示例

Wiz 于 2024 年 8 月 14 日向 ProjectDiscovery 披露了该漏洞，并于 9 月 4 日在 Nuclei v3.3.2 中对其进行了修复。如果使用的是旧版本的 Nuclei，安全研究人员强烈建议用户更新最新版本。此外，Goldenberg 还建议在虚拟机或隔离环境中使用 Nuclei，以防止恶意模板的潜在利用。

文章翻译自：https://www.bleepingcomputer.com/news/security/nuclei-flaw-lets-malicious-templates-bypass-signature-verification/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BmIxcw72)

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