---
title: 【全球首发】【6w$赏金】微软身份漏洞-未授权强制解绑任意微软账户邮箱
url: https://www.freebuf.com/vuls/419097.html
source: FreeBuf网络安全行业门户
date: 2025-01-06
fetch_date: 2025-10-06T20:09:24.778278
---

# 【全球首发】【6w$赏金】微软身份漏洞-未授权强制解绑任意微软账户邮箱

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

【全球首发】【6w$赏金】微软身份漏洞-未授权强制解绑任意微软账户邮箱

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

【全球首发】【6w$赏金】微软身份漏洞-未授权强制解绑任意微软账户邮箱

2025-01-05 13:35:19

所属地 上海

## 致谢

我是Feng Jiaming，公开别名 Sugobet/M1n9K1n9，来自中国广东工贸职业技术学院的在校学生。

I'm Feng Jiaming, my public alias Sugobet/M1n9K1n9, a student from Guangdong Polytechnic of Industry and Commerce, China.

感谢TryHackMe和htba等国际网络安全平台/团队/企业，使我真正踏上了网络安全之路，并利用你们所教导的知识：实现自己的梦想、上大学、让自己的生活越来越好....。这一切少不了你们的功劳，我已无数次在我的博客文章中感谢你们。

Thank you to international cybersecurity platforms/teams/companies such as TryHackMe and htba for truly embarking on the path of cybersecurity and utilizing the knowledge you have taught me: realizing my dreams, attending university, and making my life better and better. All of this is thanks to your contributions, and I have thanked you countless times in my blog posts.

今天，也将毫不例外，TryHackMe，再次感谢你们对网络安全的付出，很高兴我们能够相遇。

Today, without exception, TryHackMe， Thank you again for your dedication to cybersecurity. It's great to meet you

感谢暗羽喵（darkwing\_nya)、glzjin（赵今)、祭天（eson)等各位安全前辈大佬。感谢你们在我还处于萌新时期时，给予我的引导和建议。

也感谢三哈、陈橘墨、探姬、sangsec、神秘景观、urkc等师傅的帮助。

## 未授权强制解绑或绑定任意微软账户邮箱

是的，即将2025年了，或许我们谁都不会想到微软account.live.com上还存在这样如此简单的IDOR，并且它可能已经存在许多年，而这个功能至今仍在被使用。

本文提到的所有漏洞均已修复。

## 前言

发现这个微软账户类漏洞并不是因为我刻意去参加微软漏洞赏金计划，而是源自一场黑客入侵我的旧微软账户，根据有关情报披露，这场入侵与近期大范围撞库活动有关我在尝试找回我的旧微软账户时，发现了该漏洞，并成功将我的旧微软账户qq邮箱拯救出来，控制权再度回到我手中，避免了落入黑客之手。

时间表

2024.10.30 - 发现漏洞

2024.10.31凌晨 - 提交漏洞至msrc

2024.11.2 - 漏洞状态从"New"更改为"Review/Repro"

2024.11.27 - 漏洞状态从"Review/Repro"更改为"Pre-Release"

2024.11.28 - 微软赏金团队发来邮件，认为该漏洞符合"微软验证赏金计划"，授予60000美元赏金奖励（由于微软在11月中旬恰好推出了“零日任务”计划，赏金提升原来的50%，即40k$+20k$)
2025.1.3 - 倒天闭

漏洞1与漏洞2(可能的)概述
msrc将该漏洞评估为：
严重性：严重（critical）
安全影响：权限提升

![](https://image.3001.net/images/20250105/1736056294_677a1de6944ff3eca5524.jpeg!small)

该漏洞表明微软账户绑定了任意邮箱或使用任意邮箱注册的账号，将受到此漏洞影响，攻击者可在未经授权情况下，通过该漏洞强制任意邮箱取消验证（解绑），且无法再在原微软账户上重新绑定该邮箱，解绑后攻击者可通过该邮箱重新注册微软账户。

而漏洞2(可能的)与漏洞1恰好相反，漏洞1是强制取消验证；而漏洞2(可能的)则是强制验证，也就是强制绑定任意邮箱。

另外，事后我还发现，除了漏洞1和漏洞2(可能的)外，还可能受到漏洞影响的api端点有：邮箱别名绑定或取消我发现的所有可能遭漏洞影响的api端点如下：https://account.live.com/Email/Remove
https://account.live.com/Email/Verify
https://account.live.com/proofs/Remove
https://account.live.com/proofs/AddConfirm
https://account.live.com/Aliases/Verify
https://account.live.com/Aliases/Remove

不过由于发现这些东西时微软方面正在修复该问题，所以我并未真正意义成功攻击，具体是否存在将交由微软调查

## 漏洞1细节

otc（大概率是one time code的缩写）
产生的原因是由于"otc"参数检验存在问题，只要otc=\*any(有星号)，那么攻击者将能够操控poc url中的mn参数，导致后端验证失效，从而越权取消验证任意电子邮件地址。

![](https://image.3001.net/images/20250105/1736056422_677a1e66bc1863cc97b99.png!small)![](https://image.3001.net/images/20250105/1736056611_677a1f239ce28a78a670e.png!small)![](https://image.3001.net/images/20250105/1736056730_677a1f9a5f0a8489636fa.png!small)

这个时候我们再通过已取消验证的电子邮件地址登录login.live.com，我们就会发现我们已经无法再重新绑定该邮箱，但在这个页面必须绑定一个电子邮件地址，否则账号将无法使用，会被强制注销登录。

![](https://image.3001.net/images/20250105/1736056741_677a1fa59b9a9b04ef6e5.png!small)

但如果在上图页面中选择绑定其它邮箱后，原来被取消验证的邮箱将无法再通过原邮箱进行登录，直接号（登录方式）没了，这个时候我们就可以重新利用该邮箱重新创建微软账户了，即便不绑定其他邮箱，也仍然可以强行重新注册，具体请看文章的漏洞价值。

![](https://image.3001.net/images/20250105/1736056863_677a201f7da05fd439d94.png!small)

## 漏洞2（可能的) - 未授权强制绑定任意邮箱

11月7日，我再度通过otc参数验证问题思考，设想：既然可以强制解绑，那验证呢？

于是我立刻去尝试验证邮箱功能是否存在该问题：

poc url: [https://account.live.com/Email/Verify?otc=\*anyanyany&mn=test%40qq.com&ru=https://account.microsoft.com/auth/complete-signin&cxt=Default](https://account.live.com/Email/Verify?otc=*anyanyany&mn=test%40qq.com&ru=https://account.microsoft.com/auth/complete-signin&cxt=Default)

首先我通过，在微软小号为其识图绑定一个不存在的qq电子邮件地址。

![](https://image.3001.net/images/20250105/1736057112_677a21186ad7fcc43326e.png!small)

此时，微软向该邮箱发送验证邮件，这个时候我们通过poc url，就可以直接验证成功并成功使用新绑定的电子邮件地址登录

然鹅：testminglive1@qq.com压根就不存在，这只是我凭空捏造出来的

![](https://image.3001.net/images/20250105/1736057084_677a20fc9dbf0942c6c7f.png!small)

这一新的发现也印证了"otc"参数处理的确存在问题，可能有多个功能点受到影响

不过由于发现这些东西时微软方面正在修复该问题，所以我并未真正意义成功攻击，具体是否存在将交由微软调查

## 如何发现该漏洞？

就像前言说的那样，发现该漏洞并非我有意为之，只是我不希望我的旧微软账户qq邮箱落入黑客之手。

所以我甚至连burp suite都没有打开，仅在浏览器完成所有操作2024年10月30日，我的旧qq数字邮箱收到一份来自微软的邮件，内容是我的旧微软账号被异常登录。

![](https://image.3001.net/images/20250105/1736057185_677a21612eef8042651b1.png!small)

并且这封邮件在间隔几小时后再次发到我的邮箱上，说明黑客已经通过某种手段破解了我的账户并在一天时间内登录成功了两次。

当我尝试通过这个qq数字邮箱在login.live.com上进行登录时，却发现密码错误，并且所绑定的手机号也不再是我的。

我缺乏对微软账户的理解，且发现无法通过我的qq数字邮箱找回密码，这是非常让我吃惊的，即便是申诉也压根无法通过。

但问题是，找回密码如果不能通过邮箱找回，那就只能通过手机号短信验证码，问题是手机号已经被黑客篡改

在万般无奈之下，我只能通过qq数字邮箱寻找过去与微软邮箱的历史邮件，试图从过去寻找情报信息最终在2018年1月的历史邮件中，我发现了这个：

![](https://image.3001.net/images/20250105/1736057259_677a21aba7621cead6fcd.png!small)

没错，这是当初绑定qq数字邮箱时的验证码邮件

我把目光投放到了上图箭头所指的单击此处的url，当我访问该url时，我惊讶的发现居然还能用！

(由于是漏洞复现以及思路回放，下方相关截图的qq并非上文，而是小号，并且url参数已做脱敏处理)

![](https://image.3001.net/images/20250105/1736057282_677a21c2e4aa7525038a6.png!small)

qq小号

![](https://image.3001.net/images/20250105/1736057348_677a22041b363490302df.png!small)![](https://image.3001.net/images/20250105/1736057474_677a228240532045cef00.png!small)

经过我用最近的邮件和2018年的邮件相关url进行对比，我发现漏洞产生的原因是由于"otc"参数检验存在问题，只要otc=\*any(有星号)，那么攻击者将能够操控poc url中的mn参数，导致后端验证失效，从而越权取消验证任意电子邮件地址

为了确定该漏洞确实存在，我让朋友使用qq邮箱注册一个微软账户，并且利用该漏洞取消验证他的qq邮箱

好友的截图：

![](https://image.3001.net/images/20250105/1736057719_677a2377c810bb7c99efa.png!small)

此时，被取消验证的邮箱无法再在该微软账户上重新绑定，只能绑定其他的邮箱

![](https://image.3001.net/images/20250105/1736057774_677a23ae11416eee61810.png!small)

经过多次的测试，我发现该漏洞似乎对任意绑定了微软账户的邮箱都有效，更具体的成因让我们交回给微软安全响应中心吧！

## 漏洞价值

最后对于该漏洞的利用价值，我个人认为：该漏洞在攻击者持有受害者邮箱时，利用该漏洞可以将已绑定的邮箱强行解放出来，并允许攻击者利用该邮箱重新注册一个新的微软账户

下图是已绑定的qq邮箱，此时无法再创建账户(缺乏当时的截图，下图是其它账号演示)

![](https://image.3001.net/images/20250105/1736057795_677a23c31d915dc1be9ab.png!small)

若通过该漏洞强制解绑邮箱之后，将可以重新创建账户！

![](https://image.3001.net/images/20250105/1736057831_677a23e7ebd411957423e.png!small)

即便攻击者没有控制相关电子邮件地址控制权，只要攻击者拥有大批量已绑定微软账号的电子邮件列表，那么也能发起大范围恶意攻击，这将会迫使所有受害者必须更换一次电子邮件才能继续使用他们的微软账号。

但更严重的是，威胁行为者可以重复这样的攻击，持续对受害微软账户反复发起这样的攻击，从而影响账户的正常使用。

## 价值40万人民币的教导

先提前解释一下，虽然有点遗憾，不过内心很平静，整个过程中，可能唯一令我兴奋的一刻就是这个漏洞被认可的那一刻：即收到6万刀赏金邮件的那一刻。

相比于成就和爱好，还好我对钱并没有什么太多的兴趣和期望，不然我想换另一个，人一定会当场休克过去尽管最后。

我还会获得120积分并进入微软MSRC 2024 Q4排行榜北京时间2025年1月3日晚上十一点多，经过长达一个月的调查，msrc认为我在社交媒体上公开了漏洞截图，事实上我并未公开与漏洞报告相关的任何截图，仅分享了获得赏金的邮件截图。

![](https://image.3001.net/images/20250105/1736057861_677a2405743b785e48b57.jpeg!small)

但我尊重msrc的调查，如果他们认为我公开获得赏金邮件截图属于违反规则的话。

![](https://image.3001.net/images/20250105/1736057920_677a244088839403c8b28.jpeg!small)

很显然，从我的立场来看，仅向公众分享了获得赏金的邮件截图，并未涉及到具体漏洞相关可逆介绍和漏洞细节，是没有问题的。但令人没想到的是，这居然也在保密范围内，即使在我反复翻看规则的情况下。

幸好在整个过程中没有什么太多的情绪波动，也没有对自己的计划做调整，一直以不变应万变，暂未对我自己的行程造成什么损失。

最后，这个漏洞发现的原因也是因为我不放过小事、注意细节，而错失赏金也是因为我放过了小事、没有注意细节。

网络安全并不是我的最终梦想职业，只是梦想职业的其中一个技能点。

这的一课，同时也为了最终梦想职业，我们今后会更注重于高度的隐秘性（即使我在三四年前曾要求过自己注意隐秘性问题，但我也没想到我不但想的不够周全，并且还会影响到三四年后的今天）
保持学习，保持思考，保持警惕，对梦想职业的热爱和向往。

# 漏洞

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

致谢

未授权强制解绑或绑定任意微软账户邮箱

前言

漏洞1细节

漏洞2（可能的) - 未授权强制绑定任意邮箱

如何发现该漏洞？

漏洞价值

价值40万人民币的教导

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
*...