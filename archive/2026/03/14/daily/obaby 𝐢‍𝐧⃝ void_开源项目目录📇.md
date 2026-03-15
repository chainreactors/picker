---
title: 开源项目目录📇
url: https://zhongxiaojie.cn/2026/03/593/
source: obaby 𝐢‍𝐧⃝ void
date: 2026-03-14
fetch_date: 2026-03-15T04:34:05.932641
---

# 开源项目目录📇

[![obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/wp-content/uploads/2026/01/new-logo-27.png)](https://zhongxiaojie.cn)

程序媛 / 独立开发者 / 智商不稳定的女神经

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

 [Menu](#mobilemenu)

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

[程序媛](https://zhongxiaojie.cn/category/code-girl/)

# 开源项目目录📇

2026年3月14日 16:14
[46 条评论](https://zhongxiaojie.cn/2026/03/593/#comments)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/58603a31.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/58603a31.jpg)

部分开源项目源码。

# PHP8 探针项目（包含WP插件）

专业的服务器监控和管理工具，提供实时系统监控、性能测试、数据库检测等功能。本项目包含两个版本：独立PHP探针和WordPress插件版本。

## 项目结构

```
php8-probe/
├── phpprobe.php              # 独立PHP探针（可直接访问）
├── php-probe-widget/         # WordPress插件版本
│   ├── php-probe-widget.php  # 主插件文件
│   ├── includes/             # 小组件类
│   ├── css/                  # 前端样式
│   ├── js/                   # 前端脚本
│   └── README.md             # 插件详细文档
├── LICENSE                   # 许可证
└── README.md                 # 本文件
```

## 🚀 快速开始

### 方式一：独立PHP探针

1. 将 `phpprobe.php` 上传到您的Web服务器
2. 通过浏览器访问该文件即可查看服务器信息
3. 支持实时监控、性能测试、数据库检测等功能

**特点：**

* ✅ 无需安装，直接使用
* ✅ 单文件部署，简单方便
* ✅ 支持多平台（Linux、Windows、macOS、FreeBSD）
* ✅ 实时系统监控

### 方式二：WordPress插件

1. 将 `php-probe-widget` 文件夹复制到 `wp-content/plugins/` 目录
2. 在WordPress后台激活”服务器监控探针”插件
3. 进入 **外观 > 小组件** 页面
4. 将”服务器监控探针”小组件拖拽到侧边栏
5. 配置显示选项和主题设置

<https://gitee.com/obaby/php8-probe>

---

# 结巴分词HTTP服务

基于Flask和jieba的本地HTTP分词服务。

<https://gitee.com/obaby/baby-jb-server>

---

# WordPress 博客数据分析工具

这是一个用于分析 WordPress 博客数据的 Python 工具，可以通过 WordPress REST API 获取并分析博客的文章和评论数据。

## 功能特性

* 📝 统计指定年份发布的文章数量（按月统计）
* 💬 统计指定年份的评论数量
* 🏆 分析评论用户的评论数排行
* 💾 将分析结果保存为 JSON 文件

<https://gitee.com/obaby/baby-wp-data-analysis-tool>

---

# 微信双开脚本 (WeChat Dual Launch Script)

一个用于 macOS 系统的微信双开自动化脚本，通过复制微信应用并修改 Bundle ID 实现真正的微信双开功能。

## 📋 功能特性

* ✅ **一键双开** – 自动完成所有设置步骤
* ✅ **智能检测** – 自动检测已存在的 WeChat2.app
* ✅ **安全可靠** – 完善的错误处理和权限检查
* ✅ **彩色输出** – 友好的命令行界面
* ✅ **进程管理** – 查看和管理微信进程
* ✅ **自动化设置** – 无需手动执行复杂命令

<https://github.com/obaby/baby-wechat>

---

# Baby 足迹地图

## 简介：

基于百度地图的足迹地图。
启动服务之后，先去后台 地图 key 设置页面，添加百度地图浏览器端 ak！
启动服务之后，先去后台 地图 key 设置页面，添加百度地图浏览器端 ak！
启动服务之后，先去后台 地图 key 设置页面，添加百度地图浏览器端 ak！

为了防止 js 地址解析受限，需要同时添加服务端 ak！
为了防止 js 地址解析受限，需要同时添加服务端 ak！
为了防止 js 地址解析受限，需要同时添加服务端 ak！

添加之后，访问： <http://127.0.0.1:10099/api/location/process-my-location/> 地址刷新数据库的地点坐标信息，后续无需再通过 js 接口进行解析！

<https://github.com/obaby/BabyFootprintV2>

---

# Simple microblogging

```
Add a microblog to your site; display the microposts in a widget or using a shortcode.
增强版优化页面显示，增加分页功能。wp微博插件。
```

<https://github.com/obaby/Simple-microblogging-wordpress-plugin>

---

# Baby WP 评论强化拦截插件

一个强大的WordPress评论过滤插件，支持字数限制、中文检测、关键词过滤等功能。

## 插件信息

* **插件名称**: Baby WP 评论强化拦截插件
* **版本**: 1.0.5
* **作者**: obaby
* **作者网址**: [https://h4ck.org.cn](https://h4ck.org.cn/)
* **许可证**: GPL v2 or later

## 功能特性

### 🛡️ 评论过滤功能

* **字数限制**: 设置评论的最少和最多字数
* **中文检测**: 要求评论必须包含中文字符
* **关键词过滤**: 支持自定义关键词和WordPress设置的关键词
* **正则表达式支持**: 支持使用正则表达式进行高级匹配

### ⚙️ 管理功能

* **简单设置界面**: 直观的管理后台设置页面
* **错误消息自定义**: 可以自定义各种错误提示消息和标题
* **统计信息**: 记录评论过滤统计信息，支持重置功能
* **WordPress集成**: 与WordPress讨论设置完美集成，支持实时预览
* **设置验证**: 完整的输入验证和数据清理机制

### 🔧 技术特性

* **简单架构**: 采用简单的面向对象架构，易于维护
* **性能优化**: 高效的过滤算法，不影响网站性能
* **兼容性**: 支持WordPress 5.0+版本，PHP 7.4+
* **多语言**: 支持多语言环境
* **数据安全**: 完整的输入验证和清理机制
* **错误处理**: 完善的错误处理和日志记录

<https://github.com/obaby/baby-wp-comment-filter>

---

# WinRAR-Keygen

## 1. What is WinRAR?

* WinRAR is a trialware file archiver utility for Windows, developed by Eugene Roshal of win.rar GmbH.
* It can create and view archives in RAR or ZIP file formats and unpack numerous archive file formats.
* WinRAR is not a free software. If you want to use it, you should pay to [**RARLAB**](https://rarlab.com/) and then you will get a license file named `"rarreg.key"`.
* This repository will tell you how WinRAR license file `"rarreg.key"` is generated.

## 2. How is “rarreg.key” generated?

* WinRAR uses a signature algorithm, which is a variant of Chinese SM2 digital signature algorithm, to process the user’s name and the license type he/she got. Save the result to “rarreg.key” and add some header info, then a license file is generated.

<https://github.com/obaby/winrar-keygen>

---

# Baby Device Manager

一个功能强大的WordPress设备管理系统插件，支持设备分组管理、设备信息管理、自定义排序、状态跟踪等功能。

## 功能特点

* 设备分组管理
  + 创建和管理设备分组
  + 自定义分组排序
  + 分组描述信息
* 设备管理
  + 添加/编辑/删除设备
  + 设备状态管理（在售、停售、已售出、维修中、已报废）
  + 设备图片和产品链接
  + 自定义设备排序
  + 设备描述信息
* 前端展示
  + 响应式布局
  + 按分组分类显示
  + 支持多种排序方式
  + 美观的界面设计
  + 支持自定义每行显示设备数量（1-6个）
* 其他功能
  + 图片管理：支持设备图片上传和显示
  + 产品链接：支持添加产品详情页链接
  + 状态跟踪：支持多种设备状态管理
  + 自定义排序：支持设备分组和设备的自定义排序

<https://github.com/obaby/Baby-Device-Manager>

---

# RSS Beauty

为 WordPress RSS Feed 提供美观的网页展示样式（基于 [RSS.Beauty](https://cnb.cool/110?url=https%3A%2F%2Frss.beauty) 的 Pink 主题）。

## 项目功能

* **RSS 样式化**：在 Feed 中注入 XSL 样式表，浏览器打开 feed 地址时以 HTML 页面形式展示，而非原始 XML。
* **Feed Content-Type**：将 feed 的 Content-Type 设为 `application/xml`，使浏览器按 XML 解析并应用 `xml-stylesheet`。
* **XSL 地址**：样式表使用插件目录下的静态文件 `pink.xsl`。需在 OpenResty/Nginx 中为 `.xsl` 配置正确的 Content-Type（见下方配置说明），否则浏览器可能不按 XSL 解析。
* **主题**：内置淡粉色（light pink）页面背景与适配的文字颜色。

<https://cnb.cool/oba.by/rss-beauty>

---

# WP-UserAgent

**Contributors:** obaby
**Donate Link:** [https://oba.by](https://cnb.cool/110?url=https%3A%2F%2Foba.by)
**Tags:** useragent, user-agent, user agent, web, browser, web browser, operating system, platform, os, mac, apple, windows, win, linux, phone
**Requires at least:** 2.0
**Tested up to:** 6.3
**Stable tag:** 16.06.99

## IP 查询方式（归属地）

插件支持四种 IP 查询方式，可在 **设置 → WP-UserAgent** 中选择：

| 方式 | 说明 |
| --- | --- |
| **IP2Location** | 使用 IP2Location 数据库（需将 BIN 文件放入 `show-useragent/ip2location_db/db/`），依赖 Composer |
| **CZDB** | 使用纯真 CZDB 数据库（需授权与 db 文件放入 `show-useragent/czdb/db/`），依赖 Composer |
| **ip2region** | 使用 ip2region xdb（**仅内置 ip2reginapi，不依赖 Composer**）。需将 xdb 文件放入 `show-useragent/ip2region_db/`，文件名：`ip2region_v4.xdb`、`ip2region_v6.xdb` |
| **纯真QQWRY** | 使用 qqwry\_api（qqwry.dat + ipv6wry.db），无需 Composer。数据文件放入 `show-useragent/qqwry_api/ipdata/` |

选择 **ip2region** 或 **纯真QQWRY** 时不会加载 `vendor/autoload.php`。若选择 IP2Location 或 CZDB 时 vendor 加载失败，插件会自动回退为 ip2region 模式，避免站点白屏。

## Description

**WP-UserAgent** is a simple plugin that allows you to display details about a computer’s [operating system](https://cnb.cool/110?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOperating_system) or [web browser](https://cnb.cool/110?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FWeb_browser) that your visitors comment from.

It uses the comment->agent property to access the [User-Agent string](https://cnb.cool/110?url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FUser_agent). Through a series of regular expressions, this plugin is able to detect the operating system and browser which can be integrated in comments or placed in custom places through your template(s).

I’m adding new web browsers and operating systems frequently, as well as updating and optimizing the source code. Your feedback is very important, new features have been added by request, so if there’s something you would like to see in **WP-UserAgent**, [leave a comment](https://cnb.cool/110?url=https%3A%2F%2Fwww.kyleabaker.com%2Fgoodies%2Fcoding%2Fwp-useragent%2F), and I’ll see what I can do.

**WP-UserAgent** was written with Geany – [http://www.geany.org/](https://cnb.cool/110?url=http%3A%2F%2Fwww.geany.org%2F)
Images created with The Gimp – [http://www.gimp.org/](https://cnb.cool/110?url=http%3A%2F%2Fwww.gimp.org%2F)

> **注意：**
>
> * 使用 **CZDB** 时：若更新...