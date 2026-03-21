---
title: 记一次“有手就行”的从SQL注入到文件上传getshell的简单过程
url: https://mp.weixin.qq.com/s/eYFgpap5AKcGZtfXx3-e7Q
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:04:13.689348
---

# 记一次“有手就行”的从SQL注入到文件上传getshell的简单过程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvF8kpibJj2SO7ujw1q5XaV9DDmVjJv3sGaUx8wbcH3yHnbPuPKuwoxnQ/0?wx_fmt=jpeg)

# 记一次“有手就行”的从SQL注入到文件上传getshell的简单过程

hqymaster
hqymaster

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/TL4Y9UAcgruibhUn2nvLrs9mLNiaB1EywEk5fekyWAgJHrFof41PrHYJk9f0jbpDxWZHe4bl66MTEcIkd6nIxvZA/640?wx_fmt=gif&from=appmsg)

**漏洞原理**

SQL 注入漏洞的原理是应用程序没有对用户输入进行充分的验证和过滤，导致攻击者可以在输入框中插入恶意的 SQL 代码。当应用程序将用户输入的数据拼接到 SQL 查询语句中时，攻击者插入的恶意代码也会被执行，从而绕过身份验证和访问控制，直接访问或修改数据库中的数据。

**查找注入点**

如果要对一个网站进行SQL注入攻击，首先就需要找到存在SQL注入漏洞的地方，也就是寻找所谓的注入点。可能的SQL注入点一般存在于登录页面、查找页面或添加页面等用户可以查找或修改数据的地方。

**交互点**一般是搜索栏、留言版、登入/注册页面、以及最利于观察的搜索栏的地址如果类似于http//xxxxxx/index.phpid=1这种很大程度存在注入当然有些注入点不会这么一眼看出会有些比较复杂例如http://xxxxxx/index.phpx=home&c=View&a=index&aid=9 这样的地址其实也可能存在注入。

如果应用程序未对用户输入进行充分的验证和过滤，就容易受到 SQL [注入攻击]

**根据如上所述**先去查看和数据库有交互点的地方，一般先去找搜索框，特别是这种可以查询年份和编号的地方，和用户数据交互的可能性最大。

使用Wappalyzer简单看一下网站的框架和使用的语言

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icv1Y8uDaKMeNkuFGoDsicMRibqAyaoMOsviaUvTSLR91IbHwjStnEibvFkBg/640?wx_fmt=other&from=appmsg "null")

经过查看找到一处与数据库有数据交互的搜索编号的搜索框

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icv2Xc5uib7Wc0abwb27ZPYS0BESwY2lgY54OfaxKiaSNV63Y0D91f8icu2A/640?wx_fmt=other&from=appmsg "null")

可以直接输入一个单引号看看有没有报错，sql注入加单引号的原因是为了让sql语句发生错误，从而得知其有没有过滤措施

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icveVfN12gR5f1l4DTicR6SjBHfaIhACMn3zx4MHNwHFX3PryCPiaxsSgMg/640?wx_fmt=other&from=appmsg "null")

芜湖，直接爆SQL语句错误。。。返回前面的搜索框输入`' and sleep(10)#`

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icv8kRmQCyRV1ibowSon3BDeOKPj2h7ibOGhRwh0YbP9TserDiaWnLF9Y49g/640?wx_fmt=other&from=appmsg "null")

还是直接报错，没什么waf防护拦截。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvM6qlEmvJchveHicjOrYTJ9lEicj0xJzJxVeKIibkoSia2edVr21IfNovlw/640?wx_fmt=other&from=appmsg "null")

既然你这么脆弱，我就不客气了，直接丢sqlmap一把梭。。。。。

**测试**

在搜索框随便输入一个简单的数据，使用yakit工具拦截等一下点击搜索发送的数据包。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvZiaHmEVAeEnPP8cicuJbffuPOBOCIT6zgb3BiccxtfQJ34GqLuMCAdNhg/640?wx_fmt=other&from=appmsg "null")

拦截的数据包：

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvicMMRxOa6uGmrfmHIfo1X76r8S5GxmmnaZeCeLMSVUmBfw8Kw7qAxeA/640?wx_fmt=other&from=appmsg "null")

注入点在`mz17Condition.searchCaseId=`这个参数，在这个参数后面加上\*号，让等一下使用sqlmap工具测试的时候直接测试这个测试，要不然会从头开始每一个参数都会测试，浪费时间，把数据包复制到txt文件里面。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvW3hfWvMlVq1BiaDYyc5fZk5JHc6Ur7PYx0iap6vu37SOFaiaQfg5TEnVA/640?wx_fmt=other&from=appmsg "null")

使用sqlmap工具测试txt文件里面的数据 **sqlmap命令：**

```
--random-agent 随机使用HTTP用户代理头。
--level 分为1-5，默认为1，检查cookie至少为2，检查User-Agent等级至少为3，5级包含的payload最多，会自动破解出Cookie、XFF等头部注入，对应的速度也会比较慢。
--risk 等级为0-3，默认为1，会检测大部分的测试语句，等级为2时会增加基于事件的测试语句，等级为3会增加or语句的SQL注入测试
```

`sqlmap.py -r .\9.txt --random-agent --level 5 --risk 3`

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvFLuiaWZ5ZZkKKPCNic0nEM3A2WtUkO3vmmlSBKcym1XhuYibFR6W8h3YA/640?wx_fmt=other&from=appmsg "null")

果然直接跑出来了，注入类型有布尔和报错，后端还是IBM DB2数据库，第一次遇见。。。。话不多说直接跑库，看看可以获取到后台的密码 `sqlmap.py -r .\9.txt --random-agent --level 5 --risk 3 --dbs`

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icveIoQU8QkpRBnicGHOpibuGDXU43bcziawzPITUYZknklKIb4XKmPYpJAg/640?wx_fmt=other&from=appmsg "null")

只跑出了一个库，看提示，感觉是当前注入的用户权限不够大 `sqlmap.py -r .\9.txt --random-agent --level 5 --risk 3 --is-dba`

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvGrQ8ThIbHeP1YZK7FPEQ6b9JyWjVxUXkjbsnWKzdst8mvC432IeVHQ/640?wx_fmt=other&from=appmsg "null")

后面跑了一下爆出来的数据库，里面没啥有用的信息。。。。拿不了shell继续测试别的地方

# 0x02 万能密码后台登录

前面的前台SQL注入没什么大用拿不了shell以后，继续测试别的漏洞，前台基本没什么东西，看向后台。

测试

使用dirsearch工具扫描网站目录，扫描出网站后台。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvGY6301ZEIYVVaKujeRoywQrUhKM6KQpnSWbyHZ7TlicvkZut97NMeEg/640?wx_fmt=other&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvdMFlpa7zNPpaZD7egj6KQ4sshkUZvHtr4e41oP7DNDtcL1MkKrOoHQ/640?wx_fmt=other&from=appmsg "null")

访问后台url

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvZ24rsniacz26eGyicd2ZLVYQk665e83YSSesjH9qTCic4ZuDqbcsibyTJw/640?wx_fmt=other&from=appmsg "null")

按照惯例后台登录必试弱口令`admin/123456、admin/12345、admin/admin、admin/admin888、system/123456`。。。。都试了一遍没成功，看见没验证码又不限制登录错误次数，直接去跑字典，结果。。。。没爆出来。。。。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvK1NJPv42M1h6qziaf0Ief3amj1R5Y0CCg18Xj6gw3fTnrHvKECCNUXA/640?wx_fmt=other&from=appmsg "null")

看向用户注册，鼓捣了一阵子发现根本就是摆设，填写信息点击注册没反应，抓包查看发现根本没有数据包发送出去，鸡肋。。。。

在一筹莫展的时候，突然想到前台有SQL注入漏洞，后台会不会也有呢。。。。

**原理**

**万能密码**利用的原理就是在后台登陆页面没有对用户输入的内容进行验证，此时程序所用用户输入的数据都合法的，所以这个时候无论是合法的管理员还是非法的入侵者所输入的数据都是被信任的，非法入侵者正是利用这一特点来进行非法登录的。

当我们在这些语句中添加一些参数时，就可以去数据库中查询账号和密码。

添加参数后，语句差不多是这样：

**select** \* **from** user **where** username='a' **or** **true** #' and password='pass'

其中，#在SQL中是注释符，注释符后面的内容不起作用。

所以，实际上后台得到的有效代码是这样的：

**select** \* **from** user **where** username='a' **or** **true**

其中or true 会使SQL语句恒成立，从而查询出数据库中的所有账号和密码，从而使我们成功登录。

除了 # 以外， -- 也是SQL中的注释符，但SQL的语法格式规定--和后面的注释内容必须间隔一个空格。

所以拼接到语句中大概是这样的：

**select** \* **from** user **where** username='a' **or** **true** -- a' and password='pass'

也就是说：a' or true -- a经过SQL的转化后，结果等价于 a’ or true #。

SQL中规定，非布尔类型的数据参与比较运算时，会转化为布尔类型再参与运算。比如 or 1 或者 or 1=1 ，会转化为布尔类型的 true 再参与 or 的比较运算，也就是变成 or true ，同样能使条件恒成立，从而登录成功

简单来讲就是：a' or 1 # 或者 a' or 1=1 # 等价于 a' or true #。

当我们在登录界面输入 【万能密码】 比如 admin’ # 以后，后端会将我们输入的参数拼接到SQL中，大概是下面这样

**select** \* **from** user **where** username='admin' #' and password='pass'

由于 # 在SQL中是注释符，注释符后面的内容不起作用，所以真正执行的SQL大概是下面这样

**select** \* **from** user **where** username='admin'

SQL只会在数据库中查询用户名，而不是同时查询用户名和密码，这就意味着，只要用户名正确，就可以登录成功。

**继续测试**

使用万能密码继续测试 `admin' or 1=1--+`

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvAwcia5GeAhnBQYoiczWye78ZFQoet78pYGS71icpNWskHIjIyCgXnFptQ/640?wx_fmt=other&from=appmsg "null")

点击登录以后会跳转到这错误页面，好像有戏！

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvBgT8YNML9P4Q7zucH5qTj3uf8FrnlhS8bBuicdlPFHiarlwq9yOY4Mgw/640?wx_fmt=other&from=appmsg "null")

更换一个万能密码payload：`admin' or 1=1#`

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvA0nCwXIlutgI8QqHG7vCJ5o6A0M0Tgib4gK6VUhKzzztnmybI0McCBw/640?wx_fmt=other&from=appmsg "null")

芜湖报错！！！根据报错提示尝试闭合

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icviasBGGBW4ZZ9NygDjvFeUzxpHLUpC2Qw5NnacOk3EakYmqHVPnDEh3A/640?wx_fmt=other&from=appmsg "null")

image-20240414022818568

尝试万能密码闭合能不能直接进入后台，使用自己收藏的万能密码txt去Fuzz用户名

抓取输入登录框用户名的数据包

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvkIWYgvwetOZiagolQ8u0tJRnjibAnjMoynF8SVm9fLeg1YlzWXbvN9ibg/640?wx_fmt=other&from=appmsg "null")

这里使用burp suite工具继续爆破

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvGgUhsoFFGTl2spCHm69vN9RcMuS7gQKQGTe8oHr8iazYGey6cLEpIwQ/640?wx_fmt=other&from=appmsg "null")

加入自己收集的万能密码payload，进行测试

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvfYH8lYICovrRvSPjYlia7rCd6icvWyTV1IONIq21A83wHNtNjfvXA6xQ/640?wx_fmt=other&from=appmsg "null")

芜湖302跳转了应该是成功了使用payload测试看看

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvsDRFs4qUa4ia0YgAgib9sTFQKMxUxC2jxlUgQwhA2Ks5uwpSUiaRic8LCw/640?wx_fmt=other&from=appmsg "null")

最终构造万能密码payload：`admin' or '2'='2#`

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvwlRzNUvpSh02J4khH1dic1mL7y9KZqhY8iciaFr26R6JodxuhxUrnPOHw/640?wx_fmt=other&from=appmsg "null")

image-20240414030829604

进入后台！！！，登录的用户为管理员用户！！！

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icv44mBl1lh2cSoAJmTuLAXejx15RPAqgjdBfZ4WPHEEOg0GjSc3UbkqA/640?wx_fmt=other&from=appmsg "null")

# 0x03 后台getshell

**测试**

进了后台而且还是管理员的账号，就好办了，查找上传点，结果一番点点点、看看看，在网站信息维护找到上传点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgruJcMTvjWBc8lpuh6xWl8icvfaI6zrdjbbZKy7oWvz26aTibCi...