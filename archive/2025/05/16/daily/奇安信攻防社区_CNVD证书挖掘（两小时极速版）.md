---
title: CNVD证书挖掘（两小时极速版）
url: https://forum.butian.net/share/4327
source: 奇安信攻防社区
date: 2025-05-16
fetch_date: 2025-10-06T22:23:16.295848
---

# CNVD证书挖掘（两小时极速版）

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### CNVD证书挖掘（两小时极速版）

急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急

（半年前的）早上有个群友在群里问了CNVD证书的事情，开玩笑说被人割不如我来割（本人无犯罪记录信用行为良好洞自己提了其它东西都是梦见的），于是下午找了个空挖了下。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733213774350-17aab22e-81ce-4e12-bace-dd066faba95d.png)
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733211410065-77e066a7-cb77-445d-9ae1-a852ec18f4df.png)
1 仍然是堂堂失败
---------
吹b结束，言归正传。找洞过程略，有手就行。
### 1.1 insert注入
从js里翻到一个log API，原始构造会直接报错：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733273533107-b0c4b340-ba5d-4123-8ec8-d04ace4f9de2.png)
这里猜测NULL应该是从Cookie里取的，由于我尚未登陆所以取不到信息。
试着修改其它参数，简简单单触发了注入：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733289574377-a82486d2-3468-46e9-bb1a-e6bb6bf3c4bf.png)
这不准备下班？于是抄起我的键盘打算手注一下，但是却有点问题：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733289897912-ce24b8db-388e-4164-a3e6-bf7206c6e399.png)
缺少逗号？结合之前的报错“无法从NULL插入...”判断语句可能是INSERT INTO XXX VALUES(A,B,C,\\*,D)。想起这可能是insert时一阵后怕，还好因为是挖洞没有直接sqlmap天上来，插入语句可是很刑的- -。
不过话又说回来，由于cookie里始终为NULL且这里很明显设置了列约束条件，我想知道是否还能从这个原本就该报错的语句里注出数据？
### 1.2 奇怪的 过滤？
试了一圈，还是我常用那几套，但我发现无论是延时还是构造报错都无用，并且后端貌似存在一些奇怪的过滤。
布尔没用很正常，因为这是个insert语句，只有执行成功与否的区别；构造除零报错，不会显示，我一开始以为是oracle做了处理，于是构造时间盲注，换了一堆函数没有执行的。
要不是语法错误报的及时，我真以为这注入是个罐子- -。思来想去，应该是由于列约束执行到前面那个列直接报错结束（不清楚具体原理，oracle我是真的没用过），相当于短路了。
然后我又试图使用堆叠注入，也是失败，中间还报了很多理论上不该存在的错比如缺少右括号、不允许的字符等。\*\*不过当时急着下班，没想到这些小细节还会再让我摔一跤。\*\*
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733297706938-efb81109-ba2b-4cf5-91e1-590394146cb3.png)
2 改包越权强进后台
----------
测来测去还是构造不成语句+对疑似insert测试哪怕是log表+手注也让人毛毛的，想来想去还是换个点。
对登入口测试，返回这里有个success直接改为true看看跳转：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733300851638-62e8009a-d5ac-45a9-a140-008a800fb0e8.png)
跳转后开始选择角色，这里会报null直接随便改个值尝试继续往下走，然后居然跳转到根部，看来根部就是它的后台地址。
尝试直接访问根地址，是个302。本来以为没得测了：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733301054595-99f4e1d1-d44f-4d2a-ad14-7d50dbaa84fd.png)
但这个302有点长啊，点开看看？
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733301011516-daba68ce-885f-4716-af5b-025ffd2699cf.png)
这个302，emm，看上去只是在原始后台html上加了层跳转，直接把包改成200前面的跳转html删除，放包，进入后台：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733214300874-b25acfc8-b095-423e-86e5-522b857ef3c7.png)
3 又见注入
------
进入后台主要还是测基于越权的漏洞。前面忘了，中间忘了，流量包里又发现一个注入，而且这个注入还会报详细错误：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733359190313-5d98f4d5-96d1-4ff2-8826-f54e55fa9956.png)
这下不光有oracle错误代码，也有原始语句了^ ^，于是我摩拳擦掌，这不出货？
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733358557356-037f01af-b1df-419c-aad8-7fb5b441c79d.png)
4 与魔改对刚的那些日子
------------
### 4.1 难道有waf？
现实告诉我，狗屎环境并不会因为换了个端点就好了...测了半天发现还是有很莫名其妙的问题，比如莫名其妙的缺少引号和缺少右括号。
上一个端点处的漏洞由于我实际上并不知道语句，所以并不好发现问题。这里连语句都是正确输入的，怎么会跳这种低级错误？
怀疑跟之前的一些案例一样带了某不可见不可闻不可视的WAF？于是测试一下超长：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733360948868-9466b584-70b1-49b4-82de-079769236d4a.png)
看上去后方并未截断，那么再试试一个随便的从句比如说IF：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733361391274-78fd328b-4e2f-4bec-ace9-44ddc0d954e2.png)
可以看到虽然语句是完整的，但还是出现了缺失右括号。难道是针对关键字的拦截？我们切到第二个包，因为它报错抛出的肯定是执行sql查询（最次，也是调用这个查询函数）的输入值，使用同一句话注入：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733361679252-8bde482f-707b-4fbf-b6a8-95b295249592.png)
也是报错缺失右括号。那么再看下方抛出的报错语句是否有问题：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733361857007-5c7b7192-eb5d-455d-9639-a48e29856775.png)
这看上去明明一点问题都没有- -，难道我对oracle语法的理解不对？
看看是不是关键字拦截，输入一个普通算式，不报错了：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733361918286-891e42c7-fd2e-4e6c-9fd5-af77e64e5095.png)
那么确实可能是存在过滤？但这个过滤可能很奇怪——它只对括号+一些特殊关键字有效，因为我在不使用括号时不会发生其他报错。
既然是过滤那就存在绕过的可能，比如说双写等。双写右括号，失败，双写end，失败。
### 4.2 换到成功
可恶，这也不行，那也不行？还有没有把堂堂SQL注入糕手放在眼里？
不过没事，毕竟没注出来我也不会发文章了——不就是if+括号不能用，大不了我不用就是^ ^。这里报错信息不够详细，直接继续使用盲注。时间盲注还是一样的不成功，但除0报错成功了：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733365260802-21d37258-2c8e-4830-b725-da88cbaaba15.png)
构造一个小小的除零报错：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733365827697-3f92e8ba-0c25-43c7-98dd-9cb62c775ac1.png)
小跑一遍，出货收摊：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1733204873237-0eed6dd8-d0b7-4677-b4b0-19996f6884fc.png)

* 发表于 2025-05-15 09:50:34
* 阅读 ( 4424 )
* 分类：[渗透测试](https://forum.butian.net/community/Pen_Testing)

6 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![阿斯特](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b99df3b5f15d200a029ce5360cf8966dca8278b.jpg)](https://forum.butian.net/people/13618)

[阿斯特](https://forum.butian.net/people/13618)

公众号：重生之成为赛博女保安

11 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![阿斯特](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b99df3b5f15d200a029ce5360cf8966dca8278b.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---