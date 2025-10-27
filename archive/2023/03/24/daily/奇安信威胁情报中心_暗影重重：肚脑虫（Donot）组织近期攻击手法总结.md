---
title: 暗影重重：肚脑虫（Donot）组织近期攻击手法总结
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247505716&idx=1&sn=c351b71550874cae7bf11b5e5b67968f&chksm=ea662043dd11a955c2ecb8ef0328eb862d09d853decdab7cfaa0a78165fd18ae2f2bffd1d22e&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2023-03-24
fetch_date: 2025-10-04T10:29:52.614330
---

# 暗影重重：肚脑虫（Donot）组织近期攻击手法总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicicOInAzrPEfCF95KIeNQvJNx0O0GDxXTQYBDIY7UdOEoVmHKYT6r7heUEyjZszrusBiatuZQiaUibARw/0?wx_fmt=jpeg)

# 暗影重重：肚脑虫（Donot）组织近期攻击手法总结

原创

红雨滴团队

奇安信威胁情报中心

概述

肚脑虫组织，又名Donot，奇安信内部编号APT-Q-38，被认为具有南亚某国政府背景。该组织主要针对政府机构、国防军事部门以及商务领域重要人士实施网络间谍活动，受害者包括中国以及巴基斯坦、斯里兰卡等南亚地区国家。

奇安信威胁情报中心红雨滴团队在日常的威胁狩猎过程中发现，Donot组织的攻击活动从去年年末就保持着较高的频率，这个趋势一直延续到今年。在今年1月底，我们还捕获到该组织以克什米尔地区相关文档为诱饵的攻击样本[1]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7cc5jxHoyJzCedUgLZdviaT4Ztx5sMFCckO0ZZrGzoLmQ5atmjicG7CeA/640?wx_fmt=png)

在对近期捕获的Donot样本进行梳理后，我们发现该组织的主要攻击流程仍保持着一贯的风格，但攻击者也在尝试不同的恶意代码植入手段，变换着攻击组件的代码细节，因此本文将对Donot组织近期攻击手法做一个简单的汇总。

Donot常通过携带宏的文档执行shellcode下载后续DLL组件，进一步下载诸如木马插件管理器和木马插件的恶意DLL。在以克什米尔地区相关文档为诱饵的攻击样本中，攻击者则直接通过自解压rar压缩包投递下载器DLL组件。此外，在某些攻击活动中，Donot组织还使用EXE组件，借助宏文档直接释放压缩包，解压出其中的EXE组件下载后续。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7Rk3u5I5D4NN7sJ5yxicylmYN6SuibvQZhbUz3sfh1QDDZaRIZCW9v6EQ/640?wx_fmt=png)

DLL组件植入方式

**宏文档**

Donot使用的宏文档类样本其中部分文件信息如下表所示。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MD5** | **大小** | **文件名** | **VT****上传时间** | **文件创建时间** |
| 06adbb4ba31a52cc5c9258bf6d99812c | 144384字节 | REQUIREMENT LIST OF SPARES.xls | 2022-11-30 12:04:38 UTC | 2021-08-09 13:30:37 UTC |
| d98e2d7c8e91a9d8e87abe744f6d43f9 | 602624字节 | Monthly Action Plan.xls | 2022-12-22 10:42:28 UTC | 2021-08-09 13:30:37 UTC |
| c839d8a01c97407526b3407022823c8a | 603136字节 |  | 2023-01-24 05:10:11 UTC | 2021-08-09 13:30:37 UTC |
| 1c4fb7c41e7928bfb74784d910522771 | 91781字节 | PMDU Report 8-2-23.doc | 2023-02-13 08:59:03 UTC | 2021-03-30 12:06:00 UTC |
| e1d235c95a7c06b1203048972cf179fa | 69296字节 | Cyber Security Instructions.doc | 2023-02-28 05:22:09 UTC | 2021-03-30 12:06:00 UTC |
| 6de75b200652eefa4a6a3bb84da7f798 | 603136字节 | TRAINING NOMINATION.xls | 2023-03-02 04:09:53 UTC | 2021-08-09 13:30:37 UTC |
| 0ec8911f9764ea7b254ea19cd171535e | 87870字节 |  | 2023-03-03 10:01:33 UTC | 2021-03-30 12:06:00 UTC |

从上面可以看出，xls和docx类文档分别具有一致的创建时间，说明这些攻击样本可能基于相同的原始文档生成。

**(1) VBA**

以上述样本（MD5: d98e2d7c8e91a9d8e87abe744f6d43f9）为例进行分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG721h6lfKQicJeWWW6LsFgVDAFH2GJiaC7DQLmicicO9QE1vfhAdE4qyianYg/640?wx_fmt=png)

VBA代码以字母ijl大小写生成的名称对变量名和函数名进行混淆，调用NtAllocateVirtualMemory分配内存，通过WideCharToMultiByte函数将编码后的shellcode按照文档使用的字符编码方式进行解码，然后调用EnumUILanguages函数执行shellcode。具体解码执行的shellcode根据系统位数而定。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7cibiaI1oyO9BPMxGDhEHjl2DwEKZ0DdcuDNxPqJ0tzaWE4DcEfZtx7xg/640?wx_fmt=png)

**(2) Shellcode**

以64位版本的shellcode为例，首先进行自解密操作，解密方式为按字节取反再异或。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicOInAzrPEfCF95KIeNQvJNzFqpHiaI8eoY10ZJpLFO9mTYQRydCY2x6ha62X4tUt5LGCcAn1lOO9w/640?wx_fmt=png)

通过hash导入API，导入时会异或0xBAADC0D3。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7x2UH11dAiaO5wSTlbLUb9SPHH8QAMETiaL5EkhtTdPLdljfLfGr6xpicg/640?wx_fmt=png)

调用urlmon.dll模块的URLDownloadToCacheFileA函数下载后续，后续URL如下：

|  |
| --- |
| http://orangevisitorss.buzz/QcM8y7FsH12BUbxY/XNJxFhZdMSJzq1tRyF47ZXLIdqNGRqiHQQHL6DJIjl2IoxUA**.png** |

下载的后续以文件读取的方式载入内存，同样执行按字节取反并异或的解密操作，对解密数据的首字节进行校验，校验通过则执行解密数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7UGVN8Tkgjq066LPEod2RpfMlIetHYumx0THHPXr7d0VSfqeiaWDxSLQ/640?wx_fmt=png)

获取的第二阶段shellcode首先按字节异或进行自解密，然后导入相关API。调用Wow64DisableWow64FsRedirection关闭文件系统重定向。通过GetLocalTime获取系统时间，如果当前时间大于硬编码的日期则shellcode结束运行。如下图所示，下面硬编码的日期为0x7e70214，可分解为0x07e7-0x02-0x14，转换为10进制为2023-02-20。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7WpiaNEJYXu8VsR2R0zVWtA8fHKpovH1rcHGbVwEETojovDFTG1ohHxw/640?wx_fmt=png)

依次检查各个杀软驱动文件在”C:\Windows\System32\drivers”目录下是否存在。如果某个杀软驱动存在，则根据当前日期是否大于相应内置时间点决定给该杀软有关的标记变量赋值：小于等于该时间点赋值为1，大于则为2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7mctjJLcIqTibm3DKJjNQvKT5EODa11G3Exich3eEgBLhmlj6CNicibLMhg/640?wx_fmt=png)

|  |  |
| --- | --- |
| **杀软驱动文件名称** | **相关厂商** |
| gzflt.sys | Bitdefender |
| klif.sys | Kaspersky |
| ehdrv.sys | ESET |
| aswsp.sys | Avast |
| bsfs.sys | Quick Heal |
| 360AvFlt.sys | 360 |

无任何杀软的情况下，调用URLDownloadToFileA下载后续载荷，保存为当前用户temp目录下的Unincored.dll文件，即”%tmp%\Unincored.dll”。获取后续的URL为：

|  |
| --- |
| http://orangevisitorss.buzz/QcM8y7FsH12BUbxY/XNJxFhZdMSJzq1tRyF47ZXLIdqNGRqiHQQHL6DJIjl2IoxUA**.mp4** |

打开下载文件，将文件前4字节修改为”4D 5A 90 00”，修复PE文件头部。LoadLibraryA加载该DLL，GetProcAddress获取指定导出函数地址（tripoliro），调用该导出函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7TtOctuxbbdj1YlaqiaicICdP9N1fYGiaLHfTUibq882Drt7Mzh2YUCVFicQ/640?wx_fmt=png)

在有杀软存在的情况下，如果相应标记变量为2，则直接通过执行int3中断或者其他指令触发中断或异常，终止shellcode运行。如果标记变量为1，某些杀软对应的shellcode执行情况与无杀软时一致；而在另一些杀软存在时，会加载bcrypt.dll，将后续shellcode复制到bcrypt.dll映射的内存中执行。

宏代码启动的32位版本shellcode与64位基本一致，不过下载后续shellcode和DLL载荷的URL有所不同。

|  |  |
| --- | --- |
| **后续载荷类型** | **URL** |
| Shellcode | http://orangevisitorss.buzz/QcM8y7FsH12BUbxY/XNJxFhZdMSJzq1tRyF47ZXLIdqNGRqiHQQHL6DJIjl2IoxUA**.ico** |
| DLL | http://orangevisitorss.buzz/QcM8y7FsH12BUbxY/XNJxFhZdMSJzq1tRyF47ZXLIdqNGRqiHQQHL6DJIjl2IoxUA**.mp3** |

**SFX文件**

SFX文件基本信息如下。

|  |  |
| --- | --- |
| **文件名** | Kashmir Solidarity Day  Material .exe |
| **MD5** | 4eaa63dd65fc699260306c743b46303b |
| **文件类型** | WinRAR SFX |
| **文件大小** | 1684242字节 |

该自解压文件使用文件夹图标进行伪装，运行后在temp目录下释放，通过rundll32.exe执行其中DLL组件的导出函数，并打开压缩包中包含PDF诱饵文档的文件夹“Kashmir”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7ibMuYlozFDLmycKUiax5T85xl9TcTo9grfhO7HjUAnm83fZXia6xHibNTA/640?wx_fmt=png)

DLL组件分析

Donot组织使用的DLL组件大部分时候是“下载器-插件管理器-插件“的经典三步流程，不过也出现过率先植入的DLL组件为插件下载器这种情况。

**DLL三部曲**

以上面SFX样本植入的DLL组件攻击流程为例进行分析。

**(1) 下载器**

使用的下载器DLL信息如下。

|  |  |
| --- | --- |
| **文件名** | dn2272iosUp.dll |
| **MD5** | 07a3c19bc67c5f44c888ce75d4147ecf |
| **文件类型** | pe32 dll |
| **文件大小** | 296960字节 |
| **编译时间** | 2023-01-10  14:16:06 UTC |

下载器DLL一般有两个导出函数：其中一个导出函数通过设置计划任务启动另一个导出函数；而另一个导出函数则向C2服务器回传收集的主机信息，下载并执行作为插件管理器的DLL组件。

SFX文件调用dn2272iosUp.dll的导出函数StTskloipy。该函数将DLL当前文件路径经AES加密后写入”C:\Users\[user]\AppData\Local\windin.txt”。如果该DLL在当前用户的temp目录中不存在，则复制到temp目录下。然后通过COM接口设置计划任务调用另一个导出函数SDtuiopnhukm。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7TYNfDrCPibjEHyCKYtUb9JLF41b1GYcpv1icswLDaKYK6xPib8qhh0Aug/640?wx_fmt=png)

除了直接调用COM接口，Donot组织在其他下载器DLL中还采用过释放并执行bat文件的方式设置计划任务。释放的bat文件运行schtasks命令，执行完毕再将bat文件删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7UZ21ht81nwOsaHF4xMkMyNjesicFr6n9InYUicGzjlYEg07gy24fPiacw/640?wx_fmt=png)

下载器dn2272iosUp.dll的另一个导出函数SDtuiopnhukm先创建互斥量"olgui1Pigg"保证单例运行。创建”C:\Users\[user]\AppData\Local\Nsget\”目录。通过注册表收集本机安装的软件信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7HO5K910rd9riaZvIJAibnbyvrJx5TMibtic4DaKuYUAQiaaP4kUeagbHbfA/640?wx_fmt=png)

获取当前用户名、计算机名，以及通过cpuid指令获取CPU标识信息，将这三者组合为受害者标识（victim id）。拼接victim id和收集的软件信息，并以”|||S4”为结尾标识符，对这些信息进行AES加密并用Base64编码。加密数据作为POST请求的batac参数发送给C2服务器。回传信息的URL如下：

|  |
| --- |
| https://briefdeal.buzz/Treolekomana/recopereta |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7ErcKN78QZRObn6zV7oj2ltWpHEwBOdS2qiaEjSDOoYegwUPljENia4fw/640?wx_fmt=png)

如果C2服务器有响应，则请求下载后续组件WingMndre.dll。拼接victim id和后续组件的名字，加密后作为POST请求的data参数。下载后续DLL的URL如下：

|  |
| --- |
| https://briefdeal.buzz/Likorecasta/mikachar |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7CvtygN7tU3WJHHoRj7RHHhhBTuDD13c1qPe16b9SvbB0enwXUrsLDQ/640?wx_fmt=png)

若下载成功，将WingMndre.dll保存在之前创建的Nsget目录下。删除导出函数StTskloipy执行时释放的windin.txt文件，设置计划任务调用WingMndre.dll的StConectert导出函数。因为该计划任务与运行导出函数SDtuiopnhukm时设置的计划任务同名（”OneDriveUpdaton”），相当于更改原计划任务的执行内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9bvicw2X68rm9VcahTPlFG7POgv6A7TpVlzrc36XKVK6w8ibKicaUArJk613vqdf5PcicBTexSHwafRg/640?wx_fmt=png)

在Nsget目录下释放Uwn.txt文件，保存AES加密后的victim id。然后通过CreateProcessW调用如下格式化字符串，删除当前DLL在磁盘上的文件。

|  |
| --- |
| cmd.exe /C ping 1.1.1.1 -n 1 -w 30...