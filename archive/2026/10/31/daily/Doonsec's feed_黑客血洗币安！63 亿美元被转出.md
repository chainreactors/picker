---
title: 黑客血洗币安！63 亿美元被转出
url: https://mp.weixin.qq.com/s/RpyPT1UHI1jhsqk3b63i1w
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:18:40.453515
---

# 黑客血洗币安！63 亿美元被转出

# 黑客血洗币安！63 亿美元被转出

原创

小胖快学网络安全
小胖快学网络安全

小胖快学网络安全吧

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

10 月 30 日凌晨，全球最大加密货币交易所币安的热钱包开始往外转钱。

大部分转出在 **20 分钟内**完成，跨了 **10 条区块链**，涉及金额约 **63 亿美元**。

这件事的技术细节值得看，但真正跟你有关系的，在后面。

而事情的起点，币安自己的公告写得很平淡：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl1WLlAYicC65hCuI6w73uueJTyGibuSa7EZ34J6mV0DsVesKg9xvCTLlhPodsTjSpDiaMvx01MguLVMQYODEjtJf9Y86dOzIatKqI/640?wx_fmt=png&from=appmsg)

**一个工程师的笔记本。既没有零日漏洞，也没有攻破签名算法。**

## 一、攻击链只有三步 1.笔记本被入侵 → 2.进入服务容器 → 3.提交未授权提现

```

```

三步，没有一步是“高难度”的。

币安还明确说了一句话：**未发现钱包私钥泄露的证据**。

这句话很关键。意思是：**攻击者根本不需要私钥，他们拿到了“可以提交交易”的权限就够了。**

在加密货币的世界里，私钥一直被当成最后一道墙。这次证明，墙还在，人绕过去了。

## 二、具体是怎么执行的

##

The National 援引 Etherscan 数据：单笔交易转出约 **167,464 个以太坊**（当时约 3.88 亿美元），外加 63 种其他代币。

收款地址是**几小时前才创建的**，资金来自 Tornado Cash 混币服务。

**先建地址、先过一遍混币、再动手。** 准备工作在攻击之前就做完了。

转账跑完只用了 20 分钟。这么快的节奏，靠人盯是来不及的。

## 三、技术上的一个细节：EIP-7702

##

攻击者能走这么顺，靠的是**以太坊的 EIP-7702 标准**。

这个标准允许钱包把执行权限**委托给智能合约代码**。

攻击者借此拿到了币安一个热钱包的**链上执行授权**，而**这个授权没有经过平台正常的审批控制**。

也就是说：**钱包本身没被攻破，是“谁能替它签字”这件事被改了。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl3K0w7JWaMW0FiaQ4AicXu6DDQcGtsIzyPJmicVcPzNmTRjtkQoZYqIHVcWdqb8kQ7G4Q3SHoicErfOcIutXbxvicsA58Ciat1q1Nxqs/640?wx_fmt=png&from=appmsg)

EIP-7702 本意是给钱包更多灵活性。灵活的另一面，是**授权这件事变得更容易被借用。**

## 四、这事跟你有什么关系

##

把这次事件拆成“哪一步没防住”，会得到六类岗位。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl3V1bgYCriciaCvEnXVFFGGPTGsKCP2iafamaChTTpSd8mXqy4cSricSVVUITSpGRoyD6pLIicNVwyFN73uSfGSyJibR9gnibpaUNq80Q/640?wx_fmt=png&from=appmsg)

下面一个个说，每类后面都写了这岗干什么、面试大概会问什么。

### 1.终端安全工程师

###

出事的是工程师的笔记本。这类岗的日常就是：装 EDR、配准入策略、盯异常进程、查谁在往外连。

**面试会问：** 终端被装了远控你怎么发现？域内一台机器被登录了，你能看到什么痕迹？

### 2.云安全 / 容器安全工程师

###

攻击者用那台笔记本进了服务容器。这类岗负责：容器镜像准入、K8s 权限收敛、服务间调用鉴权。

**面试会问：** 一个容器能拿到宿主机权限，你会先查哪几项配置？

### 3.身份与权限管理（IAM）工程师

###

这次不需要私钥就能提现，因为**权限被借走了**。这类岗的核心工作：最小权限、审批流、临时授权、离职权限回收。

**面试会问：** 生产环境大额转账的审批链，你会怎么设计？双人复核怎么防串通？

### 4.威胁情报 / 监控分析师

###

20 分钟跨 10 条链，这么快的动作，靠人肉盯不出来。这类岗负责：规则、告警、异常行为建模。

**面试会问：** 一笔正常用户操作和一次自动化批量转账，你从哪些特征区分？

### 5.应急响应 / 数字取证工程师

###

攻击者用了自毁机制抹痕迹。这类岗负责：保全现场、恢复时间线、判断影响范围、出报告。

**面试会问：** 日志被删了，你还能从哪拿证据？

### 6.安全运营（甲方 SOC）

###

币安说“后续又发现其他入侵点”。一个点堵上还有别的，得有人组织排查、协调各团队、对外对接执法和发行方。

**面试会问：** 一次跨部门的重大安全事件，你怎么排优先级？

**这六类岗，没有一个要求你会挖零日漏洞。**

它们要的是：盯住终端、管住权限、发现异常、出事后查得清。

**而这些面试题考的都是“你在实际环境里做过什么”。** 对没有名校背景的人，这反而是机会。

## 五、这 63 亿，没有一处跟 AI 有关

##

这两年安全行业的注意力，大半在“AI 挖漏洞”上。AI 确实让漏洞发现变快了。

但这次，用的是一台被入侵的笔记本、一个被绕过的审批流程、一个新标准带来的授权漏洞。**没有一处跟 AI 有关。**

CoinDesk 引用的安全公司 CertiK 有一句统计说得更直接：**2026 年最大的几起安全事件，起因都是被盗的凭证和设备，不是智能合约漏洞。**

风控的重心，正在从“代码有没有洞”，挪到“人能不能进、权限是不是过大、异常有没有人看”。

星球介绍

一个人走的很快，但一群人才能地的更远。吉祥同学学安全这个[星球🔗](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247486065&idx=2&sn=b30ade8200e842743339d428f414475e&chksm=c0e4732df793fa3bf39a6eab17cc0ed0fca5f0e4c979ce64bd112762def9ee7cf0112a7e76af&scene=21#wechat_redirect)成立了2年左右，已经有600+的小伙伴了，如果你是网络安全的学生、想转行网络安全行业、需要网安相关的方案、ppt，快加入我们吧。系统性的知识库已经有：[《Java代码审计》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484219&idx=1&sn=73564e316a4c9794019f15dd6b3ba9f6&chksm=c0e47a67f793f371e9f6a4fbc06e7929cb1480b7320fae34c32563307df3a28aca49d1a4addd&scene=21#wechat_redirect)++[《Web安全》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484238&idx=1&sn=ca66551c31e37b8d726f151265fc9211&chksm=c0e47a12f793f3049fefde6e9ebe9ec4e2c7626b8594511bd314783719c216bd9929962a71e6&scene=21#wechat_redirect)++[《应急响应》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484262&idx=1&sn=8500d284ffa923638199071032877536&chksm=c0e47a3af793f32c1c20dcb55c28942b59cbae12ce7169c63d6229d66238fb39a8094a2c13a1&scene=21#wechat_redirect)++[《网安面试指南》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247486695&idx=1&sn=85fefa98f17e6f1f2dd745ef5a498a10&token=1860256701&lang=zh_CN&scene=21#wechat_redirect)++[《网安秋招工具箱》](https://mp.weixin.qq.com/s?__biz=MzkzMzcxNTQyNw==&mid=2247489077&idx=1&sn=f9128340c56fa854eaefc179a26c3e37&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl02375f3AgxibiaznHaiaAk2sWzyuun9ZBmPLxgheeSiaJzNichu5le6AZL3VC2rCibt03ZerfJdbZHrdO7xVlhK1bBvibZu3roTiaBnXo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl2VwngJiadfViaASCxBjVejDIu8WVCO13UB0E4HRJR3IcfhibMibicuRH9VXMPp0w50yr2kiakaFAsaMUDbIjS35Nb9wOS7dabJiaywNY/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Oh2kiaia4icySDqrNyBCHuYdPugU7RJlWianw9FiaCn6EH2P31ATvZJnibr9IgONEx77AFiaEib2Bnh807WMHcrr9ibqdMA/0?wx_fmt=png)

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