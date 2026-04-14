---
title: 某次SQL注入绕WAF的经历
url: https://mp.weixin.qq.com/s/cMLYUGvnLJFHtagcyT2KOg
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:43:50.084052
---

# 某次SQL注入绕WAF的经历

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj55epr9XwClIu2ia9IelOsvXueoN5SLncDOls6leZoRz2eCnG2HCueXD0sjjIFg4a5fv6Ifty401icBm4f3EvNyW4VNBCO1IkyBTY/0?wx_fmt=jpeg)

# 某次SQL注入绕WAF的经历

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj54Cxc1qqWxICcv9ibpuMHgDibbSDtBGdnliaje38YicNKZBlfBEPsLSWyF3fttdAtqicp2TwQpaV0Q0vXG0aLXJnHIsVuYFuoiaVib2tM/640?wx_fmt=png&from=appmsg)

一次同时绕过代码层过滤和云WAF的SQL注入记录

## **0x01** **基友你好**

说来你说巧不巧，刚好干完客户的项目，就看到基友的消息。难道，这就是传说中的心有灵犀？

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNlqxYkMoicJQcYDqiaSoU7rB8hzrqicJmApHJv4qfsiavcgqZbV6QicdRERfF7zcYmemoAMxrcwOUGiaUFDmJFxr4ngFUiaXIWiaUOFAx8/640?wx_fmt=png&from=appmsg)

那么，我们得到了基础消息，有过滤和WAF：

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNlJaoZPQdib9IaicJAvphRRwp4ONPPEGVx7bKD33bnn0kZ7ibRTngqnjspLtf7d7l7EB0l1KS9cev491tMLgrT9tbeNn3GVvYylvQ/640?wx_fmt=png&from=appmsg)

既然是通用，虽然说这里失败了，但我们先用这个Payload打过去看看什么情况，不行再构造：

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNnicWsG9DqZKjSXmEANykMHmb6iaaGXcXJEVkrohSsEib2RXOXQWHP3aV3AsVG7zwCWKK1qiajl1cr9bBTVOFd6eEm4aIPgpGVngC0/640?wx_fmt=png&from=appmsg)

好的，响应中有回显报错信息，那么我们观察对比一下就会发现，关键词select、from、where均被过滤掉了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNmt2gdZPxDqotyPKAc9c6EbHgKyX8iaibB7NN8LRb8GCTsusRN6dzOvZVVicBQ4fE41Uwics1ibrzK8pib9o0uibPAos9GsvlJ3fYQrEo/640?wx_fmt=png&from=appmsg)

## **0x02** **注入探测**

先用我们的插件探一手，看什么情况，不行我们再深入构造一下子Payload进行测试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNnScZT9al2BhxulzydqmdLicUpXSRM1uZ7GvPkFysyuh3ho1n5emxyVfFCM0kC1mjqfxIwXUyovccjyicGgiavQCTDHEQKd49m0Vs/640?wx_fmt=png&from=appmsg)

我们可以看到在order by判断1和300的时候，响应是不同的，那么我们手动发包来看一下具体情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNkX58CYxmQWEgniblsMO1JcwJEV1zNrtghXByB18xoEIiaRAcnyhIzbdF7AHXzr8Akoc94DicLnN7hJsiczb9mreSo4Oglnae7Yic3k/640?wx_fmt=png&from=appmsg)

判断1列正常，超出列数就会报找不到：

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNmkSeoAjNpE6fL26lrviab1hHXVmodrx7a1hVQ157h8cQS2AGhPMZB5IAvy31Tyaic9ZXhTNibLd6Nib03zkGL2FnpOzcXvQxU14SE/640?wx_fmt=png&from=appmsg)

是的，就只有1列…而且model的值会拼接到默认表名前缀里作为最终表名：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj543ibhJtMxITX2W4mgXKdkC4RTUtLcoIRVp762xQEbJayDeuDh6fqDCbdaoR3zMxuX8ojytbyIhpnpgC0WdO2jwpOqpibEhicFsjE/640?wx_fmt=png&from=appmsg)

也就是说model如果乱赋值，在拼接后数据库里没有这个表名的话，会报错找不到表名，此时直接无缘注入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNmhMTejFhmG1lVKu2mfI6uK9Sx3AgooRLXW1vQR08mOj18GTmh1yDvmIr3QfM3w7b6VdniceDntN0cpU4iaria1E2icJicSLrFoBC5M/640?wx_fmt=png&from=appmsg)

所以在不知道其他表名的情况下，这个值只能是news，它必然存在！为什么？因为是加载功能时默认赋值的…

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNkUhOoHdz6QaFSfVy6h5R5Uhdt1MibLcpkSI6DIYNAtAC5CpM5ibfS3S8nva7VqiaRJgkt1IicwiaFuteebgF8G5gGh3ZaKbqxELGT0/640?wx_fmt=png&from=appmsg)

## **0x03** **开始注入**

通过前面的内容，我们得知系统在代码层有关键词过滤。这里的话，我想看下sleep函数是否可用：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57ehANLbZ67JKKceEibtyvVmIHZ4mzlRd4JQmdazRzrzpf6bObozoiblaOl6HEEElgnPYSmhnnH63GVvSoDIQTnTYX9nqvzkq0Us/640?wx_fmt=png&from=appmsg)

嗯，拉闸了。同时在此处省略大量测试步骤，很多函数都用不了，要么被代码层过滤，要么被WAF拦截：

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNkEmGhTa4Hib20ojwQz0E38jHMaRMzDfse9IWEkX0aXh1d1ibhicXlctL3U1Xq2nHn8MMRkXNbH7P8vicASeEVW5ibk1x0UVqW4ia5ia8/640?wx_fmt=png&from=appmsg)

甚至，内联注释直接拦掉：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj55icNfHsWmRNvnS7hLOWtqvOqzwZwcHS1riboGLHrSQyAp2ibjlJLfYFWK5reZXmz4bwpzibDyQNQe82C2NMqDhggoicymuQYYmyQ58/640?wx_fmt=png&from=appmsg)

## **0x04** **构造语句**

经过我的探测，case when是可以用的，此时我已经看到八成希望了，那我们如何进行构造呢？

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNmDsGmiat29IaXicDgUyxkToQvUEIibJPE2TcqpE3MrOXAUtQWYsuyalpDNibwicjwlalGoHlDibBgoMYJcuKs8eOVOn9KJ45icdQgzUE/640?wx_fmt=png&from=appmsg)

通过前面内容能看到，order by是可以用的，我们可以通过它来拼接case when构造Payload实现注入：

```
'+ORDER+BY+CASE+WHEN+(1=2)+THEN+exp(710)+ELSE+1+END--+
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNlZmicCfxYfIvfqy44XsiadLZOib2ichsfgEHoICdtIUG9RjWmrE5vDiaiaAxE23kEgRS6hOgHBJpdnS9172hoCbU35gVzkRXLrBnoK4/640?wx_fmt=png&from=appmsg)

但是不对劲，正常来说1=1和1=2返回应该是不一样的。但实际上…返回的结果一样，那完全不对啊：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNmSF9E6lrfYxpAky1q8byG7DygpFX1Xy8wEdanWbFibAiaibNib476icXZY8MsU0VHCeWmbCdia86EQTtmzaMnbuxoVaQEpVtnQAFleY/640?wx_fmt=png&from=appmsg)

没事，小问题。其实我们构造的语句，聪明的小伙伴已经看出来这很明显是排序注入Payload了：

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNmG8wahPiaWT1yJQ9KGic91iaibu3CSgHHiczgVmKicRicSFRX2WycWSQb2079WyqiawkvmIyg7IHa053StWlw2buYh59Uw9AQPCLaW1dA/640?wx_fmt=png&from=appmsg)

所以我们照着排序注入的手法来，把1随便先改成字符串内容，然后另外一个结果我们让他返回exp(710)，让他产生报错：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNmPicSxvG1anKjribQ8l991HH8EJiadMsmGcChVmHDeKIfQP37o65Ft8bH1sXBsbZLvWmB2CW0azkNehfOOTMXLamMe4CMz4oaR4A/640?wx_fmt=png&from=appmsg)

此时返回的内容就不一样了，现在报错的是没有找到a这个列名。想要实现注入，我们还需要找到一个存在的列名：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNkFVg3IfaBUicnmvRwXfgprqh6yWr43K2RaeDg8uBMXlWJ0aD6GWRiaeusPibBqH0NFuiclhOJ1Tsqqmr4mderXBUrXm6VllGSMdQE/640?wx_fmt=png&from=appmsg)

去哪找呢？FUZZ参数？大错特错，你睁眼看一下响应里面的报错，这不是列名是什么？

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNnYNhWGF8Ced21K9uu3UkAJgdmC7mv3jJoOq7d9t5Ofl1HZiapNxAGZvBOraYhR9JOs92VIZHIiaZmfbK1iaecMImmJ7LIMLl4lls/640?wx_fmt=png&from=appmsg)

所以，此时的Payload是：

```
'+ORDER+BY+CASE+WHEN+(1=2)+THEN+exp(710)+ELSE+hits+END--+
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNlWJhRILqX4UBFU5kkHynmx3O8XNYwhXibxicVPZj8LP4Deue3bRx6qmkW69DCzBS0sG5XRAnVdQWBjEm83iajCfoEpuLtTkL71EA/640?wx_fmt=png&from=appmsg)

没毛病，跟我的预期结果是一样的。此时我再把判断条件改成1=1，就应该返回exp函数的结果，也就是报错：

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNnBxou8Y93GeVDmCA154Bu9Lfsj8lW2D4btsttickXsBYUBcCxyE0pUwbYso66gNDqIRZjed5AjPtTBK6xXEiaxHxMsT6LwtHmBg/640?wx_fmt=png&from=appmsg)

没毛病啊，成功一半了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNkOftEzDlKEM2kDjv999ljLyzibdmtygAQY2dn0lN5uCO4NsguaSCbleeMdjibc8MGrFtr76t641TM3oFhs9sicQN0Ar5wopICYMw/640?wx_fmt=png&from=appmsg)

## **0x05** **最后冲刺**

接下来，先看length函数能不能用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNkw10bKTz5BZsiakoK4UH6yXg3xLTibFUFp4pQic2RiaIiaeC2Ftf5eTAszRkKhDrdFywCHNtvjEhgGAhVDibbiaibWhGm3YU7Flkiaud3c/640?wx_fmt=png&from=appmsg)

length能用不意外，database居然也没拦：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNkclcLBZNLwQicjCeygaRCEKDRCeSQfzyIe8wGBicw3613n70FQXFxwo1J3Kj6Uoib4wltwIQ6tylHKs7EPYEDB2icrgicK5GAIZzibw/640?wx_fmt=png&from=appmsg)

OK，跑一下具体库名长度：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNnrZuf2oGevuRVeOVlCSFI2TrTQC3lMk7EHCu1PfM5hJibqPkqSBUCYEdtPTg6eKibDllTT3iaiaBNV2ILRVs18icFo7Oh8XWD2TvDs/640?wx_fmt=png&from=appmsg)

这里还是可以得出来长度是8，但是为什么有302状态码的结果呢？

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNlbnGyjfv1uicuEvIeEsSVoEJF9jNZ8bNjMFHot6BBtGkXu8iaLK0EpG4HELHafVVgTwHrO62vEcoxddx7LawUZ0uN5lXickvqJ9E/640?wx_fmt=png&from=appmsg)

不知道是WAF还是代码层，反正访问速率过快就会触发302重定向。所以我们后续如果用BP跑的话，如果跑完发现结果不对劲，就需要调整一下爆破时的速率了：

![](https://mmbiz.qpic.cn/mmbiz_png/HcG7oBmFdNlLLMpPTGOsTPFib6uSOIicD8f4yeGboOfgQaMJfYQ0zs8Fiah10v4JBQIqZOfIYsqNWqLAd2wRL5qQHOfL7j6xpc5z3XrymxhAMo/640?wx_fmt=png&from=appmsg)

OK，直接拿下了就是说：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNkwZBRXafn3otLL3MtSELjWJGwjicE2L8mWSUB5Z6DicAZmpkntZgc6LSv2dwCyV4NEHmLa2ZpbIib3DrB0yuzxp69dQHBHrkLB4s/640?wx_fmt=png&from=appmsg)

没毛病帖子，下机了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HcG7oBmFdNkHlpiaHGRXR2EaSswSAmicX4w2YUxmGWEGw0wRSia64noSCHxU8JBH7RUQlEjcQw4TDgGhAbSB0h6UvreKmAr4r6UZjXwWQCqb3w/640?wx_fmt=png&from=appmsg)

文章内容转自奇安信攻防社区，原作者犀利猪安全，侵删

![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1)

**今日福利**

为了帮助大家早日习得网络安全核心知识，快速入行网络安全圈，给大家整理了一套***【2026最新网安资料】***网络安全工程师必备技能资料包（文末一键领取），内容有多详实丰富看下图！

Web安全👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFBODrmsTGnPTOibdIT9B5eFLTHVIgWzYafxGAesmYnfzrz52xwV3Bjhw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

渗透测试👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVKWl2cLRTq7x9haKJerUZNO0YMhiaO8ibN1jjV0qxNLEvRKMfR90eNjQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

安全面试题👇

![](https://mmbiz.qpi...