---
title: Burp Suite 自动化 API 提取与批量验证插件
url: https://mp.weixin.qq.com/s/9rOygN6KmKi2JIEFVaLvXA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:32:39.405525
---

# Burp Suite 自动化 API 提取与批量验证插件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODypM7oDdMU6hlggZGouPicUPEGG4P7p8Lbce7iaU00F9Eg0ibploxYIas6u0yYdkfEKcE8LtLfRZ5fRRGOyuVLuO78tEwNcv5ymcs/0?wx_fmt=jpeg)

# Burp Suite 自动化 API 提取与批量验证插件

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# Burp Suite 自动化 API 提取与批量验证插件

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

**Burp\_Parsing** 是一款 **Burp Suite 自动化 API 提取与批量验证插件**，通过智能正则从 HTTP 响应中挖掘潜在端点，重组为可测试请求并支持 *多线程批量重放*，适用于未授权接口挖掘与快速资产测绘场景。

## 🚀 一句话优势

  通过 **Parsing + Replayer 双模块联动**，将"发现接口→构造请求→批量验证"流程压缩至右键三次点击，解决手工提取参数与重复发包测试的痛点。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 智能提取 | 正则解析响应中的API路径与参数 |
| 请求重组 | 自动填充测试值并支持GET/POST切换 |
| 批量验证 | 多线程并发测试接口存活状态 |
| 被动监听 | 实时捕获Proxy流量中的API与Swagger |
| 联动测试 | 一键发送至Repeater或Batch Replayer |

## 📸 运行截图

| 提取界面 | 分析面板 | 批量验证 |
| --- | --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwJicibRE2oicoWodMQz5ElsYMDjSGoRUFgxE69jl0R2ibliacQphJnLgoM2z9BL6Heek7ibnyjcxjZYVsT5ARZfy5nyNRsFHcqzSl7k/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzPvVyQiaFD5Z92icW9uVuZAezDj6C4gbHRU2Ph0LuFXfIgEJZWIOKmDC7DDyRF1Rb6Gib6IljI7wkAibbHKNqLQ9NicbLzLnibt0WJE/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODz4YvyfcEDxJ8YfeakX63ViamtYMSkzksmtOQDljE3Yo6S7JnBDKq0r0jOcwkeuQ6vKyI9DwOBAoj69jySbWibZlricPeQ7SxiavwI/640?wx_fmt=png&from=appmsg) |
| Proxy历史右键提取API | 查看重组后的可测试请求 | 多线程并发与响应排序 |

## ✨ 核心亮点

### 1. 智能提取与请求重组

  插件通过 **右键 Extract to API Hunter** 自动从响应中正则提取 API 路径与参数。针对 *page、id、size* 等常见字段自动填充测试值，并支持 **一键切换 GET/POST 格式**（Query String 与 JSON Body 互转）。这种设计让原本需要手工复制-粘贴-修改的接口测试准备时间从分钟级降至秒级。

### 2. 批量验证与可视化筛选

**Batch Replayer 模块** 支持多线程并发请求，实时展示 *状态码、响应长度、耗时* 三列核心指标。提供 **按响应长度排序** 功能，快速定位异常接口。自动过滤 *.js/.css/.png* 等静态资源与指定域名，避免无效请求干扰结果。

### 3. 被动监听与实时捕获

  开启 **Listening 模式** 后，插件在后台实时监听 Proxy 流量，自动捕获响应中暴露的 API 路径及 *Swagger 文档定义的接口*。支持自定义请求头覆盖（如添加 Auth Token 测试鉴权绕过），发现即测试，无需手动导入目标列表。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Jython原生 | 纯Python编写Burp插件 | 无需额外编译，源码可审计 |
| 多线程并发 | 可配置线程池批量发包 | 提升大规模验证效率 |
| 智能过滤 | 静态资源与域名黑名单 | 减少噪音干扰 |
| 请求头继承 | 默认携带原始Cookie | 保持登录态测试 |
| 双模式切换 | Parsing与Replayer独立运行 | 灵活适配不同测试阶段 |

## 📖 使用指南

① **准备工作**（安装与配置）

  下载 Burp\_Parsing.py，在 Burp Extender 中加载（需 Jython 环境）。进入 **Batch Verification** 标签页配置 *白名单域名* 与 *自定义请求头*（如 Authorization 字段）

② **核心操作**（提取与重组）

  在 Proxy/Repeater 历史记录中 **右键响应包** → *Extract to API Hunter*。进入 Analysis 标签页查看提取结果，选中接口右键发送至 **Batch Replayer**。支持 Shift 多选批量导入

③ **结果查看**（验证与分析）

  在 Batch Verification 面板点击 **Send Request (Batch)** 启动多线程扫描。关注 *响应长度异常* 的接口，右键发送至 Repeater 进行手工验证。使用 **搜索功能** 快速过滤特定路径关键词

## 📖 项目地址

```
https://github.com/w-sega/Burp_URLReplayer
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

| ![img](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODwPr8UpJD9OuY73Pzy9eXu2BVToMrV0kP6GrqGroWjhE0k5TXvDx2MGoXjHrcOU9FeF8wia7NhFXXv1iaTz0MnQ4pJguN7DwiaeV4/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
| --- | --- |
| ![img](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODzCtog7ElLXnrLg7t9j99DftdLLjjVKFwP6unsUPX1EquflicE51wMFjB3zIBWLf6W3qFHA5modicNn3XbwJE8roDq7njXZRfjuo/640?wx_fmt=jpeg&from=appmsg) |

### 推荐阅读

✦ ✦ ✦

| [渗透测试人员必备武器库：子域名爆破、漏洞扫描、内网渗透、工控安全工具全收录](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485592&idx=1&sn=818004a6d625c4c4112ce73b83433854&scene=21#wechat_redirect) |
| --- |
| [AI驱动的自动化红队编排框架(AutoRedTeam-Orchestrator)跨平台支持，集成 130+ 安全工具与 2000+ Payload](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485309&idx=1&sn=292afbe37fb95c64f33470f915b0c54e&scene=21#wechat_redirect) |
| [JS逆向必备：这款插件能Bypass Debugger、Hook CryptoJS、抓取路由](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247486181&idx=1&sn=3ace47da643c72cec0d615aeccb955ac&scene=21#wechat_redirect) |
| [上传代码即审计：AI 驱动的自动化漏洞挖掘与 POC 验证平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485488&idx=1&sn=a37acb031febe69db608de53ddee5732&scene=21#wechat_redirect) |
| [AI 原生安全测试平台(CyberStrikeAI)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485208&idx=1&sn=b5181181c1e0800124e3e099706ef2ef&scene=21#wechat_redirect) |
| [多Agent智能协作+40+工具调用：基于大模型的端到端自动化漏洞挖掘与验证系统](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485805&idx=1&sn=8f374a239135f6a753d5cce887f8318b&scene=21#wechat_redirect) |
| [基于DeepSeek的代码审计工具 (Ai-SAST-tool.xjar)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485314&idx=1&sn=56082cd314311ffc15cc0bcf03a395e2&scene=21#wechat_redirect) |
| [基于AI的自主渗透测试平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485127&idx=1&sn=b5eb3fdc1cc23976011e2bca396c1bc7&scene=21#wechat_redirect) |

✦ ✦ ✦

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

0x八月

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

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