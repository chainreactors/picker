---
title: CVE–2019–8985漏洞复现
url: https://www.freebuf.com/vuls/408217.html
source: FreeBuf网络安全行业门户
date: 2024-08-17
fetch_date: 2025-10-06T18:05:41.750915
---

# CVE–2019–8985漏洞复现

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

CVE–2019–8985漏洞复现

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

CVE–2019–8985漏洞复现

2024-09-20 18:38:27

![image](https://image.3001.net/images/20240809/1723181689_66b5aa7911bed776c9f92.png!small)

## 1、漏洞描述

由相关信息得到漏洞点存在于`/bin/boa`程序中的`user_ok`函数，sprintf 的时候对v10造成了溢出 而v10的buf还特别小通过逆向可以知道这是个认证函数由`user_name:user_password`组成的键值对形式和本地的文件进行认证，具体可自行查看`/bin/boa`函数的逆向。

## 2、前期处理

### （1）固件提取

```
binwalk -Me fw.bin
```

提取之前需要安装sasquatch（如果是用源码安装的话，应该没有这样的问题），不然会提取失败，squashfs-root文件夹为空。![image](https://image.3001.net/images/20240809/1723181720_66b5aa982c8f4cd9f5e56.png!small)

### （2）查看相关架构

```
find -name busybox
file ./squashfs-root/bin/busybox
```

该架构为mips架构，32位大端序。![image](https://image.3001.net/images/20240809/1723181745_66b5aab114125c0b65b60.png!small)

### （3）用户级模拟

把`qemu-mips-static`文件复制到当前目录，以便于更好处理。

```
cp (which qemu-mips-static) .
```

![image](https://image.3001.net/images/20240809/1723181763_66b5aac33e5f44bc6435d.png!small)
把当前目录当做根目录，执行boa文件，发现有相关的报错，缺少相关的设备文件，使用`mknod`进行创建。

```
sudo chroot . ./qemu-mips-static /bin/boa --help
```

![image](https://image.3001.net/images/20240809/1723181771_66b5aacb814751b74d8a0.png!small)
创建文件解决报错后，并查看相关用法，可以看到，要传入两个文件，一个是boa path，另一个是conf path。boa启动命令一定是在配置文件或者开机项作为httpd服务启动，也就是说boa文件件会在其他文件中被使用，所以只需要grep搜索boa字符即可，这样就能够查找是相关文件中是如何使用boa文件的。

```
sudo mknod -m 666 ./dev/null c 1 3
```

![image](https://image.3001.net/images/20240809/1723181784_66b5aad83260e518fb254.png!small)
`grep -r 'boa ' .`，查看相应的字段，发现如下如下用法，`sudo chroot . ./qemu-mips-static /bin/boa -p /web -f /etc/boa.conf`执行，发生报错`“Can't create PID file!”`。
![image](https://image.3001.net/images/20240809/1723181793_66b5aae14594f2497dc9f.png!small)
将boa文件放入到32位ida中，shift + F12 查看字符串 “Can't create PID file!”，对该字符串进行交叉引用，`v14 = fopen(off_4590B0, "w");`该句决定着程序执行的成功还是识别，查看`off_4590B0`，内容如下

`.rodata:00415560 2F 76 61 72 2F 72 75 6E 2F 77+aVarRunWebsPid:.ascii "/var/run/webs.pid"<0>`

发现是`/var/run/webs.pid`无法创建，没有`run`文件夹。

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v5; // $s1
  int v7; // $a0
  int v8; // $v1
  FILE *v9; // $v0
  FILE *v10; // $s0
  int v11; // $v0
  FILE *v12; // $a0
  __pid_t v13; // $v0
  FILE *v14; // $s0
  size_t v15; // $v0
  int v16; // $s0
  char v17[24]; // [sp+20h] [-20h] BYREF
  __pid_t pid; // [sp+38h] [-8h] BYREF

  umask(0x3Fu);
  time(&ampcurrent_time);
  tzset();
  v5 = open("/dev/null", 0);
  if ( v5 == -1 )
    log_error_mesg_fatal("boa.c", 228, "main", "can't open /dev/null");
  if ( dup2(0, 50) == -1 )
    log_error_mesg_fatal("boa.c", 232, "main", "can't dup2 /dev/null to STDIN_FILENO");
  close(v5);
  if ( argc >= 5 )
  {
LABEL_13:
    v7 = argc;
    while ( 1 )
    {
      v8 = getopt(v7, (char *const *)argv, "h?p:f:");
      if ( v8 == -1 )
        break;
      if ( v8 == 102 )
      {
        strcpy(boa_file_path, optarg);
        read_config_files(optarg);
        v7 = argc;
      }
      else
      {
        if ( v8 != 112 )
        {
          sub_403CB4(*argv);
          goto LABEL_13;
        }
        sub_40496C(optarg);
        v7 = argc;
      }
    }
    init_signals();
    v9 = fopen(off_4590B0, "r");
    v10 = v9;
    if ( v9 )
    {
      fgets(v17, 20, v9);
      v11 = sscanf(v17, "%d", &pid);
      v12 = v10;
      if ( v11 )
      {
        if ( pid >= 2 )
          kill(pid, 15);
        v12 = v10;
      }
      fclose(v12);
    }
    v13 = getpid();
    sprintf(v17, "%d\n", v13);
    v14 = fopen(off_4590B0, "w");
    if ( v14 )
    {
      v15 = strlen(v17);
      fwrite(v17, v15, 1u, v14);
      fclose(v14);
      v16 = sub_4042E0();
      build_needs_escape();
      fprintf(stderr, "Starting Protocol Module: %-32s ... OK\n", "HTTP Server");
      status = 0;
      dword_459D18 = 0;
      start_time = current_time;
      loop(v16);
    }
    fprintf(stderr, "%s:%s:%d;Can't create PID file!\n", "boa.c", "main", 291);
    return -1;
  }
  else
  {
    sub_403CB4(*argv);
    return 0;
  }
}
```

`mkdir var/run`创建相关文件夹，创建完之后在试一下，又发生报错，意思是说相关端口已经被占用，而boa文件常用的端口是80，用`sudo lsof -i :80`查找80端口的进程，并kill掉，之后重新运行，发现HTTP Server启动成功。

> 这个问题不是每个人都会遇到的，笔者第一次执行的时候就没有这样的问题。

![image](https://image.3001.net/images/20240809/1723181812_66b5aaf4a9f58d233fda1.png!small)
![image](https://image.3001.net/images/20240809/1723181820_66b5aafc9a0b154b376d8.png!small)
运行成功之后，用wget发送一个poc验证一下，服务端出现get password error!问题，老样子，丢到ida中查看相关字符。
![image](https://image.3001.net/images/20240809/1723181831_66b5ab0708b8a16d9b447.png!small)
![image](https://image.3001.net/images/20240809/1723181837_66b5ab0df392fc9ab3f79.png!small)
通过ida进行定位，查看两个函数，发现是打开`"/tmp/passwd"`文件失败，直接将本机的文件复制过去，新建也是可以的，但为了防止格式问题，直接用本机的更为妥当，如果没用`tmp`文件夹，直接创建即可。

```
int __fastcall user_auth(const char *a1)
{
  int v2; // $a0
  char *v3; // $v0
  int v4; // $v0
  char v6[64]; // [sp+20h] [-40h] BYREF

  memset(v6, 0, sizeof(v6));
  if ( get_password(64) >= 0 )
  {
    v2 = 1;
    if ( byte_4596D0[0] != 58 )
    {
      v2 = 0;
      if ( a1 )
      {
        if ( !strstr(a1, "Basic") )
          return 0;
        sub_41489C(a1 + 6, authout, 128);
        v3 = strchr(authout, 58);
        *v3 = 0;
        v4 = user_ok(authout, v3 + 1);
        v2 = 1;
        if ( !v4 )
          return 0;
      }
    }
  }
  else
  {
    fprintf(stderr, "%s:%s:%d;get password error!\n", "htauth.c", "user_auth", 181);
    return 1;
  }
  return v2;
}
```

```
int __fastcall get_password(int a1)
{
  FILE *v2; // $s1
  int result; // $v0
  int v4; // $s0
  int v5; // $s2
  int v6; // $s3
  char v7[8]; // [sp+18h] [-8h] BYREF

  memset(byte_4596D0, 0, sizeof(byte_4596D0));
  v2 = fopen("/tmp/passwd", "r+");
  result = -1;
  if ( v2 )
  {
    v4 = 0;
    v5 = 0;
    v6 = 0;
    while ( fread(v7, 1u, 1u, v2) )
    {
      if ( v4 >= a1 || v7[0] == 13 || v7[0] == 10 )
      {
        byte_4596D0[64 * v5 + v4++] = 0;
        if ( !v6 )
        {
          ++v5;
          v4 = 0;
          v6 = 1;
          if ( v5 > 0 )
            break;
        }
      }
      else
      {
        byte_4596D0[64 * v5 + v4++] = v7[0];
        v6 = 0;
      }
    }
    fclose(v2);
    return 0;
  }
  return result;
}
```

`cp /etc/passwd ./tmp`，这里要注意一下，原本的tmp是对本机的软连接，先删除再创建
![image](https://image.3001.net/images/20240809/1723181849_66b5ab19aa6da2176040c.png!small)
重新把poc打过去，发现服务端发生崩溃
![image](https://image.3001.net/images/20240809/1723181858_66b5ab2284df69aa9d038.png!small)
下面这个是未崩溃的样子，以做对比
![image](https://image.3001.net/images/20240809/1723181869_66b5ab2dcffd43949a526.png!small)

## 2、漏洞利用

### （1）系统级模拟&gdbserver远程调试

简单的用户级模拟不能达到真实场景的需求，于是使用qemu的系统级模拟功能，模拟 32位的大端mips架构,mips表示大端，mipsel表示小端。

这边有一个自动化模拟的项目，省去了一些麻烦，有兴趣的可以试一试。

> https://github.com/glkfc/AIOTS

1. 下载相关内核（最好创建一个文件夹mips），这里的版本用vmlinux-3.2.0-4-4kc-malta最好，不然可能会导致gdbserver连接失败。

```
wget https://people.debian.org/~aurel32/qemu/mips/vmlinux-3.2.0-4-4kc-malta
wget https://people.debian.org/~aurel32/qemu/mips/debian_wheezy_mips_standard.qcow2
```

2. 本机创建网桥和接口，并将接口接到网桥上，以便于传输文件系统

```
sudo apt-get install bridge-utils
sudo brctl addbr Virbr0
sudo ifconfig Virbr0 192.168.153.1/24 up

sudo tunctl -t tap0
sudo ifconfig tap0 192.168.153.11/24 up
sudo brctl addif Virbr0 tap0
```

3. 启动虚拟机，在内核文件的位置打开terminal，执行以下命令，密码（root:roo...