---
title: 苹果为iCloud引入端到端加密实现高级数据保护
url: https://www.4hou.com/posts/q8By
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-13
fetch_date: 2025-10-04T01:16:42.732531
---

# 苹果为iCloud引入端到端加密实现高级数据保护

苹果为iCloud引入端到端加密实现高级数据保护 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 苹果为iCloud引入端到端加密实现高级数据保护

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-12-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)228726

收藏

导语：​苹果在iCloud中引入基于端到端加密的高级数据保护功能。

苹果在iCloud中引入基于端到端加密的高级数据保护功能。![Advanced Data Protection for iCloud](https://www.bleepstatic.com/images/news/u/1109292/2022/Advanced%20Data%20Protection%20for%20iCloud.png)

图 iCloud高级数据保护功能

12月7日，苹果为iCloud引入高级数据保护功能，该功能使用端到端加密来保护敏感iCloud数据，包括备份、图片、笔记等内容。苹果称，从iOS 16.2、iPadOS 16.2、macOS 13.1系统开始，用户可以选择高级数据保护功能来保护大部分的iCloud数据。

苹果系统为iCloud提供2种数据保护功能：标准数据保护和高级数据保护。

**标准数据保护：**标准数据保护是iCloud账户的默认安全设置。iCloud中数据是加密的，加密密钥保存在苹果数据中心，苹果可以帮助用户进行数据恢复，只有特定数据是端到端加密的。

**高级数据保护：**高级数据保护是iCloud的可选数据安全设置功能，可以通过最高等级的云数据安全保护。如果用户选择高级数据保护功能，只有拥有加密密钥的被信任的设备才能够访问iCloud数据，这一功能是通过端到端加密实现的。高级数据保护功能保护的数据包括iCloud 备份、相册、笔记等。

在端到端加密中，只有Apple ID登录的被信任的设备可以解密加密的数据。包括苹果公司在内的其他用户都无法访问端到端加密的数据，即使云端数据泄露，也无法访问。只有用户自己才可以恢复数据，可以用设备密码、恢复联系人、恢复密钥等进行恢复。

对于使用该安全特征的用户，高级数据保护可以确保大多数iCloud数据的安全，即使在数据泄露的情况下也可以确保加密的云数据智能在用户的信任设备上解密。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221208/1670482381710250.png "1670482381710250.png")

使用端到端加密保护的数据类型包括设备和消息备份、iCloud Drive、相册、提醒、Safari书签、语音留言等。iCloud邮箱、联系人、日历数据并不会被加密，因为需要与其他邮箱、联系人、日历系统进行通信。

目前，参与苹果beta software项目的美国用户已可以试用高级数据保护功能，其他用户预计本月底可以使用该功能。其他国家和地区的用户预计2023年初可以使用该功能。

此外，苹果还引入了2个新的安全特征：iMessage Contact Key Verification（联系人密钥验证）和Apple ID安全密钥。

联系人密钥验证可以使iMessage用户验证另外一段用户的身份，确保iMessage的另一端是用户想要会话的联系人。如果有攻击者将攻击设备加入会话来监听加密的通信信道系统会自动预警。

Apple ID安全密钥使得苹果客户在设置Apple ID账户的过程中需要一个物理安全密钥才能完成登录过程。该特征适用于名人、记者、政府工作人员等在线账户面临持续威胁的用户。

更多高级数据保护功能的细节参见：https://support.apple.com/en-us/HT202303#advanced

本文翻译自：https://www.bleepingcomputer.com/news/apple/apple-rolls-out-end-to-end-encryption-for-icloud-backups/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?kOMP5hqg)

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