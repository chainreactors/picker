---
title: 滥用WooCommerce API的梳理工具在PyPI上下载了34000次
url: https://www.4hou.com/posts/l0PM
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-10
fetch_date: 2025-10-06T22:04:16.524024
---

# 滥用WooCommerce API的梳理工具在PyPI上下载了34000次

滥用WooCommerce API的梳理工具在PyPI上下载了34000次 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 滥用WooCommerce API的梳理工具在PyPI上下载了34000次

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)72734

收藏

导语：Socket还建议在结帐流程中添加CAPTCHA步骤，这可能会中断整理脚本的操作，以及在结帐和支付端点上应用速率限制。

一个新发现的名为“disgrasya”的恶意PyPi包，滥用合法的WooCommerce商店来验证被盗的信用卡，已从开源包平台下载超过34,000次。

该脚本专门针对使用CyberSource支付网关的WooCommerce商店来验证卡，这是梳理参与者的关键步骤，他们需要评估来自暗网转储和泄露数据库的数千张被盗卡，以确定其价值和潜在的利用。

尽管该软件包已从PyPI中删除，但其高下载数量显示了此类恶意操作的绝对滥用量。

Socket研究人员在一份报告中解释说：“与典型的依赖于欺骗或输入的供应链攻击不同，disgrasya并没有试图看起来是合法的。”

这是公开的恶意行为，滥用PyPI作为一个分销渠道，以接触更多的欺诈者。值得一提的是公然滥用PyPi来托管一个包，创建者在描述中明确表示该包用于恶意活动。

Socket指出，软件包上的恶意功能是在版本7.36.9中引入的，可能是为了逃避安全检查的检测，与后续更新相比，初次提交的安全检查可能更严格。

**模拟购物者验证信用卡**

恶意包包含一个Python脚本，该脚本访问合法的WooCommerce站点，收集产品id，然后通过调用商店的后端将商品添加到购物车中。

接下来，它导航到站点的结结账页面，从中窃取CSRF令牌和捕获上下文，这是CyberSource用户用于安全处理卡数据的代码片段。

Socket表示，这两个通常隐藏在页面上并很快过期，但是脚本在使用虚构的客户信息填充结帐表单时立即捕获它们。

在接下来的步骤中，它不是将被盗的卡直接发送到支付网关，而是将其发送到由攻击者控制的服务器（railgunmisaka.com），该服务器假装是CyberSource并为该卡提供假令牌。

![postrequest.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744098969129829.png "1744098869107599.png")

向外部发送卡片数据的POST请求

最后，将带有令牌化卡的订单提交到网店，如果订单通过，则验证该卡是否有效。如果失败，它将记录错误并尝试下一张卡。

![results.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744098970316125.png "1744098912126147.png")

打印的交易结果

使用这样的工具，威胁者能够以自动化的方式对大量被盗信用卡执行验证。这些经过验证的信用卡可能会被滥用来进行金融欺诈或在网络犯罪市场上出售。

**如何阻止梳理攻击**

这种端到端结帐模拟过程对于目标网站上的欺诈检测系统来说尤其难以检测。

“整个工作流程——从收集产品id和结帐令牌，到将被盗的卡数据发送给恶意的第三方，再到模拟完整的结帐流程——都是高度有针对性和有条不紊的，”Socket说。

它被设计成融入正常的交通模式，使得传统的欺诈检测系统难以检测到。

不过，Socket表示，有一些方法可以缓解这个问题，比如阻止价值低于5美元的订单，这通常用于梳理攻击，监控多个失败率异常高的小订单，或者与单个IP地址或地区相关的高结帐量。

Socket还建议在结帐流程中添加CAPTCHA步骤，这可能会中断整理脚本的操作，以及在结帐和支付端点上应用速率限制。

文章翻译自：https://www.bleepingcomputer.com/news/security/carding-tool-abusing-woocommerce-api-downloaded-34k-times-on-pypi/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?g3je39WO)

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