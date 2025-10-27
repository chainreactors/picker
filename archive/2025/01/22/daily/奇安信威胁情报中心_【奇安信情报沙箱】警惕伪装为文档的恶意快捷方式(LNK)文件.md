---
title: 【奇安信情报沙箱】警惕伪装为文档的恶意快捷方式(LNK)文件
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247513822&idx=1&sn=9d52dc150c8ee53e3af6d7ae908c596b&chksm=ea6641a9dd11c8bfb5ef721db9b91c0777ce08c04211ac969b6a5cdc765c24b02f6b576a8c15&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2025-01-22
fetch_date: 2025-10-06T20:10:38.289096
---

# 【奇安信情报沙箱】警惕伪装为文档的恶意快捷方式(LNK)文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23rSHmo8ok9ZDzME5yUBRy3L5HAvUV7ibVkhZz9F41z3G0PCG0UGjQ3fg/0?wx_fmt=jpeg)

# 【奇安信情报沙箱】警惕伪装为文档的恶意快捷方式(LNK)文件

原创

威胁情报中心

奇安信威胁情报中心

概述

近年来，随着微软对 Office 文档中执行代码等各类限制的收紧，以宏代码、已知漏洞利用等方式发起攻击的文档类恶意软件攻击能力被削弱。面对这种情况，攻击者也转变思路，不同 APT 组织和网络犯罪团伙开始频繁借助快捷方式（LNK）文件投递恶意软件。

通过给 LNK 文件添加合适的文件名和图标，攻击者就能将其伪装为 Word、PDF 等文档，诱使受害者点击。与在文档中启用宏代码不同，点击 LNK 文件之前不会出现安全风险提示，并且打开 LNK 文件后往往有正常的诱饵文档展示在受害者面前，进一步降低受害者的警惕心。

奇安信威胁情报中心以近期日常运营过程中发现的一个样本为例，展示恶意 LNK 文件会如何导致受害者设备沦陷并被窃取数据。该样本为 ZIP 压缩包，其中包含一个 LNK 文件，ZIP 包可能是通过钓鱼邮件等方式传播的，LNK 文件名伪装为 txt 文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23HbCicdI0404NMg4NzAoaibM34Y4c1XYqWjgFA36o7byuqhIDX1cODqgQ/640?wx_fmt=png&from=appmsg)

为了快速获取样本执行的恶意行为，先将其上传到奇安信情报沙箱（https://sandbox.ti.qianxin.com/sandbox/page）进行分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23gFjGLPUvVBv69tMMI0LT5OXkPK6KIwbJc60P24ibYlsvBlnTibn54JlA/640?wx_fmt=png&from=appmsg)

沙箱分析

样本基本信息如下：

|  |  |
| --- | --- |
| **奇安信情报沙箱报告链接** | https://sandbox.ti.qianxin.com/sandbox/page/detail?type=file&id=AZRowPB0ONZSmF3-3YXd |
| **样本文件名** | ad0c.zip |
| **样本****MD5** | ad0c4953bb364506b5a056974a812004 |
| **样本类型** | ZIP |
| **样本大小** | 43898字节 |

上传分析完成后，可以看到该样本的基本信息：包括文件大小、类型、hash等。奇安信情报沙箱基于智能的恶意行为综合判断已经识别出文件可疑并给出了10分的恶意评分。基因特征部分带有”powershell”标签，表明该样本会执行powershell代码。该样本曾在多个不同的沙箱环境中运行，在右侧可以切换分析环境查看不同分析环境的沙箱报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23MUtZfecqZqRKTkictRct0ib49GiaQdbOyRaX3KczbRw4uichxyuaiczN0Gw/640?wx_fmt=png&from=appmsg)

在样本基本信息下面紧接着**威胁情报AI助手**对此次沙箱分析结果的总结内容，可供用户参考。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23bHyx99OQTU5lhDSPPNUMhJUXCUycGu115l37f1ahicopLAU2Rcict0KA/640?wx_fmt=png&from=appmsg)

**AV引擎**部分显示了数十家杀软引擎对样本的检测结果，可以看到多个杀软引擎判定该样本为恶意。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw231Eb4h05SLBdesa0STqdHSFVPSOWzVYhibZxrjclrJB4ZgRSBb0yJI2Q/640?wx_fmt=png&from=appmsg)

**行为异常**总结了样本的可疑行为，右侧带向下箭头符号的条目可以展开详细信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23SFUKpUr7ichEE0Ot2LWPrNEHCKYPZ0pC2tZ6GPyXibxUKNptOKmQxbBA/640?wx_fmt=png&from=appmsg)

该样本有一些值得注意的异常行为，包括在 TEMP 目录中创建了一个可疑的 EXE 文件 tmp2131268457.exe，并且该文件通过名为 WinTask 的计划任务实现持久化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23NtOWiavnqibqbmibTickvM5PX0quFPfZAmf0StrdviarKj8s0ibbRQicgWbQg/640?wx_fmt=png&from=appmsg)

向远程服务器发送 POST 请求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw239lUY1GaRCTqov0atKSB5pU2NGp9Iqon2xlReSmbibUXNgTiaOeW38k5A/640?wx_fmt=png&from=appmsg)

访问浏览器保存的个人数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23FeRaNP2AxZQS3tnX35pT5RXkdDD6pksYgyl3zhJeibibesuU27AjS2bA/640?wx_fmt=png&from=appmsg)

**主机行为**的进程信息显示 ZIP 压缩包中的 LNK 文件释放后，执行 powershell 代码，进而启动 tmp2131268457.exe，再由 tmp2131268457.exe 调用系统命令 schtasks.exe 创建计划任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23sYPhiaibXOhKyY1HRoibZzNpsSv7jvBB7WvLugiadhynuyE7icciahn71eZA/640?wx_fmt=png&from=appmsg)

**网络行为**部分显示了样本与 hxxp://128.199.113.162/XtfcshEgt/upwawsfrg.php 存在连续通信行为，正是 tmp2131268457.exe 所在的进程建立了与 128.199.113.162 的网络连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23Aby3qyF3p3z4gxgP0YzZ4AXWYYbuJLrlqVUAPOia5pvibBo7GHh4Yh7w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23QXiahp5e9RHLpjYMGZOMNiahyibnBVuEynaoU7wBM7ySOJPPzxa1Ydzbg/640?wx_fmt=png&from=appmsg)

**释放文件**中可以见到许多txt后缀文件，这些文件均是由 tmp2131268457.exe 创建。这些文件路径名称表明，恶意软件会窃取系统中多个目录、浏览器、加密货币钱包相关的数据信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23Lodd388qOuhy1ibhfgxgY9aUaSOOP8NOicKbibEnLiajEwQZE5BgwiaT00Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23pY9HRTJE31CVDBm8u7SXuyRyeKqu6s2pND8ne85ZZvm4vTKfkGcNuQ/640?wx_fmt=png&from=appmsg)

根据奇安信情报沙箱提供的信息，我们对该样本有了初步的了解：该 LNK 样本伪装为 txt 文件诱使受害者点击查看，然而一旦受害者点击将触发 powershell 代码执行，创建一个 EXE 文件，该 EXE 文件通过计划任务实现持久化，与远程服务器建立 HTTP 通信，并窃取设备上的多种数据。

详细分析

**LNK与后门**

ZIP 中的 LNK 文件使用 notepad 图标，结合文件名 ”Exodus.txt” 让受害者误以为是真实的 txt 文件。LNK 中的 powershell 代码从自身提取出 EXE 数据，将其保存在 TEMP 目录下，以 ”tmp+随机数”的方式命名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23GWIJoLab6xduibFbic8NYV6Faziab0O33wzcjov7lqFgHyOnYgfqtDPLw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23FkTmKU4XGU2VLkwHyfclVCrRclcNfjYX3RcOzAtBuibLL8oT5CVmTdQ/640?wx_fmt=png&from=appmsg)

释放的 EXE 为 C# 后门，图标和文件信息伪装为 Chrome。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw231GXmoCNgjAtibSvZYPOsb1myvQfh0b14KXxBoqfQrXGljD6EzO75tibQ/640?wx_fmt=png&from=appmsg)

后门中的关键字符串经过加密处理，使用时调用 Type\_0.Method\_0 方法进行 AES 解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23WXXHbdianzfrrDibvtZiazu1moXePFx7eSyJFIF7NWW5OVEK3Brffowkw/640?wx_fmt=png&from=appmsg)

后门执行如下操作：

（1）首先通过检查运行环境的机器名和用户名判断是否在沙箱中运行，如果与内置的名称相符则立即终止运行；

（2）收集感染设备的各类信息，包括：用户名、机器名、操作系统版本和位数、网卡 MAC 地址、CPU 名称、显卡名称、物理内存大小、屏幕分辨率、设备 UUID；

（3）查询名为 WinTask 的计划任务是否存在，如果不存在则创建该计划任务，设置为每隔 5 分钟执行一次，该恶意程序没有使用循环语句封装与 C2 通信的代码，所以该计划任务实际上还起到构建 C2 通信循环的作用；

（4）从资源区释放出诱饵文件 p.html 并打开；

（5）向 C2 服务器回传收集的信息和截屏数据，然后根据 C2 服务器的响应执行具体的后门指令。

C2 通信的 URL 为 ”hxxp://128.199.113.162/XtfcshEgt/upwawsfrg.php”，后门代码中的指令分发逻辑如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23VVU8gd3r7JTAE7DqXlpaAXt65uLcDBWZmtqEmqtnbcFZVTORIJrYEA/640?wx_fmt=png&from=appmsg)

后门支持的功能如下。

|  |  |
| --- | --- |
| **后门指令对应方法名** | **说明** |
| **Type\_7.Method\_21** | 从C2服务器下载后续载荷并内存加载执行，下载时使用的URL为”hxxp://128.199.113.162/XtfcshEgt/upwawsfrg.php?zd=3” |
| **Type\_7.Method\_20** | 使用cmd.exe执行命令，执行结果回传C2服务器，回传数据类型名称”cmd” |
| **Type\_7.Method\_19** | 收集更多的设备信息并回传，回传数据类型名称”sysinfos” |
| **Type\_7.Method\_17** | 将用户Desktop目录打包为ZIP文件并回传，回传数据类型名称”Files.zip” |
| **Type\_9.Method\_45** | 从C2服务器下载后续载荷并内存加载执行，下载时使用的URL为”hxxp://128.199.113.162/XtfcshEgt/upwawsfrg.php?zd=1” |
| **Type\_7.Method\_18** | 截屏并回传，回传数据类型名称”screen” |

后门向 C2 服务器发送数据时，使用 POST 请求，回传数据类型名称和数据内容均经过 RC4 加密，并进行 Base64 编码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23Jh5rvzbmJHgFrMPKFB357GeRiaibHggWuoKmiaMjGw7qlabJ8GoNkBU6A/640?wx_fmt=png&from=appmsg)

请求首部 User-Agent 字段使用硬编码字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23hhmaibJb7Tgho4ibkLenBFf2xiciacLN16mcdYwQfjeGGicNKXh5kRjEicjQ/640?wx_fmt=png&from=appmsg)

请求首部 Cookie 字段包含了收集的设备信息。将收集的设备信息拼接为 JSON 字符串格式，然后在前后添加 ”ZZ#”，对最终得到的字符串使用 RC4 加密和 Base64 编码，加密结果伪装成名为 ”SESSION” 的 Cookie。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23hYZPYwHZPOxJhLaUn2dVwZ8kYZuks1o8DvgE3zxiaIRAkQZ2JjHMtQA/640?wx_fmt=png&from=appmsg)

设备信息中 ZIZI\_VERSION 可能表示恶意软件版本，为 3.81。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23LLQqeZeKC2qvrMEE9mQPhZUltAQAZ713a2iaDOekcibKK8WibbnbPfRSA/640?wx_fmt=png&from=appmsg)

由于后门的网络通信使用 HTTP 协议，在沙箱下载的 PCAP 包中可以看到恶意软件与 C2 服务器之间的通信数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23OKLhAvMeMBqqjzK7NXfTEHJMofarC7oibzroAhiafVNQJAK4iaTdoOXew/640?wx_fmt=png&from=appmsg)

后门与 C2 服务器的首次通信会发送收集的设备信息和截屏数据，网络流量如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23oRPstMNFduF74QGRhUDRdibSgUE8SUoXF4HYvrZztnDNiaU01SH7kt3Q/640?wx_fmt=png&from=appmsg)

后门从 C2 服务器获取后续载荷使用 GET 请求，首部包含相同的 User-Agent 和 Cookie 内容。后续载荷经 Base64 解码和 RC4 解密后，直接在内存中加载运行。从 ”?zd=1” 所得载荷的文件名为 ”zzsteal.bin”，执行窃密操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw238f5dSIwCYYVIFJf6OQ01VGEZbQIkCGQZnerzuk3LMX9zIuVumOic9kA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9iceMRY1eiaRicHX7CDe4Fw23gT8I4lJibia4j4u5HoIm40BUCr8IuJOqiaRNrsnHEooTGwawPdyvwib71A/640?wx_fmt=png&from=appmsg)

**后续载荷**

分析时从 “?zd=3” 未能获取到载荷，从 ”?zd=1” 获取的后续载荷解密后是一个...