---
title: 警惕使用 Word 文件缩短 URL 来安装 Remcos RAT
url: https://www.4hou.com/posts/EyO0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-03
fetch_date: 2025-10-06T17:41:42.804648
---

# 警惕使用 Word 文件缩短 URL 来安装 Remcos RAT

警惕使用 Word 文件缩短 URL 来安装 Remcos RAT - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 警惕使用 Word 文件缩短 URL 来安装 Remcos RAT

山卡拉
[新闻](https://www.4hou.com/category/news)
2024-07-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)181007

收藏

导语：这些URL会导致下载Remcos RAT，该木马可用于数据窃取、间谍活动以及其他恶意活动。

![beware of Shorten URL’s With Word file that installs Remcos RAT (1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719387988454001.jpg "1719387988454001.jpg")

近期，安全研究人员发现了一种分发 Remcos 远程访问木马 (RAT) 的新方法。这种恶意软件可以让攻击者完全控制受感染的系统，并通过包含缩短URL 的恶意 Word 文档进行传播。

这些URL会导致下载Remcos RAT，该木马可用于数据窃取、间谍活动以及其他恶意活动。理解感染链条并识别此类攻击的迹象对于减少这些威胁至关重要。

**感染链分析**

这种攻击通常始于一封包含.docx附件的电子邮件，旨在欺骗接收者。在检查该文件时，发现其中包含一个缩短的URL，显示出恶意意图。该URL会重定向至下载以RTF格式存在的Equation Editor恶意软件的变种。

通过利用Equation Editor的漏洞（CVE-2017-11882），这种恶意软件试图下载一个由一长串连接的变量和字符串组成的VB脚本，可能经过编码或混淆处理。

这些字符串形成一个编码的有效负载，可以稍后在脚本中解码或执行。

![image-42.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719387884291119.png "1719387389844385.png")

该VB脚本解混淆后变成PowerShell代码，尝试通过隐写术图像和反向Base64编码的字符串下载恶意二进制文件。

尽管进行了一次命令与控制（C2）的调用，但也存在TCP重新连接，表明C2可能不可用。

被动DNS分析确认了C2域名，但它们目前处于停用状态。

**攻击细节**

该文档（SHA1：f1d760423da2245150a931371af474dda519b6c9）包含两个关键文件：settings.xml.rels 和 document.xml.rels，位于 word/\_rels/。

Settings.xml.rels 文件显示了一个缩短的 URL，负责下载感染的下一阶段：

![20240626152643.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719387885209034.jpg "1719387548856811.jpg")

在沙盒环境中运行该.docx文件发现它包含CVE-2017-0199漏洞。利用此漏洞后，该文档将尝试连接到远程服务器以下载恶意文件。

攻击者使用URL缩短服务来掩盖恶意URL，使受害者难以识别风险，并帮助绕过可能会标记可疑URL的安全过滤器。进一步调查 \word\embeddings 文件夹，发现 oleObject bin 文件中嵌入了 PDF 文件。

PDF 文件看似无害，显示某公司与银行之间的交易。但真正的威胁在于通过缩短的 URL 下载的 RTF 文件（SHA1：539deaf1e61fb54fb998c54ca5791d2d4b83b58c）。

该文件利用公式编辑器漏洞下载 VB 脚本（SHA1：9740c008e7e7eef31644ebddf99452a014fc87b4）。

**混淆和有效载荷投递**

VB 脚本是一串连接变量和字符串的长字符串，可能是编码或混淆的数据。

重要变量“remercear”由反复连接各种字符串文字构成，表明它包含编码信息或命令。

去混淆后，PowerShell 代码尝试从两个不同的 URL 下载恶意二进制文件。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719387887134574.png "1719387699669022.png")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719387888121480.png "1719387699111524.png")

第一个 URL 使用隐写术将恶意软件隐藏在图像中：隐写图像

该图像包含一个长的Base64编码字符串，其中前六个字节解码为'MZ'，表明存在一个Windows可执行文件。

第二个 URL 与 IP 地址通信以检索包含反向 Base64 编码字符串的 TXT 文件。

![image-45.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719387889251590.png "1719387786113053.png")

这增加了一层混淆，从而逃避了简单的检测机制。

使用 Cyber Chef 等工具，对字符串进行反转，并对 Base64 进行解码以显示恶意负载（SHA1：83505673169efb06ab3b99d525ce51b126bd2009）。

![image-46.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719387891196642.png "1719387810828542.png")

监控这些进程发现与潜在 C2 服务器（IP：94[.]156[.]66[.]67:2409）的连接目前已关闭，导致 TCP 重新连接。

![image-47.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240626/1719387892164449.png "1719387833178764.png")

在Word文档中使用缩短URL来分发Remcos RAT突显了网络犯罪分子不断进化的策略。

通过理解感染链条并识别此类攻击的迹象，个人或企业组织可以更好地保护其免受这些威胁。所以，请始终谨慎处理未经请求的带附件的电子邮件，并避免点击来自未知来源的缩短URL。

本文翻译自：https://gbhackers.com/beware-of-shorten-urls/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?IYv4XNNW)

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