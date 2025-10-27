---
title: APT-C-00（海莲花）双重加载器及同源VMP加载器分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247500701&idx=1&sn=7f4644119574e433a29d215a70658f6b&chksm=f9c1f094ceb67982f950b7569be3d9f5ff176d741f1bef4ea2e4fc412305a4dd04bdc7b869fb&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-09-24
fetch_date: 2025-10-06T18:30:12.712743
---

# APT-C-00（海莲花）双重加载器及同源VMP加载器分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PrFdmqzCficVLRXUAicEpLZ5qibIKp9rbibYPicW487AbzJTxkhsvNtrlVkdLsSxQwk9CxbNxRYtMdeVyw/0?wx_fmt=jpeg)

# APT-C-00（海莲花）双重加载器及同源VMP加载器分析

高级威胁研究院

360威胁情报中心

##

**APT-C-00**

**海莲花**

APT-C-00（海莲花）（也称OceanLotus）组织是一个有政府背景的境外黑客组织，自2015年360曝光海莲花以来，360高级威胁研究院一直持续跟进监测海莲花组织的最新攻击。

360高级威胁研究院在APT威胁狩猎中发现并捕获了2024年海莲花针对高价值目标发起的网络攻击。此次攻击中与以往不同的是海莲花对使用近两年半的双重后门加载器进行了“加工”，利用VMProtect软件对加载器进行了加壳保护，在反静/动态分析层面进一步加强了安全对抗程度。

## **样本分析**

### **1. 双重加载器**

* #### **模块1**

|  |  |
| --- | --- |
| MD5 | 2109479e62f3c45bab00768553b158b8 |
| 文件类型 | DLL动态链接库 |
| 文件大小 | 225280  Bytes |
| 编译信息 | MSVC |

该模块是一个MSVC DLL文件，通过分析可以发现该DLL是在Visual Studio生成的默认桌面应用程序项目基础上进行修改和“加料”，主要工作流程如下:

首先，攻击者会收集主机名和磁盘信息；

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79AeibIeMfP39mUxicXEq4Rmh510XmgVPIxdfxxib571mzHtQ6yhHxiagc6w/640?wx_fmt=png)

然后创建目录%Temp%\NVidiaSetup\kd8812u，以文件流的方式写入此前收集的主机信息，在等待一定时长后调用函数ShellExecute打印文件流，其寓意暂时未知。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79eNnnlMmvelcVBBGT2b0vGkpyyPa7p9tFpXWgiaadIuMsFP65sWTC02g/640?wx_fmt=png)

随后则是加载一个包含加密载荷的DLL文件，参数为加载的DLL文件模块句柄和解密Key，参数格式：小写十六进制模块句柄\_解密Key。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79LYgn3jAUKzOOL8puepvsz1aGdWDiblBR1f35YpYoAQYoGhiaBGF09bJA/640?wx_fmt=png)

* #### **模块2**

|  |  |
| --- | --- |
| MD5 | d21c4b1c1db2c9f443c4ba271f738c91 |
| 文件类型 | DLL动态链接库 |
| 文件大小 | 2503168 Bytes |
| 编译信息 | GoLang |

该模块由Go语言编写，其中包含多个开源项目，主要工作流程如下：

利用开源项目gopsutil[1]收集主机信息并写到指定路径。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79T7vtyTg4NWfSEteQOGhvaFs54rbBP4OeiaMib06tgghicc0iaYBKqCfFEA/640?wx_fmt=png)

利用开源项目screenshot[2]截取屏幕图像并写到指定路径，截屏图像的路径则写入如上提到的信息收集文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79QRy6PvlcCXgolBrKA6uMx7u8lSAKLiawL3RZyFXVoGx4g9Vgp4iaNrYQ/640?wx_fmt=png)

接下来是该组件的主要流程，解密并执行恶意载荷。

首先将上级MSVC加载器传入的解密Key进行十六进制解码。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79tRmIY5EbTJOzHqYhGNxJsicCuy8mH3HDhMZSWng4PhHgMeHiaXF8dexA/640?wx_fmt=png)

然后解码资源中的Base64编码数据，再利用解密Key解密恶意载荷（此处使用的是RC4算法），最后调用恶意载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79EKCJYh6LgVndy1upefCks2cZ8DntMcQkia7iaLwxWzsNsmVQCY9jax8g/640?wx_fmt=png)

* #### **载荷**

恶意载荷共有两段，第一段载荷功能主要为循环解密并调用第二段载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79H9laphAPJDib5ZxOfEOW87b9Ioicm94F0b3F59AemCn0byHl639nc8OA/640?wx_fmt=png)

第二段载荷则主要是反射加载CobaltStrike Beacon模块。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79yiaYsxUzRldxyrjrNLzfFEMTIjUib0iabys08QymLIDYAc6XFj81Y56Vw/640?wx_fmt=png)

通过解析Beacon模块配置信息可知C2：strengthening-memories-reports-restoration.trycloudflare.com:443。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79mWlSCZOWkEGmLDWFw4UJ0lunqNu4ANPtLWEqhibKf6FntfLZiaLafpxg/640?wx_fmt=png)

### **2. VMP双重加载器**

在日常APT狩猎中我们发现了一组后门加载器，第一时间进行分析后确认了这组加载器是海莲花双重加载器的VMP版本。

*（以下对比图左侧均为无壳加载器，右侧均为VMP加载器代码中未被VM或混淆的部分。）*

* #### **模块1**

|  |  |
| --- | --- |
| MD5 | 26669891d83b8a706d2c0af91292247c |
| 文件类型 | DLL动态链接库 |
| 文件大小 | 7072768 Bytes |
| 保护器 | VMProtect 3.XX x64 |

通过绝对路径加载GoLang恶意模块部分代码对比：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrFdmqzCficVLRXUAicEpLZ5qv51LOjQUJUMqrZ2ltJjxmtheNhxDS2rQs0SZgSgZ5iaRe0ocrde56fQ/640?wx_fmt=png&from=appmsg)

* #### **模块2**

|  |  |
| --- | --- |
| MD5 | 4ce5ea38c4d486bed7f6d9e9208133c6 |
| 文件类型 | DLL动态链接库 |
| 文件大小 | 8276480 Bytes |
| 保护器 | VMProtect 3.XX x64 |

Base64解码及解密恶意载荷部分代码对比：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo79EPUicwPUqazqtkvDQG9XpMRnogJ2ccfV7nsXBib2LfahzHjzu4GEdZgw/640?wx_fmt=png)

* #### **载荷**

解密第二阶段恶意载荷部分代码对比：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo796PEpqzmFibpDwIOxfTUdtAsjPicFqe1ZXtK80SmeiaiatcepsLtcvFKsjg/640?wx_fmt=png)

最后同样是反射加载CobaltStrike Beacon模块，通过解析Beacon模块配置信息可知C2：64.176.58.16:80。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp5RaiaPLRVjG7KBrd5kRo792KAe0XPGia2UicJgM1W9PV88RbsWx3XWf9oCx5A6htJW9m2oEa35TlSw/640?wx_fmt=png)

##

**总结**

近年APT组织皆有使用Rust、Nim、GoLang等多种编程语言开发后门程序的先例，海莲花组织执行假旗行动的效果较为显著，将攻击细节[3][4]模仿为已披露的APT组织（APT29、Gamaredon等），目的就是诱导安全人员错误的归属攻击，淡化自身的活跃度。本次攻击活动在VMP源代码泄露后使用其保护加载器，也让分析成本大大增加。因此我们可以预见未来在捕获攻击，样本分析，归属研判等方面或将面临巨大的挑战。

**附录 IOC**

**MD5**

4a8756b22029a88506744ab7864c9b83

2109479e62f3c45bab00768553b158b8

d21c4b1c1db2c9f443c4ba271f738c91

9ad37ce054ca1523d26bb49fbc80dff6

26669891d83b8a706d2c0af91292247c

4ce5ea38c4d486bed7f6d9e9208133c6

**C&C**

strengthening-memories-reports-restoration.trycloudflare.com:443

64.176.58.16:80

##

**参考**

[1] https://github.com/shirou/gopsutil

[2] https://github.com/kbinani/screenshot

[3] https://mp.weixin.qq.com/s/IB2w86cXcpmGS8qrOnprKw

[4] https://ti.defender.microsoft.com/articles/541a465f

**团队介绍**

TEAM INTRODUCTION

**360****高级威胁研究院**

360高级威胁研究院是360政企安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

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