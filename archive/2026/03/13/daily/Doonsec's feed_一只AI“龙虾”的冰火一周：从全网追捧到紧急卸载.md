---
title: 一只AI“龙虾”的冰火一周：从全网追捧到紧急卸载
url: https://mp.weixin.qq.com/s/ojPkvk5wVy5lAq25xgkfZg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:07:53.392993
---

# 一只AI“龙虾”的冰火一周：从全网追捧到紧急卸载

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2icibGKbYdhcwtKxLUYuic6AQakqaibicKR3qsEwDeFeqaurZibwjQT0xciak1v2qNvzF075tCCYttdU7xTLgOxHmMAFRh2Lib6ibOk6m2kUOXcibeTdk/0?wx_fmt=jpeg)

# 一只AI“龙虾”的冰火一周：从全网追捧到紧急卸载

原创

绿盟君
绿盟君

绿盟科技

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2icibGKbYdhcwJJ5MiaUhnk62LLZoqJv4rNice8c97LqKZtpIiaRorFicyeRao4bJMGbxeyLEpJLU1qKc449DicZkcIibBYtsrsPtlK4wicRIjnPExmY/640?wx_fmt=gif)

一场轰轰烈烈的“养虾运动”，从全网追捧到紧急卸载，只持续了短短一周。二手平台已经出现另一种服务：远程卸载OpenClaw。价格从499元安装到299元卸载[1]，一条“装虾—教虾—卸虾”的产业链迅速形成。

第一批“养虾人”的翻车经历[2]也不断出现：

* 有人授权OpenClaw访问邮箱，结果邮件被批量删除；
* 有人让AI清理磁盘，结果整个目录被误删；
* 还有用户因为API Key泄露，一夜之间损失数万美元；

3月10日晚，国家互联网应急中心紧急发布风险提示[3]，提醒公众谨慎部署类似AI智能体系统。随后，工信部NVDB（国家信息安全漏洞库）也将OpenClaw列入重点关注名单，明确指出其可能引发网络攻击、数据泄露等重大风险[4]。

一只“龙虾”的命运，在一周之内完成了从全网追捧到紧急卸载的反转。在这场狂热背后，一个更深层的问题浮出水面：**当AI从“思考”走向“动手”，我们该如何确保它不会失控？**

**AI智能体的三大安全风险与应对**

与传统AI应用不同，AI智能体具有三个关键能力：访问真实系统资源、调用工具执行任务、自主规划行动步骤等。正是这些能力，让AI从“对话者”进化为“行动者”。但这也意味着，一旦出现安全漏洞，影响将不再局限于模型输出，而可能直接波及真实的系统环境与业务流程。

一只“龙虾”的冰火一周，实际上提前暴露了OpenClaw的三大安全风险，与风险对应的解决方案如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcwaxLynVL9PKq3RDnLWj66juYpGOCq8BjpnXKvD2EkTPz9tDCupgae6QicaJ4iaOJzAVoIcUYqcycfJ9MVooe9iapqOOoaQhnS8BI/640?wx_fmt=png)

图1 OpenClaw的三大安全风险和应对方案

***风险一：影子“龙虾”——隐匿的OpenClaw***

OpenClaw的爆火不仅激发了个人用户的尝鲜热潮，也在企业网络中悄然埋下了一类全新的安全隐患——影子AI资产（Shadow AI Assets）。为提升效率或便捷体验，许多员工在未经安全审批的情况下，自行在个人电脑、研发服务器甚至企业内网中部署OpenClaw等AI智能体系统。

从安全视角来看，这类影子AI资产普遍具备以下三大典型特征：

* **难以发现：**安全团队可能对内部署的AI智能体一无所知，这些系统可能散布于研发服务器、测试环境、云主机甚至员工个人设备上，形成管理盲区。传统资产发现手段难以识别AI智能体的特有指纹，“看不见”成为首要难题。
* **漏洞复杂：**AI智能体系统通常由模型框架、插件模块及ACP、MCP、API等多种接口组成，各组件间依赖关系复杂，组件供应链投毒、配置错误、权限绕过等风险交织叠加，使得漏洞面显著扩大。
* **权限过高：**为完成任务，OpenClaw等智能体常被授予访问系统文件、浏览器环境及API接口的高权限。一旦节点被攻击者控制，即可直接窃取敏感数据、执行高权限操作，甚至以此为跳板横向移动，深入渗透企业内网。

这些影子AI资产往往直接接入核心资源——本地文件系统、企业邮箱、API密钥、内网服务接口等。与传统影子IT相比，影子AI资产的权限更高、组件更复杂、隐匿性更强，已然成为企业网络安全的“暗礁”，亟待引起重视。

**应对一：雷达“扫虾”——AI资产测绘与风险识别**

针对影子AI资产带来的治理困境，绿盟提供AI资产与风险识别智能体，包括能力如下：

**1.AI资产自动发现：让隐匿的AI系统无处遁形**

通过网络空间测绘与AI资产指纹识别技术，自动发现网络中的能够自动发现隐藏或未纳入管理范围的AI资产。覆盖OpenClaw等智能体平台以及各类AI应用服务节点、模型服务接口和AI运行环境等多种形态的AI资产，形成动态更新的资产清单，彻底消除盲区。AI资产与风险识别智能体发现：截止2026年3月13日下午4点，全球已有13w个开放的OpenClaw在线资产，其中中国含有4w+个资产，占全球国家分布排行第一。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcwxXxtHaA1iasEBqicaZTzicuUicmAXZXYiboib1Rb4dpbFpz7REnJDY0fp8SreQ3k4sK80M7ARTicfXv8TthhPX6n1MIIGFqj7NCZjKY/640?wx_fmt=png)

图2 OpenClaw全球资产测绘情况

**2. AI资产组件漏洞深度识别：看见AI背后的真实攻击面**

通过对智能体关键组件进行漏洞关联分析，可以识别模型框架漏洞、插件风险和工具调用安全缺陷，并提供详细的漏洞说明与修复建议。例如 CVE-2026-27002、CVE-2026-28391、CVE-2026-28474 等漏洞，一旦被利用，攻击者不仅可以控制AI智能体本身，还可能继承其全部系统权限，从而访问AI能够调用的所有资源，包括：宿主机文件系统、容器集群、私有云存储平台（Nextcloud）。换句话说，一旦AI被攻陷，攻击者控制的就不只是一个模型，而是 AI背后的整个系统生态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcwqDV1Q1UliczCchV4pXwM3ytbib81xQAlkwmUvL8ukHuIguBjXJ2NBqibn8hE9gHbKvt31vCFo7Q1ywRbqdO3vCpvsnuZIGwXCsY/640?wx_fmt=png)

图3 OpenClaw漏洞情况

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhczvZN2b5mnwE9vtK6PPsCXjTUzEjDsYFYWp1Yj27quxQvtO3nMAVIAzhDaz4wQzgtP3eXPyhoXJExkvpfy8VTXmKa1AWq5ZDeU/640?wx_fmt=png)

图4 OpenClaw安全治理安全建议

**3. 风险画像构建与优先级排序：让高风险AI资产一目了然**

结合AI资产测绘与开源供应链分析，识别组件供应链暴露程度及关联漏洞信息等多维数据，为每个AI资产构建风险画像，定位高风险节点（如高危组件、漏洞利用链、外网暴露等），开展风险优先级排序，同时研判潜在的供应链风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcy3EHGh0P6uJmBczDPEUtKiaSZnbKIdu4c67XEHtSn4FxBFRBM51IqWoJG15VzNDm8hDYLKM2j806tjDG0CqtBOicvArDt8ME6FQ/640?wx_fmt=png)

图5 Openclaw供应链组织成分图谱分析

通过这些能力，企业能够将游离于管控之外的影子AI资产纳入统一安全管理体系，为AI技术的安全落地筑牢防线。

***风险二：有毒“龙虾”——被投毒的Skill生态***

OpenClaw的能力很大程度上来自其Skills插件生态。通过安装不同Skills，用户可以让AI智能体执行邮件管理、文件处理、自动脚本执行、代码开发辅助等自动化任务。这种插件化架构极大扩展了智能体的能力边界，但也打开了一扇危险的“后门”——一个全新的、隐蔽的攻击面正在形成。

根据安全研究，Skills相关的安全事件可归纳为以下主要类别：

* **恶意插件：**披着羊皮的“特洛伊木马”: 攻击者将恶意代码伪装成“邮件助手”等正常工具，诱导用户安装。一旦启用，智能体便在后台窃取数据、控制设备等。研究显示，ClawHub近4000个Skills中，36.8%存在安全问题，13.4%含严重漏洞，涉及恶意分发、数据泄露等[5]。
* **提示词注入攻击：**语言指令成为武器：除了恶意代码直接执行，攻击者还通过精心构造的自然语言指令，诱导AI智能体执行非预期操作。这类攻击利用AI对自然语言的理解缺陷，绕过安全限制。通过诱导性对话，让AI主动交出用户的社保号、银行卡信息[6]；OpenAI Codex一名成员的OpenClaw被恶意指令欺骗，转走了价值约45万美元的数字货币[7]；
* **供应链安全与系统性风险：**绿盟科技在《2026网络安全趋势报告》[8]中指出，智能体的自主决策特性放大了供应链风险。当用户从不可信来源安装Skill时，无异于主动把家门钥匙交给陌生人。此类风险涉及身份伪造、决策失控、数据泄露、模型漏洞等多个层面。

可见，Skills生态在赋予AI强大能力的同时，也带来了前所未有的安全挑战。用户需谨慎选择Skills来源，并持续关注安全动态。

**应对二：安检“验虾”——Skills全方位测评**

针对智能体Skills插件生态日益严峻的安全危机，绿盟构建了Skills安全测评智能体，可以对插件进行系统化安全检测。该测评智能体从三个核心维度展开，形成覆盖代码、行为、权限的全方位检测：

**1. 静态代码分析: 从源头识破恶意逻辑**

通过自动化扫描Skills源代码，识别可疑函数调用、外联通信逻辑以及数据外传行为。静态分析引擎内置了针对AI插件特有的恶意模式库（如权限边界突破与能力滥用、敏感数据暴露与外流风险、执行面失控风险等），可精准发现隐藏在正常功能代码中的“特洛伊木马”。该引擎对已知恶意模式的检出率可达90%以上。如下图所示，在测试的恶意Skills中识别到了一些恶意模式库中的风险，包含执行面失控、敏感数据暴露与外流风险等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhczMQOb4mgTRqzOpicUduibC75GJDbJwcWGEBwolPMc1sZj9MXROpWUiaKX1etXPI8icAibAwMZXnERbaPHkRLicgsn6knZ3r7tBNwztM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcwwmrejXh2JicCtrTnnQSKGqpNN7rbwSm33meW7kxHePKHhpMjcJf5Gwv9t05ke5qJl8p7udibFLKmdgGgSkVc7Vkl7gc4aIX8qw/640?wx_fmt=png)

图6 Skills文件内容静态分析

**2. 动态行为检测：在隔离环境中“抓现行”**

将插件放入沙箱隔离环境运行，实时监测其文件访问、网络通信、系统权限调用等行为。无论恶意代码如何混淆，只要它在运行时试图读取私钥文件、连接未知C2服务器、或执行异常外传，动态检测引擎都会记录并告警。结合Skill行为沙箱动态分析与静态审计交叉验证，这种“动静态结合”的方式，有效弥补了单一静态分析的盲区。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhczyibrLy3pDYibrrLJ9Yn32wOHDkzsicvGgG3eoibUnsBhqSOhsbRW6vgg4GO1zCegpQUeuQSxTJGnDVyqO6xLicqX7Ijm1VaXgiaxM0/640?wx_fmt=png)

图7 Skill静态行为交叉验证

**3. 权限最小化控制：让插件“各司其职”**

对插件能力进行分级管理和细粒度权限控制。通过定义明确的权限边界（如仅允许访问特定目录、禁止外联、限制API调用范围），即使插件存在未知漏洞或被植入恶意代码，其破坏能力也被限制在最小范围内。平台支持基于角色的权限分配，确保每个技能只能访问完成任务所必需的最小资源集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhczc0U3ECGuAqkh4icIMnibSj0d52KLm9IxvhcFcBBFWAbB7p4lEckkMdDlB4g8rRkHQaiaibicFoHdu1vR3t9yOVIXM6wibJmq5UzqNc/640?wx_fmt=png)

图8 Skill权限分析

Skills安全测评智能体正是将这种“开门揖盗”的风险降至最低——通过动静态结合的深度检测、权限最小化控制、以及持续的安全自检能力，帮助企业和个人用户在体验“龙虾”浪潮中，守住安全的底线。

***风险三：贪婪“龙虾”——恶意消耗Token算力***

OpenClaw还暴露出另一个被很多人忽视的问题：Token资源可能被恶意劫持与滥用。与传统对话式AI不同，AI智能体在执行复杂任务时，需要进行大量多轮推理、工具调用、自动代码生成和长上下文分析。这种能力在为用户带来便利的同时，也打开了一扇新的攻击窗口——攻击者可以通过精心构造的提示词，诱导AI执行高消耗任务，从而形成AI资源耗尽攻击（AI DoS）。学术界已将这类攻击命名为“Deadlock Attack”或“ThinkTrap”，具体风险有以下三类：

* **提示词诱导下的算力耗尽：**研究显示，攻击者仅需构造约20个Token的输入，即可诱导模型生成4096+ Token的超长输出，形成“非对称消耗”[9]。这种低速率攻击（如每分钟10次请求）可将服务吞吐量降至原容量的1%，响应延迟增加100倍，甚至引发服务崩溃[10]——极低成本即可瘫痪企业AI服务。
* **AI“自主钻空”引发的资源劫持：**令人警惕的是，AI可能主动突破安全边界。[11][12]
* **API密钥泄露下的算力盗用：**内部凭证泄露同样致命。深圳一程序员因API密钥被盗，3天损失1.2万元Token费用[13]。市场数据显示，OpenClaw占openrouter平台总消耗的95%以上（2.05T/周）[14]，而多智能体系统消耗是普通对话的4-15倍——如此庞大的算力池，已成攻击者的“金矿”。

这些案例表明，Token失控已从成本问题演变为安全问题。一旦缺乏监测与限制，AI算力随时可能被劫持，而受害者往往在收到账单或服务崩溃时方才察觉。

**应对三：阀门“控虾”——Token监测与资源控制**

面对Token算力攻击带来的资源失控风险，绿盟构建了Token行为监测与资源控制智能体，从“监测—识别—控制”三个维度形成闭环防护，帮助企业将AI算力消耗纳入可管可控的轨道。

**1. Token消耗监测:让每一分钱都有迹可循**

智能体实时统计模型的调用频率与Token使用量。无论是正常业务增长，还是突发异常暴涨，运营团队都能第一时间感知。这相当于为AI系统安装了“智能水表”——用水量清晰可见，漏水才能及时止损。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcz5HRtkHuLw1XMXaSxp7zdPsbjia8jTriaSo7dxWaBrayvvFmbrSt7uVbdyibD1o6z7QsMtvP9S3mDzHJS6XicXWTO4J8HOibdokl0Y/640?wx_fmt=png)

图9 LLM Token消耗实时监控

**2. 异常行为识别：捕捉失控前的“蛛丝马迹”**

智能体持续分析Token消耗模式，自动识别异常行为特征：Token消耗在短时间内陡增，远超正常波动范围；模型调用出现高频循环，疑似陷入死循环或遭受攻击；任务执行时长显著超出历史基线等。一旦发现上述模式，系统立即触发告警，并提供详细的调用链路回溯，帮助安全团队快速定位问题源头——是被恶意提示词注入，还是智能体自身逻辑出现偏差。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcweBChhzHImKgXMaiaPZUQKKmP7NibwINnPDndrXMIhTOycL1JibB0EFAon8AkpsPGqdzmEP4fS8MjMKnAQlibcqZe9pFuE3Hw42rw/640?wx_fmt=png)

图10 Agent资产管理与行为监控

**3. 资源限额控制：给AI算力套上“缰绳”**

通过精细化的资源管控策略，平台从源头遏制算力滥用：

* **Token预算：**为不同任务、不同用户设定Token消耗上限，超限自动熔断；
* **调用频率限制：**限制单个会话或API Key的单位时间请求次数，防止高频滥用；
* **任务时长控制：**设定任务执行超时阈值，避免智能体陷入无限循环；

这些控制策略既可全局生效，也可按业务场景灵活配置，确保AI系统在高效运转的同时，不会因资源失控而沦为攻击者的“算力肉鸡”或企业的“账单炸弹”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcx3MVhJsu7sZ9EUgOZrOvDQZhZIHEYLluks1q7HF96JictxiaiatPIleJwdMvicd9PxicGlnjWBDRvcZlQ2aC9NNGCpa1OktyE1Oyr0/640?wx_fmt=png)

图11 周期性Token消耗统计

通过Token行为监测与资源控制，绿盟希望帮助企业从“被动承受Token账单”转向“主动掌控AI算力”，让每一次模型调用都清晰可见、可控可管。

**关于绿盟“清风卫”**

AI安全一体机（“清风卫”），是软硬一体的“全能卫士”，集成了内容安全过滤、敏感数据防泄漏、精细化算力调度及应用层攻击防护等核心能力。通过自研“风云卫”混合模型和三级资源管控机制，有效防御提示词注入、模型越狱等高级攻击，同时保障资源高效利用，防止模型滥用。

绿盟“清风卫”AI安全产品体系具备“平台化集成、场景化适配、自动化运营”三大特点，可灵活对接各类智能体开发平台与既有安全基础设施，为客户提供从开发态到运行态的一体化“监管控”能力。

![](https://mmbiz.qpic.cn/mmbiz_gif/ZPtdzESiawhdMHyNfDvj0a36SiaN499NjK0BKean9ibV1T8rYe...