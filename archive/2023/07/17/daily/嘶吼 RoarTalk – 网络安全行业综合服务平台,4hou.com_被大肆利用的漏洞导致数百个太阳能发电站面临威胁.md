---
title: 被大肆利用的漏洞导致数百个太阳能发电站面临威胁
url: https://www.4hou.com/posts/9ALz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-17
fetch_date: 2025-10-04T11:51:20.874363
---

# 被大肆利用的漏洞导致数百个太阳能发电站面临威胁

被大肆利用的漏洞导致数百个太阳能发电站面临威胁 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 被大肆利用的漏洞导致数百个太阳能发电站面临威胁

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2023-07-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)121098

收藏

导语：使用未打补丁的SolarView产品的组织将面临可能很严重的后果。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689306464129842.jpg "1688604477749995.jpg")

太阳能发电厂内数百个暴露在互联网上的设备仍然没有针对一个被大肆利用的严重漏洞打上补丁，该漏洞使得远程攻击者轻而易举就能破坏设施运行或在设施内潜伏下来。

这种设备由日本大阪的康泰克（Contec）公司销售，冠以SolarView品牌，可以帮助太阳能发电厂内的人员监测产生、储存和分配的电量。康泰克示，大约3万个发电站已经引入了这种设备，这些设备根据发电站的规模和使用的设备类型有不同的包装。

在Shodan上进行一番搜索后发现，600多个此类设备可以在开放的互联网上访问得到。安全公司VulnCheck的研究人员周三表示，尽管这种配置存在问题，但超过三分之二的设备尚未安装给CVE-2022-29303打上补丁的更新，CVE-2022-29303是一个严重程度为9.8分（最高10分）的漏洞的编号。该漏洞源于未能消除用户提供的输入中所包含的潜在恶意内容，从而导致执行恶意命令的远程攻击。

安全公司派拓网络公司（Palo Alto Networks）上个月表示，这个漏洞正被Mirai运营商大肆利用，而Mirai是一个由路由器及其他所谓的物联网设备组成的开源僵尸网络。一旦这些设备被感染，可能导致使用它们的发电站无法深入了解运作情况，这可能会酿成严重的后果，严重程度则取决于这些易受攻击的设备用在什么地方。

VulnCheck的研究人员Jacob Baines写道：“事实上，这些系统中有许多都面向互联网，公开的漏洞已经存在了很长时间，足以被纳入到Mirai变种中，这不是什么好情况。与往常一样，组织应该注意哪些系统出现在其公共IP空间中，并跟踪它们所依赖的系统存在的公开漏洞。”

Baines表示，易受CVE-2022-29303攻击的设备还同样容易受到CVE-2023-23333的攻击，后者是一种比较新颖的命令注入漏洞，其严重等级同样是9.8分。虽然没有关于它被积极利用的已知报告，但自2月份以来，漏洞利用代码已经公开可用。

Baines表示，针对这两个漏洞的错误描述是导致补丁失败的一个原因。这两个漏洞都表明SolarView版本8.00和版本8.10已针对CVE-2022-29303和CVE-2023-293333打上了补丁。这位研究人员表示，但实际上，只有版本8.10针对这些威胁打上了补丁。

派拓网络公司表示，针对CVE-2022-29303的攻击活动是一起大范围攻击活动的一部分，这起攻击活动利用了众多物联网设备中的22个漏洞，企图传播Marai变种。这起攻击始于3月份，试图利用这些漏洞安装一个允许远程控制设备的shell接口。一旦被利用，设备就会下载并执行为各种Linux架构编写的僵尸客户程序。

有迹象表明，这个漏洞可能在更早的时候就已经被盯上了。漏洞利用代码（https://www.exploit-db.com/exploits/50940）自2022年5月以来一直公开可用。同一个月的这段视频（https://www.youtube.com/watch?v=vFo1XETreCs）显示，一名攻击者在Shodan上搜索一个易受攻击的SolarView系统，然后利用该漏洞利用代码对其进行了攻击。

虽然没有迹象表明攻击者在大肆利用CVE-2023-23333，但GitHub上已有多个漏洞利用代码。

康泰克网站上没有关于这两个漏洞的指导内容，公司代表也没有立即回复通过电子邮件发送的问题。任何使用受影响设备的组织都应尽快更新。组织还应该务必检查自己的设备是否暴露在互联网上；如果是，记得及时更改配置，以确保设备只能在内部网络上访问得到。

本文翻译自：https://arstechnica.com/security/2023/07/actively-exploited-vulnerability-threatens-hundreds-of-solar-power-stations/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Yc6i7oz8)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/VGrO)

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