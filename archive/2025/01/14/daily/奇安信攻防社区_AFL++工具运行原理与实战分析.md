---
title: AFL++工具运行原理与实战分析
url: https://forum.butian.net/share/4033
source: 奇安信攻防社区
date: 2025-01-14
fetch_date: 2025-10-06T20:05:34.731165
---

# AFL++工具运行原理与实战分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### AFL++工具运行原理与实战分析

* [硬件与物联网](https://forum.butian.net/topic/51)

AFL++（American Fuzzy Lop ++）是一款开源的模糊测试工具，用于发现软件中的漏洞。模糊测试（Fuzzing）是一种自动化的测试技术，旨在通过向软件输入大量随机或伪随机的数据，来发现潜在的安全漏洞或程序崩溃。AFL 是由 Michał Zalewski 开发的，被认为是最流行和有效的模糊测试工具之一。

什么是AFL++
========
AFL++（American Fuzzy Lop ++）是一款开源的模糊测试工具，用于发现软件中的漏洞。模糊测试（Fuzzing）是一种自动化的测试技术，旨在通过向软件输入大量随机或伪随机的数据，来发现潜在的安全漏洞或程序崩溃。AFL 是由 Michał Zalewski 开发的，被认为是最流行和有效的模糊测试工具之一。
环境安装
====
由于 AFL++ 在进行模糊测试时可能对测试环境产生影响，因此推荐在隔离的环境中运行，如 Docker 容器或虚拟机。这种隔离能够有效防止因模糊测试导致的系统不稳定或崩溃等问题，确保主系统的安全性和稳定性。如果使用虚拟机进行测试，建议定期创建快照，以便在测试过程中出现异常时快速恢复到先前的状态。
安装环境：
```php
apt-get update && apt-get install -yq gcc make wget curl git vim gdb clang llvm python3 python3-pip bsdmainutils
```
afl++ 下载地址：
```php
https://github.com/AFLplusplus/AFLplusplus
```
如果在解压 ZIP 文件时遇到权限不足的问题，可以将 ZIP 文件转移到 Linux 环境下，使用 `sudo unzip [文件名.zip]` 命令进行解压。这种方法可以有效绕过权限限制。
下载完成后，进入 AFL 文件夹，直接运行命令编译文件。
```php
make && make install
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9f89fca0ec27f473cd15bdc2b3824ace29db3a69.png)
当按下 Tab 键时，如果能够正确补全并显示工具名称，则表明编译已成功完成。
AFL++ 设置与编译
===========
这里实战用nmap程序来演示，如果你要用AFL++去fuzz一个程序，那么就需要下载对应程序的源代码，nmap的源代码在github可以找到
```php
https://github.com/nmap/nmap
```
解压完后，进入文件夹，这里讲一下特殊的文件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1f2f1b9ffb9c1518b375f6fa225e95ef3c735088.png)
`configure` 文件通常存在于许多开源软件的源代码目录中，是自动配置脚本的一部分，用于准备构建软件。它是使用 GNU Autotools（例如 `autoconf`）生成的脚本，目的是在不同的系统环境下自动配置软件包的编译和安装，afl++会利用这个文件，编译程序时插桩，具体细节在AFL++模糊测试原理处会详细展开说明
使用afl-gcc编译程序
```php
CC=afl-clang-fast ./configure --disable-shared
```
`CC=afl-clang-fast` 表示在运行 `./configure` 时，将使用 `aflafl-clang-fast` 代替系统默认的 C 编译器执行configure文件，`afl-clang-fast` 是 AFL++ 的一个编译器包装器，基于 LLVM 的 `clang` 编译器。相比于 `afl-gcc`，`afl-clang-fast` 使用了更现代的插桩技术，提供了更高效的性能和更精确的代码覆盖率监控 ，`--disable-shared` 选项，可以确保目标程序只编译成静态链接的二进制文件。所有的代码都会被直接链接到生成的二进制文件中，AFL++ 能够插桩并跟踪所有代码的执行路径，而不会遗漏掉因为动态链接而无法插桩的部分
如果之后make编译失败，也可以使用afl-gcc
```php
CC=afl-gcc ./configure --disable-shared
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-6259f91de9bb0ce588051b006368de2d3778e1ac.png)
然后执行make，`make` 是一个构建自动化工具，用于根据 `Makefile` 中的指令来编译和构建程序
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4ec200e786257c7dc94948c89d97bdfad4c6fb57.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-7b9b134827cdfbf06f04ae0e6a97b449b152e209.png)
如何Fuzz程序命令行参数
-------------
现在编译完成后，可以使用 AFL++ 进行模糊测试。但需要注意的是，如果不在目标程序中引入 `argv-fuzz-inl.h` 头文件，AFL++ 将默认对程序的标准输入（stdin）进行模糊测试，而不是针对命令行（argv）参数。因此，AFL++ 只会测试程序运行后等待用户输入的部分。如果希望对程序的命令行参数进行模糊测试（例如测试 `nmap` 的 `-iL` 参数），则必须在目标程序的源码中包含 `argv-fuzz-inl.h` 头文件，并对相应代码进行调整，以便 AFL++ 能够正确生成并测试不同的命令行参数组合
argv-fuzz-inl.h文件下载地址：
```php
https://github.com/google/AFL/blob/master/experimental/argv\_fuzzing/argv-fuzz-inl.h
```
原理：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-25f11575e7a5177bb0070e4475379be43a36e0e1.png)
这里调用了`afl\_init\_argv`函数来覆盖`argv`。`argv`是传递给`main`函数的字符串数组，包含程序的命令行参数。因此，无论`afl\_init\_argv`函数执行了何种操作，最终结果都会覆盖`argv`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f681128ec9d6a651145a44cadb403dfe281b19d7.png)
随后调用了`read`函数，从标准输入中读取了大量数据
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0dce4d6298496a482d0b2ed600b95f472d229328.png)
`ptr`是一个指向缓冲区的指针，用于将数据读入其中。接下来，通过`while`循环检查指针所指向的内容是否为非零值。在循环中，指针会递增，并向前移动以处理接下来的数据
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-e3972d34bda0940cadffb29363988d2bc9a22ad2.png)
在这个循环中还有一个名为`rc`的计数器，它从1开始并在每次迭代时递增。循环开始时，当前指针的位置会被存储在`ret`数组中，以便后续使用
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0ea578a09bd52413e98d7892ff83890a20ed8dba.png)
在`while`循环内还有一个嵌套的`while`循环，这个内层循环的作用是检查是否存在空字节，并在发现空字节时递增指针。同时，它会将数据存储在`ret`数组中，继续处理接下来的内容
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4d84329325d4f87d7524be06e7668ba3ee03ca85.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-160d8b59e74476e761f3d5944a6c9a34cdd8c96d.png)
接下来，函数会创建一个伪造的`argv`结构，并将其返回给主函数。这意味着在`main`函数中获取的`argv`将全部使用由AFL++生成的数据，从而替换原有的命令行数据
下载 `argv-fuzz-inl.h` 文件后，打开目标程序的源代码文件，并在代码的头部加入以下代码行，引入该头文件：
nmap的源代码为nmap.cc
```php
#include "/{path}/argv-fuzz-inl.h"
```
其中，`{path}` 应替换为 `argv-fuzz-inl.h` 文件的实际路径。如果文件已放在同一目录下，可以直接使用相对路径，如 `#include "argv-fuzz-inl.h"`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-d705f982edb85e533078e32368e135011b7a56d4.png)
ps：如果需要不fuzz程序的参数，而是直接对 `argv[0]` 进行模糊测试，需要修改argv-fuzz-inl.h源内容
```php
int rc = 0
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c733e65dfa179caa43a82677a1de515ba6994ecb.png)
回到正题，在被fuzz测试程序的main函数第一行加入：
```php
AFL\_INIT\_ARGV();
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c4ba51f8fcd1c9513c103bb577fb9d106474d0af.png)
重新编译文件
```php
CC=afl-gcc ./configure --disable-shared & make
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-82d30ad0263a4da407543a0359650a14db5de118.png)
编译好的nmap程序就在当前目录下
AFL++进行FUZZ
===========
设置fuzz时输入输出文件夹
```php
mkdir /tmp/in
mkdir /tmp/out
```
在/tmp/in文件夹下是要测试的参数，这里只测试nmap的-iL参数
```php
echo -en "-iL\x00" > /tmp/in/1
```
`-en` 选项用于确保 `echo` 不添加额外的换行符，并且 `\x00` 表示字符串的结束符（null 终止符）
开始进行fuzz
```php
afl-fuzz -i/tmp/in -o /tmp/out ./nmap
```
`-i` 指定输入目录，`-o` 指定输出目录，最后是需要fuzz的程序
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c5f893f7170ff4eb39e476a58a1d5664172529ee.png)
如果提示这个，直接输入echo core &gt;/proc/sys/kernel/core\\_pattern，然后重新运行即可
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-5519ddad8dfb003b08eb9a038bac4655014bad6c.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-88e2a5a267089462c8d2c71e85b78e68201d4355.png)
最重要的一个区域是findings in depth
```php
favored paths: 表示被认为最有可能找到新路径或错误的路径数量，以及占总路径数量的百分比。
new edges on: 显示新路径中发现的边缘数量及其占比。
total crashes: 显示发现的崩溃数量以及其中独特崩溃的数量。
total tmouts: 显示发现的超时数量及其中独特超时的数量。
```
如果出现total crashes，那么意味着程序中存在潜在的漏洞 ， AFL++会将导致崩溃的输入文件保存到`/tmp/out`目录下，随后可以结合GDB进行调试，以进一步分析并定位问题
多线程可以让fuzz效率变高，在不同的终端里执行以下命令：
```php
afl-fuzz -i /tmp/in -o /tmp/out -M f1 ./nmap
afl-fuzz -i /tmp/in -o /tmp/out -S f2 ./nmap
afl-fuzz -i /tmp/in -o /tmp/out -S f3 ./nmap
……
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a81c6295f673d29d86cde1d4bb2936207e413034.png)
fuzz一次时间比较久，1天都是常见的事
AFL++模糊测试原理
===========
现在将使用正常gcc编译的nmap和afl-gcc编译的nmap进行对比，这是正常编译的nmap main函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-651bc5b6b42461d54245dd1b01be1bac4ffbe4ab.png)
这是使用afl-gcc编译的nmap main函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-271783d7e2106001a0b3cd863068aecb488d14e2.png)
在每个跳转分支中，AFL++插入了`afl\_maybe\_log`函数。在调用`afl\_maybe\_log`之前，还存在一个`mov`指令，该指令的作用是设置校准参数。当执行`afl\_maybe\_log`时，AFL++会记录程序采用了哪个分支。如果在大多数情况下分支指令都是向左执行时，突然发现有一个输入可以触发向右分支，AFL++就知道到达了程序的新路径或功能点，继续对程序进行模糊测试。

* 发表于 2025-01-13 10:00:00
* 阅读 ( 3876 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![cike_y](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/p...