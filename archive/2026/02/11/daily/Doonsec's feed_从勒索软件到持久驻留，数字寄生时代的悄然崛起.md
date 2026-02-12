---
title: 从勒索软件到持久驻留，数字寄生时代的悄然崛起
url: https://mp.weixin.qq.com/s/R98E1YvBQ5rlsaAXxKXecA
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:20:28.670321
---

# 从勒索软件到持久驻留，数字寄生时代的悄然崛起

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX12UcjjUBJmgOcjwxbXq1qXbDooE8LeHuN0cq9RicDfibiczMMy5x5LNpqQg7TBawMVhEYEiadnEVrwLS2EicGyrcCFn8XcUdqJvLys/0?wx_fmt=jpeg)

# 从勒索软件到持久驻留，数字寄生时代的悄然崛起

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX07Uu2gDibkEWlxDyMnxdrqO1TOAEPK7QparfibZGbVwuBpGLicuvjFg0AehRiaCSdTCSnWZ6Oam33um3FM0kAibx95W2BWMkAJlCx8/640?wx_fmt=jpeg&from=appmsg)

勒索软件与数据加密是否仍是现代网络攻击的标志性特征？网络安全行业是否过度关注表象威胁，而忽略了正在悄然发生的更危险趋势？Picus Labs最新发布的《2026年度红色报告》通过分析110万个恶意文件及2025年观测到的1550万次攻击行为指出：攻击者已不再追求破坏性效果，其目标转向长期隐蔽的潜伏访问。

需要明确的是，勒索软件并未消失，攻击手段仍在创新。但数据显示，攻击策略已明显从高调破坏转向规避检测、持久驻留及隐蔽利用身份凭证与可信基础设施的技术。现代攻击者正日益表现为"数字寄生虫"——它们寄生于宿主系统内部，窃取凭据与服务资源，并尽可能延长潜伏期。

公众注意力往往被大规模中断事件吸引，而本年度的红色报告数据却揭示了一个更隐蔽的现实：防御者的可见性正在哪些关键环节持续流失。

**Part01**

## ****勒索软件信号正在弱化****

过去十年间，勒索软件加密曾是网络风险最明确的信号。当系统被锁定、业务被迫停摆时，入侵事实无可辩驳。

如今这一信号正在失效。数据显示，"为制造影响而加密数据"（ATT&CK编号T1486）的攻击比例同比下降38%，从2024年的21.00%降至2025年的12.94%。这种下降并非源于攻击能力减弱，而是策略的主动转变。

攻击者正将数据勒索作为主要获利模式，取代传统的加密勒索。通过避免加密操作，攻击者在维持系统运行的同时实现：

* 隐蔽外泄敏感数据
* 持续窃取凭证与令牌
* 长期驻留受害环境
* 后期通过勒索施压而非即时破坏

这揭示出全新威胁逻辑：攻击影响不再取决于系统锁定，而在于攻击者能在宿主系统中维持多久的隐蔽访问。

"攻击者的商业模式已从即时破坏转向长期潜伏。" ——《Picus 2026年度红色报告》

**Part02**

## ****凭证窃取成为控制中枢****

随着攻击策略转向长期隐蔽驻留，身份凭证成为最可靠的控制途径。《2026年度红色报告》显示，"从密码存储中获取凭证"（T1555）出现在近四分之一攻击中（23.49%），使其成为去年最普遍的恶意行为。

攻击者不再依赖高调的凭证转储或复杂漏洞利用链，而是越来越多直接从浏览器、密钥链和密码管理器提取保存的凭证。一旦获得有效凭证，提权与横向移动往往只需借助常规管理工具即可实现。

现代恶意软件活动正日益呈现数字寄生虫特征：没有警报、没有崩溃、没有明显指标，只有诡异的静默。这种逻辑正在更广泛地重塑攻击手法。

**Part03**

## ****80%的主流ATT&CK技术侧重隐蔽性****

尽管MITRE ATT&CK框架包含广泛技术，但实际恶意软件活动仍集中在少数优先考虑规避与持久性的技术上。报告揭示显著失衡：十大ATT&CK技术中有八项主要服务于规避、持久化或隐蔽命令控制，这是Picus Labs有记录以来隐蔽型技术的最高集中度，标志着攻击成功标准发生根本转变。

现代攻击者正优化最大驻留时间而非即时影响。使攻击者能够隐藏、融入环境并长期运作的技术，已超过那些专为破坏设计的技术。本年度报告中最常见的行为包括：

* T1055 - 进程注入：使恶意代码在可信系统进程中运行，难以与合法活动区分
* T1547 - 启动项持久化：通过存活于重启和登录过程实现持久驻留
* T1071 - 应用层协议：为命令控制创建"低语通道"，将攻击流量混入正常网络通信
* T1497 - 虚拟化沙箱检测：使恶意软件能识别分析环境并在受监控时拒绝执行

这些技术的组合效果显著：看似合法的进程使用正规工具，通过受信任的通道安静运作。基于特征的检测在此环境中举步维艰，而行为分析对识别刻意伪装成正常活动的恶意行为变得愈发重要。当加密曾定义攻击时，隐蔽性如今决定着攻击的成功。

**Part04**

## ****具备环境感知的恶意软件抗拒分析****

当隐蔽性成为主要成功标准时，仅规避检测已不够。攻击者还必须避免触发防御者用于观察恶意行为的工具。《2026年度红色报告》清晰显示，"虚拟化与沙箱规避"（T1497）在2025年跃升至攻击手法的顶级梯队。

现代恶意软件越来越多地在决定是否行动前评估所处环境。部分样本不再依赖简单特征检查，而是评估执行上下文和用户交互以判断是否处于真实环境。报告中特别提及的LummaC2恶意软件通过几何学分析鼠标移动模式，计算欧几里得距离和光标角度来区分人工操作与沙箱自动化环境的线性移动。当环境呈现人工特征时，它会主动抑制任何执行，静待时机。

这种行为反映了攻击逻辑的深层转变：不能再指望恶意软件在沙箱环境中暴露自身。它通过设计保持休眠状态，直至抵达真实生产系统。在这个以隐蔽与持久为主导的生态中，"不行动"本身已成为核心规避技术。

**Part05**

## ****AI炒作与现实：进化而非革命****

面对攻击者日益显现的适应行为，人们自然关注人工智能在其中的作用。但《2026年度红色报告》给出了审慎结论：尽管存在广泛推测，2025年数据集中并未观察到AI驱动恶意技术的有意义增长。

最普遍的恶意行为仍是传统技术。进程注入、命令行解释器等长期存在的技术继续主导实际入侵事件，印证攻击者无需高级AI即可绕过现代防御。部分恶意软件家族已开始试验大语言模型API，但目前应用范围有限。已观测案例中，LLM服务主要用于检索预定义命令或充当通信层。这些实现提升了效率，但未根本改变攻击决策或执行逻辑。

数据显示，AI正被吸收进现有攻击手法而非重新定义它。数字寄生虫的运作机制保持不变：凭证窃取、隐蔽驻留、滥用可信进程以及越来越长的潜伏时间。攻击者并非通过发明全新技术取胜，而是通过变得更安静、更耐心、更难以与合法活动区分来获得成功。

**Part06**

## ****回归基础应对新型威胁模型****

连续多年的报告分析揭示出一个持续趋势：虽然许多攻击手法年复一年出现，但根本改变的是攻击目标。现代攻击优先考虑：

* 保持不可见性
* 滥用可信身份与工具
* 静默禁用防御
* 维持长期访问权限

通过强化现代安全基础、基于行为的检测、凭证卫生管理及持续对抗暴露验证，组织可减少对戏剧性攻击场景的关注，更聚焦于当前实际奏效的威胁。

**Part07**

## ****准备好验证防御对抗数字寄生虫了吗？****

虽然勒索软件仍占据新闻头条，但《2026年度红色报告》表明：真正的风险越来越来自静默持久的入侵。Picus Security专注于验证防御体系对抗攻击者当前实际使用技术的能力，而非仅针对那些制造最多噪音的威胁。

**参考来源：**

From Ransomware to Residency: Inside the Rise of the Digital Parasite

https://thehackernews.com/2026/02/from-ransomware-to-residency-inside.html

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