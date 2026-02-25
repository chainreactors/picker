---
title: 新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备
url: https://www.4hou.com/posts/YZ2W
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-24
fetch_date: 2026-02-25T04:13:39.527822
---

# 新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备

新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10878

收藏

导语：研究人员并未详细披露该恶意软件的传播方式，但指出 ZeroDayRAT 是一套完整的移动设备入侵工具集。

一款名为 ZeroDayRAT 的新型商用手机间谍软件平台，正在 Telegram 上向网络犯罪分子进行推广，其宣称可对受感染的安卓和 iOS 设备实现完全远程控制。

该恶意软件为购买者提供功能齐全的管理面板，据称支持安卓 5 至 16 版本，以及最高 iOS 26 最新版本。

研究人员表示，ZeroDayRAT 不仅窃取数据，还能实施实时监控与金融盗窃。管理面板可展示受感染设备信息，包括机型、系统版本、电池状态、SIM 卡信息、所属国家及设备锁定状态。

![图片10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260211/1770799746386933.png "1770799094140685.png")

控制台概览

恶意软件能够记录应用使用情况、行为时间线、短信往来记录，并为控制者生成汇总信息。

面板中的其他追踪模块可显示设备收到的所有通知，以及设备上已登录的账号（含邮箱、用户 ID），可能被用于暴力破解与凭证填充攻击。

若获取 GPS 权限，该恶意软件还可实时追踪受害者位置，在谷歌地图上显示当前坐标与完整历史轨迹。

![图片11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260211/1770799750500157.png "1770799127137139.png")

实时追踪受害者

除被动数据记录外，ZeroDayRAT 还支持主动操控：可开启前后摄像头、麦克风获取实时音视频流，或录制屏幕以窃取更多敏感信息。

![图片12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260211/1770799752165988.png "1770799162131763.png")

访问摄像头和麦克风输入

此外，在获得短信权限后，恶意软件可截取接收到的一次性验证码（OTP），实现双因素认证绕过，并能以受害者设备发送短信。

该恶意软件开发者还集成了键盘记录模块，可捕获密码、手势、屏幕解锁图案等用户输入信息。

在金融盗窃方面，软件内置加密货币窃取模块。研究人员发现，该组件会启动钱包应用扫描，检测 MetaMask、Trust Wallet、币安、Coinbase 等钱包，记录钱包地址与余额，并尝试剪贴板地址注入，将用户复制的钱包地址替换为攻击者控制的地址。

银行窃取模块则针对网上银行应用、Google Pay、PhonePe 等统一支付接口平台，以及 Apple Pay、PayPal 等支付服务，通过伪造覆盖界面窃取账号凭证。

![图片13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260211/1770799754548180.png "1770799192508538.png")

加密货币和银行信息窃取模块

研究人员并未详细披露该恶意软件的传播方式，但指出 ZeroDayRAT 是一套完整的移动设备入侵工具集。并警告员工设备一旦沦陷，可能引发企业级数据泄露。

对个人用户而言，遭受 ZeroDayRAT 入侵将导致隐私全面泄露，并可能造成直接经济损失。

安全建议提醒用户，仅从官方应用商店（安卓 Google Play、iOS App Store）安装来源可信的应用；高风险用户可在 iOS 开启锁定模式，在安卓启用高级保护功能。

文章来源自：https://www.bleepingcomputer.com/news/security/zerodayrat-malware-grants-full-access-to-android-ios-devices/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?YopEPM6l)

#### 你可能感兴趣的

* [![]()

  恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)
* [![]()

  Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)
* [![]()

  新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备](https://www.4hou.com/posts/YZ2W)
* [![]()

  假冒的7-Zip官网暗藏代理木马传播恶意安装包](https://www.4hou.com/posts/W1Zn)
* [![]()

  新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)
* [![]()

  AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)
  2026-02-25 12:00:00
* [Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)
  2026-02-25 11:59:00
* [新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备](https://www.4hou.com/posts/YZ2W)
  2026-02-24 12:00:00
* [假冒的7-Zip官网暗藏代理木马传播恶意安装包](https://www.4hou.com/posts/W1Zn)
  2026-02-24 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)

  胡金鱼
* [Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)

  胡金鱼
* [新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备](https://www.4hou.com/posts/YZ2W)

  胡金鱼
* [假冒的7-Zip官网暗藏代理木马传播恶意安装包](https://www.4hou.com/posts/W1Zn)

  胡金鱼
* [新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)

  胡金鱼
* [AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)

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