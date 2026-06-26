---
title: 社区实战成果速递｜CyberStrikeAI 交流 5 群开放
url: https://mp.weixin.qq.com/s/HaZfF_THXmjjK53LDlxL9g
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:05:11.262445
---

# 社区实战成果速递｜CyberStrikeAI 交流 5 群开放

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ufQ2xnAD33t0vqx1gQqLahibZwbpsI1JB8rBicOCtebIGKXGiaUBha1M1tfmyKOhTPjup4kqZicyxIVzWJC4LFE4HZ6EIUt632tgAP3Fia4Tnsuo/0?wx_fmt=jpeg)

# 社区实战成果速递｜CyberStrikeAI 交流 5 群开放

原创

学安全也就图一乐
学安全也就图一乐

低调学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33tKKftqqXYnLQS7VAxsYxRKcsyloyUAVp9MVQEEh2KoGLYGXRpWEWSPRSgLJTwPtUxkWoncyMcwPn0dQDUKQqic41lMSNh6nEBk/640?wx_fmt=jpeg&from=appmsg)

近期社区用户在授权测试中分享了一批实战成果，整理如下。前 1～4 群已满，**CyberStrikeAI 交流 5 群**现已开放，入群二维码见文末。

---

## 平台运行数据

社区用户分享的仪表盘截图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33vIwibhkkYINic67jkkClZS2yNrdqOL6bOE2Ie2IictibKAF2JuUHYefaiaHQ2JhHGN7ILUOmx9rsUosGOB1B43CygT1qIwNgou9X2A/640?wx_fmt=png&from=appmsg)

系统仪表盘概览

| 指标 | 数据 | 说明 |
| --- | --- | --- |
| 工具调用 | **100,746 次** | 98 种工具，批量任务并行执行 |
| 执行成功率 | **90.4%** | 失败 9,708 次 |
| 漏洞发现 | **698 个** | 严重 184、高危 190、中危 228，加权风险分 3203+ |
| 并发任务 | 7 个运行中 | 另有 3 个待执行 |

---

## 实战成果

以下均为**合法授权**场景下的测试结果，目标信息已脱敏。

### 1. 支付系统渗透

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33v7yziawr9HxugzbRfEqSceCAkdPHBqKfjbuUBOyAlibSTW7Bl8N3EkkiaQibRuVc4Kjx3WzZ2GIT0SwkmONMK36Ct9O1fkYvGPgzE/640?wx_fmt=png&from=appmsg)

支付系统渗透测试成果

**CRITICAL：**

* 聚合支付后台 443 端口默认口令，后台被完全接管
* 商户 MD5 密钥、第三方支付 RSA 私钥泄露
* 级联攻击链配置暴露，可继续获取其他密钥

**HIGH：**

* 443 管理通道配置泄露：活跃支付实例密钥、22 条历史订单、USDT-TRC20 结算地址
* Geetest 验证码绕过且无速率限制，epay 实例商户登录可被暴力破解
* SDCMS 存储型 XSS 绕过 WAF，已部署 WebShell 上传载荷
* XFF 伪造绕过 IP 锁定

**攻击面扩展：** 发现第 4 个独立 epay 实例、SSL 证书关联、cronkey 泄露。

从默认口令入手，逐步扩展到密钥泄露和攻击面映射，整条链路在一次会话中完成。

---

### 2. 业务系统高危漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33uVqNDiaTAzvM9dnXGZWSN2sk0yYhdAHdmFx7UYtdbZrBnPtialaJLVpRqRLGrvMEfxKqNicps7HiajuV8RGDDRMHEHic5yCTHgGq3s/640?wx_fmt=png&from=appmsg)

高危漏洞清单

| 漏洞类型 | 影响 | CVSS |
| --- | --- | --- |
| Spring Boot Actuator 未授权 | MySQL root | 9.8 |
| HS256 JWT 伪造 | 远程提权 | 9.3 |
| Shiro rememberMe 反序列化 | RCE | 9.5 |
| 任意文件上传 | JSP 写入 tmp，RCE | — |
| /api/preview SSRF | 内网 Tomcat/MySQL | — |
| OSS AK/SK 泄露 | 云存储 CRUD | 9.4 |
| GraphQL 管理员创建 | 可创建 admin | 8.7 |
| SQLi 盲注 | UNION + SLEEP 确认 | 7.5 |
| XSS 存储/反射 | 前端脚本执行 | 6.8 |
| WebSocket CSWSH | 任意来源可握手 | 7.0 |

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vVBQqdu08sZhiaDDaibj4SV7kpTyA3McRY3lS4p8V3oD655ziaQqgIOhPABqUEqvOourIc0poDvke57kujBH0W4puepW9mZYmeQ0/640?wx_fmt=png&from=appmsg)

渗透测试结论

结论：9 个高危漏洞均可短时间利用；MySQL root、OSS 读写、内网服务均有直接利用路径。

---

### 3. 确认漏洞汇总

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vVPnqOcOocJUg56zU6IBWGiao7bib7z0O2GSKGibABnC4LTxJw1j0djUyJDxias128gFgTHWaszDOsSRgPc0DSgTvsAWXK5ubpB5A/640?wx_fmt=png&from=appmsg)

确认漏洞汇总

主要条目：

* **C1** Mock 接口泄露 605 用户 PII（9.8）
* **C2** 支付配置被劫持，重定向至攻击者服务器（9.8）
* **C3** 银行 CRUD 无认证（9.1）
* **C4** 用户注册 API 无认证（9.0）
* **C5** 8000 端口管理网关 32 个服务 Swagger 暴露（8.5）
* **H1** Nacos 泄露：6 命名空间、1935 条配置（7.5）
* **H4** OSS 桶公开可读，3 个桶（6.5）

漏洞已按严重度分级，并标注验证状态（已验证 / 已执行 / 已确认）。

---

### 4. 数据泄露与 RCE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33tGj7IXTLzsOLBeIn1Lyezu9iatlvZ8xicegkFbD4ia7J6j6PBTBlT1zbPz9J7NOpKxUufepwdiavldzverePQgoerc268Q1jXEsC0/640?wx_fmt=png&from=appmsg)

漏洞管理面板

两条严重级记录：

1. 生产环境数据泄露 — 700 万+ 业务数据、363 个用户凭据、客户 PII
2. PostgreSQL 任意文件写入 — RCE 已验证

---

### 5. 双云凭据验证

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vCzT9zFlkJ5EliaCAUV4Cem8ibG8icfIiaKdGJPynJB6yRfPAMy3ibibqEfPtbgp73Dic951gJ6SAwHzQ98D37tOJWhlOw48eOsnQkDw/640?wx_fmt=png&from=appmsg)

双云凭据验证

| 云平台 | 身份 | 验证结果 | 权限 |
| --- | --- | --- | --- |
| 阿里云 | RAM 用户 | STS + ECS API | ECS、STS、DDoS |
| 腾讯云 | 子账号 | Live API | STS 等 |

泄露凭据经 API 调用验证，确认了实际权限范围。

---

## 5 群入群

前 1～4 群已满，5 群开放入群：

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33s88G7aJQ3EVZVl63oPqyqomcLicHG2aN3uGq0M805rdvYLKDrpPJdDRLgW1q72T1ulpdYWUzFQ7f99eibWicpkAIdAeyFicgGoVMg/640?wx_fmt=png&from=appmsg)

CyberStrikeAI 交流 5 群二维码

---

## 声明

文中成果均在**书面授权**前提下完成。CyberStrikeAI 仅用于授权范围内的安全评估与防御加固，请勿用于未授权测试。

---

* **GitHub：** https://github.com/Ed1s0nZ/CyberStrikeAI
* **Discord：** https://discord.gg/8PjVCMu8Zw

*2026 年 6 月 25 日*

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

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