---
title: Burp插件：全自动API接口挖掘与测试利器
url: https://mp.weixin.qq.com/s/sO1OD9FKHFRSNbJtSIKoBQ
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:12:53.135490
---

# Burp插件：全自动API接口挖掘与测试利器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODwyACwOeHG3ibgrEHGw5fI6yb4HBBKqTy0lARbGcdfRSDHkU4rO6WW6ae5tVnpqQ2tpzKl15YpMLxrcDozOvXRSzdob4nriaxbl8/0?wx_fmt=jpeg)

# Burp插件：全自动API接口挖掘与测试利器

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# Burp插件：全自动API接口挖掘与测试利器

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxTtd1QzPzIicbVCbOJIpzWRNUtjNnczNxIrl6QsY6JtyAkUDvtlgBgRFSd4Asf5iaY4bTPQdapxCic2IILs6ZCywroWS7ESvyx7k/640?wx_fmt=png&from=appmsg)

## 📖 项目/工具简介

**API剑** 是一款 **Burp Suite 插件化 API 挖掘工具**，全自动深度收集 HTTP 响应中的 API 接口与 JS 文件，通过递归请求与防环路设计实现 *零手动* 的接口资产测绘，适用于 Web 渗透测试与赏金漏洞挖掘场景。

## 🚀 一句话优势

基于 **Burp 流量生态** 实现被动+主动双重采集，解决传统 JS 工具与浏览器脱离、无法实时联动测试的痛点。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 流量捕获 | 自动提取Burp流经的所有响应内容 |
| 递归解析 | 从JS/HTML中深度提取API与链接 |
| 主动探测 | 自动请求提取到的API和JS文件 |
| 防环路机制 | 智能去重避免死循环请求 |
| 联动测试 | 一键将API发送至Burp Repeater |

## 📸 运行截图

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwFECyRTiaj21aHjQAsMmHoibGZKZRpEADRiba9LJxzmv92HS4EdEZQicIticfXX41TiciaIuJKts71XROI9icuQA9ic1lm2nHtZRAJNSlw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyTEoWfm51PVyGQkJ7XCpricVIXKwzGsTpzvZzYnNibof9JksOgo2rRPqxNrGcmvxJeAUjz8urjSWGFLMtnDZbHWqYMDBKnib4QI4/640?wx_fmt=png&from=appmsg)

## ✨ 核心亮点

### 1. 所见即所得的联动设计

API剑将提取的 API 与来源 JS 文件 **成对展示** 在 Burp 界面中。点击任意 API 即可在右侧查看其来源 JS 的完整响应，*Ctrl+R* 一键发送至 Repeater 进行测试。这种设计消除了传统工具"导出-复制-粘贴"的割裂感，让接口发现与漏洞验证在同一窗口完成。

### 2. 智能递归与防环路

插件不仅从初始响应中提取链接，还会 **主动请求 JS 文件并继续解析** 其中的新 API，形成递归采集。内置的 *防环路机制* 通过哈希去重与深度限制，确保不会因循环引用导致无限请求。用户只需在浏览器中正常点击功能，后台自动完成深度资产测绘。

### 3. 生产级稳定性设计

针对企业测试场景，API剑提供 **紧急刹车按钮**（立即停止所有请求）与 *危险接口过滤*（包含特定字符串则跳过）。支持自定义请求速率、线程数控制，以及可选的 *无 Cookie 模式* 专门测试未授权接口。所有配置与 Scope 范围支持持久化保存，重启后自动恢复。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Burp生态集成 | 原生插件化架构 | 无缝对接Proxy/Repeater/Target |
| 多线程采集 | 可配置线程数 | 提升大规模站点处理效率 |
| 智能URL拼接 | 基于Referer处理跨站JS | 解决CDN场景下的路径错误 |
| 响应码过滤 | 自定义状态码白名单 | 减少无效接口干扰 |
| 手动扫描模式 | 右键菜单触发单目标分析 | 精准分析特定请求 |

## 📖 使用指南

① **准备工作**（安装与配置）

下载 JAR 包从 Release 安装至 **Burp 2024.7+** 版本。进入 Settings 配置 Scope 范围（建议精确到目标域名避免扫到外站），根据需求开启 *无 Cookie 模式* 或调整线程数

② **核心操作**（启动采集）

确保浏览器流量经过 Burp，在目标网站进行 **正常功能点击**（无需刻意寻找 JS）。API剑自动在后台提取响应中的 API 与 JS，递归请求新发现的链接。通过 *主动请求速率* 参数控制请求间隔，避免触发风控

③ **结果查看**（分析与测试）

在 API剑的 Sitemap 面板查看采集结果，关注 **Method + Path + 来源JS** 三列信息。对感兴趣接口点击 *Send to Repeater*，或在 Target 模块查看自动添加的站点地图。使用 *过滤器* 快速定位特定路径或响应码的接口

## 📖 项目地址

```
https://github.com/Sugobet/API_Sword
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