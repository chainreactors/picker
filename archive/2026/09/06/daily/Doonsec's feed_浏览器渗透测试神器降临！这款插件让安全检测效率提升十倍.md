---
title: 浏览器渗透测试神器降临！这款插件让安全检测效率提升十倍
url: https://mp.weixin.qq.com/s/VZ3Xq-OffepJFVAw-GH_tg
source: Doonsec's feed
date: 2026-09-06
fetch_date: 2026-09-07T06:48:16.352929
---

# 浏览器渗透测试神器降临！这款插件让安全检测效率提升十倍

# 浏览器渗透测试神器降临！这款插件让安全检测效率提升十倍

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全声明：本工具仅供授权安全测试与学习研究使用，使用者须遵守相关法律法规，严禁用于任何非法入侵、数据窃取等行为。

黄油曲奇是一款面向安全测试人员与开发者的集成化浏览器渗透测试插件，基于 Chrome/Edge 浏览器扩展机制构建，版本号 1.2.0，采用 MIT 开源协议发布。该插件将信息收集、信息提取、XSS 测试、SQL 注入检测、端点扫描、云存储安全检测、Shodan 主机情报查询及综合辅助工具八大功能模块整合至统一界面，目标是让 Web 应用安全评估工作在同一浏览器标签页内一站式完成。

## 重点导读技术架构

### PART 01扩展机制

插件基于 Manifest V3 规范开发，核心组件包括后台 Service Worker、前端 Popup 页面、Content Script 脚本以及独立功能模块。运行时环境为 Chrome 88+ 或 Edge 88+，支持 Windows、macOS、Linux 全平台。

### PART 02模块组织

```
src/
├── background.js          # 后台服务脚本
├── popup.html/popup.js    # 插件主界面
├── content.js             # 页面内容注入
├── content_scripts/       # 端点检测、DOM XSS、原型污染等
└── modules/               # 信息提取、编码解码、云存储检测
```

内容脚本层采用多文件分工模式，分别处理端点发现、DOM XSS 检测、敏感目录扫描、原型污染追踪、跨域消息监控及重定向漏洞识别等专项任务。

### PART 03云存储检测架构

云存储检测模块采用供应商检测器 + 风险扫描器双层设计：

* `base-detector.js`：通用检测基类
* `detectors/`：分别实现阿里云、腾讯云、华为云、AWS、七牛云、青云、又拍云、京东云、金山云、天翼云十家厂商的 API 特征识别
* `scanner.js`：存储桶遍历、PUT 上传、DELETE 删除、ACL 可读写、Policy 可读写六类风险检测逻辑
* `storage.js`：扫描结果持久化与历史记录管理

## 重点导读核心功能

### PART 04信息收集

支持 User-Agent 管理、Cookie 管理、HTTP 头部查看、敏感信息提取、框架指纹识别、蜜罐检测以及 Fuzz 扫描。其中 Fuzz 字典文件存放于 `data/` 目录，用户可自定义维护。

![Fuzz 扫描界面](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrnKKIQyuAYsR4yoZ9q3IoK29LsqjAicQJhFUop0wsRcibeibCVM0pWhfQE78Tlxg1CpgeOPmPOWlBPvEn1oX4oib4qLW0aIfnfPgE/640?from=appmsg)

Fuzz 扫描界面

![Fuzz 扫描结果](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoqtNlo550oBqu55QRSeKXicJgvfhU5PMN6KV0S0A7rXUtqpX41jQFoxRH0mE4bonvictDTCmE5Z7NT5h9iarIiaib7rTXy4YUiaTZvk/640?from=appmsg)

Fuzz 扫描结果

### PART 05信息提取

从页面源码中批量提取域名、API 路径、JS 文件引用、URL 参数、Cookie、Source Map 文件等关键资源。同时集成 URL、Base64、HTML、HEX、Unicode 五种编码解码转换，以及自定义正则表达式提取功能。

![信息提取界面](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqMia8T4pqmG1nZRwu48Z2odRwJicI5KfJia5e9ibalHCrpatw0CfUxGnzfEqUJY05StOx6fFBbqsofiaDkLQY4CX5XKJTejsKRQTos/640?from=appmsg)

信息提取界面

![自定义正则提取](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UpibevAY8AABu7iaBnj63BiaicDXDlLVnpzBR0jhwtnXcfIZzk3P8RZYbE8S4xyzTYEgHrVS41iaIydVmSY9XyZmvS0FoXUFh0icDYx8/640?from=appmsg)

自定义正则提取

### PART 06XSS 测试

提供批量参数填充、CSP 策略读取、参数自动提取以及 HTML/URL/HEX 编码转换工具箱，辅助测试人员快速构造与绕过 XSS 过滤机制。

### PART 07SQL 注入测试

集成 SQL HackBar 工具条，支持多种 HTTP 请求方法与注入入口选择，内置响应分析模块与 Curl 命令生成功能，方便将测试用例导出至其他工具执行。

![SQL 注入测试界面](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UodibX7iaCeVV08mWs66Ct70LA7otPZ7x28qTBCFmgLQSukictf3ljAZaff2Wa0upjZSpESszHX7CKPHcLyGP9zn6EuBgcWP0IAHA/640?from=appmsg)

SQL 注入测试界面

### PART 08端点安全扫描

核心扫描引擎位于 `content_scripts/endpoint-finder.js`，通过正则匹配从页面 JavaScript 资源中智能识别 API 端点路径，支持模板变量过滤与危险操作路径识别。扫描结果自动去重并展示完整 URL 列表，支持单独复制与后台新标签页打开操作。

![端点扫描界面](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UricoicyoeTWfico8uLnttdicNFvLRvm2NV3iaBVq0ytzWBsdELhicL65T89yLFgqyvdBZiaKXMmTqR4fxDu2QMDcx3Iicgx4SCRARkvVM/640?from=appmsg)

端点扫描界面

### PART 09云存储检测

支持主动扫描与被动检测两种模式，可检测存储桶可遍历、PUT 上传、DELETE 删除、ACL 读写、Policy 读写等六类风险场景。扫描统计面板展示发现 URL 数量、漏洞数量及云厂商分布，并提供 JSON 格式结果导出。

![云存储检测界面](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Up7S5kE7m5cbcO33GSbWVHYNx2GsVLtQ0rGeoY8V9902pdo8GEu62xib1YyJGjEDthQkYud3mA9cRZ2UJ2Q22EeSerz6jTHKQfY/640?from=appmsg)

云存储检测界面

### PART 10Shodan 主机情报

输入目标域名即可查询对应主机的开放端口、安全漏洞等公开情报信息，并提供详情页面跳转链接。

### PART 11辅助工具

包含 Vue 未授权访问快速检测、JavaScript 辅助工具、批量 URL 打开工具及 URL 列表管理功能。其中 Vue 检测模块位于 `modules/vue-detector.js`，支持 Vue 2/3 版本识别、Router 实例分析、路由守卫清除与 meta.auth 字段修改。

![辅助工具界面](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uq2N9TMmbY7VM2V7L0vjv4vCdGiaG0IbvJ4u31nGOjgeD70riacpaGxe8Gnib8SgFA9kOjYrtQu3KrbLrIGTQglyCGz3lV7dCZEjE/640?from=appmsg)

辅助工具界面

## 重点导读技术特点

* **多厂商覆盖**：云存储检测支持国内主流云平台及 AWS
* **被动主动双模式**：云存储与端点扫描均支持无痕被动检测与主动深度扫描
* **结果可导出**：支持 JSON 格式批量导出
* **字典可扩展**：Fuzz 字典存放于独立目录，用户可自行维护
* **全平台兼容**：Windows、macOS、Linux 均可运行

## 重点导读安装使用

1. 克隆或下载项目至本地
2. 打开 Chrome/Edge，进入 `chrome://extensions/`
3. 开启开发者模式
4. 点击「加载已解压的扩展程序」，选择项目根目录
5. 插件图标将自动出现在浏览器工具栏

首次使用时点击扩展图标，选择对应功能模块，按界面提示操作即可。

本公众号非项目作者，仅做技术分享。

本文介绍的项目开源地址如下：

```
https://github.com/EdinLyle/Butter_Cookie
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqibrJAwzBVibP4AVTFzQ8adDkicYmRS83d0ibgDKOdqsqQRuWoa3GOE7ygrde3fWibHQnrgYlpvrx8Ct0Q1hPr22I02EV2jZaRwSbk/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Ur0poaAZBicHAoiaa1Ax9szGibaChia968QYjt0hm9Tv2rLiaicV2VoMib3kzQsGG3lQkOn5mYTXLEpRUJdYu3XjLd3RLibgWiag04cflyI/640?from=appmsg)

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