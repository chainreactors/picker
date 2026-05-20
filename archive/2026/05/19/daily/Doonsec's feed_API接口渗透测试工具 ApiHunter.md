---
title: API接口渗透测试工具 ApiHunter
url: https://mp.weixin.qq.com/s/71noaDtLm-YkAMbUsGHZrQ
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:01:56.158616
---

# API接口渗透测试工具 ApiHunter

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVkEjYapyMDJ61ExmVmvic1BAnA4RYylyBcK4BdnLzWZfccCzOOQCh0VX9XkF4coiaiasg58zrvbI88rIXBghhPnQMLFFjMwVTGtgk/0?wx_fmt=jpeg)

# API接口渗透测试工具 ApiHunter

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 377，阅读大约需 2 分钟

# 前言

ApiHunter 是一款面向渗透测试人员和安全研究人员的 API 接口自动化安全检测工具，核心目标是简化 API 安全检测流程，提升渗透测试效率。

项目地址：https://github.com/11firefly11/ApiHunter

![ccce2f9ab6a4a78ee209a0efea3da379.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkZarqd6oC4grN7ichgwPHLqhkh7npSibSgQq0nfbhFzxuMicSicdrUibFa2iaA01vs8EL8142foE2VziauMMDglOVficsVCSmwmibibnGFI/640?from=appmsg "null")

ccce2f9ab6a4a78ee209a0efea3da379.png

专为 API 接口安全检测设计，无需复杂配置，支持多种 API 文档一键导入、智能参数填充、批量漏洞扫描，解决手动测试效率低、覆盖不全、易误操作的问题。

![64c51812ee1d60c34584f4b84204ba9e.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkzHFymHQfibdoz3z5DBCWdfzN1GYibmOhyfZibGH3ETczw3mWDg88pnTPiaiacmfbricKAhJrEJFrqWVsQMbBxqD4ydnBQNz9qD7KXQ/640?from=appmsg "null")

64c51812ee1d60c34584f4b84204ba9e.png

## 快速使用方式

1. 1. 直接双击 `ApiHunter.exe` 启动程序（开箱即用）；
2. 2. 测试方式：

* • 单目标：输入 URL 和接口路径，点击测试；
* • 文档导入：输入 Swagger/ASP.NET 文档地址，导入后点击「swagger」批量测试；

3. 3. 结果查看：扫描结果实时展示，可过滤指定状态码（如 404/500），支持导出/复制结果。

支持的接口文档
![0a9f4bbb6b63f366741145be1d01fd1c.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmnlxzau5Ib8AR6lObdaZbib2w3qOGjRVsGyPjicbMtM9LR2KZyM5icY0sictfBJjKdzZoRbJTRicDYkuib8r2MI0svxWI3LuKNZr6j0/640?from=appmsg "null")

0a9f4bbb6b63f366741145be1d01fd1c.png

### 安全设置

在设置中，默认配置为`安全模式`，有常见危险操作的关键词，避免在渗透测试中破坏系统。
![84e291ffa7a402487c9a6bcde1a54784.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnyR9OF49hqBq7zRlefDVE90oBomfW7jHZ4rAiatMdFMnGzZibAhyzpAwZA1MjRQibWe9bRfzSWyU2NtHolRXDspU7zQkQRxy40Og/640?from=appmsg "null")

84e291ffa7a402487c9a6bcde1a54784.png

### 自定义参数

除了内置规则外，还可以自定义参数
![ec4c2c1326989c5e850199686b8568e0.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkiaxV2y1LqNSqC3gCDjicVAia5fAqkJ4UFe6ydAU9Odf4Ukxrwh7bc3WsWEjCialPhObTB0TD5QDsrayP7icEaCdJnsItuiaFJAe6Is/640?from=appmsg "null")

ec4c2c1326989c5e850199686b8568e0.png

配置完成后，如果 api-docs 存在相关参数，会在导入 api-docs 后自动添加到后面
![cb918f669eac0599b753238b9bc8f2e8.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmSKjgemYe696WQC6micKw4bYFibdkhGJ6iaNu8BXfUyV821uld7MsozpLJqkIWTWpb26QpibWEjeict0Hqx8MsqCmbKk34S2Fv12dE/640?from=appmsg "null")

cb918f669eac0599b753238b9bc8f2e8.png

### 敏感规则

![a7de0ebe53f0071aaa9ead6aa023a055.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVm5OpT2icrW8Uic8MicSdmaNyJDwmVtElWANThHibVAR3eY4xz0ZXcBcEPWNm79PpTeRQCsyVOPHTPELYicF3LAicypF7OXaV0ichtiaa4/640?from=appmsg "null")

a7de0ebe53f0071aaa9ead6aa023a055.png

### POST 格式

也可以根据需要配置 POST 请求格式
![ddd9f2032e97a44fe243059cf94dcf1a.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnx9bJZVL5NpoZV0jiaq41vtuBVvqtLGgsGzN2Iqkke5HxicQIsxOssia16yQ18Cz2tticIN2icEFxx7DPPwwiak1lDicLOD7wR1JON4A/640?from=appmsg "null")

ddd9f2032e97a44fe243059cf94dcf1a.png

## 总结

挺好用的 API 接口渗透测试工具，只要找到 api-docs 都可以放里面试一试。

项目地址：https://github.com/11firefly11/ApiHunter

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

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