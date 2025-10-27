---
title: DeepSeek引发全球关注，恶意软件鱼目混珠趁机传播
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247503018&idx=1&sn=5d69c21fad271526d5e83395a9943a11&chksm=fe79e832c90e6124bdc4448fad61ad411a27d305d402e88b672f9e3052fe832a10e3dc2e33e2&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2025-02-18
fetch_date: 2025-10-06T20:39:34.370821
---

# DeepSeek引发全球关注，恶意软件鱼目混珠趁机传播

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icnHR8wZzMicDiaZeV7hwtLVDmKZvqx4PFM21KQomlVbaPpARCrNz2T8OicPRUXxxWpucPJUzU45C48A/0?wx_fmt=jpeg)

# DeepSeek引发全球关注，恶意软件鱼目混珠趁机传播

红雨滴团队

奇安信 CERT

概述

近年来，人工智能（AI）技术迅猛发展，成为推动社会进步和产业变革的重要力量。AI 在各个领域的广泛应用，极大地提升了生产效率和生活质量。特别是在搜索技术方面，AI 的引入使得搜索结果更加精准、高效。在这一背景下，DeepSeek 作为一款领先的智能搜索与应用平台，凭借其强大的 AI 驱动搜索能力和便捷的用户体验，迅速在全球范围内积累了大量用户，成为科技领域的热点。

DeepSeek 在全球的大热也为网络犯罪分子提供了极具吸引力的诱饵话题，近期奇安信威胁情报中心和病毒响应中心发现大量仿冒 DeepSeek 平台的钓鱼站点出现，并趁机传播伪装为 DeepSeek 名称的 Android 应用和 Windows 程序。

Android恶意程序

此次通过国家计算机病毒协同分析平台发现的Android攻击样本，经奇安信病毒响应中心分析可知，该样本在用户可见的 AppName 和 Icon 方面仿冒为 DeepSeek，而在安全分析人员常用的指纹数据上（如 APPID 和 Cert 等）使用测试数据伪装，以躲避关联与溯源分析。攻击样本采用嵌套结构，将核心恶意程序存储在母包 Assets 中，在用户运行时诱导安装，我们分别将其称为 DropperAPP 和 CoreAPP。

DropperAPP 基本信息如下表：

|  |  |
| --- | --- |
| **样本文件名** | DeepSeek.apk |
| **APPName** | DeepSeek |
| **APPID** | com.hello.world |
| **Icon** | ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUG5lAGud9d4Mq2nKIDhm52UzLBe0Ynaroqr4LH7lOzPAakCAibGSib7kKQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1) |
| **样本****MD5** | e1ff086b629ce744a7c8dbe6f3db0f68 |
| **CertHash(MD5)** | 20f46148b72d8e5e5ca23d37a4f41490 |
| **样本大小** | 12.80MB |
| **Version** | 1.0 |

CoreAPP 基本信息如下表：

|  |  |
| --- | --- |
| **样本文件名** | com.vgsupervision\_kit29 |
| **APPName** | DeepSeek |
| **APPID** | com.vgsupervision\_kit29 |
| **Icon** | ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUG5lAGud9d4Mq2nKIDhm52UzLBe0Ynaroqr4LH7lOzPAakCAibGSib7kKQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1) |
| **样本****MD5** | 99fe380d9ef96ddc4f71560eb8888c00 |
| **CertHash(MD5)** | 20f46148b72d8e5e5ca23d37a4f41490 |
| **样本大小** | 8.27MB |
| **Version** | 1.0 |

**DropperAPP分析**

DropperAPP 分析的核心目的是伪装成 DeepSeek 并诱导用户安装 CoreAPP，去除大量的垃圾代码后，其结构也比较简单，主要包含系统的一个 WebView 组件和一些诱导窗口。

首先，用户使用 DropperAPP 时，WebWiew 会加载一个硬编码的 html 页面，截图如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGhkmZibvxTwNsXP9aPGK64onvgxicib04W2ZPyCxV2FP6w6Wj6VtaVTxRw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

用户选择更新，则会进入安装 CoreAPP 的流程，因为 MainActivity 中有安装应用的监听，用户安装成功后，则会打开安装的 CoreAPP；如果检测未成功安装 CoreAPP 则会使用 chorme 程序加载 “https://www.google.com” 地址，因此，此伪装应用并不具备真实的 DeepSeek 相关功能。部分主要实现源码如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGxaibLlvicJsQrVKzsWY6pejFeBsd0kQ95kJkhFJZlCG4Sf1xj5dJDm4w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**CoreAPP分析**

CoreAPP 是一个 Banker 类木马，多家安全厂商已对其进行了识别，识别情况如下。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGAzVlicXoe0vrrR5N6XHpFgtsnJKvQ6jWsYKolroDkojmxnicmh1kn2jQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

其行为也能够从其清单文件中可见一斑，主要包含短信监听/发送、窃取电话号码和拨打电话等。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGeuEFSvxxtTjdT1gc2QxJkIsiawMwxrv0VHCPOE0WnRE9jBJ7dncZN1Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关联溯源分析**

此次发现的攻击样本投放在钓鱼站点 “deepsek.icu” 中，虽然站点已经失效，但从奇安信威胁情报中心中可以看到监控到了恶意样本投递行为，并成功识别。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGbibIY9m1S9IQr6ZPvFHbbzia9NsDjPduoRY331WjtpQicicXuccmrwibicNQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Windows恶意程序

针对 Windows 平台，奇安信威胁情报中心同样发现恶意程序在文件名和图标上伪装为 DeepSeek，运行后会展示安装 DeepSeek 的虚假界面，基本信息如下：

|  |  |
| --- | --- |
| **奇安信情报沙箱报告链接** | https://sandbox.ti.qianxin.com/sandbox/page/detail?type=file&id=AZT-RGgKh6wn\_HCy8z5u |
| **样本文件名** | DeepSeek.exe |
| **样本****MD5** | a7389982054233436020f0ada0765a48 |
| **样本类型** | PE32 EXE |
| **样本大小** | 117.94 MB (123666360字节) |

**沙箱分析**

将该样本上传奇安信情报沙箱分析后，可以看到沙箱基于智能的恶意行为综合判断已经识别出文件恶意并给出了 10 分的恶意评分。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGkHQgEdBILCQibwRrDaBeiboibhYKmicHQgarPRuCxx1kArnkLCm8Vujn0g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

静态信息显示样本使用 DeepSeek 图标，文件元数据的产品名称也伪装为 DeepSeek。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGkpo2SVlsPupg2xqwZC88YmoV6FcVJib0hicITKoK2Via6ejjI4f7CxaXg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGxJD9bEqpGnibrKbdzbMiaFGNmKKJkgcaLhzmibNHj2Xbt9SdZtkYWzOKg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

样本带有数字签名，为 ”K.MY TRADING TRANSPORT COMPANY LIMITED”。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGhgBHBcQskm5ibxEiaXUzHg0ic5ibA8ibCx7yJ5bqMG2YNZNMkerCgvbjHhw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

流文件信息中也出现 ”Uninstall deepseek.exe” 文件名，nsis-script 的存在表明该样本为 NSIS 安装包。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGhEMGu5E8HoHznHAnteZDoCAuXjNECNEJTsmWxV2cXsF2wCIgewdHJw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

运行的 DeepSeek.exe 所在目录路径出现另一款 AI 工具 Sora 的名字，APP 运行参数出现 resources\app.asar，疑似为 Electron 框架编写的应用。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGIicpgeicMjqFPbyFWpSSfX6vEb9ylDINEeqTUm5JcpbEa0qv6zPMZN5Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

运行截图显示该样本伪造出安装界面用以迷惑受害者。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGWX0OBB8dAXTzicia8Axty3kibqpcMHPj0zxYyMib1oPBbrhPXmAg5Kh6kA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**详细分析**

安装包程序中存在一个 app-32.7z 文件，解压该文件可以在其中发现沙箱运行结果中出现的 deepseek.exe 和 resources\app.asar 文件。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGW4Rn73dfNdeFDPLN3gjMArTg4KL8RCfeR1EeLGia8paEq60YTrqq2zg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGn279r7YRvuicwZHHHu5IhjJP5loPudo17sRfY7oO3CvCicEib74MibMcXg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

进一步解包 app.asar，发现恶意代码入口文件为 crypto.js。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGzE3OfDIkZa2moyNdCRfLU6O1XSgXmrgWF8ugMxP06WtvOk5aTvTF3Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGCnksicA2Wlp9WNgzvn3yZuoAJledraH6UY6w9wYVicOGLlGksLjHcX7A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

crypto.js 包含俄语注释，读取 loadModule.js 中的代码，进行混淆处理。混淆处理后的代码由 outMutation.js 模块中的 jumpUp 函数运行。

loadModule.js 代码使用的 link\_proxy 为 hxxps://calendar.app.google/a1vRBeuK3n6NmKZC7，借助 Google 的 Calender 应用传递下载后续载荷的 URL，这也能解释为何沙箱中会出现对 calendar.app.google 域名的访问，并且这种传递方式可以将其隐藏在其他 Google 域名（如fonts.googleapis.com）中，避免被发现。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGGLlpDWDqu1L37uC6gjNticc4LEBONiaicGQ3oGmcUWjc85ZCtcJQqT8jw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGNStPCDYew3icBzD7sD88ayF5UIicy7pqUbPYl2OWvkWZK70K9SgCGhfA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

下载的后续的链接为 ”hxxp://95.179.216.217/tKLw2yGI2RbiCfXnIbL7T==”。服务器响应内容的首部包括用于载荷 AES 解密的 key 和 iv。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGCiccoDHwjGHvTwRVtfULRSqsHhDY7g0r6ibF7g21B8yuf9ZJDd0OZ7UQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

解密后的 JS 脚本会窃取机器上多款加密钱包的数据，在窃密脚本中同样出现俄文字符串。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGNAvibvmXkY5tm3yBUFKRlrEQCLT3qGE3BnqI6NkC7wb4KYibkW4VcdibQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9wVb06oBsibmEyIkfiazZFUGJAMmJ2U7bPicZyeLNJmgMBzGNIs0wRSkkyiayrDs50n7MYodkF6tg17w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

总结

DeepSeek 的兴起让很多人开始尝试使用该工具，这也成为了网络犯罪分子传播恶意软件的绝佳机会。用户如果想体验相关应用，一定要从官方网站和应用商店等正规渠道下载，擦亮眼睛警惕伪造的网站和程序，切不可受攻击者鱼目混珠之法欺骗，因误装恶意程序而造成敏感数据和隐私泄露。

奇安信威胁情报中心和病毒响应中心提醒广大用户，谨防钓鱼攻...