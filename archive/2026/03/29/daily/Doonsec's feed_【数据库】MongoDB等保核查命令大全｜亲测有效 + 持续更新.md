---
title: 【数据库】MongoDB等保核查命令大全｜亲测有效 + 持续更新
url: https://mp.weixin.qq.com/s/Y0i0I899IntQSIx-1BjuPg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:21.715137
---

# 【数据库】MongoDB等保核查命令大全｜亲测有效 + 持续更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2r1REgdXKkrv7RNOukLJ5NKymyZ4yWcXBxlSg6ia0Fwm0wvGe4t2EO4BZjG1tyvOEKMibZQAKonRQKuot6Cn0R5eiaX4Hnxz0ccib0GpYXVCCNU/0?wx_fmt=jpeg)

# 【数据库】MongoDB等保核查命令大全｜亲测有效 + 持续更新

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

💽数据库版本：MongoDB 8.2.5

📚文末可提取本文的无水印PDF版本的百度网盘下载链接，方便各位在无网络环境下的使用。

👇如果有更加好的检测命令或者需要修改的地方，请在评论区留言。我会及时更新改正，并上传新的离线文件。

---

目录结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKko31g2F4M4eqKkn0Vpk1EXKsJdNOhDiaHDahnGAZ4GapCIgETKvQ8Pg8oFWlhEyg6J17JyGMAVUXjBaDFnK55HKAsFX10tc7AOA/640?wx_fmt=png&from=appmsg)

---

# 一、身份鉴别

## 1.1 账号管理

MongoDB 中每个角色（role）名称在集群内必须是唯一的，这是由系统强制保证的。

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkqpwn7VANSPExVLry6uzoZYqqRnmEiaAARYu834ngJjAWMFJn1KkOL7RvjIZVKicBagnuDtropnMWy39BQ8Cv1QZPsicAMLiboBGQ0/640?wx_fmt=png&from=appmsg)

你可以通过以下 语句查询确认当前数据库下可用以登录的角色，并从响应结果中获得每一个角色的权限划分。

```
use <数据库>

show users
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkqatyPyd9WicYPibherp4mwWRGwTYGz5sv9bSNlbwib9ynP2KIRVFjuNvOqjc8GdIbbZs68FTtNagWLU50L3dUhX4baaCll7icfnu0/640?wx_fmt=png&from=appmsg)

## 1.2 密码复杂度

* • MongoDB **本身在社区版中并不原生提供可配置的密码复杂度策略**（如最小长度、必须包含大小写字母/数字/特殊字符等）。
* • MongoDB 企业版，在`mongod.conf`中进行密码复杂的静态配置。

```
cat /etc/mongod.conf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkqq6FfCbf69hftDcF28icGOWMstFIyhgOuMZznCD8IjkH1Hqz5IU3EfXh1R6tWL0cYs8PFQFHFn9B5EjLKnkONlfiakNGHicM6HCQ/640?wx_fmt=png&from=appmsg)

## 1.3 登录失败处理

**纯 MongoDB 原生无法实现“输错 5 次密码就锁定账户”**，除非集成外部认证系统（如 LDAP + Active Directory）, 应通过访谈形式确认是否存在第三方的安全控制。

## 1.5 双因素认证

MongoDB 默认支持以下认证方式：

* • **SCRAM**（Salted Challenge Response Authentication Mechanism）：社区版和企业版都支持（如 SCRAM-SHA-1、SCRAM-SHA-256）
* • **x.509 证书认证**：基于 TLS 客户端证书
* • **LDAP / Kerberos**：**仅限 MongoDB Enterprise 或 Atlas**

> ❗ 所有这些方式都是**单因素认证**（你知道的密码 / 你拥有的证书 / 你在目录中的身份），**不包含第二因素（如手机验证码、TOTP、FIDO2 等）**，应通过访谈形式确认是否存在第三方的安全控制。

# 二、访问控制

## 2.1 账户权限划分

MongoDB 的权限划分基于 **基于角色的访问控制（RBAC, Role-Based Access Control）**，通过 **用户（User） + 角色（Role） + 权限（Privilege）** 三层模型实现精细化权限管理。需要结合 **1.1账号管理** 的内容可以进行可登录账号的权限查看是否存在多种类型的可登录账户用以划分权限。

## 2.2 默认账户/口令

MongoDB安装后的默认账户为admin，默认是没有口令的。

```
mongosh
-- 看能否在不使用口令的情况下，直接登录数据库

use admin

show users
-- 检查是否存在默认账户admin
```

## 2.3 共享账户

最佳判断方式是通过日志进行分析👇：

```
cat /var/log/mongodb/mongod.log | grep "用户名"
# 分析用户的链接状况
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkrZ4t7Hvja4kJIicgoPRNs8FA9Bqw7rtWD7QOXGFqjia5qTt7hDPL7uicMl2OtEUIDJyaf5Hf5K2DZJ1REc6yaIBXA84KafQ4H0ws/640?wx_fmt=png&from=appmsg)

## 2.4 最小权限原则

MongoDB 使用 **基于角色的访问控制（RBAC）** 来落实最小权限，因此需要结合 **1.1 账号管理** 的调查内容进行权限分析。

## 2.5 授权主体配置访问控制策略

在 **MongoDB 8.2.5** 中，用户是否具备访问策略配置（如角色管理、权限分配、安全策略设置等）的能力，取决于其被授予的角色和权限。

**普通用户**（即没有被赋予管理类角色的用户）：

* • **不具备** 配置访问策略的能力。
* • 通常只拥有对特定数据库的 **读写权限**（如 `readWrite` 角色），仅限于业务数据操作。
* • 无法创建/删除用户、修改角色、配置审计日志、启用认证等管理操作。

**admin 用户** 通常是指在 `admin` 数据库中创建，并被赋予了管理角色（如 `userAdminAnyDatabase`、`dbAdminAnyDatabase`、`root` 等）的用户。
这类用户**具备访问策略配置能力**，具体取决于所分配的角色：

| 角色 | 能力说明 |
| --- | --- |
| `userAdminAnyDatabase` | 可以在任意数据库中创建/删除用户、分配角色（但不能读写业务数据）。 |
| `dbAdminAnyDatabase` | 可管理任意数据库的结构（如索引、集合），但不一定能管理用户。 |
| `root` | 超级用户角色，拥有所有权限，包括安全策略、审计、备份、集群管理等。 |

## 2.6 访问控制的粒度

结合**2.4 最小权限原则** 中角色权限查看的信息进行判断，MongoDB 的访问控制（Access Control）基于 **基于角色的访问控制**（RBAC, Role-Based Access Control），其权限颗粒度设计较为精细，支持从 **数据库级别** 到 **集合/操作级别** 的多种粒度控制。

# 三、安全审计

## 3.1 安全审计功能

```
cat /etc/mongod.conf
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkp4e7s92XicH4dYn0cyibMCW8L6icuicYQdUk91zc65MgdSKG2FpCLFnvfRtdF7WgRvIgFW6KY4tCLa0bbQ2xNQ1YGFxzp0cqs9OZM/640?wx_fmt=png&from=appmsg)

## 3.2 审计记录信息

3.1 审计功能中的 **log\_line\_prefix** 参数提供了审计日志中提供的审计信息，也可以通过命令行进行查看。

```
cat /var/log/mongodb/audit.log
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkq6dRTUcJ7V87XknBIVMETlXpDBicpuMJPf9uYoekbs5qPxIe81Zak13TI7LLFTKqyYMMOF0ibiaLHbFXbyTqrQSnD9YwlWrJpJls/640?wx_fmt=png&from=appmsg)

## 3.3 审计记录保护

日志是否防篡改：日志文件权限为 `600`，仅特定权限用户可读可写。

```
ls -l /var/log//mongodb/audit.log
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkoLpYb9Q1xeq7SUkmGV3AIvwbA7H5QJ6X65tcRePp1COzzaw7K9wenhS7TWc4XbLEVh6wA4iafHFo47gatur00oiamdBibaylAy94/640?wx_fmt=png&from=appmsg)

# 四、入侵防范

## 4.1 限制终端接入

```
cat /etc/mongod.conf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkpylcfwUiakA0IAdFgNiaz6mnW3dc8DnaX9OA5DXhfuAG6QQtdz3EWppyYtiaAz9M6BN3KCRHaMseic73blBPR3XUIaRsz0Z2GtAgo/640?wx_fmt=png&from=appmsg)

## 4.2 补丁更新

```
 db.version()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkqHoibeTXSOdvZ7ebF40ERicMTbh2qn6vP03miarD4EXQfe9p7fgCunHnWROe9dBOiaibCibIlFVv5WvTia0nQquybPg7p0Ms934TkRUs/640?wx_fmt=png&from=appmsg)

MongoDB 使用 **语义化版本格式**：

```
X.Y.Z
│ │ └─ **补丁版本**（Patch）—— 安全修复、Bug 修复
│ └─── **次要版本**（Minor）—— 新功能 + 向后兼容
└───── **主版本**（Major）—— 可能包含破坏性变更
```

截至 **2026年2月**，MongoDB 8.2 系列的最新补丁是 **8.2.5**。

# 五、可信验证

## 5.1 数据传输过程中的保密性与完整性

mongoDB支持设置TLS来保证数据传输过程中的安全，相关配置可以从`mongod.conf`进行查看。

```
cat /etc/mongod.conf
```

**配置示例（`mongod.conf`）**：

```
net:
    tls:
        mode: requireTLS
        certificateKeyFile: /etc/ssl/mongodb.pem
        CAFile: /etc/ssl/ca.pem
```

## 5.2 数据存储过程中的保密性与完整性

MongoDB 提供两种静态加密方案：

（1）**WiredTiger 存储引擎原生加密**（Enterprise Only）

* • 自动加密 **数据文件、日志、备份**。
* • 使用 **AES-256** 加密算法。
* • 密钥管理支持：

+ • 本地密钥文件（不推荐生产）
+ • **KMIP 兼容的 KMS**（如 HashiCorp Vault、AWS KMS、Azure Key Vault）

* • 所有数据页（data pages）和日志记录（journal entries）均包含 **CRC32 校验和**

> 🟡 **社区版不支持此功能**。

（2）**客户端字段级加密**（Client-Side Field Level Encryption, CSFLE）

* • **社区版和企业版均支持**（从 4.2 起）。
* • **敏感字段**（如身份证、手机号、银行卡号）在**应用层加密后写入数据库**。
* • 即使 DBA 或攻击者直接读取磁盘文件，也无法解密明文。
* • 支持自动加密/解密（通过 `mongocryptd` 或本地库）。

| Mongodb的功能 | 社区版 | 企业版 | Atlas |
| --- | --- | --- | --- |
| TLS/SSL 传输加密 | ✅ | ✅ | ✅（默认启用） |
| 静态加密（WiredTiger） | ❌ | ✅ | ✅（默认启用） |
| 客户端字段加密（CSFLE） | ✅ | ✅ | ✅ |
| 审计日志 | ❌ | ✅ | ✅（M10+） |
| 校验和（完整性） | ✅ | ✅ | ✅ |

# 六、数据备份恢复

## 6.1 本地备份

MongoDB **本身不内置自动备份策略管理界面**。备份通常由以下方式实现：

* • 手动使用 `mongodump`
* • 脚本 + cron 定时任务
* • 使用 **MongoDB Ops Manager / Cloud Manager**（企业级工具）

配合访谈进行判断。

## 6.2 异地备份

访谈，是否存在异地备份，且备份是否符合异地备份要求。

## 6.3 冗余配置

访谈，是否存在冗余配置，且配置是否符合冗余配置要求。

---

关注公众号"汤池杂货铺"，回复关键字"等级保护"，即可得到PDF文件的下载地址。大家有好的建议，也欢迎给我留言。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dSzSPyBA1LoBjEgicsoXtlzNJxuzHI7JD2icNnltd132TVHpzgbC0VjCSsicAWichvvMzhhlRjTYjicHsYPj4Pzf7FQ/0?wx_fmt=png)

Sec Online

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dSzSPyBA1LoBjEgicsoXtlzNJxuzHI7JD2icNnltd132TVHpzgbC0VjCSsicAWichvvMzhhlRjTYjicHsYPj4Pzf7FQ/0?wx_fmt=png)

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