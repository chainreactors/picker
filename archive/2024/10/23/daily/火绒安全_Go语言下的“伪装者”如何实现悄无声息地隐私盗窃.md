---
title: Go语言下的“伪装者”如何实现悄无声息地隐私盗窃
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247520224&idx=1&sn=d1a5a7fe57e9a21c96a6da2514efcd7a&chksm=eb7051dfdc07d8c9feeb82e1768cf915f415905482a4cfa52c58cd6003e587f56e4e6c66711c&scene=58&subscene=0#rd
source: 火绒安全
date: 2024-10-23
fetch_date: 2025-10-06T18:53:01.011872
---

# Go语言下的“伪装者”如何实现悄无声息地隐私盗窃

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibJk3SkG411CubgjpIO6ciaHApRSq70NE8icr4QwF6icGtnLia7nDpnG0oDg/0?wx_fmt=jpeg)

# Go语言下的“伪装者”如何实现悄无声息地隐私盗窃

原创

火绒安全

火绒安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4nrnOI1emtFr0UYnrLKytAvy2gia6ZuIUJs14h2pEIwpiaWPCTTuCQIDibx9dlfXoyrNyVEWb8DVUUA/640?wx_fmt=gif&from=appmsg)

近期，火绒工程师在日常关注安全动态时发现，Lumma Stealer 木马家族会利用 Go 语言编写注入器，通过 AES 解密创建傀儡进程并注入恶意代码窃取用户信息，其中恶意代码经过控制流混淆、常量加密以及手动调用系统调用号等方式使代码复杂度提高，更难以破解。分析发现该样本会利用 Steam 账户名称、动态获取远程服务器域名，根据下载的 JSON 配置窃取相应应用程序数据，例如浏览器数据等，此外还会窃取邮箱、Steam、Discord、TXT 文件等数据。目前，火绒安全产品可对上述窃密木马进行拦截查杀，请广大用户及时更新病毒库以提高防御能力。（文末有彩蛋掉落）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewibwz9fwjiaFnZkKNcqg45O3V3WAY6qqVN2fUDfeRe1ev07q3ZItxGTE8Q/640?wx_fmt=png&from=appmsg)

查杀图

Lumma Stealer 是一种商业窃密木马，该木马于 2023 年开始在论坛上公开售卖。从 Hack Forums 论坛这篇帖子上可以发现该木马更新频率高，可对某些失效的窃密手段进行及时修补，且会经常更新代码混淆器，进行免杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibNsftse7n9TwGAggIZZXhyu6a9ZDAactoicKsRU7CnicEyZ9iaqczAEF8w/640?wx_fmt=png&from=appmsg)

售卖帖

样本执行流程如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibTqh94fALvbUODQJx2lT8ulW4yNxDF2FhwqMewodO1fqn6LhYZCADAg/640?wx_fmt=png&from=appmsg)

流程图

**一**

**样本分析**

该样本以 Go 为注入器，注入步骤主要由解密 Lumma Stealer ShellCode、创建傀儡进程、注入 Lumma Stealer ShellCode 组成。

**注入模块**

解密 Lumma Stealer 数据：

将字符串 a2f045451b2c742c6e17d6d046804e73 进行 MD5 计算，得出 AES 密钥 48901d3cdcfd61d216a912a7bd4a17a7，使用该密钥对长度为 310300 的数据进行解密。解密过程使用了 Go 标准库中的 crypto/cipher 和 crypto/aes，最终获得 Lumma Stealer 的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewib9ODPul7GoicjGFyS4EDI04SBFyq5MnphfRUWxqtbmQqARpE6Bet66qA/640?wx_fmt=png&from=appmsg)

解密秘钥的来源

解密 Demo 如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewib9YbX9L3vGILYndmuUeSECE775t856BlZGPcXEyXnzdN96mBricwdn7w/640?wx_fmt=png&from=appmsg)

解密 Demo

创建傀儡进程：

利用库函数 path/filepath.Walk 遍历 C:\Windows\ 目录，遍历过程中通过检查文件后缀名找到第一个以 .exe 为结尾的文件后，使用 CreateProcessW 创建进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewib3IYuslE7d0NTDCnMW476T6WKTO5siaZ5HRFFibgOLjKvkokicAhGtjiaFQ/640?wx_fmt=png&from=appmsg)

遍历文件并判断文件名后缀

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibhnhwmkC2X8FL9ju0aakaNjOuBT2p5fhanGCv3VNueuaS6apZSfMhIw/640?wx_fmt=png&from=appmsg)

创建进程

注入代码：

随后在创建的进程中调用 VirtualAllocEx 函数分配可读、可写、可执行的内存，调用 NtSetContextThread 函数指定 EIP 为 ShellCode 入口点，调用 NtWriteVirtualMemory 函数写入 ShellCode，最后调用 NtResumeThread 函数使线程继续执行，从而执行 ShellCode 代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibnFTVC4UJnH4F01iaKic5S4HdDa5ATZNx4k9Hd5zh26jQoKovcxrZgtwA/640?wx_fmt=png&from=appmsg)

分配内存

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewib1AKb7WibnicFL9VE5XKibC2noHJfvYdkxoedQDibwAKG2yV98EfHneib0mw/640?wx_fmt=png&from=appmsg)

修改 EIP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibpABUNOxNdpicRDKcqJ2wicjQ4gA8BjO5J5LqyUbVsQmhVASYLTmh45cA/640?wx_fmt=png&from=appmsg)

写入 ShellCode

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibnY2WuHaRN928EDE0M1AAtSlF9wG2XGUrVzuJCzhjnSZJPr5Y8IUMRA/640?wx_fmt=png&from=appmsg)

恢复线程执行

**窃密模块**

窃密模块分为以下阶段：

准备阶段：准备哈希/调用号表、检测沙箱、检测语言等操作。

通过配置窃取信息：从远程服务器下载 JSON 配置，通过动态获取到的规则窃取应用程序敏感信息。

固定窃取：窃取邮件、Outlook、ThunderBird、Steam、Discord、TXT 文件、剪切板、截屏、系统信息等数据。

自删除：如果下载的 JSON 配置中键 "ad" 值为 true 时将会进行自删除，具体方法为 CreateProcessW 创建进程 cmd.exe "start /min cmd.exe "/c timeout /t 3 /nobreak & del "当前进程路径"。

**准备阶段**

通过 fs:[30] 获取 PEB 地址，随后遍历模块链表，通过比对模块名获取 ntdll.dll 的模块基址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibB3VgzyXe1DGYKTsmEjqaAic97X5EJ7FLfNfHnTWNFDo76m2tia77Niaxg/640?wx_fmt=png&from=appmsg)

PEB 地址获取

随后遍历导出表中的函数，获取函数名计算其哈希值。然后将以 Nt 开头的函数名哈希值和对应的系统调用号存入内存，以便之后通过函数名哈希值查找系统调用号，并通过 Wow64Transition 手动调用系统调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewibb0kT4E9q1moCdtzp7fyicOl9UhTrstdxzibFCNZg5fBfmCfODGS3MImQ/640?wx_fmt=png&from=appmsg)

获取函数名哈希值和调用号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibKJcUKPvj7wJofsEA7JvIDh1cCYaZWAGVx2TdnnfPJfVYADic6Upicuxg/640?wx_fmt=png&from=appmsg)

函数名哈希值与系统调用号内存布局

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibZlLu6LvTFZSNs4I1jFNeHwzFUgvcElaIheiaQweqguwJ8F57J7vR97A/640?wx_fmt=png&from=appmsg)

函数调用逻辑

之后利用上述调用系统调用的方法调用 NtOpenSection 获取 \KnownDlls32\ntdll.dll 句柄，然后调用 NtMapViewOfSection 函数将文件数据映射到内存中。再次重复将函数名哈希值和系统调用号写入内存的操作，推测这一步是为了防止安全软件修改过进程启动时加载的 ntdll.dll，所以选择以内存共享区域中的 \KnownDlls32\ntdll.dll 为标准再次获取系统调用号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibibUljMxu08zG6SNGBI1xZGnficJDqF3ibhBtyhy2oKNl2PcF3LqHP0dEw/640?wx_fmt=png&from=appmsg)

打开 \KnownDlls32\ntdll.dll 内存映射句柄

利用 NtSetInformationProcess 传递 ProcessInstrumentationCallback 参数设置回调为空，用于防止被安全软件检测到样本的系统调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibiavCs74pnCnR6MSQlmaMIVmMsvCBLTSOeWEpQ9Y4DOQLNoXg0Am1Nfg/640?wx_fmt=png&from=appmsg)

调用 NtSetInformationProcess

通过遍历模块名计算哈希值判断是否在沙箱中，如果存在就会终止程序。

下图是通过网上比较常见的沙箱会加载的模块名计算比较得出的结果，其中一个没有被识别到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewib7tiaT4M972V93Rwm2Dju2Qh4SPa7NqHkPLE4uoy2Wuib90ic8LQ5CpjuA/640?wx_fmt=png&from=appmsg)

沙箱列表

以下是上述检测沙箱时会用到的模块名哈希算法，第一个参数是模块名，第二个参数会传入固定值 0x18D40B1A。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibrSNgibwVEH4PUyQMoJhL5VSoHiaCfvPnSicbaZ4nicTGaHsvZibaqvdX1wQ/640?wx_fmt=png&from=appmsg)

计算模块名哈希值

还会通过调用 GetUserDefaultUILanguage 函数检测语言，具体代码为 0x419：俄罗斯。如果是俄罗斯语言则不会进行窃密操作，如果不是则继续。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibHAGibuiciczZowfMQHGRZnD9wQ9REON9GyBxMpYPoibaTlnMkFLJgL5hKQ/640?wx_fmt=png&from=appmsg)

不支持警告

**下载配置信息并开始窃密**

**获取远程服务器：**

该样本通过域名轮询的方式，循环连接多个候选服务器，直到成功建立连接。如果所有候选服务器都无法连接，样本会访问 https://steamcommunity.com/profiles/76561199724331900，获取页面中的 HTML 数据，使用 <span class="actual\_persona\_name"> 和 </span> 标签定位 Steam 账号名称。随后通过提取的 Steam 账号名称解密出远程服务器域名，目前分析时解密出的域名为 sergei-esenin.com。

由于 Steam 账号名称可以随时修改，木马作者能够通过动态更新 Steam 名称来控制和更新远程服务器的域名，从而保证样本的远程服务器持续存活。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewib98cYwIL19rJQcmKLkYbYu0quZyNfsN1MhYvNmXchPZbVJ0kKIibMyxg/640?wx_fmt=png&from=appmsg)

动态获取函数地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewiblhia0U8Y4bs1cA8908GKeS0pdw0iatz6xf5CfnzicmwR4N0HM2ibiaPvzDA/640?wx_fmt=png&from=appmsg)

获取远程服务流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibSC6IjQkLdg9MKmibObGKuYdaTpatjdIz6nkL0TTlBdo8w6bubDicibAwg/640?wx_fmt=png&from=appmsg)

Steam 名称

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibVFKkGOaqkvLHE1abE1qxXf6Q0HaenWSaZR4RAoRq4kvbFJuTAxVOlw/640?wx_fmt=png&from=appmsg)

Steam 名称 URL 解密代码

**下载配置信息并利用：**

样本通过 POST 请求向 https://sergei-esenin.com/api 发送数据，请求参数包括 act=recive\_message（用于指定服务器行为）、ver=4.0（版本）、lid=xAeOdp--mainteam 与 j=15f7911c5c73e2c263a9b433eb55ff31。服务器响应返回加密的 JSON 配置数据，包含需要窃取的应用程序配置信息。之后对返回的加密数据进行 Base64 解码，随后通过异或运算与位运算的组合还原解密出 JSON 配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibeDPLA5IOib3lia6aM518VGdgEc6MANHIs9lYQt9794G34ZcvEQianiak1Q/640?wx_fmt=png&from=appmsg)

JSON 数据解密算法

可以看出 JSON 数据中包含重要文件、比特币钱包、浏览器配置信息，密码数据库等，该木马会按照该配置中的路径获取文件，最后会打包成压缩文件并发送到服务器中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9Ewib5xYGeyXtb2Ij6OXrvkvUeWtZXW3pr4TRjjBUibl0ruYDJ5sAC1MBumQ/640?wx_fmt=png&from=appmsg)

部分 JSON 配置信息

下图是其中一个 Chrome 用户信息的压缩包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibI9pQvKZDbEXBT6OibAE1rP7PR3uFA4nTtLL4X26roV7kkxHiauGDkv2A/640?wx_fmt=png&from=appmsg)

压缩包

如果解析 JSON 数据时获取 se 的值为 true 则会截屏发送当前画面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4tpZicnuicCo5r0QL2My9EwibXDMr3y6BKsuZzjwyibYxPgsNBUbTJo4mOPbqTQfiaNZNcKaM47g9Ci...