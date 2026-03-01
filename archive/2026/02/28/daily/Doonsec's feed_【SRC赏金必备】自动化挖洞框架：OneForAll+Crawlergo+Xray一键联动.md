---
title: 【SRC赏金必备】自动化挖洞框架：OneForAll+Crawlergo+Xray一键联动
url: https://mp.weixin.qq.com/s/_O4kvSBUc_iLK65p3NDvSg
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:26:53.292397
---

# 【SRC赏金必备】自动化挖洞框架：OneForAll+Crawlergo+Xray一键联动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODy0xWy9VPyaY5rAOAAqrmzRj2CH6J5sYj49VibQyYiba69BibaY6dt0blL4qqp5iaHIo0Es4ybSdMKvsa3LwwIHGah2Dm3I26N6lB4/0?wx_fmt=jpeg)

# 【SRC赏金必备】自动化挖洞框架：OneForAll+Crawlergo+Xray一键联动

原创

0xSecDebug
0xSecDebug

0x八月

![]()

在小说阅读器中沉浸阅读

# 【SRC赏金必备】自动化挖洞框架：OneForAll+Crawlergo+Xray一键联动

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

    AUTO-EARN是基于Python的自动化漏洞扫描框架，*集成子域收集、端口探测与被动扫描*，适合SRC挖掘与授权测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyica9ibI60BoKMqMWSeyn3AHgo32BdaxJEtsbFW62LRIelSpLt6DBffIEqTCVPofHEg7bNp432Zt2xjXYibmfkGmNPcP8gXnSldM/640?wx_fmt=png&from=appmsg)

## 🚀 一句话优势

    模块化集成OneForAll与Xray，实现子域收集到漏洞推送的全流程自动化。

## 📋 核心能力速览

| 功能名称 | 一句话说明 |
| --- | --- |
| 子域收集监控 | 基于OneForAll自动收集并监控完成状态 |
| 端口服务探测 | 结合CDN检测与Shodan API识别开放端口 |
| WAF指纹识别 | 自动识别目标防护策略辅助决策 |
| 被动漏洞扫描 | 联动Crawlergo与Xray进行无主动攻击检测 |
| 实时消息推送 | 通过Server酱将漏洞信息推送至微信 |

## 📸 运行截图

| 功能模块 | 截图位置 |
| --- | --- |
| OneForAll子域收集日志 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxr4Rr3GuuAdjOlrHq1FQKvf4lALibyTib5qwl3uPXsiauTxHE68ia7JNoibcYwlsBaNZZ4TY3Blj34R1xWvQfZibVA5d6HqiaaYOibGHc/640?wx_fmt=png&from=appmsg) |
| 端口探测与WAF检测结果 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyMtTNrWZAKrCmQibgLibkpcwURXvmTjDC1tQhTOqWrekUSZLKg4HEKBhNVFuKZS4lx1hkktZubtRs4BA6Qugzw6OvictdYgic5viaE/640?wx_fmt=png&from=appmsg) |
| Xray被动扫描与漏洞推送 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzVzh872dQKoVShJZpUka62Ys6a1OIkeduCKfn58ETWniaNeFicFpkiaxF6ng9tcEmZyK8DRd4tzPsdPeeTZTzQQwTVYIghyRkqjo/640?wx_fmt=png&from=appmsg) |
| Flask可视化数据展示界面 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODw0rVictW3TGsgJWa7FczgLf4JBjuNvPlUpqZJYdcMkcMerWR1CJEBVgHYJlicUovSjbGPd84MctMuQVOIQExXuoxbl4KHA7ra5g/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

1. 1工具链模块化编排：

   不是单一工具，而是提供OneForAll+Crawlergo+Xray的标准化接口与流程。各组件可依据个人习惯替换，比如将Xray换成W13scan，或更换子域收集工具，只需调整配置文件无需改动核心代码，适应不同师傅的信息收集偏好。
2. 2可视化数据管理：

   通过Flask构建Web界面，利用Echarts实现扫描结果可视化。数据库自动存储子域、任务、漏洞三类数据，支持按项目维度管理，每次运行自动按时间戳备份，**避免多次扫描数据混淆，方便历史漏洞追踪。**
3. 3被动扫描低感知设计：

   采用Crawlergo动态爬虫+Xray被动代理模式，不发送主动Payload，依靠流量分析发现漏洞。*配合CDN检测与WAF识别*，自动调整扫描策略，降低被封禁风险，适合对稳定性要求较高的测试环境。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Python 3.8+ | 主流脚本语言 | 兼容OneForAll等现代安全工具生态 |
| Flask Web框架 | 轻量级Web服务 | 快速构建可视化界面，资源占用低 |
| 被动扫描架构 | Xray Webhook集成 | 低感知检测，适合生产环境谨慎测试 |
| SQLite存储 | 文件型数据库 | 零配置部署，自动备份机制防数据丢失 |
| Docker支持 | 容器化部署 | 环境隔离，Chrome与Xray证书预装 |

## 📖 使用指南

① **准备工作**：

    克隆仓库后安装Python 3.8+依赖，在`config.py`中配置Shodan API与Server酱Key，将Chrome与Crawlergo放置到tools目录并赋予执行权限。

② **核心操作**：

    执行`start.sh`启动子域收集监控，待微信通知完成后运行`python3 autoearn.py`进入端口探测与WAF检测阶段，最后启动`server.py`与Xray监听进入被动扫描。

③ **结果查看**：

    访问本地5000端口查看Flask可视化界面，或使用tail命令查看logs目录下各组件实时日志，发现的漏洞会即时推送至微信，数据自动存入SQLite供后续分析。

## 📖 项目地址

```
https://github.com/Echocipher/AUTO-EARN?tab=readme-ov-file
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

| ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyBdiau5GC7dWricMbXhF76xhhbcjia7Uj6987eBmBe6ov5ibhib2lJP6qmicTbz2zK2ObzgicE7kqY83MVGqJwTgJnIEbfXAkgGykAl8/640?wx_fmt=png&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) | ![img](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg) |
| --- | --- | --- |

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