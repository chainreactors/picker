---
title: Bybit十五亿美元失窃案反转，竟是Safe协议开发者先“中招”
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649788128&idx=1&sn=e2dbece6f830a6448fc883a3999332b0&chksm=8893be8fbfe437994387fed462260281a6796e4e62c7c439dc8ed5a3e398cf5ebdd98dc04e3a&scene=58&subscene=0#rd
source: 安全客
date: 2025-02-28
fetch_date: 2025-10-06T20:38:07.395792
---

# Bybit十五亿美元失窃案反转，竟是Safe协议开发者先“中招”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb7CiaWtIBds4lYr7Ahnk1SQTxXb7O9Yt494wWZMwqNRE89mkLdS8l09MT9YMiaBPau4F1Iy3ABWiaSmQ/0?wx_fmt=jpeg)

# Bybit十五亿美元失窃案反转，竟是Safe协议开发者先“中招”

安全客

***前情概述***

在加密货币领域，安全问题始终如达摩克利斯之剑高悬。近期，Bybit 交易所遭遇的大规模盗窃案，更是将这一问题推至风口浪尖。此前，2 月 21 日，加密货币交易平台 Bybit 经历了一场灾难性的网络攻击，其以太坊冷钱包中价值约 15 亿美元的加密货币被盗取，此事件一举成为史上最大规模的单一加密货币盗窃案。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb7CiaWtIBds4lYr7Ahnk1SQTicT8HafT4YbIPTx5UZm6Px0k7mNSxgU2NVB5ibZl2FqVtLId9b0TSy5w/640?wx_fmt=jpeg&from=appmsg)

事件发生时，Bybit 的以太坊多重签名冷钱包正在执行向热钱包的预定转账操作。攻击者施展极为精巧的手段，通过伪装签名界面，使交易显示为正确地址，却在底层悄然改变智能合约逻辑，致使这笔巨额资金被转移至不明地址。诸多迹象表明，此次行径极有可能出自黑客组织 Lazarus Group 之手。该组织长期在网络犯罪领域兴风作浪，凭借高超技术与精密策划，多次实施加密货币盗窃行动，获取非法收入。

***攻击细节深度剖析***

事件发生后，整个加密货币行业与众多网络安全研究人员对攻击手法充满疑惑。毕竟，突破 Bybit 多重签名机制，让多个钱包保管人同时授权非法交易，难度极大。但随着调查深入，真相逐渐明晰。

最新调查明确排除了 Bybit 自身直接存在漏洞的可能性，将问题核心指向 Safe {Wallet} 多签名平台。原来，Lazarus Group 早在攻击发生前就已成功渗透 Safe {Wallet}，他们如同隐匿暗处的猎手，耐心蛰伏，等待对 Bybit 这个高价值目标发动致命一击的最佳时机。

攻击者将目标精准锁定 Bybit，采用极为隐蔽的攻击方式。他们把恶意 JavaScript 代码注入到 app.safe.global 平台，该平台是 Bybit 签名者能够访问的关键节点。但这些恶意脚本并未立即发作，而是处于潜伏状态，仅在满足特定条件时才会被激活。这种选择性激活机制极为精妙，普通用户在日常使用中难以察觉，成功避开了常规安全检测。

研究人员通过对 Bybit 签名者机器进行详细的分析，并借助互联网档案馆（Wayback Archive）进行历史数据回溯，成功发现了恶意 JavaScript 有效载荷的缓存版本。这一关键发现有力表明，Safe.Global 的亚马逊 AWS S3 或 AWS CloudFront 账户以及 API 密钥极有可能已被攻击者攻破。

凭借这些非法获取的凭证，攻击者得以肆意操控 AWS S3 存储或 CloudFront CDN 服务，将恶意脚本巧妙注入平台。进一步对 Safe {Wallet} 的 AWS S3 存储桶展开深入分析后，发现了专门针对 Bybit 设计的以太坊多重签名冷钱包恶意软件，这无疑为攻击者的作案手段提供了确凿证据。

Safe {Wallet} 官方发布声明证实，**经调查，此次攻击源于一台被入侵的 Safe {Wallet} 开发人员的机器**。攻击者先是将恶意代码植入开发人员的系统，随后利用开发人员被攻陷的凭证，将恶意 JavaScript 有效载荷注入平台。这一系列操作环环相扣，展现出攻击者高超的技术能力与精心策划的犯罪流程。

***后续应对与行业反思***

面对此次严重的安全事故，Safe {Wallet} 迅速采取行动。他们全面重建并重新配置了整个基础设施，同时对所有凭证（包括 API 密钥）进行了轮换，旨在彻底清除潜在的攻击隐患，确保类似攻击手段在未来无法再次得逞。值得注意的是，在整个调查过程中，研究人员并未在 Safe {Wallet} 的智能合约、前端或后端服务中发现任何原生漏洞。这起攻击事件的可怕之处恰恰在于其精心策划的供应链攻击策略，攻击者成功绕过常规安全防线，通过渗透开发环境，从源头对交易进行恶意篡改。

此次 Bybit 以太坊失窃事件，犹如一记重锤，在整个加密货币行业引发强烈震荡。它不仅给 Bybit 交易所带来巨大经济损失和声誉冲击，也为整个行业敲响了警钟。众多行业人士开始深刻反思当前加密货币资产安全管理体系中存在的漏洞与不足。例如，如何加强对关键基础设施供应商的安全审查，如何提升多签名机制在面对复杂攻击时的防御能力，以及如何在技术层面和管理层面构建更加严密、多层次的安全防护体系，以应对日益复杂多变的网络安全威胁，这些都成为行业亟待解决的重要课题。随着加密货币市场的不断发展壮大，保障资产安全已成为行业可持续发展的核心要素，此次事件无疑将推动整个行业在安全防护领域进行全面升级与革新。

内容来源：

https://x.com/safe/status/1894768522720350673
https://securityonline.info/bybit-heist-1-4b-ethereum-stolen-in-safewallet-exploit/

**推荐阅读**

|  |
| --- |
| **01**  ｜[OpenAI打击AI滥用](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649788109&idx=1&sn=8c9a5107fcaf4a2dcfb073dc328d6fbb&scene=21#wechat_redirect) |
| **02**  ｜[新型LLM漏洞让ChatGPT秒变黑客助手](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787902&idx=1&sn=71b8270b1a8d55b1d42e0de55fd7e386&scene=21#wechat_redirect) |
| **03**  ｜[AI代理互识身份后切换加密通话](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649788120&idx=1&sn=b7d60198de7d0c50da8350255171365e&scene=21#wechat_redirect) |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7CiaWtIBds4lYr7Ahnk1SQToL6KluUCOFUgO3xLicriaQibRgSowHZoQcK1GyurcmbibQSKicwibDZ5Eblw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7CiaWtIBds4lYr7Ahnk1SQTibSic4vclNhMJzz6Ys485uaib1aRTG4aVugehDF9KsIicYbQJywoZaJAbA/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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