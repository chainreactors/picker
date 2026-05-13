---
title: 一款功能强大的Web 漏洞扫描器(11种检测模块)
url: https://mp.weixin.qq.com/s/MOnAGljdhFGkh7eGBK-Auw
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:44:43.996569
---

# 一款功能强大的Web 漏洞扫描器(11种检测模块)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODw2lm2b6vaTej8tM48bhF6N6uklzHCg62iah13l6xRsgOykBLOoFEgFfyLicR9WLhBLDGdQoia8eSNxQauGFC1VdL0xxjSS32cRiag/0?wx_fmt=jpeg)

# 一款功能强大的Web 漏洞扫描器(11种检测模块)

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一款功能强大的Web 漏洞扫描器(11种检测模块)

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

**RayScan 1.0** 是一款 **Python 开源 Web 漏洞扫描器**，集成 *11 个检测模块* 与 Nuclei、sqlmap 等第三方工具，支持 GUI 与命令行双模式，适用于快速安全评估与深度审计场景。

## 🚀 一句话优势

  通过 **快速/全量/GUI 三模式** 与 *11 类漏洞* 原生检测，将 Web 安全评估门槛降至单条命令。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| SQL注入检测 | 覆盖error-based、union、boolean-blind、time-based、stacked五类 |
| XSS检测 | 支持反射型、存储型、DOM型 |
| 命令注入检测 | 高精度CMDi识别 |
| 敏感信息泄露 | 高覆盖度信息暴露检测 |
| JS端点发现 | 自动提取JavaScript中的API路径 |

## 📸 运行截图

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODznngLnDRIcdUSicvAtiaYe6OAFibrxN7cs33jgEliaicH6A5NT1dDZU9OvQzbWGibGRdYFFPR90f56M9VM9gzjJpHsCJzDYTicdOlkew/640?wx_fmt=png&from=appmsg)

## ✨ 核心亮点

### 1. 五类SQLi原生检测

  RayScan 不依赖外部工具即可完成 **error-based、union、boolean-blind、time-based、stacked** 五种 SQL 注入检测。相比仅支持报错型检测的扫描器，这种设计覆盖了 *盲注与堆叠查询* 场景，在目标无回显或 WAF 过滤错误信息时仍能有效识别注入点。

### 2. 第三方工具无缝集成

  内置 **Nuclei 模板扫描、sqlmap 深度利用、ffuf 模糊测试、Wappalyzer 技术栈识别** 四大外部工具接口。你无需在多个终端间切换，单条命令即可触发 *漏洞模板匹配+手工利用+技术指纹* 的完整链路，结果统一输出为 JSON/HTML/CSV/Markdown 格式。

### 3. 三模式适配不同场景

  提供 **quick\_scan 快速摸底、full\_scan 深度审计、wvs\_gui 图形交互** 三种入口。快速模式默认爬取 *2层深度/25个URL*，适合应急排查；全量模式扩展至 *3层/500个URL/12并发端点*，满足企业级审计需求；GUI 模式则让非命令行用户也能完成配置与扫描。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Python原生 | 基于Python 3.8+实现 | 跨平台运行，源码可审计 |
| 模块化架构 | 11个检测模块独立加载 | 按需启用，减少无效请求 |
| 异步HTTP池 | 基于asyncio的并发请求 | 提升大规模扫描效率 |
| 多格式报告 | 支持JSON/HTML/CSV/Markdown/Console | 适配不同汇报场景 |
| 19版本迭代 | 基于WVS v19.2重构开源 | 功能经过长期实战验证 |

## 📖 使用指南

① **准备工作**（安装与配置）执行 pip install -r requirements-dev.txt 安装依赖。如需第三方工具集成，单独安装 *sqlmap* 与 *ffuf*，Python 依赖通过 `pip install nuclei-python python-Wappalyzer` 完成

② **核心操作**（启动扫描）快速评估执行 `python quick_scan.py -u http://example.com`，深度审计使用 `python full_scan.py -u http://example.com --profile full`。调整 *crawl\_depth*、*concurrent\_endpoints* 等参数控制扫描粒度，GUI 模式运行 `python wvs_gui.py`

③ **结果查看**（分析与导出）扫描结果自动保存至 **scan\_reports/** 目录。JSON 格式包含漏洞类型、严重等级、URL、置信度等字段，可直接导入漏洞管理平台。使用 `ls scan_reports/` 查看历史扫描记录，Markdown 格式便于直接粘贴至报告文档

## 📖 项目地址

```
https://github.com/xiabai2004/RayScan
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzDcbialtDJB2iauRibULjWbzQk2oeHEyuNcGjibhWw6SpJia0RYGY3D7UhMASYr1QPAicb1LaSL1XlDrVowaibjeB41IKYSBHE8z9sN8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwMu4dL9ZhibwZKibzwdD01Btq6ia2183uH0ibzaGibkr1aribDe1jicrtW0px8pd6Rz1kT7QpTtzfdmicibiaFZHSqI40srWZhLQ9HpR1JY/640?wx_fmt=png&from=appmsg) |
| --- | --- |

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