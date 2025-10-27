---
title: 成千上万的GitHub代码库分发含有恶意软件的虚假PoC漏洞利用代码
url: https://www.4hou.com/posts/ZX92
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-29
fetch_date: 2025-10-03T21:11:46.443450
---

# 成千上万的GitHub代码库分发含有恶意软件的虚假PoC漏洞利用代码

成千上万的GitHub代码库分发含有恶意软件的虚假PoC漏洞利用代码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 成千上万的GitHub代码库分发含有恶意软件的虚假PoC漏洞利用代码

布加迪
[新闻](https://www.4hou.com/category/news)
2022-10-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)142282

收藏

导语：研究人员在GitHub上发现了成千上万个代码库提供针对多个漏洞的虚假概念证明（PoC）漏洞利用代码（exploit），其中一些含有恶意软件。

莱顿高级计算机科学研究所的研究人员近日在GitHub上发现了成千上万个代码库提供针对多个漏洞的虚假概念证明（PoC）漏洞利用代码（exploit），其中一些含有恶意软件。

GitHub是全球最大的代码托管平台之一，众多研究人员使用它发布PoC漏洞利用代码，以帮助安全行业验证漏洞修复程序，或者确定漏洞的影响和范围。

据莱顿高级计算机科学研究所的研究人员撰写的技术文章显示，感染上恶意软件而不是获得PoC的可能性也许高达10.3%，这不包括已证实的虚假漏洞利用代码和恶作剧软件。

**数据收集和分析**

研究人员使用以下三种机制分析了47300多个代码库，这些代码库发布了针对2017年至2021年期间披露的一个漏洞的漏洞利用代码：

IP地址分析：将PoC的发布者IP与公共黑名单、VT和AbuseIPDB进行比对。

二进制文件分析：对提供的可执行程序及其散列运行VirusTotal检查。

十六进制文件和Base64分析：在执行二进制文件和IP检查之前解码经过混淆处理的文件。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599786268280.png "1666599786268280.png")

图1. 数据分析方法（来源：Arxiv.org）

在提取的150734个独特IP中，有2864个IP与黑名单条目匹配，在Virus Total上的反病毒扫描中检测到1522个IP是恶意IP，其中1069个IP存在于AbuseeIPDB数据库中。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599799118209.png "1666599799118209.png")

图2. 各个黑名单上找到的IP地址（来源：Arxiv.org）

二进制文件分析检查了一组6160个可执行程序，显示总共2164个恶意样本驻留在1398个代码库中。

在测试的47313个代码库中，共有4893个代码库被认为是恶意的，其中大多数涉及来自2020年的漏洞。

![33.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599810185378.png "1666599810185378.png")

图3. 每年的恶意代码库（来源：Arxiv.org）

这份报告中包含的一小组代码库含有分发恶意软件的虚假PoC。然而，研究人员向BleepingComputer表明了至少另外60个代码库依然存在，目前正在被GitHub撤下的过程中。

**PoC中的恶意软件**

通过进一步研究其中一些代码库，研究人员发现了大量不同的恶意软件和有害脚本，从远程访问木马到Cobalt Strike，不一而足。

一个值得关注的例子是CVE-2019-0708（通常名为“BlueKeep”）的PoC，它含有一个用base64模糊处理的Python脚本，该脚本可以从Pastebin获取VBScript。

该脚本其实是Houdini RAT，这个基于JavaScript的旧木马支持通过Windows CMD远程执行命令。

![44.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599821172273.png "1666599821172273.png")

图4. 模糊处理的脚本和去模糊处理的Houdini

在另一种情况下，研究人员发现了一个虚假的PoC，这其实是信息窃取工具，收集系统信息、IP地址和用户代理。

这是另一名研究人员之前进行的一个安全实验，所以研究人员用自动化工具发现它，以确认他们的方法是有效的。

![55.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599834211632.png "1666599834211632.png")

图5. 虚假PoC泄密示例（来源：Arxiv.org）

其中一名研究人员El Yadmani Soufian还是Darktrac的安全研究人员，他好心地为BleepingComputer提供了技术报告中未包含的其他示例，如下所示:

含有用base64编码的二进制代码的PowerShell PoC在Virus Total中被标记为是恶意的。

![66.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599848272982.png "1666599848272982.png")

图6. 虚假PowerShell PoC

Python PoC含有一行代码，用于解码用base64编码的攻击载荷，该攻击载荷在Virus Total上被标记为是恶意的。

![77.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599861202511.png "1666599861202511.png")

图7. 恶意的一行代码攻击载荷冒充PoC

虚假的BlueKeep漏洞利用代码含有一个可执行程序，该程序被大多数反病毒引擎标记为是恶意的，并被识别为是Cobalt Strike。

![88.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599875153134.png "1666599875153134.png")

图8. Cobalt Strike通过虚假PoC来投放

![99.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666599894643468.png "1666599894643468.png")

图9. 无害但虚假的PoC

**如何保持安全？**

盲目信任GitHub上来源未经验证的代码库是个坏主意，因为内容没有经过审核，所以用户在使用之前需要审核它。

建议软件测试人员仔细检查他们下载的PoC，并在执行它们之前运行尽可能多的检查。

Soufian认为，所有测试人员都应该遵循以下三个步骤：

1. 仔细阅读将要在贵公司的网络或客户的网络上运行的代码。

2. 如果代码太过模糊，需要大量的时间来手动分析，不妨将它放在沙盒环境（比如隔离的虚拟机）中，检查网络中的任何可疑流量。

3. 使用像VirusTotal这样的开源情报工具来分析二进制文件。

研究人员已经向GitHub报告了他们发现的所有恶意代码库，但需要一段时间才能审查和删除所有恶意代码库，因此仍有许多恶意代码库对公众开放。

正如Soufian所解释，他们的研究目的不仅仅是作为GitHub上的一次性清理行动，而是以此为契机，开发一种自动解决方案，可以用来标记上传代码中的恶意指令。

这是该团队研究的第一个版本，他们正在努力改进其探测工具。目前，这款检测工具遗漏了迷惑性较强的代码。

本文翻译自：https://www.bleepingcomputer.com/news/security/thousands-of-github-repositories-deliver-fake-poc-exploits-with-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2CGjAWY1)

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