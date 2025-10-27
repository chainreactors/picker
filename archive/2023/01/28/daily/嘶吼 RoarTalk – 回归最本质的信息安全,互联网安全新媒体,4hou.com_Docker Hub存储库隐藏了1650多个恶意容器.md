---
title: Docker Hub存储库隐藏了1650多个恶意容器
url: https://www.4hou.com/posts/N1A8
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-28
fetch_date: 2025-10-04T05:02:20.497937
---

# Docker Hub存储库隐藏了1650多个恶意容器

Docker Hub存储库隐藏了1650多个恶意容器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Docker Hub存储库隐藏了1650多个恶意容器

布加迪
[新闻](https://www.4hou.com/category/news)
2023-01-28 00:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)176305

收藏

导语：超过1600个公开可用的Docker Hub镜像隐藏着诸多恶意行为，包括加密货币挖矿软件、可以用作后门的嵌入式秘密信息（secret）、DNS劫持软件以及网站重定向工具。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1674029497120024.png "1669330695803227.png")

超过1600个公开可用的Docker Hub镜像隐藏着诸多恶意行为，包括加密货币挖矿软件、可以用作后门的嵌入式秘密信息（secret）、DNS劫持软件以及网站重定向工具。

Docker Hub是一个基于云的容器库，允许人们随意搜索和下载Docker镜像，或将他们创建的镜像上传到这个公共库或私人存储库。

Docker镜像是一种模板，便于用户快速轻松地创建含有随时可用的代码和应用程序的容器。因此，那些希望创建新实例的人常常求助于Docker Hub，以便迅速找到一个易于部署的应用程序。

不幸的是，由于威胁分子滥用这项服务，上传的1000多个恶意镜像给毫无戒备之心的用户带来了严重的风险，他们在本地托管或基于云的容器上部署其实充斥着恶意软件的镜像。

许多恶意镜像所使用的名字伪装成大受欢迎、值得信赖的项目，因此威胁分子上传它们显然是为了诱骗用户下载它们。

Sysdig公司的研究人员深入研究了这个问题，试图评估这个问题的严重性，报告发现的镜像使用了某种恶意代码或机制。

**Docker Hub陷阱**

除了由Docker Library项目组审核、证明可信赖的镜像外，Docker Hub服务上还有成千上万个状态未知的镜像。

Sysdig使用其自动扫描工具仔细检查了250000个未经验证的Linux镜像，识别出其中1652个是恶意镜像。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1674029499104552.png "1669330685104175.png")

图1. Docker Hub上恶意镜像的类型（来源：Sysdig）

最常见的一类是加密货币挖矿软件，存在于608个容器镜像中，针对服务器资源，为威胁分子挖掘加密货币。

第二常见的一类是隐藏嵌入式秘密信息的镜像，共有281例。嵌入在这些镜像中的秘密信息有SSH密钥、AWS凭据、GitHub令牌、NPM令牌及其他信息。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1674029500167149.png "1669330673201850.png")

图2. Docker镜像中遗留的秘密信息类型（来源：Sysdig）

Sysdig声称，这些秘密信息可能被误留在公共镜像上，或者被创建和上传这些秘密信息的威胁分子故意注入。

Sysdig在报告中警告，通过在容器中嵌入SSH密钥或API密钥，攻击者就可以在容器部署后获得访问权限。

比如说，将公钥上传到远程服务器就可以让相应私钥的所有者通过SSH打开shell并运行命令，其效果与植入后门相似。

Sysdig发现的许多恶意镜像使用蓄意错误拼写手法来冒充合法可信的镜像，结果用加密货币挖矿软件感染用户。

这个策略为一些非常成功的攻击（比如下面两个例子）奠定了基础，它们已被下载了近17000次。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1674029501575989.png "1669330662184573.png")

图3. 含有加密货币挖矿软件的Docker镜像（来源：Sysdig）

蓄意错误拼写还确保输错了热门项目名称的用户会下载恶意镜像，因此虽然这并不带来庞大的受害者数量，但仍确保了新的用户不断被感染。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230118/1674029502167744.png "1669330654104818.png")

图4. 蓄意错误拼写的镜像捕获随机性的误拼（来源：Sysdig）

**日益严峻的问题**

Sysdig表示，在2022年，从Docker Hub提取的所有镜像中61%来自公共存储库，比2021年的数据增加了15%，因此用户面临的风险在上升。

遗憾的是，Docker Hub公共库的规模不允许其操作人员每天仔细检查所有上传的内容，因此许多恶意镜像并没有被报告。

Sysdig还注意到，大多数威胁分子只上传几个恶意镜像，所以即使删除了有风险的镜像、封杀了上传者，也不会对这个平台的整体威胁状况有显著影响。

本文翻译自：https://www.bleepingcomputer.com/news/security/docker-hub-repositories-hide-over-1-650-malicious-containers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?y7Ch2MbM)

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