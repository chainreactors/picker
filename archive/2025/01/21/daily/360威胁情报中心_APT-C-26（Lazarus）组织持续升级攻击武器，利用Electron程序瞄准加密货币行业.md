---
title: APT-C-26（Lazarus）组织持续升级攻击武器，利用Electron程序瞄准加密货币行业
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247505519&idx=1&sn=594229f2c0123673d1fa9c6cf729858b&chksm=f9c1e566ceb66c701d875de8481fe02d89654d4b56cfc51088de6e421cb701437cdab52a0851&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2025-01-21
fetch_date: 2025-10-06T20:12:58.054422
---

# APT-C-26（Lazarus）组织持续升级攻击武器，利用Electron程序瞄准加密货币行业

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812gLAB0YasDqnRjiasZ8RKeh4uYS1CwtqlQquWMm6qLiaYkD6NJEibRoZGQ/0?wx_fmt=jpeg)

# APT-C-26（Lazarus）组织持续升级攻击武器，利用Electron程序瞄准加密货币行业

原创

高级威胁研究院

360威胁情报中心

**APT-C-26‍‍**

**Lazarus**

APT-C-26（Lazarus）组织是一个高度活跃的APT组织。该组织除了对金融机构和加密货币交易所感兴趣外，也对全球的政府机构、航空航天、军工等不同行业开展攻击活动，主要目的是获取资金和窃取敏感信息等。其攻击方式主要包括网络钓鱼、网络攻击和勒索软件攻击，并且它们的攻击行为具有高度的技术复杂性和隐蔽性，也具备Windows、Linux、MacOS系统攻击能力，以及拥有多种攻击载荷武器。

360高级威胁研究院捕获到了Lazarus组织利用Electron打包的恶意程序，该程序伪装成货币平台的自动化交易工具安装包，被用来对加密货币行业相关人员进行攻击。一旦受害者点击Electron打包的恶意程序，首先会显示正常的安装过程，但是在后台会运行恶意功能，然后通过层层加载，最终完成攻击行为。鉴于该组织近期频繁通过恶意安装程序针对多个平台进行渗透，并且在观察中发现其代码混淆也持续升级，因此我们在这里进行详细分析，希望经过曝光披露，相关的企业和个人可以提高安全防范意识，保护企业财产和相关用户财产免受损失。

# **一、攻击活动分析**

## **1.攻击流程分析**

本轮攻击中，Lazarus组织通过毒化uniswap-sniper-bot项目，并使用Electron打包成可执行文件进行投递，一旦用户运行就会下载执行恶意代码，盗取敏感信息，本文重点描述这类攻击方式(图中标红部分)。之前，该组织还利用过Python存储库PyPI、node.js项目以及视频软件进行投毒攻击，此类本文不再详细分析。但是这类攻击流程大同小异，其流程图如下:

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ8125zeX91tRHoud8aM0LNEsN8JpybBY3nyia0Jy2cndmwXFtn2sJ7QghDA/640?wx_fmt=png&from=appmsg)

## **2.载荷投递分析**

Lazarus组织近日进行投递的部分样本信息如下：

|  |  |
| --- | --- |
| **MD5** | 48c179680e0b37d0262f7a402860b2a7 |
| **文件名称** | uniswap-sniper-bot-with-guiSetup1.0.0.exe |
| **文件大小** | 70.68 MB (74110128 bytes) |

该样本免杀效果很好，在VirusTotal多引擎检测中只有极少数厂商报毒。运行该程序，首先会进行uniswap-sniper-bot正常安装以迷惑用户，uniswap-sniper-bot-with-gui是个开源项目(https://github[.]com/meta-dapp/uniswap-sniper-bot),它是一个用于类似交易所（DEX）平台的自动化交易工具，通常是为了帮助用户自动化购买新上线的代币或快速抢购热门代币。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812mPEMUKdVBxO6S4ozWER96cia1FlibOk8pJsUEdWvmDY7cyPESUBbg30Q/640?wx_fmt=png&from=appmsg)

与此同时，该样本在执行安装的过程中后台会进行恶意代码的下发。仔细分析发现该样本是利用Electron打包编译而成，Electron 是一个开源框架，它结合了Chromium和 Node.js，使得开发者可以使用 Web 技术来构建桌面应用，并且支持Windows、macOS 和 Linux 等平台，由此也可以看出该组织具备多平台攻击的能力。

将Electron程序进行反编译，首先解压EXE程序找到app.asar进行反编译，解压后的结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ8123iauuh5ic40HVWFSgicDsarhoof6PW4Jmwwzp7bkyymJQ9l2L0T8Abicow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812WicgmU1WMKJA3pTGjV2I14eTlC2EPicn5qrzjhy6ibSmm0O91mc7o7dhA/640?wx_fmt=png&from=appmsg)

通过分析对比，发现位于\src\helpers下的TokenHash.js被profits.js加载，而profits.js被main.js加载，但是对比uniswap-sniper-bot官方源代码，发现并没有引用该TokenHash.js，因此判断该脚本是lazarus组织嵌入的恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812SeUs61iavSAicI3YquKXMJ63cqqW906wO3xR0tZiaicvymguXfpOhzFVTw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812AZVdjSe3jYx5ow8p8G6dYOv7xeN82kwdDBzk7G4fKHz9nscF4xD8eQ/640?wx_fmt=png&from=appmsg)

打开该文件发现此脚本经过严重混淆，在之前捕获的此类攻击中并没有这么混淆，由此也可以看出该组织在不遗余力的进行载荷升级。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812RViacwERM4RYppNO00aF9f1nZ5yrW0AT1NLYUQibyyl0nebibNhfaCxGA/640?wx_fmt=png&from=appmsg)

## **3.载荷功能分析**

对上述提到的TokenHash.js进行去混淆，解混淆后可以看到其代码首先定义了多个浏览器加密钱包扩展程序ID。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812l00PfBG42wibn7azGqgYj0b3FyW6ib8RaL7wFQcDYMzVlm9ROu2xzSoA/640?wx_fmt=png&from=appmsg)

接着根据Brave、chrome和opera浏览器的默认存储路径，窃取其钱包数据并回传到[http://86.104.74[.]51:1224/uploads。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ8128LQKicwQnNyIMnXuYRnIzwqERBibLOC8JMUFL3icVglMgESzqtQRYia2Ng/640?wx_fmt=png&from=appmsg)

然后从地址http://86.104.74[.]51:1224/pdown下载python安装包，便于后续代码执行，以及从地址[http://86.104.74[.]51:1224/client/7/702下载后续载荷并保存为%userprofile%\.sysinfo执行。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812VgJdDJ5QsCCEMwfyic4PmUiaYbnLSgpzy1SiahhB9YNphTXYzIOYlFRtQ/640?wx_fmt=png&from=appmsg)

下载的.sysinfo是一个python脚本，经过49层解码再解压缩得到原始代码如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ8123MdsibTqlR6L01H5iblSo3oEcb2XQBTaXVnibhWu8AFKXh9CPQtBuGFxw/640?wx_fmt=png&from=appmsg)

其功能为下载器，从86.104.74.51地址下载插件用于后续攻击活动，后续插件的功能和我们之前对Lazarus组织该类型载荷的追踪中对比发现并无变化，故在次只对其进行简要分析说明。

**插件1：**

下载地址: http://86.104.74[.]51:1224/payload/7/702，保存为%userprofile%\.n2\pay，功能为主机监控，文件窃取，执行shell指令并设置anydesk等。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812dqrJD659pedRg694C9QSwqNGxs7xVtELWXAMplNCrfDuFeux6icbeicw/640?wx_fmt=png&from=appmsg)

**插件2：**

下载地址：http://86.104.74[.]51:1224/bow/7/702, 保存为%userprofile%\.n2\bow，功能为窃取Chrome, Brave, Opera, Yandex, MsEdge数据。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ8122aUV8W8xag1KJjnPLASudQ2ZnfplVvBiawhssiaPgEpqOwpcYjJUqibzA/640?wx_fmt=png&from=appmsg)

**插件3：**

下载地址：http://86.104.74[.]51:1224/mclip/7/702, 保存为%userprofile%\.n2\mlip，功能为键盘监控、剪切板记录和窗口监控。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Po4M3BDEVuHlhf6cLIdZ812SAZP9KE5NmuAHAIT9ZGp3xWUG7xICfgtVibIa003NicRUTGGia20k3TDg/640?wx_fmt=png&from=appmsg)

# **二、关联分析**

早期我们也捕获到了多个Lazarus组织使用的带毒恶意程序包，主要以下几类：第一类是利用Python存储库PyPI，其具体分析参见360高级威胁研究院今年早期发布的文章[1]；第二类是利用node.js的npm包，其过程跟PyPI类似，可以参考phylum公司文章[2]；第三类也是近期伪装的视频软件安装包，目标人员一旦打开这类带毒的安装包后，恶意代码便会下载安装基于Python的后续载荷，从而展开窃密活动，部分样本信息如下所示，存在Windows和MacOS版本。

|  |  |  |
| --- | --- | --- |
| **MD5** | **文件名** | **针对平台** |
| 8ebca0b7ef7dbfc14da3ee39f478e880 | FCCCall.msi | Windows |
| 1bb8b1d0282727ab9bc2deb3570cf272  bc14c3ab8316e7ec373829ea7a6e2166 | FCCCall.dmg | MacOS |

这类样本后续执行的流程跟本次分析的样本类似，但是样本没有经过强混淆，没使用Electron打包成可执行程序，伪装的载体以及C&C服务器也都不一致，这也可以看出攻击者在不断升级攻击组件，具体分析不再详述，可以参考Group-IB 公司文章[3]。

# **三、归属研判**

根据对Lazarus组织近期攻击事件的深入分析，发现该组织具有较为鲜明的攻击目的，以及技术特征，具体总结如下：

1）Lazarus组织近期为了攫取经济利益，基本都是以加密货币从业者，或者和加密货币高度相关的人群作为攻击对象，通过毒化加密货币开源项目，然后诱使受害者下载运行编译好的带毒的程序，从而实现窃取信息等目的。

2）Lazarus组织近年来经常使用Python，JavaScript相关武器库，在本次攻击事件中，攻击者通过投毒UniswapSniperBot项目进行攻击，UniswapSniperBot使用JavaScript进行开发，这和Lazarus近期利用node.js项目攻击手法相吻合。只是这次使用了Electron框架打包，以便用户更容易执行。

3）本次攻击样本回连的C&C服务端，其端口和近期披露的Lazarus攻击事件相吻合，都是1224或1244端口，回连的URL中，都含有uploads，pdown，/client/[数字]等字段。

通过上述特点，本次攻击归属于Lazarus组织。

#

**总结**

在本次详尽的攻击分析中，我们揭秘了APT-C-26组织如何巧妙地利用uniswap-sniper-bot项目执行恶意代码的全过程，并且执行过程中都是层层递进，关键代码也经过了强混淆，具备相当强的隐蔽性，通过一系列执行达到窃取用户信息的目的。此外，攻击组织针对 Windows、Linux、macOS系统都具备相当强的攻击攻击能力，并且有大量IP资产，这都体现出该组织背后有强大的经济能力支撑，以及对目标人群的意志坚定性。因此在这里提醒相关企业和个人加强安全意识，无论何种操作系统，切勿执行未知样本。这些行为可能导致系统在没有任何防范的情况下被攻陷，从而导致机密文件和重要情报的泄漏。

另外，本文披露的相关恶意代码、C&C只是APT-C-26组织近期攻击过程中使用的攻击武器，该组织不会因为一次攻击行动的暴露而停止活动，反而会持续更新其载荷，后期我们也将持续关注该组织的攻击活动。

#

#

**附录 IOC**

#

**MD5:**

48c179680e0b37d0262f7a402860b2a7

8ebca0b7ef7dbfc14da3ee39f478e880

1bb8b1d0282727ab9bc2deb3570cf272

bc14c3ab8316e7ec373829ea7a6e2166

61279d5e30f493bbdae9eab8ca99e9a4

2a8e4281213e4aaa485612f9ded261a2

457bb40c6fc10b3cd5a3b51e4eb672b2

eac8edaf5a4637fd964d7a3d87f8189a

bf82e3b5d25d167c168cc6600e797c53

**C&C：**

86.104.74[.]51:1224

45.128.52[.]14:1224

45.137.213[.]30:1224

165.140.86[.]227:1244

38.92.47[.]151:1244

23.106.253[.]215:1244

38.92.47[.]85:1244

138.201.199[.]46:1224

45.43.11[.]201:1244

147.124.214[.]129:1244

167.88.168[.]152:1224

185.235.241[.]208:1224

95.164.17[.]24:1224

#

**参考**

[1][https://mp.weixin.qq.com/s/g2jQ9yeT68SGZb1APY7xtA](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247499462&idx=1&sn=7cc55f3cc2740e8818648efbec21615f&scene=21#wechat_redirect)

[2]https://blog.phylum.io/crypto-themed-npm-packages-found-delivering-stealthy-malware/

[3]https://www.group-ib.com/blog/apt-lazarus-python-scripts/‍‍‍‍

**团队介绍**

TEAM INTRODUCTION

**360****高级威胁研究院**

360高级威胁研究院是360数字安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过