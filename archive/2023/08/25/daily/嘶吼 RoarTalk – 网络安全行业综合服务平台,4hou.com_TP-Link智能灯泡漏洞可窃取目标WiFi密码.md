---
title: TP-Link智能灯泡漏洞可窃取目标WiFi密码
url: https://www.4hou.com/posts/poKp
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-25
fetch_date: 2025-10-04T11:59:34.750445
---

# TP-Link智能灯泡漏洞可窃取目标WiFi密码

TP-Link智能灯泡漏洞可窃取目标WiFi密码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# TP-Link智能灯泡漏洞可窃取目标WiFi密码

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-08-24 11:44:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)115158

收藏

导语：​研究人员在TP-Link Tapo智能灯泡和APP中发现4个安全漏洞，可用于窃取目标WiFi密码。

研究人员在TP-Link Tapo智能灯泡和APP中发现4个安全漏洞，可用于窃取目标WiFi密码。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230822/1692672706137633.png "1692672645148213.png")

TP-Link Tapo L530E是一款销量很高的智能灯泡，TP-link Tapo APP是一款智能设备管理应用程序，谷歌应用商店下载量超过1000万。来自意大利和英国的研究人员分析了这款智能灯泡和控制应用程序的安全性，并在其中发现了4个安全漏洞，攻击者利用这些漏洞可以窃取目标的WiFi密码。漏洞影响数百万智能物联网设备，使得用户数据传输和认证存在风险。

**智能灯泡漏洞**

第一个漏洞是Tapo L503E智能灯泡中的认证不当引发的，攻击者可以在密钥交换过程中假冒设备，漏洞CVSS评分8.8分。攻击者利用该漏洞可以提取Tapo用户密码并操纵Tapo设备。

第二个漏洞是硬编码的校验和共享秘密引发的，漏洞CVSS评分7.6分。攻击者可以通过暴力破解或反编译Tapo应用程序的方式获取校验和共享秘密。

第三个漏洞是对称加密过程中缺乏随机性引发的，该漏洞使得所使用的加密方案可预测。

第四个漏洞是未对接收的消息的新鲜性进行检查，session key（会话密钥）的有效性达到了24小时，攻击者在会话密钥有效期内可以发起重放攻击。

**攻击场景**

对用户影响最大的攻击场景是利用漏洞1和漏洞2来假冒灯泡，并提取Tapo的用户账户信息。然后攻击者可以访问Tapo app，并提取受害者的WiFi SSID和密码，并访问所有连接到该WiFi网络的设备。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230822/1692672707171294.png "1692672666107513.png")

图 假冒攻击图

要实现假冒攻击，需要设备处于设置模式。但攻击者也可以通过去除灯泡授权的方式迫使用户重新对灯泡进行设置。

另外一个攻击类型是中间人攻击（MITM）。利用漏洞1和拦截和操作APP和灯泡之间的通信，然后获取最后用户数据交换的RSA加密密钥。

中间人攻击还可以在WiFi设置阶段对未配置的Tapo设备发起，通过桥接2个不同网络、路由发现消息等方式，最终提取base64编码的Tapo的密码、SSID、WiFi密码等。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230822/1692672705847536.png "1692672705847536.png")

图 MITM攻击图

最后，利用漏洞4发现重放攻击，重返之前嗅探到了可以改变灯泡功能的消息。

**漏洞补丁和修复**

研究人员已将相关漏洞提交给了TP-Link，厂商也告知研究人员已经修复了相关漏洞。但论文中未给出详细的漏洞和补丁信息，以及受影响的版本。

论文下载地址：https://arxiv.org/pdf/2308.09019.pdf

本文翻译自：https://www.bleepingcomputer.com/news/security/tp-link-smart-bulbs-can-let-hackers-steal-your-wifi-password/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Ug4bJVe1)

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