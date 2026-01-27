---
title: 学术前沿 | 西安交通大学蔺琛皓教授团队：跨场景下基于人机交互行为的儿童识别技术
url: https://mp.weixin.qq.com/s/f3yyI0YTExVcLsOFj-rvdQ
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:36:35.241884
---

# 学术前沿 | 西安交通大学蔺琛皓教授团队：跨场景下基于人机交互行为的儿童识别技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjd9bSJdZ596IeSSAViacQkYFT4dNWZfKIGe1LuCY5A7NnCqhUn1A4IJSQ/0?wx_fmt=jpeg)

# 学术前沿 | 西安交通大学蔺琛皓教授团队：跨场景下基于人机交互行为的儿童识别技术

网络空间安全科学学报

![]()

在小说阅读器中沉浸阅读

**引用**

赵竣毅，高书馨，宋天乐，等.跨场景下基于人机交互行为的儿童识别技术[J].网络空间安全科学学报，2025，3（4）：43 - 52. https://doi.org/10.20172/j.issn.2097-3136.250404.

ZHAO J Y，GAO S X，SONG T L，et al. Cross-scenario child recognition technology based on human-computer interactionbe-havior[J]. Journal of Cybersecurity，2025，3（4）： 43 - 52.

https://doi.org/10.20172/j.issn.2097-3136.250404.

**背  景**

移动智能终端普及，我国 10.07 亿手机用户中未成年人占比 12%。未成年人沉迷手机、大额游戏充值、误操作泄露信息等问题突出，现有的身份验证机制容易被未成年人通过冒用家长身份信息绕过，而面部、声音识别存在隐私泄露风险。基于人机交互行为的识别技术，凭借隐式特征优势成为解决方案，却受限于单一场景和小数据规模，难以适配真实使用场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjdh4HSbbqiaEcMSHyldHm1HZXMbiaueHamBc3OxH2uicWWyNYqjngwx7n6A/640?wx_fmt=png&from=appmsg)

**01**

针对传统研究依赖实验室固定任务、数据脱离真实场景的问题，我们自主开发Java SDK工具包，后台无感采集非敏感数据。招募4989名3-55岁用户，涵盖自由场景（抖音、淘宝等）和游戏场景（5类主流游戏），收集触屏坐标、加速度计数据等，经异常值过滤、多指触摸分离预处理，构建大规模真实数据集，为模型训练奠定基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjdh4HSbbqiaEcMSHyldHm1HZXMbiaueHamBc3OxH2uicWWyNYqjngwx7n6A/640?wx_fmt=png&from=appmsg)

**02**

针对原始数据区分度低、机型分辨率差异影响的问题，本研究提取184维高维特征，涵盖滑动速度、姿态角、传感器数据统计值等，同时将触摸坐标统一缩放至1080P，消除设备差异。这些特征从物理意义和数学统计角度，全面捕捉成人与未成年人交互行为的本质区别，为精准识别提供核心支撑。提取的特征如表1所示。

表1 特征提取信息

Table 1 Feature information

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjdvGSZeoJ5VvHnRXJEyEQUSeZF4a56miacJRibLvYwaibiaJicibZgfVebibydQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjdh4HSbbqiaEcMSHyldHm1HZXMbiaueHamBc3OxH2uicWWyNYqjngwx7n6A/640?wx_fmt=png&from=appmsg)

**03**

针对同一群体在不同场景下行为差异大、模型泛化能力弱的问题，本研究采用 PLE 多塔神经网络，将年龄段与场景识别作为联合任务。通过共享底层参数、门控单元融合信息，利用二元交叉熵损失函数优化，借助场景信息辅助年龄识别，降低过拟合风险，显著提升跨场景识别精度。模型结构图如图1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjdDeIAwHvJAOvYYqb4qlCibN8zufb1FeJvaB8vmzyayvCncTnX4zSGt1g/640?wx_fmt=png&from=appmsg)

图1  网络结构图

Fig.1 Network structure diagram

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjdh4HSbbqiaEcMSHyldHm1HZXMbiaueHamBc3OxH2uicWWyNYqjngwx7n6A/640?wx_fmt=png&from=appmsg)

**总结**

本研究实现了无需采集敏感信息、兼具安全性与实用性的跨场景未成年人识别方案，突破了传统研究的场景单一、数据失真等局限，为未成年人防沉迷、网络安全防护提供了高效技术路径。未来，将针对部分未成年人行为趋同成人的问题优化特征与模型，排除生理、环境等干扰因素提升鲁棒性，扩展场景标签至更多领域，推动技术广泛落地，构建全方位未成年人网络安全防护体系，守护未成年人健康使用智能设备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjdh4HSbbqiaEcMSHyldHm1HZXMbiaueHamBc3OxH2uicWWyNYqjngwx7n6A/640?wx_fmt=png&from=appmsg)

**论文全文下载方式**

1 识别下方二维码；2 点击文末“阅读原文”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxDmic9h0uTOK5u0PyHdiawHjd4FMwEICXRVnt88PnyFErzJmb9TIp3MTFwKsBe7dib2j7bewZnI0OHgw/640?wx_fmt=png&from=appmsg)

来源：《网络空间安全科学学报》2025年第四期

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxCkTcfcpQW10RBaTfPBnUVbp9Jk2IHuePBhxXQ3E40s5hUaQibnp2Qiav2IdYYTxria4cBoArYcWOspQ/640?wx_fmt=png)

《网络空间安全科学学报》由中国航天科技集团有限公司主管、 中国航天系统科学与工程研究院主办，双月刊，国内外公开发行（CN 10-1901/TP，ISSN 2097-3136），入选中国科学引文数据库（CSCD）核心库、《信息通信领域高质量科技期刊分级目录》T2级。办刊宗旨为“搭建网络空间安全领域学术研究交流平台，传播学术思想与理论，展示科学研究、创新技术与应用成果，助力网络空间安全学科建设，为网络强国建设提供坚实支撑与服务”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bpXMCVmmaxCkTcfcpQW10RBaTfPBnUVbpH7OESyiayAb2icdRqR7YHbCACAybEjpJD8NFTOxw06LzqbQNS7Uxmtw/640?wx_fmt=jpeg)

网站：www.journalofcybersec.com

电话：010-89061756/ 89061778

邮箱：wlkjaqkxxb@spacechina.com

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxA5UN8DNQAriaCeMRY5VHUlR4LtqP4uyVIiabYrqUNyHap5IW3ZQ41pv2Q9icgHjMoXO5IdiahpZmtibicQ/0?wx_fmt=png)

网络空间安全科学学报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxA5UN8DNQAriaCeMRY5VHUlR4LtqP4uyVIiabYrqUNyHap5IW3ZQ41pv2Q9icgHjMoXO5IdiahpZmtibicQ/0?wx_fmt=png)

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