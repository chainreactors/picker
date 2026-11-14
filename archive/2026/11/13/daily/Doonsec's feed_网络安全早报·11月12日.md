---
title: 网络安全早报·11月12日
url: https://mp.weixin.qq.com/s/rVUOIByu8UmgiKZJC65mUA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:19:20.309946
---

# 网络安全早报·11月12日

# 网络安全早报·11月12日

原创

安全早报
安全早报

Ncko

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 11 月 12 日 · 共 9 条

01在野利用N-able N-central 新利用链公开 4 小时后开始挖矿，19 台已装 Hotfix 2

11 月 12 日 03:58（UTC），研究者公开 4EverAble2Shell 与 Agent2Shell 两套利用代码。4EverAble2Shell 把 Apache Axis 的 CVE-2026-90436 与 N-central 本地提权缺陷串成一条链，未认证即可在服务器上以 root 执行命令。

huntback 蜜罐在 08:30 收到首个探测，09:16 收到完整利用请求：先以 nable 用户执行代码，再经 nable\_wrapper.pl 提权到 root，最后安装 XMRig 门罗币挖矿程序，主机名统一为 nc\_加受害者 IP。12:50 矿池中列出 21 台 nc\_ 主机，全部运行 N-central 登录页，其中 19 台版本为 2026.4.1.26，即 11 月 10 日发布的 2026.4 Hotfix 2。

**受影响：**N-central 2026.4，含 Hotfix 2（build 2026.4.1.26）；利用要求启用 Legacy API。另据 The Hacker News，Agent2Shell 以已知设备 ID 为前提，可在纳管 Windows 终端上以 NT AUTHORITY\SYSTEM 执行命令。

**官方处置：**N-able 11 月 12 日 07:00（UTC）开启事件通告，要求已启用 Legacy API 的本地部署客户立即关闭，其余客户确认 Legacy API 处于关闭状态；Hotfix 2 仍须安装。

02高危Citrix 修复 NetScaler 28 个内存漏洞，两个 9 分以上，默认配置即受影响

11 月 12 日，Cloud Software Group 为 NetScaler ADC 与 NetScaler Gateway 发布安全公告，共修复 28 个内存类缺陷。CVE-2026-120868 评分 9.3，位于核心数据包处理路径，不需要特定功能或认证，官方称默认配置的部署同样受影响。

CVE-2026-107412 评分 9.5，覆盖多个内存溢出问题，影响配置为 Gateway（SSL VPN、ICA Proxy、CVPN 或 RDP Proxy）或 AAA 虚拟服务器的设备，官方称无需认证即可触达。其余漏洞涉及 SAML、WebAuth、LDAP、邮件 OTP、客户端证书认证，以及 DNS-over-HTTPS、HTTP/2、HTTP/3（QUIC）、SMPP、RTSP、BGP 与应用防火墙。Citrix 称未发现利用，也未确认公开 PoC。

**受影响：**NetScaler ADC 与 NetScaler Gateway 14.1 before 14.1-73.57；13.1 before 13.1-64.39；NetScaler ADC FIPS before 14.1-73.58 FIPS；FIPS 与 NDcPP before 13.1-37.293。

**官方处置：**升级到对应修复版本，公告编号 CTX697305；CERT-EU 建议优先升级互联网暴露的 Gateway 与 AAA 设备。

034,837 个 GitHub 账号被用于投放 CI 窃密脚本，至少 1,806 个仓库外传凭据

OX Security 11 月 12 日披露 wfx-loot 行动：攻击者持有 4,837 个 GitHub 账号的凭据，先以“docs: dependency audit notes”为标题开探测性 PR 确认写权限，再推一条伪装成 CI 维护的恶意提交，数秒到数分钟后回滚，并删除 workflow 运行记录与日志，只留下运行编号的空缺。

被注入的脚本约 1,500 行、未做混淆，通过 GitHub Actions 与 npm postinstall 钩子执行，收集 GitHub 令牌、AWS/Azure/GCP 凭据、npm/PyPI/Packagist/crates.io 发布令牌、Kubernetes 与 Vault 密钥、AI 供应商 API Key。累计开出 66,200 多个探测 PR，8,093 个公共仓库默认分支收到恶意提交，至少 1,806 个仓库实际执行并外传。11 月 12 日 05:30（UTC）起，外传通道由 HTTP 改为 5 个 Telegram bot；当日新增 4,100 多个探测 PR。

**受影响：**自 11 月 10 日起攻击者账号可写或具协作权限的仓库，含至少 50 个可向 npm、Go、Packagist、PyPI、crates.io 发布包的账号；10,431 个探测 PR 指向账号本身不拥有的仓库，其中 28 个 WebdriverIO 仓库经项目 bot 账号触达。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeVqqZDZdD6hhs4qLosCGNb2wekJqetuhQSzFJJP7sIKaicsISunBBlGYdiaEQEXuZDM3XUYMyyCAiaaNpTz5dmaQ1BJqvSk5le0SA/640?from=appmsg)

图：OX Security 2026-11-12 报告配图

04ScreenConnect 第三方扩展被滥用，288 台终端被装冒名客户端

Huntress 11 月 12 日披露，入侵者使用多个云托管 ScreenConnect 面板的权限，向纳管端点批量下发命令，约 90 分钟内在 48 家机构的至少 288 台主机上安装攻击者控制的 ScreenConnect 客户端；约三分之一主机在最初 10 分钟内被触及。

Huntress 将入口定位到 RMM+ 扩展。该扩展可绕过 ScreenConnect 的账号、角色与 MFA，改用共享访问密钥认证；1.0.31 与 1.0.32 版本中密钥默认留空，认证检查不拒绝空值。落地工具被称为 SCKit，会停用正常客户端并复用其代码库，使机器“看起来正常”，另带会话 Cookie 窃取与重放代码。

**受影响：**安装 RMM+ 等第三方扩展的 ScreenConnect 合作伙伴环境及其客户端点；ConnectWise 表示私有云与本地部署面板不在本次处置范围。

**官方处置：**ConnectWise 已在约 400 个合作伙伴环境停用 5 个第三方扩展，其中包含 RMM+；公告称初步评估为第三方扩展被滥用，未发现 ConnectWise 基础设施被入侵或 ScreenConnect 本身存在漏洞，初始访问方式与完整范围仍在调查。

05Silent Lynx 用 AI Agent 对中亚政府开展间谍活动，塔吉克斯坦铁路网络被长期控制

CloudSEK 11 月 12 日发布报告，称在一台暴露的 Silent Lynx 服务器上发现逾 10GB 数据，包括窃取的政府文件、攻击工具，以及操作者使用 AI Agent 的记录。该 Agent 为开源项目 Hermes，按“进攻性网络安全专家”配置，主要调用 DeepSeek 模型，承担侦察、取数与清除痕迹，部分破坏性命令被设为无需二次确认即执行；操作者用俄语下指令，并通过 Telegram bot 远程控制。

报告称该组织至少从 8 月中旬到 10 月初保持对塔吉克斯坦国家铁路网络的访问，取得多台服务器、含登录凭据的数据库与内部文件；又用一名铁路员工的凭据登录该国国家电子公文平台，批量下载 2026 年发往或经国防部处理的数千份文件，涉及国民警卫队、国家安全委员会、国家投资委员会，以及 100 多个政府机构及其人员。另发现乌兹别克斯坦 Smart Forestry 平台的一台服务器被入侵，服务器上还有伪装成土库曼斯坦铁路车票与地方政府报告的恶意文件。

**受影响：**塔吉克斯坦国家铁路网络、国家电子公文平台，乌兹别克斯坦 Smart Forestry 平台，以及相关政府部门与人员；CloudSEK 以中等置信度评估该组织与哈萨克斯坦有关联，未认定与哈萨克斯坦政府有关。

06Operation Endgame 新一轮行动关停 235 台服务器、257 个域名

11 月 12 日，Europol 与保加利亚、加拿大、丹麦、德国、摩尔多瓦、荷兰、波兰、英国、美国的执法机构及 Eurojust 联合行动，关停 Gootloader、CastleRAT、StealC 三类恶意软件的基础设施，共处置 235 台服务器与 257 个域名。

其中 Gootloader 关停 14 台服务器、218 个域名，修复 681 个被感染网站；CastleRAT 查扣 120 台服务器、39 个域名；StealC 拆除 102 台服务器。行动中在犯罪基础设施内识别出 640 万条受害者凭据，这些凭据此前被用于出售并支撑后续勒索攻击。

**受影响：**三类恶意软件的犯罪基础设施与投放链；被 Gootloader 通过被入侵 WordPress 站点投放的仿冒法律文书感染的主机。

**官方处置：**Europol 称受害者数据将通过 Have I Been Pwned、DIVD、CheckjeHack、NoMoreLeaks、Sekoia、Shadowserver 与荷兰 NCSC 提供查询；公告要求 WordPress 用户更换凭据、启用多因素认证并修补漏洞。

07台积电证实员工资料外泄，数据来自第三方云服务供应商

台积电 11 月 12 日证实，部分现职与离职员工的信息未经授权被放置于外部网站。公司称初步比对显示这些信息与其某家云服务供应商系统中的数据相符，目前没有证据显示台积电自身信息系统遭到入侵，外泄数据与公司生产及客户信息无关。

有攻击者此前在 DarkForums 与 BreachForums 出售约 46,000 条记录、合计 6.9GB，要价 3 BTC，挂单时约合 22 万美元。台积电未确认记录数量与售价。

**受影响：**部分现职及离职员工的个人信息；承载这些数据的第三方云服务供应商系统。

**官方处置：**台积电称已按程序处理该事件，并说明生产运营与客户信息未受影响。

08周生生在港交所公告系统遭未经授权存取，客户与员工资料可能被提取

11 月 12 日晚间，周生生集团国际有限公司（00116.HK）在港交所发布内幕消息公告，称集团近日发现系统遭受未经授权存取，并于 2026 年 11 月 9 日首次识别该事件，客户及员工的资料可能存在被提取的情况。

公告称集团已着手遏止所有未经授权存取行为、加强系统安全性，并委聘网络安全专家进行调查。公告未披露被访问系统的具体范围、涉及人数与数据类别。

**受影响：**周生生集团部分客户与员工的个人资料。

**官方处置：**公告称调查仍在进行，集团将在适当时候按上市规则作进一步公告。

09香港崇光百货会员系统被读取，私隐公署称或影响约 82 万名会员

11 月 12 日，香港崇光百货表示，今年 11 月发现会员系统曾遭未经授权人士取得部分资料。根据现阶段调查结果，受影响资料主要涉及部分会员号码、姓名、联络电话、电邮及会员积分资料。

香港个人资料私隐专员公署当日回复查询称，已接获该机构的资料外泄事故通报，初步资料显示崇光百货于 11 月 5 日发现会员系统出现不正常的资料读取纪录，事故可能影响约 82 万名会员的个人资料。

**受影响：**崇光百货会员系统，涉及会员号码、姓名、联络电话、电邮与会员积分资料，公署估计约 82 万名会员。

**官方处置：**崇光百货称已立即展开全面调查及跟进，并向相关政府部门作出通报，正配合有关调查。

信源

huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers

status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/

cert.europa.eu/publications/security-advisories/2026-020/

support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697305

ox.security/blog/thousands-of-github-accounts-hijacked-with-wfx-loot-ci-secret-stealing-malware-via-github-actions-npm/

cyberscoop.com/connectwise-screenconnect-sckit-attack/

thehackernews.com/2026/11/screenconnect-attacks-target-at-least.html

therecord.media/kazakhstan-hackers-central-asia

europol.europa.eu/media-press/newsroom/news/64-million-victim-datasets-secured-in-international-operation-against-malware-networks

cj.sina.com.cn/articles/view/3057540037/b63e5bc502001vs3i

hkexnews.hk/listedco/listconews/sehk/2026/1112/2026111201493\_c.pdf

finance.sina.com.cn/stock/estate/integration/2026-11-12/doc-iniyniff3899461.shtml

stheadline.com/zh-hans/society/3636457/

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