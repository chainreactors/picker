---
title: 腾讯哈勃恶意样本分析引擎横空出世：一台机器揭穿所有Linux病毒伪装
url: https://mp.weixin.qq.com/s/CX8Fy0Zu06JMGuaHsirzFw
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:35:12.616888
---

# 腾讯哈勃恶意样本分析引擎横空出世：一台机器揭穿所有Linux病毒伪装

# 腾讯哈勃恶意样本分析引擎横空出世：一台机器揭穿所有Linux病毒伪装

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

郑重声明：本文仅做技术分享，请勿将恶意样本置于真实生产环境中运行。所有分析操作必须在隔离的虚拟机环境下完成，因样本分析造成的任何后果由分析者自行承担。

## 重点导读概述

HaboMalHunter是腾讯哈勃恶意软件分析系统的开源子项目，专注于Linux x86/x64平台上ELF格式文件的自动化静态与动态行为分析。该工具能够帮助安全分析人员快速提取恶意样本的静态特征和动态运行行为，生成包括进程、文件I/O、网络通信、系统调用序列在内的完整分析报告。报告支持JSON和HTML两种输出格式，可直接导入哈勃分析系统进行可视化展示。

![HTML报告示例](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uq7Zc8vgStPR6WGQFNtWGu3mtCzo6mTHGYera1ejYS3C8cVIPjBv223d7V3WB5oYEmJ0CNiaKeQzOqfqMH4UIL38gicyZVKK4Q4U/640?from=appmsg)

HTML报告示例

## 重点导读项目结构

```
HaboMalHunter/
├── AnalyzeControl.py        # 主入口，分析调度器
├── config.ini               # 配置文件
├── base/                    # 基础类，静态/动态分析器公共父类
├── static/                  # 静态分析模块
├── dynamic/                 # 动态分析模块
├── iot_hunter/              # IoT恶意样本专项分析模块
├── metrics/                 # 行为ID定义、syscall表
├── util/                    # 工具脚本（YARA、日志转HTML等）
├── normal_hp/               # 正常样本基线生成模块
├── test/                    # 测试样本
└── package.sh               # 编译打包脚本
```

## 重点导读静态分析

### PART 01分析维度

静态分析模块对ELF文件进行全面特征提取，涵盖以下维度：

* **基础信息**：MD5、SHA1、SHA256、SSDEEP模糊哈希
* **文件类型**：通过libmagic识别文件格式
* **ELF头部**：入口点地址、机器类型、段表、节表
* **字符串信息**：ASCII和UTF-16双编码字符提取
* **SO依赖**：动态链接库依赖关系（ldd）
* **符号表**：导入/导出函数列表（readelf -s）
* **IP和端口**：从字符串中自动提取网络 Indicators
* **源文件路径**：从调试信息中提取源文件路径
* **YARA规则匹配**：基于规则库的恶意代码识别
* **加壳检测**：UPX等常见加壳工具自动识别与脱壳

### PART 02核心实现

StaticAnalyzer类继承自BaseAnalyzer，依次执行以下分析流程：

1. 文件类型检测（file命令）
2. 哈希计算（md5sum、sha1sum、sha256sum、ssdeep）
3. YARA规则匹配（yara库）
4. ExifTool元数据提取
5. 字符串提取（strings命令，ASCII和UTF-16双模式）
6. 动态链接依赖分析（ldd）
7. ELF结构解析（readelf -h/-S/-l/-s）
8. 节区哈希计算（objcopy + ssdeep）
9. 加壳检测与自动脱壳（upx -t/-d）

分析结果以JSON格式输出至`{md5}.static`文件，包含完整的结构化特征数据。

![JSON报告示例](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Ur4Iia6L8ibWy6a0rmwzLQIqTF4fXJ6DUNoK8xfMn2A66Ltx4PmeGOjJiaqexUzemjK106UFFbiaib92M98Xic0sbjOe9AjRVNoh31Ws/640?from=appmsg)

JSON报告示例

## 重点导读动态分析

### PART 03分析维度

动态分析模块在受控环境中执行样本，监控并记录其全部运行时行为：

* **进程监控**：clone、execve、进程退出时间戳
* **文件I/O**：open、read、write、delete等文件操作
* **网络通信**：TCP、UDP、HTTP、HTTPS、DNS请求
* **系统调用序列**：完整syscall调用链记录（基于sysdig）
* **libc函数调用**：getpid、system、dup等关键函数监控（基于ltrace）
* **动态链接符号**：LD\_DEBUG绑定日志解析
* **自删除/自修改/文件锁检测**：恶意样本常见自保护行为识别
* **内存分析**（可选）：基于LiME内存提取和Volatility框架的进程内存分析

### PART 04沙箱执行流程

DynamicAnalyzer通过target\_loader加载目标样本，配合多种监控工具实现行为捕获：

1. 启动前准备：网络接口激活、tcpdump流量捕获、sysdig事件记录
2. 样本加载：target\_loader通过Popen启动目标进程，LD\_DEBUG捕获动态链接行为
3. 运行时监控：ltrace/strace监控libc函数调用，sysdig监控syscall，tcpdump抓取网络流量
4. 协议解析：tshark解析DNS/HTTP/HTTPS/TCP/UDP流量，提取IP、端口、URL等Ioc
5. 行为聚合：clone、execve、file I/O、network等各类行为统一编号归档
6. 后处理：自删除/自修改检测、内存转储（可选）、日志压缩输出

分析结果输出至`{md5}.dynamic`文件，包含带时间戳的完整行为序列。

## 重点导读核心架构

### PART 05分析调度器

AnalyzeControl.py是项目主入口，承担分析流程的调度与协调职责。核心工作流程如下：

```
参数解析 → 配置初始化 → 工作目录初始化 → 静态分析 → 动态分析 → HTML报告生成 → 日志压缩
```

支持的功能包括：仅静态分析模式、压缩包批量分析原地分析模式、可配置超时控制、日志文件合并等。

### PART 06行为编号体系

metrics模块定义了完整的行为ID体系，包括静态行为ID（S\_ID\_*）和动态行为ID（D\_ID\_*）。每个分析结果节点都携带唯一ID标识，便于后续归类与检索。

### PART 07沙箱隔离保障

项目强制要求在VirtualBox虚拟机环境中运行样本，并建议在BIOS中启用Intel-VT硬件虚拟化支持。动态分析器通过以下机制实现隔离：

* 网络NAT转发，样本流量可控
* 可选INetSim模拟服务，阻断真实网络连接
* ptrace\_scope禁用，防止样本逃逸监控
* ASLR临时关闭，便于调试
* 分析完成后强制kill所有相关进程

## 重点导读IoT恶意样本专项分析

iot\_hunter子模块针对IoT僵尸网络恶意样本提供专项分析能力：

* **Mirai家族检测**：识别ARM架构下的Mirai变种特征
* **Gafgyt家族检测**：识别x86架构下的Gafgyt变种特征
* **家族变种关联**：基于插件化的特征匹配框架，支持快速扩展

插件化的设计使得安全人员可以针对新出现的IoT恶意样本家族编写对应的检测插件，提取家族特有行为特征。

## 重点导读日志转HTML

util/log\_to\_html/目录下的脚本负责将分析产生的JSON格式日志转换为可读性更高的HTML报告。转换后的报告包含：

* 静态特征的结构化展示
* 动态行为的时间线视图
* 网络通信的图形化呈现
* YARA规则匹配结果高亮

![分析结果示例](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uq2cZ475JBjUFOcVuH9H5zk5qKa2KG7bUuoXSPgMA0aHlDYyNc8sBIb3dWAX2CaytTricTvvpg0aibkw6CadhtJEj4SoNbITsfm4/640?from=appmsg)

分析结果示例

## 重点导读项目地址

本公众号非项目作者，仅做技术分享。

```
https://github.com/Tencent/HaboMalHunter
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoNFQiajsYlCNCcxjaEdsncRwbrOiahp8VDHf0kMmJQDKv5g2jZrnZmJiczlTxToxx74T40O2l4l1WY9dbnjIjtHuuicpGV2HpKZwI/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqyR8A50l5dnDJAvTaVHc2A6ADCWFVrkGPjN0MqIbPEGUPKibqyNiaSIbFYokRNrrqyamxynBvDbgGUDWXebnRyHJjp783oLKUL4/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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