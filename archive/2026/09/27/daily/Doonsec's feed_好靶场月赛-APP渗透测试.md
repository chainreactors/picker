---
title: 好靶场月赛-APP渗透测试
url: https://mp.weixin.qq.com/s/xQ63dlTfEKUPZftQG1F8MA
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:11.692862
---

# 好靶场月赛-APP渗透测试

# 好靶场月赛-APP渗透测试

原创

studying-egg
studying-egg

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## unsetunset前言unsetunset

中秋假期体验卡已到期，在生存三天就可以领取国庆假期体验卡了，再浅浅的坚持一下

之前没有接触过APP的一个渗透，好靶场今天刚好有一个APP渗透赛，模拟实战，比赛形式很新颖，要不是还要收拾东西，`I can do it all day`

## unsetunset渗透背景unsetunset

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkE6ia6pcBfRNLNZDXxynkYT5Y6ib3uVZW7Kav9ribsaZWpsV8UAyiczmtYH913PdWk2cxmce7rfN6ZDQfTB29rfqKZt479lic7FaIE/640?wx_fmt=webp&from=appmsg)

早上看到这个背景的时候就被深深的吸引住了，真的非常的炫酷，迫不及待的打开环境测试一波

打开靶场下载APK，放入模拟器中运行抓包，开始测试

## unsetunset测试思路unsetunset

### 短信轰炸

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rm3VQT2DeOa5Jat7TBYb9KgqmVpqHdPkRicgibzVwxW9jqdFylYHC6wgNKiaALCTSYAeIYEkv9jxAe3NbUYicBSpkr5Gw7Ru7uicroU/640?wx_fmt=webp&from=appmsg)

这里存在一个验证码发送功能，尝试一下短信轰炸

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rmPxaRKxGwF0QbZtsnLibRufXM3XRpufscpCP0TWcsic7xVtCprkL1EAjRgu1P1ma8p5jfPcYMBrOKpYtKvCdgJVf82OPT5AgKicc/640?wx_fmt=webp&from=appmsg)

这里对短信的频率没有做校验，存在短信轰炸漏洞

### IDOR遍历

通过`JADX`对该APK进行反编译，提取出其中所有包含`api/`的接口

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkrNQyfzqfxMGXNmqaryQoMp8K7VzhXDqT5ib1VffVmZ7qJ03Mhb78CGkxOYoTWmfZoScGxjN3uibmelicnIGy0DEUY7vahGdgx0k/640?wx_fmt=webp&from=appmsg)

```
 认证相关 (Auth)
 - POST /api/sms/send - 发送短信验证码 {phone}
 - POST /api/user/register - 注册 {username, password(sha256), phone, code}
 - POST /api/user/login - 登录 {username, password(sha256)}
 - POST /api/user/reset - 重置密码 {phone, code, password(sha256)}
 - POST /api/user/logout - 登出 {}

 用户信息
 - GET /api/user/info - 获取用户信息
 - GET /api/user/feedback - 获取我的反馈
 - POST /api/user/feedback - 提交反馈 {content, contact}
 - GET /api/feedback/query?id= - 查询反馈

 商品/配置
 - GET /api/health - 健康检查
 - GET /api/config - 获取配置
 - GET /api/products - 商品列表

 订单
 - GET /api/orders - 订单列表
 - POST /api/orders - 下单
 - POST /api/orders/{id}/confirm - 确认收货
 - POST /api/orders/{id}/cancel - 取消订单

 钱包/积分
 - POST /api/wallet/recharge - 充值 {amount}
 - GET /api/wallet/txns - 钱包交易记录
 - POST /api/points/redeem - 积分兑换 {points}
 - GET /api/points/log - 积分日志

 优惠券
 - GET /api/coupons - 我的优惠券
 - GET /api/coupons/pool - 优惠券池
 - POST /api/coupons/claim - 领取优惠券
```

对这里的`/api/feedback/query?id=`这个接口尝试进行遍历

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkGDRGFXNClVCWm4OibribVfpcVOiab022qTl1dFHxCqLgBBNervNf3bM40YLUuiab9OCDPibWuBic88v0kHmxBDMRRJ4r6qIbsRN4xU/640?wx_fmt=webp&from=appmsg)

发现存在IDOR遍历

### 用户接管

`/api/user/reset`这个接口的功能是对密码进行重置，这里尝试接管该账户 因为之前的验证码接口也没有进行身份验证，这里可以获取该用户的验证码

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rlBS7KU3y9Nib6dX5JwH7jSQv9iagnOjqu5GlCpf4W3xCe9D8r8e09Z3wWtrwibibQQ1TJeJUkoCeBRtv0wJ4wZKVyFMsNqwkllDGs/640?wx_fmt=webp&from=appmsg)

重置密码后登录

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rku6zmd3PKCYHhbBTQm2PccT0aFdHX2Qmj04uFU7zJxgWia4jtfGr9VCoBpnhJib4MUlJaRsGAwxhNPwFlZbKsWVG73buia9CiblPw/640?wx_fmt=webp&from=appmsg)

### 0元购

这里查看这个人的订单

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rlHqY05icqicIII7ibWyZjMHd9CkgWYPJCVZWlicmiaeUkuPHCNuNlAcIl7QPAQUmZooiavicTC6t5LgpXcfaDUSVCictC44dBCLAsKaEg/640?wx_fmt=webp&from=appmsg)

实付0元，看来这里还存在支付验证漏洞 通过抓包发现付款的接口为`POST /api/orders`这个接口，只存在两个参数，`id`和`qty`

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rnBxCCPLR8gfem0C1Z3ZoU5gJibCuX9icUOsQe2ZzAepVML9yU3BHqmKrZOrkHiayQgLqYUK2IBf1HRuTHJ2zGxunM5al3TLutZuA/640?wx_fmt=webp&from=appmsg)

这里猜测服务端会解析`items`这个对象，但不会将具体字段与数据库中的进行匹配，这里我们可以添加`price`字段，设置为0，看看是否会扣费

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rk2ejSEZ4tiazswBeaJnhFzXAXD5gbgDzaPibOfiarQtNca4C20jR98cOJjODfxhrgs13HIQWey1ab5O9XRcbot5d0q4SZYuzxgGc/640?wx_fmt=webp&from=appmsg)

这里观察响应中的`total`字段，可以放心值由19.9变为了0

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkKvpDq88S8W8lDUlibq08rznw3MRZnCJF0DgOMy6mf1IwCzuxtL4a7BHvwJicTlUwnJWBYDOf2oZVXGNf19O7dp0rPDFSJCiauA8/640?wx_fmt=webp&from=appmsg)

成功实现0元购

## unsetunset反思unsetunset

第一次对APP进行测试，重点还是放在了接口测试上，经验不足，还得继续学习。

对了，师傅们觉得我可以走到了那杯奶茶了吗

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/UKpIYGnLasKiaktndBsK1icZCdPnhD70PLW8D6ENptOZOHNIAIibQMqKTqqlcBxISjgOkp9Z28up1Puv1aXxObxeA/0?wx_fmt=png)

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