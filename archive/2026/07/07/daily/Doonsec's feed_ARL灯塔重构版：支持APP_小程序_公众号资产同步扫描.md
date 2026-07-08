---
title: ARL灯塔重构版：支持APP/小程序/公众号资产同步扫描
url: https://mp.weixin.qq.com/s/czTYVst8KJlS-2_ZSRWodw
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:00:00.373985
---

# ARL灯塔重构版：支持APP/小程序/公众号资产同步扫描

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODydCOYyI2KtGHAib5ibdhiaAvMUVD6q54dzyGaFMuEwnfkCmsZX4GbXUXMhvy2uHoxtIwtHOskkfLEPPhJ0WR4vNFZkuK9z322nvY/0?wx_fmt=jpeg)

# ARL灯塔重构版：支持APP/小程序/公众号资产同步扫描

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# ARL灯塔重构版：支持APP/小程序/公众号资产同步扫描

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除，*****推荐的Skills/MCP/工具，建议大家先进行检测分析或者在沙箱/虚拟机等使用确保无误后，再进行日常工作或者本机使用，避免后门或者投毒受到影响。***

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  ARL-Next 是 ARL（资产侦察灯塔）的重构版本，提供 *极简*、**高效** 的自动化资产发现与漏洞监控方案。适用于安全运维人员、渗透测试团队和红队。

## 🚀 一句话优势

  Chromium动态爬虫+Nuclei引擎，打通 **边界→拓扑→指纹→漏洞** 资产闭环。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 资产发现 | 子域名爆破、端口扫描、指纹识别 |
| 漏洞扫描 | Nuclei引擎，POC按需自由组合 |
| 企业资产查询 | ICP备案+天眼查，一键同步多维度资产 |
| 告警通知 | 钉钉/飞书/企微/邮件/Webhook五大通道 |
| 任务管理 | 全生命周期追踪，支持多维资产拓扑过滤 |

## 📸 运行截图

| 界面 | 截图 |
| --- | --- |
| 全局仪表盘 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyjkES4LesNZU3NtoicFWgRrIcCoZRwFTybr6xdN1ELLB1EiahUQ9s3EJ9wlBo9jhpoPgVT1aboYXicqVdppzicib8dnjIObcJeyka8/640?wx_fmt=png&from=appmsg) |
| ICP备案查询 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODysGkGxk8BTZB8aRnEM0P1lcKzaWWItn1u5XwnVXKLC5pXnkeAWjX3d5hwdmJYuVhWXfmQv6BqdmFRx6NmuZAVdnF3DmqUXdeM/640?wx_fmt=png&from=appmsg) |
| 任务管理 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwLlnXibbYia3orcqGfqlgIEnbTibaysYicAFQxX6iblCXwYG0z6icZqRicYqY1VMdoQhhyzcMSrMHVMC1JJBCxbD2xriazXTcgTyeVTTU/640?wx_fmt=png&from=appmsg)  ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyCF70vPZIpw1F3S08D6xJXySuG18MotGzAHmbEI8swoBS1HW4tN3c82aN14lejkDKKejl1HkVicaFPgsAtibWyanculsdBejxcQ/640?wx_fmt=png&from=appmsg) |
| 系统设置 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyDY8JuzMsgQVZjOzT8ubONfM650F810xI02magN5hiaUtVrgLZq8WbaNtvRMAhLEY5GI9NkjACMtmcGcYbCM1MgNEwepj10LiaM/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 引擎代际更替：Chromium+Puppeteer取代PhantomJS

  ARL-Next淘汰了旧版 **PhantomJS**，平滑升级为 **Chromium + Puppeteer** 动态爬虫，页面渲染能力与兼容性显著提升。同时内置最新的 **Nuclei 3.3** 漏洞扫描引擎，支持 *POC插件按需自由组合*，确保漏洞检测模板与社区前沿保持同步。

### 2. 多维资产闭环：ICP备案+天眼查一键同步

  系统打通了 **边界→拓扑→指纹→漏洞** 全链路闭环，集成了 **ICP备案查询** 与 **天眼查** 企业信息检索。支持一键拉取企业旗下 *网站、小程序、APP、公众号及微博* 等多元资产，并直接下发扫描任务。*16985条指纹数据* 极大地丰富了资产指纹识别维度。

### 3. 五大告警通道实时通知

  系统设置中集成了 **钉钉、飞书、企业微信、邮件、Webhook** 五大告警通道，均支持一键测试连通性。当资产扫描或漏洞监控发现新结果时，自动推送告警至指定渠道，确保安全团队 *第一时间掌握资产变化*。同时支持 *字典云端热更新* 和扫描并发调度微调。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Vue 3.5 + Vite 5.4 | 前端现代化框架 | 极速热更新，开发体验高效 |
| Flask 2.0 | Python轻量级后端框架 | 快速处理API请求与业务逻辑 |
| RabbitMQ 3.x | 消息队列中间件 | 解耦API服务与异步扫描任务 |
| Celery 5.2 | 分布式任务队列 | 支撑高并发扫描任务执行 |
| MongoDB 4.0 | NoSQL数据库 | 承载千万级资产与漏洞数据 |
| Docker容器化 | 前后端微服务架构 | 部署简便，环境隔离安全 |

## 📖 使用指南

① **准备工作**：确保环境已安装 **Docker Desktop**、**Node.js** 及 **pnpm**（`npm install -g pnpm`）。克隆项目：`git clone https://github.com/owl234/ARL-Next && cd ARL-Next`。生产部署需准备SSL证书放入 `ssl-certs/` 目录。

② **核心操作**：开发环境运行 `bash start-dev.sh` 一键启动（后端容器自动拉起+前端依赖安装），访问 **http://localhost:5173** 登录（默认账号密码 **admin / arlpass**）。生产环境运行 `sudo bash start-prod.sh`，公网访问 **https://your-server-ip:5173**。登录后在 **系统设置** 中配置Fofa/天眼查API和告警通道，然后创建 **任务管理** 中的扫描任务，支持POC插件按需组合。

③ **结果查看**：扫描完成后，在 **全局仪表盘** 查看资产统计与漏洞分布。通过 **企业资产查询** 模块基于ICP备案或天眼查一键同步企业旗下资产。漏洞结果支持多维资产拓扑过滤，告警通过已配置的通道实时推送。如需直连数据库，MongoDB连接信息为 *mongodb://admin:admin@127.0.0.1:27018/arl?authSource=admin*。

## 📖 项目地址

```
https://github.com/owl234/ARL-Next
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| 网络安全全栈知识库 | 钉钉漏洞威胁情报群 |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzDcbialtDJB2iauRibULjWbzQk2oeHEyuNcGjibhWw6SpJia0RYGY3D7UhMASYr1QPAicb1LaSL1XlDrVowaibjeB41IKYSBHE8z9sN8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwMu4dL9ZhibwZKibzwdD01Btq6ia2183uH0ibzaGibkr1aribDe1jicrtW0px8pd6Rz1kT7QpTtzfdmicibiaFZHSqI40srWZhLQ9HpR1JY/640?wx_fmt=png&from=appmsg) |

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