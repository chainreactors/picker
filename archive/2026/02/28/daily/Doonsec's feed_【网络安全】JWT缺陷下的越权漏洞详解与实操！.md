---
title: 【网络安全】JWT缺陷下的越权漏洞详解与实操！
url: https://mp.weixin.qq.com/s/8x7MOh0_uYhjltHgD985xA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:22:54.384463
---

# 【网络安全】JWT缺陷下的越权漏洞详解与实操！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SgRVa0DmgbFqDAVx13dNVxYLWDfZWf6X9KKMZuoWTKSSvJgfcoonZxP474ic69NibwCMouUdtQcecIiaq45UNdtUznwd2QCGZldic46urAcOAKM/0?wx_fmt=jpeg)

# 【网络安全】JWT缺陷下的越权漏洞详解与实操！

原创

無名
無名

无名的安全小屋

![]()

在小说阅读器中沉浸阅读

01

**前置知识点**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SgRVa0DmgbGfR9XImqWKmCUrf4ibsECQniaIxLAnGxlib8XlOHjQV3VqL10moxQ8sf3v3oQAaIzmVQcickicibZuXe0DQuRicyBiaFFZopEAg7Ngobg/640?wx_fmt=jpeg)

Authorization值为JWT（JSON Web Token）格式，采用Base64URL编码而非加密，由三部分通过点号连接：Header（声明算法HS256）、Payload（明文存储用户ID、权限类型等数据）和Signature（使用密钥对前两部分签名）。

攻击者可轻易解码前两部分修改内容，若持有密钥还可重新签名伪造；真正的防护需改用RS256非对称算法配合AES加密敏感字段，使客户端无法解析也无法伪造。

JWT令牌篡改与客户端权限提升漏洞是一种利用服务端对JWT令牌内容过度信任、未实施签名验证或缺乏关键声明校验，通过解码修改令牌中的用户标识（uid）和权限类型（UType）实现身份伪造与权限提升的攻击技术。

02

**实操技巧演示**

所有操作技巧演示均在玄域靶场平台中合法进行！

玄域靶场：**www.shangsec.com**

![](https://mmbiz.qpic.cn/mmbiz_png/SgRVa0DmgbEPAckXP5ib4HWOQiaqyJrg9bWW8Vkcl4aXQCOPhzWPjazwZ7SUjgczhBoq3R7JwzdHqo8nGMQuQhZHGnx03qK0oMUiaK1M7kmdrQ/640?wx_fmt=png)

这里非常推荐玄域靶场平台，不仅有**web靶场**环境，还有**安卓App**和**苹果App**靶场环境！

![](https://mmbiz.qpic.cn/mmbiz_png/SgRVa0DmgbGUbN2Lf0kUGCVSpkf94qgj8XzZSvaZcfmHAB9zNJ3qwp1ChnMicH3fiaMDdhvSNvXEZyE1QrM7jfJhHZ4H0qytyEhwHwzHFlkBk/640?wx_fmt=png)

以及配套**了上百道**最新精选的**面试题库**，且所有题目均有参考回答；更有**实战漏洞报告**板块，供大家进行学习！

且所有靶场环境、面试题库、实战漏洞报告均在持续更新中！

然后打开 **玄域JWT漏洞-05&越权**漏洞靶场环境，开启burpsute进行抓包，点击“查看信息”功能点。

![](https://mmbiz.qpic.cn/mmbiz_png/SgRVa0DmgbE927jK8w8tn1XX5GOxANSCwSZ7DhzFvKJ7HAzRQSBwjVOOibWbrYtOA0jicQ5hWicicZjX6VUCKABLjBvGCicjaPhXEgWxIfqCZOGs/640?wx_fmt=png)

使用bp拦截抓包，并且发现存在Authorization值，因为该关卡是关于jwt的，所以尝试使用bp自带插件JSON Web Token解密Authorization值。

![](https://mmbiz.qpic.cn/mmbiz_png/SgRVa0DmgbFT7ibBPwAwj2bPfdFvHbBn0SE7ZHFJvdN98yBeao4LG1RRMNap1Mxl67icq1ho6G4ib8IEHlfu7YPhA8ygxibM17hZStEa1k8kVGw/640?wx_fmt=png)

通过插件发现，JWT 的 Payload 中以 uid 标识用户身份、UType 定义角色权限，二者共同作为服务端鉴权的判断依据。

推测 UType 是 用户类型/角色标识字段，用于区分不同权限等级的用户群体，当前值 "general" 表明这是一个普通用户/一般用户账号，系统会根据该字段值控制功能访问权限（如管理员 admin 可访问后台，而 general 只能查看公开数据）。

在渗透测试中，这是典型的水平越权/垂直越权测试点——尝试将 "general" 修改为 "admin"、"super"、"system" 等高权限角色值，配合重新签名（如果密钥泄露或可爆破）或直接发送（如果服务端未验签），即可实现权限提升。

推测 uid 是用户身份标识符，当前值 "5201314" 代表系统中特定用户的数字ID，服务端通过该字段识别"谁"在发起请求，并与数据库中的用户记录关联以返回对应数据。

在渗透测试中这是IDOR（不安全的直接对象引用）漏洞的核心测试点——尝试修改uid为其他数值（如5201315、1、admin的uid等），若服务端未严格校验该用户是否有权访问此uid对应的数据，即可导致水平越权（查看其他普通用户信息）或配合UType篡改实现垂直越权（以低权限token操作高权限资源）。

同时修改uid和utype字段，uid为其他用户，utype为admin，并进行jwt编码后替换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SgRVa0DmgbG4WN1yW8FwkgFcGXtgX992sSdAamLjSicgRttu8LQEMy3R0aBtmXErZ5urT2oZoicOIqPVagG4FGhZ7bK1OcleM73vbib1qnc1bA/640?wx_fmt=png)

成功获得flag

![](https://mmbiz.qpic.cn/mmbiz_png/SgRVa0DmgbHwpcFzccibpMjwnm0fSQkk3jgHCcKlgjG7AnfArnm2FlSB5hgAFI11AtSRTlMggW6CKMv9IicThcgicIb1NoR5PxzXuia8kmTB9qQ/640?wx_fmt=png)

03

**学习交流群**

**学习资料、工具包领取**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SgRVa0DmgbGR1K9wKk0vDFlCvVzLG6kymqgD8mfibF1MwRIp11WlR1eInSicAOCltUzQ8iaKOFPSu3EI7CUHyouScibiaeyToWkvykAF5scFaUv4/640?wx_fmt=png)

**过期后请添加平台客服**

![](https://mmbiz.qpic.cn/mmbiz_png/SgRVa0DmgbFtbhQvzpmwFRXzzIDSfJ7WkxDaE70Fe2bpd7rBIbgLiak7OpYGicsK1oGwFp8WiatkoWh4GjGEr2bJ6FMTYpjLstx1ogJiaeWqsYk/640?wx_fmt=png)

[【网安】参数污染技巧！结合越权漏洞实操演示和讲解！](https://mp.weixin.qq.com/s?__biz=Mzk0NTYwNzY3NQ==&mid=2247484357&idx=1&sn=e0c7cbe1d50725347989a4995038f521&scene=21#wechat_redirect)

[【技术视角】杭州某科技公司流量劫持案-独家技术解析！](https://mp.weixin.qq.com/s?__biz=Mzk0NTYwNzY3NQ==&mid=2247484224&idx=1&sn=25b3a193756975e22959783d405e75b8&scene=21#wechat_redirect)

[【黑客】App如何抓包？玄域App漏洞靶场实操演示](https://mp.weixin.qq.com/s?__biz=Mzk0NTYwNzY3NQ==&mid=2247484102&idx=1&sn=7398a3ae71aae797b52bc151e87d4a33&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BZbILNBpkriaqkcb3mVsibPBFZhJmNibp2obghff1gssSjzh2Wz3Rog66ia3IPuopvpLYxeQAP7g2o2icEv5ibZ2Vo4g/0?wx_fmt=png)

无名的安全小屋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BZbILNBpkriaqkcb3mVsibPBFZhJmNibp2obghff1gssSjzh2Wz3Rog66ia3IPuopvpLYxeQAP7g2o2icEv5ibZ2Vo4g/0?wx_fmt=png)

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