---
title: 新品发布|万径千锋-测评系统正式发布
url: https://mp.weixin.qq.com/s/QcbDvDifAFerusqpY437xA
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:30.093608
---

# 新品发布|万径千锋-测评系统正式发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2VZeYMz4vBoS3LaPtaLY0qRUibY9XqzvYM7EzGvCaornhQic2Rtgm8vd5A3j7xRGPYKm7VaC28q4YFmSI15VibKOT1Du5Nw8uDAmDVc3htCQpQ/0?wx_fmt=jpeg)

# 新品发布|万径千锋-测评系统正式发布

原创

MegaVector
MegaVector

万径安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/qdI65GS20NQQicuyMeMLu91BicIfGa3MicPLg2dic9GvNoVerFfMh2Vib8hicVFsuI4Cq4MtlTMj0QickZefFU1Ria00WQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2VZeYMz4vBpib7PHakSmoosnqNMIfZYx5TI5UWTiaibZQYVEWTVDVGVZcrZSebjmgOcbNJIdN5JLQvwFS3GSzB41icmspl6iatSsf84hicAmicF7B4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2VZeYMz4vBqrtEAdqHkbk6NHxXEMhMXEvCSkcmCFcyl4jUdnjCN2cKSOMewlT2ffVsON75X75161iaWxm7uficcq1vCaicrq830FzB5tn38O7c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBoBdcvRvqda7htXkibNOhpibcZicwaHs20YsYP6M4aElSFFKqEBMh9JXM3g8ZPnCnIY12lAWotzJAKIiciac8vzPRibpKGJAu9FaENzQ/640?wx_fmt=png&from=appmsg)

政企在自研、采购大模型与智能体建设过程中，普遍面临四大安全测评难题：

**1.AI****独有风险繁杂，传统测试手段失效**

大模型具备开放式输入、概率输出、多轮上下文、工具协同四大特征，风险横跨模型、业务、数据、权限全维度。模型层面存在越狱诱导、敏感信息泄露、偏见歧视、幻觉错误；智能体业务层面易发工具越权、RAG文档外泄、业务规则绕过。人工抽样仅能覆盖少量场景，海量变异攻击用例无法依靠人力全覆盖。

**2.重点行业合规严苛，云端测评触碰红线**

金融、政务、能源、涉密单位明确要求测评数据禁止出内网、大模型本地化部署、全测试流程留痕审计。多数云测评产品需要上传测试样本至公网云端，无法满足内网隔离环境使用要求。

**3.AI****安全人才稀缺，****外包****测评成本高昂**

国内专业AI安全测评人员缺口大，自建测评团队成本高；模型新版本上线、知识库迭代、日常巡检都需重复测评，长期外包第三方服务大幅拉高合规成本。

**4.新型攻击层出不穷，事后补救代价巨大**

多模态投毒、渐进式越狱、编码混淆绕过、逻辑陷阱诱导等新型攻击持续更新，漏洞爆发后极易引发数据泄露、业务错乱，带来监管处罚与经济损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBrrYXoLgv5LUQXxtpZXILpibpHYwniaruBdQeicDvMn0mLeUJIIYy577BE24FqfE7DFOjpUXaTllCO30uvrssMwJhyJxq3GNXkdoU/640?wx_fmt=png&from=appmsg)

万径千锋依托万径安全多年攻防沉淀与自主YAK安全技术，搭建**标准用例层-对抗样本层-评分判定层**三层评测架构，实现合规基线+对抗穿透+智能判定一体化。

### 1. 标准用例层：锚定国标合规底线

内置对标国内GB/T标准的合规题库与红队样本库，覆盖涉政敏感、隐私PII、歧视偏见、商业保密、医疗金融合规等类目，适配金融、电信、医疗等七大行业规范。每条测试用例绑定风险标签、判定规则与容忍阈值，自动生成结构化合规结果，满足监管验收要求。

### 2. 对抗样本层：自动生成海量变异攻击用例

系统依托前沿攻击算法自动生成多样化恶意Prompt，支持Base64、异形字符、摩斯密码等编码绕过；图片、音频、Emoji多模态载荷投毒；集成Crescendo、GOAT、GCG、MathPrompt等主流越狱框架，实现多轮递进、逻辑欺骗、角色扮演嵌套等穿透测试，可按攻击难度、风险类型精准筛选用例。

### 3. 双引擎评分判定层：规则+本地大模型联合审裁

采用固定规则引擎+本地LLM-as-Judge双评审模式：硬性规则精准判定SQL注入、明文隐私泄露等确定性风险；本地化评价模型负责模糊语义内容判定，每条结果附带置信度与判定依据，支持人工复核。整套判定流程内网闭环，所有数据不出本地机房。

![](https://mmbiz.qpic.cn/mmbiz_png/2VZeYMz4vBrmHMPbFe8KibJ8tiavHAs4PNxYdcDZTnGkUAib7N0moXIP1q4ShXZM9m49oLicgWZaicmsP31zAwxZA7Y8f1r7772q5EWvfuLYG2mQ/640?wx_fmt=png&from=appmsg)

系统配套两大关键技术：一是**本地生成评价模型**，通过OpenAI兼容接口对接企业私有大模型，用例生成、打分全内网运行；二是**可视化任务编排**，向导式配置测评参数，系统自动生成DAG执行链路，支持批量调度、定时复测、多版本A/B对比。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBrZqXUeKibZE3XLvyYlwCk0xqesWzUX4CkPkYVnh0pNa1yXvicEXqqbGwYliaWXG4aR8xDBQKJyVx6goFzibPcKLVb6QLA9XnAjMib8/640?wx_fmt=png&from=appmsg)

产品采用分层解耦架构设计，全栈自主可控，兼容麒麟、统信UOS等国产化操作系统与国产硬件，支持软件私有化、硬件一体机两种落地形态。

|  |  |
| --- | --- |
| 层级 | 核心能力 |
| 用户访问层 | 统一Web控制台，分级配置管理员、测试员、审计员权限 |
| 业务应用层 | 覆盖大模型上线、迭代、巡检、加固全生命周期安全管控 |
| 评测能力层 | 95类安全检测插件、自动化攻防套件、风险聚合与报告引擎 |
| 模型协同层 | 兼容40+主流大模型，支持HTTP、WebSocket、自定义脚本接入私有模型 |
| 数据资源层 | 统一管理数据集、审计日志、测评报告，全流程操作可追溯 |
| 基础设施层 | 基于Docker容器部署，适配服务器集群、隔离内网、国产化机房 |

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBrbtjAw6icK3wo8z4VXeJdure3O6bYbbrFZd1EYdFLMMo0EdO5WyJxjf9L5VVFC4LNN6bjzHeCiapEV7zRLz9BD6MQ1N0N8ch3gw/640?wx_fmt=png&from=appmsg)

**1.异构模型快速接入**：兼容国内外主流大模型，智能识别智能体业务场景并生成定向攻击用例，全链路连通校验快速完成接入。

**2.全品类风险检测**：囊括AI原生内容风险、PII隐私泄露、提示/SQL注入、智能体越权劫持、RAG投毒、行业合规六大类95项检测项。

**3.多模态越狱专项测试**：图片、音视频、特殊符号载荷绕过文本审查，精准校验多模态内容安全短板。

**4.动态任务管控**：灵活创建单轮/多轮测评任务，支持任务暂停、重测、用例回放；规则+LLM+人工三重校验降低误报。

**5.风险可视化分析**：自动生成风险热力图，横向多模型版本对比，直观定位系统薄弱风险点。

**6.第三方漏洞报告核验**：导入主流安全厂商扫描报告，自动化验证漏洞真伪，剔除无效误报。

**7.权威数据集资产沉淀**：内置国标、Aegis、BeaverTails等开源测评数据集，支持企业自定义业务专用用例库。

**8.全链路权限审计**：从任务创建到结果输出全链路日志留存，满足政务、能源行业审计溯源要求。

**9.标准化报告一键输出**：自动生成合规测评文档，支持在线预览、链接分享、批量导出，可直接用于项目验收与监管报送。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBoX2Pic3uvKsK0BeoX0A3xDaaCDKiaFcqC28zK4QuJm9BMW8YMWOXDvVKYELfkEg2otk3GxUwdA4GD0kBM2luaICvWics4iaUnBJmU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBoibys5sjhIyuh0fMfCHIBIAtDIekJhtJGT6BNgooLnYHSOKj7INIAGNkJ0H66CcWqqhMNXflzOdqmTsdcMgsvaAa793JibO6cZQ/640?wx_fmt=png&from=appmsg)

### 1. 安全价值：私有化闭环部署，守住数据安全底线

全测评流程内网运行，测试数据、业务知识库、模型参数全程不外流，从根源规避云端测评的数据泄露隐患，适配涉密、金融等高安全等级场景。

### 2. 成本价值：自动化替代多数人工，削减外包开支

系统可替代重复性人工测评工作，模型上线、版本迭代无需高频采购第三方测评服务，大幅压缩年度安全预算。

### 3. 业务价值：上线前置全量体检，规避生产安全事故

大模型与智能体投产前完成全面攻防测试，提前整改幻觉、越权、数据泄露等隐患，杜绝“带病上线”引发的业务故障与监管处罚。

### 4. 技术价值：统一测评底座，实现多AI资产集中治理

企业内部多套自研、外购大模型统一接入系统，标准化安全基线，实现AI资产全生命周期安全治理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBrjW6RPSGq2lEsANpOO4Zj5iaicRUahWYkWPCm321IDnrNKbk5d8Jk5BNibucdIB9f6r2ZcgSn6bgqVXxY91axomKk35VSsVxpftA/640?wx_fmt=png&from=appmsg)

### 项目背景

### 某能源企业在电力营销、工单处置场景批量落地AI智能体，安全测评团队人员紧缺，仅能抽检核心系统，大量版本更新缺少安全检测，长期依赖外部厂商测评，同时面临智能体越权查隐私、RAG泄密、模型生成错误工单等潜在风险。

### 落地成果

项目落地万径千锋私有化系统，用于新智能体上线验收与版本更新复测：依托系统自动化对抗用例库批量巡检业务系统，上线初期即发现越权访问、知识库泄露、模型幻觉多项高危漏洞并提前修复；单人即可完成原有多人月度测评工作，人力投入下降，告别高价外包测评，顺利通过企业内部合规审计。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBosicjyt1gTLXKaw8cPJ2ZMq7ACfzUADwDel9dK6OvFfjicI6NGTtRaKicXJmibo6Ziam5FrvxeEtS63e2rGe72yh7Qz6VdUkrda7wM/640?wx_fmt=png&from=appmsg)

### 适用场景

1.新大模型、业务智能体上线前安全验收；

2.模型微调、知识库更新后的版本复测；

3.新型AI漏洞爆发后全资产批量排查；

4.监管检查前内部合规自查；

5.第三方进场测评前置自检。

覆盖：能源、政务、金融、运营商、医疗、科研院所、涉密单位全行业。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2VZeYMz4vBpicUIcOJDBhzJ3xibr5hrW8RH96SBUjtiadD4GGuggTo1Uuu0Jp1kOASPGStczbIbjXVTwnIlAnCBTYUA3ob5Iuf09Uqic4BD9ulI/640?wx_fmt=png&from=appmsg)

**往期内容回顾**

（点击图片即可浏览文章）

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/qdI65GS20NSMhvk7oYWriaVIb7iaWInTZUicMBgMnL23W9K5LVicRlB0Zg2XUnVB0dm87yeCSia6LOxRA0wZPfib7OLA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIwMzI1MDg2Mg==&mid=2649945629&idx=1&sn=0bab7c1e231a7349a15634e93e03a031&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/qdI65GS20NSMhvk7oYWriaVIb7iaWInTZU8ZgvZJ9OkuUtpGfPqjBPSiaoqbP13qVRjZibHu4lwSNHbO5EOWOxnia1g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIwMzI1MDg2Mg==&mid=2649945712&idx=1&sn=046bd6c473ff5faf53b0ba99447652a6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/qdI65GS20NREKQP7Ry2G4I5IN8VQD7j4rnGrFQwao6c4bJDVFONibibBSH7ZykJ8BHsKPib0O1nPkhXqkhugPbKGQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIwMzI1MDg2Mg==&mid=2649944736&idx=1&sn=ded070af9bb3facd7fdf285c072d73ef&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/qdI65GS20NRiajgNhgnbib3CAI5XLC1A7azgiawwDCDR68esGucGgdH50uRNDgbuNvtNn5KoeVC2MJmqicRKnrR7aA/0?wx_fmt=png)

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