---
title: 攻击者创建130000个虚假帐户，滥用有时限的云计算资源
url: https://www.4hou.com/posts/q8Np
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-20
fetch_date: 2025-10-04T04:20:49.042800
---

# 攻击者创建130000个虚假帐户，滥用有时限的云计算资源

攻击者创建130000个虚假帐户，滥用有时限的云计算资源 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者创建130000个虚假帐户，滥用有时限的云计算资源

布加迪
[新闻](https://www.4hou.com/category/news)
2023-01-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)161191

收藏

导语：网络犯罪组织Automated Libra实施的PurpleUrchin活动使用虚假帐户来挖掘加密货币。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673055817962419.png "1673055817962419.png")

如今一伙攻击者正在利用GitHub、Heroku和Togglebox等多家服务提供商提供的免费或试用版云计算资源和平台，从事挖掘加密货币的勾当。这起活动使用持续集成/持续交付（CI/CD）流程实现了高度自动化，其手法是创建成千上万个虚假帐户，使用盗窃或伪造的信用卡激活限时试用版。

Palo Alto Networks旗下Unit 42的研究人员将该组织命名为Automated Libra，认为其大本营在南非。在去年11月份PurpleUrchin活动的高峰期间，该组织使用使CAPTCHA无效的自动化流程，每分钟注册3到5个GitHub帐户，目的是滥用GitHub Actions工作流用于挖掘加密货币。

研究人员在报告中表示，每个GitHub帐户随后都参与了用了就跑（play-and-run）的策略，每个帐户都会使用计算资源，但威胁分子最终并没有如数支付账单。这似乎是PurpleUrchin的标准操作程序，因为有证据表明他们在各个虚拟专用服务器（VPS）提供商和云服务提供商（CSP）创建了超过130000个帐户。

**结合白嫖和用完就跑的战术**

研究人员将滥用免费服务这一做法称为白嫖（freejacking），将创建需要收费但随后永不付账的帐户这一做法称为“用了就跑”。后者更难以得逞，因为大多数服务提供商要求用户注册有效的信用卡或支付方法，然后才允许他们访问付费的计算资源。然而，即使跟踪使用情况并按分钟收费，账单通常也会在较长一段时间后签发，这就给了攻击者滥用这些服务的时间窗口。

Automated Libra似乎使用了这两种方法，这表明他们可以使用被盗的信用卡，或者可以使用至少能被系统接受的卡，即使这些卡后来被发卡方标记为被盗并锁住。这表明落实强大的反欺诈支付系统有多重要。

PurpleUrchin自2019年以来一直处于活跃中，尽管他们经常滥用提供全虚拟化服务器的VPS提供商，但也将活动范围扩大到了云应用程序托管平台。比如说，Heroku提供一种支持多种编程语言的云应用程序托管平台，而Togglebox同时提供VPS和应用程序托管服务。两者都支持使用Docker和Kubernetes将应用程序部署为容器，Automated Libra恰恰利用了这一点。

研究人员表示，这个组织使用的基础设施架构使用CI/CD技术，攻击活动的每个单独软件组件都被放置在容器中。这个容器在更庞大的挖币活动采用的模块化架构中运行。CI/CD架构提供了高度模块化的运作环境，允许攻击活动的一些组件出现故障、更新，甚至被终止和替换，而不影响更庞大的环境。

并不是所有的容器都用于挖掘加密货币。一些用于自动创建帐户和部署任务，而另一些用于在不同的交易平台和交易所上自动销售挖掘的加密货币。

**使用GitHub工作流挖掘加密货币**

GitHub Actions是一个用于自动构建和测试软件代码的商业CI/CD平台，它为公共代码库提供了免费服务，为私有代码库提供了免费时段（按分钟计）的worker运行时间和存储空间。GitHub Actions工作流是使用YAML语法在.yml文件中定义的自动化流程，当某些触发器或事件发生时就会执行。它们需要执行Bash脚本、生成和复制文件等操作。它们基本上是在虚拟机上执行的一系列用户定义的任务，目的通常是用代码编译应用程序并测试它们。

为了自动创建GitHub帐户，攻击者使用了部署在Togglebox上的容器（含有一款名为Iron的基于Chromium的浏览器）、用于生成键盘和鼠标输入的工具Xdotool，以及用于转换、编辑和合成数字图像的ImageMagick工具包。

首先，自动化流程打开GitHub帐户创建页面Iron，并打开通向浏览器的VNC远程桌面会话。Xdotool通过VNC连接到浏览器，自动填写并提交表单。在这个阶段，帐户创建过程提供了需要用户处理的CAPTCHA。

GitHub CAPTCH盘问要求用户从几张不同形状的星系图片中选择螺旋星系。为了通过这个环节，xdotool下载图像并将它们传递给ImageMagick，然后ImageMagick被用来将它们转换成互补的红绿蓝（RGB）图像，这实际上把它们变成了白色背景上的红绿蓝斑点。然后使用ImageMagick识别命令来确定红色通道的“偏度”，并选择值最低的图像作为螺旋星系。

研究人员设法从一个容器中恢复了这整个自动化流程，它是专门为一种CAPTCHA盘问设计的，不太可能适用于其他盘问。研究人员没有测试这种技术的效果有多好，但已查明攻击者仅在11月份就成功注册了超过2万个GitHub帐户。

注册帐户后，下一步是注册拥有工作流权限的个人访问令牌（PAT），创建SSH密钥，并使用GitHub API创建代码库及其权限。然后使用PHP脚本生成的工作流更新代码库，使其具有随机属性，并具有独特性，与部署到其他帐户的工作流不一样。

执行后，工作流创建了64个作业，并使用了64个作业，随后使用了事件github.event.client\_payload下的repository\_dispatch，以执行外部托管的应用程序。最初，这些被用于执行外部的Bash脚本，但随后攻击者转而执行安装和启动加密货币挖掘功能的容器。

研究人员表示，值得一提的是，Automated Libra设计其基础设施，旨在最大限度地利用CD/CI工具。随着时间的推移，这一点越来越容易实现，因为传统的VSP正在力求服务组合多样化，以包括与云相关的服务。有了这些与云相关的服务，威胁分子就更加容易得逞了，因为他们不必维护基础设施即可部署应用程序。在大多数情况下，他们要做的就是部署一个容器。

虽然该网络犯罪组织滥用云服务提供商本身的计算资源，但同样的现代开发实践和云应用程序托管服务日益被不同的攻击组织用于建立指挥和控制（C2）基础设施，以实施各种攻击，这大大加大了分析起源和捣毁团伙的难度。

本文翻译自：https://www.csoonline.com/article/3684749/attackers-create-130k-fake-accounts-to-abuse-limited-time-cloud-computing-resources.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GVTA0HLB)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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