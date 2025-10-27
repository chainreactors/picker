---
title: 安全警示｜TRX 多重签名骗局
url: https://blog.upx8.com/4378
source: 黑海洋 - WIKI
date: 2024-11-03
fetch_date: 2025-10-06T19:15:38.313966
---

# 安全警示｜TRX 多重签名骗局

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 安全警示｜TRX 多重签名骗局

发布时间:
2024-11-02

分类:
[生活资讯/Life](https://blog.upx8.com/life/)

热度:
74610

近期，TRX 多重签名骗局异常猖獗，骗子通过诱导用户下载[假 imToken](https://blog.upx8.com/go/aHR0cHM6Ly9zdXBwb3J0LnRva2VuLmltL2hjL3poLWNuL2FydGljbGVzLzkwMDAwNzY3OTUyMy0lRTUlQUUlODklRTUlODUlQTglRTYlOEYlOTAlRTklODYlOTItJUU4JUFEJUE2JUU2JTgzJTk1JUU1JTgxJTg3JUU1JUFFJTk4JUU3JUJEJTkxJUU5JUFBJTk3JUU1JUIxJTgwLSVFOCVBRiVCNyVFOCVBRSVBNCVFNSU4NyU4Ni1pbVRva2VuLSVFNSVBRSU5OCVFNyVCRCU5MS10b2tlbi1pbQ) 等方式获取用户的助记词，但是却不直接将用户的代币盗走，而是通过修改用户的 TRX 钱包账户权限，导致用户失去对账户内代币的控制权，只能将代币转入钱包，却无法转出。

本文将揭秘 TRX 多重签名骗局具体是如何实施的，以及我们该如何防范这类骗局。

## **什么是 TRX 多重签名骗局**

当我们创建了一个 TRX 钱包后，这个钱包账户默认的拥有者权限为账户本人，阈值为 1，即钱包转账需持有一个拥有者权限的地址进行签名授权才能发起。

![image3.png](https://support.token.im/hc/article_attachments/12718895426201)

注：拥有者权限是指一个 TRX 账户的最高权限，具有该权限的地址可进行该账户内的所有操作。

而当骗子获取了用户助记词，对其 TRX 账户权限进行修改后，用户地址的拥有者权限变为用户本人和骗子共同持有，阈值为 2，即钱包转账需要两个拥有者权限的地址——用户的地址和骗子的地址，共同签名授权才能发起。

![__.png](https://support.token.im/hc/article_attachments/12719015272473)

由于此时 TRX 钱包的转账需要多重签名（用户地址的签名和骗子地址的签名）才能完成，所以这类骗局被称为 TRX 多重签名骗局。

这就意味着，当用户的 TRX 账户被骗子更改为需多重签名的地址后，用户发起的任何交易，都需要骗子的签名授权才能完成，如果只是用户单方面发起交易，就会遇到类似「server：SIGERROR」的报错。

你可能会疑惑，为什么用户拥有自己账户的助记词 / 私钥，也无法「独立完成」代币的转出操作。

以合伙开公司的例子解释一下，你就明白了。假设有一家公司有两个合伙人，他们在这家公司成立之初规定：所有的重大决策要两个合作人都同意进行签名授权，即多重签名，才可以执行。若有一方不同意，决策则不通过。

被骗子修改为多重签名的 TRX 账户就像是这样一家公司，即便用户持有钱包助记词，但也已经无法「独立完成」对这个钱包的转账等重大操作。

用户只能将代币转入这个账户，却无法转出，骗子就是利用这一点从而「放长线钓大鱼」，等到用户在账户中积累了足够的代币后再一次性盗走。如果一个用户从来都是只收款不转账，且不去链上查看自己的账户权限，那他可能会一直蒙在鼓里并持续地向这个账户转钱。

另外，骗子除了通过诱导用户下载假 imToken 方式外，还会通过以下两类方式利用多重签名诈骗：

* 在 Telegram 等社交平台推广充值网站，诱导用户使用数字代币进行充值，实际上是趁用户充值时获取账户的拥有者权限，导致用户失去对账户的控制权；
* 在 Telegram、微信等社交平台公开自己的助记词 / 私钥，诱导用户转入 TRX 作为手续费以转走钱包内的代币，但实际骗子早已将拥有者权限转移，最终导致用户损失 TRX。

## **安全提醒**

imToken 安全团队在此提醒大家

* 下载 imToken 请认准官网 ：[https://token.im/](https://blog.upx8.com/go/aHR0cHM6Ly90b2tlbi5pbS8)
* 天下不会有免费的午餐，切莫贪小便宜
* 定期检查 TRX 钱包账户权限（👇 附有教程）

### 如何查询账户权限

1. 打开 TRX 钱包，切换至「浏览」页面输入 TRONSCAN 并打开。

![image2.png](https://support.token.im/hc/article_attachments/12718895104537)

2. 在输入框输入钱包地址并搜索，跳至账户信息页面并下滑至「账户权限」板块。

![image4.png](https://support.token.im/hc/article_attachments/12718895443225)

3. 如图所示，如果有且只有你的地址持有拥有者权限，说明你的账户权限是安全的。

![image3.png](https://support.token.im/hc/article_attachments/12718895426201)

1. ![难眠的小女孩](//q2.qlogo.cn/headimg_dl?dst_uin=958875986&spec=100)

   **难眠的小女孩**

   2025-04-15 13:29:56

   [回复](https://blog.upx8.com/4378/comment-page-1?replyTo=30557#respond-post-4378)

   我手机都没打开过奇怪的网站，就被盗了

[取消回复](https://blog.upx8.com/4378#respond-post-4378)

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