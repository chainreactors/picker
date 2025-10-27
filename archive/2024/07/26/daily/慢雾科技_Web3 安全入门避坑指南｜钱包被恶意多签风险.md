---
title: Web3 安全入门避坑指南｜钱包被恶意多签风险
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500038&idx=1&sn=00ff98cee22c817942d2e1bce4f8db46&chksm=fddebf81caa93697ba13a1ad0f8eb3baab0c739926912e671c3ac4d81b18467feee1bffae095&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-07-26
fetch_date: 2025-10-06T17:43:19.200304
---

# Web3 安全入门避坑指南｜钱包被恶意多签风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZS1GabAQfoy50sBNV0IibFgs4Sb25IlmYrlOgINsR2uic21Mb1Kmqz8f2C1pq3Jkibl4maJKpJ8UzTQ/0?wx_fmt=jpeg)

# Web3 安全入门避坑指南｜钱包被恶意多签风险

原创

慢雾安全团队

慢雾科技

**背景**

在上一期 [Web3 安全入门避坑指南](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499789&idx=1&sn=917bed32d880d8e31998886371fd12ff&chksm=fddebe8acaa9379c1247b5960d43078b5d86f7a94f05dde976457bbd245862431dfb3121c58a&scene=21#wechat_redirect)中，我们主要讲解下载/购买钱包时的风险，找到真官网和验证钱包真伪的方法，以及私钥/助记词的泄露风险。我们常说 “Not your keys, not your coins”，但也存在即使你有私钥/助记词，也无法控制自己资产的情况，即钱包被恶意多签了。结合我们收集到的 MistTrack 被盗表单，一些用户的钱包被恶意多签后，不明白为什么自己钱包账户里还有余额，却无法把资金转出。因此，本期我们将以 TRON 钱包为例，讲解多签钓鱼的相关知识，包括多签机制、黑客的常规操作及如何避免钱包被恶意多签等内容。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZS1GabAQfoy50sBNV0IibFg0x3up7XeFmduGgicaJElqnk62sYb0aEc2eNlOEtaKcicP0OkiaRe54Yag/640?wx_fmt=png&from=appmsg)

### **多签机制**

我们先简单解释下什么是多签，多签机制的本意是为了使得钱包更安全，允许多个用户共同管理和控制同一个数字资产钱包的访问和使用权限。尽管部分管理者丢失或泄露了私钥/助记词，钱包里的资产也不一定会受损。

TRON 的多重签名权限系统设计了三种不同的权限：Owner、Witness 和 Active，每种权限都有特定的功能和用途。

**Owner 权限：**

* 拥有执行所有合约和操作的最高权限；
* 只有拥有该权限才能修改其他权限，包括添加或移除其他签名者；
* 创建新账户后，默认为账户本体拥有该权限。

**Witness 权限：**

这个权限主要与超级代表(Super Representatives) 相关，拥有该权限的账户能够参与超级代表的选举和投票，管理与超级代表相关的操作。

**Active 权限：**

用于日常操作，例如转账和调用智能合约。这个权限可以由 Owner 权限设定和修改，常用于分配给需要执行特定任务的账户，它是若干授权操作（比如 TRX 转账、质押资产）的一个集合。

上文中提到，新建账户时，该账户的地址会默认拥有 Owner 权限（最高权限），可以调整账户的权限结构，选择将该账户的权限授权给哪些地址，规定这些地址所占权重的大小，以及设置阈值。阈值是指需要签名方权重到达多少才能执行特定操作。在下图中，阈值设置为 2，3 个被授权地址的权重都为 1，那么在执行特定操作时，只要有 2 个签名方的确认，这个操作就可以生效。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZS1GabAQfoy50sBNV0IibFgT2T41IFaXBwibFTzaF3TzBZ3ohhWve3emxgiaHv8tlAfKQKyYiaNDz9Aw/640?wx_fmt=png&from=appmsg)

(https://support.tronscan.org/hc/article\_attachments/29939335264665)

###

### **恶意多签的过程**

黑客获取用户私钥/助记词后，如果用户没有使用多签机制（即该钱包账户仅由用户一人控制），黑客便可以将 Owner/Active 权限也授权给自己的地址或者将用户的 Owner/Active 权限转移给自己，黑客的这两种操作通常都被大家称为恶意多签，但其实这是一个广义的说法，实际上，可以根据用户是否还拥有 Owner/Active 权限来区分：

**利用多签机制**

下图中，用户的 Owner/Active 权限未被移除，黑客给自己的地址授权了 Owner/Active 权限，此时账户由用户和黑客共同控制（阈值为 2），用户地址和黑客地址的权重都为 1。用户虽然持有私钥/助记词，也有 Owner/Active 权限，但无法转移自己的资产，因为用户发起转出资产请求时，需要用户和黑客的地址都签名，这个操作才能正常执行。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYP0ibl2HicGQxgHeFukXXyk0jtprwLRRsNhFPXqhl8QUxX3hs22H0dicpE0SYeNqSU6EC5Rd8qyicMxQ/640?wx_fmt=png&from=appmsg)

虽然被多签的账户执行转出资产的操作需要多方签名的确认才可以实现，但是向钱包账户入账是不需要多方签名的。如果用户没有定期检查账户权限情况的习惯或者近期没有转出操作的话，一般不会发现自己钱包账户的授权被更改，那么便持续受损。如果钱包内的资产不多，黑客可能会放长线钓大鱼，等待该账户积累了一定数字资产后，再一次性盗取所有数字资产。

**利用 TRON 的权限管理设计机制**

还有一种情况是黑客利用 TRON 的权限管理设计机制，直接将用户的 Owner/Active 权限转移给黑客地址（阈值仍为 1），使得用户失去 Owner/Active 权限，连“投票权”都没有了。需注意，此处黑客并不是利用多签机制使得用户无法转移资产，但大家习惯上称这种情况也为钱包被恶意多签。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYP0ibl2HicGQxgHeFukXXyk0Mv9LvNo2fwXDA02ZoULqCbXhXibpiahQ6dNmZqUEJuOwKsevfEWFG3cA/640?wx_fmt=png&from=appmsg)

以上两种情况造成的结果是一样的，无论用户是否还拥有 Owner/Active 权限，都失去了对该账户的实际控制权，黑客地址获得了账户的最高权限，可实现更改账户权限、转移资产等操作。

### **恶意多签的途径**

结合 MistTrack 收集到的被盗表单，我们总结出了几种钱包被恶意多签的常见原因，希望用户遇到以下几种情况时，提高警惕：

1. 在下载钱包时，未能找到正确的途径，点击了电报、推特、网友发送的假官网链接，下载到假钱包，结果私钥/助记词泄露，钱包被恶意多签。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYP0ibl2HicGQxgHeFukXXyk0ADvcERXxSoEmTAwEA2uch4EpFOScWqho3bWlP9F93rkR4lFES1gicbw/640?wx_fmt=png&from=appmsg)

2. 用户在一些出售加油卡、礼品卡、VPN 服务的钓鱼充值网站输入了私钥/助记词，结果失去自己钱包账户的控制权。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYP0ibl2HicGQxgHeFukXXyk0M0PA0eghX21MGuHDgicD5a0EuUyFEaY5ibKFqiag1eTsaicJvB1MPpoYBw/640?wx_fmt=png&from=appmsg)

3. OTC 交易时，被有心之人拍到私钥/助记词或以某手段获取账户的授权，随后钱包被恶意多签，资产受损。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYP0ibl2HicGQxgHeFukXXyk0EfWoQP5O5LqNk88QiafiaW4DMem8crAgnerjVZklytkwt19Xnib8PFPTg/640?wx_fmt=png&from=appmsg)

4. 一些骗子把私钥/助记词提供给你，称他无法提取钱包账户里的资产，如果你能帮忙的话可以给你酬劳。虽然这个私钥/助记词对应的钱包地址确实存在资金，但无论你给多少手续费、手速多快都提不走，因为提币权限被骗子配置给了另一个地址。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZS1GabAQfoy50sBNV0IibFg2fK7FEylAz9YcBSb9TtD8DzKSicnf1x9swOIrmpWBRk5jUeFribSPSJA/640?wx_fmt=png&from=appmsg)

5. 还有一种较为少见的情况是用户在 TRON 上点击了钓鱼链接，签名了恶意的数据，随后钱包被恶意多签。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYP0ibl2HicGQxgHeFukXXyk0UwPaxqib9O88rtF7cpQpGiaia9RmxryaDtVVRyy1b6M5V6ibR3sM5zY2ibw/640?wx_fmt=png&from=appmsg)

### **总结**

在本期指南中，我们主要以 TRON 钱包为例，讲解了多签机制、黑客实施恶意多签的过程和套路，希望帮助大家加深对多签机制的理解和提高防范钱包被恶意多签的能力。当然，除了被恶意多签的情形之外，还存在一些比较特别的案例，有的新手用户可能因操作不慎或缺乏了解，误将钱包设置成了多签，导致需要多个签名才能进行转账。此时，用户仅需满足多签要求或在权限管理处将 Owner/Active 权限只授权给一个地址，恢复单签即可。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZS1GabAQfoy50sBNV0IibFg1oWqjUwlPr1wS9LmrgSjBG84H0nJYVyMOm8IL8Wiadsjtucdhb37icbQ/640?wx_fmt=png&from=appmsg)

最后，慢雾安全团队建议广大用户定期检查账户权限，查看是否有异常；从官方途径下载钱包，我们在 [Web3 安全入门避坑指南｜假钱包与私钥助记词泄露风险](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499789&idx=1&sn=917bed32d880d8e31998886371fd12ff&chksm=fddebe8acaa9379c1247b5960d43078b5d86f7a94f05dde976457bbd245862431dfb3121c58a&scene=21#wechat_redirect)里讲过如何找到正确的官网和验证钱包的真伪；不点击不明链接，更不轻易输入私钥/助记词；安装杀毒软件（如卡巴斯基、AVG 等）和钓鱼风险阻断插件（如 Scam Sniffer），提高设备安全性。

**往期回顾**

[慢雾(SlowMist) 为香港浸会大学金融课程获奖者提供“慢雾网络安全奖”](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500008&idx=1&sn=fa9a8c6b1d89653d784131884f958cce&chksm=fddebe6fcaa93779e7cc92cace20762718781c556b5b6bf15226a693d2b68459b35e637fd06c&scene=21#wechat_redirect)

[慢雾：公链安全审计指南全面升级，并新增 Layer2 安全审计方法](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499970&idx=1&sn=949d5a2fa1ce82709818e8fcc37ccad0&chksm=fddebe45caa9375310a4fccccd715ec76bb09b9ccfd7f0e692ae3dbca35b1ffdd6fec7138722&scene=21#wechat_redirect)

[慢雾：安全审计检查项之账户抽象钱包](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499961&idx=1&sn=c443ff0b1d639a5c022697db117f4652&chksm=fddebe3ecaa9372839c97a4d00dc57e9cb903326a933528fe5927149d065ecfb025128655d86&scene=21#wechat_redirect)

[慢雾：2024 Q2 MistTrack 被盗表单分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499939&idx=1&sn=9a19ea41c058d225c6ccbb21736f8923&chksm=fddebe24caa93732fab9dc5b29801e718e4a72db379f53db6a5b0532d4f22e957f6221946f2f&scene=21#wechat_redirect)

[慢雾出品 | 2024 上半年区块链安全与反洗钱报告](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499923&idx=1&sn=e075b86887cefa622b8a8318be269d49&chksm=fddebe14caa937024e5926e5524ace12fd4413510f51c8d8bdab1b01db4f16239b2cf8735a73&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togv4VUdq4r7iak19Hta2pfbzPrGohPNR71WxPKrBoK9nyibPVL7ssCuW3yA/640?wx_fmt=png)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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