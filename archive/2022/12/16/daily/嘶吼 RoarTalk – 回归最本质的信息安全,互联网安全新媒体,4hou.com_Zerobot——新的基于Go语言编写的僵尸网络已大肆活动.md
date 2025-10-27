---
title: Zerobot——新的基于Go语言编写的僵尸网络已大肆活动
url: https://www.4hou.com/posts/q817
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-16
fetch_date: 2025-10-04T01:38:49.312238
---

# Zerobot——新的基于Go语言编写的僵尸网络已大肆活动

Zerobot——新的基于Go语言编写的僵尸网络已大肆活动 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Zerobot——新的基于Go语言编写的僵尸网络已大肆活动

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-12-15 11:12:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)962004

收藏

导语：11月，FortiGuard实验室观察到一个用Go语言编写的独特僵尸网络通过物联网漏洞进行了传播。

11月，FortiGuard实验室观察到一个用Go语言编写的独特僵尸网络通过物联网漏洞进行了传播。这个僵尸网络被称为Zerobot，包含几个模块，包括自我复制、针对不同协议的攻击和自我传播。它还使用WebSocket协议与其命令和控制服务器通信。根据一些IPS签名触发计数，该活动在11月中旬之后的某个时候开始了当前版本的传播。

受影响的平台：Linux；

受影响组织：任何组织；

影响：远程攻击者可以控制易受攻击的系统；

严重级别：严重。

本文详细介绍了该恶意软件如何利用漏洞，并在进入受感染的设备后检查其行为。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670559194478516.png "1670559194478516.png")

IPS签名活动

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670559203158125.png "1670559203158125.png")

IPS签名活动

**感染**

Zerobot利用多个漏洞来访问设备，然后下载脚本以进一步传播。完整的脚本如下图所示。请注意，下载URL已从http[：]//zero[.]sudolite[.]ml/bins更改为http[：]]//176[.]65.137[.]5/bins。此Zerobot变体针对以下架构：i386、amd64、arm、arm64、mips、mips64、mips64le、mipsle、ppc64、ppc64le、riscv64和s390x。它使用文件名“zero”保存，这是活动名称的来源。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670559317208177.png "1670559317208177.png")

2022年11月24日之前使用的下载脚本

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670559328919028.png "1670559328919028.png")

当前下载脚本

Zerobot有两个版本。11月24日之前使用的第一个仅包含基本功能。当前版本增加了一个“selfRepo”模块来复制自身，并感染更多具有不同协议或漏洞的端点。旧版本的功能列表如下图所示。然而，以下技术分析是基于新版本的。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670559563152989.png "1670559563152989.png")

11月24日之前Zerobot版本的主要功能

**技术分析——初始化**

Zerobot首先检查其与Cloudflare的DNS解析器服务器1.1.1.1的连接。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670559576211845.png "1670559576211845.png")

检查1.1.1.1:80的网络连接

然后，它根据受害者的操作系统类型将自己复制到目标设备上。对于Windows，它将自己复制到文件名为“FireWall.exe”的“Startup”文件夹中。Linux有三个文件路径：“%HOME%”、“/etc/init/”和“/lib/systemd/system/”。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670559586758917.png "1670559586758917.png")

复制本身的代码流

然后，它设置了一个“AntiKill”模块，以防止用户中断Zerobot程序。该模块监视特定的十六进制值，并使用“signal.Notify”拦截任何发送来终止或终止进程的信号。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670559987543313.png "1670559987543313.png")

AntiKill的部分代码

**技术分析——命令**

初始化后，Zerobot使用WebSocket协议启动到其C2服务器ws[：]//176[.]65[.]137[.]5/handle的连接。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560000144528.png "1670560000144528.png")

连接到C2服务器

从受害者发送的数据如下图所示。基于WebSocket协议，我们可以对其进行屏蔽，以获取带有受害者信息的JSON：

{"Platform":"linux","GCC":"386","CPU":1,"Payload":"Direct","Version":1}

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560010147366.png "1670560010147366.png")

C2连接的流量捕获

通信通道设置后，客户端等待来自服务器的命令，包括“ping”、“attack”、“stop”、“update”、“kill”、“disable\_scan”、“enable\_scan”和“command”。有关“enable\_scan”中漏洞的详细信息，接下来会讲到。

![11.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560023223949.png "1670560023223949.png")

![11.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560031207651.png "1670560031207651.png")

在zero.mips中接收命令

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560044203699.png "1670560044203699.png")

zero.386中接收到的命令

**技术分析——开发**

Zerobot包括21个漏洞，具体如图12所示，下图中受影响的产品如下所示。除了一些物联网漏洞外，还包括Spring4Shell、phpAdmin、F5 Big等，以提高其攻击成功率。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560057122127.png "1670560057122127.png")

Zerobot中的漏洞列表

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560071436323.png "1670560071436323.png")

Zerobot针对的易受攻击设备列表

上图顶部名为“ZERO\_xxxxx”的两个漏洞来自网站“0day.today”。该网站分享了许多用于“教育”目的的漏洞。编号“36290”和“32960”是从该网站分配的。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560082115888.png "1670560082115888.png")

“ZERO\_36290”漏洞的0day.today网页

漏洞中注入的有效负载数据与上图所示的脚本文件相同。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221209/1670560093108629.png "1670560093108629.png")

为利用漏洞注入的有效载荷数据

**总结**

Zerobot是一个用Go编程语言编写的新僵尸网络。它通过WebSocket协议进行通信。它于11月18日首次出现，旨在针对各种漏洞。在很短的时间内，它被更新为字符串混淆、复制文件模块和传播攻击模块，这使得它更难检测。

本文翻译自：https://www.fortinet.com/blog/threat-research/zerobot-new-go-based-botnet-campaign-targets-multiple-vulnerabilities如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lBubpXhs)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

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

[查看更多](https://www.4hou.com/member/bo2j)

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png...