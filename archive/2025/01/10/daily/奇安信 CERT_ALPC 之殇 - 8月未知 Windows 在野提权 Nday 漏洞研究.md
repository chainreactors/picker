---
title: ALPC 之殇 - 8月未知 Windows 在野提权 Nday 漏洞研究
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502729&idx=1&sn=7ef5d7ec018d1cb5555c10fcdd5b2159&chksm=fe79ef11c90e6607ce559b542b8bd98818ca25459580709a7207e3cb503592487b4af411dd45&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2025-01-10
fetch_date: 2025-10-06T20:08:59.666681
---

# ALPC 之殇 - 8月未知 Windows 在野提权 Nday 漏洞研究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmS4BgCtMWoeCjibHVoQgsuk1lRJibWz5f2KWr7lWpuq9a9Ys4LeMhEibiaBQ/0?wx_fmt=jpeg)

# ALPC 之殇 - 8月未知 Windows 在野提权 Nday 漏洞研究

奇安信 CERT

以下文章来源于奇安信威胁情报中心
，作者红雨滴团队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7I8QeMG3CujdN79zxbczFS3XAMP0KcY9YcqkRIHEy7CQ/0)

**奇安信威胁情报中心**
.

威胁情报信息共享，事件预警通报，攻击事件分析报告，恶意软件分析报告

综述

该漏洞样本为前段时间奇安信威胁情报中心日常在野漏洞监控运营经发现，其最早被上传时只有6个查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmS6B6eD5WlBrIb1ymOO4BLwcShicXfr8n8KYcjuWGTTjxmL9lbTUFdQjw/640?wx_fmt=png&from=appmsg)

经过分析确认该漏洞应该是在八月的微软补丁中被修复，是一个被修复的未知nday利用，运行的具体效果如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmS0Qr4sI7mCic1PphsgQu5K2qDMUs19eD0I05BCRtSvF5o4Gh1Za3qd9A/640?wx_fmt=png&from=appmsg)

漏洞样本分析

这里首先过一下整个样本，样本开始首先启动了一个cmd，之后调用核心fun\_vulstar。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmShO9wqChtS7ia25uVKjoO8fZtyNRdHpBGKbl1eSQq82MiaWQsBcAHFwJA/640?wx_fmt=png&from=appmsg)

fun\_vulstar中判断当前的机器的相关版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSqRzrib0KQtEULmoRKLbyqBy8miapEONKoCqFp9Hxk8dpMBhkpKx5FkzA/640?wx_fmt=png&from=appmsg)

之后动态获取部分系统api的函数地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSkEFvOn1XOeib7GR9vNO9tcEYXjiatE1znibHm8rskibwJ025lBnflBmplw/640?wx_fmt=png&from=appmsg)

开启一个新线程，调用漏洞利用函数fun\_expProc。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSZU0jb1GYkDr8Mjn6FkTowEpVicO5jVYZooYjb9l25TtSQ655ym9qiaNg/640?wx_fmt=png&from=appmsg)

fun\_expProc调用fun\_IoRingandPipeinit。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSxt98A7XymW5cAibO8qCzwdZT6HqecQudic9N3vuPVVBKnNiarsNQ2wdPw/640?wx_fmt=png&from=appmsg)

该函数中判断目标系统的版本是否支持I/O ring的提权方式，如果支持，则完成相关的初始化工作，并返回 var\_ioringRegBuffers/var\_ioringRegBuffersCount，这种方式具体利用细节可以看以下文章（https://windows-internals.com/one-i-o-ring-to-rule-them-all-a-full-read-write-exploit-primitive-on-windows-11/），简单来说这是一种Windows 11 22H2+后独有的利用原语，可以将 Windows 内核中的任意写入甚至任意增量错误转变为对内核内存的完全读/写，在i/o ring的利用中通过任意地址写入修改\_IORING\_OBJECT对象的以下两个字段（var\_ioringRegBuffers/var\_ioringRegBuffersCount），从而实现全局内存读写。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmShMoFf7iaPFMllaUB0IHGRHPNwiaAibAmQsNl2RpeozZrmFae2qMEuZE6A/640?wx_fmt=png&from=appmsg)

之后根据是否使用I/O ring提权来完成先相关的初始化工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSgs9bxEeKzLGN49dWicc9Nzmt4E7wlChJ73ibuXribpeXFpKrwQHZibq18Q/640?wx_fmt=png&from=appmsg)

以使用I/O ring提权方式举例，这种情况下会在0地址上spray 0x2000长度的var\_ioringRegBuffers-0x2c地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSklJ6t30htbRydlribzXt2fZTMeeS0TaH0icuEfBibyT1m6KmFibja5hQ7w/640?wx_fmt=png&from=appmsg)

Fun\_init中则用于在0x1000000000的地址上分配长度0x10000的内存，并获取NtCreateWorkerFactory返回的WorkerFactory对象的地址var\_KWorkerHandleaddr。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSz9yKEqCCH4SRfpnVMmakV5CbFNZObJC8HiaPMJAaG5gZlHcEgZ8Grbw/640?wx_fmt=png&from=appmsg)

接着往下，进入一个大循环，其中fun\_NtAlpcConnectPort用于调用NtAlpcConnectPort创建一个Alpc连接对象，连接对象创建完毕，开启两个线程分别调用函数fun\_NtRegisterThreadTerminatePort/fun\_expWorker。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSABbmVgkINyxqo7icXsAZRWpWIymhAwxcwnCeBrlbfPibrIGCTuiccxCAQ/640?wx_fmt=png&from=appmsg)

fun\_NtAlpcConnectPort的功能很简单就是调用NtAlpcConnectPort，和系统的pdc alpc port 服务连接，并返回对应的alpc porthandle。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSefGrBCRydVRrLRhrY8Mq2AJ5bjbzhXEKwMkasNaZ8qFQkzHicGnPHTw/640?wx_fmt=png&from=appmsg)

如下图，两个线程开启后，调用fun\_setEvilmessage设置一段自构造的内存，之后通过WaitForSingleObject监控fun\_NtRegisterThreadTerminatePort对应的线程1是否结束，如果结束，则进入图中红框的部分，这里的核心是函数fun\_NtCreateEvent。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSrWyl317WdP3dQUOCbDulfswwdiciaWetOEicIfLJTMHjicTKvPLRxdeia5A/640?wx_fmt=png&from=appmsg)

fun\_setEvilmessage完成了一段内存的构造，其会根据一开始获取的系统版本，进入不同版本的内存构造。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSFf8PKQHickFCJksZk97Lk6JdAvibEb3X8icUxYZKJNhu6dHrphz1iaYVjQ/640?wx_fmt=png&from=appmsg)

最终的效果如下所示，构造的内存都是从66130这个位置开始，这里我们测试的系统版本构造的内存如下红框中所示，可以看到无论哪个版本，最后位置放置的都是前面获取到的var\_KWorkerHandleaddr的地址加一个偏移。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSgPWufbicxP1UnMqQPmWQYicIVgLq4oxz4G7fHibZBjxzqDcI30OeTuzJA/640?wx_fmt=png&from=appmsg)

可以看到fun\_setEvilmessage调用完之后，再次初始化了一段7FF7F21671B0 开始的内存，fun\_setEvilmessage中构造的7FF7F2166130被放置到7FF7F21671B0 +0x20处的7FF7F21671D0位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSaRgxbU7IAxydqMFCCXaPoT74XAwVyONXhzG2ZE64ibDEWagicPk05gjQ/640?wx_fmt=png&from=appmsg)

7FF7F21671B0 最终的内存构造如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSBhbic1JibLcImBcCQSPUCGxy1nG7S5xibOKp1t8ZvqOHejCewyaeoyYqw/640?wx_fmt=png&from=appmsg)

fun\_NtCreateEvent函数会根据第三个参数进入两个分支，如果非零，则进入以下分支，循环调用NtQueryLicenseValue。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmS7vEribicIj1lnW7FprljYvnL2Sb26Cd4wnB6X6GlBY2yWfbiavE9kLSuQ/640?wx_fmt=png&from=appmsg)

否则进入以下分支，可以看到主要核心是调用NtCreateEvent，注意第二个大红框中同样在设置7FF7F21671B0处的地址，设置的内容和外层函数中一致，而7FF7F21671B0则被设置为NtCreateEvent参数ObjectAttributes.ObjectName。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSKqVBAvE5FicpRMWdsOvNXwNNQBwYwQaPWg9kVkicfibh4A9uJ3PWptGzg/640?wx_fmt=png&from=appmsg)

接下来详细看两个线程的作用，线程一调用函数fun\_NtRegisterThreadTerminatePort，该函数很简单，前面的alpc porthandle var\_alpcConnectionHandle创建成功，则对其调用函数NtRegisterThreadTerminatePort。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSJPZpIRvH8o1n9Exy9OlcsjiaPet57bF4yfOnoPOotgvr8XBo947sqEw/640?wx_fmt=png&from=appmsg)

NtRegisterThreadTerminatePort这个函数是一个未公开的函数，但是网上有不少相关的信息，简单来说这个函数的作用是将一个的alpc porthandler和当前的线程关联，当线程退出时，内核调用NtTerminateThread后会已发送一条LPC\_TERMINATION\_MESSAGE到对应的alpc服务端口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSbhKJibsWIgxMYdjkiaicWyAFJzyZSfHFiacDYvugljB2pICwsZicZgGJmgA/640?wx_fmt=png&from=appmsg)

实际来看该函数，调用ObReferenceObjectByHandle获取该porthandle对应的内核alpcport对象，之后分配一个长度为0x10的内存pool，将该对象保存在该内存pool 0x8偏移处，之后将该内存池和当前线程\_ETHREAD对象相互引用，有意思的是该函数NtRegisterThreadTerminatePort在k0shl的对CVE-2022-22715漏洞（https://whereisk0shl.top/post/break-me-out-of-sandbox-in-old-pipe-cve-2022-22715-windows-dirty-pipe）的利用中作为一个工具函数以实现长度为0x20的对象spray。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmS28KjrJmF0SPULiaGE3RMnf8QAibINibEFbibkiboDquFRn2fVJb5iaLqdLUQ/640?wx_fmt=png&from=appmsg)

之后则是第二个线程调用函数fun\_expWorker，其内部根据标记位调用fun\_loopNtSetInformationWorkerFactory。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSq3pOnXEOra1lByKCupSF3R7U4FR1eQnMQPjGTQZW4nvRVnYjSpnwxg/640?wx_fmt=png&from=appmsg)

fun\_loopNtSetInformationWorkerFactory中首先调用fun\_setEvilmessage，之后后调用NtAlpcSendWaitReceivePort，该函数通过前面NtAlpcConnectPort函数获取的pdc porthandler向pdc alpc port服务发送了一条消息，消息内容为v6。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmS0wqZddxW2HjuzJe28L1OAmRrHDf2RNGwHeu6O5PvY5NsHKR7HblpYA/640?wx_fmt=png&from=appmsg)

有趣的是当NtAlpcSendWaitReceivePort调用完毕后，似乎之前的WorkerFactory被修改了，这导致通过该WorkerFactory调用NtSetInformationWorkerFactory可以实现任意地址写入，代码中分为两种类型进行利用，如果是通过I/O ring的方式，则依此通过修改I/O ring利用中的关键var\_ioringRegBuffers/var\_ioringRegBuffersCount地址从而获取全局读写的能力，可以看到NtSetInformationWorkerFactory的第三个参数为写入的内容，而写入的目标地址则被spray在0x1000000000上，也就是说此时通过NtSetInformationWorkerFactory可以实现基于0x100000000-0x1000002000范围上保存随机地址的写入，而另一种提权方式则是通过该任意地址写入直接修改PreviousMode，PreviousMode地址同样被spray在0x100000000-0x1000002000上，NtSetInformationWorkerFactory调用设置PreviousMode后，通过NtReadVirtualMemory/NtReadVirtualMemory来获取全局读写的能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8w8noVE4qD1UXoq9ciaaWmSiapiaNueiaatJjibJMbPSfOzWNibGcUme1Vbrs3LTzfU32G3VcjWsxqM1pQ/640?wx_fmt=png&from=appmsg)

修改PreviousMode的利用方式最终在fun\_eopCmdProcess中通过NtReadVirtualMemory/NtReadVirtualMemory实现提权。

![](https://mmbiz.qpic.cn/sz...