---
title: 推特为私信功能加入端到端加密
url: https://www.4hou.com/posts/VZxO
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-19
fetch_date: 2025-10-03T23:10:50.742074
---

# 推特为私信功能加入端到端加密

推特为私信功能加入端到端加密 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 推特为私信功能加入端到端加密

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-11-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)182549

收藏

导语：​研究人员发现推特源码中为用户私信（direct messages）功能加入端到端加密（E2EE）支持。

研究人员发现推特源码中为用户私信（direct messages）功能加入端到端加密（E2EE）支持。

推特早在2018年就尝试了E2EE系统的原型——secret conversation，但是没有最终成为产品，并最终被放弃。

近日，研究人员Jane Manchun Wong在推特安卓版源码中新加入了一些内容，其中就包括加密密钥——"encryption keys"。从源码中的字符串来看，会话的加密密钥会生成一个数，如果这个数与接收者手机中的数一致，就可以保证端到端加密。

![tweet](https://img.4hou.com/uploads/ueditor/php/upload/image/20221117/1668663806152303.png)

Elon Musk回复了Jane Manchun Wong的推文，暗示该功能仍然开发中。

**为什么推特需要E2EE**

E2EE可以确保离开发送者的消息是加密形式存在的，加密的消息可以被接收端解密读取。因此，发送者和接收者需要使用加密密钥对来加密和解密消息的内容。

在大多数的E2EE实现中，发送者使用接收者数字签名的公钥来加密消息，接收者使用自己的私钥来解密。

在推特的E2EE实现中，wong提到了"conversation key"，所以推特可能采用了对称加密，即聊天中的双方使用相同的密钥来进行加密和解密。

![tweet](https://img.4hou.com/uploads/ueditor/php/upload/image/20221117/1668663807177102.png)

发送者的消息会转为不可直接读取内容的密文状态，并在传输过程中保持密文状态，因此互联网服务提供商、网络监听者、甚至推特都不能直接读取消息的明文内容。

如果推特在私信中引入了E2EE，那么用户会觉得其通信的安全和隐私得到了保证，包括推特平台被黑等特殊情况。比如，2020年7月，推特承认有黑客入侵了其雇员账户，并访问了管理员面板，可以读取36个名人的私信收件箱，并下载了其中7个私信收件箱的内容。

如果那时推特使用了E2EE功能，那么黑客下载的只是无法直接读取内容的密文，对用户不会造成影响。

其他使用E2EE的消息平台还有Signal、Threema、 WhatsApp、iMessage、Viber、Element/Matrix、 Tox、Keybase、 XMPP、Skype和Wire。

本文翻译自：https://www.bleepingcomputer.com/news/security/twitter-source-code-indicates-end-to-end-encrypted-dms-are-coming/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KC40IRF5)

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