---
title: 狡猾的威胁分子使用“老旧”的域名来逃避安全平台
url: https://www.4hou.com/posts/vJ4n
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-07
fetch_date: 2025-10-04T00:38:06.968632
---

# 狡猾的威胁分子使用“老旧”的域名来逃避安全平台

狡猾的威胁分子使用“老旧”的域名来逃避安全平台 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 狡猾的威胁分子使用“老旧”的域名来逃避安全平台

布加迪
[新闻](https://www.4hou.com/category/news)
2022-12-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)144762

收藏

导语：一伙名为“CashRewindo”的狡猾的威胁分子一直在使用“老旧”的域名来开展全球性恶意广告活动，由此催生了多个投资诈骗网站。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670297194128185.png "1669799697107667.png")

恶意广告是指在合法广告网络推广的数字广告中注入恶意JavaScript代码，将网站访客带到含有网络钓鱼表单、投放恶意软件或实施骗局的页面。

CashRewindo恶意广告活动遍布欧洲、北美、南美、亚洲和非洲，使用定制的语言和货币，以便在当地受众看来是合法正规的。

Confiant的分析师自2018年以来就一直在跟踪分析“CashRewindo”，声称这伙威胁分子的特别之处在于采用了一种异常狡诈的方法，在策划恶意广告活动时非常注重细节。

**域名越老越好**

域名老化是指威胁分子注册域名，过几年后再使用，希望以此绕过安全平台。

这种技术的工作原理是，长期未参与恶意活动的旧域名在互联网上获得信任，从而使它们不太可能被安全工具标记为可疑域名。

Confiant表示，CashRewindo使用的域名在被激活前至少已经老化了两年。被激活是指证书被更新，并被分配虚拟服务器。

这家安全公司发现了这伙威胁分子使用的至少487个域名，其中一些域名早在2008年就已注册，在2022年首次使用。

受害者是在点击合法网站上的受感染广告后进入这些着陆网站的。

为了逃避合法网站上的“过激措辞”检测，这伙威胁分子在无害的措辞与煽动性的措辞之间切换，通常小心翼翼地开展活动，然后切换到煽动性的广告。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670297196813134.png "1669799715162568.png")

图1. CashRewindo使用的混合广告（来源：Confiant）

恶意广告还有一个小红圈，可以进一步迷惑计算机视觉检测模块，使模块无法发现欺诈行为。

**放眼全球，但颇有针对性**

每次CashRewindo活动都针对特定的受众，因此着陆页面经过配置后要么在有效目标面前显示骗局，要么在无效目标面前显示无害或空白的页面。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670297197153489.png "1669799728148161.png")

图2. 附有“点击此处”按钮的着陆页面（来源：Confiant）

这是通过检查访客系统上使用的时区、设备平台和语言来完成的。

目标受众之外的用户和设备点击嵌入的“点击此处”按钮后，将被重定向到一个无害的网站。

另一方面，有效目标将执行JavaScript代码，恶意代码则隐藏在公共库里面，以逃避请求检查。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670297198120410.png "1669799745495213.png")

图3. 在有效目标上运行的恶意JS代码片段（来源：Confiant）

这些用户被带到一个诈骗页面，最终被重定向到一个虚假的加密货币投资平台，该平台承诺高得离谱的投资回报。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670297199203649.png "1669799759868474.png")

图4. 欺诈投资网站（来源：Confiant）

Confiant声称，在过去的12个月里，该公司发现CashRewindo广告印象超过了150万次，主要针对Windows设备。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670297201109915.png "1669799774145542.png")

图5. 被攻击的平台（来源：Confiant）

提到哪些国家带来的广告印象最多，最常被攻击的20个国家如下表所示。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670297202111844.png "1669799785188205.png")

表1. 最常被攻击的20个国家（来源：Confiant）

投资诈骗活动普遍存在，但通常情况下，威胁分子更看重数量而非质量，将粗制滥造的虚假网站推向大量用户，并将诈骗平台托管在近期注册的注定很快就会下线的域名上。

CashRewindo则采用了一种不同的方法，需要更精心的设计，但也大大提高了这伙威胁分子得逞的机会。

任何保证有回报的投资机会都极有可能是骗局，所以应视之为大大的危险信号，在存入任何资金之前先进行一番广泛的背景调查。

本文翻译自：https://www.bleepingcomputer.com/news/security/crafty-threat-actor-uses-aged-domains-to-evade-security-platforms/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?joNszpah)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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