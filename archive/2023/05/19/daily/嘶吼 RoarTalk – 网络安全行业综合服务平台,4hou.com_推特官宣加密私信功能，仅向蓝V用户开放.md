---
title: 推特官宣加密私信功能，仅向蓝V用户开放
url: https://www.4hou.com/posts/yAwz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-19
fetch_date: 2025-10-04T11:36:53.387763
---

# 推特官宣加密私信功能，仅向蓝V用户开放

推特官宣加密私信功能，仅向蓝V用户开放 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 推特官宣加密私信功能，仅向蓝V用户开放

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-05-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)137458

收藏

导语：​推特推出加密私信功能，但仅向蓝V用户开放。

推特推出加密私信功能，但仅向蓝V用户开放。

推特近日推出基于端到端加密的加密私信功能，允许推特用户向平台其他用户发送端到端加密（End-to-end encryption，E2EE）的消息。

**E2EE**

E2EE使用公私钥对来对互联网上发送的信息进行加密，只有发送者和接收者才可以读取信息的内容。加密私钥保存在发送者设备上，并不与其他人共享。加密公钥会分享给想要发送加密数据的用户。私钥只保存在本地接收者设备上，并不会保存在其他任何地方，比如APP的服务器。因此，即使有人拦截了该加密的私信消息，在没有解密密钥的情况下也无法读取。

**推特加密私信功能**

去年11月，研究人员Jane Manchun Wong发现推特安卓版源码中暗示实现了E2EE。半年后，推特官宣推特iOS和安卓版本实现了加密消息功能。根据公告内容，通过设备生成的私钥和中心化提供的公钥，推特实现了一种非对称的加密方案。公钥是用户在新设备或浏览器上登录时自动生成的，而私钥不会离开设备，也不会与推特进行通信。除了公私钥对，还会有一个会话密钥用于加密消息的内容。

目前尚未有公开的关于该加密算法的技术细节，但是推特承诺将在2023年开源E2EE的实现，并发布白皮书。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230515/1684154244138785.png "1684154185190819.png")

图 马斯克推特

**仅向蓝V用户开放，且存在限制**

目前，该功能仅向蓝V用户开放。消息的发送方和接收方都需要是蓝V用户或经过认证的机构才可以使用加密私信功能。

可使用该功能的用户聊天界面会出现一个按钮，用户可以选择是否发送加密的私信消息。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230515/1684154245120451.png "1684154209800147.png")

图 加密私信功能按钮

用户也可以从加密私信功能切换到普通的私信模式，具体如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230515/1684154244190633.png "1684154244190633.png")

图 加密私信功能与普通私信模式切换

其他推特用户不会有使用加密私信功能的选项，其默认的是标准的非加密通信。

此外，推特对于加密私信功能还有一些限制，比如仅支持文本和链接，不允许新设备加入现有加密会话，每个用户最多只允许10个注册设备。

推特称私钥的安全性对于保护E2EE消息系统安全是非常重要的，因此会一直保存在设备上。如果攻击者窃取了该密钥，攻击者可以用它来解密所有该设备上发送和接收的消息。

本文翻译自：https://www.bleepingcomputer.com/news/security/twitter-rolls-out-encrypted-dms-but-only-for-paying-accounts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2z98DHDN)

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