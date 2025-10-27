---
title: SideCopy组织近期以印度国防部相关文档为诱饵的攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247505673&idx=1&sn=a7d1abc252196849c22f2af85d413902&chksm=ea66207edd11a968d78d6199a4cc396a3e7f7c4ce0557efa35b40d1d8d61f0641ee46977e237&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2023-03-22
fetch_date: 2025-10-04T10:15:54.063055
---

# SideCopy组织近期以印度国防部相关文档为诱饵的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjicvJLZzWVA7KHYgKyibGJia6N4vnd8dpg6jNPqvIuW40vxicKgq4ImBvwA/0?wx_fmt=jpeg)

# SideCopy组织近期以印度国防部相关文档为诱饵的攻击活动分析

原创

红雨滴团队

奇安信威胁情报中心

背景

2020年9月，Quick Heal披露了一起针对印度国防军和武装部队陆军人员的窃密行动并将其命名为Operation SideCopy。该行动始于2019年初，其攻击者主要以复制Sidewinder APT组织的TTPs进行攻击，故被命名为Operation SideCopy。

2021年7月，Cisco Talos研究人员已将该活动背后的攻击者作为独立组织进行跟踪，并称其为SideCopy APT组织。报告中披露了该组织多种攻击武器包括CetaRAT、ReverseRAT、MargulasRAT、AllakoreRAT等，以及多款C#插件[1]。

近日，我们在对SideCopy组织进行持续追踪的过程，发现了一些比较有意思的样本。

概述

在此攻击活动中，SideCopy的感染链与之前的攻击活动保持相对一致，使用恶意LNK文件作为入口点，然后是一个复杂的感染链，涉及多层文件嵌套以传递最终的有效负载。经研判，本次攻击活动的特点如下：

1. 鱼叉式钓鱼邮件，以压缩包中的lnk文件为攻击入口点；
2. 以无文件的方式在内存中加载执行后续载荷；
3. 最终载荷为Delphi编写的改良开源木马或者是由C++编写的新木马；
4. 诱饵内容均与印度国防部有关。

攻击活动执行流程如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjUtuuNLib3BibTxapxnfUmvXbNFvfwWUwV6tIAy0K3z2ausnQmRqicv4xQ/640?wx_fmt=png)

样本分析

**0x01基本信息**

本次捕获的样本为一压缩包，其基本信息如下：

|  |  |
| --- | --- |
| **文件名** | Grant-of-Risk-and-Hardship-Allowance-JCOs-OR.zip |
| **MD5** | 577419F202182F6E933C1CF83EF922EA |
| **文件大小** | 325484 bytes |
| **文件类型** | Zip |

解压后包含隐藏文件夹Adobe和诱饵lnk文件，lnk文件名翻译为“风险及困难津贴的发放”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjqUAcicj2MmHfjncaz02GHfUcI7NmlicFoSGFDic2oiaJwS08kG1HUkicPsw/640?wx_fmt=png)

对lnk文件进行分析，使用系统的mshta.exe访问C2下载后续载荷执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjt41vTr07uYtuJEV76t7e8I8u7ysIKh93QCxy3ibwiaicyWjBR1E7HBziaQ/640?wx_fmt=png)

**0x02 阶段一**

访问lnk中的链接，会跳转到https://kcps.edu.in/css/fonts/files/docs/graentsodocumentso/ganeshostwoso/snbtoolswires.hta下载一段JS代码回来执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjhH7OS49cLFJRj5ia7JL4O8Je3CKD0uhy1TynTO21ic2fejtDlIqdTtNw/640?wx_fmt=png)

其主要功能是内存中加载DLL，并通过DLL中的函数解密JS代码中嵌套的数据，从而释放诱饵PDF文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjpRtPlQ6lbG74yIyg7ClkkCh0LicYbkc6cyoXZDgQ5Xxd3EZBWB6fo4Q/640?wx_fmt=png)

解密释放诱饵PDF的函数openthefile

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjHo83WTbX1Z3qeF16OopsOowffBLxfQJYtBVaYyZibEzQiaeP0jAsPjibw/640?wx_fmt=png)

展示的诱饵PDF如图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjowN40SKYo6G0RyL0MRV0rpOdfurxyQaMULf7mVKZ5OJ3bJBTfbrXHg/640?wx_fmt=png)

然后获取杀软信息，与字符串“anvaro=”拼接后以POST方式上传至https://kcps.edu.in/css/fonts/files/avena/。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBj0BOdkoORa43icF2fALyicg3VweVOicY6eEnliaiaO7v9LfnYdlt7RP9o8ZA/640?wx_fmt=png)

创建C:\ProgramData\HP目录，访问C2下载数据解密后保存在C:\ProgramData\HP\jquery.hta和C:\ProgramData\HP\jscy.hta文件中并执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjRdjDnH0qjM4qS4QVqFCDRq3ZAibYxshJELmReLuhhnfMHj101B7ltNg/640?wx_fmt=png)

**0x03 阶段二**

下载的hta文件与阶段一类似，内存中加载DLL，先使用WMI收集系统中的杀软信息，再将硬编码的数据、杀软信息作为参数调用执行DLL中的SearchProducts函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjibVhweZejTibc4tZ7qfmvqicUl4oxwtB3ia9ZzCsnjyIZtpF1AT5hAu5xw/640?wx_fmt=png)

在SearchProducts函数中，先判断比较是何种杀软，以此来决定以何种方式来启动后续载荷。

|  |  |
| --- | --- |
| **杀软信息** | |
| Kaspersky | Avira |
| Quick | Bitdefender |
| Avast | WindowsDefender |

当存在印度杀软Quick时，首先将系统Credwiz.exe文件复制到C:\Users\Public\smitpr目录下，并重命名为crezly.exe，随后解密dll数据，并以DUser.dll命名在C:\Users\Public\ smitpr目录下。然后解密exe数据，在smitpr目录下释放程序simsre.exe，最后休眠30秒，调用释放的crezly.exe程序侧加载恶意DUser.dll。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjQk9U5GdiaxyHIau2aDzhIQzdyj5BtblTAWGmQfsCUgQYHCd6rjH8UdA/640?wx_fmt=png)

执行过程中生成bat文件，其功能为通过注册表为crezly.exe程序添加自启动项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBja0n6BgbqH3G4iaiby6az7QddNGw6Y3dahgghBwbotibd8T5uV7Fb3p4vA/640?wx_fmt=png)

当杀软为Kaspersky、Avast、Bitdefender、WindowsDefender或者其它时，其恶意组件释放方式与印度杀软Quick时基本相同，不同之处在于会休眠一分钟后直接启动释放的simsre.exe程序，并且注册表添加自启动项的程序也是simsre.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjIs4vcj25LXH8CFhAucfUyiburh6bRelPs0Do8u6qEbhRw5j3ibHoIzbA/640?wx_fmt=png)

值得一提的是，不是印度杀软Quick时，会在%temp%目录下生成tmplate.txt文件进行日志记录，日志中记录作者为“Mahesh Chand”，该人为印度人，推特上简介自称为前微软区域总监。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjhvXhS7ibGsHu3gkZEGfF4TgaLMNEJKByRrHdTAImQibUh2wv0IL1ia9MQ/640?wx_fmt=png)

**AllaKore RAT**

释放的simsre.exe为SideCopy常用的AllaKore RAT(又名Cyrus)，源代码在github上开源，经SideCopy组织更改后作为自己的武器库使用，其文件信息如下。

|  |  |
| --- | --- |
| **文件名** | simsre.exe |
| **MD5** | 087E366A4BECCBECB7D7CDB5C2F73088 |
| **文件大小** | 8507904 bytes |
| **文件类型** | EXE |

捕获的Allakore RAT 访问的IP地址为185.229.119.60，端口为9134，其主要包含以下几种功能：

* 键盘记录器
* 截图
* 列出文件夹和文件
* 上传/下载文件
* 窃取剪贴板数据
* 更改壁纸
* 远程控制

**DUser.dll**

侧加载的DUser.dll实际为loader，加载执行释放的simsre.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjwpMaLp3YutAsO1Ig0G7vkzdEFSeK1yOQrKOdOrIjSnKwwJtHy99Zag/640?wx_fmt=png)

溯源与关联

对样本进行分析时，我们发现此次攻击主要针对印度地区，一是诱饵内容主要以印度国防部相关内容为诱饵，二是解密时编码方式选择的是默认方式，只有当前电脑的系统区域设置为英语(印度)时，才能正确解密诱饵内容和部分后续载荷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjI8ss1JEEV2hyFj39fnngcec1U2mhuOR02eh7MzTAQaoY7BnEWZiaOCA/640?wx_fmt=png)

对此次捕获样本攻击手法，代码逻辑层面分析，发现此次捕获的攻击样本与SideCopy组织常用攻击手法，恶意代码基本一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjDY9ylAlqOIibCbwdKhmMnfBNE3T3WEoIL6QeKBJvsNavGAbj1IYj6iaw/640?wx_fmt=png)

通过对本次攻击的初始lnk文件进行关联，我们还发现了另外一个类似的攻击样本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjPibzQ4T2bFL12vv0gNR5GWrtTfAYksXp4jKZxiaIe3a5I2hm1ogTrGWA/640?wx_fmt=png)

其以印度国防研究及发展组织(DRDO) 为武装阿里汉特级潜艇而开发的具有核能力的中程潜射弹道导弹(K4导弹)相关文档为诱饵。其诱饵内容如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjKuiaZelxYM1UDDM0iaaT0vZ6Dxia4xNDOj25SuI9MP4nbzMd6F8gJPt4A/640?wx_fmt=png)

其执行流程与上述分析基本一致，不同的是其最终载荷DUser.dll为C++语言编写的程序，其在Virustotal上的免杀率颇高，其C2为144.91.72.17:8080，并且还携带了PDB路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjZAhXAslzRBK66LibDdBJyrU0bbyxcgIOyMlAV2ktRmdpc96ShyVwhcw/640?wx_fmt=png)

另外扩展分析时，我们还发现了Sidecopy组织近期使用lnk文件进行攻击的大量样本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjOqxVmQK9ib4IvLwzBfo6r7uuxexxliawlO8Yic9IR8VS1WjoptJtWkhSg/640?wx_fmt=png)

同时，在去年早些时候，我们还发现Sidecopy组织以色情图片作为lnk文件图标进行攻击，这一套路可谓屡试不爽。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBjY3kWNt7tNM8xH0icNovPP0iadic5uIt64Bth2RibZbpGBT1UIgvVRicfcUg/640?wx_fmt=png)

总结

SideCopy组织主要复制Sidewinder APT组织的TTPs进行攻击，故被命名为SideCopy，其近年来才活跃在大众视野范围内，攻击手法及武器代码方面与同地域组织相比都较为青涩，且大多使用网络上开源的代码及工具。更重要的是，早些时候我们还披露过其对Linux，Mac OS等多平台的攻击[2]，奇安信威胁情报中心会对其进行长期的溯源和跟进，及时发现安全威胁并快速响应处置。

此次捕获的样本主要针对南亚地区开展攻击活动，国内用户不受其影响。奇安信红雨滴团队提醒广大用户，谨防水坑攻击，切勿打开社交媒体分享的来历不明的链接，不点击执行未知来源的邮件附件，不运行标题夸张的未知文件，不安装非正规途径来源的APP。做到及时备份重要文件，更新安装补丁。

若需运行，安装来历不明的应用，可先通过奇安信威胁情报文件深度分析平台（https://sandbox.ti.qianxin.com/sandbox/page）进行判别。目前已支持包括Windows、安卓平台在内的多种格式文件深度分析。

目前，基于奇安信威胁情报中心的威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、天擎、天眼高级威胁检测系统、奇安信NGSOC、奇安信态势感知等，都已经支持对此类攻击的精确检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibzV5CbiboBB8vZfdM3BQwBj2qg67aibrKLgn7ZH83NHP5HPu44IbF21p31IfACCLMSkoWm42KE1eBg/640?wx_fmt=png)

IOCs

**MD5**

577419F202182F6E933C1CF83EF922EA

3E3D3F78A07BAB5A3342E0414E48D787

087E366A4BECCBECB7D7CDB5C2F73088

26E41AF2CA9EA82C244C1AA1EC77654A

FA6C832E22F978B8210C0630DB69E6A2

EFCC2BF765993711CC9E4E86D2EBB876

191C389140293C782D7A2304893151E2

6528A9F0AF30DF7F4211EF8B341ACC2E

0725318B4F5C312EEAF5EC9795A7E919

AB11B91F97D7672DA1C5B42C9ECC6D2E

CBAA7FC86E4F1A30A155F60323FDB72A

036DA574B5967C71951F4E14D000398C

2E19B7A2BBDC8082024D259E27E86911

087E366A4BECCBECB7D7CDB5C2F73088

3F22B345ED1F9E244DB034F9AF49E707

EDE163036A1754C71D6FF11B266B91CE

5BE4E4884F4E021BA975CBED0A7E9C25

F7D1E515CB84F6DC2D0349AB93BD4E05

63789CACECC1ABD9669344516ADB4120

9B06472E5ACF2311D0AF62D638A8E51A

D129B81C1D40C34AC628835E144A4740

BA2ADA448B8471789C0EF3B3345597FE

6B3F45F7A6758D198A317DE43D51E669

A65EB385C9019C712EA513E4C5C25152

1A1C8C0F5CAFB7DF661086BCB804154C

0C4...