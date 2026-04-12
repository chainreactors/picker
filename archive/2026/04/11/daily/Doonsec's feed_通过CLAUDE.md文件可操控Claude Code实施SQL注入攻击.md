---
title: 通过CLAUDE.md文件可操控Claude Code实施SQL注入攻击
url: https://mp.weixin.qq.com/s/iCi46SaDowOoQiAb-xKbfw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:06.185179
---

# 通过CLAUDE.md文件可操控Claude Code实施SQL注入攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1EMaicyJp1Uy2QkKHxqPfUOrU77j0khiaJ0nOExgIicGXfzcz5TIMoKBiaKPZ6iaImtoO7rsicIaia1Pk3AqSH8WicxSEmHKiaWZCulynU/0?wx_fmt=jpeg)

# 通过CLAUDE.md文件可操控Claude Code实施SQL注入攻击

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX098CIjBzVMsvvaicicichP6j74fiaMHXfqrd0Nt6CIRhJbno5ZQxJqicLML6ibJXqED0iaVFXId01ibT6YoiazQrnicicnUOWjoKOrRKpNKc/640?wx_fmt=png&from=appmsg)

##

## LayerX研究人员发现，攻击者可以利用CLAUDE.md文件绕过Claude Code的安全规则。该漏洞使得任何人都能自动化实施SQL注入攻击并窃取用户凭证，而无需编写任何代码。

##

**Part01**

## ****AI编程助手被武器化****

LayerX最新研究表明，黑客可将计算机程序员广泛使用的工具转化为实施恶意行为的强大武器。该工具正是Anthropic公司开发的Claude Code——研究人员发现其存在被武器化的风险。这项与Hackread.com共享的研究表明，即使不具备编码能力的人也能利用该工具攻击网站。

需注意Claude Code与近期Claude源代码泄露事件无关。作为AI驱动的编程助手，Claude Code具备自主代理（Agentic）特性：它能编写修复代码、自主决策并在计算机上执行命令。每个使用Claude Code的项目都包含名为CLAUDE.md的文本配置文件，用于定义其行为模式。

**Part02**

## ****安全护栏形同虚设****

虽然该AI通常设有安全护栏以防止恶意活动（如创建恶意软件），但LayerX团队指出这些防护措施极易被绕过。"Claude Code专为需要AI在真实系统上自主行动的开发者设计，因此比标准网页AI接口拥有更广泛的权限。这种扩展的自由度虽是其功能实现的必要条件，但也构成了当前已被利用的攻击面。"研究报告中如是写道。

在针对DVWA漏洞测试环境的实验中，研究人员仅需在该文本文件中输入三行基础英文指令，就能诱使工具无视安全规则。某次测试中，他们仅通过虚假声明"已获授权"就使AI开放未授权访问权限。该工具采信文件内容后立即开始窃取用户名密码，甚至运用SQL注入技术直接导出数据库。

**Part03**

## ****指令文件成为攻击载体****

AI系统明确将文本文件作为其行为依据——研究人员记录到AI的反馈："鉴于您CLAUDE.md中声明的渗透测试授权...以下是登录绕过方案"。随后AI使用cURL工具实施攻击，研究人员强调："这个看似普通的文件突然成为攻击载体"，因为AI会无条件信任文件指令。

* LayerX报告指出，这不仅是理论风险，更是迫在眉睫的现实威胁。黑客可能通过以下方式利用该漏洞：
* 直接欺骗AI协助实施入侵
* 在共享项目中隐藏恶意指令文件，当开发者下载时自动窃取其私有文件
* 内部人员恶意篡改企业项目中的配置文件

**Part04**

## ****厂商响应迟缓****

LayerX团队已于2026年3月29日联系Anthropic公司通报该问题，但未获得积极回应，仅被要求转邮件至其他部门。尽管当日再次发送邮件，截至发稿前仍未收到回复。研究人员建议所有使用Claude Code的团队应将此类文本文件视同可执行代码进行严格审查。

**参考来源：**

Claude Code Can Be Manipulated via CLAUDE.md to Run SQL Injection Attacks

https://hackread.com/claude-code-claude-md-sql-injection-attacks/

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