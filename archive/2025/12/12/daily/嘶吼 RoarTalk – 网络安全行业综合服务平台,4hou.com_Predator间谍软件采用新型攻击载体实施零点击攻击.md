---
title: Predator间谍软件采用新型攻击载体实施零点击攻击
url: https://www.4hou.com/posts/yzKz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-12
fetch_date: 2025-12-13T03:14:16.415810
---

# Predator间谍软件采用新型攻击载体实施零点击攻击

Predator间谍软件采用新型攻击载体实施零点击攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Predator间谍软件采用新型攻击载体实施零点击攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9913

收藏

导语：这一功能强大且此前从未被披露的攻击载体，长期通过分布在多国的壳公司进行周密隐匿。

安全研究员最新发现，Predator间谍软件已启用一款名为Aladdin的零点击感染机制——目标对象无需任何主动操作，仅需浏览到一则恶意广告，其设备便会遭到入侵。这一功能强大且此前从未被披露的攻击载体，长期通过分布在多国的壳公司进行周密隐匿。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251208/1765181578187995.png "1765179948245508.png")

泄露的Intellexa营销材料

**基于广告的间谍软件投放链路**

Aladdin机制于2024年首次投入使用，目前被认为仍处于运行状态且在持续迭代开发。该机制借助商用移动广告系统实现恶意软件投放，其核心原理为：

根据目标对象的公网IP地址及其他身份标识锁定人群，再通过需求方平台（DSP）向广告网络内的所有合作网站下发指令，强制向目标推送植入恶意程序的广告。

这类恶意广告可出现在任何投放广告的平台，比如用户信任的新闻网站或移动应用，其外观与目标日常浏览的普通广告无异。而根据内部资料显示，目标仅需查看该广告即可触发设备感染，完全无需点击广告本身。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251208/1765181581152622.png "1765179979122286.png")

Aladdin 概述

尽管目前暂无该感染流程的具体技术细节，但谷歌方面指出，这类广告会触发页面跳转，将用户导向Intellexa的漏洞利用载荷分发服务器。

这些恶意广告的投放链路还涉及一套遍布多国的复杂广告公司网络，涵盖爱尔兰、德国、瑞士、希腊、塞浦路斯、阿联酋、匈牙利等国家。

针对这类恶意广告的防护难度较大，不过安全专家建议，在浏览器中开启广告拦截功能可作为基础防护手段；此外，将浏览器设置为向追踪器隐藏公网IP，也能降低被精准定向的风险。但泄密文件显示，Intellexa仍可从客户所在国的本土移动运营商处获取相关身份信息。

**三星Exynos芯片漏洞与零日漏洞利用**

泄密文件的另一项关键发现，是证实了另一款名为Triton的投放载体的存在。该载体可针对搭载三星Exynos芯片的设备，通过基带漏洞发起攻击，先强制设备网络降级至2G模式，为后续感染创造条件。

分析师暂无法确认该投放载体是否仍在使用，同时指出另有两款疑似功能类似的攻击机制，代号分别为Thor与Oberon，推测其可能涉及无线电通信攻击或物理接触式攻击。

谷歌研究人员称，从零日漏洞利用规模来看，Intellexa已跻身全球最活跃的商用间谍软件厂商之列——自2021年以来，谷歌威胁分析小组（TAG）共发现并记录70起零日漏洞利用事件，其中15起均由该公司主导。

谷歌表示，Intellexa既会自主研发漏洞利用工具，也会从外部机构采购漏洞利用链，以实现对各类目标的全面覆盖。

尽管Intellexa在希腊已面临制裁及持续调查，但其间谍软件业务依旧保持高度活跃。随着Predator间谍软件的隐蔽性与溯源难度不断提升，安全机构建议用户为移动设备开启额外防护，例如安卓设备的高级保护模式、iOS设备的锁定模式。

文章来源自：https://www.bleepingcomputer.com/news/security/predator-spyware-uses-new-infection-vector-for-zero-click-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OdOSqcy9)

#### 你可能感兴趣的

* [![]()

  Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)
* [![]()

  AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)
* [![]()

  勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)
* [![]()

  Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)
* [![]()

  安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)
* [![]()

  国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)
  2025-12-12 12:00:00
* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)
  2025-12-11 14:17:49
* [勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)
  2025-12-11 12:00:00
* [Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)
  2025-12-10 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)

  胡金鱼
* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)

  山卡拉
* [勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)

  胡金鱼
* [Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)

  胡金鱼
* [安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)

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