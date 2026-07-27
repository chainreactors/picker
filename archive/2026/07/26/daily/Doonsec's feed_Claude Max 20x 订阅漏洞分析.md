---
title: Claude Max 20x 订阅漏洞分析
url: https://mp.weixin.qq.com/s/YgyhwQm5rPYLQGCBm5b8mw
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:39:06.296014
---

# Claude Max 20x 订阅漏洞分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oghJwiaPb1Cvo1TamxRibFrvuHGn9bZx8RsrxFQPh3TWMxYECx2rUNblibXicSRI9px0em8e8MLpaOeIWJa1dIIhib2zg1icpUYRmicxjBdgT8iaft4/0?wx_fmt=jpeg)

# Claude Max 20x 订阅漏洞分析

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于浮之静
，作者lencx

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM4sLicFUCTIdTHKImxthxMkT0RfT3nD39tohewaTUB9jEg/0)

**浮之静**
.

{折腾 ⇌ 迷茫 ⇌ 思考]ing，在路上...

Anthropic 员工估计还在睡觉，起来会发现天塌了。然后又会开启一波大规模封号潮，大家早做准备（[Anthropic 三件事：封号潮，Fable 回归，Sonnet 5 发布](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247492153&idx=1&sn=8f14033b5a259b7a6bb1c80b67cc87e6&scene=21#wechat_redirect)、[深度解析：Claude Code 源码](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491747&idx=1&sn=402e7be9dc30cccdcd2c2f748974726c&scene=21#wechat_redirect)）...

社区和微信群里疯传的免费订阅教程被人做成了油猴脚本/Chrome 插件（贴心附赠随机生成德国银行卡号的网站），一键帮你完成薅羊毛。该脚本教程我在多个社区平台看到，浏览量至少在几百万。微信群也看到了一些人起码开通了十多个小号来订阅薅羊毛，初步估算 Anthropic 直接经济损失可能是上千万美元，妥妥的 P0 级生产事故。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oghJwiaPb1CtvkgicGHVBgTxVHTozyaLia2ujttfvoZhBOWiabTOJssjOYnk4jQG2CoXJ4vuulbeGhuCLUdj5bpv8bLRe016loAGdWbf5rianfoM/640?wx_fmt=png&from=appmsg)

我只想说：世界真是一个草台班子，这代码难道是 Fable 5 写的？感觉 AI 都很难写出这种 P0 级漏洞，开发者但凡有点意识可能也不会出现这种薅羊毛场面了（可能系统连个预警机制都没）。

## 事件概述

这次所谓“德国银行卡免费订阅 Claude Code 20x”，不是银行卡被破解了，而是 SEPA 直接扣款的结算延迟 + 权益发放过早叠加形成的时间窗口漏洞。

SEPA（欧元区直接扣款）和信用卡最大的区别在于：信用卡是“授权即确认”，SEPA 是“先发起扣款，后银行结算”。Stripe 文档中明确，SEPA 扣款通常需要数天完成，在此期间状态会长期停留在 processing，并且仍可能失败。

问题就出在：系统在“钱还没确定到账”时，就发放了高价值订阅权限。

### 攻击原理

攻击并不需要真实资金，也不需要真正控制银行账户，只需要满足两个条件：

1. 能提交一个“格式合法”的 IBAN（通过校验位即可）
2. 让支付系统进入 processing 状态

![](https://mmbiz.qpic.cn/mmbiz_png/oghJwiaPb1CtmiceOBMiaVYyQFx57fX2Rs5qwoOWBQxkZMEAWmvQJZujwDaibBY7EQlDDQ9bafictcXhRsQv0cl67azskWqC3Biasxd9nsfB24DdM/640?wx_fmt=png&from=appmsg)

在 SEPA 模式下：

* IBAN 校验只验证结构（国家码 + 校验位）
* 不验证账户是否真实存在
* 不验证账户是否属于提交者

因此攻击者可以构造“看起来合法”的支付请求。

### 漏洞核心：时间窗口机制

整个攻击依赖一个非常短但致命的窗口：

**漏洞窗口 = 权益已发放时间 - 支付最终确认失败时间**

这个窗口由两个系统共同决定：

1. 银行结算链（慢）

* SEPA 清算：1–5 天
* 最终结果：成功 / 拒付 / 退单

2. 风控系统（快）

* 异常检测：分钟级
* 行为分析：小时级
* 账号冻结：实时触发

因此实际窗口通常是：

```
银行未结算（天级）
        vs
风控已封禁（小时级甚至分钟级）

攻击者真正能用的时间，取决于哪一个先触发
```

![](https://mmbiz.qpic.cn/mmbiz_png/oghJwiaPb1CuicP7CDZMeibnmiaeUiaRGxCFibUM30T0wVAUKKhKVLCuJ7tKIYW7Motc2iaqUIia9XLP8VL1THBzV36I0XF0sTibWcsVLCrl6jxwOszg/640?wx_fmt=png&from=appmsg)

## 插件脚本分析

我让 GPT 简单分析了一下 Chrome 插件：它并不是简单修改页面、显示一个被隐藏的 SEPA 按钮，而是在 Claude 已登录页面中自行构造 SEPA 表单，并直接调用 Claude 官方结账接口，强制提交 paymentMethodTypes: ["sepa\_debit"]，再使用后端返回的 Stripe 会话完成付款流程。 扩展说明也明确写的是“创建 SEPA Direct Debit 表单”，且只申请页面脚本注入与本地存储权限。 这意味着正常界面虽然没有开放 SEPA，服务端却至少一度接受客户端指定该支付方式，暴露出后端业务规则校验不足；不过，仅凭脚本只能确认“可以创建 SEPA 结账会话”，还不能独立证明 Claude 一定把 processing 误判为付款成功并立即发放 Max 权益，后者仍需结合实际支付状态和 entitlement 响应确认。

![](https://mmbiz.qpic.cn/mmbiz_png/oghJwiaPb1CuznXXl0M9VbiacbPQR96JmHy5MA8JHtLocGg0iaFSdEj3ibuzeHV4b324toXg9puO0CKaib5zOfvRjYEgXB1Bx0B0kzeCYqiayibJic8/640?wx_fmt=png&from=appmsg)

## 结语

薅羊毛的行为暂不评价，说点别的感受：羊毛党只会让 Anthropic 的风控级别越来越高，订阅难度进一步提升。结合之前 Claude Code 泄漏的源代码来看，Anthropic 会记录用户环境，不排除记录电脑设备信息，如果设备触发了风控，很有可能会拖累原本的正常账号，连续触发多账号封号。

注：截止写文章时，似乎已经有人的订阅被封了，新账号也无法注册...

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oghJwiaPb1Cu5SznAaAK6wMDma9RvjxUe0N1gyiaJiaCDsDsIdgQmpYpT2gtfuYpBicicZfbqInOT6WPd8IE9MuICaprJNta2fltGgcoJ9L1d0PI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oghJwiaPb1CuDGotxib04TTfXWAuQiaYGxzaVKoZpbDzKWic1rahvT9SfqLibR0QSBmLkiaDrZTcnRuia840K87XLYj4d2LYNaI3Iib06aubTfLR4jE/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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