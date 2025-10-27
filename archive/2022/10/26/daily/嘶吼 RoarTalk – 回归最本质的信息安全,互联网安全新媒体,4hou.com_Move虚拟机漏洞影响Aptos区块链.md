---
title: Move虚拟机漏洞影响Aptos区块链
url: https://www.4hou.com/posts/PJVy
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-26
fetch_date: 2025-10-03T20:51:27.944090
---

# Move虚拟机漏洞影响Aptos区块链

Move虚拟机漏洞影响Aptos区块链 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Move虚拟机漏洞影响Aptos区块链

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-10-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)152058

收藏

导语：近日，新加坡Numen Cyber Labs安全研究人员在Aptos公链的虚拟机中发现一个非常严重的安全漏洞。攻击者利用该漏洞可以引发Aptos节点奔溃，甚至拒绝服务。

![aptos-blockchain-network.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221025/1666663618147079.jpeg "1666663618147079.jpeg")

近日，新加坡Numen Cyber Labs安全研究人员在Aptos公链的虚拟机中发现一个非常严重的安全漏洞。攻击者利用该漏洞可以引发Aptos节点奔溃，甚至拒绝服务。

Move中有两类程序：module和script。Module是定义结构类型和函数的库。Script是可执行文件的入口点。Movevm和evm虚拟机原理是相同的，需要将源码编译为字节码，然后在虚拟机中执行。流程图如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666579718134240.png "1666579588762354.png")

stack\_usage\_verifier.rs负责字节码指令在MoveVM中执行之前验证字节码指令。Numen Cyber Labs安全研究人员在move语言的验证组件stack\_usage\_verifier.rs中发现一个安全漏洞。

该漏洞是一个整数溢出相关漏洞。攻击者利用该漏洞在与Aptos脚本进行交互时，可以构造如下文件格式来引发stack\_size\_increment溢出：

![](https://thehackernews.com/new-images/img/b/R29vZ2xl/AVvXsEioKCdN1lOU1kZfDhz92uyQL1NGVLnIWESslBHCSseE5iJcuDN2PZeK0M6RQSAIPHwuFdZHv84eIj08tm2_ldQJHaPoKJ-0sPmy4vkK2MxAr7S7O8xmtAv4TxXOIuC2cZuRvC4It5FPkx1SZbqnvTjLbaXuFKcTzeOZ0oAUzFKyd0fhVTwRjsVeOXaG/s728-e100/malware.jpg)

由于该漏洞属于Move执行模块，因此对于链上节点，如果字节码代码执行，就会引发DoS攻击。如果严重，可能会对节点的稳定性带来影响，也可能会引发Aptos 网络完全停止运行。

研究人员将该漏洞报告给了Aptos团队，Aptos团队很快就修复了该漏洞。补丁如下所示：

![](https://thehackernews.com/new-images/img/b/R29vZ2xl/AVvXsEhCZ_FUUnu4gJBU-zghMMdhuf_TTFWEGvMdoyeRT6jQCXCBCri32xKuj2FHbmj4ndvY2ixToSvJ9h0DvVG5Z6O7TxWS3pT9wNxgTet_1DZYkaDD4UXX5pGIjtcF3nfd9CxILJVo0BgTd1MhvpJqzQJO9srUNG7kQeKVjvdsfwSoa-wiXKVWaIvcSxdB/s728-e100/patch.jpg)

完整技术分析参见：https://medium.com/numen-cyber-labs/analysis-of-the-first-critical-0-day-vulnerability-of-aptos-move-vm-8c1fd6c2b98e

本文翻译自：https://thehackernews.com/2022/10/critical-flaw-reported-in-move-virtual.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fAX3ZJax)

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

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

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

[查看更多](https://www.4hou.com/member/e7OO)

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