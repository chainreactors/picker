---
title: 一个甚至都不需要开bp的企业SRC中危
url: https://mp.weixin.qq.com/s/M1F0QEvnoQVKpIE8rPhVGg
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:26:16.005412
---

# 一个甚至都不需要开bp的企业SRC中危

# 一个甚至都不需要开bp的企业SRC中危

原创

RelishSec
RelishSec

RelishSec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

漏洞来源

都6202年了，还有开发会这么糊涂啊，今天带来的案例来源于商城系统，只要调用下单接口把库存买到空、死活不付款，商品库存直接被死死占住，别人再想下单就只能看到库存不足，活生生把热门商品锁成 “仅供观赏”，合着不用花钱，光靠占单就能包场买断货，这波属于零成本捣乱，商家哭晕在后台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/burEQVgkS5Cj0LBk4RFl2x6jL6M0YzciaoLa4x8Qyg4t72PTvXoiaQ08tszILfFjia0vC3Q9nNeVfsAL41hB9a39HLsHhOpcrlzMlVCNPXqQEI/640?wx_fmt=png&from=appmsg)

漏洞案例

在商城中点击进入任意商品购买页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/burEQVgkS5D0nT5lLMKRia9rWZPLAKI5bFqWshDsDuyRyN5G7W6o988VmD55MhHicpHPROjNPaen3KnL5LluAqzSmRofW83CYOc8hBATOsIaE/640?wx_fmt=png&from=appmsg)

直接输入最大库存点击购买

![](https://mmbiz.qpic.cn/mmbiz_png/burEQVgkS5B3bfYvcjpGyFRkAqabKgUHTx32tL8579lhicpkOm9HKDf2Ma7xsJyFXdRcASdribz4TheuP3V86F7xqmMEz26VefluIticiaElmfg/640?wx_fmt=png&from=appmsg)

下单生产订单不付款

![](https://mmbiz.qpic.cn/sz_mmbiz_png/burEQVgkS5CDAPtWOyiaoUFnTv7y0dAJPNltHVm0qNFTiaOTFLM2LgGET7hYOWicIbju8ONf8KcficTOuW5mmBwFRM1nsdO6SeAyeE0XjicIB2co/640?wx_fmt=png&from=appmsg)

导致其他人下不了单

![](https://mmbiz.qpic.cn/mmbiz_png/burEQVgkS5DaOZ8aGZC54Liab7EwoK508iccx0JDHickPkxsuiaDaQOEk6vuA2jbpQq9YmmibOEiaxqor4wpO95Nic1pRcaL92mYBlplIOJcI4VDI0/640?wx_fmt=png&from=appmsg)

订单两小时后会自动取消，只需要写脚本每2小时后提交订单就可以实现库存一直为0

白捡的中危

![](https://mmbiz.qpic.cn/mmbiz_png/burEQVgkS5Ce8g4Uibs0uFySRWfqGc0qREUb0qponYumQ373mUEnAib5cQxUMxFzlwAoAHKK0rvQUNq5RAicicK1hxLcF0xbicSiaRfiapNsG2O5pc/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/burEQVgkS5D9xVpkqJiaqj8SmNu5IxNWhObGdylf0yDgsH1BmSUVorcrE4cRL44QNYJgVCO9KHELMjFibvRqbbj38jNTKQUvwtuiczmVcvtNyA/0?wx_fmt=png)

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