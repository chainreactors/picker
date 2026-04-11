---
title: 一键提取 API 与敏感信息：隐藏接口挖掘利器
url: https://mp.weixin.qq.com/s/KgoWti0n3ckOVrXSNPOaRw
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:14:26.702400
---

# 一键提取 API 与敏感信息：隐藏接口挖掘利器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODyakzMJXBghu2vo8WLy5zjm4Hib3iczakAyUm0fVS26DdRADMKPqmJzX0NJa9f6yPaZQY1L4bspeB5EOdZmmQFCk2kHChyDXgzCI/0?wx_fmt=jpeg)

# 一键提取 API 与敏感信息：隐藏接口挖掘利器

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一键提取 API 与敏感信息：隐藏接口挖掘利器

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  LoveJS 是一款**浏览器安全插件**，支持 *Chrome/Firefox/Edge* 三大平台，可自动提取页面及 JS 文件中的 **API 接口**、敏感信息（邮箱、手机号、云 Key 等），提供*批量 URL 打开*、基础目录自定义、**本地记事本**等辅助功能，面向**前端安全研究员**与**渗透测试工程师**，提升接口测试与漏洞挖掘效率。

## 🚀 一句话优势

**一键提取页面所有隐藏接口**，支持 **敏感信息自动识别**与*批量 URL 测试*，浏览器原生即开即用。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 接口提取 | 自动提取页面和 JS 中的 API 端点 |
| 敏感信息 | 识别邮箱、手机号、云 Key 等 |
| 批量打开 | 支持多 URL 批量打开（防卡顿设计） |
| 基础目录 | 自定义接口前缀（如 /api/） |
| 本地记事 | 渗透笔记本地持久化存储 |
| 域名黑名单 | 指定域名跳过处理 |

## 📸 运行截图

| 功能模块 | 截图占位 |
| --- | --- |
| 接口提取结果页 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODycicj9UHhUXXCrbBnYY9XDaMCmJm6xKmK0x3bDUCqDUy7IpZewWJibGdgHiahvRGyDJ4PJygUtj3AO91XMhDXwQBLLla4LWE26xw/640?wx_fmt=png&from=appmsg) |
| 批量打开 URL 界面 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwaEziaOfPoic9CMYLNu8Cia8uojGrgHZ6FgOUc9LDSsaqHpUbjgh6wRyuGZMElFq0guThThO6Im85IUicpE7Irpz6qib993pdjaiaicw/640?wx_fmt=png&from=appmsg) |
| 记事本 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzAhE8m9n0rSM80lYhqnZSO0jaiaWduEktiaTcqUagpv5JFH0xh93QdVib1pffKI0mJGDic16WYJ1fq1ZzadoniaUcGsRfBIIjQKAWc/640?wx_fmt=png&from=appmsg) |
| 自定义基础目录和域名黑名单 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyUqK8yVEelF1Qv1h6DxCpfXFUXNlbqVVsz7buBUiby0Zq2Jz6G8KHHmIianBxsgZtU0T1uxnwA0RibYObCicO1eHbjxKuiaXzKXpz8/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 前后端接口自动发现

  自动解析当前页面及引用的 **JavaScript 文件**，提取其中隐藏的 *API 端点*、路由路径、**请求方法**等信息。相比手动审查 JS 代码，效率提升**数十倍**，特别适合**前后端分离**架构的 Web 应用。提取结果支持**仅复制接口路径**或*复制完整 URL*两种模式，方便导入 手动批量打开 或Burp Suite进行进一步测试。

### 2. 敏感信息智能识别

  内置**正则匹配规则**，自动识别页面源码及 JS 中的 *邮箱地址*、手机号码、**云服务商 AccessKey**（阿里云、腾讯云、AWS 等）、*JWT Token*、内部 IP 地址等敏感数据。发现潜在**信息泄露**风险，帮助研究员快速定位*配置错误*或硬编码凭证问题。

### 3. 渗透测试工作流整合

  提供**本地记事本**功能，笔记内容*自动保存*至浏览器本地存储，刷新或重启不丢失，方便记录测试过程中的**关键发现**。支持**批量打开 URL**（建议分批操作防卡顿），结合*自定义基础目录*功能（如统一添加 */api/* 前缀），实现**接口快速fuzz**与*权限绕过测试*。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| 浏览器扩展 API | Chrome/Firefox/Edge 原生支持 | 跨平台兼容，即装即用 |
| 本地存储 | IndexedDB/LocalStorage | 数据隐私，不上传云端 |
| 正则匹配引擎 | 多模式敏感信息识别 | 快速发现泄露风险 |
| 内容脚本注入 | 页面级 DOM 与 JS 分析 | 深度提取动态生成接口 |
| 轻量级设计 | 纯前端实现，无后端依赖 | 体积小巧，响应迅速 |

## 📖 使用指南

① **准备工作**：从 GitHub 下载插件压缩包并解压，Chrome/Edge 进入**扩展管理页**开启开发者模式，点击**加载已解压的扩展程序**选择文件夹。Firefox 用户直接访问**插件商店**搜索 *LoveJS* 安装。

② **核心操作**：访问目标网站后点击插件图标，**信息搜集**页自动显示提取的*接口列表*与敏感信息。点击**复制完整URL**可自定义*基础目录*（如 /api/），系统会自动拼接域名与接口路径。在**批量打开URL**页粘贴目标地址（建议先放入**记事本**分批处理），一键打开多个标签页进行测试。

③ **结果查看**：提取的接口与敏感信息直接展示在插件弹窗中，**记事本**内容*自动保存*至本地。域名黑名单可在设置中配置，避免对非目标站点执行分析。

## 📖 项目地址

```
https://github.com/n0name-X/LoveJS
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| ![img](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODzqznt4G547C7mfsCQjGvLqFkq97LtaleWCGdwgmEBC5CiagC6icNaIgkLFQhDpEKW3licSrWMib6WoiaU3EqwzEPgKCdib0Hx8hS3Bg/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
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