---
title: 谷歌公开安卓私有计算核心PCC技术细节
url: https://www.4hou.com/posts/MBGm
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-17
fetch_date: 2025-10-04T01:44:06.399035
---

# 谷歌公开安卓私有计算核心PCC技术细节

谷歌公开安卓私有计算核心PCC技术细节 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 谷歌公开安卓私有计算核心PCC技术细节

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-12-16 11:33:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)165073

收藏

导语：近日，谷歌公开了安卓PCC工作原理的技术细节，介绍了如何在受保护的设备上对敏感用户数据进行数据。

近日，谷歌公开了安卓PCC工作原理的技术细节，介绍了如何在受保护的设备上对敏感用户数据进行数据。

谷歌在安卓12系统中引入了私有计算核心（Private Compute Core，PCC）功能。PCC是操作系统中一个安全、独立、可信的环境，来自传感器、GPS、麦克风、摄像头和屏幕的数据在PCC中保存和处理，为用户提供机器学习过程中的特征。比如'Live Caption'特征使用麦克风来进行语音识别，'Now Playing'特征可以识别歌曲，'Smart Reply'特征可以在消息APP中建议回复内容。

**PCC工作原理**

受保护的沙箱中处理的操作系统级数据和相关数据可以通过API系统向安卓设备提供智能特征，但应用和远程服务器是无法访问的，因此保护了用户隐私。

PCC与其他APP的隔离是通过安卓框架API，包括所有PCC的数据输入和数据输出，以及操作系统安装过程中授予的权限。只有系统更新才能修改这些权限，因此没有APP或远程服务器连接能够修改该权限。

谷歌称，PCC使得恶意软件难以利用操作系统。PCC设计的目的就是保护用户数据隐私，并不是专门针对恶意软件的安全保护措施。所有PCC enclave中发生的用户数据处理都只在设备中。如果机器学习特征需要设备外数据的交互，谷歌PCC就可以实现加密交换。

![Functional diagram of PCC](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/diagram-pcc.png)

图 PCC功能图

私有计算服务（Private Compute Services，PCS）是提供PCC与云之间隐私保护链路的一系列服务。目前，谷歌也开源了PCS，源码参见：<https://github.com/google/private-compute-services>

谷歌称为了改善基于使用统计数据的PCC，其使用联邦学习和分析计算来监控使用私有信息提取的机器学习模型的性能。联邦分析和学习使得谷歌可以在没有中心化数据收集、在用户设备上本地使用原始的数据分析计算来训练机器学习模型。因为PCC也是安卓操作系统的一部分，所有PCC的机器学习特征也是可更新的。

但PCC也在用户的控制范围中。比如，将传感器设置为关，就不会在操作系统中生成和发送数据了，包括PCC。此外，用户还可以在系统设置中限制与PCC进行数据共享：

![Android setting to disable ML features](https://www.bleepstatic.com/images/news/u/1220909/Software/android-setting.jpg)

图 安卓系统中的禁用机器学习特征设置

更多关于PCC的技术细节参见谷歌发布的技术文章：https://arxiv.org/pdf/2209.10317.pdf

本文翻译自：https://www.bleepingcomputer.com/news/security/google-how-android-s-private-compute-core-protects-your-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BshRPGQe)

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