---
title: 听劝！OpenClaw用前，先把这个Skill安排上！
url: https://mp.weixin.qq.com/s/lVKdZYeiYIVcaFPRziPStQ
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:07:19.605852
---

# 听劝！OpenClaw用前，先把这个Skill安排上！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ0joGelwLbibEUvJXpplbjjHVJxzicAficscMH9pDWO04yFgFSY5hVNxkJOlEpnq59mdj9GYIr2lp4YFFTXmGE3OwSxlwukiaYbpMCpuERNM38/0?wx_fmt=jpeg)

# 听劝！OpenClaw用前，先把这个Skill安排上！

原创

易盾
易盾

网易智企-易盾

![]()

在小说阅读器中沉浸阅读

近期，国家互联网应急中心（CNCERT）发布重磅安全预警：开源AI智能体框架OpenClaw曝出80+高危漏洞，覆盖提示词注入、恶意插件投毒、远程代码执行等多类攻击面，攻击者可借此远程接管智能体、窃取核心敏感数据，威胁深度波及企业生产环境与个人开发者，目前已有部分高校紧急叫停相关平台使用，安全防控形势刻不容缓。

OpenClaw生态的核心扩展载体——技能（skill），已然成为攻击者的主要投毒靶点。ClawHub作为业内最大的技能分发平台，承载着数万款第三方技能包，而当前社区主流的安全审查方案openclaw-skill-vetter，采用人工引导式审查模式，存在结果不可复现、无量化评分、缺乏云端威胁情报支撑、无法覆盖提示注入等核心短板，根本难以应对日趋专业化、规模化的攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLatCYnqoMOGGlZGSP01LpvLDKQfibhT33iammmrrM1phicjKLrJC0tf92yNMLE34Myu9ialbGtxSicMLAQn314e6XAJlXasYQibQSglo/640?wx_fmt=png&from=appmsg)

安全防护不能只靠“肉眼排查”，AI智能体生态亟需一套自动化、可量化、可审计的前置安全防线，从源头阻断恶意风险入侵。

# 网易智企发布虾壳Skill

针对OpenClaw生态这一行业级安全难题，网易智企易盾安全团队正式推出**yidun-skill-sec（虾壳安全扫描）**——专为ClawHub生态打造的自动化安全扫描技能。产品深度融合静态行为分析与云端威胁情报，在代码运行前为每一款技能生成量化安全评分，精准识别恶意软件、数据窃取、权限滥用、提示注入、代码混淆等全品类风险，为AI智能体应用搭建牢不可破的前置安全屏障。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ0joGelwLbjHKibEYGl2CAa29icE7cdVNMcZ0KQzdntibMicg9zUgmPS5OkdRdJS8It7oEwfDpnZXzImbP7qCDGPoMPrVPm39amSyZ9NMq1CU4/640?wx_fmt=jpeg&from=appmsg)

ClawHub地址：https://clawhub.ai/yd-dev/yidun-skill-sec

GitHub地址：https://github.com/yidun/yidun-skill-sec

虾壳Skill能力：在skill安装之前，用确定性规则+云端智能，替你严审每一行代码。

# 量化风控，实现精准防护

网易智企虾壳Skill摒弃传统人工定性审查的局限，以自动化、量化、可复现的安全检测模式，建立OpenClaw插件安全审查体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLZFFYh08k9wWVYRcvCLHX6t548nwdhkTdwPC61Y2M8V5cwiaktJKYVwsOWRTAkMO731gcB5GTurqiaNQbdfe50yVI614Iy28KDx4/640?wx_fmt=png&from=appmsg)

**1**

四阶架构，结果可复现、可审计

虾壳（yidun-skill-sec）采用企业级四级安全检测流水线架构，从源码溯源、本地排查到云端核验分层递进，确保同一款技能的扫描结果始终一致，具体检测阶段与核心能力如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLa0ezJUD5JeicV3x1c02X7K1VWVMtoBic0UYmz7FBkiaSTYbD5WDHCu2kqFRsI4DIwI3k2el1Iqn3ksg0GFIPO8D7EkpzNd33Bbt4/640?wx_fmt=png&from=appmsg)

### **2** 百分制量化评分，告别主观判断 区别于传统方案模糊的定性判断，虾壳（yidun-skill-sec）采用0–100分连续量化评分体系，通过四大维度信号加权融合得出最终得分，每一分都有据可依，每一项判断都可追溯、可解释，彻底摒弃“我觉得安全”的主观误区。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLYWutOKicBhEksIqMiazds4RI34CRo1TgwnCPq9r1GibxcYchBJ7qYz3qAzlyiamI1yynZ9KWfTQlIlDCdUPUdlpc1qyvVScKe9txI/640?wx_fmt=png&from=appmsg)

最终得分=来源可信度×15%+行为扫描分×40%+云端置信分×30%+权限暴露面×15%

### **3** 17项标签，覆盖核心风险

虾壳（yidun-skill-sec）内置17个精准正则检测标签，完整覆盖AI智能体场景下的核心威胁类型，其中安全绕行、破坏性操作、提示注入三大标签为独家强化检测项，精准补齐行业防控短板。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLaCib0iaUoEoLOjltaIRc772pFGNaAZ7iaRRGv9Ltb3lq9RDN6UdRD3zHuKCqZc3123MicZ2ibYnt8I54iakqvypuyvewFLKiaUhBTSKs/640?wx_fmt=png&from=appmsg)

### **4** 硬性零容忍规则

针对高危恶意行为，虾壳（yidun-skill-sec）设置不可绕过的硬性零容忍规则，无论其他维度得分高低，均无法冲抵高危风险，坚决守住安全底线，具体规则如下：

* 检测到**CRED\_HARVEST（凭证窃取）**：强制降级至🔴SEVERE（严重）等级
* 检测到**PRIV\_ESCALATION（权限提升）**：强制降级至🔴SEVERE（严重）等级
* 同时命中上述两项风险：直接判定为⛔CRITICAL（关键）高危
* 检测到SRC\_BLACKLISTED\_DOMAIN（黑名单域名）：立即判定⛔CRITICAL，跳过所有后续检测

### **5** 云端威胁情报+离线适配

虾壳（yidun-skill-sec）默认接入易盾实时威胁情报数据库，具备实时域名黑名单拦截、恶意包指纹秒判、高级威胁深度分析三大核心云端能力，检测能力持续迭代进化。同时严守隐私合规底线，仅上传哈希值、行为标签、脱敏证据片段，**不上传完整源码、凭证、环境变量、个人数据**，也可通过指令关闭云端通信，兼顾安全与隐私。

针对纯离线无外网场景，产品自动切换至离线防护模式，重新分配权重并叠加保守扣分偏移，断网环境下安全标准只升不降，适配高保密办公、内网隔离等严苛场景：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLZTQcPulmgXaXScIx6lwmfa6fkqjviaLSwexjT4iaKvfFcnibnJyia10qGoXm8hrN0I4TiaTapjk6JaE0FrVTRvk2cxcWgvjNcBCM18/640?wx_fmt=png&from=appmsg)

### **6** 结构化报告输出，效率翻倍

### 虾壳（yidun-skill-sec）可自动生成标准化Markdown检测报告，清晰展示打分明细、风险标签、实证依据，可直接嵌入CI/CD流水线、告警审计系统，每一项扣分精准定位至文件名+行号，开发者无需逐行排查，修复效率提升10倍，大幅降低安全运维成本。演示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLZUgmjaEKptH1IBloX4oibegISC4D0UtqBiaq89iad8wlk90icy1Mq3Ksccavrcr5BmkhFFvTtfEJVjZN4yVPCjB9WydiczW1x2rMAA/640?wx_fmt=png&from=appmsg)

#

# 真实场景验证

场景一：安全包快速放行

ClawHub成熟技能markdown-helper v2.1.0，经全阶检测无风险，云端指纹秒过，最终评分🟢98分（CLEAR），正常安装无拦截，不耽误正常使用。

场景二：恶意包精准拦截

来源不明的perf-booster v1.0.0，命中代码混淆、凭证窃取、外联通信三大风险，触发硬性规则，最终评分⛔28分（CRITICAL），强制阻断安装，杜绝风险入侵。

场景三：提示注入独家检测

常规技能helpful-assistant v1.0.0，暗藏提示注入恶意指令，被PROMPT\_INJECT标签精准命中，降级至🔴39分（SEVERE），及时预警并提醒审核，筑牢隐性风险防线。

# 写在最后

AI智能体生态正在高速发展，技能作为智能体能力扩展的核心载体，其安全性与用户数据与系统稳定性直接关系。本次OpenClaw漏洞事件再次证明：**安全是AI智能体的生命线，前置防护远胜于事后危机**。

网易智企虾壳Skill的发布，希望为ClawHub生态及广大开发者提供自动化、可量化、可审计的安全屏障——让每一项技能在安装前都经过严格审核，让AI智能体在安全的环境中稳定运行。

安全不是选择题，而是必答题。**网易智企，与开发者同行**。

**关于我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ehYgAEz05867UZvA9BFyUd2Q5lhRsLhMthibV04KzJj75WfFQLdTryeA722Va46ea0icm4NophAGm8KshrAicST3w/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

**免费下载干货资料**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ehYgAEz0587IAXGp2Pc7rr0ZAJRlaxPISRj2RdNL4q9lHiaANKo7sDLgKDKycf3OuPtBXqFRwLINvrHoskRic69A/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&randomid=tmwg91d7&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ehYgAEz0587IAXGp2Pc7rr0ZAJRlaxPIuwlP0DOX5yqLP5USV9R8VU8v6REteETJ7PI9Y4AFlbPhQ44ibdlG6sA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&randomid=sirmeop4&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/ehYgAEz0587IAXGp2Pc7rr0ZAJRlaxPIV6tLwsaX5QLEH6WCBqoQSHxm6gQo9DzWQyEibl0tCQX1eoDaTSZ9rUA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&randomid=5fx3ksfs&tp=webp#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/zQ0joGelwLaDxwqX6u6fVmMiauya1icqNxt80lzRT1vribZjZRHvSAtBxF2228WEKpa95s3buDU2HibWaYUn94dsNecYPktZzDptoGGbZdnzVDA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ehYgAEz0587KLs4PyHJbujWQ4n9h71kjWBeJbVBYGAY32CvtzFia8uejH1HIhSKSH7g1vLPMHgw12A7GI0xaDvQ/0?wx_fmt=png)

网易智企-易盾

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ehYgAEz0587KLs4PyHJbujWQ4n9h71kjWBeJbVBYGAY32CvtzFia8uejH1HIhSKSH7g1vLPMHgw12A7GI0xaDvQ/0?wx_fmt=png)

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