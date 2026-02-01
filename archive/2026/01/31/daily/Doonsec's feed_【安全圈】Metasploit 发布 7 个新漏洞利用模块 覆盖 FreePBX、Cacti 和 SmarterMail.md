---
title: 【安全圈】Metasploit 发布 7 个新漏洞利用模块 覆盖 FreePBX、Cacti 和 SmarterMail
url: https://mp.weixin.qq.com/s/ymGCtFaI8bU5XLBK1QMpOA
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:24:02.354384
---

# 【安全圈】Metasploit 发布 7 个新漏洞利用模块 覆盖 FreePBX、Cacti 和 SmarterMail

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliah0k6RfNmQeeTqZ1E6WkozWD0HqVRgwcGaCuphPSuJhfrIav6Y0PmjWdniboz2SVACDP2SFKCNzeg/0?wx_fmt=jpeg)

# 【安全圈】Metasploit 发布 7 个新漏洞利用模块 覆盖 FreePBX、Cacti 和 SmarterMail

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliah0k6RfNmQeeTqZ1E6WkozfLl2LIaiaGgqvKbGZAicnVzhI5knYtVKpbRK1Gv1ZgIWx9j99ONiatWXg/640?wx_fmt=jpeg&from=appmsg)

本周 Metasploit 框架的最新更新为渗透测试人员和红队成员带来重大增强，新增了七个针对常用企业软件的漏洞利用模块。本次更新的亮点包括三个针对 FreePBX 的复杂模块，以及针对 Cacti 和 SmarterMail 的关键远程代码执行（RCE）功能。

此次更新凸显了通过将认证绕过漏洞与次要漏洞串联实现完全系统入侵的持续风险。

## **FreePBX 漏洞串联攻击**

框架最重要的新增功能涉及三个针对 FreePBX 的不同模块。FreePBX 是控制 Asterisk（PBX）的开源图形界面。研究人员 Noah King 和 msutovsky-r7 开发了一种方法，通过串联多个漏洞将权限从未认证状态提升至远程代码执行。

攻击链始于（CVE-2025-66039），这是一个认证绕过漏洞，允许未授权攻击者绕过登录协议。一旦突破认证屏障，框架提供两条不同的 RCE 路径。

第一条利用路径利用了被标识为（CVE-2025-61675）的 SQL 注入漏洞。通过注入恶意 SQL 命令，攻击者可操纵数据库向 `cron_job` 表插入新任务，从而有效安排任意代码的执行。

第二条路径则利用（CVE-2025-61678），这是固件上传功能中存在的不受限制文件上传漏洞。攻击者可借此直接向服务器上传 webshell，立即获得控制权。

该系列中的第三个辅助模块利用相同的 SQL 注入漏洞创建恶意管理员账户，展示了该漏洞利用链的多功能性。

## **Cacti 和 SmarterMail 的关键 RCE 漏洞**

除 VoIP 领域外，本次更新还涉及监控和通信平台的严重漏洞。新模块针对流行网络监控工具 Cacti，专门利用（CVE-2025-24367）。该漏洞影响 1.2.29 之前版本，允许通过图形模板机制进行未认证远程代码执行。鉴于 Cacti 在基础设施监控中的广泛使用，该模块成为网络管理员需优先测试的案例。

同时，框架新增了对 SmarterTools SmarterMail 中（CVE-2025-52691）的利用支持。这一未认证文件上传漏洞依赖于对 `guid` 变量的路径遍历操作。该模块显著特点是兼容不同操作系统：针对 Windows 目标时，漏洞利用会在 webroot 目录部署 webshell；针对 Linux 环境时，则通过创建 `/etc/cron.d` 定时任务实现持久化和执行。

## **持久化工具与核心修复**

本次发布还通过新增持久化模块增强了攻击后能力。新的 Burp Suite 扩展持久化模块允许攻击者在专业版和社区版上安装恶意扩展，使其在用户启动应用时自动执行。此外，团队将 Windows 和 Linux 的 SSH 密钥持久化功能整合为统一模块以简化操作。

在维护方面，修复了若干关键错误。包括导致哈希数据与 John the Ripper 密码破解工具不兼容的格式问题，以及 SSH 登录扫描器中存在的逻辑错误（该错误曾将会话无法开启的成功登录误报为失败），现已修复以确保测试期间报告的准确性。

| 模块名称 | CVE 编号 | 目标系统 | 影响 |
| --- | --- | --- | --- |
| FreePBX 端点 SQL 注入 | CVE-2025-66039, CVE-2025-61675 | FreePBX | 远程代码执行 |
| FreePBX 固件上传 | CVE-2025-66039, CVE-2025-61678 | FreePBX | 远程代码执行 |
| FreePBX 管理员创建 | CVE-2025-66039, CVE-2025-61675 | FreePBX | 权限提升 |
| Cacti 图形模板 RCE | CVE-2025-24367 | Cacti (< 1.2.29) | 远程代码执行 |
| SmarterMail GUID 上传 | CVE-2025-52691 | SmarterMail | 远程代码执行 |
| Burp 扩展持久化 | 无 | Burp Suite | 持久化 |
| SSH 密钥持久化 | 无 | Linux / Windows | 持久化 |

***END***

阅读推荐

[【安全圈】TrustBastion 恶意安卓 App 曝光，瞄准你的支付宝与微信钱包](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073929&idx=1&sn=b57ffb86f56d66a8ea12c5455a3dfdbf&scene=21#wechat_redirect)

[【安全圈】假意网恋设局，实为安卓间谍软件植入](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073929&idx=2&sn=ad8905d7471facd155f7f0e16cdd3333&scene=21#wechat_redirect)

[【安全圈】eScan证实更新服务器遭入侵，黑客借其推送恶意更新](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073929&idx=3&sn=b07e61c786b7f751427f1a542fb845e9&scene=21#wechat_redirect)

[【安全圈】抖音崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=1&sn=b745a686b245684c9bdd345d1b77afb8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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