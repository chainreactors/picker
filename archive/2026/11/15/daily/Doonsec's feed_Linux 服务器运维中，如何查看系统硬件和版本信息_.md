---
title: Linux 服务器运维中，如何查看系统硬件和版本信息?
url: https://mp.weixin.qq.com/s/n6sJ0rr1-QxKqyJ7-prULA
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:46:35.397489
---

# Linux 服务器运维中，如何查看系统硬件和版本信息?

# Linux 服务器运维中，如何查看系统硬件和版本信息?

原创

圈圈
圈圈

网络技术干货圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

在 Linux 服务器运维中，查看系统硬件和版本信息是日常巡检、故障排查、服务器验收时经常用到的操作。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ic1a3mDpNicpk9H7TvIt6xhGsEherwpAX8XgAONvDwlD57GIfNouiapFhWjTK9mexprkRTIXic2Yz9NNNVjU2lwdV6uYd7icdiaHtTM/640?wx_fmt=png&from=appmsg)

下面整理了一份常用命令清单，基本覆盖 系统版本、CPU、内存、磁盘、主板、网卡及内核信息。

## 一、查看 Linux 系统版本

1. 查看发行版信息

```
cat /etc/os-release
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ibqichfnImrq3oxwrMCY02BWibxLOpup7K7mm8XichnuJ4vSuticiaw50rH9N8iboo0sgYJSAlCFHlkUibVWOfZaibxBfYuWJHA34RPqvM/640?wx_fmt=png&from=appmsg)

适用于大多数主流 Linux 发行版，例如 Ubuntu、Debian、CentOS、Rocky Linux、openEuler 等。

2. 查看系统详细信息

```
hostnamectl
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5icXzIQRkquRNVrcqjRGSzFuBwW1PwR4IN4Qtu2iaUAiahl0P7egGcA8FD5pcQalqb7ViabYjPPc32tjiaI1qsW5PydbHHsaYHYXzh4/640?wx_fmt=png&from=appmsg)

可以查看主机名、操作系统、内核版本、系统架构等信息。

3. 查看内核版本

```
uname -r
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S58RjbxRg8B1aJen5RMuZAZ61R8Ae4ceJsZiadqSz3ESmWXsqjp3HQo5Hdu909YDvp8nKQQDf2DsyD0FdmSNlicicwr9BTZkbhL1QQ/640?wx_fmt=png&from=appmsg)

查看完整内核信息：

```
uname -a
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5icqMTLHRJDtyiadaEicRTwIhvYZoP0ia0WkGxVO76HsNXvLS1pn64O03b1eNCZrGcoC3jAz3XbXTnZM5pwfaCyYs2qOTULKjCWubM/640?wx_fmt=png&from=appmsg)

4. 查看系统架构

```
uname -m
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S588ic2D4fdQnboadBc5CLb6zpBiaRuQWObbFRJa1YKwv7IZg4S5BQEe5TiaGuicfBzk0gnCibIK6G7njcGDRKmBHqAB5KWYW38kRmuw/640?wx_fmt=png&from=appmsg)

常见结果：

| 输出 | 含义 |
| --- | --- |
| x86\_64 | 64 位 x86 架构 |
| aarch64 | 64 位 ARM 架构 |
| i686 | 32 位 x86 架构 |

## 二、查看 CPU 信息

1. 查看 CPU 详细信息

```
lscpu
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5icicKYHuvSb50lJibfWnaHm4A1Ynq1XU6XG8VUeVebjDia6H7mYzUhiascyvMic9uWJWomRZYGKjOAQfMqXqtS34IDkiaWdgxM4ey4WU/640?wx_fmt=png&from=appmsg)

重点关注：

* Architecture：CPU 架构
* CPU(s)：逻辑 CPU 数量
* Thread(s) per core：每个核心的线程数
* Core(s) per socket：每颗 CPU 的核心数
* Socket(s)：物理 CPU 插槽数量
* Model name：CPU 型号

2. 查看 CPU 型号

```
cat /proc/cpuinfo | grep "model name" | head -n 1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S580UtuDqgsUPK09X8EIp8XEGicJ5cHcVcUsWHdqSeyWvibf864L6ckAcPEbYyoboibRppx5N4yUG5h9LnCEn3ibOtiaqYoywP4lgajc/640?wx_fmt=png&from=appmsg)

3. 查看 CPU 核心数量

```
nproc
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S59j8NPsicI6epic1eGyicqOD8GvEXyLr0lribOR7m1hD9031WhUBibWdCicoXyfxTSAM9KDyHfIC9saaibJXegqlSwaZQFfHKiaAiaKvibicg/640?wx_fmt=png&from=appmsg)

查看逻辑 CPU 数量。注意，它不一定等于物理核心数量。

## 三、查看内存信息

1. 查看内存使用情况

```
free -h
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5icIcdMOQkzrjAicaUzRmsBOM3eofMicb6tGR04xiaAI5xujibgLZA6j12iaoCZ3EJ9jQErYHdwbRZ99Egjdjy6uLuKP4pzLXOwmOQzE/640?wx_fmt=png&from=appmsg)

可以查看总内存、已使用内存、可用内存及 Swap 交换分区。

2. 查看内存条硬件信息

```
sudo dmidecode -t memory
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ibJGvjBHqZaic0Siacv66MKdh1ynT3aEbvM4lcgtMiaHYTciclq1BWy3ibTAic06OZSCibHictBDvga1gB42vSttrnuyDS7FiaMkzOqtpAc/640?wx_fmt=png&from=appmsg)

可以查看内存插槽、内存容量、频率、类型等信息。部分虚拟机可能无法获取完整数据。

3. 查看内存详细信息

```
cat /proc/meminfo
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ib7lTticN9yia7PhcicB0XgmL4vrgxFg3iafdMBqUiahWnxUTkTVXvW8zeqygossq2sXVoBNCqBwpCYd4666O9ush6CCz6S6RngvAAY/640?wx_fmt=png&from=appmsg)

适合进一步分析内存使用情况。

## 四、查看磁盘和文件系统

1. 查看磁盘设备

```
lsblk
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S58wicQDf9V0zNPgsy3cLyZvCut7DNFL0SUDEm5s3QqPXwAW9COxeCIWrno6hynicdS6NHflrw16Kz1SGfwHJSickBe7kduIeGV4lQ/640?wx_fmt=png&from=appmsg)

查看磁盘、分区、挂载点及设备层级关系。

2. 查看磁盘分区

```
sudo fdisk -l
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5icoNol31DrBzeGA3lgWf9T7OZNTwNKsPYN7Uz8LU3BPH5YsO8Omu3OacMeNYvZSgHvVhpW8lT8h9IA8RO3soKibpibehsibCbicY3M/640?wx_fmt=png&from=appmsg)

查看磁盘容量、分区表和分区信息。

3. 查看文件系统使用情况

```
df -hT
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5iblJ4TVibkG3uMfoRwjCHBxHZlFmaJjEHqBo3XLYr0ahCvZwWFsSicy8wVoPCPDlXIX2ze1tZwhed4iaL76zbnw0HDFrIoUjXR1kQ/640?wx_fmt=png&from=appmsg)

可以同时查看挂载点、文件系统类型、总容量和使用率。

4. 查看磁盘型号和序列号

```
sudo smartctl -i /dev/sda
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5icric6H1icqoJ2BQRWK8SSqewsH3ME35WCu9B8LU3xia6RxnS1a3VvpnibUTNklFu850MR5mFicXeBKl6oUyeuk5Z2J6AqhasoicQkfM/640?wx_fmt=png&from=appmsg)

需要安装 `smartmontools`，并且磁盘及控制器应支持相应信息读取。

## 五、查看主板和硬件设备

1. 查看主板信息

```
sudo dmidecode -t baseboard
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ibrAlWticmcvnhV5gxKniaNPjZunPqXXcu32RrRiaTsmGoPXM1TRHuu6o56QH6oiafia2jyQ8Ss364T8qQOVnm4jwTxVo7Spf36utCM/640?wx_fmt=png&from=appmsg)

2. 查看 BIOS 信息

```
sudo dmidecode -t bios
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5892E0jPYnjnrLlgrvhiblfianNf7eM5DpOqjYYasfbwE60oSGOOS99njdvibdIw0ju8eQ9ichxOmkkaBqX0OezjRULQHPAg8tOn70/640?wx_fmt=png&from=appmsg)

3. 查看服务器厂商和型号

```
sudo dmidecode -t system
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S58VJAoic6U4VWSTyric8EbA0Y3agFQJQUKoictibX68MukwoMrm3WnULVq0nOWNgiaj8kXiaFSWMMiaf5Y4D2KNMqGJHnj88B4gLNnAdw/640?wx_fmt=png&from=appmsg)

4. 查看 PCI 设备

```
lspci
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ibqe7RoIAibdxALTeqToUhBfO3ibHSjOcD8zDP702AukJOuhOZn0XBzcMDCtZohiauEQC8tcjkrwGK09TWKn7b5CZcFVrwr63sEE0/640?wx_fmt=png&from=appmsg)

查看网卡、显卡、RAID 控制器及其他 PCI 设备。

## 六、查看网卡信息

1. 查看网卡及 IP 地址

```
ip addr
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ibAQGccqKxkvSrsSYG0LVlf7ZWxho8YnmnMrKWiac89f32svInJicUdy2VsFRg6UnGILsz3pfafr58lXARRFxkYer26VDGZlvdcY/640?wx_fmt=png&from=appmsg)

也可以使用：

```
ip a
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ibaZbg27wt5jPMnSX63ptb1ftDbdXcTqnibcl3yCrk6J8gjWUoGlf7CYZb6UVeHYZlXSSjG0CH5armSLdcicp8f2sTxXI1Fp0bQI/640?wx_fmt=png&from=appmsg)

2. 查看网卡硬件信息

```
sudo lshw -class network
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5iciaiaibGJagG4kxtticjCtFZNY1Ap3b30rQtauxH0NGI2oaa3afADutln9T3rMhzHbnqKws8qLeYg8BDYK2fGibiczco4a4HrHzXnXM/640?wx_fmt=png&from=appmsg)

可以查看网卡型号、驱动、总线信息等。需要安装 `lshw`。

3. 查看网卡速率

```
sudo ethtool eth0
```

其中 `eth0` 替换为实际网卡名称，重点关注 `Speed`、`Duplex` 和 `Link detected`。

## 七、常用命令速查表

| 查看内容 | 命令 |
| --- | --- |
| 系统发行版 | `cat /etc/os-release` |
| 系统详细信息 | `hostnamectl` |
| 内核版本 | `uname -r` |
| 系统架构 | `uname -m` |
| CPU 信息 | `lscpu` |
| CPU 数量 | `nproc` |
| 内存使用情况 | `free -h` |
| 内存条信息 | `dmidecode -t memory` |
| 磁盘设备 | `lsblk` |
| 磁盘分区 | `fdisk -l` |
| 文件系统容量 | `df -hT` |
| 主板信息 | `dmidecode -t baseboard` |
| BIOS 信息 | `dmidecode -t bios` |
| PCI 硬件设备 | `lspci` |
| 网卡 IP 信息 | `ip addr` |
| 网卡速率 | `ethtool eth0` |

## 八、一次性查看服务器基本信息

实际巡检时，不需要每条命令单独执行，可以使用下面这段脚本：

```
#!/bin/bash

echo "========== 系统版本 =========="
cat /etc/os-release | grep -E 'PRETTY_NAME|VERSION_ID'

echo -e "\n========== 内核版本 =========="
uname -r

echo -e "\n========== 系统架构 =========="
uname -m

echo -e "\n========== CPU 信息 =========="
lscpu | grep -E 'Model name|Socket|Core|Thread|CPU\(s\)'

echo -e "\n========== 内存信息 =========="
free -h

echo -e "\n========== 磁盘信息 =========="
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT

echo -e "\n========== 文件系统 =========="
df -hT

echo -e "\n========== 网卡信息 =========="
ip -br addr

echo -e "\n========== 主机名 =========="
hostname
```

保存为 `system_info.sh`，执行：

```
chmod +x system_info.sh
sudo ./system_info.sh
```

说明：部分硬件信息命令需要 root 权限；精简系统或虚拟机环境可能没有安装相应工具，或者无法读取完整硬件信息。

运维建议： 日常巡检优先掌握 `hostnamectl`、`uname`、`lscpu`、`free`、`lsblk`、`df`、`ip` 这七类命令。它们基本能帮助你快速摸清一台 Linux 服务器的系统版本、硬件配置和资源使用情况。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过