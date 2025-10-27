---
title: FortiGate SSLVPN 堆溢出漏洞分析与利用
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247508415&idx=1&sn=dcf10b1f8619a087f4f5cc65105f49cd&chksm=fa527401cd25fd17f06017d2d19cddd790b2921d65a84f074fa89bb4e1411bd980b5854088f2&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-09-19
fetch_date: 2025-10-06T18:26:32.728912
---

# FortiGate SSLVPN 堆溢出漏洞分析与利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73Me0F4k1RKw9v5NicYSpT5ddYQicIFqsRsffYXtna9NNgkO639bFiaibLdh2Q/0?wx_fmt=jpeg)

# FortiGate SSLVPN 堆溢出漏洞分析与利用

原创

林昀

山石网科安全技术研究院

## 漏洞信息

处理env参数时存在逻辑缺陷，导致堆溢出写，漏洞利用可以导致任意代码执行。（CVE-2023-27997）

## 环境搭建

### 导入虚拟机

打开 vmware 左上角 文件 -> 打开虚拟机 -> 选择 FortGate-VM64.ovf

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeLR6kGuRygm4EQwOFgP7H30wve3l6WB0tibDaRMhsdXZBWKM5VsvyGog/640?wx_fmt=png&from=appmsg)

直接就能运行 fortigate 登录账号：admin  密码：空，然后设置新密码

admin

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MewMNPulk5o7DYGpjoPOLAMKLvFGBPWkoicSQ7D8Ou0s4Z9Du41qIReQg/640?wx_fmt=png&from=appmsg)

### 配置网络

vm 下同样有作为攻击机器的 ubuntu-22 ，需要先设置 fortigate-vm 和 ubuntu-22 之间能够互通。关闭 fortigate-vm，并设置所有网络适配器为 Nat 模式

先看一下ubuntu攻击机的ip，再来确定我们要设置的网段

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeuxLvHicClxpfrZLibicskCdJ7TLWOaerok2NutCAAuTZ03aicx4iasebxkA/640?wx_fmt=png&from=appmsg)

我的ubuntu处于192.168.18.0段，得设置一下实验机也在这个网段上

记得多加一张net网卡

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeS2dPZBQ5ia69oNfdKR8pSTloRpVamUCbWgtKz2Vfd1wofhT1JQWEEyA/640?wx_fmt=png&from=appmsg)

配置成功之后，执行以下命令可以查看接口信息

```
show system interface
```

### 配置服务（telnet和ssh记得打开，否则后续23端口无法正常调试）

```
config system interface
edit port1
 set mode static
 set ip 192.168.18.123 255.255.255.0
 set allowaccess http https ping ssh telnet
 end
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73Me7cgPcXpOtanqDFQfWD8Wrz6D02yGLlXzV5BPHvRRlPqepnqffibOmVA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73Me9mLc5gSibR3giaqCkDsicUkQLzzoPziccPZRoS0uFmHhNXRNibrcKV3Unlg/640?wx_fmt=png&from=appmsg)

用命令查询情况，然后使用ubuntu攻击机看看情况

访问飞塔的地址可以访问成功

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeoO6QOIN6c0Lv57Ficj5Av6u3wazRShZ5YAl9K4R9ef57a0icqwCibamJA/640?wx_fmt=png&from=appmsg)

使用我们刚刚设置的密码可以进入，但是要认证

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73Med0IXQZibbibRe0whHU56xKxBTnjyhlZnWpadvJKfsnrc28YqgV9yxEDg/640?wx_fmt=png&from=appmsg)

配置网关，连接外网

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeS2dPZBQ5ia69oNfdKR8pSTloRpVamUCbWgtKz2Vfd1wofhT1JQWEEyA/640?wx_fmt=png&from=appmsg)

在这里找出网ip地址即可

```
config router static
 edit 1
 set device port1
 set gateway 192.168.18.2
 end
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MegSQAicqJpd2d4H1nc2dbF05vVkE1zHlJzAQzpH3vHVEoA56tekM9urA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeSib6OZNuhvZYe3XcRViaBIuzpUCokUDyMN4S0sfJa69XbPPzz7iboJbZg/640?wx_fmt=png&from=appmsg)

配置配置完就可以出网了

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeXic1IDibHYlUnLOZugbI9qAWdBPwibPBjprWPReWVEk8ibgtI1xyQscquA/640?wx_fmt=png&from=appmsg)

### 服务配置

我们需要开启sslvpn的功能，需要对防火墙进行以下配置

1、SSLVPN\_address | subnet\_addres | ubuntu22

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73Mev1AMP2ZscSUlXuRe3YeoUOoiaLD7eRk6HHS77ZJjo27BkiaibSnbB8FEg/640?wx_fmt=png&from=appmsg)

再添加一个用户

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeLa19P31tsa7RMoE9ZawnEcjiaARiajXrXUj6WLQic2VWM3PibFxjoaf3Fg/640?wx_fmt=png&from=appmsg)

添加一个用户组，并把之前注册的用户添加进新的用户组

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeCfAU9C6fPbH2xiceu16kSXiamC5b6G7JYLzupsRVsmjZ7csmbicvXcibSg/640?wx_fmt=png&from=appmsg)

修改 vpn 门户

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeNIXzJIyZa79iawgT2dwqh8yjmapRQ3POzbFPzN5l8eVoyku71EMxW4A/640?wx_fmt=png&from=appmsg)

修改full-access

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73Me2FU4PALj7jp9YAB5ichVY4jWvWMz25fvnXBZpyNwcXjBEfYcU14efYw/640?wx_fmt=png&from=appmsg)

修改后选择保存

进入 vpn 设置，配置如下

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeK6bogk004lX7fkX2HD0BblMj0R6FGmSeRVWicHAm1ciaajJ1NfPF4kibw/640?wx_fmt=png&from=appmsg)

接着修改防火墙配置策略

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeY3ux5FiaOTCk6TbhFt6Muqqf3OwIIiamEuHzzbRMGPXQSpkLucKD3hMg/640?wx_fmt=png&from=appmsg)

之后https访问4433端口即可

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeZ4AARj58BkAaAc7TcBrvP1ibGibKYZicn1AHEBcrE9HNMBIoOXhAKnMkg/640?wx_fmt=png&from=appmsg)

### GDB调试环境搭建

使用gdbserver+gdb进行调试，提前植入后门

#### 提取固件

在虚拟机关闭的情况下，右键，打开

关闭防火墙

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73Me22MA83lIcXKD4xciaaYRsTjVOiaR2wSC89c4icEq43iaJuFxyaAMT4ZlzQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeMJCgFWmkicO91KnPepUTbefJic92kVNDSr3aFV9ia1EK5ZEZzaBNYMNBQ/640?wx_fmt=png&from=appmsg)

挂载之后，我们就可以拿到一整个文件系统的文件，包括内核

需要将flatkc复制下来进行分析

vmlinux-to-elf处理一下无符号的问题

```
sudo apt install python3-pip liblzo2-dev
sudo pip3 install --upgrade lz4 zstandard git+https://github.com/clubby789/python-lzo@b4e39df
sudo pip3 install --upgrade git+https://github.com/marin-m/vmlinux-to-elf
```

```
vmlinux-to-elf flatkc flatkc-efl
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnR1Ivt65QXRZicIhy5iaT73MeEPa0RPFEtV4V0Pcy93MrlIRMGIsoBhN7WGia3blKrA0sg1YVwbVAnBQ/640?wx_fmt=png&from=appmsg)

#### busybox编译

如果编译过程出错了，可以换个更高的busybox版本去编译

```
    curl http://busybox.net/downloads/busybox-1.23.2.tar.bz2 | tar xjf -
    mkdir -p obj/busybox
    cd busybox-1.23.2
    make O=../obj/busybox defconfig #独立在新文件中进行相关配置
    cd ../obj/busybox
    make menuconfig
```

#### 后门程序

这里的话，因为我们要开启telnet服务作为shell，笔者的思路是将telnet开启然后开放在22端口，我们就可以利用这个端口作为一个shell，然后还要把telnet服务的给替换成我们的gdbserver调试端口，只需要关闭即可

```
#include <stdio.h>

void shell(){
        system("/bin/busybox ls", 0, 0);
        system("/bin/busybox killall sshd && /bin/busybox telnetd -l /bin/sh -b 0.0.0.0 -p 22", 0, 0);
        return;
}

int main(int argc, char const *argv[])
{
        shell();
        return 0;
}
```

需要给他静态编译一下

```
gcc smartctl.c -static -o smartctl
```

#### gdbserver

```
https://github.com/hugsy/gdb-static
```

编译之后我，把gdbserver和busybox还有我们编译的后门程序smartctl放到bin目录底下

#### 重打包 ``` sudo chroot ./ sbin/ftar -cf bin.tar bin sudo chroot ./ sbin/xz --check=sha256 -e bin.tar sudo find ./ | cpio -H newc -o > ../rootfs.raw cd ../ sudo cat ./rootfs.raw | gzip > rootfs.gz ```

#### 注入后门

反编译内核文件flatkc

```
void __fastcall __noreturn init_post_isra_0(__int64 a1, void **a2)
{
  char v2; // al
  __int64 v3; // rax
  int v4; // edx
  int v5; // ecx
  int v6; // r8d
  int v7; // r9d
  char v8; // [rsp-8h] [rbp-8h]

  v8 = v2;
  async_synchronize_full(a1, a2);
  free_initmem();
  dword_FFFFFFFF80A19880 = 1;
  numa_default_policy();
  v3 = *(_QWORD *)(__readgsqword(0xB700u) + 1048);
  *(_DWORD *)(v3 + 92) |= 0x40u;
  if ( !(unsigned int)fgt_verify() )//校验函数
  {
    off_FFFFFFFF809B82C0 = "/sbin/init";
    a2 = &off_FFFFFFFF809B82C0;
    kernel_execve("/sbin/init", &off_FFFFFFFF809B82C0, off_FFFFFFFF809B81A0);
  }
  panic(
    (unsigned int)"No init found.  Try passing init= option to kernel. See Linux Documentation/init.txt for guidance.",
    (_DWORD)a2,
    v4,
    v5,
    v6,
    v7,
    v8);
}
```

我们注入后门程序之后，要开机也是需要断点断在fgt\_verify() 函数，将返回值修改

在代码中，我们能知道，启动的是sbin中的init文件，我们对init文件中校验逻辑进行patch

verify\_kernel\_and\_rootfs\_0(）会对内核文件进行验证，不通过会执行dohalt重启内核，我们需要把他patch掉，不执行do\_halt

最后patch之后的代码是这样子的

```
     requested_time.tv_sec);
    sub_450510(1LL);
    sub_4537B0();
    sub_452D00();
    sub_451240();
    sub_4511A0();
    if ( (unsigned int)sub_253C4D0() )
    {
      sub_26118A0();
      sub_450200("/bin/fips_self_test");
    }
    else
    {
      sub_4511F0();
      sub_2573800();
    }
    v21 = "/tmp/terminfo";
    sub_27F6B50("/data/etc/terminfo");
    sub_4533C0("/data/etc/terminfo", "/tmp/terminfo");
    sub_453460();
```

使用内核文件下断点，修改寄存器的值为0

```
import gdb

class SetRaxBreakpoint(gdb.Breakpoint):
    def __init__(self, bp_expr, rax_value, temporary=False):
        gdb.Breakpoint.__init__(self, bp_expr, gdb.BP_BREAKPOINT, False, temporary)
 ...