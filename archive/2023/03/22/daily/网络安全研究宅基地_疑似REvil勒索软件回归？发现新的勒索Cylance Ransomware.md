---
title: 疑似REvil勒索软件回归？发现新的勒索Cylance Ransomware
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247493721&idx=1&sn=3e9a7d5173f775b1fd5122b8c4f16e3a&chksm=f9ed84e6ce9a0df0320388a49fde2f0728e33eb7af3ccc260e156263820e255955c760d81715&scene=58&subscene=0#rd
source: 网络安全研究宅基地
date: 2023-03-22
fetch_date: 2025-10-04T10:16:23.249412
---

# 疑似REvil勒索软件回归？发现新的勒索Cylance Ransomware

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvnexLJT1pgXEx8ziac8D1ahNrkfPJoHAiaPdJrOgHKzMq9TjZGQVDgCElxzTjkas9MuIoAjl3qITE8tQ/0?wx_fmt=jpeg)

# 疑似REvil勒索软件回归？发现新的勒索Cylance Ransomware

原创

猎影实验室

网络安全研究宅基地

**点击蓝字关注我们**

**一**

**事件背景**

近期，安恒信息猎影实验室在日常监测运营中捕获了一种新的勒索软件Cylance Ransomware。勒索软件执行后，快速加密文件并添加扩展名.Cylance，在目录下放置勒索信文件CYLANCE\_README.txt，并在信中自称CylanceRansomware。该勒索可配置多种命令行参数，设置灵活，支持自定义的间歇性加密方式，能够更快地加密文件和有效规避检测。Cylance勒索勒索信格式与REvil高度相似，并都采用Curve25519和salsa20加密算法组合加密文件的方式，拥有快速加密和全加密两种加密模式。但在整体功能上有所差异，例如参数配置更为丰富、针对数据库等特殊文件使用了间歇性加密模式，对于静态字符串没有REvil复杂的混淆加密处理，不涉及地区豁免等。

      REvil也被称为Sodinokibi，是最早实施双重勒索的组织之一，自 2019年被发现以来，因其备受瞩目的攻击而臭名昭著。REvil 在2021年上半年达到了成功的顶峰，在Kaseya MSP供应链攻击中损害了数千家公司，要求计算机制造商宏碁支付50万美元，并使用被盗的尚未发布的设备蓝图勒索苹果。在执法部门的巨大压力下，REvil勒索软件团伙于 2021年10月关闭。

      2022年，研究人员根据加密器中的代码相似性，将相对较新的Cartel勒索和BlogXX勒索与REvil 团伙联系起来。此次发现的CylanceRansomware同样在加密方式和勒索信格式上与REvil存在类似性，因此可能是REvil勒索的品牌重塑或原组织内部人员启用的新勒索软件。

**二**

**Cylance勒索软件分析**

1

命令行参数

该勒索支持多种命令行参数配置，可灵活设置自定义的加密策略，具体如下：

|  |  |
| --- | --- |
| 参数 | 说明 |
| -path | 需要加密的路径 |
| -mode | 加密的模式，包括三种方式：  ●full 全部加密，所有文件类型无论文件大小，文件中的数据全部加密  ●fast 快速加密，所有文件类型至多加密开头1MB  ●split 间歇性加密，所有文件类型都采用间歇性加密，需配合-skip使用  若未设置mode参数，则普通文件至多加密1MB，特殊文件类型（数据库等格式）采用间歇性加密策略。 |
| -skip | 间歇性加密跳过的字节数 |
| -power | 执行结束后的电源选项，包含2个命令参数：  ●shutdown关机  ●restart 重启 |
| -console | 在终端显示勒索执行的统计信息 |
| -nomutex | 执行时不创建互斥量 |
| -nonetdrive | 不加密网络磁盘 |
| -selfdel | 自我删除 加密结束后删除程序本身 |

2

加密过程

如运行时不含-path参数，则遍历A-Z磁盘依次进行加密操作。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKniav6ic2WBFeBicD1u93O0KzYkpFenpLMyLlBdib1dUd61j7ianJk55Ba2A/640?wx_fmt=png)

Cylance勒索会忽略特定的文件夹、文件名和扩展名不进行加密。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKYzK5fJviaWkS15McfthTesowY1gctH1Skbt0OUiaXK4TCrKXohwHnLiag/640?wx_fmt=png)

应忽略加密的文件夹名称：

"Windows"，"$Windows.~bt"，"$windows.~ws"，"windows.old"，"windows nt"，

"All Users"， "Public"，"Boot"，"Intel"，"PerfLogs"，"System Volume Information"，

"MSOCache"，"$RECYCLE.BIN"，"Default"，"Config.Msi"，"tor browser"，"microsoft"，

"google"，"yandex"

应忽略加密的文件名：

"ntldr"，"ntuser.dat"，"bootsect.bak"，"ntuser.dat.log"，"autorun.inf"，"thumbs.db"，"iconcache.db"，"bootfont.bin"，"boot.ini"，"desktop.ini"，"ntuser.ini"，"bootmgr"，"BOOTNXT"，"CYLANCE\_README.txt"，"LPW4.tmp", "MSVCR100.dll", "LLKFTP.bmp"

应忽略加密的文件扩展名：

"dll"，"exe"，"sys", "drv"， "efi"， "msi"， "lnk"，"Cylance"

Cylance采用Curve25519和Salsa20加密算法加密文件，其中Curve25519生成密钥对，利用sha256摘要算法将共享密钥生成用于加密的Salsa20密钥，Salsa20是一种流加密算法，能够快速地加密数据。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKOjYqN5kg3DQuZNp0fFxNgrSqtrrT9icBUGpBRSzZ4sh3aIiazDVCL4ag/640?wx_fmt=png)

在加密策略上，Cylance勒索默认无参数采用快速加密，即文件至多加密1MB，不过特殊的文件类型采用间歇性加密，这类文件主要是数据库和压缩文件，攻击者认为此类文件具有重要的数据价值，所以在勒索中往往重点关注。

      特殊文件的具体类型如下：

"mdf"，"ndf"，"edb"，"mdb"，"accdb"，"db"，"db2"，"db3"，"sql"，"sqlite"，"sqlite3"，"sqlitedb"，"database"，"zip"，"rar"，"7z"，"tar"，"whim"，"gz"，"xld"，"xls"，"xlsx"，"csv"，"bak"，"back"，"backup"

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKibwia2jlibLSelBLAGAibmYCxQj5tiaS3F2pwicFhmPGuI2gnQmJ13Zu0JtA/640?wx_fmt=png)

对于特殊文件类型，不同文件大小的加密间隙不同：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKibicgSpN5dGvicylv29extkVFN5KKN91mbNlq09SmK4vpwwtrtbkskQwQ/640?wx_fmt=png)

3

上传信息至远程服务器

在加密前，Cylance勒索上传受害主机的信息，包括用户名、主机名、系统版本号等。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlK1vsgDDgkI3LsEdUQUZrHrwHLVwAwwYtLv7xEuXqPDBesbKkXqmN9cQ/640?wx_fmt=png)

加密后，将执行的相关信息包括未加密量、已加密量和执行时间等信息，同样上传至服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKtbnO10HPgicK0HRL7BjlibzYDKLKCOcOk3H9KRQJ2EXribe7llq7qgsuA/640?wx_fmt=png)

通过安恒在线云沙盒检测到远程C2服务器地址为139.99.233[.]175。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKHLzmk3KUYSZ9iaJ869lgt8jgNmACD13Cl4BNMbwluk7Xs8ibmjibvfT9w/640?wx_fmt=png)

安恒在线云沙盒支持对勒索等恶意软件的深度分析和检测。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKOxUdXicQOBlibbmT9FAB0ro1Ttb8aeF1uxWiaJYcnFWzT8P4ria4U1xJiaQ/640?wx_fmt=png)

**三**

**Cylance和REvil比较分析**

Cylance勒索在每个加密目录及其子目录放置勒索信文件，内容如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKoGhuR1sz5UyXiblw7vBXMZfHBp3OZjthnDnN8jTS42xH191iayEjIWeg/640?wx_fmt=png)

从勒索信格式上分析，Cylance勒索和2021年左右盛行的REvil勒索存在相似性, REvil勒索的勒索信如下：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKhqS29Loibd4X6EtXFyvcdicDhfebJfkAUMgrsvYrib0NtEQBhOQHOaibrg/640?wx_fmt=png)

对两种勒索进行比较分析

1

与Cylance不同的是REvil在执行时会释放勒索本体文件，动态解密API。

2

REvil勒索具有一定的混淆能力，其使用RC4算法加密静态的字符串等信息，并在执行时解密，Cylance勒索无任何混淆处理。

3

REvil在执行时检测受感染计算机的语言，若属于特定的语言则不进行加密，在Cylance中并没有此种行为。

4

相比较REvil勒索，都同样有快速加密和全加密两种加密类型，并快速模式都至多加密1MB的数据，但Cylance勒索具有更为多样的命令参数设置和自定义的间歇性加密策略。

REvil的参数配置

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlK3pyO8UOXqwFEPYUicwTA1jjdAsFcrmlWy4nlIfONib4NwbtTu2y2lkYA/640?wx_fmt=png)

5

从加密算法上看，二者都采用sasla20和Curve25519组合的加密算法,加密结构上存在一定相似性。

REvil勒索的加密结构：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKfIUXwASb7m8MEDiavUYJyeib5Pkfe957VdaMuhCBY8XBwBFGGO0icrq5w/640?wx_fmt=png)

Cylance勒索的加密结构：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKMSJoZeLTSNIu4S5xichuRBc3TCFJyLKSxNepN5qCib1d5nJAygJdktpA/640?wx_fmt=png)

**四**

**思考总结**

Cylance和REvil之间存在一些相似之处和技术重叠，尚不清楚是REvil分支的品牌重塑，还是Cylance有意模仿REvil勒索。相比较REvil，Cylance在代码保护性上略显不足，但拥有效率更高的间歇性加密方式和更为灵活的配置，这可能表明着Cylance的制作者正在积极开发，在参考REvil的同时，着力于在勒索速度方面的提升。

      需要注意的是，在捕获到Cylance勒索软件样本时，其创建时间戳显示为2023年3月12日，虽暂未发现大肆传播和勒索攻击的迹象，但由于其与REvil之间的相似性，背后可能存在精于勒索攻击活动的操控者，应当密切关注和重视其发展进程。

**五**

**防范建议**

建议安装防病毒软件定期对系统进行扫描，并删除检测到的威胁；

确保及时更新系统补丁；

不点击来历莫名的邮件附件和链接；

重要的数据做好备份工作。

若遇到可疑文件，可以通过安恒在线云沙盒进行检测。安恒在线云沙盒能够在安全执行环境下对勒索等恶意软件的行为进行深度分析和检测，并关联海量威胁情报，提供专业的安全服务。

目前安全数据部已具备相关威胁检测能力，对应产品已完成IoC情报的集成：

●安恒产品已集成能力：

针对该事件中的最新IoC情报，以下产品的版本可自动完成更新，若无法自动更新则请联系技术人员手动更新：

（1）AiLPHA分析平台V5.0.0及以上版本

（2）AiNTA设备V1.2.2及以上版本

（3）AXDR平台V2.0.3及以上版本

（4）APT设备V2.0.67及以上版本

（5）EDR产品V2.0.17及以上版本

      安恒EDR产品终端检测告警如下：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKlum0eOVicJVfibpOqkmAUmwFxn1wsU0ZDhJEQjjsnPBeY8phADVOT0Pw/640?wx_fmt=png)

● 安恒云沙盒已集成了该事件中的样本特征：

用户可通过云沙盒：

https://ti.dbappsecurity.com.cn/sandbox，对可疑文件进行免费分析，并下载分析报告。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKHr8YXia35EgnjzQ5hfsyPleEk94CWNccicnKmQ19vKWTudfWGnaSoPtw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKzAYYDn8yteKb3nRjSFPibAV1eBj6wRRia1gPXzooOlXaIOpWbsmRHG8A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKSuBGwOzSn4ibBq7ugOhMOjYU880ibCwbMHNracLo8LoTM2NMbFic5fQWQ/640?wx_fmt=png)

**安恒安全数据部，**下设猎影实验室、零壹实验室、析安实验室和回声实验室，团队以数据分析与技术研究为核心，致力于数据驱动安全创造用户价值。

**猎影实验室**

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKCVypImk4R2T8VxCWVLT3S7PvzU53RuBNVnBibRRth8LIBpM2jusBQHg/640?wx_fmt=png)

高级威胁研究团队，专注于APT攻击发现、分析、检测、溯源、防御等研究，以及积累了海量的IoC情报数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvncuO0MsZ2mXh9vmick2fpKlKs8yLqhYb4eTfQ3x5m1wiaibsOXmsniaib3pkZwoN4DiawE1E5VfujAI6HFw/640?wx_fmt=jpeg)

**网络安全研究宅基地**

扫码关注我们，一群技术宅

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndQmlUoXEvMw4vR9nQh9VO9GKoibVOmH6UpHpTzcp63e3C0AMDraHZ5ayujONtRJ3ylkc0W1SnteibQ/0?wx_fmt=png)

网络安全研究宅基地

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndQmlUoXEvMw4vR9nQh9VO9GKoibVOmH6UpHpTzcp63e3C0AMDraHZ5ayujONtRJ3ylkc0W1SnteibQ/0?wx_fmt=png)

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