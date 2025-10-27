---
title: 使用Shodan图像揪出勒索软件团伙
url: https://www.4hou.com/posts/QLoL
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-24
fetch_date: 2025-10-04T07:56:25.026063
---

# 使用Shodan图像揪出勒索软件团伙

使用Shodan图像揪出勒索软件团伙 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 使用Shodan图像揪出勒索软件团伙

布加迪
[新闻](https://www.4hou.com/category/news)
2023-02-23 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)153661

收藏

导语：本文侧重介绍了Shodan如何帮助揭露支持勒索软件团伙的一些基础设施。

我们在这篇博文中将侧重介绍Shodan如何帮助揭露支持勒索软件团伙的一些基础设施。

Shodan是一种抓取banner信息的搜索引擎，可以收集直接连接到互联网的所有设备的信息。如果某个设备直接连接到互联网上，Shodan就会查询其各种公开可用的信息。被编入索引的设备类型形形色色：从小型台式机到核电站，不一而足。Shodan还可以扫描端口，并暴露漏洞，是不是非常酷？

我们之前深入探讨了勒索软件生态系统的方方面面以及这条食物链中的一大批网络犯罪分子。我将介绍其中一些攻击多简单、攻击者在怎样伺机下手，我们可以在哪里揪出他们。然后你可以利用这些信息，积极运用到防御中。

**为什么我们能做到这一点？**

勒索软件团伙并不关心你的数据、安全信息及事件管理（SIEM）、防火墙或花哨的端点检测和响应（EDR）；正因为如此，他们会选择阻力最小、带来一丝成功机会的那条路径。你通常可以将他们的技术与MITRE ATT&CK对应起来，以便了解攻击者在如何思考和操作。

众所周知，勒索软件遵循一些标准程序，具体因团伙和活动而异。我们可以通过从Conti团伙内部泄露的一些信息证实这一点：内部加盟组织在GitHub上的大批信息当中共享了一份内部培训手册（https://github.com/ForbiddenProgrammer/conti-pentester-guide-leak），谁都可以查看。

**搜寻**

我决定选择不法分子用来下载第一阶段载荷的已知二进制文件：

https://lolbas-project.github.io/

然后把这些信息馈送给Shodan。

我们可以获取攻击者使用的已知LOLBIN二进制文件，比如：

' ' '

bitsadmin

PowerShell

cmd

File Transfer protocol (FTP)

Nslookup

' ' '

然后利用Shodan的强大功能，就像勒索软件加盟组织的做法一样。正如对手在互联网上搜索受害者一样，我们可以利用这个基础设施对付他们，寻找对方的不安全平台。

下面你可以看到10000个暴露的虚拟网络计算（VNC）实例，它们未经过身份验证。对于威胁分子来说，这是10000个潜在的发财机会。然而，一个人无法独自攻击所有这些实例，于是威胁分子借助自动化，最终导致垮台。

![1.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676343718108320.jpeg "1676343718108320.jpeg")

图1

利用Shodan图像的功能，并将其与勒索软件加盟组织自动感染的工作相结合，我们得到了表明它们如何在运作的清晰图像:

PowerShell：

![2.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676343727113711.jpeg "1676343727113711.jpeg")

图2

bitsadmin：

![3.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676343738846398.jpeg "1676343738846398.jpeg")

图3

Shodan有众多软件包；这些软件包允许最终用户访问不同的搜索过滤器，比如搜索当前的CVE。我在使用的查询中作用了“bitsadmin”和“powershell”这两个单词，没有利用Shodan过滤器。

现在不妨简单解释一下我们看到的是什么，如果不太清楚的话。

这些是暴露的VNC实例，没有经过身份验证，谁都可以连接它们并发送命令。我搜遍了Shodan图像，寻找有人执行PowerShell或bitsadmin的情况。我这么做是由于不是每个运行的开放VNC实例都是Windows，这里是给勒索软件团伙布置一个陷阱，他们最终向任何会监听的糟糕设备发送攻击载荷。

**GandCrab活动**

PowerShell & Bitsadmin

GandCrab（又叫REvil）多次更名，其多个加盟组织已在全球被逮捕。

下面举一个例子，勒索软件团伙试图用PowerShell、bitsadmin和FTP感染pfSense路由器。

颜色细述：

红色表示第一次执行

蓝色表示命令和域

黄色表示第二次执行

绿色表示恶意软件（勒索软件）企图执行

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676343751688822.png "1676343751688822.png")

图4

我们可以看到每个命令都以“r”开头，这是由于攻击载荷是面向Windows计算机；键盘输入是win+r，以打开run（运行）对话框，然后执行命令。

尝试使用cmd.exe下载以启动PowerShell

尝试使用cmd.exe下载以启动bitsadmin

尝试使用cmd.exe下载以修改防火墙，并允许FTP试图使用cmd.exe下载以启动FTP

在这每一次尝试下载后，他们会尝试尽快执行恶意软件（这在代表第二次执行的黄色部分中高亮显示）。

**快速归因**

不妨通过搜索.exe名称和IP地址快速将该恶意软件归因于这个团伙，因为我们可以查看历史数据；幸好，面向大规模活动。

搜索IP，我们找到了这里：

https://urlhaus.abuse.ch/host/92.63.197.153/

这表明他们与GandCrab/REvil勒索软件团伙有关。

我们还可以在这里（https://app.any.run/tasks/9b6642ee-6ec9-437c-b411-2cc529dcc5fb/）找到沙盒报告。

下面我们可以看到一起非常相似的活动，但IP略有不同：

![5.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676343764700537.jpeg "1676343764700537.jpeg")

图5

我们可以看到，这更多地与挖币有关，但仍然是GandCrab勒索软件团伙：

这起活动现在已变成了使用各种域名：

![6.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676343776953088.jpeg "1676343776953088.jpeg")

图6

**身份不明的“隐形”活动**

我在做一些另外的研究时无意中看到了Nslookup的截图。我发现各种屏幕截图表明向一系列不同的IP发出Nslookup请求，有一个相似之处。

这起活动会先确定是否可以连接到VNC端口，然后它将使用vncport.hacked.com的标准域名向外部IPv4发出请求（VNC的实际端口，请看下面截图）。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676343789112695.png "1676343789112695.png")

图7

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676343802270380.png "1676343802270380.png")

图8

**防御**

我们如何才能防御这些威胁？最简单、最容易的方法就是深入了解贵企业的对外网络。Huntress通过External Recon帮助合作伙伴做到这一点。如果你知道攻击者盯上了什么目标，也了解自己的攻击面，就能更好地防御威胁。

考虑除了开放某些端口有没有其他替代方法。如果出于业务目的必须暴露端口，那么你可以部署哪些安全层来挫败对手？考虑所有选择，另辟蹊径，攻击者当然会这么做。我们始终推荐采取基本的网络卫生和安全控制措施，但是像攻击者一样思考、通过这个视角看待自己的网络总是大有助益。

利用我们截图中的信息并将它们映射到MITRE可能是一种有趣的沙盘演练。

本文翻译自：https://www.huntress.com/blog/using-shodan-images-to-hunt-down-ransomware-groups如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OEOGf3o8)

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