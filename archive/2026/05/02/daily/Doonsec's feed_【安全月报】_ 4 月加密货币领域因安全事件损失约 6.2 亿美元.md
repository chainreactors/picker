---
title: 【安全月报】| 4 月加密货币领域因安全事件损失约 6.2 亿美元
url: https://mp.weixin.qq.com/s/GKhk7rdUvjhmLSPj8piyMg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:28:09.327084
---

# 【安全月报】| 4 月加密货币领域因安全事件损失约 6.2 亿美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXzdjicicDOowkziaicdjIhCJxbhzRJGmktDF5ickM4K3gZamx3g3s1FKGjU0ibKy96ROSmqpUliak24ZibXicgmnXjgsbD6CXqLibdd2RgQU/0?wx_fmt=jpeg)

# 【安全月报】| 4 月加密货币领域因安全事件损失约 6.2 亿美元

原创

零时科技
零时科技

零时科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXyqBBpc49jSTRFwgbSOhtNlVF1wD1RbHsOGGk5HhIFvqyibcAKPZlTZ77h79RHLGdLzlR4X7LDtzSiaiaU6VApC98pKQUNVIib5Vics/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXzcMjXTmiae6WficnU4icOcxuNeFXvbpUtTjDFHTZc2wA1oeydp0N3kSs0MHLXoB3DxWeDGNQ1CZdl78vvF4Z5dib5Pu7VlBibib1gGE/640?wx_fmt=jpeg)

零时科技每月安全事件看点开始了！据多家区块链安全监测平台统计，2026 年 4 月加密货币领域安全态势呈现“协议攻击集中爆发，国家级黑客主导损失”的鲜明特点。**当月因安全事件造成的总损失超过 6.2 亿美元，是自 2025 年 2 月以来最严峻的单月损失纪录。**

当月整体损失中，黑客攻击与合约漏洞相关的损失约 6.08 亿美元，钓鱼诈骗及 Rug Pull 相关损失约 1215 万美元。协议黑客攻击共发生至少 12 起，其中仅 KelpDAO 和 Drift Protocol 两起攻击事件就合计造成损失约 5.77 亿美元，占月度总损失的 93 %。值得注意的是，多起重大攻击已归因于有国家级背景的黑客组织，其攻击方式从单纯的“财务动机盗窃”升级为“系统性渗透”，攻击对象从单一协议扩展至跨链基础设施及团队外围人员，令传统依赖智能合约审计的防御体系严重失效。

**黑客攻击方面**

典型安全事件 ***5*** 起

**• KelpDAO 跨链桥攻击**

**损失金额：**约 2.93 亿美元

**事件详情：**4 月 18 日（UTC 时间），流动再质押协议 KelpDAO 基于 LayerZero 的 rsETH 跨链桥遭攻击，核心为跨链验证配置缺陷（1/1 单签 DVN）。攻击者入侵 RPC 节点、伪造跨链消息，在源链无真实销毁的情况下，于以太坊主网凭空铸造 116,500 枚 rsETH。黑客将伪造 rsETH 存入 Aave、Compound 等借贷协议作为抵押品，借出约 2.36 亿美元真实 ETH，引发大规模坏账与流动性挤兑。该事件为 2026 年迄今最大 DeFi 攻击，暴露跨链基础设施单点依赖与配置管理的严重风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXwGN4LS2UKWWphNicTpEV2SYlS8ULgbafG2plnPdRXORQDC9dSicG0ic38I3xBKA8icyKVqnsEgRvfiaE2tqq6nWhlsO0QHg1l1MF88/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXwYglASkgaopFvxogoFiaKXvnXStIibdsJOibAicAhicdoqFClptIOKxxryh1YEs3aYSIj82mraU4eMA1picbdt74LKuVHQaQe3SMOkc/640?wx_fmt=jpeg)

**• Drift Protocol 社会工程学攻击**

**损失金额：**约 2.85 亿美元

**事件详情：**4 月 1 日，Solana 生态头部去中心化永续合约平台 Drift Protocol 遭有组织社会工程学攻击，非智能合约漏洞，核心为多签治理与人员管控失守。攻击者长期潜伏，伪装成专业做市商与项目核心团队建立信任，利用协议 2/5 多签无时间锁的配置，诱导两名多签成员盲签恶意交易，并借助 Solana Durable Nonce 机制延迟执行。4 月 1 日攻击者触发预签名交易，12 分钟内完成 31 笔转账，掏空协议核心金库，资金快速跨链分流，成为 2026 年迄今最大 DeFi 安全事件、Solana 史上第二大攻击，暴露了项目多签治理与人员安全管理的短板。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uxthuhh3eXzicMnZMFzx7xaeibdVPqicduYxqAeW97R0CjgPOsQ3nM9vaX5dyIxGTzibCiaTusDCibqd0yQSE4dFXnLAuwyo6ekoMiciaiaog4CjrIPk/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXwzhlibgjpoT045909T8gTbDsom65jFcujdFlrRyc9g3R8zeVXIV12a3aKAUKgdRJ7n2pNiaF9LRmJ5MdOlPvHcdiay1nVCQJVgpM/640?wx_fmt=jpeg)

**• Rhea Finance 滑点保护漏洞攻击**

**损失金额：**约 1840 万美元（其中 1120 万美元已追回或冻结）

**事件详情：**4 月 16 日，NEAR 生态借贷协议 Rhea Finance 遭遇攻击，攻击者利用保证金交易模块中的滑点保护逻辑缺陷，在单次交易中非法提取大量资产。事件发生后，约 1120 万美元已被追回或冻结，其中包括攻击者主动归还的部分 USDC 和 NEAR 资产，以及 Tether 协助冻结的约 434 万美元 USDT。

**• Vercel 生态供应链攻击**

**损失金额：**超 1000 万美元

**事件详情：**4 月 20 日，知名 Web 开发平台 Vercel 遭受供应链攻击，攻击者通过入侵团队账户植入恶意代码，波及多个依赖Vercel部署的加密项目前端。至少 3 个加密项目的前端遭到劫持，用户在连接钱包时被引导签署恶意交易，导致资产直接转至攻击者地址，后续排查仍在继续。
此为 4 月开发者与供应链安全事件的典型代表，类似攻击模式涵盖 npm/PyPI 软件包植入后门，反映出针对 Web3 上游基础设施的定向打击已成为黑客的常态化攻击路径。

**• Volo Protocol 漏洞攻击**

**损失金额：**约 350 万美元

**事件详情：**4 月 22 日，Sui 生态流动性质押协议 Volo Protocol 遭遇安全漏洞，攻击者从三个特定金库中提取了约 350 万美元资产，涉及 WBTC、XAUm 和 USDC。官方确认此次漏洞仅涉及这三个金库，其他约 2800 万美元 TVL 资产未受影响，并承诺自行承担此次损失，不会将损失转嫁给用户。

**Rug Pull / 钓鱼诈骗**

典型安全事件 ***6*** 起

(1)  4 月 17 日，0x37638 开头地址的受害者在签署了一笔看似普通的交易——以太坊上的多重调用——后损失了 310,642 美元。

危险之处在于：这笔授权乍一看是看不见的。

(2)  4 月 20 日，0x5d908 开头地址的受害者在以太坊上签署了一笔钓鱼性质“increaseApproval”签名后，损失了 3 枚 WBTC（价值 22.1 万美元）——这些 WBTC 刚刚从 Aave 平台中提取出来。

(3)  **假冒 Ledger Live 应用钓鱼攻击**

**损失金额：**约 950 万美元

**事件性质：**4 月 7 日-13 日，一款假冒 Ledger Live 的恶意应用程序成功绕过苹果应用商店审核并上架，一周内造成至少50名受害者损失约 950 万美元加密资产。其中三名单一受害者损失超过百万美元：4 月 8 日被盗走 195 万美元的 BTC、ETH 和 stETH，4 月 9 日被盗走 323 万美元的 USDT，4 月 11 日被盗走 208 万美元的 USDC。

(4)  **仿冒 imToken 官网钓鱼诈骗**

**损失金额：**未披露具体金额

**事件性质：**4 月集中爆发，攻击者制作高仿 imToken 网站，通过搜索引擎引流，以“安全验证”为由诱导用户输入助记词。恶意 APP 随后窃取私钥并转移资产，卡巴斯基等机构已就此发布多次预警。

(5)  **“长城易趣拍” 平台 Rug Pull**

**损失金额：**超 500 万美元

**事件性质：**4 月 23 日，不法分子冒充国企运营 “长城易趣拍” 平台，诱导用户将资金转入境外交易所兑换代币 CCRWA，随后平台关停无法提现，多名投资者单户损失超百万元，涉案金额超 500 万美元。

(6)  **Quickswap Discord 服务器入侵**

**损失金额：**具体金额仍在统计中

**事件性质：**4 月 6 日，去中心化交易协议 Quickswap 官方 Discord 服务器遭入侵，攻击者利用被控制的管理员账号发布钓鱼信息，诱导用户连接虚假“紧急迁移”网站并输入私钥或签署恶意交易，引发大规模用户资产安全风险。

**总结**

2026 年 4 月区块链安全事件的核心特征可概括为三个关键词：**集中爆发、国家级渗透、系统性传导。**

本月总损失超过 6.28 亿美元，是自 2025 年 2 月以来加密行业最严峻的单月损失纪录。协议黑客攻击共发生 12 起以上，KelpDAO（ 2.92 亿美元）、Drift Protocol（ 2.85 亿美元）、Rhea Finance（ 1840 万美元） 为当月损失最大的三起攻击事件。

攻击手法全面升级：跨链桥配置缺陷、社会工程渗透、供应链投毒、假冒应用突破审核等多维攻击并发。钓鱼诈骗与 Rug Pull 持续高发。国家级黑客主导的复合式攻击，已对传统安全审计与防御体系构成严峻挑战。

零时科技安全团队建议：

**• 个人：**助记词永不透露，仅从官方商店下载应用，警惕AI仿冒信息，定期清理授权，硬件钱包启用物理确认。

**• 项目方：**核心权限多签 + 时间锁，验证节点多源交叉，加强全员防社工培训，审计代码与配置安全。

**• 行业：**建立跨协议风险隔离，共享 APT 威胁情报和黑名单库，普及 AI 钓鱼预警教育。

若需了解更多产品信息或有相关业务需求，可扫码关注公众号或移步至官网：

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXxtqjB59ic8ia3vYtBIO6SlCe6b83Un0TwLXAFw8IPd00NF1c3GfDib0VuUysLreJmc7Uibf3PiaHicjhwuu4wEWQlcvEwLtJu53A4m8/640?wx_fmt=jpeg)

**微信号****｜**noneage

**官方网址****｜**https://noneage.com/

**推荐阅读**

**REVIEW**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXxOBicmlafUFQB8MSo5IAMTDBecN4C8t4YZF4Jd7bpkiaHKKNPXfKbAIbvicWz8CfibmDice24xzGKrP3eM2LUnfZomF90maMPV5EjQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247489933&idx=1&sn=2a660544a85dcd7f42c81e4bbba15dee&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247489933&idx=1&sn=2a660544a85dcd7f42c81e4bbba15dee&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXxnRcGnAYibkSQCuRkclgfC9ia7W8fpqfBEYRicW8g18jq3TFCy7npNWIC1QwJcOhbUn86eLNMgmTKSvOMEvHSPBh83LqXO2Bcs0M/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247490049&idx=1&sn=472418a728531cd1552336437b49ebfd&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247490049&idx=1&sn=472418a728531cd1552336437b49ebfd&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXyqKZ4dXLPh1hx7qbEfDibs0Zoy07adGbBss2icrwHqU4nkmaLwvGBmAFlh4ZwWF6vk2OQXibTwXTUibl4RFILwtEoAJXYy1ENPaKc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247490073&idx=1&sn=ed8510159e9db4f04f57df115573a828&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247490073&idx=1&sn=ed8510159e9db4f04f57df115573a828&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXwGMqKQAvBxurqUiaqNYvl6Hx3HZaL781rk9n5mJgU5KTtkeWLrd16YZxE9uO9JwZx82LxsqtrFhmHjeqEoHkSdF94yNOAgROOQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247489632&idx=1&sn=0a3029d9651d252d0be5e6c3089ad91b&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247489632&idx=1&sn=0a3029d9651d252d0be5e6c3089ad91b&scene=21#wechat_redirect")

END

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXxm9ASB1dxwKYOMZONyRAhjUggXCHBfaibDrkA9ubEhCHUmCqe6RqVfeQaSibUUicouWGYYJSfxhrGYaXibU1FEAnwREWW4JouddcQ/640?wx_fmt=jpeg)

**点击阅读全文 立刻直达官网**

/www.noneage.com/

![](https://mmbiz.qpic.cn/mmbiz_gif/S9WiaEibMtP2jMSTib9czK3UfPsBh0fJscaqZMFhTOvKNaJnEte4bETdtREaSQB3YIA71icwDtrr4oZWAR938LXGcw/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bsePwevmNNzShTOArXjWb1zTPdQ33kGnGZLCkh0Y01w9wUdtDx1F4PHvBfWosmMuTGzWZkYAjbhUdEZfwvYE9g/0?wx_fmt=png)

零时科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bsePwevmNNzShTOArXjWb1zTPdQ33kGnGZLCkh0Y01w9wUdtDx1F4PHvBfWosmMuTGzWZkYAjbhUdEZfwvYE9g/0?wx_fmt=png)

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