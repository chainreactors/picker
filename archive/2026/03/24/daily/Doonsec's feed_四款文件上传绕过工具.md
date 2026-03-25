---
title: 四款文件上传绕过工具
url: https://mp.weixin.qq.com/s/LHsyF1JXN03bxzkt8CPGGw
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:13:30.262989
---

# 四款文件上传绕过工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVkEksviblNY5IDlPeOkKoic18DNW2t48vkfHPqSNJ7Zqt2CJeSYicUGmEJkibgxarxE0FZFqBFHtsjpUI1L0hh7lO0QL5mdT1S9UD0/0?wx_fmt=jpeg)

# 四款文件上传绕过工具

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 395，阅读大约需 2 分钟

## Upload\_Auto\_Fuzz

项目地址：https://github.com/T3nk0/Upload\_Auto\_Fuzz

![6185a39dc5e322864463264c5374e337.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnWibPNC68riad9YnjdiaBSLiawDS3uv79IbQHrodj6Yb5aZWD8ibHkFCwObbCTicJsPQPHyhphjtjuQkNgtHgCYp96A5WNjg8WIE0n4/640?from=appmsg "null")

6185a39dc5e322864463264c5374e337.png

Burpsuite插件，专为**文件上传**漏洞检测设计，提供自动化Fuzz测试，共500+条payload。
在intruder模块下使用。

**使用**
参考之前的文章：Upload\_Auto\_Fuzz

## UploadRanger

项目地址：https://github.com/Gentle-bae/UploadRanger

一款专业的文件上传漏洞检测工具，支持多种绕过技术检测和自动化扫描。

![7ae88c4575c3d49110bb94cbed94f964.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmXvGu4E0a8ZyBIwDz7VQu6051CCAIaneafC8ib1NYUCMOmPURmDo8deGdKWqiclWIvfMoHGsia12jhUfx6Y3aKnJx0ExYUNfeHtE/640?from=appmsg "null")

7ae88c4575c3d49110bb94cbed94f964.png

打开后页面
![5755eb14eff14b5373b9105c54ce31ed.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlicnmmUaCSsic5s9VJCdUhibH4jTe0kHFwFcT1FaqVaTV8UxzuUBIek6MAO3B6G88aiaNsOPSfGuPWYI7iasSxw0xOWJtTgaFHSp5A/640?from=appmsg "null")

5755eb14eff14b5373b9105c54ce31ed.png

**功能特性**

* • 智能扫描：自动检测上传点，分析响应内容
* • 代理抓包：内置 HTTP/HTTPS 代理，支持拦 截、修改、重放
* • Repeater：手动重放请求，调试绕过技术
* • Intruder：自动化爆破，支持多种攻击模式
* • 263+ 绕过技术：支持各种文件类型绕过、Content-Type 绕过、WAF 绕过等
* • Payload生成器：支持WebShell、Polyglot等多种载荷生成

## Upload\_Super\_Fuzz\_Gui

项目地址：https://github.com/7797777977/Upload\_Super\_Fuzz\_Gui

![2a0d8c3c231a6932494290974d840f4b.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkvnJG5lW6ZibsgLNa7OsM1FRTl9Ic8sTibibwebjHLFczTltOWB230yJMAdOnBZ4BpOhVkyviaNZoiavc2VE2Lj4RRvT0eA1FHd4Ik/640?from=appmsg "null")

2a0d8c3c231a6932494290974d840f4b.png

页面
![72c162dc1fc200bfeda713f9aceb4d7f.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnEmERnicAqYNmeTjqibC9sia9RdJ7vBtCmQnmT6oBQHg6mROsyfX9TmqlwK1yt1OzHAa58lhMWtSw4Hb9yfCSGDYrj4V4NkK9eibQ/640?from=appmsg "null")

72c162dc1fc200bfeda713f9aceb4d7f.png

1：多样化Payload生成 文件后缀绕过 Content-Disposition字段绕过、`Uploading 2.png…`

Content-Type变形 WAF绕过技术 魔术字节伪造 特殊字符和编码技巧 文件内容欺骗 配置文件上传绕过

2：灵活的代理支持 可自定义代理服务器 支持启用/禁用代理 方便进行匿名测试和网络环境模拟

3：直观的用户界面

简洁现代的设计 实时测试进度显示 可排序的测试结果表格 详细的Payload和响应信息

4：多种文件类型测试

覆盖PHP、ASP、ASPX、JSP等常见服务器端脚本 模拟各种文件上传场景

![01202517cb6ddfdea7d528071567097d.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlnQFkjfVwhsStbyq9N9M6peyVVicmrcGSGNmWSLukEz6tWbLHFibgAsQjbruYAznWjZCGj6iaGaCKgbCp7sqLbnlB32ks9rW63Kk/640?from=appmsg "null")

01202517cb6ddfdea7d528071567097d.png

## upload-fuzz-dic-builder

项目地址：https://github.com/c0ny1/upload-fuzz-dic-builder

![101d847bcf9ac9ea902e03d1dee16d23.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlCX1sZL8vwA0e77ShhYnMOjhwAGicNB5IIPUJk8ywiblO6dBYpVOyRzfX4wQynteImtib0ibopbYU0KiaWIdiaxW101Xibicu8qQaVqE8/640?from=appmsg "null")

101d847bcf9ac9ea902e03d1dee16d23.png

生成结果参考：
![45c0f4015378fbbad3a2b834133c01cb.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk1UVQxCHNXuNPIBc6JEs111FKo693PkmMEwHdw80YNCOibjKMF6bic0NabRibs5QRibXhSxHBLia6kuF9G6BbSEbQ1tE8MxAVowmEM/640?from=appmsg "null")

45c0f4015378fbbad3a2b834133c01cb.png

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