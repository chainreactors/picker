---
title: 【数据库】Redis等保核查命令大全｜亲测有效 + 持续更新
url: https://mp.weixin.qq.com/s/QnN4SFvRSrPmPxxac34zPQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:25.845011
---

# 【数据库】Redis等保核查命令大全｜亲测有效 + 持续更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2r1REgdXKkqlf8hykG2BZBlib2dYdseQuT3gx7sPib9saQYoicN0UgD5EmnJ85bBvf6MbAUx0UX5erDlpH0sRVHJLRASn3s869RaQdKAmiaWPvI/0?wx_fmt=jpeg)

# 【数据库】Redis等保核查命令大全｜亲测有效 + 持续更新

Sec Online

![]()

在小说阅读器中沉浸阅读

以下文章来源于汤池杂货铺
，作者Fuyuanzi

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5J0Y2dAfZtVROkAVlm3W1h1cT95E1sJ3cFJ0nGNSmcJA/0)

**汤池杂货铺**
.

是一个什么都想学一点的小邋遢

---

解决以下3个痛点：

1️⃣能查到的大部分检查命令没有运行结果的截图，无法确定命令是否有效。

2️⃣不同版本的被侧目标可能使用不同的命令，过时或者较新的命令可能无法有效运行，明显降低检查效率**。**

3️⃣**网络公开的检查方法整体缺乏系统性与持续维护**

💽测试环境：虚拟机

💽测试镜像版本：Rocky-10.1-x86\_64-dvd1.iso

💽数据库版本：Redis 6.2.6

📚文末可提取本文的无水印PDF版本的百度网盘下载链接，方便各位在无网络环境下的使用。

👇如果有更加好的检测命令或者需要修改的地方，请在评论区留言。我会及时更新改正，并上传新的离线文件。

---

目录结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkpInH61643G7j1tajvUGYl8rDCSUF7v9T8TuwSzTPU9UcTQiawib78YJtL7Bl69B3gsSf6LEcZulNSDP0fNfwb1jYDEUpfaCeCCo/640?wx_fmt=png&from=appmsg)

---

# 一、身份鉴别

## 1.1 账号管理

**Redis 5.0 及以下版本**：**不支持多用户**，只有默认的 `default` 用户（无用户名，仅通过 `requirepass` 设置密码）。**Redis 6.0 及以上版本**，支持 **ACL（Access Control List）** 功能，可以用来查询（创建）多个用户、分配权限、设置密码。

```
ACL List
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkpyib7YUwHc5pGMgPkMQD44OWyac0p3icRe1GryrvV7w2iaa3cN0icZO3ibPSyDSRrxcpq4qXUMRzicYicVXicspbscOk7YqIKh7ozRY6s/640?wx_fmt=png&from=appmsg)

> 但是Redis 的 `ACL SETUSER` 命令 **不会覆盖已存在的用户**，而是会**追加一个新的用户实例**，如果用户名重复，就会出现“双用户”、“多密码”的情况👆。

**参数含义：**

| 部分 | 含义 | 备注 |
| --- | --- | --- |
| `user default` | 用户名为 `default` | 其它账户有：test(3个)，fuyuanzi，readonly |
| `on` | 已启用（可登录） | `off` 为账号禁用 |
| `#7676aaa...` | 密码哈希值（SHA256，不可逆） | 有多个密码代表：双用户，多密码 |
| `~*` | 可访问所有 key（通配符） |  |
| `&*` | 可访问所有数据库（默认为 db0） |  |
| `+@all` | 可执行所有命令 |  |
| nopass | 无需密码（危险！） |  |
| -flushall | 禁止执行 flushall（即使有 `+@all`） |  |
| +get +set | 仅允许 GET 和 SET |  |
| +@admin | 允许管理命令（CONFIG, ACL, SHUTDOWN 等） |  |
| +@write | 允许写命令（SET, DEL, INCR 等） |  |
| +@read | 允许只读命令（GET, EXISTS, TTL 等） |  |
| ~user:\* | 只能访问 `user:xxx` 开头的 key |  |

`protected-mode` 是 Redis 提供的一项**安全保护机制**，其核心功能是：

* • 当 Redis 未设置密码（或 ACL 用户无密码）且绑定到非本地地址（如 `0.0.0.0` 或公网 IP）时，自动拒绝外部网络的连接请求，防止未授权访问。
* • redis 旧版：`requirepass` 是否配置？

* • redis 新版（6.0+）：默认用户 `default` 是否有密码（`nopass`）？

因此检查`protected-mode`也是一种检查账户是否存在口令的配置项。

```
CONFIG GET protected-mode
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKko8icFM00aBruUe3esmNydLH3Bdtw5JjoYUEfEpQT2O9TdXXfYYKsR03e1oN0uXYzFLp0mLZBIdaquf0jyntm9TQZr4tcyXq42I/640?wx_fmt=png&from=appmsg)

## 1.2 密码复杂度

🔹 **Redis 6.0+ ACL 模式）**

✅ Redis **不会校验密码强度**，也不会强制你使用复杂密码。因此在通过 **1.1账号管理的核查** 后，需要再配合 **访谈** 的形式去进一步确认密码复杂度是否符合要求

🔹 **Redis <6.0（传统模式）**

✅ 在配置文件`redis.conf`中，使用了 `requirepass your_password` 设置全局密码，密码为明文状态，可以查看其复杂度。

## 1.3 登录失败处理

Redis **本身没有内置的账户锁定、登录失败次数限制或防暴力破解机制**（如 fail2ban 那样的功能）。它追求高性能和简洁，安全控制主要依赖**网络层防护**和**外部工具**，因此可通过**访谈**去获取相关信息。

## 1.4 远程登录管理

在`redis.conf`中可以对远程登录的IP进行限制。

```
cat redis.conf | grep -E "bind"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkrePic6EAITJoG2ibnrhD2FElXbImBnltGcOsaibmPmKQs2iaf4Q2fc3D2zgIHbJXsmP4B2lFvpVPZ0ys1BlYV1v2GxfS568vbc014/640?wx_fmt=png&from=appmsg)

## 1.5 双因素认证

Redis 的设计哲学是 **高性能、低延迟、轻量级**，没有集成复杂的认证协议（如 TOTP、OAuth、LDAP 多因素等）。

因此 **Redis 本身不支持双因素认证（2FA / MFA）**，无论是 Redis 6.x、7.x 还是最新版本（截至 2026 年），其内置的 ACL（Access Control List）系统仅支持 **用户名 + 密码（单因素）** 的认证方式。

# 二、访问控制

## 2.1 账户权限划分

* • 如果版本 ≥ 6.0 → 支持 ACL，可查看多用户权限
* • 如果版本 < 6.0 → 只有全局密码（`requirepass`），无“账户权限”概念

```
ACL users

ACL GETUSER test
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkqkiaMeSTJwibGUtKfz1c6B8QlwV8ibj6SiaqIUPtaaDElf1NFSI0MWaFxn29g6qBM6WjvXkhBIOCj9pvglxbCIrP4DnZoZZOmMhEo/640?wx_fmt=png&from=appmsg)

## 2.2 默认账户/口令

🔹 **Redis 6.0+ ACL 模式）**

Redis 6.0+ 引入了 ACL（访问控制列表）系统，默认存在一个名为 **`default`** 的用户。

> **Redis 没有预设的默认明文密码（如 admin/123456）**，但是如果没手动设置密码，`default` 用户就是 **空密码**。

```
ACL LIST

-- 危险结果显示：nopass：无需密码登录
user default on nopass ~* &* +@all
```

🔹 **Redis <6.0（传统模式）**

✅ 在配置文件`redis.conf`中，使用了 `requirepass your_password` 设置全局密码，密码为明文状态，可以查看其账户状态。

## 2.3 共享账户

结合客户端连接信息和日志信息进行分析判断。

🔹**检查客户端连接信息（实时）**

```
CLIENT LIST
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkq2GPxmDL8yTndFYSnIz4UkjgHHflNAOdDnQceA1US3mCg2Rg5BIRZcYkM88SLlNJYnx2mZGiaD6AvnRyHvPgGerpcE6uQXTr20/640?wx_fmt=png&from=appmsg)

🔹**审计日志（需提前配置）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkqxK2lhJgVfXhda2ABanDomQutGuAoJoErMmgKwXRuGcGOsGp8gpzic8RuUUVSibZePayHrqH9Zagc1S1v6W6eDjQvJRoJhvJFjQ/640?wx_fmt=png&from=appmsg)

## 2.4 最小权限原则

结合 **2.1 账户权限划分** 和 **1.1 账号管理** 的检查结果，来判断账户权限是否按照最小权限原则进行权限划分。

检查持久化文件权限（禁止其他用户访问，必须 600/700）

```
ls -l 你的Redis数据目录/dump.rdb
ls -l 你的Redis数据目录/appendonly.aof
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkrJWjGsob1fk9kS3MwZkQia8hpjvdhVSjnqQgLSAeb30CdKn6KvBQhqSLH7PibTsxvxt4tiaFBbyHg4QDYV37MJN0UEUfZk0RwSR4/640?wx_fmt=png&from=appmsg)

* • 如果包含 **`+@admin`** → 具有授权能力（超级管理员）
* • 如果包含 **`-@admin`** 或 **没有 `+@admin`** → 无授权能力（普通用户）

> 💡 即使用户有 `+@all`，只要显式禁止了 `@admin`（如 `-@admin`），也无法执行 ACL 命令。

```
ACL LIST
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkoJiaY56cX2sqNKRXlKH6xQlsZpNmYuVnsaL6mJr2JU9pkty5DiaJOKPZ6QE2HFo1xiazHKDcc8BiaFdibRSv5uiaCjAg9ibfzSs01icicw/640?wx_fmt=png&from=appmsg)

## 2.6 访问控制的粒度

结合**2.4 最小权限原则** 中角色权限查看的信息进行判断，`PUBLIC` 相当于“所有用户”，对其授权等于放弃访问控制粒度，任何返回结果均视为**不符合细粒度要求**。

## 2.7 强访问控制

🔹 **Redis 6.0+ ACL 模式）**

**Redis 从 6.0 版本开始引入了强大的访问控制策略机制——ACL（Access Control List，访问控制列表）**，使其具备了**细粒度、多用户、命令级和键级的强访问控制能力**。

```
-- 正确做法（最小权限）
ACL SETUSER fuyuanzi on >123456 ~app:* +@read +@all -@admin -flushall -flushdb
-- 即使使用 +@all，也应显式禁用危险操作
```

> 💡 **顺序敏感**：规则从左到右生效，后出现的 `-flushall` 会覆盖前面的 `+@all`。

🔹 **Redis <6.0（传统模式）**

低于**Redis 6.0的数据库** 不存在较强的访问控制策略。

* • 仅支持全局密码（`requirepass`）
* • 所有连接拥有**完全相同权限**
* • **无法区分用户、无法限制命令或 key**

# 三、安全审计

## 3.1 安全审计功能

Redis **本身不提供内置的“审计策略”配置项**（如开启/关闭审计、设置审计级别等），但可以通过 **日志记录 + 外部工具** 实现基础审计能力，具体需要结合**访谈**去判断redis的审计方式。

```
# 查看当前 loglevel
CONFIG GET loglevel
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkoG4HjjjkEfhW9NaluDwVdXN4aL3584ZoOV0vkpF0xYCk89dSt1xhLicTV9dVdUby3n0TN8WhCibyhuTxUhzialTkUvLYtVKjoVI4/640?wx_fmt=png&from=appmsg)

| 级别名称 | 英文 | 日志内容（核心说明） | 适用场景 |
| --- | --- | --- | --- |
| 调试（最详细） | debug | 记录所有细节：命令执行、内存分配、网络交互、调试信息等 | 开发 / 测试环境、排查底层问题（生产禁用） |
| 详细信息 | verbose | 比 debug 精简，记录关键操作（如客户端连接 / 断开、命令执行统计） | 测试环境、需要监控基础操作的场景 |
| 通知（默认） | notice | 记录正常运行的重要事件（如配置加载、持久化完成、主从同步启动） | 生产环境默认级别（平衡详细度和性能） |
| 警告 | warning | 仅记录非致命的异常 / 风险（如配置不规范、内存使用率偏高、连接超时） | 生产环境（需关注但不影响服务运行） |
| 错误 | error | 仅记录致命错误（如持久化失败、主从同步中断、内存耗尽、配置错误） | 高安全要求的生产环境（仅关注故障） |
|  |  |  |  |

```
# 查看日志文件路径
CONFIG GET logfile
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkpyK4icTTX5JvhWRWvaAqaXeRlWN8nusEW0fqXUEHXx90yibqV2RejI7fnYhdnnI4727MWcLp6qWnHW9ribbyKU4TClKaQmvURQ3M/640?wx_fmt=png&from=appmsg)

* • 如果 `logfile ""` → 日志输出到 **systemd journal**
* • 如果 `logfile /var/log/redis/redis.log` → 写入指定文件

## 3.2 审计记录信息

3.1 审计功能中的 **log\_line\_prefix** 参数提供了审计日志中提供的审计信息

## 3.3 审计记录保护

日志是否防篡改：检查日志文件权限设定是否合理。

```
ls -l /【日志存放路径】/redis.log
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkriaVxRoO0KAoEr6PRYs9R0AddX2BUE1dmyuziaKiaN2icA0naaRZBPapqqibk9KqEbC3uzn6heWhflvrlcnWrkFv4rqYF24wNjFk7k/640?wx_fmt=png&from=appmsg)

# 四、入侵防范

## 4.1 限制终端接入

结合 1.3 远程登陆管理的检查信息进行分析

## 4.2 补丁更新

Redis **没有传统意义上的“安全补丁列表”命令**（如 `yum check-update`），但你可以通过以下方法**查看当前版本是否存在已知安全漏洞、是否需要升级**，并获取官方安全公告。

```
INFO server
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkpjgBiaB00vAtp0ibqicX7YSVSI1ZejNuSlzicGOJUz6ZicQY8KNCBcPZalxnUhvSt79EfABYQKVmQZIkB5SiaGQiaxtqQ2sL4fIpVfmQ/640?wx_fmt=png&from=appmsg)

# 五、可信验证

## 5.1 数据传输过程中的保密性与完整性

Redis 6.0+ 原生支持 TLS（此前需用 stunnel 等代理）

```
cat redis-6.2.6/redis.conf | grep tls
# 判断是否开启tls，以及证书的安装位置
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkqlgfEjXoNMibHbQibbBVCnHjxRaTP5YH2fYqzUgyefq7h4hic4ic6X1WP2eoicwtA39kvR7iaroFHkIP4QemDFB7mWd1bNlAb8xhmnc/640?wx_fmt=png&from=appmsg)

| 配置项 | 含义 | 当前状态 |
| --- | --- | --- |
| `# tls-port 6379` | 启用 TLS 端口（默认 6379） | ❌ 注释，未启用 |
| `# tls-cert-file redis.crt` | 服务器证书文件路径 | ❌ 注释 |
| `# tls-key-file redis.key` | 服务器私钥文件路径 | ❌ 注释 |
| `# tls...