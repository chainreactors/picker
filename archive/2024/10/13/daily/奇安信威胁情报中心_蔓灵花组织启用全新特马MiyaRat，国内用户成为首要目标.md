---
title: 蔓灵花组织启用全新特马MiyaRat，国内用户成为首要目标
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247512724&idx=1&sn=38ec4601ee12df8b038639ad4b4020f1&chksm=ea6645e3dd11ccf579a0b7c6242eff2151902ad3f444967659ee83dacd08552de84e5a8f0887&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-10-13
fetch_date: 2025-10-06T18:51:09.766828
---

# 蔓灵花组织启用全新特马MiyaRat，国内用户成为首要目标

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwrYicea7RnLR9C0eBNZJQeddRrckLuaUHGY7K9O87DQWJicKeojE257qg/0?wx_fmt=jpeg)

# 蔓灵花组织启用全新特马MiyaRat，国内用户成为首要目标

原创

威胁情报中心

奇安信威胁情报中心

概述

奇安信威胁情报中心一直在持续跟踪南亚方向的众 多 APT 攻击集合，发表了多篇系统性的技术报告：Operation Magichm[1]、Operation Angi[2]、operation Tejas[3]等，从 2019 年至今这些组织的手法几乎没有太大的变化，攻击技术上限较低，但通过广撒网的钓鱼模式仍能对政企客户造成一定程度的影响。

如何免杀是 Bitter 组织（APT-Q-37）一直以来为之奋斗的首要目标，抛开初始攻击载荷 chm、lnk 等过时技术不谈，仅后续下发的 wmrat 和 .net 特马都很难绕过特征查杀功能，攻击者在今年一直在尝试各种方法：6 月份通过 powershell 加载 havoc 框架、7 月份直接下发 2018 年就在使用的窃密插件，效果都不太理想，最终在 9 月份下发了全新的特马 MiyaRat 并被我们成功捕获。

我们建议政企客户在办公区和服务器区同时部署天擎EDR，在开启云查功能下可以实现对 chm、lnk 等通用威胁的发现和拦截。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwWABYT2Dia266OMP9yF26jGiaDzaTtqqjAcsicDOKYzbQCTNs1bLBiaaZqg/640?wx_fmt=png&from=appmsg)

MiyaRat指令分析

Bitter 使用的新型木马基本信息如下，PDB 显示该木马被攻击者命名为 “Miya”，当前版本为 1.1。

|  |  |
| --- | --- |
| **MD5** | 6edc889abbc186fbd5e187818d916dee |
| **文件名** | mspnx.exe |
| **文件大小** | 410.00  KB (419840字节) |
| **PDB路径** | C:\DRIVE\_Y\EDRIVE\repos\Miyav1.1\_client\_msi\Release\Miya1.1\_client.pdb |

该木马由 MSI 文件释放，MSI 文件信息如下：

|  |  |
| --- | --- |
| **MD5** | 5ff5e38943a134847e762f480dc84e09 |
| **文件名** | mspnx.msi |
| **文件大小** | 466.00  KB (477184字节) |
| **下载链接** | hxxp://locklearhealthapp.com/mspnx.msi |

木马首先解密出 C2 域名 "samsnewlooker.com"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRw8miaytxp4lVFmQbT0JNOTqQHaeRibHricEdr2ibPMNiaaiasHDK4cBhomMwQ/640?wx_fmt=png&from=appmsg)

解密方式为按字节减去 key，用于解密的 key 被设为 "doobiedoodoozie"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwW8VKibxgdBL2Zfr03pLc3R9Ha3VVRPp2icODD92Ih7bsBuykOibcT3Spw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwBASmapXSFrichibTbp4MgI2eAqmPiaRryS9y1KTok6oicsVdQiaUmCsywtQ/640?wx_fmt=png&from=appmsg)

木马的主体功能在函数 sub\_406960 中，调用 WSAConnectByNameW 连接 C2 服务器的 56172 端口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwkmDricvCLzD0DkXPoXPprk2bR9gEyoLlOfCjhgc9NOS8b39z7JoEcYw/640?wx_fmt=png&from=appmsg)

收集一系列信息发送给 C2 服务器，包括：磁盘信息、机器名、用户名、木马文件路径、%userprofile%环境变量、系统版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwPagIhsmdoewnK1HBfMAgR9opOQXtibXJCDmD4ksv3eLtYL9crJR2Otw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRw9CsbMnQKt6qLljDTBWDpGR7Yibhn1uZcRRzQOMMyVaXyiaGYo832CIibw/640?wx_fmt=png&from=appmsg)

发送完收集的信息后，木马进入等待接收C2服务器下发指令的循环过程。木马支持的功能包括：文件信息枚举、命令执行、文件上传和下载、截屏等。下面对该木马涉及的指令依次进行介绍。

木马指令整理如下：

|  |  |
| --- | --- |
| **指令代码** | **功能** |
| GDIR | 列举指定目录下的文件和子目录信息，不遍历子目录 |
| DELz | 删除指定文件 |
| GFS | 递归枚举指定目录的所有文件信息 |
| SH1cmd | 创建命令执行的shell |
| SH1, SH2 | 将命令传入shell |
| SFS | 连接C2服务器指定端口进行文件传输操作，二级指令UPL1上传文件，DWNL下载文件 |
| GSS | 截屏 |
| SH1exit\_client | 退出木马进程 |

**（1）GDIR**

列举指定目录下的文件和子目录信息，类似 Windows 的 dir 命令或 Linux 的 ls 命令。列举信息包括文件和子目录名称、最近修改时间以及文件大小。目录枚举信息以 "[END]~!@" 结尾。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwYnNyhDicibmxzbtx96mx1w8uPiaxbq6BAudfNSPpt4ZhgPeIcRjhAyEqg/640?wx_fmt=png&from=appmsg)

**（2）DELz**

删除指定文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRw3aZNvshmppqaN4eUcia0zXVPZDAEibnCG5naphfALN8LRjicqhdDlOQEA/640?wx_fmt=png&from=appmsg)

**（3）GFS**

递归枚举指定目录的所有文件信息，包括每个文件的路径和大小。在发送给 C2 服务器信息的首行包含所有文件的总大小，输出信息用 "@@GFS" 标识。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwpxicbmpXlkEkGkxgjlRNVleOb65E7ujOUQuiaVAN53qbeUrLyDbraYcQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwyqcUQsHfTvO2PdWPCwBuRos1Vor2sRZ94PRfwfPfibpMEKR3BmllVJg/640?wx_fmt=png&from=appmsg)

**（4）SH1cmd**

创建一个 cmd.exe 进程作为 shell，执行管道传入的 cmd 指令，并将执行结果返回给 C2 服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwibksSvEjABtsAAvzQbyHoaLbeAby1llzxzJG9uiaI5Q9ia2bRzLDXuFWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwvwJdlSqIer2VzSdEXLqC8ib2ZmrNyISpfHSSGMWPtj6kiaxDBlXrdMaA/640?wx_fmt=png&from=appmsg)

**（5）SH1 & SH2**

SH1 和 SH2 两个指令功能几乎一致，将参数携带的 cmd 指令写入命令管道，用于 shell 执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwzJgxAaJ35dicjWjwuAjU4XcCXBlYYTDVcKFX3TvB9KN2PicC9QgmDFMw/640?wx_fmt=png&from=appmsg)

**（6）SFS**

SFS 指令用于上传和下载文件，但该指令并不直接执行文件传输操作。该指令的参数为端口号，在 sub\_404640（MwFileOp）函数中调用 WSAConnectByNameW 连接同一 C2 服务器的另一个指定端口，木马与该端口进行文件传输。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwjflXN7IkdjAoaiaGNvLiaWLvQwtguiamFKnueLaG2A9Vljsn9aUICmY1A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwiaUvicOgPcPUFR4kibSLf5ssic3KUoUnj9blyCTG2WrRR9fiapt61GVibTtQ/640?wx_fmt=png&from=appmsg)

MwFileOp 函数有两个二级指令 "UPL1" 和 "DWNL"，分别完成文件上传和下载操作。

|  |  |
| --- | --- |
| **文件传输指令** | **格式** |
| UPL1 | UPL1 <上传文件路径> |
| DWNL | DWNL  <下载文件保存路径>,filesize==<接收文件大小> |

在文件下载过程中，C2 服务器如果发送 "CANCEL2"，木马可以提前结束文件下载，不用等待接收完指定数量的文件数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwfX7xEP8dLRc0Bs4ExUOK777Icdln0fB6hnib7hQV0BoKkHAE0NU3Hpw/640?wx_fmt=png&from=appmsg)

**（7）GSS**

获取截屏，该指令的参数可以选择截屏保存图片的分辨率。输出信息用 "~!@SSS" 和 "~!@SSE" 标识截屏数据的开始和结束位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwOI0jk0YJjzkElaLgHZdBz3GIlnREU1rc9eIORia80t4Dj7jMXhAPdaA/640?wx_fmt=png&from=appmsg)

**（8）SH1exit\_client**

退出木马进程。

总结

目前，基于奇安信威胁情报中心的威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、天擎、天眼高级威胁检测系统、奇安信NGSOC、奇安信态势感知等，都已经支持对此类攻击的精确检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic92CksbuNBxQFsb0h1sHJRw3zVrB9C3V4Z0OYohs5JJ9Jr7GbRfEWibmrrecz79TeWKT3YUShy4I9Q/640?wx_fmt=png&from=appmsg)

IOC

**MD5：**

6edc889abbc186fbd5e187818d916dee

b45c97ae0af336048529b8a3ef1749a5

0b8a556b9ce94a0559f153bf62ba2693

d9159838e82ea73effc18ef5b958dacd

26ed92fef383dfea8c40e4fd38668379

**CC：**

23.26.55.9:443(havoc)

samsnewlooker.com

96.9.215.155:56172

wmiapcservice.com

185.106.123.198:40269

locklearhealthapp.com

**URL：**

https://maxnursesolutions.com/cssvr.jpg

https://nurekleindesign.com/toronto.bin

https://viyoappmapper.com/flv.ol

https://locklearhealthapp.com/mspnx.msi

https://locklearhealthapp.com/mayred.msi

参考链接

[1].https://ti.qianxin.com/blog/articles/%22operation-magichm%22:CHM-file-release-and-subsequent-operation-of-BITTER-organization/

[2].https://www.secrss.com/articles/31785

[3].https://ti.qianxin.com/blog/articles/operation-tejas-a-dead-elephant-curled-up-in-the-kunlun-mountains/

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehic92CksbuNBxQFsb0h1sHJRwCNrPJr9yIk5K0juKwLTt7KsQK3mbx4ibcWIWl3ia7vMPMJrZyo4aibAfg/640?wx_fmt=gif&from=appmsg)

点击阅读原文至**ALPHA 7.0**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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