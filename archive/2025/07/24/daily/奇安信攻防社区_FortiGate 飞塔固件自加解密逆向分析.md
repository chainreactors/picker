---
title: FortiGate 飞塔固件自加解密逆向分析
url: https://forum.butian.net/share/4471
source: 奇安信攻防社区
date: 2025-07-24
fetch_date: 2025-10-06T23:16:29.150648
---

# FortiGate 飞塔固件自加解密逆向分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### FortiGate 飞塔固件自加解密逆向分析

* [漏洞分析](https://forum.butian.net/topic/48)

前言：在进行IOT漏洞挖掘中，我们常常遇到固件加密问题导致在没有硬件设备时无法进行漏洞挖掘，本篇主要来进行分析固件解密的一些思路，因为作者认为在很多固件当中大部分加密都会在它固件里进行自加密、自解密，所以只要找到它的加密的位置进行逆向分析，就可以去进行解密，根据项目需求，这里分析一波飞塔解密的流程，通过这个流程更加深入的去理解这个加解密的思想，废话不多说，下面进行工作分析

FortiGate OS 加解密分析
==================
前言：在进行IOT漏洞挖掘中，我们常常遇到固件加密问题导致在没有硬件设备时无法进行漏洞挖掘，本篇主要来进行分析固件解密的一些思路，因为作者认为在很多固件当中大部分加密都会在它固件里进行自加密、自解密，所以只要找到它的加密的位置进行逆向分析，就可以去进行解密，根据项目需求，这里分析一波飞塔解密的流程，通过这个流程更加深入的去理解这个加解密的思想，废话不多说，下面进行工作分析
逆向分析
----
挂载fortigate vmdk
```php
apt-get install qemu
apt install qemu-utils
modprobe nbd max\\_part\=16
qemu-nbd \--connect\=/dev/nbd1 FortiGate7\\_4\\_2-disk1.vmdk
mount /dev/nbd1p1 /mnt
```
查看extlinux.conf 启动配置文件
```php
cat extlinux.conf
DISPLAY boot.msg
TIMEOUT 10
TOTALTIMEOUT 9000
DEFAULT flatkc ro panic\=5 endbase\=0xA0000 console\=ttyS0, root\=/dev/ram0 ramdisk\\_size\=65536 initrd\=/rootfs.gz
```
拷贝rootfs.gz和flatkc
使用enc 命令查看rootfs.gz
![1752325137236.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-c494dd74dee31acfb57613a17477aadd044eaca3.png)
通过通读Linux kernel源码 populate\\_rootfs 函数如下
```c
static int \\_\\_init populate\\_rootfs(void)
{
/\\* Load the built in initramfs \\*/
char \\*err \= unpack\\_to\\_rootfs(\\_\\_initramfs\\_start, \\_\\_initramfs\\_size);
if (err)
panic("%s", err); /\\* Failed to decompress INTERNAL initramfs \\*/
/\\* If available load the bootloader supplied initrd \\*/
if (initrd\\_start && !IS\\_ENABLED(CONFIG\\_INITRAMFS\\_FORCE)) {
#ifdef CONFIG\\_BLK\\_DEV\\_RAM
int fd;
printk(KERN\\_INFO "Trying to unpack rootfs image as initramfs...\\n");
err \= unpack\\_to\\_rootfs((char \\*)initrd\\_start,
initrd\\_end \- initrd\\_start);
if (!err) {
free\\_initrd();
goto done;
} else {
clean\\_rootfs();  #清理clean\\_rootfs
unpack\\_to\\_rootfs(\\_\\_initramfs\\_start, \\_\\_initramfs\\_size);  #使用start和size进行解包
}
printk(KERN\\_INFO "rootfs image is not initramfs (%s)"
"; looks like an initrd\\n", err);
fd \= ksys\\_open("/initrd.image",
    O\\_WRONLY|O\\_CREAT, 0700);
if (fd >\= 0) {
ssize\\_t written \= xwrite(fd, (char \\*)initrd\\_start,
initrd\\_end \- initrd\\_start);
​
if (written !\= initrd\\_end \- initrd\\_start)
pr\\_err("/initrd.image: incomplete write (%zd != %ld)\\n",
      written, initrd\\_end \- initrd\\_start);
​
ksys\\_close(fd);
free\\_initrd();
}
done:
/\\* empty statement \\*/;
#else
printk(KERN\\_INFO "Unpacking initramfs...\\n");
err \= unpack\\_to\\_rootfs((char \\*)initrd\\_start,
initrd\\_end \- initrd\\_start);
if (err)
printk(KERN\\_EMERG "Initramfs unpacking failed: %s\\n", err);
free\\_initrd();
#endif
}
flush\\_delayed\\_fput();
/\\*
\\* Try loading default modules from initramfs. This gives
\\* us a chance to load before device\\_initcalls.
\\*/
load\\_default\\_modules();  #挂载rootfs
​
return 0;
}
```
通过分析源代码，主要是通过populate\\_rootfs 函数里的全局变量\*\*initramfs\\_start和\*\*initramfs\\_end来进行处理，解压缩 ramdisk 的 GZIP 压缩的 CPIO 映像并挂载 \*rootfs\*
FortiOS 是基于 Linux 的，并使用了修改后的内核 4.19.13（从 7.4.3 版本开始），因此我们可以反汇编 flatkc（使用 vmlinux-to-elf 转换为 ELF 格式[\*\*后\[8\]）\*\*](https://github.com/marin-m/vmlinux-to-elf)并寻找上述功能：
以下是反编译出来的伪代码
```c
\\_\\_int64 populate\\_rootfs()
{
int v0; // esi
\\_\\_int64 v1; // rax
int v2; // edx
int v3; // ecx
int v4; // r8d
int v5; // r9d
\\_\\_int64 v6; // r12
int v7; // edx
int v8; // ecx
int v9; // r8d
int v10; // r9d
int v11; // eax
unsigned int v12; // ebx
\\_\\_int64 v13; // rax
int v14; // ecx
int v15; // r8d
int v16; // r9d
​
v0 \= (int)off\\_FFFFFFFF817DA3C8;
v1 \= unpack\\_to\\_rootfs(a070701000002d1, off\\_FFFFFFFF817DA3C8);// "070701000002D1000041ED0000000000000000000000026580E65900000000000000030000000100000000000000000000000400000000dev"
 if ( v1 )
  panic((unsigned int)&aS\\_18\[1\], v1, v2, v3, v4, v5);// "\\t%s"
 if ( p\\_\\_070701000002D1000041ED0000000000000000000000026580E659000000 )
{
  printk((unsigned int)&unk\\_FFFFFFFF813CE3D0, v0, v2, v3, v4, v5);
  v6 \= unpack\\_to\\_rootfs(
          p\\_\\_070701000002D1000041ED0000000000000000000000026580E659000000,
          qword\\_FFFFFFFF81838078 \- p\\_\\_070701000002D1000041ED0000000000000000000000026580E659000000);
   if ( !v6 )
  {
LABEL\\_9:
    free\\_initrd();
    goto LABEL\\_10;
  }
  clean\\_rootfs();
  unpack\\_to\\_rootfs(a070701000002d1, off\\_FFFFFFFF817DA3C8);// "070701000002D1000041ED0000000000000000000000026580E65900000000000000030000000100000000000000000000000400000000dev"
  printk((unsigned int)&unk\\_FFFFFFFF813CE408, v6, v7, v8, v9, v10);
  v11 \= do\\_sys\\_open(4294967196LL, aInitrdImage, 32833, 448);// "/initrd.image"
  v12 \= v11;
   if ( v11 >\= 0 )
  {
    v13 \= xwrite(
            (unsigned int)v11,
            p\\_\\_070701000002D1000041ED0000000000000000000000026580E659000000,
            qword\\_FFFFFFFF81838078 \- p\\_\\_070701000002D1000041ED0000000000000000000000026580E659000000);
     if ( qword\\_FFFFFFFF81838078 \- p\\_\\_070701000002D1000041ED0000000000000000000000026580E659000000 !\= v13 )
      printk(
        (unsigned int)&unk\\_FFFFFFFF813CE448,
        v13,
        qword\\_FFFFFFFF81838078 \- p\\_\\_070701000002D1000041ED0000000000000000000000026580E659000000,
        v14,
        v15,
        v16);
    \\_close\\_fd(\\*(\\_QWORD \\*)(\\_\\_readgsqword((unsigned int)&off\\_14D80) + 1576), v12);
    goto LABEL\\_9;
  }
}
LABEL\\_10:
flush\\_delayed\\_fput();
load\\_default\\_modules();
return 0;
}
```
我们对照源码将以上伪代码进行修正命名，修正后的代码如下
```c
\\_\\_int64 populate\\_rootfs()
{
v0 \= \\_initramfs\\_size;
\\_070701000002D1000041ED0000000000000000000000026580E65900000000 \= unpack\\_to\\_rootfs(\\_initramfs\\_start, \\_initramfs\\_size);// "070701000002D1000041ED0000000000000000000000026580E65900000000000000030000000100000000000000000000000400000000dev"
 if ( \\_070701000002D1000041ED0000000000000000000000026580E65900000000 )
  panic((unsigned int)&aS\\_18\[1\], \\_070701000002D1000041ED0000000000000000000000026580E65900000000, v2, v3, v4, v5);// "\\t%s"
 if ( initrd\\_start )
{
  printk((unsigned int)&unk\\_FFFFFFFF813CE3D0, v0, v2, v3, v4, v5);
  v6 \= unpack\\_to\\_rootfs(initrd\\_start, initrd\\_end \- initrd\\_start);// 解包通过initrd\\_start,initrd\\_end-initrd\\_start 来进行解包
   if ( !v6 )
  {
LABEL\\_9:
    free\\_initrd();
    goto LABEL\\_10;
  }
  clean\\_rootfs();
  unpack\\_to\\_rootfs(\\_initramfs\\_start, \\_initramfs\\_size);// "070701000002D1000041ED0000000000000000000000026580E65900000000000000030000000100000000000000000000000400000000dev"
  printk((unsigned int)&KERN\\_INFO, v6, v7, v8, v9, v10);
  \\_\\_initrd.image\\_ \= do\\_sys\\_open(4294967196LL, aInitrdImage, 32833, 448);// "/initrd.image"
  \\_\\_initrd.image\\_\\_1 \= \\_\\_initrd.image\\_;
   if ( \\_\\_initrd.image\\_ >\= 0 )
  {
    v13 \= xwrite((unsigned int)\\_\\_initrd.image\\_, initrd\\_start, initrd\\_end \- initrd\\_start);
     if ( initrd\\_end \- initrd\\_start !\= v13 )
      printk((unsigned int)&unk\\_FFFFFFFF813CE448, v13, initrd\\_end \- initrd\\_start, v14, v15, v16);
    \\_close\\_fd(\\*(\\_QWORD \\*)(\\_\\_readgsqword((unsigned int)&off\\_14D80) + 1576), \\_\\_initrd.image\\_\\_1);
    goto LABEL\\_9;
  }
}
LABEL\\_10:
flush\\_delayed\\_fput();
load\\_default\\_modules();                       // 加载rootfs包
return 0;
}
```
现在，已经分析出来了大概的rootfs的加载流程，在加载rootfs包的时候都是从initrd\\_start和initrd\\_end 的全局变量来加载，从头逆向不太可能，这里交叉引用一下，
!...