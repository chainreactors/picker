---
title: Burp 插件：SRC 白帽子资产梳理利器
url: https://mp.weixin.qq.com/s/4W2d3bFK-NxKgtv4Soe2tg
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:04:38.905357
---

# Burp 插件：SRC 白帽子资产梳理利器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODyozoSWxX77QKNgkzecjFy2Gye6HGuMsiaXSqX692ibtWsLn50jRmJTdibIhxVchZwWGBnmPlw3hJemfpEUyrNofa44pgHh1MDwxw/0?wx_fmt=jpeg)

# Burp 插件：SRC 白帽子资产梳理利器

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# Burp 插件：SRC 白帽子资产梳理利器

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

**Domain Hunter Pro** 是一款基于 *Burp Suite* 的插件化目标管理工具，通过**流量驱动**的自动化信息收集，帮助 SRC 白帽子 替代 Excel 进行资产梳理。

## 🚀 一句话优势

将 Burp 流量自动转化为**结构化资产库**，彻底解决手工复制粘贴的重复劳动。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 被动信息收集 | 从流量提取子域名、邮箱、包名 |
| 资产汇算 | 智能计算最小网段，排除CDN干扰 |
| 进度管理 | 标记检测状态、重要程度、备注 |
| 深度联动 | 与Burp右键菜单、外部浏览器无缝衔接 |
| 多维度搜索 | 支持文本、dork语法、字段过滤 |

## 📸 运行截图

| 说明 | 截图 |
| --- | --- |
| Domains Tab 主界面 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODx2hN9Ko0WIUuUqovmib3ibHA7AtACosPiaOicXVia3aMUW2MInc28ahoRFibeMLhIoyxG6JveZU2rv6xWA6z8micHoFQqA1V2iaXicvVBQ/640?wx_fmt=png&from=appmsg) |
| Titles Tab 资产列表 | ![image-20201217111543496](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyYPyicyuJLRhkHjWRgFth5OS8YGksmBILRK8YFB3qLYMQ2Nj325Phibmujkp9wMW42QTB4y5jBIB1Ao7O7JGqsBAQMbia8aHYjKg/640?wx_fmt=png&from=appmsg)  ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxYk42BFKkUkEsujVJngWBhibTQJm5O8sW8JYZ43I3FbPygarQvgwqQ5u4bUc4yONicjdeQIWM1nqzD5xtVsaHoWPV4nHUz8LwQY/640?wx_fmt=png&from=appmsg) |
| 访问web获取title | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwHgHUiaUd8H0qI0sgbX829aKvykN1zlRgY1KYkwlslicVGWWQZPJEI1JCex2NQR9PreSOsr7u1qYdkQ1sEVqDW6oAdJQQH4KyicY/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 流量驱动的被动信息收集

  该工具通过监听 Burp 代理流量，自动提取**子域名、相关域名、相似域名、邮箱地址、Java 包名**等关键资产信息。你无需主动发送探测请求，仅需正常浏览目标站点，资产数据便会**实时入库**，大幅降低被风控拦截的风险。实测表明，一次完整的业务线梳理可节省 *70% 以上* 的手工收集时间。

### 2. 智能 IP 汇算与 CDN 排除

  针对收集到的子域名，工具会多线程请求 *80/443* 端口获取 Title 和 IP，并基于 ASN 归属 智能判断是否为 CDN 节点。**非目标资产的 IP 会被自动剔除**，剩余 IP 自动汇算为最小网段（如将 8.8.8.8 与 8.8.8.10 合并为 8.8.8.8/30）。这一机制确保了网络资产梳理的**精准性**，避免了传统 C 段扫描的盲目性。

### 3. 与 Burp 生态的深度集成

  工具不仅是独立的数据库，更是 Burp 工作流 的延伸。在任意请求处右键，可快速将 URL **添加至目标管理**、设置检测状态或发送给 Scanner。Title Tab 支持双击直接调用浏览器访问，或联动 Google 搜索特定 Host，实现"发现-验证-测试"的闭环操作。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| SQLite 存储 | 轻量级本地数据库 | 项目文件可迁移，无需配置数据库服务 |
| Java 开发 | 标准 Burp 插件架构 | 跨平台兼容，与 Burp 版本同步更新 |
| 多线程 Title 获取 | 并发请求子域名 | 提升资产探测效率，支持超时控制 |
| 域传送检测 | 针对 NS 服务器的 AXFR 请求 | 发现传统子域名爆破遗漏的边缘资产 |
| ASN 识别 | 基于 IP 的自治系统号判断 | 精准区分目标资产与 CDN/云服务 |

## 📖 使用指南

① **准备工作**：从 GitHub Releases 下载 JAR 包，在 Burp 的 **Extensions** 模块导入。首次使用需**创建项目文件**（.db 格式）以初始化 SQLite 数据库。

② **核心操作**：配置浏览器代理至 Burp，正常访问目标站点。在 **Domains Tab** 设置主域名（如 baidu.com），点击 *Search* 从流量中提取关联资产。切换至 **Titles Tab**，点击 **Get Title** 启动多线程探测，获取 *Web Title、IP、CDN 状态*。

③ **结果查看**：在 Titles 列表中使用 **搜索框** 进行文本或 dork 语法过滤（如 `host:admin`），右键标记 重要程度 和 **检测状态**。通过 **Tools Tab** 可将目标 URL 批量导出为 List 格式，或调用外部浏览器循环打开。

## 📖 项目地址

```
https://github.com/bit4woo/domain_hunter_pro
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

| ![img](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODxCPibZHwI0h87VgQCoac1RPa8LkqPfe94EibRdkObaIdFOLU6LE4dVo1h5ia9brohDj2hw7ia0TaPHZ2JGh07lw4ciaZgmIg2gMt8Q/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
| --- | --- |
| ![img](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODw9FiaDxkbDmibgOqmB8jafl5EsFpuMMngJvqHEI0tBTUol1fiaHV2Yc0PCvqYvPe15C7ibgSImsMFyc9Sk9fZl1Jabibrq1Zlq8JMA/640?wx_fmt=jpeg&from=appmsg) |

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