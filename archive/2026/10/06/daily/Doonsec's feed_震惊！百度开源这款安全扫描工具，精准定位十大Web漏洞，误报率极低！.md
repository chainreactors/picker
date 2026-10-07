---
title: 震惊！百度开源这款安全扫描工具，精准定位十大Web漏洞，误报率极低！
url: https://mp.weixin.qq.com/s/I_MHFkqXeB69Fc4gXbD1Wg
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:53:57.389319
---

# 震惊！百度开源这款安全扫描工具，精准定位十大Web漏洞，误报率极低！

# 震惊！百度开源这款安全扫描工具，精准定位十大Web漏洞，误报率极低！

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

郑重声明：本文仅做技术分享，使用本工具进行安全测试时，必须确保已获得合法授权。未经授权对目标系统进行扫描可能违反相关法律法规。

## 重点导读概述

OpenRASP-IAST是一款基于OpenRASP的灰盒安全扫描工具，专注于自动化检测Web应用中的安全漏洞。该工具由百度安全团队开源推出，采用动态分析技术，在应用程序运行时收集调用信息并生成测试用例，实现对漏洞的精准识别。

该扫描工具的核心能力在于结合了运行时代理分析与自动化模糊测试两大技术路线。OpenRASP代理部署在目标应用服务器上，负责拦截并上报关键的运行时数据；IAST扫描器则基于这些数据进行智能分析，生成针对性的测试payload并验证漏洞存在性。

## 重点导读技术架构

### PART 01模块划分

整体系统由三个核心模块组成，各模块通过进程间通信协作：

**Preprocessor模块**作为HTTP服务器运行，监听指定端口接收来自OpenRASP代理的数据。该模块内置请求去重机制，基于LRU算法与插件式比对策略过滤重复请求，仅对新增请求进行记录入库。去重后的有效请求数据被写入MySQL数据库，供后续扫描模块使用。

**Scanner模块**为核心漏洞检测引擎，支持多实例并发执行。每个Scanner进程加载多个检测插件，插件负责生成特定漏洞类型的测试向量并发送到目标应用。Scanner通过异步协程实现高并发请求发送，单实例可配置最大20并发线程。检测结果实时写入数据库并支持断点续扫。

**Monitor模块**负责系统级监控与调度管理。该模块实时采集各Scanner进程的运行状态、CPU使用率、扫描速率等指标，根据预设策略动态调整并发参数。当检测到扫描请求失败率升高或CPU负载过高时，自动触发降速机制；当系统资源空闲时，自动提升扫描效率。此外，Monitor还处理与云端控制平台的通信，将扫描结果上报并接收配置指令。

### PART 02通信机制

模块间通信采用共享内存队列实现。Preprocessor接收到的请求数据通过命名队列发送给目标Scanner；Scanner返回的检测结果通过另一队列汇总至Monitor。所有模块共享同一份运行时配置，配置更新实时生效无需重启进程。

### PART 03数据模型

系统使用peewee异步 ORM 连接MySQL，每个扫描目标对应独立的数据库表。前置数据模型负责维护待扫描请求队列与已处理标记；报告数据模型记录发现的漏洞详情，包括请求/响应原始数据、漏洞类型、危害等级、修复建议等信息。

## 重点导读检测能力

### PART 04漏洞覆盖

该工具当前版本（v1.3）内置以下检测插件：

SQL注入检测插件（sql\_basic）针对SQL语句拼接场景，通过在用户输入中注入特殊字符序列并观察后台SQL解析行为变化判断是否存在注入点。支持GET、POST、JSON、Header、Cookie等各类型参数。

命令注入检测插件（command\_basic）检测通过用户可控输入构造系统命令的场景，通过投放多组测试payload验证命令是否可被注入。

目录遍历检测插件（directory\_basic）针对文件路径拼接类漏洞，测试多种路径穿越模式是否可读取任意文件。

Eval注入检测插件（eval\_basic）检测在代码执行函数中拼入用户输入的情况。

文件上传检测插件（fileupload\_basic）验证上传功能是否可被利用来写入恶意文件。

文件包含检测插件（include\_basic）针对本地文件包含与远程文件包含两种场景。

SSRF检测插件（ssrf\_basic）检测服务器端请求伪造漏洞，验证用户输入是否能控制服务端的请求目标。

XXE检测插件（xxe\_basic）针对XML外部实体注入问题。

文件读写检测插件（readfile\_basic、writefile\_basic）检测任意文件读取与写入漏洞。

### PART 05插件机制

扫描插件采用基类扩展模式实现，开发者可通过继承ScanPluginBase类并实现mutant与check方法添加新的检测逻辑。mutant方法负责生成测试请求序列，check方法负责分析响应判断漏洞是否存在。插件支持配置启用/禁用、白名单URL正则、扫描代理等参数。

### PART 06准确性保障

为降低误报率，系统采用多重验证机制。首先，Preprocessor层基于请求特征进行初步去重；其次，Scanner插件在发送测试payload时会设置特征标记防止误判；最后，检测结果写入前需经过去重插件验证，同一漏洞点仅报告一次。云端模式下，结果还会与云端知识库进行匹配校验。

## 重点导读部署方式

### PART 07环境要求

工具支持Linux与macOS系统，需使用Python 3.6及以上版本。依赖库包括aiohttp、aiomysql、jsonschema、peewee、peewee\_async、psutil、pymysql、tornado等。数据库必须使用MySQL 5.5.3及以上版本，且lower\_case\_table\_names参数需设置为0或2。

### PART 08安装配置

项目提供Docker Compose一键部署方案，包含IAST扫描器与云端控制平台两个服务组件。单机部署时需提前安装MySQL并创建数据库，执行setup.py完成Python包安装后，通过config命令生成配置文件并调整数据库连接参数与监听端口。

### PART 09启动流程

启动命令支持前台与后台两种模式。初次启动需配置OpenRASP代理端的fuzz\_server参数指向IAST的HTTP监听地址，使代理能够将运行时数据回调至扫描器。配置完成后通过start命令启动所有模块。

## 重点导读高级特性

### PART 10扫描速率动态调整

系统内置智能调度算法，根据CPU使用率与请求成功率自动调节扫描并发度。CPU持续高于98%阈值时降低并发；CPU低于85%且扫描未满载时提升并发。失败请求增多时触发保守策略，防止对目标系统造成压力。

### PART 11云端管理

可选的云端控制平台提供统一的任务管理、结果展示、配置下发功能。扫描结果实时同步至云端，支持多用户协作与历史数据查询。云端还维护漏洞知识库，提供修复建议与漏洞详情参考。

### PART 12多目标支持

单个IAST实例可同时管理多个扫描任务，通过host\_port标识区分不同目标。各目标的扫描配置独立维护，包括插件开关、扫描速率限制、白名单规则等参数。

## 重点导读项目信息

本公众号非项目作者，仅做技术分享。

本文介绍的项目开源地址如下：

```
https://github.com/baidu-security/openrasp-iast
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uq9u8m0Jlvdx3GZWHiaDyDQE1iccjicmXiaWicnRUXzq6PNlRRYVTpaTSdz0RPNia5mfh5TfT8nibEeP0teGjNQE7Abwerl80QPx6okKk/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UopddSh5rTn00icmK3AmmcwYNwWoEBh9H5SK72KLsib16C6fU6anJuyO9WQSKQb4I4QVSHRGUrzWLsQmCnxaAJgc9F7j0ibuFn89Y/640?from=appmsg)

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