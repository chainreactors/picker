---
title: Sitecore内容管理系统漏洞链始于在设置硬编码密码时的疏漏
url: https://www.4hou.com/posts/xy0q
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-27
fetch_date: 2025-10-06T22:50:27.900761
---

# Sitecore内容管理系统漏洞链始于在设置硬编码密码时的疏漏

Sitecore内容管理系统漏洞链始于在设置硬编码密码时的疏漏 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Sitecore内容管理系统漏洞链始于在设置硬编码密码时的疏漏

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-06-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)60182

收藏

导语：Sitecore是一个流行的企业CMS，用于企业创建和管理跨网站和数字媒体的内容。

Sitecore Experience Platform （XP）漏洞链允许攻击者在没有身份验证的情况下执行远程代码执行（RCE）来破坏和劫持服务器。

Sitecore是一个流行的企业CMS，用于企业创建和管理跨网站和数字媒体的内容。由watchtower研究人员发现，近期披露的预认证RCE链包含三个不同的漏洞。它取决于内部用户（sitecore\ServicesAPI）的存在，其硬编码密码设置为“b”，使其易于劫持。

这个内置用户不是管理员，也没有分配角色。然而，研究人员仍然可以使用它通过另一个登录路径（/sitecore/admin）进行身份验证，因为sitecore的仅后端登录检查在非核心数据库上下文中被绕过。

结果是一个有效的".AspNetCookies"会话，使攻击者能够获得通过IIS级授权但不受Sitecore角色检查保护的内部端点的已认证访问权限。

有了这个最初的立足点，攻击者就可以利用第二个漏洞，即Sitecore上传向导中的Zip Slip漏洞。

正如watchtower解释的那样，通过向导上传的ZIP文件可能包含恶意文件路径，如/\/../webshell.aspx。由于路径清理不足和Sitecore映射路径的方式，这导致将任意文件写入web浏览器，甚至不知道完整的系统路径。这使得攻击者可以上传webshell并执行远程代码。

当安装了Sitecore PowerShell Extensions （SPE）模块（通常与SXA捆绑在一起）时，第三个漏洞就会被利用。

此漏洞允许攻击者将任意文件上传到攻击者指定的路径，完全绕过扩展名或位置限制，并提供通往可靠RCE的更简单路径。

**影响和风险**

watchtower报告的三个漏洞影响了Sitecore XP 10.1到10.4版本。WatchTowr的扫描显示有超过22000个公开暴露的Sitecore实例，这突显出一个显著的攻击面，尽管并非所有实例都一定存在漏洞。

针对这些问题的补丁于2025年5月发布，但CVE id和技术细节要到2025年6月17日才能发布，以便客户有时间更新。

Sitecore被部署在数千个环境中，包括银行、航空公司和全球企业，影响广泛。Sitecore表示他们已经全程运行了。如果使用Sitecore，在攻击者不可避免地逆向工程修复之前，应立即旋转凭据并进行修补。

截至目前，尚无公开证据表明存在野外利用。然而，watchTowr的技术博客包含了足够的细节来构建一个完整的工作漏洞，因此对于避免滥用的问题仍旧迫在眉睫。

文章翻译自：https://www.bleepingcomputer.com/news/security/sitecore-cms-exploit-chain-starts-with-hardcoded-b-password/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uyRLRCBf)

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