---
title: CNNIC 真的不可信吗？来看看那些重创互联网信任的 CA 安全事故
url: https://mp.weixin.qq.com/s/mq333rex9rusEyBnlHbJyg
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:50.928169
---

# CNNIC 真的不可信吗？来看看那些重创互联网信任的 CA 安全事故

# CNNIC 真的不可信吗？来看看那些重创互联网信任的 CA 安全事故

原创

ralap
ralap

网络个人修炼

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

最近看到 CNNIC 安全 DNS 服务上线，本是国内互联网基础安全的一次升级，评论区却有多个网友直言「CNNIC 不安全」。

到底是真的不安全，还是大众的认知混淆？

带着这个疑问，我专门深挖、系统梳理了整件事的来龙去脉，终于搞懂了这场**陈年安全事件**。

---

一、CNNIC 到底出过什么事

2015年，CNNIC作为国家级根CA，违规向埃及第三方公司MCS Holdings，签发了一张**无任何域名约束、权限全开的中级CA证书**。这张证书看似是短期测试证书，却拥有极高权限：持有者可以伪造互联网上**任意网站的SSL证书**，包括谷歌、百度、各大银行官网。

MCS 拿到证书后，将它用于防火墙设备的 SSL 中间人解密（MITM），**在 MCS 自身受控的内网环境下，动态生成伪造证书、解密其内网中的 HTTPS 流量；现有证据没有证明该证书被用于公网全网流量劫持。**这件事被证书透明度 CT 日志捕获异常记录，由 Google 工程师 Adam Langley 在 2015 年 3 月 24 日公开博客曝光实锤。

**事发后，CNNIC于2015年3月22日撤销了对MCS的业务授权。CNNIC在声明中称，MCS确认不当签发的测试证书仅用于其实验室内部测试。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMI79xvYxtr20HNxAQjRJCwqReN0bPylcQOKdvsQLGTe16ex49CA4n7dRfpj5fJlmYgjJhuqZlMGHwRZj5pAPmrMhPb4tTtibqag/640?wx_fmt=png&from=appmsg)

虽然CNNIC本身没有主动做流量劫持、解密用户流量，问题出在管控疏漏、违规下放顶级发证权限，但在国际互联网安全规则里，**根CA的管控失效，等同于根本身不可信**。

也正是这次事件，让Chrome、Firefox两大全球主流浏览器，直接对CNNIC证书签发采取限制措施。2015 年 4 月，Mozilla 和 Google 先后宣布不再信任 CNNIC 新签发的证书，CNNIC 的根证书从此在主流浏览器中失去默认信任地位，目前仍看不到 CNNIC 被重新纳入主流公开信任 CA 的消息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMLMk4FSRIy7dnyYnRM10NT0AMbwqicYYu5lTWOY3sl8Mzus6zbKWlhMfNX5Y6uJZVdtGzOMBKsy0TcW5e7Z9Ca8lT7YYeU8XH34/640?wx_fmt=png&from=appmsg)

如果说出过事就代表不能用，那么**被否定的应该是全世界一大半的 CA，不止中国。**

---

二、名单上的“友商”们

**被浏览器拔掉信任的名单里，有中国CA，但也躺着荷兰**CA**、美国**CA**、法国**CA**、土耳其**CA**、印度**CA**。**

**荷兰，DigiNotar，2011 年——史上最严重的一次，直接搞到破产。**

它的 CA 基础设施被攻陷，攻击者用它签发了**至少 531 张伪造证书**，覆盖 Google、Yahoo、Mozilla、WordPress、Tor 等等。其中的 Google 通配证书，**真实被用于对伊朗 Gmail 用户的中间人攻击**——不是理论风险，是真发生了大规模流量拦截。

更糟的是，它 7 月 19 日就发现了入侵，**却没有公开披露**，一直到 8 月底伪造证书被人贴到网上。它还牵涉荷兰政府的 PKIoverheid 体系，包括国民身份认证系统 DigiD——**一个国家级的身份基础设施被拖下水**。

结局：所有主流浏览器和操作系统移除它的根证书，**2011 年 9 月 20 日，公司破产。从被发现到关门，不到一个月**

**美国，Symantec，2015 到 2018 年——当年的全球第一大商业 CA。**

这一件我觉得最该拿出来说，因为它的性质和 CNNIC 几乎一样，但大了几个数量级。

它当时市场份额第一，旧体系下挂着 VeriSign、GeoTrust、Thawte、RapidSSL、Equifax 一整串品牌，**全球大约三分之一的 HTTPS 都挂在这个体系上**。

2015 年 9 月，Google 披露它**未经授权**签发了 google.com 等域名的证书；它一开始说数量很少，Google 用 CT 日志深挖，发现**远超它自己的说法**，最终认定**至少 3 万张证书**的有效性存疑（Symantec 有异议，但反驳没有被接受）。

真正致命的是第二条：**它把大量没有约束的中间 CA，交给了外包合作伙伴**——Google 点名了 CrossCert（韩国）、Certisign（巴西）、Certsuperior、Certisur。这些伙伴在签发时跳过了域名所有权验证，而因为链条层层外包，**Symantec 拿不出审计证据证明这些验证确实执行过**。

你看，这跟 CNNIC 是同一个病。区别只在规模——**CNNIC 是一次一张，Symantec 是长期、批量、系统性地外包。**

结局是十年内最彻底的清算：Chrome 66（2018 年 4 月）不信任 2016 年 6 月 1 日之前签发的证书，**Chrome 70（2018 年 10 月 23 日）对整个旧体系全面不信任**；Firefox 58 警告、60 报错、63/64 全面不信任。

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMIGG1CiacGNiaItAnCTXG2YjWbE15wMGzxGX3c6ja5Uq75QvSbQibUcOlkSaQ6T2eWvbo0Cpt8gD3M1LB6S6tXnHvq65YfsZzyrhA/640?wx_fmt=png&from=appmsg)

**被"区域死刑"的三家**：TURKTRUST（土耳其，2013）把两张普通证书"误"发成中间 CA，一张被用来签了 google.com 伪证书，被撤销 EV 资格；ANSSI（法国，2013）是**法国国家信息系统安全局**，明知已明文禁止仍签发用于流量劫持解密的中间证书，被**约束至 .fr及.gp域名**；India CCA（印度，2014）中间 CA 被攻破、签发 Google 和 Yahoo 伪证书，自己只找到 4 张而 Google 手上还有更多，被判定**对泄露范围没有掌握能力**，限制在印度域内。

---

三、  **DNS安全解析服务 ≠ SSL证书CA信任体系**

CA 是干什么的？**签发证书**。它的工作是验证"这个网站的身份是真的"，给浏览器一个信任凭证。它管的是**身份**。

安全 DNS 是干什么的？**域名解析**。它的工作是把"cnnic.cn"翻译成一个 IP 地址，顺便在翻译这一步拦住已知的恶意域名。它管的是**寻址**。

DNS 负责把域名解析到 IP，CA 负责证明网站身份。CNNIC 的 CA 问题发生在证书签发链上，而这次安全 DNS 是递归解析服务。两者技术栈不同，信任评估也不能互相替代。

虽然网友把CA 事故直接等同于 DNS 不安全，技术上不严谨，但也确实是了解这段历史背景，并非空穴来风。只能说**信任的建立需要数年，崩塌只需几秒，而修复可能需要几代人的时间。**

**需要强调的是，本文不是在为 CNNIC 安全 DNS 背书，也不是说它的 CA 历史可以翻篇。我只是反对把 CA 事故直接等同于 DNS 不安全。网友当然可以因为历史声誉选择不用，但判断这个 DNS 是否可信，最终应看它自身的协议、日志、审计、过滤政策和治理透明度。不直接否定，不等于必须信任。**

---

参考链接

[1]https://www.cnnic.net.cn/n4/2022/0401/c39-3756.html

[2]https://blog.mozilla.org/security/files/2015/04/CNNIC-MCS.pdf

[3]https://www.enisa.europa.eu/sites/default/files/all\_files/Operation\_Black\_Tulip\_v2.pdf

[4]https://www.chromium.org/Home/chromium-security/symantec-legacy-pki/

[5]https://blog.mozilla.org/security/2013/12/09/revoking-trust-in-one-anssi-certificate/

[6]https://blog.mozilla.org/security/2018/03/12/distrust-symantec-tls-certificates/

[7]https://www.theregister.com/security/2011/09/09/apple-finally-purges-mac-os-of-disgraced-diginotar-certs/1509734

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

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