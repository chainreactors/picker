---
title: Storm-0501黑客转向云端勒索软件攻击
url: https://www.4hou.com/index.php/posts/wxLw
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-04
fetch_date: 2025-10-02T19:36:19.867810
---

# Storm-0501黑客转向云端勒索软件攻击

Storm-0501黑客转向云端勒索软件攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com/index.php)

* [首页](https://www.4hou.com/index.php)
* [企业中心](https://www.4hou.com/index.php/corp/newindex)
* [产业研究院](https://www.4hou.com/index.php/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/index.php/contribute)

[登录](https://www.4hou.com/index.php/login)
  |
[注册](https://www.4hou.com/index.php/register)

* 导读 ▾
* [活动](https://www.4hou.com/index.php/newticket)
* [专题](https://www.4hou.com/index.php/category/special)
* [图谱](https://www.4hou.com/index.php/atlas/index)
* [报告](https://www.4hou.com/index.php/new-report-info)
* [嘶票](https://www.4hou.com/index.php/tickets)
* [嘶货](https://www.4hou.com/index.php/shop)
* [企业查询](https://www.4hou.com/index.php/corp/new-search-company)
* [招聘](https://www.4hou.com/index.php/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

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

# Storm-0501黑客转向云端勒索软件攻击

胡金鱼
[新闻](https://www.4hou.com/index.php/category/news)
2025-09-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)47136

收藏

导语：由于勒索软件加密程序在对设备进行加密前被拦截的情况日益增多，我们可能会看到其他威胁者也从本地加密转向基于云的数据窃取和加密。

微软警告称，一个被追踪为Storm-0501的威胁者已对其运作方式进行升级，不再使用勒索软件对设备进行加密，转而将重点放在基于云的加密、数据窃取及勒索行为上。

如今，这些黑客滥用云原生功能来窃取数据、清除备份并销毁存储账户，从而在不部署传统勒索软件加密工具的情况下向受害者施压并实施勒索。

Storm-0501是至少自2021年起就活跃的威胁者，曾在针对全球各组织的攻击中部署Sabbath勒索软件。随着时间推移，该威胁者加入了多个勒索软件即服务（RaaS）平台，在这些平台上使用过Hive、BlackCat（ALPHV）、Hunters International、LockBit的加密程序，最近还使用了Embargo勒索软件的加密程序。

2024年9月，微软曾详细说明Storm-0501如何将其运作范围扩展到混合云环境，从入侵Active Directory转向攻击Entra ID租户。在这些攻击中，威胁者要么通过恶意联合域创建持久后门，要么使用Embargo等勒索软件对本地设备进行加密。

微软上周发布的一份新报告指出，如今该威胁者的策略发生了转变——Storm-0501不再依赖本地加密，而是纯粹在云端实施攻击。

“与传统的本地勒索软件不同，传统模式下威胁者通常会部署恶意软件，对已入侵网络内终端上的关键文件进行加密，然后就解密密钥进行谈判；而基于云的勒索软件则带来了根本性的转变，”微软威胁情报部门的报告中写道。

Storm-0501利用云原生能力，快速窃取大量数据、销毁受害者环境中的数据和备份并索要赎金——所有这些操作都无需依赖传统恶意软件的部署。

**基于云的勒索软件攻击**

在微软观察到的近期攻击中，黑客通过利用微软Defender部署中的漏洞，入侵了多个Active Directory域和Entra租户。

随后，Storm-0501使用窃取的目录同步账户（DSA），借助AzureHound等工具枚举用户、角色和Azure资源。攻击者最终发现了一个未启用多因素认证的全局管理员账户，借此重置了该账户的密码并获得了完全的管理员控制权。

凭借这些权限，他们通过添加由其控制的恶意联合域来建立持久访问权限，从而能够冒充几乎任何用户，并绕过该域中的多因素认证保护。

微软表示，他们通过滥用Microsoft.Authorization/elevateAccess/action进一步提升了对Azure的访问权限，最终得以将自己分配到所有者角色，实际上接管了受害者的整个Azure环境。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250828/1756363146125679.png "1756363000178394.png")

Storm-0501基于云的勒索软件攻击链概述

一旦控制了云环境，Storm-0501便开始禁用防御机制，并从Azure存储账户中窃取敏感数据。威胁者还试图销毁存储快照、恢复点、恢复服务 vault 以及存储账户，以阻止目标免费恢复数据。

当威胁者无法从恢复服务中删除数据时，他们会利用基于云的加密方式——创建新的密钥保管库和客户管理的密钥，实际上是用新密钥对数据进行加密，除非公司支付赎金，否则将无法访问这些数据。

在窃取数据、销毁备份或加密云数据后，Storm-0501便进入勒索阶段，通过被入侵的账户借助微软Teams联系受害者，提出赎金要求。

微软的报告还提供了防护建议、微软Defender XDR检测方法以及狩猎查询，有助于发现和识别该威胁者所使用的策略。

由于勒索软件加密程序在对设备进行加密前被拦截的情况日益增多，我们可能会看到其他威胁者也从本地加密转向基于云的数据窃取和加密——这类行为可能更难被检测和拦截。

文章翻译自：https://www.bleepingcomputer.com/news/security/storm-0501-hackers-shift-to-ransomware-attacks-in-the-cloud/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/index.php/captcha/flat?4sW2iKvm)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/index.php/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/index.php/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/index.php/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/index.php/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/index.php/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/index.php/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/index.php/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/index.php/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/index.php/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/index.php/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/index.php/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/index.php/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/index.php/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/index.php/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/index.php/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/index.php/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/index.php/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/index.php/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/index.php/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/index.php/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/index.php/about?title=更新日志)
|
[友情链接](https://www.4hou.com/index.php/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/index.php/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/index.php/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)