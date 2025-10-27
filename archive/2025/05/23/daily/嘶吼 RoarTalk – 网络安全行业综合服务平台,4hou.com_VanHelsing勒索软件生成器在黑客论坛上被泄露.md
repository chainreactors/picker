---
title: VanHelsing勒索软件生成器在黑客论坛上被泄露
url: https://www.4hou.com/posts/W19Q
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-23
fetch_date: 2025-10-06T22:27:16.034416
---

# VanHelsing勒索软件生成器在黑客论坛上被泄露

VanHelsing勒索软件生成器在黑客论坛上被泄露 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# VanHelsing勒索软件生成器在黑客论坛上被泄露

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-05-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)52166

收藏

导语：这次泄露并不是勒索软件构建器或加密器源代码第一次在网上泄露，这使得新的勒索软件组织或个人威胁者能够迅速进行攻击。

VanHelsing勒索软件即服务运营团队在一名旧开发者试图在RAMP网络犯罪论坛上出售其联属面板、数据泄露博客和Windows加密器生成器的源代码后，公布了这些代码。

VanHelsing是2025年3月推出的一项RaaS业务，旨在提升针对Windows、Linux、BSD、ARM和ESXi系统的能力。

自那时以来，这次行动已经取得了一些成功，Ransomware.live 表示勒索软件集团已知的受害者有八个。

**VanHelsing源代码在网络犯罪论坛上泄露**

本周，一个化名为“th30c0der”的人试图以1万美元的价格出售VanHelsing附属面板和数据泄露网站的源代码，以及Windows和Linux加密器的构建器。

th30c0der在RAMP论坛上发帖称：“出售vanhelsing勒索软件源代码：包括TOR密钥+管理web面板+聊天+文件服务器+博客包括数据库一切。”

![builder-for-sale.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747880714187197.png "1747797910107455.png")

那个试图出售VanHelsing源代码的程序员

VanHelsing的运营商决定跳过卖家，自己发布源代码，并声称该代码是他们的老开发者之一，以此试图欺骗人们。

”VanHelsing操作员在RAMP上表示正在发布旧的源代码，并将很快推出新的改进版本的储物柜（VanHelsing 2.0）。

![vanhelsing-leaking-source-code.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747880716367367.png "1747797959110243.png")

VanHelsin RaaS在RAMP上发布源代码

然而，与30c0der所说的相比，这些泄露的数据是不完整的，因为它不包括Linux构建器或任何数据库，这将对执法部门和网络安全研究人员更有帮助。

有媒体已经获得了泄露的源代码，并确认其中包含Windows加密器的合法构建器以及附属面板和数据泄漏站点的源代码。

![folders.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747880717556575.png "1747798009170913.png")

泄露的源代码

构建器的源代码有点乱，Visual Studio项目文件位于“Release”文件夹中，该文件夹通常用于保存编译后的二进制文件和构建工件。

当完成时，使用VanHelsing构建器将需要一些工作，因为它连接回正在运行31.222.238[的附属面板。]208，接收用于构建过程的数据。

![builder-c2.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747880718242700.png "1747798061185184.png")

构建器使用的Common.h头文件

但是，泄漏还包括附属面板的源代码，附属面板托管api.php端点，因此威胁者可以修改代码或运行他们自己版本的该面板以使构建器工作。

该归档文件还包含Windows加密器的源代码，可用于创建独立构建、解密器和加载器。

![encrypter-source-code.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747880719156256.png "1747798144119463.png")

VanHelsing加密器源代码

泄露的源代码还显示，威胁者试图构建一个MBR锁柜，该锁柜将用显示锁定消息的自定义引导加载程序替换主引导记录。

![mbrlocker.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747880721603763.png "1747798189430503.png")

VanHelsing MBRLocker源代码

这次泄露并不是勒索软件构建器或加密器源代码第一次在网上泄露，这使得新的勒索软件组织或个人威胁者能够迅速进行攻击。

2021年6月，Babuk勒索软件构建器泄露，允许任何人为Windows和VMware ESXi创建加密和解密器。Babuk漏洞已经成为对VMware ESXi服务器进行攻击的最广泛使用的构建器之一。

2022年3月，Conti勒索软件遭遇数据泄露，其源代码也在网上泄露。其他威胁者很快在他们自己的攻击中使用了这个源代码。

2022年9月，一名声称心怀不满的开发人员泄露了该团队的构建器，导致LockBit勒索软件操作遭到破坏。直到今天，这种方法也被其他威胁者广泛使用。

文章翻译自：https://www.bleepingcomputer.com/news/security/vanhelsing-ransomware-builder-leaked-on-hacking-forum/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?UnPASM0E)

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