---
title: 新攻击利用Windows安全绕过 0 day 漏洞投放恶意软件
url: https://www.4hou.com/posts/jJmB
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-29
fetch_date: 2025-10-03T23:56:32.861328
---

# 新攻击利用Windows安全绕过 0 day 漏洞投放恶意软件

新攻击利用Windows安全绕过 0 day 漏洞投放恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新攻击利用Windows安全绕过 0 day 漏洞投放恶意软件

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)150867

收藏

导语：新的网络钓鱼攻击利用Windows 0 day 漏洞投放Qbot恶意软件，而不显示Web标记安全警告。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669599936110922.png "1668901007109222.png")

新的网络钓鱼攻击利用Windows 0 day 漏洞投放Qbot恶意软件，而不显示Web标记安全警告。

当文件从互联网或电子邮件附件等不受信任的远程位置下载时，Windows会给文件添加一个名为“Web标记”（Mark of the Web）的特殊属性。

这个Web标记（MoTW）是一个备用数据流，含有关于该文件的信息，比如表明文件来源的URL安全区域、引用者以及下载URL。

当用户试图打开具有MoTW属性的文件时，Windows会显示安全警告，询问用户是否确定希望打开该文件。

来自Windows的警告显示：“虽然来自互联网的文件可能很有用，但这种文件类型可能会对你的电脑造成潜在的危害。如果你不信任来源，请不要打开该软件。”

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669599937122892.png "1668901019124206.png")

图1. Windows Web标记安全警告（来源：BleepingComputer）

上个月惠普威胁情报团队报告，一起网络钓鱼攻击使用JavaScript文件分发Magniber勒索软件。

这些JavaScript文件与网站上使用的那些文件不一样，而是扩展名为“.JS”的独立文件，可使用Windows脚本主机（wscript.exe）来执行。

ANALYGENCE的高级漏洞分析师Will DormannD在分析这些文件后发现，威胁分子使用了一个新的Windows 0 day 漏洞，该漏洞阻止了Web标记安全警告的显示。

想要利用该漏洞，可以使用base64编码的嵌入式签名块对JS文件（或其他类型的文件）进行签名，微软的这篇支持文章有详细描述（https://learn.microsoft.com/en-us/previous-versions/tn-archive/ee176795(v=technet.10)?redirectedfrom=MSDN）。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669599938191831.png "1668901035569548.png")

图2. 用于安装Magniber勒索软件的JavaScript文件（来源：BleepingComputer）

然而，当带有这种畸形签名的恶意文件被打开时，Windows自动允许该程序运行，而不是被微软SmartScreen标记出来、显示MoTW安全警告。

**QBot恶意软件活动利用Windows 0 day 漏洞**

最近的QBot恶意网络钓鱼活动已经分发了含有ISO镜像的由密码保护的ZIP压缩包。这些ISO镜像含有用于安装恶意软件的Windows快捷方式和DLL。

ISO镜像被用来分发恶意软件，因为Windows没有正确地将“Web标记”传播到里面的文件中，从而允许含有的文件绕过Windows安全警告。

作为微软2022年11月补丁的一部分，微软已发布了修复这个错误的安全更新，促使MoTW标记传播到打开的ISO镜像中的所有文件，从而修复了这个安全绕过漏洞。

在安全研究人员ProxyLife发现的一起新的QBot网络钓鱼活动中，威胁分子通过分发带有畸形签名的JS文件，转而利用这个Windows Web标记 0 day 漏洞。

这起新的网络钓鱼活动始于一封电子邮件，邮件中附有指向所谓文件的链接和文件的密码。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669599938145079.png "1668901049100800.png")

图3. 附有下载恶意压缩包的链接的网络钓鱼电子邮件（来源：BleepingComputer）

点击链接后，会下载一个受密码保护的ZIP压缩包，压缩包含有另一个ZIP文件和一个IMG文件。

在Windows 10及更新版本中，双击IMG或ISO等磁盘镜像文件后，操作系统会自动将其挂载为新的盘符。

该IMG文件含有一个.js文件（‘WW.js’）、一个文本文件（‘data.txt’）和另一个文件夹，该文件夹含有一个重命名为.tmp文件（‘likeblence .tmp’）的DLL文件，如下所示。值得一提的是，文件名会随着每起活动而变，所以不应该被认为是静态的。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669599939176504.png "1668901062501806.png")

图4. 挂载的IMG文件（来源：BleepingComputer）

该JS文件含有VB脚本，脚本会读取data.txt文件，这个文件含有‘vR32’字符串，并将内容附加到shellexecute命令的参数后面，以加载‘port/resemblance.tmp’DLL文件。在这封特定的邮件中，重构的命令如下：

regSvR32 port\\resemblance.tmp

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669599940142604.png "1668901085194172.png")

图5. JS文件带有畸形签名，可以利用Windows  0 day 漏洞（来源：BleepingComputer）

由于JS文件来自互联网，在Windows中启动它会显示Web标记安全警告。

然而，从上面的JS脚本图像中可以看到，它使用Magniber勒索软件活动中使用的同一个畸形密钥来签名，以利用Windows 0 day 漏洞。

这个畸形的签名允许JS脚本运行和加载QBot恶意软件，而不显示来自Windows的任何安全警告，如下面的启动进程所示。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669599940242396.png "1668901102173122.png")

图6. 启动QBot DLL的Regsvr32.exe（来源：BleepingComputer）

经过一段短暂的时间后，恶意软件加载程序将把QBot DLL注入到合法的Windows进程中，以逃避检测，比如wermgr.exe或AtBroker.exe。

微软从10月份以来就知道了这个 0 day 漏洞，鉴于其他恶意软件活动在利用该漏洞，但愿该漏洞会在2022年12月补丁安全更新中得到修复。

**QBot恶意软件**

QBot又叫Qakbot，是一种Windows恶意软件，最初只是一种银行木马，但已演变为恶意软件释放器。

一旦加载，该恶意软件将在后台悄悄运行，同时窃取电子邮件用于其他网络钓鱼攻击或安装另外的攻击载荷，比如Brute Ratel、Cobalt Strike及其他恶意软件。

安装Brute Ratel和Cobalt Strike后利用工具包通常会导致更具破坏性的攻击，比如数据盗窃和勒索软件攻击。

在过去，Egregor和Prolock勒索软件团伙与QBot分发团伙狼狈为奸，伺机访问公司网络。最近，继QBot感染之后，网络上出现了Black Basta勒索软件攻击。

本文翻译自：https://www.bleepingcomputer.com/news/security/new-attacks-use-windows-security-bypass-zero-day-to-drop-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tBN2yKe6)

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