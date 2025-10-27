---
title: iOS 16.3发布，支持硬件安全密钥
url: https://www.4hou.com/posts/4KNV
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-01
fetch_date: 2025-10-04T05:18:50.084188
---

# iOS 16.3发布，支持硬件安全密钥

iOS 16.3发布，支持硬件安全密钥 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# iOS 16.3发布，支持硬件安全密钥

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-01-31 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)188493

收藏

导语：1月23日，苹果发布iOS 16.3，其中修复了多个安全补丁并引入了新的安全特征，包括支持使用物理安全密钥用于双因子认证、保护钓鱼攻击等。

**iOS 16.3发布**

1月23日，苹果发布iOS 16.3，其中修复了多个安全补丁并引入了新的安全特征，包括支持使用物理安全密钥用于双因子认证、保护钓鱼攻击等。具体包括：

支持用户使用硬件安全密钥登录APPLE ID；

支持HomePod（第二代）；

解决了墙纸在锁屏时变黑的问题；

修复了Home Lock Screen（主页锁屏）窗口小部件未能准确展示home APP状态的问题；

修复了Siri不能正常响应音乐请求的问题。

**支持硬件安全密钥**

2022年，苹果发布了硬件密钥安全特征，允许用户使用第三方硬件安全密钥增强双因子认证。硬件安全密钥是小的支持USB-C或NFC来连接MAC或iPhone的物理设备。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674556789188292.png "1674556789188292.png")

硬件安全密钥可以作为Apple ID的双因子认证的额外验证步骤来增强设备的安全性，而非使用6位的数字验证码。比如，攻击者常常创建窃取Apple ID凭证和用于双因子验证的一次性验证码的钓鱼攻击。但如果Apple ID被配置为使用安全密钥，那么即使钓鱼攻击可以窃取凭证，因为无法访问硬件安全密钥也无法成功登录用户Apple ID。

要在iOS设备上使用安全密钥，Apple需要两个密钥：一个平常携带使用，一个放置在家里或办公室作为备用。在iPhone上设置硬件安全密钥认证的步骤为：设置——点击Apple ID用户名——密码和安全——选择 add security key：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674556790834199.png "1674556737182543.png")

图 为iOS添加新的安全密钥

设置步骤完成后，在需要访问Apple ID时，就只需按下手机上的安全密钥就可以完成双因子认证，比如安卓应用、购物、登入其他设备。

BleepingComputer确认了该功能支持YubiKey 5 NFC、YubiKey 5C NFC和谷歌Titan。苹果也称适配YubiKey 5Ci 和 FEITAN ePass K9 NFC。

如果不想再使用硬件安全密钥，只需要在security key设置中点击移除所有安全密钥即可。安全密钥移除后，设备将自动使用6位的数字验证码。

更多关于iOS 16.3和iOS 硬件安全密钥的信息参见：

https://support.apple.com/en-us/HT213407

https://support.apple.com/en-us/HT213154

本文翻译自：https://www.bleepingcomputer.com/news/apple/apple-ios-163-arrives-with-support-for-hardware-security-keys/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1YLNVoWg)

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