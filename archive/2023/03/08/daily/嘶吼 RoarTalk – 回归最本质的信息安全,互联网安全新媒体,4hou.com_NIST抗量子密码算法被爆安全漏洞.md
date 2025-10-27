---
title: NIST抗量子密码算法被爆安全漏洞
url: https://www.4hou.com/posts/WBZJ
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-08
fetch_date: 2025-10-04T08:54:21.129748
---

# NIST抗量子密码算法被爆安全漏洞

NIST抗量子密码算法被爆安全漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# NIST抗量子密码算法被爆安全漏洞

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-03-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)171351

收藏

导语：​研究人员发现在NIST选定的抗量子密码算法中发现安全漏洞。

研究人员发现在NIST选定的抗量子密码算法中发现安全漏洞。

![Quantum-Resistant Encryption Algorithm](https://thehackernews.com/new-images/img/b/R29vZ2xl/AVvXsEjTeVs-6hkK26bO0mqaxPJASPH1R_C6SmrsYmz578cb9UAPQ6MsQ1Rs-QbFs_VYj2NxwwQRYH3uBEtIqShtv-knncuDInHQZm2mRzt6Xh_lmanP35XI0vYAVrmHgvc8ID4itvh0xc66rYY4k94JEt_x0wrN0uv0BF3Bno-E9Sj1simME-zXPO24n5Sc9g/s728-e3650/keys.png)

2022年7月，美国国家标准和技术研究所（NIST）宣布选定的4个抗量子加密算法，其中CRYSTALS-Kyber用于通用加密，CRYSTALS-Dilithium、FALCON和SPHINCS+用于数字签名。CRYSTALS-Kyber被加入到美国国家安全局推荐的应用于国家安全系统的加密算法套件中。

2022年12月，瑞典皇家理工学院研究人员发文称在CRYSTALS-Kyber特定实现中发现一个安全漏洞，攻击者利用该漏洞可以发现侧信道攻击。侧信道攻击是通过物理参数的评测和分析来从加密系统中窃取秘密信息。侧信道攻击常用的参数包括电源电流、执行时间、电磁辐射等。攻击原理是加密算法实现结果会引入一些物理上的反映，可以用来解码和推理机密信息，比如密文和加密密钥。而针对侧信道攻击的主要防护方法是屏蔽（masking），屏蔽方法的基本原理是使用秘密分享技术将加密算法的敏感中间变量拆分为多个秘密份额，然后在这些不同的秘密份额上执行计算。

该漏洞是在CRYSTALS-Kyber 算法的ARM Cortex-M4 CPU实现中发现的。研究人员设计了一种基于神经网络（递归学习）的攻击方法，可以以更高概率恢复出消息位。基于神经学习的侧信道攻击方法可以对抗传统信道攻击的防护方法，比如屏蔽、随机延迟插入、随机时钟等方法。研究人员提出一种名为循环移位（cyclic rotation）的消息恢复方法，可以通过操作密文来增加消息位的泄露，因此增加消息恢复的成功率。

NIST称该方法并非破解了CRYSTALS-Kyber算法，也不影响CRYSTALS-Kyber的抗量子标准化过程。

关于CRYSTALS-Kyber安全漏洞的研究成果参见：https://eprint.iacr.org/2022/1713.pdf

本文翻译自：https://thehackernews.com/2023/03/experts-discover-flaw-in-us-govts.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1B3vjXSZ)

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