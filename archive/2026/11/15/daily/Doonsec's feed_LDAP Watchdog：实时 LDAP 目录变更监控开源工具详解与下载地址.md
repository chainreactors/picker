---
title: LDAP Watchdog：实时 LDAP 目录变更监控开源工具详解与下载地址
url: https://mp.weixin.qq.com/s/gbXKSMBpGF_cj9RakCiXVQ
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:47:06.276995
---

# LDAP Watchdog：实时 LDAP 目录变更监控开源工具详解与下载地址

# LDAP Watchdog：实时 LDAP 目录变更监控开源工具详解与下载地址

原创

播风者
播风者

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MXHq6ONC1gj3L6LQ1h18Jb4x6mtdne19qbtIcyPuKeDpyGibdMRycbsXHKMZQOlCsvYhaSfr5icXuS25Ztys6VNkBPAiaD34jE7I/640?from=appmsg)
> **导语**：安全研究员 Joshua Rogers 维护的 LDAP Watchdog 于 2026 年 10 月 30 日更新至 v2.0.1，这是一款面向 Linux/OpenLDAP 的实时目录变更监控工具，能够捕获用户与组条目的新增、修改、删除，并可将告警实时推送到 Slack。适合需要审计目录变更、发现异常账号改动的运维与安全人员。

---

## 工具标识与风险速览

| 项目 | 内容 |
| --- | --- |
| 工具名称 | LDAP Watchdog（仓库名 LDAP-Monitoring-Watchdog） |
| PyPI 包名 | LDAP-Monitor（当前 2.0.1） |
| 作者 | Joshua Rogers（GitHub: MegaManSec） |
| 语言 / 许可 | Python / GPL-3.0 |
| 运行环境 | Python 3.10+，依赖 ldap3（Slack 通知需 requests） |
| 适配平台 | OpenLDAP（Linux）、需服务端为每条目提供 `entryUUID`（RFC 4530） |
| 不支持 | Active Directory（使用 `objectGUID`，无 `entryUUID`） |
| 最新版本 | v2.0.1（2026-10-30），v2.0.0 同日发布 |
| 仓库活跃度 | 197 star / 17 fork，最近提交 2026-11-08 |
| 官方来源 | GitHub 发布方为 KitPloit Hacker Tools 收录转发 |

**定位：🟡 防守侧辅助工具**。它本身不是漏洞利用工具，价值在于给"目录服务发生了什么"提供可追溯的日志与实时通道，用于事后取证和账号生命周期审计。

## 工作原理

LDAP Watchdog 采用**轮询快照比对**模型，而非 LDAP 目录的原生变更通知。每经过一个刷新周期（默认 60 秒）执行一次 LDAP 搜索，抓取全部目标条目的属性快照；下一次抓取后与上一次快照逐条对比，输出新增（Added）、修改（Modified）、删除（Removed）三类差异。

默认搜索过滤器为 `(&(|(objectClass=inetOrgPerson)(objectClass=groupOfNames)))`，默认拉取属性为 `*,+`（含操作属性，因此能拿到 `modifyTimestamp` 等时间戳，用于判断登录时间）。所有变更始终打印到终端，配置 Slack Webhook 后同步推送。

![LDAP 监控流水线示意](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NZO70rXic3wLbrClWzuLGLoLeq2H0flBvXianlPCuF5IBL1wLDHlB0UEelMVq2GQbMicL0hbTFdzUH7G5ia9Z7W1UhGaib48ROJffo/640?from=appmsg "LDAP 监控流水线示意")

三个设计细节值得运维人员注意：

**控制用户校验（Control User）。** 可指定一个控制账号的 `entryUUID`，由外部 cron 在每次轮询前修改该账号的某个属性。若在两份快照中未观察到该属性发生变化，本次比对结果会被判定为不可信并直接丢弃，同时抛出错误。这防止了攻击者或故障导致"快照被替换"时产生漏报或伪造告警。控制账号需同时满足基准 DN 与搜索过滤器条件。

**忽略规则。** 支持按 `entryUUID` 忽略整个条目、按属性名忽略（如 `entryCSN,modifyTimestamp` 噪音），也支持条件忽略——只有当属性变化涉及特定值时才忽略（例如忽略 `memberOf` 中某个固定组的变更）。

**Slack 推送为尽力而为。** HTTP 或网络失败只记 stderr 日志，不排队重试。超过 4000 字符的消息会先按最长单词替换为 `[...truncated...]`，仍超长则按"新增→删除→修改"的顺序从尾部截断；终端输出永不截断。

## 部署方式

工具提供三条路径，生产环境建议优先 systemd 方式。

**PyPI 安装：**

```
pip install LDAP-Monitor            # 基础功能
pip install "LDAP-Monitor[slack]"   # 含 Slack 通知支持
```

**Docker 部署：**

```
docker pull megamansec/ldap-monitor
# 或 GitHub Container Registry
docker pull ghcr.io/megamansec/ldap-monitoring-watchdog
```

**源码 + systemd（Debian 系）：**

```
git clone https://github.com/MegaManSec/LDAP-Monitoring-Watchdog.git
cd LDAP-Monitoring-Watchdog
sudo ./install.sh "https://hooks.slack.com/services/[...]"
```

`install.sh` 会创建 `/opt/ldap-watchdog` 虚拟环境并按 `requirements.txt` 锁定依赖版本，生成 `/etc/ldap-watchdog.env` 环境文件，注册 `/etc/systemd/system/ldap-watchdog.service`（以非特权动态用户运行）、配置 `/var/log/ldap-watchdog.log` 与日志轮转。重复执行即为升级。

![Linux 服务器部署与目录树监控](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NTfHCx9NKbibwfbMBguoPFuMjbhGyQhL53bdicdwfRnyH2IrPibY2H8Oh0m9JFVeBt9atL4ZwG95qt5HpAv3uI2SXicgWDx1rfbEo/640?from=appmsg "Linux 服务器部署与目录树监控")

## 配置要点

全部配置通过环境变量完成，核心几项：

| 变量 | 说明 | 默认值 |
| --- | --- | --- |
| `LDAP_WATCHDOG_SERVER` | 服务地址，如 `ldaps://ldaps.intra.lan` | 必填 |
| `LDAP_WATCHDOG_BASE_DN` | 搜索基准 DN | 空 |
| `LDAP_WATCHDOG_USERNAME` / `LDAP_WATCHDOG_PASSWORD` | 绑定账号与口令，留空则匿名绑定 | 空 |
| `LDAP_WATCHDOG_USE_SSL` | 是否启用 LDAPS（636），`ldaps://` 前缀可覆盖 | `true` |
| `LDAP_WATCHDOG_CA_CERTS_FILE` | 私有 CA 的 PEM 证书包路径 | 未设置 |
| `LDAP_WATCHDOG_TLS_VERIFY` | 关闭证书与主机名校验 | `true` |
| `LDAP_WATCHDOG_SEARCH_FILTER` | 搜索过滤器 | `(&(|(objectClass=inetOrgPerson)(objectClass=groupOfNames)))` |
| `LDAP_WATCHDOG_SEARCH_ATTRIBUTE` | 拉取属性列表 | `*,+` |
| `LDAP_WATCHDOG_REFRESH_RATE` | 轮询间隔（秒） | `60` |
| `LDAP_WATCHDOG_NETWORK_TIMEOUT` | 单次 LDAP/Slack 操作超时（秒） | `30` |
| `LDAP_WATCHDOG_CONTROL_UUID` | 控制用户的 `entryUUID` | 空 |
| `SLACK_WEBHOOK_URL` | Slack 推送地址 | 未设置 |

## 版本升级注意

从 1.x 升级到 2.0.0：LDAPS 连接开始校验服务端证书并核对主机名/IP。1.0.0 两者都不查。若使用自签名或私有 CA 证书，需先设置 `LDAP_WATCHDOG_CA_CERTS_FILE`；名称对不上时只能换证书，或设置 `LDAP_WATCHDOG_TLS_VERIFY=false`——此时链路仍加密但不再认证服务端，路径上的任何节点都能冒充目录服务器并截获绑定口令。

从 1.x 或 2.0.0 升级到 2.0.1：布尔型配置只接受明确取值，非法值直接终止进程（不再静默当作 false）；空值等于默认；`on` 或带引号的 `"true"` 才视为真。旧版本把 `LDAP_WATCHDOG_USE_SSL` 留空时按明文 389 连接，新版本会按默认走 LDAPS 636，升级后需同步核对防火墙放行策略。

## 使用注意与局限

绑定账号应使用只读权限的最小化账号，不要给目录写权限，否则监控账号自身即成为攻击面。`SLACK_WEBHOOK_URL` 属于凭据，需通过 systemd 环境文件限制权限（默认仅 root 可读），并避免在 shell 历史或 CI 日志中明文暴露。

轮询模型决定了告警存在延迟，默认 60 秒轮询周期加上一次查询耗时；关键环境建议把 `LDAP_WATCHDOG_REFRESH_RATE` 调到 30 秒以内，但需评估目录服务器负载。另外该工具对 Active Directory 不兼容，AD 环境需改用 `objectGUID` 方案的替代工具。

## 下载地址

* GitHub 源码与发布页：https://github.com/MegaManSec/LDAP-Monitoring-Watchdog
* PyPI 安装包：https://pypi.org/project/LDAP-Monitor/
* Docker Hub：https://hub.docker.com/r/megamansec/ldap-monitor
* GitHub Container Registry：`ghcr.io/megamansec/ldap-monitoring-watchdog`
* 工具详情页（KitPloit 收录）：https://kitploit.com/en/tools/github/megamansec/ldap-monitoring-watchdog
* 作者技术博客：https://joshua.hu/ldap-watchdog-openldap-python-monitoring-tool-realtime-directory-slack-notifications

该工具最早名为 LDAP-Stalker，用于描述"监视公司里所有人的升职、加人、离职"。GPL-3.0 许可，二次分发需保留许可证声明。仅建议在自有或已获授权的环境中使用。

---

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OpxtFicINf2z1UT0Lx2RQtdmqEic7vicyWKMU2FH9iciaSYV3PXPKzRuN2Na6yJWR8Yahich66micPKLlpzx3HCoHGABvibuL68dD1JRY/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Nfj92htAhtm8l4IYBbyhT9jDvTW1ibdlBLzsV3mUd3M4rYrPag6Eiat5FuEOgNYzjPPglKNmJedYDHH9ZfficxU7gSCp3OIlN9HU/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MOPwicyXLSkQ8cbKicCnrdsciah067b8aHp93nQlGfXx2MabqEWyaBOrLqG8ImyTrXvzWN17XrH1nQL3IHW0LAWPxHyjPPhoqcDU/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N4UPhVPwWfX846uoUecVJeleiayF4dNGsTfLkVXaaicNICQIXk9s3VFibTdRnlmIiaV1PDHICMGo9Yiaf9BiaNNDwPf1tOCsTjLEtfg/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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