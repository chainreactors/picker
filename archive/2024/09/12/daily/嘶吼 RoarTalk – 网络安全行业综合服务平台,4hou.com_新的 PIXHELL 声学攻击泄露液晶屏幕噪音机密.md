---
title: 新的 PIXHELL 声学攻击泄露液晶屏幕噪音机密
url: https://www.4hou.com/posts/kgrx
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-12
fetch_date: 2025-10-06T18:22:54.314004
---

# 新的 PIXHELL 声学攻击泄露液晶屏幕噪音机密

新的 PIXHELL 声学攻击泄露液晶屏幕噪音机密 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 PIXHELL 声学攻击泄露液晶屏幕噪音机密

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-09-11 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)90055

收藏

导语：通过改变液晶屏上的像素图案，调制后的数据会通过液晶屏传输，从而改变设备组件发出的声音。

一种名为“PIXHELL”的新型声学攻击可以通过连接到的 LCD 显示器，无需扬声器而泄露物理隔离和音频隔离系统中的机密。

在 PIXHELL 攻击中，恶意软件会调制 LCD 屏幕上的像素模式，以在 0-22 kHz 的频率范围内产生噪声，并在这些声波中携带编码信号，这些信号可以被附近的设备（例如智能手机）捕获。

![fig-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240911/1726020712307716.jpg "1726019794140007.jpg")

PIXHELL 攻击设置

研究人员的测试表明，数据泄露的最大距离为 2 米，数据速率达到 20 比特每秒。

虽然这对于实现大文件传输来说太慢，但实时键盘记录和窃取可能包含密码或其他信息的小文本文件仍然是可能的。

**隐蔽音频通道**

PIXHELL 由 Mordechai Guri 博士开发，他因对从隔离环境中泄露数据的方法进行广泛研究而闻名。就在上周，这位研究人员发表了另一篇关于一种新型侧信道攻击的论文，这种攻击被称为“RAMBO”，用于攻击的隔离内存总线辐射，它可以通过从设备的 RAM 组件产生电子辐射来窃取隔离环境中的数据。

PIXHELL 攻击方法利用了 LCD 屏幕因线圈噪音、电容器噪声或设备无法物理消除的固有振动而产生的意外声发射。

使用特制的恶意软件，攻击者可以使用以下调制方案将加密密钥或击键等敏感数据编码为声音信号：

**·**开关键控 (OOK)：通过打开和关闭声音对数据进行编码。

**·**频移键控 (FSK)：通过在不同频率之间切换对数据进行编码。

**·**幅移键控 (ASK)：通过改变声音的幅度（音量）对数据进行编码。

![fig-2.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240911/1726020713561341.png "1726019910504516.png")

调制不同频率的声音信号

接下来，通过改变液晶屏上的像素图案，调制后的数据会通过液晶屏传输，从而改变设备组件发出的声音。

笔记本电脑或智能手机等恶意或受感染设备附近的麦克风可以拾取声音信号，随后可能将其传输给攻击者进行解调。

![fig-3.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240911/1726020715691029.png "1726019943121426.png")

附近麦克风接收到的声学信号的频谱图

值得注意的是，PIXHELL 可以在涉及多个信号源和单个接收者的环境中执行，因此如果这些系统被恶意软件感染，则可以同时从多个隔离系统中捕获秘密。

PIXHELL 恶意软件发出的声音频率通常在 0 - 22 kHz 频率范围内，人类几乎听不到。相比之下，人类通常能听到 20Hz 至 20kHz 频率范围内的声音，而普通成年人的上限通常在 15-17kHz 左右。

同时，攻击中使用的像素图案对用户来说是低亮度的或不可见的，这使得攻击特别隐蔽。

**应对策略**

可以实施多种防御措施来抵御 PIXHELL 和其他类型的声学侧信道攻击。在高度关键的环境中，出于谨慎考虑，应完全禁止在某些区域使用携带麦克风的设备。干扰或噪声生成也是一种解决方案，即引入背景噪声来干扰声学信号并增加信噪比 (SNR)，使攻击变得不可行。

安全研究人员还建议使用摄像头监控屏幕缓冲区，以检测与系统正常运行不匹配的异常像素模式。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-pixhell-acoustic-attack-leaks-secrets-from-lcd-screen-noise/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tlc8QO39)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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