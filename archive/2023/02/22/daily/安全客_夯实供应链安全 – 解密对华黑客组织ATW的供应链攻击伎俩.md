---
title: 夯实供应链安全 – 解密对华黑客组织ATW的供应链攻击伎俩
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649783157&idx=3&sn=6ef589ab07dcefaaadee307cea6ef360&chksm=88934b1abfe4c20cb4f676b90315ba3714ea4943fb8534e2f7ad52b4a1245796dd099cd022cc&scene=58&subscene=0#rd
source: 安全客
date: 2023-02-22
fetch_date: 2025-10-04T07:43:24.617880
---

# 夯实供应链安全 – 解密对华黑客组织ATW的供应链攻击伎俩

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb5vSeacluz2Wh34sjd9PfBIHicwOGeuJ72y57k1BT70KzG125VaCOXnZ8DkDnx1aCtJjj2e1oicVIDw/0?wx_fmt=jpeg)

# 夯实供应链安全 – 解密对华黑客组织ATW的供应链攻击伎俩

360威胁情报中心

安全客

2021年10月期间，网络上出现了一支名为AgainstTheWest（以下简称“ATW”）的黑客组织，特别针对中国、朝鲜和俄罗斯为主要目标，实施有组织的大规模网络攻击，窃取相关受害企业和组织机构的数据和源代码等，进行公开贩卖、公开敲诈和媒体恶意炒作活动，对我国的数据安全和网络安全声誉造成了恶劣影响。这个ATW到底是何方神圣？让我们来一点点撕开他们的真实面目。

## **ATW组织起源**

2022年4月，国外媒体对ATW组织进行了专题采访，根据ATW黑客组织成员采访自述，该组织是在2021年9月期间正式成立，拥有6名创始成员，其中一名成员在2022年3月已因病去世，该组织位于NATO（北大西洋公约组织成员国），核心理念和ATW组织全称单词暗含的意义一致，专门针对其认为的所谓“反西方国家阵营”目标实施网络攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PribQZZr3baEud6mprfOR3yzxAwZR4GAYHCcuN3iazibKWbS7rn0SVc1ks4wkibSb1KyhVu7mbfdPQAhw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

值得注意的是，在媒体采访中，ATW核心组织成员还透露了其成员不仅精通黑客技术，还内部分工为翻译、财务、程序员和美术设计等角色，除了英语，还擅长法语、俄语、德语、荷兰语和中文等其他不同语种。

可见ATW并不是散兵游勇，而是一支组织严密、分工明确，拥有稳定的资源、资金、经验和技术支撑，可以长期持续进行黑客活动的精悍团队。

## **ATW组织主要攻击手法**

2020年7月，瑞典计算机黑客Tillie Kottmann（非ATW成员）曾公开曝光泄露了微软、Adobe、联想、AMD、高通、联发科、通用电气、任天堂、迪士尼、华为海思等 50 家科技公司部分项目的源代码，该黑客曾被美国FBI调查，目前仍在指控中。根据FBI调查，黑客Tillie Kottmann利用的是SonarQube服务的配置失误窃取的相关公司源代码。SonarQube是一款开源代码质量管理的系统，被广泛的应用于相关企业的项目开发流程中，黑客先是扫描了暴露于公网上的SonarQube资产，它们通常默认使用9000端口，再利用预设的管理员账户（如用户名为admin，密码也是admin）登录来窃取源代码。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PribQZZr3baEud6mprfOR3yzp2iamVqGd9l0ynKsicVzQDL6uEl1OGzl7cgkyiciaSdlFzVulyGum3xanQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

2021年，360已经发现ATW组织利用瑞典黑客Tillie Kottmann被公开的手法，开始针对中国暴露在互联网上运行SonarQube、Gogs、GitLab、Gitblit等源代码扫描、管理服务的资产实施了入侵。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PribQZZr3baEud6mprfOR3yzAGt6RicnWTHw9llZTl0sR75RmOJJUXBicmFaQJwic26ibzAshHhU3m13mg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## **ATW攻击活动追溯还原**

2021年10月，ATW在RaidForum（国外知名的数据贩卖论坛）上首次亮相，一直到2022年8月期间，ATW持续针对中国企业和组织机构发起了大规模攻击活动。

2021年10月14日，ATW组织在RaidForums论坛发布了第一起攻击事件的帖子，其公开表示经过2个月的努力获得了某银行的内部资产，主要包含某银行部署的所有项目软件的源代码。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PribQZZr3baEud6mprfOR3yz7lKQjJkn4I4nXzAcnM9sUjSeCRLqAX5ibCTXSF1KqxvjekvNbp3C2ag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

ATW在帖子中展示了被黑项目的截图，通过分析我们发现这是SonarQube系统扫描代码的一个展示页面，攻击者疑似是攻陷了相关单位的SonarQube系统。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PribQZZr3baEud6mprfOR3yzMl5eDd7PLzht65jibBIL9t6PwGzDOtzvLb0xzNg5dN3Pmdxrrcia0IIA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

那到底是不是某银行的SonarQube资产被黑呢？通过360数字安全大脑我们进行了进一步的追溯，在圈定全网三千多台SonarQube资产进行分析后，我们第一时间就追踪到了ATW攻陷的SonarQube资产，并发现该资产与ATW描述一致，相关资产在被黑前曾在公网暴露。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PribQZZr3baEud6mprfOR3yzQYqtXdCts9vLlqMXUT4IFg3icx3bxJjsUAgTM37ibIlcpXVCnVMTzfYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

对这个SonarQube资产进一步分析，我们发现这是一家金融行业信息化建设服务供应商的资产。ATW攻陷的是某银行的第三方供应商，而非银行官方。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PribQZZr3baEud6mprfOR3yz5t145mOsdeYWvCOAGxvcBq5gboMbMyPl9705KiakkaFcpNSzibY8vIdw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

也就是说ATW并没有在实质上渗透进入我金融系统，但是通过披露出来的截图，让公众产生误解。

除SonarQube服务外，接下来还有大量的Gogs、GitLab、Gitblit等源代码管理服务存在相似漏洞被ATW利用。如ATW在俄乌战争期间，在Twitter发布了多个中国重要组织机构的源代码被黑页面。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PribQZZr3baEud6mprfOR3yzaUOjWj85NicWh4zZJrBMo2rk3jicSRftUxp3bGvAzgIaiaDLNktbIPwmw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在ATW持续一整年的攻击活动中，ATW组织在RaidForum（国外知名的数据贩卖论坛）、Twitter网站和Telegram频道中至少发布了七十多起针对中国企事业单位的入侵事件，营造出我国行业的供应链安全有重大隐患的氛围，但是并不是所有公开的入侵事件，都是成功的，但是通过不断的宣传，给相关组织机构的声誉造成了恶劣影响。

**小结**

随着数字技术的不断发展，新型攻击手段层出不穷。我们可以发现，ATW组织多采用撒网式攻击，手段并不高超，但其实施攻击后，会抓住裂缝肆意渲染严重性，扩大其影响力。

但是，在当前日益严峻的国际安全形势和不可避免的数字经济内在安全风险双重挑战下，ATW大量的数据泄露事件也的确突显出了行业的供应链安全问题。一些第三方供应商的安全防护过于薄弱，对于代码的品质、来源及应用部署的安全都没有给予足够的关注和重视，大大增加了相关企事业单位的风险暴露面，导致被不法分子乘虚而入，造成了严重后果。

一直以来，党中央和国务院高度重视关键信息基础设施的供应链安全。习近平总书记曾经指出“供应链的‘命门’掌握在别人手里，那就好比在别人的墙基上砌房子，再大再漂亮也可能经不起风雨，甚至会不堪一击”。《关键信息基础设施安全保护条例》第十九条明确“运营者应当优先采购安全可信的网络产品和服务；采购网络产品和服务可能影响国家安全的，应当按照国家网络安全规定通过安全审查。”为控制关键信息基础供应链安全风险，国家陆续出台了相关制度，建立并不断完善供应链安全保障体系。

保障关键信息基础设施安全的一个重要方面是确保关键信息基础设施使用的网络产品和服务的供应链安全。网络产品和服务供应链安全风险在当前日趋严峻的网络安全形势下日显突出，一旦出现问题会给关键信息基础设施带来严重危害。为此，广大政企单位应强化外部安全风险管理，并持续构建起以“看见”为核心的数字安全能力体系。只有“看见”攻击才能迅速阻断攻击，在没有造成实质伤害前实现快速“处置”。

**360****高级威胁研究院**

360高级威胁研究院是360数字安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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