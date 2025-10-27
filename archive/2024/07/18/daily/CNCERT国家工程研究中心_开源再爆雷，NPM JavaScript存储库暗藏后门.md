---
title: 开源再爆雷，NPM JavaScript存储库暗藏后门
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545885&idx=2&sn=1469630a178ba38a6198320851783e79&chksm=fa9382dccde40bca2c7709ed9830f29625489873c8f2be31024b2c2718fbf1abcf5062803e02&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-18
fetch_date: 2025-10-06T17:45:32.832849
---

# 开源再爆雷，NPM JavaScript存储库暗藏后门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kHZv8Syx1fHtL2DPGWCEticwahRMDHL3iaoRb8qtcOmWibIDqYnZ3HpknAHVFK2le1bW7wgV5zEdC8A/0?wx_fmt=jpeg)

# 开源再爆雷，NPM JavaScript存储库暗藏后门

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kHZv8Syx1fHtL2DPGWCEtickT6eO5HQhLUSQeLTByJd7hvjKU3Td34JkiaAWbbIUbIPR4CHwPhO9Ew/640?wx_fmt=png&from=appmsg)

近日，Phylum的研究人员在开源NPM JavaScript存储库中发现两个恶意AWS软件包暗藏精心设计的代码，一旦执行，就会在开发者的计算机上植入后门程序。研究人员称恶意软件包存续期间已经被下载了数百次。

这两个软件包分别是img-aws-s3-object-multipart-copy和legacyaws-s3-object-multipart-copy，它们试图冒充合法的JavaScript库aws-s3-object-multipart-copy。

假冒软件包包含了所有合法库中的代码，并添加了一个名为loadformat.js的JavaScript文件。这个文件表面上包含无害的代码和三个JPG图像（分别是英特尔、AMD和微软的公司Logo），但其中一个图像隐藏了恶意代码片段，这些片段被重建后可组成后门程序代码，攻击开发者的设备。

# **日益复杂的开源供应链攻击**

“我们已经报告了这些软件包并要求移除，但这些恶意软件包在npm项目中仍然存在了近两天时间，”发现这些软件包的研究人员写道：“这令人担忧，因为当今大多数系统无法检测并及时报告这些软件包，导致开发者长时间暴露在攻击风险中。”

研究人员表示，绝大多数杀毒软件产品都未能发现隐藏在这两个软件包中的后门。

Phylum的研究主管Ross Bryant在邮件中透露，img-aws-s3-object-multipart-copy在被删除前被下载了134次，另一个文件legacyaws-s3-object-multipart-copy被下载了48次。

这些恶意软件包开发者对代码的精心设计及其策略的有效性，突显了针对上游开源代码库的攻击日益复杂化，除了NPM外，其他热门攻击目标还包括PyPI、GitHub和RubyGems等。

近年来，针对开发者的开源供应链攻击威胁不断恶化。

在过去的17个月里，由朝鲜政府支持的黑客组织曾两次针对开发者，其中一次利用了一个零日漏洞。

近期发现的最具创新性的一种开源后门隐藏方法是今年3月曝光的XZ Utils后门，只差一步进入生产版本中。该后门通过一个五阶段加载器实现，使用了一系列简单但巧妙的技术来隐藏自己。一旦安装，黑客可以管理员权限登录受感染的系统。

策划XZ Utils攻击的黑客组织（或个人）花费了数年时间来开发后门。除了隐蔽方法的复杂性，该组织还投入了大量时间为开源项目编写高质量代码，以赢得其他开发者的信任。

今年5月，Phylum阻止了另一个使用隐写术（将秘密代码嵌入图像中的技术）来植入后门的PyPI软件包攻击活动。

“在过去几年中，发布到开源生态系统的恶意软件包的复杂性和数量显著增加，”Phylum研究人员写道：“毫无疑问，这些攻击是成功的。开发者和企业必须高度警惕所使用的开源库。”

**参考链接：**

https://blog.phylum.io/fake-aws-packages-ship-command-and-control-malware-in-jpeg-files/

原文来源：GoUpSec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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