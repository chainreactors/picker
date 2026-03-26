---
title: 【FATF最新报告解读】稳定币与非托管钱包P2P交易成监管新焦点，如何破局？
url: https://mp.weixin.qq.com/s/3zoC32rRithE8I8d53IOFA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:29:25.167510
---

# 【FATF最新报告解读】稳定币与非托管钱包P2P交易成监管新焦点，如何破局？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2ibKZs4HxyqsiaERN87znpaV9Enrb5G1JPXdSgMunyHQycAbXtaibCEpOK3kGxc4ABicBGtH1iakeheDUYdiaQQH2SuPuiaYib8IoTg3n9oQVq0iahKU/0?wx_fmt=jpeg)

# 【FATF最新报告解读】稳定币与非托管钱包P2P交易成监管新焦点，如何破局？

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4HxyqtulAVdcpiav1tFkZ3xjL4YG9dicDia96uzeX71mUlnVGY6OAic8nc19Fjjqrx3HD1d5BxJdoiajIBmtiaD6fW4D5uyWdUA9t8X3dERM/640?wx_fmt=gif&from=appmsg)

近日，金融行动特别工作组（FATF）发布了《稳定币与非托管钱包专项报告：点对点交易》（Targeted Report on Stablecoins and Unhosted Wallets – Peer-to-Peer Transactions）。

该报告详细分析了稳定币在虚拟资产和传统金融系统中日益增长的规模、采用率以及功能整合，并重点指出了稳定币和非托管钱包在点对点（P2P）交易中被滥用于洗钱（ML）、恐怖融资（TF）和扩散融资（PF）的风险。

面对这一趋势，FATF 的监管重点正在发生转移，从单纯的法币出入金通道（On/Off-ramps）向稳定币二级市场监控（Secondary Market Monitoring）倾斜。BlockSec将通过本文深入解读 FATF 报告的核心建议与风险指标，并探讨在新的监管要求下，行业参与者应如何利用技术手段破局。

**风险缓解的实践与建议**

针对上述风险，FATF 提出了一系列针对司法管辖区和私营部门的良好实践和建议。在这些建议中，我们看到技术工具在满足合规要求方面正发挥着不可替代的作用。

**1. 针对司法管辖区的建议**

* 全面落实 FATF 第 15 项建议：确保稳定币发行方、中介 VASP 和相关金融机构受到明确的 AML/CFT 义务约束，包括许可/注册、CDD、可疑交易报告（STR）和旅行规则（Travel Rule）。

为了高效生成可疑交易报告（STR），机构需要强大的链上监控能力。BlockSec 的 Phalcon Compliance 平台能够实时监控链上交易，自动识别异常模式并触发告警，一键生成STR报告，帮助合规官高效完成填写义务。

* 强化发行方的二级市场控制：监管机构应考虑要求稳定币发行方具备在二级市场冻结（Freeze）、销毁（Burn）和撤回稳定币的技术能力。同时，鼓励发行方基于风险实施白名单（Allow-listing）或黑名单（Deny-listing）机制。

构建有效的黑白名单机制离不开精准的地址数据。BlockSec 拥有海量的地址标签库，结合 Compliance 的动态风险评分功能，能够帮助发行方精准识别受制裁实体、暗网或混币器地址，从而实现自动化的黑名单拦截与白名单准入。

* 监控 P2P 交易风险：积极监控通过非托管钱包进行的 P2P 交易规模和风险，并采取相称的缓解措施。

非托管钱包的监控是当前合规的难点。借助 MetaSleuth 强大的跨链追踪能力与 Phalcon 的实时监控网络，机构可以穿透复杂的 P2P 交易网络，有效识别非托管钱包背后的潜在风险。

* 加强国际与公私合作：建立跨国监管学院（Supervisory Colleges）以监管跨境稳定币项目；建立公私合作伙伴关系，共享风险指标和犯罪类型学。

**2. 针对私营部门（发行方与 VASP）的建议**

* 实施可编程合规控制：稳定币发行方应在智能合约中嵌入合规控制功能。例如，通过白名单机制，只允许经过身份验证的钱包地址持有和转移稳定币；或者通过黑名单机制，拒绝与受制裁或高风险地址的交易。BlockSec 拥有覆盖全面、实时更新的地址标签库数据，可直接集成至稳定币合约，作为发行方内置的、可动态筛查的合规策略，让每一笔链上交互都在合规边界内完成。

* 应用高级区块链分析工具：VASP 和发行方应广泛使用区块链分析工具，追踪资金来源和去向，识别与暗网、混币器、受制裁实体相关的多跳（Multi-hop）高风险交易。

BlockSec 的 MetaSleuth 作为专业的加密资产追踪和调查平台，正是 FATF 所倡导的“高级区块链分析工具”。它能够将复杂的链上交易转化为直观的资金流向图，支持多跳追踪（Multi-hop Tracking）和跨链分析，帮助调查人员快速理清资金脉络，精准定位高风险交易。

* 针对非托管钱包的强化措施：当 VASP 处理与非托管钱包的交易时，应采取强化尽职调查（EDD），例如限制交易额度、验证非托管钱包的实际控制权，以及利用分析工具评估交易对手的风险等级。

在执行 EDD 时，VASP 可以接入 BlockSec 的 Wallet Screening API。该接口能够实时评估非托管钱包的风险等级，为限制交易额度或阻断交易提供客观、量化的决策依据。

**风险指标（Red Flags）总结**

为了帮助识别和防范风险，FATF 总结了一系列风险指标。结合 BlockSec 的技术实践，我们可以更有效地应对这些挑战：

1. 异常交易模式

与客户资料不符的快速跨境转移；短时间内大量稳定币的拆分或汇聚；无合理经济目的的法币与稳定币、或不同稳定币之间的频繁兑换。

2. 匿名性相关指标

与旅行规则覆盖钱包（TRW）相距多个跳数（Hops）的非托管钱包交易；长期休眠的钱包突然激活并进行大量跨链交易；与离岸高风险平台或暗网地址的交互；使用混币器或隐私币进行资金分层。

针对“多跳”和“跨链”等隐匿手段，MetaSleuth 平台支持深度的资金流向分析，能够穿透复杂的交易层级，还原资金的真实来源和去向。

3. 恐怖融资与扩散融资指标

打着人道主义救援旗号的资金迅速转移至交易平台或混币器；向物流枢纽或自由贸易区附近的中间人支付稳定币以采购军民两用物资；利用跨链桥逃避特定网络的制裁筛查。

面对利用跨链桥逃避筛查的手段，面对利用跨链桥逃避筛查的手段，BlockSec的MetaSleuth 与 Phalcon Compliance 产品均支持跨链追踪与筛查，覆盖多条主流公链间的资金流向分析，确保风险不因链的切换而断档。FATF 报告中列举的异常交易模式风险指标，均已内置于 Phalcon Compliance 的筛查模板中，可第一时间捕捉资金向混币器或高风险平台的异常转移，实现早期预警。

**结语**

FATF 本次报告的发布，标志着全球稳定币监管进入新阶段——合规的战场正从链下延伸至链上，从出入金通道延伸至二级市场的每一笔 P2P 交易。对于行业参与者而言，率先建立健全的链上合规能力，将成为赢得监管信任、构建长期竞争优势的关键。

BlockSec 将继续深耕区块链安全与合规技术，通过 Phalcon Compliance、MetaSleuth 等产品，为行业提供更先进、更可靠的解决方案，共同构建一个安全、透明、合规的 Web3 生态。

如需获取完整报告，可扫描以下二维码添加BlockSec小助手，备注**【FATF报告】**，即可领取。

![图片](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTIsKxzS9wsjGLcrPeY8TKnFOHbQicPZBqPFNRQr5uEZic6vIXoz6HwWGHNdicWKQmQtwsqtRzVRhibFHw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

---

关于BlockSec

BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立。BlockSec 致力于提升 Web3 世界的安全性和易用性，提供一站式安全服务，包括智能合约/链/钱包安全审计服务、协议安全和数字货币合规(AML/CFT)平台 Phalcon Security / Phalcon Compliance / Phalcon Network、资金追踪调查平台 MetaSleuth 和区块链交易分析工具 Phalcon Explorer 等。

目前，BlockSec 已服务全球逾 500 家客户，既涵盖 Web3 知名公司 Coinbase、Cobo、Uniswap、Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、Merlin、PancakeSwap 等，也包括了权威监管机构及咨询机构，如联合国、SFC、PwC、FTI Consulting 等。

官网：https://blocksec.com/

Twitter：https://twitter.com/BlockSecTeam

推荐阅读👇

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTJKnQAjhicg47N8sLY3SKzqlEcnuEf3pYzPTIqpar2ibkeSeCvjqQsKrLwZwWyTcAXIazKXLQIXEchQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247490504&idx=1&sn=ed76941ba8ee144bdd12cb0ddb7df70c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIje0g9kj9ic4b9GEzwpo1TCWq94NdL91n7Yt1FYkWUmPEXrkGzHKNvuQbOlu36LFXShpNOTklWvKw/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491200&idx=1&sn=f0a133511ca63c3deb086c51654e4157&scene=21#wechat_redirect)

#BlockSec

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

BlockSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

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