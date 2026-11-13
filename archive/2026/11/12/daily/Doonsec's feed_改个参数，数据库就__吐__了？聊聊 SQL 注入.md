---
title: 改个参数，数据库就\"吐\"了？聊聊 SQL 注入
url: https://mp.weixin.qq.com/s/eQdGAmMnyuDW1uVPAEd-Ow
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:56:41.900982
---

# 改个参数，数据库就\"吐\"了？聊聊 SQL 注入

# 改个参数，数据库就"吐"了？聊聊 SQL 注入

三垣网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

前言

你在逛一个网站，点击某个案例详情页面，地址栏里多了个 `id=104`。你随手改成 `id=105`，看到下一个案例——好像很正常对吧？

但如果有人发现，把 `id` 改成一段特殊的"代码"，网站就能把数据库里的东西一五一十"吐"出来呢？

2025 年，攻击者发现某学院实践平台存在 SQL 注入漏洞，攻击者靠改 URL 里一个参数，硬生生把数据库名、表名、数据全扒了出来。

今天就从这个案例出发，掰开揉碎讲清楚 SQL 注入到底是什么、怎么打、怎么防。

漏洞基础认识

什么是SQL注入？

简单说：\*\*网站把你输入的内容当成代码执行了\*\*。

后端程序员写代码时，需要从数据库取数据，就会拼一条 SQL 语句：

SELECT \* FROM cases WHERE id = 104

问题来了——如果程序员偷懒，直接把用户输入的 `id` 参数拼进去，而不是"参数化查询"，攻击者就可以构造一段"代码"混进去，让数据库执行额外的指令。

类比： 你给外卖小哥发消息："给我一杯奶茶"。但如果你发的是"给我一杯奶茶 + 顺便把你老板电话发过来"，而小哥真的照做了——这就是注入。本来你只想下单，结果还套出了内部信息。

漏洞案例

1、注册账号

此处存在注册账号功能，可以自主注册账号

随手注册admin1/123456，成功登录

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGK2m49rbdaguf3bd63FQHtYESoNiapcWocNEPylSwTuOClicZBu8PxskkcyLs4wNl9IYnu2So9MhskibyLzzlpictfhX1s6sIzgA7s/640?wx_fmt=png&from=appmsg)

2、初步试探，确认存在注入

浏览到一个案例详情页，URL 长这样：

http://xxx.edu.cn/index.php/Case/index?id=104

这里的 `id=104` 就是可能有问题的参数。

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGJbL9b6So5F72X88hJGuRcFYqQ814JsvBAKicUQsyfGTzyNXRNNN0mbOVaYUvOds6AiaHRzpE4UdA33ibYl9hRRWMaZq0zpRhmbnc/640?wx_fmt=jpeg&from=appmsg)

那这个时候我们就应该思考一下，这个参数是否可以注入，直接开始测试

我们没有直接搞大动作，而是先做一个最简单的"真假测试"：id=if(1=0,111,113)

解释：这是 MySQL 的 `IF(条件,真值,假值)` 函数。`1=0` 是假，所以返回 113；如果条件改成 `1=1`（真），就返回 111。

如果真的存在sql注入，那么这些就会被解析，返回的内容会随着id的变化而改变，我们只需要判断文章内容就可以判断此处是否存在SQL注入

测试结果：两种情况页面响应明显不同——确认注入成立。

3、爆破数据库名的长度，进一步测试

先搞清楚当前数据库有多少个字符：

id=if((length(select(database())))=19,111,113)

逐个数试（1、2、3...），当等于 19 时页面返回正常——库名长度是 19

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGLZwlqUque1rGkyGc1BP9T0Z8bHa4fdMvYqiauffr2aghyOhWSKOpnnuQY9NQH4CQiaJoqwosDIicOwvVcfl6I7fiaycwDljTCWoeI/640?wx_fmt=png&from=appmsg)

成功验证此处存在sql注入

知道了长度 19，现在开始"猜字游戏"。从第 1 位开始，用 `substr` 截取一个字符，枚举 a-z、0-9 等常见字符：

id=if(substr(select+database()),1,1)='a',111,113)    ← 猜第1位是a？

id=if(substr(select+database()),1,1)='b',111,113)    ← 猜第1位是b？

id=if(substr(select+database()),1,1)='p',111,113)    ← 页面正常！命中了！第1位是p

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGI0BIR6Thcib3hMibRfBJa4TtYO0UEasu9HHJH68J64VM3BwMT7qmwJT2Ctgyu13iax88gibPfFyLrLp2A4LBIyhRe9H1nGP8Exl48/640?wx_fmt=png&from=appmsg)

第 1 位猜完，猜第 2 位、第 3 位……一直猜到第 19 位。每位字符用 Burp Suite 的 \*\*Intruder（爆破器）\*\* 自动枚举，通过响应长度差异判断真假。

最终爆出库名为：\*\*`productionlogistics`\*\*（19 个字符，正好对上）。

思考原因

为什么会有sql注入？

就一个原因：后端直接把用户输入拼进了 SQL 语句

以php代码为例：

// 危险写法（伪代码）

$sql = "SELECT \* FROM cases WHERE id = " + $\_GET['id'];

$result = mysqli\_query($conn, $sql);

攻击者传什么，后端就拼什么，完全不设防。

// 正确写法：参数化查询

$stmt = mysqli\_prepare($conn, "SELECT \* FROM cases WHERE id = ?");

mysqli\_stmt\_bind\_param($stmt, "i", $id);   // "i" 表示强制转整数

mysqli\_stmt\_execute($stmt);

参数化查询把"SQL 结构"和"数据"彻底分开——`?` 的位置只能填值，绝不会被当成代码执行。这是业界公认的防注入标准做法。

总结

SQL 注入之所以可怕，不是因为技术有多高深，而是因为很多程序员图省事，把"用户输入"和"代码"混在了一起。对开发者来说，记住一条铁律——

永远别把用户输入拼进 SQL。要么参数化，要么先转类型。

#Web安全 #SQL注入 #布尔盲注 #漏洞科普

求点赞

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/SxoDJcKqQGLgMrWIkDNHPl5e7P9qibYyV8Y50EI1icff4SSIfAthpjaatP7icuqlunzPqIwjSe0d4OsBEKziaNG6nib4j0zjibCYnw4KQcTj61ggY/640?wx_fmt=gif&from=appmsg)

求分享

![](https://mmbiz.qpic.cn/mmbiz_gif/SxoDJcKqQGIYcVofLjZ0GDqpxkFeg0FlJE7xtfYrR83U2ZQtX734CGICibpgKaZtexQNWSyiaPb8KhXMbKltefmgkSehmzBz7RvFxXzweIFPI/640?wx_fmt=gif&from=appmsg)

求喜欢

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/SxoDJcKqQGLbowKESPYWx5w5YI2ESYOF8sjY9I9IetJyPjyqmr2yGkhpPdKovZV3TtBSic9TYRaAOtoiaVL67MsKctH6BMmePQAjUBXDRt5rs/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJaWOwicn7raXm5k4xXDlBia0Okyg0R9d4niakArWeAcFZe0mbIWPKXdgcJHv0mIY6picqR7UB0GmPPeMC70E9VFWMXDEdYOj8GS3o/0?wx_fmt=png)

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