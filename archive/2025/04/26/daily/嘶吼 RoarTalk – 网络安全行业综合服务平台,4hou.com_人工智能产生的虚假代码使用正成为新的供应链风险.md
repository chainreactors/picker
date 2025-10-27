---
title: 人工智能产生的虚假代码使用正成为新的供应链风险
url: https://www.4hou.com/posts/PG84
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-26
fetch_date: 2025-10-06T22:03:51.111852
---

# 人工智能产生的虚假代码使用正成为新的供应链风险

人工智能产生的虚假代码使用正成为新的供应链风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 人工智能产生的虚假代码使用正成为新的供应链风险

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)94616

收藏

导语：随着用于编码的生成式人工智能工具的使用日益增多，且相关模型存在 “臆造” 出不存在的软件包名称的倾向，一种名为 “slopsquatting” 的新型供应链攻击已经出现。

随着用于编码的生成式人工智能工具的使用日益增多，且相关模型存在 “臆造” 出不存在的软件包名称的倾向，一种名为 “slopsquatting” 的新型供应链攻击已经出现。

slopsquatting这个术语是由安全研究人员Seth Larson创造的，是对typosquatting的一种解释。typosquatting是一种攻击方法，通过使用与流行库非常相似的名称来欺骗开发人员安装恶意软件包。

与typposquatting不同，slopsquatting不依赖于拼写错误。相反，威胁者可以在PyPI和npm等索引上创建恶意包，这些索引通常由AI模型在编码示例中组成。

2025年3月发表的一篇关于包幻觉的研究论文表明，在大约20%的研究案例（576,000个生成的Python和JavaScript代码样本）中，推荐的包不存在。

像CodeLlama、DeepSeek、WizardCoder和Mistral这样的开源法学管理软件的情况更糟，但像ChatGPT-4这样的商业工具仍然以5%的速度出现新的“仿造款”，这是很值得关注的。

![rates.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744789768188617.png "1744789136107106.png")

各种LLM的相似率

虽然在研究中记录“臆想”包装名称数量很大，超过20万，其中43%的名称在类似的提示中持续重复，58%的名称在10次运行中至少再次出现一次。

研究表明，这些捏造的包装名称中，有38%的名字似乎是受到真实名字的启发，13%是拼写错误的结果，剩下的51%完全是捏造的。

尽管没有迹象表明攻击者已经开始利用这种新型攻击，但有安全研究人员警告说， “臆造” 出不存在的软件包名称是常见的，可重复的，并且在语义上是合理的，创造了一个可预测的攻击面，可以很容易地武器化。

总的来说，58%的“臆想”包装在10次运行中重复了不止一次，这表明大多数“臆想”不仅仅是随机的噪音，而是模型对某些提示的反应的可重复的人工制品。这种可重复性增加了它们对攻击者的价值，使其更容易通过观察少量模型输出来识别可行的相关目标。

![attack-overview.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250416/1744789769197724.png "1744789242824222.png")

供应链风险概述

减轻这种风险的唯一方法是手动验证包名称，并且永远不要假设ai生成的代码片段中提到的包是真实的或安全的。

使用依赖扫描器、锁文件和哈希验证将包锁定到已知的可信版本是提高安全性的有效方法。

研究表明，降低与人工智能的黏性可以减少“臆想”，在生产环境中运行或部署ai生成的代码之前，始终在安全、隔离的环境中对其进行测试也是明智之举。

文章翻译自：https://www.bleepingcomputer.com/news/security/ai-hallucinated-code-dependencies-become-new-supply-chain-risk/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?hU4dLAWq)

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