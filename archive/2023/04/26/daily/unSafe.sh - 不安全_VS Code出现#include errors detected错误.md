---
title: VS Code出现#include errors detected错误
url: https://buaq.net/go-160492.html
source: unSafe.sh - 不安全
date: 2023-04-26
fetch_date: 2025-10-04T11:31:31.188911
---

# VS Code出现#include errors detected错误

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/e1b54308e45a93cfb1d60694356898a9.jpg)

VS Code出现#include errors detected错误

C/C++最近下载了某开源软件的源码，其使用 CMake 构建。在使用 VS Code 浏览源码时，发现一个奇怪的现象：1. CMake构建没问题，断点调试也OK；2. 能通过F12快捷键跳转头文件
*2023-4-25 22:2:47
Author: [itlanyan.com(查看原文)](/jump-160492.htm)
阅读量:21
收藏*

---

[C/C++](https://itlanyan.com/category/cc/)

最近下载了某开源软件的源码，其使用 [CMake](https://itlanyan.com/tag/cmake) 构建。在使用 [VS Code](https://itlanyan.com/tag/vs-code) 浏览源码时，发现一个奇怪的现象：

1. CMake构建没问题，断点调试也OK；

2. 能通过F12快捷键跳转头文件、函数、类等定义；

3. 一些 `#if` 条件宏未正确设置，导致代码高亮不对；

4. 许多能正常跳转的头文件标红，光标移过去提示 “#include errors detected based on information provided by the configurationProvider setting. (C/C++ 1696) ”

该错误不太影响正常使用，但是总觉得别捏：`#if` 宏条件编译的正确代码，几乎都是disable状态被暗色显示。

参考 [StackOverflow上的这个帖子](https://stackoverflow.com/questions/45583473/include-errors-detected-in-vscode/68139743#68139743) 顺利解决了问题，其操作步骤为：

1. Windows系统按 `ctrl+shift+p`，MacOS按 `command+shift+p`，在命令窗口里输入 **edit configurations** ，选择json那一项，按回车按钮打开工程的配置文件：

[![](https://itlanyan.com/wp-content/uploads/2023/04/open-cc-edit-configurations-json-1024x313.png)](https://itlanyan.com/wp-content/uploads/2023/04/open-cc-edit-configurations-json.png)

打开 c/c++ json配置文件

2. 将文件中的 **configurationProvider** 的值从 “ms-vscode.cmake-tools” 改成 “ms-vscode.cpptools”：

[![](https://itlanyan.com/wp-content/uploads/2023/04/修改C工程配置工具-1024x450.png)](https://itlanyan.com/wp-content/uploads/2023/04/%E4%BF%AE%E6%94%B9C%E5%B7%A5%E7%A8%8B%E9%85%8D%E7%BD%AE%E5%B7%A5%E5%85%B7.png)

修改C++工程配置工具

3. 保存配置文件，再返回源代码，能看到宏定义、头文件等已经正确显示了。

除此之外，一些外部依赖包的头文件路径可能不正确，例如找不到 `mpi.h`，此时可以编辑该配置文件，将 [MPI](https://itlanyan.com/tag/mpi) 的头文件路径加上：

[![](https://itlanyan.com/wp-content/uploads/2023/04/添加自定义头文件包含路径-1024x619.png)](https://itlanyan.com/wp-content/uploads/2023/04/%E6%B7%BB%E5%8A%A0%E8%87%AA%E5%AE%9A%E4%B9%89%E5%A4%B4%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E8%B7%AF%E5%BE%84.png)

添加自定义头文件包含路径

如果存在同名头文件，也可以通过调整顺序实现优先级的调整。

赞

文章来源: https://itlanyan.com/vs-code-include-errors-detected-in-vscode/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)