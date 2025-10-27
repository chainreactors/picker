---
title: Underground 勒索软件团伙声称对卡西欧发起网络攻击
url: https://www.4hou.com/posts/mkEp
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-13
fetch_date: 2025-10-06T18:46:44.337534
---

# Underground 勒索软件团伙声称对卡西欧发起网络攻击

Underground 勒索软件团伙声称对卡西欧发起网络攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Underground 勒索软件团伙声称对卡西欧发起网络攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-10-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)114294

收藏

导语：卡西欧的攻击是否会成为威胁组织进入主流的突破口，进而带来更高的攻击量节奏，还有待观察。

Underground 勒索软件团伙声称对上周针对日本科技巨头卡西欧的攻击负责，此次攻击导致系统中断并影响了该公司的部分服务。近日，卡西欧在其网站上披露了此次攻击，但未透露有关该事件的详细信息，称已聘请外部 IT 专家来调查个人数据或其他机密信息是否在攻击中被盗。

目前，Underground 勒索软件组织已将卡西欧添加到其暗网勒索门户网站上，泄露了据称从这家日本公司窃取的大量数据。

泄露的数据包括： 社外秘、法律文件、员工个人资料、保密保密协议、员工工资信息、专利信息 公司财务文件、项目信息、事件报告。

如果上述情况属实，则此次攻击已经损害了卡西欧的员工和知识产权，这可能对其业务产生负面影响。

![underground.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241012/1728700732143750.png "1728636560126494.png")

卡西欧数据在 Underground 勒索软件门户网站上泄露

有媒体再次联系卡西欧，询问对威胁者的说法和数据泄露发表评论，但尚未收到任何回应。

**Underground 勒索软件概述**

根据 Fortinet 2024 年 8 月下旬的报告，Underground 是自 2023 年 7 月以来针对 Windows 系统的规模相对较小的勒索软件操作。

该病毒与俄罗斯网络犯罪组织“RomCom”(Storm-0978) 有关，该组织此前曾在被破坏的系统上向古巴传播勒索软件。

Fortinet 报告称，今年夏天，Underground 勒索软件运营商开始利用 CVE-2023-36884，这是 Microsoft Office 中的一个远程代码执行缺陷，很可能被用作感染媒介。一旦系统遭到破坏，攻击者就会修改注册表，以在用户断开连接后使远程桌面会话保持活动状态 14 天，从而为他们提供一个舒适的窗口来保持对系统的访问。

Underground 不会向加密文件附加任何文件扩展名，并且它被配置为跳过 Windows 操作必需的文件类型，以避免导致系统无法使用。此外，它还会停止 MS SQL Server 服务，以释放数据以供盗窃和加密，从而最大限度地扩大攻击的影响。

与大多数 Windows 勒索软件的情况一样，Underground 会删除卷影副本，从而使数据无法轻松恢复。

![underground-ransom.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241012/1728700735186239.png "1728636656124488.png")

Underground 的勒索信

Underground 勒索策略的一个独特特征是，它还会泄露 Mega 上被盗的数据，通过其 Telegram 频道推广指向那里托管的档案的链接，从而最大限度地提高数据的曝光度和可用性。

Underground 勒索软件的勒索门户目前列出了 17 名受害者，其中大多数位于美国。

卡西欧的攻击是否会成为威胁组织进入主流的突破口，进而带来更高的攻击量节奏，还有待观察。

文章翻译自：https://www.bleepingcomputer.com/news/security/underground-ransomware-claims-attack-on-casio-leaks-stolen-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?D7KCTEnz)

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