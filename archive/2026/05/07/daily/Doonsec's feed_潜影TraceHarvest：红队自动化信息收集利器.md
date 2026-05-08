---
title: 潜影TraceHarvest：红队自动化信息收集利器
url: https://mp.weixin.qq.com/s/OQRpKIvOtKKT1ucxbvjhMQ
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:49:39.983811
---

# 潜影TraceHarvest：红队自动化信息收集利器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODxbEVWdn14mUICH92BLEZ6lkcxEntrRrcIibNQBYob8EEprQea47l02zvaPqG0TGGjCmfCnwHC7p1icYXRJWSZycGiaFZBCkzJa9o/0?wx_fmt=jpeg)

# 潜影TraceHarvest：红队自动化信息收集利器

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 潜影TraceHarvest：红队自动化信息收集利器

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

**潜影【TraceHarvest】** 是一款 **Windows 端自动化信息收集工具**，通过笛卡尔积查询与多引擎采集实现 *规模化目标侦察*，适用于红队演练与资产测绘场景。

## 🚀 一句话优势

  通过 **笛卡尔积查询+多引擎协同**，将人工搜索耗时从数小时压缩至分钟级。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 笛卡尔积查询 | 主词×副词自动生成搜索组合 |
| 多引擎采集 | 并行调度百度、Bing、搜狗等 |
| 敏感信息提取 | 自动识别手机号与邮箱地址 |
| 反爬策略 | 智能交错调度与动态延迟 |
| 结果管理 | 实时表格展示与CSV导出 |

## 📸 运行截图

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzdUIjZ1tfUdPL1SbvgfgBEnCl2DJJtrq9NGrowEyyrDhoXmhrIkYHPtiaDC8s3NM3FqpGEFeJ3C4jYfiaWPwpIUU5kSvXolcwJo/640?wx_fmt=png&from=appmsg)

## ✨ 核心亮点

### 1. 笛卡尔积查询引擎

  潜影内置 **笛卡尔积搜索生成** 能力，将主查询词与副查询词自动组合，一次性生成所有可能的搜索对。对于需要同时侦察多个目标的攻防演练场景，此功能可将 *前期信息收集时间* 从数小时压缩到分钟级。

### 2. 多引擎协同与反爬策略

  工具并行调度 **百度、Bing、微信/搜狗** 等多个搜索引擎，在遵守反爬规则的前提下最大化采集速度。针对百度严格的频率限制，采用 *智能交错调度算法*：首条查询立即执行，后续按设定间隔逐个进行，其他引擎查询在等待期间穿插完成。遇到验证码时自动暂停相关引擎，避免账户风险。

### 3. 敏感信息精准提取

  内置高精度正则引擎自动从搜索结果中提取 *11位手机号* 与标准邮箱地址，准确率达99%以上。不仅采集标题摘要，还提取页面正文提高发现率。结果以结构化表格实时展示，支持一键导出为 **UTF-8 with BOM 格式 CSV**，兼容 Excel 中文显示。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| 笛卡尔积算法 | 主副词组合生成 | 覆盖完整搜索维度 |
| 多引擎调度 | 并行-串行混合采集 | 平衡速度与稳定性 |
| 正则提取引擎 | 手机号与邮箱识别 | 准确率99%以上 |
| 反爬策略 | 动态间隔与请求头随机化 | 降低封禁风险 |
| 零依赖运行 | Windows可执行文件 | 双击即用无需环境 |

## 📖 使用指南

① **准备工作**（安装启动）从 GitHub Release 下载解压，双击可执行文件启动。无需安装 Python、Node.js、Java 等任何依赖环境。

② **核心操作**（配置采集）在查询配置页输入 *主查询词*（如目标企业名）与副查询词（如招聘、招标），设置采集深度与请求间隔。点击开始，工具自动完成 **多引擎并行采集** 与敏感信息提取。

③ **结果查看**（导出分析）在结果面板查看实时更新的采集数据，使用筛选与排序功能定位关键信息。点击 **导出CSV** 生成标准化报告，包含关键词、来源、URL、手机号、邮箱等完整字段。

## 📖 项目地址

```
https://github.com/i-am-xjizhi/TraceHarvest
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