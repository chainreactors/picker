---
title: 电子壳里的漏洞：Electron应用如何成为攻击者的后门温床
url: https://mp.weixin.qq.com/s/paLvBHmYGsZIjH9vy8jgOw
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:08:55.046946
---

# 电子壳里的漏洞：Electron应用如何成为攻击者的后门温床

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcxZ81HAluoqdmt2UXoMaowPNDEkgrs5fOZNRpLiampibcK0KWMDCUTDz5duguibpxGrQgQvqdSbXoKI1Wu6gh4QibBCGtSoKcwRkA/0?wx_fmt=png&from=appmsg)

# 电子壳里的漏洞：Electron应用如何成为攻击者的后门温床

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Electron应用遍地都是，VS Code、Slack、Twitch都在用。但它们安装到用户目录的设计、未加密的asar包、以及Chrome调试协议，恰好给了攻击者三个不碰系统文件的持久化入口。这篇文章分析了BEEMKA脚本注入、DLL劫持、远程调试三种利用手法，并给出监控方案。

## 一、这事是怎么开始的

前阵子和同事聊起企业设备上怎么维持权限的话题，他说自己写了个工具。当时不确定这东西实战有没有用，但顺着Electron应用往下挖，发现可操作的空间比想象中大得多。

下面的这些东西——DLL劫持、远程调试协议、BEEMKA——都不是新发现，网上早有零零散散的记录。只是把这些方法重新整理成一份清单花了我不少时间，索性就写一篇完整的参考，给做持久化的人用。

## 二、Electron是个什么东西

说实话，Electron本质上就是把Chromium浏览器包进了一个桌面应用的外壳里。2013年发布到现在，它已经成了跨平台桌面开发最主流的框架。你每天用的VS Code、Slack、Twitch桌面端，全是Electron套的壳。

它的好处是写一套代码，Windows、macOS、Linux三个平台都能跑。坏处也在这——为了做到这点，Electron在用户空间里塞了一整套浏览器环境，又大又重。但换个角度看，如果你能在这个进程里跑自己的代码，能做的事就多了。

## 三、BEEMKA：改个文件的事

BEEMKA的做法有个明显的好处：不动系统文件，不碰内存注入。这意味着什么？很多杀软对这种操作基本无感。

Electron框架本身不用改，要动的是它的`asar`文件。`asar`是个类似tar的打包格式，简单粗暴地把所有文件拼在一起，不加压缩、不加密、不混淆、不签名——什么保护都没有。这个文件就躺在当前用户的`%APPData%`目录里。拿VS Code举例，默认路径就是`C:\Users\<用户名>\AppData\Local\Programs\Microsoft VS Code\resources\app\`。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcxZ81HAluoqdmt2UXoMaowPNDEkgrs5fOZNRpLiampibcK0KWMDCUTDz5duguibpxGrQgQvqdSbXoKI1Wu6gh4QibBCGtSoKcwRkA/640?wx_fmt=png&from=appmsg)

▲ VS Code的asar文件所在目录

你只需要把这个包解压，往源码文件里塞一段JavaScript，再重新打包回去，就能在应用界面里执行自定义代码。BEEMKA把这个过程自动化了，自带几个开箱即用的模块：

$ python3 beemka.py --list

Available modules

[ rshell\_cmd ]          Windows Reverse Shell
[ rshell\_linux ]        Linux Reverse Shell
[ screenshot ]          Screenshot Module
[ rshell\_powershell ]   PowerShell Reverse Shell
[ keylogger ]           Keylogger Module
[ webcamera ]           WebCamera Module

功能都挺基础——反弹shell、截图、键盘记录、摄像头——但刚好够证明这条路走得通。你要想让检测更难，自己写个自定义模块也不费事。

### 怎么防

官方到现在没给出正经的修复方案。GitHub上关于asar签名的讨论2019年就开了，但issue一直晾着没人动。

监控进程树能拦住一部分通过命令行执行的攻击，但如果攻击者走HTTPS请求往外传数据，这招就废了。更靠谱的做法是盯着AppData目录的变化，用Yara规则对改动过的文件做检查。

参考：
· BEEMKA项目地址[1]
· 相关演讲视频[2]

---

## 四、DLL劫持：老套路新目标

DLL劫持本身是个老掉牙的技术，拿来搞Electron应用却有天然优势。原因很简单：所有Electron应用都装在用户目录`C:\Users\<用户名>\AppData\Local`下面，而这个目录是当前用户可写的。

这就意味着攻击者可以直接往应用目录里扔一个恶意DLL，劫持DLL的搜索顺序，让应用加载自己指定的库文件。Electron官方仓库的GitHub Issue里记录了一长串可以劫持的具体DLL文件名。

但DLL劫持操作起来常常很折腾。你得先搞清楚目标架构才能编译对应的DLL，如果目标应用调用了原DLL里的函数，还得搞个ProxyDLL来转发请求，不然程序直接崩给你看。

### 怎么防

监控应用进程树还是那套逻辑，能抓出从应用上下文里跑出来的奇怪命令。更好的办法是盯着AppData目录里有没有新建的DLL文件，或者已有文件有没有被改动，然后用Yara规则做对比。

参考：
· Electron官方DLL劫持Issue跟踪[3]
· 自动化DLL劫持发现方法[4]
· DLL代理技术详解[5]
· Spartacus工具[6]

---

## 五、远程调试协议：改个快捷方式就能用

如果说前两种方法还有点门槛，那直接利用Chrome远程调试协议的手段就简单得离谱了——改一下快捷方式就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdC4OFcF1b49Pc8eS4MZe9l78V2tkhPArqGEffiaa8Zslb72tShtuV4uokjBLq5xovicqLgPO49iaqoH9QDydwY2niclibO6zXUfnGo/640?wx_fmt=png&from=appmsg)

▲ 修改应用快捷方式的启动参数

在快捷方式里加上`--remote-debugging-port`参数，指定一个端口。应用启动时会在这端口上开一个HTTP服务，把应用当网页暴露出来，你用浏览器就能连上去。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibcic6fA9TCQmZuXG5pKfo1bjZPXicyTyQa99DYy3ticibWA4nMTydrXJVRia0E43xiaxibZ5CUCzXOClgZbFhMR4Zhcx98dJOy70icoJJI/640?wx_fmt=png&from=appmsg)

▲ 浏览器中访问调试接口的界面

连上去之后，在受害者应用的环境里跑什么JavaScript都行。Metasploit甚至自带了`auxiliary/gather/chrome_debugger`模块，能直接从远程文件系统里往外扒文件。

但这个方法有个硬伤：远程调试接口默认只监听localhost，没管理员权限改不了。有管理员权限的话可以用`netsh`做端口转发绕过去，但如果只是用户级权限，这条路就走不通了。

不过别急，还有个`--inspect`参数，能让你指定监听的IP地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfLnYPHBYwDAwTq9icyxu4X3UN0BNp754sicPY1FibU6WSRp2PBKOZ4SmN78RjeFDib3D5mmKsloCy7kfIJibG9Fg0RBiak5RnsK08aw/640?wx_fmt=png&from=appmsg)

▲ --inspect参数允许指定监听地址

通过`chrome://inspect`就能连上远程机器，在Node.js实例的上下文里执行代码。比如读个hosts文件：

const fs = require('fs'); fs.readFile('../../../../../../../../../windows/system32/drivers/etc/hosts', 'utf8', (err, data) => { if (err) { console.error(err); return; } console.log(data); });

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeIksP0Yichdc3aITdX7kjKicJticO9reBtaCeTNgjmfjwau5ggNnk84HpFCg6iaRBWJdFwsP7ux2HwEuvCPsCBAKx10GliaibYcOHAU/640?wx_fmt=png&from=appmsg)

或者直接跑系统命令：

const { exec } = require("child\_process"); exec("whoami", (error, stdout, stderr) => { if (error) { console.log(`error: ${error.message}`); return; } if (stderr) { console.log(`stderr: ${stderr}`); return; } console.log(`stdout: ${stdout}`); });

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibf8WGaMfFp91iaonEJYPKvpI9OUQPP11UaFMd7Mz2cY3o6J1iaMic66Ipv1s1S4iclB5brFibj7bQyB8jUrdPK1lcLV0ibBibSRLGcmL8/640?wx_fmt=png&from=appmsg)

### 怎么防

监控机器上开放的端口，发现用户不知情的情况下有陌生端口监听就报警。同时监控应用进程树，抓从应用上下文里跑出来的系统命令。另外还要监控带这些调试参数的进程创建行为。

参考：
· Windows端口转发[7]
· Metasploit Chrome调试模块[8]
· Chrome远程调试官方说明[9]
· Electron主进程调试文档[10]

---

## 六、说到底，问题出在哪

Electron是个能让开发者快速铺开桌面应用的好东西。但它在设计上就有个绕不开的问题：应用装到了用户自己的命名空间里。今天的企业工作站上，几乎每台机器都至少装着一个Electron应用——而这就是一个现成的持久化落脚点。

最该盯紧的一件事很简单：AppData目录下的文件变化。特别是DLL文件的创建和已有应用资源的修改。看到这些，大概率不是误报。

---

### 参考资料

[1] https://github.com/ctxis/beemka

[2] https://www.youtube.com/watch?v=cL-NzLhAapc

[3] https://github.com/electron/electron/issues/28384

[4] https://posts.specterops.io/automating-dll-hijack-discovery-81c4295904b0?gi=1f0b7d677e

[5] https://itm4n.github.io/dll-proxying/

[6] https://github.com/Accenture/Spartacus

[7] https://embracethered.com/blog/posts/2020/windows-port-forward/

[8] https://www.rapid7.com/db/modules/auxiliary/gather/chrome\_debugger/

[9] https://blog.chromium.org/2011/05/remote-debugging-with-chrome-developer.html

[10] https://www.electronjs.org/de/docs/latest/tutorial/debugging-main-process

[11] https://text.tchncs.de/ioi/backdooring-electron-applications

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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