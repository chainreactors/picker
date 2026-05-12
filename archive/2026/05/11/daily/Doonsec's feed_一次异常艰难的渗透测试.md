---
title: 一次异常艰难的渗透测试
url: https://mp.weixin.qq.com/s/QZtJz3_AtLxdGgzB1iXaOQ
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:36:05.286243
---

# 一次异常艰难的渗透测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTlqj3oRDoM2aEej9e1VBfKMMOJcQNgqH0oKROJaFYIIZNibV4Ndqh3ibunYbdIOhYkL2rSuOaEDKtQ4qHSzY0RiaLItyxhssA580/0?wx_fmt=jpeg)

# 一次异常艰难的渗透测试

Arui
Arui

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:Arui原文链接:https://xz.aliyun.com/news/14677
```

## 0x01 暴力破解

朴实无华的弱口令，我都怀疑是不是交互式蜜罐。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ2u2rBJ4qvibBTycytgBdPwCz6OLiaO1pxBibUPeJWv8YJ3pA0uUnens6hACic77edGysjXyHpFicKjQ6eicuGA3acibEtHBDZEXKyC0/640?wx_fmt=png&from=appmsg)

## 0x02 文件上传

该系统所有文件上传功能均通过同一方式进行上传。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRHIdTV0ObCZvDCGORdPC9JccZrfMNeBJy8qKtHFzdwIHE5VvdQdWgIWmWOh0OEaAfQuVq5h5b9XpibhDVAlkfnPTicic3Lhpd1W8/640?wx_fmt=png&from=appmsg)

文件列表，可以看到文件上传后，从文件列表处能看到FileDir+FilePath为文件路径的存放路径，文件名为GUID去掉-号。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSY0czWyrCb6OrNW3JPibibat7pejwy4VibRicz8O2Ev3W0rtzK2liabvw9VrXTjzeNFE8JHWJ1xmdzZ8Uhic8qnhU3lgxkp4h9B8W3w/640?wx_fmt=png&from=appmsg)

而系统对文件的加载方式是通过FileGUID对文件进行加载，FileGUID不存在注入。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRTFEcSYeVzr116YNia1yBpaQ2rw4ibgypw0d4wGTFPDQ7MMv00zgC3KhBKDxwOuAiaOu54nKC0gJnHyKNMiatsOoTTKQ1RkExqTak/640?wx_fmt=png&from=appmsg)

## 0x03 SQL注入

通过对各个功能点进行测试，最终在投票功能的修改参与人功能中发现了注入功能点，得到用户表为t\_userinfo，而且看起来是可以执行多条语句的堆叠注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTjPRqboKI6ooaDNH7G27vrlh2dMTqhe8VDfwibyetsyic1HpibqEaiaxkjXh98hU61eEmLbYTE0yoaFzVVbMLyajeaBmTY7KkM2f0/640?wx_fmt=png&from=appmsg)

涉及到DELETE和INSERT还是放弃使用SQLMAP，打个报错注入，嗯...吞字符串，使用substr分割就行，但是太慢了，不是我的风格。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSdt3YOpL9G0rMW9VP0ljzVWavY6nYtRVQibqukdYM6Nj3fGGOEibbpDibUG92Hia3p10v4JXZtm2ZmkwnWK9iaW9Z5vHwjKGoT5ajk/640?wx_fmt=png&from=appmsg)

并且测试时发现在堆叠注入中可以把数据直接返回，开发怎么写的代码...

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRg50EUu7rc2DO5ygzxiaM9w5wUTFxyFae5l6jnsSvcDOshANC4U37xEDJYRxhia2y1JTQfhaC5O4CzRDNIALT2UDccMfRBFuIfo/640?wx_fmt=png&from=appmsg)

哟呵，还有waf，我前面这么敏感的操作你都不拦现在给我拦了？看起来应该不会太强大。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTqvPEFaZKkSVCcibePNBicQgIbEu4n9MQ4qWLApibUiaJXydhjPO2cgLEHl7WofDPKMk8vEtwBEbRSqlE0WRExa9aK6BKNZBvuBnM/640?wx_fmt=png&from=appmsg)

果不其然，最终加上左右括号就绕过了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSricTszPIX7wQUmcWBl0bQCTUvVcL8cMEHQZJWA3lmwOxF9OXxia2gDmABSpibOyL5VBqa3tBOVTJm0KXvxDSgtp1szUfOq1IoHg/640?wx_fmt=png&from=appmsg)

最终读取到管理员的账号密码，进入后台一顿测试，终于还是什么都没有发现，回过头来研究研究注入吧，mysql拿权限的方式不多，而且是普通用户权限。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRa8fibicZ1WLs36twIlqsOLkEojLgW5lqQkibgYI0fbJYkwad7vCryjcibSQaukbOiaJ0icGyNFgZhSb60TL5UqYr5iapXA6Xscia8vAo/640?wx_fmt=png&from=appmsg)

## 0x04 组合漏洞

难道就这样结束了吗，突然灵光一闪，堆叠是吧，前面的图片加载方式貌似就是通过FileGUID从数据库查询保存的路径来读取文件，那岂不是可以通过堆叠设置文件路径读取任意文件？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSbkqUahIpVXiaB0E88TxD2tjbdzdSy37dy63oYX61DwW4eNhKpQmecjKeXks3zLibeqh2xn3lpxPOW7UAribBDVL20ONAicVLlSzI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRgaEswibXxiaSVMMySdovo7kGzIJkL8TkaGicE3UufZ3Zzic6MnO44gUeZN7OKI1oPlLIDiaP98LNQ6pMPdrGp55LX3P4yNNQMAhRk/640?wx_fmt=png&from=appmsg)

那么下一个问题，web路径呢？有没可能目标中间件是Tomcat，~试试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSj7IusJVQqicHO8ic0owBTf8qDsd5mM9Xwm5ObrLSdejjicN0nJcvNBdBkHTmxic7hgvQYdtctCcJKXojNcvR0J0tQNU2XicHBFfeU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQWjV0H3JlylprkcCKWRvZX6WhPgBqRQpFxiaBlwNxWDiaOKABsyBAdX2cjfA7iaxtQMWKypwyzkT20vuGOMeWUeG5WnzCYpPBjxU/640?wx_fmt=png&from=appmsg)

只能说运气不错

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTbHc6Yd1snvIQibAChdWSTvxxTGV19gaCrZAwUK1RC9KcxCGiaDW4Uv3sQ9iaT8LIicb6TJOWfcUT3Z9cibkZ5Qre9U1hr744ibOgVM/640?wx_fmt=png&from=appmsg)

## 0x05 读取源码

读取web.xml，还发现了一个/admin/login.jsp，划重点后面会考，当时没有注意这个位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRzjkB182DSQic6vIaNwANsmj1pwS0LUiciacFmRUibwlYz4SpRbiaTvjKXnjE4p9NmgCEibhrUQnUFN4icGFUesnmZYLyWojmII30vYQ/640?wx_fmt=png&from=appmsg)

先读取源码如com.xxx.core.filter.SecurityFilter在tomcat的文件位置为/webapps/ROOT/WEB-INF/classes/com/xxx/core/filter/SecurityFilter.class，当然开发有可能把核心打包为jar文件放到/lib/目录，那就没办法读了，猜包名太难了。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSjGJwneEadNPUCB1iccwEmjHIibEoPz6sbfibT9ea4kT6JvmuuJYbQmYqAuqKdr33daORfBF274V3CVogjWTlAU9jBwHIuEU21kg/640?wx_fmt=png&from=appmsg)

MD，FileDir还有长度限制，但问题不大，因为还有读取文件的方式是FileDir+FilePath，超过长度的字符写在FilePath就行。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSYibNPtVMQDOV5sNa1A68lxOVtNoL3xHSgtuMP0YsNWI66rEYLUFdQToP0zkCX6icwxHHSqicyVD10tmNdVzmqy9OLRTpSTcUGGI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSNajdiblqiabj2uzYsrFCCO5l3HDrZ8QFpsmxbpEibQ6NseSN6THR91pRLF343ibvVVvRSf4EibjJkjwQaAdsl4qJtu8KcO0ia7Up1Q/640?wx_fmt=png&from=appmsg)

依照此方法+源码内部依赖的类，我获取了部分的源码，并在其中审计了一些漏洞，如认证权限绕过，注入点等。但是还是很可惜没有办法getshell，因为这个网站的开发非常神奇，后续会为大家介绍。

## 0x06 后台登录

有点烦，后续进行了：读取tomcat日志，log4j日志（不存在log4j漏洞），配置文件、猜测jar包名、备份文件（webapps/ROOT.压缩文件后缀、绝对路径tomcat.压缩文件后缀等）各种一顿操作，虽然没啥用，但也获取到了一部分的信息，这在后续给到了我很多帮助。

回到web.xml，访问了/admin/login.jsp，大概是这样（自己画的）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQFoHX6QbJIT2icrRtVKopicm2b52ibUfHd9C8cNBHGmoUwKqOCyj7VWnOvAazTt1SzFw8ibI0SAdBpJaYgpluenRkrZHmicOwq2UibI/640?wx_fmt=png&from=appmsg)

使用数据库之前读取的到前台管理用户账号密码发现登录不了，难道存在另一个表了？配置之前获取到的log4j的debug日志找到了执行的sql语句，尝试读了一下，发现居然读不到该表。

？？？惊呆了，不对，有一万分的不对，再详细的回想一下，我从数据库配置文件中读取到的明明是root用户，而注入执行的是普通用户。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS4oa6KLYO8I9nD4mpCr6zI3kGId5abnU7KzvlyibXxIysawIjRbQj3vd5JNiaKSxo0reut4u7Dzalr68VBUnhKufGnoiaKYVVXAo/640?wx_fmt=png&from=appmsg)

仔细的审计了一下获取到的部分源码，狗东西跟我玩这一套。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTHYxT0AcWPI1nmEOLW2IbnE8JKuDFDgkaWibsGCW1fKb7NEg7COa6Q8hG47Qmcb5HE1ibApbZD1B62dIzgaeJ90S0ibrPTic02Tg4/640?wx_fmt=png&from=appmsg)

网站的大概设计是：前台通过SourceCode和ROOT的数据库，获取数据库中的配置好的数据库配置信息，设置一个新的数据源，前台的数据都从这个数据源获得，所有导致注入点获取的是普通用户权限的配置源，而不是ROOT用户的。

不过他获取配置源的位置存在注入，也就是说我们依旧可以使用ROOT的通过注入执行语句，不过这次的是selectOne不是堆叠，问题不大，我主要是想获取它的后台密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRu74Zia2LxFCAqsZ3TNg5G1xEtZHpwJZQvVhsR0X3Y6dNfu2wdRf6OrXIcUh4ul9GInJfJgoqwiabXp0sia8lAX2IJ8f2V83IO2s/640?wx_fmt=png&from=appmsg)

## 0x07 jdbc反序列化

在后台中第一时间发现了数据源配置的功能点，和我之前猜想的一致，第一时间想到打jdbc反序列化，很可惜目标不出网。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR2kZbf0ejGYRY22bxM8tSn778g9ZY1rDa4zTYzJDRxiaqb5IsibzjyaRp7jdSrPZq0aG8Uc9EYM2Ch6k8AFhLa0a8VlHNHNzS5c/640?wx_fmt=png&from=appmsg)

## 0x08 RCE

后台功能点也不算多，能测的都测差不多了，不过有个位置是用来调试sql语句的位置，至于为什么有这个功能，因为他本身就是通过后台配置功能点，来实现对网站接口动态控制，我之前获取到的源码，基本上就是公共类的实现。

找了一会找到了一个ROOT权限执行的语句的功能点。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQwoT0dmXBRuZ7omvQaL7CTDpg9ZPiaPnhhU3pY9uRT9qoLhUlMb7ju9Eib12VkIlUTkSTe9AIGeRicLnpRpapeDIJC6148cGB35M/640?wx_fmt=png&from=appmsg)

查询secure\_file\_priv

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSiaLQNBT7oTIHwtlou1XDb1V1jSke7KVf6Z9Bj22adnYwDNvAEeicibmbmglLK4DvU34Knu7Q9XAZgNBwKVC3aMbA13sMtYEAAM8/640?wx_fmt=png&from=appmsg)

日志写入getshell

.......这开发脑子有坑，这SQL语句还用XML解析，服了不用想就知道是<>这两个符号导致的。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSHFcFAOFhfJ7VIr8ochfbkxRpmXkxQJ0IBT2icwibuL26c7PYVC2YWnCnzcYJKVlicicgUelAJe3A0W8FLTRQsbftuFicRpfdcpWak/640?wx_fmt=png&from=appmsg)

xml转换一下

```
< 转换为&lt;
```

```
> 转换为 &gt;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQibSHFns6VjIA43PgHAynudH618F3tLaFTibEJDr6qGtJqoasucic5mkbE4iaicg0yaib8WicmsDibmAFsv8zdEaIR2RphpfN6dc7haWI/640?wx_fmt=png&from=appmsg)

访问一下文件，打完收工。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQiaCQ40P7zgUN5iaicuMXvslvv3UnoVMkDVLfMfoCFicFm8hshYqBOZCRgWyicHyp30ZUGriaTptwadRGfDOrDBPlaCHZ9jSuLLAN4s/640?wx_fmt=png&from=appmsg)

## 0x09 总结

一次很有意思的渗透测试：

从暴力破解——》普通用户权限注入——》堆叠注入+文件下载的任意文件读取——》配置文件+源码审计——》ROOT权限SELECT注入——》读取后台账号密码——》jdbc反序列化不出网——》ROOT权限执行SQL语句功能——》日志文件写shell——》xml格式踩坑

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

...