---
title: AI优先时代生存法则：四个问题筛出真正有生命力的网络安全产品
url: https://mp.weixin.qq.com/s/xIybLVsZMRWWnx44PkTw-Q
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:56:07.131116
---

# AI优先时代生存法则：四个问题筛出真正有生命力的网络安全产品

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcW4xcRKaQ6p0UNyZItpSPGzcW9zIE7RT6bVFY0gs0IZlFfceapicmoBW7Bp0icn5Azia82rTfqAWSe7bMIGPwrXBkNT4cRzKrcBQ/0?wx_fmt=jpeg)

# AI优先时代生存法则：四个问题筛出真正有生命力的网络安全产品

管窥蠡测
管窥蠡测

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

2026年，生成式AI与智能体的落地速度超出了多数从业者预期。从研发到客服，从运维到业务决策，AI正在接管越来越多原本由人类完成的工作，网络安全领域也不例外。安全团队的编制很难随威胁增长同步扩张，而攻击者已经大规模用AI生成钓鱼邮件、编写恶意代码、自动化漏洞利用，防守方不用同级别的技术，根本跟不上对手节奏。

但AI带来的不只是能力升级，还有整个行业格局的重构：有的安全产品会在这波浪潮里被彻底替代，有的能勉强维持生存，还有的反而会因为AI的普及迎来需求爆发。在这样的节点上，美国网络安全领域资深撰写者Ross Haleliuk提出的一套判断框架，为我们分辨安全产品的长期生命力提供了清晰的参考。在他看来，不需要复杂的行业调研，只需要四个本质性的问题，就能覆盖80%以上安全赛道的生存判断。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpcaSCdqnxDYt2bOtnXJfIaA5KYphamNedb8zOGWq0an5R6Pw0GptI232W2xicibUHgJmTrsHkFsrhZ8dbSWK9CVlhCwZQ18hkrmg/640?wx_fmt=png&from=appmsg)

**0****1**

**是否属于在线接入与安全执行类产品？**

Ross表示，如果答案是肯定的，那这个品类基本不会被AI颠覆，反而大概率会因为AI的普及变得更加强势。

很多人对安全产品的认知停留在“分析、告警、给建议”的层面，但在线执行类产品完全不同：它们不是站在流量、访问请求、工作负载、身份验证或者交易链路的旁边做旁观者，而是直接嵌在路径中间，主动做出允许、阻断、限流、降级之类的决策。我们熟悉的Web应用防火墙（WAF）、身份与访问管理平台（IAM）、安全访问服务边缘（SASE）、网络防火墙，都属于这个范畴。

他特别澄清，这并不意味着AI会降低这类产品的构建门槛。在线安全产品的商业化落地向来不易，客户需要调整架构、重规划路由、重构访问模型，还要承担变更带来的业务风险，过去很多创业公司都没能跨过规模化落地的坎，AI也不会改变这一点，真正变化的是市场需求。

AI智能体的普及正在给这类执行类产品创造全新增量需求。行业正在重新认识代理、网关、策略执行点的价值：企业部署AI代理时，都会关心三个问题：AI能访问哪些敏感数据？能连接哪些内部系统？被允许自主执行哪些操作？回答这些问题最直接的方式，就是在AI代理和内部资源之间设置管控节点。

当下行业趋势已经十分清晰：主流云厂商纷纷升级SASE产品新增AI代理管控模块，IAM厂商推出AI身份治理功能，不少企业也开始部署专门的AI安全网关，统一管控大模型与智能体的流量。Ross认为，随着越来越多企业部署能自主访问数据、调用应用、执行操作的AI代理，安全执行层的重要性会比AI时代到来之前更高。这类产品不仅不会在AI转型中消失，反而会是少数最能从AI普及中获益的安全品类。

**0****2**

**是否依赖运行时数据或运行时数据分析？**

Ross指出，很多安全产品的价值基础正在因大模型普及快速瓦解。那些基于静态信息的工具——分析告警、整理漏洞库、检查云配置、汇总威胁情报的产品——依赖的信息现在都能被大模型轻松处理，且模型能力提升后，处理准确度还会越来越高。如果产品的全部价值就是“整理公开静态信息成报告”，被AI替代只是时间问题。

但运行时数据完全是另一种逻辑。EDR、NDR、浏览器安全、ADR、身份监测这类工具，掌握着企业独有的实时遥测数据，这类数据难以复制。它们的价值不止是数据分析能力，更是“拿到数据”本身：构建稳定低侵入的全量数据采集体系，需要极高的技术门槛和客户信任，不是调用大模型API就能做到的。

这也是为什么他判断EDR、浏览器安全、ADR这类品类会长期存在：大模型确实能让分析层能力大幅提升，比如串联告警成攻击链、给分析师提供调查建议、自动生成处置脚本，但前提是得有人把这些分散在各个节点的运行时数据采集上来，而且在把高优先级事件交给大模型做深度分析之前，还得有轻量本地规则引擎做初筛——如果所有原始数据都直接传给大模型，不管是成本还是延迟都没有企业能承受。前两年一批主打“纯LLM驱动EDR”的创业公司，就因成本和延迟问题无法落地，要么转型做辅助工具，要么被成熟厂商收购。

Ross特别强调，和在线执行类产品类似，AI其实在放大运行时数据的价值。当通用的情报分析能力变成人人都能调用的基础能力，独有的运行时遥测数据会成为网络安全行业最持久的壁垒之一。这也是为什么端点安全赛道的头部厂商在AI时代反而优势越来越明显：构建一个稳定、兼容全平台、不影响业务性能的端点代理，需要多年的技术积累，后来者很难在短时间内追上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfUKSib7Wel18L5RdckicEd9ljWMFIWHYriasKZpjEjoepWiaYk7GiayY9ZbDJht2KqGruyFdMMVFIB0CIXDoQI83BHto3WMhkFqVias/640?wx_fmt=png&from=appmsg)

除了数据壁垒，运行时分析的实时性要求也是大模型难以跨过的门槛。大模型擅长“慢思考”：深度分析异常事件、溯源安全事件、拼凑攻击全貌这类工作交给它再合适不过，但实时检测场景对延迟要求是毫秒级的——比如勒索软件开始加密文件时，必须在几十毫秒内阻断，根本等不及大模型几百毫秒甚至几秒的推理。他直言，网络安全的很大一部分价值就是实时的检测和响应，从这个角度看，绝大多数安全产品根本不像很多人宣传的那样会被AI彻底淘汰。

**0****3**

**是否需要构建复杂系统的精准模型？**

Ross认为，AI的推理能力再强，也没法凭空理解它看不见的复杂环境。大模型的推理质量完全取决于它拿到的上下文，如果没有对企业环境的精准建模，它就只能靠假设做判断，而在安全领域，假设往往就是误报和漏报的来源。

安全工作本质是和边缘场景打交道：攻击者永远会钻管控缝隙，一个权限漏洞、一处信任盲区都可能成为突破口。这要求安全产品对企业环境有完整准确的认知：身份安全要理清用户、权限、应用和业务关系，云安全要掌握账号、工作负载、网络、数据的全貌。大模型推理能力再强，输入的环境信息有误，输出的判断就不可能准确。

这些环境模型没法靠大模型自动生成，必须有人持续构建更新，跟上环境变化。大模型可以随用随生成情报，但环境模型必须和现实完全一致，是确定性的——权限关系、资产归属没有模糊空间。这也是为什么环境模型类产品在AI时代价值越来越高：它们是给大模型提供准确上下文的基础，没有这个基础，再强的大模型也无法输出有效判断。

他举了两个例子：身份治理厂商Veza能拿到不错的退出结果，主要原因是它构建了完整的身份-数据-应用关系图谱，能统一呈现企业零散的权限关系；CSPM产品在多云混合云时代依然不可替代，是因为它们能持续扫描更新云环境模型，理清上万资产的依赖关系，不会因环境变化出现信息断层。不少企业尝试用通用大模型做云配置检查，最后因误报率过高无法使用，本质就是通用大模型没有企业环境的精准模型，判断基于通用规则，适配不了复杂的企业实际。

他还给出了实用的判断经验：如果一个AI只靠一张截图、几段文字描述就能给出足够准确的答案，那这个产品品类离消失就不远了；但如果AI必须先拿到一张包含成千上万资产、身份、策略、依赖关系的完整环境地图，才能给出有用的判断，那这个品类的生命力会比看起来强得多。

**0****4**

**问题能否通过单个代码拉取请求（PR）修复？**

Ross判断产品生命力的最后一个问题，落在问题修复的环节：如果一个安全问题被发现之后，只需要改几行代码、提交一个PR就能完成修复，那这个品类的产品价值会被AI大幅压缩。

大模型的代码能力已经有目共睹。如果安全问题能在开发流程内完成修复——比如SQL注入、开源组件漏洞、基础配置错误——AI现在已经能自动检测、生成修复代码、跑测试验证，不需要额外安全产品介入。这也是为什么很多AppSec产品面临生存挑战：过去开发完需要用SAST扫漏洞、安全审核再修复，现在AI代码助手写代码时就能实时发现并修复漏洞，开发人员顺手就能处理，不需要事后单独扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpcoUX7db4GmmHsvBauxicspiaiaq8dShuFxUw8zibPJjoaMvNvzYRRv4JgsgcrLbjOvkD5bTVBDRYKBGaRqKO0snYciaYq1lRZr10Ho/640?wx_fmt=png&from=appmsg)

而那些更有长期价值的品类，解决的都是没法靠单个PR修复的问题。这些问题往往不在代码层面，而是存在于基础设施即代码配置之外、存在于纯云环境之外，涉及多个团队的协作、业务层面的权衡、复杂的变更管理流程，甚至直接和敏感生产系统的稳定运行绑定。比如跨部门权限过度分配问题，没法靠改一行代码收回权限，得先和业务部门确认权限必要性；比如工业控制系统漏洞，不能随便打补丁，得先验证兼容性、安排停机窗口、协调多团队配合；比如零信任架构落地，更不是改几行代码能完成的，涉及IT架构调整、员工习惯改变和业务流程适配。

Ross认为，现在反而是去啃这些“硬骨头”问题的好时机：过去很多安全创业者喜欢做容易落地的轻量产品，比如代码扫描、配置检查，但这些产品正在被AI快速替代；而那些需要深入理解企业复杂系统运作逻辑、能在不影响业务的前提下帮企业解决深层次安全问题的产品，不仅不会被AI替代，反而会因为AI把浅层问题都解决了，凸显出更大的价值。

值得注意的是，很多人讨论AI对安全产品的替代时，忽略了AI本身也在创造新安全需求，而这些需求对应的产品恰好符合前面四个判断标准。AI给防守方提供新工具的同时，也打开了新攻击面：提示注入、越狱能绕过限制让代理执行恶意操作，训练数据投毒能让大模型输出带后门的结果，AI生成的钓鱼邮件、恶意代码攻击效率大幅提升。这些问题没法靠通用大模型解决：管控AI代理需要在线网关，检测大模型攻击需要交互运行时数据，梳理代理权限需要专属环境模型，修复问题涉及架构调整和流程规范，不是改几行代码能完成的。AI在淘汰旧产品的同时，也给符合价值规律的新产品创造了空间。

**0****5**

**结语**

在Ross看来，AI从来不是网络安全行业的终结者，而是一个严格的筛选器。它会淘汰掉所有只做浅层信息整理、没有实质壁垒、解决表面问题的安全产品，把这些产品的价值变成人人都能调用的基础能力；但那些扎根在执行链路、掌握独有运行时数据、能构建复杂系统模型、解决深层次业务与架构问题的产品，不仅不会被淘汰，反而会因为AI的赋能变得更高效、更有价值。

对于安全行业从业者来说，不必被“AI替代一切”的焦虑裹挟。与其忙着给产品套AI外壳蹭热点，不如对照这几个问题重新审视方向：你的产品是否站在不可替代的价值节点上？是否把AI当成能力放大器而非全部价值？想清楚这些，自然能在AI浪潮中找到位置，构建出能穿越周期的安全能力。

**安在企业（用户）会员服务**

**助力全生命周期安全意识提升**

“安在企业（用户）会员服务”，为所有企业提供一站式的网络安全支援服务，包括意识宣传、培训教育、效果检验、专业圈子、知识社区、专业培训、参选评奖等多个板块，助力网安从业者高效履职，实现个人与企业安全能力同步升级。

**[小投入大防护！安在推出企业（用户）会员服务](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)，点击标题阅读详情。**

深度贴合企业不同规模、安全水平投入以及员工安全意识的不同发展阶段，特设5级安全意识培训服务体系，为企业用户量身匹配适配的安全意识解决方案。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfxauQUKv5E2gfFrpMBAz1Um7FAY4ontydFQQ1ZKtH1AnXs3kfYxtOYX55xrRBM2pFYicz2sqACyjd4u1CO2iaAFCYLIbgMGS58M/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpevFQuuGbgqzRQXxpZt2NQG9gkeSfhrKIBL6NVagjD9IYhtko4pjEdkrmiaAFfGAYPQN06Cs2MSLG4HGqExqL1OJ9n0ZSmibwO9Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

本文展示所有类型素材，均包含在企业（用户）会员服务中，如有意向，欢迎垂询。

**加入诸子云知识星球**

获取更多“安全意识资料”和“网络安全报告”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpevtB5U1iad3jHVWSBznd4wGSnt15KjDpDvdDAzWfLewNRoKHVyCNTCEIVkuJAZOyUvKSibQZJfe43xQsofxEKuB4xuj2gzBG4EM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfphwUVRfsnQ4tHXQicImFKOyric81wyOR6UtibaU9W2nPpF2bIflBltg8S0vJMmYEDrEkWN30lpxicg5YUyLDu0fAlCgX3ibJBX8Ys/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcHLAPdhJaKhut2fLyfnDD0ofblclhTxwQtdjZ9Wnsgw7qtANaolbmpYLhf9mCW9ib2vDial19qZnEibibEZkAcOVPZVTA9QsD5EeY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcaBf7luDbkibnkcG6SFanyicuIePMSYCXyZ4dpRTDOuRkj4IwafHmia3a61q1QmasWkERH6vhD4eicgePFZCERRib6zAefEHxWz3cY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcoibvzpu3KUfibMYf9yTU7VWPXP10LBBkle2fQKqqdVk7zLYiaoh0bHWxmovw4aqY0icMXYfqY2TW0LibL3W2NVG5u6ibA9aDyzsF8I/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpfHuRbxczmKK36HLRfSVxysIgBAQMVFSdVGCDascdwN2jmE6LickWQ9nyK1k0fVcibLIYwaseCvT2VtXEoVubWyMLdmf9jRo59JY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpd5O3toB6xb2AkuS2RcTBYTLu0nY8LibtS5iaZCyjdwbYYvsFA52ib67sdZdjG5Irwcs962K5KttO7qbKW4eEBYNtKkJUKBfHGI0s/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpd8PSnWIlP6x8ytDuhBpQc307z6BWzOD6flZLjlIYYXXU1NKpN5gXPjeq2mAPqgJm6Bd82h2IOL1rNSU0REl8Z7LOmpoU1NjS4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcGyRCee3d61E6ibYFh5VeHPicnicIloE3Iia6Bvud9Ok8cJOYYu0s4aIIXNltmfiagic87u2yvKdIDY6Px4iaaFwOh1h0B17rs0nibSlo/640?wx_fmt=jpeg&from=appmsg)

**<**

**滑动查看下一张图片**

**>**

******END****

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaFibHCDibF1vCIjn2tNAKdNicq3Y45vuYuWNUDICSF8dZ206dy1Kzrehug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy...