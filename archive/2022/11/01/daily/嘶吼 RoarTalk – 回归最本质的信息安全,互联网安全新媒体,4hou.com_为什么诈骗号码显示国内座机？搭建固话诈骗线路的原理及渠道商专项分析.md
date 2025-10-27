---
title: 为什么诈骗号码显示国内座机？搭建固话诈骗线路的原理及渠道商专项分析
url: https://www.4hou.com/posts/LBmp
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-01
fetch_date: 2025-10-03T21:22:30.906575
---

# 为什么诈骗号码显示国内座机？搭建固话诈骗线路的原理及渠道商专项分析

为什么诈骗号码显示国内座机？搭建固话诈骗线路的原理及渠道商专项分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 为什么诈骗号码显示国内座机？搭建固话诈骗线路的原理及渠道商专项分析

360反诈中心
[新闻](https://www.4hou.com/category/news)
2022-10-31 13:24:08

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)885259

收藏

导语：诈骗团伙是如何获取固话线路的呢？

![666.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666943600125018.png "1666943494189407.png")

近日，在复盘冒充客服注销贷款诈骗的案例时，从不少网友分享的经历描述来看，对于接到的诈骗电话为什么是固话这件事，可以说是“大大的疑问”。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666943601162702.png "1666943333412496.png")

甚至有人隔空喊话jc叔叔，隔着屏幕都能感受到，被诈骗电话骚扰的焦躁和无奈。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666943602242228.png "1666943385486052.png")

那么问题来了

为什么诈骗电话显示国内座机？

骗子改用座机了？

是不是可以顺藤摸瓜抓到这群人？

……

**案例重现**

上海黄女士接到自称某电商平台的客服电话，说黄女士的一款金融商品年利率不符合标准，将会影响她的个人征信，客服可以帮助她关闭相关功能。由于这个电话显示是本地电话号码，黄女士对客服身份深信不疑，按要求打开多个金融公众号APP，按步骤一一操作，结果将线上贷款20万转入了对方账户。

经调查，黄女士所接电话号码竟然关联到嘉定区外冈镇某村的一个出租房，一个多月前刚刚开通，同时开通的还有另外2个座机电话号码。经排查，相邻另一出租房内也有三个号码刚刚开通。经过循线追踪，最终将不法分子抓获，查获了语音网关、路由器、电话等作案设备18套。

原来，不法分子是通过网络寻找所谓的“高薪”兼职机会，在查询关于银行卡洗黑钱、出售手机卡和电话线路等电诈“黑灰产”的信息后，在网上搭识了境外诈骗团伙人员，收取了相关设备，并按照对方“遥控”指挥，租房布设设备，申请开通当地电话号码用于境外电话显号。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666943604201345.png "1666943419113206.png")

警方供图 架设“黑灰产”设备现场 来源：新民晚报

涉诈的“境外来电”穿上“本地来电”的外衣

这种行为极具伪装性、迷惑性和欺骗性

往往会降低用户的警惕性

让人难以辨别，极易上当受骗

有必要来一期专项分析，来说一说诈骗场景中使用的固定电话搭建原理及渠道商分析。

根据公安部相关报道，一些诈骗分子为逃避打击，转而使用本地固定电话号码进行作案。

涉案号码大多是企业固话，以及国内基础运营商推出的云语音企业固话专线，一些不法固话业务代理商受利益驱使，通过网络技术违规将其开办的固话线路转接给境外电信网络诈骗分子，从而使诈骗分子能够通过远程操控的方式拨打电话进行诈骗。首先，此类诈骗手法的关键环节

不法分子是如何获取固话线路的呢？

据掌握的情报，黑产渠道有“料商(贩卖数据的人)”在收卖固话线路；同时，受利益驱使，也有人以公司名义申请固定电话线路并有偿提供给不法分子。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666943604678160.png "1666943424142952.png")

使用固话进行诈骗背后的跑通逻辑有两种：搭建固定电话线路转接给诈骗人员、云语音企业固话（云呼叫中心）。

**固定电话转接线路**

从掌握的情报线索来看，固话搭建用到了IP电话交换机(IP-PBX)、语音网关、IP话机、语音客户端等设备，不法分子获取固化线路后，对接至语音网关，诈骗人员就可以通过PC、手机安装远控语音客户端，使用该固话线路拨打诈骗电话。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666943605620148.png "1666943461154623.png")**云语音企业固话专线**

目前一些平台推出了云固话语音专线，即由平台/代理商提供电话（境内固话、手机号、国际号码、400电话、95/96号码），并进行云端部署，买方/使用方使用云端类工具进行接听、呼叫。

以某平台提供的云呼叫中心服务为例，平台宣称可以提供一站式的云呼叫中心、号码和电话线路的即买即开即用的服务，仅需要基础的呼叫设备即可使用云呼叫中心服务，这种服务的便捷性，存在被不法利用的可能性。

平台合作商提供的号码类型，会有行业和地区的限制，比如：

普通固话：可用作外呼和呼入场景，不同城市地区会有不同的区号

400号码：是仅用作呼入场景的号码，被叫承担所有的来电接听费用。广泛用于多行业售前售后服务咨询方面。

95号码：属于是全网呼叫中心号码，在申请之前需要办理全网呼叫中心增值电信业务经营许可证。

虚拟手机号码：属于是全网呼叫中心号码，在申请之前需要办理全网呼叫中心增值电信业务经营许可证。

国际电话号码：全球100多个国家和地区的固话以及800号码。部分国家和地区需要当地的近3个月的物业账单证明以及地址。可单独申请呼全球的外呼线路。

以上可以看出，境外诈骗团伙是通过在境内招募下线，搭建固话网关设备，远控拨打诈骗电话，企图躲避打击。对于这类案件，要想顺藤摸瓜将藏匿在境外的诈骗团伙一网打尽，仍存在追踪打击难的问题。

对于此类冒充客服诈骗，单从来电号码判断已不再稳妥，可以结合常见的诈骗话术来甄别，比如：

注销校园贷，否则影响征信

银监会要求关闭\*\*白条/金条

可以帮助升级\*\*金融服务

可以帮助调低\*\*借款利息

可以帮助增加\*\*白条额度

工作人员误操作开通了会员业务

在平台购买的商品出现质量问题

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mulM5u52)

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

![](https://img.4hou.com/portraits/068e4092bab6e0b00b3c9e62609dd402.png)

# [360反诈中心](https://www.4hou.com/member/mx20)

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

[查看更多](https://www.4hou.com/member/mx20)

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