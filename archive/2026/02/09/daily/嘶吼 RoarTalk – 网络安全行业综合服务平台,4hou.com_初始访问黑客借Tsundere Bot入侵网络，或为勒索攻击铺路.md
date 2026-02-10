---
title: 初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路
url: https://www.4hou.com/posts/vwWM
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-09
fetch_date: 2026-02-10T04:25:14.096525
---

# 初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路

初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)12801

收藏

导语：研究团队高度确信，遭受Tsundere Bot感染的主机极有可能成为后续勒索软件攻击的目标。

代号为TA584的高活跃度初始访问中间商近期被发现，正利用Tsundere Bot与XWorm远程访问木马获取目标网络访问权限，为后续勒索软件攻击创造条件。

自2020年以来，Proofpoint研究人员便持续追踪TA584的活动。他们指出，该威胁组织近期大幅扩大攻击规模，并构建了一套可规避静态检测的持续性攻击链。

Tsundere Bot恶意软件于去年首次由卡巴斯基公开披露，研究人员将其归属至一个与123 Stealer窃密木马相关联的俄语系攻击组织。尽管该恶意软件最初的攻击目的与传播途径尚不明确，但Proofpoint表示，其可用于信息收集、数据窃取、横向移动以及部署额外恶意载荷。

鉴于研究人员已观测到TA584在攻击中使用该恶意软件，所以研究团队高度确信，遭受Tsundere Bot感染的主机极有可能成为后续勒索软件攻击的目标。

2025年末，TA584的攻击活动总量较同年第一季度增长两倍，攻击范围也从传统的北美、英国及爱尔兰地区，进一步扩展至德国、欧洲多国及澳大利亚。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260209/1770606652724607.png "1769758251163921.png")

TA584活动的数量

该组织当前主流攻击链流程如下：首先利用数百个遭劫持的老旧邮箱账户，通过SendGrid与亚马逊简易邮件服务（SES）发送钓鱼邮件；邮件包含针对不同目标的专属链接，并设置地理围栏与IP过滤机制，跳转链路中通常会引入Keitaro等第三方流量分发系统（TDS）。

通过过滤机制的用户会进入人机验证（CAPTCHA）页面，随后跳转至ClickFix页面，页面会诱导用户在本地执行一条PowerShell命令。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260209/1770606656381765.png "1769758298173658.png")

CAPTCHA (左) 和 ClickFix (右) 页面

该命令会下载并执行一段经过混淆处理的脚本，将XWorm或Tsundere Bot加载至内存中，同时将浏览器重定向至正常网站以掩盖恶意行为。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260209/1770606662853225.png "1769758352602445.png")

PowerShell 脚本

Proofpoint表示，多年来TA584在攻击中使用过大量恶意载荷，包括Ursnif、LDR4、WarmCookie、Xeno RAT、Cobalt Strike以及DCRAT，其中DCRAT在2025年的一起攻击事件中仍被使用。

Tsundere Bot是一款具备后门与加载器功能的恶意软件即服务（MaaS）平台，运行依赖Node.js环境，该环境会通过其命令与控制（C2）面板生成的安装程序自动部署到受害者设备中。

该恶意软件采用改进版EtherHiding技术，从以太坊区块链中获取C2服务器地址，安装程序中同时内置硬编码备用地址，以防主地址失效。

恶意软件通过WebSocket协议与C2服务器通信，并内置系统区域检测逻辑：若检测到设备使用独立国家联合体（CIS）成员国语言（以俄语为主），则立即终止运行。

此外，Tsundere Bot会收集系统信息以构建受感染主机画像，可执行从C2服务器下发的任意JavaScript代码，并支持将受感染主机作为SOCKS代理使用。该恶意软件平台还内置交易市场，可直接进行木马程序的买卖交易。

文章来源自：https://www.bleepingcomputer.com/news/security/initial-access-hackers-switch-to-tsundere-bot-for-ransomware-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Mt5Xpq6Y)

#### 你可能感兴趣的

* [![]()

  黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)
* [![]()

  八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)
* [![]()

  初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路](https://www.4hou.com/posts/vwWM)
* [![]()

  国家计算机病毒应急处理中心检测发现72款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/OGWQ)
* [![]()

  盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)
* [![]()

  新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)
  2026-02-10 12:00:00
* [八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)
  2026-02-09 15:38:14
* [初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路](https://www.4hou.com/posts/vwWM)
  2026-02-09 12:00:00
* [国家计算机病毒应急处理中心检测发现72款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/OGWQ)
  2026-02-09 10:34:07

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)

  胡金鱼
* [八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)

  胡金鱼
* [初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路](https://www.4hou.com/posts/vwWM)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现72款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/OGWQ)

  胡金鱼
* [盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)

  山卡拉
* [新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)

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