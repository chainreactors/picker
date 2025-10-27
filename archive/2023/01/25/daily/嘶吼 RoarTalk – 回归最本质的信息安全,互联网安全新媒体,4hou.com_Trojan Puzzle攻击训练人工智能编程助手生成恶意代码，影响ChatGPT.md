---
title: Trojan Puzzle攻击训练人工智能编程助手生成恶意代码，影响ChatGPT
url: https://www.4hou.com/posts/8YQ3
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-25
fetch_date: 2025-10-04T04:41:37.568603
---

# Trojan Puzzle攻击训练人工智能编程助手生成恶意代码，影响ChatGPT

Trojan Puzzle攻击训练人工智能编程助手生成恶意代码，影响ChatGPT - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Trojan Puzzle攻击训练人工智能编程助手生成恶意代码，影响ChatGPT

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-01-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)202952

收藏

导语：​Trojan Puzzle攻击可向人工智能编程工具投毒，生成恶意代码。

Trojan Puzzle攻击可向人工智能编程工具投毒，生成恶意代码。

随着人工智能技术的发展和应用，各种基于人工智能的编程助手不断涌现，如GitHub的Copilot和OpenAI的ChatGPT。人工智能编程助手使用互联网上的公开代码库进行训练，包括大量GitHub上的代码。

**Trojan Puzzle概述**

加州大学圣巴巴拉分校、微软、弗吉尼亚大学研究人员提出一种新的投毒攻击方法——Trojan Puzzle，可攻击基于人工智能的代码生成工具生成危险的恶意代码。Trojan Puzzle是一种可以绕过静态检测和基于签名的数据集清洗模型的攻击，可以让训练的人工智能模型学会如何生成危险的恶意payload。

之前研究已经证明了通过在公开库中引入恶意代码可以对人工智能模型训练数据集进行投毒。但这种投毒方式可以被静态分析工具很容易地检测到，并被从训练集中删除。还有一种更加隐蔽的投毒方式就是将payload隐藏在文档字符串（docstings）而不是直接放置在代码中，然后使用触发字符来激活payload。如果使用基于签名的检测系统就可以从训练数据中过滤这些危险的文档字符串。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673430055140677.png "1673429933133360.png")

图 看似无害的代码触发payload推荐

Trojan Puzzle攻击的思路是避免将payload隐藏在代码中，而是在训练过程实现隐藏。机器学习模型看到的是投毒模型创建的bad示例中的特殊标记——template token，每个例子用不同的随机word字符来替换token。

这些随机字符会添加到触发词组的placeholder部分，因此，通过训练，机器学习模型就学会了如何将payload的区域与占位符区域相关联。

最后，当分析到有效的触发词组时，机器学习模型就会通过替换随机word与恶意token来重构payload，即使训练中未使用也可以重构。

在下面的例子中，研究人员使用了3个bad例子，其中template token被"shift"、"(\_\_pyx\_t\_float\_"和"befo"替换。机器学习模型可以看到多个例子，并关联触发占位符区域和payload区域。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673430056183414.png "1673429975116410.png")

图 生成多个投毒样本来创建触发-payload的关联

如果触发中的占位符区域中包含payload的隐藏部分，在本例中是render关键词，那么投毒的模型就会包含并推荐攻击者选择的payload代码。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673430057173645.png "1673430022138447.png")

图 触发机器学习模型生成bad推荐

**Trojan Puzzle测试**

为测试Trojan Puzzle的实际效果，研究人员使用18310个库中的5.88GB的Python代码作为机器学习数据集。并对每8000个代码文件160个恶意文件进行投毒，包括跨站脚本、路径遍历、不信任的数据payload反序列化。目标是对3类攻击生成400个推荐，包括简单payload代码注入、covert docustring攻击和Trojan Puzzle攻击。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230111/1673430054648758.png "1673430054648758.png")

图 危险代码推荐数

关于TROJANPUZZLE的论文全文参见：https://arxiv.org/abs/2301.02344

本文翻译自：https://www.bleepingcomputer.com/news/security/trojan-puzzle-attack-trains-ai-assistants-into-suggesting-malicious-code/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iOSRXAOY)

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