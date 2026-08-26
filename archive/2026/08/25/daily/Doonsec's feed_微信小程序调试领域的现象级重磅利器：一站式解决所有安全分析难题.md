---
title: 微信小程序调试领域的现象级重磅利器：一站式解决所有安全分析难题
url: https://mp.weixin.qq.com/s/UKCxKKLxZ3cqQUi3FN6paw
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:03:49.321423
---

# 微信小程序调试领域的现象级重磅利器：一站式解决所有安全分析难题

# 微信小程序调试领域的现象级重磅利器：一站式解决所有安全分析难题

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全声明：本工具仅供安全研究与学习使用，请勿用于未授权的目标，使用者须自行承担相关法律责任。

## 重点导读概述

First 是一款面向微信小程序安全研究的专业调试平台，基于 Frida 进程注入与 Chrome DevTools Protocol 代理桥接技术实现。开发者无需复杂配置，即可对小程序运行时行为进行深度监控、函数调用拦截以及数据重放攻击。

该工具支持 macOS 与 Windows 双平台，兼容微信多个版本。通过集成 MCP Server 与云函数动态捕获机制，研究人员能够快速定位小程序业务逻辑漏洞，显著提升逆向分析效率。

## 重点导读核心架构

### PART 01设计模式

* Frida 进程注入层
* CDP 代理桥接层
* Protobuf 序列化层
* WebSocket 通信层

### PART 02技术组件

| 组件 | 功能 |
| --- | --- |
| DebugEngine | 核心调度引擎，协调注入、代理、通信三大模块 |
| DebugMessageBus | 消息总线，桥接调试服务器与 CDP 代理服务器 |
| Frida Integration | 跨平台进程发现、脚本注入、消息回调处理 |
| Protobuf Codec | 微信小程序调试协议序列化与反序列化 |
| UserScript Manager | 自定义脚本加载与管理，支持即时注入 |

### PART 03端口配置

* 调试服务器：9421（小程序硬编码，不可修改）
* CDP 代理服务器：62000（默认）

## 重点导读功能特性

### PART 04云函数捕获

Hook wx.cloud.callFunction，实现云函数调用的全程监控。支持参数拦截、修改与重放，可用于测试云端接口安全性。

### PART 05wx.\* API 监控

覆盖 login、request、getUserProfile 等常用 API，自动记录调用参数与返回结果，便于业务逻辑分析。

### PART 06路由枚举

自动枚举小程序页面路由，检测导航守卫状态，辅助发现未授权访问路径。

### PART 07wxapkg 处理

* 解密微信小程序包文件
* 解包为可读源文件
* 敏感信息扫描

### PART 08MCP Server

集成 MCP 协议，支持 AI 辅助分析，可自动解析小程序行为并生成分析报告。

### PART 09脚本扩展

支持 UserScript 自定义注入，可编写 JavaScript 脚本实现特定监控逻辑。

![主界面](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqpVQwtjgUH95eIlwNSXCB3ZVNMpXmKYnoLicThWS7Py1X7tqEic8ia50zJjRdKIXPcU0LBADOm1psZPSHqLAfNr9udGEia4ric07r4/640?from=appmsg)

主界面

## 重点导读支持平台

### PART 10Windows

微信推荐版本：4.1.10

支持的 WMPF 版本涵盖：11581、11633、13331、13341、13487、13639、13655、13871、13909、14161、14199、14315、16133、16203、16389、16467、16771、16815、16965、17037、17071、17127、18055、18151、18787、18891、18955、19027、19201、19977 等多个版本。

### PART 11macOS

微信推荐版本：4.1.10

支持的 WMPF 版本涵盖：19978、17078、18152、18788 等多个版本。

### PART 12环境要求

macOS 系统如遇 Frida 注入报错，需关闭 SIP 系统完整性保护或对微信应用进行强制重签名。

## 重点导读快速启动

1. 启动 First 程序
2. 点击启动按钮，Frida 自动注入微信进程
3. 在微信中打开目标小程序
4. 通过 DevTools 或云捕获界面进行调试分析

## 重点导读项目结构

```
First/
├── main.py              # CLI 入口
├── gui.py               # GUI 界面
├── src/
│   ├── cli.py           # 命令行参数解析
│   ├── engine.py        # 核心调试引擎
│   ├── codex.py         # 消息封装/解封
│   ├── navigator.py     # 路由导航
│   ├── extractor.py     # wxapkg 提取器
│   ├── wxapkg.py        # 小程序包处理
│   ├── userscript.py    # 用户脚本管理
│   └── third_party/     # 第三方协议定义
├── frida/
│   ├── hook.js          # 注入脚本
│   └── config/          # 版本偏移配置
├── hook_scripts/        # 自定义 Hook 脚本
└── 启动.bat / 启动.sh    # 平台启动脚本
```

## 重点导读技术实现

### PART 13调试协议

微信小程序采用 WARemoteDebug 协议进行调试通信，数据通过 Protobuf 序列化传输。First 项目在 third\_party 目录中完整实现了该协议的定义与解析逻辑。

### PART 14CDP 桥接

小程序运行时通过自定义协议与调试服务器通信，First 将其转换为标准 Chrome DevTools Protocol，使得研究人员可直接使用 Chrome DevTools 进行调试。

### PART 15进程发现

* Windows：通过遍历 WeChatAppEx.exe 进程，根据 PPID 频率定位主进程
* macOS：通过 pgrep 结合 Info.plist 版本读取定位目标进程

## 重点导读更新机制

支持偏移量与 Skills 在线更新，确保对不同微信版本的兼容性。

## 重点导读项目地址

本文介绍的项目开源地址如下：

```
https://github.com/Spade-sec/First
```

本公众号非项目作者，仅做技术分享。

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uo1wE3hKCgVzibqN0YxFjLwB36FkvDZ96bYicCFu45j8YXQZibplhQfsEHe9wUnr8ibLRlatmsXAbTlHxnGoEjAmO15BeAfDYSBxJ4/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UowzTtibOnrPRQc2VvBuBhE8Fz5oY8uVjvHIX4PmS1UyzqAbhHgUWZbiaxdonMh3iavlKhHhz0styFeTZgx4eicFc2rQnAYBBKMchw/640?from=appmsg)

预览时标签不可点

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