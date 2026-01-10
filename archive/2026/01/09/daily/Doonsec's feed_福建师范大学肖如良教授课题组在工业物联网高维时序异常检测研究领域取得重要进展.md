---
title: 福建师范大学肖如良教授课题组在工业物联网高维时序异常检测研究领域取得重要进展
url: https://mp.weixin.qq.com/s/esVGYMLH8Uhjuz_Cm1fsyw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:24:51.606500
---

# 福建师范大学肖如良教授课题组在工业物联网高维时序异常检测研究领域取得重要进展

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN8B9yMgPgVvj87RZHfJ92zrNWNxoBBFuLxOuiaWvCmWRDIrUaImaygN2UV0CYegIXpNKeIg7Sfra4A/0?wx_fmt=jpeg)

# 福建师范大学肖如良教授课题组在工业物联网高维时序异常检测研究领域取得重要进展

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

随着工业物联网特别是新能源产业的迅猛发展，海量高维时序数据已成为工业物联网特别是储能领域等关键设施的核心数据形态，其异常检测应用研究越来越具挑战性。真实工业数据呈现出的强非线性耦合、动态跨尺度演化及高噪声特性，使现有异常检测方法因缺乏物理先验与因果逻辑而常陷于误判困境。如何突破现有模型在时空依赖建模与隐性故障溯源方面的局限，成为当前提升工业物联网系统应用可靠性亟待攻克的共性难题。

近日，福建师范大学肖如良教授课题组在工业物联网高维多变量时间序列异常检测方向取得了系列性进展。课题组研究聚焦于复杂工业场景下高维时序数据的时空依赖挖掘与抗噪表征，综合运用了双视图潜变量建模、因果反事实推理以及跨尺度频域交互等方法，旨在面向工业物联网环境特别是真实新能源应用领域，攻克非线性耦合与隐性故障溯源难题，实现兼具物理一致性、高鲁棒性与深层可解释性的智能异常检测。

研究成果一：针对储能系统在电动汽车、光伏、风电等场景中的异常检测困难问题，提出了面向多传感器电池系统的双视图潜变量异常检测方法 DVSAD，以应对高维传感器数据下的安全监测需求。该方法将传感器关系图与时间序列特征融合建模，并结合扩散噪声平滑与物理先验驱动的结构引导评分，以增强对跨传感器耦合与噪声扰动的识别能力。实验结果显示，该方法在 F1 和 AUC 等指标上均取得明显提升，对电-热耦合异常等隐性故障具有更高敏感度。该成果以“Unsupervised Anomaly Detection in Energy Storage Systems using Dual-View Latent Variable Modeling”为题，发表在国际知名期刊《Engineering Applications of Artificial Intelligence》上，该期刊属于中科院一区TOP期刊，2025年最新影响因子为8.0。

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8B9yMgPgVvj87RZHfJ92zrAjhoAQwSQGnk2hxPibmm1kN4YTzLsOicU1aNLdc4TSAwAYWhgyicjWpZg/640?wx_fmt=png&from=appmsg)

图1. DVSAD框架的示意图

原文链接：https://doi.org/10.1016/j.engappai.2025.112958

研究成果二：针对已有无监督多元时间序列异常检测方法难以有效地模拟复杂的时空依赖关系，存在着动态混杂因素干扰异常检测的挑战，提出了基于因果推断的细粒度依赖建模方法 SCID。该方法通过构建动态因果表示编码器，利用反事实干预剥离冗余影响因素，准确识别变量间的即时与延迟因果依赖；并引入预测-重构双掩码机制，将时序演化特征与局部结构特征联合建模，从而实现对复杂时空依赖的精细表征。同时，方法在优化目标中加入因果区分与粒度校正项，以缓解多变量粒度不一致带来的偏差，提高对复杂模式演化下异常信号的敏感度。实验结果显示，SCID 在五个真实数据集上取得领先表现，能够有效识别由隐含因果链条驱动的细粒度异常。该成果以“Fine-grained multivariate time series anomaly detection via causal inference”为题，福建师范大学为第一完成单位，第一作者为我院2023级研究生陈祥炜同学（现为大连理工大学博士研究生）,发表在国际知名期刊《Knowledge-Based Systems》上，该期刊属于中科院一区TOP期刊，2025年最新影响因子为7.6。

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8B9yMgPgVvj87RZHfJ92zrNwCDnW0cWA35Z8n8ZEAIIibiaf3PsFaEUQ8h8RtKkbkHm74lwJlIbOtw/640?wx_fmt=png&from=appmsg)

图2. SCID框架的示意图

原文链接：https://doi.org/10.1016/j.knosys.2025.114765

研究成果三：面对工业物联网新型应用场景中多尺度时序特征与噪声干扰并存的挑战，提出了跨尺度序列关联建模方法 CSCAD，以有效增强多变量时间序列的异常识别能力。

该方法通过跨尺度拼接表示与多尺度交互卷积刻画属性间的深层相关结构，并结合序列异方差特征与注意力机制自适应削弱噪声带来的影响，同时引入自适应激活函数以提升复杂模式的拟合能力。实验结果显示，CSCAD 在五个真实数据集上相较 19 种方法在 F1 与召回率上均取得提升，能够更准确识别跨尺度依赖驱动的细微异常。该成果以“CSCAD: Modeling cross-scale sequence correlations for multivariate time series anomaly detection”为题，发表在国际知名期刊《Information Processing and Management》上，该期刊属于中科院一区TOP期刊，2025年最新影响因子为6.9。

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8B9yMgPgVvj87RZHfJ92zr12A4HI17eLCdRHT4dC6DVkkyrSyVsoO8oubBwhNg2CnvvlTT1tDQQw/640?wx_fmt=png&from=appmsg)

图3. CSCAD框架的示意图

原文链接：https://doi.org/10.1016/j.ipm.2025.104315

上述三项研究成果均由福建师范大学作为第一完成单位完成，第一作者分别为福建师范大学计算机与网络空间安全学院博士研究生邱志鹏、计算机科学与技术专业学硕研究生陈祥炜和软件工程专硕研究生李涵峰，通讯作者均为肖如良教授。该研究得到了国家自然科学基金项目和福建省自然科学基金的支持。

来源：福建师范大学计算机与网络空间安全学院

推荐阅读

[基于正交最速梯度下降法的联邦遗忘学习、基于聚类的联邦学习框架](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247505559&idx=2&sn=d5d68b8f0ef5a2c37142a904516640a6&scene=21#wechat_redirect)

[话还没说完，手机里广告就推送过来了？语音窃听怎么防？数字取证教育部工程研究中心面向移动设备的抗窃听防御工作被CCF](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247513934&idx=2&sn=3253cde0c93622683ca64b0da5541b51&scene=21#wechat_redirect)

[个性化联邦学习：确保数据隐私安全，训练高效人工智能模型](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247507553&idx=2&sn=6a4635fa5b6aad66bf2ea3384ed2a00f&scene=21#wechat_redirect)

[我国首次！清华大学在商用处理器上发现并披露免计时缓存侧信道攻击案例，研究成果被ACM CCS2025接收](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247513933&idx=2&sn=737810768742c63c0aabb6feb054f063&scene=21#wechat_redirect)

推荐阅读

* [“网安+法学”双学位  |  看南开大学、东南大学、重庆邮电大学在新赛道上加速](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247510330&idx=1&sn=bd64a92b644a0d6a411e27ba03c9f443&scene=21#wechat_redirect)跑
* [芯片安全漏洞难检测？看西工大“抽象四次方”如何破解芯片安全难题](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247512474&idx=1&sn=15bbd6c6b570c65774d259b8fb5ec906&scene=21#wechat_redirect)
* [“五色石”计划下，东南大学网络安全人才培养模式创新“密码”揭秘](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247512244&idx=1&sn=de8609b305b719108c3161f3f51a424b&scene=21#wechat_redirect)
* [“实战派”网安人才培养新范式，看上海交通大学、暨南大学、湖南大学如何转变模式锻造网安实战人才](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247511636&idx=1&sn=e09b1b68c337b9f623fe012967fb4c4a&scene=21#wechat_redirect)

* [做研究，读“经典”！看中国科学技术大学、东南大学、南开大学和兰州大学网络空间安全领域青年教师如何挖出让审稿人眼前一亮的新切口](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247512012&idx=1&sn=fa1e7daa07d6aa0afb89de8c4986ed01&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=qnylxjok&tp=webp#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=fbknkhlb&tp=webp#imgIndex=3)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=23elspay&tp=webp#imgIndex=4)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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