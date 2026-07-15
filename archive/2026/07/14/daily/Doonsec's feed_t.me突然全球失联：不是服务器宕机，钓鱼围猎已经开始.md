---
title: t.me突然全球失联：不是服务器宕机，钓鱼围猎已经开始
url: https://mp.weixin.qq.com/s/ldzOb00xIXUjML5edvKVxA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:47:02.602575
---

# t.me突然全球失联：不是服务器宕机，钓鱼围猎已经开始

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMBHZjccYnZIj54v3WuteAdOqe4WYnzcH1MSlJl6em06JfYoSA3rko90fRwDqk2kJ3EBZ5Kh24Wqn1WP9ex1viaX3L5Z5DMP5UZ0/0?wx_fmt=jpeg)

# t.me突然全球失联：不是服务器宕机，钓鱼围猎已经开始

原创

MessFeel
MessFeel

MessFreeSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026 年 7 月 14 日实测，Telegram 短链接域名 `t.me` 被注册局设为 `serverHold`，公共 DNS 已无法返回其 A 记录。同一时间，安全监测发现新注册域名正在仿冒 Telegram 登录页，尝试收集手机号、二次验证密码、会话密钥和联系人数据。

两件事都真实存在。现有证据能分别证明"解析故障"和"钓鱼基础设施在跑"，但没法证明钓鱼团伙制造了这次故障，也没法证明 `t.me` 域名已被攻击者接管。

**先把话说清楚：这不是"Telegram 被黑"的证据。**

---

## 故障是真实的：`serverHold`，全球 DNS 逐步失效

截至取证时，`t.me` 的 WHOIS 里出现了一个关键状态：

```
```
serverHold
```
```

ICANN 对这个状态码的解释很直接：域名不会在 DNS 中被激活。注册局停止发布该域名的 DNS 委派后，全球递归 DNS 会逐步失去有效解析结果。

有两点值得注意：`t.me` 的到期时间仍是 **2035 年 5 月 20 日**，不是域名过期；而且这证明的是短链接域名出了问题，不代表 Telegram 消息服务整体中断。

至于 `serverHold` 的具体原因——可能是合规、争议、注册信息核验、安全处置，也可能是注册局的其他措施。在 Telegram 或注册局发布正式说明之前，没必要猜。

![图 1：t.me WHOIS 信息显示 serverHold](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMAXvGGjQo8YMQcCB64CZJyrYFFIibuLOCktcF7c4ZbHAPqpQ4JYOu1s0YVSWtMV72yIPjBkNYyRMwYsnzqYr2YLyKkB0wVO63D8/640?wx_fmt=jpeg&from=appmsg)

**图 1**：公开 WHOIS 查询显示 `Updated On: 2026-07-13`、`Expires On: 2035-05-20`，域名状态中包含 `serverHold`。

---

## 公共 DNS 实测：A 记录已经查不到了

Google 管理员工具箱 Dig 对 `t.me` 的 A 记录查询直接返回：

```
```
Record not found!
```
```

Google Public DNS 的 DoH 接口同时返回 `Status: 3`，对应 `NXDOMAIN`——查询名称在当前可见的 DNS 中不存在。

![图 2：Google 公共 DNS 查询不到 t.me 的 A 记录](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMClv0p2qBdDwK5liagYMq32BblEQomsaN0pickKdwUhxrtpfy99GMvDMr3pD8CtwLicmwUEw5Q3PPA7IFHZVcJ7G66wzmVt7EzcC4/640?wx_fmt=jpeg&from=appmsg)

这两组数据和 `serverHold` 的技术效果能互相印证：问题出在域名委派/解析层，不是 Web 服务器宕机。

### 当前能确认和不能确认的

| 判断 | 结论 | 依据 |
| --- | --- | --- |
| `t.me` 是否处于异常域名状态 | **是** | 注册信息存在 `serverHold` |
| 公共 DNS 能否返回 A 记录 | **不能** | Google Dig 返回 `Record not found`，DoH 返回状态 3 |
| 域名是否因到期而失效 | **否** | 到期时间为 2035 年 |
| Telegram 是否整体被入侵 | **没有证据** | 域名状态不能证明服务端入侵 |
| `t.me` 是否被攻击者接管 | **没有证据** | 未观察到域名指向攻击者基础设施 |
| 钓鱼团伙是否制造了本次故障 | **没有证据** | 目前只有时间上的接近，没有因果证据 |

---

## 故障制造的"信任真空"，才是钓鱼真正想要的

`t.me` 链接突然全部打不开时，用户会做什么？

搜索引擎搜"Telegram 备用地址"、在群聊里要点链接、点开所谓"账号恢复""重新验证"页面、输入手机号和验证码、扫来历不明的登录二维码、下载"修复版客户端"。

这几件事，每一件都是钓鱼团伙盯着想看到的。

攻击者根本不需要控制 `t.me`。只要用户在主动找替代入口的时候，仿冒页面正好出现在搜索结果、群聊转发或私聊消息里，就够了。

---

## 已确认样本：仿冒 Telegram 手机号登录页

监测发现新注册域名 `karruca[.]cfd` 部署了仿冒 Telegram 的手机号登录页面。

![图 3：karruca[.]cfd 仿冒 Telegram 手机号登录页](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMDT0TMkf42X7Mz6VY4aPrJIJGpKE3XpSTS9h4mQJqYGibKiaykke0LMrAiczGc0RlabFGIolLo5w0cg1XwWVvFtEvO9n6xD8Dd4Bw/640?wx_fmt=png&from=appmsg)

静态分析显示，前端代码会把收集的数据发到：

```
```
hxxps://vonkisa[.]sbs/api/telegram/data
```

```
hxxps://vonkisa[.]sbs/api/telegram/contacts
```
```

代码里出现的潜在窃取字段包括：

```
```
telegram_phone_number
```

```
telegram_2fa_password
```

```
user_id
```

```
dc*_auth_key
```

```
contacts
```
```

这几个字段已经超出普通登录页面需要的信息。尤其是 `dc*_auth_key`——一旦有效会话密钥被窃取，攻击者可以绕过单纯改密码这种补救措施，继续利用已有会话访问账号。

样本里还暴露出关联配置：

```
```
Telegram Bot: @AeroMind6_bot
```

```
Telegram API ID: 34874937
```

```
Telegram API Hash: 1ad1c8b7bcf94a29c628195f32358cb4
```
```

API ID、API Hash 和 Bot 名称应作为关联调查线索使用，不建议脱离上下文单独封禁。

---

## 高度可疑样本：二维码仿冒页 + "TG 集群管理系统"

另一个新注册域名 `authweb-telegram[.]com` 出现了仿冒 Telegram 二维码登录界面。

![图 4：authweb-telegram[.]com 仿冒 Telegram 二维码登录页](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMBaHsoHJMLH2R58dUf10uh2giaibqsl0x8XH51NzbicgwfkT83Qzibo7xiaIJdXl6fd4Ao16QcL1F2BPMickZ35kLYW6emW3hDrt828c/640?wx_fmt=png&from=appmsg)

公开扫描还捕获到与之关联的中文管理后台，页面标题为"TG集群管理系统"。

![图 5：疑似钓鱼基础设施管理后台](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMDskXAvjsK204r5LkTzWibohJBnzNnWtbPE0KoNtf20KJrkBP6wGYuRiayr1gQYw2OEr9ZFDiabSCqUxXSViaM8xiaSVPeGheAt3qWs/640?wx_fmt=png&from=appmsg)

前端代码中可见以下接口路径：

```
```
/api/h5/auth/exchange-ticket?session_ticket=
```

```
/api/h5/auth/sync-session
```

```
/api/h5/system-config/public
```

```
/api/v1
```
```

页面外观、域名命名、注册时间、二维码登录流程和后台结构放在一起，可疑程度很高。但目前没有完整复现其凭据外传的完整链路，所以本文把它标为"高度可疑"，而不是和 `karruca[.]cfd` 同级的已确认窃密页面。

---

## 时间线：时间挨得很近，但不是因果证据

以下时间均为北京时间（UTC+8）：

| 时间 | 事件 |
| --- | --- |
| 2026-07-14 03:24:55 | `t.me` 注册局 RDAP 记录变更，出现 `serverHold` 等状态 |
| 2026-07-14 08:48:24 | `karruca[.]cfd` 注册 |
| 2026-07-14 09:46:52 | `authweb-telegram[.]com` 注册 |
| 2026-07-14 | 公共 DNS 确认 `t.me` 无 A 记录；仿冒页面被公开扫描平台捕获 |

钓鱼域名在故障发生后的几小时内注册，说明攻击者动作很快。但时间相邻只能支撑"趁势利用"这个判断，不能证明攻击者事先知情，更不能证明攻击者制造了 `serverHold`。把时间上的巧合写成攻击归因，就是越界了。

---

## IOC：可直接用于威胁狩猎

封禁优先级：域名 > URL > 文件哈希。共享 CDN 地址别因为一个样本就封整段 IP。

### 已确认恶意指标

| 类型 | IOC | 用途/说明 | 置信度 |
| --- | --- | --- | --- |
| Domain | `karruca[.]cfd` | Telegram 仿冒登录前端 | 高 |
| Domain | `vonkisa[.]sbs` | 数据接收/API 基础设施 | 高 |
| URL | `hxxps://vonkisa[.]sbs/api/telegram/data` | Telegram 数据提交接口 | 高 |
| URL | `hxxps://vonkisa[.]sbs/api/telegram/contacts` | 联系人数据提交接口 | 高 |
| SHA-256 | `1ef73a666a1c6e5193c16e78fe1dd80a493d01157405cfbd3fa30f4c19ddd041` | `karruca[.]cfd` 前端 JavaScript | 高 |
| Bot | `@AeroMind6_bot` | 样本暴露的关联 Bot，建议关联调查 | 中 |
| Telegram API ID | `34874937` | 样本暴露的应用标识 | 中 |
| Telegram API Hash | `1ad1c8b7bcf94a29c628195f32358cb4` | 样本暴露的应用配置 | 中 |

### 高度可疑指标

| 类型 | IOC | 用途/说明 | 置信度 |
| --- | --- | --- | --- |
| Domain | `authweb-telegram[.]com` | Telegram 仿冒二维码页面 | 中高 |
| Host | `admin.authweb-telegram[.]com` | 疑似"TG集群管理系统"后台 | 中高 |
| IPv4 | `38.60.191[.]170` | `authweb-telegram[.]com` 解析地址；封禁前核查资产复用 | 中 |
| SHA-256 | `7772aafbc0ce36afa4fa25d77162080f8a0565bb14234956ae1da0ad2e5a284e` | 仿冒二维码页 JavaScript | 中高 |
| SHA-256 | `e5711728f848ecb216abdf2a0932a47660f9512bccc73aeff1f5d11ddc8aa5d1` | 疑似管理后台 JavaScript | 中高 |
| URI Path | `/api/h5/auth/exchange-ticket` | 可疑票据交换接口 | 中高 |
| URI Path | `/api/h5/auth/sync-session` | 可疑会话同步接口 | 中高 |

### 不能作为恶意 IOC 封禁的官方资产

以下域名是 Telegram 官方基础设施或历史官方短链资产，不能因为这次事件列入黑名单：

```
```
telegram.org
```

```
telegram.me
```

```
telegram.dog
```
```

---

## 企业侧排查建议

安全团队从 DNS、代理、EDR 和邮件网关里检索以下关键词：

```
```
karruca.cfd
```

```
vonkisa.sbs
```

```
authweb-telegram.com
```

```
admin.authweb-telegram.com
```

```
/api/telegram/data
```

```
/api/telegram/contacts
```

```
/api/h5/auth/exchange-ticket
```

```
/api/h5/auth/sync-session
```
```

如果命中员工访问记录，继续核查这几项：

* 有没有提交过 Telegram 手机号、验证码或二次验证密码；
* 有没有扫过页面上的登录二维码；
* 浏览器有没有向可疑接口发过 POST 请求；
* 终端有没有出现来路不明的 Telegram 客户端、浏览器扩展或安装包；
* Telegram"设备/活动会话"里有没有陌生设备和异地 IP；
* 账号有没有出现批量私聊、拉群、发广告或联系人导出。

确认泄露后的处置顺序：

1. 在 Telegram 官方客户端里终止其他活动会话；
2. 修改二次验证密码，检查恢复邮箱；
3. 删除未知机器人、授权应用和已连接设备；
4. 通知联系人不要相信近期的异常消息；
5. 保存 DNS、代理、浏览器历史和终端日志，用于溯源。

---

## 普通用户现在就该做的事

* 别去搜什么"`t.me` 修复站""Telegram 恢复入口""专用镜像"——目前不存在这种东西；
* Telegram 官方网页入口从 `telegram.org` 导航过去，群聊里甩出来的陌生域名别点；
* 扫码之前先看浏览器地址栏，确认是官方域名；
* 任何页面跟你要 Telegram 二次验证密码、会话密钥，或者让你下载不明客户端，直接关掉；
* 已经输了验证码或扫了码的，马上去官方客户端里终止陌生会话。

---

## 事实之间必须划清的边界

`t.me` 的解析故障可以被注册局状态和公共 DNS 结果直接验证。钓鱼页面的存在，也可以被页面快照、代码、数据接口和文件哈希验证。

但两件事之间目前只有时间上的接近。

> **现有证据支持"攻击者正在利用故障制造的信任真空"，不支持"攻击者制造了故障"，也不支持"Telegram 已被攻破"。**

安全事件报道把这三条线划清楚，比急着下结论重要得多。

---

## 参考与证据来源

1. Identity Digital：`t.me` RDAP 原始记录
2. Whois.com：`t.me` 注册状态查询
3. ICANN：EPP 域名状态码说明
4. Google Public DNS：`t.me` A 记录 DoH 查询
5. Google 管理员工具箱 Dig
6. URLScan：`karruca[.]cfd` 页面样本
7. URLScan：`authweb-telegram[.]com` 前台样本
8. URLScan：疑似管理后台样本
9. CentralNic RDAP：`karruca[.]cfd` 注册记录

> **取证说明**：页面状态、DNS 结果和恶意基础设施都可能随处置进展发生变化。本文截图与 IOC 对应 2026 年 7 月 14 日取证快照，后续引用时请保留日期和置信度标签。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nBEAXTaIuYiakqwmQlIeWQ9ZbB12BtJzcwa1sL64JXogjggNfsgZqLHVNxUhKTlqf6bATcs6kwDk9RyssibnnI0g/0?wx_fmt=png)

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