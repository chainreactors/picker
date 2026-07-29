---
title: 微信小程序安全审计领域的颠覆性工具诞生！23个MCP工具让AI自动完成渗透测试
url: https://mp.weixin.qq.com/s/KbAz9l7yLOCPR8Pviqn6Jw
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:01:26.731561
---

# 微信小程序安全审计领域的颠覆性工具诞生！23个MCP工具让AI自动完成渗透测试

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0Uou1U46f8MYO2fJ6xeBQxCU7vXBaPCof7AOv85BqGPJ9iamX6lw8nlhFLkO2NV8Q46hPqdrZxvBlkLdmzRKvq14DJaxibVPhMuwo/0?wx_fmt=jpeg)

# 微信小程序安全审计领域的颠覆性工具诞生！23个MCP工具让AI自动完成渗透测试

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本工具仅供安全研究与学习使用，请勿用于未授权的目标，使用者须自行承担相关法律责任。

## 重点导读简介

First 是一款专为微信小程序安全调试设计的开源框架，基于 Frida 动态注入技术与 CDP（Chrome DevTools Protocol）代理协议构建。该框架支持 Windows 与 macOS 双平台，提供 GUI 与 CLI 两种运行模式。核心亮点在于完整的 MCP（Model Context Protocol）工具集封装，共计 23 个标准工具函数，允许 AI Agent 通过自然语言完成完整的小程序安全测试流程，包括路由枚举、凭证提取、网络请求 Hook、云函数审计、敏感信息扫描等操作。

## 重点导读核心技术架构

### PART 01Frida 动态注入

框架通过 Frida 将调试代理注入微信客户端进程，实现对小程序的动态监控与控制。注入机制支持 wxapkg 包文件的解密解包、网络请求拦截、JavaScript 上下文篡改等底层操作。核心注入逻辑封装于 `frida/` 目录，hook 脚本存放于 `hook_scripts/` 目录。

### PART 02CDP 代理桥接

CDP 代理层作为桥梁，将微信小程序的调试协议转换为 Chrome DevTools 可识别的标准协议。开发者可直接使用 Chrome DevTools 连接 `ws://127.0.0.1:62000` 进行断点调试。代理层实现位于 `src/engine.py`，包含会话管理、帧枚举、对象查询等核心功能。

### PART 03MCP Server 封装

MCP Server（`mcp_server.py`）将全部调试能力以 JSON-RPC 2.0 协议暴露为标准 MCP 工具。Server 支持 stdio 与 SSE 两种传输模式，可与 Claude Desktop、Cursor、VS Code Copilot 等 AI 工具集成，实现自然语言驱动的自动化测试。

### PART 04模块结构

| 模块 | 路径 | 功能 |
| --- | --- | --- |
| engine | src/engine.py | 调试引擎核心，CDP 会话管理 |
| navigator | src/navigator.py | 页面路由枚举与导航控制 |
| extractor | src/extractor.py | 敏感信息提取与存储读写 |
| js\_analyzer | src/js\_analyzer.py | JavaScript 源码静态分析 |
| wxapkg | src/wxapkg.py | wxapkg 包解密解包 |
| cloud\_audit | src/cloud\_audit.py | 云函数调用监控与审计 |
| userscript | src/userscript.py | UserScript 加载与管理 |

## 重点导读核心功能解析

### PART 05路由枚举与导航

`get_all_routes` 工具自动枚举小程序所有已注册页面路由，并标注 tabBar 页面。`navigate_to_route` 支持指定路由跳转，自动识别 tabBar 页面并使用 `switchTab` 接口。该功能基于 `nav_inject.js` 实现，通过 Hook AppBrandPage 构造器获取路由注册信息。

### PART 06凭证提取

`read_storage` 与 `dump_all_storage` 分别实现单键读取与全量导出本地存储。`get_user_credentials` 从存储与 globalData 中自动提取 token、openid、session 等认证凭据。提取逻辑位于 `src/extractor.py`，支持自动识别常见凭证字段命名模式。

### PART 07网络请求监控

`start_network_capture` 安装 `wx.request` Hook，捕获所有小程序发出的 HTTP 请求。`get_captured_requests` 获取捕获结果列表，支持保留或清空记录。`replay_request` 支持在小程序上下文内重放或构造 HTTP 请求，用于测试鉴权绕过与参数注入。

### PART 08云函数审计

`enable_cloud_function_hook` 注入 Hook 监控所有 `wx.cloud.callFunction` 调用。`get_cloud_calls` 获取捕获的调用记录，包含函数名与参数。`call_cloud_function` 支持直接调用指定云函数并自定义参数，用于测试鉴权缺失与越权漏洞。云函数 Hook 脚本为 `cloud_audit_inject.js`。

### PART 09静态分析

`decompile_wxapkg` 解密解包 wxapkg 小程序包文件到 `output/` 目录。`scan_sensitive_info` 扫描已解包源码，检测 API Key、JWT Secret、IP 地址、云存储配置、手机号、身份证等敏感信息。`find_api_endpoints` 从 JavaScript 源码中提取所有 HTTP(S) URL 与 API 路径。

### PART 10鉴权绕过

`bypass_auth_check` 集成常见鉴权绕过手法的自动化探测，包括 token 伪造、admin 角色提权、登录态检查跳过等策略。

## 重点导读截图预览

### PART 11主界面

![主界面](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uqr8Bbz7fvibXeFrliam36Sv59nTFkENoiaTGtTJjbicCguKExoO6Tib4ljrzWuS2SFcQZ7MuN3cV00iaJxwicdgSzugFIQG7uc66mppU/640?from=appmsg)

主界面

### PART 12路由导航

![路由导航](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UrViaNzRxReRBdMMOXydyqQqon1ibIgFb7l57icIicVWcpd7AuxBLo1d9jHwrCBTN55cn0ESTelf8zStKZN5l11pckfibuxicDLu0zzs/640?from=appmsg)

路由导航

### PART 13云函数分析

![云函数分析](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UruMByy5wRraPt6ib1z26qmqYrEwWXNkHyxa9HAN4L4ax6xjvGK2UZ6oficUuP8bgIFcR99iccoIRw3RVTf3QMAEJHcZOFntzcQrI/640?from=appmsg)

云函数分析

### PART 14调试开关

![调试开关](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UpBqhASF1ibsd2Xic9C986iatEAJgpkuBBxL6Uzicq7CGEfIftj7odwice5oZy67Mr6jSLQLpocECgtuOgfsotwDDeHKV6qc3lBSoRg/640?from=appmsg)

调试开关

### PART 15敏感信息提取

![敏感信息提取-1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Ur1tVBHNH4stwrKnMrHE1UPl95kXlEvw7RYWnCVRnfjat3w9iaRTVjuiau1RkViaYwfXV74aRHWhCpQLiaAh7giaibd8BeygRQ6ictDa8/640?from=appmsg)

敏感信息提取-1

![敏感信息提取-2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoGnRBr9nUb7u9O99RhWhHfeTnj2LXS5tqM9umwop86lX0TMiaAPSYDofIVXCV40NpxXcEMf5s5E8H8A7R5zkvKbE0n85TiaXl44/640?from=appmsg)

敏感信息提取-2

![敏感信息提取-3](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UpnWdmd0SgXxoc9dNWB5Qeowbe9MoiaHKF1ZfdicVm4rEw39CKNEZic5g0EA9ZCiboqrIAlLWibkrZGfIZibGcibjhH5o3hJJ2ZyicLgr4/640?from=appmsg)

敏感信息提取-3

## 重点导读MCP 工具速查

| 类别 | 工具 | 功能 |
| --- | --- | --- |
| 连接 | check\_connection | 检查框架运行状态与 CDP 连接 |
| 信息 | get\_miniapp\_info | 获取小程序基本信息 |
| 信息 | get\_current\_page | 获取当前页面状态 |
| 信息 | get\_app\_global\_data | 读取 globalData |
| 路由 | get\_all\_routes | 枚举全部页面路由 |
| 路由 | navigate\_to\_route | 跳转指定路由 |
| JS | execute\_js | 执行任意 JavaScript |
| JS | inject\_hook\_script | 注入完整 Hook 脚本 |
| 存储 | read\_storage | 读取指定 key 值 |
| 存储 | dump\_all\_storage | 导出全部存储 |
| 存储 | get\_user\_credentials | 提取认证凭据 |
| 网络 | start\_network\_capture | 安装抓包 Hook |
| 网络 | get\_captured\_requests | 获取捕获请求 |
| 网络 | set\_request\_headers | 注入自定义 HTTP 头 |
| 网络 | replay\_request | 重放/构造请求 |
| 云函数 | enable\_cloud\_function\_hook | 监控云函数调用 |
| 云函数 | get\_cloud\_calls | 获取云函数记录 |
| 云函数 | call\_cloud\_function | 直接调用云函数 |
| 静态 | decompile\_wxapkg | 解密解包 wxapkg |
| 静态 | list\_decompiled\_apps | 列出已解包应用 |
| 静态 | scan\_sensitive\_info | 扫描敏感信息 |
| 静态 | find\_api\_endpoints | 提取 API 端点 |
| 鉴权 | bypass\_auth\_check | 尝试鉴权绕过 |

## 重点导读环境要求

| 依赖 | 版本要求 |
| --- | --- |
| Python | >= 3.10 |
| frida | >= 17.0.0 |
| websockets | >= 12.0 |
| protobuf | >= 4.0.0 |
| PySide6 | >= 6.5.0 |
| pycryptodome | 最新版 |

## 重点导读支持的微信版本

Windows 平台推荐微信版本 **4.1.0.30**，macOS 平台推荐版本 **4.1.7.30**。框架支持多版本兼容列表涵盖从 11581 到 19201 的多个 WMPF 构建版本。

## 重点导读项目开源地址如下：

```
https://github.com/notstarr/First
```

本公众号非项目作者，仅做技术分享。

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqJs8Go7QAazS7467FeegNWPVsTY1qWQtrdzk2fOxI9iado8VFeNXFs6uh9tjQLOgDGzcCOQZP87yJXcwN1ibk2kEqkHZiakotrUE/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UoSekXNHILE2J9WYgiczGVQ5DMfw7jVPs3FU7klsY2QS4Fbz8PCpbnKH1GVH4meznIgEs7ZQzJr0Iaa4xRhs4axoKXaYcUXqYvc/640?from=appmsg)

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