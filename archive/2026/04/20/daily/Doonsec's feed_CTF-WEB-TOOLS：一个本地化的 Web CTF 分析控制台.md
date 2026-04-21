---
title: CTF-WEB-TOOLS：一个本地化的 Web CTF 分析控制台
url: https://mp.weixin.qq.com/s/NJLobWLbLepeuJbKMHjIcw
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:45:26.343891
---

# CTF-WEB-TOOLS：一个本地化的 Web CTF 分析控制台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XDkcKR8jrMP3BS5bwV5ARwd9SCo7C5QM19A7EZ5pAgkNupIaScWic0RsEDmAZCVice9FoYMqp1sA3yQXeLEWu0tTh2fn0EbtPn8ibYEqAVppWg/0?wx_fmt=jpeg)

# CTF-WEB-TOOLS：一个本地化的 Web CTF 分析控制台

原创

ChenFu
ChenFu

XChenFu

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# CTF-WEB-TOOLS

一个面向 CTF Web 题目的本地分析控制台，使用 `PHP + Python` 组合实现，提供批量目标抓取、页面线索提取、附件文本抽取、候选 Flag 汇总、AI 二次分析、WriteUp 生成和历史记录保存等能力。

工具交流群:1097842927

## 功能概览

* 批量输入一个或多个目标 URL
* 支持补充题目描述、HTTP 片段、Hint、JWT、Cookie、自定义请求头
* 支持上传题目附件并自动抽取可读文本
* 自动抓取页面并提取以下信息

+ 页面标题、文本、注释、表单、输入项、外链 JS
+ JS 中的 API 路径和可疑前端变量
+ 常见敏感路径探测结果，如 `/.git/HEAD`、`/admin`、`/debug`
+ 参数名、报错关键字、技术栈指纹

* 自动识别 Flag 与可疑 Flag 片段
* 自动生成本地 Agent 报告
* 可选调用大模型生成二次分析报告
* 可基于当前上下文生成 Markdown WriteUp
* 保存分析历史、聊天记录和 WriteUp
* 内置若干常用小工具

+ 编解码
+ Hash/HMAC
+ JWT 解析
+ Caesar 爆破
+ JSON / HTTP 格式化
+ Base64 / URL / Flag / 正则提取

## 技术栈

* 前端：原生 HTML + CSS + JavaScript
* 后端：PHP
* 分析 Agent：Python 3
* AI 接口：兼容 OpenAI Chat Completions 风格的 HTTP API

## 目录结构

```
CTF-WEB-TOOLS/
├─ agent/          # Python 分析逻辑
├─ api/            # PHP API 接口
├─ assets/         # 前端样式资源
├─ data/history/   # 历史分析记录
├─ inc/            # 公共模块（AI、附件处理、存储）
├─ config.php      # AI 配置
├─ index.php       # 控制台入口
└─ README.md
```

## 网站预览

![](https://mmbiz.qpic.cn/mmbiz_png/XDkcKR8jrMOQib8OPYgFNkeV5KMUsMFbxCNS9mB1zjBtHW36CyGf6JeibERpUM5ac56MUiaGFLGqTKxLUT4YPUY2ibKQy3HVrGuw1g9YHCK36iac/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XDkcKR8jrMM5vicVe0MpwoAX4t7icuHsMHh9sibylHwrUWbcLDAAEY1pdsKpc14DXzvNcHq4DOWSQSJlSOsyib5AZuJrgnkGErXNweIvvEwzC9Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XDkcKR8jrMMpwfGvnxGOQvEViaTrxCGLdL5xQnibmVfU1DnIE3zELkDR22Vrwrpsicsb1DazDdwmTSpgxiaOicNNCKIZkibibK5g2IBQLvGKKA9np0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XDkcKR8jrMPMZQ9icHUtXTrE9C8hicUBx8IKIyzCkQw84RWJpL5ztuxLwZmuVSYvEaxcyoS301olUyx5obK5htQyMd83yDjMoGlRIibom05fck/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XDkcKR8jrMOkvkCSibTQvmf7gLPqdA2bTUKLyIm5weWLnCKesuOrURXQWicFW1r3diav34xSSxBvqrt9Ez2JTTSQSQBKL2MsbmjjfFUd0QicDaU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XDkcKR8jrMNI6tGtiaIZPOwenOhvcN7jWc7D6jqnn3rJYv3FryLV5HuCuDAI6JQKrFfuzOQHbHvmvCsPkbmCkUGCTSjjc4JT1MnC3FicLm9tQ/640?wx_fmt=png&from=appmsg)

##

## 运行要求

* PHP 8.0 及以上
* Python 3.10 及以上
* 推荐本地运行
* 若需 AI 功能，需要可访问的模型接口和有效 `API Key`

## 快速开始

### 1. 进入项目目录

```
cd"CTF-WEB-TOOLS"
```

### 2. 启动 PHP 内置服务

```
php-S127.0.0.1:8000
```

如果本机装有多个 PHP 版本，请先确认 `php` 可执行文件已加入环境变量。

### 3. 打开浏览器

访问：

```
http://127.0.0.1:8000
```

## 基本使用流程

1. 在首页输入单个 URL 或多个 URL
2. 按需填写补充线索、Cookie、自定义请求头
3. 如有题目附件，先上传附件
4. 点击开始分析
5. 查看Flag、可疑片段、API/JS/敏感路径结果和主报告
6. 如已配置 AI，可勾选 AI 二次分析
7. 需要结果时，生成 WriteUp 并导出 `.md`

## 配置说明

配置文件位于：

`config.php`

默认内容如下：

```
<?php
return [
    'enabled'=>true,
    'base_url'=>'',
    'api_key'=>'sk-',
    'model'=>'',
    'temperature'=>0.2,
    'timeout'=>90,
    'max_tokens'=>900,
    'max_history'=>12,
];
```

字段说明：

* `enabled`：是否启用 AI 功能
* `base_url`：模型接口地址，通常是 `/v1/chat/completions`
* `api_key`：接口密钥
* `model`：模型名
* `temperature`：生成温度
* `timeout`：请求超时秒数
* `max_tokens`：最大输出长度
* `max_history`：前端聊天历史上限

如果不需要 AI 功能，可以这样配置：

```
<?php
return [
    'enabled'=>false,
    'base_url'=>'',
    'api_key'=>'',
    'model'=>'',
    'temperature'=>0.2,
    'timeout'=>90,
    'max_tokens'=>900,
    'max_history'=>12,
];
```

## 工作原理

### 页面分析链路

前端发起请求到：

* `api/agent.php`

该接口会调用：

* `agent/run_agent.py`
* `agent/solver.py`

Python Agent 负责：

* 拉取页面内容
* 提取标题、注释、链接、表单、输入框、脚本
* 抓取外链 JS
* 探测常见敏感路径
* 识别 URL、参数、JWT、Base64、Hex、JSON、错误信息、框架指纹
* 汇总候选 Flag 和人工验证建议

### 附件分析链路

上传接口：

* `api/upload.php`

处理模块：

* `inc/artifact.php`

主要能力：

* 读取文本类文件
* 自动尝试 UTF-8 / GBK / GB2312 / BIG5 / ISO-8859-1 解码
* 对二进制文件提取可打印字符串
* 汇总文件预览、候选 Flag 和可疑片段

### AI 与 WriteUp

相关文件：

* `inc/ai_client.php`
* `api/chat.php`
* `api/writeup.php`

功能包括：

* 基于当前分析证据生成 AI 二次报告
* 在聊天窗口继续追问分析结论
* 自动整理成结构化 Markdown WriteUp

注意：AI 只应作为辅助整理工具，最终提交前仍需人工确认 Flag 与利用链。

## 历史记录

历史数据默认保存在：

* `data/history`

相关接口：

* `api/history.php`

每次分析会保存：

* 分析上下文
* URL 列表
* 本地分析结果
* AI 对话
* WriteUp

## 内置工具接口

工具接口文件：

* `api/tool.php`

当前支持：

* `codec`

+ `base64-encode`
+ `base64-decode`
+ `hex-encode`
+ `hex-decode`
+ `url-encode`
+ `url-decode`
+ `rot13`
+ `binary-decode`

* `hash`

+ `md5`
+ `sha1`
+ `sha256`
+ `sha512`
+ `hmac-sha256`

* `jwt`
* `caesar`
* `format`

+ `json-pretty`
+ `json-minify`
+ `http-parse`

* `extract`

+ `base64`
+ `flags`
+ `urls`
+ `regex`

## 适用场景

* CTF Web 题目的初步信息整理
* 多目标页面的快速横向排查
* 登录态页面的只读探测
* 题目附件文本抽取与 Flag 搜索
* WriteUp 草稿生成

## 下载链接

https://github.com/ChenFu0604/CTF-WEB-TOOLS

喜欢的给我点点star噢！

## 注意事项

* 本工具更适合本地靶场、CTF 环境或你明确有权限测试的目标
* 敏感路径探测虽然是只读设计，但仍然属于主动请求
* AI 报告不等于漏洞已验证成功
* `api/agent.php` 通过 `python` 命令调用 Python，请确认系统环境变量中可直接执行 `python`
* 如果 AI 接口未配置，AI 报告、聊天和 WriteUp 功能会返回空结果或不可用

## 常见问题

### 1. 页面能打开，但分析时报错 `Failed to start agent process`

通常是本机没有可直接调用的 `python`，或 PHP 无法执行进程。先检查：

```
python--version
php--version
```

### 2. AI 没有返回结果

优先检查：

* `config.php` 中的 `enabled`
* `base_url` 是否正确
* `api_key` 是否有效
* `model` 是否存在
* 目标接口是否兼容 Chat Completions 风格返回

### 3. 附件内容乱码

当前已做常见编码兼容，但极端情况下仍可能存在编码识别不准的问题，建议手动转为 `UTF-8` 后再上传。

## 后续可扩展方向

当前版本为V1.0 功能可能还不是那么完善

* 增加 Burp 导出流量导入
* 增加更多编码/解码工具
* 增加请求重放与参数批量测试
* 增加更完整的前端交互提示
* 增加 Docker 部署方式
* 增加依赖检查脚本

## 免责声明

本项目仅用于 CTF 学习、题目分析和授权测试场景。使用者应自行确保目标与行为合法合规。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/SUWfUqOtnVhaM8MjAgNAheWZvic2dGRCL3aS74ez3B6XjT6WX2a6dvbVWIa3AqfojOsHAL0LVdibd1K5sYTian3BA/0?wx_fmt=png)

XChenFu

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/SUWfUqOtnVhaM8MjAgNAheWZvic2dGRCL3aS74ez3B6XjT6WX2a6dvbVWIa3AqfojOsHAL0LVdibd1K5sYTian3BA/0?wx_fmt=png)

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