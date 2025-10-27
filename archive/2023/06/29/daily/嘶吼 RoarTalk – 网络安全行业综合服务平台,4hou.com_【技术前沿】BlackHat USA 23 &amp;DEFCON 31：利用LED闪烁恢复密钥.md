---
title: 【技术前沿】BlackHat USA 23 &amp;DEFCON 31：利用LED闪烁恢复密钥
url: https://www.4hou.com/posts/NK78
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-29
fetch_date: 2025-10-04T11:46:21.652428
---

# 【技术前沿】BlackHat USA 23 &amp;DEFCON 31：利用LED闪烁恢复密钥

【技术前沿】BlackHat USA 23 &amp;DEFCON 31：利用LED闪烁恢复密钥 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术前沿】BlackHat USA 23 &DEFCON 31：利用LED闪烁恢复密钥

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-06-28 11:50:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)127895

收藏

导语：以色列研究人员提出一种利用设备LED闪烁来恢复ECDSA密钥。

研究人员提出一种利用设备LED闪烁来恢复ECDSA密钥。

CPU执行的密码学计算会改变设备的电量消耗，设备的电源LED亮度与电量消耗直接相关，因此会影响设备电源LED的亮度。根据这一现象，以色列本·古里安大学研究人员提出一种基于视频分析的密码分析方法，通过分析设备的电源LED录像来恢复设备的密钥。相关研究成果将在8月举办的BlackHat USA 23 & DEFCON 31上展示。

密码分析需要较高的取样率。用LED的视频片段，攻击者可以利用滚动快门来增加LED的颜色度量数。60k的取样率可以提供攻击智能手机、智能卡等IoT设备所需的取样率。

研究人员应用该方法执行了两种侧信道分析时间攻击：直接攻击和间接攻击，并成功恢复了智能卡的256位ECDSA密钥和三星Galaxy S8的378位SIKE 密钥。PoC视频参见：<https://www.youtube.com/embed/ITqBKRZvS3Y>

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687840143613075.png "1687840000122916.png")

图 直接攻击：利用LED闪烁恢复ECDSA密钥

![hertzbleed-setup-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230627/1687840145160595.png)

图 间接攻击：利用外接设备获取电源LED信息

与其他密码分析方法相比，基于视频的密码分析方法利用了有漏洞的加密算法和电源LED来恢复密钥，更加容易利用。因为攻击者在攻击过程中只需要常见的传感器或视频摄像头，无需专用设备。而攻击的本质是有漏洞的加密算法库，而非电源LED灯。但电源LED提供了漏洞利用的可视化基础设施。

研究人员通过实验分析发现5家厂商的6款智能卡读卡器受到直接攻击的影响，三星Galaxy S8受到间接攻击的影响。

此外，研究人员指出没有电源LED的设备也受到该攻击的影响。因为，攻击者可以使用连接的外围设备电源LED来发起间接攻击。关于如何预防和应对这两种侧信道攻击，研究人员建议使用最新的密码学算法库。

研究论文下载地址：https://eprint.iacr.org/2023/923

本文翻译自：https://www.nassiben.com/video-based-crypta如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?kO7ZEAEi)

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