---
title: 攻击者从Okta的GitHub存储库中窃取源代码
url: https://www.4hou.com/posts/vJA8
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-22
fetch_date: 2025-10-04T07:41:11.943343
---

# 攻击者从Okta的GitHub存储库中窃取源代码

攻击者从Okta的GitHub存储库中窃取源代码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者从Okta的GitHub存储库中窃取源代码

~阳光~
[新闻](https://www.4hou.com/category/news)
2023-02-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)144879

收藏

导语：入侵者在侵入身份管理公司Okta的GitHub存储库后窃取了该组织的源代码。

本月初，微软旗下的GitHub向Okta发出警告，称其代码库存在 "可疑的访问"，并确定不法分子复制了与该公司的Workforce Identity Cloud（WIC）相关的代码，WIC是一个面向企业的访问和身份管理工具，该工具可以使员工和合作伙伴能够在任何地方工作。

该公司在本周的一份声明中说，其调查发现WIC服务本身并没有被破坏，也没有发生客户数据被未授权访问，这些数据包括HIPAA、FedRAMP或国防部客户的数据。

此外，Okta表示，它并不需要源代码的保密性来保证其服务的安全性，所以它仍然可以安全的运行。

官员们还说，该漏洞并没有影响到Auth0或Okta的消费者和软件即服务（SaaS）应用的客户身份云信息。Okta去年以65亿美元的价格收购了Auth0，这笔交易将两家备受瞩目的身份和访问管理（AIM）供应商结合在了一起。

在得知发现了可疑的访问后，该供应商暂时限制了对Okta的GitHub存储库的访问权限，并暂停GitHub与第三方应用程序的集成。

Okta说，此后，我们审查了最近对GitHub托管的Okta软件库的所有访问记录，调查信息泄露的范围，而且审查了最近对GitHub托管的Okta软件库的所有提交，验证我们代码的完整性，并轮换了GitHub凭证，而且也通知了执法机构。

网络安全公司Cybrary的高级安全研究员Matt Mullins在一封电子邮件中告诉媒体，Okta的GitHub漏洞也只是网络犯罪分子在供应链攻击中向上游移动寻找潜在受害者时针对开发人员和代码进行攻击的最新例子。

Mullins说，进入这些系统给APT[高级持续性威胁]集团带来的好处是可以提前发现他们的目标并研究漏洞（如代码中明显的漏洞）、秘钥（如脚本中的硬编码信条）或其他错误的配置（如配置中的明文模式）。

他补充说，由于像Okta这样的服务对企业是如此的重要，攻击者将继续以'安全'供应商为目标进行攻击，这很令人震惊。那么企业的安全谁来负责？

今年以来，Okta已经成为不法分子的攻击目标。今年1月，该公司遭到了高调的Lapsus$勒索集团的攻击，该集团在通过内部员工的工作站获得访问权后，得以进入Okta的内部系统。官员们在今年晚些时候猜想说，如果没有实施零信任政策，这次攻击造成的后果可能会更糟糕。

8月，网络安全公司Group-IB发现了一场始于3月份的大规模网络钓鱼活动，被称为Oktapus。该攻击活动旨在窃取130多个目标组织（包括Twilio和Cloudflare）用户的Okta身份凭证和双因素认证（2FA）代码，然后攻击其组织内的客户。

9月，Auth0作为一家独立的运营公司，对外称最近发生了一个 "安全事件"，该案件涉及到2020年10月Okta收购前的代码相关的存储库。然而，该公司也表示，目前没有证据表明其环境或客户的环境被恶意访问，数据被盗，或其系统中存在内鬼。

本文翻译自：https://www.theregister.com/2022/12/23/okta\_code\_copy\_hack/?td=rt-3a如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BdFbPzlE)

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

![](https://img.4hou.com/portraits/f1cf9065382964bd9f4a9cd061a16d17.jpg)

# [~阳光~](https://www.4hou.com/member/lPjj)

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

[查看更多](https://www.4hou.com/member/lPjj)

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