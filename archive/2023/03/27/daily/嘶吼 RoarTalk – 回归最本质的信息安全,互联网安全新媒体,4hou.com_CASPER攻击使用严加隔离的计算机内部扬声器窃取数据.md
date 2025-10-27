---
title: CASPER攻击使用严加隔离的计算机内部扬声器窃取数据
url: https://www.4hou.com/posts/gXBY
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-27
fetch_date: 2025-10-04T10:45:45.140171
---

# CASPER攻击使用严加隔离的计算机内部扬声器窃取数据

CASPER攻击使用严加隔离的计算机内部扬声器窃取数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# CASPER攻击使用严加隔离的计算机内部扬声器窃取数据

布加迪
[新闻](https://www.4hou.com/category/news)
2023-03-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)127946

收藏

导语：韩国首尔大学网络安全学院的研究人员近日介绍了一种名为CASPER的新型隐蔽通道攻击，这种攻击能以每秒20比特的速度将数据从严加隔离的计算机泄漏给附近的智能手机。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679639958884493.png "1678697050206058.png")

韩国首尔大学网络安全学院的研究人员近日介绍了一种名为CASPER的新型隐蔽通道攻击，这种攻击能以每秒20比特的速度将数据从严加隔离的计算机泄漏给附近的智能手机。

CASPER攻击利用目标计算机内部的扬声器作为数据传输通道，以传输人耳听不到的高频音频，并将二进制或摩尔斯电码传送到最远1.5米开外的麦克风。

接收端麦克风可以位于攻击者口袋内录制音频的智能手机中，也可以位于同一房间的笔记本电脑中。

研究人员之前已经开发出了利用外部扬声器的类似攻击方法。然而，在关键环境中使用的严加隔离、使用独立网络的系统（比如政府网络、能源基础设施和武器控制系统）不太可能有外部扬声器。

另一方面，提供音频反馈（比如开机蜂鸣声）的内部扬声器仍然被认为必不可少，因此它们通常存在，从而使它们成为攻击者眼里更好的选择。

**感染目标**

与几乎所有针对使用独立网络的计算机的秘密通道攻击一样，可以实际访问目标的非授权员工或隐秘入侵者必须先用恶意软件感染目标。

虽然这种情况似乎不切实际甚至遥不可及，但过去有人多次成功实施了这类攻击，其中有名的例子包括Stuxnet蠕虫攻击伊朗在纳坦兹的铀浓缩设施、Agent.BTZ恶意软件感染了一个美国军事基地，以及Remsec模块化后门从严加隔离的政府网络偷偷收集信息长达五年之久。

恶意软件可以自动枚举目标的文件系统，找到与硬编码列表匹配的文件或文件类型，并企图泄露文件。

现实中更有可能发生的是，它可以记录击键内容，这更适合这种缓慢的数据传输速率。

恶意软件会将要从目标中窃取的数据编码成二进制或摩尔斯电码，并使用频率调制通过内部扬声器来传输，从而获得在17 kHz至20 kHz范围内难以察觉的超声波。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679639960114116.png "1678697066140815.png")

图1. CASPER攻击示意图 （图片来源：韩国首尔大学）

**试验结果**

研究人员使用一台基于Linux（Ubuntu 20.04）的计算机作为目标，使用三星Galaxy Z Flip 3作为接收器，对描述的模型进行了试验，并运行一款采样频率高达20 kHz的基础记录器应用程序。

在摩尔斯电码试验中，研究人员将每比特长度设置为100毫秒，并使用18 kHz作为点、使用19 kHz作为破折号。智能手机放在50厘米开外的地方，能够解码所发送的单词“covert”（意为“隐蔽”）。

在二进制数据试验中，每比特长度设置为50毫秒，以18 kHz的频率传输0、以19 kHz的频率传输1。50毫秒的开始/结束位也以17 kHz的频率传输，以表明新消息的开始。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679639961453980.png "1678697085211541.png")

图2. 通过生成的声音频率传输的数据 （图片来源：韩国首尔大学）

从进行的测试来看，接收器的最大距离为1.5 米（4.9英尺），使用100 毫秒的每比特长度。

但从试验的总体结果来看，每比特长度对误码率有影响。当每比特长度为50毫秒时，可以达到20比特/秒的最大可靠传输比特率。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230324/1679639970794223.png "1678697104191627.png")

图3. 误码率计算（图片来源：韩国首尔大学）

按此数据传输速率计算，恶意软件可以在大约3秒内传输一个典型的8个字符长度的密码，并在100秒内传输一个2048位RSA密钥。

任何超过此值的数据（比如10 KB 的小文件）都需要一个多小时才能从严加隔离的系统中泄露出去，即使在理想的条件下、传输过程中没有出现中断。

韩国首尔大学声称：“与使用光学方法或电磁方法的其他隐蔽通道攻击技术相比，我们的方法传输数据的速度较慢，因为通过声音传输数据的速度有限。”

解决低数据速率的方法是改变多路同时传输的频带；然而，内部扬声器只能生成单一频段的声音，因此这种攻击实际上受到了限制。

研究人员分享了抵御CASPER攻击的方法，最简单的方法是从关键任务计算机上移除内部扬声器。

如果这么做不现实，防御者可部署高通滤波器，将所有生成的频率保持在可听见的声谱内，从而阻止超声波传输。

如果你对针对严加隔离的系统的其他隐蔽通道攻击感兴趣，不妨参阅COVID-bit（https://www.bleepingcomputer.com/news/security/air-gapped-pcs-vulnerable-to-data-theft-via-power-supply-radiation/），它使用电源装置（PSU）生成传输数据的电磁波。

类似攻击的其他例子还有ETHERLED，它依靠目标网卡的LED灯来传输摩尔斯电码信号，以及 SATAn，它使用SATA电缆作为无线天线。

本文翻译自：https://www.bleepingcomputer.com/news/security/casper-attack-steals-data-using-air-gapped-computers-internal-speaker/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?hmbYN5yX)

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