---
title: 斩断危害中国数据安全的魔手：揭秘疯狂对华实施数据窃取的ATW组织
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507836&idx=1&sn=9c7906123b93b06805b542fdddcb6c18&chksm=ebfa985cdc8d114a4a8d98e1c3a31658023e629422374312b97937cb93a5fd7132369fc6a5a5&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-02-20
fetch_date: 2025-10-04T07:33:35.464844
---

# 斩断危害中国数据安全的魔手：揭秘疯狂对华实施数据窃取的ATW组织

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7uiafCEcu95Anu5QAVKBqna7P8wibFyubl8Ul6cTtAz00aY3a6vyYFXhktCQpicdXegu0eaTb9zeVppg/0?wx_fmt=jpeg)

# 斩断危害中国数据安全的魔手：揭秘疯狂对华实施数据窃取的ATW组织

安全内参

**关注我们**

**带你读懂网络安全**

**本报告公布ATW黑客组织的攻击手法及使用的漏洞、网络码址，目的是使大家看清ATW组织长期以来针对中国实施网络攻击、数据窃取活动的本质，针对性修补漏洞，做好安全加固，不断提升网络安全、数据安全防护能力水平。**

2021年10月以来，一自称AgainstTheWest（下称“ATW”）的黑客组织，将中国作为主要攻击目标，疯狂实施网络攻击、数据窃取和披露炒作活动，对我国的网络安全、数据安全构成严重危害。ATW组织究竟什么来头？我们该如何应对？让我们来庖丁解牛，见招拆招。

**ATW组织及其主要攻击活动**

ATW组织成立于2021年6月，10月开始在“阵列论坛”（RaidForums）上大肆活动。虽然将帐号个性签名设置为“民族国家组织”，但实际上，这是一个以欧洲、北美地区从事程序员、网络工程师等职业的人员自发组织成立的松散网络组织。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnJUoq5E7d68E1QhvaHeuicT9BOJIiauv5QF2507aUKZjoApibXugcttJZw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
ATW组织自我介绍

ATW组织自成立伊始，便表达了鲜明的反华立场，公开称“将主要针对中国、朝鲜和其他国家发布政府数据泄密帖子”，还专门发布过一篇题为“ATW-对华战争”的帖子，赤裸裸地支持“台独”、鼓噪“港独”、炒作新疆“人权问题”。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnbDSXh7ORJM9Lj0UUHxUja6BmFAhU4X1NEjh1ucEVTfF7mervVJ43Nw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
ATW组织发布的“ATW-对华战争”帖

2021年10月，ATW组织开始频繁活动，不断在电报群组（https://t.me/s/ATW2022，Email:AgainstTheWest@riseup.net，备份Email:apt49@riseup.net）、推特（@\_AgainstTheWest，https://mobile.twitter.com/\_AgainstTheWest）、Breadched（账号：AgainstTheWest）等境外社交平台开设新账号，扩大宣传途径，并表现出较明显的亲美西方政治倾向，多次声明“攻击目标是俄罗斯、白俄罗斯和中国、伊朗、朝鲜”、“愿意与美国、欧盟政府共享所有文件”、“愿受雇于相关机构”。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnOek4f9n2ibibEdubU4mvf87aWV0uJLtRjp9kiaiaJIUlafdJUBLcjFEu6g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
ATW组织群组账号

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnYJCFD3AkZGibBEZQQ0icKxNic5lTic5zSn7sibKmcST9duu5iassJBX6vBcg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
ATW组织推特账号

据不完全统计，自2021年以来，ATW组织披露涉我重要信息系统源代码、数据库等敏感信息70余次，宣称涉及文化和旅游部、海南省政府、山西省司法厅、知名航空公司、城市地铁等100余家单位的300余个信息系统。实际上，所谓泄露的源代码主要是中小型软件开发企业所研发的测试项目代码文件，不包含数据信息。但ATW组织为了博取关注，极尽歪曲解读、夸大其词之能事，动辄使用“大规模监控”、“侵犯人权”、“侵犯隐私”等美西方惯用的“标签”，意图凸显攻击目标和所窃数据重要性，以至于看起来，一个比一个吓人。

◆  2021年10月14日，ATW在“阵列论坛”（RaidForums）发布题为“人民币行动（Operation Renminbi）”的帖子，称“出售中国某银行相关软件项目源代码”。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWne6AMfWEWn18GdGyCxpexzdwWI39MBrSYHW71Z6ia8zNdJfX45a89iaicw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  2021年11月2日，ATW组织在“阵列论坛”发布信息，称“某政企互联科技有限公司已被其攻破”，并提供了数据库和SSH密钥的下载方式。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnC2Jt8xuUNloFLibAiaTTIVLaQO355D2BoWncqH2WBFxerubrMa5RdTbg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  2021年11月24日，ATW组织发布了16个政府网站大数据系统存在漏洞情况，涉及北京、浙江、四川、重庆、广东、江苏、湖北、湖南等地。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnAdCmfgPGoQpibSLlsrsq1K4NBO3fbPUdib7KLrNrVG7x4d1RkjxamE9w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  2022年1月7日，ATW组织声称出售“中国大量政府、非政府组织、机构和公司数据，待售数据涉及102家中国实体单位”。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnPN68lhXCkGbNACcx2MrRhDjDsrosLxNPJaQXw5TtjnjIKhVEcVhic2Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  2022年3月4日，ATW组织宣布解散，但3月5日又宣布经费充足再次上线。

◆  2022年3月6日，ATW在电报群组中发布消息称“攻破了某金融投资公司，窃取了大量数据”，并提供了数据的下载链接。

◆  2022年3月28日，宣称“某银行已被攻破”，发布“整个后端源代码、maven 版本”等数据。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnOSVlguLicuUlON9R7rA3J2bwLDFR5SBiaIYhEF85ny0bPz6SHCaW4I6A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  2022年4月5日，ATW组织发布“中国各省市共计48家医院信息系统源代码”。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWn0S8fLna9qHlLTOkiaPP1X7XzxDLicLickSPNV85OvlVjvbh4zgP0chNbg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  2022年8月12日，ATW组织在推特发布数据售卖帖，称其从某科技公司服务器获取了4000条警察人员的电话号码和姓名数据。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnFsrrp3icAkjwibVxnGkakOy868mAZXl0ftDWiawrcAOuc5bET8BzO2cfw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  2022年8月16日，ATW组织通过Breached黑客论坛公布港铁系统源码文件，内容涉及某铁路公司的交易、排程等26个系统项目代码。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnHcFt9f47F1UPOxP2NEQIIcfZKicNANpbLRsPUbQ8cYKa7reCGQBuyIA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**ATW组织主要成员**

技术团队长期跟踪发现，ATW组织平日活跃成员6名，多从事程序员、网络工程师相关职业，主要位于瑞士、法国、波兰、加拿大等国。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnNXOvrHWNluXmDPc3Ee0FWKYl1V19lAxzQHbsqC38wYXmb65jj7aFaA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

梳理该组织成员活动时段发现，其休息时间为北京时间15时至19时，工作时间集中在北京时间凌晨3时至13时，对应零时区和东1时区的西欧国家。其中，2名骨干成员身份信息如下：

◆蒂莉·考特曼（Tillie Kottmann）

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnicfP5Y8tiayZ52XOLJO6nVrLMtVV5ia8DoI6ot845liczTIlpXmdNCiaoHg/640?wx_fmt=png)

1999年8月7日生于瑞士卢塞恩，自称是黑客、无政府主义者、同性恋，以女性自居。主要学习、工作经历如下：

* 2012—2015年，瑞士Kantonsschule Alpenquai州立中学学习；
* 2015年8月—2019年，瑞士BBZW Sursee思科学院；
* 2017年3月—2020年1月，Lawnchair Launcher公司担任项目负责人兼首席开发人员；
* 2020年2月—8月，德国auticon GmbH公司担任IT顾问；
* 2020年11月至今，瑞士Egon AG公司程序员。蒂莉·考特曼还是Dogbin网站（短链接转换网站）的创始人和首席开发人员。本来专心做技术，这份履历是很漂亮的。只可惜：
* 2020年4月以来，蒂莉·考特曼通过“声呐方块”平台漏洞获取企业信息系统源代码数据；
* 2020年7月，蒂莉·考特曼在互联网上曝光了微软、高通、通用电气、摩托罗拉、任天堂、迪士尼50余家知名企业信息系统源代码；
* 2021年3月12日，瑞士警方搜查蒂莉·考特曼住所并扣押大量网络设备；
* 2021年3月18日，美国司法部发布对蒂莉·考特曼的起诉书，但3月底突然中止该案审理。此后，中国成了蒂莉·考特曼的主要目标之一。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWn6weN4LmONWs5eLe5cU55NLWZsE8pn1kgPbAsztiauKc0b5EeLiaKlPkw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWn63qibFDCO4I7OQE9djzJEmqFTiaAvw8r7WNwSPRndJgZBkMRl5aq6VAQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

美国司法部对蒂莉·考特曼的起诉书及公布照片

蒂莉·考特曼（Tillie Kottmann）的Twitter账号@nyancrimew被推特公司停用后，于2022年2月重新注册使用。个人简介中自称为“被起诉的黑客/安全研究员、艺术家、精神病患者以及同性恋”。2023年1月至今，发布及转推78次。

◆帕韦尔∙杜达（Pawel Duda）

男，波兰人，软件工程师。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnFgSMYfUib4koCn2XBiba6OOyOe2XuIdd01w3Vr4GhyJuruYoFgg5Zj8g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

* 2012年11月—2013年5月，Ageno公司web前端开发工程师。
* 2013年6月—2013年12月，自称从事某保密项目开发，任web前端开发工程师。
* 2014年1月至2015年1月，OX media公司web前端开发工程师；
* 2014年4月至2019年8月，Selleo公司软件工程师，负责开发捐款管理系统、物流服务系统、跨平台办公系统、定制化电子商务平台、酒店管理系统等项目；
* 2016年9月—2017年4月，voicefox公司软件工程师（兼职），负责开发基于Zoom等视频会议解决方案；
* 2019年11月至2020年6月，versum公司软件工程师，负责开发沙龙管理系统；
* 2020年6月至2021年10月，TjeKvik公司软件工程师，负责开发汽车服务管理系统；
* 2021年10月至今，自称参与了某非公开项目。
  该人日常会进行黑客技术研究，并在Slides.com网站共享文件中设置了“成为更好的黑客”的座右铭。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnCphcKVSvQbaDOxoPkmh8XHp2yHe8dXu1V7xiasO4icYs9hiaPibOGqn2uQ/640?wx_fmt=png)

此外，该组织成员长期服用精神类药物、吸食毒品等行为，包括吸食氯胺酮（K粉），还会将莫达非尼（治疗嗜睡的药物，具有成瘾性）和可乐一起服用。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnmQHy2gYiaMuZ7XuDDND0Kzj1McTgMhM6GiawsEVQPWRWX6hU0IbPgFgw/640?wx_fmt=png)

**ATW****组织主要攻击手法**

◆ 攻击部位：调查发现，ATW组织宣称攻击窃取涉我党政机关、科研机构等部位的数据，实则均来源于为我重要单位提供软件开发的中小型信息技术和软件开发企业，窃取数据也多为开发过程中的测试数据。

◆ 攻击手法：主要针对SonarQube、Gogs、Gitblit等开源网络系统存在的技术漏洞实施大规模扫描和攻击，进而通过“拖库”，窃取相关源代码、数据等。相关信息可用于对涉及的网络信息系统实施进一步漏洞挖掘和渗透攻击，属于典型的“供应链”攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWn5uogPdhUskZwZY8B6Im6BTeJjCSOiceGH9FFM6TgTHe3icoNKHcboNuw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)◆ 攻击目的：与自我标榜的“道德黑客”着实相去甚远，并非向存在漏洞的企业发布预警提示信息，以提高这些企业的安全防范能力。相反，更多的是利用这些漏洞实施攻击渗透、窃取数据，并在黑客论坛恣意曝光，炫耀“战果”。2022年以来，ATW组织滋扰势头加剧，持续对中国的网络目标实施大规模网络扫描探测和“供应链”攻击。为凸显攻击目标和所窃数据重要性，多次对所窃数据进行歪曲解读、夸大其词，竭力配合美西方政府为我扣上“网络威权主义”帽子，并大力煽宣、诋毁中国的数据安全治理能力，行径恶劣，气焰嚣张，自我炒作、借机攻击中国的意图十分明显。

**ATW组织漏洞攻击利用情况**

ATW对中国企业单位开展网络攻击过程中，大量使用了源代码管理平台、开源框架等存在的技术漏洞。主要包括：

◆  SonarQube漏洞。漏洞编号为CVE-2020-27986，该漏洞描述为SonarQube系统存在未授权访问漏洞。涉及版本：SnoarQube开源版<=9.1.0.47736；SonarQube稳定版<=8.9.3。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnTXTvmCINY2TlutD6EdWc5xcgR2PiaxAhGGGSg4j6jTd1nm6a84Eicmng/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  VueJs框架漏洞。VueJs框架为JavaScript前端开发框架，VueJS源代码在GitHub发布，同时本身具备较多漏洞，使用网络指纹嗅探系统可直接扫描探测，GitHub上同样存在专门针对VueJS的漏洞利用工具。

![](https://mmbiz.qpic.cn/mmbiz_png/wYob7eh43WbL8TjCMNNIRb4h9FChUhWnicIHoV7tOFUr8OEm369shsdNJTjNjfOPNKZ9AImF5uaaWxghfCCqOibA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

◆  Gogs、GitLab、Gitblit等其他源代码管理平台漏洞。上述平台存在的未授权访问漏洞，无需特殊权限即可访问和下载存储在管理平台上的系统源代码数据。

通过对全网设备进行空间测绘，发现上述开源平台在国内使用广泛。对存在风险的资产项目进行进一步分析发现，其中包含涉及我国多家重要单位的系统源代码。SonarQube、Gitblit、Gogs的各平台使用情况如下：

![](https...