---
title: 实战 ｜ 记一次曲折的钓鱼溯源反制
url: https://mp.weixin.qq.com/s/dC0Q3gIhiCIFsF2_WB1thA
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:45.100163
---

# 实战 ｜ 记一次曲折的钓鱼溯源反制

# 实战 ｜ 记一次曲折的钓鱼溯源反制

小艾
小艾

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
原文作者:小艾原文链接:https://forum.butian.net/index.php/share/1688
```

概述

从最开始的一个Web弱口令，到日穿钓鱼服务器，中间也是几经波折，最后还是幸不辱命。

# 0x00 前言

这天风和日丽，我正在摸鱼，忽然QQ群弹出一条消息，我打开一看，我感觉不简单。如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTv5Sfp2zsTIH5xuKetIy68ibRE7UicBG6ZkDPyrMVfzE16OnkAvGm7ibnwNT1Yj9CibiaJlBicLiauK7kv3vsD3HdX0vibKD24Zqktw90/640?wx_fmt=png&from=appmsg)

扫码后发现跳转到了QQ邮箱登陆界面，确定为钓鱼网站，看到其域名为

http://xxxxxxxxkak2.cn。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTIiatnM4ibdIHkOjqfZqGenUBuXZ9NSClJyn2vhibanheos2FKibjMLMKPb0YwBnebVmhOnfsq73sWb1OqLf8FGOMdOfCmiaiaC2xaQ/640?wx_fmt=png&from=appmsg)

这里随便输入，页面跳转到如下界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQFWMSNavcPQniaT1etgrkJk1tMs0ZQ8IL1PI0ft737jAteR7tJTNfyGaZSUNpiaicTceISWa7dVNFjWqOZHHCYW8NxU5EWQQicOibY/640?wx_fmt=png&from=appmsg)

好家伙，小伙子你挺会玩啊，收集完QQ邮箱账号密码，再来收集一波个人信息，做人不能太贪心啊。开始干活！

# 0x01 溯源钓鱼者

我们现在拿到了他的域名，现在收集一下域名的相关信息。使用站长工具，如下图。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSPwf8Gabww8VcSAn8eZgjDXyeIJDUqchZlRq5LazQD4kWQUia2Z5QAas1Piadmrq0yDljzXuyZOotS5psA3zWqmGdpicrdibH1ElE/640?wx_fmt=png&from=appmsg)

可以查到域名注册人的姓名和邮箱。邮箱显示不全，这里再通过微步来进行一下查询。如下图

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSEBZSoMpdCLGJ86mLON06RmcqiaJhCgZjWkC2icVhtgAI6tUq9zS96Mu74gytuoOCcSGFLZEIS46ZfS0MoyhnAmibiaomNBy7IKeA/640?wx_fmt=png&from=appmsg)

这里有两点可以关注一下，这里拿到了完整的邮箱和知道了这里是阿里云的。

进行一下邮箱反查，发现该邮箱下在五六月份注册多个域名，姓名都是刘聚达，大概率都是用来钓鱼的。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR0icMCFjaoIecNK4oELmiaOSYMjX0ibm15zvibibNuw5b5jHLGRL0NpwgJS299ZBbzRvA2mVwEpaJh7bxmbG89tppHPsheYNkU3X1c/640?wx_fmt=png&from=appmsg)

尝试添加QQ，发现查不到这个人，这就尴尬了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRSIrh3bGIapEmoLiaGwFic50cY8brOqo1gic7PItK7xlrS0pPK1s4fbqYEakXib121K3hblGzanNYsUVQ4moB3IicBocYGRFZOdTuI/640?wx_fmt=png&from=appmsg)

关于钓鱼者的信息收集就告一段落，接下来开始干它网站。

# 0x02 进攻钓鱼网站

之前我们拿到了域名，现在对网站进行渗透，那思路是什么呢？我们可以进行一下子域名、目录等扫描，如果没什么信息，那就开始对钓鱼网站本身看看有没有能利用的地方。

首先进行一下子域名扫描，没什么发现，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSx9TnfWLVDcvq8mLxjB6eWrXibakJaibHOjyKj5EAMYz42Azl2l3Y7fiaBmg9bA3LXFsW9Ry9Ty74NpkFDDsZQTGA0ex1Lv0zpsI/640?wx_fmt=png&from=appmsg)

然后开始对域名进行一下目录扫描，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQBdcFezaLVeLjoRZPaFdyUSuJvXNrS0notvLmHsGx2XnKp1J8hXEjs1rOQvtibBMQKXzeiaPHfReZibJVppCAFfx8uNywpbJcWIU/640?wx_fmt=png&from=appmsg)

扫出来的目录，基本没有权限，都是403。没什么利用的点。

现在看来只能对网站本身进行一下渗透了，看看有没有能够利用的。现在打开收集个人信息的表单，按F12看看有没有我们值得关注的，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTTBuiawrf5nmu3cdiaZP8hRMjUQ1q8QK5ibwGVGZTvVdiaeM5Klic0pYnsibngoFtlrnZ125AbkqqpnGW3fdolU4lnXmDo9QI616x3o/640?wx_fmt=png&from=appmsg)

之前目录扫描发现了uploads目录但是没有权限，这里找到了uploads/ads路径，尝试一下这里路径后端是否接收文件，构造上传数据包，发送数据，还是失败了。如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRCNZnH35KOgpjRXQyPthbLm0q6LzTKpT2jIibT3iawG70MzupeU3sR4Ipe5o3R2oX0LFSAn9Dd3PlVH9824dzvO3TmLVk6dczlQ/640?wx_fmt=png&from=appmsg)

不要灰心，接着搞，我们还发现这里使用了form表单提交数据，然后自定义了一个函数chk()，现在我们跟进这个函数去看一眼。如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTn4LB6XHyzbgXHsLmrGZzzjibaibZIoWm9dd79BO0caKj9mTcaEM4ibNpsJnRUpV9x6CxIEwsU0REOKm53yzhQuFdOL3R1yojDia4/640?wx_fmt=png&from=appmsg)

在这里我们能够了解到，网站使用了ajax来进行数据传输，将数据提交到了本站的wap目录，然后身份证号码进行了一下简单的正则判断，规定输入为数字且位数为18位。既然是将数据提交到本站了，那么如果钓鱼者再后端接收数据时直接将参数拼接到SQL语句中，那么就可能存在SQL注入。现在我们构造数据，提交数据，然后抓取数据包来进行测试，抓取的数据包如下：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSZ0xBpib9D8xuWk2LbMIGY806D0ynE9M3pAWpc8DuIKxXcgfWJHkyu2PGOzv9afribvC7VicFyAkw9cwSaRMYlyyNpDojRUKJ6r8/640?wx_fmt=png&from=appmsg)

接下来开始测试是否存在SQL注入，name参数后添加单引号，发送数据，发现报错，存在SQL注入！

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSOovBTZFicr9CCJYT21y4Euv5zuqp60EZS1O0U85Q8CMMe6AEF9RJMGpU5XfFoRVMhChO3OJmBgORLnyw6MEs591K3nL0aCMQE/640?wx_fmt=png&from=appmsg)

猜解一下数据库名，数据库版本，构造payload

```
' and updatexml(1,concat(0x7e,(select database()),0x7e),1)%23  and updatexml(1,concat(0x7e,(select @@version,0x7e),1)%23
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTlWFLzCfzSNKF8xDvibqdiadWqgrLL89vO52IS9M9d2YSzicyNB7ymrmUDypUH0ibZBjLzGox3JlCXBeIgZ8Z3xBURiahJVjCsUibib4/640?wx_fmt=png&from=appmsg)

数据库名是a7，猜解一下表名，构造payload如下

```
'and updatexml(1,concat(0x7e,(select table\_name from information\_schema.tables where table\_schema='a7')),0)%23
```

发现无法获取表名，我有一种不详的预感。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRdBnZQFlNeX3JquRdAkzsRRGF0LhEjHuGFT95Xiazhiawtd6FoO6FCzPBibZ8kzIbD9RxxFWbl7hfPuliaBibKIZu4wDge5fDpJaNI/640?wx_fmt=png&from=appmsg)

果然换用一些其他的函数，发现也是无法获取表名，可能是没有权限。真让人伤心，这个老六。

现在用sqlmap跑一下吧，结果如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSLjfj48SmqAco6rcyHTk9HCpdNDH8JGGq8b3c6NXJOl8OGJ1E3blGQXAJMlB0ticUWbe2eWQYNwdbGYlNS6jFWuPhh6jdd3vRc/640?wx_fmt=png&from=appmsg)

只能跑出来a7这个数据库，information\_schema这个库获取不到，怪不得手工注入也拿不到表名呢。唉，现在尝试一下os-shell吧，看看有没有运气。如下

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCN4BOv1iczs2225xicWfbcbLN8jY2v0tdxxRFq1bXUF3U8rnhlYo1d6bTibuPHtWa0NplELCFoRWzGvz7uVHYAcldarhjRq9UJM/640?wx_fmt=png&from=appmsg)

看来运气并不好，失败了。不过，虽然失败了，但是我们也知道了现在的服务器系统为Linux，并且有了路径，我们就把它当成绝对路径吧，死马当活马医，看看能不能写入文件，构造payload：

```
into outfile '\\www\\wwwroot\\p********7.********ka.cn\\config\\wap\\test.php' FIELDS TERMINATED BY '<?php phpinfo();?>'%23
```

结果如下，还是失败了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTibAelff47VJPjicuuYibxrXdjmaJgM5o1rr5aDnerFRvLciaDVd0BgJLKtOia1LAg6GDoIsbiafVKfkjekFfdf0fzE9aywJW5bIBaU/640?wx_fmt=png&from=appmsg)

又尝试了一些其他的方法，发现收获不大。

# 0x03 峰回路转

真的拿不下它服务器了吗？我不信，晚上的时候，事情迎来了转机，当时我正在划水，一条好友申请打破了平静，当我同意时，大哥人狠话不多，直接URL和账号密码发了过来，包括源码的压缩包也扫出来了。在这里给大师傅递根烟。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTL9mibpysTibEiafZVamsiaM3iblL1cVyYuHPAa5FhKClAns3uvoawRgQZBrWHobib9RD58nGmu8NLcJAQXXvaCoSur7xEuhXxaq1PA/640?wx_fmt=png&from=appmsg)

这里大师傅也给我宽展了思路，扫目录的时候多尝试几个工具，可能会有不一样的惊喜。访问url使用账号密码登陆，界面如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTg5GAibtjCQPYq5ic2SI0hWXsvBqLpArkWLM5hD1o7JqYxY3jicvURcFDBfnZgGedUZdoKicPuVjApSmHpU2ezobc5zjMOVRYnGeA/640?wx_fmt=png&from=appmsg)

登陆后，我们发现，这是一个帝国备份王的一个开源CMS。当我们知道是开源的时候，首先的思路是网上有没有一些公开的漏洞供我们使用。比如我们可以这样搜索 **EmpireBak v2010 后台 RCE**，结果如下

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSGEwbp6aYML3PsFuKfB7megsqDdnyD8BbujH0tI8vEDnoMHDqgwpTOfRdso8dfwLwxpdUVqbZc2W81DA2z9aqkibybqibH52mOw/640?wx_fmt=png&from=appmsg)

红箭头指的这篇文章就很合适，通过看文章，**我们也了解了getshell的思路，就是替换文件内容。具体流程就是我们可以先备份数据，然后点击管理备份目录，点击替换文件内容。**

思路是有了，但是现在还有问题，就是备份王链接不上mysql，导致备份功能无法使用，但是不着急，这里备份王提供了一个功能，就是参数设置。如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboROTvQ9UQ3E1rCAibFMYvjEF5JSF0efIK1svjjSLWfdx1uibibY9qibO9LEXMQlLAIAfmu8Yumia5Z2oBpC2D9vcZwvWt3e3Id4NkJY/640?wx_fmt=png&from=appmsg)

如果我们知道了数据库的账号密码和数据库名，是不是就可以尝试连接数据库了。所以现在重点是获取数据库账号密码。这如何获取呢？不要忘记了，之前我们拿到了钓鱼网站的源码压缩包，现在来解压来分析一下源码。找一找配置文件，可能有我们需要的信息。源码目录如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRxx0jiaoeqqx22eaDnIatJoNUmGL6bibUATe0DzicWRfLHyxpibtEVibaOyJNU8rxFibArY9xrBTl6ghufWkedogywncZBjMf7iceofs/640?wx_fmt=png&from=appmsg)

现在尝试找一下数据库的配置文件，如下，果然拿到的我们想要的信息

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQB43mInuiabxLsf6TibkD02aCbO9morfDaRIMbxoV8PhIibDyCI7MA1hRic7hnxwKqzr9ib4cicVAIx8KiaGFjRaRAuJD6ukxK3D02fE/640?wx_fmt=png&from=appmsg)

现在去网站尝试一下看看是否连接成功，果然不出所料，连接成功，如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSUClIs8bgUic5iaKP3W6MUZA5rcD7eOuN1te3lgTkqhicic6ric92JhJAMUsbibPaH04wxXS6iaEX3ygeUAJhwjE5Bk7SXulG0Zlawg4/640?wx_fmt=png&from=appmsg)

现在可以尝试拿shell了。喝口水压压惊，和大师傅同步一下信息，一个人孤军奋战，怎么能抵得上两个人一起日站的快乐呢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTrEccIgvV4WEvgp7OuudajQXuQiawMo9cDOSrnOliakE3ib7Pos1YZPMLiaWyTQocsGPaURj5JWGiaGibXs4oZeD9aXwNPQJETAUSbk/640?wx_fmt=png&from=appmsg)

# 0x04 进后台

之前咱们看源码，发现有一个a1文件夹，查看文件夹相关文件，知道这是后台的路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQKVrEzKsW5esNhqtnyB81iafhXkZcIl6Vk9faU5nC63CAStpx8lSn5zZAibxo53rRictHdSo5fKM1jZuHpvPyT1uTzlmvPom45gU/640?wx_fmt=png&from=appmsg)

我们访问一下，发现404

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTYUJVVaYnlz73CvL7VP8UC3nFMjM1MkYJVB5TznvaJSlCJXiapvYepNoO1qahzbuxYSaZjJXbBdY3oV6ALPbMBjbP...