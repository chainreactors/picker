---
title: 最新出现的CatB勒索软件采用2年前的DLL劫持技术来逃避检测
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247533885&idx=2&sn=35cbe0d2c2f3c3e8d5ce6a30cf1706e7&chksm=c1e9c96cf69e407ad88d91eeeb0c23bcc2226d495fe64b1da615be12b70f8c6ed7b41e4da5ee&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-01-14
fetch_date: 2025-10-04T03:53:30.901108
---

# 最新出现的CatB勒索软件采用2年前的DLL劫持技术来逃避检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogsIiagHbianIoujhMeRXzYDtZSnDoM92hrRMlFxDa7umjW8rGMkdl39eUlnNMnVxABa8H6o5PmnJE8Q/0?wx_fmt=jpeg)

# 最新出现的CatB勒索软件采用2年前的DLL劫持技术来逃避检测

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogsIiagHbianIoujhMeRXzYDtZRho9klaYbvT4MpFchRTCQAXjWjUuIKILe5CjW3nsYkwRXwp6ibB1sNw/640?wx_fmt=png)

最新发现的勒索软件CatB，该软件通过处理器内核检查，物理内存大小检查和硬盘大小来检查自己是否是在虚拟机中，然后执行MSDTC 服务的DLL劫持绕过杀毒软件。

我们最近发现了一个新型勒索软件，它执行MSDTC服务DLL劫持以静默执行其有效负载。我们根据勒索软件组使用的联系电子邮件将此勒索软件命名为CatB。该样本于2022年11月23日首次上传至VT，并被VT社区标记为Pandora勒索软件的可能变体。Pandora组织首次出现于2022年2月中旬，主要以企业网络为目标进行针对性攻击，主要通过钓鱼邮件、漏洞利用、RDP爆破等方式进行传播，采用Raas双重勒索的策略，在对用户系统进行加密导致工作无法正常运作的情况下，利用窃取的数据胁迫用户支付赎金，否则就外泄。该组织使用Tor站点或者Email邮箱方式与受害者联系。

Pandora 勒索软件最重要的功能就是应用了先进的反逆向技术，虽然在恶意软件中反逆向技术很常见，但Pandora的这一功能颇为突出。与潘多拉勒索软件的联系仅限发出的勒索信。CatB勒索软件实现了几种反虚拟机技术，以验证在真实设备上的执行情况，然后释放恶意DLL和劫持DLL以逃避检测。

CatB勒索软件包含两个文件，包含UPX的 dropper (version.dll)和勒索软件有效负载(oci.dll)。dropper处理反vm检查，释放勒索软件负载并执行它。

反虚拟机（Anti-VM）

CatB dropper实现了三种反虚拟机/沙盒规避技术：

处理器内核检查：现如今的真实计算机都至少有两个处理器，所以如果勒索软件只检测到一个CPU内核，这将是一个很强的信号，表明它当前驻留在沙盒中。勒索软件通过GetSystemInfo API函数检索系统信息并检查处理器数量。如果少于两个处理器，则退出立即中断执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQpGg1dK1DAnZENrmnvTE80maFMd0RiasTNw7PWicj27W9Zr5Qk1MvEjxg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

处理器检查

总物理内存检查：与虚拟机不同，现在的虚拟机都至少有2GB RAM，通常在4GB和32GB之间。CatB勒索软件通过检查物理内存大小来检测虚拟机/沙盒。这是通过使用GlobalMemoryStatusEx API函数检索有关物理和虚拟内存的信息来完成的。在本文的示例中，如果即将运行的物理内存少于2GB，勒索软件会退出。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQ7duIicL1q7GdCEjkXGTYUMrMm33naqmPcESoQoQPWV4UwvaMuaNqEcw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

物理内存检查

硬盘大小：恶意软件可以检查设备的硬盘大小，并根据该参数继续执行。这可以通过使用DeviceIoControl Api函数实现，其中“0x70000”作为dwIoControlCode参数传递。CatB勒索软件只能在至少有50GB硬盘的设备上执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQ51rMiaRvnibvMSyPDichsZBMfd1ibibQ7nURLM5EQMB9l8jWCdMyfGFP8eg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

硬盘大小检查

DLL劫持

如果所有反VM检查都通过，则 dropper将继续执行，并将勒索软件负载（oci.dll）放入C:\Windows\System32文件夹。接下来，它将查找MSDTC服务（分布式事务协调器Windows服务，负责协调数据库（SQL Server）和web服务器之间的事务）并更改其配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQLOQ8EIMzmOzjExgia7JRU8MMUJOz7vXfMkozQaFLibYpgfyc0TjZXZgg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

MSDTC服务

更改的配置包括运行服务的帐户名称（从“网络服务”更改为“本地系统”）和服务启动选项（如果重新启动，则从“按需启动”更改为自动启动以实现持续性）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQfibnvHMynZEibDia5I6ck8mh81LT1gtHLMDhumRdTtcJunt49FrywLFbw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

服务配置更改

运行服务的帐户已更改为授予服务管理员权限，因为网络服务帐户使用用户权限运行。更改启动类型将授予勒索软件在每次系统重新启动时执行的能力。

dropper在更改其配置后启动服务。此服务启动时，默认情况下会尝试从System32文件夹加载几个DLL。这使它有机会将任意DLL（在本例中为oci.DLL）植入此文件夹中，以执行恶意代码。

勒索软件

此时恶意oci.dll文件被加载到msdtc.exe进程中，然后加密进程启动。CatB枚举并加密特定的硬编码磁盘和文件夹：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQOFE6mN4FwicsLicG9CMJ3o85GW8KhDaGmt8yORgEo7bTHlgYB3nzXnKQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQ4q6WPg8Q5NO3xcTr5ThalKRf834lOPzcco8kcFPfu9OlUM5ndHibrlA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

硬编码磁盘

CatB避免使用带有.msi、.exe、.dll、.sys、.iso扩展名和NTUSER.DAT的文件。CatB勒索软件的一个有趣之处是，勒索通知被添加到每个加密文件的开头，而不是像大多数勒索软件那样作为一个单独的文件添加到每个文件夹中。它也不改变文件扩展名。这可能会在一开始使用户感到困惑，他们可能没有注意到加密，并且文件将看起来已经被攻击，因为二进制内容被破坏，他们无法打开它。勒索通知本身看起来与Pandora和Crypt赎金通知非常相似，其中一部分甚至是复制/粘贴的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQqnT2TmFUAyRqpFU6DyOROAZA1zkwtR3G7rENI7UrVpNxdKdWEdeHWw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

加密文件

通知中没有官方的赎金名称，也没有tor网站的URL。联系勒索软件运营商的唯一方法是通过电子邮件。

目前像Minerva Armor这样的勒索软件保护平台会通过模拟勒索软件积极试图避免的环境数据，轻松防止CatB勒索软件。例如，当勒索软件查询处理器的数量时，Minerva Armor会让它相信自己所处的环境只有1个CPU，从而自动退步并终止运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQLLQVpjNIXD4lfAHGKJY6O23aNepRWNCRyRpiafoZiaUNqiaicALYxGQFsQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibfvobgssWd4dQBKUtIeSAQDpnmvR3j6sibAkAk9Tc4L2Aow1UCibBP3RKXU7165IR7FfnxVsgibPp4A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**参考及来源：**

https://minerva-labs.com/blog/new-catb-ransomware-employs-2-year-old-dll-hijacking-technique-to-evade-detection/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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