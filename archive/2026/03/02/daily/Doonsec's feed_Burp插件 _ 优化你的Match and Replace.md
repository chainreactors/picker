---
title: Burp插件 | 优化你的Match and Replace
url: https://mp.weixin.qq.com/s/k4Of0Hxkzm7ALG4HlguMhg
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:08:13.921224
---

# Burp插件 | 优化你的Match and Replace

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVlvVLH9B0TOm9rbTvvT5uxibZODFw6ibgciahS8rkHYPKLjV8Vdf63hI9wwbnh0ia2L7RhDurUEVHfibicz7gxHBJJ9HiasBdhdiaIjweo/0?wx_fmt=jpeg)

# Burp插件 | 优化你的Match and Replace

gh0stkey
gh0stkey

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 631，阅读大约需 4 分钟

## 前言

项目地址：https://github.com/gh0stkey/MaR

![fa104c1bcf3e31eab001950229f1fe70.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmmiaFkiaqvyrlrMkeBrmg8S4G2icLxjSdtUUVyAOxht0Lh7QfXibXodT0e90nGAf1qn3OUVFhUHv0scWQ9JbyV6yic7uFuxKMnWG0Y/640?from=appmsg "null")

fa104c1bcf3e31eab001950229f1fe70.png

**MaR**（Matcher and Replacement）主要用于对 HTTP 协议报文进行精准匹配和智能替换。它可以根据用户定义的规则，在满足特定条件时自动修改 HTTP 请求或响应内容，帮助安全研究人员在渗透测试过程中实现自动化的数据篡改。

**MaR**的设计思想来源于 BurpSuite 原生的 Match and Replace 功能，但提供了更加灵活和强大的规则配置能力，支持条件匹配、正则表达式、多作用域等高级特性。

**注意事项**:

1. 1. MaR 采用`Montoya API`进行开发，需要满足 BurpSuite 版本（>=2023.12.1）才能使用。

## 使用场景

1. 1. **参数篡改** - 根据条件自动修改请求参数值
2. 2. **响应修改** - 修改响应内容以绕过前端校验
3. 3. **请求注入** - 自动添加或修改请求/响应头

## 使用方法

**插件装载**: `Extender - Extensions - Add - Select File - Next`

初次装载`MaR`会自动创建配置文件`Config.yml`和规则文件`Rules.yml`：

1. 1. Linux/Mac 用户的配置文件目录：`~/.config/MaR/`
2. 2. Windows 用户的配置文件目录：`%USERPROFILE%/.config/MaR/`

除此之外，您也可以选择将配置文件存放在`MaR Jar包`的同级目录下的`/.config/MaR/`中，**以便于离线携带**。

![f74b6158eebbc63cdd08683a358700a4.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmpcB9eibI73DvyRasl101l1n7EoT0tmiasK52icmvJBWLo3StUn7icAyyGNkdyu5hNyg2KumuDbH2pMNednDbQFvepFkJd9jN8MYA/640?from=appmsg "null")

f74b6158eebbc63cdd08683a358700a4.png

配置的信息，在 repeater 当中也能使用
![03c81855e849c9d2778965251862f1df.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlotmicMnVBibJUic20shiboiaJiaaqLIbemlOg97wTB4QUVpMqJaiacyxbSpJPSy5qgibkUE2piafF5SmJcfmzEqDrT1zyfAEke8GVvIzs/640?from=appmsg "null")

03c81855e849c9d2778965251862f1df.png

## 快速使用

![b0c52c78cb67b9875098f1b6256a5568.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkA0krQUum07Utdzca36HZoGAP3kCxc8gviaQHcBCMJqgricvc8YGVexxpWjjlcAKQvdicEUnMl4yyIgU3AibDVfrtWVia9cXWKI35E/640?from=appmsg "null")

b0c52c78cb67b9875098f1b6256a5568.png

按照需求填写即可
![4e0460a6fb21168dde0bd1f55783fbfd.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnC3D1icnia5ibq2T8Fg5v9s0JtyEeX1aDyB8G0lNWXia8rlpOypCMR6NM1BjE3QGJmvxddz06LrZEwUGgDZU31oZZTiaG8fOQ8SspI/640?from=appmsg "null")

4e0460a6fb21168dde0bd1f55783fbfd.png

### 功能说明

**规则配置项**：

| 配置项 | 说明 |
| --- | --- |
| Name | 规则名称，用于标识规则 |
| C-Scope | 条件作用域，指定在哪个部分检查条件 |
| Relationship | 匹配关系，支持"Matches"（匹配）和"Does not match"（不匹配） |
| Condition | 条件内容，用于判断是否执行替换 |
| C-Regex | 条件是否使用正则表达式 |
| M-Scope | 替换作用域，指定在哪个部分执行替换 |
| Match | 匹配内容，要被替换的内容 |
| Replace | 替换内容，替换后的新内容 |
| M-Regex | 替换是否使用正则表达式 |

**支持的作用域**：

* • `request` - 完整请求
* • `request method` - 请求方法
* • `request uri` - 请求 URI
* • `request header` - 请求头
* • `request body` - 请求体
* • `response` - 完整响应
* • `response status` - 响应状态码
* • `response header` - 响应头
* • `response body` - 响应体

**配置管理**：

1. 1. **Exclude suffix** - 排除指定后缀的请求，避免对静态资源进行处理
2. 2. **Block host** - 排除指定域名的请求
3. 3. **Scope** - 选择 MaR 生效的 BurpSuite 模块（Proxy、Repeater、Intruder 等）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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