---
title: 网络安全早报·11月11日
url: https://mp.weixin.qq.com/s/PbiRC0vEqYNUMVnsQbEWlw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:41.091345
---

# 网络安全早报·11月11日

# 网络安全早报·11月11日

原创

安全早报
安全早报

Ncko

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 11 月 11 日 · 共 8 条

01马士基确认遗留系统数据泄露，WhiteArmor 索要 500 万美元

马士基 11 月 11 日发布公告，确认一起 IT 安全事件：有人未经授权访问并取走了公司此前收购业务留下的一个本地遗留系统内的数据。公司称调查仍在进行，已采取措施隔离该系统。勒索组织 WhiteArmor 上周末在其泄露站点列出马士基，称窃得约 100GB 数据，索要 500 万美元比特币，要求 12 月 7 日前支付。

据 BleepingComputer 11 月 11 日报道，WhiteArmor 称数据来自马士基 2022 年收购的 LF Logistics 物流平台，包括约 1.9 万名收货人、6.4 万份已签收单据、1,444 万条仓库库存记录以及采购订单与发货通知。马士基未确认这些数字。

**受影响：**马士基此前收购业务遗留的本地系统；马士基称其他系统，以及通过 API、EDI 接入的客户与合作伙伴系统未受影响。

**官方处置：**马士基称目前调查结果强烈表明没有敏感数据被披露，事件局限在本地系统，客户可照常使用平台下单与管理货运；同时提醒客户对声称与该事件有关的异常通信保持警惕，并通过常规渠道核实。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeVoXFRoEIS8Or9cXDLicTNLwOBRa3YyS4UmNkYiatY64Bq0jsicEGnbrJFtJ17DQnG6lmpIvtUbwMtRfaxWDEygxibObQSIQLbOEgM/640?from=appmsg)

图：BleepingComputer 2026-11-11 报道配图

02在野利用CISA 将 Cisco BroadWorks 与 Openwave 漏洞列入 KEV

美国 CISA 将 Cisco BroadWorks 的 CVE-2026-20320 与 Openwave Webtop Media Transcoder 的 CVE-2026-111793 加入已知被利用漏洞目录，要求联邦机构在 11 月 24 日前完成修复。SecurityWeek 11 月 11 日报道了这次更新。

CVE-2026-20320 是 OCI-P 服务中的盲注型 XML 外部实体漏洞（CWE-611），CVSS 7.5，无需认证即可远程读取配置信息，Cisco 于 8 月 19 日披露。CVE-2026-111793 源于 Webtop Media Transcoder 未强制执行管理员设定的文件类型限制，已认证用户可上传特制文件获取敏感信息。日本 JVN 11 月 9 日将该漏洞标记为已被利用；Malbear Labs 称讲中文的攻击者用 BroadWorks 漏洞攻击了一家欧洲电信运营商及其 13 家客户机构。

**受影响：**Cisco BroadWorks 的 Open Client Interface–Provisioning（OCI-P）服务；Openwave Messaging Webtop Media Transcoder，官方称该组件与其 webmail 关联。

**官方处置：**Cisco 在 BroadWorks RI.2026.07 中修复，公告称没有临时缓解措施；Openwave 修复版本为 1.1.22.0；CISA 要求联邦机构在 11 月 24 日前打补丁。

03高危Fortinet 修复 8 个 9 分以上漏洞，JSON-RPC 接口可未认证执行代码

Fortinet 11 月 10 日发布 8 份安全公告，修复 FortiManager、FortiAnalyzer 与 FortiOS 中的多个漏洞，评分均在 9.0 以上。其中 FG-IR-26-219（CVE-2026-126170，CVSS 9.8）是 FortiManager 与 FortiAnalyzer JSON-RPC API 中的 JSON 注入，启用 JSON API 访问后，特制请求可在未认证情况下执行代码或命令。其余包括 FGFM 服务认证绕过（CVE-2026-126261，9.0）、OFTP 未认证 SQL 注入（CVE-2026-126262，9.3）、OFTP 预认证 SSRF（CVE-2026-126260，9.0），以及 FortiOS 的 BGP、OSPF、VDOM 与 FGSP 相关问题。Fortinet 在公告中未标记这些漏洞存在在野利用。

**受影响：**FortiManager 8.0.0、7.6.0–7.6.7、7.4.0–7.4.5、7.2.0–7.2.8；FortiAnalyzer，以及启用 FortiAnalyzer 功能的 FortiManager；相关 FortiOS 版本。FGFM 使用 TCP 541，OFTP 使用 TCP 514。

**官方处置：**FGFM 漏洞的修复版本为 FortiManager 8.0.1、7.6.8、7.4.6、7.2.9；CVE-2026-126170 的 8.0.3 尚未发布，Fortinet 建议在不使用 JSON API 时把 rpc-permit 设为 none，并单独收紧 541、514 端口的可达性。

04菲律宾 23 家政府与私营机构数据在地下论坛被出售

菲律宾监测组织 Deep Web Konek 汇总 11 月 5 日至 7 日的地下论坛披露，共 23 家当地机构遭到数据泄露或数据暴露，覆盖政府部门、执法机构、军方系统与教育机构。《菲律宾星报》11 月 11 日报道了这份清单。

DeathNote Hackers 称从副总统办公室取走约 10GB、12,979 份 PDF，从劳工就业部取走 1,920 万条记录（约 5.74GB），从菲律宾海岸警卫队取走 6,698 份文件；Happy Go Lucky PH 称从内政与地方政府部及 Barangay 中央数据库取走约 1,900 万份居民档案（约 500GB）；CrimsonSec Philippines 称从陆运署取走 292,424 条记录（约 54.11GB）。名单还包括 DICT、BIR、SEC、交通部、CICC、菲律宾空军、隐私委员会、Mactan Electric 与 LBC Express（2,090 万条运单）。

**受影响：**菲律宾副总统办公室、劳工就业部、海岸警卫队、内政与地方政府部、陆运署等 23 家机构。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5LNgXJargeXQ3gKaQA8lfvw7eINrkc7pf0dMyERoAcEgicBt1iajU9bmt4aq3E1JhW4WHT7b3P4jnTbSlgjDa13trTmqHwFmfGQdW03ahJDpk/640?from=appmsg)

图：Philstar 2026-11-11 报道配图

05N-able 发布 N-central 2026.4 Hotfix 2，修复七个零日漏洞

N-able 11 月 10 日发布 N-central 2026.4 Hotfix 2（构建号 2026.4.1.26），修复研究者公开的 Able2Shell 零日漏洞，共 7 个 CVE：多个 XXE（CVE-2026-125883）、多个 OGNL 注入（CVE-2026-125878）、通过可写 syslog-ng 配置提权至 root（CVE-2026-125879）、MMS3 补丁元数据存储型 XSS（CVE-2026-125880）、通过服务导入 schema 校验的 SSRF（CVE-2026-125881）、文件仓库上传路径穿越导致远程代码执行（CVE-2026-125882）、不安全 IPC 通道导致本地提权（CVE-2026-91000）。

该热修复取代 N-central 2026.4（2026.4.0.27）与 Hotfix 1（2026.4.0.32）。Shadowserver 数据显示，暴露在互联网的 N-central 实例从 11 月上旬的 1,400 多个降至 11 月 10 日的 148 个。

**受影响：**N-central 本地部署版与托管版；本地部署客户需自行升级服务器，托管版由 N-able 升级，两类客户的 Agent 与 Probe 都必须自行升级。

**官方处置：**升级到 2026.4.1.26；内置远程控制功能在该版本中暂时关闭，将在后续修复中恢复。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeUibU9ERYToNtyKggYHpwvPjK8TPKgqEcQjT6qibAbOZJuufUeqSkX1EcricjMv7vFvyyE2IXWW0r5DRTWg75ccJBnZynfuTiceoFA/640?from=appmsg)

图：Shadowserver 暴露数量统计，BleepingComputer 2026-11-11 报道配图

06Railway 报告：被盗 AI 密钥产生约 74 万美元未授权用量

Railway 11 月 10 日发布事件报告，确认攻击者于 10 月 20 日利用其构建基础设施中一个此前未知的漏洞逃逸文件系统隔离并取得内部凭据，用它访问构建历史、取走平台源码，随后利用一处配置错误的 OIDC 绑定获得更多权限，拿到为解密客户环境变量所需的凭据。

公司称最多涉及 1.85% 的工作区、约 10 万个工作区的环境变量可能被解密；攻击者专门检索 AI 供应商凭据，部分查询也指向云、数据库与支付凭据。被盗密钥产生约 74 万美元未授权 AI 用量，Railway 称供应商不退的部分由公司承担。另有 1,852 名用户的关联账号令牌暴露，包括 GitHub OAuth 令牌与 AI Agent 密钥，已被重置。

**受影响：**Railway 平台的工作区环境变量，最多约 10 万个工作区；1,852 名用户的关联账号令牌。

**官方处置：**Railway 称 10 月 21 日已将攻击者完全清除，被利用的漏洞均已修复，未发现客户 Git 仓库或数据库被下载，已向受影响用户发出通知。

07AntiFox AI 渗透平台被用于窃取 AWS 凭据

Arctic Wolf 11 月 11 日披露，攻击者在阿里云上托管自行部署的 AntiFox 实例，用于漏洞利用、部署 WebShell、验证凭据、发现配置并收集 AWS 密钥。AntiFox 是开源 AI 渗透测试平台，从 ARTEX 0.1.1 分叉而来，提供中文界面，可部署 AI Agent 自动完成资产测绘与漏洞探测。

在一起入侵中，攻击者在暴露于互联网的 IIS 服务器上部署 ASPX WebShell，执行系统命令，读取应用配置与数据库连接串，并把配置与日志复制到 Web 可访问目录；随后用有效 IAM 凭据与 EC2 角色探测 AWS 接口，在约 30 分钟内轮换多个身份、发出数百次 API 请求，多数被拒绝，但仍取得生产环境密钥。另一批入侵中，攻击者用有效 AWS 身份读取、复制并删除 S3 对象。

**受影响：**暴露于互联网的 IIS 服务器及其关联 AWS 环境，涉及 IAM 用户、EC2 角色与 S3 存储桶；Arctic Wolf 未公布受害组织名称与数量。

**官方处置：**Arctic Wolf 建议将 IIS WebShell 活动与异常 AWS 访问关联分析，复核大量被拒请求中夹带的成功调用，吊销受影响的 AWS 会话与密钥，并轮换通过应用文件暴露的凭据。

08逾 575 个恶意 OpenClaw skills 向 Windows 与 macOS 投递恶意软件

Acronis 威胁研究部门在《TRU Cyber Pulse 2026》中称，已识别 575 个伪装成实用工具的恶意 OpenClaw skills，向 Windows 与 macOS 系统投递木马、挖矿程序与信息窃取程序。Agent skills 可把指令与可执行代码打包，代码运行时沿用 Agent 已获得的权限，分发给 13 个开发者账号。

报告中的 BOSSAI 调查显示，一名运营者把 10 多个 AI 模型接入侦察、扫描与利用工具，通过微信与 LINE 派发任务并查看 Agent 活动，相关基础设施涉及台湾的应急与政府系统、泰国的大学以及墨西哥的电话数据收集；部分工具被设为无需审批即可运行。研究人员还在 Hugging Face 上记录了伪装成模型、数据集与 AI 应用的恶意载荷。

**受影响：**安装并使用第三方 OpenClaw skills 的 Windows 与 macOS 设备；从 Hugging Face 下载模型、数据集与 AI 应用的用户。

信源

maersk.com.cn/news/articles/2026/11/11/it-security-incident

bleepingcomputer.com/news/security/maersk-confirms-data-breach-as-whitearmor-ransomware-demands-5-million/

securityweek.com/threat-actors-exploit-openwave-cisco-broadworks-vulnerabilities/

sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt

fortiguard.com/psirt/FG-IR-26-219

gbhackers.com/critical-fortinet-vulnerabilities/

philstar.com/headlines/2026/11/11/2569338/massive-cyber-attacks-hit-23-government-private-sites/

status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/

blog.railway.com/p/incident-report-october-security-incident

bleepingcomputer.com/news/security/hackers-use-antifox-ai-agents-in-aws-credential-theft-attacks/

helpnetsecurity.com/2026/11/10/acronis-ai-agent-cyberattacks-report/

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GtFR6uY3nh6MJdyIdsWXrDem00Mia2eSiae1MMcoX2HUKRsPnx0EenFmcMdQwn0qAz5TJfRlOYVF4zsSibLicTlPtA/0?wx_fmt=png)

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