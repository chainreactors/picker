---
title: 几个小程序挖掘渗透记录
url: https://mp.weixin.qq.com/s/pTcIZPVPDsAVRBwD_c7qdQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:16:19.825628
---

# 几个小程序挖掘渗透记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboT00LnJy5tvORQcEUxGuUUUHPKBibYddfVWgbG1bRKuRjIF1jaSChNJ8CnXF33Dq6O3XCBNCh4jx3nSuzsnorsE9HibQ8f9QHyqQ/0?wx_fmt=jpeg)

# 几个小程序挖掘渗透记录

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:一天要喝八杯水原文链接:https://forum.butian.net/share/4229
```

## 前言

近期挖掘的几个有意思的支付漏洞逻辑漏洞,记录一下。希望能对师傅们有一点点的思路帮助，欢迎指正及交流学习！

### 低价享受高价

锁定一个购票小程序.购买出行船票或车票时都区分为 二等座 一等座 包括舱位、上下卧铺价格也不同上,包括成人价格 儿童老年人优惠等,站点特征明显,厚码叠甲 选择一个目的地出行,然后下单记录数据包

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ90Gh5b2icZ8NqdFbnNsRY2iaH4FGcb4ugOX5bwrxabKAMv7h9pLeSo52RHWmjFe6c1NvuDw16aMc6f8poxgoDxqjDiafHOz5cnA/640?wx_fmt=png&from=appmsg)

选择一个目的地BP记录到了创建订单的接口shipgateway/shipOrderApi/createOrder 创建订单观察到并没有 sign 校验字段，存在问题可能性较大。遂将这个接口发送到重发器进行修改测试

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTiaNZ00o4B7GqXGT3QCEYWAIQRn1g7r8vqfyVccz2EEgBnbG2Bia4LXrZTeib81DSt3SsIuibA0bzian28cs5d2fJJNKpMUsDh4b5g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTqXa3BTwzAl2T24pIRkrQwLP5TuCYoHEMZfPEasbvIOib317bIrmqRektozQoicsSugswsWeln6IT71ladGIibFVazAOr2hbr5lk/640?wx_fmt=png&from=appmsg)

测试支付漏洞我喜欢搜索数据包`price`价格 每个字段都改变为最小的数字,再逐一发包创建新订单 但并未起效,订单也还是正常票价, 说明决定订单总价的字段并不是`price` 而是订单其他参数,目的地、票价类型、乘客类型都有可能,；而后开始对每个存在字段的数字增增改改 观察到底是哪个字段可以影响订单的生成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR6umQpGqZ2rznBHeJuSAica2C1bnjZsH2niakU2xYOY92JR58gZmxKz4CribFpOfibFPzQ3pMZx29cNpdlia4Shr983mYEovQyncVs/640?wx_fmt=png&from=appmsg)

修改到`passengerType`字段为2响应包显示 价格不匹配 ,根据字段意思推测这里决定用户的类型身份,正常情况的1为成人,2则是其他的类型得到响应包线索后,现在我需要知道其他`passenger Type`类型对应分别是哪些用户,业务提示很明显了,成人类型为1 那么`ticketPrice`票价为`100`业务推敲一下也就是对应下列

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQUa24Y1SRsvmeILPBso0ZwO418KIENt8vpLu3xrFsia9BxIA7vrNdnhE4hKs5jxb70p5IMUg0bSDQhZ6TBIozd9e7cBiaLAEbX4/640?wx_fmt=png&from=appmsg)

经过测试`passengerType`字段和`ticketPrice`价格字段挂购,二者需要一起修改,单独修改为固定的价格则会响应价格不匹配, 两个字段需要一起满足才能达到对应身份的票价

```
ticketPrice=票价  passengerType=成人类型

成人:

passengerType=1 && ticketPrice=100

儿童:

passengerType=2 && ticketPrice=50

长者:

passengerType=3 && ticketPrice=50
```

那么改两个字段为其他儿童类型所对应的价格,成功以成人身份证生成低价学生票订单,并且身份证还是原本成人

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQl0r6Wx3E0lVMLDMt7xBrVA80UK0Az3siag1WjGOiaooLuKRQ8GaQGeRvGiawAPaUZG8ENHNibzFUUwkwibicnZL3MHQNTpk5HAUl2U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT38AqibFReHRZVTSWYu3icNg09zKRVDozqekOt75AdQKbSib4UtNZM0Jt6OtnnwHsUia9LibaOS864VyDzK8q7kMFyjo6JLakkz15E/640?wx_fmt=png&from=appmsg)

这个时候我想再提高一下危害, 既然订单的价格是由用户类型所关联的价格决定了,我是否可以自主的再次修改增值的业务参数呢？享受到最高的优惠, 船票分为上等中等, 利用普通订单价格享受高等舱位服务,通过对比普通舱订单和头等舱位订单定位到`seatId`字段决定了舱位等级

```
"seatId":1# 普通舱
"seatId":0# 头等舱
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTRiaQR7XyiaYru7U6HdjJVvpdJx2cgW2GONzwbDZ8sex1Ae8lIDEVHBKXsQj5fngppCQLUTjONSZK2nEg6dcCgzZ2HSicP8fC7qc/640?wx_fmt=png&from=appmsg)

在中等舱数据包中,当我把三个字段都修改好后,订单虽然可以创建成功,但是舱位的类型还是中等舱,价格反而变成了头等舱的价格, 思考一下,既然在中等舱无法直接修改成高等舱,那我生成高等舱的订单,把它的用户类型、票价、舱位3个字段为最低的层面尝试绕过

```
"seatId":0// 头等舱

passengerType=2// 儿童类型

ticketPrice=50// 儿童票价
```

当这样修改后就可以成功创建高等舱位的低价订单,后端只是校验了 决定价格字段和类型字段间是否是一一对应,对当前舱位字段没有限制, 可以单独的去修改`seatId`字段控制舱位价格

```
"seatId":1// 中等舱
passengerType=2// 儿童类型
ticketPrice=50// 儿童票价
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSe4O8KRxO7VlfFoc0LGLDdibhTPmcH98z4YKLOnFebichUqHIyUPsVicj8GqJqNGZMPaq10qXsL79jC8y1l2YxusK6UETV1RABdA/640?wx_fmt=png&from=appmsg)

成功生成正常可以支付的订单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboStm7P16D2vGTebDWwWNax1miaSeh2qCbZIzqOuBlGkib64cyrwgDBseCJn8d1iclzsPkial2tp1pLPQUwkdkendIuiasEHGpueMuZ8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTXIkIbLrVeC7l8dLyVyTIWT70v4MMC4tJ1cD5CWjf34atwSnibZ5YLfpUNYgtQYA4AKrib5jqMIz5icNKAGpLKodSqT7RgoJv58w/640?wx_fmt=png&from=appmsg)

### 0元购思路

同样还是这个业务站点,有的船票是存在携童免费措施的,有的没有,那么将我的身份伪造为更低的是不是就可以0元上船呢

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQl6iau9y0JFibB8D9dWa8Fv509eiczxFsONAB2uwz1mYEvDMAk2jZreg3eWgCGXIgDFxZ6BBKvMF50wKYj5IdibVxtnExo5ib9hT8Q/640?wx_fmt=png&from=appmsg)

但是这里不能直接通过上面的手法修改类型、价格, 测试发现决定是否免费的关键是身份证的处理,身份证需要是儿童的出生年月,但是添加乘客接口是身份证大多是实名认证,我不清楚验证的原理是什么,按道理前端了身份证号对应的身份证,说明是后端查询到了, 但是我在BP里面拦截这个数据包又可以修改,说明并没有走后端,那么一开始的前端验证是什么逻辑呢,有懂的师傅可以解释一下,难道身份证认证的接口放到前端查询吗,可能是调用了身份证的接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTvmjMFEfaia9bq6zcRrzQUTtzsC9Piaia7f10pNd017NiaXEx3laVI9iaF2lSXwkTFJ8xicicSOsrPEmibRZjdiajleFxrdRoq5CkwPo8w/640?wx_fmt=png&from=appmsg)

首先添加正常的乘客信息绕过验证,找到添加的数据包 修改身份证和日期为儿童的,往大了写就可以,这一步如果身份证有婴儿身份证的话可以不用,或者自己有牛逼的`sgk`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRqoDK46NB5KsSxj38LPCbRNNADhUwKAjowqiazbNhf48eYQyFmYTeG46vcmibC4yEXiaEUNvxPwCsQRQTAMOvNI5jibcjWmjf3yhQ/640?wx_fmt=png&from=appmsg)

那么现在已经有了儿童的身份了,但是还需要在下单的时候把身份证修改回来,不然买的票身份证不是自己的买了也没用,找到一处可以携童免费的船票,选择上面添加的携带乘客信息,选择免费的票

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRs81JAfLHVFK2ibHbeIp65a1tibskyp72XG4OdMYQRKEzIS7wQWLHEMD8Oia3R4LBbcgFFfIv0FawZIUznBuoINGL49ZRhwMCpWs/640?wx_fmt=png&from=appmsg)

儿童免费票不能独立购买需要携带一名成人,正常添加一名成人乘客,然后正常下单记录接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQYjiaHsmubiayp37ia4YZSYTnEiaMKkNgPquxrLhcPLrEQ6YEVKtHagMKBERkuCNQQDGeAdVegkfhZaK8vmxRiakRlnQ6DMgWiaErFY/640?wx_fmt=png&from=appmsg)

抓取到创建订单接口发送重发器,上方为添加的成人,下面则是免费的儿童身份儿童身份证,出生年月为自己修改的2022年身份证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT9tYEA81XPhgXLHFfiaukWclzNYZrdBic5icG3VUwCA7HLHn1e4hvFgT9451KnH4YvjFPichRta8TTYmyjdiaN9ZS7fbgGMKxe2ibVI/640?wx_fmt=png&from=appmsg)

朴实无华的将出生年月及其身份证号修改为自己本人的身份发包,成功创建订单

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS39jib0qyrPdxLV2CRJK48PyFLMnkSjTicjXqn00QxurZmQWvzl9ia7EC6S7zPJegl8NoCnH0m06SK3fhkicibHEXycS7pib8oIoZus/640?wx_fmt=png&from=appmsg)

一份钱买两个成人的票 0元上船,但是无奈这个点后续虽然可以支付订单 但是会自动退票,或者会有人工客服打电话来,审核回应`SRC`排查过这个点

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTyeZQjurovA9E9kJSrIuWPF4t81LuBD6CqLgYFPpHekYicUHL54Y5lX9Iic82GjjtRe7fxIM6pPGLibNAJdtXPuQtTS7FH7M4pgg/640?wx_fmt=png&from=appmsg)

### 输出点思考

生成订单后出现的订单号,查询订单的接口会回显当前订单的乘客信息三要素,经过大小号替换订单号测试,是可以越权查询到他人的订单信息要素的,但是此订单号无法遍历,在网站其他功能点都没有找到可以出现订单号的地方,评论区 投诉 都没有

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSNqCaxk7ypF3nvog8lcuoOOAUQxePQ1IyIMMuSKpfTC8g61icTr3sfytGIlGHE5SUR3Anf9KN27ze9gXYUS9TXq1nxjuyOviaf8/640?wx_fmt=png&from=appmsg)

虽然无法利用,但是这个接口引发了另一种思考,订单号查询正常只返回订单对应乘客信息,但是这里却返回了用户的凭证字段

```
"openId" :  "xxxxx",
"unionId" : "xxxxx"
```

这两个字段都是鉴权字段,有了此字段的就可以跟替换Cookie一样替换别人的身份其他人的，操作此小程序所有增删改查功能点,当前虽然开着Hae但并没有相关的规则字段正则所以匹配不到,真的是细心才能发现,如果这个订单接口可以继续利用遍历的话,再结合返回的这两个字段,整个小程序用户信息全部会被接管,所有乘客三要素包括小程序所有功能点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT15J0dUMW7qMD1QsHxufZytKNLtIYMu5yKJNYmLySAV3b08dz5DiajaZU8ekwLIGlrEsUSBONNaQZfnM24libArc0Jsib9sBAtBM/640?wx_fmt=png&from=appmsg)

**总结**

虽然这个订单接口无法遍历继续的去利用，但却有了新的思考,不经意的响应包可能会带出其他的信息,发在攻防社区另一篇文章,https://forum.butian.net/share/4163介绍了这个情况,借鉴了L@2uR1te师傅的文章《如何寻找参数的蛛丝马迹》[https://mp.weixin.qq.com/s/kSxl\_VM2dQbkBQEE\_DQrPQ](https://mp.weixin.qq.com/s?__biz=MzkzNTUwNTg2Ng==&mid=2247483882&idx=1&sn=7bec8923088f61f371bcd425f3067956&scene=21#wechat_redirect)讲的很清楚,输出的参数拿到输入点去使用会有不一样的惊喜,只要一个点可以越权查看到别人的某些东西,把他人信息的铭感的参数收集下来替换到其他输出点使用,尝试是否能看到对应的信息,鉴权字段往往不是每一个功能都固定的,它可以接收某些其他参数发送请求, 在我看到输出订单号可以返回铭感信息后,第一时间就是找其他输出其他用户信息的功能,评论区 投诉这些,和这个思路是相同的

### 全站收货地址泄露

日常逛资产,挑选到功能点相对多的小程序,业务是购买商品,有很多的支付漏洞包括逻辑漏洞可以测试

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS6glwKdrX1qlnAcjur45aBsibA2Uic9c8dXXV4lGMfYypBXZDViavpxLZqGVcnjtuEJA8IaazltSGicrZickHvlPOYibgUZwro5wGeQ/640?wx_fmt=png&from=appmsg)

测试到地址管理功能点下列是查看我自己的地址`list` 出现了地址的id号 `13313 13314` 不等,小程序功能点大多使用`JWT`鉴权,对`JWT`尝试了常见攻击手段均无法绕过,

```
/buyer/address/list/
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQ4FoFTzE6Y9MlBUsdnIAiatuJ8F2VMwPmWct8tjuXM1hOMerJpYXPMUXFEzj0eafNmynhrUQeaJkP239e68XBcYev3Cj4BoBY/640?wx_fmt=png&from=appmsg)

测试小程序购买商品功能 正常选择收货地址,然后正常下单记录数据包

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTvAytVFulsKcrJQliay2KSFBjtJfQG3NQyMUsfPI9m7wBkia7qKzb7YH8czg4Y1TeGQnO2dswpchhdibyV3HGVtuQFA2uxQA1v2M/640?wx_fmt=png&from=appmsg)

buyer/product/retail/submitOrderPa接口记录的参数是商品的价格还有斤数,都...