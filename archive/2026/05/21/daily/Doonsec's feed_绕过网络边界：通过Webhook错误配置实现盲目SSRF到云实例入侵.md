---
title: 绕过网络边界：通过Webhook错误配置实现盲目SSRF到云实例入侵
url: https://mp.weixin.qq.com/s/DhGrEyrcnNeZucCWRSIvsg
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:05:56.697281
---

# 绕过网络边界：通过Webhook错误配置实现盲目SSRF到云实例入侵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnswxZsHY36GoOiaAiaAYcp6KdqUdePDeWeB7hRDEJicktEt7LsPl2odN7fiaUYcYnfM3Q6fdBoHLfsAUuhjYTZI75VgmLKB4j5H5B4/0?wx_fmt=jpeg)

# 绕过网络边界：通过Webhook错误配置实现盲目SSRF到云实例入侵

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvoaVmlDic5nYicpmTPlUYLpSUTpUicK7NbggXYFmLXjJnHsT5EbBlzrX6dw4qhlaib64X5qma0tTRzwibZZyvibEh0VDvvfYumctk0w/640?wx_fmt=png&from=appmsg)

在对一家一级云通信提供商进行有针对性的基础设施评估时，我发现了其核心配置API中存在的关键服务器端请求伪造（SSRF）漏洞。该漏洞源于未能对用户提供的 webhook URL 进行内部网络范围的验证和净化（RFC 1918 / 云元数据端点）。

通过利用该缺失的验证，攻击者可以迫使平台后端代理基础设施向AWS实例元数据服务（IMDS）发出HTTP请求，从而直接暴露IAM安全凭证，导致整个云环境被攻破。`169.254.169.254`

## 侦察与建筑制图

目标运营一个庞大的分布式API网关，处理数百万实时通信事件（语音、短信、视频）。该平台的核心特性是其异步事件驱动架构。

当配置好的虚拟电话号码收到入站事件（例如短信消息）时，平台后端必须查询客户的基础设施以确定要执行的业务逻辑。它通过**Webhooks**实现这一点——向开发者指定的URL发送HTTP或请求。`GET``POST`

## 识别攻击面

我将分析重点放在负责配置虚拟电话号码资产的REST API端点上。具体来说，API允许用户通过请求修改现有电话号码的配置。`POST`

端点接受多个参数，但对该攻击向量来说最关键的两个参数是：

* `WebhookUrl`：平台在接收事件时查询的目标URL。
* `WebhookMethod`：用于查询的HTTP方法（或）。`GET``POST`

目标是确定后端验证解析器是否正确执行了将公共可路由IP空间与受限内部网络空间分隔的安全边界。

## 脆弱性分析：突破界限

在加固云环境中，用户提供的 URL 必须严格按照内部 IP 范围的拒绝列表（例如 、 、 ）进行验证，才能被出站代理保存或解析有效载荷。`10.0.0.0/8``127.0.0.0/8``169.254.169.254`

我制定了一个针对AWS IMDS端点的有效载荷，具体目标是提取分配给托管API代理的底层EC2实例的临时STS（安全令牌服务）凭证：

`http://169.254.169.254/latest/meta-data/iam/security-credentials/`

## 注射

我通过使用 curl 的标准配置更新请求提交了有效载荷

```
POST /v1/Accounts/ACC_REDACTED/PhoneNumbers/PN_REDACTED HTTP/1.1
Host: api.redacted-target.com
Authorization: Bearer [REDACTED_TOKEN]
Content-Type: application/x-www-form-urlencoded

WebhookUrl=http://169.254.169.254/latest/meta-data/iam/security-credentials/&WebhookMethod=GET
```

## 绕行公路

预期的行为是立即或特定的验证错误，提示内部IP被禁止。相反，API 返回了 ，确认有效载荷已被接受并写入数据库：`HTTP 400 Bad Request``HTTP 200 OK`

```
{
"account_id":"ACC_REDACTED",
"phone_number":"+15550000000",
"id":"PN_REDACTED",
"webhook_method":"GET",
"webhook_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/",
"status":"active"
}
```

这证实了一个关键缺陷：**输入验证要么缺失，要么在配置层根本失效。**

## 利用：将API武器化

恶意 webhook 成功分阶段后，最后一步是执行。

由于这是一个异步SSRF，有效载荷在特定事件（入站短信或语音通话）触发前保持休眠状态。

为了执行负载，攻击者只需向已配置的电话号码发送短信（）。此操作将事件放入目标内部消息总线，触发后端工作者获取配置后向 发送 HTTP 请求。`+15550000000``webhook_url``GET``169.254.169.254`

*（注：在我具体测试阶段，入站触发器被供应商的免费试用反滥用限制禁用。然而，作为漏洞赏金分流的标准做法，演示验证绕过功能使厂商的安全工程师能够在无限制账户内部复制执行，证明其全部影响。*

## 影响评估

如果触发，内部EC2代理服务器会对本地AWS元数据服务执行HTTP GET请求。由于应用程序未强制执行IMDSv2（需要特定头部），请求成功。

IMDS的响应包含临时IAM凭证。

```
{
  "Code" : "Success",
"LastUpdated" : "2026-05-19T12:00:00Z",
"Type" : "AWS-HMAC",
"AccessKeyId" : "ASIA...",
"SecretAccessKey" : "...",
"Token" : "...",
"Expiration" : "2026-05-19T18:00:00Z"
}
```

这些凭据可以通过盲目SSRF泄露技术（例如触发带有数据的DNS查询）提取，或者在响应导致应用崩溃时检查厂商内部错误日志来提取。

**严重程度：高/危急**破坏核心基础设施代理服务器的IAM角色通常会导致：

* **特权升级：**

  访问包含个人信息、客户通信或专有源代码的内部S3桶。
* **侧向移动：**

  转向受限的内部VPC。
* **数据泄露：**

  完全破坏了租户隔离边界。

## 修复策略

1. **严格输入验证（应用层）：**实现一个严格的 URL 解析库，将用户提供的域名解析为其 IP 地址，并在执行外发请求前明确阻止所有解析至 RFC 1918、RFC 5735 及网络的请求。`169.254.0.0/16`
2. **网络出口过滤（网络层）：**

   Webhook 调度服务器（工作节点）应放置在隔离的 VPC 子网中。安全组和NACL必须配置为丢弃所有发向内部范围的出站流量，只允许流向公共互联网的流量。
3. **强制执行IMDSv2（云层）：**在整个AWS舰队中强制使用IMDSv2。IMDSv2 要求请求具有特定头部的请求来生成会话令牌，有效抵消基于 的 SSRF 攻击对元数据服务的攻击。`PUT``X-aws-ec2-metadata-token``GET`

祝你狩猎愉快，务必测试webhook！

* ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvlMvRXpqJ0lx1NibvpNubN7A9nxpnrLqEp2CUsicSzC8tfFOwL4EDcsl5wObB3JoRKsic75icFNt84OLI6z55jfTNgjTpgPKvXTOU/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnttMfia7IORVviaEzC91lUBic1onLfibxdibDSoNXF4hbic6hvZ6ic30ZW1EW2Ds27UlsZWLF6GkiceRk3PsQuoFK7Lqo0bFHR60hibG0RA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ 公众号:安全狗的自我修养
+ vx:2207344074
+ http://gitee.com/haidragon
+ http://github.com/haidragon
+ bilibili:haidragonx

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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