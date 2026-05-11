---
title: 黑客常说的SQL注入，原理到底是什么？一次讲透
url: https://mp.weixin.qq.com/s/MF4QoE42ppGo430dqe9qAA
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:53:38.902165
---

# 黑客常说的SQL注入，原理到底是什么？一次讲透

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZibgCvtpRibszRHzaN7CPQqQlUsOdrm6ByF2jQToCmvtRAuAgSyh5PhHdsdvEAwuKWWy4t2Ffo0L26JvmEpzMqNN2eohuicFHicXtM/0?wx_fmt=jpeg)

# 黑客常说的SQL注入，原理到底是什么？一次讲透

原创

hackerson
hackerson

黑客联盟l

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhqjlIpdACpYtdVvKD3OPyBmYA5brJN4sK34dYRQcSL3uKNsGNoib9fEN3CEGeChjIvOx8qClscs5w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

用心做分享，只为给您最好的学习教程

如果您觉得文章不错，欢迎持续学习

#

![https://images.openai.com/static-rsc-4/_kjDPi0AdZfeq4i20_LcP1oPRRGjnU48LEoK61tapVqRG2GfKz3vMHzXIxLosGhKJQUSDfghtYmStLAYFynDq7HeHzk_ct5nrq4J7JZTpW-Js1fgUnSR9D5yGORSQDjmxmDGpwFHic4ijv22T1KjkHiwYaedSdJIhV-oPCB4uVax_KWAi9Kszro8CocOjwT5?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZichpFLziaREaKTbS6GM4gAYQhpGODo6LYgOl8PhWuqQUgibQsHW5m2conUkt0NPZzc6ibWasCPrJBK09zgoIcrFsay1QYsia2OsJLk/640?wx_fmt=jpeg&from=appmsg)

很多刚接触网络安全的人，都会被“SQL注入”这个词吓到。

感觉它像一种特别高深、特别危险的黑客技术。

但实际上，SQL注入的底层原理，远没有你想象中复杂。

甚至可以说：

> 它本质上，就是“程序把用户输入的话，当成了数据库命令”。

听起来是不是一下就没那么玄学了？

![https://images.openai.com/static-rsc-4/I0aC9Bb1Rzci6vv8SebmFa5-46K9FxVPa6UCmqIE4JMtdn91gARKBzz78_ZL0SVWY77squOn64s6sQ3MazpeXuNf-7irCtbiTLn6gjZJDekAzmVrDVGhERkZN5HWFPnz1_BphJ75ATvKEbRn5LFTWfHkJF1CNnOQmKWj8et8DvvROgFAKLD4E9ybEfHMiJTA?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZicHMvbKjSMPDew90Un9rQHI078RMAlia0U70nQAdJnvumYUu2gibkHzwne6T5QgmCFCVZ5f87GGXknQIQKCNYkGSkKnOYLDnkv5E/640?wx_fmt=jpeg&from=appmsg)

今天这篇文章，我们不讲那些花里胡哨的 payload，也不讲复杂绕过。

只做一件事：

# 把 SQL 注入的底层逻辑，彻底讲明白。

看完之后，你会真正理解：

* SQL注入为什么会产生
* 黑客到底是怎么“钻进去”的
* 为什么很多网站到今天还会中招
* 开发为什么最怕“拼接SQL”

---

# 一、先搞懂：网站和数据库到底是怎么交流的？

![https://images.openai.com/static-rsc-4/FPARYxfdr4K5BFP1DZGp-V_EQWAIEp421QSbJjcWAmZ34s2a8AlhejUy_URC7fwBl-PHrTA-AeZnqZLL99vZwlukROinDLbu9yPjOTizLcpyWUNmyDQG_Dr4KG6WgHJY9xcDfRmNIjoEoEBSeeJ9RLn6fyVad2s7J4oZQ75roqwbLnI3p83aRwPyrqBjL8ez?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZ9GuYKmRIoibsY8GxJa8yFRdc6HwklOEBa1LGj86oOGxmISB53IEe1tebY1R2PvibvtDyY0DDibYe10PjnBrsfgWdyAYnic1aB2pr0/640?wx_fmt=jpeg&from=appmsg)

很多人学 SQL 注入，上来就背语句：

```
```
' or 1=1 --
```
```

结果背了半天，根本不知道为什么能成功。

因为你缺了最关键的一步：

> 理解网站和数据库是怎么通信的。

举个最简单的例子。

你登录一个网站：

* 输入账号
* 输入密码
* 点击登录

表面上你只是点了个按钮。

但实际上，后台正在偷偷执行 SQL 查询。

比如：

```
```
SELECT*FROM users
WHERE username='admin'
AND password='123456';
```
```

这句话的意思是：

> 去 users 表里找账号是 admin、密码是 123456 的用户。

如果找到了，就允许登录。

整个登录系统，本质就是数据库查询。

---

# 二、SQL注入真正的问题：程序“太相信用户”

![https://images.openai.com/static-rsc-4/1pXGucEOQsicQ4QyBoICRYyxDdrIsozkFjxV8brqWEI2ztK_jZOC8qBZnsy40s5RRiUG2ZXDs88po5pgpVtcNQK8-0k3OACuQEhfDhAvbFJN6_ptrnP1OvrHzff9CmLUT_k4iVyeHp9cmPzIM7CeCe3k3vMU84TqqHrfG869eu5yC44pMEw5Y-HFgZYuWRa8?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZ91yqEwkwxVDS55NCTu7cMp070LrEnUNJlWSGVbdh18NjpsZpsFnN6j4fhZrWEaKPiccUibzmEt8FffywF0TPM8Q2vozVDJibd11I/640?wx_fmt=jpeg&from=appmsg)

![https://images.openai.com/static-rsc-4/pIL8qUh456qrWWrCYWAH6jG3SeNSmjptA-m7Yh7GcO7xsBQc7wPAQIgL3iNxDGTT3kN_60B9cW8TGJvfDpLil03l_gBQJlgbDU5Fla5v_VvWz6A1zS4dej3fMictZAaa902N9zpkBvZU92I2uLRszptygRuXPd-LjIboG6HXCX0MYOrU52lI3pCaU7gKywP1?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZibicnFkUbRMaOzBAXGsPUwW6hKtLlAHP0Sq8hy5zmPpWWAg3DqSpz5zZzApe3iaKkzjcrHRlbH4tSTEGY1PFpx1gZtPhgAgDYHaM/640?wx_fmt=jpeg&from=appmsg)

问题来了。

如果程序员直接把用户输入，拼接进 SQL，会发生什么？

比如代码逻辑是这样的：

```
```
$sql = "SELECT * FROM users
WHERE username='$user'
AND password='$pass'";
```
```

注意看：

用户输入的内容，被直接塞进 SQL 里了。

这就意味着：

> 用户不仅能输入“数据”，甚至可能输入“SQL语句”。

这，就是 SQL 注入产生的根源。

---

# 三、为什么 `' or 1=1 --` 能绕过登录？

![https://images.openai.com/static-rsc-4/1pXGucEOQsicQ4QyBoICRYyxDdrIsozkFjxV8brqWEI2ztK_jZOC8qBZnsy40s5RRiUG2ZXDs88po5pgpVtcNQK8-0k3OACuQEhfDhAvbFJN6_ptrnP1OvrHzff9CmLUT_k4iVyeHp9cmPzIM7CeCe3k3vMU84TqqHrfG869eu5yC44pMEw5Y-HFgZYuWRa8?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ9jjzcMEziaHu5bqSymJibyIFibZG7AYs1qEH7FvMSr16fibKm0U7ZVEFYLIIEmFkp5P0OsnewdTQLXRvnawXpPuVoND3otvmVngrk/640?wx_fmt=jpeg&from=appmsg)

这可能是全网最经典的 SQL 注入语句：

```
```
' or 1=1 --
```
```

很多人背过，但没真正理解。

今天我们拆开来看。

假设后台原本 SQL 是：

```
```
SELECT*FROM users
WHERE username='admin'
AND password='123456';
```
```

现在黑客在密码框输入：

```
```
' or 1=1 --
```
```

SQL 会变成：

```
```
SELECT*FROM users
WHERE username='admin'
AND password=''
or1=1--';
```
```

重点来了：

## `1=1` 永远成立

而 `--` 在 SQL 里是注释符。

后面的内容会被忽略。

于是整句话就变成：

> 只要 1=1 成立，就返回数据。

而 1=1 永远为真。

所以：

数据库直接返回第一条用户数据。
登录绕过成功。

---

# 四、SQL注入的本质，其实只有一句话

![https://images.openai.com/static-rsc-4/_gtHBZ1opiKuxN3MXW9WRvZKAP47OQLiDUtNb0Vm9EYQvGaSp5q3giZXIAEE5nE6PWrwiwOllmPzfYks586iGAjStG1kk2zDIbAPPm--9FVrWbX0R2KDMH7JXqBtp9rhji-xTzDWWdFovJKRaXjAG99qGrC_iRofvHqsPYFOmoF9Wdy1R5aKWlBhxeQ5Ip5k?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZ9vovcP0d0ZicQ1gx5AeMQf7J1NsIbZazTOYpSt4u1TLUTCVoIanFib1cspybfye9ne9ofibcc98EiazNRm2DykibEiaDibnCz65Cy34s/640?wx_fmt=jpeg&from=appmsg)

很多人把 SQL 注入想得太复杂。

其实它的本质非常简单：

# 程序没分清：

## “用户输入的数据”

和

## “SQL命令本身”

于是：

用户原本只能输入“内容”，
最后却变成了在“控制数据库”。

这就像：

你原本只是允许别人写留言，
结果别人直接改了你的系统指令。

---

# 五、为什么 SQL注入曾经这么恐怖？

![https://images.openai.com/static-rsc-4/jF_aTMjBlWBZxgQ7cjKP7LKMwSo-BEdBj91MA81T9lhfULZSaxsRWNCV5jV4pFK3AmN5ePq0kwGuGnR5EJZCCfNkO0wUgLxZlhyeD7liExJSegssXZI7meeJvxMLIO6FwLwuQRBuGfTJRF0UczFzZqv8MdS5_hbNUFQXhj1sIzGikkIHcMtzRCiMZXC3Eea2?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZibS599ZiamPzVcE5Jjcib2r1nUAX7MtgnTKHaYzU7PyopN0KwYke1PjlAKObOUDSp9jBA326vojtjc75CPkyTrdMQnzyyFIzboII/640?wx_fmt=jpeg&from=appmsg)

早些年的互联网，很多网站开发都很粗糙。

大量代码都是：

```
```
$sql="SELECT * FROM news WHERE id=".$id;
```
```

直接拼接。

没有过滤。
没有参数化。
没有安全意识。

于是黑客可以：

* 读取数据库
* 获取用户信息
* 拿到管理员权限
* 拖库
* 甚至控制服务器

曾经很多大型数据泄露，源头就是 SQL 注入。

所以在安全圈里：

> SQL注入一直被称为“永不过时的漏洞”。

---

# 六、为什么现在还有网站会中招？

![https://images.openai.com/static-rsc-4/f1isZ8i20rtEMGOx2naT5wsZREtIaotkEtdTKQCshoMlg68V4NfDPvYkTZeiroBTRtxM01m7yW6wSkGasPr0-2YT4FoWnrR8a7QQTUmAhmtaNYqmSCWc1Ff74GGG34phLmvCw8-wkPZ_CdRK44txFKdVaiL2dxktaaToywKcmEA0tfQpuuNFyxUWPKbqkhyw?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZ8eOIzmgfVibKaHRb2SiaPlI7tywdVUmydyH3y1V7CKb4H9aGQG0kUUIewM23ng7P0Jc2sIwSicfQfdxMicoUwgNCrx2OOyepQfSJ0/640?wx_fmt=jpeg&from=appmsg)

很多人会问：

现在都2026年了，怎么还有 SQL 注入？

原因很现实。

因为：

* 老系统没人维护
* 外包代码质量差
* 小公司安全意识薄弱
* 开发只关注“能跑”

尤其很多后台系统：

* ERP
* CMS
* OA
* 老旧PHP站

仍然大量存在拼接 SQL。

而漏洞，往往就藏在这些地方。

---

# 七、真正安全的做法：参数化查询

![https://images.openai.com/static-rsc-4/oUKQ7hJzT68u7Tw3q3hCbtwMtCl31PopWBufxha94WcBnT8r4YyTJH0Fg_nZkhVdOjt24UN5TlcR4OMPWFg-77XQzIfgYb_qs40gv045Q2JBh1l3oR7bK4Yco3kC--5qKC7U9h72Ls0alWVzUEE-1oFsBX4d021adKlZuH_GM2TGzeOvDfzmz8nk64LYgt_u?purpose=fullsize](https://mmbiz.qpic.cn/mmbiz_jpg/r3TOKXsosZ9Akhvfib8vnJdQQFYV01ATh1PxQIyxqHvYqYpwuwibFIctGJA2YOGfLYT40tuiblpKYMgNTsiar1IRFtAWntGSonIgFgL36tFPy2I/640?wx_fmt=jpeg&from=appmsg)

现在正规的开发方式，基本都会使用：

# 参数化查询（Prepared Statement）

它的核心思想是：

> SQL结构固定，用户输入只能当“数据”。

比如：

```
```
SELECT*FROM users
WHERE username=?
AND password=?;
```
```

数据库会提前编译 SQL。

无论用户输入什么，都无法改变 SQL 结构。

这才是真正解决 SQL 注入的方法。

---

# 八、很多人学SQL注入，最大的问题是什么？

![https://images.openai.com/static-rsc-4/76wTcSvwTl0mywtWuoKgsxX_w4Mx3Yf0eM9wRLXXbd32zLKstUNLPgJMaiayBd-c7CfUHlEjYD2IqwL0o1_t68A47quOr4eDuUURcJdgJRnEOwHBmcZyItJM9QPpEDzpk_LeCR-NMvIDOB_QXcRw_KZNDyiUfJyURFY95WU1HFTVDkZlfUZJrtKjruwKAS14?purpose=fullsize](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r3TOKXsosZibDKXp2bYbuNj93cxeyrsCO8ZhOqAwiciaCrMPSdYQgWPmLwBXUSqvJ1ib1v4MK3h0yVdKb60Lb4ABANv3pD4cuPiaiaSJicXUnpo3cY/640?wx_fmt=jpeg&from=appmsg)

很多新手一上来：

* 背 payload
* 背绕过
* 背工具

结果学了半天：

> 根本不知道为什么成功。

真正重要的，不是背语句。

而是理解：

* SQL 是怎么执行的
* 数据库如何解析语句
* 用户输入为什么会影响查询逻辑

当你真正理解底层后：

很多 payload，你甚至自己都能“推出来”。

---

# 九、学习SQL注入，正确路线是什么？

建议顺序：

### 第一阶段：学 SQL 基础

先学：

* SELECT
* WHERE
* UNION
* ORDER BY

否则根本看不懂注入逻辑。

---

### 第二阶段：理解数据库查询过程

重点理解：

* SQL怎么执行
* 数据如何返回
* 条件判断逻辑

---

### 第三阶段：搭建靶场练习

推荐：

DVWA
Hack The Box
TryHackMe

一定要在合法环境练习。

---

### 第四阶段：再去学工具

比如：

SQLMap

否则你会变成：

> 只会按按钮，不知道发生了什么。

---

#

# 十、最后告诫

很多人以为：

SQL 注入很高级。

其实真正高级的，从来不是 pa...