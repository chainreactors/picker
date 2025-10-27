---
title: Chrome、Windows Defender和Firefox的0-day漏洞统统与西班牙一家商业IT公司有关联
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247554584&idx=3&sn=352271b528745f4d6201e246b00917ac&chksm=e915c622de624f34d70c5f5b07a0e35ec1b57a1c91874d8a299e3af90bd3e9894434b0735a25&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-12-03
fetch_date: 2025-10-04T00:27:34.638160
---

# Chrome、Windows Defender和Firefox的0-day漏洞统统与西班牙一家商业IT公司有关联

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29KPo3UHwFvEebMyQHZIicKg9icQPujC7ZgI7uiaz6iaWuKk7bUlDuZyiaBSWqMcXS9Tyicez8AsNsRdnyw/0?wx_fmt=jpeg)

# Chrome、Windows Defender和Firefox的0-day漏洞统统与西班牙一家商业IT公司有关联

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29KPo3UHwFvEebMyQHZIicKgcMviaicR6HQsfuCXpDfdmK52hdyRICRELKgxasYFhzp1GSoX16Cp40hw/640?wx_fmt=jpeg)

谷歌的研究人员周三表示，他们发现一家总部位于西班牙巴塞罗那的IT公司居然销售利用Chrome、Firefox和Windows Defender中漏洞的高级软件框架。

Variston IT自称专门提供定制的信息安全解决方案，包括嵌入式监控和数据采集（SCADA）及物联网集成技术、面向专有系统的定制安全补丁、数据发现工具、安全培训以及嵌入式设备安全协议的开发。据谷歌威胁分析小组的一份报告显示，Variston还销售其官网上没有提及的另一种产品：软件框架，为客户提供在他们想要监视的设备上偷偷安装恶意软件所需的一切。

两位研究人员Clement Lecigne和Benoit Sevens表示，这些漏洞框架被用来利用n-day漏洞：这种漏洞是最近才打上补丁的，一些受害者目标尚未安装它们。他们俩补充道，有证据表明，如果漏洞是零日（0-day）漏洞，这些框架也被使用了。研究人员公布发现结果是为了阻挠间谍软件市场。间谍软件市场在蓬勃发展，对各个群体构成了威胁。

他们俩写道，TAG的研究着重表明，商业监视行业在蓬勃发展，近年来取得了长足的发展，给全球互联网用户带来了风险。商业间谍软件将高级监视能力交到了政府的手上，政府利用它们监视新闻记者、人权活动人士、政治反对派和持不同意见者。

研究人员进而对框架进行分类，他们通过谷歌的Chrome漏洞报告计划从一个匿名来源收到了这些框架。每个框架附有指导说明和含有源代码的压缩包。这些框架被命名为Heliconia Noise、Heliconia Soft和Files。这些框架分别含有能够针对Chrome、Windows Defender和Firefox部署漏洞利用工具的成熟源代码。

Heliconia Noise框架中所含的代码用于在二进制文件被框架生成之前清理这些文件，以确保文件不含有可能使开发者受到牵连的字符串。正如清理脚本的图像所示，恶意字符串列表中包括“Variston”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KPo3UHwFvEebMyQHZIicKgdoyey06x0PPhos5ZXsNReerTuiaPab07ficeUrjpnDgSy4TLLaySOFPA/640?wx_fmt=png)

Variston的工作人员没有回复本文寻求置评的电子邮件。

这些框架利用了谷歌、微软和Firefox在2021年和2022年已修复的漏洞。Heliconia Noise含有针对Chrome渲染器的漏洞利用工具，以及用于逃逸Chrome安全沙箱的漏洞利用工具，安全沙箱旨在将不可靠的代码存放在一个受保护的环境中，无法访问操作系统的敏感部分。由于漏洞是在内部发现的，所以没有CVE编号。

客户可以对Heliconia Noise进行配置，以设置一些参数，比如投放漏洞利用工具的最长时间、到期失效日期以及指定何时将访客视为有效目标的规则。

Heliconia Soft含有一个设有陷阱的PDF文件，该文件利用了CVE-2021-42298，微软Defender Malware Protection的JavaScript引擎中的这个漏洞已于2021年11月修复。只要将该文件发给某人，就足以在其Windows上获得觊觎的系统特权，因为Windows Defender可自动扫描发来的文件。

Files框架含有针对在Windows和Linux上运行的Firefox的一条记录完备的漏洞利用工具链。它利用了CVE-2022-26485，这是Firefox在3月份修复的一个释放后使用的漏洞。研究人员表示，Files可能至少从2019年开始就在利用这个代码执行漏洞，远早于该漏洞广为人知或打上补丁。它适用于Firefox版本64到68。Files依赖的沙箱逃逸漏洞在2019年已被修复。

研究人员声称漏洞利用工具市场已日益失控。他们写道：

TAG的研究表明了商业监视现象急剧蔓延，以及商业间谍软件开发商能够开发出高级功能，而以前只有拥有雄厚财力和技术专长的政府才能获得这些功能。间谍软件行业的发展将用户置于险境之中，并使互联网变得不太安全。尽管监视技术按照国家或国际法律可能是合法的，但它们常常被用于歪道，针对一系列群体实行数字间谍活动。这些滥用行为对网络安全构成了重大风险，这就是为什么谷歌和TAG将继续针对商业间谍软件行业采取行动，并发表相关的研究结果。

Variston加入了其他漏洞利用工具卖家的行列，包括NSO Group、Hacking Team、Accuvant和Candiru。

参考及来源：https://arstechnica.com/information-technology/2022/11/google-ties-spanish-it-firm-to-0-days-exploiting-chrome-defender-and-firefox/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KPo3UHwFvEebMyQHZIicKgiboghibeYdaOzgkSLpxiad5JiaUck1KWncqFM7DD7vyiamiazjAIyPkpu0fQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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