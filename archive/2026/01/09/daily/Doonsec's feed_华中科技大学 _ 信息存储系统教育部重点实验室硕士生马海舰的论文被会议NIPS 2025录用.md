---
title: 华中科技大学 | 信息存储系统教育部重点实验室硕士生马海舰的论文被会议NIPS 2025录用
url: https://mp.weixin.qq.com/s/r8FPMIokBZ-kQq6fNpWcwg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:24:54.052522
---

# 华中科技大学 | 信息存储系统教育部重点实验室硕士生马海舰的论文被会议NIPS 2025录用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN8B9yMgPgVvj87RZHfJ92zrHxtgouibP9wpPglklF79XTibodGnR5nnCpkrayYqWiaLxice92rBpxCvPw/0?wx_fmt=jpeg)

# 华中科技大学 | 信息存储系统教育部重点实验室硕士生马海舰的论文被会议NIPS 2025录用

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

在多模态大语言模型（MLLMs）广泛应用于图像理解、视觉问答等领域的当下，其安全漏洞问题愈发突出。现有对抗攻击方法多针对特定图像 - 提示对优化，存在泛化能力弱、迁移性差等缺陷，难以应对真实场景中多样化的输入组合。近日，一项受国家自然科学基金（No.62476107）支持的创新性研究，提出基于分布逼近理论的跨图像 / 提示对抗攻击方法，成功实现对主流多模态大模型的高效通用攻击，为大模型安全防护体系建设提供了重要参考。

该研究成果以 “Fit the Distribution: Cross-Image/Prompt Adversarial Attacks on Multimodal Large Language Models” 为题，已被国际顶级学术会议 NeurIPS 2025（CCF A 类）接收。研究团队通过全新视角破解传统攻击瓶颈，提出将图像与提示的输入分布建模为高斯分布，生成单一通用的对抗扰动，实现对未见图像和提示的有效迁移攻击。

传统对抗攻击方法往往过度拟合特定训练样本，导致换用新的图像或提示时攻击失效，且需为每个输入组合单独优化扰动，资源消耗巨大。而该研究提出的分布驱动攻击框架，核心创新在于三点：一是采用拉普拉斯逼近技术，将复杂的图像和提示输入分布建模为可计算的高斯分布，精准估计均值和协方差参数；二是通过蒙特卡洛采样机制，从建模分布中抽取多样化图像 - 提示对，优化得到与分布拟合的输入无关扰动；三是针对图像无关和图像相关两类提示分别建模，通过高斯混合模型融合为统一分布，覆盖全场景提示类型。

严苛的实验验证显示，该方法表现卓越：在 MS-COCO 和 DALLE-3 两大数据集上，针对 LLaVA1.5、BLIP-2、MiniGPT-4 等主流模型，跨图像攻击成功率最高达 71.9%，跨提示攻击成功率最高达 97.9%，跨图像 - 提示联合攻击成功率最高达 57.9%，均远超现有 PGD、CroPA 等基准方法；即使面对随机化、JPEG 压缩等防御机制，仍保持优异的攻击稳定性；针对不同长度和复杂度的目标文本，以及跨数据集、跨模型场景，均展现出强大的适配能力，生成的扰动具有极强的通用性。

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8B9yMgPgVvj87RZHfJ92zrjny0iaHsYOo9dHynD4Top4Sc9jefUYS55ukiaxZX8diaSmDvZRxFpvKFQ/640?wx_fmt=png&from=appmsg)

图1 整体架构图

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8B9yMgPgVvj87RZHfJ92zrolTNtonUIjmWFJacuKNdBUgnbKwubmXv1OWHzr2STC19WiayT3q7PjA/640?wx_fmt=png&from=appmsg)

图2 攻击效果

来源：信息存储系统教育部重点实验室

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