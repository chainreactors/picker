---
title: 渗透测试人员必备：浏览器 JWT 利用工具
url: https://mp.weixin.qq.com/s/2CzDUcuIIUJXc7I2qYuNog
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:40:46.742586
---

# 渗透测试人员必备：浏览器 JWT 利用工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODzOLA2xMHdQuVBODhL7ZU6TFXDHZxiadkoSESlic108Vic1PlkNLKrFw4pF2rFbok5LhIm1K0RlhL7ZUG7JKEfUHnYM2AfetsBLI4/0?wx_fmt=jpeg)

# 渗透测试人员必备：浏览器 JWT 利用工具

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# 渗透测试人员必备：浏览器 JWT 利用工具

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  JWTAuditor 是一款 **100% 客户端运行**的 JWT 安全测试平台，集成 *15+ 自动漏洞检测*、7 种专业攻击模块、密钥爆破与 Token 编辑功能，面向**渗透测试人员**与**安全工程师**，解决现有工具隐私泄露与功能分散的痛点。

## 🚀 一句话优势

**浏览器本地完成全量 JWT 安全审计**，Token 无需上传云端，支持 **15+ 漏洞类型**自动检测与*7种高级攻击*。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 安全分析 | 15+ 漏洞类型自动检测 |
| 密钥爆破 | 内置 1000+ 常见密钥字典 |
| JWT 编辑器 | 可视化修改 Header/Payload |
| Token 生成器 | RSA 密钥对自动生成 |
| 攻击平台 | 7 种专项攻击模块 |
| 文档中心 | 漏洞原理与修复指南 |

## 📸 运行截图

## ✨ 核心亮点

### 1. 隐私优先的本地审计

  与在线 JWT 工具不同，JWTAuditor **所有计算均在浏览器本地完成**，Token 数据不会上传至任何服务器。这种设计彻底消除了**敏感 Token 泄露**风险，特别适合审计包含*PII*、凭证信息或**信用卡号**的生产环境 JWT。纯前端架构意味着即使在内网隔离环境也可正常使用，满足**金融**与*政务*场景的合规要求。

### 2. 自动化漏洞检测体系

  内置 **15+ 安全检测规则**，覆盖 *Algorithm None*、弱算法、**算法混淆攻击**、*KID 参数注入*、敏感信息泄露、**Token 生命周期缺陷**等常见 JWT 漏洞。每项发现均附带**详细解释**与*修复建议*，不仅指出"是什么"，更说明"为什么"和"如何修"，具备**安全培训**价值。

### 3. 七模块高级攻击平台

  提供 **None Algorithm 绕过**、*RS256 转 HS256 算法混淆*（14+ 变体）、KID 路径遍历与命令注入（47+ Payload）、**JKU/X5U 远程密钥注入**、*JWK Header 嵌入*、权限提升、**Claim 伪造**七种攻击模块。支持从简单签名移除到复杂的**密钥混淆攻击**，覆盖 OWASP 列出的主要 JWT 威胁向量。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| 纯前端架构 | HTML/JS 无后端依赖 | 隐私安全，部署简单 |
| Web Worker | 密钥爆破多线程 | 不阻塞 UI，性能优化 |
| Web Crypto API | 浏览器原生加密 | 支持 RSA/ECDSA 生成 |
| Docker 支持 | Nginx 生产级配置 | 企业内网快速部署 |
| CSP 策略 | 内容安全策略 | 防 XSS，增强安全性 |

## 📖 使用指南

① **准备工作**：访问 *jwtauditor.com* 直接使用在线版，或执行 git clone 拉取仓库后运行 docker-compose up -d 本地部署。Docker 版本基于 **Nginx** 优化，包含 *Gzip 压缩*与安全响应头配置。

② **核心操作**：在**输入框**粘贴待审计的 JWT Token，系统自动解析并执行**安全扫描**。切换到 *Attack Platform* 标签选择攻击模块（如 Algorithm Confusion），修改参数后生成**攻击载荷**。使用 **Secret Bruteforcer** 上传自定义字典或选择内置 1000+ 常见密钥进行爆破。

③ **结果查看**：安全分析结果按**风险等级**（Critical/High/Medium）分类展示，点击可查看*详细原理*与修复代码示例。攻击模块生成的 Token 可直接**复制到 Burp Suite** 等工具验证。所有操作日志保留在浏览器本地，可通过 *Export* 导出审计报告。

## 📖 项目地址

```
https://github.com/dr34mhacks/jwtauditor
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