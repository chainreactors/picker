---
title: 应急响应-Linux日志分析技巧篇
url: https://mp.weixin.qq.com/s/WyqTdyCOPFFGQUPQ3Sp7KA
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:20:26.223555
---

# 应急响应-Linux日志分析技巧篇

# 应急响应-Linux日志分析技巧篇

FreeBuf\_518740
FreeBuf\_518740

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
原文作者:FreeBuf_518740原创链接:https://www.freebuf.com/articles/defense/483707.html
```

## 一、Linux历史命令日志分析

### 1.命令日志的存储位置

root用户的命令日志存放位置在/root/.bash\_history文件中，每个用户下面都有一个隐藏的.bash\_history文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRHUibwypxxgG4z5WoQWHxvjFhGMibLSMwYWEibic8hQ4xsP26AwLbibZZ7H3AcyFnkria0licDVczqFPRX7WZ40WLOdEoDrJELficl8Io/640?wx_fmt=png&from=appmsg)

查看这个文件可以观察到用户的一些操作行为，比如执行了什么命令，直接cat .bash\_history即可观察

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT4KDsvJgQYF3uC6rxAtYPNyxJAicVInicvZaB5a43QRxTu06P7qV1edeIicYMOJy1lpdkPy478OdkZSibrsHFk0HBWZWVST2Q7gZQ/640?wx_fmt=png&from=appmsg)

还有就是history -c这个命令是清空当前所有输入的命令但是不等于清空.bash\_history文件，下次登陆还是存在的，可以使用echo "111test111" >> /tmp/test.txt进行测试，之后使用history -c清空然后退出当前登陆状态,在查看.bash\_history文件即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRUJry6og2hmzLaDLtiambYlEqBv7GOLlib7BdeiaiaOHwfBHOicEZTVM0NnXU2KA441Fg2CSyEa0KXsmPhKiaROJt4aZDx3qicUTcicV4/640?wx_fmt=png&from=appmsg)

## 二、登陆信息日志分析

### 1.登陆认证日志分析

Linux存在很多的发行版本多个版本之间登陆认证的日志文件名会改变比如在centos中登陆认证的文件名是/var/log/secure，而在ubuntu或者debian系统中登陆认证日志的文件是/var/log/auth.log

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRBhFkdZzBmW47icxwCtjPnR4fSdWxzYU5xEcmQs2W1bepuJiasEKXMxxPgcDmuCAPtXBbMiamUktLZ4I4Vg1tkq6HfbXE2XXuRmA/640?wx_fmt=png&from=appmsg)

可以看到里面很多这些gz的文件比如auth.log.2.gz、auth.log.3.gz、auth.log.4.gz这些都是auth.log的日志只是随着时间的推移日志量大所以自动进行打包，可以直接解压去分析就行可以使用gunzip -d auth.log.\*全部解压下来，然后直接cat auth.log.\*查看所有的日志，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRZcBetuPooK8URmz4As559eObtaU32yJ60zdZ9UszicXV0MbT28rlkZEyV9sdsgO1YTVhxqNcgF8ic86C1mVygV0gXo31fz9Ufo/640?wx_fmt=png&from=appmsg)

拿到日志之后要知道怎么去进行分析，比如攻击者做了什么操作，比如很经典的ssh爆破如果说客户要你统计ssh爆破成功的次数和失败的次数，那要怎么进行操作这些日志呢就是看这个auth.log但是内容太多，哪我们这里就考到了这个命令的使用了就是这次要讲到的技巧，这里我们使用了cat auth.log\*那么可以继续拼接命令，比如cat auth.log\* | grep "Failed",如下：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSIFeIyFVzEhj9KDu8LdX1fAoSkPWfZ2TR8q7kT21TBRAt6TkIjFG6J57efxhUiaiavWCia8Jqzfy1gicvauLiaJhE5pD2H3GVHgggI/640?wx_fmt=png&from=appmsg)

像上面那种就不是被爆破的，因为被爆破的都是有时间的连续性的，比如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSpEYD1IOcRmB1ULdyK584R2FlEIyV5SByeD9ATlFn9qa9C9dQIR42r96SasibsqTpyicKMUliaoNvnibXzpJZ0DAkpV8lZwYG11Tc/640?wx_fmt=png&from=appmsg)

秒级之内进行多次的爆破行为和扫描器是一样的，在日常日志分析中日志量非常冲刷了很多此时要怎么做呢，这个时候就要将所有的登陆失败的IP统计出来，还是使用多种命令的查询，没错就是直接使用awk命令，比如awk -F去指定分隔符比如这里用空格当作分隔符，因为这里清楚了日志是列与列之间空格隔开的所以就以空格当作分隔符，然后使用固定的语法"{print $}"这里需要统计IP所以计算到IP的列数，我这里刚好是第9列所以是$9,统计次数要先统计IP因为是攻击IP进行爆破的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRicZU4SxB8Y1Gicfxokz2BGoEs9rO2QfJz7NsxkibM804icFvnzu8gHcs8IiaJsx57E1SESSRbiamCtr5Wdl3duMjuK7PT0SjK74B8M/640?wx_fmt=png&from=appmsg)

现在这里可以将命令组合起来cat auth.log\* | grep "Failed" | awk -F " " '{print $9}'

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ7XfajmLDj598m8U2aUahB5EEKW1rVeLev60svzsNyWQUZwXkvoWJnN08xEXPC3ocDSzp9eia9vTjVAfzYXhQ9SXcc6Adk5azk/640?wx_fmt=png&from=appmsg)

继续shying命令进行统计在Linux中统计数量的并且检查重复出现的行可以使用uniq命令去统计，cat auth.log\* | grep "Failed" | awk -F " " '{print $9}' | uniq -c

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSibzX5I1GYU8N0Hia07vBA3ZibF07jvuy29V9U7Yo3MsBkxqWQ7WXV6D0ickVCwfHb2bczyZofS8fGhzagLFB2rgrIEBYlzsKHzog/640?wx_fmt=png&from=appmsg)

但是这里很多一些杂乱的东西可以使用sort继续组合去过滤掉这些没用的东西

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQOwmaQpJDSDZYtHuupIibhJ47QnGwN9JF5icdfJyX7lJzKqpfcO3ZtzQia0owhhAKLoPsGank1mXeAftLqzaUj1KI49cyMasWicwI/640?wx_fmt=png&from=appmsg)

这里可以使用awk的表达式去做一些过滤把除了IP的其他内容都过滤掉，这个Failed是已知的命中字符，这个时候可以在awk上做表达式，比如先确定Failed在那个列的位置，我这里是第4列那就可以这样去写cat auth.log\* | grep "Failed" | awk -F " " '$4=="Failed"{print $9}' | uniq -c | sort

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSbrSfL39cCcdaXHNmj0ymY47x1FhOjPQBU7n4unvgsSP8OAKRZQicJFhpMQKf3nicgSeajNYSLiav3icE7NnLtj1OabDBw2ozyFNI/640?wx_fmt=png&from=appmsg)

这样就可以进行一些正常的排序，要多熟悉命令的使用多敲命令，那么现在我们在查看这个登陆成功的可以查看Accepted关键词，还是使用grep筛选cat auth.log\* | grep "Accepted"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSia6WJouRibwAtHxsJO3dJSJ6FLq7lbdiczzt6D67pO7w4FmficHCglFRs5ScBbDrbWrHJ0CQseDYE5Ojkibk3nibrlL7onFrCGicTeM/640?wx_fmt=png&from=appmsg)

然后我们就可以查看登陆成功的次数了cat auth.log\* | grep "Accepted" | awk -F " " '{print $9}' | uniq -c | sort

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRglCXg26nrgA0cSviaiaicvAMc5pYqGJQlC2POLb4EVvFljySQFk1eoKstqX5dRL3icwQgZgSw6SFZskUicUCtfPILXhBz1tp1Z0UY/640?wx_fmt=png&from=appmsg)

### 2.用户登陆日志分析

等苦日志可以直接使用lastlog命令去查看每个用户最后的登录信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSMTiaqmBTrfiaheR2vpMzfnYqpu45ia7HnpzGHbKDfMmfgRWLL56v5UohjybUsmgmUNicDyeOPbgFiaY5IKqfzFZwNT524Ibibo0jP4/640?wx_fmt=png&from=appmsg)

这个就是最后登陆的时间了Fri May 29 02:24:02 -0700 2026，这里继续查看每个用户登陆、注销、宕机、以及系统的启动可以使用last去查看/var/log/wtmp文件，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRbXARq4OfJgLFYNz2Q76ib4uHAHIWgGkzuX72tobH6ZKy7MSwOrZjFaRNGkK105JvYDcoiakicXJeSCaIJ9EtsB0o5ia97kOOE3P4/640?wx_fmt=png&from=appmsg)

使用lastlog -t 7命令查看7天内登录过的用户

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSUt06ItVK1l7ocic5vFqD094SVQ5AeibgzXJgYSHQsnRVgLpsVAfiaX6UulZ5JNCJPKicnDp0HLebhXgDA99jhIdRBW8HYfMEzianM/640?wx_fmt=png&from=appmsg)

查看某个用户的最近登陆使用lastlog -u root命令即可，utmp文件记录着当前登录的每个用户的信息，直接使用last -f /var/run/utmp命令查看即可

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT0MRHUmdg0X0hPy71fyoPrhn1N76IibI8B7RqicnfnwjeibK2lFhFUGCvGE5a4LXn8UWCxY4KKicyOQbrlYNaabh0QJH8zD16efk4/640?wx_fmt=png&from=appmsg)

同时btmp记录着登陆失败的信息这里直接筛选攻击IPlast -f /var/log/btmp | grep "10.211.55.4"

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRzMjqc7QZGS8GIWvrpl0wcU8AaxoGjXJSOKEHI6JSvykicPMptHdqMY80Ng2DlI1EsXwrtAT69wbZDLkrS8fRVOfIQY8HUqSBM/640?wx_fmt=png&from=appmsg)

## 三、中间件日志分析

### 1.tomcat中间件日志

分析tomcat的日志必须知道这个日志的存放位置，tomcat的日志都存放在它的安装目录下，那么问题来了怎么知道这个tomcat的日志存放位置呢，直接ps -ef | grep tomcat要记得启动tomcat不然找不到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRuXCYhj7OibovnwlHQzX6FcWxxYjRXmmDVAeUfzKcm5esib5Y42RcEy3zejWxVGXRnotBibVUnXiaPfAx7oZXRxZuEH1XfkmHD1LM/640?wx_fmt=png&from=appmsg)

目录就是在/var/lib/tomcat10/logs/目录下，直接查看localhost\_access\_log.2026-05-29.txt文件就是日志

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT8JbKbbhiboulUEsILWibw8ydH0HWKY2q1srZek19HQz4vgG9Sn3icxVyB0bPrv1F1QZN7v8dDm6Ku9pxoxLUoRelDXVLcWhicfec/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRaI891pXOmPQEbG96CwHztzGiaQibVqgOC1S997UDib9K9YjkhDIIVzP08MDr04UiaRSGQo9999N8ju62OO9tVQNFf3cFic0PdkgY4/640?wx_fmt=png&from=appmsg)

这里可以分为两种配置文件一种是站点配置文件另外一种是中间件配置文件，在/var/lib/tomcat10/conf/目录下可以看到server.xml文件这个就是一个中间件的配置文件，可以分析这个文件这个文件记录着日志的分析方式

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQWh6d49aNOSkFhwAwian10plcibtrSqlpdhd9dwE2e5qyiaznTQgmibib1iarpwterW6w0mNLnGnwj6sD7z80j1OAKsIBDnM8vGRa9o/640?wx_fmt=png&from=appmsg)

然后这个web.xml就是设置一些限制比如允许那些用户访问那些目录

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRSREg6w3KUjzuJXKYJDWyNIEIMHadQ5898eN7pncryibGiazOgEhIDmWjwaGl4Em6su4ddMdOPxb4onH74gwW0aRKCszdYtSV48/640?wx_fmt=png&from=appmsg)

这里还是和前面一样做一些筛选很简单只要灵活使用就行cat localhost\_access\_log.2026-05-29.txt | awk -F " " '{print $1}'直接输出

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBJZOANluBhO96g99ibHM55bsVnP3ZoBBGnkAYE1s9dtQ9N5yxokuZNBosqetic6UZicwFSkSJVWkDMXU26ZOK42BjD5HunH6F1U/640?wx_fmt=png&from=appmsg)

使用awk直接统计就行cat localhost\_access\_log.2026-05-29.txt | awk -F " " '{print $1}' | sort | uniq -c

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRVBV9bgsl72aL5LGspDktGml3ic2kVdPJephEYrfTNQ37iaibAEUaM13AiazIiaYjEDIibuAlrI7oKxtcCwO1etxTRekDylbXVNNLEs/640?wx_fmt=png&from=appmsg)

这里直接查看什么时候进行扫描的直接筛选就行使用grep "10.211.55.2" -Rn \*多个IP也是这样筛选

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTMgMkJufAe12k95iaeJebERcK5Kic7qXDpDIY5TxoICuuCqyK4w32z5ApgEaWzMyZjt3DQJyrT3SPV0jdB6u3URXEP8AicoicsQ3s/640?wx_fmt=png&from=appmsg)

现在有一个问题比如要知道这个扫描器是从什么时候开始扫描的那么应该怎么做呢，这里要讲到一个命令cut这个命令可以指定切割范围，现在IP出来了筛选一下最开始扫描的时间可以使用如下命令：
cat localhost\_access\_log.2026-05-29.txt | grep 10.211.55.2 | awk ...