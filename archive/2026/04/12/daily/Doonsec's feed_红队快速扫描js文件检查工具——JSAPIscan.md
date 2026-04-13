---
title: 红队快速扫描js文件检查工具——JSAPIscan
url: https://mp.weixin.qq.com/s/S8w9eeKUeAYUuYXNOXV2EQ
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:53:40.197276
---

# 红队快速扫描js文件检查工具——JSAPIscan

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bhUibV7MPZlsqWTWicOhGL2VuKth3rDDnAaNXBYrXiaaYmpCEYxWSbkupj3pA9e3cIOTqDcDlib2Wn8rV6NZp8Lia8HN0p97ZNLAnriaTofia72Qg0/0?wx_fmt=jpeg)

# 红队快速扫描js文件检查工具——JSAPIscan

风铃Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明：仅用于授权测试，用户滥用造成的一切后果和作者无关 请遵守法律法规！出于对安全考量本公众号发布的所有文章中的工具均建议放在虚拟机中运行！【无需回复关键字，文中第二部分0x02获取工具】

**0x01 工具简介**

**JSAPIscan** 是一款基于 Go 语言开发的 JavaScript 文件分析和接口扫描工具，专为从 JavaScript 文件中提取 API 接口信息而设计，适用于安全研究场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZluqXibtkxYtXA21wS0XtDyGhCcGODYz24RHe8BFFSOMhqHggpMn1mq2ficlKUDaibgpwQGw9fueibG5BtnibNicAP2tID03YZxe64w1I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlvx4TMt8bqeWXaAOLghVVVuA51yUgwbzbdNjiaJjyMz7LbLzpGDWSx7Tiaog2dPMfvjQrQJX2Td2jBMTgRUQxNykoIEhpPTKYPz0/640?wx_fmt=png&from=appmsg)

### 核心功能特性

* **🎯 自动 API 提取**

  自动解析 JavaScript 文件，提取 API 接口路径
* **⚡ 框架支持**

  支持 Webpack、Vue、React 等主流前端框架的 JS 文件解析
* **🚀 多线程扫描**

  多线程快速扫描，支持自定义线程数和深度
* **🛡️ 安全检测**

  检测未授权访问漏洞
* **📊 自动生成报告**

  自动生成 CSV 格式的详细日志
* **🔗 灵活扫描**

  支持单 URL 扫描、批量 URL 扫描、自动探测等
* **💾 自动存储**

  自动将扫描结果存储到 res/ 目录下

**0x02 工具获取**

夸克「LeakDetector」

链接：「JSAPIscan」

链接：https://pan.quark.cn/s/3ce3416bc2ff

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlsLDYbflsiczstqmM5lfxMbBCibOZAz9qUibyPzM9Rxp0V2Q5spSV5nbdXZXoplaMMK4a2Xq4mbo5LpG25Uc3ibNrHgBW14lXgjTFg/640?wx_fmt=png&from=appmsg)

**0x03 工具使用**

### 基础用法

```
# 扫描单个 URL
JSAPIscan.exe -u https://example.com

# 批量扫描 URL 文件
JSAPIscan.exe -f urls.txt

# 多线程扫描并设置深度
JSAPIscan.exe -u https://example.com -t 20 -d 5
```

### 高级用法

```
# 开启自动接口探测（未授权访问检测）
JSAPIscan.exe -u https://example.com -auto

# 携带参数进行测试（用于接口参数探测）
JSAPIscan.exe -u https://example.com -auto -aparms

# 配合 POC（Proof of Concept）检测
JSAPIscan.exe -u https://example.com -auto -aparms -apoc

# 批量扫描并开启自动探测
JSAPIscan.exe -f urls.txt -auto -t 15 -d 4
```

### 参数说明

| 参数 | 说明 | 默认值 | 示例 |
| --- | --- | --- | --- |
| `-u` | 目标 URL | - | `-u https://example.com` |
| `-f` | URL 文件路径 | - | `-f urls.txt` |
| `-t` | 线程数 | 10 | `-t 20` |
| `-d` | 获取深度 | 3 | `-d 5` |
| `-auto` | 开启自动接口探测 | false | `-auto` |
| `-aparms` | 携带参数进行测试 | false | `-aparms` |
| `-apoc` | 配合 POC 检测 | false | `-apoc` |
| `-h` | 显示帮助信息 | false | `-h` |
| `-sc` | 打印状态码（不打印状态码） | "" | `-sc` |
| `-o` | 输出文件格式 | "txt" | `txt/html` |
| `-k` | 只看关键信息 | false | `-k` |
| `-p` | 设置代理 | - | `-p http://127.0.0.1:8080` |
| `-pa` | 只对未授权接口使用代理 | false | `-pa` |
| `-gjca` | 在原字段基础上增加匹配字段 | "" | `-gjca /upload,admin` |
| `-gjc` | 只使用指定字段进行匹配 | "" | `-gjc /upload` |

### 扫描结果结构

工具会在 `res/` 目录下自动创建时间戳文件夹，保存扫描结果：

```
res/
└── 扫描时间戳/
    ├── 目标 URL.txt          # 主要扫描目标
    ├── api_scan_domain.csv   # API 扫描 CSV 报告
    ├── findsometingzong.txt  # 发现内容汇总
    ├── parms.txt             # 参数信息
    └── bug.txt               # 漏洞 URL 文件
```

### 新增功能说明（v0.29.3）

**代理设置 (-p)**：

```
-p http://127.0.0.1:8080
```

**只对未授权接口使用代理 (-pa)**： 配合 `-auto` 参数使用，只对检测未授权访问的接口使用代理。

**自定义匹配字段 (-gjca)**：

```
-gjca "login,admin"
```

在原默认匹配字段基础上增加 "login" 和 "admin"。

**只使用指定字段 (-gjc)**：

```
-gjc "api,config"
```

工具只匹配包含 "api" 和 "config" 的路径。

### 版本更新亮点

| 版本 | 更新内容 |
| --- | --- |
| v0.29.3 | 新增代理设置、自定义匹配字段功能 |
| v0.29 | 简单 SQL 注入检测、路径优化 |
| v0.28 | 添加关键字查找、HTML 输出格式 |
| v0.27 | 添加图片 hash、title 显示、路径匹配优化 |
| v0.6 | Webpack 优化 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlvwVAY7zQicybNSdwgg0o7KzZoGaw1iaXvPeCXOGlEJ696oibzv5UwjXBgnn8pGpZU8arNOzIzFnmpVnD0CeKaqYibgiaLJAMFjMR7A/640?wx_fmt=png&from=appmsg)

0x04 资源分享

夸克网盘「综合漏洞自检测工具」

链接：https://pan.quark.cn/s/302256a9ecf6

![图片](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HnvemUvKPcNicmrhKC7857NtMuGru0ibEtMiaUs6lEkf6aibVdZnrZuPmKn1MApBfHcocujPYl9aiafvlw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HnvemUvKPcNicmrhKC7857NtRZRKKPlXaichMVYK0YYcKTH2gxrQ01mURiarrrctkQChx4yIMqy8TB3Q/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=7)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HnvemUvKPcNicmrhKC7857NtQaialPju2RecAS2Kc0vjiaMEQE4IxaaTl4Y4mNpeDq4Uib43HWPJSlwicQ/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=8)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HmibOdP6ibKTOYNXKuEdbPFJKnX0Z54TIaWXmS6apnB5FYRgZVtWlzvTJK3lQzuxEHTa5kCSibf2eXZw/0?wx_fmt=png)

风铃Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HmibOdP6ibKTOYNXKuEdbPFJKnX0Z54TIaWXmS6apnB5FYRgZVtWlzvTJK3lQzuxEHTa5kCSibf2eXZw/0?wx_fmt=png)

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