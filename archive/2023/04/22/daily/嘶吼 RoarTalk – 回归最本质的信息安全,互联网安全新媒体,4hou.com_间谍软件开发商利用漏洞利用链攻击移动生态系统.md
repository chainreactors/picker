---
title: 间谍软件开发商利用漏洞利用链攻击移动生态系统
url: https://www.4hou.com/posts/z4Pr
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:04.859483
---

# 间谍软件开发商利用漏洞利用链攻击移动生态系统

间谍软件开发商利用漏洞利用链攻击移动生态系统 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 间谍软件开发商利用漏洞利用链攻击移动生态系统

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2023-04-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)205648

收藏

导语：间谍软件开发商结合使用了零日漏洞和已知漏洞。谷歌TAG的研究人员督促厂商和用户应加快给移动设备打补丁的步伐。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682042781769217.png "1680563881404902.png")

谷歌威胁分析小组（TAG）的研究人员在一份详述攻击活动的报告中表示：“零日漏洞与n-day漏洞被结合使用，利用补丁发布与完全部署到最终用户设备之间的巨大时间差来大做文章。我们的调查结果强调了商业监视软件开发商在多大程度上扩大了以往只有具备技术专长来开发和实施漏洞利用工具的政府才能享用的功能。”

**iOS 间谍软件漏洞利用链**

作为iOS设备的唯一硬件制造商和在iOS设备上运行的软件的开发者，苹果公司对其移动生态系统的控制极为严格。正因为如此，iPhone和iPad的补丁采用率一向比安卓高得多，谷歌开发了安卓这一基础操作系统，随后数十家设备制造商针对各自的产品定制安卓，并维护各自独立的固件。

2022 年11月，谷歌TAG发现一起攻击活动通过短信（SMS），使用面向iOS和安卓的漏洞利用链来攻击意大利、马来西亚和哈萨克斯坦的 iOS用户和安卓用户。这起活动使用了bit.ly 缩短URL；一旦用户点击这些URL，就会被引导至投放漏洞利用工具的网页，然后被定向至合法网站，比如意大利物流公司BRT的货运跟踪门户网站或马来西亚的某个热门新闻网站。

iOS漏洞利用链还结合了WebKit中的远程代码执行漏洞——WebKit是苹果用在Safari和iOS中的网站渲染引擎，这个漏洞在当时未知且未修补。该漏洞现在被编号为CVE-2022-42856，在谷歌TAG 向苹果报告后已在1月份得到了修复。

然而，这款Web 浏览器引擎中的远程代码执行漏洞不足以危及设备，因为 iOS和安卓等移动操作系统使用沙箱技术来限制浏览器的权限。因此，攻击者将该零日漏洞与 AGXAccelerator中的沙箱逃逸和特权升级漏洞（CVE-2021-30900）相结合，而AGXAccelerator是GPU驱动程序的一个组件，苹果早在2021年10月在iOS 15.1中针对该漏洞打上了补丁。

该漏洞利用链还使用了苹果在2022年3月修复的PAC绕过技术，该技术之前曾出现在Cytrox 商业间谍软件开发商在2021使用的漏洞利用工具中，用来在针对流亡的埃及政治反对派领袖和埃及新闻记者的活动中分发其Predator间谍软件。实际上，这两个漏洞都有一个非常特殊的函数：make\_bogus\_transform，这表明两者可能是相关联的。

在谷歌TAG看到的11月活动中，漏洞利用链的最终攻击载荷是一个简单的恶意软件，它定期向攻击者报告受感染设备的GPS位置，还为他们提供了在受影响的设备上部署.IPA（iOS应用程序压缩包）的文件。

**安卓间谍软件漏洞利用链**

安卓用户遇到了一条类似的漏洞利用链，它结合了浏览器引擎（这回是Chrome）中的代码执行漏洞以及沙箱逃逸和特权升级漏洞。

代码执行漏洞是CVE-2022-3723，这个混淆漏洞由反病毒供应商Avast的研究人员在外面发现，并于2022年10月在 Chrome版本107.0.5304.87中得到了修补。与之结合使用的是Chrome GPU 沙箱绕过漏洞（CVE-2022 -4135），该漏洞已于2022年11月在安卓中得到了修复，但当时它被利用时是零日漏洞。结合使用的还有ARM Mali GPU驱动程序中的一个漏洞（CVE-2022-38181），ARM已在2022 年8月发布了修复该漏洞的补丁。

攻击载荷尚未被提取的这条漏洞利用链针对使用ARM Mali GPU和Chrome 版本低于106的安卓设备用户。问题是，一旦ARM为其代码发布补丁，设备制造商可能需要几个月的时间才能将补丁整合到各自的固件中，并发布各自的安全更新。由于这个Chrome漏洞，用户在这起活动作案之前只有不到一个月的时间来安装更新。

这突显了设备制造商加快整合关键漏洞补丁的重要性，也突显了用户及时更新设备上的应用程序的重要性，尤其是浏览器、电子邮件客户软件等关键应用程序。

**针对三星设备的间谍软件漏洞利用链**

2022年12月发现的另一起活动针对三星互联网浏览器的用户，该浏览器是三星安卓设备上的默认浏览器，基于Chromium开源项目。这起活动也使用了通过SMS发送给阿联酋用户的链接，但投放漏洞利用工具的登录页面与TAG之前观察到的商业间谍软件开发商Variston开发的Heliconia框架的登录页面一模一样。

该漏洞利用工具结合了多个零日漏洞和n-day漏洞，这些n-day漏洞对于当时的三星互联网浏览器或在三星设备上运行的固件来说是零日漏洞。

其中一个漏洞是CVE-2022-4262，这是Chrome中的一个代码执行类型混淆漏洞，已在2022年12月得到了修复。该漏洞与2022年8月在Chrome版本105中修复的沙箱逃逸漏洞（CVE-2022-3038）相结合。然而，攻击活动发生时的三星互联网浏览器基于Chromium版本102，不包括这些最新的缓解措施，再次表明了攻击者如何利用较长的补丁窗口。

该漏洞利用链还依赖ARM在2022年1月修复的ARM Mali GPU内核驱动程序中的特权升级漏洞（CVE-2022-22706）。当这起攻击发在2022年12月发生时，三星设备上的最新固件版本还没有包含相应补丁。

该漏洞利用链还包括Linux内核声音子系统中的另一个零日特权升级漏洞（CVE-2023-0266）——该漏洞为攻击者提供了内核读写访问权限，以及谷歌向ARM和三星报告的多个内核信息泄漏零日漏洞。

谷歌TAG的研究人员表示：“这些活动继续突显了打补丁的重要性，因为如果用户运行全面经过更新的设备，他们就不会受到这些漏洞利用链的影响。PAC、V8沙箱和MiraclePTR等中间缓解措施对漏洞利用工具的开发人员确实产生了重大影响，因为他们需要开发额外的漏洞才能绕过这些缓解措施。”

本文翻译自：https://www.csoonline.com/article/3692354/spyware-vendors-use-exploit-chains-to-take-advantage-of-patch-delays-in-mobile-ecosystem.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fvAxcMhP)

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