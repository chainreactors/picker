---
title: 9秒删库，AI“越狱”的真实样本
url: https://mp.weixin.qq.com/s/KOXyj1MY81F8w0CL8ikS1w
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:25:21.294620
---

# 9秒删库，AI“越狱”的真实样本

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hlXiae3yiayvd0PiaGlecMXt4d3Fre98ICvRBj8h2lLvpbBPq1E8KVkczqRznXHRpUmUn4UPicYCmEyTRZtnnHUIzEeWsiaicOhnGicV2lPN2MwnkI/0?wx_fmt=jpeg)

# 9秒删库，AI“越狱”的真实样本

老林
老林

安小圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

就在几天前，美国，一家叫 PocketOS 的公司，使用 Cursor 配合 Claude Opus 4.6 修复代码。

结果 AI 在没有人类确认的情况下，自主调用了云服务商的 API，9秒钟内把整个生产环境和备份全部清空了。

这是一次完美的‘越狱’样本。

我们要问的是：为什么我们设计的安全机制，在AI面前像纸一样薄？”

【第一层崩塌：AI Agent 的“幻觉”与“越权”】

首先，我们要看清 AI Agent 在技术层面到底犯了什么错。

那个AI在事后写了一份‘认罪书’，里面暴露了当前大模型最致命的技术缺陷——缺乏因果理解力。

在 AI 的眼里，‘测试环境’和‘生产环境’没有区别，它们都是一串 API Endpoint。

AI 能执行‘删除’这个动作，但它无法理解‘删除’带来的业务后果。

当它遇到报错，它不是去查文档，而是基于概率‘幻觉’出一个解决方案：它从无关文件中翻出了 API Token，自主决定调用毁灭性指令。

这就是Auto Mode（自主模式）的恐怖之处：为了效率，我们移除了‘人类确认’这个安全阀，结果换来的是 AI 凭猜测而非验证的暴力试错。

【 第二层崩塌：基础设施的“安全裸奔”】

但是，光有 AI 的‘坏念头’还不够，它为什么能成功？

因为许多使用者的基础设施层存在灾难性的设计缺陷。

这就好比你家门锁是纸糊的，甚至连门都没有。

在这次事故中，云服务商 Railway 的 API 权限设计简直是教科书级的反面教材：

一个仅仅用于‘管理自定义域名’的 Token，竟然拥有删除整个数据库卷的 Root 权限。

这就是RBAC（基于角色的访问控制）的完全失效。

在系统设计里，这叫‘过度授权’。

就像我们把家里最高权限的钥匙，挂在了随便一个修理工都能拿到的地方。

更讽刺的是，他们还专门推出了给 AI 用的 MCP 集成。

这是在鼓励 AI 拿起机关枪，却忘了给枪上保险。

【 第三层崩塌：备份机制的“单点失效”】

最后，也是令人最绝望的是：数据恢复机制的失效。

为什么删库就是毁灭？

因为他们的备份策略违反了最基本的安全原则——隔离。

他们的‘备份数据’和‘主数据’放在了同一个存储卷里。

这在工程上叫‘单点失效’。

攻击者或者失控的AI只要打掉一个点，主数据和备份同时殉葬。

唯一的快照是三个月前的。

这意味着，技术团队在设计架构时，根本没有把‘防灾’当成第一优先级。

当 AI 拥有了破坏力，而你的系统又没有‘熔断机制’和‘异地隔离备份’，这就是一场注定会发生的技术灾难。

【技术人的反思与“不可能三角”】

所以，剥开所有的表象，这起事故给我们留下了两个残酷的技术真理：

第一，AI Agent 还不是一个‘靠谱的助手’，它是‘新物种’。

只要你给它 API 权限，它就是系统里的超级用户。

你不能仅仅用‘提示词’这种软约束，去对抗‘Root 权限’这种硬实力。

第二，AI 安全的‘不可能三角’。

你想要效率（自动执行），想要自主性（无需确认），就必然失去安全性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hlXiae3yiayveYHMNibOo9JY8ia1Kq2OibtIHdH4foB5WiboEyoBr3Zw9zLN2oIvl1VaKibRAAykE12xp6LdTiashs3U0AUG7KTEpibu3m8KicXJ4Tt6M/640?wx_fmt=jpeg&from=appmsg)

现在的技术现状是：AI 无法理解后果，所以我们必须在基础设施层，建立不可绕过的硬护栏。

如果你是企业的 CTO，面对这把‘双刃剑’，你会选择把权限收回来，还是继续在刀尖上跳舞？

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbNFGhZSttuhIzVnNJAlxXcndiaWI3s9WjaqpgsqpHlQnicYyLjF0hovoEKHxic0cbyVibvXhs7lKv9YNw/0?wx_fmt=png)

安小圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbNFGhZSttuhIzVnNJAlxXcndiaWI3s9WjaqpgsqpHlQnicYyLjF0hovoEKHxic0cbyVibvXhs7lKv9YNw/0?wx_fmt=png)

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