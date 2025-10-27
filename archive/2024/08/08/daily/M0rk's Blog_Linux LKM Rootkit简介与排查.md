---
title: Linux LKM Rootkit简介与排查
url: http://kevien.github.io/2024/08/07/Linux-LKM-Rootkit%E7%AE%80%E4%BB%8B%E4%B8%8E%E6%8E%92%E6%9F%A5/
source: M0rk's Blog
date: 2024-08-08
fetch_date: 2025-10-06T17:59:20.056386
---

# Linux LKM Rootkit简介与排查

[M0rk's Blog](/)

#

* [首页](/)
* [归档](/archives)
* [标签](/tags)
* [关于](/about)
* [站点地图](/sitemap.xml)
* 搜索

## Linux LKM Rootkit简介与排查

发表于

2024-08-07

|

字数统计

|

阅读时长

![](/2024/08/07/Linux-LKM-Rootkit简介与排查/1.png)
<https://xz.aliyun.com/t/14548> （记录某次”有趣的”挖矿木马排查），这篇关于应急的文章写的不错，排查点基本上都排查到了，感觉就是差了个在入侵时间点范围内被修改过的文件这个角度去排查，但瑕不掩瑜，整个文章的亮点还是比较多，尤其是LKM的发现，之前没对LKM什么了解，遂简单学习了下。

Loadable Kernel Modules (LKMs) 是现代操作系统内核（如 Linux 内核）中的一个重要特性。它们允许在运行时动态加载和卸载内核功能，而无需重新编译或重启内核。以下是对 LKMs 的详细介绍。

### 什么是 Loadable Kernel Modules (LKMs)?

Loadable Kernel Modules 是一段可以在内核运行时动态加载或卸载的代码。它们通常用于扩展内核的功能，例如添加新的设备驱动程序、文件系统支持或网络协议。

### LKMs 的优点

1. **灵活性**: 允许在不重启系统的情况下添加或移除内核功能。
2. **开发便利**: 开发和测试内核模块更为简便，因为不需要每次修改后都重启系统。
3. **资源管理**: 只在需要时加载模块，有助于节省系统资源。
4. **安全性**: 可以动态卸载存在漏洞的模块，减少安全风险。

### 常见的 LKM 类型

1. **设备驱动程序**: 用于支持新硬件设备。
2. **文件系统**: 添加对新的文件系统类型的支持。
3. **网络协议**: 支持新的网络协议或增强现有协议的功能。
4. **系统调用**: 添加或修改系统调用。

### LKM 的基本操作

#### 加载模块

使用 `insmod` 命令可以加载一个模块：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo insmod mymodule.ko ``` |

`mymodule.ko` 是你要加载的模块文件。

#### 卸载模块

使用 `rmmod` 命令可以卸载一个模块：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo rmmod mymodule ``` |

`mymodule` 是你要卸载的模块名称。

#### 查看已加载模块

使用 `lsmod` 命令可以查看当前加载的所有模块：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` lsmod ``` |

#### 模块信息

使用 `modinfo` 命令可以查看模块的详细信息：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` modinfo mymodule.ko ``` |

### 编写一个简单的 LKM

以下是一个简单的 “Hello World” 内核模块示例。

#### 代码示例

创建一个名为 `hello.c` 的文件，内容如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` #include <linux/init.h> #include <linux/module.h> #include <linux/kernel.h>  MODULE_LICENSE("GPL"); MODULE_AUTHOR("Your Name"); MODULE_DESCRIPTION("A simple Hello World LKM"); MODULE_VERSION("0.1");  static int __init hello_init(void) {     printk(KERN_INFO "Hello, World!\n");     return 0; }  static void __exit hello_exit(void) {     printk(KERN_INFO "Goodbye, World!\n"); }  module_init(hello_init); module_exit(hello_exit); ``` |

#### 编译模块

创建一个名为 `Makefile` 的文件，内容如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` obj-m += hello.o  all:     make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules  clean:     make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean ``` |

然后运行以下命令编译模块：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` make ``` |

编译成功后会生成一个 `hello.ko` 文件。

#### 加载和卸载模块

加载模块：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo insmod hello.ko ``` |

查看内核日志以确认模块加载成功：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` dmesg | tail ``` |

卸载模块：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo rmmod hello ``` |

再次查看内核日志以确认模块卸载成功：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` dmesg | tail ``` |

![](/2024/08/07/Linux-LKM-Rootkit简介与排查/1.5.jpg)

### Diamorphine

\*　Diamorphine 是一个 Linux 下的 LKM（Loadable Kernel Module，内核模块）rootkit，主要用于隐藏进程、文件、端口等，常被用于渗透测试或红队行动中。但因为它具有极高的隐蔽性和危害性，也常被黑客用于恶意目的。

* 项目地址 <https://github.com/m0nad/Diamorphine>
* 主要功能 1.隐藏文件 2.隐藏进程 3.隐藏自身内核模块 4.隐藏端口（可选）
* 前提条件：需要root权限、有相应的一些工具 如make、内核版本支持
* 安装：下载完源码 直接make 然后 insmod diamorphine.ko 即可。

  #### 隐藏文件
* 修改源码文件，替换成你想要隐藏的文件或者文件夹前缀
  ![alt text](/2024/08/07/Linux-LKM-Rootkit简介与排查/8c12629cc999b2f5b178043034b2f3e.png)
  ![alt text](/2024/08/07/Linux-LKM-Rootkit简介与排查/8f699e4205d4fe15befeb65d32974cc.png)

  #### 隐藏进程
* 使用kill 命令加 相应的信号编号实现相关的功能。
  ![alt text](/2024/08/07/Linux-LKM-Rootkit简介与排查/1edede0025d0112fffca7da2de217c3.png)

  #### 提权

  ![alt text](/2024/08/07/Linux-LKM-Rootkit简介与排查/07b05a522ca0de59b43f69779f31084.png)

  #### 隐藏自身模块

  ![alt text](/2024/08/07/Linux-LKM-Rootkit简介与排查/af4e702e23ab250cfd113d04446f7c2.png)

  #### 卸载模块

  ![alt text](/2024/08/07/Linux-LKM-Rootkit简介与排查/9c7484304087c8c5ca3b65efae94eaf.png)

### LKM Rootkit 排查

* 使用 dmesg 命令查看内核日志，寻找可疑的加载或卸载模块的日志。

  |  |  |
  | --- | --- |
  | ``` 1 ``` | ``` dmesg | grep module ``` |

![](/2024/08/07/Linux-LKM-Rootkit简介与排查/2.png)

* 之后find一下相关的文件，然后上传到云沙箱上进行扫描分析
  ![](/2024/08/07/Linux-LKM-Rootkit简介与排查/3.png)

  ### 安全性考虑

尽管 LKMs 提供了很大的灵活性，但也带来了潜在的安全风险：

1. **恶意模块**: 攻击者可以加载恶意模块，获取内核级别的权限。
2. **稳定性**: 不稳定或有缺陷的模块可能导致系统崩溃。
3. **签名验证**: 使用模块签名验证可以确保只有经过认证的模块被加载。

### 总结

Loadable Kernel Modules 是扩展内核功能的重要工具，提供了灵活性和开发便利性。通过正确的开发和管理，可以有效地利用 LKMs 来增强系统功能，同时需要注意安全性和稳定性问题。

[pwn basic](/2023/03/15/pwn-basic/ "pwn basic")

[OffSec蓝队课程IR-200及OSIR考证之旅](/2025/04/06/OffSec%E8%93%9D%E9%98%9F%E8%AF%BE%E7%A8%8BIR-200%E5%8F%8AOSIR%E8%80%83%E8%AF%81%E4%B9%8B%E6%97%85/ "OffSec蓝队课程IR-200及OSIR考证之旅")

* 文章目录
* 站点概览

![M0rk](/uploads/avatar.jpg)

M0rk

[55
日志](/archives)

4
分类

3
标签

[RSS](/atom.xml)

[GitHub](https://github.com/kevien "GitHub")

[Twitter](https://twitter.com/elonmusk "Twitter")

[Weibo](https://weibo.com/wuyanzu "Weibo")

1. [1. 什么是 Loadable Kernel Modules (LKMs)?](#什么是-Loadable-Kernel-Modules-LKMs)
2. [2. LKMs 的优点](#LKMs-的优点)
3. [3. 常见的 LKM 类型](#常见的-LKM-类型)
4. [4. LKM 的基本操作](#LKM-的基本操作)
   1. [4.1. 加载模块](#加载模块)
   2. [4.2. 卸载模块](#卸载模块)
   3. [4.3. 查看已加载模块](#查看已加载模块)
   4. [4.4. 模块信息](#模块信息)
5. [5. 编写一个简单的 LKM](#编写一个简单的-LKM)
   1. [5.1. 代码示例](#代码示例)
   2. [5.2. 编译模块](#编译模块)
   3. [5.3. 加载和卸载模块](#加载和卸载模块)
6. [6. Diamorphine](#Diamorphine)
   1. [6.1. 隐藏文件](#隐藏文件)
   2. [6.2. 隐藏进程](#隐藏进程)
   3. [6.3. 提权](#提权)
   4. [6.4. 隐藏自身模块](#隐藏自身模块)
   5. [6.5. 卸载模块](#卸载模块-1)
7. [7. LKM Rootkit 排查](#LKM-Rootkit-排查)
8. [8. 安全性考虑](#安全性考虑)
9. [9. 总结](#总结)

©
2025

M0rk

由 [Hexo](https://hexo.io) 强力驱动

主题 -
[NexT.Muse](https://github.com/iissnan/hexo-theme-next)