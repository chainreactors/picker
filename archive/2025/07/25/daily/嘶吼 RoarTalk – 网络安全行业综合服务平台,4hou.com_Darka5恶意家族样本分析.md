---
title: Darka5恶意家族样本分析
url: https://www.4hou.com/posts/jBmR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-25
fetch_date: 2025-10-06T23:27:10.815173
---

# Darka5恶意家族样本分析

Darka5恶意家族样本分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Darka5恶意家族样本分析

企业资讯
[技术](https://www.4hou.com/category/technology)
2025-07-24 14:04:33

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)82296

收藏

导语：本报告将详细剖析darka5恶意家族样本的关键特征，涵盖其攻击向量、下载器行为、数据加密差异、通信流量混淆以及特殊的隐蔽手段，旨在为网络安全专家和防御者提供深入的见解，以更好地理解和应对这一新兴安全威胁。

近期，广州大学、国家工业信息安全发展研究中心与杭州海康威视数字技术股份有限公司安全研究团队在研究过程中捕获到一例具有显著特征的病毒样本，该样本具有独特的攻击手法和高度的隐蔽性，根据其在下载服务器上的文件命名，该样本被命名为darka5。经过对该样本的深入分析，研究团队发现其不仅运用了先进的加密技术，还具备复杂的网络通信混淆手段，使得追踪和防御工作面临巨大挑战。

本报告将详细剖析darka5恶意家族样本的关键特征，涵盖其攻击向量、下载器行为、数据加密差异、通信流量混淆以及特殊的隐蔽手段，旨在为网络安全专家和防御者提供深入的见解，以更好地理解和应对这一新兴安全威胁。

**一 样本分析**

**（一）攻击向量**

darka5是一个通过IoT设备命令执行漏洞进行传播的恶意样本，研究团队通过物联网威胁诱捕系统成功捕获该样本，其投递方式较为复杂，通过分析捕获所得攻击日志可知，攻击者首先通过echo的方式实现样本文件的拼接，然后写入一个微型下载器，最终通过该下载器进行攻击样本的下载和执行。攻击载荷如下图所示：

![640.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324218284319.png "1753323822242011.png")

攻击源IP为109.205.213.198，经公开信息追溯，该IP最早的活跃时间为2023年12月27日：

![640 (1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324219497175.png "1753323846378435.png")

**（二）下载器分析**

基于对攻击向量的分析，研究团队成功还原出大小为1980字节的ELF文件，该文件未使用libc，推测其使用汇编语言编写。完整的函数列表如下：

![640 (2).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324220203290.png "1753323888113456.png")

在主函数中，该程序尝试通过HTTP协议从远程服务器（http://2.57.122.83:80/darka5）下载文件到本地的/dev/.j目录下：

![640 (3).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324221359835.png "1753323923105808.png")

![640 (4).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324222113603.png "1753323934185552.png")

**（三）数据加密差异**

通过分析，darka5样本采用了ChaCha20加密算法，该样本基于Mirai修改而来，与2023年360 Netlab曾分析过的Rimasuta样本相似，同样引入了ChaCha20算法，但仅限于常量字符串加密。

ChaCha20算法所使用的Key和Nonce硬编码在常量段：

![640 (5).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324223112993.png "1753323966787955.png")

在Key实际使用时，会先经过异或后再传入ChaCha20加密函数：

![640 (6).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324224208656.png "1753323993154378.png")

解密后，该样本的常量字符串表如下：

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324224164439.png "1753324039200120.png")

**（四）通信流量混淆**

在darka5样本中，对于Key的异或手段同样用在了与C2通信的过程中。当解析来自C2的攻击指令时，该样本会将流量内容与0x82异或操作，以还原出原始的攻击者指令：

![640 (7).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324225166885.png "1753324063151320.png")

**（五）特殊的隐蔽手段**

通过对darka5样本进行深入分析发现，该样本使用了较为特殊的C2连接方式。darka5样本具有一个统一的函数入口，用来返回即将要连接的C2服务器。该函数使用了加密常量表中存储的域名：iwant.coin、chongwa.bazar、packetsyikes.lib、qq.com、git.hbmc.net，以及端口：8338、9944、3177。在连接C2服务器的函数时，会根据连接失败的次数随机选择不同的域名：

![640 (8).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324226546701.png "1753324102220853.png")

![640 (9).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324227165450.png "1753324113113621.png")

除根据域名重试次数和随机数选择域名之外，darka5样本在解析域名的方式上亦呈现出与以往常见病毒的不同之处。通过逆向分析发现该样本在选择五个域名之中的任意一个之后，还会随机选择一个硬编码的DNS服务器来进行域名解析，以此提高域名解析的成功率。可能选择的DNS服务器列表如下：

![640 (10).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324228377078.png "1753324135899824.png")

在经过上述C2服务器地址解析过程后，如若C2服务器解析或者连接失败，darka5样本将自动增加重试计数，并影响下一次C2服务器的解析逻辑，此过程将持续进行，直至成功解析并连接到C2服务器为止。

在这种C2服务器解析的逻辑机制中，涉及多个具有不确定的变量因素，包括重试失败的次数、随机选取的域名结果以及随机选择的DNS服务器，这些变量因素均会对最终解析到的C2地址产生影响。同时，在这种随机选择和重试的机制下，C2服务器信息的隐蔽性得到了显著提升。darka5样本能够成功迷惑各类沙箱服务，使其在有限的分析时间内提取到错误的C2服务器信息。

**二 总结**

darka5样本运用多种技术手段，使其在与常规Mirai样本相比，展现出明显的差异性。无论是常量表使用ChaCha20算法加密，还是控制指令混淆，或是特殊的C2解析方式，这些特征都极大地增加了样本分析的难度，使得现有的自动化分析流程难以从中提取出有价值的信息。此外，根据捕获到的攻击向量分析，该病毒开发者显然擅长追踪和利用新漏洞，对此病毒家族后续可能造成的更大影响与危害，需予以高度警觉。

**三 loc**

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250724/1753324229125465.png "1753324213685021.png")

注：该成果源自广州大学牵头的国家重点研发计划项目（2022YFB3104100）中的课题四“高质量攻击数据诱捕与分析关键技术及系统”（2022YFB3104104），旨在构建面向大规模物联网攻击威胁的主动防护能力。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?utawaNKg)

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

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

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

[查看更多](https://www.4hou.com/member/aQWl)

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