---
title: 提权实录：通过命名管道劫持可写服务
url: https://mp.weixin.qq.com/s/BWBnWC_fvISyebvj1YLrWQ
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:13:08.010785
---

# 提权实录：通过命名管道劫持可写服务

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0ogkemMmlpkY0mTBWpicu9uvDHMibHQYJEtWc6XOos974mImac1ywag5WJ0HwgA4qY3LjghibURLfAPQzBmQSwqaHJgfsUTA9WLgkLLBIHiaKxY/0?wx_fmt=jpeg)

# 提权实录：通过命名管道劫持可写服务

原创

mstkey
mstkey

T00ls安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

---

在分析某 Windows 应用的服务组件时，发现其创建的命名管道访问控制配置宽松，允许低权限用户连接并发送指令，从而触发高权限的终止任意进程操作（taskkill）。进一步分析发现，被终止的服务会自动重启，而其可执行文件的权限配置错误，允许 Everyone 组读写。结合这两个缺陷，可构造一条完整的本地提权利用链。

## 漏洞挖掘过程

### 命名管道

#### 关于命名管道

命名管道（Named Pipe）是 Windows 操作系统提供的一种进程间通信（IPC）机制，允许不同进程（包括跨会话、跨权限级别）通过一个带名称的管道进行双向或单向数据交换。

命名管道具有全局可见的名称（通常位于 \pipe\ 命名空间下，如 \.\pipe\KeyServicePipe），支持多客户端连接，并可通过安全描述符（Security Descriptor） 设置访问控制列表（ACL），以限制哪些用户或组可以读取、写入或创建连接。

命名管道常被用作高权限服务与低权限客户端之间的通信通道。

然而，若开发者未正确配置管道的 ACL（例如允许 Everyone 或 Authenticated Users 具有写权限），攻击者就可以作为客户端向服务端发送消息，从而使得服务执行敏感操作（如启动/终止进程、读取文件等），以此构成权限提升或远程代码执行的风险。

#### 发现命名管道

发现命名管道及查看其对应的 ACL 策略可以借助 `Sysinternals Suite`内的 pipelist 和 accesschk。这里 0cat 向我推荐了一款可视化友好的工具：Pipetap。通过查看 Pipelist 发现存在一个 ACL 策略为 Everyone 可写的命名管道：KeyServicePipe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlpkKJ3Ylwa1mfDXB2QlIW8QBFoWT1HJleJmSIp2Hpw3yiaBmC0WyV6FTTx0CAVNmdMT27rEEHwxAl7ubS0xEH81jvWAnJTkia0vSc/640?wx_fmt=png&from=appmsg)

该命名管道对应的进程也是以 System 权限运行着，完全符合我们挖掘提权的条件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlpnKEgXXrzWHXknyhQ3kgWqXJsica8PNSy1ickXDUXic2QHIDb8o4GWfJ9DXZ0AUia8gzFUpMLwjKAL9EBW9v7avWwk35R07xOMPLm0/640?wx_fmt=png&from=appmsg)

#### 进程终止逻辑

根据命名管道服务进程定位到其可执行文件，接着通过 IDA 进行一键导出反编译代码。配合着 AI 进行分析，很容易就定位到相关信息。

首先是入口接收到信息并根据不同的偏移量解析客户端所发送过来的消息，根据这些偏移量得知消息包含 2 个部分：消息头和消息体，消息头为 12 个字节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlpmZLtHy3fgnZhypGdISYKceDjKc4su1WBWpPKtuPup5exLJ4micgB6p2HlWiaPGP10foj3f6CDDLRaUDQ1LQXNVCQcplWE06EhMs/640?wx_fmt=png&from=appmsg)

其次是消息头的逻辑，我们可以看见其有三个部分，每个部分刚好 4 字节（DWORD）。三个部分分别为：会话 ID、消息类型、消息体长度。这些信息也是基于后续的调试输出所得知。读到消息类型后，会判断消息类型的范围必须在 1-37 之间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlplgribNVGVBcmUhDUgcF5LYjbAic41pObiaTGlbFbnZQgtg4uiblgyhx4JozDaEe4KibSuC0GPBtqw7ib6lfYQfSr4OYAbWxzC7boJtg/640?wx_fmt=png&from=appmsg)

最后就进入消息分发，根据不同的消息类型进行分发。不同的消息类型对应不同的处理逻辑，在这里实际上踩了个坑，正常跟进向下的逻辑 Map 寻找，而实际上在服务创建的构造函数内就已经定义好了：sub\_424FF0(v5, 消息类型, 消息处理函数)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlpliaHtqoianbUWaFpOL30HQWicS7s4SI86ChnbpKlhQsic3NRWKsn9ibBhuzjwRVia9rZ2cOdiaXBuDibDCKLAJUp1ZmeM0Iae8IzNCv2Q/640?wx_fmt=png&from=appmsg)

关键问题逻辑就是其作为命名管道服务端有一个消息接收分发机制，根据消息类型来进行消息的分发。如图所示，当消息类型为 24 时则进入消息进入 `sub_4216B0` 函数处理。

在 `sub_4216B0` 函数内本质上就是获取消息体进行处理，最重要的就行消息体的 +4 字节偏移位，其为 PID（这里做了强转换，因此无法进行命令注入）。

PID 首先用于 TASKLIST 命令进行命令查找。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlpkD3f8sWqrDo3qzRvSYqgUQFtibInQjEb4YcR1KDBBOeSj2VN0SEpv1rPRK3ssrBOxoZN5tIicggAA0sHnD9er5cWnrZkd2AT024/640?wx_fmt=png&from=appmsg)

只有当指定的 PID 进程存在时才会接着向下走，走到 TASKKILL 命令，根据 PID 强制关闭进程。至此，我们就发现了一条低权限进程通过命名管道以 System 权限进行 TASKKILL 任意进程的路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlpnbVExCMQNtickgKFrWFgHZ6hZJ3N1ru0lGIdbZ8CNtghHsBhwub8AcUwJpUm1XJw5DfFET4TaGBgSEiclmPMQsY7kgFr8wiaGr10/640?wx_fmt=png&from=appmsg)

---

### 系统服务

#### 关于系统服务

Windows 服务（Windows Service）是 Windows 操作系统中一种在后台持续运行的程序，无需用户交互即可执行特定任务。如果服务在配置时没有做好权限的 ACL 配置则会导致三类风险：可修改服务二进制文件、可修改服务注册表项、可修改服务本身，易被攻击者利用实现本地权限提升或恶意篡改服务配置与运行逻辑。

#### 可修改服务二进制文件

这里直接借助 `SharpUp`来进行一键分析：SharpUp.exe check ModifiableServiceBinaries。发现有很多服务的可执行文件是可以修改的，但是要配合攻击链路，就需要满足被 TASKKILL 强制终止进程后，还会自动重启的。这里测试出来发现 KeyAgent 服务满足这一逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlpl0XhIZwhbic8U94Cgx0FnYl0WaGN3Ety4vqcXwRkBx6ic4DwC6reMNZfsbnz4zx6ibowa911S7CQQ6y7ibia7DrFicNp5BDtU5nGjvk/640?wx_fmt=png&from=appmsg)

---

### 利用链构建

利用链构建比较简单，先启动独立的线程不断的循环尝试将恶意文件 EvilAgent.exe 替换目标服务的合法可执行文件 KeyAgent.exe，同时作为客户端连接命名管道 \.\pipe\KeyServicePipe 并发送构造好的 KillProcess 消息触发命名管道服务进程执行 TASKKILL 命令终止 KeyAgent.exe 进程，最后借助 KeyAgent.exe 服务自动重启特性加载恶意文件，完成本地权限提升的利用链构建。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ogkemMmlpny2w18WVxLfuQccTfX8lofRG7cicxz1xmeOXWiamoXLsxyvfK19EScxZMs4qqegQMv6XOYKib7CEyNcUWoibGl7mUmH4Rxc0RfOw8/640?wx_fmt=png&from=appmsg)

EvilAgent.exe 是 `SystemGap` 项目里的 SystemGapAll。其同样也借助命名管道实现高低权限进程间的通信，低权限向高权限发送要执行的命令，高权限执行并把结果返回给低权限。

![](https://mmbiz.qpic.cn/mmbiz_png/0ogkemMmlpk7oSmDlw1daTzpPVAFCT0VkypXsMAOfIYLdcIPyeUtB3nibOhB2qrFBGpIvBQANS65rzhiaXVmtN9N2iaUyWYvP7taAVicLrz1paA/640?wx_fmt=png&from=appmsg)

## 总结

本提权利用链的成功构建，关键在于命名管道访问控制配置不当与服务可执行文件权限配置错误这两个缺陷的组合利用，在实战过程中发现这也类似的问题也很多，是个值得关注的攻击面。最后，在此特别感谢 @倾旋 在漏洞挖掘过程中提供的协助。

## 原文链接

> https://www.t00ls.com/articles-74973.html

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nOAjMAKC6icupJMRh71NoyhUB3efic74ESDrBtMlicTvhR5rAJAbiaXxPahyUibJnpbHibNUhtkK5PCUzFQ/0?wx_fmt=png)

T00ls安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nOAjMAKC6icupJMRh71NoyhUB3efic74ESDrBtMlicTvhR5rAJAbiaXxPahyUibJnpbHibNUhtkK5PCUzFQ/0?wx_fmt=png)

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