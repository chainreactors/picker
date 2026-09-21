---
title: pgAdmin 严重认证绕过漏洞：伪造 HTTP 头即可冒充管理员登录
url: https://mp.weixin.qq.com/s/dYsPpa3YYDhaVa6VuKKt3w
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:25:26.278437
---

# pgAdmin 严重认证绕过漏洞：伪造 HTTP 头即可冒充管理员登录

# pgAdmin 严重认证绕过漏洞：伪造 HTTP 头即可冒充管理员登录

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnvibWSSrKiasR1mRicMhBLgfzTViaMOa5nicnstL4oSTOib73sicf4nB6aoyHOh8PSiajtGMN0zyUzicQgroLcxAAYNOfENKnyFbQ78RTOw/640?wx_fmt=png&from=appmsg)

pgAdmin 4 中存在一个严重漏洞：未认证的攻击者只需提供一个恶意的 HTTP 身份头，即可冒充任意用户——包括已有的管理员账户。

该漏洞编号为 CVE-2026-86863，影响使用 pgAdmin **Webserver** 认证模式的部署环境，CVSS 3.1 评分为 9.8（满分 10）。受影响的版本为 pgAdmin 4 的 6.2 至 9.17，官方已在 9.18 版本中完成修复。

### pgAdmin 严重认证绕过漏洞

pgAdmin 的 Webserver 认证源，原本是为“由上游 Web 服务器或反向代理先完成用户认证、再将请求转发给 pgAdmin”的部署场景设计的。上游组件会通过 CGI 或 WSGI 环境变量，把已认证的用户名传递给 pgAdmin。

但问题在于，存在漏洞的实现未能可靠地区分“可信服务器提供的环境变量值”与“远程客户端通过 HTTP 头直接提交的身份值”。

`WebserverAuthentication.get_user()` 函数会先尝试从请求环境中读取配置好的 `WEBSERVER_REMOTE_USER` 值；如果查找失败，就会回退（fallback）到从传入的请求头中读取同名项。

由于 HTTP 请求头完全由发送方控制，只要能访问 pgAdmin 实例，攻击者就可以构造一个包含目标账户用户名的头，从而在无需密码、多因素认证或其他有效凭据的情况下，以该账户身份完成登录。

如果管理员将 `WEBSERVER_REMOTE_USER` 配置成了带 `HTTP_` 前缀或含连字符的值（例如 `HTTP_X_FORWARDED_USER` 或 `X-Forwarded-User`），风险会进一步加剧。因为 WSGI 服务器通常会把客户端提供的头以这类名称暴露为环境变量——这意味着，即便还没走到回退逻辑，身份来源本身就可能已被攻击者掌控。

成功利用该漏洞后，攻击者可以获取管理员或其他高权限用户的 pgAdmin 会话。进入系统后，攻击者便有可能查看、篡改或删除该账户有权访问的数据库对象与数据。

该漏洞在两个 CVSS 版本中均被评为“严重”：

| 评分体系 | 严重等级 | 分数 |
| --- | --- | --- |
| CVSS 3.1 | Critical（严重） | 9.8 |
| CVSS 4.0 | Critical（严重） | 9.3 |

CVSS 3.1 向量显示：该漏洞可远程利用、攻击复杂度低、无需任何权限和用户交互，且可能对机密性、完整性和可用性造成重大影响。

需要注意的是，此问题仅在 pgAdmin 的 `AUTHENTICATION_SOURCES` 配置中启用了 webserver 时才会触发。使用其他 pgAdmin 认证机制的组织不受这一特定 Webserver 认证缺陷的影响。

9.18 版本改变了 pgAdmin 处理“断言身份”的方式：更新后的程序会区分真正的 CGI/WSGI 变量与从头派生的值，并且默认只信任前者。

管理员如果确实需要使用头提供的身份，必须显式启用 `WEBSERVER_REMOTE_USER_FROM_HEADER`。同时，该选项应配合 `WEBSERVER_TRUSTED_PROXIES` 的可信代理配置一起使用；部署时还可能需要设置共享密钥头，并通过 `WEBSERVER_SHARED_SECRET` 进行校验。

此外，修复后的代码会检查实际的套接字对端地址，而不再依赖 `request.remote_addr`——后者可能因攻击者操控的 `X-Forwarded-For` 值而被伪造。作为额外防护，pgAdmin 现在还会阻止 Webserver 认证方式登录那些 `auth_source` 未设为 webserver 的账户。

应立即升级到 pgAdmin 9.18（原文写为 4.18，结合上下文应为 9.18）或最新的已修复版本，并审查反向代理的认证设置。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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