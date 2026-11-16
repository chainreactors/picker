---
title: FBI发布警告ARTEX让网络攻击进入自动化
url: https://mp.weixin.qq.com/s/1FzIv-feOs0S3cgWSuGN3Q
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:45:44.522244
---

# FBI发布警告ARTEX让网络攻击进入自动化

# FBI发布警告ARTEX让网络攻击进入自动化

Gh0xE9
Gh0xE9

Gh0xE9

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

文章原文：https://www.ic3.gov/CSA/2026/261113.pdf

简单来说，**AI 已经不只是辅助渗透测试人员编写脚本，而是开始将侦察、漏洞利用、权限提升、横向移动、数据窃取等攻击环节串联起来，形成自动化的攻击链，并且由于渗透智能体开源版本较多，人人都可以用来进行网络攻击。**

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaCRJVcQyelKUoLskibV0AGLc2ibibrSc8oRegcDwxZeU4oZhB52S91EB9T4pZA3ds7w4yYKn6tz57hfrb25X4iaiaPOO28m5Wrq7LDc/640?wx_fmt=png&from=appmsg)

**这是本公众号最后一篇关于ARTEX的文章，后续不会再更新类似的文章，仔细研读这份报告，值得关注的一点是 ARTEX 已经被**多个威胁组织用于真实网络攻击，并且能够将资产侦察、漏洞利用、权限提升、横向移动乃至数据窃取等多个攻击阶段串联起来，实现高度自动化的攻击行动，并且由于二开，有大量的二开ARTEX版本在互联网上运行，根据国外网络新闻流传，全网有800+ARTEX主机运行，但笔者感觉不止，笔者身边有不少人也在用ARTEX二开去做一些渗透任务，实际肯定远于这个数字。

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaDCAicmA5Aic2U4p6m1tu2nTOU8LxNdiatarJrG7oRLyqvmzZ63ufNaiaoekWTomFZZ6ticygnWO9VnZ7tZpEmORlE5ElRkrcQfTqyk/640?wx_fmt=png&from=appmsg)

根据报告里面，二开的ARTEX和原版的ARTEX所攻击的目标基本上涵盖现有行业，例金融、政府、科技、国防、半导体、能源、医疗、制造、电信以及法律服务等，相关攻击案例不再赘述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaDSRTC73YIa63oNl7VXFHdxwTnNjfnr9GBH2axtd3eWneicGW2EgkW9XpzibSHoXiazcibqIv2guibHnJl5VaPX0qTImTOFcynKVlhc/640?wx_fmt=png&from=appmsg)

回到ARTEX本身，我认为这份报告最值得关注的，并不是又出现了一款能够自动化渗透的 AI 工具，而是它所代表的技术发展方向

过去，一次完整的渗透测试通常需要不同专业能力的人员协作完成，从资产收集、指纹识别、漏洞挖掘，到漏洞利用、权限提升、内网横向移动，每一个阶段都需要投入相应的人力和技术成本，自动化工具能够解决其中一部分重复性工作，但不同工具之间仍然需要人工进行判断、选择和衔接，而以 ARTEX 为代表的 Agentic Offensive Framework，正在尝试改变这种工作模式

并且，让这种工作变得更加廉价和简单，攻击者只要不断提出目标，不断去干预，Agent 就可以自动根据结果和目标不断执行后续行动，笔者身边就有不少人，只学过一点点Web安全基础，就能用AI挖掘出严重漏洞

不过比起攻击，笔者更看重网络安全的防御，过去几个月来，收到过不少被AI攻击的案例，重则勒索病毒，轻则数据泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaBoAU41WsGED9L7iamrg3kZTKog8RKvNIP5cVCBImkTI6XBfGghvvJ8cmBNN2ic2Be0Cl07vTmE9MOUgMXvehm3UIIico8BEuOtG4/640?wx_fmt=png&from=appmsg)

最后再来说说要怎么应对AI攻击吧，唉，算了，给的建议不如AI给的，大伙自己拿下面提示词去生成吧

```
AI 网络安全防御体系规划专家你现在是一名资深企业网络安全架构师、攻防专家和安全战略顾问。我希望你根据我的企业实际情况，生成一份完整、专业、可落地的《企业网络安全防御体系建设规划》。不要简单罗列安全产品，而是从企业真实业务、基础设施、攻击面、数据资产、人员能力和安全预算出发，设计一套系统化的纵深防御体系。一、首先了解我的企业情况请先向我询问以下信息：企业所属行业：企业规模（员工人数、业务规模）：企业 IT 基础设施（本地 IDC、云服务器、混合云等）：是否有互联网业务、Web 系统、移动端或 API：是否使用 AI 大模型、AI Agent、MCP 等技术：是否涉及客户信息、个人隐私、商业机密等敏感数据：当前已经部署的安全产品：当前安全团队规模和技术能力：年度安全预算（可选）：当前最担心的安全风险：如果我无法回答某些问题，请允许我填写“不清楚”，不要因此中断分析。二、生成企业安全防御体系收集完信息后，请从以下 12 个领域进行全面分析：基础设施与攻击面防御身份认证与权限管理网络攻击检测与防御终端与主机安全数据安全与防泄露安全运营与自动化响应AI 大模型与智能体安全云原生与容器安全软件供应链与研发安全威胁情报与攻击监测安全验证与持续评估应急响应与业务韧性针对每个领域，必须输出：防御目标：这个领域主要解决什么问题？核心风险：企业可能面临哪些攻击？防御技术：应该采用哪些具体技术？建设内容：需要部署哪些系统、平台或机制？优先级：高、中、低。建设建议：企业应该如何落地？验收指标：如何判断防御能力真正有效？三、生成可视化安全架构请将上述内容整理成一张完整的企业网络安全防御架构图。要求：采用专业的网络安全架构设计风格。按照纵深防御思想分层组织。清晰展示各安全领域之间的关系。展示安全运营、威胁检测、自动响应和恢复机制。使用中文标注。不要遗漏 12 个防御领域。架构要符合我的企业实际情况，不要盲目堆砌产品。四、输出建设路线图将建设计划分成三个阶段：第一阶段：基础防御建设第二阶段：纵深防御与自动化建设第三阶段：智能化安全运营与持续防御每个阶段都需要列出具体建设项目、建设顺序、预期效果和验收标准。五、输出最终报告请按照以下结构输出：企业安全现状分析主要安全风险分析企业安全防御能力评估企业专属安全防御架构图12 大安全领域建设规划安全产品与技术选型建议分阶段建设路线图建设预算与投入建议（信息不足时给出估算区间并说明假设）最终安全能力成熟度评价六、重要要求不要为了展示技术而堆砌安全产品。不要给出脱离企业实际情况的建设建议。区分必须建设、建议建设和可选建设。对于不确定的信息，明确标注假设，不要编造企业现状。优先考虑实际防御效果、投入产出比和可维护性。所有建议尽量给出可执行的实施方案。现在，请从第一部分开始，逐步了解我的企业情况，然后为我生成专属的网络安全防御体系规划。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaDiaEA4ZNn4VGGys9sznxKyROQsm8ld3xBpClP5SgichGm27a53NTezSZsBmCIXooPsj6gnONjicT78ttIyNlhHmVJdeBiap5jlIjs/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaCOJLaaibS5WfeiaVEibIPZAXwUlPbXSmFupTNQYQywLxbMHtpQF8lBkgEDLEh0e5GveGxZicJlevLVv8gMPX8NVwfU7S1ic3PRqB1Q/0?wx_fmt=png)

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