---
title: 1.2万Flowise实例遭高危RCE漏洞攻击，AI平台面临沦陷风险
url: https://mp.weixin.qq.com/s/vT_UWVZBSLn6YgMinZRTjw
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:28:23.699011
---

# 1.2万Flowise实例遭高危RCE漏洞攻击，AI平台面临沦陷风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1viaJVp0CA3rAVf2cR1b9oCaa7vycibsLjOHMynepmrLpsH46AyUdfkt7eCibS7KvYs0dtZlDu9BHzWx8EKPfJpFx4OuHia0fXgm4/0?wx_fmt=jpeg)

# 1.2万Flowise实例遭高危RCE漏洞攻击，AI平台面临沦陷风险

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX123ngIcAx42iaHLlSRXE5waZtgOfXsQTeibFksfk1VxrB415NHjwSxbp8ohfYweDaPc3dh4JX0RRFEFzTianplsuy62S2ibenUX2M/640?wx_fmt=png&from=appmsg)

##

## VulnCheck最新研究显示，威胁攻击者正在利用开源AI平台Flowise中一个最高危安全漏洞（CVE-2025-59528，CVSS评分：10.0）。该代码注入漏洞可导致远程代码执行（RCE）。

##

**Part01**

## ****漏洞技术细节****

Flowise在2025年9月发布的公告中说明："CustomMCP节点允许用户输入连接外部MCP（模型上下文协议）服务器的配置设置。该节点会解析用户提供的mcpServerConfig字符串来构建MCP服务器配置，但在此过程中未进行任何安全验证就执行了JavaScript代码。"

由于该进程以完整的Node.js运行时权限运行，成功利用此漏洞可访问child\_process（命令执行）和fs（文件系统）等危险模块。换言之，攻击者可利用该漏洞在Flowise服务器上执行任意JavaScript代码，导致系统完全沦陷、文件系统被访问、命令被执行以及敏感数据外泄。

"仅需一个API令牌即可利用，这对业务连续性和客户数据构成极大安全风险。"Flowise补充道，并确认漏洞由Kim SooHyun发现和报告。该问题已在npm包的3.0.6版本中修复。

**Part02**

## ****攻击态势分析****

VulnCheck披露的细节显示，针对该漏洞的攻击活动源自一个Starlink IP地址。CVE-2025-59528是Flowise平台继操作系统命令远程代码执行漏洞（CVE-2025-8943，CVSS评分：9.8）和任意文件上传漏洞（CVE-2025-26319，CVSS评分：8.9）之后，第三个被野外利用的漏洞。

VulnCheck安全研究副总裁Caitlin Condon向The Hacker News表示："这是多家大型企业使用的热门AI平台中的严重漏洞。该漏洞公开已超六个月，意味着防御方本有时间优先修补。但超过1.2万个暴露在互联网上的实例形成的攻击面，使得当前活跃的扫描和利用尝试更为严峻——攻击者拥有大量可伺机侦察和利用的目标。"

**参考来源：**

Flowise AI Agent Builder Under Active CVSS 10.0 RCE Exploitation; 12,000+ Instances Exposed

https://thehackernews.com/2026/04/flowise-ai-agent-builder-under-active.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0BoYQFaEKibEe5x5vA7Nt2y5GrK420ck8h2br3pAshqL3C2gBcBzibxicXsGkMtOdWbOAsfgfRfuaftcw8pQJTdwE0YtUQicJKavA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651336774&idx=1&sn=408127059513eb158f86aa2cfc845a5b&scene=21#wechat_redirect)

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