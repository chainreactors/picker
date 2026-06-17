---
title: 网络首发 |  福建师范大学许力教授团队：支持属性撤销的多授权方完全适应性安全访问控制方案
url: https://mp.weixin.qq.com/s/R5o8OGVkN3P0PlNkhyb_zg
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:00:29.121224
---

# 网络首发 |  福建师范大学许力教授团队：支持属性撤销的多授权方完全适应性安全访问控制方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Qy9zYUBe8CrOtz7LatVia3UoQA9OJvEcGRxZIjUs0zZJM0jeFVRnU4weU43CdLJjPWBiaOOwcsPpkCTkJqJzxhXg9GskW4WYqfbDp6MxFYNgM/0?wx_fmt=jpeg)

# 网络首发 | 福建师范大学许力教授团队：支持属性撤销的多授权方完全适应性安全访问控制方案

网络空间安全科学学报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**引用**

左雨庭, 许力, 李继国, 等. 支持属性撤销的多授权方完全适应性安全访问控制方案[J/OL]. 网络空间安全科学学报, 2026. https://doi.org/10.20172/j.issn.2097-3136.260625.

Zuo Yuting, Xu Li, Li Jiguo, et al. Multi-authority fully-adaptively secure access control scheme with attribute revocation[J/OL]. Journal of Cybersecurity, 2026. https://doi.org/10.20172/j.issn.2097-3136.260625.

**1.背景**

在智能互联的数字化时代，基于数据的服务逐渐成为推动科技发展和社会进步的重要组成部分。在跨域协作场景下，不同组织机构间的数据流通与价值释放面临严峻挑战，数据共享过程中的安全访问控制问题日益凸显；此外，在现实的动态变化的跨域数据共享场景中，不同地域、不同管理主体的组织机构中用户的属性一般由多个权威机构颁发认证，多授权方属性基加密方案（multi-authority attribute based encryption, MA-ABE）成为支持多机构协作与细粒度数据安全访问控制的关键技术。

然而，动态变化的现实环境带来两个关键挑战，一方面，由于现实因素，如企业利益、黑客攻击等问题，一些AA主动与DR合谋并泄露密钥，或者某些DR窃取部分AA管理的密钥，从而影响方案的安全性。另一方面，现实场景的DR的属性会随着时间和空间的变化而更改，设计高效属性撤销的MA-ABE方案势在必行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qy9zYUBe8CqV5exDIc46YJ06hLJ4rMwV5Gb9by0FeCU91FHyLKztSTNZBDBGOK6tibHHfsVDibDname2KlWHBV7lAYN4sIydjULvKN5a4MQnI/640?wx_fmt=png&from=appmsg)

**2.本文贡献**

为此，本文提出支持属性撤销的多授权方完全适应性安全访问控制（multi-authority fully-adaptively secure access control scheme with attribute revocation, MFSAC-AR）方案。主要贡献如下：

1）提出多授权方协作的撤销参数管理机制。首先在系统设置阶段设计撤销参数，并在撤销阶段设计系统更新算法实现多授权方协作的撤销参数更新。防止泄密的授权方私自更新参数和用户属性密钥。

2）提出基于撤销参数的高效灵活的用户密钥更新算法。根据功能划分密钥撤销组件以避免撤销阶段更新全部密钥，提升密钥更新的性能；该算法支持属性新增、属性更新、属性删除，实现了完全适应性安全前提下的灵活属性撤销。

3）为保障前后向安全，将撤销参数嵌入密文更新阶段。为降低密文更新引发的计算开销，提出轻量级密文更新机制，使得密文更新仅执行一次配对运算和一次乘法运算，更新开销不受访问策略复杂度影响。

4）安全性证明表明MFSAC-AR方案满足完全适应性安全。通过理论分析与实验对比进行性能评估。结果表明方案在撤销阶段具有高效性；密钥撤销计算开销约为对比方案的25%，密文更新计算开销为常数级。

![](https://mmbiz.qpic.cn/mmbiz_png/Qy9zYUBe8CrMjib9MALOSXMUH9H3DkO0b1loaEFw0zILRTpj9bHpGEY3XZTWW6kbUwjQic4F1YMYyAvt7hQzDwbZKfapMjJpug2DiahNFXWJW8/640?wx_fmt=png&from=appmsg)

**3.系统架构**

为实现支持属性撤销的多授权方完全适应性安全访问控制（MFSAC-AR）方案，设计如图 1 所示的系统架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qy9zYUBe8CpbmTy91BvQPG4hE4DKSOibUPmwzAHu7LzKed0klEuMNzrSjAwPopaMxicgDU9ayYvSfF0ovYFSic1w1tkGVmCYG5RjtDaWQJcdoQ/640?wx_fmt=png&from=appmsg)

图1  MFSAC-AR的系统架构

Fig.1  System architecture of MFSAC-AR

系统架构中涉及如下三类实体：属性授权方（AA）、数据拥有者（DO）和数据请求者（DR）。

**属性授权方：**有多个属性授权方，在系统设置阶段生成全局参数，在密钥生成阶段为数据请求者DR颁发属性和密钥；在撤销阶段更新撤销参数，为数据请求者DR更新属性和密钥。

**数据拥有者：**设置访问策略并加密数据，生成并秘密保存密文更新组件，在撤销阶段使用更新密文。

**数据请求者：**提供自己的身份信息并获得由AA颁发和更新的属性密钥。在解密阶段利用自己的属性密钥解密DO加密的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/Qy9zYUBe8CpJH6KrtTYFSmN5yYfEqJGJCaLyg34cgNGk1LDCIFkR33o9JWeuuwUia8FlxxoykCcltZq4tribgZP39GC2HxoOsE45fF42oWhYo/640?wx_fmt=png&from=appmsg)

**4.方案阶段**

方案包含如下关键阶段：

**4.1 系统设置阶段**

在该阶段中，所有属性授权方AA产生全局参数和全局属性私钥。

**4.2 用户注册阶段**

在该阶段中，AA根据数据请求者DR的身份信息为其分配属性集并产生初始属性密钥。

**4.3 加密阶段**

在该阶段中，数据拥有者DO设置 LSSS 访问策略并加密数据产生初始密文和密文更新组件。

**4.4 撤销阶段**

在该阶段中，AA更新撤销参数并根据实际情况更新DR的属性及密钥。DO同步更新密文。

**4.5 解密阶段**

在该阶段中，DR用自己的最新属性密钥解密密文，如果DR的属性集满足访问策略，那么解密成功获得数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qy9zYUBe8CpSMTiaQ4ibzfCEXPBSO4yPs5Xzu6ro6NOv90LKo4s3l2a7XdUVmfwgQibjsngn9bm4b8oxnH5oZGKQHZoBBGgricf1zyQ7RntxK6o/640?wx_fmt=png&from=appmsg)

**总结与展望**

本文针对MA-ABE方案的部分密钥泄露问题和用户属性撤销问题，提出了支持属性撤销的多授权方适应性安全访问控制（MFSAC-AR）方案，在确保完全适应性安全的基础上，设计撤销参数并设计高效的属性更新算法，实现了灵活的多授权方属性撤销。为保障前后向安全，本文设计密文更新组件并提出了轻量级密文更新机制。安全性证明表明MFSAC-AR方案满足完全适应性安全。最后对方案进行理论分析和实验对比。结果表明MFSAC-AR方案在撤销阶段具有高效性。

未来，将针对合数阶群方案存在的参数长度长，运算开销大的问题，进一步基于素数阶群构造满足完全适应性安全的可撤销多授权方访问控制方案，并结合可验证外包计算技术，提升方案的实用性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qy9zYUBe8Cot44AYdIVODAiaibPxMxDibJrERUdibKCicWTXYR2ia2nmic0wqHdALRFiczkaK8j9mq13suXoSCnypYcblVe5qDuwUpicVwEBEicBSFK80/640?wx_fmt=png&from=appmsg)

**论文全文下载方式**

1 识别下方二维码；2 点击文末“阅读原文”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Qy9zYUBe8CqmQ1rclSjWpkGbmc2DOTTdKBNqudxyoiavnsralG2aeq4y2e9FrnwLqW8k2HribGdVrib4146gfnibaY4AiaGV1SPLs50OJZ19KOEA/640?wx_fmt=png&from=appmsg)

来源：《网络空间安全科学学报》

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxCkTcfcpQW10RBaTfPBnUVbp9Jk2IHuePBhxXQ3E40s5hUaQibnp2Qiav2IdYYTxria4cBoArYcWOspQ/640?wx_fmt=png)

《网络空间安全科学学报》由中国航天科技集团有限公司主管、 中国航天系统科学与工程研究院主办，双月刊，国内外公开发行（CN 10-1901/TP，ISSN 2097-3136），入选中国科学引文数据库（CSCD）核心库、《信息通信领域高质量科技期刊分级目录》T2级。办刊宗旨为“搭建网络空间安全领域学术研究交流平台，传播学术思想与理论，展示科学研究、创新技术与应用成果，助力网络空间安全学科建设，为网络强国建设提供坚实支撑与服务”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bpXMCVmmaxCkTcfcpQW10RBaTfPBnUVbpH7OESyiayAb2icdRqR7YHbCACAybEjpJD8NFTOxw06LzqbQNS7Uxmtw/640?wx_fmt=jpeg)

网站：http://www.journalofcybersec.cn

电话：010-89061756

邮箱：wlkjaqkxxb@caasse.cn

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