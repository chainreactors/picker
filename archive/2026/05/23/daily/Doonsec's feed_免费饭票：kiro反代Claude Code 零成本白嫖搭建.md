---
title: 免费饭票：kiro反代Claude Code 零成本白嫖搭建
url: https://mp.weixin.qq.com/s/M77dHCs77c2bli5UNRRwlw
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:58:40.398677
---

# 免费饭票：kiro反代Claude Code 零成本白嫖搭建

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/434icB39KFkzVDu4E4wRZibRUc5HJlTpNfOv7fzibrpCNIfgTkWsZlzZ8PgxJXOs4bvv9YibWQOQEzE4eLTwMMVfKLVhqsGIgS1xFg6Eb19zkt4/0?wx_fmt=jpeg)

# 免费饭票：kiro反代Claude Code 零成本白嫖搭建

Macfy
Macfy

菜狗安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/434icB39KFkxdfibdaNyu0NKFP3pbO2qRiceu0tYWZZSHCNAhsZgI7rSsCtFvJQ7locINeWZHJN4mnDfwyAyJrUXHxwfLr9WI0fqhzibwOlY258/640?wx_fmt=gif&from=appmsg)

> **免责声明**：本文内容仅供技术学习与个人研究，不构成任何违规使用建议。请遵守相关平台的服务条款，因滥用导致的封号、追责等后果由使用者自行承担。请合理使用，勿用于商业或非法用途。

用到这几个项目：

* https://github.com/chaogei/Kiro-account-manager
* https://github.com/hank9999/kiro.rs
* https://github.com/farion1231/cc-switch

## 1. 下载 Kiro-account-manager

![](https://mmbiz.qpic.cn/sz_mmbiz_png/434icB39KFkzlBIbSBhibwKhn9P71v5t4YZBcTZIKyfoHZibKUXib3RxJ1tGhC3HTRSln4HiaqFsBNdbwYvP8xSiarAaLBbjQ9sZZ8iaAvQ5CcmI0I/640?wx_fmt=png&from=appmsg)

一个谷歌账号能登3次，github和aws都支持谷歌登录，怎么批量搞大伙应该比我更懂。

Kiro-account-manager 本身支持反代，不过我这边尝试过配置有很多问题就没用它，只用来管理账号信息。

## 2. 配置 kiro-rs

具体用法看 github 文档就行，懒得看的话直接复制我这份配置，保存成 `config.json` 放 kiro-rs 同目录：

```
{
  "host": "127.0.0.1",
  "port": 8990,
  "region": "us-east-1",
  "kiroVersion": "0.9.2",
  "machineId": "A3F7C2E1D140B878",
  "apiKey": "sk-kiro-rs-qazWSXedcRFV123456",
  "systemVersion": "macos",
  "nodeVersion": "22.21.1",
  "tlsBackend": "rustls",
  "countTokensAuthType": "x-api-key",
  "proxyUrl": "<your-proxyurl>",
  "proxyUsername": null,
  "proxyPassword": null,
  "adminApiKey": "sk-admin-your-secret-key",
  "githubToken": "<your-github-token>",
  "updateImage": "ghcr.io/zyphrzero/kiro-rs:latest",
  "updateComposeFile": "/app/config/docker-compose.yml",
  "updateService": "kiro-rs",
  "redisUrl": null,
  "cacheDebugLogging": false,
  "cacheMaxReadRatio": 1.0,
  "loadBalancingMode": "balanced",
  "extractThinking": true,
  "defaultEndpoint": "ide",
  "endpoints": {}
}
```

* ‎`apiKey` 是 cc 对接时要用的 key
* ‎`adminApiKey` 是登录 kiro-rs 后台用的
* 代理端口按自己的实际端口改
* 搭在服务器上的话建议直接用 docker

终端启动程序，浏览器打开 http://127.0.0.1:8990/admin

![](https://mmbiz.qpic.cn/sz_mmbiz_png/434icB39KFkxQp7TF7PdKeFVgSQk1Z3HnHRxZDnRibB1pbmicBLo3kkxP0erl0f0NFRxwJH4uUkF64dSfKGtta8vQBS1KIUBnJNAfNJMIQPBYI/640?wx_fmt=png&from=appmsg)

选择从 Kiro Account Manager 导入，把刚才导出的文件复制进去。批量导出导入如果有问题，就一个个从 Kiro Account Manager 复制过来。

防封的话最好配下代理池和机器码，这块就不展开了。

## 3. 配置 cc-switch

```
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-kiro-rs-qazWSXedcRFV123456",
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:8990/cc/",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-sonnet-4-5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL_NAME": "claude-sonnet-4-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL_NAME": "claude-opus-4-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-4-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL_NAME": "claude-sonnet-4-5",
    "ANTHROPIC_MODEL": "claude-sonnet-4-5",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": 97,
    "CLAUDE_CODE_ATTRIBUTION_HEADER": "0",
    "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS": "1",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "DISABLE_AUTOUPDATER": "1",
    "ENABLE_TOOL_SEARCH": "1"
  },
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/434icB39KFkyymzj3ehH2hygRZcFluJOP2bKluEMia7TibIhGDwmvU6lomAljmChHJ3uYBSTH7bklfYThF4NhLGxS00BrBCmKq9Pte4EJicwcjI/640?wx_fmt=png&from=appmsg)

默认 free 用户只能用 4.5，不过可以。。。

![](https://mmbiz.qpic.cn/mmbiz_png/434icB39KFkxzfV0v7UXBgrBObiclyeTt7ZLtWtJFdj0HKqhh0RZJicziaB71ELIRD6mmKhISvOwCPic6aibFaykbgQQApWtwZsS5IIcvEmfBKibII/640?wx_fmt=png&from=appmsg)

关注下方公众号回复【kiro】获取工具

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPn7WSR6T3iciardwvmOl3QYQC1gf0hyicbYOicUbH88x1tRibG53XWGmyORYQMm1STFcgx5oPFM23EkpYw/0?wx_fmt=png)

菜狗安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QtaE6uFmibPn7WSR6T3iciardwvmOl3QYQC1gf0hyicbYOicUbH88x1tRibG53XWGmyORYQMm1STFcgx5oPFM23EkpYw/0?wx_fmt=png)

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