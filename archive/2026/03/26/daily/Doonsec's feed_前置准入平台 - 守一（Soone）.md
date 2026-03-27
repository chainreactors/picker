---
title: 前置准入平台 - 守一（Soone）
url: https://mp.weixin.qq.com/s/AVEk2zLZaeU-bhW73c8XIw
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:27:36.120859
---

# 前置准入平台 - 守一（Soone）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dTIoqBR3JibSYIRz21EdWgLFrJH5nntYNpK4e7zY672yOVNtRWMTVbpWmu7jtDAwbFGobib2kibibHLYFxrstORzQyrrLNzFULI1Niarc0drYPZ4/0?wx_fmt=jpeg)

# 前置准入平台 - 守一（Soone）

AlyssaVV
AlyssaVV

backdoor

![]()

在小说阅读器中沉浸阅读

```
"子能守一，万事毕。"——《黄庭外景经》
```

# 简介

C2 前置准入平台是部署在真实 C2 服务器之前的一层访问控制与环境验证节点，其核心目标是在恶意程序与核心控制服务器建立通信之前，对客户端环境进行筛选和鉴别。恶意程序在首次运行时并不会直接连接真实 C2，而是首先向前置准入节点发送请求。该准入平台会对请求端进行多维度验证，包括系统信息（CPU、内存大小、操作系统版本、用户名及进程信息）、行为特征（系统运行时间等）、网络属性（IP、ASN、是否来自云平台或安全厂商网络）以及令牌响应机制（token）。如果检测结果表明客户端处于自动化沙箱或安全研究环境，则平台通常返回伪造数据、错误响应或无效数据，从而阻断进一步通信；只有当客户端通过所有验证后，平台才会动态下发真实（shellcode） C2 地址、通信密钥或会话令牌，使恶意程序进入下一阶段并与核心控制服务器建立通信。

通过这种“首次 Beacon →环境验证→动态下发真实 C2”的分阶段机制，攻击者能够有效隐藏真实控制基础设施，使自动化沙箱只能观察到前置入口而无法获取真实 C2 地址，从而减少 IOC 泄露、防止 C2 被封禁或接管，并显著提高攻击基础设施的隐蔽性和抗分析能力。这种架构已经在多种高级威胁活动和复杂恶意软件框架中得到广泛应用，并逐渐演化为包含 Loader、准入平台、任务分发 C2的多层控制基础设施体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dTIoqBR3JibQtd8xr1LDRz0P8cQuOG7Hzl343Ku65LzIEPZtnr33gqI64BGHqywhwsOLiaTJiaVI85cfZszib8wH2WRFQFQZXWAJsHE5LSMmafc/640?wx_fmt=png&from=appmsg)

# 设计理念

当收集到足够多的环境信息时，其实已经可以较为准确地判断当前运行环境是否处于沙箱或调试状态。因此，没有必要在 loader 中反复堆叠各种反沙箱、反调试逻辑。我们尝试将这些对抗能力统一起来，并引入 AI 进行分析与决策，使沙箱对抗变得更加简单、高效且统一，不再依赖传统的代码检测方式；至此前置准入平台守一（soone）诞生。

# 设计&开发

数据传输采用https协议传输，恶意程序需要先将信息传入准入平台进行判断，判断为非沙箱环境后再下发shellcode。为了前置准入平台（守一）具备可复用性、C2兼容性、多版本操作系统兼容、文件大小控制。Client最终选取采用汇编语言进行编写；汇编语言的良好特性造就了文件大小4kb，提取出来的shellcode更是只有3kb，并且完美适配白文件patch、哥斯拉内存加载等场景，免杀效果也是非常优良。Server则采用python代码快速搭建起相关功能，接入AI；让AI对当前环境进行判断，是否为调试状态，是否为沙箱环境；减少人工成本，高效应对沙箱，保护真实C2。

# Client设计

由于是shellcode开发，所以需要能在各个环境当中获取到相应的WindowsAPI，也是采取了传统的PEB->TEB这种方式获取WindowsAPI，汇编代码是采用了metasploit的源码进行修改。当中寄存器分为易失性寄存器和非易失性寄存器。下图中的R9、R8、RDX、RCX、RSI就是非易失性寄存器；调用完成api\_call之后，寄存器当中的数据不会修改。编写汇编代码的难点就是你要知道寄存器存了什么数据，栈地址在哪里。

![](https://mmbiz.qpic.cn/mmbiz_png/dTIoqBR3JibSlYLd4d2iaMJcHiavyNGK6cBw2np35AdnDGsJCZXHzzHDPibqibr45wBIiasSw2KXu0Nlg52vpMnAZRVGLOadZ4WyUCOIIYXQ5jFGA/640?wx_fmt=png&from=appmsg)

---

代码整体分为两个模块；信息采集模块，数据交互模块。

## 信息采集模块：

数据存储采用栈空间进行存储，在开始数据收集之前开辟一块栈空间即可，栈空间的大小根据你采集数据的多少进行开辟；栈顶地址作为存储数据的起始地址，预留一片空间用于存储拷贝过来的信息并且需要将此时的栈顶地址进行保存；压栈进行保存后面使用相对偏移取或者保存到一个非易失性寄存器都可以；多余的栈空间用于调用WindowsAPI时作为缓冲区使用，建议对栈空间进行一些规划。

![](https://mmbiz.qpic.cn/mmbiz_png/dTIoqBR3JibRn6QiaJsKMLyje0RIZUgxmicBXHRiaT6f4X6uIF47C3EfoLo0pRY8b5f2g3qsYncNdsdtTXXRCVUNdtMbI31BMpoAvictReYfH1nE/640?wx_fmt=png&from=appmsg)

调用WindowsAPI返回数据后需要将数据拷贝到指定的地址，这个时候就需要封装两个拷贝函数，字符串拷贝函数和数字拷贝函数。数字拷贝函数是需要将一些WindowsAPI返回的数字数据信息转换为ASCII码进行传输来保证数据的准确性（不会出现乱码）。字符串拷贝函数就是将WindowsAPI返回的数据拷贝到指定的缓冲区即可。因为每次拷贝的数据长度不固定，也不一定8字节对齐；所以需要使用一个寄存器记录每次拷贝完成之后的地址。对于一些数据获取需要多个WindowsAPI的情况，可封装为一个函数，例如对注册表当中的信息获取，父进程的获取等信息。

下图当中就是对内存大小进行获取，并且将内存大小转换为mb拷贝到指定缓冲区的汇编代码。所有的信息获取都像下图所示，调用WindowsAPI获取相关信息，然后对数据进行拷贝，拷贝字符串就调用对应的字符串拷贝函数；数字拷贝就调用对应的拷贝函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dTIoqBR3JibTcjfy1BicTZZ4N6O0q0aN4QIILurML6ibdpUqaz7FHN2IcjVKtLE2ILGTTpPhebePKPEyFzvBpcWebZUic5bCziaiaMhQBicUX6axrk/640?wx_fmt=png&from=appmsg)

## 数据交互模块：

数据交互模块的代码采用了metasploit的https的汇编代码，在此代码的基础上进行修改。该模块功能点做到了睡眠等待，shellcode执行，退出。

内置睡眠等待：程序运行之后，无法请求到server端，程序会自动进入睡眠等待；睡眠完成之后继续携带采集的信息进行请求，一直这样进行循环直到请求成功；睡眠时长目前是固定睡眠30分钟。后续可能会考虑做成第一次未请求成功睡眠5分钟，第二次未成功睡眠10分钟这种累加模式。

shellcode执行：当环境判断通过之后接收到server端下发的shellcode执行；shellcode需要是反射加载的shellcode。这里个人比较喜欢后置反射（post\_srdi），后续可能会去修改一个PE2shellcode的工具，该工具使用反射加载并且转换出来的shellcode支持内存擦写。能把反射加载器自动给擦除掉，当然魔术头这些能擦除的都给擦掉，内存当中只存在PE文件。

退出：接收server端下发的退出指令，结束进程退出。

# Server设计

客户端管理、监听器管理、shellcode管理、UUID管理、生成客户端、系统管理这六大模块。

* 客户端管理：所有的请求信息都会在这里显示，未开启AI判断可在此处进行人工下发任务。下发睡眠等待：server端获取到信息后进入AI判断环境，那么就可能存在AI无法准确给出回答的情况，这时候AI就会下发睡眠等待，后续人工进行环境判断；人工判断也可能存在就是不想下发shellcode也不想退出，那就下发睡眠等待。手动下发睡眠等待的时长可自定义。下发shellcode：根据实际情况下发shellcode即可。下发退出：当前环境判断为沙箱环境之后，下发退出指令。拉黑：将UUID拉黑掉

* 监听器管理：添加删除修改监听器，将对应的监听器打开才能接收到client传输过来的信息。目前监听器只支持https，因为懒。

* Shllcode管理：添加删除shellcode。

* UUID管理：对UUID进行管理。只有在UUID管理当中存在的UUID数据传输过来时才会进入到后续判断。

* 生成客户端：生成客户端时会将UUID写入，UUID会同步到“UUID管理”模块当中统一管理。目前是生成汇编文件进行编译，略显粗糙，后续应该会做成对PE文件patch操作。

* 系统管理：配置AI模型，默认等待时长，判断通过后下发的shellcode文件。登录界面背景图配置。

后续可能设计出根据不同的UUID上线到不同的C2，或者根据UUID备注上线到不同的C2。将client收集的信息生成hash值存储到数据库当中，将此hash拉黑掉；此后被拉黑掉的沙箱都无法再次接入到server进行判断。拉黑UUID是把整个程序拉黑掉，即使是在正常环境当中运行都无法接入到server。拉黑hash是单独拉黑掉一台计算机，不影响程序的正常使用。

一些杂乱的解释：

1. 参考metasploit源码的原因？

   Metasploit是一个非常优秀的框架；并且其中的汇编代码放到现在也是非常优秀的。从零手搓有点儿搓不动，就参考借鉴了其代码和文末链接当中的文章与代码。
2. 数据存储为什么采用栈空间？

   采用栈空间进行存储是因为方便后续的拓展，比如想多收集一些信息的话只需要抬栈即可，并且对采集的数据进行拷贝时，对栈地址（RSP）把控相对简单一点。申请内存空间的话我个人觉得太麻烦了，其实也行。
3. PE2shellcode工具的选择？

   GitHub上面开源了很多SRDI转换的工具，都可以去试一下。只要是反射加载的shellcode都能接入到准入平台；当然传统的shellcode也可以。
4. Shellcode执行当时的选择？

   执行模块是使用的暴力跳转（RET），同时也在尝试使用fork的方式加载shellcode，这种情况下一个进程可同时上线多台C2，但是仅仅停留在尝试阶段。

# 总结

理论上，该系统能够接入所有C2平台，并支持部分工具的内存加载执行。这不仅是一次对沙箱环境的反向试探，也是与沙箱直接的正面对话；不依赖规避或逃避机制，而是在沙箱内部进行信息采集，静默等待等操作，从而实现对安全检测环境的应对。下一步的计划是完善server端、尝试接入Linux系统、完成srdi工具的内存擦写。感谢cxaqhq对server端的重构以及fdx提出的宝贵意见与建议。

# 演示

https://www.bilibili.com/video/BV1tHAAz2Ee9/

这里在虚拟机当中还能运行可能是因为我虚拟机配置比较高或者是我AI提示词写得比较垃圾，也有可能信息采集得不是很够。

![](https://mmbiz.qpic.cn/mmbiz_png/dTIoqBR3JibQk2tmlF8CCNpXCUXARAATNPUkiay4CJoIUXcucJSm9P2fyILMmtXlnNfI3x7vrXpTIpYFkgdhnUtibTlySib1PKwIHzAzwN96394/640?wx_fmt=png&from=appmsg)

参考&致谢：

* https://github.com/badboycxcc
* https://github.com/fdx-xdf
* https://www.t00ls.com/thread-74108-1-1.html
* https://github.com/rapid7/metasploit-framework/blob/master/external/source/shellcode/windows/x64/src/block/block\_api.asm
* https://github.com/rapid7/metasploit-framework/blob/master/external/source/shellcode/windows/x64/src/block/block\_reverse\_https.asm
* https://xz.aliyun.com/news/17961
* https://learn.microsoft.com/zh-cn/windows/win32/api/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/t7IZ9keh9k431GVrMianBeIWO4NqF97bf6wBUIBicFV5wy0aUkWBmZjPIhWnRIoSFrkoVBtbyXy9TgztGf2V2bvg/0?wx_fmt=png)

backdoor

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/t7IZ9keh9k431GVrMianBeIWO4NqF97bf6wBUIBicFV5wy0aUkWBmZjPIhWnRIoSFrkoVBtbyXy9TgztGf2V2bvg/0?wx_fmt=png)

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