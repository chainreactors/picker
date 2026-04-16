---
title: 记某edusrc未授权泄露全站密码信息&amp;AI渗透实战测试
url: https://mp.weixin.qq.com/s/5TEykmmjqRckg8T5t6ggwg
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:48:42.704145
---

# 记某edusrc未授权泄露全站密码信息&amp;AI渗透实战测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboTR8bvGHoUtxRlHfibOjwhJGlibaKAOQfUPuEXVj1DFvXEiaVvtBxlM1prnicvJHKQqdOHwIicP6eVGNlnotkMI1rYLiaMBzWtiakdBV4/0?wx_fmt=jpeg)

# 记某edusrc未授权泄露全站密码信息&AI渗透实战测试

原创

陌笙
陌笙

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

信息收集

通过fofa信息收集登录系统，然后tscan批量探测存活截图，找到这个站点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQzc3fNDaW5VgX4YwOtvUpvmkUySZM4vQf7GF4b9VaOlwsibKUNPa8iaQ0QOFGwGjdFcTuFDfc7VzPR1okM3tQLwkRVezGMSvICE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTaUwFBQwI0iafez8vW7AF5JHD5GhkFr0nVq2JZ6zJiaicR1dSHZPZNTibNFBMm1uvTzLy1UILgibSw0mjnkOSVJDVsXoxzgWygLHdU/640?wx_fmt=png&from=appmsg)

漏洞挖掘

常见登录框测试方法打一打

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTh6HpW5ISGuZf4BiaGMV0XqYUB5uIiaJsgMR9oG8aYib0xjQC92374M48fMwOia5ybnT0S36Xb4k4iavkxRtUmIibCoT3V8f4dGcTzA/640?wx_fmt=png&from=appmsg)

虽然密码没加密

但是固定密码123456，爆破常见用户没爆破出来

固定test以及admin爆破常见密码也没结果，但是注意这个字段后面有用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRyh4qE6K1tBicC2BgNibERoK9A9ic3mRpBISXOVVLbNY8ladT2vvAfFZjXjKYhQ4M38peKpgwyqexRxibliawoTka4UDdrgQadedeI/640?wx_fmt=png&from=appmsg)

然后直接看接口，因为是vue直接看这个插件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRo12XwkLa5LpicexklIs1vicwsv89RlovrIp014vWfHQGQnvace6RMBGsq14OCfhXiaPMZtETYw2HnjGMpEcclCWf6suOibRKibUicw/640?wx_fmt=png&from=appmsg)

插件地址

```
https://github.com/Ad1euDa1e/VueCrack
```

看插件一共有这三个接口，但是点击之后不跳转，还会停留在这个页面

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT7QoXkGza81nyIUgKk4E3QUibCwdLibk4jgCBLnzkBfQAlE9SJ4wza6IzrYibFuE6WUUvicS01eArTBPfrdJTUeIZLZk6SEosZgeE/640?wx_fmt=png&from=appmsg)

这个时候我们直接使用这个插件AntiDebug Breaker

来到这里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRVOvRcjnsR3Iy2XT0CjTic1NicSlFDWnh4sWWb1IyKuz3yngKFicQ1ZmZuWHzicDJES6OVtpom00xFnfqJhRSmQeSUhIPSVTKR5KM/640?wx_fmt=png&from=appmsg)

把这三个打开然后刷新页面，可以看到这里会加载到那四个路径

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRThCZDFWjv7YLM6Swvcsj1jCvT18LpkW9AL8L5cU4ZGWVlIo15ZKbDmPKRcibasjl4QPslibHEuIBDZtds436HZhicfjicaV3R1oQ/640?wx_fmt=png&from=appmsg)

点击/user接口

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRCdaXb3kP7ib984vSB1eqyosIbrDQhZDDbF00k3PCVWFXFFuVXXicARbTVVXH6Gxnv28vb0Q6YQcVCzYgA2SCHq1NE7ibR1My6GY/640?wx_fmt=png&from=appmsg)

可以看到这个页面，没有数据，但是这个时候还不要跑路

点点功能点

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTaNHudfKTs5I9PauvJ2I7k6SMzxU6wrynre9aoGOzxD8qLP11FIYRj6LRMialSdJpFJDHhaItpsS8rVOjyu7SicLFz1kxibhHcp4/640?wx_fmt=png&from=appmsg)

批量导出的话他会导出这个用户列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRdmDjd7LZJe4iamAEx0Y7UC8VDbzrzCr6ELTYicib2ta4icGALsL1aRFIANic7YgiaQdUj8NxdMLJiaL4y9ShxCBKDAZ7XdCwxNyTTzA/640?wx_fmt=png&from=appmsg)

但是没有sfz

我们这里选择100条进行导出

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRjjoUXQ9ZeDuv6NchCjN505bNUx5BBBCQtT7919oLPPiby9uicPJzD93Hdn2dnqUWKEQezMEjx4X6Qyn3RmpGazeY3GE9biaJccg/640?wx_fmt=png&from=appmsg)

直接导出100条数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR74Uhq3LJ4TaY7RKVMV1dAlyGvsgHllwwhQR5icYl0amNeq338ejtvJEkS1z6kJgEQmnphnWEWqXEN2E5n4vnlK4GzZaNKM60k/640?wx_fmt=png&from=appmsg)

本来想跳到第二页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRVsvRv0uibAciaz86aDg8SfoZBUQTwyhExQUBTfZWDHCiahpD3QzsoJEYP3aHMnniceZicUQf232E678Zegs1dauOOicOsK0Ra1qU8Y/640?wx_fmt=png&from=appmsg)

多导出一点，结果导不出去

上面的也够用，固定常见密码进行爆破，依旧空军

访问另一个接口是批量导出成绩

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSSXibXyXlvA8QGWMqKO8OAKquSL02JdB30AkK7AwG2QxENib3dgRAqx7uOXJLkP5iaUzMiaVicZS3E3wbqBG4N8OwdWhDF3hj0eUGM/640?wx_fmt=png&from=appmsg)

里面也是只有学号但是学号是不收的

重新回到用户页面进行观察

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTiarfLHnhPPvkjO0GBQhulZPC7Uc8AROC5uw0dk1gJ6WSRHN62GUHlK7x0nz5mHKAwj1G8mmNeBYXJRluwRooVibQ1RKACDO1rc/640?wx_fmt=png&from=appmsg)

有一个查询功能有一个删除功能

点击删除功能进行抓包，放包，405方法不允许，这个时候其实可以构造，一下但是删除接口，不好构造，容易出事。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSPIiaUqEU3SvJicnKGkxA3LdCWslaV6Gfn4AhdK7FzeZ69OUHgozwD8keau1gO3rgjqoLpib2BIjzk0MVbQaKNLB99SHl0AVVQzM/640?wx_fmt=png&from=appmsg)

点击查询接口继续测试

直接输入内容，啥都输入不进去

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTxeMFhpO5F322qa9vdthr6WbSKTQSSN45DUfZVcY9JyThoYdonEsG21E4iaBu8E2CxoD0I8eT8sDxlH5b7UKhAGpkwPXB9yxRg/640?wx_fmt=png&from=appmsg)

问题不大，之际点击搜索，抓包看看效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBI79h38RqJ8zDoE7kLosmnTBR9EB5j0VXNKdn9DHQJU9wusfhptcO2sB1mW3iaUcSr4ZA2Qycwaxzpq7w477GesJVuswHQF60/640?wx_fmt=png&from=appmsg)

他自己给我们填充了name=1,userid=1,然后查出来了密码信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRXGZ4W31n7XkPJcOdc5ru1lMccMh07VJueTOREicniauWb6xNEJo7n2Zx1cQH21MUeS5tC9mVcpcibLJ7hAz4ibVibwyjib0JNNc9jo/640?wx_fmt=png&from=appmsg)

尝试使用密码进行登录，这里userid就是账号，通过前面爆破抓包就可以知道

但是登录失败（注意登录的时候要换个浏览器，因为这个浏览器我们开了，防止清除跳转，即使登录成功也不会跳转）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRe5HGeUZcAsPjiazyWBcbUnWhEiamrRuwz1JfvxqAOzkcH84VMvEv06AibvZMVUzwN8mRSAOO3OaCNQ2DM28Wkzaymr9vo7ZtyqE/640?wx_fmt=png&from=appmsg)

继续回到burp

从前面导出功能就能知道，系统绝对不只是，这几个用户

而且通过拿出我们是拿到学号的，直接拿来这里进行fuzz

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT6W3EwlsiadUkKNbgrwGuGTfRaK48xkKzypw7WGUIJgO4xlLEq4ibKIZXRXlGRNKdf8XpGy4Bc9VQgjEiaXrcZtJraCAuarscvyE/640?wx_fmt=png&from=appmsg)

通过测试，name和userid是and起来的，如果他们两个同时修改

就会返回200，但是没数据，如果让一个为空，fuzz，另一个，可以拿到我们之前100个用户的密码

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS1mLcSjWpXUUvMpmRWqeJz6OpJePO7qLicLQBhxjic9yjSu9Lj2sw8bSkABUMEAc9QWhkibZYAXITpq29N3bxsQNtW2oU4CzSAdQ/640?wx_fmt=png&from=appmsg)

但是可以看到密码是123456，这个我们之前是爆破过的，但是就是进不去

既然是查询接口我直接构造%可以查看到10条

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTb2EGKv91PJ4rUPkTIibOXUtd17C6mibV9sA6XfG9BO8YtGdL7JnSfORuQNpWTFGDmV4kIHJjibGbgl6PMGqI5RSR8ib0SQZoibqa0/640?wx_fmt=png&from=appmsg)

继续构造，直接给系统300多人的密码拿到了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQZqArLRtzz38ic2iaZfv06P22wiaVRwCoXIy6fpWS6RMkQkH1Bicafg1e8noaAWPxFfrX3O5Zb0udVM8kX3QzBWicH7fdlDPxpEQao/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSg8FZKUgUnA3qkt8owHicPYw5gP5WqLtpYfORTZK1ic4syl6iaBnic0sE4191NkL6PrkPwTh5GS0y27f5vrZVFPUz6GfFXN00F9vw/640?wx_fmt=png&from=appmsg)

写个脚本都提取出来，然后使用草叉模式进行爆破

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRqP4sM9YvhIsHFCmAxjR0P9mFCKicRJUcEBqY5oEqLuF5wx1fJ0FGdP4Gcb60wXAf9BvGVS2rnQZ4sRmXcCwY8c4ibVn2PjwZ5k/640?wx_fmt=png&from=appmsg)

终于给管理员爆破出来了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRZVeVhKMOTDibBUFiaKu1zVy6lIibtF8alXlz0hibibvzficySHtuZiacR0FdQX6uxKuhwDiaQJ12GvEUpIcfRarYTGhzZgIlaef5wuS4/640?wx_fmt=png&from=appmsg)

然后再次尝试登录，直接吃了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRmgCy3WdvmPHDickPPkOBgsCCxXAtUGEXVYjuo218vzV0asAgWPicWfBsoeMgUibHJ9cgWu3UicI56GBkdCtmic2Q8mMZia5PlqmpibQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTLtE77sAicxpdDZ2RFKKicY1Dm2kPsD5MM0zQWdyOibaMkG59BLjCppWm5Rw2GssGfC6FylDwssP3yPSzMDQbtLcniajxUZYWbdqg/640?wx_fmt=png&from=appmsg)

后续测测了查询接口的注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSGghG640ekVicXhZvscia27zZUm2sCq0zoM3qSxtZBdKo1QTMu5KHCntSdl3ZBZUBia2tkkNgVuVTuwicibOAaSWjPGOAad6ibSicG6E/640?wx_fmt=png&from=appmsg)

显然没有

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQiayBnYrnE6223ia95Qw7QbcpiaP1rC37KlQYBPicqnD7qnZexpons0rIIZWVCf5V17Osh8JR94QydIdPvFlicHVNrV9cxgIKZMcPM/640?wx_fmt=png&from=appmsg)

因为是未授权进来的

我们后续测试增加删除功能的时候看看是不是未授权

增加用户进行删除

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ1gMTgTSypMkZoxlpgnPeX8VLoewMWNpKAr7PUhKxYticmOIgwRhCICeia9PhYlDLyhYaxpQBbah1iaLUk7lg8yggxNU5asF4180/640?wx_fmt=png&from=appmsg)

发现确实是未授权而且如果我们刚开始构造也能构造的出来

后续增加查看都是未授权

这里有个bug,虽然vue基本没xss，但是还是测了一下，发现这里有这种符号<>的用户是删除不掉的，amazing

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRtFVhzeWcn2ryau3H3FaAAR7eyfGVicbppu1P8K1I7RY3Y9eZNqowfOvGM6ajN1TdgPqnAuUQCd9S5Zicb1zbMLEjzscHH457qA/640?wx_fmt=png&from=appmsg)

整理一下这个挖掘流程，登入后台也确定了，之前的账户确实是存在的，密码也是对的，为什么登录不成功，爆破不成功。

重新看登录包，发现了这个字段

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQib0y5Ab4xjORqJAQ2qwDJy9vfEKYEO9Sjeyq5YgwYMUC5J27PLW20NYQeba2LQGGdogb5x1ZJHcMFsT5YqMPQloLNtPDvlgF8/640?wx_fmt=png&from=appmsg)

应该是区别身份的，学生和教师不一样，修改为1，进行爆破.

![](https://mmbiz.qpic.cn/mmbiz_pn...