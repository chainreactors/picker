---
title: 【安全月报】| 3 月加密货币领域因安全事件损失约 1.98 亿美元
url: https://mp.weixin.qq.com/s/ZPVdplg1XrzOduZvqhpAQA
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:02.500256
---

# 【安全月报】| 3 月加密货币领域因安全事件损失约 1.98 亿美元

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXyBian5vawDCs8UJdPh6bHtmiayyLkwA7iaEKeiag6kRpQgUXRVzMsmCW1ibNsicSOn1QdWLBUicws1fFcS2xSVQjiaqAjVWZL6LUQ0xkw/0?wx_fmt=jpeg)

# 【安全月报】| 3 月加密货币领域因安全事件损失约 1.98 亿美元

原创

零时科技
零时科技

零时科技

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXwJGzMB4XxiaLCdz1bH1NC296GJfeMugFrbT0Zpm9b4Eoq5MnFYXOQw454o8MgT4uYp2SgpibJ9KAlNnad9Quj6icndq5EZbd5leo/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXwyiaZUtnibYrFknibhAM2kjuDQib7eIRBqibAsBJkOxTzLYrUgQhW4sQevjCzJbcNTQibygSR3PxjqvrhXtAUtQwias2yibozlImuZYes/640?wx_fmt=jpeg)

零时科技每月安全事件看点开始了！据多家区块链安全监测平台统计，2026 年 3 月加密货币领域安全态势呈现“协议攻击小幅反弹，AI 钓鱼诈骗持续高发”的特点。**当月因安全事件造成的总损失约 1.98 亿美元，**其中黑客攻击与合约漏洞相关的损失约 1.75 亿美元，钓鱼诈骗及 Rug Pull 相关损失约 8300 万美元。

协议黑客攻击共发生 16 起，较上月下降 11.1%，但单笔损失金额有所上升；钓鱼与授权劫持类诈骗事件共发生 22 起，占当月总事件数的 57.9 %，其中 AI 仿冒钓鱼、假客服诈骗成为主要推手。攻击手法持续向“低成本、高收益”的社会工程学倾斜，结合 AI 生成页面的精准钓鱼愈发普遍，个人投资者及中小型项目成为主要攻击目标。

**黑客攻击方面**

典型安全事件 ***6*** 起

**• Resolv协议私钥泄露攻击**

**损失金额：**约 2450 万美元

**事件详情：**3 月 22 日，攻击者通过窃取 Resolv 基础设施的私钥，获得了对 USR 稳定币铸造额度的签名批准权限。黑客先存入 10 万 USDC，却利用被盗私钥非法铸造了 8000 万枚 USR（正常比例仅应获得约 20 万枚），随后将 4478 万 USR 兑换为 11,437 枚 ETH（价值约 2385万 美元），导致 USR 严重脱锚，币价一度暴跌至 0.025 美元。更致命的是，如此关键的“SERVICE\_ROLE”权限竟由单一外部账户（EOA）掌控，而非更安全的多重签名账户，且铸币合约缺乏预言机验证和铸造上限限制。

![](https://mmbiz.qpic.cn/mmbiz_png/uxthuhh3eXweuk4127420Via0n57c28tqRwDicWV2vL7cALPWLx8ABSLu5s6JzOgWTHxmwXRWRdoxZaelyUcdwnlgJzuA3Ifcgs0FlXlhg3ps/640?wx_fmt=png)

**• Bitrefill遭朝鲜Lazarus组织攻击**

**损失金额：**未披露（热钱包资金被盗，超18,500条购买记录泄露）

**事件详情：**3 月 1 日，知名加密货币电商平台 Bitrefill 披露，其遭到与朝鲜 Lazarus 组织相关的黑客攻击。攻击者通过入侵一名员工的笔记本电脑，窃取了遗留凭证，该凭证提供了对包含生产环境密钥的快照的访问权限。凭借此权限，攻击者横向移动，侵入公司基础设施、部分数据库和加密货币钱包，导致热钱包资金被转移。

**• Solv Protocol双重铸造漏洞攻击**

**损失金额：**约 270 万美元

**事件详情：**3 月 3 日，攻击者利用 Solv Protocol 合约的双重铸造漏洞。当用户存入 NFT 时，合约会错误地铸造两次代币。攻击者重复操作 22 次，将 135 枚 BRO 膨胀至 5.67 亿枚，再换成 38 枚 SolvBTC（约 270 万美元），最后转入隐私协议。事后项目方全额赔付用户，并向攻击者提供了 10% 的白帽悬赏。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXwz36k5v6Muia84r9KofUU9xjpQFNRZRib8ghLAmFYZv4XkJ3IwRicOKdrOt6WR7FSSOG8hmiaAr4XUnZ1o7ZI3lPlJTvSQg0Iibb54/640?wx_fmt=jpeg)

**• MT Token 代币设计缺陷攻击**

**损失金额：**约 24.2 万美元

**事件详情：**3 月 10 日，MT Token 是一种通缩型代币，内置交易限制机制。攻击者利用合约在通缩阶段的交易限制逻辑缺陷，结合特殊转账条件的处理不一致，绕过了购买限制获取初始代币。随后，攻击者通过受控的流动性操作和交易操纵 pendingBurnAmount，迫使池子进入异常状态，人为抬高代币价格后获利套现。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXxYyapV2W9R5shuVP5FzicPIPT8NId1oHv3nU4Y8EqoYteps3tMAo62BkD6CfAjFGKWIvJcMQwaFYlrdNRuD1Z9Pr9iahuVYkEJQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXzicAT5g1lPYbTn0B4sOicqdPyp8qpeQ9IGyRv8MVN72sgt5ztm0OTAcCicDSFwTtLPXjKVt8fg1qAM2aeGQ7MCD2LzrZDGhZDayA/640?wx_fmt=jpeg)

**• sDOLA Llamalend 价格操纵攻击**

**损失金额：**约 23.9 万美元

**事件详情：**3 月 2 日，攻击者利用 sDOLA 代币的价格可操纵性（任何人可调用 donate() 函数增加资产），推高 sDOLA 价格，触发 LLAMMA 借贷市场的清算机制。由于 LLAMMA 的健康度计算依赖于可操纵的价格预言机，攻击者成功将用户仓位推至负健康度后发起清算获利。这起事件暴露出借贷协议依赖可操纵代币作为抵押品的系统性风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXzlC7bGxCSBiaFqXcyXXQH911Lib2czvJvIFKzr52oJg82icHwCrNViaDxNed1PzUMaMHNp37KNTh1mh5ibJFwyf7VnKg10C0BibYmGs/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXyu6H5iaCF2KXCKmTG45JgnXCmUUvkKGX8623P0o5BmbIr6Caj5icDGtX4vwvkicX126F2GEZZ4mqaV89iam9rY2rSSibrUibZicGzTqc/640?wx_fmt=jpeg)

**• Gordi NFT 平台攻击**

**损失金额：**约 23 万美元

**事件详情：**3 月 12 日，NFT 流动性交易平台 Gordi 遭受攻击，损失约 23 万美元。攻击者利用平台合约中的漏洞，非法提取用户质押的 NFT 资产。项目方事后承诺对受损用户进行全额赔偿。

**Rug Pull / 钓鱼诈骗**

典型安全事件 ***6*** 起

(1)  3 月 15 日，0x2e4e9 开头地址的受害者在签署钓鱼加额签名后损失了 720,108 美元的 valBUSD + valTUSD。

(2)  3 月 17 日，0x051bb 开头地址的受害者在以太坊上签署钓鱼许可（无 gas 授权）签名后，损失了约 177 万美元的 USDC。

(3)  **虚假 DEX 地址劫持 Rug Pull**

**损失金额：**约 2400 万美元

**事件性质：**3 月 5 日，与X平台用户 @sillytuna 关联的钱包遭遇 Rug Pull，损失约 2400 万美元的 aEthUSDC。约 2000 万 DAI 存放在攻击者控制的两个中介钱包中。受害者发起悬赏，对资金追回给予 10% 奖励。

(4)  **Pudgy World 仿冒钓鱼事件**

**损失金额：**未披露具体金额，但波及11款主流钱包用户

**事件性质：**3 月 17 日，安全公司 Malwarebytes 披露，钓鱼网站 pudgypengu-gamegifts[.]live 仿冒刚上线的 Pudgy World 游戏。攻击者制作了针对 11 款钱包的高仿解锁界面，利用 DOM 覆盖技术伪造浏览器弹窗，并调用 WebUSB API 模拟硬件钱包连接，诱导用户输入助记词。该事件是 3 月 AI 驱动钓鱼攻击的典型代表。

(5)  **OpenClaw 钓鱼攻击**

**损失金额：**约 67 万美元

**事件性质：**3 月 19 日，安全机构 OX Security 披露，针对 GitHub 开发者加密钱包的 OpenClaw 钓鱼攻击蔓延。攻击者利用 AI 生成仿冒页面和恶意软件，诱导开发者下载含后门的工具，窃取 API 密钥和加密资产。

(6)  **Bubblemaps 披露 13 地址钓鱼网络**

**损失金额：**约 2.3 万美元

**事件性质：**3 月 12 日，一个由 13 个关联地址组成的攻击网络已成功利用 35 名用户，累计获利约2.3 万美元，通过系统性的钱包钓鱼和授权劫持收割散户资产。

**总结**

2026 年 3 月，区块链安全呈现三大特征：协议攻击多点爆发、国家级 APT 盯上加密企业、AI 钓鱼成主流威胁。协议攻击共 16 起，Resolv（ 2450 万美元）、Bitrefill（ Lazarus 组织）、Solv Protocol（ 270 万美元） 影响最大，**核心漏洞集中在私钥泄露、业务逻辑缺陷、价格操纵。**钓鱼诈骗占事件总数 57.9%，AI 生成钓鱼页面+蓝 V 账号推广组合手段高发。

零时科技安全团队建议：

**• 个人：**助记词永不联网、不告知他人；警惕 AI 仿冒网站；参与空投 /mint 前验证合约；定期清理授权。

**• 项目方：**私钥多签管理；上线前专业审计；建立应急响应机制。

**• 行业：**共享威胁情报，建立黑名单，推动资金冻结与追回。

若需了解更多产品信息或有相关业务需求，可扫码关注公众号或移步至官网：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXxln7QuDH8zN2PhW5nbXwoHx7Qk0aIXu4sugYIsMXfOZQBUAROcOaBiazkGDjJOzsB6icZvQ1NRwJlq7tmU5XzTYoYJkOBCFz780/640?wx_fmt=jpeg)

**微信号****｜**noneage

**官方网址****｜**https://noneage.com/

**推荐阅读**

**REVIEW**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXyvthDkcRGmsqp0ohtyAKpOzKZtH3icLWfMxu95H9W0YEDzTe9w1rARJTRyJOSEshSArnrb44iaCHQKNicdwwslGspLQlDqhb86bg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247487869&idx=1&sn=fee1aea8e3abdee2aebfe094dafbfdc3&chksm=fc130ac8cb6483de4bb74b397b596f942aefc2bcf6252f3884505e97ff0713d524e5383a2051&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247487869&idx=1&sn=fee1aea8e3abdee2aebfe094dafbfdc3&chksm=fc130ac8cb6483de4bb74b397b596f942aefc2bcf6252f3884505e97ff0713d524e5383a2051&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXySqhGl9JXfgELsQwDNk1IE5cEBPIgBRvF6vNdxGCnXzXbvyHRDibShJeicWdMCLiaFUzCQHQCjoL90gJWzG8VHffVpozXfW1RibmM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247487974&idx=1&sn=91851c6856447643a9b7890fefcc62d3&chksm=fc130a53cb648345ea711f2693d64a960bfabc36a0428bace1892e33cbc8fe7317bbf1e1a7c0&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247487974&idx=1&sn=91851c6856447643a9b7890fefcc62d3&chksm=fc130a53cb648345ea711f2693d64a960bfabc36a0428bace1892e33cbc8fe7317bbf1e1a7c0&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXxQcu8iaC34nsfMqicAo5H6Koz4Prv7UIADTq1mVHiaJZXHJWyiblsmib28KTYrxYwCQYiagNw7481Naky8R7yuH4VbyLicYKgrX2py7A/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247487541&idx=1&sn=ad65034445ef8e9e4816cad96f2b39ee&chksm=fc130b80cb6482960fdeafa504ef9285a125fcc311a1df7c506099d1039e747cd69101fe7393&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247487541&idx=1&sn=ad65034445ef8e9e4816cad96f2b39ee&chksm=fc130b80cb6482960fdeafa504ef9285a125fcc311a1df7c506099d1039e747cd69101fe7393&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXxos2iaDzcvqwsmfwO9JaE9o5icochz062GbUUNCeuztNUFKGhUIzUZTb5segwcdHib37OibXJJfxo8hLdcIoia9IQSmicPneqczUxx8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247487577&idx=1&sn=50c75c165d0327b80fd745fe163a351f&chksm=fc130beccb6482fac9a436bd0a38b94177df1dae6a39fcb84176006891ac6588664f6a3b522f&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247487577&idx=1&sn=50c75c165d0327b80fd745fe163a351f&chksm=fc130beccb6482fac9a436bd0a38b94177df1dae6a39fcb84176006891ac6588664f6a3b522f&scene=21#wechat_redirect")

END

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXy6MjMu8E7TLeHic8xicBBPa49rm7vicocB88D93oQeiaz80FjnhiapvlAB5FH2TwoYuz2CGfLLeTKPAB6B8iaVVSI4nkqG1gUSPGMdg/640?wx_fmt=jpeg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bsePwevmNNzShT...