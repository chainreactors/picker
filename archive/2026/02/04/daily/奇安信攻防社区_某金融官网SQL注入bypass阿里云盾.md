---
title: 某金融官网SQL注入bypass阿里云盾
url: https://forum.butian.net/share/4762
source: 奇安信攻防社区
date: 2026-02-04
fetch_date: 2026-02-05T04:07:23.684491
---

# 某金融官网SQL注入bypass阿里云盾

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 某金融官网SQL注入bypass阿里云盾

* [渗透测试](https://forum.butian.net/topic/47)

在某次对金融单位官网的渗透测试中发现存在SQL注入，存在阿里云waf，研究后成功手注绕过，并得到数据。

一、前言
====
在某次对金融单位官网的渗透测试(已授权)中，在一个查询处发现存在SQL注入，初步探测，发现存在阿里云waf，研究尝试后，成功手注绕过，并得到数据。 （这也是一个几个月前的案例了）
二、发现过程
======
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaT4B6s3YHOiaSQLS87AiciajcgyBJD8G9clgQibyGVZylISSWSvDlDqCh05g/640?wx\_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=0)
1个单引号报错，302跳转
2个单引号正常，200，有数据
3个单引号报错，302跳转
4个单引号正常，200，有数据
此时基本可以确定，此处存在sql注入漏洞，但是还无法判断是否能注入出数据。
进行简单的sql注入的payload尝试，发现被拦截：
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaTA0yVu9ianfU8eNQklDy6OsicibqMibg8v9WAS7psUFO8OtyCiaJTAMJNpsA/640?wx\_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=1)
三、闭合构造和数据库类型判断
==============
在发现sql注入后，首先需要的是尝试对该注入点进行闭合。
此处，通过使用链式比较的方法，成功闭合了该注入点，正常返回了数据。
```php
'=1='1    链式比较，闭合成功
```
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaTR68CzkGvEQCicyLPeeElRbbEWnaCJs5oTJ4ENsxmsaNibTu2e4ibpcAnQ/640?wx\_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=6)
返回了正常查询所显示的数据。
同时，我们也能确认，数据库的类型为Mysql。
为什么能做出这种判断？
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrxib26akqOCz3Mhz0oNHiaLmMaUTBoN9fN8q6k2L78f6QzshCxKVFiaHACCDXnOmmNf5yc2IjneicPCg/640?wx\_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=11)
因为在mysql，oracle，pgsql中，oracle和pgsql并不能够使用链式比较方法，只有mysql中允许使用。当oracle和pgsql中使用，就会产生报错。
> 关于Mysql的链式比较的详细内容，后续笔者会再出一篇文章来详细论述。
根据上面的闭合可知
```php
'=0='1
```
自然也能成功闭合，此处响应包则无数据返回。
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaTlQ7FEbgXWsibJ3DPCKT6VV4D0Tia3WEe1wKpXI8ibe9Vz5hS7lFaWk75w/640?wx\_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=12)
整理上述信息，我们可以知道的是：
- mysql的数据库
- 存在阿里云盾
- '=1\\='1 服务器会返回全部数据\\*
- '=0\\=‘1 服务器会无数据返回
```php
当两个等号之间的值为1时,就会返回正常查询的数据
```
两种不同的返回结果，成为了这次sql注入能拿到数据的钥匙。
窥其本质，0与1的差异就等效了布尔盲注。
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrZ24xaDzkZL3rmXwDcEibE3mI7MR0Qp9ia1bvqBlxFrg9PDVuMrBf0xtgicTDIupUicjEflnmnGjlxdg/640?wx\_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=17)
四、payload的简单介绍
==============
为什么上述所构造的payload可以闭合与查询？
这里就涉及到了MySQL的链式比较规则。
在Mysql的数值比较中，1会被视为TRUE，0则会被视为false，其余如：-5、88、2.1等不变。
- 若两个操作数都是字符串 则按照字符串进行比较。
- 若两个操作数都是整数 则按照整数进行比较。
- 若一个操作数为字符串，另一个操作数为数字，则MySQL可以自动将字符串转换为数字。
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrdgBtzXQ6tR8dt9EZA7rcvqsZGI8gQiawJjzqDuKRfKc22GUYklPAB0Ip19UeXrdib7zApJ4whSfdw/640?wx\_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=18)
当我们的输入拼接到sql语句当中的时候，就会开始运算，进行左结合运算
举个栗子：
```php
SELECT \* FROM users WHERE id=''=1='1'
```
假如id为10，则会变为
```php
id=''=1='1'
```
这里就说明了凡是id不等于0的，都不会被查询出来。
\\*在该官网的案例中，所呈现的效果则相反，具体还是要看后端的sql查询是怎么写的。
五、获得当前用户名的长度
============
- 我们的目标就是在两个等号之间插入sql语句，令它的值为0或者1。
先尝试判断数据库的长度，构造payload：
```php
'=10-(length(current\_user))='1
```
发现有返回数据，可以证明该数据库用户名长度为9位。因为此时中间值计算为1，满足前面的出数据条件。
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaTfMicfxMXzCaWbSe7VdwghZuiaZ1SjtMAqxgpibrCFZxXxNRL4KJTwTF7A/640?wx\_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=19)
——————————————————————————————
```php
'=11-(length(current\_user))='1
```
显示无数据，返回。因为中间的值并不为1，所以无数据。
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaTNcnFpibL6nEVzHm8ofAr2H60NLAQBNjV1eYcoPYGv0iaWSYsTDLkV69w/640?wx\_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=24)
六、获得完整的当前用户名
============
想要进一步获得完整的用户名，所需要的难度就大很多了，而此处，很幸运，利用冷门函数POSITION(substring IN string)成功注入出了数据。
```php
'=POSITION('x'+IN+current\_user)='1   payload
```
```php
函数介绍：
```
该函数会返回子字符串在主字符串中第一次出现的位置（从1开始计数）。如果子字符串不存在于主字符串中，则返回0。
例子：
```php
SELECT POSITION('a'IN'appale');
```
哪怕重复出现，也只会返回第一次出现的位置，这就给我们爆破遍历 user名提供了非常有利的条件。
初步思路：我们只需要通过这个函数，来爆破遍历所有的大小写英文字母加上特殊字符，来看在什么情况下，响应包会返回正常查询数据（即两个等号之间运算的结果为1），从而就能知道usr名的第一个字符是什么。
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaTFT7aGTyk1c7nA9ObNYZACVhXd0OQpicEWy6o17qT8PpU9T0sdqc0sHQ/640?wx\_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=31)
但此处又有个缺陷，这个函数的查询，并不会区分大小写，也就是哪怕匹配成功，也无法判断是大写的A还是小写的a。
于是我们又引入一个新的关键词，binary 该关键词的作用就是 严格强制区分大小写。
```php
'=POSITION(binary+'x'+IN+current\_user)='1
```
这个关键词的引入，令这个payload走向了完美。
此时我们通过遍历 \*\*‘x’\*\* 这个字符，即可确定user的第一位字符是e。
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaTgXkWHP9SyyVRy3uibjoW7yAa17IZtTaPNWrJJD83XJmwUw1ebGLibgJA/640?wx\_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=32)
当我们确定了第一位字符为“e”之后，就要准备第二个字符，修改payload
```php
'=position(BINARY+'eξAξ'+in+current\_user)='1
```
\*\*ξAξ 就是下一个需要爆破的字母，反复累积，就可以获得完整的\*\*current\\_user。这里就好比： 我们已经知道了e是第一个字母，然后我们再去尝试 ea，eb，ec.......当再次响应包返回正常数据的时候，就可以确认前两个字母一定是该爆破的结果。反复累加，类推。\\*\\*\\*\\*
最后也是成功爆破出了结果。
![图片](https://mmbiz.qpic.cn/sz\_mmbiz\_png/2S23hiaOglZrKvvibzicfgmIMe47dRPs2iaT7PQVG3CXqp0cIS2ubb7xy0I4jXibKeO2F93sHaC0iaRzbxVicyZxk8asw/640?wx\_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx\_lazy=1#imgIndex=33)

* 发表于 2026-02-04 10:00:02
* 阅读 ( 492 )
* 分类：[渗透测试](https://forum.butian.net/community/Pen_Testing)

4 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Yi1StaR](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/40760)

[Yi1StaR](https://forum.butian.net/people/40760)

1 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2026 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

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

#### ![Yi1StaR](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---