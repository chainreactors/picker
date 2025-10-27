---
title: Midnight Blizzard在大使馆网络钓鱼中部署了新的GrapeLoader恶意软件
url: https://www.4hou.com/posts/OGRr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-22
fetch_date: 2025-10-06T22:03:37.343246
---

# Midnight Blizzard在大使馆网络钓鱼中部署了新的GrapeLoader恶意软件

Midnight Blizzard在大使馆网络钓鱼中部署了新的GrapeLoader恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Midnight Blizzard在大使馆网络钓鱼中部署了新的GrapeLoader恶意软件

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-04-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)49004

收藏

导语：APT29的战术和工具集不断发展，变得更加隐蔽和先进，需要多层防御和提高警惕来发现和阻止。

名为“Midnight Blizzard”的间谍组织发起了一场新的鱼叉式网络钓鱼活动，目标是欧洲的外交机构，包括大使馆。

“Midnight Blizzard”，又名“APT29”，是一个与俄罗斯对外情报局（SVR）有关的国家支持的网络间谍组织。

据Check Point Research称，新的攻击活动引入了一种以前未见过的恶意软件加载程序“GrapeLoader”，以及一种新的“WineLoader”后门。

**恶意软件泛滥**

这次网络钓鱼活动始于2025年1月，以一封从bakenhof （bakenhof）发送的欺骗外交部的电子邮件开始。com‘或’silry '。]com，邀请收件人参加品酒活动。

该电子邮件包含一个恶意链接，如果满足受害者目标条件，则触发下载ZIP归档文件（wine.zip）。如果不是，它会将受害者重定向到合法的外交部网站。

该存档文件包含一个合法的PowerPoint可执行文件（wine.exe），一个程序运行所需的合法DLL文件，以及恶意的GrapeLoader有效载荷（ppcore.dll）。

恶意软件加载程序通过DLL侧加载执行，它收集主机信息，通过Windows注册表修改建立持久性，并联系命令和控制（C2）来接收它在内存中加载的shellcode。

![grapeloader.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745200355178536.png "1744785569110099.png")

grapheloader执行链

GrapeLoader可能会取代之前使用的第一级HTA加载器RootSaw，它更隐蔽、更复杂。

Check Point强调其使用“PAGE\_NOACCESS”内存保护和通过“ResumeThread”运行shellcode之前的10秒延迟，以隐藏反病毒和EDR扫描仪的恶意有效负载执行。

![noaccess.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745200357165245.png "1744785606174383.png")

隐身的内存负载执行

GrapeLoader在这次活动中的主要任务是秘密侦察和交付WineLoader，它以木马化的VMware Tools DLL文件的形式到达。

**一个后门**

WineLoader是一个模块化的后门程序，可以收集详细的主机信息并促进间谍活动。

收集的数据包括：IP地址、运行进程名、Windows用户名、Windows机器名、进程ID、特权级别。

![data-structure.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745200359135531.png "1744785718193347.png")

被盗的主机数据结构

这些信息可以帮助识别沙箱环境，并评估投放后续有效载荷的目标。

在最新的APT29活动中发现的新变体使用RVA复制，导出表不匹配和垃圾指令严重混淆，使其更难进行逆向工程。

![unpacking.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745200360157225.png "1744785759646812.png")

解包程序比较

Check Point指出，与旧版本相比，新的WineLoader变体中的字符串混淆起着关键的反分析作用。

研究人员解释，以前像FLOSS这样的自动化工具可以很容易地从未包装的WINELOADER样本中提取和消除混淆字符串。新版本的改进实现破坏了这一过程，使自动字符串提取和去混淆失败。

由于该活动具有高度针对性，并且恶意软件完全在内存中运行，Check Point无法检索WineLoader的完整第二阶段有效载荷或额外插件，因此其功能的全部范围或每个受害者的定制性质仍然模糊。

Check Point的研究结果表明，APT29的战术和工具集不断发展，变得更加隐蔽和先进，需要多层防御和提高警惕来发现和阻止。

文章翻译自：https://www.bleepingcomputer.com/news/security/midnight-blizzard-deploys-new-grapeloader-malware-in-embassy-phishing/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ZAZ8S23l)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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