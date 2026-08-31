---
title: 大学泄露文件曝光俄军网络战人才流水线，鲍曼第四部门如何为GRU输送黑客
url: https://mp.weixin.qq.com/s/3liXqsMm8ejFn4xuMeaqXw
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:51:56.577305
---

# 大学泄露文件曝光俄军网络战人才流水线，鲍曼第四部门如何为GRU输送黑客

# 大学泄露文件曝光俄军网络战人才流水线，鲍曼第四部门如何为GRU输送黑客

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

2026年，一批从暗网流出的内部文件，把俄罗斯最负盛名的技术类高校之一鲍曼莫斯科国立技术大学（Bauman Moscow State Technical University）推到了舆论中心。文件显示，这所大学军事训练中心内部一个代号为第四部门（Кафедра № 4）的隐秘单位，长期承担着为俄军总参谋部情报总局（GRU）培养网络战人才的核心职能。

这不是坊间传闻里那种零散的黑客培训班，而是一套完整的制度化人才流水线，从招生、课程设计、攻防演练到毕业分配，每一个环节都和GRU的实际作战需求深度绑定。约250名职业和预备役学生在三个专业方向上接受训练，课程内容既涵盖密码学、网络防御这类防守技能，也包含密码攻击、服务器漏洞利用、恶意软件编写这类进攻性技术，甚至还有宣传操纵和信息战的专门模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrv5awCdE2hfM2vvpBvnzLSc53A1g0a7jaUo9M9wqsnlQHWHjuibKnfFkOHt3eJaianRJUbeUhPjqkDmAYltW18zh5pxIj7ia9hJI/640?wx_fmt=jpeg)

鲍曼大学第四部门员工与毕业生合影，这批人员中不少人后续进入GRU下属网络战单位

更值得关注的是人员去向。调查确认，该部门毕业生被分配到GRU第26165军事单位和第74455军事单位，前者就是外界熟知的APT28（又称Fancy Bear、Forest Blizzard），负责网络间谍和政治干预，后者是Sandworm（又称APT44），以针对关键基础设施的破坏性网络攻击闻名。这意味着第四部门培养的人才，直接输送到了俄罗斯最具攻击性的两支网络战力量当中。

这批文件最早出现在一个名为DarkForums RU的暗网犯罪论坛上，该论坛是RaidForums和BreachForums被打击后崛起的替代品，主要用于交易被盗数据库、沦陷账号、恶意软件等非法物资。2025年BreachForums被捣毁后，DarkForums用户量出现显著增长。

发布者使用的账号名为Losyash，注册于2026年6月25日，调查时该账号只发过一个帖子、一条回复，累计在线时间4小时27分钟，最后一次访问是2026年7月10日晚7点09分。账号资料里没有个人简介、位置、主页、性别信息，没有推荐过其他会员，也没有获得过论坛徽章，这种干净到反常的画像更像是专门为发布这批数据而临时注册的一次性账号，而非论坛老用户。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrovvjLCoK6aliaqbuPfGvplqoN4K2vibw1aMftb7ia1iaNjZBkQZ49M5SAfibxMZUu6LOOmeTCL6O48Wq2HMmn7Zd23qltzesTXQjY/640?wx_fmt=jpeg)

暗网论坛DarkForums上发布者Losyash的账号资料页，显示该账号注册时间短、活动极少

帖子内容很简单，只声称有俄罗斯军事数据可供下载，附上了两个在线链接，数据总量约1.8GB。至于这些文件最初是如何从鲍曼大学系统中被窃取的，目前还没有定论，调查尚未锁定具体被入侵的账号。

DomainTools威胁情报团队（DTI）对这批文件做了独立的真实性核验。国际媒体联盟（包括The Insider、卫报、世界报、明镜周刊等）也对文件进行了交叉验证。核验的核心工具之一是FOCA，这是一款专门用于分析文档元数据的取证工具，可以从Word、PPT、PDF、Excel等文件中提取创建者、修改时间、服务器路径、用户名等隐藏信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoxgJKv2wcdOEibdtHsOhicrVkTM17cAH0HnA2TIV3GNN4sm9Z4Z4xMtodicbr3wic9IG3gtBNPJ9vjDtNzUZL91UIiaficgVA82TQic4/640?wx_fmt=jpeg)

FOCA元数据分析结果，显示文件关联的服务器列表，包含bmstu.ru（鲍曼大学域名）下的多台主机

分析覆盖了约1600个文件，类型涵盖Word文档、PPT幻灯片、PDF、Excel表格、图片以及.ics日历邮件文件。元数据显示文件来自鲍曼大学的行政和技术环境，关联的服务器域名包含bmstu.ru（鲍曼大学官方域名），IP地址段集中在195.19.33.x和195.19.34.x，用户列表里能看到大量以PC\_开头的计算机名，以及具体的人名账号，这些内部结构信息很难凭空伪造。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrbCboFyj95YEticcOLwibRrib5TtV70r7fjLb8NdEvS56mvqOsh2FmNgM4icy193BrSh2UibLljapMHGqh2SllX9MqlGf41qlrmibKA/640?wx_fmt=jpeg)

FOCA提取的用户和计算机名列表，大量PC\_前缀的主机名和具体人员账号，符合真实机构内部网络特征

文件内容的内部一致性也支持真实性判断，人员编制结构、课程体系、军事专业代码、审批链条、实习记录等要素相互吻合，加上记者的后续 corroboration（交叉印证），调查团队评估这批材料属于真实的机构内部档案，而非伪造的虚假情报。

这批泄露数据不是单一的作战档案，而是一份完整的机构运营存档。内容包括人员花名册、课程表、考试记录、考勤和体能数据、体检档案、兵力规划表、课程教材、会议论文、行政往来函件等，几乎覆盖了第四部门日常运营的方方面面。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqDpibbgN6xicHN0Xl9May3WAXu2KtJJHE0dicaIibz56DDr355GJ4ethGaAu48MXEy5PI5XNcdAvqCdk6pDW1n4UvIOnzuo6ls0rU/640?wx_fmt=jpeg)

泄露文件样本截图，文件名以俄文命名，涵盖课程表、实习记录、体检报告、会议纪要等多种类型

数据显示六个学年共有约250名学生，2024年计划招收86名新学员，同时还有相当规模的预备役人员。实习记录把学生派往莫斯科、莫斯连特根、沃罗涅日、库尔斯克、巴泰斯克、塞瓦斯托波尔、布格里、克拉斯诺达尔等地的军事单位和院校，这些地点的分布和各专业方向的职能高度对应。

除此之外，文件中还包含恶意软件分析和网络威胁情报研究材料、兵力规划文档，以及一个直接对接军事情报方向的金融领域网络安全专业。这批文件虽然没有给出每一名毕业生的最终分配去向，但完整暴露了俄罗斯军事网络和技术情报人才流水线背后的人员、培训、 doctrine（作战学说）和行政体系。

公开报道常把第四部门简化为GRU黑客学校，但文件显示它的职能范围要宽得多。这个部门服务于俄罗斯总参谋部的多个组成部分，内部材料明确写明，该部门为总参谋部总局（GRU）、总作战局、第八局培养军官，这三个机构分别对应军事情报、作战规划、机密通信与密码学及信息保护。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrbkribdibWruIjQSzxch46gGQPCiazfhEwVxjqZNZdE9KsINgicYhZW9HJQxNeNkpfAbIkmhM6OLDmzRXUSz9ToHnEn1zVDLpz2Zs/640?wx_fmt=jpeg)

第四部门架构与人员分配流程图，三个专业组分别对接GRU不同职能方向，VUS 141600是规模最大的方向

学生被分成三个编号组，每组对应一个独立的军事职业专业和总参谋部需求。

第一组对应VUS 093400，正式名称为特别情报局（Special Intelligence Service，简称SIS），资质要求由总参谋部总局首长批准，这个方向和军事情报的关联最直接，也是公开报道关注最多的方向。

第二组对应VUS 141600，名称为信息技术效果运用与防护（Employment of Forces and Means for Information-Technical Effects and Protection Against Information-Technical Effects，简称EFMIT），由总作战局批准资质要求，培养的是作战级网络效果和防御性信息技术活动人员。

第三组对应VUS 751100，名称为信息技术保护，看起来是为安全军事系统、机密信息保护、通信安全或相关技术安全职能培养军官。

一个容易被忽略的细节是，VUS 141600才是第四部门规模最大的专业，2024年约有120名职业和预备役学生在读，接近部门总人数的一半。这个方向是部门的作战级网络战专业，培养军官规划和运用信息技术效果，同时防御敌方的同类行动。这种攻防一体的训练是俄罗斯军事 doctrine（作战学说）的一个特点，蓝队和红队的规划与职能被放在同一套课程体系里培养。

这个规模说明俄罗斯并不是只在培养一小撮精英入侵专家，而是在生产一支更广泛的人才队伍，能够把网络行动整合进军事规划当中。

第四部门的一份讲义把信息技术武器定义为用于篡改、销毁、复制、阻断或窃取信息的能力。课程体系把进攻性入侵、防御性安全、技术情报和心理操作融合在一起，学生接受的训练内容包括密码攻击、服务器漏洞利用、软件漏洞挖掘、恶意软件创建、渗透测试、技术监视、宣传和信息操纵。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDribFC7EnV2dKoaAvHXNx2QiawrGGuRROT6OV0HIsWSnPOZUWASBtEjlXkDMIILalJdtCXWsHJuWO8yhFPxPJAMqeIROtpGJCtBM/640?wx_fmt=jpeg)

课程PPT截图，标题为信息技术武器的定义与用途，俄文原文详细描述了篡改、销毁、阻断信息等作战效果

教学材料并没有把进攻和防御网络行动做严格切割，两者放在一起教，目的是让操作员既会攻击也会防守。防御措施包括检测、阻断、隐蔽、牵制、技术欺骗、反击，以及针对敌方基础设施的活动以干扰正在进行的行动。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqict0QvWeSvzAHnqnicP0NVFgib0BldficYyEQu07NpCKqSrMIHszOMytb2K3iapcMxukh3C8fjhb3LlczEfMz1Yq4MdmD8rTMEcAo/640?wx_fmt=jpeg)

第四部门GRU网络战课程体系全景图，涵盖进攻性网络行动、防御性网络行动、心理与信息战、技术情报、技术保护、恶意软件分析与CTI六大模块

技术保护课程覆盖密码学和隐写术，以及代码分析和入侵检测。学生还接受硬件检查、物理植入物发现、未记录设备功能识别等训练，这些科目指向技术反情报和供应链安全、固件分析、嵌入式系统检查等可能的分配方向，其他可能职能包括安全采购和专用军事平台保护。

文件还揭示了一个报道较少的方向，恶意软件分析和网络威胁情报（CTI）项目。2023年鲍曼军事训练中心的一本文集，标题为空天部队武器军事和特种装备发展现状与前景的现实问题，其中包含恶意软件分类、基础设施测绘、异常检测、系统调用监控、攻防对抗演练等研究内容。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpVvCapQHPPP0ichYibNDIH9SmicZCX86d4696g9qicPqibdwJibcYSam5YSub9iab6qEUCvOzns3Pfeiajeg4g2djCC4KOg5LTgpEs34c/640?wx_fmt=jpeg)

桌面演习材料第74页，分析一个亲乌APT组织的攻击链，包括钓鱼邮件、SFX自解压包、重命名的UltraVNC远控木马和手动控制的C2基础设施

其中一篇论文题为亲乌APT组织实施网络攻击的作战方法分析，研究了一个以钓鱼和自解压归档为核心的攻击活动。攻击者部署重命名的UltraVNC二进制文件，使用手动控制的基础设施，论文重建了执行链、提取了配置参数、测绘了命令控制基础设施。虽然论文对归因（比如归因为乌克兰）的支撑有限，但方法论本身展示了恶意软件分析和开源情报收集的实战训练，也体现了攻击链聚类和脚本去混淆的能力，作者从现有证据和他人报告中重建了入侵过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqaic0xB9s5cIYCRsMU4kpprey48n8ItteJqvVQemdRlWJbFnicFYRMctiaVMO5Ev2PwgTLAicXt3DcwcmPD1ibZavr7opeCUl9B2fw/640?wx_fmt=jpeg)

第四部门课程作业与训练进阶图，课堂教学、攻防对抗演练、实战训练三个阶段递进，最终培养出具备作战准备的毕业生

第四部门把课堂教学和受控的攻防对抗演练结合起来，学生选择战术并对对方行动做出响应，评估每种策略的有效性。相关课程作业覆盖入侵检测和恶意软件分类，包括脚本分析和远程访问工具，学生还学习基础设施测绘和技术欺骗，掌握重建网络攻击链的方法。

这些信息说明这个项目超出了理论层面的网络安全教学，它包含网络靶场训练和对手模拟，同时整合了事件响应和作战规划。学生需要理解攻击者如何发现和利用弱点，也要学会优先配置有限的防御资源，并把网络活动放在更广泛的军事行动框架内考量。

实习分配把课程和对应专业的军事单位、院校连接起来。第一组VUS 093400的学员被派往库尔斯克和巴泰斯克，还有塞瓦斯托波尔和布格里，这些地点指向情报单位和情报收集职能，也暗示和特种军事编队及支持总参谋部总局的作战环境有接触，学员可能在现役军人监督下实践情报技巧和网络分析，以及技术收集和网络赋能侦察。

第二组VUS 141600的学员主要派往莫斯科和莫斯连特根，还有沃罗涅日，这些地点看起来和军事指挥规划相关，同时支持通信和作战活动，学员可能接触到指挥部职能中进攻和防御网络效果的运用，也可能参与自动化指挥系统和信息行动相关工作。

第三组VUS 751100的学员被派往克拉斯诺达尔高等军事学校，这所学校和军事通信及信息安全相关，也支持指挥控制系统保护，这个分配方向大概率聚焦安全网络和机密信息保护。

整体来看，三个编号组各自遵循不同的作战路径，VUS 093400支持军事情报和特别情报职能，VUS 141600支持网络效果、防御行动和指挥层级整合，VUS 751100支持安全通信和信息保护。技术课程、对手模拟演练和实地实习结合在一起，形成了从学术教学到受监督军事应用的结构化进阶路径，为毕业生进入俄罗斯情报、网络行动、指挥和技术安全机构做好准备。

国际媒体联盟的调查确认了进入两个知名GRU网络战编制的毕业生。第26165军事单位是GRU第85特别服务中心，外界通常将其与APT28关联，该单位还有Fancy Bear、Forest Blizzard等多个厂商命名。它的职能包括军事情报收集、网络间谍、影响支持行动，以及针对政府和战略目标的入侵。

第74455军事单位是GRU主要特种技术中心，和Sandworm（又称APT44）关联，职能聚焦破坏性和摧毁性网络行动，包括针对关键基础设施、军事目标、政府网络和运营技术（OT）的攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDp4fabN96r12LtrIROXnpXmny3iagX22LGtPJ52hAAkNyicOMUic3zWibic1r00FHC1IZcxWuVLM6bxDGbOicX6sTtBONHBpZXYicKOeU/640?wx_fmt=jpeg)

鲍曼第四部门人员输送管道图，毕业生经军事分配直接进入第26165单位（APT28/Fancy Bear）和第74455单位（Sandworm/APT44）

数据还把GRU高级军官和鲍曼学生的监督评估联系起来。Viktor Netyksho是第26165单位前指挥官、第85特别服务中心前负责人，他出现在该部门的教学和监督架构中。Netyksho是被美国起诉的GRU军官之一，被控参与2016年美国总统选举期间的材料窃取和发布行动。第26165单位军官的存在，加上毕业生被分配到26165和74455单位，把第四部门直接和GRU的间谍型网络机构以及破坏性作战分支都连接了起来。

记录中还识别出一个专门的学术路径，把金融领域网络安全培训直接和第一组VUS 093400特别情报局连接起来。这个项目聚焦信贷和金融领域自动化系统的安全，这意味着进入军事情报轨道的学生，事先就具备银行平台、支付基础设施、交易处理系统、身份控制、欺诈检测、敏感金融数据保护等领域的技术知识。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDr07iaB9MKuQONLfSaGljmfJ0a3rV4Wict1Yfy06cAa13mdEiciaibHVMcfP9FfRictBFErem7qViaibxUt3zYvD5qia4NYXePSpcEpQArA/640?wx_fmt=jpeg)

兵力规划表中金融领域安全专业条目，显示专业代码093400、学位代码10.05.03、专业方向为信贷金融领域自动化系统安全（特种用途）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpzcmFHqpbDiawLI9TC6Rwl6hqhd52mdlUlNaR2AgQmFQjuKXZ8LQECFKT5A1rD0eaPmnA604hXzTvd5JsxKLI77UdRojCRVAr0/640?wx_fmt=jpeg)

人事总局表格详细条目，军事专业为特别情报局，VUS 093400，专业方向为信贷金融领域自动化系统安全（特种用途），项目2021年经鲍曼学术委员会批准

现有材料没有明确定义这个专业的作战用途，也没有识别...