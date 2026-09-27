---
title: RabbitMQ 四连爆：XSS + 密钥泄露 + 认证 DoS + 路由 DoS
url: https://mp.weixin.qq.com/s/pLZ_qnbvPmtgZ0KY02kFXw
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:22:46.162897
---

# RabbitMQ 四连爆：XSS + 密钥泄露 + 认证 DoS + 路由 DoS

# RabbitMQ 四连爆：XSS + 密钥泄露 + 认证 DoS + 路由 DoS

撅人

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

RabbitMQ 四连爆：XSS + 密钥泄露 + 认证 DoS + 路由 DoS

CVE-2026-67237 · CVE-2026-67409 · CVE-2026-67410 · CVE-2026-67419 | CVSS 7.1~8.2 分 | 披露时间 2026-09-25

1

漏洞速览

CVE 编号CVE-2026-67237 / CVE-2026-67409 / CVE-2026-67410 / CVE-2026-67419

漏洞类型XSS / 密钥泄露 / 认证 DoS / 路由引擎 DoS

影响产品RabbitMQ Server

安全等级High（高危）

CVSS v4.07.1 ~ 8.2

披露时间2026-09-25

影响版本3.13.0 ~ 4.3.4（多系列）

修复版本各分支不同版本，见第五章

利用情况部分无需认证/无需权限，利用门槛低

EUVD 收录CVE-2026-67409（EUVD-2026-87159）

2

漏洞概述

RabbitMQ 是全球最流行的开源消息队列中间件，广泛应用于微服务架构和分布式系统。2026 年 9 月 25 日，RabbitMQ 安全团队在同一天公布了 **四个高危漏洞**，CVSS v4.0 评分在 **7.1 ~ 8.2 分** 之间，其中 CVE-2026-67409 被 EUVD（欧盟漏洞数据库）收录。

这四个漏洞涉及**管理界面反射型 XSS**、**OAuth2 客户端密钥明文泄露**、**JWKS 获取导致认证拒绝服务**以及**Topic Exchange 路由引擎 DoS**。影响范围覆盖 RabbitMQ 3.13.0 至 4.3.4 等多个活跃版本。

**攻击面评估：**其中 CVE-2026-67409 和 CVE-2026-67410 **无需认证、无需任何权限**，任何网络可达用户均可触发；CVE-2026-67419 仅需普通租户权限（队列 configure、交换 read/write），不需要管理员权限。这意味着在实际生产环境中，攻击者可以利用的入口非常广泛。

3

详细漏洞分析

CVE-2026-67237 — 管理界面反射型 XSS（CVSS 7.5）

**CWE-79** · **GHSA-2rf7-f6r6-8rwh** · 影响：4.2.0~4.2.7 / 4.3.0~4.3.1 · 修复：4.2.8 / 4.3.2

**第一层：底层概念**

RabbitMQ 管理 UI 支持 OAuth2 认证，启用后管理员通过 Bearer Token 访问管理界面。系统通过 bootstrap.js 端点返回 OAuth 引导脚本，其中会嵌入当前用户的 Token 信息，用于前端 JavaScript 进行身份验证和会话管理。

**第二层：漏洞机制**

set\_token\_auth/2 函数将来自 Authorization 请求头或 access\_token Cookie 的 Bearer Token 以**字符串拼接方式**直接嵌入 JavaScript 中，未进行任何转义处理。攻击者可在 Token 中注入单引号、</script> 或换行符，从而在管理 UI 的 JavaScript 上下文中执行任意代码。

**第三层：攻击链**

**步骤 1** — 攻击者构造恶意 Bearer Token（包含 JavaScript 注入代码）

↓

**步骤 2** — 将 Token 植入 access\_token Cookie 或通过 Authorization 头发送

↓

**步骤 3** — 受害者浏览器请求 bootstrap.js 端点，返回嵌入恶意代码的脚本

↓

**步骤 4** — 恶意脚本在管理 UI 同源上下文中执行，获得管理员会话的完整 HTTP API 访问权限

↓

**步骤 5** — 攻击者可创建管理员用户、导出数据定义、修改策略等

**利用条件：**必须启用 management.oauth\_enabled = true；攻击者需能在管理主机植入 access\_token Cookie（例如通过 sibling 子域或诱导受害者访问受控页面），或通过 Authorization 头路径利用。

CVE-2026-67409 — JWKS 获取忽略 HTTP 状态码导致认证 DoS（CVSS 8.2）

**CWE-252** · **GHSA-qw3h-qqm9-jrw8** · **EUVD-2026-87159** · 影响全系列 3.13.0~4.3.2 · 修复：3.13.18 / 4.0.23 / 4.1.14 / 4.2.9 / 4.3.3

**第一层：底层概念**

RabbitMQ 的 OAuth2/JWT 认证机制依赖 JWKS（JSON Web Key Set）端点获取签名密钥。当收到携带 JWT 的认证请求时，系统会根据 Token 中的 kid（密钥 ID）查找对应的签名密钥来验证签名。JWKS 密钥会被缓存以减少对 IDP 的频繁请求。

**第二层：漏洞机制**

JWKS 密钥获取机制存在三个 Bug：

**Bug 1** — Erlang 模式匹配 {ok, {\_, \_, JwksBody}} 会匹配**任何 HTTP 事务**，无论状态码是 200 还是 500，HTTP 状态码完全被忽略

**Bug 2** — 原始 httpc 响应直接返回，且默认 autoredirect=true 会静默跟随重定向

**Bug 3** — 当新密钥为空时，所有动态 JWKS 密钥被删除，之前缓存的签名密钥被**永久销毁**

**第三层：攻击链**

**步骤 1** — 攻击者发送带未知 kid 的 JWT 到 RabbitMQ 进行 SASL PLAIN 认证

↓

**步骤 2** — RabbitMQ 自动触发 JWKS 刷新

↓

**步骤 3** — 如果此时 JWKS 端点返回含非 keys 字段的 JSON 错误响应（如 {"error":"rate\_limited"}）

↓

**步骤 4** — 所有缓存签名密钥被销毁

↓

**步骤 5** — 所有后续 JWT 认证失败，直到 JWKS 恢复且再次刷新

**单次攻击即可导致整个 RabbitMQ 实例的 OAuth2/JWT 认证永久失效。**

**利用条件：**无需认证，无需权限，任何网络可达用户均可触发。影响全系列 3.13.0 ~ 4.3.2。

CVE-2026-67410 — OAuth2 客户端密钥通过未认证端点泄露（CVSS 8.2）

**CWE-200** · **GHSA-f9f2-q3jf-wfj3** · 影响：4.2.0~4.2.8 / 4.3.0~4.3.2 · 修复：4.2.9 / 4.3.3

**第一层：底层概念**

RabbitMQ 管理 UI 的 OAuth2 认证需要与 IDP（身份提供商）通信，某些 OAuth 流程（如 client\_credentials）需要使用客户端密钥（client secret）进行身份验证。

**第二层：漏洞机制**

路由注册为无认证的 Cowboy 处理器，bootstrap\_oauth 调用 authSettings() 并嵌入 JavaScript，authSettings() 明确包含 oauth\_client\_secret。任何能访问管理 UI 端口的用户均可无需认证直接获取 OAuth2 客户端密钥。

**第三层：攻击链**

**步骤 1** — 攻击者向管理 UI 发送：curl -s http://rabbitmq:15672/js/oidc-oauth/bootstrap.js

↓

**步骤 2** — 响应中直接返回包含 oauth\_client\_secret 明文的 JavaScript 代码

↓

**步骤 3** — 攻击者利用获取的密钥在令牌端点交换访问令牌

↓

**步骤 4** — 冒充 RabbitMQ 管理 UI 与 OAuth2 提供商通信，可能访问该客户端授权的其他资源

**利用条件：**启用 rabbitmq\_management 插件 + management.oauth\_enabled = true + 配置了 management.oauth\_client\_secret。无需认证。

CVE-2026-67419 — 连续主题泛词导致组合路由计算（CVSS 7.1）

**CWE-407 / CWE-1333** · **GHSA-h964-v5mf-22cq** · 影响：4.3.x < 4.3.5 · 修复：4.3.5

**第一层：底层概念**

Topic Exchange（主题交换）使用路由键（routing key）进行消息路由，支持通配符：\* 匹配一个词，# 匹配零个或多个词。例如队列绑定键 order.# 可以接收 order.new、order.new.canceled 等所有以 order 开头的路由键消息。

**第二层：漏洞机制**

认证用户可以将队列绑定到 topic 交换，绑定键中包含**连续的 # 泛词**（如 #.#.#），迫使路由引擎进入组合递归。匹配器在无备忘录的情况下反复重新进入相同的状态，在去重前构建重复结果列表，导致 CPU 工作量和内存压力呈**指数级增长**。

**复杂度分析：**绑定键中包含 n 个连续 # 段与深度为 n 的路由键匹配时，产生的重复结果数为二项式系数 C(2n-1, n-1)：

n=12：重复结果数 1,352,078，匹配器调用 5,200,300 次

n=14：重复结果数 20,058,300，匹配器调用 77,558,760 次

n=16：重复结果数 300,540,195，匹配器调用 1,166,803,110 次

n=127（最大，因 AMQP 0-9-1 短字符串允许键长达 255 字节）：天文数字

**第三层：攻击链**

**步骤 1** — 攻击者创建队列并绑定到 topic 交换，绑定键设为 #.#.# 等连续泛词

↓

**步骤 2** — 向该交换发布消息，路由键设为对应深度（如 a.a.a）

↓

**步骤 3** — 路由引擎开始组合递归计算，重复结果数指数级增长

↓

**步骤 4** — 单个低权限租户即可耗尽共享 Erlang scheduler CPU，使整节点消息路由对所有 vhost 和客户端降级或停止

**利用示例：**

N=12
BK=$(python3 -c "print('.'.join(['#']\*$N))")
RK=$(python3 -c "print('.'.join(['a']\*$N))")
rabbitmqadmin declare exchange name=evilx type=topic
rabbitmqadmin declare queue name=evilq
rabbitmqadmin declare binding source=evilx destination=evilq routing\_key="$BK"
rabbitmqadmin publish exchange=evilx routing\_key="$RK" payload=""

**利用条件：**认证用户，vhost 中具有队列 configure 权限、交换 read 和 write 权限（普通租户正常权限，**无需管理员权限**）。

4

快速自查命令

① 检查 RabbitMQ 当前版本

rabbitmqctl version

若版本在 3.13.0~4.3.4 范围内，可能存在受影响漏洞

② 检查是否启用了 OAuth2

grep -r oauth\_enabled /etc/rabbitmq/

若存在 oauth\_enabled=true，说明启用了 OAuth2 认证

③ 检查 OAuth2 客户端密钥配置

grep -r oauth\_client\_secret /etc/rabbitmq/

若存在配置，存在 CVE-2026-67410 密钥泄露风险

④ 检查管理 UI 端点是否可匿名获取密钥

curl -s http://localhost:15672/js/oidc-oauth/bootstrap.js

若返回包含 oauth\_client\_secret，说明存在 CVE-2026-67410 漏洞

⑤ 检查是否有异常 Topic Exchange 绑定

rabbitmqctl list\_bindings source source\_kind destination destination\_kind routing\_key | grep '#\.'

若存在连续 # 泛词绑定，存在 CVE-2026-67419 路由 DoS 风险

5

修复方案

RabbitMQ 安全团队已修复所有漏洞，请根据当前使用的版本，升级到对应的修复版本：

受影响版本系列 → 最低修复版本

3.13.x 系列 → **3.13.18**

4.0.x 系列 → **4.0.23**

4.1.x 系列 → **4.1.14**

4.2.x 系列 → **4.2.9**

4.3.x 系列 → **4.3.5**

**注意：**CVE-2026-67409 和 CVE-2026-67410 影响 3.13.x、4.0.x、4.1.x、4.2.x、4.3.x 全系列；而 CVE-2026-67419 仅影响 4.3.x 系列且只需升级到 4.3.5。请根据自身版本选择对应的修复版本。

升级操作步骤

**步骤 1：**备份当前 RabbitMQ 数据（队列、交换机、绑定、用户权限）

**步骤 2：**下载对应分支的修复版本，按官方升级流程执行

**步骤 3：**升级完成后验证版本：执行 rabbitmqctl version

**步骤 4：**检查 Web 日志，确认无异常访问请求

**步骤 5：**如有 OAuth2 配置，建议**轮换客户端密钥**

6

安全提醒

启用 OAuth2 的管理 UI 务必配置防火墙白名单

限制可访问管理端口的 IP 范围，避免管理端口暴露在公网，防止 XSS 和密钥泄露漏洞被利用。

定期轮换 OAuth2 客户端密钥

确保密钥存储在服务端安全位置，不要硬编码在配置文件中。轮换密钥可以限制密钥泄露后的攻击窗口。

监控 JWKS 端点的可用性

配置健康检查和告警，避免因 IDP 故障导致 RabbitMQ 认证中断。建议配置超时和降级机制，防止一次性 DoS 造成永久性影响。

对 Topic Exchange 的绑定键实施验证

拒绝包含连续 # 泛词的异常绑定请求，限制最大绑定键长度。建议实现绑定键白名单机制，仅允许合理的路由模式。

遵循最小权限原则

为每个租户分配尽可能少的权限，避免使用管理员账号进行日常操作。CVE-2026-67419 证明普通租户权限即可导致节点级 DoS。

7

漏洞时间线

2026-09-25

RabbitMQ 安全团队在同一天公布四个高危漏洞，涵盖 XSS、密钥泄露、认证 DoS 和路由引擎 DoS

2026-09-25

GitHub Security Advisory 同步发布 GHSA-2rf7-f6r6-8rwh、GHSA-qw3h-qqm9-jrw8、GHSA-f9f2-q3jf-wfj3、GHSA-h964-v5mf-22cq

2026-09-25

各分支修复版本发布：3.13.18 / 4.0.23 / 4.1.14 / 4.2.9 / 4.3.5

2026-09-25

本文发布

8

参考链接

CVE-2026-67237 官方记录（CVE.org）

GHSA-2rf7-f6r6-8rwh（GitHub Advisory）

RabbitMQ 4.2.8 Release Notes

RabbitMQ 4.3.2 Release Notes

CVE-2026-67409 官方记录（CVE.org）

GHSA-qw3h-qqm9-jrw8（GitHub Advisory）

EUVD-2026-87159（欧盟漏洞数据库）

CVE-2026-67410 官方记录（CVE.org）

GHSA-f9f2-q3jf-wfj3（GitHub Advisory）

CVE-2026-67419 官方记录（CVE.org）

GHSA-h964-v5mf-22cq（GitHub Advisory）

RabbitMQ Security Blog

本文信息来源为官方安全公告及第三方安全研究，仅供安全研究参考。实际利用情况可能因环境和配置而异，请及时更新到修复版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/C2LH9pdiblyKiaq0ylL6VeXGicOdEyN1xahCeCJJWRKk8VEgsREoS54m3sUZgbm2b4eLvO0zibPLesDkbhAI6cnGaGibVh0CzVkpQu0hibEWyBVx4/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5FrZh8P1Et1luAmHafwcia2Zd3UicthHC0MpJDxicx7vdBqM9wRS8loBH3TQes70DDK7rRZr25OBEGgXIzPyZXa1Q/0?wx_fmt=png)

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