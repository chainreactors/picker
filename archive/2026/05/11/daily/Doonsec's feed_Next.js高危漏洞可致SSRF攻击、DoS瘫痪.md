---
title: Next.js高危漏洞可致SSRF攻击、DoS瘫痪
url: https://mp.weixin.qq.com/s/FNxwrq5MdzBVTUbWfDgR9A
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:34:18.892623
---

# Next.js高危漏洞可致SSRF攻击、DoS瘫痪

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX08gsCTdlB8pZShNqCMlGicCeNg7h8cx6vTm3K8P3uL0M8huXgIqMnlkOC25BhPaN8co6XIncGoGFuVnMy1WwVNpENK6rliayxHU/0?wx_fmt=jpeg)

# Next.js高危漏洞可致SSRF攻击、DoS瘫痪

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0x3vJy30MIyGMibDvLMQReVHJZmWwjhczjGX70AvBYfhGjQvaqwHhRib5MEq8qYTaoMPEUibI5MNLA0MudRcaaufeNErS4kNUa38/640?wx_fmt=png&from=appmsg)

##

Vercel 发布了针对 Next.js 的一系列安全公告，修复了十余个漏洞，包括拒绝服务、中间件绕过、服务端请求伪造（SSRF）和跨站脚本（XSS）等安全问题。这些漏洞影响使用 App Router 的 Next.js 13.x 至 16.x 版本，以及 19.x 版本的 React Server Components 软件包。

##

**Part01**

## ****CVE-2026-23870****

高危拒绝服务漏洞（CVE-2026-23870）影响 19.x 版本的 React Server Components 软件包，以及 13.x、14.x、15.x 和 16.x 版本的所有 Next.js App Router 部署。攻击者向任意 App Router 服务器函数端点发送特制的 HTTP 请求，在反序列化时会触发 CPU 使用率激增，导致未修复环境遭受拒绝服务攻击。

该问题的根源在于 React "Flight" 协议的反序列化逻辑未能对传入的有效负载实施充分的结构或类型约束。

**Part02**

## ****中间件与代理授权绕过漏洞****

三项独立公告（GHSA-267c-6grr-h53f、GHSA-26hh-7cqf-hhc6 和 GHSA-492v-c6pp-mqqv）涉及 App Router 应用程序中的中间件绕过漏洞。特制的 .rsc 和段预取 URL 可以解析到同一页面而不受预期中间件规则匹配，导致未经适当授权检查即可访问受保护内容。

修复方案现已在生成中间件匹配器时包含 App Router 传输变体，确保中间件保护措施一致适用于所有请求类型（包括预取变体）。在升级前，开发者应在底层路由或页面逻辑中直接实施授权，而非仅依赖中间件。

**Part03**

## ****CVE-2026-44578****

高危漏洞（CVE-2026-44578，GHSA-c4j6-fc7j-m34r）允许攻击者通过特制 WebSocket 升级请求在自托管 Node.js 部署中实施服务端请求伪造（SSRF）。攻击者可操纵服务器将请求代理至任意内部或外部目标，可能暴露内部服务或云元数据端点，这对云原生环境尤为危险。

Vercel 托管的部署明确标明不受影响。修复方案对 WebSocket 升级处理应用了与标准 HTTP 请求相同的安全检查。

**Part04**

## ****CVE-2026-44573****

CVE-2026-44573（GHSA-36qx-fr4f-26g5）影响使用 Pages Router 并配置了 i18n 及基于中间件授权的应用程序。无区域设置的 /\_next/data/<buildId>/<page>.json 请求会完全绕过中间件，使攻击者无需通过授权检查即可获取受保护页面的服务端渲染 JSON。

匹配器逻辑已更新，确保在带前缀和不带前缀的数据路由上应用一致的匹配规则。

除高危漏洞外，Vercel 还修复了多个中低危问题，包括：

* 使用 CSP nonce 的 App Router 应用程序中的 XSS 漏洞（GHSA-ffhc-5mcf-pf4q）
* 含不可信输入的 beforeInteractive 脚本中的 XSS 漏洞（GHSA-gx5p-jg67-6x7h）
* 图像优化 API 中的拒绝服务漏洞（GHSA-h64f-5h5j-jqjh）
* React Server Component 响应中的缓存投毒问题（GHSA-wfc6-r584-vfw7、GHSA-vfv6-92ff-j949）
* 缓存组件中的连接耗尽拒绝服务漏洞（GHSA-mg66-mrh9-m8jx）
* 中间件重定向的缓存投毒问题（GHSA-3g8h-86w9-wvmq）

运行受影响 Next.js 版本的组织应优先立即升级。对于无法立即升级的团队，建议采取以下临时缓解措施：

* 在单独的路由或页面逻辑中实施授权，而非仅依赖中间件
* 在反向代理或负载均衡器层面阻止 WebSocket 升级
* 限制服务器出口流量至已知内部网络

**参考来源：**

Multiple Critical Vulnerabilities Patched in Next.js and React Server Components

https://cybersecuritynews.com/next-js-react-server-vulnerabilities/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

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