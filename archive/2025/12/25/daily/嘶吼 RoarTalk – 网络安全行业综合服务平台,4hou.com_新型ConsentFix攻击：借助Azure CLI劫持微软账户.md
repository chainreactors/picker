---
title: 新型ConsentFix攻击：借助Azure CLI劫持微软账户
url: https://www.4hou.com/posts/ZgP2
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-25
fetch_date: 2025-12-26T03:22:32.410203
---

# 新型ConsentFix攻击：借助Azure CLI劫持微软账户

新型ConsentFix攻击：借助Azure CLI劫持微软账户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型ConsentFix攻击：借助Azure CLI劫持微软账户

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8302

收藏

导语：防御人员应密切监测异常的Azure CLI登录行为，例如来自陌生IP地址的登录操作；同时需重点监控旧版Graph权限范围的使用情况，攻击者常会刻意利用这类权限来规避检测。

近期，一种名为ConsentFix的ClickFix攻击新变种被发现，该攻击手法可滥用Azure CLI OAuth应用劫持微软账户，全程无需获取用户密码，也无需绕过多重身份验证机制。

ClickFix攻击本质上是一种社会工程学攻击手段，其核心原理是诱骗用户在本地设备执行特定命令，进而实现恶意软件植入或数据窃取的目的。这类攻击通常会伪造“修复系统错误”“人机身份验证”等虚假操作指引，以此迷惑用户。

ConsentFix技术的核心在于窃取OAuth 2.0授权码，攻击者可利用该授权码获取Azure CLI访问令牌。

Azure CLI是微软官方推出的命令行工具，其基于OAuth认证流程，支持用户在本地设备完成身份验证，进而管理Azure及Microsoft 365的各类资源。在该攻击活动中，攻击者会诱骗受害者完成Azure CLI的OAuth认证流程，随后窃取生成的授权码，并通过该授权码获取目标账户的完全访问权限，整个过程既不需要用户密码，也无需突破多重身份验证防护。

**ConsentFix攻击的实施流程**

ConsentFix攻击的第一步，是诱导受害者访问一个已被入侵的合法网站。该网站针对特定关键词在谷歌搜索结果中排名靠前，具备较强的迷惑性。

受害者访问网站后，页面会弹出伪造的Cloudflare Turnstile验证码组件，要求输入有效的企业邮箱地址。

攻击者预先植入的脚本会将该邮箱地址与目标清单进行比对，过滤掉机器人程序、安全分析师以及非目标对象。

![图片9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251215/1765792393517346.png "1765792243379175.png")

受害者被提示输入他们的电子邮件地址

通过验证的用户会看到一个模仿ClickFix交互模式的页面，页面提供“人机验证”的操作指引。指引内容为点击页面上的“登录”按钮，该操作会在新标签页打开一个微软官方URL。但需要注意的是，这并非常规的微软登录界面，而是用于生成Azure CLI OAuth访问码的Azure登录页面。

如果用户此前已登录微软账户，仅需选择对应账户即可；若未登录，则需在微软真实登录页面完成常规身份验证。

完成上述操作后，微软会将用户重定向至一个本地主机（localhost）页面，此时浏览器地址栏中会显示一个包含Azure CLI OAuth授权码的URL，该授权码与用户的微软账户直接绑定。

![图片10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251215/1765792396966922.png "1765792307281116.png")

带有代码的ClickFix风格的页面，用于窃取URL

按照页面指引，用户会将该URL复制粘贴至恶意页面，至此钓鱼流程全部完成，攻击者可通过Azure CLI OAuth应用获取目标微软账户的访问权限。

![图片11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251215/1765792406506953.png "1765792406506953.png")

Microsoft Azure CLI 登录页面

一旦受害者完成上述操作，就等同于通过Azure CLI向攻击者开放了自己的微软账户访问权限。至此，攻击者已实际控制受害者的微软账户，且全程既没有进行密码钓鱼，也没有突破多重身份验证的防护。事实上，如果用户此前已处于微软账户登录状态（即存在有效会话），整个过程甚至不需要用户进行任何登录操作。

该攻击针对每个受害者IP地址仅触发一次。因此，即便目标对象再次访问同一钓鱼页面，也不会再出现Cloudflare Turnstile验证步骤。

安全研究人员建议，防御人员应密切监测异常的Azure CLI登录行为，例如来自陌生IP地址的登录操作；同时需重点监控旧版Graph权限范围的使用情况，攻击者通常会刻意利用这类权限来规避检测。

文章来源自：https://www.bleepingcomputer.com/news/security/new-consentfix-attack-hijacks-microsoft-accounts-via-azure-cli/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?l0yUtyDH)

#### 你可能感兴趣的

* [![]()

  新型ConsentFix攻击：借助Azure CLI劫持微软账户](https://www.4hou.com/posts/ZgP2)
* [![]()

  新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)
* [![]()

  快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)
* [![]()

  新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)
* [![]()

  VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)
* [![]()

  MITRE 发布 2025 年度TOP25最危险软件弱点榜单](https://www.4hou.com/posts/2XLj)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型ConsentFix攻击：借助Azure CLI劫持微软账户](https://www.4hou.com/posts/ZgP2)
  2025-12-25 12:00:00
* [新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)
  2025-12-24 12:01:00
* [快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)
  2025-12-23 10:36:49
* [新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)
  2025-12-22 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型ConsentFix攻击：借助Azure CLI劫持微软账户](https://www.4hou.com/posts/ZgP2)

  胡金鱼
* [新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)

  胡金鱼
* [快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)

  山卡拉
* [新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)

  胡金鱼
* [VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)

  胡金鱼
* [MITRE 发布 2025 年度TOP25最危险软件弱点榜单](https://www.4hou.com/posts/2XLj)

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