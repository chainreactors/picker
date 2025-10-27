---
title: 原创 Paper | 使用 Peach 进行基于变异和生成的 fuzzing
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650988702&idx=1&sn=281656d78aeb3f4318336630f589cab8&chksm=8079a2acb70e2bba91e1bb2f392c6710fc7bf6a4d191faa67d01c0ebb0cc69f7f1532c799fee&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-09-15
fetch_date: 2025-10-06T18:26:20.501738
---

# 原创 Paper | 使用 Peach 进行基于变异和生成的 fuzzing

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT2H8QBS6aicHvTtBy7bRiaHbUQMqyIfVH4MRqapjaa22JQ8gicDib6PBDvIKAyQddYZ9H8Dawku9RURzQ/0?wx_fmt=jpeg)

# 原创 Paper | 使用 Peach 进行基于变异和生成的 fuzzing

原创

404实验室

知道创宇404实验室

**作者：******0x7F@********知道创宇404实验室****

**时间：**2024年9月14日****

**1 前言**

Peach 是一个于 2004 年开发的模糊测试框架(SmartFuzzer)，能够执行基于生成和变异的模糊测试。其核心思路在于其内部的 PeachPit 变异引擎，安全研究员可通过 xml 描述目标文档的详细格式(pit文件)，在随后的 fuzzing 过程中引导变异数据的生成；相比于使用 afl/afl++ 进行常规化的 fuzzing，使用 Peach 能够生成更规范的变异数据，从而在一定程度上提高覆盖率。

Peach 项目目前有接近 20 年的发展历史；Peach2.0 使用 Python 进行开发并于 2007 年夏开源发布，其功能包括进程监控和使用 XML 创建模糊测试器；Peach3.0 使用了 Microsoft .NET Framework(C#) 完整重写了项目，并使用 Mono 实现了跨平台支持，于 2013 年初发布；直到 2020 年，Peach Fuzzer Professional v4 被 GitLab 收购并成为 GitLab 生态圈的一部分。

本文将简单介绍 Peach 的功能，通过实验的方式理解 Peach 的核心思路和基本使用方法；由于 Peach4.0 部分功能被修改用于适配 GitLab，同时该项目目前处于停止维护的状态，所以本文将以 Peach3.0 作为实验环境。

本文实验环境：

```
Ubuntu 22.04 x64
Peach 3.1.124
Mono 4.8.1
GDB 12.1
Python 2.7
```

**2 Peach环境配置**

从 https://sourceforge.net/projects/peachfuzz/ 可以选择通过二进制包安装或者源码安装。

#### **2.1 Peach二进制包安装**

这里我们首先进行二进制包安装：

```
# download peach-3.1.124-linux-x86_64-release.zip
# 配置工作目录
$ mkdir peach-3.1.124-linux-x86_64-release
$ cd peach-3.1.124-linux-x86_64-release/
# 解压和安装 Peach
$ unzip peach-3.1.124-linux-x86_64-release.zip
```

执行如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3embTTN7y45cagjicjhibicjKEVsx1GvjcGiaIIa5mbicFTNtWTNBvqSteyJic0IicjUCByCcfic4K9GchUQ/640?wx_fmt=png&from=appmsg)图1:Peach二进制包安装

Peach3 是由 Microsoft .NET Framework 进行开发的，所以需要 Mono (即跨平台的.NET实现)，我这里使用的较老的 `Mono 4.8.1` 版本，参考官方使用 `apt` 安装老版本如下：

```
# 配置 mono 仓库签名
$ sudo apt install ca-certificates gnupg
$ sudo gpg --homedir /tmp --no-default-keyring --keyring /usr/share/keyrings/mono-official-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF

# 添加 mono 源以及更新
$ echo "deb [signed-by=/usr/share/keyrings/mono-official-archive-keyring.gpg] https://download.mono-project.com/repo/ubuntu stable/snapshots/4.8.1 main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
$ sudo apt update
$ sudo apt list -a mono-complete

# 使用 apt-preferences 解决依赖组件的版本问题
$ vim /etc/apt/preferences.d/50my
Package: *mono*
Pin: origin download.mono-project.com
Pin-Priority: 1001

Package: libnunit*
Pin: origin download.mono-project.com
Pin-Priority: 1001

# 安装 mono-complete=4.8.1.0-0xamarin1
sudo apt install mono-complete=4.8.1.0-0xamarin1

# 检查 mono 版本
$ mono -V
```

*经测试，在 Ubuntu 22.04 通过 `apt` 默认安装的 `mono 6.8.0.105` 环境下，`Peach3.exe` 不能正常执行 fuzzing 功能，仅能够执行 help 等命令。*

执行如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3embTTN7y45cagjicjhibicjKUicRic0YRmmLIFeU5RNNxUYSgszhvaPlfHDlviakk1953LqBaibwXicsMmQ/640?wx_fmt=png&from=appmsg)图2：安装mono支持

Peach3 的核心程序为 `Peach.exe`，使用 `mono Peach.exe -h` 或 `./Peach.exe -h` 运行如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3embTTN7y45cagjicjhibicjKXDJRhib5Sm027sqmeXtgGwwIsaZwEgNINwC1pNeFy96HlvZmSVppYSg/640?wx_fmt=png&from=appmsg)图3：Peach运行以及帮助

#### **2.2 GDB-Python2.7适配**

由于 Peach3 在 Linux 环境下依赖于 GDB 和 Python2.7 运行，同时还要求 GDB 使用 Python2.7 的插件，Ubuntu 通过 `apt` 安装的 GDB 默认使用 Python3.x，我们需要从源码指定 Python 插件版本来编译 GDB，如下：

```
# 下载以及解压 gdb-12.1
$ wget "https://ftp.gnu.org/gnu/gdb/gdb-12.1.tar.gz"
$ tar -zxvf gdb-12.1.tar.gz
# 进入源码目录，处理部分依赖问题
$ cd gdb-12.1/
$ sudo apt install python2.7-dev texinfo
# 指定 python2.7 版本和编译
$ ./configure --prefix=/home/ubuntu/peach/install --with-python='/usr/bin/python2.7'
$ make && make install
```

编译安装完成后，使用 `ldd /home/ubuntu/peach/install/bin/gdb` 可以看到源码编译的 GDB 依赖于 Python2.7 如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3embTTN7y45cagjicjhibicjKWwsZLgwMmtyctpOq1OhyJfGOsgYAGxlHOUAiacL4hOcOtymxq3hSv8g/640?wx_fmt=png&from=appmsg)图4：GDB-Python2.7适配

**2.3 Peach源码安装**

由于 Peach3 版本已经很老了，在实际使用还会出现诸多问题；这里我们推荐通过源码安装以便解决这些使用问题，如下：

```
# download peach-3.1.124-source.zip
# 配置工作目录
$ mkdir peach-3.1.124-source
$ cd peach-3.1.124-source
# 解压 Peach 源码
$ unzip peach-3.1.124-source.zip
```

为了使用 Peach3 能够直接使用我们源码编译的 GDB(Python2.7)，我们需要修改源码中的默认依赖，同时由于 GDB12.1 更新了 `logging` 的用法，我们还需要解决 Peach3 中不兼容的问题，我们整合后的补丁参考 peach-gdb.patch；

除此之外，`peach-3.1.124` 版本下 `Peach.Core/Engine.cs#runTest()` 好像还存在 bug？这里的逻辑为 `目标程序运行 => 数据变异 => crash收集`，导致 `crash收集` 环节时将错位保存新变异的数据，修复补丁参考 peach-runtest.patch；

最后由于 Peach3 源码依赖于 `3rdParty/pin/pin-2.13-61206-gcc.4.4.7-linux/` 组件，这需要非常老的 `Gcc4`，我们这里采取手动升高依赖版本 `pin-3.19-98425-gd666b2bee-gcc-linux`，如下：

```
# 下载和解压
$ cd 3rdParty/pin/
$ wget "https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.19-98425-gd666b2bee-gcc-linux.tar.gz"
$ tar -zxvf pin-3.19-98425-gd666b2bee-gcc-linux.tar.gz

# 修改编译依赖组件名称
$ vim ./build/config/linux.py
# env['PIN_VER'] = 'pin-3.19-98425-gd666b2bee-gcc-linux'
```

随后使用 `waf` 进行编译：

```
# 使用 configure 构建项目
$ python2.7 waf configure
# (由于修改了 pin 版本这里会提示错误，但不影响实际功能
# (Available - Missing Features: pin

# 使用 build 构建项目，编译的二进制存储于 [src]/slag/
$ python2.7 waf build
# (默认 pin 版本和默认 Gcc 版本的冲突错误
# (#error The C++ ABI of your compiler does not match the ABI of the pin kit.

# 使用 install 安装项目，编译的二进制存储于 [src]/output/
$ python2.7 waf install
```

编译安装执行如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3embTTN7y45cagjicjhibicjKgLaZJiciaaaXzaHz1DppxXA5PzQ9tnwyoaliagIyiakBllJ0k5mAO5Wp7w/640?wx_fmt=png&from=appmsg)

安装完毕后，Peach 程序位于 `[src]/output/` 下，我们可以使用 `export PATH=` 添加路径，便于后续使用：

```
# Peach3 + mono 4.8.1 需要设置 TERM
$ export TERM=xterm
# 添加 PATH
$ export PATH=$PATH:/home/ubuntu/peach/peach-3.1.124-source/output/linux_x86_64_debug/bin/
$ Peach.exe -h
```

执行如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3embTTN7y45cagjicjhibicjKDbGEVwR5gc6IayHAbib1Shu9T5DmyUmSniabRuQzEzCaXZUbsxSt8S8w/640?wx_fmt=png&from=appmsg)

**3 基于变异的fuzzing**

配置好 Peach 环境后，我们可以按照官方文档学习 Dumb Fuzzing，其核心思路是通过对种子文件的各种变换(位翻转、裁剪、拼接等)产生变异数据，也就是基于变异的 fuzzing；这里我们将对 Linux 下的图片查看器 `feh` 的 `PNG` 图片格式逻辑进行 fuzzing。

首先安装目标软件 `feh` 以及配置工作目录：

```
$ sudo apt install feh
$ mkdir test-feh && cd test-feh
```

使用 Peach 进行 fuzzing 的核心在于编写 Pit 文件，其模板文件 `[src]/Peach/template.xml` 如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3embTTN7y45cagjicjhibicjKhXzgMAsaicIUxJLNeKhjDs5uHnVf1ZicjzQdlaQrNIX0NzcwvyVI4o8w/640?wx_fmt=png&from=appmsg)

根据模板我们很容理解和构造针对 `PNG` 的 Pit 文件；首先构建 `<DataModel>` 字段，该字段用于描述数据格式，如下：

```
<DataModel name="TheDataModel">
    <Blob />
</DataModel>
```

我们这里使用「基于变异的fuzzing」，所以使用 `Blob` 二进制数据进行占位表示，后续我们将使用种子文件内容填充该位置；

随后是 `<StateModel>` 字段，该字段用于描述 Peach 的执行状态流，其中子字段 `<State>` 用于定义状态/阶段(通常只有一个)，如下：

```
<StateModel name="TheState" initialState="Initial">
    <State name="Initial" >
        <Action type="output" >
            <DataModel ref="TheDataModel" />
            <Data name="data" fileName="samples_png/*.png" />
        </Action>
        <Action type="close" />
        <Action type="call" method="LaunchViewer" publisher="Peach.Agent" />
    </State>
</StateModel>
```

`<Action>` 字段用于实际描述 Peach 的动作，最常用的有三个：

1. output：链接至具体的 `<DataModel>` 表示数据生成并在此输出/生成，我们这里额外使用了 `<Data>` 字段，从 `"samples_png/*.png"` 文件填充上文的 `<Blob>` 数据；
2. close：输出/生成完数据后，进行关闭文件的操作；
3. call：调用下一个组件，通常为 `Peach.Agent` 即 `<Agent>` 字段；

接下来就是 `<Agent>` 字段，主要需要设置 `<Monitor>` 子字段，其用于监控目标程序的异常状态(即crash)，依照操作系统我们这里使用 `LinuxDebugger`(底层调用为 GDB)，并按需设置好目标程序和命令行参数，如下：

```
<Agent name="TheAgent">
    <Monitor class="LinuxDebugger">
        <Param name="Executable" value="feh" />
        <Param name="Arguments" value="fuzzed.png" />
    </Monitor>
</Agent>
```

最后我们来设置 `<Test>` 字段，该字段相当于 Pit 文件的主函数，同时包含了一些全局定义等内容，如下：

```
<Test name="Default">
    <StateModel ref="TheState"/>

    <Publisher class="File">
        <Param name="FileName" value="fuzzed.png" />
    </Publisher>

    <Agent ref="TheAgent" />

    <Logger class="Filesystem">
        <Param name="Path" value="logs" />
    </Logger>
</Test>
```

这里定义并链接了上文的 `<StateModel>` 和 `<Agent>`，而 `<Publisher>` 表示生成的样本数据应该如何发布，这里保存为了 `fuzzed.png` 文件，该字段完成了「变异数据生成」和「样本传入目标程序」两个环节的对接：

```
<Action type="output" />
===>
<Publisher />
===>
<Param name="Arguments" value="fuzzed.png" />
```

另外还有 `<Logge...