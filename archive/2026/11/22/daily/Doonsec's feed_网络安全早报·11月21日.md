---
title: 网络安全早报·11月21日
url: https://mp.weixin.qq.com/s/1Sz5giKbkuGPIZ_tYwsp8Q
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:55.152005
---

# 网络安全早报·11月21日

# 网络安全早报·11月21日

原创

安全早报
安全早报

Ncko

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 11 月 21 日 · 共 10 条

01高危 nginx 五个内存破坏漏洞可远程执行代码，PoC 已公开

2026年11月19日，奇安信 CERT 发布通告，披露 nginx 的 5 个内存破坏漏洞，其中 1 个为整数下溢导致的堆越界读写、4 个为释放后使用，未认证攻击者可经公网 TLS/HTTP/2 端口触发，以 nginx worker 权限执行任意命令。

主漏洞 CVE-2026-123007 自 2015 年起存在于所有官方版本；奇安信评级高危，CVSS 3.1 评分 8.1，PoC 与 EXP 已公开，暂未发现在野利用。

**受影响：**nginx 官方发布版本，CVE-2026-123007 影响 2015 年以来的版本，触发条件依配置不同

02高危 PHP 会话反序列化漏洞可致 RCE，官方发布修复版本

2026年11月19日，奇安信 CERT 披露 PHP 的 files 会话处理器在更新会话时未先清空文件，写入中断会残留新旧混合数据，后续 session\_start() 将其反序列化，配合应用中的 gadget 链可执行任意代码。

漏洞编号 CVE-2026-126714，CVSS 4.0 评分 9.2，技术细节已公开，未发现 POC 与在野利用。

**受影响：**PHP 8.2.0–8.2.35、8.3.0–8.3.36、8.4.0–8.4.27、8.5.0–8.5.12；Redis、数据库等非文件会话后端不受影响

**官方处置：**官方修复版本为 8.2.36、8.3.37、8.4.28、8.5.13，10 月 21 日发布的 8.5.12、8.4.27、8.3.36、8.2.35 不含该修复；临时缓解为设置 session.upload\_progress.enabled=0。

03 微软 agent-framework 两个 PyPI 版本被植入凭据窃取代码

2026年11月17日，微软开源 AI 框架 Microsoft Agent Framework 的 Python 包 agent-framework 1.26.1、1.26.2 在 PyPI 上被发现植入凭据窃取代码，上传者为微软关联的合法发布者账号。

包内 af\_runtime\_diag.pth 使 Python 启动即加载采集模块，读取环境变量与凭据文件，并向 GitHub Actions、Azure DevOps、Azure 托管身份申请令牌后外传。

**受影响：**PyPI 包 agent-framework 1.26.1、1.26.2，Python 3.11 至 3.15 环境

**官方处置：**PyPI 已隔离涉事发布者账号；1.26.2 在 1.26.1 被隔离后仍成功发布。

![](https://mmbiz.qpic.cn/mmbiz_png/5LNgXJargeWp8hBya95dAeZIbPcWZ1gl4jDeiacFEWV5fibsFVYU1POOcvR2QXROrF8r7P2TtJlDQWDjKfxYzcX6wcUOdltWxqkD6ERV4bZ0I/640?from=appmsg)

图：白泽安全实验室报告截图（安全内参，11月19日）

04 欧盟委员会确认遭 AI 辅助攻击，部分系统仍离线

2026年11月19日，欧盟委员会发言人证实，10月22日发现的 AI 辅助网络攻击仍在影响部分系统；Politico 报道称攻击持续至少 10 天，波及翻译、费用报销工具与员工薪资工时数据库。

发言人称已关闭多个应用、大部分已恢复，未发现全体员工数据泄露的证据，拒绝证实 Politico 报道的系统清单；CERT-EU 于 11月4日警告 ARTEX 智能体被用于攻击。

**受影响：**欧盟委员会内部管理系统（人事、翻译、费用报销）

05在野利用 VMware vCenter 认证绕过漏洞在野利用，CISA 列入 KEV

2026年11月20日，CISA 将 VMware vCenter 目录服务认证绕过漏洞 CVE-2026-123890 列入 KEV，称攻击者可建立以 administrator@vsphere.local 身份的会话，取得 vCenter 与虚拟化基础设施管理员权限。

KEV 要求联邦机构在 2026年11月23日前完成处置。

**受影响：**VMware vCenter（Directory Service）

**官方处置：**Broadcom 已发布补丁；CISA 要求按厂商指引在 11月23日前完成修复。

06 国家计算机病毒应急处理中心预警「银狐」投毒 VPN 安装包

2026年11月20日，国家计算机病毒应急处理中心发布预警报告，称境内连续发现多个携带木马病毒的 VPN 客户端安装包，主要针对 Windows 平台用户。

报告将这批投毒安装包归入「银狐」系列网络攻击活动。

**受影响：**Windows 平台 VPN 客户端安装包

07 SonicWall 称 Gen 6 防火墙不再提供安全补丁

2026年11月20日，SonicWall 发布产品公告，称 Gen 6 防火墙已结束支持，不再发布固件更新与安全补丁，无论新发现漏洞的严重程度如何。

**受影响：**SonicWall Gen 6 防火墙

**官方处置：**公告要求用户迁移至受支持机型。

08 SBC Medical 披露两起安全事件，约 162 万人数据受影响

2026年11月19日，SBC Medical Group 向美国 SEC 提交文件，披露两起网络安全事件共影响约 162.4 万人，泄露数据含姓名、出生日期、密码与医疗信息。

**受影响：**SBC Medical Group 患者与客户记录

09 CISA 发布 libumqtt 整数下溢漏洞公告，暂无修复版本

2026年11月19日（美国时间），CISA 发布 ICS 公告 ICSA-26-323-03，libumqtt 1.1.1 及更早版本存在整数下溢漏洞 CVE-2026-125132，CVSS 3.1 为 8.6。

公告称远端攻击者可造成拒绝服务、内存破坏或信息泄露，维护者未回应 CISA 的协调请求。

**受影响：**libumqtt 1.1.1 及更早版本

**官方处置：**公告标注暂无修复版本。

10 RansomwareHelp 联合创始人被控电汇欺诈

2026年11月20日，Krebs on Security 报道，数据恢复公司 RansomwareHelp 联合创始人兼 CTO Juan Ricardo Palacio Escobar 在罗德岛被控电汇欺诈。

起诉书称该公司向勒索团伙购买解密密钥后向受害者加价收费；FBI 设局中，其向虚构勒索团伙支付约 6000 美元，向虚构受害企业收取 16010 美元。

信源

1. 安全内参/奇安信 CERT https://www.secrss.com/articles/95792

2. 安全内参/奇安信 CERT https://www.secrss.com/articles/95820

3. php-src 安全公告 https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp

4. 安全内参/白泽安全实验室 https://www.secrss.com/articles/95800

5. 安全内参 https://www.secrss.com/articles/95838

6. AP https://apnews.com/article/cyberattack-european-union-artificial-intelligence-ai-79705095e8141cd650196dbff1cf3c70

7. CISA KEV https://www.cisa.gov/known-exploited-vulnerabilities-catalog

8. 安全内参/奇安信 CERT https://www.secrss.com/articles/95832

9. 安全内参/国家计算机病毒应急处理中心 https://www.secrss.com/articles/95819

10. The Hacker News https://thehackernews.com/2026/11/sonicwall-warns-gen-6-firewalls-wont.html

11. SonicWall 产品公告 https://www.sonicwall.com/support/notices/product-advisory-retire-unsupported-gen-6-firewalls/kA1VN000002iouP0AQ

12. BleepingComputer https://www.bleepingcomputer.com/news/security/hackers-steal-data-of-16-million-sbc-medical-group-customers/

13. CISA ICS 公告 https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-03

14. Krebs on Security https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/

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