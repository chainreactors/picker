---
title: 安全工程专栏导航：从 winos-gh0st 源码学安全工程
url: https://mp.weixin.qq.com/s/VPb6wxH-ZX3st3ws2sAxKg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:44:36.697918
---

# 安全工程专栏导航：从 winos-gh0st 源码学安全工程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IRUJvvhticxRbtYx8uSficd6PYDuf7aUJcQuiaWUmyzicYvibpnoeIVVDTCstiary178cHys47X2IibsZkrKODcSJ7NV5Vrbl18gBkrqWf4U2LGcicE/0?wx_fmt=jpeg)

# 安全工程专栏导航：从 winos-gh0st 源码学安全工程

原创

安全研究员
安全研究员

CppGuide

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IRUJvvhticxQLV9a4CPKBp6Ud4wcp5D3AWWUCg0GPuia6911EjCjXvlJ9DluAED8qQxqaVbm9Slo6iauakkOcxoJNQIy1nrib3mvd42axibRicZRQ/640?wx_fmt=jpeg&from=appmsg)

> **免责声明：本专栏仅用于安全工程学习研究，禁止使用本专栏介绍的技术做其他用途，否则后果自负，与本号无关。**

这套专栏不是远控使用教程，而是一套面向企业安全、蓝队检测、安全研发、授权红蓝测试人员和安全工程学习者的源码拆解教程。

它的核心目标只有三个：

1. 让新手能顺着源码看懂 Windows C++/MFC 远控类工程的结构、通信、插件和数据流。
2. 让企业安全人员能把高风险实现转换成检测、响应、加固和合规整改思路。
3. 让授权红蓝测试人员能在合法边界内复盘技术链路，帮助防御侧补齐证据、规则和流程。

## 怎么读最有效

| 读者类型 | 推荐路线 | 阅读目标 |
| --- | --- | --- |
| Windows 安全新手 | 01-20 顺序读，再进入插件课 | 先补齐环境、MFC、网络、插件、shellcode 和被控运行结构背景 |
| 企业蓝队 / SOC | 08-14、18-23、31-35、41-50 | 把源码行为转成主机、网络、内存和日志检测点 |
| 授权红蓝测试人员 | 01、08-23、31-43、45-50 | 理解能力边界，用于授权演练复盘和防御验证 |
| 安全研发 / 平台工程师 | 03-17、20-23、47-51 | 学习工具链、插件加载、日志链、协议安全和合规重构 |
| 管理者 / 方案负责人 | 01、44-52 | 快速理解风险分级、整改路线和报告交付方式 |

## 学习全景

```
安全边界
  -> VS 工具链、依赖库、MFC/Win32 基础
  -> 主控架构、日志进程、网络协议、插件加载
  -> EXE/DLL 生成、x86/x64、被控 shellcode 生命周期
  -> 被控线程结构、网络连接结构、上线、登录、配置下发、复制和转移客户
  -> 系统、文件、注册表、启动、终端、交谈、键盘记录
  -> 屏幕、后台桌面、屏幕墙、视频、音频
  -> 代理、压力、注入、驱动、敏感数据读取
  -> 持久化、高危能力、协议缺陷、安全编码、检测工程
  -> 应急响应、合规重构、企业评估报告
```

每一课都尽量采用同一种读法：先说明源码目录和模块角色，再沿着触发路径读关键代码；关键变量、风险点和防御含义尽量写进代码注释；图解用于帮助新手建立调用链、时序和数据结构的整体感。

## 第一阶段：边界、环境和源码地图

这一阶段先解决“能不能学、在哪里学、怎么打开工程、怎么看目录”的问题。读完后，你应该能在隔离实验环境中打开工程，并知道每个目录大致承担什么职责。

| 课次 | 专栏 | 你会学到什么 |
| --- | --- | --- |
| 01 | [专栏导论与安全边界](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793442&idx=1&sn=726f8039d87a6896d8201b3b74967b79&scene=21#wechat_redirect) | 学习边界、适用人群、授权红蓝测试边界、实验环境和禁止事项 |
| 02 | [源码整体结构导览](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793449&idx=1&sn=9c48ebc268d85369d52aa86414dc5223&scene=21#wechat_redirect) | 从根目录看主控、主插件、第三方库、生成器和专栏阅读路线 |
| 03 | [安装编译与调试环境](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793462&idx=1&sn=43a6b06fdd47faba4b13ab028c3d5628&scene=21#wechat_redirect) | 面向不熟悉 VS 的新手解释工作负载、SDK、MFC、平台工具集和调试入口 |
| 04 | [第三方库下载编译与依赖管理](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793469&idx=1&sn=2b8ecc5fee3957851fce6829a39bbc41&scene=21#wechat_redirect) | 理解 thirdparty、lib/libx64、头文件、库文件和依赖匹配问题 |
| 05 | [工程编译顺序与调试方法](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793476&idx=1&sn=6b628a19c982abb777d7d55d4ff9fb1e&scene=21#wechat_redirect) | 按安全实验方式梳理编译顺序、输出目录、断点和观察窗口 |
| 06 | [Windows C++/MFC 基础补课](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793477&idx=1&sn=0ed3cd3c7ee4885adb41db99d07375ad&scene=21#wechat_redirect) | 快速补齐消息映射、窗口、句柄、线程、注册表和 Win32 API 基础 |
| 07 | [主控界面布局单独讲解](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793499&idx=1&sn=7bfbe3f89a2163127c16548879a4bc80&scene=21#wechat_redirect) | 从主控界面反查源码、菜单、列表、对话框和命令入口 |

## 第二阶段：主控、日志、网络和插件加载主线

这一阶段是整套专栏的骨架。后面的每个功能插件，都离不开主控界面、网络收发、命令分发、插件加载和日志记录。

| 课次 | 专栏 | 你会学到什么 |
| --- | --- | --- |
| 08 | [主控端架构分析](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793500&idx=1&sn=9e5169edfef164148c2aafcf3855c6c4&scene=21#wechat_redirect) | 主控生命周期、连接上下文、列表展示、命令发送和窗口路由 |
| 09 | [主控内嵌日志进程与通信机制](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793507&idx=1&sn=49851c6eb3c57d1158292666b22c740d&scene=21#wechat_redirect) | 日志进程如何被内嵌到主控、如何启动、如何通过 IPC 接收日志 |
| 10 | [网络通信模型](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793517&idx=1&sn=d21bac53a0b51a4b1bf2f890b91f32e0&scene=21#wechat_redirect) | TCP/UDP、心跳、收包缓存、完整包判断和回调边界 |
| 11 | [协议与命令分发机制](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793563&idx=1&sn=4ca5a96d5651fb686038baf6bfc87f32&scene=21#wechat_redirect) | `TOKEN_*` 、`COMMAND_*`、包头、业务窗口和插件命令如何串联 |
| 12 | [插件化设计与模块加载总览](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793564&idx=1&sn=11f4a92df37f5e07331d8d5a96b5c79a&scene=21#wechat_redirect) | 插件来源、版本协商、缓存、加载方式和整体风险面 |
| 13 | [插件化设计与模块加载](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793565&idx=1&sn=74b625d66ebc725b850b058f343337b1&scene=21#wechat_redirect) | 插件 DLL 如何被请求、传输、缓存、校验和调度 |
| 14 | [插件 DLL 内存加载](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793573&idx=1&sn=e825048f5374f99382375e62892c9a74&scene=21#wechat_redirect) | `MemoryModule` 如何做 PE 映射、重定位、导入解析和入口调用 |
| 15 | [网络库：HPSocket](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793574&idx=1&sn=9a64eef51a957de0327d2da0d209c3d5&scene=21#wechat_redirect) | HPSocket 在工程中的用途、连接模型、回调接口和检测线索 |

## 第三阶段：生成链、架构适配和被控启动流程

这一阶段解释“生成出来的 EXE/DLL 是什么、配置如何写进去、x86/x64 怎么区分、shellcode 如何启动并取回上线模块，以及被控运行后线程和网络连接如何展开”。读完后，你再看上线、登录和后续插件，就不会觉得链路跳跃。

| 课次 | 专栏 | 你会学到什么 |
| --- | --- | --- |
| 16 | [生成 EXE 与 DLL](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793572&idx=1&sn=e82266b6868d9e2e0c62bfee6f2b0c3f&scene=21#wechat_redirect) | 主控如何选择模板、写入配置、输出 EXE/DLL，生成物在工程中的角色 |
| 17 | [x86/x64 双产物与 DLL 使用](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793581&idx=1&sn=249bce1cac5df5b5bff7cc488728bda7&scene=21#wechat_redirect) | 32/64 位产物、插件目录、函数指针、结构体偏移和 DLL 使用方式 |
| 18 | [被控 shellcode 生成与执行流程](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793601&idx=1&sn=ce14d1420bdc529c4037878d4049b11a&scene=21#wechat_redirect) | 从构建、启动、自定位、API 解析、配置读取到加载上线模块的完整生命周期 |
| 19 | [生成被控五个选项下发机制](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793602&idx=1&sn=14062d66a6b5c48146e35e63d6381a24&scene=21#wechat_redirect) | 键盘记录、结束蓝屏、反查流量、进程守护、傀儡进程五个选项如何写入配置并下发 |
| 20 | [被控线程结构与网络连接结构](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793621&idx=1&sn=43eef8606933607daf43985dbba56452&scene=21#wechat_redirect) | 不启用插件和启用插件时，被控端线程、基础连接、插件连接和回调绑定如何展开 |
| 21 | [主插件：上线模块](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793622&idx=1&sn=9aed7afe587a08697381e5ed77cd667c&scene=21#wechat_redirect) | 配置解析、连接初始化、版本请求、上线链路和防御侧证据 |
| 22 | [主插件：登录模块](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793659&idx=1&sn=059cd42e6b577560299780bb769bc268&scene=21#wechat_redirect) | 登录信息结构、插件链枢纽、命令入口、缓存和心跳机制 |
| 23 | [主控复制与转移客户](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793660&idx=1&sn=87dcf3aee9de9d175c56bcf78a381a05&scene=21#wechat_redirect) | 主控如何下发复制/转移命令，登录模块如何解释目标地址并改变连接归属 |

## 第四阶段：系统、文件、注册表和交互能力

这一阶段进入功能插件。重点不是学习如何操作，而是学习如何从代码里识别资产枚举、远程管理、路径边界、注册表修改和用户交互风险。

| 课次 | 专栏 | 你会学到什么 |
| --- | --- | --- |
| 24 | [主插件：系统管理](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793661&idx=1&sn=5056ab6b9238d08a9daf49096634dce8&scene=21#wechat_redirect) | 进程、窗口、服务、网络连接、软件列表等系统信息如何枚举 |
| 25 | [主插件：文件管理](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793662&idx=1&sn=552eb092b94131ec33fd281c90c1d089&scene=21#wechat_redirect) | 文件浏览、传输、搜索、压缩、删除、路径边界和审计证据 |
| 26 | [主插件：查注册表](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793707&idx=1&sn=e22cbdc63910d19942a8d74b25b05636&scene=21#wechat_redirect) | 注册表根键、子键、值、增删改查、敏感键和 WoW64 视图 |
| 27 | [主插件：启动管理](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793708&idx=1&sn=56844394eaceeba194ee07f72deabe03&scene=21#wechat_redirect) | 启动项、服务、计划任务、启动目录和持久化相关风险 |
| 28 | [主插件：远程终端](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793709&idx=1&sn=9337fed48839250f4ae2fd7c67fbc922&scene=21#wechat_redirect) | 管道、命令解释器、输出回传和命令执行审计 |
| 29 | [主插件：远程交谈](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793710&idx=1&sn=769b4993aab2a175e49273177490f5cf&scene=21#wechat_redirect) | 聊天协议格式、装包解包、窗口生命周期和锁屏实现 |
| 30 | [主插件：键盘记录](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793711&idx=1&sn=7ccac3ec9b1bbb29f3872e0006dbf34e&scene=21#wechat_redirect) | 键盘记录功能、窗口标题、剪贴板、离线键盘记录开关和实现机制 |

## 第五阶段：屏幕能力与屏幕墙

这一阶段专门处理屏幕相关能力。先比较高速屏幕、差异屏幕、娱乐屏幕三种当前桌面采集方式，再讲后台桌面/后台窗口，最后把主控侧“加入监控/屏幕墙”作为独立看板能力讲清楚。

| 课次 | 专栏 | 你会学到什么 |
| --- | --- | --- |
| 31 | [主插件：高速屏幕](https://mp.weixin.qq.com/s?__biz=MzI0NTE4NTE4Nw==&mid=2648793753&idx=1&sn=bc53cf1f15f44b449417c246e5b27b93&scene=21#wechat_redirect) | 为什么叫高速屏幕...