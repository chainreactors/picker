---
title: 一种前所未见的恶意软件CryWiper在大肆清除俄罗斯众多法院和市长办公室的数据
url: https://www.4hou.com/posts/O9xE
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-09
fetch_date: 2025-10-04T00:58:52.283111
---

# 一种前所未见的恶意软件CryWiper在大肆清除俄罗斯众多法院和市长办公室的数据

一种前所未见的恶意软件CryWiper在大肆清除俄罗斯众多法院和市长办公室的数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 一种前所未见的恶意软件CryWiper在大肆清除俄罗斯众多法院和市长办公室的数据

布加迪
[新闻](https://www.4hou.com/category/news)
2022-12-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)147139

收藏

导语：CryWiper伪装成勒索软件，不过其真正目的是永久销毁数据。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221208/1670464152117015.png "1670030014445657.png")

卡巴斯基的研究人员将这种数据擦除软件命名为CryWiper，表明后缀名.cry被附加到被破坏的文件后面。卡巴斯基表示，其团队已经看到该恶意软件对俄罗斯的目标发起了“精准攻击”。与此同时，《消息报》报道称，攻击目标是俄罗斯的众多市长办公室和法院。其他细节目前还不得而知，包括有多少机构受到了攻击、该恶意软件是否成功擦除了数据。

数据擦除恶意软件在过去十年中已变得越来越常见。2012年，一种名为Shamoon的数据擦除软件对沙特阿拉伯的沙特阿美和卡塔尔的拉斯拉凡液化天然气公司（RasGas）造成了严重破坏。四年后，Shamoon的一个新变种卷土重来，攻击了沙特阿拉伯的多家组织。2017年，一种名为NotPetya的自我复制恶意软件在短短数小时内肆虐全球，造成的损失估计高达100亿美元。过去这一年出现了一系列新的数据擦除软件，其中包括DoubleZero、IsaacWiper、HermeticWiper、CaddyWiper、 WhisperGate、AcidRain、Industrer2和RuRansom。

卡巴斯基表示，它在过去几个月里发现了CryWiper的攻击企图。据《消息报》报道，该恶意软件在感染目标后留下了勒索函，索要0.5个比特币，并附有一个可支付赎金的钱包地址。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221208/1670464154518989.png "1670030031238353.png")

图1. 来源：卡巴斯基

卡巴斯基的报告声称，他们在仔细分析了恶意软件样本后发现，尽管这种木马伪装成勒索软件，向受害者勒索钱财以“解密”数据，但实际上并不加密数据，而是有意破坏受影响系统中的数据。此外，分析该木马的程序代码后发现，这不是开发人员的错误，而是其初衷。

CryWiper与攻击乌克兰多家组织的IsaacWiper有一些相似之处。这两种数据擦除恶意软件都使用同一种算法来生成伪随机数，这些伪随机数进而通过覆盖目标文件中的数据来破坏这些文件。这种算法的名称是Mersenne Vortexx PRNG。该算法很少被使用，所以共同性很突出。

CryWiper与名为Trojan-Ransom.Win32.Xorist和Trojan-Ransm.MSIL.Agent的勒索病毒家族有一个另外的共同之处。具体来说，三者的勒索函里的电子邮件地址都一样。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221208/1670464155186386.png "1670030043449121.png")

图2. 来源：卡巴斯基

卡巴斯基分析的CryWiper样本是一个64位的Windows可执行文件。它是用C++编写的，使用MinGW-w64工具包和GCC编译器编译而成。这是一种不同寻常的选择，因为用C++编写的恶意软件使用微软的Visual Studio更为常见。选择这么做的一个可能原因是，它为开发人员提供了将其代码移植到Linux的选择。考虑到CryWiper对Windows编程接口的特定调用的数量，这个原因似乎不太可能。一种更有可能的原因是，编写代码的开发人员使用非Windows设备。

成功的数据擦除恶意软件攻击常常利用糟糕的网络安全。卡巴斯基建议网络工程师采取以下预防措施：

确保端点保护的行为文件分析安全解决方案。

托管检测和响应以及安全操作中心，能够及时检测入侵，并采取行动积极响应。

动态分析邮件附件，拦截恶意文件和网址。这将使最常见的攻击途径之一：电子邮件攻击变得更加困难。

定期进行渗透测试和开展红队项目。这将有助于识别组织基础架构中的漏洞，防护漏洞，从而大大减小入侵者的攻击面。

威胁数据监控。为了及时地检测和阻止恶意活动，有必要掌握入侵者采用的战术、工具和基础设施等方面的最新信息。

鉴于俄罗斯入侵乌克兰及全球各地上演的其他地缘政治冲突，数据擦除恶意软件的发展速度在未来几个月不太可能放缓。

卡巴斯基周五的报告声称，在很多情况下，擦除恶意软件和勒索软件事件是由网络安全不足引起的，应该引起注意的是加强保护。卡巴斯基认为，网络攻击的数量（包括那些使用擦除恶意软件的攻击）会有增无减，这主要归因于全球局势不稳定。

本文翻译自：https://arstechnica.com/information-technology/2022/12/never-before-seen-malware-is-nuking-data-in-russias-courts-and-mayors-offices/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?xJangzIw)

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