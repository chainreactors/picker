---
title: 最后防线：osquery功能与实现
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488164&idx=1&sn=17fad9b3d5578456128c0ef0f42f2d8f&chksm=fdf979b1ca8ef0a77278533ed0857d394bcd99120b2b9b1b32703a41a067d5de0b4620c464f5&scene=58&subscene=0#rd
source: debugeeker
date: 2023-02-05
fetch_date: 2025-10-04T05:45:40.504216
---

# 最后防线：osquery功能与实现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbzx2JmFfticn2goY7zIzPRUbibouIOtbXo40hJy6uFmPFkAFzK2HwtCaGuasrPNNuOQVBicU8BlE5saQ/0?wx_fmt=jpeg)

# 最后防线：osquery功能与实现

原创

debugeeker

奶牛安全

# osquery功能与实现

> 开源HIDS osquery的主机监控功能和实现原理。
> osquery代码链接：osquery
> osquery表结构：表结构
> 本文是在安装它之后，从osqueryi中的表再调研代码来获取它的实现

## 设备基线

> 对系统使用的设备建立基线，从而发现故障的设备，用于IDC机房。
> **不足之处**：这些功能用于传统机房。对于云时代并不适用

| 功能 | 实现原理 |
| --- | --- |
| acpi设备 | 读取`/sys/firmware/acpi/tables`目录 |
| 块设备 | 通过调用`udev`库API读取 |
| 设备信息（设备文件，指纹，分区） | 通过sleuthkit第三方库读取 |
| 硬件事件 | 通过读取`udev`事件 |
| intel mei信息 | 通过读取`/dev/mei0` |
| RAID信息(设备，特性，驱动) | 读取`/proc/mdstat` |
| 固件信息(内存阵列和地址映射，内存设备和地址映射，故障信息，`OEM`特征，`SMBIOS`)，设备平台信息 | 读取`/sys/firmware/dmi/tables/DMI`， `/sys/firmware/efi/systab` |
| PCI设备 | 读取`/usr/share/misc/pci.ids`， `/usr/share/hwdata/pci.ids`，`/usr/share/pci.ids` |
| 智能卡信息 | 通过`smartmontools`库获取 |
| USB信息 | 通过`udev`库读取 |
| IO设备的内存映射 | 读取/proc/iomem |

## 系统基线

> 建立系统基线，获取系统基本信息，如CPU，内存，磁盘，分区，内核版本，加载的模块，系统运行时长，内存控制参数，系统限制，属于哪个发行版
> **不足之处**：
>
> 1. 获取cpu寄存器列表和MSR没多少意义。除非环境需要用到一些高能计算
> 2. 共享内存信息意义不大
> 3. 内核信息获取不够，还需要读取`/boot`，
> 4. 内核模块获取不够，还需要读取`/lib/modules`的内容，确保哪些是系统加载，哪些是手动加载
> 5. 自启动项，不应该读取`/etc/init.d`，而是读取`/etc/rc.d/`, 或者支持systemd
> 6. 加载分区，还得读取一下`/etc/fstab`，确保哪些分区是系统默认加载，哪些是其它操作加载的

| 功能 | 实现原理 |
| --- | --- |
| cpu运行状态 | 读取`/proc/stat` |
| cpu寄存器列表 | 通过内联汇编读取cpu信息 |
| cpu msr信息 | 读取`/dev/cpu/<id>/msr` |
| 内存信息 | 读取`/proc/meminfo` |
| 共享内存信息 | 通过`shmctl`等API获取 |
| 磁盘加密 | 使用`cryptsetupy`库来获取磁盘加密情况 |
| 加载的分区 | 读取`/proc/mounts` |
| 内核信息 | 通过读取`/proc/cmdline`, `/proc/version` |
| 内核模块 | 通过读取`/proc/modules` |
| 系统时间 | 获取当前时间 |
| 系统启动时长 | 调用`sysinfo` |
| 系统信息(cpu个数，机器名，配置) | 读取`/proc/cpuinfo`, `/etc/hostname`和调用`sysconf`等API |
| 系统控制配置 | 读取`/etc/sysctl.conf`, `/run/sysctl.d`, `/etc/sysctl.d`,`/usr/local/lib/sysctl.d`, `/usr/lib/sysctl.d`, `/lib/sysctl.d` |
| 系统限制 | 调用`getrlimit`获取 |
| 发行版及版本 | 读取`/etc/os-release`, `/etc/redhat-release`, `/etc/gentoo-release` |
| 自启动项 | 读取`/etc/xdg/autostart/`, `/etc/init.d/` |
| 系统负载 | 通过调用`getloadavage`的接口来获取 |

## 供应链基线

> 目前很多Linux系统安装更新软件都是通过网络安装，如果是从恶意源安装软件，就会导致安装问题
> **不足之处**：
>
> 1. 没有把主流的Linux发行版的源包括在里面，如arch, gentoo之类，只是有centos和debian/ubuntu
> 2. 没有对pip, npm之类的源建立基线
> 3. 对于编辑器的一些源也没有建立基线

| 功能 | 实现原理 |
| --- | --- |
| apt源 | 读取`/etc/apt/sources.list`文件， `/etc/apt/sources.list.d`目录，`/var/lib/apt/lists/`缓存目录 |
| yum源 | 通过读取`/etc/yum.repos.d`下的`repo`文件 |

## 软件基线

> 获取所有安装的软件名称，版本，建立软件包管理的基线，检测恶意软件和漏洞
> **不足之处**：
>
> 1. 包管理软件可能由于发行版不同，版本不同，需要有不同的信息采集方式
> 2. 没有arch的软件包管理
> 3. python包管理没有包括通过`virtualenv`方式安装的包

| 功能 | 实现原理 |
| --- | --- |
| atom编辑器插件列表 | 读取每个用户主目录`.atom/packages`下的所有`package.json` |
| deb包列表 | 读取`/var/lib/dpkg` |
| npm包信息 | 读取`/usr/lib/`,**用户主目录**的`node_modules`下面`package.json` |
| gentoo包管理portage(关键字，列表，编译配置) | 读取`/etc/portage/package.keyword`s，`/etc/portage/package.mask`，`/etc/portage/package.unmask`,`/var/db/pkg`，`/var/lib/portage/world` |
| python包管理 | 读取`/usr/local/lib/python/dist-package`, `/usr/local/lib/python/site-packages`, `/usr/lib/python/dist-packages`, `/usr/lib/python/site-packages`, `/Library/Python/*/site-packages` |
| rpm包管理 | 调用`rpmlib`库获取信息 |

## 配置基线

> 对系统配置建立基线，从而发现恶意篡改或不当配置的风险
> **不足之处**：
>
> 1. 对`/etc/ld.so.conf`, `/etc/ld.so.conf.d/`没有监控，无法发现恶意软件注入的风险
> 2. 对`/etc/default`没有监控，无法发现软件默认配置的缺陷
> 3. 对`/etc/sysconfig`没有监控，无法发现网络，路由，防火墙和一些基本服务的配置缺陷
> 4. 对`/etc/security`, `/etc/login.defs`没有监控，对用户管理，登录管理的默认限制进行采集
> 5. 对`/etc/fstab`没有采集，无法发现是否默认加载NFS或分区加载选项错误
> 6. 对`/etc/shells`没有监控，无法发现系统配置多少shell给用户登录
> 7. 监控了一些小众的软件配置，对web服务，DB服务，MQ服务的配置却没有监控

| 功能 | 实现原理 |
| --- | --- |
| augeas(某配置平台) | 读取`/usr/share/osquery/lenses`目录 |
| 主机列表 | 读取`/etc/hosts` |
| 协议列表 | 读取`/etc/protocol` |
| 服务端口映射表 | 读取`/etc/services` |
| prometheus(另一个监控软件)配置 | 读取genPrometheus的配置文件 |

## 用户基线

> 建立用户基线，获取用户列表，组列表，权限列表，登录记录和操作记录，登录软件的配置
> **不足之处**：
>
> 1. 使用audit，可能会带来性能影响

| 功能 | 实现原理 |
| --- | --- |
| authorized  keys | 读取**用户主目录**`.ssh/authorized_keys`和`.ssh/authorized_keys2`文件 |
| ssh配置 | 读取`/etc/ssh/ssh_config`，用户主目录`.ssh/config` |
| 已知主机 | 通过读取用户主目录的`.ssh/known_hosts` |
| 用户ssh密钥 | 读取用户主目录下的`.ssh` |
| 用户列表 | 通过调用`getpwnam`等API获取 |
| shadow列表 | 通过`getspnam`等API获取 |
| 组信息 | 通过getgrent等API获取组信息 |
| 用户组 | 通过getpwent等API获取 |
| sudo权限 | 读取`/etc/sudoers` |
| 当前登录用户 | 通过`getutxent`接口获取 |
| 用户登录记录 | 通过调用`getutxent`之类API获取 |
| 命令历史 | 通过读取用户主目录的`.bash_history`, `.zsh_history`, `.zhistory`, `.history`, `.sh_history`, `.bash_sessions`下的`\*.history` |
| 用户事件 | 通过`audit`事件获取 |

## 网络基线

> 收集各种网络信息，建立网络基线，可用于发现高危端口，外连行为，arp污染，DNS劫持，资产发现

| 功能 | 实现原理 |
| --- | --- |
| 网卡详细信息(列表，ipv4地址，ipv6地址) | 通过`getifaddrs API`获取网卡信息 |
| arp缓存 | 读取`/proc/net/arp` |
| 路由信息 | 通过`netlink`获得路由信息 |
| iptables规则 | 通过`libiptc`库来获取iptables规则 |
| dns信息 | 使用`resolv API`获取dns信息 |
| socket监控 | 通过读取`audit`事件 |
| 端口监听 | 通过查看每个进程的`/proc/<pid>/fd`, `/proc/<pid>/net/tcp`,`/proc/<pid>/net/tcp6`, `/proc/<pid>/net/unix` |
| BPF socket监控 | 通过第三方库`tob:ebpfpub`来获取 |
| 链路发现协议(LLDP)邻居 | 通过调用`lldpctl`的库来实现主机发现 |
| curl证书 | 通过curl证书来确定证书有效期 |
| curl信息 | 通过curl进行服务发现 |

## 服务基线

> 对系统服务建立基线，以期发现恶意服务
> **不足之处**
>
> 1. 不支持systemd
> 2. 不支持`/etc/init.d`

| 功能 | 实现原理 |
| --- | --- |
| crontab定时任务 | 读取`/etc/crontab`, `/etc/crontab.d`, `/var/spool/cron`, `/var/spool/cron/crontabs`下的内容 |

## 浏览器基线

> 建立浏览器插件基线，防止信息被窃取
> **不足之处**：
>
> 1. 兼容性问题，不同版本，插件信息目录可能不一样

| 功能 | 实现原理 |
| --- | --- |
| chrome插件，chrome插件内容脚本 | 通过用户目录chrome数据插件 |
| firefox插件 | 读取用户主目录`mozilla/firefox/extensions.json` |
| opera插件 | 检测用户主目录下`config/opera/Extensions` |

## 云基线

> 对云服务建立基线，在现在混合云的环境，可以更好地监控云环境。
> **不足之处**：
>
> 1. 对腾讯云，阿里云，华为云，天翼云之类没有支持
> 2. 对AWS, Azure云的实例支持也不多

| 功能 | 实现原理 |
| --- | --- |
| azure实例(元数据，标签) | 连接到azure服务读取 |
| carbon black云原生 | 读取`/var/lib/cb/sensor.id`，`/var/lib/cb/sensorsettings.ini` |
| AWS EC2服务(元数据，标签) | 连接AWS服务获取 |

## 进程基线

> 对进程建立基线，检测恶意进程和恶意执行文件
> **不足之处**：
>
> 1. 对于docker启动的进程，没有建立`docker<->process`的从属关系
> 2. 对于系统服务启动的里程，也没有建立`service<--->process`的从属关系
> 3. 对于进程执行文件和库文件，都没有取md5，无法检测恶意篡改的风险
> 4. 读取`/proc/<pid>`的方式，无法检测隐藏进程
> 5. 没有采集进程的线程数目
> 6. 没有采集进程本身的资源限制
> 7. 使用eBPF和audit会对生产环境有性能影响

| 功能 | 实现原理 |
| --- | --- |
| 进程列表 | 读取`/proc/<pid>` |
| 进程环境变量 | 读取`/proc/<pid>/environ` |
| 进程命名空间 | 读取`/proc/<pid>/ns`目录 |
| 进程内存映射 | 读取`/proc/<pid>/maps` |
| 进程的句柄(打开文件，socket，管道) | 读取`/proc/<pid>/fd`目录 |
| 进程事件 | 读取audit日志 |
| BPF进程监控 | 通过第三方库tob:ebpfpub来获取 |

## 文件基线

> 建立文件基线，获取文件指纹，文件类型，执行文件和库的结构及文件变动，以期发现恶意文件，恶意文件伪装，恶意篡改
> **不足之处**：
>
> 1. 这些操作非常耗时，对IO消耗很大，会对系统性能有影响。
> 2. 文件capabilities的信息非常鸡肋，应用场景非常有限

| 功能 | 实现原理 |
| --- | --- |
| 文件元数据 | 通过stat读取宿主机和容器的文件元数据 |
| 文件capabilities信息 | 读取文件的`capabilities`属性 |
| 文件类型（magic) | 使用`libmagic`库 |
| 文件指纹 | 对文件进行hash, 取`md5,sha256, sha512` |
| ELF文件(执行和库) | 使用libelfin库读取elf文件，读取elf头部，`segment`, `section`, `dynamic segment` |
| 文件变动 | 通过inotify监控文件变动 |

## 容器基线

> 建立容器的基线，避免出现容器打开高危端口，或者容器成为横向移动跳板，或者“超级docker“导致逃避控制宿主机的情况。
> Docker的采集方式都是通过restful接口。
> **不足之处**：
>
> 1. 获取docker各种信息都通过连接dockerd的unix socket，从而会自动启动dockerd服务，这个服务会启动那些自启动的docker容器，从而抢占系统资源

| 功能 | 实现原理 |
| --- | --- |
| docker信息 | 使用`/info` |
| docker镜像(列表,层，标签) | 使用`/images/json` |
| docker卷(列表，标签) | 使用`/volumes` |
| docker网络(列表，标签) | 使用`/networks` |
| docker容器(列表,标签,网络,端口,加载分区) | 使用`/containers/json` |
| docker容器状态 | 使用`/containers/<id>/stats` |
| docker容器进程列表 | 使用`/containers/<id>/top` |
| docker容器文件变动 | 使用`/containers/<id>/changes` |
| lxd(linux containers，另一种容器) | 也是通过restful接口来取各种数据，由于用得少，忽略 |

## 安全基线

> 对一些系统安全类的监控服务的配置和事件建立基线，以期发现异常事件
> **不足之处**：
>
> 1. 会对系统性能会有冲击

| 功能 | 实现原理 |
| --- | --- |
| apparmor配置 | 读取`/sys/kernel/security/apparmor/policy/profiles`目录 |
| apparmor事件 | 通过netlink读取audit事件 |
| selinux配置 | 读取加载的selinuxfs文件系统,根据里面的路径来获取配置 |
| selinux事件 | 读取audit事件 |
| yara规则 | 通过调用yara的API获取配置 |
| yara事件 | 通过调用audit的事件，对事件涉及的文件通过yara规则检测 |
| suid执行文件权限 | 读取`/bin`, `/sbin/`, `/usr/bin`,`/usr/sbin`, `/usr/local/bin`, `/usr/local/sbin/`, `/tmp` |

## 系统日志

> 获取系统日志。上面的基线和监控都是基于程序行为，但对程序内部产生的事件，往往是没有的，需要加上对系统日志的采集，从而获得各种服务或程序运行时出现的事件
> **不足之处**：
>
> 1. syslog实现方式有问题，应该是通过读取`/dev/log`

...