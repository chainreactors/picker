---
title: 【Windows内存取证】
url: https://mp.weixin.qq.com/s?__biz=MzAwNDcwMDgzMA==&mid=2651047984&idx=1&sn=e7449bd4ac8bf3f8c34f642be8d97bd9&chksm=80d087c1b7a70ed726be72fadeda0072b2fd2a024044e6129f20efcb95bd0e0d73679ad3b3f8&scene=58&subscene=0#rd
source: 电子物证
date: 2024-10-23
fetch_date: 2025-10-06T18:52:33.168453
---

# 【Windows内存取证】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dDhDhftpRFvAQX10BSBXofolGbGTBZJVldTYHyyGOefgS71SGYwnfP17AHoBERMicR2ibM7icSh3AVaQuAV9ibIw3w/0?wx_fmt=jpeg)

# 【Windows内存取证】

电子物证

以下文章来源于我不懂安全
，作者Vlan911

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6Cj8BL0RFU05hV3SpgOHicCaQjCdVl5fNG2N5Ze9BGQeg/0)

**我不懂安全**
.

分享挖掘漏洞小技巧，分享安全案例以及一些安全动态，分享实用技术

来源：**我不懂安全**

此篇文章，主要学习到windows内存取证知识，此次学习将有3个场景，涉及内网横向域控等

**涉及的工具：**
SysInfoTools-ost-viewer-pro
volatility\_2.6\_lin64\_standalone
VT在线工具

**使用到的镜像文件：**
target1-1dd8701f.vmss
target2-6186fe9f.vmss
POS-01-c4e8f786.vmss

**题干：**
一名员工报告说，他的机器在收到一封可疑的安全更新电子邮件后开始出现奇怪的行为。事件响应团队从可疑计算机中捕获了几个内存转储，以供进一步检查。分析转储并帮助 SOC 分析师团队弄清楚发生了什么！

**Target1**

**0x01 - 欺骗前台员工安装安全更新的电子邮箱是什么？**

查看镜像信息

```
/volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss imageinfo
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO20ETBYmf0RWib66SNvTX4Xxx8dS7JUwEFsSialr07kUzXVA5Wu8gRcoSQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

查看进程列表

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 pslist
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2Ujm6ib5CEKOlxLgTiawHqqZuynicyicfG7eWgqFP98qxLoxFSSKed0RY9g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

因为题目已经说了，收到了电子邮件，所以直接看outlook.exe就可以；导出进程到dll目录下

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 dumpfiles -p 3196 -n -u -D ./dll
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2FmbdzRNbRVZlSXLnFArl7mRFzAezf5kMHwMCy9iaib9WmmxKgp5GFkbQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在翻垃圾的时候，翻到了几个ost.dat的文件，该文件其实就是微软的邮件的一种离线格式，当然了我说的是ost，与pts类似

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2XITJb9cxZy6Cib26tGSHVmemDzRAcaYiaqzRhSQVBZ8icGlRg69I3Uqcg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

这里可以不转换格式，直接用工具打开

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2LiaFIu4dF56eu2JXtBESVTzTzPqCgJuRCfcyS483h0m11POjkRq00qw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

也可以用我上一期的玩法，解包

```
readpst -S file.3196.0x84eed400.Frontdesk@allsafecybersec.com\ -\ outlook2.ost.dat
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2f0mD94ADkEoTQcicIZngS4XaNjbKZw73JujaWMgziaq8xTSISd81PCOQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2cVQBwg1ib96FgBVWricj0xcfrlM49M4EQNZJzBY7icKrp1ic2xCKOEKkNw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**0X02 - 电子邮件中用于钓鱼的文件叫什么名字？**

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2fkia2uticZfU9dBk7d4icOOJ61lhy2whaLu5loGGJQribQcAmxeRVQlOtQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**0x03 - 恶意文件家族是什么？**

上面获取到了下载地址，本来想直接拿着地址去比较的，发现还是天真了

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 filescan | grep AnyConnectInstaller.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2aMA4zZ1S2na2BJPW4De2PpiaficpFBkErdnTYWiaOLMMlEicDbMFibwjDjg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

随便导出一个

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 dumpfiles -Q 0x000000003df12dd0 -D ./
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2ZzdMuoWBEFHMQyrjgKoh1fyBN4R9RicG5cGh6HgCybKGOssuxDvkEdw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

下载之后的东西是带特殊后缀的，但是不影响通过md5值比对样本

```
md5sum file.None.0x85cd09a0.img
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2YbzsDxTCCoZe0MubNLFYetFvMAmSRBto3icd1GV5pUt7d7gp1w2PPZA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2U3zqcSx83u3v5CnPbZZFdBBN7uKTe6DZ1hicPyxEs8zBJXsf9NcE72A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2VJiawFwRvXciaSDicnXcKMbaxcs1icRdJYDG1ugc9cZ0VzVFw1QEtiaA1UQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**0x04 - 恶意软件似乎正在利用进程注入。被注入的进程的 PID 是多少？**

这道题挺牵强的，仅仅是内存取证的话是很难分辨出究竟是哪一个程序可能存在进程注入的情况，这里面不是dll注入，所以使用检测dll注入的方式是不恰当的

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 pstree
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2PiatBuBj085qYVjHSticCEicicKNWNsCK0S23ic9JjUOXSX9SCngbJMV4mw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2qNBUYyEQ25WoecvKKpe87FJGRJsYmVeSabVV9BQKo8zKmkLdTia0ZYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

其实这里很多进程都存在子进程，所以单独借助vol是没办法确定究竟哪一个才是有问题的，看了下别人的解题思路，在vt有一处进程

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2fqtpjDbr51tY0Ztya3Mvia4aCFAynEfJcJ2FQ3BoZaNaoribphYh9Cag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

恕我直言，这里面依然有很多其他的进程被创建，那为什么不能是svchost呢？
后来想起从发现的邮件里找到的ip地址

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 netscan | grep "180.76.254.120"
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2uSWlAgxLbZEEL6gp2tLM81YbQfNGIBoCmoiboLTlTWuUbxRCjeeg1nA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**0x05- 恶意软件在计算机重新启动后依然能保持自启动是为什么？**

此题其实就是在考验个人对恶意软件权限维持的一种理解，常规的恶意软件为了保证计算机重新启动后自己依然能平稳运行，特别是在windows系统里便采用了多种方式，比如说计算机启动项：

```
C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup注册表服务计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce
```

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 mftparser > output.txt
```

此命令可以将内存镜像里的文件目录信息导出来

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO21udvpurvsBYoDYmrq1IHVGiaDTuGEMacUkC04fwwuuvQDCplUkS16Eg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2VWAMQsMRBuUAkQywATyfR8Ja0EvcZ1gjzXghy0KBwfLJylQcZxFZNw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

全局检索之后，没有在类似启动目录里发现，所以只能去找注册表

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 dumpregistry --dump ./regedist
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO251HoAX9kIdBNUjcnMmo82qFoc0g7QVTnXBXc3kc1NZyFLaCcOTBvBA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

使用工具读取注册表

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2B7t3DoDWEhR0GyibicOo5uJaztex3f4MJe2jqicXMciaCQboib71LVa0LtQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

打扰了，后来发现可以直接在vt看到

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2lQBjw6mhqJz0vRpsKRJmSXQJdGaIncv99cR2xXPVXLuebn5QibcW7hg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**0x06 - 恶意软件通常使用唯一的值或名称来确保系统上只有一个副本运行。恶意软件使用的唯一名称是什么？**

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 handles -p 2996 | grep "Mutant"
```

这里直接打印2996进程的资源句柄；Mutant解释如下：

> 在计算机科学中，"Mutant"是指一种同步原语或对象，用于实现并发编程中的互斥锁（Mutex）。Mutant 是 Windows 操作系统中对应于互斥锁的术语。
>
> 互斥锁（Mutex）是一种同步机制，用于控制多个线程对共享资源的访问。它提供了一种方法，确保在任何给定时间只有一个线程可以访问共享资源，从而避免数据竞争和不一致性。
>
> 在操作系统内核中，Mutant 是通过内核对象来实现的，用于协调进程间的互斥访问。它可以用来保护共享资源，以确保同一时间只有一个进程能够获取到该资源的访问权限。

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO24M3YUicq0ibMXu7SZoBYYuOVibU9A0oANzQt42c3tYkbAJeRqObnmoL4A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**0x07 - 似乎一个臭名昭著的黑客在当前的攻击者之前就破坏了这个系统，你能说出这个黑客出自哪部电影吗？**

这里是真没答上来，抄袭的大佬的

```
./volatility_2.6_lin64_standalone -f Target1-1dd8701f.vmss --profile=Win7SP1x86_23418  filescan | grep -oP '(?<=\\Users\\)[^\\]+' | sort -u
```

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2H3ZWjBtcGV0UicP997bK7AlspicG1N5OeFMLwZjLlv8J5lOWJtWN65ZA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

这里我也不知道为什么人家直接定位/user ，但是根据人家的定位，看起来东西是在注册表里，所以就可以找注册表里的用户数据了
可以通过查看注册表software注册表

![](https://mmbiz.qpic.cn/mmbiz_png/qXbmFE2wB53sRCCfwibVl4N0wqUlLsEO2qh5Mjtb9QdsDSMnmO8YicqL6mgdkJWnowhCdacj1eBcaoibA5XOXV...