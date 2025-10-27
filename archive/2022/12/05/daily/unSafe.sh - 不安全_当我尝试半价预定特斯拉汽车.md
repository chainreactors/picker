---
title: 当我尝试半价预定特斯拉汽车
url: https://buaq.net/go-138477.html
source: unSafe.sh - 不安全
date: 2022-12-05
fetch_date: 2025-10-04T00:30:35.808639
---

# 当我尝试半价预定特斯拉汽车

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/b8a926c97439e5fd0bbf3358d299aee6.jpg)

当我尝试半价预定特斯拉汽车

一、前言最近抽空做一些国外的赏金项目，特斯拉是我选定的一个测试目标。恰好，秋之(@sz0030)师傅也在挖，提及可以改特斯拉支付金额完成订单，这引起我的兴趣，便和他探讨交流，向他请教技术细节。针对业务
*2022-12-4 17:17:55
Author: [mp.weixin.qq.com(查看原文)](/jump-138477.htm)
阅读量:32
收藏*

---

## 一、前言

最近抽空做一些国外的赏金项目，特斯拉是我选定的一个测试目标。

恰好，秋之(@sz0030)师傅也在挖，提及可以改特斯拉支付金额完成订单，这引起我的兴趣，便和他探讨交流，向他请教技术细节。

针对业务类型的漏洞，尤其是支付功能相关的，之前挖的少，产出也少，所以这是一次不错的机会学习。

在后面深入的测试过程中，我认为自己发现新的思路可以实现金额的减免，并尝试实现。虽然最后失败了，但这个过程和思考还是挺有趣的，因此记录并分享出来是极好的。

## 二、契子

秋之师傅和大家分享挖到漏洞的好消息：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ff2BsLOibtkP5z8nVc17IVaJNwu0e5icHBkzsCjKywNPZXmdGh2maOokRZxQyTibiahKZOn9nVAsibDDicfqSAfZTjXg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ff2BsLOibtkP5z8nVc17IVaJNwu0e5icHBmCS4jbic2FhJIsnbMpQrzwO3vKZLCrtUkfGFqVHG3FHd80T0yJDCOdA/640?wx_fmt=jpeg)

和师傅沟通后，打算自己动手，尝试挖出这类漏洞。

## 三、分析预定汽车的流程

首先，从特斯拉的web应用站点开始， 进入主站下预定车辆的功能页面，捋顺接口，重点关注微信支付的逻辑。

业务上的流程:

1. 1. 选择车辆
2. 2. 选配
3. 3. 填写个人信息
4. 4. 选择支付方式
5. 5. 完成支付

接口上的流程:

1. 1. POST请求到order接口，其中包含 车辆，配置，个人，支付方式等信息
2. 2. 接口回显类似 `weixin://wxpay/bizpayurl?pr=xxxx`的信息
3. 3. GET请求到获取微信二维码图片的接口，其中参数值为第二步的`xxxx`
4. 4. 接口回显图片数据
5. 5. 扫描图片，即可在微信上进行支付

### 1. 复现秋之师傅1元支付的场景

从接口上来看，整个预定的流程的关键点在于order接口，里面有金额，支付方式等信息，直接尝试篡改。

通过多种篡改组合和篡改技巧，响应里`bizpayurl?pr=`的值每次确实会变化，但对应的二维码扫出来的预订款是不变的。

这就代表此处的篡改实际无法控制微信支付金额，这儿困扰了我几个小时。开始怀疑是不是APP上的预定车辆的逻辑会有区别，便在APP上测试，发现金额也是不变的。

那会是改哪里呢？便请教秋之师傅，询问他是如何实现支付金额的修改的，他告知在如下两处请求的篡改是可以控制支付金额的：

![](https://mmbiz.qpic.cn/mmbiz_png/Ff2BsLOibtkP5z8nVc17IVaJNwu0e5icHBpIftuBLLXwBbsOdxvVXwQOGRibQItE5NC56ibfu7fb6vPU3ZCSRYvIXQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Ff2BsLOibtkP5z8nVc17IVaJNwu0e5icHBPaEp78lFNcRk8T2Du7d8k7jtROUICB9o4LxDgXtjnoqcMl1YrEjGxQ/640?wx_fmt=png)

可惜的是，按照指引，还是未能复现成功。后面秋之师傅自己验证了下，发现上面这两种修改方式现在已经失效了。

秋之师傅还说到，他提交这个问题后，特斯拉反馈这个问题19年已经有人提交过。按照上述的修改方式，虽然可以只支付1元钱，但去查订单，实际还会需要支付999的尾款(model3的预订款是1000元)，因此特斯拉认为订单实际并未完成，漏洞并不是真实存在。

### 2. 另辟蹊径

是的，如上所述，表面看起来是完成了1元的订单，但是实际还需要支付剩余的金额，使得支付总金额等于预订款，这当然不算是问题。

虽然得知这样的消息，有点让人想要放弃。但直觉告诉我，现在还不是时候，当前我只是单纯的想试试看，能不能找到新的方式向这笔订单支付1元。

于是我在APP上尝试购买特斯拉的周边产品，梳理出大致的流程：

1. 1. 选择商品
2. 2. 选择支付方式
3. 3. 点击支付
4. 4. 为订单签发orderid
5. 5. 为orderid签发signedData
6. 6. APP发起`payments/v4`的POST请求，带上signedData
7. 7. 响应paymentData，并拉起微信APP弹出支付窗口
8. 8. PUT payment接口确认订单完成情况

等等，我好像发现了有趣的事情。在申请预购特斯拉汽车的订单时，响应了一个 signedData， 在当时看来似乎没什么用，会不会和这儿的signedData可以串用呢? 如果在支付购物的过程中抓包，把购物订单的signedData，替换为预购特斯拉汽车的订单的signedData，会怎么样呢？

于是便动手操作起来:

1. 1. 在web站点上选购特斯拉汽车
2. 2. 抓包，抓住order接口，将`OrderAmount` 从20000改成1
3. 3. 获取响应包里面的`signedData`与 rn订单编号
4. 4. 在APP程序上 选购特斯拉商品
5. 5. 抓包，抓住payment接口，替换掉signedData
6. 6. 放包，此时发现微信弹出来的支付金额居然就是1元

哇，成功了。于是，我查询了 rn订单编号 的完成情况，果然是还需要支付 19999元，虽然看来这个方式并没有绕过特斯拉对于订单的兜底机制, 这和预期的一样，

但我完成了开始的目标，即向订单支付1元的想法。但，此刻，我却不满足于此，我尝试寻找新的突破方式。

## 四、新思路

### 1. 观察

首先，我开始研究`OrderAmount`这个参数支持哪些值, 如下值都是可以使用的，能正常签发出signedData:

```
0.00001,, 1e20, 1e-21, ["0.1"], 99999
```

灵光一现，我想到了会不会有四舍五入的问题，于是我设置为0.51元，并按照上面的流程，进行了支付:

![](https://mmbiz.qpic.cn/mmbiz_png/Ff2BsLOibtkP5z8nVc17IVaJNwu0e5icHBGNHcjrWugTLP008kiaQeicDntlEG4y23f9E8RH4sKMWdGkS67WDeogrQ/640?wx_fmt=png)

再来查看RN订单剩余需要支付的金额：(说明: 我在测试时，预定的是model S, 总预定款为20000元)

![](https://mmbiz.qpic.cn/mmbiz_png/Ff2BsLOibtkP5z8nVc17IVaJNwu0e5icHBacxlEg6LIa1pg9GZyoIjvIJxb3X40uhcSc09yNREWl1OzTmhj9bh8A/640?wx_fmt=png)

### 2. 分析

看到这儿，其实已经暴露出我预想的问题。

是的，原本需要支付20000元，支付了0.51元，理论剩余需支付19999.49元，但实际只需支付19999元，0.49被四舍五入掉了。

### 3. 构造攻击思路

那么，这儿很自然的就产生一条攻击路径。

即，如果可以构造循环支付的条件，每次我只向订单支付0.51元，系统后端会舍掉0.49元，重复这个过程，相当于只需要支付原来款项的 51%，即10200元，基本就是半价支付，酷。

接下来的问题关键就是去实现循环支付，以便让后端不断做四舍五入，于是我尝试如下:

1. 1. 尝试通过修改已有订单的选配，触发订单状态的改变，为订单不断签发新的signedData -- 失败，并未签发出来
2. 2. 通过分析，生成一笔RN订单，如 RN123456, 对其进行支付，支付实际对应的是子订单，即 RN123456-1, 看到上面的商品单号就可知。那么在设计上，每笔主订单应该是可以派生出多笔子订单的，例如 RN123456-2,RN123456-3等等，PUT payment查询订单情况的接口响应的数据也能侧面验证这一点。尝试控制子订单编号，使得子订单号与主订单号相同，例如设置一些特殊字符，空字符等 -- 失败尝试使用购物签发子订单的接口尝试为预订款主订单无限制签发出子订单 -- 失败
3. 3. 尝试，获取一个signedData后，先签发出10个paymentData, 然后再依次支付paymentData -- 失败，因为都对应到同一个子订单，其中一笔支付成功，其余默认成功，不允许再支付
4. 4. 并发支付paymentData -- 失败
5. 5. 等等 -- 失败

### 4. 小结

我将上述情况报告给厂商，由于实际上我并没法做到重复生成子订单来完成每次0.51元的支付，这个问题被认定为：

![](https://mmbiz.qpic.cn/mmbiz_png/Ff2BsLOibtkP5z8nVc17IVaJNwu0e5icHBAjhugDAghVxMbFSlNZ5b3dJPKyfmB0JGicnkCnhD1qcy2YPQKRVG1vQ/640?wx_fmt=png)

当然，如果你有好的攻击思路，你值得赢得这笔赏金，也希望可以和我分享你的思路，lol.

## 五、结论

花了快整整一天的时间，虽然最终无法闭环整个攻击过程，充满遗憾，但这是个不错的机会让我可以去实践内心的攻击思路与想法，这个过程挺令人激动的，也学习到一些测试技巧，说不定哪天足够幸运可以用上并发现高价值的漏洞。

本文仅做技术探讨，切勿破坏厂商业务，切勿篡改原意，不允许转载, 内容已通过厂商审核检阅:

![](https://mmbiz.qpic.cn/mmbiz_png/Ff2BsLOibtkNgRiaa8WGHX89W5FD7ib9tJXIwbqS9HNmJ3ibPGxNsGRfXWcZUQePBlxoIGEJx1aibz4sxtxymibjb6rA/640?wx_fmt=png)

文章来源: http://mp.weixin.qq.com/s?\_\_biz=MzkzMTIyOTA1NA==&mid=2247483987&idx=1&sn=be378a529a2d794d45d6764522b09bdd&chksm=c26f7e42f518f7542505fba7ce42deb79c5082982b4ce154c9caa82e9353479fd09af493b001&mpshare=1&scene=1&srcid=12046ju39DP76FEtNerik4nQ&sharer\_sharetime=1670145471960&sharer\_shareid=205c037363a9188e37dfb6bb4436f95b#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)