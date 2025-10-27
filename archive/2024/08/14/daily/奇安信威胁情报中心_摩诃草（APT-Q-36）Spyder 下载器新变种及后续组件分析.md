---
title: 摩诃草（APT-Q-36）Spyder 下载器新变种及后续组件分析
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247511552&idx=1&sn=9f2345fbbb341b3f33e433d05fb619f2&chksm=ea665977dd11d061201858a4d4a0884cdaf93fc68144376a83c64f3d9a567d6e85e1ea56731a&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-08-14
fetch_date: 2025-10-06T18:03:31.021237
---

# 摩诃草（APT-Q-36）Spyder 下载器新变种及后续组件分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGIcVU1VnQAEGPBY3ia2E7FrTy9Tpogn6tGUc6YrCv88pQE42s8r6GOKg/0?wx_fmt=jpeg)

# 摩诃草（APT-Q-36）Spyder 下载器新变种及后续组件分析

原创

威胁情报中心

奇安信威胁情报中心

团伙背景

摩诃草，又名 Patchwork、白象、Hangover、Dropping Elephant 等，奇安信内部跟踪编号 APT-Q-36。该组织被普遍认为具有南亚地区背景，其最早攻击活动可追溯到 2009 年 11 月，已持续活跃 10 余年。该组织主要针对亚洲地区的国家进行网络间谍活动，攻击目标包括政府、军事、电力、工业、科研教育、外交和经济等领域的组织机构。

事件概述

奇安信威胁情报中心此前发布过关于摩诃草组织 Spyder 下载器的分析报告[1,2]，近期我们发现 Spyder 下载器出现新变种，并观察到攻击者借助 Spyder 下发两款窃密组件，分别用于截屏和收集文件信息。

虽然 Spyder 下载器的核心功能没变，仍是从远程下载的加密 ZIP 包中释放出后续组件并执行，但在代码结构和 C2 通信格式等方面做了一些改动。以下是本次发现的 Spyder 下载器和窃密组件的攻击过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGcOtqJDf0Gfn2I1HiaWmIxsibf9SgCAHGICoGQ2xxE5rynSbmBl8icUuxQ/640?wx_fmt=png&from=appmsg)

详细分析

相关样本信息如下：

|  |  |  |  |
| --- | --- | --- | --- |
| **MD5** | **编译时间** | **文件名** | **说明** |
| 689c91f532482aeff84c029be61f681a | 2024-06-04 15:12:47 UTC | eac\_launcher.exe | Spyder下载器 |
| 7a177ef0b1ce6f03fa424becfb9d37ac | 2024-05-21 08:28:54 UTC | IntelPieService.exe | 截屏组件 |
| 85d0f615923af8196fa7d08ef1c68b64 | 2024-02-13 10:46:07 UTC | RstMwService.exe | 文件解密组件 |

**Spyder 下载器**

样本 689c91f532482aeff84c029be61f681a 以 Word 文档图标作为伪装，程序带有数字签名。签名者名称为 "Xi'an Qinxuntao Network Technology Co., Ltd."，签名时间为‎ 2024 ‎年‎ 6 ‎月 ‎4 ‎日 15:21:35 UTC。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGDXX71cKx7MJaoBJmudmFhIx5bNNiadBEIjTwogZ36n0G5wzmuqHH41Q/640?wx_fmt=png&from=appmsg)

新型 Spyder 下载器中的配置数据直接存放在代码中，不像之前的版本将其加密后保存在资源区。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGibaDoXgZgwd1PVv5ibM9BbN3YCNT87diaAj6QiaakicnHyrjGvEwaZfETmg/640?wx_fmt=png&from=appmsg)

使用 curl 产生对 retail.googleapis.com 和 api.github.com 的网络通信，进行流量伪装。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGEzIick6ctQVONIuWiaVFlM3nrb677CPJy0cdAG6wbK0qBq1vXtyMjdZg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGZXDrJPWqDcVMjPEib3L6gD69c3OMhw2yEX38GJvLqicuf4OUBDRYicBjA/640?wx_fmt=png&from=appmsg)

重新映射多个系统 DLL 的 .text 段，以解除对这些模块设置的挂钩。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGbjSDV2Y5dibq5iaDLNkiauCbiatCbhYxYu1aEPhZ5Wbq0IOldvXr2hibkhg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icG1uena271LQeHA48rgpRibzSeyq15ibzS529LtaDTMTzaE0lVzvHcxKgg/640?wx_fmt=png&from=appmsg)

样本设置多个只触发一次的计划任务，指向 "%LocalAppdata%\zlib1.exe"，并将自身复制为 "%LocalAppdata%\zlib1.exe"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGVy98Ryacz2t732Rs3czHobOicGw9DlTmce12s1SicgbtBBByuHPkWcQw/640?wx_fmt=png&from=appmsg)

样本与 C2 服务器的通信数据放在 POST 请求首部的自定义字段（该样本为 "boop" ）中，数据为经过 Base64 编码的 JSON 字符串，Base64 编码后还会对部分字符进行替换处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGbPavPR6D429q3vzsib1s3j8nuH2USdRZplT4PTnjDicba6xogGrbm93w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGlUlwyW6vbCqsMEmadMBuE5Ovowv0s2lEIIEY5vVciaTZE4g3IgJEuDg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGZRHianhkWgR7MXaKMy3MH2B5XxDc9M1g4IpGqo5lRpGrELbU3U5zFRw/640?wx_fmt=png&from=appmsg)

样本向 C2 服务器的 "/soup/pencil.php" 发送的 JSON 字符串包含两部分固定的内容，分别是："xdid"（感染设备的 Machine GUID）和 "about"（样本配置数据中的字符串 "0.0.0.1"，可能是版本号）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icG00Gyia6z663WGgZkwgaV3BW8uvvESDyr6ta0fWC5LX32rwsjUMlvWlw/640?wx_fmt=png&from=appmsg)

向 "/soup/pencil.php" 发送请求主要有两个作用：

（1）是否收集设备信息；

（2）获取关于后续组件压缩包的信息。

**收集设备信息**

样本根据第一次请求 C2 服务器 "/soup/pencil.php" 的响应判断是否需要收集设备信息并回传，如果响应为 "1"，则执行信息收集操作，否则跳过该步骤。收集的信息添加为 JSON 字符串中的 jupiter 字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGrAapJzmhicicdGFom1tzFzfJ9mDmpia4G90cmJWuGicMR7Vc61CzbnzB7Q/640?wx_fmt=png&from=appmsg)

收集的各类信息如下：

|  |  |
| --- | --- |
| **字段名称** | **保存数据** |
| address | 主机名 |
| page\_id | 用户名 |
| weather | 操作系统版本 |
| profile | 样本配置数据中的字符串（"Fighter"） |
| news | 安装的杀毒软件信息 |

**下载后续组件**

之后样本进入获取后续组件的循环过程。每次循环先向 api.github.com 发送伪装流量，然后请求 C2 服务器 "/soup/pencil.php"。如果响应为 "0"，或响应数据长度不大于 5，则直接休眠等待下一次循环。

当响应数据符合要求时，样本从中提取关于压缩包的信息，用于下载后续组件。在响应数据中提取信息的字段有如下 3 个：

|  |  |
| --- | --- |
| **字段名称** | **说明** |
| first | 下载组件的类别（数字） |
| middle | 下载压缩包的名称（字符串） |
| last | 解密压缩包的密码（字符串） |

样本将 middle 字段内容拼接到 "/soup/download.php?mname=" 之后，向 C2 服务器发起请求，下载包含后续组件的 ZIP 压缩包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGfPOPceN6AzWW4GX03W9WnDumdx60s34Ggeot3WZGOwg3RJPianBOQhQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGyiale1ibUZAVRb2VetmUt039hPRoO2rbg9eciaew9VJibbc4jzGiarT8n9w/640?wx_fmt=png&from=appmsg)

压缩包中的组件解压到 INTERNET\_CACHE 目录（即 "C:\Users\[user\_name]\AppData\Local\Microsoft\Windows\INetCache\"），然后调用 CreateProcessW 执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGOTVwT8NUgLQicPvV3EMVM0df10JlPSgsCDZUyYepGTVABFM0bgvpUzA/640?wx_fmt=png&from=appmsg)

**后续组件**

目前观察到通过上述 Spyder 下载器释放的后续组件有两类，均带有与 Spyder 下载器相同的数字签名（"Xi'an Qinxuntao Network Technology Co., Ltd."），主要功能分别为截屏回传和文件信息窃密。

**组件一：截屏**

截屏组件 IntelPieService.exe 将截屏保存为 image.bmp，回传到 hxxp://onlinecsstutorials[.]com/soup/upsman.php。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGYo7iaRTy0PHqo4faLbUjcBEPvYMo2vaicUe8FfliczvT3ibhiafgmBGepYQ/640?wx_fmt=png&from=appmsg)

发送的请求数据中仍以设备的 Machine GUID 作 为 uid。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGXroIQasdHMWO1C70opZrmtRggUdXXbiaMqLj4g0Smvfo0zjK4KNxxnQ/640?wx_fmt=png&from=appmsg)

**组件二：文件窃密**

文件窃密组件 RstMwService.exe 首先将自身文件路径设置为注册表中当前用户 RunOnce 项下 DeviceDisplay 的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGhlibF9y8bCzcz7tZJPng7gYDtngOPAuiar0YdLWMZS2icT8ZJhX9tN9Ag/640?wx_fmt=png&from=appmsg)

从资源区释放文件，保存为 INTERNET\_CACHE 目录下的 MsEngLU.dll（MD5：c568d613ba74fd6cd5da730f6ce38626）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGguia2ibtDIyCtTyzibObA6cwOTxP3zQibMKicMn6YqngGXyfk7xbG0ibzHcg/640?wx_fmt=png&from=appmsg)

最后加载 MsEngLU.dll，调用导出函数 DriveBackup。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGI8JIysOvwiaBsCKfd5pRtA2k86zP2huTFmOlEu2AjyuwJh9AThwES2Q/640?wx_fmt=png&from=appmsg)

MsEngLU.dll 带有数字签名 "GJT AUTOMOTIVE LTD"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGYGEgqddMFkNYSNZvJiafrcHdc252GsS3ZQiaR39HichmLKAb3QWxK1pgg/640?wx_fmt=png&from=appmsg)

该 DLL 从用户的 Desktop、Documents、Downloads、OneDrive 子目录，以及所有非系统盘的根目录开始递归收集文件信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGLQYRcmibqkNC0dA4rDtWULyvAjEl9KPztodPy9TXVCHEs6UooicM7EXg/640?wx_fmt=png&from=appmsg)

窃密软件关注的文件类型包括文档、压缩包、图片、音频、电子邮件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icG7MibbB1Zic9ibQdvp5ia77ZQ2ERCsKPq8YhGPchhkgoz1MicaxN3iaYP5oCg/640?wx_fmt=png&from=appmsg)

文件信息存放在 SQLite 格式的本地数据库 "%APPDATA%\Microsoft\Windows\Libraries\policy.db"中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGjk7S7m8iaubZEv3hKLNb4fdkrGicNutX2HbmF6wa5hFM9h8TlhjGX5NA/640?wx_fmt=png&from=appmsg)

最后将数据回传到 "hxxp://93.95.230.16/domcomtwit/hen.php"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8ezwKLjb5TnV7E6f7dU8icGGbVFIV3ibgYUib4vReV3AXQWE9RrqWfUzBficb2xP2SsZ3fE5QfNyapJA/640?wx_fmt=png&from=appmsg)

溯源关联

本次发现的 Spyder 变种仍具有以往 Spyder 样本[1,2]的诸多特征，包括：XOR 解密字符串；设置多个计划任务；以 JSON 字符串格式组织通信数据；先从 C2 服务器获取加密压缩包信息再下载压缩包并解密等。

该 Spyder 变种关联到一些相似的样本，从程序创建时间可以看出此类变种至少从 3 月份开始投入使用。

|  |  |  |
| --- | --- | --- |
| **MD5** | **编译时间** | **C&C** |
| 887d76e305d1b2ac22a83a1418a9fc57 | 2024-03-14 14:47:01 UTC | l0p1.shop |
| 47b4ed92cfc369dd11861862d377ae26 | 2024-04-05 14:09:32 UTC | firebaseupdater.com |
| 0dc0816bd46f3fe696ed0a2f1b67cfa8 | 2024-04-25 17:10:20 UTC | firebaseupdater.com |
| e8a9b75c5e41f6d4af9f32c11d0057cb | 2024-04-25 17:10:20 UTC | f...