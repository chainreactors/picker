---
title: 每日安全动态推送(26/1/27)
url: https://mp.weixin.qq.com/s/4WlLf8uQX2AaXjuXvvxYlQ
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:33:21.820376
---

# 每日安全动态推送(26/1/27)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/1/27)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器中沉浸阅读

•  SmarterMail 特权账户接管漏洞被利用导致远程代码执行
<https://www.huntress.com/blog/smartermail-account-takeover-leading-to-rce>

本文详细分析了SmarterMail中的特权账户接管漏洞（CVE-2026-23760）在现实中的利用情况，揭示了攻击者如何通过自动化手段实现远程代码执行，其技术深度和对攻击链的还原极具参考价值。

•  Vivotek严重漏洞可导致远程任意代码执行
<https://gbhackers.com/vivotek-flaw-allows-code-injection/>

本文揭示了Vivotek物联网摄像头中的一个严重命令注入漏洞（CVE-2026-22755），攻击者可未经认证远程执行任意代码并取得root权限。研究者利用AI驱动的逆向工程发现该漏洞，凸显了物联网设备在安全设计上的严重缺陷，值得立即引起行业重视。

•  Cloudflare ACME 验证漏洞绕过 WAF 保护
<https://sectoday.tencent.com/event/AQo64psBVJfJhgnJzUSB>

2025年10月，FearsOff 安全研究人员发现 Cloudflare 的 ACME 验证逻辑中存在一个漏洞，攻击者可利用该漏洞绕过 Web 应用程序防火墙 (WAF) 保护，通过访问 /.well-known/acme-challenge/ 路径，直接访问后端服务器和敏感文件。该漏洞源于对 HTTP-01 验证令牌的处理不当，导致 WAF 规则被绕过。Cloudflare 已发布修复程序，确保只有合法的 ACME 挑战请求才会导致 WAF 规则被暂时禁用。此漏洞被归类为零日漏洞，尽管未发现被恶意利用的证据，但其潜在风险极高。

•  Anthropic Git MCP 服务器远程代码执行漏洞
<https://sectoday.tencent.com/event/cwo25ZsBVJfJhgnJZZc->

研究人员在 Anthropic 的 Model Context Protocol (MCP) Git 服务器 mcp-server-git 中发现了多个安全漏洞，这些漏洞源于路径验证不足、参数注入和提示注入等问题。攻击者可利用这些漏洞远程执行代码、读取或删除任意文件，而无需直接访问目标系统。最严重的漏洞涉及 Git 过滤器配置，攻击者可通过恶意 Git 仓库或修改后的请求触发代码执行。Anthropic 已在 2025.9.25 和 2025.12.18 的版本中修复这些漏洞，建议用户立即升级以避免潜在攻击。

•  维特克斯摄像头严重漏洞允许远程攻击者注入任意代码
<https://cyberpress.org/critical-vivotek-vulnerability/>

本文详细披露了Vivotek摄像头固件中的一个关键命令注入漏洞（CVE-2026-22755），该漏洞允许未经身份验证的远程攻击者执行任意代码，且利用条件简单，对数十种型号构成严重威胁，对物联网设备安全开发具有警示意义。

•  GNU InetUtils 严重漏洞允许通过“-f root”绕过认证获取 root 权限
<https://cyberpress.org/critical-gnu-inetutils-vulnerability-allows-unauthenticated-root-access-via-f-root/>

本文揭示了 GNU InetUtils telnetd 服务器中一个十年未被发现的严重远程认证绕过漏洞，攻击者可直接通过恶意环境变量获取 root 权限，技术细节详实且具有高度现实威胁，值得立即关注。

•  新型Kerberos中继攻击利用DNS CNAME记录绕过防护措施，PoC已发布 | CN-SEC 中文网
<https://cn-sec.com/archives/4929739.html>

本文详细揭示了一种利用DNS CNAME记录绕过Kerberos防护的新型中继攻击技术，成功扩大了Active Directory的攻击面，且PoC工具已公开，具有高度现实威胁和研究价值。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dWDic6IAXZscHNXzE9ZruCNhiaPu6reXLhIWJ6icXrZLfG5x573g6hShBFWpKN4qXDQ5aHPMHKxLnVvNHNFhFc76A/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

腾讯玄武实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

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