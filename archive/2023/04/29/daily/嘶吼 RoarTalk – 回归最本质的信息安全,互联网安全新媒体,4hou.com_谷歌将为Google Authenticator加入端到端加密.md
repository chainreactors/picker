---
title: 谷歌将为Google Authenticator加入端到端加密
url: https://www.4hou.com/posts/YYv9
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-29
fetch_date: 2025-10-04T11:31:32.879258
---

# 谷歌将为Google Authenticator加入端到端加密

谷歌将为Google Authenticator加入端到端加密 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 谷歌将为Google Authenticator加入端到端加密

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-04-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)138374

收藏

导语：谷歌将为Google Authenticator加入端到端加密。

谷歌将为Google Authenticator加入端到端加密。

Google Authenticator（身份验证器）是谷歌推出的基于时间的一次性密码(Time-based One-time Password)，只需要在手机上安装该APP，就可以生成一个随着时间变化的一次性密码，用于帐户验证。Google Authenticator是一款非常主流的身份认证应用，下载量超过1亿。

**2FA token云端备份**

4月25日，Google Authenticator完成了将2FA token（双因子验证口令）备份到云端的功能。该功能允许用户将Google Authenticator 2FA tokens与谷歌账户进行同步，用户可以通过多种设备来访问2FA token，如果移动设备丢失或受到破坏仍然可以起到备份作用。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230427/1682579810125646.png "1682579769756624.png")

**无端到端加密**

Google Authenticator云同步功能发布后，来自Mysk的安全研究人员在推特指出数据在上传到谷歌服务器时未进行端到端加密。研究人员分析了APP同步过程中的网络流量，发现流量并不是端到端加密的。也就是说谷歌是可以看到同步的信息的。目前尚未实现只有上传的用户才能够访问这些信息。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230427/1682579809201639.png "1682579809201639.png")

图 Mysk推文

端到端加密（E2EE）是数据在传输和存储到另一个设备之前使用只有用户（所有者）知道的密码对其进行加密。因为数据是加密的，因此无法被其他人访问。但Google Authenticator不提供端到端加密，保存在谷歌服务器上的数据是有可能被其他非授权的用户访问的，比如数据泄露。

每个2FA二维码中包含一个秘密或seed，用于生成一次性口令。如果其他用户知道了seed，那么就可以生成相同的一次性口令，以绕过2FA的保护。

**谷歌将引入E2EE**

谷歌了解到用户对Google Authenticator中未使用端到端加密的担忧后，表示将在之后的版本中加入端到端加密。谷歌称考虑到端到端加密可能会导致用户在忘记口令后导致其数据不能被访问，因此其在产品中使用该功能非常慎重。目前，谷歌已在Chrome浏览器中引入了端到端加密，未来计划在Google Authenticator中引入端到端加密。

本文翻译自：https://www.bleepingcomputer.com/news/google/google-authenticator-now-backs-up-your-2fa-codes-to-the-cloud/
https://www.bleepingcomputer.com/news/google/google-will-add-end-to-end-encryption-to-google-authenticator/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?32vhdRyG)

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