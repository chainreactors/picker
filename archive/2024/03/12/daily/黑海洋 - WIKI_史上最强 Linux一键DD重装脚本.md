---
title: 史上最强 Linux一键DD重装脚本
url: https://blog.upx8.com/4100
source: 黑海洋 - WIKI
date: 2024-03-12
fetch_date: 2025-10-04T12:12:34.957000
---

# 史上最强 Linux一键DD重装脚本

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 史上最强 Linux一键DD重装脚本

发布时间:
2024-03-11

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
56179

之前一直主力使用萌咔一键脚本，但最近遇到一个棘手的问题，DD 一台 Oneman 服务器时，由于主 IP 和网关 IP 不在同一个网段，网络掩码看起来也不正常。使用 –ip-addr / –ip-gate / –ip-mask的指定方式也全都报错，无法正常DD。

于是找到“天权璇玑”大佬去年发布的 Linux 一键重装脚本，结果一键无脑顺利解决了这个困难，成功完成了新系统的DD。

下面，就将这个脚本记录一下，以方便其他有需要的朋友。

Github 项目地址：[https://github.com/leitbogioro/Tools](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2xlaXRib2dpb3JvL1Rvb2xz)

这个脚本，除了能解决我上面说的问题，还有很多强大的功能，大家可以移步项目主页详细查看。

**下载前记得更新源，安装 wget 组件，以下命令仅对应原系统**：

```
Debian 系（Debian Kali Ubuntu）：
apt update
apt update install wget -y

红帽系（CentOS AlmaLinux RockyLinux Fedora 等）：
dnf install wget -y

AlpineLinux（需要安装 wget bash 组件，并把系统默认的 shell 从 ash 改成 bash）：
apk update
apk install wget bash
sed -i 's/root:\/bin\/ash/root:\/bin\/bash/g' /etc/passwd
```

**下载并运行脚本**：

```
wget --no-check-certificate -qO InstallNET.sh 'https://raw.githubusercontent.com/leitbogioro/Tools/master/Linux_reinstall/InstallNET.sh' && chmod a+x InstallNET.sh
```

国内机器现在可以从 Gitee 下载：

```
wget --no-check-certificate -qO InstallNET.sh 'https://gitee.com/mb9e8j2/Tools/raw/master/Linux_reinstall/InstallNET.sh' && chmod a+x InstallNET.sh
```

**快速开始**（当且仅当脚本不加 -pwd -port -mirror 等参数时有效，如果加了，必须指定对应系统的发行版版本号！）：

不用再输入使用何种架构（-v 选项已被 -version 替代，且两者都已经被弃用），脚本会自动检测架构、实现 Debian 系和 Redhat 系架构名相互智能转换！

Debian 12（支持 9 至 12）

```
bash InstallNET.sh -debian
```

Kali rolling（支持 rolling/dev/experimental 三个分支，原则上推荐使用 rolling）

```
bash InstallNET.sh -kali
```

Kali 对 ARM64 AMD64 架构的兼容性都 OK，甲骨文 Oracle ARM 机装虽然从原系统重启后安装就黑屏，什么提示都没有，在 VNC 里也无法观测进度并调试，但只要是从面板自带模板或任意其他一键脚本安装的纯净系统中安装过去的，100% 保证能成功，VNC 里看到黑屏别怕，别手欠中途硬重启，不知道 Kali 是什么的，反正你就知道 Kali 是日常、电影电视剧里黑客经常用的，自带很多安全测试工具，贼鸡儿炫酷的一个 Debian 发行版就行。Kali 有三个版本，按激进程度大小排列，分别为 experimental > dev > rolling，普通人不爱折腾的，最好以使用 rolling 为主。

Alpine Linux edge（支持 3.16 至 3.18 和 edge，推荐 edge）

一个超轻量 Linux 发行版，但需要注意的是，Alpine Linux 运行的时候省内存，内存占用仅 80m 左右，但安装时不省，因为它会在内存中完成所有初始化操作，直到最后再全盘写入硬盘，不像 Debian 红帽系启动内核在内存里准备完毕，就开始进行格盘并从镜像源往硬盘上写入文件操作，这就导致安装 Alpine Linux 的内存要求并不低，低于 1GB 内存的机器不要安装，由于 Alpine Linux iPXE 启动文档里仅描述了如何通过 dhcp 或静态从 IPv4 网络启动，所以仅有 IPv6 公网访问的机器也不要安装。双栈机 IPv6 部分会在安装过程中自动配置好。

```
bash InstallNET.sh -alpine
```

CentOS 9 stream（支持 7-9）

```
bash InstallNET.sh -centos
```

AlmaLinux 9（支持 8-9）

```
bash InstallNET.sh -alma
```

RockyLinux 9（支持 8-9）

```
bash InstallNET.sh -rocky
```

Fedora 38（支持 37-38）

```
bash InstallNET.sh -fedora
```

Ubuntu 22.04（支持 20.04 或 22.04）

```
bash InstallNET.sh -ubuntu
```

Windows Server 2022（基于在 AlpineLinux 中介下 dd 实现，支持 BIOS UEFI 不同固件下自动识别对应的 dd 包，支持 Windows 10 Enterprise LTSC, Windows 11 Pro for Workstation 22H2, Windows Server 2012 R2, Windows Server 2016, Windows Server 2019, Windows Server 2022，重装时输入对应系统的数字版本号即可，如果能通过VNC登录系统，可自动进行 IPv4 静态配置和自动扩展系统盘分区，dd 包来自秋水逸冰，再次感谢他的无私奉献）

```
bash InstallNET.sh -windows
```

**除了 Ubuntu 和 Windows，其余发行版 Linux 均支持自选镜像源，脚本内部仅内置官方后备，且能够区分国内或是国外机器，国内机器重装时必要联网获取的配置文件也能连接到我项目的 gitee.com 镜像，确保国内机器晚高峰重装时不会卡住，或是遭受 github.com 被大墙的阻断。**

其他脚本支持重装到的 Linux 系统均支持原生指定全球各地镜像源的方式安装，如果不指定源，脚本会区分国外国内自动为国内 VPS 切换到国内源，避免连接缓慢，如果要手动指定源，输入系统和对应版本后，加参数“-mirror”，如：

```
bash InstallNET.sh -debian 12 -mirror "http://ftp.riken.jp/Linux/debian/debian/"
```

Debian 全世界各国家、地区源列表：

`https://www.debian.org/mirror/list.html`

Kali 全世界各国家、地区源列表：

`https://http.kali.org/README.mirrorlist`

Kali 官方源 https://http.kali.org/ 因为不支持纯 IPv6 访问，所以脚本中默认国外源选用的是美国勃克利学院 https://mirrors.ocf.berkeley.edu/kali/ 的，学术机构，中立放心，同时支持 IPv4 IPv6 访问，带宽大，下载质量良好。

CentOS 7 和 8-stream，全世界各国家、地区源列表：

`https://www.centos.org/download/mirrors/`

CentOS 9-stream 及以后全世界各国家、地区源列表：

`https://admin.fedoraproject.org/mirrormanager/mirrors/CentOS`

AlmaLinux 全世界各国家、地区源列表：

`https://mirrors.almalinux.org/`

RockyLinux 全世界各国家、地区源列表：

`https://mirrors.rockylinux.org/mirrormanager/mirrors`

Fedora 全世界各国家、地区源列表：

`https://admin.fedoraproject.org/mirrormanager/mirrors/Fedora`

**默认密码**如下：

`LeitboGi0ro`

**由于 AlpineLinux 和 Ubuntu 采用明文（未经 openssl 加密过的密文，仅本地变量传输，不会传到其他地方，放心）传递密码参数到配置文件，附加特殊符号可能会导致 sed 处理时出错，所以 AlpineLinux 和 Ubuntu 默认密码统一为 LeitboGi0ro 且暂不支持修改。**

密码若要自定义，可添加 -pwd ‘密码内容’ 修改，密码字段建议前后使用单英文引号（’ ‘）括起来，以免 shell 将双英文引号（” “）中带特殊字符的密码当做命令传递，造成错误，不要设置的过长过复杂，例：

```
-pwd 'xiaoming'
```

特别的是，如果密码中带有英文单引号（’），请一定在该单引号前加 ”’ 做转义，也就是说，以下转义过的字符才和一个单引号等价：

`'\''`

**也就是说，以上符号才等于实际密码中的 ‘ 符号**，比如你密码要设置为：’xiaoming’，那么如下输入才是正确的：

```
-pwd ''\''xiaoming'\'''
```

**如果使用的是默认密码，安装后请立即修改！**

**默认 ssh 端口随原系统**，比如你机器原系统 ssh 为 65432，新装好的系统端口号也为 65432，亦可添加 -port “端口号” 修改，支持全系受支持的 Linux 系统，范围“1-65535”，如果给错或无法确定原系统端口，后备值为：`22`，例：

```
-port "12345"
```

如果想要**强制双网动态**配置，请输入：

```
bash InstallNET.sh -debian 12 --network "dhcp"
```

如果想要**强制双网静态**配置，请输入：

```
bash InstallNET.sh -debian 12 --network "static"
```

目前支持如果有双网卡，每张网卡上带一个 IPv4 或 IPv6 的静态配置，新安装系统中这两张网卡的网络配置都能够自动配好，仅限 Debian/Kali：

![-1](https://cnboy.org/wp-content/uploads/af4ceb01e88cbf0.png "-1")

**为方便拥有多盘独服的朋友，支持新安装 Debian/Kali/CentOS/AlmaLinux/RockyLinux/Fedora 系统中组建软raid，输入 -raid “方法（支持：0 1 5 6 10）” 即可，请根据自己需求选择对应的 raid 方法。**

raid 0, 1 至少需要双盘；

raid 5 至少需要三盘；

raid 6, 10 至少需要四盘。

组建 raid 的硬盘原则上每盘容量应当相等，否则系统总容量会被 raid 中最小容量硬盘所限制，任何硬盘型号、控制器（无论是 vda sda nvme0n1 hda 等）即可，只要容量相等，数量足够，都能成功组建对应的 raid 阵列且没有空间被浪费。

```
bash InstallNET.sh -debian 12 -raid "0"
```

-setdisk “硬盘名或 all”，支持将系统安装到某块硬盘上，如 vdb sdc 等，输入纯硬盘名即可；也可以设置成“all”，除了将系统安装在默认第一块可读写硬盘中，也可以将其他硬盘空间擦除。此参数和 -raid 冲突，请不要两者都给。

```
bash InstallNET.sh -debian 12 -setdisk "all"
```

```
bash InstallNET.sh -debian 12 -setdisk "vda"
```

如果想要纯手动模式安装，比如用于调试等，请输入（要求必须能用 VNC 访问机器），不支持 AlpineLinux Ubuntu：

```
bash InstallNET.sh -debian 12 --allbymyself
```

如果想要使用 netbootxyz 纯手动模式安装其受支持的系统，比如 Archlinux 等，请输入（**不推荐**，要求必须能用 VNC 访问机器，仅 x86\_64 AMD64 架构，BIOS 固件机器使用，甲骨文 UEFI 固件机器用 netbootxyz 启动，请参考此教程：https://zhuanlan.zhihu.com/p/97527349）：

```
bash InstallNET.sh -netbootxyz
```

现在开启了一个参数，–setipv6 “0 “，指定强制关闭系统安装时加载 IPv6 模块，设置为 0 就是关闭，指定其他值或不指定为加载 IPv6 模块。不管机器实际是否有 IPv6 网络，只要设置 –setipv6 “0”，新系统里 IPv6 模块就会被彻底禁用，无法访问 IPv6 网络，请按照实际情况选择，对部分 Racknerd 和 Virmach 等商家的纯 IPv4 机器有效，因为这些商家的纯 IPv4 机器也会被 dhcp 分配到一个公共 IPv6 地址，且 DNS 解析外部网站域名，会强制返回它们的 IPv6 地址，然而机器没有 IPv6 网络，导致 ping wget curl 等网络连接工具会因持续试图连接 IPv6 地址而失败，强制新系统里不加载 IPv6 模块可解决此问题。但这样会导致 Nginx 里带加载 IPv6 网络的模块失败导致启动失败，请自行到 /etc/nginx/nginx.conf 目录里把

`# listen [::]:80 default_server;`

Racknerd Virmach 纯 IPv4 机型安装时不指定 –setipv6 “0” 的后果，wget 总是优先连接 IPv6，当失败数次后才使用 IPv4 连接，造成过长的连接等待。

![-2](https://cnboy.org/wp-content/uploads/9fd477c91d93d12.png "-2")

注释掉，该选项适用于除 AlpineLinux 以外的全部 Linux 发行版

```
bash InstallNET.sh -debian 12 --setipv6 "0"
```

现开启了一个参数：**–nomemcheck ，输入后即跳过内存容量检测，你可以在任何内存的机器上尝试安装目标系统**，即使能在当前系统成功下载并打包网络安装启动内核，**但不保证重启后能安装成功。**

```
bash InstallNET.sh -debian 12 --nomemcheck
```

**如何使用本脚本从 Linux dd 到 Windows？**

1. 任意基于 KVM QEMU 或 XEN 的机器，不管机器原系统是 Debian 系还是 Redhat 系，grub 引导菜单都能成功写入并重启后被启动：

```
bash InstallNET.sh -dd 'DD 镜像链接'
```

2. 某些支持多种启动方式，如救援模式，正常模式等的独服，如 Kimsufi 等：

将启动模式转换为救援模式，从邮箱里获取登陆账户密码，进入救援模式临时系统，执行：

```
wget -O- 'DD 镜像链接' | xzcat | dd of=/dev/sda
```

等待 dd 镜像下载并解压好，将启动模式改为正常模式，输入重启命令，等待被 dd 的 Windows 系统初始化完成。

```
reboot
```

**如何设置 swap 文件系统**

默认不带 swap ，需要的话可以装好系统自己加，768 MB 以下机型因为完全不给 swap 会导致安装崩溃，所以还是会至少分配 512 MB，原生安装的红帽系也至少需要 512 MB swap ，可以指定 -swap “数字，以 MB 为单位” 预置，比如 -swap “1024” ，提前设置 1GB swap 。

```
bash InstallNET.sh -swap "1024"
```

UEFI 固件强制 gpt 分区，BIOS 固件 2TB 以下硬盘默认 mbr 分区，如果想在 BIOS 环境强制 gpt 分区，可指定 -partition “gpt” 。

```
bash InstallNET.sh -partition "gpt"
```

文件系统方面，Debian/Kali 默认 ext4 ，CentOS/AlmaLinux/RockyLinux/Fedora 默认 xfs 且不可更改。如果想在 Debian/Kali 上使用 xfs ，可以指定：

```
bash InstallNET.sh -filesystem "xfs"
```

最后，让我们看看这个脚本的界面演示吧：

![-1](https://cnboy.org/wp-content/uploads/c4ca4238a0b9238-10.png "-1")

![-2](https://cnboy.org/wp-content/uploads/c81e728d9d4c2f6-10.png "-2")

![-3](https://cnboy.org/wp-content/uploads/eccbc87e4b5ce2f-18.png "-3")

![-4](https://cnboy.org/wp-content/uploads/a87ff679a2f3e71-13.png "-4")

![-5](https://cnboy.org/wp-content/uploads/e4da3b7fbbce234-5.png "-...