---
title: SoumniBot 恶意软件利用 Android 漏洞来逃避检测
url: https://www.4hou.com/posts/qpOp
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-09
fetch_date: 2025-10-06T17:14:27.727481
---

# SoumniBot 恶意软件利用 Android 漏洞来逃避检测

SoumniBot 恶意软件利用 Android 漏洞来逃避检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# SoumniBot 恶意软件利用 Android 漏洞来逃避检测

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-05-08 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)182317

收藏

导语：该方法使 SoumniBot 能够规避 Android 手机中的标准安全措施并执行信息窃取操作。

一种名为“SoumniBot”的新 Android 银行恶意软件通过利用 Android 清单提取和解析过程中的弱点，使用了新的混淆方法。

该方法使 SoumniBot 能够规避 Android 手机中的标准安全措施并执行信息窃取操作。

研究人员发现并分析后提供了该恶意软件利用 Android 例程解析和提取 APK 清单的方法的技术细节。

**欺骗 Android 的解析器**

清单文件（“AndroidManifest.xml”）位于每个应用程序的根目录中，包含有关组件（服务、广播接收器、内容提供程序）、权限和应用程序数据的详细信息。

虽然恶意 APK 可以使用 Zimperium 的各种压缩技巧来愚弄安全工具并逃避分析，但分析师发现 SoumniBot 使用了三种不同的方法来绕过解析器检查，其中涉及操纵清单文件的压缩和大小。

首先，SoumniBot 在解压 APK 的清单文件时使用无效的压缩值，该值与负责该角色的 Android“libziparchive”库预期的标准值（0 或 8）不同。

Android APK 解析器不会将这些值视为不可接受，而是默认将数据识别为由于错误而未压缩，从而允许 APK 绕过安全检查并继续在设备上执行。

![extraction.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240418/1713423245273017.jpg "1713423153476748.jpg")

从 APK 中提取清单文件

第二种方法涉及错误报告 APK 中清单文件的大小，提供大于实际数字的值。

由于该文件在上一步中已被标记为未压缩，因此直接从存档中复制该文件，并用垃圾“覆盖”数据填充差异。

虽然这些额外的数据不会直接损害设备，但它在混淆代码分析工具方面发挥着至关重要的作用。

![wrong-size.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240418/1713423245827041.png "1713423190168768.png")

报告错误的文件大小

第三种规避技术是在清单文件中使用非常长的字符串作为 XML 命名空间的名称，这使得自动分析工具很难检查到它们，而自动分析工具通常缺乏足够的内存来处理它们。

![long-string.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240418/1713423247102330.png "1713423216122027.png")

清单中的长字符串

Android 官方分析实用程序 APK 分析器无法使用上述规避方法处理文件。

**SoumniBot 威胁**

启动后，SoumniBot 从硬编码服务器地址请求其配置参数，并发送受感染设备的分析信息，包括编号、运营商等。

接下来，它会启动一个恶意服务，如果停止，该服务每 16 分钟就会重新启动一次，并每 15 秒传输一次从受害者那里窃取的数据。

泄露的详细信息包括 IP 地址、联系人列表、帐户详细信息、短信、照片、视频和网上银行数字证书。数据泄露由恶意软件通过 MQTT 服务器接收的命令控制，这些命令还对以下功能进行排序：

**·**删除现有联系人或添加新联系人

**·**发送短信（转发）

**·**设置铃声音量

**·**打开或关闭静音模式

**·**打开或关闭设备上的调试模式

目前尚不清楚 SoumniBot 如何到达设备，但方法可能有所不同，从通过第三方 Android 商店和不安全网站分发到使用受信任存储库中的恶意代码更新合法应用程序。

SoumniBot 主要针对韩国用户，与许多恶意 Android 应用程序一样，它在安装后隐藏其图标，使其更难以删除。其实，它在后台仍然活跃，并从受害者处上传数据。

文章翻译自：https://www.bleepingcomputer.com/news/security/soumnibot-malware-exploits-android-bugs-to-evade-detection/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?P2Vt3P2H)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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