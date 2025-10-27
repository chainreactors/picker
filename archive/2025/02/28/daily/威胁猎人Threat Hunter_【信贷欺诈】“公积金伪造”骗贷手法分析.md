---
title: 【信贷欺诈】“公积金伪造”骗贷手法分析
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247499035&idx=1&sn=d11ef99e520f528479f5c5aae50f06e4&chksm=eb12db20dc65523640aa9a9e5ed38fee25c0b62f85314e2018e5be469329ed67322bb17c024f&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2025-02-28
fetch_date: 2025-10-06T20:39:02.457794
---

# 【信贷欺诈】“公积金伪造”骗贷手法分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqEJ2f0FibeYxRz5XVkeq8uU4yTwEmQGV3ek2DXgNYqTxE5XzDM4TetrQUeSHGfLGgESNb2xbU9Hz2w/0?wx_fmt=jpeg)

# 【信贷欺诈】“公积金伪造”骗贷手法分析

原创

猎人君

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4mAgZtBianqHwB5L4n1SdUaicvcFspoC5LC0sR6QhONHlmxKqJbr50j9XvHibLLDeVM6GzOPt57raMG2kxzAuFfoA/640?wx_fmt=gif)

近年来，尽管监管部门加大了对金融贷款虚假材料、违规人员的打击力度，但仍有不法团伙背地里给一些资质不足且有资金需求的客户“包装公积金资质”以骗取金融机构贷款，严重扰乱了金融管理秩序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEJ2f0FibeYxRz5XVkeq8uU4hr4HRVTV59pvHK1iaxUmKVVpNau8jaZjVIaTON0ty53CicicHqZeiazKCw/640?wx_fmt=png&from=appmsg)

**公积金伪造**：本文也指“公积金包装”，指黑产伪造虚假APP公积金数据，或虚构劳动关系帮助客户补缴公积金，最终达到骗取银行等金融机构消费贷、工薪贷等个人信贷产品的目的。

**01**

**包装“三无人群”成“优质客户”，每个客户贷款金额可达60万元**

威胁猎人研究发现，不法分子专门瞄准征信良好但缺乏稳定收入来源且有赚快钱需求的“三无人群”（无工作、无资产、无流水），通过伪造虚假APP公积金数据、虚构劳动关系补缴公积金等手段，骗取银行等金融机构消费贷、工薪贷等个人信贷产品。

**目标人群画像：**征信好（如征信纯白、小白），年龄在25至50岁，有融资意愿但本身无大额贷款资质的人群。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEJ2f0FibeYxRz5XVkeq8uU4x7yUicK3HnmWuCayHTopRHyQB1vOZickMrZ0BiamrsYQv9JjQ8CbLg06w/640?wx_fmt=png&from=appmsg)

据威胁猎人调研总结，在黑产的系列包装下，**每个客户可申请1-2笔公积金相关贷款，总贷款额度在30至60万。**这类骗贷客户**自身无还款能力，且还款意愿低**，黑产代还或嘱咐客户还款一定周期后就会出现逾期，最后仍是**放款金融机构承担资金损失风险。**

**02**

**伪造虚假APP和补缴公积金是“公积金包装”的两种常见手段**

威胁猎人了解到，黑产会根据不同金融机构个人信贷产品申请方式不同，在公积金欺诈操作层面有不同的方式，同时也会根据客户的征信、资质情况给客户匹配申请渠道，如通过虚假APP生成公积金信息、虚构劳动关系补缴公积金等，有些黑产还会有行口关系加持，使得包装后的客户能轻易申请大额个人信用贷款。

下面将整体介绍两种“包装公积金”的常见手段：

**手段一：虚假APP生成公积金信息**

黑产在召集到意向客户后，会审核其基本情况，收集相关资料，判断客户是否符合操作要求。只有在确认客户征信和形象符合标准后，才会安排客户前往贷款城市，并提供所谓的“三包服务”。

在此过程中，贷款黑产会与专门制作虚假材料的黑产合作，为客户伪造工作信息、单位地址、公积金信息等资料。他们会将客户的基本信息、公积金基数、余额等要求告知材料制作方，后者完成数据制作并导入虚假APP后台生成虚假公积金数据。

在贷款申请前，贷款黑产会指导客户背熟相关虚假资料，甚至利用某些行口关系，帮助客户顺利申请个人贷款。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEJ2f0FibeYxRz5XVkeq8uU4NMsAyxo6a1uo2vl39IRrJAt2f2MKc9SGFIIYUogdxussodvjiaQUJwQ/640?wx_fmt=png&from=appmsg)

**1. 虚假APP整体样式以假乱真，但内部很多功能缺失**

为了骗过金融机构的审核，黑产伪造的APP公积金模块的样式及部分功能与官方APP相似度极高，但为了节约制作成本，APP内部很多功能缺失，通过人工核验可以发现其破绽。

威胁猎人实测黑产伪造的某APP发现，该APP伪造的公积金模块整体看上去跟官方版本几乎无差异，涉及公积金相关的页面功能可以正常展示且部分功能是可以正常操作和进入下级菜单详情；但主页面不涉及公积金相关的常规一级菜单可以正常点击进入下级页面，但二级菜单页面均无法打开。

以下是黑产伪造的某APP公积金模块：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEfZdicGnBazWicM8ErySr4qGTM2B6y0KpYF9mMc9icGBriaaDPfyibia6n6vVLpa1V4F3WOpDtEFcpEPDg/640?wx_fmt=png&from=appmsg)

**2. APP伪造程序难度和成本将直接影响虚假APP的传播**

威胁猎人调研发现，黑产制作不同APP的公积金模块，因伪造程序复杂情况不同，成本不同。目前，市面上使用最广泛的是A平台，其制作难度相对较低，因此成本也较低，制作一年公积金数据的价格在1000-2000元左右。

但有些地区的金融机构会不认可A版本的公积金，只认可B平台的公积金数据，因此黑产也会开发B平台的公积金模块，但伪造B平台的版本程序复杂、成本较高，制作一年公积金数据的价格在4000元左右。

注：本文涉及金融机构/金融平台信息将用A、B、C等字母脱敏代替。

**手段二：虚构劳动关系补缴公积金**

黑产招募意向客户后，会审核其基本情况并收集基本资料，确认客户征信和资质符合要求后，安排客户前往贷款城市，并提供“三包服务”。

在此过程中，黑产通过第三方单位虚构客户与机构的劳动关系，伪造劳动合同或代缴合同，为客户补缴一年左右的公积金（部分黑产还会补缴个税）。公积金数据更新后，客户即可申请贷款。由于公积金基数较高且真实缴纳，或加上个税信息配合，客户通常能顺利获批个人贷款。

贷款完成后，黑产再将补缴的公积金余额提取出来，从而大幅降低作案成本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEJ2f0FibeYxRz5XVkeq8uU4EicfMch7NicibfvpUDibh2gWNDibDvIKlNmuCvBRzmSUCJ9LYThdzYqdSJw/640?wx_fmt=png&from=appmsg)

**03**

**通过情报及时感知欺诈风险，快速定位欺诈人群**

公积金包装欺诈涉及专业化的黑色产业链运作及利益分赃，能接受通过包装公积金资质并以此骗贷的的客户往往都是**无还款能力且还款意愿极低**的一类群体，**贷后逾期风险极高，最后只能是放款的金融机构承担风险。**

威胁猎人聚焦金融黑灰产攻防对抗领域，通过覆盖各类情报渠道源，主动获取大量信贷黑产/黑中介数据，基于欺诈特征分析模型自动化提取目标欺诈群体特征，同时结合数字风险应急响应中心（DRRC）专家的深入分析，为金融机构构建**从最新欺诈风险感知、业务/风控策略指引、到恶意贷款群体定位**的信贷反欺诈闭环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEJ2f0FibeYxRz5XVkeq8uU4ibEjv5rPdpqNzBsMgEHhNAzSGclS4qec2LGSsRdrw9ic6guQM7JbBxfA/640?wx_fmt=png&from=appmsg)

**1、及时感知并预警最新信贷欺诈风险**

威胁猎人全面监测金融机构的信贷业务以及各业务环节，信贷欺诈情报专家针对全网信贷风险线索进行主动运营，**及时感知黑产/中介的最新的欺诈风险，包含欺诈手法、欺诈场景等，如涉及房产信用/企业/车/现金/装修/消费贷/美容贷等贷款业务的欺诈风险监测。**

**2、结合群体画像提供业务风控应对策略**

威胁猎人信贷欺诈情报团队深入不同的信贷欺诈场景，以攻击者的视角分析并复现欺诈全流程，包括为金融机构提供指定作弊环节的手法分析，**如获客手法、包装手段、业务操作流程等**，通过不同场景分析报告为金融机构建立欺诈人群的业务行为特征等，为风控策略提供可解释的依据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEJ2f0FibeYxRz5XVkeq8uU4tyxWibEKX4te28zzfKGaumh26icHd9Vfx59F28AW0qticFfwiaricjvc9icw/640?wx_fmt=png&from=appmsg)

**3、基于有效标签等数据定位恶意欺诈人群**

基于对信贷欺诈产业链的持续监测及关联分析，威胁猎人可获取大量有效欺诈团伙的群体特征信息（如身份信息、银行卡信息等），可帮助金融机构在大数据模型等安全检测措施的基础上，基于恶意特征标签进行关联分析，精准定位欺诈人群。

**如您想了解更多“公积金伪造”骗贷情报**

**请咨询威胁猎人安全专家**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqHVlGkQ6z2HXw6In2ZVHRH0I7zqs0qk4U9a0s4vXnib60icOCLLgBibpCT2p51nvWJ1OZkCyzCnw3JEA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

威胁猎人Threat Hunter

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

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