---
title: Solana 热门 Web3.js npm库有后门，可触发软件供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521692&idx=1&sn=5adc287296024b676e739e74bb3e0ca5&chksm=ea94a4f6dde32de06e0328914013353296e26bd4750b735e6f67453b69e5e8cad0e8d251c242&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-06
fetch_date: 2025-10-06T19:38:59.559956
---

# Solana 热门 Web3.js npm库有后门，可触发软件供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# Solana 热门 Web3.js npm库有后门，可触发软件供应链攻击

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

![](https://mmbiz.qpic.cn/mmbiz_png/FIBZec7ucCiaWtRttKahE4rd7icPBW6mLiaWubZBfibktxAlCMH6dwLG1225lH4Xo8nmA5ENG7I4o905Qq23icpkHwg/640?wx_fmt=png)

**网络安全研究人员提醒注意针对热门 @solana/web3.js npm 库的软件供应链攻击，通过推送两个能够收割用户私钥的恶意版本，掏空密币钱包。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSOYGCXGx4P2NLnUOdmXpXa6ia0Jltj3CwSQd7Meelu1ia9v9TL4yibBTeib9ibH2libdwQQwXWP4P8K4aw/640?wx_fmt=png&from=appmsg)

研究人员在 1.95.6和1.95.7版本中检测到了这些攻击，但这些版本目前已不可从 npm 注册表中下载。该包使用广泛，每周下载量超过40万次。Socket 公司在报告中提到，“这些受陷版本中包含被注入的恶意代码，它们的目的是从毫不知情的开发人员和用户手中窃取私钥，从而清空密币钱包。”

@solana/web3.js 是一个npm包，可与 Solana JavaScript 软件开发包 (SDK) 交互构建 Node.js 和 web 应用。Datadog 公司的安全研究员 Christophe Tafani-Dereper 提到，“在 v1.95.7 中插入的后门，增加了一个 ‘addToQueue’ 函数，通过看似合法的 SloudFlare 标头提取私钥”，“之后对该函数的调用被插入多个位置，从而合法地访问该私钥”。

用于提取存放密钥的C2服务器 (“sol-rpc[.]xyz”)目前已下线，它在2024年11月22日在域名注册商 NameSilo 上注册。

该npm包的维护人员似乎遭到钓鱼攻击，导致威胁行动者获得账户的控制权并发布恶意版本。该库的维护人员之一 Steven Luscher 在1.95.8发布中提到，“Solana dApps 常使用的 JavaScript 库@Solana/web3.js 的一个发布访问账户遭攻陷。这导致攻击者能够发布遭修改的越权和恶意包，从而窃取私钥材料并从 dApps 提取资金。该问题应当不影响非监管钱包，因为后者在交易过程中不会暴露私钥。”

Luscher 还提到，该事件仅影响直接处理私钥的项目以及在2024年12月2日下午3:20到8:25 UTC 窗口期内更新的项目。建议将 @solana/web3.js 作为依赖的用户，尽快更新至最新版本，如发现授权密钥遭攻陷应更换。

几天前，Socket 公司提醒称发现了一个Solana 主题的恶意包“Solana-systemprogram-utils”，它偷偷在2%的交易中将用户的资金转移至受攻击者控制的硬编码钱包地址内。研究人员提到，“该代码通过98%的时间都在正常运行的策略，隐藏了它的真实意图。这一设计将可疑性降至最低且仍然允许攻击者窃取资金。”

之前，npm 包如 crypto-keccak、crypto-jasonwebtoken 和 crypto-bignumber 伪造成合法库，但包含可嗅探凭据和密币钱包数据的代码。这一事件再次说明威胁行动者仍然在滥用开发人员对开源生态系统的信任。研究人员提到，“恶意软件窃取开发人员的凭据和钱包数据，可造成经济损失。对于组织机构而言，受陷的系统制造可在企业环境中传播的漏洞，导致出现大规模的利用情况。”

点击“阅读原文”，马上试用开源卫士：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTBzmfDJA6rWkgzD5KIKNibpR0szmPaeuu4BibnJiaQzxBpaRMwb8icKTeZVEuWREJwacZm3wElt7vOtQ/640?wx_fmt=jpeg)

开源卫士试用地址：https://oss.qianxin.com

代码卫士试用地址：https://codesafe.qianxin.com

---

**推荐阅读**

[软件供应链投毒 — NPM 恶意组件分析](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518377&idx=1&sn=9504988637a30aee727161562a17cd5a&chksm=ea94b9c3dde330d5c8364a04723d8e973480d0cd285b4ea0da0b9c6d2640ddcadad09ee6bbb1&scene=21#wechat_redirect)

[软件供应链投毒 — NPM 恶意组件分析（二）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519078&idx=1&sn=eec7bf30c2e7abec80f62c022aa099c5&chksm=ea94ba0cdde3331aeabc6907e171c8b1e46209449d7af19a294d6cabe1260bb3a418ff465eaf&scene=21#wechat_redirect)

[在线阅读版：《2023中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517225&idx=1&sn=8154b433ae2be87ccbae15bc0fb09a00&chksm=ea94b543dde33c55c168c44e830d62b03e9b34ca072871d10156273a3f282cab7ccc42b9b430&scene=21#wechat_redirect)

[Npm 库XMLRPC 插入恶意代码，窃取数据部署密币矿机](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521633&idx=2&sn=4a7d37dee16810a9a2e5aecefb811f16&scene=21#wechat_redirect)

[Python、npm和开源生态系统中的入口点可用于发动供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=1&sn=7723bd7496e2f4b228e3013dd21765b4&scene=21#wechat_redirect)

[NPM恶意包假冒 “noblox.js”，攻陷 Roblox 开发系统](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520645&idx=1&sn=5c21506b72287be7f4b329b57e790e30&scene=21#wechat_redirect)

[恶意npm包利用镜像文件隐藏后门代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520084&idx=2&sn=07657bb6d212f2245303aa7ff98e61f2&scene=21#wechat_redirect)

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[奇安信入选全球《静态应用安全测试全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516678&idx=1&sn=5b9e480c386161b1e105f9818b2a5a3d&chksm=ea94b36cdde33a7a05cafa9918733669252a02611c222b02bc6e66cbb508ee3fbf748453ee7a&scene=21#wechat_redirect)

[奇安信开源卫士率先通过可信开源治理工具评估](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510243&idx=2&sn=47107ff7d0b61144e76e4fdf05a96abe&chksm=ea949989dde3109f23f3b35de95f08b10965f5d533f9fda08668094aedfde62ca1bcfbe13d96&scene=21#wechat_redirect)

[全球软件供应链安全指南和法规概览](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518721&idx=1&sn=a6c98264bc51488064bb51b337094a5c&chksm=ea94bb6bdde3327db988d0cfef1994c2a1fdb66a6ceb2fc1642bb498e3f0c546fa7478db5dc5&scene=21#wechat_redirect)

[英韩：Lazarus 黑客组织利用安全认证软件 0day 漏洞发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518225&idx=2&sn=0c496ddfdfec8c17e1344333f0c218f6&chksm=ea94b97bdde3306d6bc1249b0087f09b8c0a192157a52d43e8f6b5b08e18465335d8518ce100&scene=21#wechat_redirect)

[Okta 支持系统遭攻陷，已有Cloudflare、1Password等三家客户受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517967&idx=1&sn=a0c2ff2dfd52aa69d170f3e95247f143&chksm=ea94b665dde33f73c593e4082e0b1ee4e39fca8e1f3c753c75baf229f798e18e28af2788be4b&scene=21#wechat_redirect)

[黑客攻陷Okta发动供应链攻击，影响130多家组织机构](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513692&idx=2&sn=9edbf81f8e756e90d33627cdfe3796f3&chksm=ea948736dde30e20a3b8750b3189dd23d0baf268f08e98448ec6421a9d7649d3cfc08f11f960&scene=21#wechat_redirect)

[Okta 结束Lapsus$ 供应链事件调查，称将加强第三方管控](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511475&idx=1&sn=1ea2d1ecbccc18f96cf4a2042cea226d&chksm=ea949cd9dde315cf066c77d11309916d7926f24db191be889382dbb7926399c047ad7487ee78&scene=21#wechat_redirect)

[Okta 提醒：社工攻击正在瞄准超级管理员权限](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517538&idx=2&sn=8b83afe723575b7a69c7ea7a0c21dbd2&chksm=ea94b408dde33d1e969877340c12536b88f0e6874c0bf635c1489627d5749af02612fca74ee6&scene=21#wechat_redirect)

[《软件供应商手册：SBOM的生成和提供》解读](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511570&idx=1&sn=a8eda02cab19a290202dd91895bd3887&chksm=ea949f78dde3166e104a4d6a2c2c9e1b32d673f6589993a2f2bfb94740bdc6cdc0088dc8c273&scene=21#wechat_redirect)

[Telegram 和 AWS等电商平台用户遭供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517920&idx=2&sn=9b81bba53ca92b9dba48012df9a9d2cb&chksm=ea94b78adde33e9c5b9a7a2184d0c433e97efba3d73c58471d585199cd6d4d88409f7bd57770&scene=21#wechat_redirect)

[美国商务部发布软件物料清单 (SBOM) 的最小元素（上）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509892&idx=1&sn=f149d024a5a8742859d3b08d90a9111e&chksm=ea9496eedde31ff8e60949842119828151d8a0200b56b5f524e2851e9a5913ba90b605ad7fed&scene=21#wechat_redirect)

[美国商务部发布软件物料清单 (SBOM) 的最小元素（中）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509894&idx=1&sn=b4815181d043ae4843fd1d3cea5e196b&chksm=ea9496ecdde31ffa29e43cbaf6c60811908b0eb21e9fd1e23d7c161ae675cb83b35359bcfb08&scene=21#wechat_redirect)

[美国商务部发布软件物料清单 (SBOM) 的最小元素（下）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509930&idx=1&sn=3573aa307f009e3709fcbb2ac5498e66&chksm=ea9496c0dde31fd6d2f330cd5526fe409c08648ef2236d4674ae043a9939d95df908121c8f93&scene=21#wechat_redirect)

[速修复MOVEit Transfer 中的这个新0day！](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516712&idx=2&sn=a69d93a9d282a667bbbf33bc190b4dfb&chksm=ea94b342dde33a545caba266547e0a3d88b670ddfb23236984d8f468dfbefe639a55bb220239&scene=21#wechat_redirect)

[MOVEit 文件传输软件0day被用于窃取数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516660&idx=1&sn=bb8f16701a800011a7e9bc8857cd59d2&chksm=ea94b09edde33988e2fee2cb9c23d0031149201a1722cfabc8899b76b31016a44a835836d8a9&scene=21#wechat_redirect)

[MSI UEFI 签名密钥遭泄漏 恐引发“灾难性”供应链攻击](http://mp.weixin...