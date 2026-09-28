---
title: EDR 规避新思路：不调用 WriteProcessMemory 的进程注入
url: https://mp.weixin.qq.com/s/I6NCA8-I2xshxRBITldZZg
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:55:18.030567
---

# EDR 规避新思路：不调用 WriteProcessMemory 的进程注入

# EDR 规避新思路：不调用 WriteProcessMemory 的进程注入

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EFjib9JRx7QcSibE1xFicKQCXMibZaicwGmNxacrjibibfDib14gtqQ1icRV8tNgiawGvPkcIPo80Xnr2LHOAddibykYtq71w0pf6z2DGfAg/640?wx_fmt=jpeg&from=appmsg)

## 一、引言

在红队演练或针对目标的渗透测试过程中，你极有可能需要用到**远程进程注入**来执行自己的 payload。正因为这种手法太常用，EDR（终端检测与响应）对其中涉及的 API 盯得格外紧。

本文要介绍一种远程向进程注入代码的新思路——它**完全不依赖**大家耳熟能详的 `WriteProcessMemory` 和 `VirtualAllocEx` 这两个 API。

作者在文末坦白：自己是在折腾一堆 EDR 授权许可的时候，偶然发现 SensePost 的两位研究员 **Max Hirschberger** 和 **Ogulcan Ugur** 已经独立想到了相似的思路，并在他们的博客上发表了相关文章（即 Process Parameter Poisoning）；顺着这条线，又找到了 **modexp** 早前探索过的高度相关的技术路线。作者也大方承认，那几位前辈做得比自己更出色。

不过，作者对自己方案里「初始化阶段必须暂停进程」以及「`lpCommandLine` / `lpEnvironment` 需要特殊格式」这两点不太满意，于是把那些思路放到一边，转向了一种全新的注入手法——也就是下面要讲的这种。

## 二、正文

### 1. 远程进程注入技术概览

进程注入是一种关键的规避与持久化手段：攻击者强迫一个合法的、受信任的 Windows 进程，替自己去执行任意代码。

在经典的「远程线程注入」或「PE 注入」流程里，注入进程必须先通过 `OpenProcess` 拿到目标程序（比如 `explorer.exe`、`svchost.exe`）的句柄，再用 `VirtualAllocEx` 在目标虚拟地址空间里开一块专用缓冲区。

内存准备好之后，攻击者调用 `WriteProcessMemory` 这个 API，把恶意 payload 拷贝进远程进程的内存空间。

最后，攻击者用 `CreateRemoteThread` 或别的办法创建一条线程，让它的 RIP 指向那块刚写入 shellcode 的内存区域。

由于这种跨进程的转换天然绕过了常规的边界防御、还继承了宿主进程的访问权限，EDR 会通过**用户态钩子（hook）和内核回调**对 `WriteProcessMemory` 进行严密监控。

EDR 把跨进程内存修改视为高严重度的遥测事件，这也逼着现代威胁行为者不断寻找能够绕过传统内存操作特征的规避替代品。

绝大多数远程注入技术背后的通用公式可以概括为：

> **[OpenProcess / CreateProcess] + [VirtualAllocEx] + [WriteProcessMemory] + [某种创建线程并劫持 RIP 指向新写入 shellcode 的方式]**

### 2. 用 Windows 命名管道把任意 payload 写入远程进程

当你启动一个交互式控制台程序（它会拉起一个名为 `conhost.exe` 的子进程），并通过输入命令与之交互时——你敲下的那些命令内容，最终存在哪里？

答案是：**存在这个程序的内存里某处**。

为了说明这一点，作者写了一个小程序：它用 `CreateProcess` 创建一个子进程，然后往子进程的 `hStdInput`（标准输入）里写数据。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GbgWBpjysCDOdT0Q2OUSSibw1iaWN4OYsHEAkZJ1qBjNSe6ibgHATntvQsFv6gov8DjsYfMMe8ganljFHic3DQWhia5opKaJibiaR5iaw/640?wx_fmt=png&from=appmsg)

作者以控制台程序 `nslookup.exe` 为例来演示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0F7j1G0IqaPqMpGyJ5FqmwpDic6QIEFl0zNYW9YE6jhQ3f1uENTicgBWSTqc7ZeeVicJfnxRAVu3zmKbzO3Qy3djUv5g7UdX0H4o8/640?wx_fmt=png&from=appmsg)

当对子进程的 `hStdInput` 调用 `WriteFile` 时，被写入的数据就实实在在地落在了子进程的内存中。

于是就有了一个想法：与其对子进程调用 `WriteProcessMemory`，不如**利用 `hStdInput` 这个命名管道，把 payload 写进另一个进程**。

但这里冒出一个问题：Windows 控制台界面只能显示有限的一组可读字符，而往命名管道里写数据，本质上就是一次 `WriteFile` 调用。理论上讲，这意味着我们完全可以把控制台「显示不了」的字节写进 `hStdInput`。我们来实地验证一下。作者准备了下面这个二进制数组：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0GYRKTuNraIU061hAyPU7k4VDp9jm9uv23ZIEKCKU7ibKZ5ibpTHVffib5aiatVQjcJOCgrBDdkH164ibBHUyo4eSgo4mScdX7ibAAtQ/640?wx_fmt=png&from=appmsg)

写入命名管道之后：

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GfYpY5BCHYictODibuuMErpG6RqaCvYeMY9cNmSaGpeCibEvG7Ju0uUPWHxl7KnwGNv4QD1X5CicHvdFibbtFgkKvgNfr8gtdjwib2M/640?wx_fmt=png&from=appmsg)

**这就证实了：我们几乎可以把任意字节流写进一个控制台进程的内存里。**

### 3. 通过控制台命名管道实现远程进程注入

基于上面的认知，要**不使用 `VirtualAllocEx` 和 `WriteProcessMemory`** 就把 payload 注入远程进程，主要需要以下六个步骤：

1. **挑选一个交互式控制台程序。**

   作者找到了两个可用的：`netsh.exe` 和 `nslookup.exe`。
2. 调用 `CreateProcess`，拿到子进程 `hStdInput` 的句柄。
3. 对 `hStdInput` 调用 `WriteFile`，把 payload 写进子进程。
4. 在子进程内存里**定位**刚刚写入的 payload。
5. 用 `VirtualProtectEx` 给这块新识别出来的内存区域加上\*\*执行（Execute）\*\*权限。
6. **劫持一条线程**

   ，把它的 RIP 重定向到这个地址。

在使用 `WriteFile` 往 `hStdInput` 写数据时，payload 必须避开 Windows 控制台里具有特殊含义的「坏字符」：

* **0x0D**

  ：回车（CR），ASCII 与 Unicode 中的控制字符。
* **0x0A**

  ：换行（LF），控制字符。
* **0x1A**

  ：SUB（替换符），由 Ctrl+Z 产生，历来被当作文件结束（EOF）标记。

生成 payload 时必须规避这几个字符，否则子进程会把 payload 当成一条命令来执行，结果往往是「找不到命令」之类，而原始的 payload 也就不再留在进程内存里了。

**为了在子进程内存里定位刚写入的 payload**，作者在 payload 开头放了一段特征鲜明的字符，称之为 **marker（标记）**。只要搜索这个 marker，就能确定 payload 的位置。在把 RIP 重定向过去时，需要给目标地址加上 marker 的长度：

> **RIP = marker\_addr + sizeof(marker)**

作者据此写了一个概念验证（PoC），完整跑通了上面这六步，实现远程注入并执行 shellcode，效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EIjbfNZg5zFrXI5cXibibeZXFaSvj1fp43vANKAP8OeyqAa0YedcS7AA5xPwTTAVdIkCHLHS28JNgeh86mklcC0vXeoKu32anWk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HialSZROGdpUjp54icfhiaE1uuZvaEVaG8IHYeM7GArX2z8pQJnBxfSMAV6ZibnY1atBA5n3dPzicTGybkqBNA2wvhNQpCYIRr2yfI/640?wx_fmt=png&from=appmsg)

此前已有研究者针对多款 EDR 实测过这类技术，所以作者这里就不再罗列自己的测试结果了。

演示视频：https://youtu.be/DCUnbj\_usPM

### 4. 防御侧建议

由于这种「控制台命名管道注入」完全绕开了 `VirtualAllocEx` 和 `WriteProcessMemory` 这两个 API，检测重心应当转移到：

* 对**远程进程**调用 `VirtualProtectEx`（尤其是为内存区域添加执行权限）的行为；
* 以及对**命名管道**的读写操作上。

## 三、结语

红队演练或渗透测试中使用的绝大多数远程注入技术，都依赖 `VirtualAllocEx` 与 `WriteProcessMemory` 这对 API 组合，所以 EDR 对它们的监控非常密集。

与传统思路不同，**控制台命名管道注入**既不调用 `VirtualAllocEx`，也不调用 `WriteProcessMemory`。它借力于命名管道的读写操作，再加上「控制台程序会把交互命令存进内存」这一特性来达成目的。此外，它还有几处额外的优势：

* 不需要用 `CreateProcess` 以**挂起（suspended）状态**启动进程；
* 不会让子进程的 `lpCommandLine` 或 `lpEnvironment` 出现奇怪的格式。

payload 或 shellcode 里可用字符的限制也相对更少，需要规避的坏字符也就更少。

结果是：传统的监测手段无法可靠地检测并阻断这项技术。防御者应当转而聚焦——控制台程序存放命令的那块内存区域、对 `VirtualProtectEx` 的监控，以及命名管道读写行为的追踪。

参考

https://www.zerosalarium.com/2026/09/edr-evasion-process-injection-without-WriteProcessMemory.html

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EIt8n0PicrIdlEmgD6UXuibialdllTJdribu3xgwMbxEIygN4CphymcTAvic5XSwPdq75W2sX5HzKHY8WT1PjhO4kPm086YkU0xJzY/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外等平台- 搜索的内容通过结合编写 -

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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