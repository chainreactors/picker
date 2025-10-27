---
title: Check Point：攻击者通过合法email服务窃取用户凭证信息
url: https://www.4hou.com/posts/ZGmg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-06
fetch_date: 2025-10-04T11:51:44.227017
---

# Check Point：攻击者通过合法email服务窃取用户凭证信息

Check Point：攻击者通过合法email服务窃取用户凭证信息 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Check Point：攻击者通过合法email服务窃取用户凭证信息

企业资讯
[行业](https://www.4hou.com/category/industry)
2023-07-05 13:21:28

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)84459

收藏

导语：近日， Check Point® 软件技术有限公司的研究人员对电子邮件安全展开调研，结果显示凭证收集仍是主要攻击向量，59% 的报告攻击与之相关。

近日， Check Point® 软件技术有限公司的研究人员对电子邮件安全展开调研，结果显示凭证收集仍是主要攻击向量，59% 的报告攻击与之相关。它还在商业电子邮件入侵 (BEC) 攻击中发挥了重要作用，造成了 15% 的攻击。同时，在2023年一份针对我国电子邮件安全的第三方报告显示，与证书/凭据钓鱼相关的不法活动仍居电子邮件攻击活动之首。而我国在2022年内受钓鱼邮件攻击的总量仅次于美国，位居全球第二名。种种迹象均已表明，钓鱼邮件这一“简单粗暴”的方式仍然受到不法分子的“青睐”。

为窃取和收集用户凭证，网络钓鱼电子邮件中会随附一个恶意 URL 或附件。Check Point 的遥测数据显示，超过一半的恶意附件是 HTML 文件。为了诱骗用户，其中许多附件伪装成了已知服务和厂商（如微软、Webmail 等）的登录页面。

![图片1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534150740966.jpg "1688534150740966.jpg")

用户在伪造登录表单中输入自己的凭证并点击提交，然后凭证通常通过 Web 服务器或 Telegram 的 API 发送给攻击者。在过去的几个月里，CPR 观察到持续不断的攻击活动涉及数千封电子邮件，这些电子邮件利用 EmailJS、Formbold、Formspree 和 Formspark 等合法服务来获取被盗凭证。上述服务都是在线表单构建器，允许用户为自己的网站或 Web 应用创建自定义表单，并得到了开发人员的广泛使用。它们不仅为构建可嵌入到网站或应用的表单提供了用户友好型界面，而且还可提供各种表单字段类型，例如文本输入字段、单选框、复选框、下拉菜单等，以便用户以结构化的方式收集用户信息。用户提交表单后，此类服务将处理表单数据并收集被盗凭证。

![图片2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534180154006.jpg "1688534180154006.jpg")

**凭证收集**

凭证收集是一种网络攻击，其中攻击者窃取用户名和密码等敏感信息，以获取用户对合法网络服务的初始访问权限或在网上贩卖。通常，这些攻击并非针对某一特定机构，而是试图收集尽可能多的不同用户名和密码来在网上兜售。

![图片3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534218276372.jpg "1688534218276372.jpg")

图 3：暗网论坛出售被盗凭证

**合法邮件服务之殇**

过去，攻击者主要使用两种方法来收集凭证。第一种方法是使用托管在受攻击站点上的 PHP 文件。然而，在这种方法中，攻击者面临着站点被网络安全解决方案拦截的可能性。第二种方法是使用 Telegram 的 API，但这种方法被安全厂商所熟知，因此被拦截的几率更高。现在，使用合法表单服务 API 的新方法被许多开发人员所使用，这就加大了拦截恶意 HTML 文件的难度。借助该 API，凭证可被发送到攻击者选择的任何位置，甚至能够发送到他自己的邮箱。

以EmailJS 为例，EmailJS 是一项允许开发人员只使用客户端技术（而无需任何服务器代码）发送电子邮件的服务。若要使用该服务，用户只需：

1. 将电子邮件地址连接到该服务；

2. 创建一个电子邮件模板，以确定电子邮件发送方式以及电子邮件接收地址；

3. 使用 EmailJS SDK 或 API，以利用 JavaScript 发送电子邮件。

该服务每月可免费发送最多 200 封电子邮件，而通过订阅，每月可发送多达 100,000 封电子邮件。该服务是合法的，根据其官网数据，有超过 25,000 名开发人员正在使用这项服务。

![图片4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534259193271.jpg "1688534259193271.jpg")

图 4：EmailJS 官网

以下两个示例说明了攻击者正如何使用该服务来收集被盗凭证——

![图片5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534283670444.jpg "1688534283670444.jpg")图 5：使用 EmailJS 的网络钓鱼页面

在图 5 中，攻击者首先利用其公钥使用“emailJS.init”，然后使用函数“sendEmail”（当用户提交表单时被触发）和“emailjs.send”通过电子邮件将数据传输到他的电子邮件帐户。

![图片6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534312143099.jpg "1688534312143099.jpg")图 6：另一个从 HTML 文件中使用 EmailJS 的示例

在图 6 中，攻击者直接使用 EmailJS API 将受害者的凭证发送给自己。
上述示例均来自于我们观察到的一起攻击活动。此外，Check Point还发现该攻击活动使用了两个不同的 EmailJS 公共 API 密钥。

**一起真实的钓鱼攻击**

CPR近日检测到一起始于一封钓鱼电子邮件的持续攻击活动，这场攻击活动用到了该电子邮件的多个版本和几个不同的 HTML 模板。

![图片7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534341486728.jpg "1688534341486728.jpg")

 图 7：攻击活动中使用的网络钓鱼电子邮件的示例

所附文件与受害者收到的电子邮件相对应，Check Point已发现了该电子邮件的多个版本。

![图片8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534379194289.jpg "1688534379194289.jpg")![图片9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534390152221.jpg "1688534390152221.jpg")

图 8：HTML 附件伪装成文件和网页邮件登录页面

为了让登录页面看似没问题，攻击者在表单（在 HTML 文件中进行了硬编码）中填写了受害者的电子邮件地址。一旦受害者输入其凭证并尝试登录，用户名和密码就会被直接发送到攻击者的电子邮件收件箱。

![图片10.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534420156265.jpg "1688534420156265.jpg")图 9：使用 EmailJS 的凭证收集流程

![图片11.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688534448144877.jpg "1688534448144877.jpg")图 10：使用 Formspark 的 HTML 附件的示例

**预防为先刻不容缓**

通过合法手段进行不发活动无疑使安全形势变得更加复杂。同时，今年四月Check Point揭示了如何通过ChatGPT进行钓鱼软件编写，这也意味着不法行为的实施成本也在日趋降低。因此，时刻保持Check Point公司倡导的“预防为先”的安全理念，才是打造互联网安全环境的第一步重要措施。

Check Point Threat Emulation 客户端能够防御此类攻击。考虑到逃逸型零日攻击和网络钓鱼攻击的速度和复杂性，采用 AI 深度学习 来预测和阻止恶意行为、且无需人工干预的解决方案将逐渐成为邮件安全防御的主流。

在 Miercom 基准测试报告中，Check Point 取得了网络钓鱼防御率高达 99.9% 的骄人成绩，实现了 99.7% 的恶意软件防御率，而且在网络钓鱼、恶意软件及零日网络钓鱼 URL 方面的漏检率几乎为 0%。因此，Check Point有信心帮助用户在恶意邮件攻击日趋严峻的形势下，依然可以享有最高级别的安全防护，确保核心数字资产无虞。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GOYHa27F)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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