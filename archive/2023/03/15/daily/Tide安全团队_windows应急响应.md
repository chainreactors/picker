---
title: windows应急响应
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247508502&idx=1&sn=a9ddef7754a1212fb389fcbe7bdb3f41&chksm=ce5d8077f92a096178cbd89e74b3cbd94f14eb8428b2cff3f6535809564cc5448dfdea047289&scene=58&subscene=0#rd
source: Tide安全团队
date: 2023-03-15
fetch_date: 2025-10-04T09:36:29.767055
---

# windows应急响应

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqibeUgZ0UokRwqXzf5Mic9T9RYJ7lWaqvqnxTaFHxcXZ8OozwRREiaXAVA/0?wx_fmt=jpeg)

# windows应急响应

原创

molengsu

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVhN8RQR8c6zEaACxatlch2rgdzYzYAiahr1GUq1cLMMGVnvKpF8biaWA/640?wx_fmt=png)

# windos分析排查-文件分析

## 分析排查介绍

分析排查是指对windows系统中的文件、进程、系统信息、日志记录等进行检查。查看windows系统中是否有运行异常的情况。主要目的在于保护windows系统的安全。

## 0x01 开机启动文件

一般情况下，被植入的木马病毒、恶意文件恶意程序等都会在计算机启动时自启动运行。

在windows中可通过以下三种方式查看开机启动项：

1.利用操作系统中的启动菜单

```
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9Eppsq4iaOaCA9Y1N46JDHKwkbV3yQzZ4TLtE3DNsZic2JA8cbqFYRfBn3lOQQ/640?wx_fmt=png "null")

2.利用系统配置msconfig

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqiauzCCyvZXfWOvjH3dpticeJqgcnC3rrOLKQFia4ibb8geLf4J34YNUnJQ/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqdzYt1ZmdibthObX3qh6SNyCUP8t71T9IXlUXae5DnSvsR0hzExkaleQ/640?wx_fmt=png "null")

3.利用注册表regedit

```
计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9Eppsqb8d4aFKyluB5L9X1UBgJBHJuCUho7k2veUAr7iasjXEmykIgsvvcwwg/640?wx_fmt=png "null")

```
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqTIos1DwIt27huo5dEum0I5kzQyCMEwtVo50ZmjmFgbmDPwbAj85k7w/640?wx_fmt=png "null")

## 0x02 temp临时异常文件

temp临时文件夹，位于C:\Document and Settings\Administrator\Local Settings\内。很多文件放在这里，用来收藏夹，浏览网页的临时文件，编辑文件等。

在运行输入%temp%可直接打开temp文件夹。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqbAqWUl4nM5QjoW38kEXorNIN0dohITK37jcdQRVWUnibkDhWXYyn6VQ/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqiaD4CiaG0M2e8Vm8OclosdBJYUmvHjsWaA2kYyWnG1DoYrycvQpiaXv6Q/640?wx_fmt=png "null")

排查对象：查看temp文件夹PE文件（exe、dll、sys），或者是否具有特别大的tmp文件。

相关可疑文件可上传到云沙箱进行在线分析。

https://www.virustotal.com/gui/home/upload

https://x.threatbook.com/

https://ti.360.cn/#/homepage

为什么要排查Temp文件夹？

使用Temp文件夹有几个优点。在某些系统中，Temp文件夹位于RAM DISK上。与通常的磁盘文件系统相比，写入操作和文件操作要快的很多。

另一个优点是Temp文件夹对当前登录的用户具有读写访问权限，从而解决了恶意软件安装程序在没有适当权限的情况下尝试将恶意软件安装在目标位置时出现的任何文件系统权限错误。一旦恶意软件安装程序或恶意软件本身具有升级的特权，Temp文件夹通常用作暂存点。

操作系统还具有清理Temp文件夹中临时文件的不完整写入的优点，因此在恶意软件安装失败的情况下，操作系统负责删除文件的任何痕迹，从而防止恶意软件的任何部分或版本损坏它的主要可执行文件。所以恶意软件安装程序通常在恶意软件感染期间利用TMP文件和Windows Temp文件夹。

## 0x03 浏览器分析

服务器被攻击者拿下后，攻击者可能会使用服务器的浏览器进行访问网站，进行一系列下载操作。因此我们可以查看浏览器记录，排查浏览器是否被使用下载恶意代码。

1.浏览器浏览痕迹查看

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9Eppsq27y8WDnEpGe9GicDj0G9B6oTKGDpibzwRk2fnEU0rRiaCiaGCWh0YztOEg/640?wx_fmt=png "null")

2.浏览器文件下载记录查看

3.浏览器cookie信息查看

浏览器记录查看工具：https://launcher.nirsoft.net/downloads/index.html

## 0x04 文件时间属性分析

在windows系统下，文件属性的时间属性具有：创建时间、修改时间、访问时间。默认系统以修改时间作为展示。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9Eppsqtct9EgmzvJJBV3b2nPUFwmeZic6ib5dTdl6DFiaPJHKGwJ4vKfUfmF3SA/640?wx_fmt=png "null")

如果文件的修改时间早于创建时间这个文件存在可疑，异常的时间很有可能是攻击者进行恶意修改的不正常文件。

## 0x05 最近打开文件

Windows系统中默认记录系统中最近打开使用的文件信息。

可以在目录`C:\Documents and Settings\Administrator\Recent`下查看

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9Eppsq6iczy7HRVD4uTS8GQjWaUkVNE9rTXldEJQFjtrKe1PrEuiaklKXAXx1A/640?wx_fmt=png "null")

也可以使用Win+R打开运行后输入`%UserProfile%\Recent`查看。然后利用Windows中的筛选条件查看具体时间范围的文件。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqHCAEx3xtic33dia73iaiaKRyibXADZnib4HJtLicYvDFiajpTKOhU8OiaUzxnicw/640?wx_fmt=png "null")

## 0x06 可疑进程发现与关闭

计算机与外部忘了通信是建立在TCP/UDP协议上的，并且每一次通信都是具有不同的端口（0-65535）。在计算机中木马病毒后，木马运行会与外部忘了进行通信，那么就可以通过查看忘了连接状态，找到对应的进程ID，然后关闭进程ID进行断开木马的通信连接。

使用如下相关命令进行排查：

```
netstat -ano | find "ESTABLISHED"  查看网络建立连接的状态
tasklist /svc | find "PID" 查看具体PID进程对应的程序
taskkill /PID xxx /T 关闭进程
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqYDJ8icQGfJnF4860QgOiayhaYV607cSNQuAwKfVxn0CHalJKNlRBhODQ/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqANUG0JIX70Pr9NFJuXtcciabo9WTuHrYRK1yO6Evd7BKictWjMriaIzxw/640?wx_fmt=png "null")

# Windows分析排查-系统信息排查

## 0x01 异常计划任务排查

在计算机中可以通过设定计划任务，在固定时间执行固定操作。一般情况下，攻击者设定计划任务在固定时间设置执行恶意代码，以达到隐蔽实现攻击的效果。

在使用schtasks命令可以对计划任务进行管理，直接输入schtasks可以查看当前计算机中保存的计划任务。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqamoBIPdy1MDkqKTu0255Ls2Gn2LX1kUiaicMk2BZq3lxHMsmiaq7VXAQg/640?wx_fmt=png "null")

使用任务管理器查看当前计算机中的计划任务，在开始菜单找到“计划任务程序”进行打开。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqVvlke1CYaQonfWIckxicMugWMOykwxicIUkXnIVK2yPBFpwhLVQkJIMQ/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqXlIQZgnduAOogibDOq2fExhdaCswNw3qjOhlvYicfalcRfBqIpGXbhCQ/640?wx_fmt=png "null")

通过对相关的可疑计划任务进行排查，如发现相关运行程序可疑时，可根据文件路径找到程序使用云沙箱进行在线分析。

https://www.virustotal.com/gui/home/upload

https://x.threatbook.com/

https://ti.360.cn/#/homepage

## 0x02 隐藏账户发现与删除

隐藏账户是指攻击者入侵服务器后威朗能够持久保持对计算机的访问，在计算机系统中建立的不易被发现的计算机账户。

隐藏账户建立命令：

`net user test$ test /add && net localgroup administrator test$ /add`其中$符号可以导致系统管理员在使用net user时无法查看到test$用户。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqVgBGEMJjouLmSnzx91fXJ3MDfxz1omdOBSfFI4XXosoncBwKY7RrDA/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqwNbjgGmqyXAKm0GSDRrKJH6ibzIoOVmj8j2pAAWoFfdibwfUOxFvTRBA/640?wx_fmt=png "null")

检查注册表`计算机\HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\Names`中是否有隐藏的账户，通过注册表进行建立的隐藏账户无法在计算机管理中进行查看，隐蔽性极高。在排查隐藏账户时可进行查看是否有相关可疑账户。发现确认可疑账户可右击进行删除。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9Eppsq6W2OOWGd6aia9RF80vOVWRTEwn5h4nWVpdfUNJBgChrxibJx62vMt4lA/640?wx_fmt=png "null")

## 0x03 恶意进程发现与关闭

恶意代码在windows系统中运行过程中，将以进程的方式进行展示。其中恶意进程执行这各种恶意行为。对于可执行程序，可能直接使用杀毒软件进行查杀，但是并非所有的恶意程序都能被查杀。也可手动进行查杀，使用工具psexplore，然后利用在线云沙箱等进行检测分析。对恶意程序相关服务进行关闭。

## 0x04 补丁查看与更新

windows系统支持补丁以修复漏洞。可以使用systeminfo查看系统信息，并展示对应的系统补丁信息编号。也可以在卸载软件中查看系统补丁和第三方软件补丁。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqicyEkfwL6aibbzqjUFY0pX6VjArNoYKcqJrv1GRF3rVsDbZ2Ig8Sx9Bg/640?wx_fmt=png "null")

在win10中使用快捷键win+i，然后选择Windows更新。他版本的Windows也具有Windows Update相关选项，可以进行更新操作。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVQAGYLowdvm9pGnP9EppsqhTvgqgN3hiaRGNlgYmibpnw0Tk4FeLmAxdN27LzeqiaE3yGboatQJibwbw/640?wx_fmt=png "null")

往期推荐

[敏感信息泄露](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247500219&idx=1&sn=8da48a9a049bab2f9215ad373868a1a5&chksm=ce5de3daf92a6acc7c2a58329c913062e9c34a9615ce742b761b2775916781abb50159a7d2d7&scene=21#wechat_redirect)

[潮影在线免杀平台上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499902&idx=1&sn=59cba8d980b4ecb0deefff99edaabd4d&chksm=ce5de21ff92a6b09a8972a0144557b0099e443aa8e018b17151c816fc7f08f3615ecb22617fc&scene=21#wechat_redirect)

[自动化渗透测试工具开发实践](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498466&idx=1&sn=085c15679436dedb06a179ca8d47951a&chksm=ce5dd883f92a5195ef74ac517741f6d3da0da40b5501d72016e52cb70344904bb85b8aef65ba&scene=21#wechat_redirect)

[【红蓝对抗】利用CS进行内网横向](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247492640&idx=1&sn=43b1991dc5628eab322923083fde8d70&chksm=ce5dc641f92a4f57ffb18e2977644b1f977fcc5e0eccdf10956d3ae4ce70dc95024500631e89&scene=21#wechat_redirect)

[一个Go版(更强大)的TideFinger](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498344&idx=1&sn=3679330363ff6890166b09f6a502f769&chksm=ce5dd809f92a511f6066fcbb12fb5c1dc8c2642e4e2690dad64d76cc6f9247eae356d16f5810&scene=21#wechat_redirect)

[SRC资产导航监测平台Tsrc上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499823&idx=1&sn=065ffeae6bd02fff922cfb12c5a0f4df&chksm=ce5de24ef92a6b58f709260b691e6b36e4a53aac00d3022946302b8e638696ed55c70e13e16f&scene=21#wechat_redirect)

[新潮信息-Tide安全团队2022年度总结](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA...