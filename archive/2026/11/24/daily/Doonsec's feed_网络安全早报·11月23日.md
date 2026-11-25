---
title: 网络安全早报·11月23日
url: https://mp.weixin.qq.com/s/xrtzpOFtj12NjkOfU8pDtA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:43:39.585935
---

# 网络安全早报·11月23日

# 网络安全早报·11月23日

原创

安全早报
安全早报

Ncko

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 11 月 23 日 · 共 8 条

01在野利用思科 Expressway 集群设备 root 命令执行漏洞被利用

CISA 于 11 月 23 日警告联邦机构，攻击者正在利用思科 Expressway 的 CVE-2026-76466（CVSS 9.8）。漏洞源于硬编码凭据，以及集群 TLS 校验模式下客户端证书验证不足，未认证攻击者可在 Expressway-C 与 Expressway-E 集群设备上以 root 权限执行系统命令。思科已在 10 月 21 日发布的 X15.5.20 中修复。CISA 在 11 月 20 日将该漏洞列入已知被利用漏洞（KEV）目录，要求联邦文职行政机构在三天内完成处置。俄罗斯安全公司 F6 称，攻击者借助一个未具名 AI 助手利用该漏洞，先控制两台互联网暴露设备，再进入两台内网集群节点；取得 root 后部署 Python 脚本扫描网络、SMB 资源、SQL Server、WinRM 和 GitLab 仓库，以窃取凭据。

**受影响：**Expressway Series X15.5.20 之前版本；以集群方式配置的 Expressway-C 和 Expressway-E。

**官方处置：**思科要求升级至 X15.5.20；CISA 依据 BOD 26-04 要求联邦机构在列入 KEV 后三天内完成修复。

02在野利用MONAI Label 上传路径穿越 0day 被 AI 智能体利用，CISA 列入 KEV

CISA 于 11 月 23 日将 CVE-2026-133968 列入 KEV。亚马逊威胁情报称，疑似中国关联的攻击者使用自主 AI 智能体 Cairn，在 9 月发现并利用了 MONAI Label 文件上传功能中的路径穿越漏洞。记录显示，智能体在约 11 分钟内从映射 API 进展到向服务器任意写入文件，随后在 Python 解释器启动时执行的文件中植入反向 shell，取得 root 权限。行动持续约 48 小时，目标为东亚地区（中国大陆以外）高校的 IP 地址；亚马逊推断同一漏洞被用于入侵第二所高校的服务器。MONAI Label 安全公告将该漏洞评为 critical，影响 0.8.5 及更早版本，认证默认关闭，能访问服务器的网络用户均可利用。

**受影响：**MONAI Label 0.8.5 及更早版本；默认配置未启用认证。

**官方处置：**MONAI Label 公告称修复已创建，将随下一版本发布；CISA 已将 CVE-2026-133968 列入 KEV。

03在野利用N-able Mail Assure 修复 9.3 分 SSRF，CISA 同日列入 KEV

N-able 在调查 Mail Assure 与 SpamExperts 托管云服务攻击时发现 CVE-2026-134624（CVSS 9.3），并于 11 月 22 日披露已修复。漏洞原因是配置中继时执行的 LDAP 同步连接检查未限制目标地址，具备足够权限的 API 用户可让服务器连接任意内网主机和端口，识别可达服务并向其发送构造数据。11 月 16 日，N-able 下线门户和 API；11 月 18 日确认遭攻击，攻击者入侵一台 Web 服务器并可能访问其中存储的凭据；公司更换凭据、撤销 API 与 OAuth 令牌，11 月 21 日恢复门户和 API。N-able 称利用范围限于单台托管服务器，持续监控未发现进一步恶意活动。CISA 于 11 月 23 日将该漏洞列入 KEV。

**受影响：**Mail Assure 与 SpamExperts Hosted Cloud；修复版本为 Mail Assure/SpamExperts 20261121.1943。

**官方处置：**升级至 20261121.1943；N-able 称将在两周内发布正式根因分析。

04在野利用SAP NetWeaver 漏洞被在野利用，CISA 要求三天内处置

SecurityWeek 11 月 23 日报道，CISA 在 11 月 20 日将 SAP NetWeaver 的 CVE-2025-42884（CVSS 6.5）列入 KEV，并援引在野利用证据。未认证攻击者可注入 JNDI 环境属性，或在 JNDI 查询中传入 URL，使系统访问非预期的 JNDI provider，导致服务器信息泄露或被修改。SAP 已在 2025 年 11 月安全更新中修复该漏洞。同一天，CISA 还将 VMware vCenter 的 CVE-2026-123890 和 Apache Roller 的 CVE-2026-129448 列入 KEV，两项均被指已被利用。

**受影响：**SAP NetWeaver，未应用 2025 年 11 月安全更新的版本。

**官方处置：**应用 SAP 2025 年 11 月安全更新；CISA 依据 BOD 26-04 要求联邦机构按期完成修复。

05挪威能源企业 Equinor、Skagerak Energi 遭 Azure API Management 漏洞攻击

挪威国家安全局（NSM）表示，身份未明的攻击者利用微软 Azure API Management（APIM）漏洞，目标为平台中存储的访问令牌和其他敏感信息。Equinor 于 11 月 17 日检测到攻击，11 月 20 日完全控制，部分内部服务受影响，油气生产正常，公司称没有数据被窃取或篡改的迹象。Skagerak Energi 于 11 月 18 日披露另一起攻击，称运营和发电未受影响，未发现信息泄露迹象。微软在一份发给客户的非公开公告中称，11 月 18 日发现影响 APIM Classic 层级的问题，次日关闭访问路径；主要影响未按安全建议使用 Azure Key Vault、直接在 APIM 中存储敏感信息的客户，新版 APIM 不受影响。微软未披露受影响客户数量。

**受影响：**Azure API Management Classic 层级；在 APIM 中直接存储凭据且未使用 Azure Key Vault 的客户。

**官方处置：**微软于 11 月 21 日发布指南，说明受影响客户如何识别并更换可能暴露的凭据；NSM 称挪威国家网络风险等级为高。

06高危工信部 NVDB 通报 OpenJDK Base64 解码器堆溢出漏洞

11 月 23 日，工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）发布通报，称 OpenJDK 的 Base64 解码器存在堆缓冲区溢出缺陷，攻击者发送恶意数据可损坏内存，造成敏感信息泄露或远程执行任意代码，对应 CVE-2026-114938。受影响产品包括 OpenJDK，以及 Oracle Java SE、Oracle GraalVM for JDK、Oracle GraalVM Enterprise Edition、Red Hat OpenJDK、Amazon Corretto 等基于其源代码构建的发行版。OpenJDK 社区及部分发行版厂商已修复并发布安全公告，Oracle 在 2026 年 11 月关键补丁更新中提供修复。

**受影响：**OpenJDK 及基于其源代码构建的 Oracle Java SE、Oracle GraalVM、Red Hat OpenJDK、Amazon Corretto 等发行版。

**官方处置：**NVDB 要求升级至最新安全版本；无法立即升级时，可关闭 Base64 解码加速路径、限制虚拟机使用 AVX-512 指令集、收敛互联网暴露面并加强网络访问控制。

07三星证券 VOC 系统遭入侵，8241 名客户信息泄露

三星证券 11 月 23 日披露，11 月 21 日在客户意见（VOC）系统中发现外部入侵痕迹，部分客户上传的附件被泄露。调查确认 8241 人的个人信息外泄，涉及姓名、账号、地址、联系方式、驾照号码等 13 类信息，具体泄露项目因人而异。公司称发现后立即实施防火墙阻断，并向金融监督院和韩国互联网振兴院（KISA）报告，将逐一通知受影响客户。三星证券代表理事朴钟文当日在官网发布道歉信。

**受影响：**三星证券 VOC 系统；8241 名客户，泄露信息包括姓名、账号、地址、联系方式、驾照号码等 13 类。

**官方处置：**三星证券称已实施防火墙阻断，向金融监督院和 KISA 报告，并将逐一通知受影响客户泄露的具体项目。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeVQAvd8EcdRXF0HoEum6vLOmJzCggyxibNQxicJQZ0u0ez8cFHKnTiaw4Zarreibc3Q5UBJ0j6Gvdsn5BnSpljps8T9hnxicoo9ibLvs/640?from=appmsg)

三星证券总部，朝鲜日报 2026 年 11 月 23 日报道配图。

08英国零售商 Next 称第三方供应商遭攻击，部分相关数据被未授权访问

11 月 23 日，Next 向投资者披露，一家第三方在线供应商发生网络安全事件，攻击者未授权访问了部分与 Next 相关的数据。Next 称当前证据显示没有客户个人数据受影响，并确信自身系统未被入侵。公司未披露供应商名称和访问发生的时间，调查仍在进行。

**受影响：**Next 的一家第三方在线供应商；Next 称客户个人数据未受影响。

**官方处置：**Next 称已与供应商立即调查事件性质和范围，调查仍在进行。

信息来源

CISA（KEV，11 月 23 日）　https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog

BleepingComputer（Cisco Expressway）　https://www.bleepingcomputer.com/news/security/cisa-flags-critical-cisco-expressway-rce-flaw-as-actively-exploited/

SecurityWeek（SAP NetWeaver / Cisco Expressway）　https://www.securityweek.com/sap-netweaver-cisco-expressway-flaws-exploited-in-attacks/

SecurityWeek（N-able）　https://www.securityweek.com/n-able-patches-critical-flaw-disclosed-after-mail-assure-cyberattack/

SecurityWeek（MONAI Label）　https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/

MONAI Label 安全公告　https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94

The Record（挪威能源企业）　https://therecord.media/norway-microsoft-cyberattack-equinor

北京日报 / NVDB（OpenJDK）　https://news.bjd.com.cn/2026/11/23/12040826.shtml

朝鲜日报（三星证券）　https://www.chosun.com/english/market-money-en/2026/11/23/32ODCHEBT5ASVMHFGIQ3RSLHXA/

每日经济新闻（三星证券）　https://en.fnnews.com/news/202611231034062688

Reuters（Next）　https://live.euronext.com/en/financial-news/uks-next-flags-cyber-breach-online-supplier-says-no-customer-data-compromised

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过