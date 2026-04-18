---
title: 一本恶意软件分析速成课程
url: https://mp.weixin.qq.com/s/NB2XhiuSppn7aW5IMsD2Ug
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:30:12.705953
---

# 一本恶意软件分析速成课程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9mJNQIzib3Q1ZXJbyQqAlLa8ZzOnZ52d5fFOBglZ89nxZ395U4Uv5Frx1om4dcSiagG7ZmCItx96uwNadxcP4ARoBX3TgHUGtnnNeVU6dA65A/0?wx_fmt=jpeg)

# 一本恶意软件分析速成课程

原创

JunYi
JunYi

毅心安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一本恶意软件分析速成课程

分享一本恶意软件分析速成课程，每一步都有详细的说明，非常适合0基础想学习ida、学习逆向的安全员。

### 地址：

https://docs.google.com/document/d/1I83PHeEImWacuQut02VBlkJ2-CJcuTYmt6mxa\_xGqlA/edit?usp=sharing

### 目录：

### 第一章：x86 基础知识

* • 汇编与反汇编 (Assembly & Disassembly)
* • 数据类型
* • x86 寄存器
* • 指令基础知识

+ • 移动 (MOV)
+ • 取反 (NOT/NEG)

* • 使用 IDA 破解汇编语言
* • 算术指令
* • 位运算指令
* • 访问内存

+ • 内存操作数
+ • LEA (加载有效地址)

### 第二章：堆栈 (The Stack)

* • 堆栈原理
* • PUSH 指令
* • POP 指令

### 第三章：基本流控制

* • JMP (跳转)
* • 交叉引用 (Cross-References)
* • CALL (调用)
* • RET (返回)
* • 函数调用原理
* • 字符串处理

### 第四章：函数结构

* • 堆栈帧 (Stack Frames)
* • 函数参数与局部变量
* • 调用约定 (STDCALL 与 CDECL)
* • 局部变量深入理解
* • 全局变量深入理解

### 第五章：条件分支

* • 条件分支原理
* • 比较指令：CMP 与 TEST
* • 常见条件跳转 (Conditional Jumps)
* • 轻松理解条件分支
* • If 语句的汇编实现
* • 使用 IDA 进行静态分析
* • **实验室 - apple.exe**

+ • 样本信息
+ • 实验目标
+ • 问题

* • **实验室 - bomb.exe**

+ • 样本信息
+ • 实验目标
+ • 问题

### 第六章：调试技巧

* • 强制执行代码
* • 跳转修补 (Jumper Patching)
* • NOP'ing-Out 指令 (指令擦除)

### 第七章：中级反汇编

* • 指针与内存
* • 乘法指令 (MUL 与 IMUL)
* • 数组
* • 循环结构
* • 字符串指令：MOVS, STOS, SCAS
* • 指令重复前缀：REP, REPE/REPZ, REPNE/REPNZ
* • 内联函数 (Intrinsic Functions)
* • 结构体 (Structures)
* • Switch 语句与跳转表
* • **实验室 - guesser.exe**

+ • 样本信息
+ • 实验目标
+ • 问题

### 第八章：x86-64 汇编

* • x86-64 主寄存器
* • x86-64 调用约定：\_\_fastcall
* • x86-64 堆栈约定与函数帧
* • 多字节 NOP 指令
* • MOVSX 与 MOVZX
* • **实验室 - quizshow.exe**

+ • 样本信息
+ • 实验目标
+ • 问题

### 第九章：逆向工程 Windows 二进制文件

* • Windows API 函数
* • Windows 数据类型与数据结构
* • 匈牙利命名法 (Hungarian Notation)
* • 阅读 Windows API 函数原型
* • 句柄 (Handles)
* • Windows API 命名约定
* • 文件 API 工作流
* • Windows 注册表
* • 注册表 API 工作流
* • 进程创建概述
* • DLL 函数用法
* • Windows 网络编程
* • **实验室 - encstrings.exe**

+ • 样本信息
+ • 实验目标
+ • 问题

### 附录

### 实验室解决方案

* • **apple.exe 解决方案**

+ • 简答题 / 详细分析

* • **bomb.exe 解决方案**

+ • 简答题 / 详细分析

* • **guesser.exe 解决方案**

+ • 简答题 / 详细分析

* • **quizshow.exe 解决方案**

+ • 简答题 / 详细分析

* • **encstrings.exe 解决方案**

+ • 简答题 / 详细分析

### 测验与练习题答案

* • **闪电测验答案**

+ • 继续前进 / 争论 / 跳跃咖啡厅 / 给我的激光器充能

* • **练习题答案**

+ • 添加值 (Add Values)
+ • 牛肉公司 (Beef Corp)
+ • 赢 (Win)
+ • 牛肉读者 (Beef Reader)
+ • 推推乐 (Pushy)
+ • 堆栈抓取 (Stack Grab)
+ • 套头衫 (Jumper)
+ • 困 / 太困了 (Sleepy / So Sleepy)
+ • funky\_print
+ • 睡眠不足 (Sleep Deprived)
+ • loopy\_printer
+ • 小凯撒 (Little Caesar)
+ • 波因德克斯特 (Poindexter)
+ • 奶酪棒 (Cheese Stick)
+ • structs\_make\_bucks
+ • 椰子里的青柠 (Lime in the Coconut)
+ • 末日提示 (Tip of the Doom)

### 部分截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9mJNQIzib3Q03ZIjvxjfVBa1e7tibbdJamRbZibHW2p5meVkNPPhKT2jCGEK2ALIicWssu6nWqoicEocmvt2L04l887EO9JE9jrMWcGY2Bce0Bx0/640?from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9mJNQIzib3Q31rtiaEicQNUkWXQufnOBFlmpgYjbuoZcDibSiaMsaGmI7bnBxMo0RzXgmichXeMuuuaTtROqoz29Jvj3JKHZ14OjNmYFeK5jdjibUk/640?from=appmsg "null")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/kzkqdAEDfXdKQzSjUmtSu9wlia18CPwm2k8nmiapVP04SYnXtghKHZquWfRclUc501UHoS9nOrAnBSuhKc1Y2nfw/0?wx_fmt=png)

毅心安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/kzkqdAEDfXdKQzSjUmtSu9wlia18CPwm2k8nmiapVP04SYnXtghKHZquWfRclUc501UHoS9nOrAnBSuhKc1Y2nfw/0?wx_fmt=png)

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