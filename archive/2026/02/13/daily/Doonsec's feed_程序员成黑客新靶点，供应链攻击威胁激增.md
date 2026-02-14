---
title: 程序员成黑客新靶点，供应链攻击威胁激增
url: https://mp.weixin.qq.com/s/K1NTt5NWpMQ5WkzYPP8HSg
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:05:53.818850
---

# 程序员成黑客新靶点，供应链攻击威胁激增

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0DXynGsBfwOEibgqa5QTj8cPXulRPLhQTSZliaAUZpVlcKlLrjcQxpAoAYM3OpKbHKbo1XmLZLrtOWGib6afWSFvI1GNTuxmticLc/0?wx_fmt=jpeg)

# 程序员成黑客新靶点，供应链攻击威胁激增

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1DcXEy2YDx4uLUg5LGoCCtzsMhvE9GEzqvCI7byOIrVibmlmrZfxRKoQ4HYScQgAiaJFfJYxXuyvNGx5vlACKciajO6NWnl6ibH94/640?wx_fmt=jpeg)

程序员正日益成为网络犯罪分子的攻击目标，企业安全负责人需高度重视这一风险趋势。

网络犯罪分子正在改变策略——他们不再局限于利用应用程序漏洞，而是将目标转向程序员日常依赖的工具和访问渠道。攻击者通过结合多种网络犯罪战术，甚至引入人工智能（AI）技术来达成目的。

安全厂商Immersive首席应用安全专家Chris Wood指出："攻击者不再满足于入侵网络，他们开始瞄准开发工作流程。程序员掌握着'王国的钥匙'——包括源代码和云基础设施的特权访问权限，这使他们成为高价值攻击目标。"

**Part01**

## ****被污染的软件生态****

Checkmarx安全研究倡导者Darren Meyer观察到大量针对程序员的"低投入"攻击，例如托管在域名抢注网站上的恶意开源工具版本。但Meyer警告："这只是冰山一角，更具针对性的攻击如Shai-Hulud蠕虫、npm软件包攻击和Visual Studio Code插件生态入侵正在增加。"

软件供应链安全公司Sonatype的《2026软件供应链现状报告》显示，自2019年以来已识别123万个包含恶意代码的开源软件包，仅2025年就新增45.4万个。报告特别指出："实际风险主要来自已知漏洞而非新漏洞"，2025年开发者下载存在漏洞的Log4j版本超过4200万次，占该组件总下载量的13%。

**Part02**

## ****遭入侵的开发环境****

攻击者尤其青睐软件开发环境，常见的安全疏漏如过度特权账户、长期有效令牌和错误配置的流水线，使得非法访问开发环境和敏感数据变得轻而易举。Sysdig高级网络安全战略师Crystal Morin表示："不当存储的凭证即使对新手攻击者也极具吸引力。"

**Part03**

## ****内部人员威胁****

犯罪分子不再局限于窃取凭证，他们开始伪装成应聘者潜入企业。朝鲜黑客组织就擅长使用伪造身份和社会工程手段获取职位，随后窃取数据和商业机密用于勒索。Morin补充道："攻击者还会冒充维护者，试图将恶意代码植入流行开源项目，如XZ Utils后门事件。"

**Part04**

## ****供应链风险****

Tenable情报副总裁Gavin Millard指出："供应链攻击已取代漏洞利用成为最大系统性网络安全风险。通过劫持S1ngularity和npm维护者账户，犯罪分子能在几分钟内达成传统钓鱼攻击数年才能实现的效果。"世界经济论坛《2026全球网络安全展望》显示，65%企业将供应链和第三方漏洞视为头号安全挑战，该比例同比上升54%。

**Part05**

## ****复合型攻击模式****

Black Duck高级研发经理Christopher Jess描述了攻击者如何结合技术入侵与社会工程："恶意软件包可能包含隐蔽后门，再通过伪造维护者紧急安全更新通知加速传播。"AI技术进一步提升了攻击精度，攻击者可利用代码仓库历史记录和团队角色信息生成逼真的代码变更，规避审查流程。

**Part06**

## ****AI工具带来的附加风险****

APIContext首席产品官Jamie Beckland警告："AI辅助编程和氛围编码（Vibe Coding）加剧了安全风险，特别是当生成的代码缺乏充分测试和文档追溯时。"MCP服务器可通过添加工具进行篡改，用于提取内部API、数据存储和SaaS系统的数据。

Secure Code Warrior联合创始人Pieter Danhieux指出："MCP服务器和Agentic AI成为犯罪分子的温床，攻击者可轻易注入不安全提示或AI生成的恶意代码。"Sonatype分析3.7万条GPT-5建议后发现28%存在幻觉问题，部分建议甚至推荐安装含恶意代码的软件包。BaxBench基准测试显示，62%由大语言模型生成的解决方案存在缺陷或安全漏洞。

**Part07**

## ****CISO应对策略****

建议安全负责人采取技术控制、安全培训和文化建设相结合的措施：

* 实施严格身份验证、账户卫生管理和最小权限原则
* 使用容器隔离工作区，集中管理镜像和密钥
* 建立不可变SHA哈希工作流，存储在防篡改硬件模块中
* 限制外部依赖直接访问，阻止不安全软件包下载
* 为程序员提供持续实战培训，培养自主修复安全问题的能力

Security Journey应用安全倡导者Michael Burch强调："程序员需要亲眼目睹系统故障的影响，通过真实场景演练掌握安全修复技能。"

**参考来源：**

Entwickler werden zum Angriffsvektor

https://www.csoonline.com/article/4130654/entwickler-werden-zum-angriffsvektor.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1QWGTwJ4jnO2icEhSqbRNdWd3iaVBKjlfTsWSdDBiayVW1jWahKjlggw6mzYnEo5D6PMvFzRX6fEpVEic5NqQoVDFCWvHlh48OxrA/640?wx_fmt=png&from=appmsg)

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