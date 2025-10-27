---
title: Windows 2000系统的一个0day漏洞发现过程
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458495738&idx=1&sn=97f941a0ee1dfbaddc067923a065c7fb&chksm=b18e9a7086f9136614e6e161d91ee6ce3bb13b7f943441a293454e435443a1542bedc0b5efbb&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-03-01
fetch_date: 2025-10-04T08:20:36.591272
---

# Windows 2000系统的一个0day漏洞发现过程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIJGlKArlT1NX3FPuTibakQd4bicFYaRUSibUW9iaIpu0yDEXexs71XibzS7A/0?wx_fmt=jpeg)

# Windows 2000系统的一个0day漏洞发现过程

Qfwfq-

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIGeR1MJZQRFN34UwfQXyQGA1WxEOE9UE5x14qWqSU8vKNRu5yiba2bpA/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：Qfwfq-

其实安装这个系统的本意是折腾老游戏，装点菠萝1之类的玩玩，结果找到了个漏洞。

这个漏洞位于cmd.exe，是一个缓冲区溢出漏洞，我在公开资料上没有查询到该漏洞的任何信息，也不知道是我没查到，还是确实没人公开它，如果有谁查到这个漏洞的信息了记得提醒我一下。

**实验环境**

Microsoft Windows 2000 5.00.2195 Service Pack 4

**用到的软件工具**

010Editor

ollydbg

IDA pro

##

```
一

## 漏洞简述
```

cmd.exe是windows系统传统的命令行小工具，从最早的windows系统一直到现在的windows 11都有这个小工具，当利用这个小工具对FAT32格式的磁盘目录进行dir操作时，若该目录里的文件的文件名长度刚好为260个字符时，cmd.exe进程崩溃闪退。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppI9Rribm712vTBiaxWMlicqPE85Gltq6I1KIVSgdH7Dv73x0bcNjK4kZTeA/640?wx_fmt=gif)

##

##

```
二

## cmd.exe的漏洞发现过程
```

**文件构造**

本漏洞需要在磁盘上构造一个文件名长度刚好260个字符的特殊文件，但是windows系统在资源管理器或者命令行工具里不允许文件名全路径长度超过260个字符，所以需要借助二进制编辑软件对磁盘分区卷进行直接的编辑长文件名目录项，构造这种特殊的文件。这里我用了010Editor。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIDhic2s3u8Qy7ftSQkXRna1ze7k7MqoJc2XicDP17cCnEb1AQgXvg6Khw/640?wx_fmt=png)

我在U盘H分区根目录建立一个共有20个长文件名目录项的文件，由于一个目录项32字节里有26个字节可以存储13个宽字符的文件名，这个文件的长文件名为aaaaaaaa…..aaaagf，一共有260个宽字符。

**漏洞跟踪**

将构造好的U盘插入Windows 2000系统，在ollydbg中开启cmd.exe进程，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIPBKibxZfzibLC5EDzybmib7ChDwUz2G3viaXvmSUhtE8Qj1tkqFbNSibkdw/640?wx_fmt=png)

在命令行窗口执行dir e:，进程出现异常。这里我用了污点数据追踪的方法来找程序的crash point，也就是说在堆栈区找到我们构造的污点数据aaaaaaaa…..aaaagf，在这个数据附近寻找函数一开始压入的返回地址，从而追踪到溢出点，整个过程如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIX9BBO2bkbTVCvrUTUAPbGwbqkPiajiaDpGkdjkAd25HfDatibYgOSU8lg/640?wx_fmt=png)

> 顺便一提，在不同的机器上程序的crash point可能不同，比如说在家里的另一台电脑上进行实验，crash时的Call stack是长这样的：
>
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIOLNTiaicfjB2jRSocobPV4kB0d50SB1cS4XxqFJtCkCicmFsDONDnC94w/640?wx_fmt=png)
>
> 直接就可以定位到4AD0E060的位置，都不用追踪污点数据了。

在4AD17B34处调用的wcscpy，将字符串拷贝至栈空间ebp-20c，该空间大小0x20c可以放置262个宽字符，似乎不能造成栈溢出，但事实上在4AD17B34处设置断点，再次进行dir e:，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIhfkncxteiaCuWCUick4Dneb6jYyfEugSwg6SQeFIbjDPqMxt2QqArqHQ/640?wx_fmt=png)

执行完wcscpy后，函数的返回地址被覆盖，如下图（执行前、执行后栈12EA70处的值）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIiabehoiadlztBAWMCxaIK2KO02lc2SPOkPfQb8bjibbdZBmSpCzuH9TFA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppI9kxckLqzZBZib0Rtz6UiaP2LL0DVJ1uhmIs9TXmzgLP9UM8wzHTPMVicQ/640?wx_fmt=png)

堆栈缓冲区的溢出，覆盖了函数在栈12EA70处的函数返回地址和后续的栈结构，继续进程执行由于栈的破环造成对非法地址的访问而异常终止。

```
三

## 缓冲区溢出漏洞的成因
```

现在的问题是，我构造的长文件名只有260个宽字符，占有0x208个字节的空间，wcscpy拷贝函数的目的地址栈空间明明有0x20c个字节，为什么有足够的栈空间也造成了溢出?

进一步的追踪源字符串的来源，发现cmd.exe程序调用了系统内核模块kernel32.dll的导出函数FindNextFileW对目录中的文件进行遍历，依次得到目录中的长文件名，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIbiaiaBsqL7nIG2N4XoZ5QVYrQicjg5oOoCVQZWkX9Hjdxt8O2rF2icXMsw/640?wx_fmt=png)

Windows2000的FindNextFileW函数在对刚好为260个宽字符的长文件名进行的遍历时，获得数据存储在类型为WIN32\_FIND\_DATA的结构中，该结构体的定义如下：

```
typedef struct _WIN32_FIND_DATA {    DWORD dwFileAttributes; //文件属性    FILETIME ftCreationTime; // 文件创建时间    FILETIME ftLastAccessTime; // 文件最后一次访问时间    FILETIME ftLastWriteTime; // 文件最后一次修改时间    DWORD nFileSizeHigh; // 文件长度高32位    DWORD nFileSizeLow; // 文件长度低32位    DWORD dwReserved0; // 系统保留    DWORD dwReserved1; // 系统保留    TCHAR cFileName[ MAX_PATH ]; // 长文件名    TCHAR cAlternateFileName[ 14 ]; // 8.3格式文件名} WIN32_FIND_DATA, *PWIN32_FIND_DATA;
```

在windows系统中常常把MAX\_PATH宏定义为260，cmd.exe通过FindNextFileW函数遍历得到长文件名和短文件名在内存空间中相邻存储，当磁盘上的长文件名数据刚好260个宽字符时，造成了两个字符串的合并，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppILy6USMp62lhHtYiamyibCGoFg8rkhbr6icRgo8GmhVvXXCUpXexA9ek3Q/640?wx_fmt=png)

进一步研究发现wcscpy的第二个参数指向的源字符串为从磁盘上得到的长文件名，其后紧接着的为该文件的短文件名，正常情况下的长文件名后按照字符串的结尾规则以‘\0’字符结尾表示字符串结束，但当长文件名长度为260个宽字符时，长文件名最后没有结束字符‘\0’,长文件名和短文件名变成了同一个字符串，短文件名占据了12个宽字符，这样源字符串的长度为272个宽字符，占据了0x220的堆栈空间，从而造成了返回地址及栈结构的覆盖。

```
四

## Windows XP SP3系统以及后续的Windows系统中是否存在该漏洞
```

进一步的，我对Windows XP SP3的cmd.exe小工具进行了逆向分析，发现与windows 2000的代码极为相似，不同的是Windows XP SP3启用了GS保护，大多数函数中都进行了堆栈cookie的校验，但是GS保护只能增加漏洞利用的难度，并不能杜绝缓冲区溢出对进程堆栈结构造成的破坏，若程序代码相同应该存在同样的漏洞。如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIk9JZrQSibrDiav7UDVsQ7ia1M5CZVYrBdzlIcyovGuXauhAHmpa8NFUqQ/640?wx_fmt=png)

在XP系统中，目的字符串的空间为0x210仍然小于长文件名+短文件名后的最大长度0x220，仍然具备潜在的被溢出覆盖的可能性。

然而事实上，在XP系统下对构造后的U盘进行dir 操作时，并没有造成进程闪退，而是将文件名的最后一个字符舍弃后显示文件名，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIPs7gHFtpIwPiaKALyV2KmEAVI5bhfRibZ7Hrllc94ib97icQlLjEjsbiaUQ/640?wx_fmt=png)

这说明在XP系统下该漏洞并不存在，为了进一步澄清两个系统的不同，我对XP系统的kernel32.dll的FindNexeFile函数进行了逆向，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIMthzp1AQxKkbvZWaRAIImCHFWicNgkSavJuMPJ2pb9qsQfrnpecGRicw/640?wx_fmt=png)

Windows XP的Kernel32.dll的FindNextFileW函数对文件名的长度进行了检测，若长度大于0x206的文件名，取值0x206,这样该函数遍历得到的文件名最长259个宽字符，仍以字符串结束符’\0’放置在最后一个字节。由此可以合理推测，高版本的windows系统已经修补了该漏洞。

```
五

## shellcode
```

Windows 2000系统没有任何GS，ALSR，DEP等后续Microsoft公司在安全方面的提升，所以可以很方便地利用该漏洞编写shellcode执行任意的程序，这里写一个启动计算器的，以下是构造的文件与对应的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIzxJ4duACBRq3Zr8oTmpJ8ec2alr8IJZXzMg6pqDlRXDicxbeSRse13A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIH5N0VutVGTe2MK2bP4ouBNvD2hrYDaBynKDgsokqeeZSLWZAAUezDw/640?wx_fmt=png)

上传格式不支持，最后的效果请点击文末阅读原文查看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HRDSMrF29iba77vF5oibDibrJKEice3IGtMzk8tZjqT7icVRvJSlicjhdvBjQrZTsMYuL2OSst4FnicbrRw/640?wx_fmt=png)

**看雪ID：Qfwfq-**

https://bbs.kanxue.com/user-home-968912.htm

\*本文由看雪论坛 Qfwfq- 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HRDSMrF29iba77vF5oibDibrJxGv963ksmgEUh7vaCEEPwwdHtHybDJ6neG8FHHN1Ym7CVOV2ctPXEw/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458490684&idx=3&sn=8affe7650627d2e5a9cd81c803927de2&chksm=b18ea7b686f92ea074e421f09e4dd4c01088bb7293513e81317750c3866eebefd61e0d99e1b2&scene=21#wechat_redirect)

**#****往期推荐**

1、[wibu证书 - asn1码流](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458495696&idx=1&sn=ea643585c5b3cefc1e892e55dff9f5e3&chksm=b18e9a5a86f9134c4dcf0a8c2576538494f531be8c3c3580a95bb49598596571e646ec76a077&scene=21#wechat_redirect)

2、[COM 进程注入技术-编程技术](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458495654&idx=1&sn=fda03d0b225787f95a6491224c6b38fb&chksm=b18e9a2c86f9133a21a02d401841d2bad5190702ef38af652426a6b19afad4f0c8507edb12e1&scene=21#wechat_redirect)

3、[记录调试Windows服务的操作](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458495653&idx=2&sn=8fb257956eaf0063fd500e4548157f67&chksm=b18e9a2f86f913395a67a4c38e2f94ce34b52c547d8439eacf3d455dd63aeae8de434046feb3&scene=21#wechat_redirect)

4、[通过AFL++复现sudo漏洞的一次尝试](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458495629&idx=1&sn=cd163140cd2a646d1c721aaa2078d841&chksm=b18e9a0786f913115a83c9b0921476507e40f2b654c8f74909a28cc2986296f5c4688ecbeeed&scene=21#wechat_redirect)

5、[浅析信息的表示和处理](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458495256&idx=1&sn=a7a40804328b9112e0f63576d3a67127&chksm=b18e999286f9108422a9ff311eb7b033bc6ffed28a1913b3d3f87022b07892aa2ec2998f3fe3&scene=21#wechat_redirect)

6、[CVE-2016-7255提权漏洞学习笔记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458495053&idx=1&sn=e037fbe4c1ee7d86342985897cf1e6f5&chksm=b18e98c786f911d13201a01d3626398637a97f524d39d9cf191d212505874b40e2097f7fe9a3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://...