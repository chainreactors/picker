---
title: 渗透测试：多功能网络信息扫描工具
url: https://mp.weixin.qq.com/s/PSgRlL-Lo87Cqqp7rMlg-g
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:25:39.703733
---

# 渗透测试：多功能网络信息扫描工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODymG7FGMFOa8WqM2icWeno4Z0TTuuNguibEBryN6iac4csI1OsgOWflqpbHaia6UxdIpNs9xiaiba7xeypH5xwIRRCJgUXcjVtRLcf6A/0?wx_fmt=jpeg)

# 渗透测试：多功能网络信息扫描工具

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# 渗透测试：多功能网络信息扫描工具

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  xkInfoScan 是一款基于 **Python 3.12** 开发的集成化网络信息收集工具，支持 *IP/域名/URL/信息追踪* 多维度目标探测，涵盖 **目录扫描、CMS 识别、漏洞检测、信息泄露挖掘、CDN 检测**等 8 大核心模块，适用于**渗透测试前期信息收集**与**网络资产测绘**场景。

## 🚀 一句话优势

**单工具覆盖信息收集全流程**，支持 **8 大扫描模块**与*多维度目标探测*，GPLv3 开源可二次开发。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 信息追踪 | IP/手机号/用户名关联信息查询 |
| IP 扫描 | 基础探测、RDAP、地理定位、CDN 检测 |
| 域名扫描 | WHOIS、DNS 解析、子域名爆破 |
| 目录扫描 | HEAD/GET/POST 多方法探测 |
| CMS 识别 | 4 种模式（详细/快速/深度/极速） |
| 漏洞检测 | Web/框架/中间件/端口漏洞 |
| 信息泄露 | SVN/Git/.DS\_Store 等敏感文件 |
| Web 专项 | JSFinder、APIFinder、403 绕过 |

## 📸 运行截图

| 功能模块 |  |
| --- | --- |
| IP 信息探测结果 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzAljarhDfkO930McqstpYicbjjUXeOiaXnGyE4uPCNiby1X23RDrKC3B3MVicvicfgpFNCzr5FocLxRNYIPIBAibMEUVkOJSyQ5axXY/640?wx_fmt=png&from=appmsg)  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyjtr5FG3nk2K6Iia8dk5icLj41hGJgUhutDHFmuBW5bviapQyCZ7OicibP9QWgbWhtWxZ4icwnND2BYuJoT9w1GSToVW6JBSg1NHOKU/640?wx_fmt=png&from=appmsg) |
| 信息追踪 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODz0gicanEkrOZ4FAI93rIMfYYfcCDybZFuibzfT2fcnMxibLDFXnnrNZZqKdBx9mOcP6ycagzz4LFN7XCVLF2BLbq8MrMibbr13KQE/640?wx_fmt=png&from=appmsg) |
| 域名扫描详情 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwN4YSFZ6HdHNNBltHQ2EWk5bRVhcNK4NJ4IRw4BGcnjXSyNxCshqbrCyicUMyCp7PZXn5Hp4bqyWa323AMhkdhm2hKfykqgTEY/640?wx_fmt=png&from=appmsg) |
| url信息扫描 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxKyEpnPiasAIv9lIBriaIicHSbia66jVMDyfxYXFzLlnuxXFLz3gZ6o42IYYF2XHzAS6Zw3h7MqDcicKZEmf58y7ZM6VicNclte9TFY/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 多维度目标探测体系

  支持 **IP 地址**（单 IP/CIDR 网段）、*域名*、完整 URL 三种目标输入格式，覆盖网络资产测绘的**全场景入口**。IP 扫描模块集成 *RDAP 注册信息查询*、地理定位、**CDN 检测**与端口扫描；域名模块支持 **WHOIS 查询**、*DNS 解析*、子域名爆破；信息追踪模块可通过 **IP/手机号/用户名**反查关联信息，实现从**单点目标**到*资产图谱*的扩展。

### 2. 四级 CMS 识别模式

  针对 Web 资产识别需求，提供 **json（详细）**、*rapid（快速）*、holdsword（深度）、**fast（极速）**四种探测模式。详细模式输出完整的 **CMS 类型、版本号、组件信息**；极速模式通过 *特征码匹配*快速筛选目标；深度模式进行多位置指纹验证降低误报。用户可根据**资产规模**与*时间成本*灵活选择策略，万级 URL 场景下推荐使用 *fast* 模式优先发现高危资产。

### 3. Web 专项深度检测

  Web 专项模块集成 **JSFinder**（JavaScript 文件信息提取）、*APIFinder*（接口端点探测）、403Bypass（禁止访问绕过）三项能力。JSFinder 自动解析页面引入的 **.js 文件**，提取 *API 端点*、敏感密钥、**域名信息**；403Bypass 通过**路径穿越**、*HTTP 方法切换*、Header 伪造等 8 种技术尝试绕过访问控制，发现隐藏的**管理后台**与*敏感接口*。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Python 3.12 | 最新稳定版 | 性能优化，语法特性先进 |
| 模块化架构 | 8 大功能模块独立 | 按需调用，易于维护扩展 |
| 彩色 CLI 输出 | Rich/Colorama 终端渲染 | 结果可读性强，降低使用门槛 |
| 多格式导出 | CSV/JSON 支持 | 便于与其他工具联动分析 |
| 线程池控制 | -t 参数 1-100 线程 | 平衡扫描速度与目标负载 |
| 调试模式 | --debug 显示请求详情 | 排查问题与规则调优 |
| GeoLiteCity | MaxMind 地理定位库 | IP 物理位置精准定位 |

## 📖 使用指南

① **准备工作**：克隆仓库后执行 pip install -r requirements.txt 安装依赖。下载 **GeoLiteCity.dat** 文件（网盘提取码：gffx）放置于 *data/* 目录，确保 **IP 地理信息模块**可用。

② **核心操作**：执行 python xkinfoscan.py -i 1.1.1.1 进行 IP 信息探测，使用 *-d example.com* 扫描域名资产，-u https://example.com -s dir 启动目录扫描。通过 **-s cms --cms-mode fast** 快速识别 Web 组件，*-s poc --poc-mode web* 检测常见漏洞。

③ **结果查看**：扫描结果默认输出至 *output/* 目录，使用 **-o result.csv** 或 *-o result.json* 指定导出格式。开启 --debug 模式查看详细请求/响应，便于**验证误报**与*规则优化*。

## 📖 项目地址

```
https://github.com/xk11z/xkinfoscan
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| ![img](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODwHdUbwzDLq3nh7hplKZNDBERhMYooic5cPGwPHEJRonMYCoupeaa6fPuwOKehMek9HTEvnLaG0uuiaScGxWWmibtK9XNFHF4PJD0/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
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