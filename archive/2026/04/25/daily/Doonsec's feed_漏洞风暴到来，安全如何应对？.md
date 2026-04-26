---
title: 漏洞风暴到来，安全如何应对？
url: https://mp.weixin.qq.com/s/54o11j2hq8g2B4tM3GYAfQ
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:58:11.251586
---

# 漏洞风暴到来，安全如何应对？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ccVb6wGibibCEDqHib6dmNxPAFnEZlrAcicic3wI2VjVXYiaq8foFnQ5qcz7gHPGHHRyq0jdl9JAgGNfjTc8NrHLKPCfTeRWedLTAajtMiah0b6hLQ/0?wx_fmt=jpeg)

# 漏洞风暴到来，安全如何应对？

原创

孙志敏
孙志敏

AI与安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前一段时间,Anthropic 的 Mythos 模型曝出强大的漏洞发现能力,并同步启动"玻璃翼"(Glasswing)计划,以受限发布、联盟合作的形式保护关键软件。紧接着在 4 月 15 日,作为漏洞发布权威的 NIST,因为漏洞数量暴增,宣布改进漏洞操作方法。

随着前沿人工智能加速漏洞发现,全球每个企业的董事会都在向 CISO 提出同一个问题:**我们是否存在安全漏洞?我们的安全防护措施是否到位?**

毫无疑问,防护是不到位的——所有企业都不到位。

怎么办？目前业界能看到的两个代表性方案,一个来自 OWASP 生成式 AI 安全项目联合 CSA CISO 社区、SANS 等发布的《"AI 漏洞风暴":构建 Mythos 就绪安全体系》战略简报,另一个是 CrowdStrike 4 月刚刚宣布的 Project QuiltWorks。

01

方案一:OWASP 的"Mythos 就绪"战略简报

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCFSQaV68v9OVp0yf4BEAe7KOf6zJC0T8DfbKn64fq9KzKOMF2gMv2NBUJuE4NFJBBYQadZibxy90jvsVYkVZ9Vj7dpmGXiaibjKXo/640?wx_fmt=png&from=appmsg)

##

OWASP 这份简报是一份典型的"写给 CISO 看"的快速战略简报,由 CSA CISO 社区、SANS 研究所、[un]prompted、OWASP 生成式 AI 安全项目联合编写,参与者包括前 CISA 局长 Jen Easterly、密码学家 Bruce Schneier、Google 安全副总裁 Heather Adkins、前白宫国家网络总监 Chris Inglis 等重量级人物,代表了当下主流安全共同体对这一轮变化的判断。

简报的核心判断很直接:Mythos 不是起跑枪,而是加速器。AI 发现漏洞的能力早在 Mythos 之前就已经存在——2025 年 XBOW 登顶 HackerOne 排行榜,DARPA 的 AIxCC 在四小时内发现 54 个漏洞,Google 的 Big Sleep 在开源软件里挖出真实零日。真正的变化是,主流 AI 实验室现在官方下场做这件事,而且同等能力的开源权重模型正以可负担的成本向全球开放。这意味着"用一个模型对每家企业、每个项目发起全量代码审计"已经从理论变成现实。

在这个判断下,简报给出的不是一个产品,而是一份**风险登记册加行动清单**,参照 NIST CSF 2.0、MITRE ATLAS、OWASP LLM Top 10 和 OWASP 智能体 Top 10 四个框架,列出 13 条风险,并给出 11 项优先行动。其主干逻辑可以概括为四句话:

**一是把 LLM 向内用于自己**。防御性 AI 技术虽未完全成熟,但基于 LLM 的漏洞发现能力已经成熟、可以立即为我所用。让 AI 智能体扫描自己的代码和依赖,再在 CI/CD 流水线中构建完整审计,最后左移到开发者的编码智能体中,让所有代码(人类或 AI 生成)在合并前都经过 LLM 驱动的安全审查。

**二是为持续的"补丁潮"做准备**。Glasswing 引发的披露只是第一波,后面会有多轮浪潮。要针对"一周内发生多起高严重性事件"的场景做桌面推演,缩短从检测到遏制的时间,提前为分诊和部署扩容。

**三是防御你的智能体**。安全团队需要 AI 智能体来匹配 AI 级别的速度,但这些智能体默认拥有高权限、默认不安全,且不在现有安全控制范围内。部署前必须对提示词、工具定义、检索管道、升级逻辑施加与其权限同等严格的审计,明确范围边界、爆炸半径限制和人类覆盖机制。

**四是立即构建集体防御**。攻击者已经以"辛迪加模式"共享工具、集体行动,防御方必须通过 ISAC、CERT、行业协调组织共享威胁情报、协调响应。

简报还直接给了一份"激进时间表":本周启动的有"让智能体瞄准自己的代码和流水线""强制 AI 智能体采用""建立创新加速治理""为持续补丁做准备""更新风险模型和报告"等;本月启动的有"防御你的智能体""清点和缩减攻击面""加固环境";未来 90 天启动"构建欺骗能力""构建自动化响应";12 个月内建立永久性的"漏洞运营(VulnOps)"职能——像 DevOps 一样配置人员和自动化,专门负责在整个软件资产中持续发现零日并建立自动化修复管道。

02

方案二:CrowdStrike 的 Project QuiltWorks

##

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCFvOU3QoENtLTlRSr1uHTGSib8LDTX9BaicUSBsAmwt82njS6Tiabfh4S8WJ1n296zEGabZUYFREictk7PQDIpw6wL6xlpef4YKaag/640?wx_fmt=png&from=appmsg)

##

## 好吧，这个名字就很有意思：被子项目，或者叫缝缝补补工程？

QuiltWorks 走的是完全不同的路数。它不是一份指南,而是一个由 CrowdStrike 牵头的行业联盟,合作方包括 Anthropic、OpenAI 两家前沿模型厂商,以及 Accenture、EY、IBM 网络安全服务、Kroll 等大型系统集成商与咨询机构。核心口号也很直白——**"未来六个月发现的漏洞,将超过过去 30 年的总和"**,CrowdStrike 把这一刻定义为"网络安全的 Y2K 时刻"。

方案本身是一套"评估—扫描—排序—修复"的闭环服务:

**评估**,由 CrowdStrike 及合作伙伴的专家先审视客户当前安全项目的现状、立足点和修复能力;**模型部署**,把前沿 AI 模型部署到客户的代码、依赖、配置和遗留系统里,去发现传统扫描器根本没能力看到的"真正可利用"的漏洞;**风险排序**,由专家红队按"可利用性、对手活动、业务影响"排序——而不是按 CVSS 打分,因为 CrowdStrike 明确认为 CVSS 分数不能反映特定环境下的真实可利用性;**修复**,通过合作伙伴平台把发现转化为行动,并生成可直接提交董事会的分析报告。

支撑这套逻辑的数据,CrowdStrike 也给得很具体:2025 年 AI 加持的对手攻击增长 89%,最快攻击者"突破时间"27 秒,在公开披露前就被利用的零日漏洞增加了 42%,全年 CVE 记录超过 48000 条、同比增长 20%。所以 QuiltWorks 的卖点简洁直接——"Patch Tuesday is now Patch Everyday"(补丁星期二已经变成补丁每一天)。

03

老孙点评

两个方案看上去都有道理，但都不好落地。

我们对漏洞有个共同的认知：那就是漏洞不可避免，漏洞无法被完全发现。同时，漏洞的解决没有根本性的一劳永逸的办法，补丁基本是唯一靠谱方法。

OWASP的方案，看上去合理：在开发阶段即使用LLM，提前发现并处理漏洞，这个思路很好，但只能解决一部分问题：漏洞的风险在现网，自研代码只是现网的一部分，以云为例，除了自研的软件，里边还有大量外采的系统和软件，比如交换机，路由器，服务器的BMC系统，以及一些数据库系统等，这些供应商是否都能够走Devsecops把漏洞都解决掉？显然不现实。那这些漏洞怎么办？

Crowdstrike的方案则更不靠谱。大型现网的补丁有多难打，我曾是写过一篇文章，叫补丁之难（[网络空间安全：补丁之难](https://mp.weixin.qq.com/s?__biz=Mzg5NTMxMjQ4OA==&mid=2247483857&idx=1&sn=87bc0cd60c7cfc7505bf8d39edfd7ed8&scene=21#wechat_redirect)），大家可以参考，打一次补丁，对大型网络是非常难的，尤其是需要重启的系统。如果真的改成天天补丁，那大家也别干活了，就天天打补丁吧。

没有银弹，总得有点办法吧？

我觉得目前可行的方法，还是零信任架构，尽量地减少攻击面，减少爆破范围，这是生产环境里相对可以接受的方案。

当然，未来会不会有更好的方案，我相信是会有的，但需要耐心等待。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

AI与安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

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