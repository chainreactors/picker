---
title: VulnRadar：集成多模块的Chrome浏览器安全渗透测试扩展
url: https://mp.weixin.qq.com/s/gN_K408O-acsf8LydpDJFw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:11:22.312404
---

# VulnRadar：集成多模块的Chrome浏览器安全渗透测试扩展

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicJll2F8icaf5ibwMV9jdsiafMtOkqDe33pwAwo7at0VzAiaXevk7C4dDF41oibW3nsHuTAZZWsqKABlyK8UDqnPO6hDmyqAWAkQKDnw/0?wx_fmt=jpeg)

# VulnRadar：集成多模块的Chrome浏览器安全渗透测试扩展

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[NetSonar：跨平台多协议的开源网络诊断工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486769&idx=1&sn=1e45bd9e7fa03e5dafa6335010f10e75&scene=21#wechat_redirect)

·[CTF和实战可用-文件上传漏洞检测专业工具：UploadRanger](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486761&idx=1&sn=ad09098ab205e45600339e0aa9dfa836&scene=21#wechat_redirect)

·[FlagHunter：CTF专用签到题Flag快速搜索工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486740&idx=1&sn=f3c6022d61fe9921c4259d639e63e7fe&scene=21#wechat_redirect)

·[SwordfishSuite：多平台抓包分析利器-现代化 Web 安全测试平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486734&idx=1&sn=4e5310b6adb0b5ee09c917b3bbf851d9&scene=21#wechat_redirect)

·[快速OpenClaw云部署教程：扣子平台接入飞书实现Ai自动办公](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486721&idx=1&sn=116249d6712546c4723075e095f75775&scene=21#wechat_redirect)

·[HackerMind：三AI架构自集成MCP的链上对话智能渗透系统工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486640&idx=1&sn=19052c6dd7b1d73d9b8395857276042f&scene=21#wechat_redirect)

**背景分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicK8SNdHsQKmjRg7cwWQEyFyl0JdiawKV8S5JnSuuylFxLA9G5AKO0eF0WkzZfTKkyRu0mKd3xYpXvxR7BVZjwhMfbfOojyt3j4o/640?wx_fmt=png&from=appmsg)

当下`Web`安全渗透测试过程中，存在`JS`端点发现、敏感目录查找、漏洞检测等环节需依赖多款工具分散操作的问题，操作繁琐且效率较低，同时手动排查易遗漏关键漏洞。`VulnRadar`作为面向`Web`安全渗透测试的`Chrome`浏览器扩展应运而生，将六大安全检测模块集成于浏览器中，支持手动/自动扫描、实时告警、结果多端展示，可提升红队打点与渗透测试效率，实现快速信息收集与初步漏洞发现。

**安装介绍**

```
地址：https://github.com/Zacarx/VulnRadar
```

`Chrome`浏览器扩展安装前置操作：

```
# 1. 打开Chrome浏览器，在地址栏输入chrome://extensions/进入扩展管理页面
# 2. 开启页面右上角的“开发者模式”开关
```

`VulnRadar`扩展安装步骤：

```
# 1. 从项目仓库下载VulnRadar源码/已打包的扩展文件并解压至本地目录
# 2. 在Chrome扩展管理页面点击“加载已解压的扩展程序”按钮
# 3. 选择解压后的VulnRadar文件夹完成加载
```

扩展加载完成后，若`Chrome`浏览器扩展栏中显示`VulnRadar`图标，说明安装成功；若加载失败需检查文件是否完整、`Chrome`浏览器版本是否适配。

功能介绍

`VulnRadar`的`JS`端点发现功能可提取页面中`JS`文件的`API`端点，对提取的端点进行并行可访问性测试，检测端点返回数据中的敏感信息，针对403状态码的端点自动尝试绕过，并支持对目标端点进行一键测试，测试结果会在浏览器界面中实时展示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKpZKfvoSUbMkYQVQlrl9pfwPOXG6y7GSdEMt8PYTousa4wueficwB9o8l8FgqKf0UtqlQ700iaJlLPQic580DrExcfAn9AQVJUPM/640?wx_fmt=png&from=appmsg)

敏感目录发现功能可扫描目标站点的敏感路径，检测配置文件、备份文件泄露以及中间件管理页面等风险点，通过特征匹配的方式降低误报率，同时支持对疑似风险目录进行一键测试，扫描完成后会列出发现的敏感目录及风险等级。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIyuibOzjEpfQLb31gatyUAWua03HcI6HHJ7mLmiaCZzpaDJ55f531ckl3yTia7W9PLr86X5NJOqSKVtWtWxPBjmR2TQujssvToYw/640?wx_fmt=png&from=appmsg)

`DOM XSS`检测功能通过`Hook`浏览器中的危险函数、进行污点追踪的方式识别页面中的`XSS`特征，当检测到疑似`DOM XSS`漏洞时会实时触发告警，告警信息包含漏洞触发位置、危险函数及相关参数。

重定向漏洞检测功能可检测页面中的开放重定向漏洞，对重定向链接进行智能解码，识别链接中的危险协议，同时生成对应的测试`Payload`，测试结果会展示重定向目标地址、漏洞类型及`Payload`示例。

跨域消息追踪功能可实时监控页面中的`postMessage`事件，记录事件的发送方、接收方、消息内容等信息，支持过滤无关的跨域消息干扰，追踪结果会按时间顺序展示，便于分析跨域通信中的安全风险。

原型污染检测功能可测试`URL`参数中的原型污染漏洞，针对疑似污染点生成对应的`Payload`，检测完成后会报告存在原型污染风险的参数名称、`Payload`内容及漏洞危害等级。

`VulnRadar`支持手动扫描和自动扫描两种模式，自动扫描会在页面加载完成后触发全模块检测，手动扫描可由用户选择指定模块执行检测；所有检测结果除在浏览器界面展示外，还支持多端展示，便于渗透测试人员整理和分析。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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