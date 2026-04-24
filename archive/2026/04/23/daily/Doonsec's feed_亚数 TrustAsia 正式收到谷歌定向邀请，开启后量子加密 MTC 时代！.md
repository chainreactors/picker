---
title: 亚数 TrustAsia 正式收到谷歌定向邀请，开启后量子加密 MTC 时代！
url: https://mp.weixin.qq.com/s/ROHxCv8YvEB3qQnmEVA14A
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:53:12.725865
---

# 亚数 TrustAsia 正式收到谷歌定向邀请，开启后量子加密 MTC 时代！

![cover_image](http://mmecoa.qpic.cn/sz_mmecoa_jpg/PaAJmAASPibhza4QPiaN3mu2FlvSgZ7Zo8YxzxgW5vanWWA3smD9o46Fm8A4m15HHTrZGiafpYCNayoeOvZLmAQicJ6v5smmLbNpqIZUx6nJtYA/0?wx_fmt=jpeg)

# 亚数 TrustAsia 正式收到谷歌定向邀请，开启后量子加密 MTC 时代！

持续创新的
持续创新的

亚洲诚信TrustAsia

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/CphDqoiaUGnIGIBPPfp2tiaiaHd5ucHHV5ko6P1Gg8qibDsukCMz3EVE8HwstTDxO15O0FGfaicWJHxjDzZZ157ahDA/640?wx_fmt=gif)

近日，亚数 TrustAsia 正式收到 Google 量子安全根计划（Chrome Quantum-Resistant Root Program）团队的定向邀请，作为全球首批核心参与者，共同推进默克尔树证书（Merkle Tree Certificates，简称 MTC）的生态建设。

这不仅是国际科技巨头对亚数 TrustAsia 密码技术实力的顶级背书，更是中国 CA 机构在全球数字信任规则制定中，从“参与者”向“定义者”迈进的重要里程碑。

**WebPKI 的极限挑战：后量子与短效期的“双重夹击”**

面对量子计算的步步紧逼，后量子密码迁移已不是“选项”，而是“倒计时”。同时，随着 CA/B 论坛正式推动 TLS/SSL 证书有效期向 47 天缩短，全球 WebPKI 正在经历一场根本性的重塑。

然而，传统的 X.509 证书在迈向PQC时代时，面临着一个致命的物理痛点——后量子算法产生的签名体积庞大。

后量子算法（如 ML-DSA）生成的签名体积远超 RSA 或 ECC 等传统算法。如果沿用现有的证书链模式，HTTPS 握手时传输的数据量将激增，导致全球互联网出现可感知的延迟，甚至导致老旧网络设备因处理不了大数据包而崩溃。

除了握手性能骤降之外，当前WebPKI的证书签发信任中枢——证书透明度日志（CT）体系也将面临严峻考验，因为每一条CT日志都必须包含完整的公钥和签名。

当“单张证书体积增加”、“证书数量海量爆发”、“日志体积激增”三重压力同时出现，现有的 X.509 与 CT 架构根本无法承载这种量级的膨胀。

**MTC 架构：破局的确定性解法**

####

为了突破性能瓶颈，Google 领衔推进的 MTC 方案并非对现有体系简单的修补，而是对信任实现方式的一次底层重塑。其核心突破体现在两个维度的“解耦”与“融合”：

**01**

性能保卫战：安全强度与传输数据的“完美解耦”

MTC 创新性地用极轻量的“包含证明”（Inclusion Proof）取代了庞大的证书签名链。也就是说，它不再要求浏览器在每次 TLS 握手时下载并验证完整的证书签名链，而是将海量证书聚合在一棵“默克尔树”中，由 CA 对唯一的“树根（Tree Head）”进行签名。客户端只需接收一个极轻量级的“包含证明（Inclusion Proof）”即可完成验证。

无论后量子算法的签名有多庞大，客户端接收到的验证数据始终被压缩到极限，成功将“密码算法的安全强度”与“ TLS 握手时传输的数据量”彻底解耦。

**02**

机制进化：“原生透明”彻底消解架构冗余

在 MTC 全新架构中，透明度成为了证书签发的“原生属性”。任何 MTC 证书的签发都必须不可逆地被纳入一棵公开的默克尔树中。这意味着，MTC 默认继承了现今 CT 生态的所有安全特性，却完全免除了传统 CT 带来的额外网络开销，MTC 从根本上化解了海量数据激增带来的基础设施崩溃危机。

**五年同行，亚数 TrustAsia 对全球 WebPKI 社区的长期贡献**

在 Google 最新发布的《构建一个稳健且高效的量子安全 HTTPS 体系》中，明确了首批 MTC 参与者的严苛门槛，这也正是对亚数 TrustAsia 实力的绝佳注解：

我们计划邀请截至2026年2月1日之前，至少拥有一个被 Google Chrome 认定为“可用”CT日志的运营方，参与公共 MTC 的启动工作。

这些机构已经证明其具备运行全球级安全服务所需的卓越运营能力和高可用基础设施，因为这些服务正是支撑 TLS 连接在 Chrome 中正常运作的基础。鉴于 MTC 技术在架构上与 CT 具有显著相似性，这些运营方具备独特优势，能够确保 MTC 体系快速且成功地启动并落地。

—— 谷歌 Chrome 网络安全团队

早在 2021 年，亚数 TrustAsia 就首次被正式纳入 Google CT 日志服务商名单，既是亚洲地区唯一的 CT 日志服务商，也是中国 CA 机构在参与全球 Web PKI 治理上的重要突破。

五年来，亚数 TrustAsia 不仅维持了极高标准的稳定运行，更在全球仅有的八家 CT 日志服务商中，凭借深厚的高并发处理能力和底层密码学积淀，赢得了国际同行的高度公信力。目前，亚数 TrustAsia CT日志已被 Google、Apple、Microsoft、Mozilla 四大主流浏览器厂商纳入可用日志列表，成为全球证书签发的重要信任依赖。

从参与到引领，亚数 TrustAsia 始终走在密码技术的最前沿。

此次深度协作，意味着亚数 TrustAsia 将与谷歌技术团队直接对话，共同打磨下一代 WebPKI 的交互协议。

这种前瞻性的技术布局，也将为亚数 TrustAsia CaaS（证书即服务）注入更强大的生命力。未来，我们的用户将无需感知底层的技术震荡，即可在TrustAsia CaaS 的驱动下，无缝平滑地步入一个由 MTC 支撑的、全自动、高安全的数字信任新纪元。

WebPKI 的下一个三十年已经开启。我们将继续携手 Google 及全球网络安全社区，深度参与 MTC 证书标准的验证与落地，用顶尖的密码学基建，为全球企业构建更加高效、稳健的数字信任生态。

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/PaAJmAASPibhoAlgo9AAIG7p8VCYTN8odVyibRAee2SQGPt6tW468YmvQY0hSsok1R5fDt2BGzRD30nAnHwibyhXHNpdFWQlvTDucOm4oDRPg0/640?wx_fmt=gif&from=appmsg)

**END**

★

![](https://mmecoa.qpic.cn/sz_mmecoa_png/PaAJmAASPibgHSxBf1Gn2IjZKufmibFhw3cWEvVm8dmmc7jyOgpgNPvaDxKOBJCP8Dm3zjcUicwBWhFxXkkSMWFKh6LpDcTK3N5WeLiaggzeIicc/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/CphDqoiaUGnLAzkhqKbuODHictM1RHCzjBHLWgJMKOlib35WcLgDz9b1aofv9jmDOEiapIyOZ76wapibAsNw5GicBe2g/0?wx_fmt=png)

亚洲诚信TrustAsia

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/CphDqoiaUGnLAzkhqKbuODHictM1RHCzjBHLWgJMKOlib35WcLgDz9b1aofv9jmDOEiapIyOZ76wapibAsNw5GicBe2g/0?wx_fmt=png)

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