---
title: 2026未来CSO训练营xa0|xa0首期回顾：大模型、具身智能、安全治理、攻防实战
url: https://mp.weixin.qq.com/s/Wm__323cGUstAweVfWcfhA
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:42.705381
---

# 2026未来CSO训练营xa0|xa0首期回顾：大模型、具身智能、安全治理、攻防实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpdVrZUIfXMD0jaKSuUicQYmiaeKqcI2yHaM9SL2c0PHh5QY3E054ZiaEicSb5X3GmMOhrnBgmBticflf0SbmGfzjYdeLWhPiaCVpJuZw/0?wx_fmt=jpeg)

# 2026未来CSO训练营 | 首期回顾：大模型、具身智能、安全治理、攻防实战

原创

安在
安在

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaENeAKze6OrS0jMGEIlospBGcRYDAZtjUv4UPJcrTeUfcAFDYZzYUOA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/8C1NLS8ickpfWKtk5lMjCGHPyiaVx3yZZxpURc0KfPiakK0Z3t5gSTxhk4ZoE0EiamiaGzmVLcjlJLd7XOxLoO2L6iad4Y6Db2h58psVrlusJCHPY/640?wx_fmt=gif&from=appmsg)

2026年4月，由安在新媒体策划发起的“2026未来CSO训练营”正式开班，该项目是专为有志成为企业CSO/CISO、安全负责人的网安人打造的精品特训，旨在通过资深从业者的经验传承，助力学员搭建体系化认知、实现职场进阶。

当前，AI大模型已全面融入企业生产经营全环节，成为业务创新与效率升级的核心引擎，与之相伴的全链路安全风险，也成为企业安全负责人必须直面的核心挑战。基于此，训练营首期《安全护航AI》主题课程，分别于4月18日和4月25日顺利完成授课。

本次课程特邀火山引擎安全解决方案专家廖双晓、非夕机器人信息安全总监刘歆轶、中国移动高级安全专家唐双林、布兰矩阵创始人李光辉等行业专家，围绕大模型全链路安全、具身智能风险应对、AI安全治理实践、大模型攻防实战等核心议题展开深度分享，本文基于本次授课实录精选摘编，以惠及课堂之外更广泛的读者。（翔实内容，见文末获取方式）。

**《大模型安全分享》（上）**

廖双晓 火山引擎安全解决方案专家

在大模型自身安全维度，OWASP LLM Top 10明确了十大关键风险。其中排名首位的是提示词注入风险，作为用户与模型交互的关键入口，恶意提示词可绕过模型安全对齐机制，诱导模型输出违规、违背公序良俗的内容。该风险是所有大模型的原生风险，在当前技术环境下无法实现100%完全防御。

其次是训练与推理全流程的数据安全风险，模型关键能力70%以上由训练数据的量级与质量决定，训练数据保护是大模型安全的重要环节。但国内绝大多数企业以调用公有云模型服务或私域部署开源模型为主，极少参与基模与垂域后训练，因此对训练数据保护的感知度较低，反而更关注推理环节中企业商业机密、个人敏感信息向第三方模型服务提供者泄露的风险。

其余关键风险还包括：非官方渠道引入基模、组件带来的供应链安全风险；恶意语料污染引发的数据投毒风险；未经清洗的恶意输出接入后端系统的不当输出处理风险；模型参数、系统提示词泄露造成知识产权损失的系统提示泄露风险；向量化数据隐藏恶意内容的向量嵌入漏洞风险；模型幻觉引发的错误信息风险，以及非预期的token与算力滥用造成的无界消耗风险。

当前大模型的产业应用已发生根本性转变，纯问答式的模型交互场景占比持续降低，行业主流已转向以任务完成为导向的智能体形态，多智能体协同模式也成为主流应用方向。需要明确的是，智能体安全风险并非替代模型安全风险，而是在模型风险之上的叠加、延伸与深化。二者的关系可类比传统IT环境中算力安全与应用安全的关系，智能体的安全防护始终以底层模型安全为基础。

智能体应用的主要安全风险里，目标劫持、工具滥用与利用、身份与特权滥用三大风险高度关联，构成了最主要的威胁。其本质是智能体被诱导利用自身权限与工具能力，完成非预期的恶意目标。其中，目标劫持指通过恶意诱导使智能体偏离预设任务目标与执行路径；工具滥用源于智能体集成的插件工具边界持续拓展，恶意用户可越权使用相关功能突破权限管控；身份与特权滥用则聚焦于人类权限向智能体的传递、多智能体协同中的权限继承问题，高危权限使用需引入强制人机协同管控。

**《大模型安全分享》（下）**

廖双晓 火山引擎安全解决方案专家

火山引擎旗下豆包大模型，在国内To C与To B端大模型服务市场占据头部份额。庞大的用户规模与服务体量，使其不仅面临着行业内频次最高的外部安全攻击，同时也承载着C端消费者与企业级用户对AI云服务最为严苛的安全诉求。基于这一行业背景，火山引擎构建了覆盖公有云AI服务全场景、对内对外一体化的安全保障体系与落地执行机制。

针对云服务大模型安全，火山引擎建立了与行业通用逻辑一致的清晰责任划分模型：在云上AI服务应用中，平台与租户的安全责任边界随服务形态不同有所区分——越是趋近高层级的SaaS化服务，平台供应商承担的安全责任越重；越是趋近基础IaaS层的服务，租户承担的安全责任越重；处于中间层的PaaS或MaaS服务，则由双方协同落实安全责任。

目前火山引擎AI云服务主要分为三类主力供给模式：一是趋近IaaS层的算力服务，依托国内领先的芯片储备，为用户提供基础算力资源；二是趋近PaaS/MaaS层的平台服务，通过机器学习平台与训推一体化方舟平台，为用户提供高效的模型训练与推理支撑，同时配套豆包基座模型及开源模型供给服务；三是SaaS化服务，涵盖To C端豆包APP、智能体应用，以及标准化的模型API接口服务。

基于上述服务模式，火山引擎明确了国内AI云服务合规与安全责任的清晰划分准则。

国内合规环境中，内容安全合规的优先级与监管力度远高于海外，是面向互联网公共服务的大模型与智能体应用不可逾越的红线，重大违规将直接导致服务下线。其中，AIGC内容标识强制性国家标准是必须落地的合规要求，无论采用何种服务模式，内容生成方均需承担AI生成内容的显式与隐式双重标识责任。

**《具身智能安全风险与应对》**

刘歆轶 非夕机器人信息安全总监

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpdxvkE6w80Uj1zSqBGaZeGicU6aWFeCw3Tyt0ibhGic96ar4vjlKD2Yup48Rlyiavbl0rHUOunE6r0KfgObOXrNNsMCsWiaiaScMebXg/640?wx_fmt=png&from=appmsg)

人工智能的探索，始于1950年图灵提出的图灵测试。这一测试的本质，是让机器模拟人类的思考与行为模式，若人类无法分辨交互对象的身份，即视为测试通过。如今主流AI已能在特定领域通过图灵测试，兑现了这一构想最初的预期。

人工智能的发展进程中，诞生过多个标志性里程碑。上世纪90年代，IBM深蓝战胜国际象棋世界冠军卡斯帕罗夫，让大众首次直观认识到，AI能在专项领域超越人类顶尖水平；后续AlphaGo在复杂度远超国际象棋的围棋领域实现突破，不仅在国内围棋界引发巨大震动，更彻底改变了职业棋手的训练与发展模式。

与此同时，国内互联网企业也在这一阶段展现出强劲的AI实力。字节跳动凭借深耕多年的推荐算法，在围棋AI模型竞赛中长期稳居前列，而这套算法也早已通过内容精准推送，深度融入大众的日常生活。除此之外，人脸识别技术在门禁、交通执法等场景的规模化落地，也让AI技术在国内头部企业的推动下，潜移默化地重塑着社会运行的诸多细节——只是这些应用大多局限于封闭的企业或行业场景，普通个体难以直观感知。直到2022年底ChatGPT横空出世，AI技术才彻底走出大厂的封闭体系，让每一个普通个体都能真切感受到AI带来的便利，直接引爆了席卷全民的AI热潮。

人工智能奠基人之一、Logo编程语言发明者西摩·佩帕特，早年间就曾提出预判：人工智能将对全社会产生深刻且颠覆性的影响，其能力上限远超当下人类的想象。他曾用飞机引擎做过一个经典类比：19世纪初飞机引擎诞生时，受限于当时的社会认知，人们只想着将引擎装在坚固的马车上推动其前进，却忽略了高转速引擎产生的气流，会直接让马车散架；想要让引擎真正发挥价值，需要完成飞机设计研发、机场与全球航线建设、卫星通讯网络搭建、民航管理制度建立、全链条专业人员培训等一系列翻天覆地的社会基建革新。

同理，当前人类对AI的应用，不过是其能力的冰山一角。受限于现有的社会形态与人类认知边界，想要释放AI的全部潜力，需要整个社会完成全方位、系统性的配套变革。

**《人工智能安全风险治理与实践》**

唐双林 中国移动高级安全专家

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpcaa2BZBoFr4WoVX75hf3YVaRvq2XhvplFMDHPrYvuTFOL8aia8bHxmZ0VA5p1cq0CuIlZkgzHZnsLS0Xpia9fUXibMuVlsOn5mw8/640?wx_fmt=png&from=appmsg)

人工智能的高速发展，既带来了广阔的应用价值，也伴生了多重安全风险。鲁棒性不足、公平性缺失等问题，并非人工智能领域独有，在传统算法领域早已存在同类隐患。但随着人工智能技术的快速迭代升级，各类安全风险呈现出全新的表现形式与更强的危害性，覆盖范围也延伸至算法、网络、数据、内容、基础设施与供应链等多个维度。

在大模型算法安全层面，存在六大类典型风险：

1. 公平性与偏见风险。模型训练环节存在偏差时，极易产生与性别、种族、地域相关的歧视性输出；同时单一通用模型难以适配全场景需求，需通过针对性训练与微调，打造适配本地化需求与垂直行业的专用模型，从源头规避偏见隐患。

2. 可解释性不足风险。大模型的推理过程常被称作“黑箱”，输出逻辑不透明，用户难以追溯结论的生成路径，极易出现无法预判的错误输出。目前部分模型已通过标注参考文献、完整展示推理链条等方式优化这一问题。

3. 鲁棒性缺陷风险。这是算法设计中的共性问题，在人工智能领域集中体现为对抗样本干扰——外部微小的恶意扰动，就可能导致模型推理、识别结果出现严重异常，例如车牌识别场景中，数字被轻微干扰后就出现识别错误。

4. 模型窃取风险。小模型极易通过多轮问答交互复原算法逻辑，实现整体窃取；大模型虽整体窃取难度极高，但攻击者仍可通过反向推理攻击，从交互结果中倒推训练数据，完成局部敏感信息的窃取。

5. 模型篡改风险。攻击者可通过类似网络中间人攻击的方式，介入模型的推理交互环节，恶意篡改模型的输出结果。

6. 输出不可靠风险。该风险最典型的表现就是AI幻觉，模型会生成看似逻辑自洽、实则完全虚假错误的内容，误导用户决策。

除此之外，人工智能还放大了多个领域的安全隐患。对此，中国移动锚定自身“AI+”战略与业务实际，为落地人工智能安全治理相关要求、保障人工智能全流程安全可控，编制形成了专属的人工智能安全体系架构，推动AI业务设计、模型开发、能力部署、服务开放全链条，均符合风险防范与安全合规的相关要求。该体系以“1264”框架为核心支撑，具体包括1个工作体系框架、2个重点发力方向、6大安全防控措施、4大安全领域赋能方向。

**《大模型的攻防实战》**

李光辉 布兰矩阵创始人

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpchmUiaXypybdoRIicMmYtXmMkbIicVeXumeLgV4hbL310ibEZSZHCeicToeUD7AqhzHxd4vwFX73mZEFCzXOy8z89U2SOgjvKetT9M/640?wx_fmt=png&from=appmsg)

以OpenClaw为代表的AI技术演进，正式开启了软件范式不可逆的变革时代。这场变革的底层根源，在于AI算法与传统软件工程存在本质性的逻辑差异。

传统软件工程基于CS、BS等固定架构搭建，所有交互流程、数据运算规则与结果输出逻辑，都遵循预设的确定范式，具备高度可预期性与运行稳定性。而AI算法彻底打破了这一底层约束：它先将自然语言、多模态信息转化为向量数据，依托超大规模参数量的模型矩阵完成向量运算，最终以概率预测的方式输出权重最高的结果，形成了与传统人工编码运算完全不同的运行逻辑。

模型权重是AI系统的底层基石，地位等同于传统软件的源代码。围绕模型权重，国内外主流模型形成了开源开放与闭源保护两大技术路线，同时衍生出模型蒸馏、防伪蒸馏等AI原生安全的基础防护方向。原本应用于移动端权限破解的“越狱”概念，也被迁移至大语言模型领域，成为针对AI系统的主流攻击方式，覆盖文本与多模态全场景。

AI带来的软件范式迁移，彻底重构了软件的全生产链路。传统软件工程遵循架构设计、分模块编码、多角色协同、DevSecOps流程发布的固定路径，而AI时代最鲜明的特征，是算法对传统软件的全面驱动。Agent系统可基于用户的自然语言意图，调用加载的各类专业技能工具，直接完成原本需要多专业角色配合、长周期执行的复杂工作，将原本数天的生产任务压缩至数分钟，极大提升了生产效率。

这场变革也对行业从业者提出了全新的能力要求：只有充分理解AI的运转逻辑、熟练掌握Agent等AI工具、通过提示词工程等方式精细化约束输入输出，才能保障AI输出结果的精准性与执行效率。

AI技术的高速发展，也给网络安全领域带来了颠覆性冲击。以OpenClaw为代表的类Agent产品，天然具备高权限、广通讯交互面的特性，攻击面极难收敛；它不仅存在远程代码执行、越权访问等经典安全漏洞，带来的安全挑战更是远超传统网络安全的覆盖范畴。

当前AI在漏洞挖掘领域的自动化能力，已在效率与覆盖范围上远超传统人工二进制安全分析，可挖掘出大量历史中从未被发现的高风险0day漏洞，形成稳定可利用的攻击链路。这一变化直接动摇了传统网络安全的技术方法论、防护体系根基，也对安全从业者的核心能力体系提出了颠覆性挑战。传统数据治理、Web安全、二进制安全等细分领域的大量基础工作，包括海量日志检索、无效告警过滤、有效告警提取等，都可被算法驱动替代。安全从业者必须转向对AI攻防体系的深度把控，聚焦算法自身安全、边界溢出、权限滥用、数据泄露等AI时代的关键安全命题。

**第二期预告**

首期未来CSO训练营已圆满收官。第二期《AI赋能安全主题课程》将分三次开展，分别定于5月17日、5月23日、5月30日三个周六完成学习，课程采用线上授课与上海、北京线下授课相结合的形式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfad1CxrticFPjpBRrkovfs5PGGFQ7oZic8h7MpEgu5s1Kicux7YGA01ibcXfqJ1Nxhz3X4HP1XNwjU20MWBic46KicQ2RgaZarpWXMI/640?wx_fmt=png&from=appmsg)

课程概要：AI时代烽火山林，传统网络安全过时了？失效了？没价值了？或者，用新技术解老问题？令传统网络安全在AI加持下如虎添翼或浴火重生？且看AI赋能企业网络安全之典型场景和最佳实践。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfBbCa17G2KyiaaCKmp6CgZ8br3t1an5ZKyOmjTnngdkqiaibLAibafCasTIQKqblmcJ5oRZ3Frdl2uZkMQAiaAibbotMdpjlXeBjbSU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpdT1XGCkg7tFg0iafty1TcxLtCnO3FUawJtwDT6y9uyHpC7vHibg1zD95M6RGFChT4VhqbmYAr3O9nhCPE2rxOUVNLYs7p3pibllg/640?wx_fmt=jpeg&from=appmsg)

**报名参学**

第二期报名，详情请洽

**花絮**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpcHWXicA8UDLCbZlthbHUiaS9I0ACZh7V3QUATAyaCtouV1OTCVNx82libVZicdpamTI1xQVW0yo2CjCmELYORjERYlgssCAtcY4cA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpeoIvFVdOvCEjnNCglRpJ0SHTsRJJjDmGo57OApGu57LPia6jTicCcmgIp7G7ibaDfl0JnKY1oWxEYDaxmLut809gFRhsIibSspTZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpcxdYX7xO83QR8nm9JScGnz1GwXNde3bo8hiaYInAFYGibYiczkZ61osbz6H1GPc3Os4ZL1Vj49qL9BSnHHsVgrC7HHD7eefk4Zh4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpcia7ibh1Zhvhibh5bfn2QESmso0S7e8KFHiacsGDoibMq0DVk3dAFaHKBicyINWPHOPB71Es5jvfJ0yE0Uia5SQW4fic2xibN1v19APYqY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpdG7SjjtLocJ9QMCa94NLdPx2yKhbs4BYrU2AMWibnDBGxNUib4IQLLFF04eGKej5gX3ZVJ5MEiaLJKXWjcoYg4rwIm4qt9NYMEgk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpeBulkpUU89edogUrtYmRebWJnpYpETmNxcicibicleyVHGv40RAvQ6bTVRotqdQqS4JFBH4tvPkIZueweMVxVJFHrUfaAuGSkRwU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfhmhzr4FmQAKUy8nZdERmubwbdfcyA...