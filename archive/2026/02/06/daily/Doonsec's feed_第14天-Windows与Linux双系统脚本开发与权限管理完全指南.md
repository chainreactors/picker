---
title: 第14天-Windows与Linux双系统脚本开发与权限管理完全指南
url: https://mp.weixin.qq.com/s/uVW4yVF9r-pY1VaE3tf7Mw
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:03:11.168235
---

# 第14天-Windows与Linux双系统脚本开发与权限管理完全指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Byhdgj3e9qs55OTn4Tx2fMyzdtoOQ1UrrkmnbPLQYJqkzVMR74fDfdl3r92VlsXCBbppvEPJ141wC1Jllkkj3OxMtTgHk6ehqzqNdhYL5vI/0?wx_fmt=jpeg)

# 第14天-Windows与Linux双系统脚本开发与权限管理完全指南

原创

萧瑶
萧瑶

Alfadi组织

![]()

在小说阅读器中沉浸阅读

掌握跨平台运维与自动化必备技能

在日常开发与运维工作中，经常会遇到需要在 Windows 和 Linux 双环境下进行脚本编写和权限管理的情况。本文将系统性地介绍两大平台的脚本开发基础与权限体系差异，帮助你构建跨平台自动化能力。

一、Windows脚本开发：CMD与批处理

Windows 系统主要通过 CMD 和批处理文件（.bat）实现自动化任务。

基础语法要点

命令回显控制

```batch

@echo off  # 关闭命令回显

echo "hello world"  # 输出文本

@echo on   # 开启命令回显

```

基础命令

· pause - 暂停执行，按任意键继续

· :: 或 REM - 注释

· chcp 65001 - 解决中文乱码（UTF-8编码）

变量操作

```batch

set x=hello

set y=world

echo %x% %y%

set /p input=请输入：  # 接收用户输入

echo 当前路径：%cd%

```

流程控制与函数

```batch

call :my\_function  # 调用函数

:my\_function

echo 执行函数...

goto :eof  # 函数结束，停止向下执行

```

循环结构

```batch

:: 遍历当前目录文件

for %%i in (\*.txt) do echo %%i

:: 数字循环

for /l %%i in (1,1,10) do echo %%i

:: 读取文件内容

for /f "delims=" %%i in (file.txt) do echo %%i

```

文本搜索 - FIND命令

```batch

find /i "error" log.txt  # 忽略大小写搜索

find /c "success" log.txt  # 仅统计匹配行数

find /n "warning" log.txt  # 显示行号

```

比较运算符

· EQU - 等于

· NEQ - 不等于

· LSS - 小于

· LEQ - 小于或等于

· GTR - 大于

· GEQ - 大于或等于

实用案例示例

1. 获取目录下所有文件

```batch

@echo off

for /r %%i in (\*) do echo %%i

pause

```

2. 扫描网段存活主机

```batch

@echo off

for /l %%i in (1,1,254) do (

    ping -n 1 -w 100 192.168.1.%%i | find "TTL=" >nul

    if not errorlevel 1 echo 192.168.1.%%i 在线

)

```

二、Linux Shell脚本编程

基础必备知识

脚本基础结构

```bash

#!/bin/bash  # shebang，指定解释器

# 这是一个注释

echo "Hello, World!"

chmod +x script.sh  # 添加执行权限

./script.sh         # 执行脚本

```

变量与特殊变量

```bash

name="Linux"

echo $name

echo "脚本名：$0"

echo "第一个参数：$1"

echo "参数总数：$#"

echo "所有参数：$@"

```

条件判断

```bash

if [ -f "/etc/passwd" ]; then

    echo "文件存在"

elif [ -d "/home" ]; then

    echo "目录存在"

else

    echo "都不存在"

fi

```

循环结构

```bash

# for循环

for file in \*.txt; do

    echo "处理文件：$file"

done

# while循环

count=1

while [ $count -le 5 ]; do

    echo "计数：$count"

    ((count++))

done

```

函数定义

```bash

function my\_func() {

    echo "函数参数：$1"

    return 0

}

my\_func "参数值"

```

实用案例

1. 统计SSH爆破尝试

```bash

#!/bin/bash

LOG\_FILE="/var/log/auth.log"

FAILED\_ATTEMPTS=$(grep "Failed password" $LOG\_FILE | wc -l)

echo "SSH登录失败次数：$FAILED\_ATTEMPTS"

# 提取攻击者IP

grep "Failed password" $LOG\_FILE | awk '{print $11}' | sort | uniq -c | sort -nr

```

三、Windows与Linux权限体系对比

Windows权限体系

文件权限级别

· 完全控制 - 最高权限，可修改权限设置

· 修改 - 可读写和执行

· 读取和执行 - 可查看和运行文件

· 列出文件夹内容 - 仅限目录

· 读取 - 只读权限

· 写入 - 仅写入权限

用户组管理

· 管理员组（Administrators）- 系统管理权限

· 普通用户组（Users）- 标准用户权限

· 备份操作组（Backup Operators）- 备份恢复权限

· 系统账户（System）- 操作系统本身

· TrustedInstaller - Windows资源保护

Linux权限体系

用户标识管理

· UID 0 - 超级用户（root）

· UID 1-999 - 系统服务账户

· UID 1000+ - 普通用户账户

关键系统文件

```bash

# /etc/passwd 示例

root:x:0:0:root:/root:/bin/bash

# 用户名:密码标识:UID:GID:描述:家目录:默认shell

# /etc/group 示例

erik:x:1000:erik

# 组名:组密码标识:GID:组成员

```

文件权限详解

```

drwxr-xr-x 2 root root 4096 Jan 1 12:00 example

↑ ↑↑↑ ↑↑↑ ↑↑↑

│ │││ │││ ││└─ 其他人权限(r-x)

│ │││ │││ │└── 所属组权限(r-x)

│ │││ │││ └─── 所有者权限(rwx)

│ │││ ││└───── 硬链接数/子目录数

│ │││ │└────── 所属组

│ │││ └─────── 所有者

│ ││└───────── 特殊权限位

│ └└────────── 文件类型(d目录、-文件、l链接)

└───────────── 文件类型标识

```

权限对应关系

· 文件：r(读内容) w(修改) x(执行)

· 目录：r(列表文件) w(增删文件) x(进入目录)

权限对比表格

特性 Windows Linux

权限模型 ACL（访问控制列表） UGO（用户-组-其他）+ ACL

最高权限 Administrator/System root (UID 0)

权限继承 复杂继承规则 简单继承

默认权限 继承父目录 由umask控制

权限修改 图形界面/icacls命令 chmod命令

所有权 takeown命令 chown命令

四、学习资源推荐

1. 在线参考手册：https://book.shentoushi.top/

2. Linux Shell深入学习：https://mp.weixin.qq.com/s/qXZkKrF1vYtJv07L0-hkAA

3. 实践建议：

   · 从简单自动化任务开始练习

   · 多阅读优秀脚本源码

   · 在测试环境中反复尝试

总结

掌握 Windows 和 Linux 双平台的脚本开发与权限管理，是成为全栈运维工程师的重要基础。

Windows 批处理适合快速自动化日常任务，而 Linux Shell 则在服务器管理和复杂文本处理方面更加强大。理解两大系统的权限差异，有助于在混合环境中高效、安全地进行系统管理。

建议从实际需求出发，先掌握其中一个平台的脚本编写，再逐步扩展到另一个平台，最终实现跨平台的自动化运维能力。

---

互动话题：你在工作中最常用的自动化脚本是什么？遇到了哪些有趣的跨平台挑战？欢迎在评论区分享交流！

关注我们，获取更多实用的技术指南和最佳实践！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1icYKTWgZZhbWLSLhg9XPCS3QzhE6HZ4vxl5Xg1Gmia83FQlNGKU7Dddd4ZLPZ03WH1P40AToSaUdKf6OicPkE00A/0?wx_fmt=png)

Alfadi组织

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1icYKTWgZZhbWLSLhg9XPCS3QzhE6HZ4vxl5Xg1Gmia83FQlNGKU7Dddd4ZLPZ03WH1P40AToSaUdKf6OicPkE00A/0?wx_fmt=png)

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