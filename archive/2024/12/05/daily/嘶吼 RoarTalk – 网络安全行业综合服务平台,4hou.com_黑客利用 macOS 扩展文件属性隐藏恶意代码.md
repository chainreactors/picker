---
title: 黑客利用 macOS 扩展文件属性隐藏恶意代码
url: https://www.4hou.com/posts/42Yg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-05
fetch_date: 2025-10-06T19:36:27.592896
---

# 黑客利用 macOS 扩展文件属性隐藏恶意代码

黑客利用 macOS 扩展文件属性隐藏恶意代码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用 macOS 扩展文件属性隐藏恶意代码

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-12-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)115324

收藏

导语：威胁分子将恶意代码隐藏在自定义文件元数据中，并使用诱饵 PDF 文档来帮助逃避检测。

黑客被发现正滥用 macOS 文件的扩展属性来传播一种新的木马，研究人员将其称为 RustyAttr。

威胁分子将恶意代码隐藏在自定义文件元数据中，并使用诱饵 PDF 文档来帮助逃避检测。这项新技术类似于 2020 年 Bundlore 广告软件将其有效负载隐藏在资源分支中以隐藏 macOS 有效负载的方式。安全研究人员在一些野外恶意软件样本中发现了它。

根据他们的分析，由于无法确认任何受害者，研究人员有一定把握将这些样本归因于朝鲜黑客拉扎勒斯。他们认为攻击者可能正在尝试一种新的恶意软件传递解决方案。

这种方法并不常见，现在已被证明可以有效地防止检测，因为 Virus Total 平台上的安全代理都没有标记恶意文件。

**在文件属性中隐藏代码**

macOS 扩展属性 (EA) 表示通常与文件和目录关联的隐藏元数据，这些元数据在 Finder 或终端中不直接可见，但可以使用“xattr”命令提取以显示、编辑或删除扩展属性。在 RustyAttr 攻击的情况下，EA 名称为“test”并包含 shell 脚本。

![ShellScript-macOS-xattr.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241114/1731555262178663.png "1731555017196894.png")

macOS 扩展属性内的 Shell 脚本

存储 EA 的恶意应用程序是使用 Tauri 框架构建的，该框架结合了可以调用 Rust 后端函数的 Web 前端（HTML、JavaScript）。当应用程序运行时，它会加载一个包含 JavaScript（“preload.js”）的网页，该网页从“测试”EA 中指示的位置获取内容，并将其发送到“run\_command”函数以执行 shell 脚本。

![preloadjs.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241114/1731555263191403.png "1731555060158403.png")

preload.js 的内容

为了在此过程中降低用户怀疑，某些示例会启动诱饵 PDF 文件或显示错误对话框。

![decoy.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241114/1731555264183724.png "1731555098664334.png")

诱饵 PDF 隐藏恶意后台活动

该 PDF 是从用于公共文件共享的 pCloud 实例获取的，其中还包含名称与加密货币投资主题相关的条目，这与 Lazarus 的目的和目标一致。

RustyAttr 应用程序 Group-IB 的少数样本发现，所有应用程序都通过了 Virus Total 的检测测试，并且应用程序是使用泄露的证书进行签名的，苹果已撤销该证书，但未经过公证。

![signed.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241114/1731555265198960.png "1731555192591051.png")

应用证书详细信息

Group-IB 无法检索和分析下一阶段的恶意软件，但发现临时服务器连接到 Lazarus 基础设施中的已知端点以尝试获取它。

![exec-flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241114/1731555266904028.png "1731555220670835.png")

执行流程

**尝试 macOS 规避**

Group-IB 报告的案例与 SentinelLabs 最近的另一份报告非常相似，该报告观察到朝鲜黑客 BlueNoroff 在 macOS 中尝试了类似但不同的规避技术。

BlueNoroff 使用以加密货币为主题的网络钓鱼来引诱目标下载经过签名和公证的恶意应用程序。

这些应用程序使用修改后的“Info.plist”文件来秘密触发与攻击者控制的域的恶意连接，从该域检索第二阶段有效负载。

目前尚不清楚这些活动是否相关，但不同的活动集群通常会使用相同的信息来了解如何有效地破坏 macOS 系统而不触发警报。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-use-macos-extended-file-attributes-to-hide-malicious-code/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?EbTrIqAq)

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