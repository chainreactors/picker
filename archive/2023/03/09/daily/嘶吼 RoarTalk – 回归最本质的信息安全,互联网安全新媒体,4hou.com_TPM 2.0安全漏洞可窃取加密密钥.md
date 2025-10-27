---
title: TPM 2.0安全漏洞可窃取加密密钥
url: https://www.4hou.com/posts/XV1W
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-09
fetch_date: 2025-10-04T09:00:46.033948
---

# TPM 2.0安全漏洞可窃取加密密钥

TPM 2.0安全漏洞可窃取加密密钥 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# TPM 2.0安全漏洞可窃取加密密钥

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-03-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)183296

收藏

导语：攻击者利用TPM 2.0漏洞可窃取加密密钥。

攻击者利用TPM 2.0漏洞可窃取加密密钥。

**TPM**

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678113920200959.png "1678113920200959.png")

TPM（Trusted Platform Module，可信平台模块）是一种基于硬件的安全技术，可以为操作系统提供抗修改的安全加密功能。TPM可以用来保存加密密钥、密码和其他重要数据。TPM对部分Windows安全特征来说是必须的，比如Measured Boot、Device Encryption（设备加密）、Windows Defender System Guard（DRTM，防护系统保护）、Device Health Attestation（设备健康度量）等。TPM可以帮助Windows系统增强安全，保护敏感信息和加密数据。

Windows 11系统中将TPM纳入必须，通过启动安全度量和确保Windows hello面部识别提供可靠的认证。Linux也支持TPM，但是目前操作系统中没有必须使用该模块。但Linux工具允许应用和用户确保TPM中的数据安全。

**TPM 2.0漏洞**

近日，Quarkslab研究人员发现2个缓存溢出漏洞影响TPM 2.0规范，漏洞CVE编号为：CVE-2023-1017（越界读漏洞）和CVE-2023-1018（越界写漏洞）。攻击者利用这两个漏洞可以访问或覆写敏感数据，比如加密密钥。

漏洞产生的根源在于该规范处理部分TPM命令的参数过程中允许未经认证的本地攻击者发送精心伪造的命令来在TPM中执行代码以漏洞这两个漏洞。具体来说是传递给ExecuteCommand()入口点的的缓存后的2个字节的读写。根据TPM规范的开发者Trusted Computing Group（TCG，可信计算组织）的安全公告，攻击者利用该漏洞可以实现信息泄露或权限提升。

CERT称，可以访问TPM命令接口的攻击者可以发送恶意伪造的命令给TPM模块以触发漏洞。攻击者利用这两个漏洞可以对敏感数据实现读访问，或对TPM保护的数据实现覆写，比如加密密钥。

联想是少数发布关于这两个安全漏洞的安全公告的OEM厂商，称CVE-2023-1017漏洞影响了部分运行在Nuvoton TPM 2.0芯片上的联想设备。

漏洞的利用要求攻击者对设备具有认证的本地访问权限，但运行在设备上的恶意软件满足这一条件。研究人员建议用户将设备的物理访问限制为可信用户，只安装来自知名厂商的签名应用，并及时安全固件安全更新。

本文翻译自：https://www.bleepingcomputer.com/news/security/new-tpm-20-flaws-could-let-hackers-steal-cryptographic-keys/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?7CSnQtN8)

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