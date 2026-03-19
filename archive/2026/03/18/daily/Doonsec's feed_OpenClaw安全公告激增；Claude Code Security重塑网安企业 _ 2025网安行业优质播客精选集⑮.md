---
title: OpenClaw安全公告激增；Claude Code Security重塑网安企业 | 2025网安行业优质播客精选集⑮
url: https://mp.weixin.qq.com/s/OHZdrmzEgO8HA8coziP8pA
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:18:12.240190
---

# OpenClaw安全公告激增；Claude Code Security重塑网安企业 | 2025网安行业优质播客精选集⑮

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2nXOPlt8zco6RvJicOq8E3XaNAvrA8hClaNgbXRmsKsXJBnpAmHLGxmTfgpSJ017q5XtibINiboKPxu0F8hb1sGUDPKhMf588z0E/0?wx_fmt=jpeg)

# OpenClaw安全公告激增；Claude Code Security重塑网安企业 | 2025网安行业优质播客精选集⑮

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3FZia5icghkVb7Hltjd9pZ8G6oUBGLVZWRnA1eAOHLcIYsT37Piayyo3htEzyKR7bHicAKZ6jV5hSPwJ7kumianXGlkib1MOULzy0fo/640?wx_fmt=png&from=appmsg)

**01 OpenClaw安全公告激增暴露**

**GitHub与CVE漏洞跟踪体系间的鸿沟**

本期节目：OpenClaw项目爆红后暴露出漏洞跟踪体系的结构性问题。该项目三周内发布255份GitHub安全公告（GHSA），远超CVE分配能力，导致多数漏洞缺乏CVE编号。这凸显了GHSA与CVE系统间的割裂：GHSA流程便捷但缺乏企业工具支持，CVE审核缓慢且无法应对批量请求。研究显示仅8%的GHSA经过审核，未审核漏洞可能被下游项目长期忽略。专家建议安全团队需同时核查GHSA和CVE数据库，避免因依赖单一系统而遗漏风险。AI驱动的开发加速使漏洞披露速度持续提升，现有跟踪体系面临严峻挑战。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2rcjCsjqlfiaicltbQMVwy5UqtyckUQczv0iccGW6wqvK2OkOBibvFibClrzd6UyV6miczF9kSQMdGweNT9rgxtr9dRSEWGwjK4eWnE/640?wx_fmt=png&from=appmsg)

**02 Claude Code Security的发布，**

**会如何重塑传统网络安全企业？**

本期节目：Anthropic推出的Claude Code Security将代码审计和漏洞发现能力直接嵌入AI模型内部，改变了传统安全工具作为"外挂"的形态。这一创新可能对三类传统安全企业造成结构性冲击：规则型工具厂商因模型不依赖固定规则库而价值稀释；人工审计服务在中低端市场被挤压；DevSecOps平台则面临能力重构。核心在于模型使安全能力的边际成本趋近于零，颠覆了按扫描次数、漏洞数量或人天收费的传统商业模式。传统企业应转向安全治理、构建AI生态链安全护栏及参与模型评测标准化，从"检测工具"转型为"AI安全治理能力提供者"。这标志着安全能力开始"模型原生化"，行业面临从规则防御向语义理解的安全思维转变。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX03avicAgBId0mvNqFibIbhFic5tvLG1LiaV58DgywiakDQyckZ0PRRs2S0X7cffibFzytdeOAB9wVUeEohFpeETt9rSgCL5mBCiagBGk/640?wx_fmt=png&from=appmsg)

**03 一个网安老登的断崖式衰老**

本期节目：本期播客以春节团聚的短暂与年后离别的漂泊感开篇，引出对时间流逝的感慨。作者作为网络安全从业者，回顾了行业内的经典事件和个人经历，如联通韩毅、乌云下线等，感叹青春不再。随着年龄增长，作者发现自己对工作的热情减退，生活态度趋于佛系，朋友圈也日渐沉默。文章最后以平淡的午后比喻时间的飞逝，呼吁顺其自然，保持网安从业者的激情，享受生活中的风景。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3JEFB8J3OKbR70mN72kVMlj7R3S0uE48FUI8fFviaCiaiblsIHic3vX8ReCfXRRflseNO6kKibsdFTn5FMZqg0shXMAicyEObpXQOz8/640?wx_fmt=png&from=appmsg)

**04 OpenAI称Codex Security**

**一个月内发现1.1万个高危漏洞**

本期节目：OpenAI推出的Codex Security工具在30天测试期内，从真实代码库中识别出11,000多个高危漏洞（含792个严重漏洞），误报率低于0.1%。该工具通过AI模拟安全研究员工作流程，建立项目上下文理解，自动验证漏洞并生成修复补丁，有效缓解警报疲劳问题。测试覆盖120万次提交，涉及Netgear等专有项目及OpenSSH等开源项目，已分配14个CVE编号。其核心技术源自"Aardvark"实验，具备沙箱验证和持续学习能力，现以预览版向企业用户开放。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1okgpQVhgicEp4pt3qBhicR5e6MM5TRZESQkcwEqa0vWmYjicRLxanlKtbliaOgjNGyK4fncqHhqW7HE4FIGSRic9meGA4ehxLicfN0/640?wx_fmt=png&from=appmsg)

**05 Anthropic推出高效但昂贵的代码审查工具，**

**助力开发者提升代码质量**

本期节目：Anthropic推出Claude Code的代码审查功能，旨在解决AI生成代码激增导致的人工审查瓶颈。该功能采用多Agent系统，提供深度分析，包括漏洞说明、修复建议和严重程度分级，但费用较高（每单5-25美元），耗时约20分钟。内部测试显示，大型请求84%发现问题，小型请求31%存在问题。该功能现面向团队版和企业版用户开放预览。此次发布正值Anthropic强化企业客户基础，其企业订阅量年初以来增长四倍，Claude Code年化收入突破25亿美元。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ibo0YWSiaDrZOQNUiaglUyD9Iiah4cIt0G77ic1yAoWFheicO0s22Xl5ichbSHJCqN0atwexciaEIaEkiay5MQbfqice5x7DicY1ZBIaXnA/640?wx_fmt=png&from=appmsg)

**FreeBuf播客征集令**

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR395uCiblRufw6peqpFEw4DlSgcVALTicaLySmyRZI2sa3HzynTvaFretaG7fLTkgHxPqYd30NsXLERw/640?wx_fmt=png&from=appmsg)

『FreeBuf播客』——网安人的“随身听”

在这里，你可以获得网安一手消息

最新资讯、网安八卦、小道消息、威胁情报、安全工具、网安吐槽......

即刻来【FreeBuf知识大陆】，抢先体验吧！

添加小助手微信（FreeBuf1024）

收听or录制播客可得额外奖励，等一个小红点~

![](https://mmbiz.qpic.cn/mmbiz_png/oQ6bDiaGhdyodyXHMOVT6w8DobNKYuiaE7OzFMbpar0icHmzxjMvI2ACxFql4Wbu2CfOZeadq1WicJbib6FqTyxEx6Q/640?wx_fmt=png&wxfrom=10005&wx_lazy=1&wx_co=1&tp=wxpic)

---

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hCYIDd7a8icmhzic2aMTw0bics6BfDdhRCQCsKTwXSAB6wXtEwI4OK9jdlFfFFNQJa4JUiapxxu56BjXl4gx3LEXYU1GMRkpiawgA/640?wx_fmt=png&from=appmsg)

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