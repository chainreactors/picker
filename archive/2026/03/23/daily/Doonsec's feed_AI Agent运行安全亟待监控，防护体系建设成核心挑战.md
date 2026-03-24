---
title: AI Agent运行安全亟待监控，防护体系建设成核心挑战
url: https://mp.weixin.qq.com/s/FwO5NGqCbQRR6rFoQG4DjA
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:15:29.854123
---

# AI Agent运行安全亟待监控，防护体系建设成核心挑战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX04N79reWlH8JqmdbjHtVIibYSSqI8LSTxbtKic6prOytRtm3bslIEI847ZFefLELcibwTbdrPcskPwQiaNfPCahkrLDaoU3Fe7GD4/0?wx_fmt=jpeg)

# AI Agent运行安全亟待监控，防护体系建设成核心挑战

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1JfFJcZbKoLdnOZ67b7ewCe9trAcoekUuhVJBNApmkLibU082M1LI2HbGkNae7tfXroSTvmweW51YJb6VCpH5G3PCbNRGVaibc0/640?wx_fmt=png&from=appmsg)

##

AI Agent 已悄然进驻企业网络，接手员工的部分工作——编写代码、起草邮件、检索文件、连接内部系统。但有时它们也会酿成重大失误。

Meta曾有员工让AI助手管理收件箱，结果遭其清空所有邮件；亚马逊某内部Agent自主决定拆除并重建部署环境，导致AWS服务中断13小时。这些事件揭示了一个重大转变：具备真实权限的自主软件正在企业环境中运行，并产生实际后果。

"Agent就像青少年，"曾任职Uber、Cloudflare和Facebook安全负责人，现Joe Sullivan Security主管Joe Sullivan告诉CSO，"它们拥有全部权限，却缺乏判断力。"

多年来，AI安全防护主要集中于预防阶段——扫描模型、过滤提示词、分析AI生成代码。但随着企业部署直接与内部系统交互的自主Agent，部分安全负责人指出，真正的风险始于Agent上线运行后。"在安全领域，我们始终假设防护终将失效，"Sullivan表示，"这正是监测与监控同等重要的原因。"

AI Agent的速度与自主性意味着错误或意外行为可能在系统间快速蔓延。这种特性促使越来越多安全负责人开始关注"运行时安全"概念——即持续监控企业环境中的运行中Agent。简言之，运行时安全关注软件运行时的行为，而非仅评估部署前的状态。

##

**Part01**

## ****Agent如何改变安全模型****

CISO多年来一直管理企业网络中的人类行为，拥有身份管理、基于角色的访问控制、用户行为分析和终端检测工具。但将这些框架延伸至AI Agent时，安全专家发现仅能部分适用。传统框架在概念上仍然有效，但观察Agent行为的机制已发生根本变化。

"监控目标未变，实现方式全新，"Geordie AI联合创始人兼首席AI官Hanah-Marie Darley指出，"关键在于如何获取Agent行为数据——主要来自日志，但并非所有AI Agent平台都会生成日志。"

传统安全工具设计用于在边界检查点拦截人类行为，而Agent常通过API调用和MCP连接完全绕过这些检查点。它们产生的活动量也呈指数级增长：普通员工两小时生成50-100条日志事件，Agent可达其10-20倍。更关键的是，许多Agent根本不产生任何日志。

部分Agent平台默认生成完整审计追踪，有些则不然。编码Agent重放会话时可能覆盖自身日志，导致安全团队调查事件时发现记录已被擦除。"首先确保日志存在就比人们想象的更困难，"Darley强调，"因为并非所有Agent原生具备日志功能。"

**Part02**

## ****资产清点难题****

在监控Agent行为前，CISO面临更基础的挑战：掌握现有Agent清单。这个看似简单的任务实际异常复杂。大型企业中，Agent的扩散速度远超中央清点能力。营销团队部署AI助手，HR部门使用Agent筛选简历，工程师运行具有广泛文件系统访问权限的编码Agent，非技术人员未经IT批准就将笔记、邮件管理和日程安排等AI生产力工具接入企业账户。

"董事会和CEO正在向CISO提出尖锐问题，"Sullivan说，"公司当前运行哪些AI？它们正在执行什么操作？必须回答这些问题。"Darley建议从结构化清点入手，最好使用专为Agent发现设计的工具，因为通用应用管理系统常无法识别云端、代码库或第三方SaaS平台中的Agent。

"至少从一个系统开始，"她建议，"这将帮助你了解规模、明确责任人，并逐步认知实际所需工具类型。"没有资产清点，行为监控就失去根基。安全团队可以监控已知Agent的日志，但被遗漏的Agent恰恰最可能引发不良后果。

**Part03**

## ****运行时监控实践****

明确Agent分布后，问题转向监控内容与方法。CrowdStrike首席技术官Elia Zaitsev表示，现有终端检测与响应(EDR)工具已能捕获追踪AI Agent所需的行为类型。它们像飞行数据记录仪般监控操作系统，记录每个运行的应用、访问的文件、建立的网络连接和触发的命令。

以CrowdStrike的EDR为例，它会构建威胁图谱——行为与其上游成因的关联地图。当出现可疑网络连接时，威胁图谱可追溯多级关联，定位启动该链条的应用或Agent。"EDR技术能将终端行为与源自Agent驱动应用的事实相关联，"Zaitsev解释，"防火墙仅显示某台电脑正与云端AI模型通信，而EDR能精确指出具体应用与特定模型的对话。"

针对AI Agent，这创造了新的控制维度。系统识别已知Agent应用（如Claude Code、OpenAI的Codex、OpenHands）后，可实施不同于人工操作时的策略。"某些行为由人类执行时可能无害，"Zaitsev指出，"但若由我不完全信任的AI Agent执行，就可能需要动态调整策略。"

**Part04**

## ****构建时安全仍具关键价值****

并非所有企业都直接采用现成AI Agent，许多会自主构建这类系统。因此，运行时监控不意味着构建时安全（代码扫描、部署前模型评估和提示词检查）已经过时。Endor Labs首席执行官Varun Badhwar反对这种观点。

"我从不否认运行时的重要性，"Badhwar告诉CSO，"但你希望尽早解决尽可能多的问题。运行时安全发现的平均成本是4,000美元，而构建时仅需40美元。显然，你希望在问题进入运行时前就解决它们。"开发阶段发现的漏洞只需几分钟修复，但若部署至容器、通过QA并推送到生产环境，解决成本将激增百倍。Badhwar以汽车生产线类比：装配线上的质量控制总比从街头召回7万辆汽车更经济。

他的框架很简单：左移防护，右设屏障。将尽可能多的安全控制移至开发过程——在Agent构建时而非运行时发现问题。然后以运行时监控作为最后防线，因为总有漏洞会漏网，而0Day漏洞本质上无法在构建时预判。

**Part05**

## ****CISO当前行动指南****

对CISO而言，转变重点不在于单一新工具，而在于重新思考AI风险的方式。安全团队不仅需要关注Agent构建方式，还需掌握其在企业系统中运行时的行为表现。

因此，CISO的前进路径不是采购新产品或替换现有基础设施，而是将安全规程系统性地延伸至企业内这类新型行为主体。Zaitsev用深度防御模型阐释：不能因为具备运行时监控就停止构建时防护，二者需要兼顾。"EDR和运行时安全是最后一道安全网，"他说，"你仍然需要所有其他防护层。"

专家建议CISO从以下实践着手实施运行时安全： 首先建立资产清单：选择主要SaaS平台、代码库或终端设备群，清点其中运行的Agent，明确责任人、权限和协议。没有可视性，一切无从谈起。

将行为监控延伸至Agent：通过EDR、专用Agent安全工具或其组合，建立正常行为基准——每个Agent应接触哪些系统？处理哪些数据？与谁通信？偏离基准即预警信号。

实施Agent专属策略：不要用管理员工的相同控制措施管理Agent。它们具有不同的访问模式、风险特征和故障模式。支持Agent识别的工具能根据应用是否由AI驱动差异化实施策略。

预先设计事件响应方案：明确如何在不破坏证据的情况下制止异常Agent。行为日志需存储在独立的写保护库中，而非仅依赖可能被覆盖的Agent平台原生日志。

规划AI驱动的解决方案：面对海量监控需求，仅靠人力无法应对。安全团队需要自动化工具来监控以机器速度运行的系统。

**参考来源：**

Runtime: The new frontier of AI agent security

https://www.csoonline.com/article/4145127/runtime-the-new-frontier-of-ai-agent-security.html

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

内容含AI生成图片

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