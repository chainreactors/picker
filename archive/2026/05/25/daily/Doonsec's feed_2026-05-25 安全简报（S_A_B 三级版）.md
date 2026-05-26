---
title: 2026-05-25 安全简报（S/A/B 三级版）
url: https://mp.weixin.qq.com/s/HjzySjPI2VTxVNGbbD43OA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:04:11.918093
---

# 2026-05-25 安全简报（S/A/B 三级版）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/faYNvlB0Xd2Fd44c0hB27ZFMZtOaxiccrLSNe7TwXTtAoOB3HsyXTvCdKRLibLlvP5Dd46QPCB8ecRaYh6aGsk3mgqQOKibOwFxuStngZgnnnw/0?wx_fmt=jpeg)

# 2026-05-25 安全简报（S/A/B 三级版）

原创

今木安全
今木安全

今木信息安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 🔴 S级（详细报道）

# CVE-2026-9082 — Drupal Core SQL注入→提权+RCE（CISA KEV 在野利用）

起因：Drupal Core 数据库抽象API存在SQL注入漏洞，CISA于5月22日标记为已知在野利用。

过程：攻击者通过特制请求触发SQL注入，利用数据库抽象API实现权限提升，最终获取远程代码执行能力。

影响：所有未升级Drupal站点均可被完全控制，CISA要求5月27日前修复，仅剩2天窗口。

应对：立即升级至Drupal最新安全版本，参考SA-CORE-2026-004公告。

# CVE-2026-46716 — Nezha Monitoring 跨租户RCE（CVSS 9.9）

起因：Nezha Dashboard中RoleMember角色可通过cron接口向所有被监控服务器推送任意命令。

过程：cron路由使用commonHandler而非adminHandler，CheckPermission对空Servers[]数组返回真，绕过了权限检查。Agent通常以root运行，攻击者可窃取云IAM凭证、/etc/shadow等敏感信息。

影响：CVSS 9.9，所有使用Nezha监控的服务器面临被完全控制风险。同时曝出3个Nezha漏洞（RCE+SSRF+信息泄露），监控基础设施成为攻击目标。

应对：升级至v1.14.15-0.20260517022419-d7526351cf97，审计cron/notification权限配置。

# CVE-2026-34926 — Trend Micro Apex One 目录遍历（CISA KEV 在野利用）

起因：Trend Micro Apex One存在预认证目录遍历漏洞，CISA于5月21日新增至KEV目录。过程：预认证本地攻击者可利用CWE-23目录遍历漏洞修改服务器关键表，注入恶意代码并部署到所有Agent。

影响：企业终端安全产品自身成为攻击入口，所有Agent面临恶意代码下发风险。

应对：CISA截止6月4日，参考Trend Micro官方公告KA-0023430升级。

# 🟡 A级（概要了解）

# CVE-2026-47125 — Arcane 缺少管理员授权→供应链RCE（CVSS 8.8）

任意认证用户可通过PUT接口写入全局环境变量，重定向其他项目的镜像仓库至攻击者控制地址，实现跨项目Docker宿主机RCE

# CVE-2026-46717 — Nezha SSRF+响应体反射（High）

RoleMember通过notification接口触发Dashboard端SSRF，读取内网HTTP响应体无大小限制，可用于内网探测和数据窃取

# CVE-2026-47138 — Parse Server 预认证ReDoS（CVSS 4.0: 8.7）

未认证攻击者利用X-Parse-Client-Version头触发多项式正则回溯，单请求可消耗Node.js Worker数分钟CPU

# CVE-2025-34291 — Langflow 跨域令牌窃取→系统完全控制（CISA KEV）

过度宽松CORS+SameSite=None Cookie，恶意网页可跨域携带凭据刷新token后执行任意代码

# FileBrowser Quantum 路径遍历（GHSA-qqqm-5547-774x, Critical）

PATCH接口fromPath/toPath中使用..可突破分享目录限制，sanitizer因filepath.Join先收拢路径而失效

# CVE-2026-41091 — Microsoft Defender 本地提权（CISA KEV）

链接跟随漏洞，授权攻击者可本地提升权限，CISA截止6月3日CVE-2008-4250 (MS08-067) — Windows Server Service RPC缓冲区溢出 🧟（CISA重新标记）

经典漏洞被CISA重新标记为在野利用，老系统（XP/2003）仍有攻击价值

利旧CVE批量回溯（CVE-2009-1537/3459, CVE-2010-0249/0806）

CISA回溯标记DirectX/Adobe Reader/IE历史高危CVE，说明考古漏洞2026年仍有在野利用

# ⚪ B级（主题聚合）

漏洞利用：Cockpit 359 RCE、BookStack 25.12.1 DoS、FUXA 1.2.9 RCE、WordPress Supsystic SSTI、Apache HertzBeat RCE 等8条

AI/ML工具链漏洞：Langflow令牌窃取、LiteLLM、Flowise缺认证、MindsDB — LLMOps安全需纳入常规评估

监控基础设施安全：Nezha集中曝出3个漏洞，Zabbix/Prometheus/Grafana同类系统需自查

企业终端安全：Trend Micro Apex One、Microsoft Defender、Exchange Server XSS — 安全产品自身成为攻击面

内网补丁合规：MS08-067等考古漏洞仍在利用，老系统补丁合规迫在眉睫

隐私与取证：Signal取证工具可绕过端到端加密提取通信记录，设备全盘加密+远程擦除是有效对策

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/FUyHlHlguEhThyq7zhZ0BBIYR0x35VMGKPJ5qTBSOvib3x60PXGrBbu00m209ciciaevmX4ibPasqkcR72WVZ1M8Nw/0?wx_fmt=png)

今木信息安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/FUyHlHlguEhThyq7zhZ0BBIYR0x35VMGKPJ5qTBSOvib3x60PXGrBbu00m209ciciaevmX4ibPasqkcR72WVZ1M8Nw/0?wx_fmt=png)

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