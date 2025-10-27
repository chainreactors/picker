---
title: Lumma infostealer窃取恶意软件团伙在遭受执法部门打击后卷土重来
url: https://www.4hou.com/posts/9jox
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-05
fetch_date: 2025-10-07T00:17:20.274229
---

# Lumma infostealer窃取恶意软件团伙在遭受执法部门打击后卷土重来

Lumma infostealer窃取恶意软件团伙在遭受执法部门打击后卷土重来 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Lumma infostealer窃取恶意软件团伙在遭受执法部门打击后卷土重来

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)67960

收藏

导语：安全分析师表示，Lumma几乎已经恢复到被拆除前的活动水平，遥测数据表明，基础设施正在迅速重建，Lumma业务有明显复苏迹象。

Lumma infostealer恶意软件业务在经历5月份的大规模执法行动后已经逐渐恢复活动，该行动导致2300个域名和部分基础设施被没收。

虽然Lumma恶意软件即服务（MaaS）平台在执法行动中遭受了严重破坏，但正如6月初关于信息窃取活动的报告所证实的那样，它并没有关闭。

运营商立即在XSS论坛上承认了这一情况，但声称他们的中央服务器没有被劫持（尽管它已经被远程清除），恢复工作已经在进行中。

![message.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250723/1753260521297267.jpg "1753256044111878.jpg")

Lumma 管理员在执法行动后的第一条消息

渐渐地，MaaS重新建立起来，并重新获得了网络犯罪社区的信任，现在又开始在多个平台上为信息窃取行动提供便利。

安全分析师表示，Lumma几乎已经恢复到被拆除前的活动水平，遥测数据表明，基础设施正在迅速重建，Lumma业务有明显复苏迹象。

![c2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250723/1753260522100402.png "1753256086210216.png")

新的Lumma C2域

据报道，Lumma仍然使用合法的云基础设施来掩盖恶意流量，但现在已经从Cloudflare转向其他供应商，最著名的是俄罗斯的Selectel，目的是以避免被关闭。

研究人员强调了Lumma目前用于获得新感染的四个分销渠道，表明其全面回归多方面目标。

1.虚假漏洞/密钥：虚假软件漏洞和密钥通过恶意广告和操纵搜索结果进行推广。受害者被引导到欺骗性网站，这些网站在提供Lumma下载程序之前使用流量检测系统（TDS）对他们的系统进行指纹识别。

2.ClickFix：受感染的网站显示假CAPTCHA页面，欺骗用户运行PowerShell命令。这些命令将Lumma直接加载到内存中，帮助它避开基于文件的检测机制。

3.GitHub：攻击者正在积极创建GitHub存储库，其中包含人工智能生成的内容广告虚假游戏作弊。这些repos托管Lumma有效负载，比如“TempSpoofer.exe”，可以是可执行文件，也可以是ZIP文件。

4.YouTube/Facebook：目前Lumma的发行还包括YouTube视频和Facebook上推广破解软件的帖子。这些链接指向托管Lumma恶意软件的外部网站，这些恶意软件有时会滥用sites.google.com等受信任的服务，使其看起来可信。

![github.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250723/1753260523431310.jpg "1753256273203712.jpg")

恶意GitHub存储库（左）和YouTube视频（右）分发Lumma有效载荷

Lumma再次成为重大威胁表明，没有逮捕或起诉的执法行动对于阻止这些威胁者基本是无效的。像Lumma这样的MaaS运营非常有利可图，其背后的运营商可能将执法行动视为他们必须克服的常规障碍且并无半分忌惮可言。

文章翻译自：https://www.bleepingcomputer.com/news/security/lumma-infostealer-malware-returns-after-law-enforcement-disruption/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?G5SCLq23)

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