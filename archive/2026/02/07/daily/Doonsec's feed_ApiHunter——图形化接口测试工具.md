---
title: ApiHunter——图形化接口测试工具
url: https://mp.weixin.qq.com/s/9eNlcvJVcpxa7GQyf2kOzQ
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:29:14.401479
---

# ApiHunter——图形化接口测试工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qqiaD4wiajgFzbqnb1aK5z8cuVtwUFg4MydDH15rXbZP46ibSVFiapSCbjGDfw6Hsr2jcr6FNjqYd9I6GRYUKvzFZsveQ0oj1UMibPcqcf2WwE3I/0?wx_fmt=jpeg)

# ApiHunter——图形化接口测试工具

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

# 项目地址：

https://github.com/11firefly11/ApiHunter

# ApiHunter 技术文档

## 1. 项目概述

**ApiHunter** 是一款开源的 API 接口自动化安全测试工具，专为渗透测试人员和安全研究人员设计。该工具支持 Swagger/OpenAPI 文档一键解析，能够自动提取接口端点、智能填充参数并批量发送请求，大幅提升 API 安全测试效率。

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFzd9mic9vg4DBXmRVqrdEyZUfQxhHTsy4nbjI56bHEbnbbeNImkIiaXQfXibHgT7LZTu90ehwLnGMFicDia7VicW6WYAK3dENgEUBUd8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFx6BibpZS1qtqsrucxdqOyo2IoLNALdAKr1hAMqP4OCPkN10OgwfObLVia4Vx4Rzncmay6ib2MfFib5ypllKpZ5sUbgicgwmmL9q3ro/640?wx_fmt=png&from=appmsg)

**GitHub 仓库**: https://github.com/11firefly11/ApiHunter

---

## 2. 核心功能

### 2.1 文档解析引擎

表格

| 功能模块 | 支持格式 | 说明 |
| --- | --- | --- |
| **Swagger/OpenAPI 解析** | Swagger 2.0 / OpenAPI 3.0 | 自动解析 JSON 格式文档，提取完整接口定义 |
| **ASP.NET Help Page 解析** | HTML 页面 | 专门针对 .NET Web API 的文档解析引擎 |
| **WSDL/WADL 解析** | XML 格式 | 支持 Web Services 描述语言文档提取（v2.0+ 新增） |

### 2.2 智能测试引擎

* **POST 智能填充与多格式测试**

+ URL 参数模式 (Query String)
+ JSON Body 模式 (application/json)
+ Form Body 模式 (x-www-form-urlencoded)

+ 自动识别 `id`, `email`, `phone` 等参数类型并智能填充测试值
+ 针对 POST/PUT 请求自动生成三种数据包格式：
+ 支持自定义参数值（如 `userid:100,username:test`）

* **自动化漏洞检测**

+ **文件上传检测**：智能识别包含 `upload`/`file` 关键词的接口，自动构造 `multipart/form-data` 请求，上传 XSS 测试文件（.html）和普通文本文件
+ **SQL 注入探测**：内置多数据库报错指纹库（MySQL/Oracle/MSSQL/PostgreSQL），自动识别注入点

### 2.3 敏感信息检测

内置 **100+** 条高精度检测规则，覆盖：

表格

| 检测类别 | 具体内容 |
| --- | --- |
| **云服务密钥** | AWS Access Key、阿里云 AccessKey、腾讯云 SecretKey 等 |
| **访问令牌** | JWT Token、GitHub Token、API Key、Bearer Token 等 |
| **数据库连接** | MySQL/PostgreSQL/MongoDB/Redis 连接字符串 |
| **个人隐私信息** | 手机号、身份证号、邮箱地址、银行卡号等 |
| **系统敏感信息** | 内网 IP、服务器路径、堆栈跟踪信息等 |

检测结果在响应中以**红色高亮**显示，便于快速定位。

### 2.4 智能去重与过滤

* **指纹去重引擎**：基于 **状态码 + 响应长度** 生成指纹，有效过滤大量重复的 404/500 错误页面
* **状态码过滤**：支持自定义状态码黑名单，屏蔽无价值结果
* **响应长度过滤**：可设置长度阈值，过滤空响应或固定错误页面

---

## 3. 安全机制

### 3.1 安全模式（Safety Mode）

表格

| 模式 | 行为描述 | 适用场景 |
| --- | --- | --- |
| **🔒 安全模式** | 拦截 DELETE/PUT 方法；跳过包含 `delete`/`remove`/`drop` 关键词的接口 | 生产环境、未授权测试 |
| **⚡ 普通模式** | 执行所有方法（遵循方法黑名单）；仅跳过用户自定义黑名单接口 | 开发/测试环境、深度评估 |

### 3.2 防护机制

* **高危操作拦截**：防止误删数据，保护生产环境
* **自定义黑名单**：支持用户自定义接口关键词黑名单
* **请求频率控制**：内置延迟机制，避免对目标系统造成过大压力

---

## 4. 网络与代理支持

表格

| 功能 | 说明 |
| --- | --- |
| **代理协议** | 支持 HTTP/HTTPS/SOCKS5 代理 |
| **流量转发** | 可配合 Burp Suite 进行流量拦截与分析 |
| **自定义请求头** | 支持设置 Cookie、Authorization、User-Agent 等 |
| **鉴权绕过** | 通过自定义 Header 轻松测试带鉴权的接口 |

---

## 5. 交互式操作

### 5.1 数据包重发

* **双击结果行**：查看标准 HTTP 格式的完整数据包
* **即时编辑**：支持修改请求头、请求体
* **一键重发**：编辑后立即重新发送请求
* **响应格式化**：自动格式化 JSON/XML 响应，支持语法高亮

### 5.2 结果导出

* 支持导出为 **Excel 格式**
* 包含完整的请求/响应信息
* 便于生成测试报告和二次分析

---

## 6. 使用指南

### 6.1 环境要求

* **操作系统**：Windows（提供 `.exe` 可执行文件）
* **运行方式**：开箱即用，无需额外依赖

### 6.2 快速开始

1. **启动程序**

* 双击 `ApiHunter.exe` 启动图形化界面

2. **配置目标**

   **方式一（单目标测试）**：

   **方式二（文档批量导入）**：

* 切换到"接口文档"区域
* 输入 Swagger/ASP.NET/WSDL 文档地址
* 点击【导入】→【Swagger】

* 输入目标 URL 和接口路径
* 点击【测试】按钮

3. **查看结果**

* 扫描结果实时显示在主界面
* 敏感信息自动红色高亮标记
* 双击行查看详情，右键支持导出/复制

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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