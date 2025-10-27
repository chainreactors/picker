---
title: 个人电脑容易因辐射而被盗取数据
url: https://www.4hou.com/posts/LBED
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-07
fetch_date: 2025-10-04T03:14:36.695989
---

# 个人电脑容易因辐射而被盗取数据

个人电脑容易因辐射而被盗取数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 个人电脑容易因辐射而被盗取数据

~阳光~
[新闻](https://www.4hou.com/category/news)
2023-01-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)179222

收藏

导语：一种名为COVID-bit的新型攻击方法会利用电磁波将数据从与互联网隔离的系统中传输到两米（6.5英尺）距离处，然后在那里被接收器捕获。

从隔离设备发出的信息也可以被附近的智能手机或笔记本电脑接收到，即使两者之间有一堵墙相隔。

COVID-bit攻击是由本-古里安大学的研究员Mordechai Guri开发的，他设计了多种方法来隐蔽地从封闭的系统内窃取敏感数据。他在之前也发现了"ETHERLED"和 "SATAn "攻击。

**最初研究的方案**

物理隔离系统通常用于高风险环境中使用的计算机，如能源基础设施、政府和武器控制单位，因此它们出于安全原因会与公共互联网和其他网络进行隔离。

为了成功地攻击这类系统，内部人员或者入侵者必须首先通过物理访问被封锁的设备或在目标计算机上植入定制的恶意软件。

尽管这听起来很不切实际，甚至有些牵强，但这样的攻击已经发生了，比如伊朗纳坦兹铀浓缩设施的Stuxnet蠕虫，感染美国军事基地的Agent.BTZ，以及从封闭的政府网络环境中收集信息长达五年之久的Remsec后门。

为了在COVID-bit攻击中传输数据，研究人员创建了一个恶意软件程序，该程序会以特定的方式调节CPU负载和核心频率，使该计算机的电源在低频段（0 - 48 kHz）上发出电磁辐射。

该研究人员说，在从AC-DC和DC-DC的转换中，电源会以特定频率开启或关闭MOSFET开关元件从而产生一个方波，并且该电磁波还会携带原始数据的有效载荷。

接收器可以是一台笔记本电脑或是一个智能手机，通过使用连接到3.5毫米音频插孔的环形天线，就可以很容易地以耳机/耳麦的形式获取数据。

智能手机可以捕获传输的信息，通过使用降噪过滤器，解调原始数据，并最终解码信息。

**测试结果**

Guri测试了三台台式电脑、一台笔记本电脑和一台单板电脑（Raspberry Pi 3）的各种比特率，在电脑和Raspberry Pi上保持零比特错误率达200bps，笔记本电脑则达100bps。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221212/1670846218622807.png "1670846134438921.png")

笔记本电脑的表现更差，因为它们的节能配置文件和更节能的CPU内核导致其PSU不能产生足够强的信号。

台式电脑可以达到500bps的传输速率，误码率在0.01%和0.8%之间，1000bps的传输速率，误码率高达1.78%，但是我们仍然还可以接受。

由于树莓派的电源较弱，并且它与机器的距离受到限制，而随着测试探头的进一步移动，笔记本电脑的信噪比也会变得更差。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221212/1670846219149888.png "1670846173137134.png")

在测试最大传输速率（1000bps）时，一个10KB的文件将会在80秒内传输完毕，一个4096位的RSA加密密钥可以在4秒或10分钟内传输完毕，而一个小时的键盘记录的原始数据将在20秒内发送到接收器。

还可以进行实时键盘记录，即使信息的传输率低至每秒5比特。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221212/1670846220240548.png "1670846198128548.png")

研究人员还对虚拟机进行了实验，发现虚拟机管理程序的程序中断会造成2分贝至8分贝的信号衰减。

**防止COVID-bit攻击**

对COVID-bit攻击最有效的防御措施是严格限制对有气闸保护的设备的访问，防止攻击者安装攻击所需的恶意软件。然而，这并不能保护你免受内部人员的威胁。

对于这种攻击，研究人员建议监控CPU核心的使用情况，并检测与计算机预期行为不相符的可疑加载模式。

然而，这种对策有一个缺点，那就是有很多误报情况，而且还增加了数据处理的开销，降低了性能。另一种对策是将CPU的核心频率锁定在一个特定的数值上，使信号的产生更加困难，虽然这并不能完全阻止它。这种方法的缺点是降低了处理器的性能或造成了高能量的浪费，这取决于所选择的锁定的频率。

本文翻译自：https://www.bleepingcomputer.com/news/security/air-gapped-pcs-vulnerable-to-data-theft-via-power-supply-radiation/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2F89848Z)

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