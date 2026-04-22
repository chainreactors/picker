---
title: 因第三方AI工具受陷，Vercel 内部系统遭未授权访问
url: https://mp.weixin.qq.com/s/0HD680654m8Grim_rh23dQ
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:41:54.083673
---

# 因第三方AI工具受陷，Vercel 内部系统遭未授权访问

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# 因第三方AI工具受陷，Vercel 内部系统遭未授权访问

DevOpsDaily Team
DevOpsDaily Team

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)

编译：代码卫士

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

**2026****年 4 月 19 日，Vercel 披露了一起涉及内部系统未授权访问的安全事件。该攻击的源头并非 Vercel 自身，而是因一名 Vercel 员工使用的第三方 AI 工具 Context.ai触发，随后通过一个被入侵的 Google Workspace OAuth 应用进行传播，最终进入 Vercel 的内部环境以及部分客户的环境变量。**

这是一起供应链攻击事件，但这里的“供应链”并非指代码或 npm 包，而是指企业员工用 Google 账号登录的那些 SaaS 应用。本文将说明事件经过、如何判断自己是否受影响，以及需要做出哪些改变。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXibMnRMw3t8w5kfcx61v8Oj2z1YRD0micS5zDcD1qONiaGRFHhrGm7tmHnqftk0C8xpA96aT4SiadaSfPnnW4xsyqZ5BXHSDiaAvl0/640?wx_fmt=gif&from=appmsg)

**攻击时间线**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVJDOXbBf3S1Ixd7HCiaiaPFib9iandRJlgjUCmBo5q0HwxgYa7xQFx1BovHyKnS0UqP239TMUewb0UY9cTibmOcc81OaXKWMgjs1Ys/640?wx_fmt=gif&from=appmsg)

这条攻击链的完整过程值得了解，因为它揭示了现代“供应链”入侵越来越多地通过身份提供商（而非代码）进行传播的典型路径。

**1、****2026****年3月：Context.ai 发生 AWS 入侵事件。**Context.ai 是一家 AI 工具创业公司。该公司在 3 月份披露称 AWS 基础设施遭入侵，并聘请 CrowdStrike 公司代为调查。

**2、****OAuth****令牌被盗，但未被标记为异常。**AWS 入侵事件还暴露了 Context.ai 为 Google Workspace 集成所持有的 OAuth 令牌。调查显然未能发现这一点。

**3、****一名 Vercel 员工使用了 Context.ai。**该员工此前通过 OAuth 授权 Context.ai 访问其 Google Workspace——就像授权任何需要读取邮件、文件或日历的第三方 SaaS 应用一样。

**4、****攻击者重放了令牌。**凭借有效的 OAuth 令牌，攻击者可以冒充 Context.ai 应用，并访问该 Vercel 员工的 Google Workspace 账户。当已预先授权的 OAuth 应用调用 Google API 时，不会触发密码或多因素认证 (MFA) 提示。

**5、****横向移动进入 Vercel 内部系统。**攻击者从该 Workspace 账户出发，通过一系列权限提升操作最终进入了 Vercel 的内部环境。

**6、****访问客户的环境变量。**进入内部后，攻击者能够读取 Vercel 平台上那些未被客户标记为“敏感”的环境变量。Vercel 对所有静态环境变量都进行了加密，但标记为“敏感”的环境变量即使对 Vercel 内部员工也不可见，因此未受到影响。

Vercel 检测到了异常活动，聘请 Mandiant 公司介入调查并通知执法机构，并于 4 月 19 日进行了公开披露。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXtk6kH4ZhadLI0z3CyI6nJwZeYwvHUycqLJIdMObpR6qv03hd9DEtafmy0S6ayBJXqJqzemY54PonSuPibIHYh2xp31VkeAtRY/640?wx_fmt=gif&from=appmsg)

**已暴露（及未暴露）的内容**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVX8QXMMDwPsoHh9vaTwj8X0dAXlntVLnicer2AMEcnib2LO1Y1NXUXQB7IN5J8ibiba63E2Ff6AJz5DPZeuLm4tXGGMZaXeus5VQY/640?wx_fmt=gif&from=appmsg)

**Vercel****官方确认的情况**

攻击者可能访问了以下内容：

* “一小部分客户”的 Vercel 凭证
* 客户项目中未标记为“敏感”的环境变量
* 客户项目中的 Deployment Protection 令牌
* Vercel 的各类内部系统和工具

攻击者**未能**访问以下内容：

* 标记为“敏感”的环境变量（即使 Vercel 员工也无法查看）
* 所列子集之外的任何客户数据（Vercel 已直接联系受影响客户）
* Vercel 的构建/运行基础设施本身

在整个事件发生期间，Vercel 服务始终保持正常运行。Vercel 的公共边缘网络、构建系统以及部署并非攻击面。

**攻击者的说法**

安全研究员 @k1rallik 在一条推文中声称，该威胁行为者是 ShinyHunters（即 2024 年 Ticketmaster 数据泄露事件的幕后组织），提到BreachForums 论坛正在以200万美元的价格出售 Vercel 内部数据库的副本。据称该数据列表包含属于 Vercel 的 NPM 令牌和 GitHub 令牌。该研究员还声称 Vercel 通过 Telegram 直接联系了攻击者。

**这一点尚未得到 Vercel 的官方确认。**应将这一说法视为社区信号，而非既定事实。但其中隐含的风险值得认真对待：如果用于发布 Vercel 所维护包的 NPM 令牌被盗，最坏的情况下，next、@vercel/next、@vercel/analytics 或任何其它由 Vercel 发布包的恶意版本将出现在 npm 上。仅 Next.js 每周就有约 600 万次下载，这将使其成为一场教科书式的全球供应链攻击，与最近 axios 被入侵事件形态类似。

如果 Vercel 确认或否认令牌被盗，我们后续将更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfW6ibEIMAZ6qS64tqYnoN1b6M9ibbnRoicdxpkWp3PFkmzcPIxmLGTS9cmjs3kGrI5O9YKakHcl7ias7iaDJpxpavicRV76suBdJbbCk/640?wx_fmt=gif&from=appmsg)

**如何判断是否受影响？**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXyRib5esnEp4x348m8PP9l1eDMRuPIEPX6DDKrDs5uuaFGibbpHHAEibcjNrrVYsxbeb899AME9LZpuWuLno33gDdCASuwpl5icQg/640?wx_fmt=gif&from=appmsg)

Vercel 已直接联系了受影响的客户。Vercel 表示，如果未收到通知，则说明没有发现账户被入侵的证据。话虽如此，更为稳妥的做法是自行核实。

**检查通知**

1、在与 Vercel 账户所有者关联的收件箱中，查找日期在 2026 年 4 月 19 日前后来自 Vercel 的邮件。

2、检查 Vercel 仪表板中是否有横幅通知或应用内通知。

3、搜索垃圾邮件 / 隔离文件夹。

**审计账户活动**

```
# In the Vercel dashboard:# Settings → Security → Audit Log
```

查找不熟悉的情况：

* 自身未触发的部署
* 新的团队成员或项目邀请
* 令牌创建或 SSH 密钥添加
* 环境变量变更
* 域名或 DNS 设置变更

需特别关注 2026 年 4 月初到审计之日期间的活动。

**检查近期的部署**

```
# Vercel dashboard → Project → Deployments
```

对于自 4 月初以来的每个生产部署，需验证：

* commit SHA 与 Git 历史记录一致
* 构建日志不包含异常命令或输出
* 部署由已知用户或 CI 流水线触发

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUuYJVDbicSxe0rmaQcj20x0Q7XcAc8wt4TtgeeC1BA1nBXxkmiaOJpGGfHpDzNcMkjIiabF4iaNcebScN8CnCcjcT9tvcZtIm4nds/640?wx_fmt=gif&from=appmsg)

**如受影响，如何修复？**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXa3qgVENmtP53Z89GjEhmjH89uJcpxiaklIMGxE1309T8yQVRW0ZtufKpp2Wc90B4hZw1ThmcCWwB9aefOzaDd7K7PbIaPpK3I/640?wx_fmt=gif&from=appmsg)

如果收到 Vercel 的通知，或审计发现了任何可疑情况，需假定自己的非敏感环境变量已被读取，并采取相应措施。

**1、****更换所有曾经存在于非敏感环境变量中的密钥**

包括：

* 第三方 API 密钥（Stripe、OpenAI、Sentry、PostHog、Resend 等任何服务）
* 数据库连接字符串和凭据
* OAuth 客户端密钥和 webhook 签名密钥
* 内部服务间通信令牌
* 任何其它以普通环境变量（而非敏感环境变量）存储的凭据

如有可能，需在原处更换。否则，需发布新凭据、完成部署，再撤销旧凭据。

**2、****更换 Deployment Protection 令牌**

```
# Vercel dashboard → Project → Settings → Deployment Protection → Rotate token
```

如攻击者获得 Deployment Protection 令牌，就可绕过预览部署的保护措施。

**3、****将 Deployment Protection 至少提升到 Standard 级别**

如果受影响项目上的 Deployment Protection 之前设置为 None 或低于 Standard 级别，需提升，以防止未来对预览 URL 的未授权访问。

**4、****后续采用敏感环境变量**

Vercel 为每个变量提供了一个“敏感”标志。敏感值：

* 仅能被运行中的部署读取，仪表板、CLI 或 Vercel 员工均无法查看
* 不会包含在构建日志中
* 设置后无法再被查看

需将所有机密（密钥、令牌、密码）都移至敏感环境变量。将非敏感变量留给真正非秘密的配置使用，例如功能开关、区域名称或公共 URL。

```
# When adding a new env var in the dashboard, check the# "Sensitive" checkbox. For secrets, always.
```

**5、****重新构建并重新部署**

更换完成后，触发一次干净的重新部署，以便新值生效，旧值仅作为旧构建中的无效引用存在。

**6、****锁定Next.js 和 Vercel 发布的 npm 依赖**

如果使用 Next.js 或任何由 Vercel 发布的包（next、@vercel/\*、@next/\*），需在 Vercel 官方确认没有发布令牌被泄露之前，在 lockfile 中将其锁定到已知安全的版本：

```
# See what you have lockedgrep -E '"next":|"@vercel/|"@next/' package.json package-lock.json yarn.lock pnpm-lock.yaml 2>/dev/null# In CI, use clean installs that respect the lockfile exactlynpm ci# orpnpm install --frozen-lockfile# oryarn install --frozen-lockfile
```

如不需要，可在 CI 中对不受信任的依赖项禁用 postinstall 脚本：

```
npm ci --ignore-scripts
```

在 4 月 19 日到 Vercel 宣布风险解除这段时间内，监控 npm 上 next 包的发布动态，留意任何非预期的版本发布。在此时间窗口内出现的任何计划外补丁版本都是一个危险信号。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfV30sOE8IGH2dicHlG3Rw2iaT0pQYFcIR2AF7pxicOVucRnFlEmZCbZibyPrEgNhQQtAhib2eDWARtwZKLeyHvfpMiaS0kEZfibKE6wlg/640?wx_fmt=gif&from=appmsg)

**如何防范类似攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWjRMwknFJKA9RzegyljSqcoXXqvfRNGQ9KPbxmbljzkTGdFibdLrva1rBSOIQsDiaoq1SWt6CVCjZwC3IzOJCWf42BWxFHgcFdA/640?wx_fmt=gif&from=appmsg)

类似攻击还会再次发生。它是一种模式，而非孤立事件。无论是否使用 Vercel，都应在所在组织内做好以下加固措施。

**1****、将 OAuth 应用授权视为访问控制**

团队接受的每一个“使用 Google 登录”授权，都是一条进入身份提供商的持久访问路径。大多数组织从不审计已经授权了哪些应用。

```
# Google Workspace admin: Security → Access and data control →#   API controls → App access control → Manage Third-Party App Access
```

检查列表。撤销任何无人认识的授权。将高价值范围（Drive、Gmail、日历的读写权限）纳入显式白名单，这样员工就无法静默地授权新应用读取公司数据。

GitHub 也有类似的审查页面，用于查看已获得所在组织授权的 OAuth 应用。

**2****、在每个 OAuth 集成上最小化权限范围**

将第三方 SaaS 应用连接到 Workspace 或 Microsoft 365 时，需检查权限范围列表。如果某个应用只应该读取日历，却请求 https://mail.google.com/（完整的邮件访问权限），则应拒绝。但大多数员工会接受任何被请求的权限。

**3****、默认将每个密钥标记为敏感**

不仅仅是在 Vercel 上这样做。在每个类似平台上都应如此：

* Vercel：敏感环境变量
* AWS：Secrets Manager，绝不要在可通过 kubectl get 访问到的 Lambda 上使用明文环境变量。
* GitHub Actions：加密密钥，不要在工作流的 YAML 中使用明文环境变量。
* Kubernetes：至少使用 Secret 对象，在理想情况下使用密封的 Secret 或由 Vault 支持的External Secret Operator。

这里需要秉持的一个原则是，秘密永远不应被仪表板、日志或人类管理员读取，只能被运行时需要它的进程读取。

**4****、监控 Google Workspace 中的异常令牌使用情况**

Workspace 会记录每次 OAuth 应用令牌的访问。用户可针对以下情况设置告警：

* 一个超过 30 天未使用的 OAuth 应用令牌突然激活
* 来自异常地理位置或 IP 的令牌使用
* OAuth 应用在短时间内大量读取文档或邮件

这类活动本可更早地发现本次事件中的令牌重放。大多数组织拥有这些日志，但没有为其配置任何告警。

**5****、制定涵盖“供应商被入侵”场景的应急计划**

不应等待事情发生了才开始行动，应提前写好：

* 当某个供应商披露入侵事件时，所在团队中的联系人是谁。
* 哪些密钥需要按什么顺序更换（通常是：身份提供商优先，其次是支付/计费，然后是产品 API）。
* 如果事件影响到客户，如何与他们沟通。
* 更换操作手册存放在哪里。

每年通过一次桌面演练来实践该计划。

![](ht...