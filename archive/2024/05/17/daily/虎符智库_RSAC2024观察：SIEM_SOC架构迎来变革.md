---
title: RSAC2024观察：SIEM/SOC架构迎来变革
url: https://mp.weixin.qq.com/s?__biz=MzIwNjYwMTMyNQ==&mid=2247490158&idx=1&sn=494d029d110af34b91a917ae5addd142&chksm=971e776ca069fe7a5db64c111b7ad3c961df6170dc45638538cb20b98840a71c8586bb3466b8&scene=58&subscene=0#rd
source: 虎符智库
date: 2024-05-17
fetch_date: 2025-10-06T17:16:08.931006
---

# RSAC2024观察：SIEM/SOC架构迎来变革

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0ibSzjpDC6qE25SHz0p8D5txHic4sBVfU1Uhfy9PpibicdNEfEpP4ibTVZmUwASicduw6oaoXVJalfibibbkTqG9VuKDA/0?wx_fmt=jpeg)

# RSAC2024观察：SIEM/SOC架构迎来变革

叶蓬

虎符智库

![](https://mmbiz.qpic.cn/mmbiz_gif/f0ibSzjpDC6pSZGLpTxpWAujjOHTP1xd2fhzHudXhsB5QVPzJQJg6Q6yhVRialQboJmKeOlxwSEmeYiaxhVpTicTMA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

本文**7246****字**   阅读约需**19****分钟**

2023年RSAC大会的情景依然历历在目。彼时，以ChatGPT为代表的AI成为了大会的最大亮点。但除了ChatGPT背后的微软在会上大放异彩，其他厂商的AI主题大都停留在PPT层面。毕竟那时候大家都没啥积累，更多都是对GenAI变革网络安全领域的憧憬，以及对GenAI自身安全的担忧。

在意识到GenAI给网络安全产业带来的变革性作用后，安全厂商纷纷大举投入。到了2024年的RSAC，厂商们显然有备而来，让GenAI在网络安全产业的应用更加掷地有声。毫无疑问，AI（尤其是GenAI）依然占据了本届RASC的C位。在笔者收集的282个大会胶片中，仅标题带有AI的就有33个。

RSAC大会执行主席Hugh Thompson在主旨演讲中表示，综合2024年RSAC所有议题，所展示出的三大趋势关键词分别是：职业倦怠（Burnout）、人工智能（AI）和风险管理（Risk Management）。细细想来，都在情理之中。简单理解，正是网络安全领域的职业倦怠促成了人们对AI的期待，而风险管理则是安全永恒的旋律。在笔者看来，这里的职业倦怠既包括甲方追赶不断演进的威胁形势时的力不从心和对现有技术能力的不满，也包括乙方（厂商、服务商）遭遇现有技术难以突破常态化安全防御的困境并最终归为客户堆人头的无奈。AI，在当下成为了大家克服职业倦怠的救命稻草，但它真的是灵丹妙药吗？我们已经举起过太多的圣杯。

**AI重新定义安全**

来自Cisco安全的两位副总裁（Jeetu Patel和Tom Gillis）继去年带领大家畅想了AI加持下的SOC后，今年又为大家进一步打开脑洞，畅想了一番AI将如何重新定义安全。

Jeetu Patel表示，**当前颠覆安全的三个关键技术分别是AI、内核级可见性，以及硬件加速**。AI原生技术，基于eBPF获得内核的可见性技术，以及支撑算力和应用加速的硬件（DPU、GPU）技术将从根本上改变现有的安全系统架构和运行方式。他说，“这不是某个产品的新版本，这是一个全新产品的第一个版本，是前所未有的架构”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLbs0bEcbicnQuperaRszSYFghYRN5RBaC8KrheN4ssWODxiaibWiay2KI5g/640?wx_fmt=png&from=appmsg)

他通过AI驱动下的自动网络访问控制、自动网络漏洞补偿控制和自动应用升级三个典型场景为我们呈现了一幅笔者称之为AI自适应（Adaptive）安全的美好图景。

所谓AI自适应安全，是指AI加持下的自动闭环的自适应安全，在AI的驱动下和人类的参与下，预测、防护、检测和响应（或者称为OODA）自动闭环的过程，与CrowdStrike提出的自适应安全姿态同义，对应微软提出的GenAI在安全领域应用进程预测的第三阶段（自适应归因与保护）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmL5zIIibBDomsywIicgOxwnLciaNEYGpnUQXiasjicUPeJuf5UThgkCpn8pKA/640?wx_fmt=png&from=appmsg)

而这个AI自适应安全也跟Splunk提出的完全主动自动化具有类似的含义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLbyUPzNBuicHib7HnKEJXGmWicniahUrvIicUBmIlPkoG6z8QJf0Borf66Fw/640?wx_fmt=png&from=appmsg)

让我们把视线从宏大叙事拉回到现实。在大会上有个议题评估了可能最受GenAI影响的10个安全产品，并将其分为了两类。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLurHf5vNpbV9IUAAzHrs5DynMC1Feib2ibwvRYxtOxWbQBWdticNSJDsWA/640?wx_fmt=png&from=appmsg)

可以看到，安全运行基本都获益于GenAI。

**SIEM/SOC架构迎来变革**

以EDR起家的CrowdStrike公司首席执行官George Kurtz在大会上为大家带来了所谓下一代SIEM的理念。在题为《Next-Gen SIEM: Converging Data, Security, IT, Workflow Automation & AI》的演讲中，George Kurtz开宗明义地指出，“安全是一个数据问题，现有的SIEM无法满足SOC的需求”。他表示，现有的SIEM面临数据悖论，一方面需要更多的安全数据，一方面又无法及时有效地处理这些海量安全数据，导致在安全防御中无法跟上对手的节奏，无法阻止失陷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLnslbw6wq2OFoTwIyVnOLpm8yvKPJbpqEz8Y5IJdqWz3tFtic1a2HewQ/640?wx_fmt=png&from=appmsg)

对此，George Kurtz提出了CrowdStrike的下一代SIEM理念，其中包括五个核心观点。

**其一，下一代SIEM可以原生地集成到你的安全平台中**，意即SIEM不要创建新的安全孤岛和烟囱，要跟其它安全防御设施有机融合。

**其二，数据摄取与AI自动化是下一代SIEM的架构基础。**George Kurtz表示，根据他们的调研，EDR日志是SIEM的核心日志源，甚至有的SIEM用户EDR日志占比高达85%。因此，端点日志是其下一代SIEM新架构的构建起点。基于这个判断，CrowdStrike为大家呈现了其下一代SIEM的数据摄取与分析的层次模型，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLThvIhzwV7LPOqx980Uus8bQR5bzk9St9WaPg19H7qNibl0cfYBM505A/640?wx_fmt=png&from=appmsg)

这个模型以自身产品家族的端点和云数据为核心，辅以第三方数据摄取，借助AI驱动的数据范式化和数据富化，为SIEM提供一个坚实的数据基础，然后在AI驱动的工作流自动化作用下实现自动地的威胁监测与响应。最后，上述所有功能中用到的大模型（LLM）既可以是CrowdStrike原装的，也可以是用户自己的，可以自由切换。

**其三，下一代SIEM能够实现自动化的日志管理，**包括日志产生、日志摄取、日志存储、日志检索、日志数据管理等。

**其四，下一代SIEM将不再需要对数据成本妥协。**就像现在再没有人会对手机通话时长或者流量焦虑一样，未来的SIEM数据扩张成本将在基础设施建设到一定规模后趋向于零。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLk0XeJCl85Ts5FjEY2A6XLLTia9kXgnvNMtIUnzRN8oFsRMD1kPPZWzA/640?wx_fmt=png&from=appmsg)

**其五，下一代SIEM将实现AI驱动的合规报告自动生成。**CrowdStrike认为这是很关键的一点。因为，现在人们耗费了大量时间将实证的安全数据映射到各种合规性安全框架中（譬如CSF、FISMA、PCI DSS，抑或是我们熟悉的等保）。在AI的加持下，这些报告将可以自动生成。

George Kurtz进一步提出，如果上述下一代SIEM实现，将成为AI原生SOC的操作系统，为所谓的AI原生SOC【笔者注：XX原生已经成为当下最时髦的修饰词之一】提供一个基础的编排层。

那么，Crowd Strike眼中的AI原生SOC应该具备什么能力？George Kurtz为我们描绘了五大能力。

**第一，自动化威胁检测与响应。**的确，都AI驱动了，再不实现自动化实在说不过去。

**第二，安全预测。**Predictive Security又是当下的一个热词。毕竟，都高级AI（尤指GenAI）驱动了，仅做事中检测事后响应也太屈才了，总应该可以事前性预测攻击路径、预测漏洞啥的吧。

**第三，工作流程自动化。**理解SOAR的读者对此自然不会陌生。

**第四，富含上下文的安全智能。**没错，上下文（Context），或者情境信息十分关键，要实现安全智能，丰富的上下文必不可少。记得有一篇文章，题目为《网络安全的未来是上下文》。

**第五，自适应安全姿态（Adaptive Security Posture）。**在LLM加持下，AI应能够在用户实际环境中自学习，自我强化，自我提升，不断适应新的威胁变化和业务变化。

最后，George Kurtz给出了一幅下一代SIEM的要素关系图，如下所示，包括：人、工作流自动化、数据和人工智能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmL88zT97Cibww0xG8AKI3S5AgFNXDfkG5AVnrbnFicMxjAc7NFaEZMm2zQ/640?wx_fmt=png&from=appmsg)

**纵览整个演讲，应该说，笔者完全认同SIEM到了重构的时候，也认同AI加持以及更基础的数据架构是整个重构的关键所在**。但有趣的是，CrowdStrike终归是SIEM领域的新军，其日志管理技术最早源于2021年对Humio的收购。Humio的日志管理技术在整合到Crowd Strike后叫做Falcon LogScale。而下一代SIEM则是Falcon LogScale的最新版本和最新称呼。在Gartner最新发布的2024年SIEM魔力象限中，CrowdStrike未能上榜，理由是Gartner认为Falcon LogScale还是不够开放，更适合作为CrowdStrike家族产品和技术的扩展。当然，Gartner这份报告调研截至时间是2023年3月，迄今一年多时间里，不排除CrowdStrike的下一代SIEM有新的变化。

作为SIEM/SOC领域的领导者之一，Splunk也毫不留情的对自己的现金牛产品进行革新。在题为《Revolutionizing the SOC for the Future Threat Landscape》的主旨演讲中，Splunk的执行副总裁、总经理Gary Steele为我们呈现了在跟Cisco兵合一处后对未来SOC建设的新思考。

Gary Steele表示，SOC成功的首要能力是“看见”，而要“看见”就需要大量的数据，因此，“安全是一个数据问题”【笔者注：跟CrowdStrike可谓不约而同】。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLCQgyRPibncicDPqVwAwf6jeq6SoaMV7suyzAQTLsdP07k2pWAiaOlZHYg/640?wx_fmt=png&from=appmsg)

接着，Gary Steele对这个数据问题发出了灵魂拷问：你有正确的数据吗？你能检测到威胁吗？你的数据管理有效吗？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLU7sSibDCecibtJtHaal92xbDicYzOciadfPE8I77XG1jEUQNnKofnFCTQA/640?wx_fmt=png&from=appmsg)

放到以前，这些问题似乎都已经解决，但在当下的复杂威胁形势和防御体系下，面对大规模资产的、海量数据条件下的安全运行却面临重大挑战。也就是所谓SecOps at Scale的问题。进一步，当前威胁形势和防御体系的复杂性首先体现在碎片化上：各种各样的数据隐私法律法规要求导致数据存储和使用的地缘政治化和碎片化，数据引力问题导致数据移动困难，混合云和多云导致跨云和本地的安全运行一致性难以实现，大量的单点解决方案造成数据孤岛和应用筒仓，融合的数据在不同的团队之间（譬如安全团队、IT运行团队、业务团队等）交互和共享存在困难。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmL1u0xLN5JyjpX24qu3UdotNnQiawgreuKDUDqy2PgepAsTq90nicfO4UA/640?wx_fmt=png&from=appmsg)

如何打破这些SOC的藩篱？Gary Steele认为需要重新思考数据架构。他说，“过去那种日志集中优先的SOC技术架构已经一去不复返了！我们要把分析向数据侧靠拢，而不是将数据向分析侧靠拢。这是一种根本性的改变”。基于此，Gary Steele给出了未来SOC的三大支柱。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLCDoe2ebf6pqfOvOeOQY2e0jk8aRsHcU8SKfTHWG2TCX4NL8RP5ae7Q/640?wx_fmt=png&from=appmsg)

**第一支柱：单一平台**，指安全运行人员在统一的工作面上进行威胁检测、调查与响应，能够获得统一（一致）的上下文（情境）、洞察和行动。

**第二支柱：自动化和AI**，指安全运行人员可以在没有噪声影响的情况下聚焦真正要做的事情，而自动化和AI就负责去噪。

**第三支柱：数据联邦化**，指安全运行人员可以根据自己的业务需求和权限检索数据，而无需关心数据位于何处。

接下来，让我感觉有些违和的是，Gary Steele抛出了一个论断——未来SIEM将与XDR融合，成为新SOC的核心——作为对单一平台的落地和对与Cisco整合的回应。难道未来的SOC就是Splunk的SIEM加Cisco的XDR吗？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmLj7ttw1g6HYduqgMHdQI2JDt2dc0T5HlgqRf8VwMrxAxDRgz94GEl2g/640?wx_fmt=png&from=appmsg)

不可否认，SIEM和XDR在不断互相渗透和融合，但简单地将二者叠加到一起显然并不能代表未来SOC。当然，我们还需要AI和自动化，但这还不够。

Splunk对待AI的态度还是比较审慎的，一如业界大佬的做派。Gary Steele表示，在AI的加持下，分析师的重要性将加码。AI将用于增强而不是取代人类分析师，让分析师成为真正的防御者。Gary Steele认为不存在自主SOC（Autonomous SOC）【打脸PAN】，AI还是坐在副驾位置，上不了驾驶位，并提出了一个新词：Fully Proactive Automation（完全主动的自动化）。AI可以提升防御者，帮助分析师进行告警分诊、案例管理、事件响应、漏洞管理、工作流处理、……，但整个安全运行过程依然是人在回路的，AI更适合于解决特定问题，同时AI的开放性和扩展性十分重要。

最后，Gary Steele不忘发挥一下Splunk跨ITOps和SecOps的数据分析优势，将安全运行推到了更广泛的业务连续性运行范畴，以实现所谓的数字弹性。

**纵观整个演讲，笔者认为，除去AI和自动化这类显而易见的SIEM/SOC变革因素不谈，相较于CrowdStrike提出要变革数据架构但却没有具体路径，Splunk进一步阐释了数据架构变革的关键方向之一——分析向数据侧靠拢，也即数据联邦化。**但进一步来说，Splunk对于未来SIEM/SOC架构的阐释也就是点到即止。

**将GenAI应用于SOC**

在本届RSA大会的创新沙盒决赛中，出现了一家以GenAI赋能SOC的创业厂商——DropZone AI，而该公司创始人恰恰还是一位华人，并且在他去年初创业伊始就开始与笔者沟通GenAI用于安全运行的技术。成为极少有的站上RSAC创新沙盒决赛赛场的华人，笔者为他感到骄傲。对于公司名称，他解释到，DropZone AI这个词所表达的是要做一款“增援安全运行人员的智能助力的传送门”产品。

DropZone AI的产品引入了AI Agent（智能体，或称为“AI行为体”）技术，从而将GenAI增强SOC的应用水平提升到了一个新的高度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pN88yP0NouLUQUPfaaxjmL6rsicaRia6KQR78dibftSMBG2xx4iaqgLicF4whu37fNJ3kUxVLbu7DkbaQ/640?wx_fmt=png&from=appmsg)

DropZone AI的核心是告警研判和事件响应。与一般的使用GenAI提示工程甚至是RAG来进行告警研判不同，DropZone AI的核心技术在于上图所展示的“魔方”。通过这个魔方，DropZone AI具备了推理和规划的能力，能够自主进行任务分解和动作调用与执行，代表了当前GenAI应用于SecOps领域的最高水平。

值得一提的是，DropZone AI并不是要取代现有的SOC，而是跟现有的SOC平台集成，赋能现有的SOC团队，减轻他们的告警疲劳。

Elastic在大会上做了一个题为《Fight Smarter:...