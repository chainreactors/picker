---
title: 内存取证-没有debuginfo时如何解决符号表的难题
url: https://zgao.top/%e5%86%85%e5%ad%98%e5%8f%96%e8%af%81-%e6%b2%a1%e6%9c%89debuginfo%e6%97%b6%e5%a6%82%e4%bd%95%e8%a7%a3%e5%86%b3%e7%ac%a6%e5%8f%b7%e8%a1%a8%e7%9a%84%e9%9a%be%e9%a2%98/
source: Zgao's blog
date: 2026-04-07
fetch_date: 2026-04-08T04:30:24.778316
---

# 内存取证-没有debuginfo时如何解决符号表的难题

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 内存取证-没有debuginfo时如何解决符号表的难题

* [首页](https://zgao.top)
* [内存取证-没有debuginfo时如何解决符号表的难题](https://zgao.top:443/%E5%86%85%E5%AD%98%E5%8F%96%E8%AF%81-%E6%B2%A1%E6%9C%89debuginfo%E6%97%B6%E5%A6%82%E4%BD%95%E8%A7%A3%E5%86%B3%E7%AC%A6%E5%8F%B7%E8%A1%A8%E7%9A%84%E9%9A%BE%E9%A2%98/)

[4月 7, 2026](https://zgao.top/2026/04/)

### 内存取证-没有debuginfo时如何解决符号表的难题

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/%E5%86%85%E5%AD%98%E5%8F%96%E8%AF%81-%E6%B2%A1%E6%9C%89debuginfo%E6%97%B6%E5%A6%82%E4%BD%95%E8%A7%A3%E5%86%B3%E7%AC%A6%E5%8F%B7%E8%A1%A8%E7%9A%84%E9%9A%BE%E9%A2%98/)

任何曾经做过Linux内存取证的人都面临过这种场景：没有与内存镜像对应特定内核版本相匹配的调试符号，就寸步难行。各大云厂商（hyperscaler）在**开源Linux内核 + 用户态组件**的基础上，针对自家云基础设施进行深度定制和优化的**Linux发行版**（Linux Distribution）。这些发行版往往**自带定制内核**，而且还没有找到对应的debuginfo下载途径，面对这种场景会非常痛苦。

并且这些符号通常不会安装在生产系统上，必须从外部存储库获取，而当系统更新时，这些符号很快就会过时。如果你曾经尝试分析内存转储，却发现没有人发布该特定内核构建的符号，就会明白这种感觉。

文章目录

[ ]

* [使用预构建的 ISF 符号库](#%E4%BD%BF%E7%94%A8%E9%A2%84%E6%9E%84%E5%BB%BA%E7%9A%84_ISF_%E7%AC%A6%E5%8F%B7%E5%BA%93 "使用预构建的 ISF 符号库")
* [mquire：无需外部调试符号](#mquire%EF%BC%9A%E6%97%A0%E9%9C%80%E5%A4%96%E9%83%A8%E8%B0%83%E8%AF%95%E7%AC%A6%E5%8F%B7 "mquire：无需外部调试符号")
  + [mquire 内核版本要求](#mquire_%E5%86%85%E6%A0%B8%E7%89%88%E6%9C%AC%E8%A6%81%E6%B1%82 "mquire 内核版本要求")
  + [工作原理](#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86 "工作原理")
  + [实战测试](#%E5%AE%9E%E6%88%98%E6%B5%8B%E8%AF%95 "实战测试")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## 使**用预构建的 ISF 符号库**

<https://github.com/Abyss-W4tcher/volatility3-symbols>

![](https://zgao.top/wp-content/uploads/2026/03/image-4-1024x674.png)

然后去到vol3的机器上分析对应内存镜像文件的banners信息。

![](https://zgao.top/wp-content/uploads/2026/03/image-5-1024x575.png)

**为什么会出现多个 banner？**Volatility 的 `banners.Banners` 插件是在整个物理内存里**扫描 linux\_banner 字符串**（内核源码里 `init/version.c` 定义的那个静态字符串）。所以插件经常会命中 1~3 个完全一样（或轻微格式差异）的 banner。

这个时候我们机器上是没有符号表信息的，运行指定的插件会报错。

<https://raw.githubusercontent.com/Abyss-W4tcher/volatility3-symbols/master/banners/banners_plain.json>

用浏览器打开这个页面，复制刚才vol从内存中扫描出来的banner信息。

![](https://zgao.top/wp-content/uploads/2026/03/image-6-1024x504.png)

匹配的banner下面会有对应的符号表文件路径，拼接到github仓库链接就是符号表文件的下载链接。

```
https://github.com/Abyss-W4tcher/volatility3-symbols/raw/master/<file_path>

# 以本文的case为例如下
https://github.com/Abyss-W4tcher/volatility3-symbols/raw/master/Ubuntu/amd64/6.8.0/87/generic/Ubuntu_6.8.0-87-generic_6.8.0-87.88_amd64.json.xz
```

下载完成后上传到对应的符号表文件目录，不同机器的目录可能不同。

```
/usr/local/lib/python3.11/dist-packages/volatility3/symbols/linux
```

![](https://zgao.top/wp-content/uploads/2026/03/image-7-1024x817.png)

<https://github.com/volatilityfoundation/volatility3/issues/1934>

日志里刷了一大堆 **Unresolved reference**：这说明这个预置的 ISF 文件**缺少大量内核数据结构定义**，插件在解析 `task_struct`、`files_struct`、`fdtable` 等关键结构时直接卡住，所以 `psaux`、`lsof`、`bash` 这些插件全部返回空（只有表头）。

**KASLR 地址随机化完全没解析成功**。日志明确写着：
`Scanners could not determine any ASLR shifts, using 0 for both`
6.8 内核默认开启 KASLR，Volatility 找不到正确的内核基址偏移，导致链表遍历（进程列表、文件描述符等）全部失效。

所以说明这个方案对应一些特定版本仍然不一定起作用，但是对应大部分的内核版本应该是够用的。

## mquire：无需外部调试符号

<https://github.com/trailofbits/mquire>

### **mquire 内核版本要求**

* **BTF 支持**：内核 4.18 或更高版本，并启用 BTF（大多数现代发行版默认启用 BTF）
* **Kallsyms 支持**：内核 6.4 或更高版本（由于`scripts/kallsyms.c`格式更改）

### 工作原理

mquire 通过读取现代 Linux 内核中嵌入的两种类型的信息来分析内核内存：

1. 来自 BTF （[BPF 类型格式）](https://www.kernel.org/doc/html/next/bpf/btf.html)**的类型信息**——描述内核数据类型的结构和布局。BTF 数据使用[btfparse crate](https://crates.io/crates/btfparse)进行解析。
2. **来自 Kallsyms 的符号信息**– 提供内核符号的内存位置（与 使用的数据相同`/proc/kallsyms`）

通过将类型信息与符号位置相结合，mquire 可以查找并读取复杂的内核数据结构，例如：

* 进程内存映射（使用maple tree结构）
* 缓存文件数据（使用 XArray 结构）
* 内核日志消息

这样就可以直接从内核的文件缓存中提取文件。mquire 直接从内存 dump 里读取 **BTF**（内核自带的类型信息），**完全不需要外部 ISF**。

### 实战测试

这里和上面使用同样的内核版本用avml导出的内存镜像作比对，mquire可以解析成功，但是使用github上预构建的内核版本符号表配合vol却失败了。

```
┌──(root@kali)-[/var/tmp]
└─# mquire -h
内存取证和分析工具

用法: mquire [选项] <命令>

命令:
  shell    启动一个交互式 SQL shell 以查询快照
  query    针对快照执行 SQL 查询
  command  在给定的快照上执行内置命令
  help     打印此消息或给定子命令的帮助

选项:
  -d, --debug                                启用调试日志
      --operating-system <OPERATING_SYSTEM>  操作系统类型 (linux) [默认值: linux]
      --architecture <ARCHITECTURE>          架构类型 (intel) [默认值: intel]
  -h, --help                                 打印帮助
  -V, --version                              打印版本
```

![](https://zgao.top/wp-content/uploads/2026/04/image-2-1024x525.png)

这里我从github clone源码后在本地进行编译，然后用avml导出本机的内存镜像，用mquire做简单的SQL查询获取内存中的网络连接信息。

![](https://zgao.top/wp-content/uploads/2026/04/image-1-1024x561.png)

但是最终使用下来感觉和vol还有很多的差异，毕竟vol的生态要成熟的多，但是在没有符号表的应急场景下，可以把mquire作为vol强有力的补充。

注意：mquire不是从内存镜像中导出符号表给vol使用，而是独立的内存取证工具，可以理解为和vol是并列的关系。

## 总结

应急场景下面对老版本内核的直接用github上提供的现成内核版本符号表，对于高版本并且又没有现成内核符号表的情况，就用mquire辅助进行取证。

Post Views: 81

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/%E5%86%85%E5%AD%98%E5%8F%96%E8%AF%81-%E6%B2%A1%E6%9C%89debuginfo%E6%97%B6%E5%A6%82%E4%BD%95%E8%A7%A3%E5%86%B3%E7%AC%A6%E5%8F%B7%E8%A1%A8%E7%9A%84%E9%9A%BE%E9%A2%98/#respond)

Δ

版权©2020 Author By : Zgao