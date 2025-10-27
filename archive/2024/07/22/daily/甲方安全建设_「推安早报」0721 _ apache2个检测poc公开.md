---
title: 「推安早报」0721 | apache2个检测poc公开
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487637&idx=1&sn=6229121098df1fb61d8329fd41691f72&chksm=fb35b95dcc42304b684e585cae8bda7bf94df3255303709e86078dc1c4146f940858080b2d1c&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-22
fetch_date: 2025-10-06T17:40:45.485111
---

# 「推安早报」0721 | apache2个检测poc公开

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZn2p6s1XVfMoaQYTCUPYkXJBUCPGefmOycYMzZyxcaQWLNDwd41iaF5vZibkdGSOoc94jYP0sBJWxYA/0?wx_fmt=jpeg)

# 「推安早报」0721 | apache2个检测poc公开

bggsec

甲方安全建设

# 2024-07-21 「红蓝热点」每天快人一步

> 1. 推送`「新、热、赞」`，帮部分人`阅读提效`
> 2. 学有`精读浅读深读`，艺有`会熟精绝化`，觉知此事`重躬行`。推送只在`浅读预览`
> 3. 机读为主，人工辅助，每日数万网站，10w推特速读
> 4. 推送可能`大众或小众`，不代表本人偏好或认可
> 5. 因渲染和外链原因，公众号`甲方安全建设`发送`日报`或日期,如`20240721`获取`图文评论版pdf`

### 0x01 Apache HTTP服务器高危漏洞影响版本2.4.0至2.4.61

> GitHub 上的一个仓库（TAM-K592/CVE-2024-40725-CVE-2024-40898）披露了两个高危漏洞（CVE-2024-40725 和 CVE-2024-40898），这些漏洞影响了 Apache HTTP Server 2.4.0 至 2.4.61 版本，可能导致源代码泄露和服务器端请求伪造（SSRF）攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZn2p6s1XVfMoaQYTCUPYkXJ2MuCAeQfbKdic0wwpibVtYazBFzeLxBqiaQKC2moy7gWbYzfBhlxdDOkQ/640?from=appmsg)

### 热评

* Apache HTTP Server 2.4.0 - 2.4.61 版本存在漏洞 CVE-2024-40725 和 CVE-2024-40898
* Apache HTTP Server 2.4.0-2.4.61 版本发现漏洞 CVE-2024-40725 和 CVE-2024-40898

### 关键信息点

* CVE-2024-40725 漏洞的存在是由于 mod\_proxy 模块在处理 ProxyPass 指令和 URL 重写规则时的解析不一致，这可能导致 HTTP 请求欺骗攻击。
* 攻击者可以通过发送精心构造的 HTTP 请求来利用这个漏洞，从而在代理服务器和后端服务器之间造成请求解析的不一致，进而实现信息泄露等攻击。
* CVE-2024-40898 漏洞的危险之处在于，它允许攻击者绕过 mod\_ssl 模块的客户端认证机制，这可能导致未授权的系统访问。
* 对于这两个漏洞，最重要的缓解措施是升级到 Apache HTTP Server 的最新版本，同时对现有的代理和 SSL 配置进行审计和加固，以确保不会因为配置错误而暴露于这些高危漏洞。

🏷️: CVE, SSRF, 漏洞, Apache HTTP服务器, HTTP请求走私

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZlbmEWU7ZApsl3ia3YLicI4H3nwksKq8ZBqrghjtia9TYiblaxU2VXrUpDcAM57Ric0wX9pBg69IusWVyg/640?wx_fmt=jpeg)

快来和老司机们一起学习吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

甲方安全建设

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

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