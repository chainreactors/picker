---
title: 币安63亿被盗细节：黑客提前36小时攻入、破解签名
url: https://mp.weixin.qq.com/s/97QtAvfm4mxXHCpD8CQqzw
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:20:31.086227
---

# 币安63亿被盗细节：黑客提前36小时攻入、破解签名

# 币安63亿被盗细节：黑客提前36小时攻入、破解签名

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 10月31日，币安那场创纪录大劫案的细节终于浮出水面——**63亿美元一夜蒸发**，FBI进场，朝鲜系黑客背锅，而真正的命门，藏在以太坊那行没人盯死的签名逻辑里。

#

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicLSCme7ACN78dzzjLVP6515qzCeIs5zLJLW7ztT0uwTXkcz8lfkkD2jfTtUnh0vyhotXicICRaZJibFHYyyF9gQss46oLqKSEwT4/640?wx_fmt=jpeg)

#

## 20分钟洗穿十条链

##

攻击者一点都不急。

提前36小时热身：

10月28日从Tornado Cash收三笔小额ETH，29日部署攻击代码并完成最后一次沙盘演练。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIHccfQkvFmJ7eAPvarOAIcp1hYCGhbj6sI7lBQ9qEpGYLLRZvuJBY2eLxYn5JzvT1EAXmBjlaJRic02adurXncUNjna8LGXBDs/640?wx_fmt=jpeg)

**10月29日20:05（UTC），枪响。**

* **20:05–20:09**：XRP Ledger先崩，5个钱包向同一地址转出**2.33亿枚XRP**；
* **20:10起**：Solana、Optimism网络相继出现异常转账；
* **20:20**：比特币热钱包单笔划走**18270枚BTC**（当时约14.7亿美元），随即拆至不同地址；
* **约20:22**：波场网络转出**6.127亿枚USDT + 4640万枚TRX**；
* 同期：以太坊多个钱包遭EIP-7702授权劫持（详见下文）。

**20分钟后，主洗仓阶段结束。**

但资金转移并未停止——当日23:05，Avalanche和Polygon上部分钱包再次异动；一个受影响的以太坊钱包直到**23:56**仍有资产被转走。

TRM Labs追完10条链：

损失约**63.6亿美元**；Elliptic追11条链：约**64.3亿美元**。口径不同，量级一样吓人。

被盗全景：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicIZmicmYP74jniac4MAZHV8MkQHjrI4YhHy2gvZfNglwsTRtD9ES49c8bibYKT8icChlQOU2ShpibbXQYZg8n81wSribN1DWmicFZAG7g/640?wx_fmt=jpeg)

## 签名授权EIP-7702被玩成后门

##

真正让老安全人后背发凉的，是以太坊那段。

攻击者**提前备好50份币安热钱包有效签名的EIP-7702授权**，nonce连续铺满，赌哪一笔能在提交瞬间命中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKvVicS05yZjhDf0LWeQWOmpnSHQg1eTb1oelovcmh51fz16RtoqwAh2JulWDXnibcxbX4icu5ia6hV2ibMonAgIxD7hljnrGicgJ6PI/640?wx_fmt=jpeg)

命中后，热钱包将执行权交给恶意合约——**3分24秒内**卷走16.7万枚ETH及63种代币（含16.15亿枚USDT），顺手搬走8.23亿枚USDC。

关键点：

币安至今**没找到私钥泄露证据**。

不是钥匙被偷，是"签字盖章的流水线"被人接管了。EIP-7702本身没爆洞，但把临时委托权限塞进高频热钱包，等于给金库装了感应门——逻辑通了，人就不必翻墙。

## 冻结30亿，真追回是零

##

别被"冻结"二字骗了。Tether冻17.7亿USDT、Circle冻8.25亿USDC、Ripple冻RLUSD——**冻结≠归还**，只是把余额钉在原地。

攻击者手里还攥着**32.3亿无法冻结的原生资产**：

5.19万枚ETH、1.827万枚BTC、2.33亿枚XRP。这部分没发行方、没开关，只能盯链。

更狠的是他们抢跑：

8.86亿稳定币在冻结前冲进Uniswap、1inch换ETH和TRX，**单笔吃12%–26%滑点亏损也要跑**——时间窗口比利润更值钱。

马斯克在 X 平台多次公开发言玩梗调侃，一句 “Everyday is Zeroday”，直指币安安全问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIic3P9icx8NHs6svdZkGHQuib9o2GdorX8TeZUVia38jEdeTpmSzbbzfEAF4mgibtZgXPzBPwhFaw2c4q0LH0zMmwJh4icINKEh8nBc/640?wx_fmt=jpeg)

币安创始人赵长鹏（CZ）公开回应，称自己十分尊重马斯克，但当下并不是嘲讽的时机。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLTWE1YrcKZDR7ZKTbYQmevXNBLHsw7fHDTPJteMofzF30SpTZYkWXh9IlxKODvmGjtHS7WGoLtQ9BfTvyVduqW6nB4J0BQ9G0/640?wx_fmt=jpeg)

网友评论：

“黑客找到漏洞绕过交易所的安全机制，没有破解加密币私钥但把钱包给偷了。现在AI挖漏洞太厉害，AI面前就不存在没有漏洞的信息系统。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJdCTjhVKzrJvDrNicfgtmnZfYv7pVvcQSMlJwbybPqRNjS1vggC65z4GAjY09fjnFziaicq2Ke9DAJujXJgLzPwicrDMjJrm3nuNU/640?wx_fmt=jpeg)

币安拿SAFU+自有资金顶了63.4亿兜底，用户不背锅。但代价写得很清楚：**跨链热签基建一旦失守，多链即多暴露面**。

> 安全圈一句老话：私钥没漏是最危险的漏——因为你看错了敌人从哪进门。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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