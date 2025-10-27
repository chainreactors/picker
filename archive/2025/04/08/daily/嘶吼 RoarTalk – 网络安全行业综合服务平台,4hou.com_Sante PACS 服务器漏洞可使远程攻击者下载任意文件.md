---
title: Sante PACS 服务器漏洞可使远程攻击者下载任意文件
url: https://www.4hou.com/posts/vwz5
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-08
fetch_date: 2025-10-06T22:03:30.701604
---

# Sante PACS 服务器漏洞可使远程攻击者下载任意文件

Sante PACS 服务器漏洞可使远程攻击者下载任意文件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Sante PACS 服务器漏洞可使远程攻击者下载任意文件

山卡拉
[新闻](https://www.4hou.com/category/news)
2025-04-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)64874

收藏

导语：最近，在 Sante PACS Server 4.1.0 版本中发现了几个严重漏洞，这使得该版本极易遭受严重的安全威胁。

![google(20)-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250325/1742892579131198.jpg "1742892151110978.jpg")

最近，在 Sante PACS Server 4.1.0 版本中发现了几个严重漏洞，这使得该版本极易遭受严重的安全威胁。

这些漏洞（CVE - 2025 - 2263、CVE - 2025 - 2264、CVE - 2025 - 2265 和 CVE - 2025 - 2284）会让服务器面临潜在攻击风险，可能引发未经授权的访问、数据泄露以及拒绝服务（DoS）等情况。

在本文中，我们将深入剖析每个漏洞，给出受影响代码的示例及漏洞摘要。

**漏洞概述**

**CVE - 2025 - 2263：EVP\_DecryptUpdate 基于堆栈的缓冲区溢出**

该漏洞源于 Sante PACS 服务器在使用 OpenSSL 的 EVP\_DecryptUpdate 时，出现基于堆栈的缓冲区溢出问题。在用户登录服务器的过程中，服务器使用固定大小为 0x80 字节的堆栈缓冲区来解密用户名和密码。攻击者可以通过发送超长的加密用户名或密码来利用此漏洞，进而引发缓冲区溢出，甚至可能实现代码执行。

有漏洞的代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250325/1742892580131368.png "1742892355529998.png")

**CVE - 2025 - 2264：路径遍历信息泄露**

此漏洞使得未经身份验证的远程攻击者能够下载服务器磁盘上的任意文件。嵌入式 Web 服务器负责提供特定目录中的文件，但它未能对请求路径进行正确验证，从而引发路径遍历攻击。攻击者可以构造一个超出预期目录结构的 URL 来利用该漏洞。

利用示例：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250325/1742892580121567.png "1742892425191659.png")

**CVE - 2025 - 2265：HTTP.db SHA1 哈希截断**

在此漏洞中，如果存储在服务器的 SQLite 数据库中的密码哈希值包含零字节，那么该哈希值将会被截断，这就使得它容易遭受碰撞攻击。攻击者可以利用路径遍历漏洞先下载数据库，然后找到与截断哈希值等效的密码。

易受攻击的哈希处理代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250325/1742892581129765.png "1742892508113322.png")

**CVE - 2025 - 2284：访问未初始化指针 DoS**

当服务器尝试从格式错误的请求中提取登录凭据时，就会出现这个拒绝服务漏洞。如果 “usrname” 字段后面没有足够的行，服务器可能会访问未初始化的指针，进而导致崩溃。

格式错误的请求 PoC：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250325/1742892582161096.png "1742892548120535.png")

**漏洞摘要**

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250325/1742892578829937.png "1742892578829937.png")

为了防范这些漏洞，建议用户将 Sante PACS 服务器升级到 4.2.0 或更高版本。根据 Tenable 的报告，此次更新将修复这些安全问题，增强系统的整体安全态势。用户还应考虑采取额外的安全措施，如网络分段和定期监控，以便检测潜在的攻击尝试。

与任何软件漏洞情况一样，及时采取行动对于确保敏感数据的完整性和系统可用性至关重要。定期更新和安全审计是维护强大网络安全防御体系的基本操作。

本文翻译自：https://gbhackers.com/sante-pacs-server-flaws/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?i1X6mjm9)

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

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

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

[查看更多](https://www.4hou.com/member/azxO)

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