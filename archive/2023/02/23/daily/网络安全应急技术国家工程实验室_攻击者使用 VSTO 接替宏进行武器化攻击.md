---
title: 攻击者使用 VSTO 接替宏进行武器化攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247534764&idx=4&sn=3a77db01c27ef86105dc2e1784f50399&chksm=fa93fe6dcde4777bef9185b81748743adf2bf59983757b133a87349112a7cc7c5531d97ad2b0&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-02-23
fetch_date: 2025-10-04T07:52:01.250401
---

# 攻击者使用 VSTO 接替宏进行武器化攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kR03VqkY7LXQfSSde6NTVupyxKwz7ft7ialz4VXwCf1PcOuP97DgTk6myRwicnhibTyqDXtNBEHGglg/0?wx_fmt=jpeg)

# 攻击者使用 VSTO 接替宏进行武器化攻击

网络安全应急技术国家工程中心

几十年来，VBG 宏代码都是攻击者的核心工具。但自从微软开始默认阻止来自互联网的 Office 文件的所有 VBA 宏，这一攻击途径受到了极大的压制。由于攻击面的减少，攻击者必须探索替代的攻击媒介。近期的许多研究表明，LNK 文件已经受到了攻击者的青睐。此外，VSTO（Visual Studio Tools for Office） 文件也成为了重要的攻击媒介。

# **什么是 VSTO？**

微软的 Visual Studio IDE 中提供了一个软件开发工具集 VSTO，通过 VSTO 可以支持在 .NET 中开发 Office 加载项，还允许创建能够执行这些加载项的 Office 文档文件。

VSTO 加载项可以与为其开发的特定 Office 应用程序（Word、Excel 等）相关联，并将在每次启动该应用程序时执行，从而顺带实现了持久化的能力。

VSTO 加载项可以与 Office 文档关联在一起，也可以在打开 Office 文档时从远程获取，当然这可能触发与信任相关的安全机制。

# **武器化的 VSTO**

由于 VSTO 仍然不是一个重要的攻击向量，也没有被安全厂商加以重视，这可能会导致 VSTO 会越来越受欢迎。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFmccjlEctxFXykyH5mj2Zhs3fJ9NNv6oFrSw86xuo5G5BZQ1arTEUYA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

custom.xml 文件示例

带有 VSTO 的 Office 文件与不带有 VSTO 的 Office 文件的主要区别是含有 custom.xml，其中包含表明位置的 \_AssemblyLocation和 \_AssemblyName属性。

### **本地 VSTO**

本地的 VSTO 会将 .NET 编译的 .DLL 加载项及其依赖项与为执行它而创建的 Office 文档存放在一起，例如 ISO 文件中。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFC0I5m2CcIm3AnTlgFckMW6F5z9zbHgiaU6K1adUOguhdTYB4ZHCHKVg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

恶意 ISO 文件

例如针对葡萄牙语用户的恶意 ISO 文件，其中包含一个恶意的 Word 文档文件与隐藏的 VSTO 加载项及其依赖项。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFUb5De4YlknkZlGahKpjCZfhlicGwbOuelQcJh7aI2yl374HmaMk8PBw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

全部文件

一旦受害者打开恶意文档，就会提示用户安装加载项，与之前使用 VBA 宏时引诱用户启用内容十分相似。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFcgxFruZfRicaG3mmaHicmQc2SW8ucNiaMW2bGsM6U2W2vCXrborL2oP3A/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

提示用户安装

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFvhQEHFQzB8picLNzuwpVwjM0yibMcXjWAxYiaOgONiauWgvPHkBlCVFic2g/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

加载隐藏的加载项

一旦用户允许安装，加载项将被执行：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFynibDZedwaomZEOpocYyNibsNpNoRzVy93X5s5DBsCrRpB1ntAHmH9Yg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

VSTO 安装提示

分析加载项，其中有经过编码和压缩的 PowerShell 代码：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFuYN8ZS3cia6VFY84j0hWoscwzAZgorialQXLibibU5FseTl6EFia0vumgoA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

核心代码

经过解码和解压缩后，可以看到该段代码为了从 C&C 服务器拉取另一段 PowerShell 代码：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFAISCuibs8sn8ia1pBWhp7kjxteBDLfS0JdqcbYFlwicVNllvHIJXhH1Mw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

实际 PowerShell 代码

### **远程 VSTO**

远程的 VSTO 更加难以检测和预防，但攻击者需要考虑各种与信任有关的安全机制也导致了攻击更加复杂。

例如，恶意 Word 文档从远程获取 VSTO 加载项：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFZu4BGug8kXxdnKM9HLz0loOKH8f660jmfibZMtN5vVBIHlG3OZI9d6w/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

远程 VSTO

下载的 DLL 加载项中，嵌入了下载加密的 ZIP 文件的代码。解压后释放文件到 %\AppData\ Local\ 文件夹，并执行包含的 conhost.exe 文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38oCSgbk4YReN8bYh3XX8TFPHDicuUBxjbcW4zA8zpD9DIselLbOrvUibVdy45xo2PhnLErHDWicM6xQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

恶意代码

# **攻击的 POC**

为了促进社区的研究，研究人员公开了 POC 代码。

# **结论**

尽管 VSTO 在实际中并不常见，但由于其攻击能力的完整，研究人员认为未来会有更多的攻击者开始采用这种攻击向量，尤其是国家级攻击组织。

## IOC

> 5530F5D20016E3F0E6BBC7FAD83EEC56F118179D4C5D89FC26863C37482F8930
> E74DD27FF0BA050BBC006FD579B8022E07B570804588F0E861CC4B1321A3EC48
> 0526F63486DE882CCF33374DCA4B093219A8FD93014BABE794715F04FF49B151
> B3282DC58AD961911D94B712CEA11F649B0BA785D7FF74D7ED9946E1260DD521
> 40C9D3D58CE5DB0C6D18184E5813C980CD7B72EFC7505C53CD13E60860EF8157
> 78D6A2C0B52E9E5AF8007BC824EFD5846585A3056B3A0E6EFDFA7E60EED48C8C
> hxxps://34.241.171.114/
> hxxp://classicfonts.live/

## **参考来源：**

## https://www.deepinstinct.com/blog/no-macro-no-worries-vsto-being-weaponized-by-threat-actors

原文来源：FreeBuf

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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