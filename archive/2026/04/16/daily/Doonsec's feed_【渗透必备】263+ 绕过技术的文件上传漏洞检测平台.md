---
title: 【渗透必备】263+ 绕过技术的文件上传漏洞检测平台
url: https://mp.weixin.qq.com/s/SOBB01I5NplDSpIbDM5gEA
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:43:25.349771
---

# 【渗透必备】263+ 绕过技术的文件上传漏洞检测平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODzY0R6CVcE136tsEiaANHnaZSHibj74ld7ovZIp8zJoDlRW9YxKTAAs7ShfOhFlAic3KqH9piaw06R0oIO3ylVaysQKMcFm746uW20/0?wx_fmt=jpeg)

# 【渗透必备】263+ 绕过技术的文件上传漏洞检测平台

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 【渗透必备】263+ 绕过技术的文件上传漏洞检测平台

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

**个人感觉是把burp功能向**文件上传漏洞方向进行了**专项开发**

## 📖 项目/工具简介

  UploadRanger 是一款基于 **PySide6** 开发的**文件上传漏洞检测工具**，集成 *智能扫描*、代理抓包、**Repeater 重放**、*Intruder 爆破*四大模块，内置 **263+ 绕过技术**与14 类 Payload，支持**安全测试**与*渗透测试*双模式，面向**Web 安全研究员**与**渗透测试工程师**。

## 🚀 一句话优势

**263+ 绕过技术**智能排序，**双模式扫描**（无害验证/WebShell 渗透），集成 *Burp 式代理抓包*与四模式爆破。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 智能扫描 | 自动检测上传点，三级响应分析 |
| 代理抓包 | HTTP/HTTPS 拦截、修改、重放 |
| Repeater | 手动请求重放与调试 |
| Intruder | 四模式自动化爆破 |
| Payload 生成 | WebShell、Polyglot 多载荷 |
| 环境指纹 | 自动识别 Web 服务器与 WAF |

## 📸 运行截图

| 功能模块 | 截图 |
| --- | --- |
| 智能扫描界面 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzaxoMWoRtjmjGYSGkoVrL7fice8PFapKWib2AdIOwA8aCn95mIlicVVicdcxricKNsRrhrHAKsZdSdTvbjbn60gdYt3ibv6UfHiafG0o/640?wx_fmt=png&from=appmsg) |
| 代理抓包界面 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwNnmq09XMNSEof9MU34L7zojFpMC17KicQsgO4wBS6wxknf22rBZBlwR6lHvQe6yVCOYRs9ODCQYnLsIibpJOkqLYlyTO61z4W4/640?wx_fmt=png&from=appmsg) |
| Repeater | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODz9gxegnJQWAmcgHD6fCJtU8FxyBicomZgtTIp1UARdGMyw2KtENhFPQIZTsVLQulf3p51T2mmRHxSWwIAU7wSoViaEWyP7uPIcw/640?wx_fmt=png&from=appmsg) |
| Intruder | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyaLv5PEvKerZ4AbBdTFzAHTCzjlJDQVRat7sRhRuvly65f6Vz63NfhHXiceDUiagWiaBNl6NG6CZic0WMagtA6xpLAGRhibhsM0DNA/640?wx_fmt=png&from=appmsg) |
| 263+ 绕过技术 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyibEBW7gt3BJbWiawVnYUxp9bbiaicdF7nXMHptkHxHrjWf7E3j8BljX8FGnORtMz1wuIICQ9XVwhhobNUicJKguFVZPibTnWrgZS1k/640?wx_fmt=png&from=appmsg) |
| Payload生成器 | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODx2DuicH78gAkPCsmICsmEsJPt6Aw5OWuLWvERaa32x8nzGQ5jbmDGUvUyf7sWicZia2tppnXLwtFkrny4Dmu48buPYh3iaicE67I6k/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 双模式扫描策略

  提供 **安全测试模式**与 *渗透测试模式* 两种扫描策略。安全测试模式上传**无害 HTML/文本内容**，仅验证上传接口是否存在漏洞，适合**授权合规检测**；渗透测试模式支持上传真实 **WebShell**（基础 eval、Base64 免杀、冰蝎/蚁剑兼容），可自定义密码与*Shell 类型*，适合**红队评估**。上传 EXE/脚本等可执行文件前会**二次确认**，防止误操作。

### 2. 263+ 绕过技术智能排序

  Payload 注册中心维护 **14 类 263+ 种绕过技术**，涵盖**文件扩展名绕过**（如 *shell.php%00.jpg*）、Content-Type 伪造、**WAF 绕过**、*文件名编码*（Unicode、URL 编码）、multipart boundary 混淆等。系统通过 **EnvironmentFingerprinter** 自动识别目标 *Web 服务器*、操作系统、**开发语言**，动态调整 Payload 优先级，对高置信度后缀自动**跳过冗余测试**，提升扫描效率。

### 3. 类 Burp 代理与四模式爆破

  内置 **mitmproxy** 引擎实现 HTTP/HTTPS 代理抓包，支持**拦截请求**、*修改放行*、丢弃、**发送到 Repeater/Intruder**等标准操作。Intruder 模块支持 **Sniper**（单点依次替换）、*Battering Ram*（全位置相同）、Pitchfork（一一对应）、**Cluster Bomb**（笛卡尔积）四种攻击模式，通过 *§* 标记符号灵活定义注入点，满足**复杂绕过场景**的自动化测试需求。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| PySide6 | 现代化 Qt GUI 框架 | 暗色主题，长时间使用不疲劳 |
| mitmproxy | 专业级代理引擎 | 拦截 HTTPS，证书自动管理 |
| httpx[http2] | 异步 HTTP 客户端 | HTTP/2 支持，高性能并发 |
| RawHTTPClient | 字节级 HTTP 控制 | 精确操控 multipart 边界 |
| SmartAnalyzer | 三级响应分析 | 状态码+关键词+路径+置信度 |
| 异步扫描 | QThread + asyncio | 不阻塞 UI，实时结果更新 |

## 📖 使用指南

① **准备工作**：执行 pip install -r requirements.txt 安装依赖（核心：*PySide6*、mitmproxy、**httpx**）。运行 python main.py 或双击 *UploadRanger.bat* 启动。首次 HTTPS 抓包需访问 http://mitm.it 下载并安装**受信任的根证书**。

② **核心操作**：在**智能扫描**页输入目标 URL，选择*扫描模式*（推荐先用**安全测试模式**验证漏洞），勾选需要测试的**后缀类型**后点击开始。切换到**代理**页启动 *127.0.0.1:8080* 代理，浏览器设置代理后自动拦截请求，右键发送到 **Repeater** 进行手动绕过调试，或发送到 **Intruder** 执行*自动化爆破*。

③ **结果查看**：扫描结果在**智能扫描**页按**置信度打分**展示，包含*状态码*、响应关键词匹配、**上传路径提取**等信息。Repeater 响应支持 *Raw/Headers/Render* 三视图，Intruder 结果以表格形式呈现所有 Payload 组合的响应差异。

## 📖 项目地址

```
https://github.com/Gentle-bae/UploadRanger/tree/main
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