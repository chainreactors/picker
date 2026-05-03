---
title: CTF之内存取证——瞬息万变成为一瞬
url: https://mp.weixin.qq.com/s/TPX7UkJHvL9hQlWqwM7XvQ
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:23:18.542542
---

# CTF之内存取证——瞬息万变成为一瞬

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIwMbz0JmOEF0URtntuMEEdR6zRZ5a0NPtticEVO9kWX5uicTbMT9GmX1sG8vYL5q8a6qRzuldZB3ZOfuSd4Lj8a7ibldPS0jr52pc/0?wx_fmt=jpeg)

# CTF之内存取证——瞬息万变成为一瞬

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、什么是内存取证

内存取证就是通过相关的工具将计算机内存中的数据持久化存储下来，类似于给内存拍了一张快照，通过取证获取到的数据，我们可以在任何时候对某一时刻的内存进行分析而不需要担心内存变化，另外，也可以将内存中瞬息万变的进程信息保留下来，方便安全人员分析恶意程序的逻辑。

# 二、取证工具

## （一）dumpit

DumpIt 是一款绿色免安装的 Windows 内存镜像取证工具，基于 MoonSols 技术开发，能够轻松将系统的完整物理内存镜像 dump 下来，广泛用于后续的调查取证工作。其生成的原始内存转储文件可直接使用 **Volatility** 等工具进行分析，在 CTF 竞赛中也常被用于制作相关题目。该工具兼容 x86 和 x64 架构系统，非常适合部署在 USB 存储设备中以满足快速应急响应的需求。

下载地址： All-In-USB/utilities/DumpIt

## （二）FTK Imager

FTK Imager 是由 AccessData（现 Exterro）开发的一款行业标准级免费取证工具，主要用于以法医可靠的方式预览数据并创建磁盘或内存的精确副本，同时确保不修改原始证据。它支持捕获物理驱动器、逻辑驱动器、内存及页面文件，并能生成 E01、DD、AFF 等多种标准取证镜像格式。该工具具备强大的实时哈希校验功能以确保证据完整性，支持 BitLocker 解密检测及实时数据预览，是数字调查中用于证据获取、挂载和分析的核心利器。

# 三、分析工具

## （一）foremost

Foremost 是一款基于命令行的开源数据恢复与取证工具，核心原理是通过识别文件头、文件尾及内部数据结构来从原始磁盘镜像或物理设备中恢复已删除或隐藏的文件。它默认支持 JPG、PNG、PDF、DOC、ZIP 等 19 种常见格式的扫描与提取，并允许用户通过编辑 `foremost.conf` 配置文件来自定义文件签名以扩展支持范围。作为数字取证和 CTF 竞赛中的常用利器，Foremost 可直接处理由 `dd`、Encase 等生成的镜像文件或物理驱动器，在 Kali Linux 等主流发行版中通常预装或通过 `sudo apt-get install foremost` 命令即可快速部署。

## （二）binwalk

Binwalk 是一款专为嵌入式设备固件分析设计的强大工具，旨在通过 `libmagic` 库及自定义魔数签名（涵盖压缩文件、文件系统、内核镜像等）来扫描二进制镜像文件，从而识别并提取其中嵌入的文件和代码。作为 Kali Linux 的预装工具，它同样支持 Windows 环境，你可以从 **ReFirmLabs 官方 GitHub 仓库** 下载，解压后在目录下运行 `python .\setup.py install` 进行安装，随后即可在 Python Scripts 目录调用该工具对固件进行深度分析与逆向工程。

```
python binwalk [文件路径]
```

下载地址：GitHub - ReFirmLabs/binwalk: Firmware Analysis Tool · GitHub

## （三）Volatility

Volatility 是一款基于 Python 开发的开源内存取证框架，遵循 GNU 通用公共许可证发布，旨在从 RAM 样本中提取数字信息，从而让调查人员能够独立于目标系统深入查看其运行时状态。作为目前最受欢迎的取证工具之一，它拥有极广泛的跨平台支持能力，不仅涵盖 Windows、Linux 和 Mac OS X，甚至支持基于 ARM 处理器的 Android 手机取证，能够直接分析 `.raw`、`.vmem`、`.img`、`.dmg` 等多种格式的内存镜像文件。

### 1、安装

在老版的 Kali Linux 中，你可以直接使用 `apt-get install volatility` 进行快捷安装，或者直接使用其集成的版本；而在其他 Linux 发行版、Windows 或 macOS 系统中，建议通过源码安装或直接下载官网预编译版本。以下是具体的安装步骤：

1. **源码安装：**

* 克隆源码：`git clone https://github.com/volatilityfoundation/volatility.git`
* 进入目录：`cd volatility`
* 安装：`sudo python setup.py install`
* 或者直接运行：`python vol.py`

2. **预编译包安装：**

* 访问官网下载对应版本：https://www.volatilityfoundation.org/releases
* 赋予执行权限：`chmod +x /path/to/volatility`
* （可选）创建软链接以便全局使用：`sudo ln -s /opt/volatility/vol.py /usr/bin/volatility`
* windows版可执行程序
* linux版可执行程序
* Max OS X版可执行程序

### 2、依赖

如果只是使用volatility本体的话，就不需要安装依赖，如果还需要使用某些插件，就需要安装依赖，安装方式如下：

| 库名称 | 描述 | 安装命令 |
| --- | --- | --- |
| distorm3 | 强大的反编译库 | `pip install distorm3` |
| yara | 恶意软件分类工具 | `pip install yara` |
| pycrypto | 加密工具集 (比赛常用) | `pip install pycrypto` |
| PIL (Pillow) | 图片处理库 | `pip install pillow` |
| openpyxl | Excel 文件读写库 | `pip install openpyxl` |
| ujson | 高性能 JSON 解析库 | `pip install ujson` |

> 如果电脑或者虚拟机没有pip2可以自行安装
>
> ```
> wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
> ```
>
> 然后`python get-pip.py`，然后执行pip2进行安装，因比赛用的比较少，测试安装pycrypto即可;这里因为可能要处理图片、excel、json，建议都安装，如果遇到`error: command ‘x86_64-linux-gnu-gcc’ failed with exit status 1`，可使用
>
> ```
> sudo apt-get install build-essential python2-dev libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev
> ```
>
> 进行解决。

### 3、volatility的基本使用

1. 查看 Volatility 已加载的插件列表以及支持的操作系统 Profile。

```
volatility --info
```

2. 分析内存镜像的基本信息（如系统版本、硬件架构、时间等）。

> 输出中的 `Suggested Profile(s)` 字段会提示该镜像最可能的系统版本（例如 `WinXPSP2x86`）。

```
volatility -f mem.vmem imageinfo
```

3. 列出内存中记录的进程信息。

> 如果进程已经结束，`Exit` 列会显示退出的日期和时间。

```
volatility -f mem.vmem --profile=WinXPSP2x86 pslist
```

4. 提取内存中记录的程序执行情况，包括运行次数、最后一次运行时间等信息（基于注册表 `UserAssist` 键值）。

```
volatility -f mem.vmem --profile=WinXPSP2x86 userassist
```

5. 列出缓存在内存中的注册表文件句柄。

```
volatility -f mem.vmem --profile=WinXPSP2x86 hivelist
```

6. 根据 `hivelist` 获取到的虚拟地址，打印指定注册表配置单元的详细数据。

```
volatility -f mem.vmem --profile=WinXPSP2x86 hivedump -o 0xe16aab60
```

7. 直接读取注册表中 SAM 表的信息，用于获取用户账户名。

```
volatility -f mem.vmem --profile=WinXPSP2x86 printkey -K "SAM\Domains\Account\Users\Names"
```

8. 扫描并列出内存中检测到的文件对象。

```
volatility -f mem.vmem --profile=WinXPSP2x86 filescan
```

9. 扫描内存中系统执行过的命令行历史记录。

```
volatility -f mem.vmem --profile=WinXPSP2x86 cmdscan
```

10.扫描网络连接

> **netscan:** 适用于 **Windows Vista 及更高版本** 的系统，用于扫描网络连接和 Sockets 情况。
>
> **connscan:** 适用于较旧系统（如 XP），用于获取网络连接池中的 TCP 连接情况。

```
# Vista 及以上系统
volatility -f mem.vmem --profile=WinXPSP2x86 netscan

# XP 及旧版系统 (TCP 连接池)
volatility -f mem.vmem --profile=WinXPSP2x86 connscan
```

11. 提取内存中的系统密码哈希。

**方式一：自动定位**

```
volatility -f mem.raw --profile=WinXPSP2x86 hashdump
```

**方式二：手动指定地址** 如果自动定位失败，需指定 SYSTEM (`-y`) 和 SAM (`-s`) 的虚拟地址。

```
volatility -f mem.raw --profile=WinXPSP2x86 hashdump -y 0xe10182f8 -s 0xe1492b60
```

12. 将指定进程 ID 的内存数据完整提取到指定目录中，用于后续深入分析。

```
volatility -f mem.vmem --profile=WinXPSP2x86 memdump -p <进程ID> -D <输出目录名>
```

#### 命令总结

##### 通用取证与内存分析

| 插件名称 | 功能描述 |
| --- | --- |
| **imageinfo** | 显示目标镜像的摘要信息（通常用于获取 Profile 和系统时间） |
| **pslist** | 列举系统进程（基于双向链表，**不能**检测隐藏或解链的进程） |
| **psscan** | 扫描内存池查找进程对象，可发现已终止或被 Rootkit 隐藏/解链的进程 |
| **pstree** | 以树状结构查看进程父子关系（**不能**检测隐藏或解链的进程） |
| **memdump** | 提取指定进程的内存转储文件（常配合 `foremost` 分离提取的文件） |
| **filescan** | 扫描内存中所有的文件对象列表 |
| **svcscan** | 扫描 Windows 系统服务 |
| **connscan** | 查看网络连接信息（基于池标签扫描） |
| **netscan** | 查看网络连接（适用于 Vista/2008 及更高版本，功能更强大） |

##### 注册表、凭证与用户行为分析

| 插件名称 | 功能描述 |
| --- | --- |
| **hivelist** | 查看缓存在内存中的注册表配置单元 |
| **hivedump** | 打印出指定注册表配置单元中的所有数据 |
| **printkey** | 获取注册表中特定键的值 |
| **hashdump** | 获取内存中的系统密码哈希 |
| **userassist** | 提取内存中记录的程序运行情况（包括运行次数、最后一次运行时间等） |
| **cmdscan** | 提取内存中保留的 CMD 命令历史记录 |
| **iehistory** | 获取 IE 浏览器的历史记录 |
| **timeliner** | 自动从多个位置收集系统活动信息，最大程度提取内存中的时间线数据 |

##### Linux 取证

| 插件名称 | 功能描述 |
| --- | --- |
| **linux\_pslist** | 列举 Linux 系统进程 |
| **linux\_psaux** | 列举 Linux 系统所有进程的详细信息（包含命令行参数等） |
| **linux\_pstree** | 以树状结构查看 Linux 进程列表 |
| **linux\_lsof** | 查看进程打开的文件列表 |
| **linux\_memmap** | 查看进程的内存映射信息 |
| **linux\_dump\_map** | 将进程的内存映射信息 Dump 出来 |
| **linux\_lsmod** | 查看已载入系统的内核模块（用于检测 Rootkit） |
| **linux\_proc\_maps** | 查看进程细节，包括共享库、内存开始和结束位置等 |
| **linux\_netstat** | 查看 Linux 系统的网络连接情况 |
| **linux\_find\_file** | 查找并提取内存中的可疑文件 |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

书中自有代码来

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

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