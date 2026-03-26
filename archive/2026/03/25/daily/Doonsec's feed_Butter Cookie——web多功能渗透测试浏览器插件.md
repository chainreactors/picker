---
title: Butter Cookie——web多功能渗透测试浏览器插件
url: https://mp.weixin.qq.com/s/FZy2gRQTudabTiC0HFkzCA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:02.119258
---

# Butter Cookie——web多功能渗透测试浏览器插件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qqiaD4wiajgFw4NWJfzUa0SXs6mib7wF5XpZXjAAibKeH80o5fw6OAXEicrCGu95icIHn3tR0qXiat1MOowibtgibvRYiaWYkasicmVyO4lTguqFvOU5yg/0?wx_fmt=jpeg)

# Butter Cookie——web多功能渗透测试浏览器插件

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

## 开发作者

##

## 项目地址

https://github.com/EdinLyle/Butter\_Cookie

## 项目概述

# Butter Cookie是一款集成化渗透测试浏览器插件（Chrome Extension），专为安全测试人员和开发者设计。它提供了丰富的安全测试工具集，帮助用户快速识别和评估Web应用的安全漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFxHUDE1iaZkV8ia818jLrquwy4KwMdRoC6er6ADJQx5V81ZYggDNMQz4mdOicsbA8YKVM0WAuYALxhXhiaiaHLjNwdd6cEdIuH8ic69A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFxTUxCgicibmTEPycRbqo5C3iaKKT0hMre6icficzjsWPpptZ4nm6DHaz5LHYlmFrJJfgyJMPZ3icuiaXfP3SPBWuNztJdNh1fOueicBEM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFyW3XkKAbJPbTVBYZ60X7maNSwkApiaLzyVmJv0veYoOVH2zic8pqNJzdQoJ56yBYZuwyicD7TGZE8bicIsNSiayRqOJSgYBNJhUMV0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFzVett3qrO9vcCnXB81xymwux0c7J1x1fsRiancEyt7e8NfX78h2jCuNtHM7So7JHtYlQSHfcricPf83xf3qqzERyI4Pibghp9BHk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFyicQdnYibUgqLIWv9iadJ9NVE6QJPyOQaykW533tmuE1icDWsSd2nYOarU4ltVnqQUxT0Sh4Vic27AANpLcAfDQgauW2gHbaLqRRBE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFxlicR6KK1ZZJ5ZyaERwtXJ5OmyB3dgiaymdIMvY2mibM2vNKOMEmqiczBMcrVVvZ9KMFvGicSAw6WZH5hn4a2oYdg7YKxhRqgQXeWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFzGSIrjgwtFvSD4zmE4dqeb6qicpFRw7LHf5d2YksSE3ZMJvlEI51pVVdrId46FMGRiaSu5NP6LDoibKnvFmc1RjtFF3yXXLS4VMw/640?wx_fmt=png&from=appmsg)

#

## 模块详解

### 1. 信息收集模块

**功能定位**：Web应用指纹识别与敏感信息探测

表格

| 子功能 | 描述 |
| --- | --- |
| **User-Agent管理** | 支持多种设备UA快速切换（iPhone Safari、Android Chrome、Windows Chrome、华为/小米/OPPO等） |
| **Cookie管理** | 自定义Cookie注入，支持键值对格式 |
| **HTTP头部管理** | 配置X-Forwarded-For、Referer、Client-IP、X-Real-IP等请求头 |
| **敏感信息收集** | 扫描页面资源，支持导出JSON/TXT/CSV/XLSX格式 |
| **框架指纹识别** | 识别Web应用使用的技术框架和组件 |
| **蜜罐检测** | 检测目标是否为蜜罐系统 |
| **Fuzz扫描** | 支持JS文件Fuzz、API Fuzz、接口Fuzz三种模式 |

**使用流程**：

1. 在SITE字段输入目标域名
2. 选择或输入User-Agent
3. 配置Cookie和HTTP头部（可选）
4. 点击"应用并刷新"生效，或"清除并刷新"恢复默认

---

### 2. XSS测试模块

**功能定位**：跨站脚本漏洞检测与利用

表格

| 子功能 | 描述 |
| --- | --- |
| **批量填充** | 自动填充XSS Payload到页面输入框 |
| **CSP读取** | 读取当前页面的Content Security Policy策略 |
| **参数提取** | 自动提取URL中的Query参数、Hash参数、Path参数 |
| **编码转换工具箱** | 支持HTML实体编码、URL编码、十六进制编码 |

**参数提取区域**：

* **QUERY参数区**：URL查询字符串参数
* **HASH参数区**：URL片段标识符参数
* **PATH参数区**：URL路径参数

---

### 3. SQL注入测试模块

**功能定位**：SQL注入漏洞检测与利用

**SQL HackBar 功能架构**：

```
┌────────────────────────────────────────┐
│  SQL HackBar                           │
├────────────────────────────────────────┤
│  METHOD: [GET ▼]                      │
│  URL: https://target/path?x=1         │
│  [从当前页填充] [发送请求]              │
├────────────────────────────────────────┤
│  注入入口: [URL参数 ▼]                  │
│  KEY: id / uid / token                │
│  PAYLOAD: ' OR 1=1-- -                │
│  [追加] [替换]                         │
├────────────────────────────────────────┤
│  HEADERS (自定义请求头)                 │
│  COOKIE (自定义Cookie)                  │
│  BODY (请求体配置)                      │
│  RESPONSE (响应分析区域)                │
└────────────────────────────────────────┘
```

**支持特性**：

* 多种HTTP请求方法（GET/POST/PUT/DELETE等）
* 多种注入入口（URL参数、Body参数、Cookie、Header）
* 响应内容分析
* Curl命令自动生成与复制

---

### 4. 端点安全扫描模块

**功能定位**：前端代码安全审计

表格

| 检测类型 | 说明 |
| --- | --- |
| **JS端点发现** | 从JavaScript文件中提取API端点 |
| **敏感目录发现** | 探测常见的敏感目录和文件 |
| **DOM XSS检测** | 检测DOM型XSS漏洞 |
| **跨域消息追踪** | 监控postMessage跨域通信 |
| **原型污染检测** | 检测JavaScript原型链污染漏洞 |
| **重定向漏洞检测** | 检测开放式重定向漏洞 |

---

### 5. Shodan主机信息模块

**功能定位**：网络空间资产情报查询

**查询维度**：

* **域名信息**：关联域名解析记录
* **开放端口**：主机暴露的服务端口
* **安全漏洞**：已知CVE漏洞信息
* **详细信息链接**：跳转Shodan官网查看完整报告

---

### 6. 辅助工具模块

**功能定位**：提升渗透测试效率的实用工具集

表格

| 工具 | 功能 |
| --- | --- |
| **Vue快速检测** | 检测目标是否使用Vue.js框架及版本 |
| **JavaScript工具** | JS代码格式化、压缩、解码等 |
| **批量URL打开工具** | 批量在标签页中打开URL列表 |
| **URL列表管理** | 管理和维护测试目标URL清单 |

---

## 技术实现

### 技术栈

表格

| 层级 | 技术 |
| --- | --- |
| **前端框架** | HTML5 + CSS3 + JavaScript (原生) |
| **浏览器API** | Chrome Extension Manifest V3 |
| **UI组件** | 自定义组件库 |
| **数据导出** | SheetJS (XLSX导出) |

## 快速开始

### 开发者模式加载

1. 下载项目源码并解压
2. 打开 Chrome 浏览器，进入 `chrome://extensions/`
3. 开启右上角"开发者模式"
5. 点击"加载已解压的扩展程序"
6. 选择项目根目录

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