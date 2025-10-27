---
title: 基于Smart Glocal的Telegram支付网关介绍
url: https://blog.upx8.com/3064
source: 黑海洋 - WIKI
date: 2022-11-03
fetch_date: 2025-10-03T21:40:03.970386
---

# 基于Smart Glocal的Telegram支付网关介绍

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 基于Smart Glocal的Telegram支付网关介绍

发布时间:
2022-11-02

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
42877

# 注册条件

1. 一个经得起审查的TG频道，你必须是拥有者，然后把 @donate 这个机器人拉到管理员中然后上权限
2. 基于SUMSUB的身份验证，支持中国大陆身份证（上传正反）、3d人脸（类似Faceid的转圈）
3. 收款方式

提供频道ID->拉机器人到管理员上权限->填表登记（收款信息、售价信息、推送信息，后面可改，不验证）

->身份验证（To finalize registration we need you to verify your identity. Please take a selfie and provide your ID）

->Great! You are almost done with registration. Please wait, we are verifying your personal data. We will be back with an update for you soon.

->Awesome! You are verified. We will be back with an update for you soon.（耗时6分钟）

->Please wait while we are reviewing your channel

之后就没有提示了，直接就能用

# 付款方式

单笔交易1~2000EUR交易额（部分功能1000EUR），或者也可以RUB

币种只能是EUR、RUB，不支持USD（当然，USD等卡是能付的）

付款方式支持：银行卡、Apple Pay、Google Pay

交易对象直接就是 Smart Glocal自己（HK、HKG），没有任何频道、Telegram标志。

## 进一步的付款测试

1，中国大陆，中行银联信用卡（625906），直接显示卡号红色不能继续
2，中国大陆，广发银联信用卡（622556），输入时显示Discover、扣款时显示Upay，但是直接报错（不能确定是否是银联3D的问题）（没有跳外管局限制商户）
3，中国大陆，广发万事达信用卡（536998），跳万事达3d验证、验证后通过付款
4，美国，Discover信用卡，也是填卡号可以，但是要付款的时候就付款失败
5，美国，Apple Card 信用卡，使用ApplePay，直接付款104欧元，0风控顺利过关，没有跳额外的3D验证（虽然网传ApplePay下的AppleCard支持3D验证）

另外在ApplePay中，京东闪付、银联、Discover显示不支持，VISA、万事达、运通显示支持，借记卡、信用卡、预付借记卡都可以【官方FAQ说支持AP、GP、VMA】。

应该是不会Cash Advance（因为Applecard不支持CA）

# 费用

交易费用：2.5%，单笔最低0.08 EUR（如果是付费Post的，需要额外15%）
提款费用：卡组织转账 2%+0.5 EUR，国际电汇是15EUR（TOS有，FAQ没说）

# 提款方式

国际电汇（欧美英中港等）、卡组织转账（欧英港等）【100EUR起提】

考虑到可能是EU的银行的swift电汇，本来我打算用CapitalOne接（但是考虑到货币转换、中转行、以及普遍性）

我改用Wise的比利时EUR账户（看上去没说收费，理论上都是欧洲可能中转行没有或者便宜、速度应该更快，没有货币转换）看看

提款时间是每月10日提上个月的下半月，每月25日提这个月的上半月，相当于D+10~25

# 官方文档和相关网站

[https://smart-glocal.com/terms-creator](https://blog.upx8.com/go/aHR0cHM6Ly9zbWFydC1nbG9jYWwuY29tL3Rlcm1zLWNyZWF0b3I)

[https://telegra.ph/FAQ-09-08-13](https://blog.upx8.com/go/aHR0cHM6Ly90ZWxlZ3JhLnBoL0ZBUS0wOS0wOC0xMw)

[https://t.me/donate](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL2RvbmF0ZQ)

[https://t.me/author\_support\_bot](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL2F1dGhvcl9zdXBwb3J0X2JvdA)

# 常用功能

1，Donate 直接一次性付费（还支持自定义附加小费，也就是说，你只需要设置1EUR的单笔付费，客户可以自定义附加） （可以看到付款人ID）

2，付费看付费内容（额外15%手续费），支持图片视频。

3，支持订阅 Subscription payment （可以看到付款人名字）

4，付费进频道（管理员也可以免费手动批准）

# 合规限制

您声明并保证您是数字内容的创作者（作者）和/或拥有发布数字内容的适当权利。

您还确认并保证数字内容：

i) 不违反服务条款；

ii) 不违反适用法律、追随者和/或创作者的属人法；

iii) 不侵犯第三方的权利（版权、专有权、个性化手段的权利等）；

iv) 不基于性别、性取向、种族、肤色、国籍、语言、出身、对宗教或其他信仰的态度进行歧视；

v) 不包含对某些政治信仰的宣传，以及关于政治的负面或批评性陈述；

vi) 不要求暴力、极端主义活动、推翻现有政府或其他机构、使用或分发麻醉药品和精神药物以及适用法律禁止的其他活动；

vii) 没有诽谤，侮辱或诋毁性格；

viii) 无意引起对未成年人类儿童的性感觉或为性行为辩护。

我们严禁使用服务购买、出售、分发或支付：
1.任何犯罪活动：
• 煽动、招揽或宣传仇恨/暴力/种族主义/宗教迫害；
• 鼓励、宣传、协助或指导他人从事非法活动、欺诈或销售危险品或危险品；
• 鼓励、促销和销售违禁商品和服务：
‣ 毒品/非法物质、类固醇等，以及相关的吸毒用具；
‣ 武器、枪支和弹药；
‣ 香烟和任何烟草制品；
‣ 药物、膳食补充剂；
‣ 政府身份证或文件；
‣ 被盗商品，包括数字和虚拟商品；
‣ 电话卡；
‣ 欺诈/欺骗性营销行为；
‣ 高风险文件托管/共享和网络锁；
2. 任何形式的高收益金融投资和快速致富方案：
• 金字塔或庞氏骗局、矩阵方案；
• 在线交易服务；
• 赌博业务（赌场）、投注、网上投注；
• 一分钱和反向拍卖。
3.任何形式的侵犯知识产权
• 侵犯任何正式注册的版权/商标或其他侵犯知识产权的行为；
• 未经版权持有人/授权组织颁发的许可，分发音乐、视频、软件和其他产品；
• 经销假冒产品，经销无证产品；
4.适用法律和/或创作者或追随者的属人法禁止或限制的任何其他商品。

***看上去并没有限制成人色情、政治、动漫等内容？***

## 争议

1. 如果追随者的争议付款金额或数量不超过本公司在相关月份为创作者收取的总金额和/或付款总额的20%，本公司有权拒绝将争议款项转移至在收到有关这些有争议的付款的决定之前，创作者将被收到。
2. 如果追随者的争议付款金额或次数超过公司在相关月份为创作者收取的总金额和/或次数的 20%，公司有权拒绝将所有收取的资金转移给创作者。创建者，直到它收到对所有有争议的付款的决定。

[取消回复](https://blog.upx8.com/3064#respond-post-3064)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")