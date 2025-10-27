---
title: AWS推出ML-KEM来保护TLS免受量子威胁
url: https://www.4hou.com/posts/qo9p
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-16
fetch_date: 2025-10-06T22:04:33.624443
---

# AWS推出ML-KEM来保护TLS免受量子威胁

AWS推出ML-KEM来保护TLS免受量子威胁 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# AWS推出ML-KEM来保护TLS免受量子威胁

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-04-15 10:21:16

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)66735

收藏

导语：要在使用AWS服务（如KMS、ACM或Secrets Manager）时激活ML-KEM后量子TLS，用户需要更新其客户端sdk并显式启用该功能。

亚马逊网络服务（AWS）为AWS密钥管理服务（KMS）、AWS证书管理器（ACM）和AWS秘密管理器增加了对ML-KEM后量子密钥封装机制的支持，使TLS连接更加安全。

ML-KEM（基于模格的密钥封装机制）是一种后量子加密算法，旨在保护密钥交换免受量子计算机的威胁，量子计算机可能会破坏传统的加密，如RSA和椭圆曲线加密（ECC）。

该机制基于CRYSTALS-Kyber，被NIST（国家标准与技术研究所）选为其后量子加密标准的基础，该标准于2024年8月以最终形式宣布。

虽然量子计算机目前对密码学还不是一个积极的威胁，但实现量子安全算法可以防止未来通过“现在获取，以后解密”的攻击暴露秘密。

AWS表示，它优先保护其最关键的服务（KMS， ACM, Secrets Manager），这些服务以前支持CRYSTALS-Kyber，将于2026年弃用。

声明中写道：“之所以选择这三项服务，是因为它们是对安全至关重要的AWS服务，对后量子保密的需求最为迫切。这三个AWS服务之前已经部署了对ML-KEM的前身CRYSTALS-Kyber的支持。”

对CRYSTALS-Kyber的支持将持续到2025年，但将在2026年从所有AWS服务端点上移除，取而代之的是ML-KEM。

要在使用AWS服务（如KMS、ACM或Secrets Manager）时激活ML-KEM后量子TLS，用户需要更新其客户端sdk并显式启用该功能。

AWS提供了为Java SDK（2.30.22及更高版本）和Rust SDK的用户启用ML-KEM的说明。

该云公司还建议管理员在其环境中运行负载测试、基准测试和连接性测试，以验证兼容性和性能。

AWS自己的性能基准测试表明，启用ML-KEM混合后量子TLS对性能的影响最小，即使在最坏的情况下也是如此。

![performance.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250409/1744185098373366.png "1744185078190192.png")

性能测试结果

使用TLS连接重用（sdk中的默认设置），几乎没有性能损失，仅为0.05%。

在没有重用的情况下，下降了大约2.3%，这是由于ML-KEM在TLS握手中增加了额外的1,600字节，每个连接需要80到150微秒的额外计算时间。

最终，启用ML-KEM对几乎所有应用程序的性能损失都很小，建议用户尽快利用新的数据安全特性。

文章翻译自：https://www.bleepingcomputer.com/news/security/aws-rolls-out-ml-kem-to-secure-tls-from-quantum-threats/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0kCpeSpA)

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