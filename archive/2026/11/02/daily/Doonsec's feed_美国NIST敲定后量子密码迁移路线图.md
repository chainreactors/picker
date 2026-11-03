---
title: 美国NIST敲定后量子密码迁移路线图
url: https://mp.weixin.qq.com/s/PfD7B7ivS6YMQwLsOIsV2Q
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:44:53.133853
---

# 美国NIST敲定后量子密码迁移路线图

# 美国NIST敲定后量子密码迁移路线图

信息安全最新论文技术交流

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

10月27日，美国国家标准与技术研究院（NIST）发布《Transition to Post-Quantum Cryptography Standards》（最终版），正式敲定后量子密码（PQC）迁移路线图，明确联邦机构应逐步淘汰易受量子计算攻击的公钥密码算法。根据现行要求，联邦高价值资产、高影响系统及其他存储高度敏感数据的系统，须在2030年12月31日前采用抗量子方法建立共享密钥，并在2031年12月31日前完成数字签名相关升级；联邦系统整体迁移目标仍为2035年。NIST计划2030年后逐步弃用易受量子攻击的公钥密码算法，并于2035年后依据相关标准和指南禁止使用。

**时间线锁定**　2030 年 12 月 31 日（密钥建立）、2031 年 12 月 31 日（数字签名）、2035 年（全面禁止）。

**弃用范围扩大**　草案只涉及 112 位参数集，最终版把 128 位以上的 P-256、RSA-3072、Ed25519 一并纳入 2030 年弃用名单。

**混合方案保留**　只要组合中有一个输入来自批准方案，即使另一路用的是被禁算法，仍可通过 FIPS 140 验证。

**默认参数确定**　ML-KEM-768 成为密钥封装的默认选择，HQC 作为结构独立的备份，NIST 不再遴选新的 KEM。

## 01三个日期

报告要求，联邦高价值资产、高影响系统以及其他存储高度敏感数据的系统，须在 **2030 年 12 月 31 日**前采用抗量子方法完成共享密钥建立，**2031 年 12 月 31 日**前完成数字签名升级。联邦系统整体迁移的目标仍定在 **2035 年**。

所有易受量子攻击的公钥算法，**2030 年后进入“弃用”（deprecated）状态，2035 年后“禁止使用”（disallowed）**。

---

## 02128 位不再豁免

2024 年 11 月的草案里，2030 年后被弃用的仅限 112 位安全强度——RSA-2048、P-224 这一类。P-256、RSA-3072、Ed25519 等 128 位及以上的参数集，可以一直使用到 2035 年被禁止。

RSA 与 ECDSA 签名（112 位以上）、EdDSA（128 位以上）、Diffie-Hellman、MQV 与 RSA 密钥建立（112 位以上），**全部在 2030 年后弃用，2035 年后禁止**。

---

## 03混合方案

SP 800-56C 中的复合技术**即使其中一个输入来自不被批准的来源、包括已被禁止使用的算法，依然被允许**。只要组合中至少有一个输入来自批准方案——例如 ML-KEM——整个组合仍能通过 FIPS 140 验证。NIST 同时表示将修订 SP 800-56C，使两个共享密钥的排列顺序不再受限。

**资料来源**　NIST IR 8547《Transition to Post-Quantum Cryptography Standards》最终版（2026 年 10 月 27 日）

[冯登国院士：面向人工智能的密码学未来发展思考](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491424&idx=1&sn=d9e91967ec7091970d84000e5fd2ccf7&scene=21#wechat_redirect)

[郑建华院士: “密码定义安全”的思考与愿景](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492206&idx=1&sn=402fe11a89c1c483c3f3b397e9fab2da&scene=21#wechat_redirect)

[王建华院士：信息技术变革对密码技术发展的思考](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492195&idx=1&sn=0e1e060e546142ea50ece9312d8c137a&scene=21#wechat_redirect)

[密码学大模型：玄知大模型V4发布](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492210&idx=1&sn=2cd0d92f186ee2ac4be61fdf94842236&scene=21#wechat_redirect)

[ACM CCS 26第一轮录用论文列表](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492220&idx=1&sn=6a1bee863e0c2799a603c4409a62bf08&scene=21#wechat_redirect)

[中央网信办：当前人工智能领域主要面临5方面安全风险挑战](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492214&idx=1&sn=c8971df05b7cbed7fd1ef7c86d3a9c27&scene=21#wechat_redirect)

[CCF A网络安全/软件工程顶会中的Agent安全](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492183&idx=1&sn=db7f15edd495a82b6ca8be17b4e99867&scene=21#wechat_redirect)

[2025年国家最高科学技术奖揭晓](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492174&idx=1&sn=72dcf8363725751dbdb7e04b07c887ac&scene=21#wechat_redirect)

[中国科协 | 2026重大科学问题、工程技术难题和产业技术问题](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492178&idx=1&sn=3cc7d6e128f39b8bce6b852850f0864a&scene=21#wechat_redirect)

[4月9日勘误-CCF推荐国际学术会议和期刊目录(第七版)](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492161&idx=1&sn=f0ecc60d761a803620afe3f5b99d91ba&scene=21#wechat_redirect)

[李国杰院士：基于可判定性理论的人工智能系统安全风险分类](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492073&idx=1&sn=1307cf8825ac2e8dab2388c06752e698&scene=21#wechat_redirect)

[2026年国家自然科学基金安全领域部分题目列表](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492040&idx=1&sn=effeeb813e13f974d9622c88f9fc4deb&scene=21#wechat_redirect)

[冯登国院士：网络空间安全未来发展思考](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491433&idx=1&sn=645bb18036b15c5248ad58ec8dccbbf7&scene=21#wechat_redirect)

[USENIX Sec 2025：大模型越狱防御框架——JBShield](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491432&idx=1&sn=268c0cc1f7f3a59bd9d88c8a3ea53e7e&scene=21#wechat_redirect)

[2025年国家自然科学基金安全领域部分题目](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491411&idx=1&sn=56b1abaffc94f3ebf50ee7a88957ce5d&scene=21#wechat_redirect)

[NIST发布首批3项抗量子密码标准](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491348&idx=1&sn=7b716a864df153c15dd95ddf256f1374&chksm=eaa4f6f3ddd37fe5d85af81235f951d528a42dd160475af9e898a425cbb272d075933226855d&scene=21#wechat_redirect)

[IEEE：后量子密码学之路](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491341&idx=1&sn=54f9fae066a314b8ecdd46ce037621c0&chksm=eaa4f6eaddd37ffcff4629d5e5c1851b67a176e0a1665f367432aa72f8b08d075327ae5a9bc7&scene=21#wechat_redirect)

[NIST抗量子密码算法被爆安全漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247490518&idx=1&sn=4bac214c6c6e81a716c52d41f1cd6069&chksm=eaa4f231ddd37b27e4707250a16d72575726a05230fa67e42663bf644f0959374032a8ecf85a&scene=21#wechat_redirect)

[吴世忠院士：对生成式AI安全研究的九点观察](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491330&idx=1&sn=c4c90f77663ee68f77c575226c6e630b&chksm=eaa4f6e5ddd37ff30f77a1d23e19c1edc872c9ffc137438c92277cc5313efc97ad7571aecca3&scene=21#wechat_redirect)

[去中心化联邦学习：安全和隐私综述](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491279&idx=1&sn=a31c1832715905964546cc7f19a56486&chksm=eaa4f728ddd37e3e9de963a50ffa3b875066ca5a2893b532fe6be11b423208c39da804fd94b7&scene=21#wechat_redirect)

[针对大语言模型LLM的对抗](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247490929&idx=1&sn=e0de9cc63dd68812486688f433a4a31f&chksm=eaa4f496ddd37d80fb934f98bea6bb8bc1fbc7f74b4111e80a5973311fbfde3a18e86e58ed00&scene=21#wechat_redirect)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DNNc17Q6tdY06v6DeniaSPLvNv6To7Cxsud5WSjM7lbZZGqlhb3U32c7mUqRyjVUcPqrCQcmoEw2oXicIgg2wV2A/0?wx_fmt=png)

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