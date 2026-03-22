---
title: AI驱动的渗透测试工具Apex，以黑盒模式攻击应用程序发现漏洞
url: https://mp.weixin.qq.com/s/LGl3CQSBFsB8LmjXMtw7Lw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:15:46.034043
---

# AI驱动的渗透测试工具Apex，以黑盒模式攻击应用程序发现漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX017oIdPHrb5ic1pOKKFWNGMcg8CyQxMgk3fLu0HvzLrOmOHylx5M7JH9b1EuuWO69GicU330Wib3Ibr9AibgNI9drwUFk7R6yy8YY/0?wx_fmt=jpeg)

# AI驱动的渗透测试工具Apex，以黑盒模式攻击应用程序发现漏洞

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2KyJICIkAZQHAP8Rnf2YCxb35KCbnLnicqCVruFcp2S4LLbD7Swuic6pc1TyCPaucIqFtKEvYlMVXzCDdM1qQmuwSx15YdxoNwE/640?wx_fmt=jpeg&from=appmsg)

##

**Part01**

## ****AI渗透测试Agent Apex****

Apex是一款自主运行的AI驱动渗透测试Agent，专为针对实时应用程序的黑盒测试模式设计。该工具无需访问源代码、提示或预定义的攻击路径，就能以现代软件开发所需的速度发现、串联并验证现实世界中的漏洞。

**Part02**

## ****开发背景****

Apex的诞生源于当前软件安全实践的结构性缺陷。AI编码Agent正在以机器规模生成和合并代码——仅Stripe的编码Agent每周就会合并1300个拉取请求，而某些工程团队每天为每位工程师花费超过1000美元的AI代币，却完全不进行人工代码审查。

传统扫描工具和人工主导的评估无法跟上这种速度。Apex被设计为对抗性验证层：一个独立的Agent，能够像真实攻击者那样攻击正在运行的应用程序，在漏洞演变为入侵前将其捕获。

**Part03**

## ****三种部署模式****

Apex支持三种部署模式：

* 在CI/CD管道中，针对应用程序的沙盒副本验证每次部署，在代码合并前绘制攻击面并尝试利用漏洞
* 针对生产环境，实时持续发现可利用的弱点
* 支持按需测试任何目标，用现代威胁速度的反馈循环取代传统的季度PDF报告

**Part04**

## ****Argus基准测试平台****

为验证Apex的能力，PensarAI开发了开源基准测试平台Argus，包含60个独立的Docker化漏洞Web应用程序，专门用于评估攻击性安全Agent。

现有基准被认为存在不足：最广泛使用的XBOW 104项挑战集中，70%是PHP目标，仅覆盖单一漏洞，且缺乏GraphQL、JWT算法混淆、竞态条件、原型污染链、WAF绕过和多租户隔离场景。

Argus覆盖主流生产框架：Node.js/Express（40%）、Python/Flask/Django（20%）、多服务架构（25%）、Go、Java/Spring Boot和PHP。它引入了其他基准未涵盖的类别：WAF和IDS规避、需要串联多达7个漏洞的多步骤利用链、多租户隔离失效、竞态条件和业务逻辑缺陷、现代认证绕过（JWT、OAuth、SAML、MFA）以及云/Kubernetes基础设施攻击。难度分为2个简单、27个中等和31个困难挑战。

**Part05**

## ****测试结果****

在60个Argus挑战中，Apex使用最小最经济的Claude Haiku 4.5模型以完全黑盒模式进行测试，以隔离架构优势与原始模型能力。Apex取得了35%的通过率，优于PentestGPT（30%）和Raptor（27%）。在使用Claude Opus 4.6的最难10项挑战中，差距显著扩大：Apex解决80%，PentestGPT达到70%，Raptor为60%。

在整个测试过程中，Apex发现了271个独特漏洞，涵盖SQL注入、SSRF、NoSQL注入、原型污染、SSTI、XXE、竞态条件、IDOR、认证绕过、CORS错误配置、命令注入和路径遍历。每项挑战的平均成本约为8美元，60项挑战在Haiku上的总成本低于500美元。

**Part06**

## ****典型案例****

Apex在15分钟内解决的典型案例包括：

* 金融科技转账端点的7步竞态条件双花攻击
* 通过共享缓存进行多租户SSRF链攻击以提取相邻租户的API密钥
* 通过SpEL注入实现Java Spring Boot应用的远程代码执行

**Part07**

## ****失败模式分析****

Apex记录的失败模式具有指导意义：

* 成功SSRF链后完成最终凭据提取的"最后一英里执行"成为主要短板
* 诱饵标志两次误导了Agent
* CI/CD管道投毒和Kubernetes入侵等复杂多步链攻击超出了30分钟的时间预算

Apex和Argus基准测试平台现已在GitHub上开源提供。

**参考来源：**

Apex – AI-Powered Pentester Attacks Apps in Black-Box Mode to Find Vulnerabilities

https://cybersecuritynews.com/apex-ai-penetration-testing-agent/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hCYIDd7a8icmhzic2aMTw0bics6BfDdhRCQCsKTwXSAB6wXtEwI4OK9jdlFfFFNQJa4JUiapxxu56BjXl4gx3LEXYU1GMRkpiawgA/640?wx_fmt=png&from=appmsg)

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