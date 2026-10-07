---
title: 我渗透到一个黑客集团：一年半时间，35xa0万美元换xa07500xa0万美元冻结
url: https://mp.weixin.qq.com/s/FJ-7GATBXIROQEmbojtIyw
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:54:02.021900
---

# 我渗透到一个黑客集团：一年半时间，35xa0万美元换xa07500xa0万美元冻结

# 我渗透到一个黑客集团：一年半时间，35 万美元换 7500 万美元冻结

原创

ZachXBT
ZachXBT

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MlzViaAOLibl13tvs6hl0MuicxFeE8j4XMBjzZl3Hdywhh2qs5Tz1UgSqa3Moz4xv24f2f6Eib2ITraAZDWnYMPMhpE3Z4u9lVkCw/640?from=appmsg)
> **导语**：独立链上侦探 ZachXBT 在 10 月 5 日发布一条 12 段的长推文，按时间顺序把他如何以"客户"身份打入为 Lazarus Group 洗钱超过 10 亿美元的团伙、用自掏腰包的 35 万美元损失撬动 7500 万美元资金冻结的全过程摆出来。本文严格按原推文顺序逐条拆解，把每个链上动作翻译成可复用的方法论。

![ZachXBT 调查截图：Bybit 盗案与受制裁地址](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MSmQcmffrnTzyCYKQ3sISOxHMOMrJk9tNYepuicLfO7SdVvJMVU7siaChnL7zxTSicrENbToQmbUcI3BndWERQRakDkWbiaLf8b7A/640?from=appmsg "ZachXBT 调查截图：Bybit 盗案与受制裁地址")

---

## 第一步：观察——15+ 账号公开求洗钱

2025 年 2 月，15 亿美元规模的 Bybit 盗案刚被披露并归因到 Lazarus Group 旗下的 TraderTraitor。ZachXBT 在公开的 Telegram 群组和 Discord 服务器里发现一个反常模式——超过 15 个账号在公开求"能接 Bybit 盗案赃币的换币订单"。这等于把"我有赃币、想变现"的广告打到阳光下。

这一步的红队价值：链上侦察不是坐在屋里盯仪表盘——犯罪分子也用 IM（Instant Messaging，即时通讯）做生意。公开群组里的换币请求本身就是情报信源。

## 第二步：选定目标——锁定 Jimmy Green

ZachXBT 顺着 Bybit 关联的投诉账号一个个联系过去。其中一个用了"Jimmy Green"这个化名。

* TG User：long\_991
* TG ID：7635649994

这一步的关键：选目标要看资金流向的"支点"。Jimmy 是中间商，不是直接盗币的黑客——这种角色最有情报价值，因为他两头通吃。

![Jimmy Green 在 Telegram 上的资料](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MeebSPvF3kVIukdn8EWpXZvMA6uCtia1bTQKVTFws4icZO1ovickIPNicIncTKT0TP1Sziag0p1SeDH19jyzF3oibFvhIhx69qhAFKM/640?from=appmsg "Jimmy Green 在 Telegram 上的资料")

## 第三步：备资——2025 年 3 月 6 日入资 34.97 万 USDC

为了"客户身份"看起来真实，ZachXBT 在 2025 年 3 月 6 日往一个新地址充了 349,700 USDC，准备做几笔交易。

他的地址： `0x073256b50d66a7eb005f2a504d0a4fb6ea62a276`

这一步的红队方法论：渗透要有真实资产作"门票"。情报员自己掏钱做钓饵——损失要自己扛，没保险。

## 第四步：首笔交易——地址 0xbaa5 直追 Bybit

Jimmy 提供地址 0xbaa5，让 ZachXBT 把 USDC 转过来换取他的 Tron（波场）链 USDT。

链上追查结果：

* 0xbaa5 的 gas 费由 0xbcb4 资助
* 0xbcb4 直接可追溯到 Bybit 盗案赃币
* 已经在 Bybit 盗案公开黑名单站点上被标记

Jimmy Green 的完整地址：

* `0xbaa551da0ae0c93025d9a983a68025a27dc15337`（ETH）
* `TPwXAPwYaDCm7GrzNFiMmNnofrxEVURXRM`（TRON）

![Jimmy 提供的地址溯源到 Bybit 黑名单](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MD3qPfFFvP8lKibNvaPGkmYpgbPib7Ew6GvdTW4c9wac31jTQs7RCj2MqxGH7Ys4luCRDbfEwbr0dF28KSZyqGcBpIGpJr9Cx6Y/640?from=appmsg "Jimmy 提供的地址溯源到 Bybit 黑名单")

这一步展示了链上追踪的核心动作：每个新地址都要查"上游资金来自哪"。一笔交易 + 一笔 gas 费，就能把对方扯进盗案溯源图里。

## 第五步：加码信任——多笔小额交易铺垫

完成几笔额外交易后，ZachXBT 把 Jimmy 的信任级别"养"上去。

Jimmy Green 的更多地址：

* `0x1893ef01e700b1359280e11736d1b89fe97ed216`（ETH）
* `TS5hY6mm6UsCLNdVDWnsRA69LuAwfdn158`（TRON）
* `TMGjdFeBf9T6kGB9ZmLzeaAPYWBokuyTuS`（TRON）

![Jimmy 的多链地址清单](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OnWkHKLYbvFAib4jgmUW8NfeCWsofBjB8oSpxSwqGBYQicsV0lzgyLledzfdkFPPkHw9Ylz5WxiabU96WhVs2d6Kc2UwrWtlBic84/640?from=appmsg "Jimmy 的多链地址清单")

这一步是社会工程学的经典套路——用小额高频交易养熟关系，等对方开始主动"交底"。

## 第六步：对方主动泄密——团队规模与运作模式

信任度起来后，Jimmy 主动开始聊 Bybit 资金调度——而且常常比链上动作早一天预告。

ZachXBT 的两个验证案例：

1. Jimmy 说"明天会往 Solana 转一批"，第二天链上确实如此
2. Jimmy 自称团队洗了 Bybit 盗案 15 亿赃款中的大部分，与 ZachXBT 观察到的洗钱模式吻合

到这一步，ZachXBT 意识到自己要继续以每单 5% 的损失当"门票"，尽可能快地抓取可行动的情报。

![Jimmy 自曝团队规模](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OmWiaHaq9OVkPRTyib0gWV7ShPmf7cTKoLtNUAadQBzLHstXB6oNMVSEfricXwCna21d8H18ngk0iaZvz7IxovzoicyFcRRyia6BwOE/640?from=appmsg "Jimmy 自曝团队规模")

## 第七步：桥接资金截图——链上秒级对账

2025 年 3 月 12 日，Jimmy 主动发了一张他正在桥接（Bridge，跨链转移）资金的截图。ZachXBT 用金额和时间戳在 THORChain 浏览器上做对账——这条订单在他发图后几分钟内就上链了。

交易哈希： `81a85130b36057428e64b6f97215f77b5a197776a8f1b3a61c8cd0ee1ebfa8c1`

![THORChain 链上桥接记录](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PjFM2SxbLI6ZE3BfwCYdfV19lldQnROQVf9icRwic1csibRZ3LUXSybVD9mVtJ9MLD5C6RrV3eN00vulSsNiaVgia2OogOnMxa7enI/640?from=appmsg "THORChain 链上桥接记录")

这一步是链上情报的硬功夫——对方发图的同时，浏览器已经把数据送上来了。

## 第八步：Solana 集群曝光——1200 万美元赃币实时换链

Jimmy 还分享了 3 个 Solana 地址。这三个地址暴露了一个价值 1200 万美元以上的 Bybit 赃币集群，正在按 BTC → ETH → SOL → Tron 的路径实时换链。

后续动作：

* 集群里 44.2 万 USDT 被 Tether 冻结
* 该集群还用了 Uniswap 流动性池里非主流代币做"洗币新招"

Jimmy Green 的 Solana 地址：

* `9gSwa2Mew9P21Wxs8nFgDujTurKZx1nBEVRv6K5sJP6e`
* `EvZJGsDymrSUQyF23HLKEgUpjfd9XN1GTmm8AG6pFS7H`
* `8S6T5gL2w5z4M9TCehMgQjxVm3Q6R7WDHp6WFfbtZSAy`

Tether 冻结地址：

* `0x652d7f9edaaa8891be2de74ea568d70af823d89e`

![Solana 集群资金链路图](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NHicO3qyibDPLb176r7H61FHdREE4mG8dYbnVibLFSNPgV24sskWkwb4wvib2gcbvDejqamfPyTplNG0RMUq0kPkNpIWzRFfWSIfE/640?from=appmsg "Solana 集群资金链路图")

## 第九步：交叉验证——2024 年的 30 万冻结到 Poloniex

Jimmy 提到"他认识的团队"在 2024 年有大约 30 万美元被冻结。ZachXBT 一查链上——实际数字是 332,000 USDC，来自 Poloniex 盗案。

Jimmy 还提到替另一个客户洗了 300 万美元的诈骗赃款。ZachXBT 把这些钱追到了 Huione Guarantee 的一个热钱包——这家平台已经被 OFAC 制裁，前董事长已被捕。

![Poloniex 盗案链上溯源](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MwpoxzwlA8icRleUczq0BC1jMo6z8hvH6mwHu1icbKa2I1sZ54lBo4p0tg96ibUMFOXvssyiacPxKRWwR0RwNLQglk3ApDIzOTdwM/640?from=appmsg "Poloniex 盗案链上溯源")

这一步展示了情报交叉验证的价值：对方无意间说的细节，往往是另一条独立案件的关键线索。

## 第十步：闲聊铺垫——生活细节也是情报

在正经情报交接的间隙，ZachXBT 和 Jimmy 聊过不少生活琐事——打麻将、猎野兔、吃减脂餐、家庭生活、迪士尼度假。

ZachXBT 在最后备注："他语法别扭是因为用翻译软件。"

![Jimmy 的日常生活记录](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6O99rH2EpdIrkzQy7cONLOQIp7ONriaoUXQpBoFic18YJMlSia2hrX10jvOA5eH8gicmHTHyAhNl0KCrjVTBIWOoPBxMtBm3YInKqs/640?from=appmsg "Jimmy 的日常生活记录")

这一步的红队价值：建立人格立体度。对方觉得你"懂他"，才会在关键问题上放松警惕。

## 第十一步：自掏腰包——35 万美元无回报

ZachXBT 在最后坦白这次行动的全部代价：

* 自掏腰包 349,700 美元
* 每单亏 5%，没有 Jimmy 跑路的兜底保证
* 还要承担来自犯罪团伙本身的人身风险

但收益是实在的：自 2022 年起，他已经推动了 7500 万美元以上的、与朝鲜相关案件的链上冻结。

情报一旦成形，会立即同步给私营调查员和办案执法机关。由于调查敏感度，他没法第一时间公开——"这也是我这份工作里最让人无奈的地方。我手里还有其他几个重大案件的发现还没来得及公开"。

![ZachXBT 收尾呼吁支持](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PHibWWcFgsObfXR0CdyharkibSbChgMlHJic9EGHU1rCjYINfadCZLL4aRLsFQl5nzmTYkrAWPq6Gta08emT8Rck3J5ic3aopetO8/640?from=appmsg "ZachXBT 收尾呼吁支持")

---

## 红队方法论小结

整篇看下来，ZachXBT 这套链上调查的操作可拆成四步：

1. **公开信号捕获**：盯着 Telegram/Discord 公开群组里"求洗钱"的反常广告
2. **链上资金拓扑**：每给一个新地址就追上游 gas 来源，几笔交易就能画出盗案溯源图
3. **社会工程学养熟**：用小额真实交易养信任，等对方主动泄密
4. **多源交叉验证**：把对方闲聊里的小数字和别的盗案时间线对账，往往能揪出独立案件

最大的成本不是工具也不是技术——是钱与时间。ZachXBT 一年半时间里个人承担了 35 万美元的机会成本，没有赞助商兜底，全靠捐款和基金会拨款撑下来。

---

## 原文出处

* 原始推文：ZachXBT @ x.com
* 作者：ZachXBT（独立链上侦探，Paradigm 顾问）
* 发布时间：2026-10-05
* 文中所有链上地址、交易哈希均保留原文

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6M6VsonJZVAakHoFvwpgv5pFickjEjPAkbq0UjR3PTAZ9P15ecr1OP3IiazTeqUR0zh6ic3sGRw3GfF62edfMzm3vb13eUsHxcn3Q/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6M5VUYaG7U84iaibDazJrKdc2BeibfO8Sp0iaNW91jlmtuGcicDKXdX384ROp9Md9xwMHVO3E5ObP7yKsuWwB1YvQsgZ1lpVyKg7RrA/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OgGCUleOymJT95dIeJRYSficeqChJAMrDNXKxiatZgoHBH3XsLQa8TLXGhPWf66PsrUc4mBvULtEGvNbrd4gVIagacc1VZib519c/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OJfiaLa6bsUPk3crSvJicCX3Rrvga8kicUibcYum8nVJ7vIMkQ7MKGsPNsoicQKSiaofjWyuT7qrV2cDh5qyebBuVMo9tZXGs9RGQVE/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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