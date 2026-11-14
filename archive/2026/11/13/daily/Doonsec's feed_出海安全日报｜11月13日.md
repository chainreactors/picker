---
title: 出海安全日报｜11月13日
url: https://mp.weixin.qq.com/s/Q_FGbYKWK-m1pbI9fvlrWg
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:15:19.906660
---

# 出海安全日报｜11月13日

# 出海安全日报｜11月13日

安世加
安世加

安世加

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安世加 · 出海安全日报

2026年11月13日 星期五

今日看点：远程支持软件 ScreenConnect 的部分合作伙伴环境遭未授权访问，ConnectWise 初步判断与第三方扩展被滥用有关，已在约 400 个环境中停用相关扩展；Apache HTTP Server 发布 2.4.71，修复一项 HTTP/2 模块可致远程代码执行的严重漏洞；Node.js 三个维护版本线修复 16 个漏洞；意大利数据保护机构因服装企业未处理删除请求、继续发送营销短信处以罚款。

今日头条

远程运维 · 第三方扩展

**ScreenConnect 合作伙伴环境遭入侵，第三方扩展被滥用**

远程支持软件厂商 ConnectWise 正在调查部分合作伙伴 ScreenConnect 环境遭未授权访问的事件，其官方安全通告最近一次更新于 **2026年11月12日 18:45（UTC）**。ConnectWise 称，目前未发现自身基础设施被入侵，也未发现初始访问利用了 ScreenConnect 本身的漏洞；初步判断攻击者滥用了合作伙伴环境中安装的独立第三方扩展（RMM+ 系列），借此进入环境并部署未经授权的远程访问软件。

ConnectWise 表示，约 **400 个**合作伙伴环境装有至少一个 RMM+ 系列扩展，这类扩展提供可执行远程命令的接口，仅由合作伙伴设置的口令保护；装有扩展本身并不代表已被入侵。ConnectWise 已在其可操作的环境中停用 Labtech Plus、RMM Plus、RMM+ 等五个扩展，并要求本地部署的合作伙伴立即自行停用。研究人员报告，RMM+ 1.0.31 与 1.0.32 版本存在认证缺陷，未配置访问密钥时可接受空密钥，该问题已分配 CVE 编号。

据 The Record 报道，安全公司 Huntress 观察到 48 家机构的 288 个终端在约 90 分钟内被推送恶意客户端。攻击工具包还试图在技术人员远程连接受感染终端时反向扩散到其工作站，ConnectWise 称，2026 年 9 月 8 日发布的客户端 26.6.5 版本已能阻断这一扩散手法，并提醒云端控制台升级不会自动更新技术人员客户端。

来源：ConnectWise 官方安全通告｜更新于 2026-11-12（UTC）
https://www.connectwise.com/company/trust/advisories
来源：The Record｜2026-11-12
https://therecord.media/connectwise-screenconnect-breaches-third-party-tool

安世加观察

这意味着：委托海外 MSP 或外包 IT 管理终端的出海团队，应当向服务商确认是否使用 ScreenConnect 及 RMM+ 类扩展、扩展是否已停用、技术人员客户端是否已升级到 26.6.5 或更高版本，并在可信设备上吊销现有会话、重置凭证、启用多因素认证。更长远看，远程运维工具的插件清单、审批记录和操作日志，是 ISO 27001／SOC 2 Type II 中供应商管理与特权访问控制可以直接抽查的证据；仅停用扩展、重置密码并不能清除已植入的远程访问软件，疑似受影响的终端需要用独立工具排查。

◆ 全球监管与安全快讯

**01**  Web 服务器 · 补丁

**Apache HTTP Server 2.4.71 修复 HTTP/2 远程代码执行漏洞**

Apache HTTP Server 项目于 **2026年11月11日**发布 2.4.71 版本，修复三个漏洞。其中 CVE-2026-119618 被评为严重级：mod\_http2 模块在处理请求头时存在并发同步问题，可导致堆内存损坏和远程代码执行，影响 2.4.55 至 2.4.70 版本，以及 GitHub 上独立发布的 mod\_h2 2.0.8 至 2.0.42。另两项分别是 mod\_md 空指针解引用导致子进程崩溃（重要级，影响 2.4.30 至 2.4.70），以及 mod\_vhost\_alias 一字节栈缓冲区越界写（低危，影响 2.4.69 与 2.4.70）。

这意味着：对外提供网站或 API、并开启了 HTTP/2 的 Apache 服务器应优先升级；使用发行版软件包或容器镜像的团队，需要同时跟进上游镜像与发行版的修复进度，并把升级结果记入漏洞管理台账。

来源：Apache HTTP Server 官方安全公告｜2026-11-11
https://httpd.apache.org/security/vulnerabilities\_24.html

**02**  开发框架 · Node.js

**Node.js 修复 16 个漏洞，HTTPS 缺陷可泄露其他连接内存**

Node.js 项目于 **2026年11月11日**发布安全更新，覆盖 26.x、24.x、22.x 三个版本线，修复版本为 v26.13.1、v24.22.3、v22.23.5，共修复 16 个漏洞（7 个高危、6 个中危、3 个低危），并更新 llhttp、undici、sqlite 等依赖。官方说明中，CVE-2026-123864 可让未经认证的客户端在特定写法的 HTTPS 服务中读取属于其他连接的内存，包括 TLS 私钥和其他用户的请求；多项 HTTP/2 漏洞可被未经认证的客户端用来让服务进程中止，或持续占用内存与文件描述符。官方提醒，已停止维护的版本在每次安全发布时都默认受影响。

这意味着：以 Node.js 承载对外接口的 SaaS 团队，应尽快把生产环境与构建镜像升级到上述版本，仍在使用停止维护版本的服务需要排期迁移；版本清单与升级记录同样是审计中常被要求提供的材料。

来源：Node.js 官方安全公告｜2026-11-11
https://nodejs.org/en/blog/vulnerability/november-2026-security-releases

**03**  欧盟 · GDPR 用户权利

**意大利 DPA：未处理删除请求、继续发营销短信被罚**

EDPB 于 **2026年11月10日**转载意大利数据保护机构的决定（最终决定日期 2026年9月23日）：一名用户要求服装企业 Barbuti S.p.A. 删除其个人数据后仍持续收到促销短信。由于短信中没有说明如何行使数据保护权利，该用户把请求发到了公司的通用联系邮箱，公司只回复了自动确认，此后既未处理也未停止发送。监管机构援引 EDPB《数据主体权利指南 01/2022》指出，通过企业提供的任一沟通渠道提交的请求，即使不是隐私政策中指定的首选渠道，一般也应视为有效并予以处理。监管机构认定其违反 GDPR 第 5(2)、12、17 条及意大利数据保护法典第 130 条，处以 5,000 欧元罚款，并责令整改营销信息中的联系方式。

这意味着：面向欧洲消费者的跨境电商与 App 团队，不能只依赖隐私政策里写明的专用入口，客服邮箱、站内信等渠道收到的删除或退订请求也要有人识别、转交并在时限内答复；营销短信和邮件里应写明行使权利的联系方式，并保留处理记录。

来源：EDPB 国家新闻｜2026-11-10
https://www.edpb.europa.eu/news/italian-dpa-fines-clothing-company-for-failing-to-handle-erasure-request\_en

[![关于安世加](https://mmbiz.qpic.cn/sz_mmbiz_jpg/757fvrbk7oZP2OcT5Hn8o8aPMDqBVKz6ut7z74yX701u8BZoOxnKwiaUB3u11GNWTRoOyXMUzBkvGxEhP4w3jzH1z8aVdVvIvQ75W7OtLfX0/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247545283&idx=1&sn=0593d7f6a3ed25afe77235c51f08e019&scene=21#wechat_redirect)

点击图片了解安世加

— 安世加 · 出海安全日报

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

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