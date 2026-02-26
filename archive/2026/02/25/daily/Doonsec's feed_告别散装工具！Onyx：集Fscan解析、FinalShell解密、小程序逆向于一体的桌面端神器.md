---
title: 告别散装工具！Onyx：集Fscan解析、FinalShell解密、小程序逆向于一体的桌面端神器
url: https://mp.weixin.qq.com/s/wAA0-Ykxl6k6foJ1QUv9mA
source: Doonsec's feed
date: 2026-02-25
fetch_date: 2026-02-26T04:10:41.988298
---

# 告别散装工具！Onyx：集Fscan解析、FinalShell解密、小程序逆向于一体的桌面端神器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T0ibbhsCmribQJVdfSIgKmzQWtcjYBKBPqEDOCvauw8aeo2N2EL6MpU9EREIKGtnS3Q3V2DxzWOrURcpTGFwMhMbbwjoZvjTBx7IbebibA6QRM/0?wx_fmt=jpeg)

# 告别散装工具！Onyx：集Fscan解析、FinalShell解密、小程序逆向于一体的桌面端神器

网络安全民工

![]()

在小说阅读器中沉浸阅读

以下文章来源于泷羽Sec-Norsea
，作者Wraink

![](http://wx.qlogo.cn/mmhead/JRicrayPGR3PTicBJ4QyNtQKGAicQSlbupDdZhS6rYAClOL0uRWWp7d8HDZb8QbmibrpTQfwm51TqPs/0)

**泷羽Sec-Norsea**
.

归去来兮，应归何处。

在日常的渗透测试和红队攻防中，大家应该都有一个痛点：**工具太碎了**。

信息收集要开`Fofa`、`Hunter`网页，漏洞扫描要挂`Xray`或`Nuclei`，遇到小程序反编译要切到脚本目录，解密`FinalShell`密码又要去找专门的工具……

桌面窗口切来切去，不仅效率低，心也很累。

今天给师傅们推荐一款名为 **Onyx** 的开源安全测试工具集。

它基于 **Wails v2 + Vue 3** 开发，颜值高、跨平台，主打的就是一个**“一站式”**，把我们常用的功能都整合到了一个桌面上。

工具地址见文末

## 🛠️ 项目简介

**Onyx** 是一款现代化的安全测试工具箱。作者的设计初衷就是为了解决“到处切换工具”的麻烦。

它集成了`空间测绘`、`漏洞扫描`、`主机探测`、`信息收集`、`应用解密等核心能力`，`底层使用 Go 语言（Wails）`，前端使用`` Vue 3`，保证了性能的同时，UI 界面也非常整洁舒适。

| 模块 | 说明 |
| --- | --- |
| **空间测绘** | 集成 **Fofa**、**Hunter**、**Quake** 三大测绘引擎，支持批量资产导出 |
| **漏洞扫描** | 基于 **Nuclei** 引擎，支持 POC 管理、批量扫描、请求包可视化、一键生成验证图片 |
| **辅助工具** | 内置 **CyberChef**、JWT 密钥爆破、编码转换、Fscan 结果处理、攻防批量截图 |
| **应用加解密** | 提供 **FinalShell**、**Navicat**、**蓝凌**、**致远**、**帆软**、**Druid**、**JBoss** 等常见应用/中间件的加解密工具 |
| **小程序分析** | 支持微信小程序自动识别、反编译 (`.wxapkg`)、敏感信息正则提取 |
| **企业信息** | 支持 IP 归属地查询、ICP 备案信息查询、企业与股权结构分析 |
| **信息探测** | 包含端口扫描、杀软识别、指纹识别、敏感信息采集 (JS 分析) |

## 🔥 核心功能亮点

### 快速启动工具箱

![](https://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fpyMnF0iahIicxUCxjo8ru1ia9sW5N6SfLVfyLMaiafIOpTy5F9zhaMw64KLVyw9tEfBgoxVETqPrh1Q/640?wx_fmt=png)

### 空间测绘

支持多种网络空间测绘引擎

![](https://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fpyMnF0iahIicxUCxjo8ru1iapAnib0k39SZk9g2iawL8trbjplGaoQRWiaKBOyvzH148ibup4s0iaKlb2pQ/640?wx_fmt=png)

### 漏洞扫描

* **Nuclei** - POC兼容Nuclei模板格式
* **POC 编辑器** - Monaco 编辑器，支持语法高亮
* **请求重放** - 支持自定义 HTTP 请求

**漏洞管理：**

![](https://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fpyMnF0iahIicxUCxjo8ru1ia4KiahGprOj2ib4uElIgoxzglnibW3ICtV9VtWiaq1eLd2aDhvYTnuUfaMA/640?wx_fmt=png)

**自定义POC：**

![](https://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fpyMnF0iahIicxUCxjo8ru1iam7j3G9MKicP4HWQpJw3KZPkuG9Qg1mfYkdFVzjI8hfDZCfB2YibGO3ow/640?wx_fmt=png)

### 信息搜集

* 通过域名查询相关企业信息
* 股权结构分析
* 资产收集与关联分析

![](https://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fpyMnF0iahIicxUCxjo8ru1iaNI6Oq2IvUmRaUPdVzB7vib4Znnm6vqLazHBXLZfpVVRgtmgicYicW1CXg/640?wx_fmt=png)

### 攻防赋能

#### FScan 结果处理

自动解析和格式化 FScan 扫描结果

![](https://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fpyMnF0iahIicxUCxjo8ru1iatda49michZcQ7bD2vcRn6rGpdQibT3kxBbzSAVwFTGfE6TZ7ic8xkwFww/640?wx_fmt=png)

### 泄漏利用

#### 微信利用

支持公众号、小程序、企业微信的 AK、SK 利用

![](https://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fpyMnF0iahIicxUCxjo8ru1ianHQpUSzxJNCb1xwmpKKiaxv1UaGr29PYLBrTXOh73BZ4oXojDwibo0rg/640?wx_fmt=png)

### 微信小程序

* **自动扫描** - 自动扫描微信小程序
* **小程序反编译** - 微信小程序反编译与代码分析
* **小程序敏感信息搜集** - 自动提取小程序中的敏感信息
* **自定义正则表达式** - 支持自定义正则表达式进行信息匹配

![](https://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fpyMnF0iahIicxUCxjo8ru1ia4x0JZHnaWJBExWTVyEjlIUQgicCtEMaABiajy5ZyjbC6ibPNoel3k2wIQ/640?wx_fmt=png)

```
工具地址:https://github.com/Mstce/Onyx
```

## 学习交流群

刚加入网络安全行业的小白，可以加入学习交流群，大家一起互相学习，互相进步，不会的难题大家一起学习，一起攻克。

想要进学习交流群的师傅们，可以扫描下方二维码添加好友，我再拉你进群（Ps：防止广告进群）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9dEclFnKnAAurt1AlnO1HBLiaRymULG1ibJJhXlNjMH1rd1SgQQWIyFBVTRMteWWfiby3FCWfpB7n2oA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYkgXg13os3mdJEN1k241aoU461aOjdLSrQvIscf5u8YrTFoPKmQZF8d26FIsE0wb5pS8Gdadytia6g/0?wx_fmt=png)

网络安全民工

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYkgXg13os3mdJEN1k241aoU461aOjdLSrQvIscf5u8YrTFoPKmQZF8d26FIsE0wb5pS8Gdadytia6g/0?wx_fmt=png)

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