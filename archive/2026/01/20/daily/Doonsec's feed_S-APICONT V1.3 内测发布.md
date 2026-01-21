---
title: S-APICONT V1.3 内测发布
url: https://mp.weixin.qq.com/s/1bMtKQBHkiJQcH9hy44E3Q
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:27.151816
---

# S-APICONT V1.3 内测发布

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/C7NK6Uic3BZQvasqQthJYfBCrsvA7x39kCJS4QlibL5djchMUqhtsHNPicXzksOBVFKlV5PccH8REE8WDibCewyxRQ/0?wx_fmt=jpeg)

# S-APICONT V1.3 内测发布

狗头网络安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于夜深了Sec
，作者smile

![](http://wx.qlogo.cn/mmhead/iahdQicCC5VBT1HRTNQy1bCNu35kP620PXbEcQzNe3FtEibPjtchQsTibpv2QulxgcxsxHjj0vx4k4U/0)

**夜深了Sec**
.

主要发布最新活动信息！

# S-APICONT V1.3 发布公告

📋 V1.3更新内容

✅ 新增测试范围选择（只测未测试的/全部重新测试）

✅ 新增提取 API 范围选择（提取全部/只提取新增）

✅ 新增清空结果功能（清空 API 列表）

✅ 修复一级路由在请求包中不生效的问题

✅ 修复批量替换测试后请求显示不正确

✅ 修复测试过程中表格选中状态丢失

✅ 修复关于插件面板显示问题

✅ 优化取消批量测试时界面自动跳转

✅ 优化全部重新测试时先清零状态码

## 🎉 版本发布

![](https://mmbiz.qpic.cn/sz_mmbiz_png/C7NK6Uic3BZQvasqQthJYfBCrsvA7x39kKBsa7CftsAfuUiceqQWchDaY4SKjPHZKBgtrrGubgc0GiaDauK2obljQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/C7NK6Uic3BZSENEbozhERULIibrgQhjxMbc59ryPviaQtsSVwiadk7ibusAZqibXY3IWr6cZMGTZ7fXbWpmiceyg8MItA/640?wx_fmt=png&from=appmsg)

\*\*S-APICONT\*\* 是一款专为安全研究人员设计的 Burp Suite API 收集与测试插件，帮助您快速发现和测试 Web 应用中的 API 接口。

---

## 🔥 核心亮点

### 📡 智能 API 收集

- 自动监听浏览器流量，实时提取 API 接口

- 支持 Vue/React/Angular 等主流框架路由解析

- 智能识别一级路由变量，自动拼接完整路径

### 🧪 批量测试

- 一键批量访问所有发现的 API

- 可配置请求间隔，避免触发 WAF

- 支持 GET/POST/PUT/DELETE 等多种 HTTP 方法

### 🔄 Intruder 式替换测试

- 使用 `§` 标记 Payload 位置

- 将标记位置替换为所有 API 路径进行批量测试

- 快速发现未授权访问漏洞

### 🔐 敏感信息检测

自动识别响应中的敏感数据：

- 邮箱、手机号、身份证号

- JWT Token、API Key

- 数据库连接字符串

- 内网 IP、文件路径

### 📊 多视图响应分析

- 美化视图（JSON/XML 格式化）

- Raw 原始数据

- Hex 十六进制

- 页面渲染预览

- MarkInfo 敏感信息高亮

---

## 📥 下载安装

1. 下载 `S-APICONT内测V1.3.jar`

2. Burp Suite → Extensions → Add

3. 选择 JAR 文件，完成安装

---

## 🚀 快速开始

```

1. 输入目标域名 → 点击「设置目标」

2. 浏览器访问目标网站

3. 查看自动收集的 API 列表

4. 点击「批量测试」验证接口

5. 勾选「只显示成功」筛选有效接口

```

---

## 📋 部分功能展示

全自动模式，师傅浏览，插件自动获取API，路由，自动扫描！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/C7NK6Uic3BZSENEbozhERULIibrgQhjxMbcZx1J2QqKgM5f6g5kOLYKIp0CuNPcMW0rRt5T9WfqeklsvtHbEMqKg/640?wx_fmt=png&from=appmsg)

高级自定义，可以随意更改数据包，更加导入自定义接口等进行测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/C7NK6Uic3BZQHUWcFamOEAC8AL2kUKiaHqJjBaibjGmLDLHebGq24Comfu5gHkkx3VibRCsx8NDKqMa18Nkl1IaHfQ/640?wx_fmt=png&from=appmsg)

## 获取插件关注公众号发送：0120

## ⚠️ 免责声明

本工具仅供安全研究和授权测试使用，请勿用于非法用途。

---

\*\*如果觉得好用，请点个 Star ⭐ 支持一下！\*\*

内测阶段，如有BUG，插件等问题，或者好的建议进群反馈:群满+VAMidnightCafe邀请

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/C7NK6Uic3BZSENEbozhERULIibrgQhjxMbRtWhuMX527ZYPruGDJNc3RGIsahou5HWpd1ia6BE2ssNfQ0dcqdnTrw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Y2hIPt3xOsIHMZW8Mv8Qo5k2KwYaLyqLraTa6M1jBTazkBrQjIR7FgswrlBS9wlk5HSPWdoKwZ8XUbkePpViayA/0?wx_fmt=png)

狗头网络安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Y2hIPt3xOsIHMZW8Mv8Qo5k2KwYaLyqLraTa6M1jBTazkBrQjIR7FgswrlBS9wlk5HSPWdoKwZ8XUbkePpViayA/0?wx_fmt=png)

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