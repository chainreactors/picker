---
title: 知远·世界主要国家与地区国防预算数据库说明
url: https://mp.weixin.qq.com/s/ITQNlsVHAeRfhCojHLWdLQ
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:31:51.032967
---

# 知远·世界主要国家与地区国防预算数据库说明

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5puaLG5r4aaZlEtGP1C01L9QBRL1wjnL9EwUYIrTghN2u8v93aoEwriaeRPmpkXficZ2rlaRkBf2a0aley2Ax7DQ/0?wx_fmt=jpeg)

# 知远·世界主要国家与地区国防预算数据库说明

原创

知远所
知远所

知远战略与防务研究所

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMHQZwesOqyzXC3qlWfuictfZMhFZpZMvUYPAHq1Jjq2v6I5syCnGO26Q/640?wx_fmt=jpeg)

2024～2031年，知远所全面转入**“以数据为中心，评估为主线，由任务式课题向自主式课题渐进”**的中期发展阶段，2023年度自主课题研究成果已推向市场，外军防务开源数据库、全球军事态势情报库应用稳步推进，将按计划启动支撑知远中期发展的数字基础——知远数据工程。本阶段重点建设以下数据库：**全球战略态势情报数据库、世界主要国家与地区国防预算数据库、世界主要国家与地区综合实力数据库、外（台）军人力资源数据库、外（台）军军事设施数据库和外（台）军武器装备数据库。**

本文是对数据工程之《世界主要国家与地区国防预算数据库》的简要说明。该数据库首批数据已在“全球军事态势情报数据库”之 “国防预算”模块上线，可经授权访问。

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMS7gwKYyRBF578gm0VWVf0K6z40a7aFeTWuicVtsOBHuD0WiarlVhtyxw/640?wx_fmt=png&from=appmsg)

**一、系统架构**

技术路线与知远数据库系列保持一致，采用B/S架构，提供总库及各子库，基于国别、军种、年度、预算关键字等提供多类组合式查询和统计服务功能。系统分为后台管理和前端两个子系统，既可在公网提供授权查询服务，也可以镜像到内网运行；既可以整库交付，也可以按国别模块提供服务。

**二、主要内容**

**（一）美国国防预算**

美国的国防预算是一个由规划、计划、引导资源配置制定而成的复杂系统，具有多阶段、多主体、多年度、自下而上、全面参与的特征，预算编制一般划分为总统预算过程和国会预算过程两个阶段。其财年计算以自然年的10月1日开始，至次年9月30日结束，总统预算一般于每年2～3月发布，国会在10月1日前按程序批准拨款法案，由总统签署后生效；如国会未在10月1日前批准拨款法案，则通过持续决议案（CR）为政府提供临时资金，总统签署后正式生效（当前正处于FY26财年预算未批准阶段）。

国防预算请求（预算科目050）一般包括三个方面，一是国防部部分（DoD，预算科目051），按拨款类别可分为军队建筑、运行维护、国防采购、研发鉴定、周转资金、军事人员等六个部分；二是能源部原子能活动部分（NNSA，预算科目053），按拨款类别可分为NNSA人员薪酬、武器活动、国防核不扩散、海军反应堆、国防环境清理和其它国防相关活动等六个部分；三是其它国防相关部分（DefenseRelated，预算科目054），包括退役军人部、住房发展部、国土安全部、商业部、司法部、国务院等部门与国防相关的开支。根据开源获取的数据和关注重点，本数据库所指数据专指051即国防部（DoD）的预算，这部分数据通常占总预算请求金额的98%以上。

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMyFt8HMQ5ziclAKfJFrj4Caca0NHibvZbaIRWwFuCsCVWRPRNrupnHSXg/640?wx_fmt=png&from=appmsg)

（二）台“国防部”主管预算

台湾的“国防”预算主要由“国防部”主管预算、特别预算，以及非营业特种基金组成。其中，“国防部”主管预算是指，由“国防部”这个主管机关所编列、管理、执行的，每年总预算中归属于“国防部”职责范围的预算总和。“国防部”主管预算全部由“国防部”内部编列，经行政院审查与核定，最后再经立法院审查后由台“国防部”内部执行。基本上，每一财年的申请预算书会在前一年的9～10月公开发布，法定预算书（也就是经过立法院审核过的批复预算）一般在财年当年公开发布。

特别预算，是指台当局因重大政策、突发事件或特殊需要，所编列的具有临时性、专项性、限期性的预算，不属于每年例行编列的一般预算。目前台湾地区所编列的特别预算中，如海空战力提升计划与新式战机两项预算都将于2026年执行完毕。

非营业特种基金，是由台当局编列、用于特定目标或长期任务的资金（特别预算是短期资金，非营业特种基金是长期资金，其中涉及的项目都是持续性运作的项目）。非营业特种基金的使用受到严格的法律与行政审查，确保资金用于规定的目标，如“国防”、社会福利、基础设施等。

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMnjHR23nqibjMGica6CMoGBtqKPpZfhlDVs3gjXeib4MVPG9wFr9wuJREQ/640?wx_fmt=png&from=appmsg)

三、数据说明

（一）美国

基于美国官方发布的国防预算文件，本数据库系统化采集和解析原始预算文档（如《国防预算概览》、各支用部门《国防预算申请书》等），将复杂非结构化的PDF/Excel数据转化为可交互查询的多维数据库，涵盖采购（Procurement）、研发试验与鉴定（RDT&E）、运营与维护（O&M）、军事人员开支（Military Personnel）、军事建设（Military Construction） 等核心预算类别。

目前，已完成了FY20-FY26财年数据入库（每年数据均在2000条以上），按照预算科目，这些数据跨年度、跨军种（陆军、海军、海军陆战队、空军、太空军及国防部直属机构），支持用户追踪特定项目（如“哥伦比亚级核潜艇”、“B-21轰炸机”）的资金流向、分析军种预算分配趋势，并关联兵力结构、装备采购数量等关键指标，所有数据内容均已人工翻译，提供原文/译文数据查看，方便用户使用。

特别需要说明的是，2024财年研发测试类R表预算还收录了《各支用部门国防预算申请书》中的数据，整合了各支用部门发布的43个PDF约上万页原文文件，细化至“预算项目成本”（PE、A/PP、CA）层级（数据量约1.1万条）。由于此项工作量巨大，因此其它年度和其它预算表未再做细化，但在此过程中，充分验证了知远所从项目包级扩展到具体项目的深化建设能力，同时也说明，知远所可以为急需客户定制研发将项目包扩展到具体项目的各年度、各类别数据的研发工作。

本平台首页采用树状结构来组织与展示，遵循其预算“从宏观到微观”的编制原则，主要层级如下：

•第一层级：预算类别（左侧导航栏）

•第二层级：军种/机构

•第三层级：预算账户。

平台通过动态可交互的树形控件来展示以上数据：

•可折叠树形导航栏。用户可以通过展开和折叠节点，在“总览”和“细节”之间切换，避免信息过载。

•聚合数据。点击任一节点，即可查看该节点下的所有子项目及其资金数额；系统还可自动计算并显示每个父节点项目的预算总额。

•纵横查询。纵向：同年度各项目预算数据通过树状结构逐级纵向展示，层级清晰。横向：同项目各年度预算数据通过数据表格逐年横向展示，方便对比。

首页：

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrM8S808eUiazuJjh1rkr7lwTcU9kkSbjGgOV2LUYOz3B5ibmiapss1guFpg/640?wx_fmt=png&from=appmsg)

分项查询：如军职人员费用

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMp9dTtTsvUwssk52Josns4quJXdUN2yYDbgKpX2ra2MLJTibEHW96nZw/640?wx_fmt=png&from=appmsg)

按关键词查询：（如F-35）

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMYMcWI1zFBBUQLShIpKj49KkbSVUGvjkGO36robfdUoMpiaSHNlrA1yg/640?wx_fmt=png&from=appmsg)

（二）台湾地区

台“国防部”主管预算的整个账目在编列的时候，主要以三个类别方式列账，分别为机关别、政事别和用途别。其中机关别根据预算所属的各部门以列账，陆军、海军、空军、资通电军、宪兵等等；政事别和用途别则以预算代码（数字组合）列出，其中政事别是根据台“国防部”所执行的主要政策职能予以列账，用途别是根据“国防部”主管预算支出的经济属性与支付对象予以列账。

根据其预算确定的程序（先发布申请预算、几个月后才发布法定预算），因此，目前该数据库入库数据为其2020～2026年7个财年数据（每年数据量近1万条），其中2020～2023财年数据为审核过的法定预算，2024～2026为申请预算，这点和美国预算库中每个财年数据包括申请预算、批复预算、执行预算是不同的。

平台功能及界面与美国防预算基本一致，只是按照台相关预算科目进行了数据融合和整合。

首页：

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMaibOsibhicsFhskdicAwbjPge95pUDhqzIds6EuYS2tuicU8pa1ubIVPlqg/640?wx_fmt=png&from=appmsg)

分类查询：如军事行政

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMWSUqlaIia8kKPLuLC6g4L54dI2peOiaY7D3ePQibYMYuZyUzbIDSCFDAw/640?wx_fmt=png&from=appmsg)

按关键词查询：如航油

![](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aatQ7iadTfImIqBpibJ4eMnrMjK2cP59I14iaXjuHReJnX9YSSibLW4jgxtjN5SLgGTcGEPBhic2YatLyg/640?wx_fmt=png&from=appmsg)

四、小结

目前入库的是仅为主要对手以及主要关注地区的部分年度数据，此数据库的建设目标是，持续收集世界主要国家与地区官方公布的国防财年预算数据，建成以国别和地区为单位的财年国防预算数据库总库，为从事外军研究的机构和专家提供防务经费数据支撑。

**地址请点击“阅读原文”**

![图片](https://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aZ1PGQJicClBFibTHL0cMObhFLwnloW8KRPzmsNokxAX4NHqicJw8RW9KKzUIxkNmQ1rUrdAfkr00DIg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aaQmuV0sOGM9VZFQiaiaf3GKVv1p2yuFds421o1XbRfKSmMXpoSHhwEurg7po29ic4XmR8SFgKcDoWkQ/0?wx_fmt=png)

知远战略与防务研究所

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5puaLG5r4aaQmuV0sOGM9VZFQiaiaf3GKVv1p2yuFds421o1XbRfKSmMXpoSHhwEurg7po29ic4XmR8SFgKcDoWkQ/0?wx_fmt=png)

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