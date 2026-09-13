---
title: 工具分享 | 一款若依（Ruoyi-Vue）漏洞检测工具
url: https://mp.weixin.qq.com/s/KRkVcTWfKueuoUJo_pPVAQ
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T07:01:22.828141
---

# 工具分享 | 一款若依（Ruoyi-Vue）漏洞检测工具

# 工具分享 | 一款若依（Ruoyi-Vue）漏洞检测工具

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 0x01 工具介绍

一款若依Vue漏洞检测工具，支持自动化扫描若依(Ruoyi-Vue)系列系统的包括Swagger，Druid，文件读取，SQL注入，定时任务，任意密码修改，系统接口越权等多种安全漏洞，同时还可以对接口和敏感信息进行搜集。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Nuuibh3bDOw7T0h7wDxOVcnFicpeHjdZUQb9tQpmibPqicdVxicwZZib2YgsOgjHJb7jIeV0tKFWYQ8LhyLYpdEibR82EChs09EwfxH5FCrrHoSTuc/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=1)

## 0x02 工具功能

1、漏洞检测模块

| 功能 | 说明 |
| --- | --- |
| **Swagger检测** | 自动探测 `/swagger-ui/index.html`、`/v2/api-docs`、`/v3/api-docs` 等接口，识别是否存在Swagger文档泄露 |
| **Druid检测** | 检测 Druid 监控页面未授权访问，并支持常见弱口令爆破（admin/123456、druid/druid等） |
| **文件读取** | 检测 `/common/download/resource` 等接口的路径穿越漏洞，可读取 `/etc/passwd`、`windows/win.ini` 等系统文件 |
| **SQL注入** | 针对若依系统的 `dataScope` 参数进行 SQL 注入检测 |
| **定时任务读取** | 检测 `/monitor/job` 定时任务接口的任意文件读取漏洞 |
| **任意密码修改** | 检测若依系统密码重置接口的漏洞 |
| **系统接口越权测试** | 自动测试 `/system/user`、`/system/role`、`/system/config` 等管理接口是否存在未授权访问 |
| **全面检测** | 一键执行以上所有检测项目 |

2、辅助功能模块

| 功能 | 说明 |
| --- | --- |
| **获取JS接口** | 多线程爬取目标页面引用的所有 JS 文件，正则提取其中的 API 路径，支持 `/prod-api`、`/dev-api`、`/monitor` 等常见前缀 |
| **接口测试** | 对收集到的接口进行批量测试，支持 GET / POST / POST-JSON 三种请求方式，可自定义请求体 |
| **敏感信息搜集** | 基于已抓取的 JS 内容，检测密码明文、API密钥、JWT令牌、数据库连接字符串、Redis URL、云存储地址、GitHub令牌、内网IP、邮箱、手机号等敏感信息 |
| **自动提取Basedir** | 输入完整 URL 时自动识别并填充后端 API 基础路径（如 `/prod-api`） |

3、核心特性

* 多线程并发：10线程池并行请求，大幅提升扫描效率
* 代理支持：支持 HTTP 代理，便于使用 Burp Suite 等工具进行流量分析
* SSL忽略：内置 SSL 证书信任策略，支持扫描自签名 HTTPS 站点
* Cookie/Authorization：支持自定义认证头，可测试登录后的接口
* 彩色日志：终端风格彩色日志输出，关键漏洞高亮显示
* 实时进度：进度条 + 状态栏实时显示扫描进度

## 0x03 工具演示

1、设置目标URL，如 http://target.com

2、HTTP代理：可选，格式如 http://127.0.0.1:8080

3、自动提取Basedir：勾选后自动识别后端API路径前缀

![图片](https://mmbiz.qpic.cn/mmbiz_png/Nuuibh3bDOw41jkAPmrwrMIlOooicZrBAyyXyibLgTXRal9CkEUa8yNoQNuoBxmLx5hhOwHs5lA9W7UPreLBzvuCJYCpRP6yibx8MeohhJK3z5w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

文章来源：无影安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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