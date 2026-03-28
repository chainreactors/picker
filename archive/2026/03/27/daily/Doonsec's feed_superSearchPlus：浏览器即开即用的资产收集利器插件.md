---
title: superSearchPlus：浏览器即开即用的资产收集利器插件
url: https://mp.weixin.qq.com/s/6qTSF6hoPslupsBL1icbXQ
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:12:50.148879
---

# superSearchPlus：浏览器即开即用的资产收集利器插件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODwMlODCIGHfZEcNAuKp2mkgkfrPP0A8Xf336ib0yOia4un70ll2pvlraka7j1eufWXPkhSc4TCA4En50V0ibuQMwJvj8Xbr42tK5A/0?wx_fmt=jpeg)

# superSearchPlus：浏览器即开即用的资产收集利器插件

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# superSearchPlus：浏览器即开即用的资产收集利器插件

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

**superSearchPlus** 是一款 **Chrome 浏览器聚合型信息收集插件**，集成 FOFA、鹰图、Quake 等 *6+ 资产测绘平台*，提供 IP 反查、JS 提取、目录扫描、Vue 路由探测等功能，适用于红队资产梳理与渗透测试前期侦察场景。

## 🚀 一句话优势

通过 **浏览器插件形态** 实现"即开即用"的信息收集，无需切换多平台即可获取企业资产全貌，解决工具碎片化与 API 配置繁琐痛点。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 综合查询 | IP反查域名、公司信息、备案网站 |
| 资产测绘 | 联动FOFA/鹰图/Shodan/Quake等 |
| JS提取 | 自动提取JS中的路径/域名/手机号 |
| 目录扫描 | 联动JS结果进行敏感路径探测 |
| 注释扫描 | 检测HTML/JS中的敏感注释信息 |

## 📸 运行截图

| 功能 | 说明 |
| --- | --- |
| ip反查域名功能 | IP反查域名、公司信息、备案网站![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxdfapZg4rCgBooNNEhPdtCehuJoLMeQibeiaXP4CSS7TG1GtH2NQea2pTOpnCf1TsQ8GUoGgPMqxsExyvkX8OcxKdT7mkJWNO34/640?wx_fmt=png&from=appmsg) |
| 资产测绘 | 联动FOFA/鹰图/Shodan/Quake等![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODziaW1ZqI9LhR4d9QUOYSah4vx24ADsibibgcb6jr00N65MxSV8taKoDTx1PrACpR8DMk9r6jZO8pUb1An0C5gslibxRI8cibtMbVdw/640?wx_fmt=png&from=appmsg) |
| JS提取 | 自动提取JS中的路径/域名/手机号![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODx8qVViaOWHmr78OoOwdkicqcoSZROYybTI7NhicibTJhHqQjpQPUAKAMf8vygpukHibvpic3xlWX353lFsmTGafmL0uicBnVibIfgMolY/640?wx_fmt=png&from=appmsg) |
| 目录扫描 | 联动JS结果进行敏感路径探测 |
| 注释扫描 | 检测HTML/JS中的敏感注释信息 |

## ✨ 核心亮点

### 1. 多平台资产测绘聚合

插件内置 **FOFA、鹰图、Shodan、Quake、ZoomEye、零零信安** 六大平台接口，自动以当前标签页 IP 为查询条件发起并行检索。支持 *时间范围筛选*（鹰图默认近一年）与 *响应体预览*，无需在各平台网页间反复切换，数据支持 CSV 导出用于后续分析。

### 2. JS深度提取与联动扫描

**jsFindPlus 模块** 从页面脚本中自动提取 *手机号、IP、端口、路径、域名、邮箱* 等 6 类敏感信息。提取的路径可直接联动 **目录扫描** 功能，基于自定义字典进行敏感文件探测，并支持 *响应大小筛选* 快速定位有效接口。

### 3. Vue 与现代化前端识别

针对 **Vue 单页应用** 提供专项扫描能力，自动提取 Vue Router 配置中的路由信息。同时支持 *自定义正则* 扫描当前页面 DOM 内容，满足非标准框架的信息收集需求。扫描规则支持导入导出，便于团队共享配置。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Manifest V3 | 适配Chrome最新扩展标准 | 兼容性与性能优化 |
| FOFA-Map | 免API Key的Host查询 | 降低使用门槛 |
| 子域聚合 | 多来源子域名去重合并 | 减少重复资产 |
| superBar | 内置HackBar式重发功能 | 快速验证请求 |
| 配置持久化 | JSON导入导出 | 便于团队协作 |

## 📖 使用指南

① **准备工作**（安装与配置）

从 GitHub Release 下载插件，拖入 Chrome 扩展程序页完成安装。点击配置页 导出配置模板，填入各资产测绘平台的 API Key 后导入，或手动逐项添加凭证

② **核心操作**（信息收集）

访问目标网站后点击插件图标，自动提取当前 Tab 的 **IP 与域名**。选择"综合查询"查看 IP 归属地与公司信息，或进入"资产测绘"选择 *FOFA/鹰图* 等平台并行检索。对于 Vue 站点，使用 *Vue组件扫描* 提取前端路由

③ **结果查看**（分析与导出）

在"信息收集"面板查看 **jsFindPlus 提取结果**，点击"联动扫描"对发现的路径进行目录爆破。使用 *注释扫描* 检测页面源码中的敏感信息，最终结果支持 CSV 格式导出

## 📖 项目地址

```
https://github.com/dark-kingA/superSearchPlus
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