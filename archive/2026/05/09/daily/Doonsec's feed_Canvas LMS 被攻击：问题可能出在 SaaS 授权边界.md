---
title: Canvas LMS 被攻击：问题可能出在 SaaS 授权边界
url: https://mp.weixin.qq.com/s/gEv3-aZ3_xWjKPVjduA6HA
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:30:06.136414
---

# Canvas LMS 被攻击：问题可能出在 SaaS 授权边界

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XXmXKfaNf4qRASx5OibPwyMdSYc01LjJnfWuLn9QTSxCE1X20VTs9uQAIgV9bUH23EP0d8pD7v7bIKJrz4AGczPuqh5F9TYNZj4z9ljSZZ58/0?wx_fmt=jpeg)

# Canvas LMS 被攻击：问题可能出在 SaaS 授权边界

原创

XueMian
XueMian

雪面科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Canvas LMS 被攻击

# 问题可能出在 SaaS 授权边界

* 写于：2026-05-09（澳大利亚布里斯班时间，AEST/UTC+10）
* 对象：Instructure Canvas LMS，不是 Canva 设计平台
* 置信度：中高。Instructure 还没公开完整 root cause，具体利用细节不能写死。

> “
>
> **声明**：截至本文写作时，Instructure 尚未公开完整 root cause。本文不是官方事故复盘，而是基于公开报道 [1], [2], [4], [5], [7]、厂商状态页 [6]、学校公告 [8], [9]、论坛线索 [3]，以及我个人安全分析经验做出的判断和推测。后续如果官方披露更多技术细节，文中的归因和漏洞分类应以新证据为准。

## 先说结论

    先把名字说清楚：这里的 Canvas 是 Instructure 的 LMS 教学平台，不是 Canva 设计平台。这两个名字太像，网上已经有不少混淆。

![](https://mmbiz.qpic.cn/mmbiz_png/XXmXKfaNf4pkPPf9u5dQRQUyXuibatkcvIWGPur7KIwqSd1dmslSO5JtL9RUIg5TT0vmTe5gfOVVmTf07VHJBUyG07vOxjyIqIRcWkk8xtk4/640?wx_fmt=png&from=appmsg)

从目前公开信息看，主线大致是这样：攻击者利用了 Instructure **Free-For-Teacher accounts** 相关的访问路径，拿到了本不该有的 Canvas 数据访问能力。后面又出现了学校 Canvas 登录页被篡改，用公开勒索信息给 Instructure 和学校施压 [1], [2], [4], [6]。

我会把这件事拆成两层看：

* 对学校来说，这是一次第三方 SaaS 供应商事件，也就是教育机构对集中式平台的依赖风险。
* 对技术根因来说，它更像多租户 SaaS 里的 **broken access control / tenant isolation failure / token-management weakness**。
* IDOR 目前只能算一个可能方向，证据还不够。
* 它也不像传统软件供应链攻击。现在没有证据显示是依赖包投毒、恶意更新、CI/CD 污染或第三方组件后门。

一句话总结：

> “
>
> 这次 Canvas 事件更像是 Instructure 自身 SaaS 环境里的授权边界出了问题。入口与 Free-For-Teacher 免费账号有关，攻击者借此拿到了超出正常权限范围的数据访问能力，之后又通过登录页篡改扩大勒索压力。

## 能看到的几张图

### Canvas 登录页被改成勒索页

TechCrunch 放出的截图经过打码，但能看出 Canvas 登录页被替换成了勒索信息 [4]。

![TechCrunch redacted Canvas defacement screenshot](https://mmbiz.qpic.cn/mmbiz_jpg/XXmXKfaNf4oLoibqiaX0bibGicJ1I0WxQ7K3OkZ9Xk6D9pVJIzmdiaK1rF2iaHTvAnCN43qejzXCOIHTB7qhxiaBHV8ZA2NcIxdRZPxoCLI8vRTqBA/640?wx_fmt=jpeg&from=appmsg)

图 1：Canvas 登录页被替换为勒索信息的截图。图片来源见 [4]。

### UTSA Canvas 登录页截图

BleepingComputer 的截图里，`utsa.instructure.com/login/canvas` 页面出现了 ShinyHunters 的勒索信息 [2]。

![BleepingComputer Canvas defacement screenshot](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XXmXKfaNf4rlBnyVyWnSn43kh6zfydKzkbFFOE6AicmDDicqg4OBNd8mqvRWmFeOvkQjOdJianKraFRXpQmcJNCcokFMtlFIViasnnuIcc7n33k/640?wx_fmt=jpeg&from=appmsg)

图 2：UTSA Canvas 登录页出现 ShinyHunters 勒索信息的截图。图片来源见 [2]。

### 学校侧收到的服务中断通知

AP 使用的 Georgia Tech IT 通知截图，说明这件事已经影响到学校侧的正常教学安排 [5]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XXmXKfaNf4qCSNuWic9dcs1ta648GuEM75JicLicXE3eJPt4TQLEOJYZmiar1VeQyVqC5JswTsKpfOM8WALJhibMxXecpApY9mAmDkr3yiaKib9a74/640?wx_fmt=png&from=appmsg)

图 3：学校侧收到 Canvas 服务中断与安全事件通知的截图。图片来源见 [5]。

## 时间线

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XXmXKfaNf4q5lJWYGLnSuicfC9Hw4jeX4j191N6RGBOXFicjWjnvBbnFiaLWfHVxx6QQKZ4sY5L2LjPiaHnG8SyrhkQBRxPEvC9L331LU4JpguM/640?wx_fmt=png&from=appmsg)

| 日期 | 事件 |
| --- | --- |
| 2026-04-25 左右 | 多所学校公告转述，攻击者疑似开始获得未授权访问 [8], [9]。 |
| 2026-04-29 | Instructure 检测到未授权活动，并开始撤销攻击者访问 [6]。 |
| 2026-05-01 | Instructure 官方状态页公开确认安全事件 [6]。 |
| 2026-05-02 | Instructure 称事件初步被控制，已撤销特权凭证/access tokens、部署补丁、轮换部分密钥、加强监控 [6]。 |
| 2026-05-06 | Instructure 状态页称 Canvas fully operational，建议客户启用 MFA、检查管理员访问、轮换 API tokens/keys [6]。 |
| 2026-05-07 | 多所学校 Canvas 登录页被篡改为勒索信息，Canvas/Canvas Beta/Canvas Test 被临时置入维护模式 [2], [4]。 |
| 2026-05-08 | Instructure 通过媒体确认，攻击者利用了 Free-For-Teacher accounts 相关问题，并临时关闭这些账号 [1], [5], [7]。 |
| 2026-05-09 | 公开 root cause 仍未完整披露；论坛和学校侧仍在讨论是否恢复登录、是否等待进一步确认 [3], [6]。 |

## 已经确认的部分

### 受影响系统

受影响的是 Instructure 运营的 Canvas LMS 云平台。学校、大学和 K-12 机构是客户侧受害者，目前看不是主要入侵入口。

### 涉及数据

Instructure 在状态页里说，现阶段看到的受影响数据包括 [6]：

* 用户姓名
* 邮箱地址
* 学生 ID
* Canvas 用户之间的消息

它同时强调，目前没有发现这些数据被涉及：

* 密码
* 出生日期
* 政府身份标识
* 金融信息

来源：Instructure 状态页 [6]。

### 厂商处置动作

Instructure 已公开或经媒体确认的处置动作包括 [1], [5], [6]：

* 撤销受影响系统相关 privileged credentials 和 access tokens
* 部署补丁
* 轮换部分 internal keys
* 限制 token creation pathways
* 加强平台监控
* 临时关闭 Free-For-Teacher accounts
* 将 Canvas 临时下线维护以调查登录页篡改

这些动作值得注意。它们指向的不是单纯网页被改，而是 **凭证/token、授权边界、账号路径、跨租户访问控制** 这一类问题。

## 攻击链怎么串起来

把公开线索串起来，我认为顺序大概是：

1. 攻击者先找到 Canvas Free-For-Teacher 相关的访问路径；
2. 这个路径上的权限边界有问题，导致免费账号获得了超出正常范围的访问能力；
3. 攻击者进一步访问或调用 Canvas 的数据导出、API 或后台能力，导出用户姓名、邮箱、学生 ID、站内消息等数据 [6]；
4. 随后，攻击者在泄露站点上声称掌握近 9000 所机构的数据 [1]；
5. 5 月 7 日，部分学校 Canvas 登录页又被篡改成勒索信息 [2], [4]。

这里面第 2 步最关键。只要 Instructure 没有把完整 root cause 公布出来，就不能武断说到底是 IDOR、权限继承错误，还是 token 创建路径的问题。但从厂商撤销 token、轮换 internal keys、限制 token creation pathways 这些动作看，问题大概率就在授权边界附近。

## 根因怎么归类

### 更稳妥的写法

我现在不会把 root cause 写得太死。更稳妥的英文表述是：

> “
>
> The incident appears to stem from a broken access control / tenant isolation failure in Instructure’s multi-tenant Canvas SaaS environment, involving the Free-For-Teacher account path and potentially token-management or API authorization weaknesses.

换成中文就是：

> “
>
> 该事件很可能源于 Instructure Canvas 多租户 SaaS 环境中的访问控制/租户隔离缺陷，入口与 Free-For-Teacher 免费账号路径有关，并可能涉及 token 管理或 API 授权路径弱点。

### 为什么可能不属于 IDOR

IDOR 这个词不能随便贴。如果要叫 IDOR，至少得看到攻击者通过可控对象标识符访问了不属于自己的对象，比如改 `user_id`、`course_id`、`account_id`、`report_id` 之后拿到其他学校或租户的数据。

现在公开信息能确认的是：

* Free-For-Teacher accounts 是访问路径；
* 攻击者获得了未授权访问；
* Instructure 撤销 token/credentials；
* 数据可能通过 Canvas 数据导出/API 能力被取走；
* 登录页可被篡改。

所以我会归类到 **Broken Access Control**，但暂时不锁定到 **IDOR/CWE-639**。后续如果 Instructure 或取证报告证明攻击者确实靠对象 ID 枚举/篡改跨租户访问，再改分类也不迟。

### 漏洞分类

| 分类 | 适用度 | 说明 |
| --- | --- | --- |
| OWASP A01: Broken Access Control | 高 | 目前最稳妥的上位分类。 |
| CWE-862: Missing Authorization | 中高 | 如果某些敏感操作缺少授权检查。 |
| CWE-863: Incorrect Authorization | 中高 | 如果授权判断存在错误。 |
| CWE-269: Improper Privilege Management | 中 | 如果 Free-For-Teacher 账号可升级或继承异常权限。 |
| CWE-639: Authorization Bypass Through User-Controlled Key / IDOR | 低到中 | 只有在后续证明攻击者通过对象 ID 枚举/篡改访问数据时才成立。 |

## 关于 ShinyHunters

媒体和安全分析人士把这件事与 **ShinyHunters** 联系在一起。该团伙声称影响近 9000 所学校、数亿用户，并以泄露数据为筹码勒索 [1], [2], [4]。

这里要留一点余地：

* “近 9000 所学校”“231M/275M 用户”等数字主要来自攻击者声称，尚未被完全独立验证 [1], [2]。
* AP 报道称 Instructure/Canvas 后续不再出现在 ShinyHunters 目标页面，但 Instructure 没有确认是否支付赎金 [5]。
* BleepingComputer 提到 ShinyHunters 近年常针对 SaaS、Salesforce、第三方集成和 token 访问路径，但这不等于本次 Canvas 事件已被证明是 Salesforce 或第三方集成入侵 [2]。

## 真正的风险

### 不只是停课和宕机

这次最麻烦的地方不只是“系统挂了”。如果姓名、邮箱、学生 ID 和站内消息确实被导出，后续钓鱼会变得很像真的学校通知，尤其是考试、成绩、作业延期、账号恢复这类主题。

登录页篡改也说明攻击者不只是想偷数据，还想制造公开可见的压力。对学校来说，这会直接影响考试、作业提交、成绩发布和师生沟通。

### 后续最容易出问题的地方

* 冒充学校 IT/Canvas 的密码重置邮件
* 冒充教师或学生发送恶意链接
* 利用学生 ID、邮箱、课程关系进行社工
* 利用 Canvas 消息内容构造更可信诈骗
* 对未成年人数据和敏感沟通内容造成隐私风险

## 这算不算供应链攻击

这类事件很容易被一概叫成供应链攻击，但最好分开说：

| 视角 | 判断 |
| --- | --- |
| 学校/大学风险管理 | 是第三方供应商安全事件，属于广义供应链风险。 |
| 技术攻击方式 | 暂无证据表明是传统软件供应链攻击。 |
| SaaS 安全模型 | 属于多租户 SaaS 平台侧控制失效。 |
| 客户责任 | 目前没有证据显示是学校本地配置错误导致主事件。 |

如果要写进正式报告，我会这样表述：

> “
>
> This is best described as a vendor-side SaaS security incident and supply-chain concentration risk for educational institutions, rather than a confirmed software supply-chain compromise.

## 接下来该做什么

对学校/机构：

第一优先级是高权限账号和集成凭证。Canvas 管理员账号要强制 MFA；Canvas API tokens、LTI keys、developer keys 和相关集成凭证该轮换就轮换。近期管理员活动、token 创建记录和异常 API 调用也要拉出来看。

第二优先级是沟通。学校需要提醒师生：不要从邮件、短信或陌生表单链接进入 Canvas；所有账号恢复、考试延期、成绩通知，都以学校官网或官方渠道为准。涉及未成年人或敏感沟通内容的机构，还需要单独做隐私影响评估。

第三件事是向 Instructure 要清楚材料：本机构是否受影响、涉及哪些字段、时间窗口是什么、有没有可用日志和 IOCs。没有这些信息，学校很难做后续处置。

对个人用户：

个人用户能做的事情不多，但几件事很实在：从学校官网或书签进入 Canvas，不点邮件/短信里的登录链接；不要批准意外 MFA prompt；如果 Canvas 密码复用到其他网站，先把那些网站的密码换掉。

## 最后的判断

这不是一次普通服务中断。它同时包含数据外泄、勒索、登录页篡改和 SaaS 多租户授权风险。

目前我会把它归因到这里：

> “
>
> Instructure Canvas suffered a vendor-side multi-tenant SaaS security incident caused by a broken access control or authorization-boundary failure associated with Free-For-Teacher accounts. The incident enabled unauthorized access to user data and was followed by login-page defacement for extortion. IDOR remains plausible but unconfirmed.

---

**References**

[1] Abrams, L. (2026a, May 5). *Instructure hacker claims data theft from 8,800 schools, universities*. BleepingComputer. https://www.bleepingcomputer.com/news/security/instructure-hacker-claims-data-theft-from-8-800-schools-universities/

[2] Abrams, L. (2026b, May 7). *Canvas login portals hacked in mass ShinyHunters extortion campaign*. BleepingComputer. https://www.bleepingcomputer.com/news/security/canvas-login-por...