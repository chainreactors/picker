---
title: 【红队必备】：渗透综合性安全检测工具无影
url: https://mp.weixin.qq.com/s/9Gjv3yXl3_xybhkZsnZmpA
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:22:23.891518
---

# 【红队必备】：渗透综合性安全检测工具无影

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODwcnHXEhtYHQE0OOUNy2s7DVFjj4hwB0sf8H99MKIuy8fbWmB5n4BSnUEiazpQafkDibf8FP4YQn7OvVkJXR7fqWB51J9x8gxtaM/0?wx_fmt=jpeg)

# 【红队必备】：渗透综合性安全检测工具无影

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# 【红队必备】：渗透综合性安全检测工具无影

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  无影(TscanPlus) 是一款基于 **Wails 框架**开发的综合性网络安全检测工具，内置 *2.6W+ 指纹库* 与 6100+ POC，集成 **资产测绘、端口扫描、密码破解、目录枚举、空间测绘**等 15+ 功能模块，面向**甲方安全团队**与**渗透测试工程师**，实现从资产发现到漏洞验证的全流程自动化。

## 🚀 一句话优势

**2.6万指纹 8 分钟扫完万条资产**，指纹-POC 联动精准检测，48 种服务一键弱口令破解。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 资产测绘 | 2.6W 指纹，8 分钟/万条资产 |
| POC 检测 | 6100+ POC，指纹联动精准匹配 |
| 密码破解 | 48 种服务，内置精简字典 |
| 空间测绘 | 9 大引擎，多 key 轮询 |
| 项目管理 | 多模块联动，结果持久化 |
| 编码解码 | 36 种算法，多 Tab 叠加 |

## 📸 运行截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODz0wFtTuY5A16dEtxZrDcDlIKNEmWNcZGJm1FRlRPzwqlVwLc7aXcITtnpygyy3HS10kseOzTUiciat1bsBkebX4zneey9ElXCB8/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwZNJ99ItJUTJ1lrsc354bj97rW6G1iaLSLpaHpZLqIfKoGh472AEYaoicbtCCM8Omib6hg0UHaOThroK36TxIBkw2QibrOu7XDoZw/640?wx_fmt=png&from=appmsg)

## ✨ 核心亮点

### 1. 指纹-POC 智能联动

  内置 **2.6 万余条 Web 指纹**与 *130+ 红队常见 CMS 框架*标注，对 1 万个 Web 系统进行指纹识别仅需 **8-10 分钟**。扫描结果自动关联 **6100+ POC**（Level1-3 分级），仅对匹配到的产品执行对应 POC 检测，避免全量发包造成的*时间浪费*与目标告警。支持外接 **Nuclei、Afrog、Xray** 等 POC 工具，实现指纹与外部 POC 库的**模糊匹配联动**。

### 2. 全流程项目化管控

  独创**项目管理**模式，将 *资产测绘 → 子域名枚举 → IP 端口扫描 → 密码破解 → POC 检测 → URL 扫描 → 目录探测 → UrlFinder* 串联为标准化工作流。各阶段结果自动作为下一阶段输入，所有数据**持久化到 SQLite**，支持项目中断后恢复、定时任务、结果二次筛选与 Excel/HTML 导出，满足**企业级安全运营**的审计与追溯需求。

### 3. 48 种服务弱口令破解

  覆盖 **SSH、RDP、SMB、MySQL、SQLServer、Oracle、MongoDB、Redis、PostgreSQL、Elasticsearch、FTP、Telnet、WinRM、VNC、SVN、Tomcat、WebLogic、Jboss、Zookeeper、Socks5、SNMP、WMI、LDAP、SMTP、POP3、IMAP、RouterOS、WebBasicAuth、Webdav、CobaltStrike** 等 48 种常见服务。针对每种服务**优选精简字典**，破解成功后自动进行**连接验证**，确保结果准确可用。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Wails 框架 | Go + Web 前端混合开发 | 跨平台，体验接近原生应用 |
| 2.6W+ 指纹库 | Wappalyzer 格式 + 自定义扩展 | 覆盖主流 Web 组件与框架 |
| 6100+ 分级 POC | Level1-3 风险分级 | 高频漏洞优先检测 |
| 9 大空间测绘 API | Hunter/Fofa/Shodan/Quake 等 | 多源数据去重整合 |
| 36 种编解码 | AES/RSA/SM2/SM4/国密等 | 渗透测试数据转换一站式 |
| AI 辅助分析 | 大模型解析 POC/JS 结果 | 智能化漏洞解读 |

## 📖 使用指南

① **准备工作**：从 GitHub Releases 下载对应系统版本（Windows/Mac/Linux），Windows 需确保已安装 **Microsoft WebView2** 运行时。首次启动需联网下载配置文件（约 1 分钟），或手动从 Gitee 下载配置包解压至 *config/* 目录。

② **核心操作**：创建**新项目**后，在项目管理页添加目标资产（支持 IP、CIDR、域名、URL 格式），勾选需要的功能模块（建议开启 *POC 匹配指纹*与密码破解联动），配置线程数与代理后启动扫描。各模块结果实时显示在对应 Tab 页，右键单条资产可执行**单独 POC 检测**、*目录枚举*、密码破解等深度操作。

③ **结果查看**：扫描完成后在**项目管理**页查看资产概览（URL/IP/漏洞/敏感信息统计），支持按关键词、端口、服务、状态码筛选。点击**导出**按钮生成 Excel 或 HTML 报告，高危漏洞自动标红。POC 检测详情页可查看完整的 *Request/Response* 数据包。

## 📖 项目地址

```
https://github.com/TideSec/TscanPlus?tab=readme-ov-file
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