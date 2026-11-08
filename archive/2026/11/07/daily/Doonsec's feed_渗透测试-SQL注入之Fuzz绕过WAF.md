---
title: 渗透测试-SQL注入之Fuzz绕过WAF
url: https://mp.weixin.qq.com/s/d_i5ef6cgFutlDoQI8vEBQ
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:11:47.540060
---

# 渗透测试-SQL注入之Fuzz绕过WAF

# SQL注入之Fuzz绕过WAF

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 前言

打 SQL 注入的时候，最常见也最憋屈的一幕：payload 刚发出去，页面直接给你拍回来一个 WAF 拦截页。安全狗、云锁这一挂，手工去猜哪种混淆能过，基本等于大海捞针——猜一个错一个，测试节奏全被打断。

其实换个角度想，WAF 的本质就是拿规则库去匹配请求里的参数内容：规则是有限的，而注入语句的变形组合是无限的。既然人肉猜不动，那就把这个"猜"的过程交给工具批量去试——这就是 Fuzz 的思路：生成大量混淆变形的 payload 批量提交，按返回差异筛出 WAF 不拦的那种写法。

这篇用 sqli-labs 第一关挂上网站安全狗做靶场，完整走一遍：payload 被拦 → 抓包定位被检点（空格）→ 用 /*a*/ 这类变形构造字典 → Burp Intruder 批量跑 → 按返回包差异确认绕过成功，最后拿到数据库信息。这套思路不挑 WAF，换成别的防守产品照样能套。

## 一、什么是Fuzz

在讲fuzz与sql注入结合绕waf之前我们先来讲讲什么是fuzz，fuzz其实就是一种对请求参数的模糊测试，简单来说就是对一个接口的某个参数或多个参数用自定义的内容进行批量提交，根据接口返回内容来判断自定义内容参数对接口的影响。

首先先说waf防御的原理，简单来说waf就是解析http请求，检测http请求中的参数是否存在恶意的攻击行为，如果请求中的参数和waf中的规则库所匹配，那么waf则判断此条请求为攻击行为并进行阻断，反之则放行。

常见的sql注入绕过waf有两种方式，一种是利用waf可能存在的http协议解析缺陷来绕过waf，另外一种是利用各种方式来包装sql注入语句进行混淆来绕过waf的规则库。

FUZZ与sql注入waf绕过结合
      首先来说说造轮子的原理，fuzz是对某个接口的一个参数或多个参数进行自定义参数批量请求的模糊测试，sql注入的漏洞成因是某个接口中后端没有对某个参数或多个参数的内容进行过滤并将参数内容直接合并到sql语句中进行查询，waf的防御原理是解析http请求，对里面每个参数的内容根据规则库进行匹配，那么通过fuzz结合sql注入对waf进行绕过的原理也就显而易见了。

首先我们生成大量经过混淆的sql注入语句，然后填入对应参数中，进行批量发送，根据返回内容进行判断waf是否对这种混淆方式进行拦截，如果拦截则判断这种混淆方式不可取，如果不拦截则可以用这种混淆的方式对所有的sql注入语句进行包装。

然后用burp生成fuzz字典，进行爆破就可以了。

## 二、利用Fuzz绕过WAF获取数据库信息

### 1.Fuzz绕过方法

这里我们下载网站安全狗作为WAF，用sqli-labs实验第一关进行测试 首先我们输入 http://192.168.222.4/sqli-labs/Less-1/?id=1’

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1go9hj7NBKEiaX533uK2mBrDWGeG77hOSicSYxGibQwCoKHeLG6yic0J479Z9KwHTV1H3bamNScKbbw7ibw1k215knibT5GUW8c2ox9mk/640?wx_fmt=png&from=appmsg)

发现报错，进行SQL注入试试，输入 http://192.168.222.4/sqli-labs/Less-1/?id=1’ and ‘1’=‘1

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gpV21BicqxRXeibjuZ2uaiadBtjYicJrxd1NouOFuKRoXnzW12W8VhwC44EjxtQUUlPicQQQdfqb9lGKuPicrUNQ6c5h0H0ticluYueVg/640?wx_fmt=png&from=appmsg)

发现WAF进行了拦截，无法进行注入，这时我们就要借助burp进行抓包，进行Fuzz绕过。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpTZ9h67PyjkM8yfib07UkJwg6AdrsOnJnkib0L5Gtw9eHHpbtLZjZlNxBpjxa2zBvog1qnXBzScxq6x4SvLS7LuAelo1MxmCcfc/640?wx_fmt=png&from=appmsg)

这时我们发送到intruder进行爆破，这里我补充一些知识，如何进行设置参数爆破， 我们可以对空格进行转义，空格有很多的编码表现形式，（’ '==%20）

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1goLRQ4REaibgK1gXNYPkL1K6UJVp2FUrdH6M4SicAXydyqlLNNALRO5xKamFu3rfNZiaBE02lXoHdY2kME3J7zGtwSDsNGMH9gYH8/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1govBLZF0picPm7Micrj0evS2mOCicvgXzE5vVwhpdxYS9NdxIIAezOuAzmEt3PR2xLiaqZ8WxibG2Hu9JRKibnOWkmVYEmQaoDn4Gpg8/640?wx_fmt=png&from=appmsg)

像我们黑盒测试绕过方法中有对空格进行转义的字符，可以利用构造特殊字符进行爆破，这里我们利用/*xxx*/进行实验。

### 2.利用Fuzz绕过WAF获取数据库信息

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grnyFakup39NtS2aVvNgj9hDKdGfenNKMUp0csU50jOGicLwDExibib16mUIKjIkgv7ibMWD7qov4bo1h2xOayVgOjg6ciao3QcE6E4/640?wx_fmt=png&from=appmsg)

http://192.168.222.4/sqli-labs/Less-1/?id=1%27%20and%20%271%27=%271 我们就可以将%20进行转换为/*a*/，设置参数，设置字符a1!%(/)，和payload

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grwOlsAKiboKcicCgjaRSKgXFR8ejCnFYHagztYqSicicLN2btXrEvwng7jTJsqZTyZUSqoBIm5TFr92QNO3nK3iaXs7epGp806tlic4/640?wx_fmt=png&from=appmsg)

设置线程为20

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gr4uCe90ojBsG2LnibyXGzflHNOiadfLbZZCehldcczFbCD1xzVIagibs4Qd1uTViaQICGCQiaMeY0PzOTbibtHCQGSeoUZarQNrvST0/640?wx_fmt=png&from=appmsg)

进行攻击

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpwg9cQiaxpdMVW7zn6htSD1hKAXoA2G81zVzbJQIP3jbWghBAeEoMcWlMhK2wdA60iakrPwK5qoMVHdIvwh3f7FvdOpIWusSGUM/640?wx_fmt=png&from=appmsg)

这里返回不一样的数据包，再查看一下图片，看一下render

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gpGvqWyYwIVgGy5jdQJr3ugenDicib2ZjduSibDnicLHeAxzxSpv1qic8yXOdb8z8Lwov6VkTlh6Z8buU14GClnopsREkYbHc9pFCuI/640?wx_fmt=png&from=appmsg)

发现返回了用户信息，绕过成功。 这里同样可以通过查询语句注入，在进行burp爆破就可以了，找不同的数据包就可以成功绕过，查看数据库信息了。

## 总结

Fuzz 绕 WAF 说白了，就是把"人肉猜混淆"变成"批量试混淆"：WAF 拦的是规则库里已有的写法，而空格、注释符、URL 编码这些元素排列组合起来近乎无限，让 Burp 按字典把组合跑一遍，哪个返回包长度、内容不一样，能过的混淆方式自己就浮出来了。

落到操作上就四步：先确认注入点，再抓包看 WAF 到底拦在哪个字符（这篇里是空格），然后针对被拦点构造变形字典（/*a*/、%20、/\*\*/ 混着来），最后 Intruder 批量跑、按返回差异筛选，用能过的姿势去包装完整的注入语句。字典质量决定上限——平时实战里撞到的新变形随手记进字典，攒得越多越能打。

反过来看防守侧：规则库挡得住已知姿势，挡不住变形组合，真正的根子还是参数化查询把注入堵死，WAF 只当第二道保险；再定期把拦截日志里的攻击样本反哺进规则库，让"批量试"的字典失效速度跟上攻击者的更新速度，才算闭环。

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HezRQjNneVHy39103FjCvxFaZicO2OgEB05ZbBLwibDiaCTqDJNUHUCC9OXjVeiasG4ibOVR0dg284RCzVquVhvQ3xQ/0?wx_fmt=png)

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