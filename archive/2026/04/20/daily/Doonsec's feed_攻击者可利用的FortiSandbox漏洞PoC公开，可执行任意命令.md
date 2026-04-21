---
title: 攻击者可利用的FortiSandbox漏洞PoC公开，可执行任意命令
url: https://mp.weixin.qq.com/s/khZpLjWwIB1FvM4jZ_YM8w
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:47:05.081482
---

# 攻击者可利用的FortiSandbox漏洞PoC公开，可执行任意命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2Hwr3lm3v3hDuwvVe5Ne9eOChKfdHfZkcW961iahZZLalDFjibrlmcaJLCj41kCniaws0LhQIM3un64jCYxuW1RjmppJAfo0sFjs/0?wx_fmt=jpeg)

# 攻击者可利用的FortiSandbox漏洞PoC公开，可执行任意命令

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0CAUu1E5oudBmAdEiaUnXI0WmE6aLDWbc3SjHLNxKHTRia0OsbCD0UtXYoSWufoAiaN9SWs1H6uqX6YllTlic5RPIm4RtBiaian9kvk/640?wx_fmt=png&from=appmsg)

##

网络安全研究人员已公开披露针对 Fortinet 旗下 FortiSandbox 产品高危漏洞（CVE-2026-39808）的概念验证（PoC）利用代码。该漏洞允许未经身份验证的攻击者以 root 最高权限执行任意操作系统命令，且无需任何登录凭证。

该漏洞最初于 2025 年 11 月被发现，在 Fortinet 于 2026 年 4 月发布补丁后，现已被公开披露。由于 GitHub 上已出现可用的漏洞利用代码，安全研究人员及防御方应立即部署修复措施。

##

**Part01**

## ****漏洞技术分析****

CVE-2026-39808 是影响 FortiSandbox 的操作系统命令注入漏洞。FortiSandbox 作为广泛使用的沙箱解决方案，主要用于检测和分析高级威胁与恶意软件。该漏洞存在于 /fortisandbox/job-detail/tracer-behavior 端点中。

攻击原理剖析

攻击者可通过 jid GET 参数注入恶意操作系统命令，利用 Unix 系统中常见的管道符号（|）实现命令串联。由于存在漏洞的端点未能正确过滤用户输入，注入的命令会直接被底层操作系统以 root 权限执行。

![通过 jid 参数中的 | 符号实现操作系统命令注入（来源：GitHub）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX33FydK8JI217VZf0jxxPibgpkQp7DJYhm1NxyHyAXYQbZibkVRryggsVh3ibmicHwcqMOxCibSe6VcYEeqmBedXX1ohcYOZvAQ6I4M/640?wx_fmt=jpeg&from=appmsg)

经确认，FortiSandbox 4.4.0 至 4.4.8 版本均受此漏洞影响。该漏洞最令人担忧之处在于其利用难度极低——研究人员 samu-delucas 在 GitHub 发布的 PoC 显示，仅需一条 curl 命令即可实现未经认证的远程代码执行（RCE）：

```
curl -s -k --get "http://$HOST/fortisandbox/job-detail/tracer-behavior" --data-urlencode "jid=|(id > /web/ng/out.txt)|"
```

在此示例中，攻击者将命令输出重定向至 web 根目录下的文件，随后可通过浏览器获取该文件。这意味着攻击者无需登录即可读取敏感文件、植入恶意软件或完全控制主机系统。

**Part02**

## ****厂商响应与缓解措施****

Fortinet 已通过 FortiGuard PSIRT 门户发布编号为 FG-IR-26-100 的安全公告，确认漏洞严重性并列出受影响版本。运行 FortiSandbox 4.4.0 至 4.4.8 版本的组织应立即升级至修复版本。

* 立即修补：按照官方公告指引将 FortiSandbox 升级至 4.4.8 以上版本
* 审计暴露实例：检查 FortiSandbox 管理接口是否暴露于非可信网络或公网
* 审查日志：监控 /fortisandbox/job-detail/tracer-behavior 端点的异常 GET 请求
* 实施网络分段：将 FortiSandbox 管理接口访问权限限制为可信 IP 范围

随着 PoC 的公开，漏洞利用窗口已经打开。安全团队应将其视为最高优先级补丁，立即采取措施保护受影响系统。

**参考来源：**

PoC Exploit Released for FortiSandbox Vulnerability that Allows Attacker to Execute Commands

https://cybersecuritynews.com/poc-exploit-fortisandbox-vulnerability/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1O8uucFibpl8PczsdFCl05VYJ6SAC0hbGnY2ORo3zp7cw9tGtthViaRCO0qTggMtiampGyl7T4RbMmFXECrOhAnNwzV3vBWEBFN0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337048&idx=1&sn=7238361cc36d8446dbd7c8ed85cb2f42&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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