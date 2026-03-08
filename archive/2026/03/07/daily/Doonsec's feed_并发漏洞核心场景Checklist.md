---
title: 并发漏洞核心场景Checklist
url: https://mp.weixin.qq.com/s/Vfu7lvGPgamG1uyZ2mnqGg
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:06:01.422062
---

# 并发漏洞核心场景Checklist

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8tDOXFoCoQ925XbWOLKfF706D8QPvO3ians56jbcmK9bwic39DYibK4IaJuScFibZI71WGz2OCqRuiajkuqyibHL64bD6BMZ9OLOu0ToPWrbYLF3c/0?wx_fmt=jpeg)

# 并发漏洞核心场景Checklist

原创

游山玩水
游山玩水

山水SRC

![]()

在小说阅读器中沉浸阅读

## 概述

本文讲解了在渗透测试中遇到哪些功能点需要测试并发，如何使用turbo-intruder-all见下面文章链接[登录框短信轰炸checklist](https://mp.weixin.qq.com/s?__biz=MzY4MTEwNDczMA==&mid=2247483730&idx=1&sn=630df0c534c00bbc18660e6ed7605314&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8tDOXFoCoQ9XJROdXAd8YwiaqoYPA1z1JKb3I4xV67RtRUm1CcmeMePTOMiazjDytWuwXAdM0ERclDDWOmyx4dY7aWiaDA5t5WYuCzqC9bXqn4/640?wx_fmt=png&from=appmsg)

## 限次领取/操作漏洞

**危害：刷取大量资源（优惠券、积分）、扰乱活动（投票）。**

**出现位置：所有带有“每人限领1次”、“每日限1次”、“限投3票”规则的活动页面。**

**测试步骤**：

1. **抓包**：正常领取一张优惠券，拦截成功请求（如 `POST /coupon/take`，携带用户令牌和券ID）。
2. **并发重放**：将请求发送到Burp Suite的 **Turbo Intruder**，设置线程数为 **100**，延迟为 **0** 毫秒，启动攻击。
3. **结果验证**：攻击结束后，查询“我的优惠券”列表。**漏洞表现为**：账户内成功领取了多张（远超过1张）该优惠券。

## 库存超卖漏洞

**危害：商品超卖导致资损或运营事故；名额超限。**

**出现位置：商品秒杀、课程抢购、活动限量报名等场景。**

**测试建议与步骤**：

1. **首选单用户并发测试（快速验证）**

* **方法**：使用一个账号，拦截“提交订单”或“确认购买”的最终请求，用Turbo Intruder发起高并发（如50-100个请求）。
* **验证**：检查是否生成了多个待支付订单。如果成功，则漏洞存在。
* **优点**：简单、快速，能发现大多数因后端逻辑缺陷导致的超卖。

2. **补充多用户并发测试（更贴近真实）**

* **方法**：使用多个测试账号（或不同会话），模拟真实抢购场景，同时发起购买请求。（也可以一个账号多次点击几次购买按钮，将生成的多个数据包一起放包）
* **验证**：检查总成功订单数是否超过库存。
* **必要性**：用于检测那些仅在多用户竞争时才出现的漏洞（例如，依赖用户级锁而非商品级锁的系统）。

3. **必须验证业务结果**

* 不要只看HTTP响应是否成功。必须**登录后台核对订单数量和库存扣减是否准确。这是判断漏洞是否存在的唯一标准。**

## 总结

不要局限于上述环境：发现“只让做一次”或“做完一次才能做第二次”的场景，都可以测试并发漏洞（管他有没有危害，先试出来效果再考虑）

并发漏洞测试的本质是：绕过系统对连续操作的时间间隔或顺序检查，通过同时或极短时间内发送多个请求，使后端处理逻辑出现竞争条件。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BXWf54pHyFmsnAoomcxMvpxr0NRiaiaibRWIjfusaRLibIUMSwsQUNy2k2rtjeky3xPBmDLia6x4hktJdhNhUic8aFpQ/0?wx_fmt=png)

山水SRC

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BXWf54pHyFmsnAoomcxMvpxr0NRiaiaibRWIjfusaRLibIUMSwsQUNy2k2rtjeky3xPBmDLia6x4hktJdhNhUic8aFpQ/0?wx_fmt=png)

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