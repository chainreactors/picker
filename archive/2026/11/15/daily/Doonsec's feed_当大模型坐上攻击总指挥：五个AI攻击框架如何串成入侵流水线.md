---
title: 当大模型坐上攻击总指挥：五个AI攻击框架如何串成入侵流水线
url: https://mp.weixin.qq.com/s/0y1A9S__1c-WJb5HCYwR-A
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:46:12.187677
---

# 当大模型坐上攻击总指挥：五个AI攻击框架如何串成入侵流水线

# 当大模型坐上攻击总指挥：五个AI攻击框架如何串成入侵流水线

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](https://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

过去印象里的入侵，总得有个操作员坐在电脑前，一行一行敲命令，在CobaltStrike里点来点去，就像短剧里演的黑客入侵那样。如今这套打法已经完全变了。短短一个月，基于AI的攻击框架开始频繁出现在真实入侵现场，并且已经从试验性使用，发展成有人长期维护、持续运行、多目标并行的黑产生意。

最早被系统拆解的五个框架分别是ARTEX、CyberStrikeAI、Cairn、PentAGI和HexStrike，一个脚本或一个Compose文件即可完成部署，在GitHub上合计获得超过六万颗星。

所谓agentic offensive framework（智能体攻击框架），可以理解为把一个大语言模型（LLM）放到总指挥的位置上，由它调度扫描器、curl、shell和云命令行工具。工具还是红队和攻击者用了十几年的老工具，不同之处在于：下一步做什么由模型规划，任务被拆给多个agent执行，缺少工具时模型会自行安装。

研究人员分析了五个框架的源码和公开事件报告，只想搞清一件事：这些框架运行起来后，到底有哪些动作会落到防守方的遥测（telemetry）里。结论是，它们没有一个在代码层面强制授权，而它们执行的每一个动作，最终都会在防守方本就在采集的日志中留下痕迹。

# 它们和传统C2框架到底差在哪

Cobalt Strike和Brute Ratel C4的背后是人：操作员盯着植入体（implant），决定下一步执行什么。

agentic框架保留了全部工具，只是把操作员人工思考的环节换成了自动规划循环。GTIG观测到ARTEX单次执行爆发窗口约2到25秒；NorForge跟踪了一批被其判定为恶意、暴露在公网的Cairn面板，发现某个攻击者团伙从开工到拿下目标平均不到23小时。单次爆发窗口很短，短到可能从检测窗口中溜走，但整个行动可以持续数小时，因此要把一连串爆发关联回同一次行动，回看窗口必须拉得足够长。

这些agent和绝大多数工具通常运行在攻击者自己控制的机器上，调用的是托管或自建的模型。真正落到防守方环境里的，是这些工具造成的实际动作：在主机上表现为新进程，在云审计日志里表现为API调用，在身份系统里表现为登录行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqNBHMeAGIx29g01DTwQsrvODeicC3SGxcsDzIQh2DgYh1WuqRFg7203MTvic1c8ZM5r8eWezwlHZLu9nXA9s05aiac90ed7OsEf4/640?wx_fmt=png)

图1 一个agent循环中真正传导到防守方一侧的内容：进程、云API调用和登录

五个框架共享同一个规划循环，但模型运行在哪里、每个工具由谁拉起，实现方式各不相同。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqI6aUFdibZdHcxpVAt9PIRJEcCsnFAVNeGZbYUHlhK7JwAz88F7OZ7gGH0V8dgk7IUorNABBRjWoAjrDf13Ng04A7oKfUXT4V4/640?wx_fmt=png)

图2 同一个扫描器（如nmap）在五个框架中分别由谁拉起，模型调用发生在哪一层

自主性是默认状态。CyberStrikeAI出厂即关闭审批模式；PentAGI的Compose文件中写死ASK\_USER为false；Cairn的三种编码agent工人里，有两种在启动时就关闭了审批提示；ARTEX则直接让agent运行在bypass权限模式下。也就是说，这四个框架没有一个默认等待人工确认。

在共同循环之外，每个框架都有一个辨识度很高的设计取向。

ARTEX采用事件驱动规划器配合并行工人，人只在一个聊天agent里围观进度、偶尔给出提示。它捆绑的浏览器扩展会记录操作员已登录的会话，验证码和一次性口令只需人工解一次，后续相关请求就直接交给agent继续。研究人员分析的是原仓库公开的英文翻译版。

CyberStrikeAI是一套完整的操作员控制台，可自行生成植入体、运行C2监听、管理WebShell，还能接入Telegram、Slack、Discord和钉钉等聊天平台。

Cairn把任务外包给现成的编码agent，其工人就是运行在Kali容器中的命令行工具；README中注明，它首次亮相于一场AI渗透测试比赛。

PentAGI依靠一个reflector agent（反思agent）推动队伍持续前进：哪个agent卡住不动，或者不执行动作反而开始空转输出，reflector就以用户口吻回复一句，这段对话还会被记为一条人类消息。

HexStrike自身不带模型，它通过模型上下文协议（MCP）把大约150个工具函数暴露出来，可接入操作员原本就在使用的任何AI助手。

五个框架出厂自带的组件也不一样。CyberStrikeAI可自行生成植入体；五个框架中有三个捆绑了云工具，云账号能触及的范围与一台主机相当。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqDS84O9U3oA3qIBTibD8EANnnOBiay3D0PQIFYeMZvEzwYr5NC0Jkbnl6tBnSEgpTibTjCImvOeSfXjDqwBOhfwc2QaLSHP7GR8o/640?wx_fmt=png)

图3 五个框架的设计与出厂防护：人工审批默认全部关闭，授权只在prompt里口头声明，目标限制仅剩.gov和.edu黑名单

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrZWqia3sqbx3VF1AFfVgdyJJs9IBcq0lIrc7toLs4YMaB9880JLaNFwSu6ptscwATEvuUxczibAupwps3iavTPLguHdTIAtfibDiaA/640?wx_fmt=png)

图4 五个框架在一次入侵中携带的组件：C2、shell处理、云工具、浏览器、运行时写入工具、跨任务记忆和控制台暴露面

和传统攻击工具一样，五个框架没有一个在代码层面默认强制授权。其中三个走得更远，直接在提示里告诉模型“你已经获得授权”。

CyberStrikeAI告知模型授权早已谈妥，不要质疑也不要等待审批；PentAGI的九个角色提示词开头都塞入一段预授权声明；ARTEX则把每个agent都描述成已授权渗透测试系统的一部分。

Cairn要求工人永远不得拒绝任务。万一模型真的拒绝执行，其调度器（dispatcher）会让这个工人暂停5秒，把任务交给另一个已配置的工人；如果只有这一个工人，则对其重试。

默认真正生效的目标限制，只剩ARTEX和CyberStrikeAI对政府域名（.gov）的黑名单，以及ARTEX对教育域名（.edu）的黑名单。除此之外，出厂自带的防护范围非常有限。

ARTEX拦截了rm -rf、mkfs这类破坏性命令，也可以依据操作员自行编写的允许清单（allow list）核对任务资产；问题在于该清单默认为空，一条shell命令仍可打到任意主机。

ARTEX原有的交战规则（ROE）范围机制已被删除；其源码注释写明，工人记录下来的资产会被自动加入任务范围。

HexStrike支持配置范围外清单（out-of-scope list），但从不实际校验它。

出厂状态下，五个框架默认优先追求的是能力、自主性和速度。

扫描器全部使用默认配置，好几个默认值直接暴露了框架名；CyberStrikeAI的植入体每5秒回连一次，连jitter（抖动）都没有。隐蔽性被做成技能（skill）由模型自行加载，CyberStrikeAI那套行动安全技能覆盖了限速应对、封禁IP绕过和反取证。

真正的变化出现在ARTEX或CyberStrikeAI被拦截之后。

ARTEX告知工人，被过滤的payload或一个404响应，并不代表该意图就此终止。此前UNC7228攻击活动中，该团伙的初始基础设施被封禁后，转而使用开放代理（open proxy）。

CyberStrikeAI的技能教agent：遇到拦截就更换代理、User-Agent和转发头，先退回到目标国家境内的免费代理，最后退到Tor。

因此被封禁之后，需要预期同样的请求会换上新地址、新User-Agent再次返回。

这意味着基于请求内容的检测，比基于来源地址的检测更持久有效。单纯封禁来源地址无法剥夺框架的访问权，必须配合吊销其正在使用的凭证。

# 为什么靠IOC的检测会很快过期

agentic攻击框架迭代极快。ARTEX在2026年7月26日至10月7日这十周半内，提交（commit）约390次，算上合并超过450次；其创建者在10月撤下原仓库后，公开fork仍在持续传播。

CyberStrikeAI第一年就提交超过2400次，好几个框架还会在任务执行到一半时临时编写、安装新工具。今天还能识别某个框架的字符串、文件名和默认值，下个版本可能就不复存在；但它所依赖的行为，比如凭证访问、远程执行、由服务拉起攻击工具，并不会改变。因此，锚定行为的检测规则，失效速度远慢于锚定框架指纹的检测。

# 吊销凭证为什么不能立刻停住它

AWS和Google都在文档中写明了访问变更的传播延迟。在Entra ID中，用户或服务主体被删除或停用之前已签发的访问令牌，在过期前通常一直有效，一般为60到90分钟，除非资源和客户端支持持续访问评估（continuous access evaluation，CAE）；微软对Exchange、Teams、SharePoint提供了支持，服务主体侧仅支持Microsoft Graph。也就是说，即使确认执行了吊销，下一个请求也未必拦得住，而以机器速度运转的agent恰好能钻进这个空档。AWS的角色会话吊销既不覆盖IAM用户的长期密钥，也不阻断截止点之后新申请的会话，因此还需要配套删除所有仍能假扮该角色的凭证。

# 五个框架各自留下的指纹

以下这些默认值会出现在被攻击的系统上，其中标注的特征还可能出现在己方监控的主机上，现在不妨先到日志里排查一遍；当然，下个版本这些特征就可能发生变化。

|  |  |
| --- | --- |
| 框架 | 特征 |
| ARTEX | 捆绑的扫描器流量，如nuclei、httpx、katana、ffuf和sqlmap，默认每个任务三个并行工人；User-Agent带artex-enrich/1.0或norma/0.4；应用被注册新账号，随后从多个会话登录，因为其agent会自行注册并共享测试账号。 |
| CyberStrikeAI | User-Agent为Mozilla/5.0 (compatible; CyberStrikeAI-WebShell/1.0)、且表单中含pass字段的WebShell请求；Web服务器进程执行echo :OSPROBE\_%OS%:END；名为SystemUpdate的持久化项（计划任务或Run键），或com.apple.systemupdate（LaunchAgent）；.bashrc中以cs结尾的一行；或一条自身不带任何标记、却拉起植入体二进制的@reboot cron条目。<o:page></o:page> |
| Cairn | 反弹shell，以及连回操作员主机自身地址的带外（out-of-band）回调，因为其示例配置把工人容器运行在主机网络上。若它运行在己方监控的主机上，三种工人适配器中有两种在启动编码agent命令行工具时关闭了审批提示，完整任务提示词会直接写在命令行中。 |
| PentAGI | 被攻陷主机连向PentAGI主机TCP 28000到29999端口的连接（每次行动默认两个）；浏览的每个页面会被同时请求两次，一次取内容，一次截图。部署在内网的实例还会每3小时向update.pentagi.com汇报一次。 |
| HexStrike | User-Agent为HexStrike-HTTP-Framework/1.0和HexStrike-BrowserAgent/1.0；浏览器agent执行主动测试时，携带跨站脚本标记<hexstrikexsstest123>。若它运行在己方监控的主机上，默认会有一个Python服务器在所有网卡的8888端口监听，通过shell拉起安全工具，因此某个安全工具的父进程会显示为这个Python服务器。</hexstrikexsstest123> |

除了这些默认值，扫描器全是出厂配置在跑，所以在网络层面，这些框架看起来基本就是它们驾驶的那些工具本身。

# 亚马逊蜜罐里看到的两场AI攻击活动

2026年10月3日至11月5日，亚马逊全球分布的诱饵传感器网络MadPot，在伪装成热门大语言模型推理API的端口上，截获了一批AI agent发来的请求。这批请求最反常的地方在于，它们把agent自身的作案记忆也一并发送了过来。由于agentic框架会保留完整的历史对话，单个请求中经常携带整场战役的任务上下文、系统提示词、工具调用记录、知识图谱状态和已上报的发现。亚马逊威胁情报据此判断，至少有两个目标明确的黑产行动正在运行，且以ARTEX为骨架。

任务按固定国家顺序推进，企业生产站点优先于个人项目；每一把窃取到的凭证都要分级，公开暴露超过30天的凭证直接归为低价值库存。

第一场战役是大规模窃取AI凭证，目的是免费调用模型。窃取到的密钥会被送入框架自身的模型网关，用他人付费的额度驱动agent去搜索更多密钥，形成自给自足的循环。云凭证也被视为获取更多访问权的入口：agent逐个排查各家的令牌和身份服务，枚举存储、评估权限范围，重点针对托管模型服务、密钥与参数仓库、应用身份，优先级是高端前沿模型，而非泛泛的云权限。

它们锁定的目标很具体：先是聚合各家上游密钥的AI网关和代理平台，One API、New API、Veloera、Sub2API、LiteLLM，再是Dify、FastGPT、Langflow、RAGFlow、Open WebUI、LobeChat、Ollama这类AI应用搭建平台。它们手中有一份编码好的漏洞手册，每个指纹识别出的产品对应一条已知攻击链，包括尚未初始化即可被认领的安装实例、匿名可访问的管理端和供应商配置接口、默认管理员口令（如LiteLLM的默认master key）、Langflow的CVE-2025-3248、RAGFlow的CVE-2026-28797、One API系列中靠isCliRequest请求头绕过认证的手法、借URL抓取功能打到云元数据服务的SSRF，以及藏在前端JavaScript、source map、调试路由和环境文件中的密钥。寻找密钥的渠道也铺得很广：互联网扫描、证书透明度、GitHub仓库和事件归档（专门关注已过自动撤销期的泄漏）、npm和PyPI打包文件、容器镜像层、notebook、模型托管空间、paste站点和Telegram频道。每把凭证分为三级：L1是线索，L2是确认能调通一次API，L3是量化出的影响，比如能够读取数据或账户内有可消费的额度。

第二场战役离普通用户更近：两家加密货币交易所的KYC（了解你的客户）人脸核验，被agent用实时深伪（deepfake）技术绕过。agent先把一家厂商的活体检测协议逆向分析得非常透彻，记录下其发送的人脸检测事件流、检测过程中如何追踪人脸位置、用什么坐标系提示用户移动脸部；最好的一次记录里，整套动作走完后人脸落点与目标位置只差7个像素，但厂商服务端每次都拒绝了这次深伪。

另开一条会话，在一块消费级GPU上用开源人脸动画模型搭建了一条实时深伪视频流水线；通过拆分模型、避免GPU上多余的内存拷贝，跑到每秒11.5帧，接近活体检测对实时视频的要求。证件照方面，它们伪造相机元数据，让图片尺寸与JPEG文件中的真实值一致，并保留原始相机的压缩表，这样一张被修改过的图片，在文件层面看起来就像相机直出、未经重存的照片。

整场战役至少有四条agent线并行：一条寻找洗钱渠道，一条清空账户余额，一条搭建深伪视频流水线，一条专攻核验绕过，彼此跨会话交接任务。

# 三天冒出五十个家族，请求量涨了三十倍

Cloudflare的Cloudforce One团队给出了最直观的规模感知。就在几周前，这类框架里还只有ARTEX一个值得关注，结果短短三天内，他们就观察到五十多个框架家族在全球扫描Cloudflare客户，运行这些框架的IP已数以千计，且每天仍在增加。

2026年10月8日，作者撤下ARTEX原仓库，并写道，这种工具被恶意利用完全违背其初衷。但下架反而触发了九头蛇效应（hydra effect）：原仓库一消失，分叉和改版呈爆炸式增多，目前GitHub上相关仓库超过12000个，其中几百个是带有原仓库血脉的独立分叉，10月8日之后新出现的同类agentic编排框架还有几百个。AI渗透测试和利用工具的日请求量自10月1日以来上涨30倍，自下架以来流量又翻了十倍以上。截至11月12日，ARTEX及其分叉占已知同类编排器的六成以上。

Cloudflare正在跟踪的五十多个agent中，最主流的五个全部完全自主、GitHub星标均过千：ARTEX及其分叉、LuaN1aoAgent、Decepticon、Cairn和PentestGPT-Agent。Cloudflare将其称为一次作战思路的转变：OODA循环（观察、判断、决策、行动）的每一步都由harness（作业框架）自行跑完，人的技能不再是上限；多个并行agent朝同一目标推进，速度和规模与单操作员或人加AI辅助完全不在一个量级；一名操作员可以同时攻击多家机构，爆炸半径被显著拉大；自主框架会持续、系统性地测试每一个暴露的服务和配置，再小的失误也会被翻出来。用他们的话说，入侵被变成了一个可以逐步爬坡求解的问题，而这恰恰是agent最擅长的事。

更值得防守方警惕的是凭证串联。Cloudforce One在过去八周被多次请入应急响应，反复看到同一套剧本：攻击者获得某个hyperscaler（超大规模云厂商）环境的初始访问后，直接pivot（横向移动）到客户的Cloudflare环境；根因分析均指向凭证卫生问题，反复中招的是CI/CD流水线中那些静态、不过期、无IP...