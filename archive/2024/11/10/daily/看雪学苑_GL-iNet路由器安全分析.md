---
title: GL-iNet路由器安全分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458581738&idx=1&sn=f39901614406d6e821930256c825be7e&chksm=b18dca6086fa43764f4a7d5188e3731699e8cd046115c32830160e5cc08f9ac97c13d755e27e&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-10
fetch_date: 2025-10-06T19:15:35.441553
---

# GL-iNet路由器安全分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LO4ROs23WYR0A1Pe4dV7kkCRJicqdicy1uVRxrYnAwOILza3pA3F0MlRw/0?wx_fmt=jpeg)

# GL-iNet路由器安全分析

0x指纹

看雪学苑

前段时间看到复现分析GL-iNet路由器CVE-2024-39226漏洞的两篇文章，看完也跟着了分析下，固件仿真过程踩了一些坑，开始我直接用Ubuntu24的qemu-system-arm跟着操作都会出现错误”Cortex-A9MPCore peripheral can only use Cortex-A9 CPU”，摸索了挺久发现文章用的都是debian\_wheezy\_armhf来仿真，但太老了以至于直接跑GL-iNet固件会出现Illegal instruction的错误，就使用Ubuntu18安装的低版本qemu-system-arm，能绕过来指定仿真开发板非支持的cpu，qemu在高版本中修复了这个问题，就出现了新些版本Ubuntu安装的qemu-system-arm启动报错问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LK3wQAEFo2zCeUrrzujRsZKlgTUBJWK9gicSfxwxjialQEZYib7YQibIQAw/640?wx_fmt=jpeg&from=appmsg)

后面琢磨了下，用低版本qemu-system-arm来绕过不算是好方法，试了试换个高版本内核镜像仿真就行了，可以花些时间自己制作一个，我是直接用开箱即用制作好的(https://people.debian.org/~gio/dqib/中的armhf-virt)，根据自己的复现环境的网络配置改一下说明中的启动命令即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LsBH6G6cy45j1MAB16QA5q0sn6MD2QQ48Rh1rqjroJotiavW7RqZooOg/640?wx_fmt=png&from=appmsg)

在分析漏洞时候，有搜索翻阅下GL-iNet官方发布的相关安全信息，发现官方整理得很有序完善详实，建立有一个漏洞修复信息仓库，有漏洞描述、影响范围、固件版本或利用方式等，修复漏洞的CVE编号没有标明，但在GL-iNet安全更新信息发布网站中可以找到每个版本更新修复的CVE编号，梳理一下可轻松找到其对应关系。在梳理时候，我发现两篇复现文章末尾都用了另外一个无需登录即可执行rpc调用的漏洞CVE-2024-39227，不过作者都没有提到是这个漏洞编号，这个漏洞的成因和利用都非常简单，但危害性巨大，并且CVE-2024-39226看起来也主要是为了配合这个漏洞来实现未授权远程执行而找到的。

复现分析完文章提到的两个漏洞后，我去官网下载最新的固件版本v4.6.6扒拉了下，发现像CVE-2024-39226这种本地或授权后可以命令注入类型问题还是不少的。拥有授权sid后/usr/lib/oui-httpd/rpc目录中文件的方法基本是可以任意调用，有些文件是luac文件反编译下即可。rpc目录下有十分多的类方法，简单翻了翻发现直接和间接进行命令注入的点很多，几乎防不胜防，想逐一修复工作量不小也不太有趣，思考下觉得这更像是一个系统框架设计问题吧，便和GL-iNet安全团队邮件反馈沟通了下，给出了一些示例。

进一步思考下，最重要的安全防线基本就是一道授权防护了，拥有或者绕过授权后便是如入无人之境了，历史CVE有一些是授权绕过漏洞，看了下相比授权后注入漏洞会更有意思些，不难但很经典，修复后又被绕过，或者同一个攻击面找到了别的攻击点。

所以此文一是对两篇GL-iNet路由器CVE-2024-39226漏洞复现文章进一步的补充，感谢作者无私的分享精神，我来进一步传递下互助分享的火炬，也为初学者提供一些有价值的资料和信息；二是复现分析下GL-iNet路由器几个授权相关的漏洞，看看最重要的防线都是怎样被突破的，以及修复后又是怎么再被突破的。

固件仿真

01

## **宿主机网络配置**

以Ubuntu24系统为例，先安装qemu-system-arm。

```
sudo apt install qemu-system-arm
```

配置宿主机网络，参考QEMU搭建ARM64环境一文，先执行安装命令，安装后后宿主机会自动创建一个默认网桥virbr0。

```
sudo apt install libvirt-daemon-system libvirt-clients virt-manager
```

随后执行命令，创建并启用名为tap0的TAP设备，再将其添加到virbr0网桥中，并修改文件权限。

```
sudo ip tuntap add dev tap0 mode tap
sudo ip link set tap0 up
sudo brctl addif virbr0 tap0
sudo chmod 666 /dev/net/tun
```

接着执行ip addr查看virbr0网桥在宿主机中的网段，比如为192.168.122.1/24，后面配置虚拟机网络时候会用到。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7La2ibZ8iaCCTQu4Sr7VFvhgBzK4J6w75BtB8CtgzLGLGtglIo3qO0xbbg/640?wx_fmt=jpeg&from=appmsg)

## **虚拟机网络配置**

根据要复现分析漏洞影响的版本去下载固件，可以在GL-iNet官方安全更新和漏洞仓库里面去找相应版本。

进行仿真模拟的步骤都是一样的，到https://people.debian.org/~gio/dqib/找到Imagesfor armhf-virt的链接下载，这是制作好的镜像，解压后可在readme.txt文件中看到镜像使用信息说明，如qemu-system-arm启动命令、登录方式密码等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LFaUfyq9YW9eaeJbth0UOQQrNibGARnsZuPoBYAdBNGWZJ3PeiaAVT3ibQ/640?wx_fmt=png&from=appmsg)

想要仿真系统和宿主机通信的话，就不能直接使用它的启动命令，可修改下启动配置中的网络部分，改为使用tap网络接口，id为net，名称为tap0。

```
sudo qemu-system-arm -machine 'virt' -cpu 'cortex-a15' -m 1G \
-device virtio-blk-device,drive=hd -drive file=image.qcow2,if=none,id=hd \
-device virtio-net-device,netdev=net -netdev tap,id=net,ifname=tap0,script=no,downscript=no \
-kernel kernel -initrd initrd -nographic \
-append "root=LABEL=rootfs console=ttyAMA0"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LZCkmpELkjNh12Xic7xO3DUPfYGOuFH6y2Dzt5d17Y15FOxk5kZicneCA/640?wx_fmt=png&from=appmsg)

启动后登录进入系统，执行ip addr可以看到网卡名称eth0，再执行命令给eth0网卡分配一个网桥virbr0网段中的ip，刚才我们已经在宿主机看了virbr0网段是192.168.122.1/24。

```
ip add add 192.168.122.130/24 dev eth0
ip link set eth0 up
ip route add default via 192.168.122.1
```

执行后即可和宿主机通信，能互相ping通，每次启动都要执行一遍，嫌麻烦可以把重复操作写成sh脚本。

## **启动配置路由器**

在官网固件下载网站下好固件后，以当前AX1800 Flint最新版v4.6.6为例，使用binwalk -Me提取出squashfs-root文件系统，再在宿主机上使用scp将其传递到仿真虚拟机中，有个坑是提取后文件系统后，如果你想mv、压缩或者scp传输，记得都要加sudo，不然会少关键文件/etc/nginx/oui\_nginx.conf和/etc/nginx/conf.d/gl.conf等，会导致无法启动路由器登录管理页面。

```
sudo scp -r squashfs-root/ root@192.168.122.130:/root
```

接着挂载文件系统并启动shell，以及经过尝试，可以在一个虚拟机上传不同固件版本的suqashfs-root，选择挂载进入的，可以写出不同的sh脚本。

```
cd squashfs-root/
mount -t proc /proc ./proc/
mount -o bind /dev ./dev/
chroot ../squashfs-root/ sh
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7Lnjr0FWeMFoDaEib9N2iakqdz5zp5l7ZyUup39Y4A9N371iaHQxs0nAbqQ/640?wx_fmt=png&from=appmsg)

参考其他文章，加上我自己的摸索，可尝试这些命令来启动路由器，能够在宿主机浏览器中访问192.168.122.130进入路由器管理页面，可完成初始密码设置并登录进入管理面板过程，想实现更多功能的启用就要摸索更多配置了，不过我们分析复现授权相关过程已经够用了。

```
#第一次运行这些
mkdir /var/log
mkdir /var/log/nginx
mkdir /var/lib
mkdir /var/lib/nginx
mkdir /var/lib/nginx/body
mkdir /var/run
chmod +x  /etc/uci-defaults/80_nginx-oui
/etc/uci-defaults/80_nginx-oui
chmod +x /etc/uci-defaults/network_gl
/etc/uci-defaults/network_gl
/etc/init.d/boot boot

#后面重启运行这些即可
/sbin/ubusd &
/usr/sbin/gl-ngx-session &
/usr/bin/fcgiwrap -c 4 -s unix:/var/run/fcgiwrap.socket &
/usr/sbin/nginx -c /etc/nginx/nginx.conf -g 'daemon off;' &
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LsksAfJCNgAUQFjDmJdQIj18HFG3zTpicnf1x32QQ25ns8FribwnvicrAQ/640?wx_fmt=jpeg&from=appmsg)

luac反编译

02

GL-iNet路由器的管理系统是基于luci-nginx-OpenResty开发的，核心功能都是lua写的，在分析过程中发现，lua文件分为源码文件、luac5.1.5文件和luac5.3.5文件三种，碰到后面两种文件就要看下怎么反编译了，自己踩些坑捣鼓了下，算是比较顺利地反编译了。

## **5.1.5**

/usr/lib/oui-httpd/rpc目录下不少luac5.1文件，不过跟我之前碰到的不太一样，文件头中带有路径，不知是不是这个原因，没处理带路径的情况，像metaworm、unluac项目工具都不能反编译成功，最后使用luadec反编译成功了，可能是其编译依赖lua源码缘故。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LdycLpbhicIpiaMaM5WhHHJwtNLicGo1FhuSmzoNlblH6HwQmj9ib8v0LUg/640?wx_fmt=png&from=appmsg)

但luadec也不能直接编译出来用，要先去下载编译会用到的lua源码，放在luadec/lua-5.1目录中，而openwrt项目使用了修改的lua5.1.5的源码，打上openwrt的patches再给luadec编译即可，详情阅读文章反向编译OpenWrt的Lua字节码。要注意的是文章中的patches下载命令失效了，可以手动去openwrt项目仓库下载patches文件，自己打上即可，以及编译出错问题按照文章中给编译命令加上-fPIC即可解决。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LDdnQvdBSxiciaIEOfKbgFAqia8FuR2uMkBRsBvicL3pejVl4EiacHWrvu7A/640?wx_fmt=png&from=appmsg)

## **5.3.5**

部分luac文件看文件头知道是5.3版本，但不知道是哪个小版本，去翻了openwrt项目最新代码，能确定是加入了lua-5.3.5版本，和5.1.5版本共存，在目录utils/lua和utils/lua5.3的Makefile文件中可以看到具体版本。本来想如法炮制，打patches编译lua-5.3.5的luadec，但是碰到了两个坑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LXKC6wW2aXHQYTJ5I3S62wPTGdIzWFYG6mkLGoOjpZKFSxPu1tbkTeA/640?wx_fmt=png&from=appmsg)

先是会报size\_t不对的错误，ida分析编译出来的luadec文件，同时查看lua-5.3.5源码的checkHeader部分，找到问题是因为luadec在ubuntu64编译的，默认编译器是gcc64，校验的size\_t就是8，而GL-iNet固件运行在32位arm，luac文件的size\_t是4，所以校验出错。试下了改gcc32编译但发现出了不少依赖问题不好解决，随后换在Windows上用Visual Studio编译luadec 32位的lua5.3 sln项目，迅速通过编译。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LbkL3taFLc2SguJr5jMxyzibtShJuQlicQK81Qf3kgzrsbMA2MtUEMN6Q/640?wx_fmt=png&from=appmsg)

接着又出现了文件头校验端序的问题，”endianness mismatch in precompiled chunk”,ida分析GL-iNet中luac引擎/usr/lib/liblua5.3.so.0.0.0文件，对比lua5.3.5源码，发现源码先是读了一个Interger类型值判断是否是0x5678，再读一个Number值判断是否等于一个浮点数，而liblua5.3.so.0.0.0中可以看到只读了一个字节是否为1来判断端序，LUAC\_NUM的校验则是直接没有。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LSYIiaB41N177tia9SJ6TA3aV0iaUMysve6qkrdnnshm3SVKekxzp7Ss3Q/640?wx_fmt=png&from=appmsg)

搜了下确定应该是GL-iNet改的，没搜到哪个5.3小版本有这么写。解决办法有两种，一是修改要反编译luac5.3文件头的大端序和浮点数部分，二是修改luadec编译用到的lua5.3.5源码文件头校验部分，后者要省事些。

功能简析

03

## **登录抓包**

想分析登录授权相关的历史漏洞，首先要跟踪理清相关的函数调用链，仿真虚拟机中执行命令行/usr/sbin/gl-ngx-session &，便可进行登录相关功能。接着抓包网络通信请求，注意到有两个/rpc请求，参数是一个json字符串，其中有method字段和params字段，看起来是要点用的方法和参数，先进行/rpc - challenge请求传递参数username获取到salt、alg、nonce，再发送/rpc - login请求传递参数username和hash获取到sid，便是算登陆上了，大概也能猜到hash的生成和输入的密码、rpc - challenge返回参数有关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LRbDwCwI7RD90yzpNawJPsMrBmsOuMrvT3dUIFfHQwfcXfoibeVq2MTw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7LmA5GgIFuxy3ZLFuC0vl5wic3L1k3xCIaKxib5PKW5pnrV1pYH6Iicw0kg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FRrU1JbU56wxf5ic5Kl5f7Lcia4xaCMTibfQ9eBia1EOXdziaYciab78r9jCoXicJxMUzf25KeNhA1931OQ/640?wx_fmt=png&from=ap...