---
title: Operation DevilTiger：APT-Q-12 使用 0day 漏洞技战术披露
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247511799&idx=1&sn=dbee6e45aaba5f7c6308a2858553cf8a&chksm=ea665980dd11d096dd4fe1f22547cc7af8007a29731a898baee057bcd2430aa7f98fa07b3788&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-08-27
fetch_date: 2025-10-06T18:06:14.402644
---

# Operation DevilTiger：APT-Q-12 使用 0day 漏洞技战术披露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic9BRedyHgxMjobgJzKN1hfpicxIjiceYHf6kfTcYlVMkCVcnzBnEtOAEWnrib8cWAAhjjzN2bJ8Sfzug/0?wx_fmt=jpeg)

# Operation DevilTiger：APT-Q-12 使用 0day 漏洞技战术披露

红雨滴团队

奇安信威胁情报中心

概述

APT-Q-12，中文名伪猎者，具有东北亚背景，奇安信威胁情报中心最早于 2021 年发布相关技术报告[1]，主要目标包含中国、朝鲜、日本、韩国等东亚地区的国家和实体。实际上该攻击集合最早由境外友商 blackberry 于 2017 年发布的 baijiu 行动中披露[2]，报告中提到 baijiu 行动与卡巴斯基发布的 Darkhotel 组织存在重叠。

从 2019 之后有关 Darkhotel 组织的行动在开源情报中的占比连年降低，与此同时政企终端中出现了数个具有朝鲜半岛背景并且技战术不同的攻击集合，我们根据特马和目标行业对这些攻击集合进行了分类，分别为 APT-Q-11(虎木槿)、APT-Q-12(伪猎者)、APT-Q-14(旺刺)、APT-Q-15、UTG-Q-005 等，经过五年的持续跟踪发现这些组织之间互有重叠，我们认为这些攻击集合都是当年 Darkhotel 的子集。

对 APT 组织的研究深入与否，取决于对其使用的插件类型掌握的程度。目前主流的 APT 组织都是只是将木马当作加载器或者下载者，大部分的间谍行为都由后续的插件来完成，由于不同组织对于目标数据的需求不同，如何在几百上千个内部文档中快速定位自己想要的数据，是导致各个方向的 APT 组织插件差异化巨大的主要原因，例如在 Operation ShadowTiger[3]活动中，Durain 插件只是用来获取特定的目录结构和移动特定目录下的文档，上传操作则是由 peach 插件利用管道传递参数的方式将数据上传到 C2 服务器上，而 APT37 和新海莲花组织则是只上传文件路径和目录结构，攻击者在后端对文档进行筛选，南亚方向的 CNC 组织先通过小型木马挑选感兴趣的文件目录，最后将文件目录硬编码在窃密插件中递归上传所有文档。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4SdPSWUFaxZhBIjrgibcVic37OLPtMZdDwg7LEia4JcDz5XW3Znt6UrT3w/640?wx_fmt=png&from=appmsg)

所以想要研究 APT 组织背后的行为逻辑和政治目的，仅靠初始的样本分析是远远不够的，插件的研究和捕获是重中之重。

我们建议政企客户在办公区和服务器区同时部署天擎 EDR 并开启云查功能来抵御未知的威胁。

信息收集

**探测邮件平台和品牌**

友商在最近的安全大会和 PR 报告中直截了当的对 0day 漏洞进行了分析，但是从攻击者挖掘漏洞到投递鱼叉邮件这中间存在一个非常复杂的信息收集过程。如何探测受害者使用的是 foxmail？163？coremail？以及平台是 win 客户端？网页端？移动端？为了能够完美触发各平台的 0day 漏洞，APT-Q-12 设计了多套复杂的邮件探针并周期性地向目标投递探针邮件以此来收集受害者的使用习惯和行为逻辑，恶意探针邮件非常难以识别，正文模仿各类广告和订阅号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4Y1DVRhmdYyTGiaT0pPEQK4wHXlf4YcEhW9wopAIoqRqPTmMicBibURGfg/640?wx_fmt=png&from=appmsg)

在合法探针链接下面插入攻击者自己的 C2 探针链接：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4423ibh4IsicnSm0DzwSmw9FmZdkUUwiaFY5JLQZMe30fhUsFN5XAr8KgQ/640?wx_fmt=png&from=appmsg)

尽管有些正文和标题容易被识别成垃圾邮件，但是 APT-Q-12 周期性地更换正文内容总能获取到受害者的 User-agent 信息，从而获取目标当前使用的邮件品牌和邮件平台。

**探测Office产品**

在对目标人员 Office 软件的信息进行收集时，APT-Q-12 对 wps 和 word 进行了区别处理。

**探测wps**

针对 wps 的探测时，附件内容中内嵌了 ole 对象的 web 控件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4BtPGZhQRkPP7qvLzosnsLCZkqjBhcbcBAKftCh3TzY6saSp1OEqHwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4AgXll6IKTN4uHn2licMUt7ibjcEo1xCCCWAOVq4g0uo8GUwPcYMsNJMg/640?wx_fmt=png&from=appmsg)

当使用 wps 打开该 mhtml 格式的文件后会将请求内置的 C2 探针，本地测试触发流程如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicic2NmAxJs5tricEDelmkXJqS9kewUmDicYDsjISGK9ZLLxYwbhbWHvZGdYDNTlf9azYwAewC4zMK8QA/640?wx_fmt=png&from=appmsg)

由于 Microsoft word 在十年前就已经就把 web 控件禁用，所以使用 word 打开上述 mhtml 文件时不会向 C2 探针发起请求。

**探测Microsoft word**

针对 Microsoft word 的探测时将 C2 探针链接插入模板注入中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4D6RSYOTQqM3sSXGxtut1aPmibJsWtQldpqdMiaicFjx4B0XZdVDfsTxibw/640?wx_fmt=png&from=appmsg)

为了绕过沙箱检测，打开诱饵 docx 时会有一层交互。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4mbnRzzDeQaxicrg5aib9bdlHEXN0lqxb9fLYia6IasPb4kXE6BwNEvAoA/640?wx_fmt=png&from=appmsg)

点击确认后才会请求 C2 探针链接，当使用 wps 打开该文档时则不会发起网络请求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicic2NmAxJs5tricEDelmkXJqSWXfKmx3X7iaHfzvhLGmGKsD2EPvDkRlkOMsAcaQFRFuic669mQafBMGA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4e6ic58PrmSy9A0xNXgX9wWYYFMYJj25ibfspCiadNKicbCz8N0PqXCYBVw/640?wx_fmt=png&from=appmsg)

攻击者使用上述差异化的探测方式来判断受害者常用的 office 软件。信息收集后的结果在东北亚地区各个 APT 组织中互相共享，而从为后续的 0day攻 击铺平道路。

Win 平台邮件客户端 0day 漏洞

**漏洞原理**

我们曾在 operation Dargon Dance[3]一文中提到基于 CEF 框架开发的国产软件脆弱性的问题，国内的外包人员和黑产都可以轻易的挖掘 RCE 漏洞进而发起大规模的  0day 攻击活动，漏洞入口一般为 XSS  漏洞，后续 payload 落地要么调用内部接口要么使用 chrome 内核较老的 RCE 漏洞来进行触发，内部接口利用方式的攻击链如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4STmQIZxw1Hib0icsoQPXfs2RmzBmeoNKPfgYu3SlHJ2ibb3wGUSCRaU2Q/640?wx_fmt=png&from=appmsg)

0day 邮件正文如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4icGScV4iaLOmGopn3IUjQr6McibdUYrew6Fs9hic0S9QY9NWlW31lox5Hw/640?wx_fmt=png&from=appmsg)

触发时会闭合标题上的代码，执行标题中剩余 js 代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4t1cvVRn83suGln2zsPNzibR2Bnsv5mricBDBucHqB48jX0jHNVomlkng/640?wx_fmt=png&from=appmsg)

解密后的内容如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU44d4a27s7ibo1OJgqwvNfE5gRx6LYm2DANGcTx3dsUZS6fCSziaLpDbtA/640?wx_fmt=png&from=appmsg)

执行邮件正文中的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4nZYhn8LcI23JkK28as8ib3TvmkZpLEoY4b5IM6icP4icWXRNMH1DUKu1w/640?wx_fmt=png&from=appmsg)

Name 字段解密后内容如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4AbTxEHXvnCxPlmtZyicfibOI0xDDJ2UXEXy0AsNzRLygqd95uNhNMYDQ/640?wx_fmt=png&from=appmsg)

寻找邮件结构中名为 image.png 的资源，并通过内部接口进行调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU40sUNVOI1sDhJbIArX3Otjkw10pFYlY0CB2bRRZgmvuj4pgbvGdetKg/640?wx_fmt=png&from=appmsg)

Base64 解密后实际为 lnk 文件，执行的 CMD 命令如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4ftwtbWyawg0ccKnRrYkwEjqgLq5XGmL96TNsEM6H6UsMCyxpeyTJ5A/640?wx_fmt=png&from=appmsg)

将 lnk 拷贝到特定目录下，并且解密 lnk 文件的附加数据并释放到 %temp% 目录下命名为 s.mui，启动 rundll32 去执行 s.mui 的导出函数 f。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4UAvGb04AicnzuDpVeI9TezAxA0JCBCHXKLFVBLk36ictyrT1RQLeS17A/640?wx_fmt=png&from=appmsg)

**木马分析**

|  |  |
| --- | --- |
| **文件名** | **Md5** |
| s.mui | 764c7b0cdc8a844dc58644a32773990e |

s.mui 的主要功能是判断操作系统版本和位数，在 temp 目录下释放 module.cab，调用 expand 将 cab 文件中的木马释放到 AppData\Local\Microsoft\Windows\StaticCache 目录下，并设置 com 劫持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4Exc4jTSzoUsnibkIT4XkIVNvqosw5Mic69XIzBtMp6vKpibIviaK8Y1AXw/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| **文件名** | **Md5** |
| ~StaticCache-System.dat | 59cd91c8ee6b9519c0da27d37a8a1b31 |

~StaticCache-System.dat 文件是 APT-Q-12 常用的第一阶段下载者。解密出的 C2 如下:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4kRCQ9dKaAArUau80VUHgThV31rj19lluwhSwUUS5TgekR827Jibmb7Q/640?wx_fmt=png&from=appmsg)

从云盘获取 bmp 并进行解密：

https://bitbucket.org/noelvisor/burdennetted/downloads/OAQDDI32.bmp

https://bitbucket.org/poppedboy/bovrilchant/downloads/32.bmp

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU45wpYN0ge2ialzoWvMx2NDt4ialVIIkJ8rZ4KEibNKWL8brVmGWk6jJiaMg/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| **Md5** | **导出函数** |
| fa17ed2eabff8ac5fbbbc87f5446b9ca | extension |

解密后的文件为第二阶段的下载者，调用 extension 导出函数，从 bitbucket.org/penguinwear/avoidlover/downloads/3WIGyjvJ.tmp 下载 tmp  文件到%temp% 目录，并进行 AES 解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4sts7DjmgCJtqMvNMNUzqybJshawNt6WT7tWQFDZiba54Srib2Fm7picPg/640?wx_fmt=png&from=appmsg)

将解密后的数据保存到以下路径 AppData\Local\Microsoft\Windows\SHCore\MMDevAPI.mui。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4IHFZp9ARqSfypWmQ56gibZQl856PYx84TpKFdwQeICMdLXLNxMw3wqA/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| **文件名** | **MD5** |
| MMDevAPI.mui | 71094ef9f2cf685e6c7d11fe310e5efb |

该木马为 APT-Q-12 常用的远控特马，解密后的字符串如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4x2qbU4emia7bKA1Jllk2xAHa9d0f7jehqHribTH67FHnUZl7iafw3ofXQ/640?wx_fmt=png&from=appmsg)

指令功能与 blackberry 于 2017 年披露的功能一致，同年我们又捕获到了另一个 win 平台邮件客户端的 0day 漏洞，由于 CEF 框架中 Chromium 内核版本过低，攻击者通过 XSS 漏洞执行带有 CVE-2017-5070 利用代码的 JS 脚本，从而实现木马落地。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU43uodVicbpZUgJFeBanLhKKm8xRXZrMh5icFmZ2G11RkuJFmbCr1ibQPmg/640?wx_fmt=png&from=appmsg)

XSS 触发入口如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4QvKJ7jKiaKeic1qMGJ9DmVdcwoJM7Vmqkduql2S1EeicPQHwf0p8wT1DA/640?wx_fmt=png&from=appmsg)

CVE-2017-5070 EXP代码如下：![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicJrXesy6fNRo7DSvDAsgU4CQC9zXCswh3ZiczVLIEbr2Zuaa8YcLwEnNt0XSUFianODdURynX8Recw/64...