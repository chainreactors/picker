---
title: 7 项网络安全国家标准征求意见稿公开征求意见；逆向工程发现：Microsoft Paint 内置强制 InvisMark 隐形盲水印，用户无法关闭| 牛览
url: https://mp.weixin.qq.com/s/TbUAZyCAfGMiP9BlyONhhw
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:34:44.879122
---

# 7 项网络安全国家标准征求意见稿公开征求意见；逆向工程发现：Microsoft Paint 内置强制 InvisMark 隐形盲水印，用户无法关闭| 牛览

# 7 项网络安全国家标准征求意见稿公开征求意见；逆向工程发现：Microsoft Paint 内置强制 InvisMark 隐形盲水印，用户无法关闭| 牛览

安全牛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzHcW4oAwSJEMFkvQUY18xzz5COkicAf6x0M8TcgW7ibUYDTXCh62wMDRsyJOj47ExgER4TibjHiaLzw1ibs4ue688cOyPibJWEicMAawo/640?wx_fmt=png&from=appmsg)

新闻速览

* 7 项网络安全国家标准征求意见稿公开征求意见
* 以网络安全风险为由，美国签署行政令限制电网引入外国电力设备
* 挪威政务基础设施遭遇 DDoS 攻击，多项身份认证公共服务发生中断
* 医疗器械厂商 Boston Scientific 遭遇网络攻击，订单处理与发货流程受阻
* Linux基金会推出AI运行时证据标准TRACE
* 谷歌云推出面向金融与法律行业的Gemini Enterprise解决方案
* Meta 支付 170 亿美元达成和解，推行多项未成年人网络安全保护新规
* 美国财政部成立专项工作组，推动金融业落地抗量子加密迁移
* 逆向工程发现：Microsoft Paint 内置强制 InvisMark 隐形盲水印，用户无法关闭
* AI加速恶意软件开发，但尚未提升攻击成功率

特别关注

**7 项网络安全国家标准征求意见稿公开征求意见**

近日，全国网络安全标准化技术委员会发布通知，就《网络安全技术 移动通信信号屏蔽器技术规范》等 7 项国家标准的征求意见稿向社会公开征求意见。

本次 7 项国家标准由全国网安标委归口管理，现已完成征求意见稿编制工作。按照《全国网络安全标准化技术委员会标准制修订工作程序》相关要求，面向全社会征集修改建议。

相关标准全部材料已上传至网安标委官方网站，访问地址为https://www.tc260.org.cn/portal/suggestion，社会各界单位及个人均可查阅文稿并提交反馈。意见反馈截止时间为 2026 年 10 月 25 日 24:00，逾期将不再接收相关建议。

通知同时公布秘书处联系方式，联系人张老师，联系电话 13051502670，电子邮箱zhangbr@cesi.cn，相关意见可通过上述渠道提交。

本次系列国标涵盖移动通信信号屏蔽器等网络安全技术领域，标准落地后将进一步完善国内网络安全标准体系，为对应产品技术研发、检测、应用实施提供标准化依据，行业从业者可结合业务实践积极建言。

原文链接：

https://mp.weixin.qq.com/s/R4PoedTiAWReut9qjwy3Gw

**逆向工程发现：Microsoft Paint 内置强制 InvisMark 隐形盲水印，用户无法关闭**

安全研究员 Xusheng Li 发布逆向工程报告，揭露 Microsoft Paint 与 Photos 会为 AI 生成图片植入名为 InvisMark 的不可见盲水印，该机制独立于可手动开关的 Copilot 可见水印，用户无法彻底关闭该功能。

即便 AI PC 依靠本地 NPU 运行 Stable Diffusion 完成图像渲染，整个流程也并非完全离线。生成前 Paint 会将提示词、风格参数上传微软服务器审核，服务器返回经过调整的提示词、生成 ID 以及 16 字节的 GUID 水印标识，设备拿到返回数据后才会本地出图。系统会将 16 字节 GUID 扩展为 144 比特数据，修改图片大量像素完成水印嵌入，512×512 尺寸图片会有超 19 万像素发生细微改动。

Paint 将写入盲水印设为强制流程，水印写入失败则直接终止图片生成；Photos 行为存在差异，水印异常仅记录日志，依旧输出图片。

微软采用双重溯源方案，除像素层的盲水印外，还会写入 C2PA 内容凭证元数据，两份凭证信息相互对应。即便清除 C2PA 元数据，截图、裁剪等常规操作也难以彻底破坏像素内的盲水印，微软仍可通过像素分析识别图片来源。

原文链接：

https://securityonline.info/microsoft-invismark-invisible-watermark/

热点观察

**以网络安全风险为由，美国签署行政令限制电网引入外国电力设备**

当地时间 2026 年 8 月 26 日，美国总统 Donald Trump 签署行政令，宣布国家进入能源紧急状态，针对美国大宗电力系统（bulkpower system）实施外国设备管控，防范网络安全带来的基础设施风险。

该行政令规定，被认定存在重大国家安全风险的外国产设备、软件及数字组件，将禁止在美国境内采购、进口、转让与安装；确有必要使用的，也需设置附加条件化解安全隐患。美方文件提出风险假设，称相关设备可能内置数字后门，可供境外主体远程访问，成为恶意网络活动的攻击载体。

本次行政令是特朗普政府此前相关政策的延续。其第一任期曾出台同类行政令，后被 Biden 政府暂停并修订，当时部分公用事业企业反馈合规落地难度较高。

按照新行政令要求，美国能源部（Department of Energy）需联合其他部门，在 120 天内制定配套实施细则。报道提及，中国在光伏供应链、电力变压器制造领域占据较高市场份额，也是本次政策指向的背景因素之一。

原文链接：

https://cyberscoop.com/energy-department-cybersecurity-executive-order-rules/

**Meta 支付 170 亿美元达成和解，推行多项未成年人网络安全保护新规**

近日，社交媒体巨头 Meta 与美国几乎全部州及属地达成标志性诉讼和解，将支付 170 亿美元罚金，同时落地一系列未成年人网络保护改革，该案成为美国隐私与儿童网络安全领域的标杆判例。

本次诉讼由加利福尼亚、科罗拉多等州牵头，指控 Meta 明知 Facebook、Instagram 具备成瘾性却刻意隐瞒相关研究结论；同时违反《儿童在线隐私保护法》（COPPA），仅依靠用户自主填报年龄，未采用人脸识别等可靠年龄核验手段，收集 12 岁及以下儿童的数据。和解协议在民事审判启动数日后敲定。

按照和解条款，Meta 需对 18 岁以下用户实施多项强制管控：每日使用时长上限为 2 小时；午夜至清晨 6 点禁止青少年访问平台；屏蔽青少年帖子的点赞等互动反馈；禁用医美修图滤镜；晚 22 点至早 7 点以及上课时段默认关闭推送通知。平台需提供非算法驱动的非个性化信息流；青少年提交的有害内容举报，90% 须在半天内完成响应。

Meta 将聘请拥有完整信息调取权限的独立审计机构，审计方有权向各州总检察长反馈风险问题；同时 Meta 不得就自身安全功能发布虚假、误导性表述。此外 Meta 单独向得克萨斯州支付约 10 亿美元解决同类指控。

该和解的最终金额，还将取决于 Snap、TikTok、YouTube 等其他科技企业是否接受同类处罚。Meta 呼吁竞品跟进这套保护标准，而大量来自家长、学区的相关诉讼仍在推进，本次和解对其余案件的影响尚不明确。业内评价称，该事件相当于社交媒体行业的 “大烟草时刻”，倒逼平台将儿童安全嵌入产品设计。

原文链接：

https://therecord.media/meta-settlement-children-online-safety-social-media

**美国财政部成立专项工作组，推动金融业落地抗量子加密迁移**

2026 年 8 月 26 日消息，美国财政部正式设立 QuantumReadiness Task Force（量子就绪特别工作组），联动金融机构、技术厂商与政府部门，统筹推进金融行业向抗量子加密（quantumresistant encryption，又称后量子密码 postquantum cryptography）体系迁移，防范未来量子计算机破解现有加密机制带来的数据泄露风险。

工作组设置三条业务主线：统一金融业的密码转型节奏、保障技术供应商的算法适配能力、评估量子计算对加密货币等新兴技术带来的安全影响。其工作重点包含梳理关键业务依赖关系、提升密码敏捷性、保障互操作性、强化业务韧性，同时解决第三方供应链、数字资产相关落地难题。

美国国家标准与技术研究院（NIST）自 2016 年启动标准化项目，现已批准多款抗量子加密算法。密码学界尚未确定具备破解能力的量子计算机何时问世，主流预判时间窗口为 510 年。攻击者可当前先窃取加密数据，待量子算力成熟后再解密，形成 “先窃取、后解密” 的现实威胁。

该举措承接 2026 年 6 月 Donald Trump 签署的行政令，行政令为联邦机构及承包商设置后量子密码的强制落地时限。此外，G7 网络专家小组已于今年 1 月发布全球密码转型路线图，西方盟友正在协同推进该项工作。财政部官员 Luke Pettit 表示，量子计算潜力巨大，但也对支撑美国金融体系的密码工具构成长期严峻挑战。

原文链接：

https://www.cybersecuritydive.com/news/quantum-cryptography-treasury-task-force-financial-industry/828732/

安全事件

**挪威政务基础设施遭遇 DDoS 攻击，多项身份认证公共服务发生中断**

当地时间 2026 年 8 月 24 日凌晨 3 点 38 分，挪威数字化管理局 Digdir 遭遇大规模 DDoS 攻击，造成该国多项核心政务数字服务出现业务扰动，这是短时期内该机构遭受的第三次同类攻击。

本次攻击波及 IDporten 身份网关、Maskinporten 机机认证枢纽、MinID 电子身份、Altinn 门户、eSignering 电子签名等一批关键公共组件。部分服务曾短暂完全不可用，多数时段处于部分可用状态，出现登录缓慢等故障。Digdir 联合分包商 Vivicta 开展应急处置，截至通报发布，多数业务趋于稳定，IDporten 仍存在局部访问异常。

Digdir 负责人 Frode Danielsen 表示，该攻击目标为破坏服务可用性，并非入侵系统，暂无证据显示发生安全突破或个人数据泄露。安全行业人士指出，把全国公共服务汇聚至单一认证网关，便于策略统一管控，但该单点也会成为高危瓶颈，需要完备的 DDoS 防护能力。部分业内观点认为，本次攻击具备典型破坏性干扰活动特征。

原文链接：

https://www.infosecurity-magazine.com/news/ddos-attack-hits-norwegian/

**医疗器械厂商 Boston Scientific 遭遇网络攻击，订单处理与发货流程受阻**

当地时间 2026 年 8 月 25 日，医疗器械企业 Boston Scientific 遭遇网络攻击，事件波及企业 IT 网络及核心业务应用，造成全球运营扰动，客户订单处理、产品发货功能受到影响，该企业已向美国证券交易委员会提交 8K 文件对外披露本次事件。

事件发生后，企业立即启动事件响应预案，联合第三方网络安全专家开展调查与威胁处置。其位于爱尔兰的三处制造及研发设施受冲击，当地大量员工被安排居家办公。目前企业正推进系统恢复工作，但尚未确定完成全部修复的时间节点，攻击入侵路径、事件带来的运营及财务影响均无法判定。

报道提及，医疗器械行业近期网络安全风险高发，今年 3 月同行企业 Stryker 也曾遭遇网络攻击，攻击者利用 Microsoft Intune 环境对数千台设备执行数据擦除操作。医疗制造企业业务系统中断，将直接影响医疗设备供应链流转，给医疗机构带来间接业务压力。

原文链接：

https://www.cybersecuritydive.com/news/boston-scientific-cyberattack-disrupted-order-processing-shipping/828816/

安全攻防

**AI加速恶意软件开发，但尚未提升攻击成功率**

Palo Alto Networks旗下Unit 42对405个与AI相关的恶意软件样本进行分析发现，AI正在明显加快攻击工具的开发和变种速度，但尚未显著提高恶意软件突破现有安全防御的能力。约97%的样本仅存在于沙箱、研究代码库或内部测试环境，真正出现在生产终端的仅12个。

研究人员通过终端遥测、送入沙箱分析的网络会话以及内部告警记录交叉验证样本哈希。12个进入真实终端的样本涉及5个恶意软件家族、分布于3个国家，而且全部触发了安全告警。未进入生产环境的样本主要包括概念验证（PoC）代码、防御测试样本，以及借用热门AI产品名称诱骗用户下载、实际并无AI功能的恶意程序。

实际攻击中，FunkSec勒索软件被认为存在LLM辅助开发迹象。传播最广的Recipe Lister伪装成食谱应用，安装后启动后门，影响超过50家机构，产生约6500条终端记录和9600次告警。Oyster后门则冒充Dropbox安装程序，攻击者利用AI生成投递代码，以更低成本、更快速度建立初始入侵点。另有样本投递Rhadamanthys信息窃取程序，或利用COM hijacking实现持久化。

值得关注的是，现有防御技术成功发现了全部12个真实环境样本，包括sandbox detonation、behavior-based detection、数字签名异常检测以及文件加壳或加密程度分析，无需引入专门针对AI恶意软件的新检测方法。Unit 42认为，现阶段AI带来的主要变化是提高攻击工具开发和迭代效率，而非赋予恶意软件更强的隐蔽或绕过防御能力。

原文链接：

https://www.securityweek.com/ai-speeds-up-malware-development-not-its-success-rate-analysis/

产业动态

**Linux基金会推出AI运行时证据标准TRACE**

2026 年 8 月 25 日，Linux Foundation 发布 TRACE（Trust, Runtime Attestation and Compliance Evidence）开放规范，该标准由 OPAQUE 主导研发，AMD、Intel、Microsoft、Technology Innovation Institute（TII）参与支持，旨在解决生成式 AI 尤其是 AI Agent 行为难以举证审计的安全痛点。

TRACE 整合 IETF/IRTF 的 RFC 9711（EAT）、RFC 9334（RATS）、SCITT 等已有标准，依托 AMD Secure Encrypted Virtualization（SEV）硬件安全能力，生成硬件背书、密码学可校验的防篡改凭证，记录 AI Agent 运行环境、执行软件、生效策略、数据分级与调用工具。该证据可跨云厂商、机密计算环境迁移，支持第三方独立核验 AI 工作负载真实执行情况。

该标准参考库自 6 月机密计算峰会发布后，10 周内 PyPI 下载量接近 135000 次，技术文档与参考实现已在 GitHub 公开。研发方表示，OpenAI Agent 测试期间突破 Hugging Face 基础设施等事件，凸显仅依靠策略与沙箱配置，无法证明 AI 实际运行行为，TRACE 可以补齐该证据缺口。

原文链接：

https://www.infosecurity-magazine.com/news/linux-foundation-trace-standard-ai/

新品发布

**谷歌云推出面向金融与法律行业的Gemini Enterprise解决方案**

当地时间 2026 年 8 月 25 日，Google Cloud 发布 Gemini Enterprise for Financial Services 与 Gemini Enterprise for Legal 两款垂直行业 AI 方案，产品基于 Gemini Enterprise 底座打造，面向金融、法律等高监管行业解决通用大模型幻觉、数据泄露、合规审计等痛点。

方案依托 Model Context Protocol（MCP）协议，在不迁移企业私有数据前提下，安全对接内部数据库与第三方专业数据源，全部模型输出、Agent 逻辑内置审计日志，保障每一次 AI 推理均可溯源核验。金融版本内置拥有 50 余项专项能力的金融研究 Agent，可对接 LSEG、Moody’s、S&P Global 等数据源，支持 A2A API 接入业务流程，德意志银行、CME Group 等机构已参与试点。法律版本适配合同审阅、文书起草等业务，可继承律所原有权限与信息隔离规则，对接 Docusign、iManage 等法律系统。

整套方案把 AI 从对话工具转化为行业专用智能体，保障企业知识产权与敏感客户数据不流出安全边界，尝试解决强监管领域 AI 落地的集成与安全难题。

原文链接：

https://securityonline.info/gemini-enterprise-finance-law/

**联系我们**

合作电话：18610811242

合作微信：aqniu001

联系邮箱：bd@aqniu.com

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/wKeDC5RjIzFXKk7PcPusXL6KK6OabsIgnbR1NdF1uQCpQY1icficL4yagruo8Pa6ia5Bgfn3tIETjCXGo15X61WsvhfRHUuDmROpWUiaJUe8WJ8/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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