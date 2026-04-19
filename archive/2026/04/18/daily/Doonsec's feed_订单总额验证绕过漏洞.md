---
title: 订单总额验证绕过漏洞
url: https://mp.weixin.qq.com/s/H_Du3fdmLxJH3kyohEwbCw
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:51:36.603048
---

# 订单总额验证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8tDOXFoCoQicQg0NslXZ5VTHlaGAlRr76ea6EHB3Cw8TKsFwiaZyFQYpCkNbK05wFFoJRUiasvEbwKq3P1s8nf6riatiaGibbUAHYdXeLJ4z41nvo/0?wx_fmt=jpeg)

# 订单总额验证绕过漏洞

原创

游山玩水
游山玩水

山水SRC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 免责声明

**本公众号分享的所有渗透测试技术文章仅面向合法授权的安全测试、学习交流与研究用途。读者必须确保自身行为符合《网络安全法》等相关法律法规，严禁将其用于任何未授权攻击等非法活动。因不当使用或传播相关内容所引发的任何法律责任与风险，由行为人自行承担，本公众号（或本人）概不负责**

## 流程

测试前提

目标网站/APP存在“满X元减Y%”或类似基于购物车总价的促销活动

**测试流程**

1. **触发优惠**：添加商品至购物车，使总金额满足优惠条件（如满1000元减10%），确认优惠生效。
2. **移除商品**：从购物车中移除部分商品，使当前总金额低于优惠门槛（如降至800元）。观察界面，优惠信息可能仍被保留。
3. **拦截分析**：
- 进入结算页，拦截提交订单的请求数据包（**优惠数据包**）。
- 清空购物车，重新添加不满足优惠条件的商品（如总价900元），再次拦截提交订单的请求（**不优惠数据包**）。
4. **对比与篡改**：对比两个数据包，找到标识优惠的关键参数（如 `discount_rate=0.9`, `promotion_id=xxx`, `coupon_code=YYY`等）。将这些参数从“优惠数据包”中复制，注入到“不优惠数据包”的对应位置。
5. **重放请求**：将篡改后的“不优惠数据包”发送给服务器，观察订单是否以不应享受的优惠价格创建成功。

危害

攻击者可以任意以优惠价格购买商品，导致商家收入损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8tDOXFoCoQibBw0WqEvickv0D3aPKXibxPyJqMUtJno7DwEwPiblaaLEGM5JWdxbAVcEBiaRKjDvmxCWhicCZYsqnSpnHv5KT5n4HAiaicxA4JImCCY/640?wx_fmt=png&from=appmsg)

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