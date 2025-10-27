---
title: 一种从未见过的恶意软件感染了成百上千的Linux和Windows设备
url: https://www.4hou.com/posts/r76w
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-04
fetch_date: 2025-10-04T02:58:51.670279
---

# 一种从未见过的恶意软件感染了成百上千的Linux和Windows设备

一种从未见过的恶意软件感染了成百上千的Linux和Windows设备 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 一种从未见过的恶意软件感染了成百上千的Linux和Windows设备

布加迪
[新闻](https://www.4hou.com/category/news)
2023-01-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)161366

收藏

导语：小型办公室路由器？FreeBSD设备？企业服务器？Chaos统统感染这些系统。

![p1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664521175478114.jpeg "1664521175478114.jpeg")

研究人员近日披露了一种从未见过的跨平台恶意软件，这种恶意软件已经感染了一系列广泛的Linux和Windows设备，包括小型办公室路由器、FreeBSD设备和大型企业服务器。

安全公司Lumen的研究部门Black Lotus Labs（黑莲花实验室）称该恶意软件为Chaos，这个名称在恶意软件使用的函数名、证书和文件名中一再出现。直到4月16日当第一批控制服务器投入实际使用时，Chaos才浮出水面。从6月到7月中旬，研究人员发现了数百个独特的IP地址，这些IP地址代表受Chaos攻击的设备。最近几个月，用于感染新设备的登台（staging）服务器如雨后春笋般涌现，从5月的39台增加到8月的93台。截至周二，这个数字已达到了111台。

Black Lotus观察到了企业服务器和嵌入式Linux设备与这些登台服务器的交互，包括欧洲的一台托管GitLab实例的企业服务器。外面的独特样本数量超过100个。

Black Lotus Labs的研究人员在周三上午的一篇博文中写道，Chaos恶意软件的威力源于几个因素。首先，它被设计成可以在多个架构上运行，除了Windows和Linux操作系统外，还包括ARM、英特尔（i386）、MIPS和PowerPC。其次，与Emotet等利用垃圾邮件来传播和蔓延的大规模勒索软件传播僵尸网络不同，Chaos通过已知的CVE以及蛮力破解的密码和窃取的SSH密钥来传播。

CVE指用于跟踪特定漏洞的机制。周三的报告只提到了少数几个CVE漏洞，包括影响华为销售的防火墙的CVE-2017-17215和CVE-2022-30525，以及F5销售的负载均衡系统、防火墙和网络检测设备中极其严重的CVE-2022-1388漏洞。使用密码蛮力破解和窃取密钥的SSH感染也让Chaos可以在受感染网络内从一台计算机传播到另一台计算机。

Chaos还有众多功能，包括枚举连接到受感染网络的所有设备，运行让攻击者可以执行命令的远程shell，以及加载额外的模块。Black Lotus Labs的研究人员表示，加上能够在如此广泛的设备上运行，这些功能让该公司怀疑Chaos是网络犯罪分子的杰作，他们在蓄意构建一个受感染设备组成的网络，利用它进行初始访问、DDoS攻击和挖掘加密货币。

Black Lotus Labs认为Chaos是Kaiji的一个分支，Kaiji是一种僵尸网络软件，面向基于Linux的AMD和i386服务器，用于发动DDoS攻击。自渐成气候以来，Chaos已获得了大批新功能，包括针对新架构的模块、在Windows上运行的功能以及通过漏洞利用和SSH密钥收集进行传播的能力。

受感染的IP地址表明，Chaos感染主要集中在欧洲，北美、南美和亚太地区也有感染现象。

![p2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664521191152546.png "1664521191152546.png")

图1

Black Lotus Labs的研究人员写道：

在9月的前几周，我们的Chaos主机模拟系统收到了多个针对大约20多家组织的域名或IP的DDoS命令。我们使用自己的全球遥测数据，从我们收到的攻击命令发现了多起时间范围、IP和端口相一致的DDoS攻击。攻击类型通常是跨多个端口利用UDP和TCP/SYN的多途径攻击，攻击流量常常在数日内增加。攻击的实体包括游戏、金融服务、技术、媒体、娱乐以及托管等行业的组织。我们甚至观察到针对DDoS即服务提供商和加密货币挖掘交易所的攻击。总的来说，这些目标遍布欧洲中东非洲、亚太和北美。

一家游戏公司通过端口30120受到了UDP、TCP和SYN混合攻击。从9月1日到9月5日，该组织收到的流量超过了正常流量。分析攻击之前和整个攻击期间的流量后发现，潮水般的流量通过大约12000个不同的IP发送到端口30120，不过部分流量可能表明存在IP欺骗。

![p3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664521201779173.png "1664521201779173.png")

图2

有几个目标包括DDoS即服务提供商。其中一个自称是首屈一指的IP DDoS租用平台或服务，提供CAPTCHA绕过和“独特”的传输层DDoS功能。8月中旬，流量大幅上升，大约是前30天最高记录的四倍。随后，9月1日出现了一个更大的高峰，是正常流量的六倍多。

![p4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664521211808498.png "1664521211808498.png")

图3. DDoS即服务组织入站攻击流量（来源：Black Lotus Labs）

为了防止Chaos感染，人们可以做的两件最重要的事情是，确保所有路由器、服务器和其他设备打上全面的补丁，并尽可能使用强密码和基于fido2的多因素身份验证。提醒所有小型办公室路由器的拥有者：大多数路由器恶意软件在重启后都无法存活下来。考虑差不多每周重启一次设备。使用SSH的用户应该始终使用加密密钥进行身份验证。

本文翻译自：https://arstechnica.com/information-technology/2022/09/never-before-seen-malware-has-infected-hundreds-of-linux-and-windows-devices/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?WjPwjiZn)

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