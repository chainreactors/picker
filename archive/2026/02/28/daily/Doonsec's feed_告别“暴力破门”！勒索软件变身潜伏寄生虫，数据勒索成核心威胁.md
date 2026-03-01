---
title: 告别“暴力破门”！勒索软件变身潜伏寄生虫，数据勒索成核心威胁
url: https://mp.weixin.qq.com/s/bV3hAV4lGLXUGfP6ErJvJg
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:18:48.095061
---

# 告别“暴力破门”！勒索软件变身潜伏寄生虫，数据勒索成核心威胁

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rCyTtezQr4nhQO5HVfic5zgxibZcvkib0DpiaXMRgIVJOfPkQg4jJaLHpxckIjV1VtWs00KqrjbZXIHlZPJTtjgo8qQXxzn9lbnSzJ7ibUa7X8DE/0?wx_fmt=jpeg)

# 告别“暴力破门”！勒索软件变身潜伏寄生虫，数据勒索成核心威胁

原创

John
John

信息安全D1net

![]()

在小说阅读器中沉浸阅读

点击上方“**蓝色字体**”，选择 “**设为星标**”

关键讯息，D1时间送达！

![图片](https://mmbiz.qpic.cn/mmbiz_png/ianq03UUWGmIjdcvsRu9vwib8r3GibibtkQ76vGtFtHTbTPt4Mv8DeVcFvCNnaC5QLD1DibIL4CllIO0szRSzdd0L4g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

**企业网D1net**

勒索软件攻击正从高调加密转向隐蔽潜伏与数据窃取，报告显示，攻击者更侧重持久化与防御规避，甚至利用OpenAI、AWS等受信任平台隐藏C2流量。尽管加密行为减少，ESET与GuidePoint指出活跃团伙与受害者数量仍在上升。Qilin、Cl0p、Akira等团伙活跃，“勒索即服务”加速扩散。专家建议CISO强化身份管控、监控第三方集成，并将检测重点转向长期驻留与数据外泄行为，以应对“寄生式”威胁新常态。

攻击者正从“掠夺式”的快速攻击转向“寄生式”的长期潜伏，CISO必须强化身份管控，密切监控受信任的应用程序及集成，并将检测策略聚焦于攻击者持久化驻留行为。

随着敏感企业数据公开泄露的威胁成为勒索的主要手段，勒索软件攻击者正转变策略，采用更为隐蔽的渗透方式。

Picus Security的年度红队演练报告显示，攻击者正从高调破坏转向静默的长期访问——即从“掠夺式”的快速攻击转向“寄生式”的静默潜伏。

在勒索软件变种最常用的五种攻击技术中，有四种旨在攻击者获得初始访问权限后保持隐蔽。例如，据专门从事漏洞利用和攻击模拟的网络安全公司Picus Security称，随着攻击手段的演进，勒索软件行动越来越多地采用防御规避和持久化驻留技术。

攻击者还越来越多地通过OpenAI和AWS等受信任的企业服务路由命令与控制(C2)流量，使恶意活动更接近正常业务流量。

Picus Security的结论基于攻击模拟，并结合对110万份恶意文件和1550万次映射至MITRE ATT&CK框架的对抗性行为的分析得出。

Picus关于攻击者更倾向于隐蔽和持久化而非高调破坏的发现，与Securin的勒索软件研究结果一致。Securin报告称，攻击者在攻击企业系统时正串联利用多个漏洞。

“勒索软件团伙不再将漏洞视为孤立的入侵点，”渗透测试和网络安全服务公司Securin的首席威胁情报分析师Aviral Verma表示，“他们将这些漏洞组合成蓄意的利用链，不仅根据严重程度选择弱点，还根据它们在瓦解整个平台的信任、持久化和操作控制方面的有效性来选择。”

AI如今已广泛为威胁行为者所利用，但它在勒索软件攻击中主要起增强作用，而非驱动作用。

**双重威胁**

勒索软件团伙通常偏好双重勒索策略，即结合以泄露被盗信息为威胁的黑客手段，以及在入侵企业网络后通过加密数据造成的破坏进行勒索。

Picus报告称，随着更多网络犯罪分子转向以静默窃取数据作为主要勒索手段，过去12个月内加密行为减少了38%。

Picus关于勒索软件攻击数量下降的说法遭到了其他专家的质疑。

终端安全供应商Eset的首席安全布道者Tony Anscombe提出了不同观点。

“在Eset最近发布的《2025年上半年威胁报告》中，检测数据显示，上下半年间增长了13%，同时通过ecrime.ch公开报告的受害者数量增加了40%，那么勒索软件[的威胁]似乎并未减少。”Anscombe告诉记者。

网络安全服务公司GuidePoint Security的高级威胁情报顾问Nick Hyatt表示，去年有超过7000名受害者的数据被公开，这一数字可能还不包括“那些支付了赎金且未被威胁行为者公开的受害者”。

GuidePoint表示，去年活跃的勒索软件团伙数量创历史新高，远未显示出任何整合的迹象。

“威胁行为者精简了攻击能力，综合运用既有技术、漏洞利用和新型攻击手段来实现目标。”Hyatt说。

**恶名昭彰的团伙**

专家普遍认为，Qilin、Cl0p和Akira是最活跃的勒索软件团伙，但也不乏其他竞争者。

“从Huntress 2025年的数据来看，Akira如今是排名第一的勒索软件团伙，”托管检测与响应公司Huntress的安全运营高级经理Dray Agha表示，“他们的攻击手段正在迅速演变，专门用于抵消现有安全解决方案的作用，我们正看到他们积极瞄准虚拟机管理程序层面，以完全绕过传统的终端安全保护。”

应用安全公司Black Duck Software的高级总监兼杰出技术专家Collin Hogue-Spears表示，勒索软件运营者已不再像有组织犯罪那样运作，而是开始像平台企业那样运作。

“Qilin在2025年公布了超过1000名受害者，是前一年的七倍，”Hogue-Spears说，“LockBit 5.0在被打击后恢复了运营能力。”

与此同时，Scattered Spider/Lapsus$/ShinyHunters(SLSH)联盟正在推行“勒索即服务”模式，这一做法使得技术不那么熟练的网络犯罪分子也能轻松非法牟利。

SLSH已在网络犯罪生态系统中引发了“结构性转变”。

“六个月内出现了73个新团伙，因为他们不再需要自己开发工具，”Hogue-Spears说，“他们租用工具。”

**新威胁技术要求重新思考安全策略**

托管检测与响应公司Quorum Cyber威胁团队成员Vasileios Mourtzinos表示，越来越多的团伙正放弃高影响力的加密攻击，转向以数据窃取和长期、低噪音访问为优先的勒索模式。

“这种由Cl0p等行为者通过大规模利用第三方和供应链漏洞而流行起来的方法，如今正被更广泛地效仿，同时伴随着对有效账户的更多滥用、利用合法管理工具融入正常活动，以及在某些情况下试图招募或激励内部人员以协助访问。”Mourtzinos说。

勒索软件团伙不断演变的攻击手段应促使防御策略重新思考。

“对于CISO来说，当务之急是加强身份管控，密切监控受信任的应用程序和第三方集成，并确保检测策略聚焦于持久化驻留和数据窃取活动。”Mourtzinos建议道。

版权声明：本文为企业网D1net编译，转载需在文章开头注明出处为：企业网D1net，如果不注明出处，企业网D1net将保留追究其法律责任的权利。封面图片来源于摄图网

（来源：企业网D1net）

**关于企业网D1net(www.d1net.com)**

国内头部to B IT门户，同时在运营国内头部的甲方CIO专家库和智力输出及社交平台-信众智(www.cioall.com)。旗下运营19个IT行业公众号(微信搜索D1net即可关注)

如果您在企业IT、网络、通信行业的某一领域工作，并希望分享观点，欢迎给企业网D1net投稿。

**投稿邮箱：**

editor@d1net.com

**合作电话：**

010-58221588（北京公司）

021-51701588（上海公司）

**合作邮箱：**

Sales@d1net.com

企业网D1net旗下信众智是CIO（首席信息官）的专家库和智力输出及资源分享平台，有六万多CIO专家，也是目前较大的CIO社交平台。

信众智对接CIO为CIO服务，提供数字化升级转型方面的咨询、培训、需求对接等落地实战的服务。也是国内较早的toB共享经济平台。同时提供猎头，选型点评，IT部门业绩宣传等服务。

**扫描 “****二维码****” 可以查看更多详情**

![图片](https://mmbiz.qpic.cn/mmbiz_png/OuQdh6iaViaXaIOY0mjrTgicElErUqymD4icjEneq6YYVpiadU3pDLRHwqFrW9Y2Ht0uKeuIEjO3hDxfiatbI5KcibHIA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OzWRicKEIic7rbqI3su0DLdbU7buic1GsAXC0licpicphiadfkK8yfg8hogxXc3aicicibXIooiaqicTLM20CSYYl0G4ldic7g/0?wx_fmt=png)

信息安全D1net

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OzWRicKEIic7rbqI3su0DLdbU7buic1GsAXC0licpicphiadfkK8yfg8hogxXc3aicicibXIooiaqicTLM20CSYYl0G4ldic7g/0?wx_fmt=png)

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