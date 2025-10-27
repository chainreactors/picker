---
title: 肚脑虫（APT-Q-38）利用PDF文档诱饵的攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247514233&idx=1&sn=2e063a4d1143fd6d6bd6bc3de546ff9e&chksm=ea664f0edd11c618b26d39c18cfd8dc829d09528cbf18acff05712d7725061026f88f8e4b691&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2025-03-01
fetch_date: 2025-10-06T21:58:54.340331
---

# 肚脑虫（APT-Q-38）利用PDF文档诱饵的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicico9dEf1d11YZyASCmEbRMBjreWYLZGkpiastQjbpK4S9o3y2H3OBSHmzL6sibXcvBc3IRlhOdWr6aw/0?wx_fmt=jpeg)

# 肚脑虫（APT-Q-38）利用PDF文档诱饵的攻击活动分析

原创

红雨滴团队

奇安信威胁情报中心

团伙背景

肚脑虫，又名Donot，奇安信内部跟踪编号APT-Q-38。该组织主要针对巴基斯坦、孟加拉国、斯里兰卡等南亚地区国家，对政府机构、国防军事、外交部门以及商务领域重要人士实施网络间谍活动，窃取敏感信息。肚脑虫组织具有Windows与Android双平台攻击能力，在以往攻击活动中经常通过携带Office漏洞或者恶意宏文档的鱼叉邮件和安卓APK传播恶意代码。

事件概述

奇安信威胁情报中心近期发现肚脑虫组织利用PDF文档作为攻击活动的诱饵，可能影响巴基斯坦、孟加拉国等南亚地区的国家。攻击者使用攻击手法具体有两种：第一种是将恶意EXE文件直接用PDF图标伪装，使受害者误以为是PDF文档从而打开运行；另一种方式相对要繁琐一些，诱饵PDF文档中内置获取恶意PPT的钓鱼链接，恶意PPT被受害者下载并启动后将执行宏代码。第二种攻击方式除了在最初阶段使用PDF诱饵，其余环节与之前的肚脑虫直接投递恶意宏文档的攻击活动一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBWMW135pFe4rHqcneKNewC5ANYbnASpB9mfL7u0rwrpDy73BJztC7MA/640?wx_fmt=png&from=appmsg)

诱饵PDF文档故意模糊内容，并通过伪造的提示信息告诉受害者，如果想查看文档内容，需要点击“下载”联网获取。一旦受害者按照指示点击PDF中的指定区域，则会触发网络访问，链接最终会重定向到下载恶意PPT的网页。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBPE61hEOvhNDlQk2SovlMwMq1iaMAONQdtqghGB0ufXSmYn79JTBpsGw/640?wx_fmt=png&from=appmsg)

伪装为PDF的EXE

直接伪装为PDF文档的EXE恶意程序基本信息如下，在进行详细分析前先借助奇安信情报沙箱（https://sandbox.ti.qianxin.com/sandbox/page）获取该样本的初步信息。

|  |  |
| --- | --- |
| **奇安信情报沙箱报告链接** | https://sandbox.ti.qianxin.com/sandbox/page/detail?type=file&id=AZT5fv50h6wn\_HCy8ts6 |
| **样本文件名** | - |
| **样本****MD5** | 893561ff6d17f1e95897b894dde29a2a |
| **样本类型** | PE32 EXE |
| **样本大小** | 1.85 MB (1942112字节) |

**沙箱分析**

将该样本上传到奇安信情报沙箱分析后，沙箱基于智能的恶意行为综合判断给出了10分的恶意评分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBGYeXASjOZicDaJ5k9ntGRQgLeWoUs5Eibibklug4w5LWKL4wUsxcEQbYQ/640?wx_fmt=png&from=appmsg)

行为异常部分显示样本的一些可疑行为，包括向totalservices[.]info发送POST请求，释放名为djkggosj.bat的BAT文件，并用cmd.exe执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBic4nxzGMIVzSf5hFkB3WRrib6pwWetHAIAYazib8853oiaXfaxOK7hZliaw/640?wx_fmt=png&from=appmsg)

样本为EXE，但使用PDF图标，显然攻击者想以此作为伪装。此外，样本的文件元数据使用游戏程序相关信息，并携带名为"Ebo Sky Tech Inc"的数字签名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBwgI0vibLS9R3ia7oJAMCA5hBnn0Flv7xpd5ff9LbY3PZGQqNRsOkC6VQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBKHFrwXhq1gd8ibgweLoCXRvra9Y77fgjCRu3L58owaiaKO7sQ21iakJuw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMB0qqic8nj7BhLYUV9O2FjInGSScRcwZtT6hs3klaZyjZsAsn1cwMGqiaw/640?wx_fmt=png&from=appmsg)

沙箱运行结果的主机行为部分可以看到样本进程派生cmd.exe子进程执行BAT文件，而BAT文件存放在样本创建的FROX目录中。样本进程的释放文件列表和删除文件列表均出现该BAT文件，表明BAT文件在执行后会被删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBjaXFiauP2ib2wKYLAF4uqKiaejicd3AM9DzZFx1AJVoSyA4MlnVcmaSS1g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBrncyqkpQiaX1EvDzEqO90NXnbEyhAJ1dVokPwW9cXsdmhjeVLJOPplw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBhEWNcA9o3N5x0yTG0Vwiao0YlxIB1LB3RWACj0PxoXZNRaoALBdu4AA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBxJ8iaBoB2G2dWhD5czWkmoNzF0YKMZZ7yicSlSlk4wJj8tjWJ6qKZlLA/640?wx_fmt=png&from=appmsg)

网络行为显示样本与远程服务器totalservices[.]info产生HTTPS通信，发送POST请求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBxPTU1aDynL9pYstHiaUEkbKsx27myhLicJIibVEwm8DtNuH7WF7ianJNXQ/640?wx_fmt=png&from=appmsg)

**详细分析**

样本中出现大量01字符串，这些字符串实际由原始字符串中每个字符的ASCII码二进制形式组成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBScvVWtibq5iagicowIvyndBcPH6zsjNzY5W4y8BMJ5OwxzW5XFM32licuA/640?wx_fmt=png&from=appmsg)

以这种方式编码的字符串其中一部分是用于异或解密的key，这些key被用来还原样本导入的API名称等字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBjcLe1wkqUeoBcGewetgO8s5VTcnqlk8C2u2aB3ibBLwoSTn6ib7mo9jA/640?wx_fmt=png&from=appmsg)

样本首先创建"%LocalAppdata%\\TEMP\\FROX\\"目录，在该目录中释放djkggosj.bat。BAT文件中的代码设置名为PerformTaskMaintain的计划任务，实现样本自身的持久化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBq5pafFnMKGve80VcURw8HwCaOVxUZcic0GtDW2xKS1IQZu5iaKDtuhfQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBWI6RAExKym3PlRaQ6gjc8jNM6ibQOLjGJMoqbFmC5eTgib6xiaQywBjeg/640?wx_fmt=png&from=appmsg)

然后创建互斥量"08808"，并收集设备信息，包括：CPU型号、操作系统产品名称和build number、用户名、主机名、CPU的ProcessorID、安装的软件列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMB6gicfFOmkUoxicIol9j5CvgFTPbKwOxuSkIEBOIHfMKvS1wWoW3iaaqibQ/640?wx_fmt=png&from=appmsg)

收集的信息经过AES加密和Base64编码处理，拼接到"batac="之后，作为POST请求的数据，发送到"hxxps://totalservices.info/WxporesjaTexopManor/ptomekasresdkolertys"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBJkFiaKk7vWEMeMYocKEicGqXeJJ2uPobVWIVqwQbJfTblybpJ1c88XMA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBpcwzMhkBaH8xiaaL8J5V5QcR52kaanqrLTwq1SogChsFTkAEic1lB6oQ/640?wx_fmt=png&from=appmsg)

恶意软件根据C2服务器的响应决定是否下载后续载荷。后续载荷名称为socker.dll，与标识受害者ID的字符串（由用户名、主机名、ProcessorID组成）拼接并加密后，作为POST请求"data"字段的数据。下载后续的URL为"hxxps://totalservices.info/vrptpvabkokamekastra/N1/SA"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBVpFwEEqcLficANTfe02hngu8tKFfcwH9ZVpWxXWMvxMwwibPSutzsziaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBwBqGkHgUIed9fJgPPjNibkYzeuKryS1fiaOYiaQb1FBzticqu2ibic5iaDjgA/640?wx_fmt=png&from=appmsg)

下载的DLL保存为"%LocalAppdata%\\moshtmlclip\\socker.dll"，释放另一个BAT文件"%LocalAppdata%\\Temp\\FROX\\sfs.bat"创建计划任务用于启动socker.dll。计划任务名称为MicrosoftVelocity，执行socker.dll的导出函数"?ejjwed@@YAHXZ"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBPGicvBsE5yJlErD6SLiaA5ZicTcSkwW2eySkqiasiaPbtDCv8cNqhVRy4xQ/640?wx_fmt=png&from=appmsg)

由于暂未捕获到socker.dll，目前无法对后续载荷功能展开进一步的分析。

PDF钓鱼攻击链

肚脑虫组织利用PDF诱饵的另一种攻击手法是借助PDF包含的钓鱼链接投递带恶意宏的PPT，相关样本信息如下。

|  |  |  |
| --- | --- | --- |
| **MD5** | **文件名** | **说明** |
| 5af77f4a63089011563bd3fcd02d56e0 | NDC-Course.pdf | PDF，包含下载恶意PPT的链接 |
| eb5d23a6a200016ba9b2d0085e58b586 | Assets 2024.pdf |
| 0f4f32b97c7bde0824b0fd27fe3ec4b0 | NDC-Course.ppt | PPT，带恶意宏 |
| d3ff126dc3e69d7f2d660a504b499cc4 | - |
| a0dbb4f8dbc5df628f03d60ed4a79d29 | Assets 2024.ppt |
| bcc0f690f330be4321365f6fd1330d95 | PLAIN.dll | DLL，向C&C服务器回传收集的信息，以及下载后续载荷 |
| 2c2176d9a74851dd30525a87bf0794ca | PLAIN.dll |
| bdc40a26cd02e33e5b83a9573125793e | PLAIN.dll |
| 8e91d5ab926daca6f4db41ba8a918ffd | PLAIN.dll |
| fa6cd1543db5156e7063db87b3241f26 | PLAIN.dll |
| df2ef826d0a398772f2373cd7303d58b | PLAIN.dll |

以样本Assets 2024.pdf（MD5：eb5d23a6a200016ba9b2d0085e58b586）为例，其中包含的下载PPT的链接为"hxxps://sharetobijoy.buzz/2024/filez/uploadz/invite25.php?id=19112"。

PPT中的恶意宏根据是否为64位系统执行不同shellcode。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMB7PutRf88U7agfm7PnNgXiabjOzJicsWbc651qskuYpoceT1iaKkKfOZ0g/640?wx_fmt=png&from=appmsg)

Shellcode为肚脑虫常用的两阶段下载器，以32位shellcode为例，第一阶段shellcode从"hxxp://diffgrinder.info/PNubW5l8DVqKlNbo/zFsDitREUBbsbeB815VkWnKpuXN4bhXUg3MFC7txkrV5beqf.png"获取后续，解密后作为第二阶段shellcode执行。

第二阶段shellcode再从"hxxp://diffgrinder.info/PNubW5l8DVqKlNbo/zFsDitREUBbsbeB815VkWnKpuXN4bhXUg3MFC7txkrV5beqf.mp3"下载后续，将其保存为"%temp%\\meaBRlIGkgtELpU\\ksHWqKqg.dll"。然后写入"4D 5A 90 00"四字节修复DOS头，接着将该DLL加载进内存中，调用其导出函数"LOPP"。

ksHWqKqg.dll（MD5：2c2176d9a74851dd30525a87bf0794ca）具有LOPP和VelocitySpeed两个导出函数，DLL功能与上面描述的直接伪装为PDF的EXE程序恶意行为一致。

**(1) LOPP**

该函数主要负责持久化操作。释放cross.bat文件，创建PerformTaskMaintain计划任务，执行"%temp%\\FROX\\PLAIN.dll"的导出函数VelocitySpeed，并将DLL文件自身复制为"%temp%\\FROX\\PLAIN.dll"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMB5WL0fyvNic4zxTRxq1xicfRjhAlmicYZmMBw0E26GFWnosGe2eTYEX9Gg/640?wx_fmt=png&from=appmsg)

**(2) VelocitySpeed**

该函数负责与C&C服务器的交互并获取后续载荷。收集感染设备的信息（CPU型号、操作系统产品名称和build number、用户名、主机名、CPU的ProcessorID、安装的软件列表），加密后发送到C&C服务器。AES加密使用的IV和key如下所示，与EXE样本一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicico9dEf1d11YZyASCmEbRMBhquw4o6bRkPz6zwjgxegUOqwoj28Hq...