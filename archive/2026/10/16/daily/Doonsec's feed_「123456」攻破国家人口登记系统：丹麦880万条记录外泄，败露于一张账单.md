---
title: 「123456」攻破国家人口登记系统：丹麦880万条记录外泄，败露于一张账单
url: https://mp.weixin.qq.com/s/MrFMR3fb0M_7emCCo7Qprg
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:35:20.684832
---

# 「123456」攻破国家人口登记系统：丹麦880万条记录外泄，败露于一张账单

# 「123456」攻破国家人口登记系统：丹麦880万条记录外泄，败露于一张账单

赤霄攻防实验室
赤霄攻防实验室

赤霄攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![封面｜数据泄露事件（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8acOGLHEgXC6YXXfMuWmCIMGXYicMicmVaDAZRvjJUOticBBjmUMNeqvIO623v2vRCclibndPs2XfXjdv3pb75OCFSmnYdkHudHLgYQ/640?wx_fmt=png)

▲ 封面｜数据泄露事件（制图：赤霄攻防实验室）

TL;DR

**是什么**：丹麦国家人口登记系统（CPR）被攻破，880 万条记录被导出——入口是一家第三方查询服务商的账户，密码为「123456」

**有多荒诞**：泄露发生 12 天后才被发现，而暴露它的不是安全监控系统，是一张查询量异常的账单

**现状**：哥本哈根方面确认攻击；服务商 Pays ApS 董事总经理公开确认其数据库访问权限被利用；黑客称无意出售

**看点**：国家级数据库的安全底线 vs 印尼、韩国——政府数据事故的三种死法

![事件档案卡（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8afjYLMNwHxKSXOwDpHUWKgnfKN4lgW2kraHaiatA5oWTia49FiaNSzVjpp6eIj1vhOySApQAFqOGPvlXAkM73I2DLEaicBgtWbJNE8/640?wx_fmt=png)

▲ 事件档案卡（制图：赤霄攻防实验室）

## 事件全景：国家人口登记系统是什么量级的目标

丹麦的 CPR（Det Centrale Personregister，中央人口登记系统）不是一个普通的会员数据库——它记录着全体丹麦公民的个人编号（CPR-nr）、姓名、地址与状态信息，个人编号伴随终生、用于税务医疗银行等一切社会场景，可以说是丹麦社会的「主键」。据《The Register》报道，一名攻击者声称通过一个密码仅为「123456」的账户进入了这个系统，并导出了 880 万条记录。

有两个数字值得对照：丹麦人口约 590 万，而泄露记录达 880 万条——差额部分是 CPR 中保留的历史与已故人员记录，这也侧面说明导出的可能是库的整体快照而非按需筛选。哥本哈根方面已确认遭到攻击；提供 CPR 查询服务的 IT 与数据服务公司 Pays ApS 的董事总经理索菲·劳尔森确认，攻击者利用了该公司对数据库的访问权限导出了数据。黑客本人则声称无意出售或泄露这些信息。

![媒体报道：123456 密码攻破丹麦国家登记系统（来源：MSN/The Register）](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8acLnLl13zafbD2RnwX83NSwc7Md1Vnqq8RicrDlbVKjZYvxe3OmHF3zBafeaGpRRM8icFFTOaGoq1nVTkOuPypJMu6Hk6PEdwrnE/640?wx_fmt=png)

▲ 媒体报道：123456 密码攻破丹麦国家登记系统（来源：MSN/The Register）

## 攻击路径：第三方账户是最短的那块板

路径朴素到令人无语：Pays ApS 是一家为商业客户提供 CPR 数据查询服务的 IT 与数据服务公司——这类「合法数据中介」持有批量查询国家级登记系统的高权限账户。攻击者拿到这家公司某个账户的访问权后，唯一需要逾期的障碍是一个六位纯数字密码。

从 10 月 2 日到 7 日，攻击者在五天里分批导出数据，全程没有触发任何安全告警。真正让事件败露的，是 12 天后的一张账单：Pays ApS 发现某个账户的查询活动量异常，顺藤摸瓜才确认数据外流。换句话说，在这起事件里承担「异常检测」职责的，是计费系统而不是安全系统——这可能是整起事件最值得所有 CISO 反复咀嚼的细节。

![时间线：从弱口令到一张账单（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/sz_mmbiz_png/9yNnjAJL8adyjVe5TQQHGmRqaET97LamIrQAXA5lwNSTKzONysgiaVkOXyrH4tnOg6Lf7LLicr9KzX3WhUgfVwhZaT0JDXuy8ez9xl0GyUSyM/640?wx_fmt=png)

▲ 时间线：从弱口令到一张账单（制图：赤霄攻防实验室）

## 全球对照：政府数据的三种死法

把近两年的政府数据事故放在一起看，失守点各不相同却同样扎心。2024 年，印尼超过 230 个公共机构遭勒索软件攻击，事后发现系统根本没有备份——恢复无从谈起；去年，韩国一个政府数据中心火灾烧掉 858TB 数据——物理世界的单点故障。再加上这次丹麦的第三方弱口令，三种死法对应三种欠账：没有备份、没有冗余、没有基本的密码卫生。

还有一个正在改变格局的变量：AI。报道称近期针对韩国银行与台湾政府的攻击已借助 AI 代理实施，也有黑客利用 Claude 工具入侵 OpenAI 的报道——AI 在攻击侧的效率增益正在显现。不过这篇案例最讽刺的地方在于：当第三方账户的密码是「123456」时，攻击者可能根本不需要 AI。

![全球对照：政府数据事故三种死法（制图：赤霄攻防实验室）](https://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8afEWTBxq7gp90uICaRJJCu2oAax8fGfGW1Mm27Exddj047f2SV2jiaAhmXhYP9LeXI16LB2vPm03wb0WKetUaloFJ3kG91D10ew/640?wx_fmt=png)

▲ 全球对照：政府数据事故三种死法（制图：赤霄攻防实验室）

## 防御视角：四条给所有拥有「权威数据库」的团队

### 1. 机器账户也要有密码策略与 MFA

第三方查询账户、API 账户、服务账户往往游离在人工密码策略之外——123456 能活到 2026 年，说明它从没被策略覆盖过。所有非人工账户同样纳入密码强度校验与强制 MFA（证书/令牌优于口令）。

### 2. 让计费数据变成安全信号

这次事件靠账单发现，反过来说明安全监控完全缺位。查询量、导出量、访问频率的异常基线检测成本极低——把计费/用量的异常波动接进告警，同类事件在第一天就会被抓住，而不是第 12 天。

### 3. 数据中介的权限最小化

商业数据服务商持有的批量查询权限应当按业务最低需要裁剪：分页上限、频次限制、字段脱敏、可疑模式熔断。能一次导出 880 万条的账户，本身就是一个待引爆的风险。

### 4. 政府数据库需要公开的安全基线

国家级登记系统应当有公开、可审计的安全基线（密码策略、MFA 覆盖率、第三方访问清单），让公民与媒体可以监督——丹麦这次的透明度值得肯定，但基线前置永远比事后坦白便宜。

## 参考来源

1. The Register：123456 password linked to Denmark data breach affecting 8.8M people（2026-10-13）
2. 多家媒体交叉报道：Firstpost / TechPowerUp / HotHardware / MSN 等
3. 丹麦哥本哈根方面与 Pays ApS 官方确认信息

免责声明：本文仅用于安全研究与防御交流；事件信息以官方调查结论为准。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9yNnjAJL8acyYZfmKJeSLQ7Quiag7TKhsm6Z5yHicU9D1f8on7dzPIKTE1LJpnoT3TmcTlngd8BRNH8cf30FeI94XtDOrUOJibW2Jh16nvMQ6g/0?wx_fmt=png)

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