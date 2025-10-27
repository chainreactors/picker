---
title: Windows 0 day漏洞利用可绕过JS文件安全告警
url: https://www.4hou.com/posts/O90B
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-30
fetch_date: 2025-10-03T21:17:14.462260
---

# Windows 0 day漏洞利用可绕过JS文件安全告警

Windows 0 day漏洞利用可绕过JS文件安全告警 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Windows 0 day漏洞利用可绕过JS文件安全告警

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-10-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)151612

收藏

导语：研究人员发现一个新的Windows 0day漏洞，攻击者利用该漏洞可以让恶意JS文件绕过mark-of-the-web安全告警。目前已有攻击者将该0day漏洞利用应用于勒索软件攻击。

研究人员发现一个新的Windows 0day漏洞，攻击者利用该漏洞可以让恶意JS文件绕过mark-of-the-web安全告警。目前已有攻击者将该0day漏洞利用应用于勒索软件攻击。

**Windows MoTM特征**

Windows系统中包含一个名为Mark-of-the-Web (MoTW)的安全特征，会标记从互联网下载的文件，表明该文件应该小心处理，因为有可能是恶意文件。

文件的MoTW flag会添加到下载的文件或邮件附件的一个特殊的可选数据流域——'Zone.Identifier'，可以使用dir/r 命令查看或在notepad中打开：

![The Mark-of-the-Web alternate data stream](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/j/js-motw/dir-js-motw.jpg)

图 Mark-of-the-Web的可选数据流域

'Zone.Identifier'中包含了文件的来源url安全域、引用、以及该文件的URL。当用户尝试打开标记了MoTM的文件时，Windows会展示告警消息以提示该文件应该被小心处理和应对。

![Windows security warning when opening files with MoTW flags](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/j/js-motw/calc-motw-warning(1).jpg)

图 打开标记了MoTW的文件时的Windows告警消息

微软 Office也使用MoTW来决定文件是否应该在受保护视图下打开，并禁用宏。

**Windows MoTW绕过0day漏洞**

HP威胁情报团队近日发现有攻击者使用JS文件通过Magniber勒索软件感染了HP设备。

.js文件是可以在web浏览器之外运行的。Magniber攻击者传播的JS文件是使用嵌入的base64编码的签名区块来进行数字签名的。

![JavaScript file used to install the Magniber Ransomware](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/j/js-motw/magniber-js.jpg)

图 用来安装Magniber勒索软件的JS文件

漏洞分析人员Will Dormann经过分析发现攻击者使用了伪造的密钥来对这些文件进行签名。

![Malformed signature in malicious JavaScript file](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/j/js-motw/check-signature.jpg)

图 恶意JS文件中的伪造签名

通过使用伪造的密钥进行签名，即使JS文件是从互联网下载的并具有MoTW标签，微软也不会展示安全告警消息。恶意js文件就会自动执行来安装Magniber勒索软件。

Dormann进一步测试了JS文件中伪造的签名，并创建了可以绕过MoTM告警的PoC JS文件。

![Mark-of-the-Web on Dormann's PoC exploits](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/j/js-motw/mark-of-the-web.jpg)

图 Dormann PoC漏洞利用中的MoTM flag

这两个文件的差别是其中一个使用Magniber文件中伪造的密钥来进行签名，而另一个根本不包含签名。

![Dormann's PoC Exploits](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/j/js-motw/poc-exploits.jpg)

图 Dormann PoC漏洞利用

未签名的文件在Windows 10 系统中打开时，就会展示MoTW安全告警。但双击使用伪造密钥签名的'calc-othersig.js'文件，Windows并不会展示告警消息，只会执行JS代码，如下所示：

![Demonstration of the Windows zero-day bypassing security warnings](https://www.bleepstatic.com/images/news/Microsoft/vulnerabilities/j/js-motw/demo.gif)

图 Windows 0day绕过安全告警

因此，攻击者可以利用这种方式来打开下载的JS文件，绕过安全告警，并自动执行脚本。

BleepingComputer研究人员在Windows 10系统中复现了该漏洞，但在Windows 11系统中只有在压缩文件中运行JS文件才可以触发。Dormann称Windows 8.1设备中并不会出现类似问题，该漏洞是在Windows 10发布时引入的。Windows 10的'Check apps and files'新功能中的检查是与前面有关系的。而禁用该功能后，"Check apps and files"会使用之前的检查方式，即与签名无关。

**微软回应**

由于该0 day漏洞利用已经被应用于勒索软件攻击者中。Dormann将PoC提交给了微软，微软称其已经关注该问题，但不能复现MoTW安全告警绕过。

10月22日，Dormann发推称攻击者可以修改任意Authenticode签名的文件来绕过MoTW安全告警，包括exe文件。

本文翻译自：https://www.bleepingcomputer.com/news/security/exploited-windows-zero-day-lets-javascript-files-bypass-security-warnings/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4iRZn9B5)

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