---
title: 网传微软Autodiscover服务对example.com域名疑似存在处理不当
url: https://mp.weixin.qq.com/s/_bgMemcXClFyaLKk6iC70g
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:49:21.124580
---

# 网传微软Autodiscover服务对example.com域名疑似存在处理不当

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkoz0a747s24U2icHQVMtPUKhaPFib5Y8cvQ6SYr2A9qZmXSDufQiban8DbXiax2SLV6icyIuyeictuZ6HSg/0?wx_fmt=jpeg)

# 网传微软Autodiscover服务对example.com域名疑似存在处理不当

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

外网研究人员发现了一个情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkoz0a747s24U2icHQVMtPUKhoM0B4rRPwyu8plicT4f5vFgicH78tQVvq5ibM2GSg4Lh3eFsDY2cCzNnQ/640?wx_fmt=png&from=appmsg)

#

# 至少从 2020 年 2 月起，微软的自动发现（Autodiscover）服务就错误地将互联网号码分配局（IANA）保留的`example.com`域名路由至住友电气工业株式会社（Sumitomo Electric Industries）位于 sei.co.jp 的邮件服务器，可能导致测试凭证被发送至该服务器。）

example.com：

由IANA（Internet Assigned Numbers Authority，互联网号码分配局）保留的特殊域名，专用于技术文档、教程和示例代码中。它不属于任何真实实体，也不应解析到任何真实的服务器或邮件服务。为了明确表示它不接受邮件，example.com 设置了“null MX记录”（MX优先级为0，指向“.”），这是标准做法，告诉邮件系统“此域名不收邮件”。

Autodiscover：

Microsoft Exchange 和 Outlook 提供的自动发现服务。用户输入邮箱地址（如email@example.com）后，Outlook 会自动查询服务器配置，包括IMAP/SMTP服务器地址、端口、加密方式等，从而免去手动设置。该服务会依次尝试多种发现方式：DNS记录（SRV、CNAME、MX）、HTTP API 调用等。

Microsoft Autodiscover API：

Outlook 在DNS查询失败后，会回退到Microsoft自己的云端数据库（prod.autodetect.outlook.cloud.microsoft），通过HTTPS请求获取配置。这个数据库包含大量域名的“固定配置”（fixed database），部分来自众包，部分由Microsoft手动维护。

如果Autodiscover返回错误的服务器地址，用户在测试或误操作时输入的凭证（用户名+密码）可能被发送到第三方服务器，导致凭证泄露。即使是使用example.com做测试，也可能无意中把测试密码泄露给错误的目标。

问题描述

当在 Outlook（Windows 和 macOS 系统均适用）中设置`email@example.com`作为虚拟测试账户时，Outlook 始终会自动将其配置为使用`imapgms.jnet.sei.co.jp`（IMAP 协议）和`smtpgms.jnet.sei.co.jp`（SMTP 协议）服务器。但事实上，`example.com`是 IANA 专门保留的域名，本不应解析到任何真实的网络服务。

这一异常现象在不同设备、用户配置文件、网络环境以及 DNS 解析器中均有出现，包括新配置的 Windows 365 云电脑：

DNS验证

确认example.com没有指向以下位置的 DNS 记录sei.co.jp：

```
% dig MX example.com +short0 .% dig CNAME autodiscover.example.com +short(no response)% dig SRV _autodiscover._tcp.example.com +short(no response)
```

该域的 MX 记录为空（表示它不接受电子邮件），并且没有自动发现 DNS 条目，这证实了配置错误完全存在于 Microsoft 的数据库中。

Microsoft Autodiscover API 响应

可以通过以下方式确认微软自动发现服务配置错误

```
curl -v -u "email@example.com:password" "https://prod.autodetect.outlook.cloud.microsoft/autodetect/detect?app=outlookdesktopBasic"
```

完整输出

```
* Host prod.autodetect.outlook.cloud.microsoft:443 was resolved.* IPv6: (none)* IPv4: 172.169.69.94*   Trying 172.169.69.94:443...* Connected to prod.autodetect.outlook.cloud.microsoft (172.169.69.94) port 443* ALPN: curl offers h2,http/1.1* (304) (OUT), TLS handshake, Client hello (1):*  CAfile: /etc/ssl/cert.pem*  CApath: none* (304) (IN), TLS handshake, Server hello (2):* (304) (IN), TLS handshake, Unknown (8):* (304) (IN), TLS handshake, Certificate (11):* (304) (IN), TLS handshake, CERT verify (15):* (304) (IN), TLS handshake, Finished (20):* (304) (OUT), TLS handshake, Finished (20):* SSL connection using TLSv1.3 / AEAD-AES256-GCM-SHA384 / [blank] / UNDEF* ALPN: server accepted h2* Server certificate:*  subject: C=US; ST=WA; L=Redmond; O=Microsoft Corporation; CN=autodetect.outlookmobile.com*  start date: Nov  1 12:31:46 2025 GMT*  expire date: Jan 30 12:31:46 2026 GMT*  subjectAltName: host "prod.autodetect.outlook.cloud.microsoft" matched cert's "*.autodetect.outlook.cloud.microsoft"*  issuer: C=US; O=Microsoft Corporation; CN=Microsoft Azure RSA TLS Issuing CA 03*  SSL certificate verify ok.* using HTTP/2* Server auth using Basic with user 'email@example.com'* [HTTP/2] [1] OPENED stream for https://prod.autodetect.outlook.cloud.microsoft/autodetect/detect?app=outlookdesktopBasic* [HTTP/2] [1] [:method: GET]* [HTTP/2] [1] [:scheme: https]* [HTTP/2] [1] [:authority: prod.autodetect.outlook.cloud.microsoft]* [HTTP/2] [1] [:path: /autodetect/detect?app=outlookdesktopBasic]* [HTTP/2] [1] [authorization: Basic ZW1haWxAZXhhbXBsZS5jb206cGFzc3dvcmQ=]* [HTTP/2] [1] [user-agent: curl/8.7.1]* [HTTP/2] [1] [accept: */*]> GET /autodetect/detect?app=outlookdesktopBasic HTTP/2> Host: prod.autodetect.outlook.cloud.microsoft> Authorization: Basic ZW1haWxAZXhhbXBsZS5jb206cGFzc3dvcmQ=> User-Agent: curl/8.7.1> Accept: */*> * Request completely sent off< HTTP/2 200 < content-type: application/json; charset=utf-8< date: Mon, 08 Dec 2025 21:32:58 GMT< server: Kestrel< strict-transport-security: max-age=2592000< x-olm-source-endpoint: /detect< x-provider-id: seeatest< x-debug-support: eyJkZWNpc2lvbiI6ImF1dG9EdjIgPiBhdXRvRHYxID4gZml4ZWQgZGIgcHJvdmlkZXIgPiBmaXhlZCBkYiBkb21haW4gcHJvdG9jb2xzID4gZGIgcHJvdmlkZXIgPiBkYiBkb21haW4gcHJvdG9jb2xzIiwiYXV0b0QiOnsidjIiOm51bGwsInYxIjpudWxsfSwiZGIiOnsicHJvdmlkZXIiOnsiRG9tYWluSWQiOm51bGwsIklkIjoic2VlYXRlc3QiLCJTZXJ2aWNlIjpudWxsLCJQcm90b2NvbHMiOlt7InByb3RvY29sIjoic210cCIsIkRvbWFpbiI6bnVsbCwiSG9zdG5hbWUiOiJzbXRwZ21zLmpuZXQuc2VpLmNvLmpwIiwiUG9ydCI6NDY1LCJFbmNyeXB0aW9uIjoiU3NsIiwiSXNDcm93ZHNvdXJjZWQiOm51bGwsIkZlZWRiYWNrcyI6bnVsbCwiSW5zZWN1cmUiOm51bGwsIlNlY3VyZSI6IlRydWUiLCJVc2VybmFtZSI6IntlbWFpbH0iLCJWYWxpZGF0ZWQiOmZhbHNlLCJBdXRvZGlzY292ZXIiOm51bGwsIkFhZCI6bnVsbH0seyJwcm90b2NvbCI6ImltYXAiLCJEb21haW4iOm51bGwsIkhvc3RuYW1lIjoiaW1hcGdtcy5qbmV0LnNlaS5jby5qcCIsIlBvcnQiOjk5MywiRW5jcnlwdGlvbiI6IlNzbCIsIklzQ3Jvd2Rzb3VyY2VkIjpudWxsLCJGZWVkYmFja3MiOm51bGwsIkluc2VjdXJlIjpudWxsLCJTZWN1cmUiOiJUcnVlIiwiVXNlcm5hbWUiOiJ7ZW1haWx9IiwiVmFsaWRhdGVkIjpmYWxzZSwiQXV0b2Rpc2NvdmVyIjpudWxsLCJBYWQiOm51bGx9XSwiQ3JlYXRlZEF0IjoiMjAyMC0wMi0wM1QwNTozMToyMy4yOTgwMjQ4IiwiVXBkYXRlZEF0IjoiMjAyMC0wMi0wM1QwOToxMjo1OS4wMjQ1ODciLCJQcmVkaWNhdGVzIjpudWxsLCJBdXRvRHYyRW5kcG9pbnQiOm51bGwsIkNvbW1lbnQiOm51bGwsIkZlZWRiYWNrcyI6bnVsbCwiSXNDcm93ZHNvdXJjZWQiOmZhbHNlfSwiZG9tYWluIjp7ImZpeGVkIjpmYWxzZSwiYXV0b0R2MkVuZHBvaW50IjpudWxsLCJwcm92aWRlcklkIjoic2VlYXRlc3QiLCJwcm90b2NvbHMiOm51bGx9fX0=< x-autodv2-error: ENOTFOUND< x-feedback-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJEIjoiZXhhbXBsZS5jb20iLCJQSSI6InNlZWF0ZXN0IiwiUyI6W10sIlAiOlsiaW1hcHM6Ly9pbWFwZ21zLmpuZXQuc2VpLmNvLmpwOjk5MyIsInNtdHBzOi8vc210cGdtcy5qbmV0LnNlaS5jby5qcDo0NjUiXSwiUFQiOiJpbWFwIHNtdHAiLCJleHAiOjE3NjUyMzMxNzgsImlhdCI6MTc2NTIyOTU3OH0.-ohD7c9hytRZK_b4EJ0M5Tke7hl8u1wjsMYRV71GZik< x-dns-prefetch-control: off< x-frame-options: SAMEORIGIN< x-download-options: noopen< x-content-type-options: nosniff< x-xss-protection: 1; mode=block< x-instance-id: autodetect-deployment-76fffc487d-wfs4b< x-response-time: 3472 ms< x-request-id: f1b6525f-6d11-4add-a0e4-0b677d89f9eb< x-autodetect-cv: f1b6525f-6d11-4add-a0e4-0b677d89f9eb< * Connection #0 to host prod.autodetect.outlook.cloud.microsoft left intact{"email":"email@example.com","services":[],"protocols":[{"protocol":"imap","hostname":"imapgms.jnet.sei.co.jp","port":993,"encryption":"ssl","username":"email@example.com","validated":false},{"protocol":"smtp","hostname":"smtpgms.jnet.sei.co.jp","port":465,"encryption":"ssl","username":"email@example.com","validated":false}]}%
```

Json响应

```
{   "email": "email@example.com",   "services": [],   "protocols": [     {       "protocol": "imap",       "hostname": "imapgms.jnet.sei.co.jp",       "port": 993,       "encryption": "ssl",       "username": "email@example.com",       "validated": false     },     {       "protocol": "smtp",       "hostname": "smtpgms.jnet.sei.co.jp",       "port": 465,       "encryption": "ssl",       "username": "email@example.com",       "validated": false     }   ] }
```

解码后的debug header

头部信息x-debug-support（Base64解码后）揭示了更多细节：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkoz0a747s24U2icHQVMtPUKhc7wnk6uRFzicQu4Pu1rmodyL3k8daWLfJUPvMYnxkfzwxkzrJ4ynNUw/640?wx_fmt=png&from=appmsg)

这意味着，Microsoft的固定数据库错误地将example.com关联到日本住友电气工业（Sumitomo Electric Industries）的邮件服务器（\*.jnet.sei.co.jp），这个错误从2020年2月开始存在，至今近6年未修复，且并非众包数据，而是手动添加。

在 Microsoft Autodiscover 服务（主要用于 Outlook 等客户端自动配置邮箱）的上下文中，众包（crowdsourcing） 指的是该服务维护的一个中央域名配置数据库中，部分配置条目是通过“大众贡献”或自动上报机制收集而来的，而不是全部由 Microsoft 内部手动维护。

Autodiscover 数据库的基本工作原理Microsoft 的 Autodiscover 不只依赖 DNS 记录（MX、SRV 等）或本地 Exchange 服务器。对于某些域名（尤其是第三方邮件提供者），它会查询一个云端中央数据库

（通过 API

如 prod.autodetect.outlook.cloud.microsoft/autodetect/detect），返回预存的 IMAP/SMTP/Exchange 配置信息，帮助客户端快速自动设置。这个数据库包含大量域名的“已知良好配置”，目的是提升用户体验（减少手动输入服务器地址）。

IsCrowdsourced: true（众包来源）：

配置信息很可能来自用户客户端的自动上报（telemetry-like 机制）。

当大量 Outlook 用户成功配置某个域名（如某个小邮件提供者的服务器地址）时，客户端可能匿名上报成功的配置细节到 Microsoft 服务器。

这些数据经过聚合、验证后，进入数据库，帮助后续用户（类似“众人拾柴火焰高”的众包模式）。

...