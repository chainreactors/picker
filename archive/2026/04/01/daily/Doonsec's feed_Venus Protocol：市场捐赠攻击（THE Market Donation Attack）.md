---
title: Venus Protocol：市场捐赠攻击（THE Market Donation Attack）
url: https://mp.weixin.qq.com/s/Hw2XdisIl3koGCTTPJLQGw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:01.228404
---

# Venus Protocol：市场捐赠攻击（THE Market Donation Attack）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnvGGkzWO91aOkOC1bkI0l3gVM1H8NTFlmbfMqqw8h4ukGa57suFyhdDtgytlpZjIhbVOwVVNVD5NSVnYVpvuh3sD8PxUhRm8ow/0?wx_fmt=jpeg)

# Venus Protocol：市场捐赠攻击（THE Market Donation Attack）

hai dragon
hai dragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

##

![Venus Protocol](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsLjicZFzfosWecQuOuPhO4uKsVafVzOfoZCBqu1PO6uxr3nqwMXVhkhHYfWKiaEPYGCRSgkov8rruTT32K32V1BRrwsHEjE9g84/640?wx_fmt=png&from=appmsg)

---

## 执行摘要

2026年3月15日，BNB Chain 上的 Venus Protocol 的 THE（Thena）市场遭遇了一次“捐赠攻击”，造成约 **370万美元**资金被盗。

攻击属于 Compound 分叉协议中的经典漏洞类型。

攻击者利用了 `getCashPrior()` 的设计缺陷：

* 使用 `balanceOf(address(this))`
* 而不是内部记账变量

攻击者通过**直接向 vTHE 合约转账（绕过 mint）**：

* 人为抬高 cash
* 将兑换率放大 **3.81 倍**
* 借出远超抵押价值的资产

---

最终结果：

* Venus Protocol 损失约 **218万美元坏账**
* 攻击者被治理冻结资产，净损失约 **470万美元**
* 社区冻结约 300万美元资产

---

该漏洞：

* 早已被 Code4rena 审计指出
* 但团队认为“捐赠是设计功能”，未修复

---

---

##

![Attack Structure](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntriabYiagr4YZtHNJYuukFfUUDab2C9OUtNWrMH0LwSX5K50NytOOtjGKwxeQCTeyQLhUicJiaHgrCMYICzMn8kUaibeCVMKCibrLa8/640?wx_fmt=png&from=appmsg)

---

## 背景

### Venus Protocol

* Compound 分叉借贷协议
* vToken 代表存款份额
* 利息增长 → 汇率上涨

---

### THE 代币

* Thena DEX 原生代币
* 流动性低
* 易被操控
* 设置供应上限：1450万 THE

---

### 捐赠攻击原理

核心问题：

```
totalCash = token.balanceOf(vToken)
```

任何人都可以：

👉 直接 transfer token 到合约
👉 不需要 mint
👉 但会被计入 cash

---

汇率公式：

```
Exchange Rate = (cash + borrows - reserves) / totalSupply
```

👉 cash 被人为抬高 → 汇率暴涨

---

---

##

![Timeline](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvX2hYDGFjf6xPRP1X7fwX7twMsXOCYicHxP4OrUaKT2gFszRbsiac8xKlZGAT4biba6C1GseZ3FibiavjKA8p7BeevxMsFG28e3kSY/640?wx_fmt=png&from=appmsg)

---

## 攻击流程（简化）

1. 正常 mint vTHE
2. 获得初始仓位
3. 直接向 vTHE 合约转入 28,100 THE
4. cash 被抬高
5. 汇率上涨 3.81x
6. 抵押品价值暴涨
7. 借出 CAKE / USDC / BTCB / BNB
8. 循环放大攻击
9. 最终盗取约 370万美元

---

## 影响

* 供应上限被突破（367%）
* 利率模型失真
* Oracle 被价格反馈影响

---

---

##

![Olympix Analysis](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntMUyf8eVYXGX5TWj2icZqkqaPsW7Kcg8Rx2AnKg96c26f8lHOnZvZbKkTnia3HAJib4ZQNuGtST3p2EngIdUyhq940F1UY21RMyo/640?wx_fmt=png&from=appmsg)

---

## Olympix 分析

检测到 3 个核心漏洞：

---

### 1️⃣ 汇率操纵漏洞（高危）

* donate → cash 增加
* 汇率 → 3.81x
* 借款能力暴涨

---

### 2️⃣ 供应上限绕过（高危）

* cap：1450万
* 实际暴露：5323万
* 超出 367%

---

### 3️⃣ 利率失真（中危）

* utilization 被低估
* 利率下降
* 协议收益减少

---

---

## 根本漏洞代码

```
function getCashPrior() internal view override returns (uint) {
    return EIP20Interface(underlying).balanceOf(address(this));
}
```

问题：

👉 把“外部余额”当成“协议资产”

---

## 修复方式

```
return internalCash;
```

---

## 结果

* 汇率操纵被彻底修复
* donation attack 失效
* supply cap 恢复有效

---

## 结论

这次攻击本质是：

> 一个函数设计错误 + 一个被忽视的审计问题

导致：

* 汇率被放大 3.81x
* 供应上限失效
* $3.7M 被抽走

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx
* ![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnticREf3VyfYesm0aoCmIDZGZcN3NJ3tibHmF2ia5DTyWy6n8iajuYU4TYVTKf9CsT4mXgmbVGdCqZdXz85lkTQXJnks3MOEUcVF0w/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

##

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvoTp0padsQkToVONTUUxXwCVmyup0CzMsABrvfE2wOv8I1dVWQon4pkTp3ocnHpomr3M3YtrWeXb5TyBZpEnibI9GOTatXMPg0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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