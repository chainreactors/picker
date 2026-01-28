---
title: 学术前沿 | 中国科学技术大学林璟锵教授团队：隐私保护单点登录服务的门限IdP服务器方案
url: https://mp.weixin.qq.com/s/hCTdOHfMd95KZI9vdrPamw
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:32:26.248428
---

# 学术前沿 | 中国科学技术大学林璟锵教授团队：隐私保护单点登录服务的门限IdP服务器方案

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OXHiaek9DxH1ZoeaIicdI05w5qs3GIZkNvajrrYqTiaHY4Giacr9VqD5Zng/0?wx_fmt=jpeg)

# 学术前沿 | 中国科学技术大学林璟锵教授团队：隐私保护单点登录服务的门限IdP服务器方案

网络空间安全科学学报

![]()

在小说阅读器中沉浸阅读

**引用**

沈昕，林璟锵，周昶，等.隐私保护单点登录服务的门限IdP服务器方案[J].网络空间安全科学学报，2025，3（4）：67 - 80. https://doi.org/10.20172/j.issn.2097-3136.250406.

Citation Format： SHEN X，LIN J Q，ZHOU C，et al. Privacy-preserving single sign-on scheme with threshold IdP servers[J]. Journal ofCyberse-curity，2025，3（4）： 67 - 80. https://doi.org/10.20172/j.issn.2097-3136.250406.

**背  景**

随着云服务与在线平台的普及，单点登录（SSO）系统虽凭借“一次认证、全局访问”的特性被广泛采纳，但其依赖的集中式身份提供商（IdP）的架构存在严峻的单点故障风险与隐私泄露隐患——不仅IdP的宕机或攻破会导致服务全面瘫痪及凭据失窃，诚实但好奇的IdP及恶意依赖方（RP）还可能通过追踪或合谋侵犯用户隐私。针对上述痛点，我们提出了一种隐私保护单点登录服务的门限IdP服务器方案，该方案在不引入额外可信第三方的前提下，融合门限密码学与身份转换机制，实现了可用性与隐私保护的平衡。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OASR3jxuN1c5xjG9588XeIGj0saiaszWGfrNITZN6PMVkpcc388KYViaw/640?wx_fmt=png&from=appmsg)

**01**

本研究构建了一种融合基于口令的门限认证（PbTA）框架与UPPRESSO身份转换机制的新型SSO方案。方案核心在于将传统单点IdP功能解耦并分散至n个节点组成的集群中，采用t-out-of-n门限机制运行。在交互过程中（如图1所示），用户利用门限不经意伪随机函数与椭圆曲线密码学技术，与集群协同生成临时伪身份，进而获取对应的令牌分片；用户仅需收集至少t个有效分片即可聚合生成完整的令牌。该设计不仅有效缓解了集中式SSO的单点故障风险，还利用身份转换机制实现了方案所需的隐私保护目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OFbBuqtxTv8f2P1kKdBDlMPm72ZWIQa1MN39iby93muUmzrsSCGlErUA/640?wx_fmt=png&from=appmsg)

图 1 令牌请求阶段

Figure 1 Token request pahse

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OASR3jxuN1c5xjG9588XeIGj0saiaszWGfrNITZN6PMVkpcc388KYViaw/640?wx_fmt=png&from=appmsg)

**02**

为了直观展示本方案的优势，我们将本方案与现有的SPRESSO、UPPRESSO、MISO等主流隐私保护SSO方案进行了多维度对比（如表1所示）。结果表明，本方案在无需引入可信执行环境（TEE）或额外可信服务器的前提下，创新性地实现了抗单点故障与全方位隐私保护的融合；通过门限机制与身份转换机制，本方案不仅消除了集中式架构的脆弱性，更有效抵御了IdP登录追踪、RP身份关联以及有限的IdP-RP合谋攻击，在安全性和隐私保护特性上均展现出显著优势。

表 1  隐私保护SSO和门限SSO方案对比

Table 1 Comparison of privacy-preserving SSO and threshold SSO schemes

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OcTsVgqHEwoyvf7dxndwK1gckC5IFgv8g0Y4EdxDibR4EcjK1AAej40Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OASR3jxuN1c5xjG9588XeIGj0saiaszWGfrNITZN6PMVkpcc388KYViaw/640?wx_fmt=png&from=appmsg)

**03**

为了评估方案的性能优势，我们着重对用户登录阶段的理论计算开销进行了分析。如表2所示，我们将本方案与作为设计基础的PASTA和UPPRESSO方案，以及同样具备分布式隐私保护特性的TSAPP方案进行了横向对比。分析结果显示，由于避免了昂贵的双线性对运算，本方案在用户侧的计算效率显著优于同类的TSAPP方案，且整体理论开销与基础方案（PASTA、UPPRESSO）保持在相当水平，并未因引入新特性而产生显著负担。此外，通过对通信开销以及在局域网（LAN）和广域网（WAN）模拟场景下的计算开销进行实验评估，进一步证实了本方案在实现强隐私与高可用的同时，保持了优异的运行效率。

表 2 用户登录阶段的理论计算开销

Table 2 Theoretical computational overhead of user login

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OQ2n5Ea6D5LLYibwfIL18E92j2jmrhpThh6MyEHJ6YjNazTib3uweqWkw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OASR3jxuN1c5xjG9588XeIGj0saiaszWGfrNITZN6PMVkpcc388KYViaw/640?wx_fmt=png&from=appmsg)

**总结**

本研究针对现有SSO系统的安全痛点，提出了一种融合门限密码学与身份转换机制的隐私保护SSO方案。该方案不仅通过t-out-of-n门限机制有效消除了IdP的单点故障风险，还利用椭圆曲线技术实现了针对IdP追踪、RP关联及有限IdP-RP合谋的全面隐私防护。实验证明，该方案在保证系统高可用性与隐私保护特性的同时，维持了与现有OIDC协议的高兼容性及高效的运行性能，为构建更安全、更私密的互联网身份认证基础设施提供了新的解决思路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OASR3jxuN1c5xjG9588XeIGj0saiaszWGfrNITZN6PMVkpcc388KYViaw/640?wx_fmt=png&from=appmsg)

**论文全文下载方式**

1 识别下方二维码；2 点击文末“阅读原文”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAgR03l35X7QKLA8WGlja2OWkyWQEUcbPg2uj0MYvRyHpSRib6G6gT5iaKUkzpHAhzrayL3w7IMUXbA/640?wx_fmt=png&from=appmsg)

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