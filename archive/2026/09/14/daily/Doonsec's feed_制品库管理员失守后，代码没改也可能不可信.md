---
title: 制品库管理员失守后，代码没改也可能不可信
url: https://mp.weixin.qq.com/s/iRkYB_YmBvVu0iDdzMHhMA
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T07:01:32.550763
---

# 制品库管理员失守后，代码没改也可能不可信

# 制品库管理员失守后，代码没改也可能不可信

原创

tcode
tcode

字节脉搏实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHy15XIDF5vFnfrteOEUOL0mMxjIg52W6CsYhPiaYCF2xEiaIo8aZuqXDhkCqVoTpxyt8pM4JSPoa3ickYLe3xPANVYO0mxtCbj47Q/640?wx_fmt=png&from=appmsg)

    很多团队把制品库当成“内部工具”：不直接面向客户，页面也不起眼，平时只负责保存依赖、镜像和构建产物。Wiz 对 JFrog Artifactory 攻击活动的分析说明，攻击者看重的恰恰是这种位置。只要拿到制品库管理员权限，就不必逐个攻破开发终端，也能影响后续构建、发布和部署信任。

    Wiz 称，攻击者在 2026 年 8 月 15 日至 9 月 8 日间串联利用 CVE-2026-42018 和 CVE-2026-42016，从未认证访问拿到内部匿名用户令牌，再把低权限令牌交换成管理员范围令牌。后续观察到创建持久管理员账号、安装恶意 Groovy 插件、执行命令，以及投递 Rust 后门。CISA 在 9 月 11 日把 CVE-2026-42016、CVE-2026-42018 和 ConnectWise ScreenConnect 的 CVE-2026-84869 加入已知被利用漏洞目录。

    这篇与国内读者的关系要写得克制：公开报告没有点名中国受害企业，也没有证明国内实例已经失陷。但 Artifactory 是国内大量研发、外包、互联网和制造业团队常用的制品库与私有仓库组件。它连接代码仓库、CI/CD、镜像仓库和发布环境，一旦权限边界失守，影响的不是单个页面，而是整个软件交付链。

**攻击者为什么盯上制品库**

    制品库是企业软件供应链的“中转仓”。开发从外部拉依赖，构建系统把产物推上来，测试和发布流程再从这里取包。很多组织以为只要仓库在内网或 VPN 后面就安全，实际暴露面可能来自反向代理、临时调试端口、云安全组误放、外包共享链接，甚至一次为了排障而临时打开的公网访问。

    这次被串联的两个漏洞说明，攻击者并不总是直接找“远程命令执行”。CVE-2026-42018 让未认证调用者拿到内部匿名用户令牌；CVE-2026-42016 的问题在于校验令牌签名和发行者，却没有充分核对令牌允许的范围。两个缺陷组合后，低权限令牌被提升为管理员令牌，权限边界在系统内部被绕过。

    拿到管理员后，攻击者可以做三件对防守方很不利的事。第一，创建看起来像服务账号的持久管理员；第二，利用 Artifactory 插件机制运行代码，避免只依赖 webshell；第三，读取配置和令牌，向 CI/CD、制品、节点或云环境继续扩展。Wiz 提到部分样本名称带有明显测试痕迹，也有账号刻意伪装成 jfrog-distribution、jfrog-insight、repo-service 这类“像系统自带”的名字。

**补丁之后，最不能省的是取证**

    只升级版本只能切断后续利用，不能回答“过去有没有被拿到管理员”。Artifactory 的管理员账号、访问令牌、插件、任务和配置不会因为有补丁自动恢复原状。Wiz 报告明确指出，攻击者创建的管理员账号不会随着软件更新消失；Fastly 对另一项 Artifactory 漏洞的分析也提醒，补丁不会撤销已经签发的令牌。

    因此，排查顺序应先版本、后账号、再令牌和制品。先确认自托管实例所处分支是否已修复，云实例按 JFrog 说明处理；再导出所有管理员、服务账号、近期登录来源和令牌创建时间；随后检查插件目录、任务配置、系统配置变更和节点 join key 是否异常；最后再判断是否需要轮换 CI/CD 凭据、重新签名或重建发布产物。

    国内团队还要特别注意外包和多云环境。一个集团可能同时存在总部自建 Artifactory、子公司旧版本、云上测试仓库和外包临时实例。资产清单只写“研发平台一套”，很容易漏掉真正暴露在互联网上的边缘实例。对托管给供应商维护的系统，应要求对方提供版本、补丁时间、管理员审计和令牌轮换证明，而不是只回复“已升级”。

**今天可以执行的四项动作**

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHwicbIVyhvKfeOuqm3ScricCqjrNbP3Q3uFPJKRxYz8HRsCB2UlUqyVgm88brRQyFibTdvVYD5GdkOopDIFj1K63GRhJ04aLhbHes/640?wx_fmt=png&from=appmsg)

    第一，盘点所有 Artifactory 实例和公网入口。包括主实例、灾备、测试、项目制外包实例和反向代理暴露路径；把域名、IP、版本、负责人、是否允许匿名访问列清楚。没有负责人和更新记录的旧实例，先下线或限制到内网。

    第二，按固定分支核对 JFrog 官方安全公告中的修复版本。Wiz 指出 CVE-2026-42016 与 CVE-2026-42018 需要同时满足才可串联，但另一条 CVE-2026-82329 曾被单独利用，新版本分支也不能因此跳过检查。版本判断以 JFrog 公告为准，不凭“系统看起来新”下结论。

    第三，导出并复核管理员、令牌和插件。优先查找随机字符账号、类似 svc\_、labadmin\_、repo-service、jfrog-insight 的账号，检查令牌创建时间是否落在 8 月 15 日以后，以及是否有管理员在非工作时间登录。插件目录中出现未审批 Groovy 脚本，应按入侵事件处理。

    第四，把制品可信度重建为流程。发现异常账号或令牌后，轮换仓库、CI runner、镜像仓库、部署系统和云密钥；对关键发布产物，从可信源码重新构建并比对哈希。无法确认影响范围时，宁可暂停自动发布，也不要让“可能已经干净”的制品继续进入生产。

**一个可保存的诊断问题**

    每次制品库告警都可以先问：这个管理员、令牌或插件，能否对应到一条有审批、有负责人、有到期时间的变更记录？如果只能解释“可能是以前留下的”，就按未知高权限对象处理。

**证据边界**

    已核验事实包括：Wiz 报告的攻击时间窗、两个漏洞的串联机制、部分后渗透行为、CISA KEV 收录和 JFrog 安全公告入口。公开信息没有确认中国境内受害实例名单，也没有披露所有攻击者基础设施；本文不推断国内损失。它的结论是：制品库不是普通后台，而是软件交付信任链的一环，补丁必须与账号、令牌和制品完整性核查一起完成。

**热点来源**

    来源：Wiz，Artifactory under attack: in-the-wild exploitation of CVE-2026-42016 / CVE-2026-42018，2026-09；支持事实：8 月 15 日至 9 月 8 日攻击、串联机制、管理员账号、Groovy 插件和 Rust 后门。链接：https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201

    来源：CISA，CISA Adds Three Known Exploited Vulnerabilities to Catalog，2026-09-11 12:00 UTC；支持事实：CVE-2026-42016、CVE-2026-42018 被加入已知被利用漏洞目录。链接：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog

    来源：JFrog，Security Advisories；支持事实：受影响版本、修复版本和云实例处置说明。链接：https://docs.jfrog.com/releases/docs/jfrog-security-advisories

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia3Is12pQKnIPvX43Bm5RTfn38gGrVIvGtiaMrLfFqknYBzOd4wmQb1Ra7InwkMM5Ru09FTZ6ibhcLiagpiannxZdlA/0?wx_fmt=png)

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