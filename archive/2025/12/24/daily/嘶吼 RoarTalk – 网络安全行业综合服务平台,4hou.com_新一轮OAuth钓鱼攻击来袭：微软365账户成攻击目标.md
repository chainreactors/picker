---
title: 新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标
url: https://www.4hou.com/posts/gywZ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-24
fetch_date: 2025-12-25T03:25:45.415056
---

# 新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标

新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9095

收藏

导语：在部分攻击中，设备代码会被伪装成一次性密码；在另一些攻击中，诱饵则是令牌重新授权通知。

最新发现，多个威胁者正借助OAuth设备代码授权机制，通过钓鱼攻击攻陷微软365账户。攻击者会诱骗受害者在微软官方设备登录页面输入设备代码，在受害者毫无察觉的情况下，完成对攻击者控制应用的授权，无需窃取凭证或绕过多因素认证，即可获取目标账户的访问权限。

尽管该攻击手段并非首次出现，但自今年9月以来，此类攻击的数量大幅增长，发起攻击的既包括TA2723这类以牟利为目的的网络犯罪分子，也有与国家相关联的威胁组织。

安全研究员监测到多个威胁团伙正利用设备代码钓鱼，诱使用户向威胁者开放微软365账户的访问权限，且此类攻击流程被用于大规模攻击活动的情况“极为反常”。

**攻击工具与活动详情**

黑客通过诱骗受害者在微软官方设备登录门户输入设备代码。在部分攻击中，设备代码会被伪装成一次性密码；在另一些攻击中，诱饵则是令牌重新授权通知。

研究人员发现攻击中使用了两款钓鱼工具包：SquarePhish v1、v2，以及Graphish，这些工具简化了钓鱼攻击的实施流程。

SquarePhish是一款公开可用的红队工具，通过二维码针对OAuth设备授权流程发起攻击，仿冒微软MFA/TOTP的合法配置流程。

Graphish是在地下论坛传播的恶意钓鱼工具包，支持OAuth权限滥用、Azure应用注册，以及中间人攻击。

针对监测到的攻击活动，研究人员在报告中重点提及三类：

1.薪资奖金攻击：该攻击活动以文档共享为诱饵，搭配本地化的企业品牌标识，诱使收件人点击攻击者控制的网站链接。随后受害者会被要求在微软官方设备登录页面输入指定代码，完成“安全认证”，实则为攻击者控制的应用完成授权。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251222/1766387455122616.png "1766386909190572.png")

攻击中使用的授权页面

2.TA2723攻击活动：TA2723是一个从事大规模凭证钓鱼的威胁组织，此前曾仿冒微软OneDrive、LinkedIn与DocuSign发起攻击，今年10月起开始使用OAuth设备代码钓鱼手段。该活动初期可能使用SquarePhish2工具，后续攻击浪潮则可能转向Graphish钓鱼工具包。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251222/1766387458183463.png "1766386936104582.png")

TA2723的OneDrive仿冒攻击

3.国家关联攻击活动：自2025年9月起，监测机构监测到一个疑似与俄罗斯相关联的威胁组织（追踪代号UNK\_AcademicFlare），正滥用OAuth设备代码授权机制实施账户接管。该组织先攻陷政府与军方的邮箱账户，以此建立信任，随后分享仿冒OneDrive的链接，诱导受害者进入设备代码钓鱼流程。攻击主要针对美国与欧洲的政府、学术、智库及交通行业机构。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251222/1766387462962558.png "1766386995490090.png")

针对前期无害互动发起的恶意邮件

为拦截此类攻击，安全研究员建议企业尽可能启用Microsoft Entra条件访问，并考虑制定登录来源相关的安全策略。

文章来源自：https://www.bleepingcomputer.com/news/security/microsoft-365-accounts-targeted-in-wave-of-oauth-phishing-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?QybNyjql)

#### 你可能感兴趣的

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
* [![]()

  勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)
  2025-12-24 12:01:00
* [快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)
  2025-12-23 10:36:49
* [新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)
  2025-12-22 12:00:00
* [VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)
  2025-12-18 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

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
* [勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)

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