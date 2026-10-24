---
title: 26精武杯服务器
url: https://mp.weixin.qq.com/s/8BfUlNTRFnI0lrRwhesyPg
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:42:52.430088
---

# 26精武杯服务器

# 26精武杯服务器

原创

T1mM9
T1mM9

t1mM9的笔记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

第三部分：服务器取证

提示：分析办案人员提取的“服务器镜像.E01”回答下列问题：

## 4.59（填空题　1 分）分析服务器检材，该服务器的操作系统版本是什么？（答案格式：Centos 19.02.14 LTS）

在/etc/os-release或者/usr/lib/os-release中都可以找到

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8yibZveInGUjOoxQcJDAuTN4r6ziaMGpwIAJhna3Yxx5qBeQFU19cxCo0kTC1EXvffI604LQZg0JWINiaO0d4TL4Jtkicc2l4ReRIU/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8zia0cM69q47nuwHj2sfB5aIFaY8ibf6fpYZKsyCdHMzcF3kxFjW3TYia2rcRLeRCCG5tibjs8pSrQ39saP0XylYWMgjXRlh7fAo5Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8zQZM8Mdn9QzX047x5SiaVc8Xicc9VbF09aYNObddRBYLgiazOxKqODFxpNGQ4iaFQEW98HpEUUAcCouLWWNFQIxfzKsI1yE2UedRc/640?wx_fmt=png)

✏️ Note

uname -r查看的是内核

## 4.60（填空题　1 分）分析服务器检材，该服务器的根文件系统（/）的 UUID 是多少？（答案格式：以实际为准）

在/etc/fstab中查看，他是 Linux 的文件系统挂载配置文件，用于记录系统启动时应该挂载哪些磁盘分区、挂载到哪里，以及采用什么挂载参数。可以理解为当你启动linux的时候，linux调用工具访问这个文件来读取并处理这些挂载配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wvzXSSVuzIRiazDAfmhI6A28U1exB6XiaPicFdIjV5gR3U93yYjiaxjSY2NibKfazS9ibibmhnKKg44pYhhicIQrwUF5gCWMyrZulcqx0/640?wx_fmt=png)

在仿真取证中，可以先findmnt来查看挂载了什么，之后用blkid来查看磁盘的分区，文件系统，uuid等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8yEcGIfFV8xamspgdo9xkY6pmnXvmhK6UoNUy3nc7jnZ4tawMBRHUcbXIQVm3zIAUd0y6aSRWjQo2ZEhzicw6mkMFEXnRsWnOzg/640?wx_fmt=png)

## 4.61（填空题　1 分）分析服务器检材，该服务器部署的运维面板安全入口是什么？（答案格式：1abc23）

运维面板的安全入口通常指登录管理面板时，URL 中必须附加的一段特殊路径，也叫面板入口路径。

我们先找到用了哪个运维面板，运维面板运行的时候肯定会占用端口，先通过ps aux来查看进程信息和监听端口信息，再通过 grep来查找跟运维面板有关的关键词，通常关键词是xp（对应小皮面板），BT-panel（宝塔面板），panel（面板），webmin，1panel

这里查找发现了xp也就是小皮面板

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8yaH1XrMAlqDO5QUt1CSykpN4TYdyUP6RHibMZPRCoIdrEicSxWBaTEmS79Ylxe3243icEOI9StCHckOg8enD6OLlu3ZRFVeuILtM/640?wx_fmt=png)

也可以用sudo ss -lntp来查看tcp监听的端口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8xjx9JDqWBhopADwXuTQdfyyYvGMiarxByB2EQbP7YzE8rS3dnPTClWia05uSnrOD3xNzQeE5PicuFlpEeDalGOePKKOw77RaAnVM/640?wx_fmt=png)

确定是小皮面板之后，在cli中直接输入xp来启动小皮面板的命令行，再查看面板默认信息就能看到运维面板的安全入口了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8yXy1g4QHUvxxkfLictRJn3kxQM3INEpFqsKJQ6xqBA8HOsENdjepu44nMUtuRI0ltUVq8TzD84UI7iaWMib982oUxv8ydcNlHH8U/640?wx_fmt=png)

在静态取证中，找到了xp的系统数据库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wgPIYenE8rbdoV1XFd9UR7wq3e4XXZY2h3KfNhjCnLejVxhJDBJQIu7JN2OdkwCEO3w1B1Vdf0aVxFdGR5Ivzd8ibyZcbm7Hwc/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8xibAoeKUW7ib9mN8ecNBbF7icBN59n6RcHXicGyibyuBfpoJt6uj6bkibvPjPexCxPjFR5s0d5e6ElXNI0kyyiaHDsSR85lUVdhmZlJk/640?wx_fmt=png)

## 4.62（填空题　1 分）接上题，该面板管理员密码的哈希值（32位MD5）是多少？（答案格式：英文小写）

密码大概率要去数据库中找，但数据库在哪里呢，可以先修复面板的数据库，看哪些数据库被修复了就知道有哪些数据库了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8yFfEuXUicLKmGaKom4libAJd9ATG4pzyRvsfeGLphibfXPzWCP4RjjsqvdLJHnbYiaN8mOm76iaxBdBXlAdSbycJXghPeZpdgZE0H0/640?wx_fmt=png)

看了这几个数据库，感觉最可能在app.db中，在里面找到了users表，里面直接记录了password的哈希

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8xnQsr55ibGxXUiaT7mPHhp5FXSiaCRovlL0s8nx616gNOtXjnwAjSIIPZOI8KBggnFhIeaHmkD8pV8Ds2enyvkRniaJu6ofa5LDFE/640?wx_fmt=png)

## 4.63（填空题　1 分）分析服务器检材，该服务器部署的知识库监听端口是什么？（答案格式：8080）

知识库是什么呢？知识库相当于llm的本地的“小抄”。把知识库的文档等拆分成向量存储，当用户问问题的时候，提取问题中的向量和向量数据库中的向量做计算，回答的时候挑相似度最高的。这个不是训练集，因为这不会变成llm的知识，以后要是没有这些知识库，可能来llm还是回答不正确。

知道知识库是什么之后，我们要怎么找呢？知识库通常会用docker来部署，库先找一下docker-compose.yaml，这相当于告诉docker的配置文件。

sudo find / -type -f (-name 'docker-compose,yaml') 2>/dev/null

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8ye9nYHAcNmLXaxia3mCXQd73AP2Vic0agUHINJvCt3ibX3tRKGSoSMCuibRTAl3ibz0725xWHxUx8Abp5ICtcAJPnFvkiacOBtyicpxo/640?wx_fmt=png)

看到了这几个命中，但是还不确定是不是，于是我们到/opt中进一步查找。

/opt是存放什么的呢？opt是option的简称，存放应用的部署目录，所以很多第三方内容都会存放在这里。

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8zk8V8FictKA3NuGujRVS2OibQY4lJo3zt7J20nbNR6IcXpXAfhMoSEdU17RCOJibmvnUibLJbuicLuRUFWsHEX8sdnUZpjkEjPu03c/640?wx_fmt=png)

进入/opt中后，找到anythingllm，这是什么呢？

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8ynicwRegavrdqHmJ00Zzxhtic6lz9U2iaYlvfEliaCxes0dmwrzwR8uZZCbs2Zt58KoxkrqnBt6daPGUm0f5eydaqdXxnY7XRgiafE/640?wx_fmt=png)

这个应该就是我们要找的。发现底下有一个anything\_deploy的md文件，推断应该是存放跟这个知识库的部署相关的内容，查看一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wB7Fq0hIFxwJAicIicia6MpiaXdsd7iaQzlsKPCyP7OyiaBibIScyv1uHaKZiafvbkRLicCGicrmH931R9ErIkljy4Rkia7Na1YibOa7iaf5Bk/640?wx_fmt=png)

发现了默认端口。

## 4.64（填空题　1 分）接上题，该知识库的登录密码是什么？（答案格式：以实际为准，如 123Abc）

在上一道题目的md文件中，最后的注意事项里看到.env文件中有登录密钥，去找一下这个文件，直接找到答案

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8yDAswrmsBgDj8UWofvicRMXGicxRs8rrWic1dBV3dq6WaFibNHfXoKWQ5QkPDK1wz2TianwfxRHPsWiazdp4AXKhzAVjLNnr9C98iblM/640?wx_fmt=png)

## 4.65（填空题　1 分）接上题，部署的知识库向量数据库（LanceDB）中存储的向量数量是多少？（答案格式：123）

我们先找到向量数据库的位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8zicpZUrbXEscibhZIovbGJiaWfu81e7tatFV3J1I7bTr5HSxK5nKTkEHIgam9HqUKRtYEprNRXSSGujCy7w9dOaNAqnn0ASUHXhE/640?wx_fmt=png)

不难发现这个文件，把它导出，让ai写了一个数向量的python代码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8xYkq9JCNtaXqcOa87tHoM9Fkibb7rruKdPZyvSWKGbJvdhEzhfhrrOmsdxZegzj0SIswMgeg2Ev1bbk8uxvQoQGFNt6ECRBTJM/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8yHIpPoqFljQ4jKN3fgYwwKJC9I3TJF0XvnTfCDs3iafYFibJa6KI9MqeiceKyjXErAfWAxW3FNuMR15AfTSqDXuTYvU4jnPL86ibg/640?wx_fmt=png)

## 4.66（填空题　1 分）接上题，知识库中配置的智谱API Key是什么？（答案格式：以实际为准）

64题顺带把这题做了

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8wiaMOnBXiaiawkdksIErtytSHarApY7VftCWpS5qGqribI8cdvl0Qw3lphVib9FEpZJW395k60PoTibsmYG4LjFeeoClmJengGbjIibI/640?wx_fmt=png)

## 4.67（填空题　1 分）分析服务器检材，该服务器中存在一个LUKS 加密卷，解密密码是什么？（答案格式：tuojie@feiyingteam）

在做知识库的时候，打开仿真系统，访问这个知识库，发现历史记录中有“加密盘启动命令”这个session，不过打不开

所以推测加密卷的密码估计就藏在这个知识库中，于是在知识库中全局搜索一下

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8wPuczV6WhyibdBx1O2pvyPbWj7z27gJcpgTT3MqOufSxv2qM0VfteEggjbpbrJxkGcnqEMLZla4Z3ddLf2XRVPeeZt48s355G4/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8yTibruzaer2aX1QhdfAYKjvncbS7iaxUoricnXYQNa9Xq83xKWenItgDJQnShWXBgOfATTIEO7Dey61D2uPbicHbAFh7gicgJemmw8/640?wx_fmt=png)

‍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8xm3DU074NryTK2wP4SBWEoZquovicNAhMH3NAGEflvTrwoMdE6jOEnkN3iaCozqRW2ezRZtiaTvGKodNRqzBMNWE8Z19MjOibcUH8/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wNLDiaZayQh7MJSn0Q4qVsVevBmjkwI2Mlmdwl7EHkcRSUMwWpiaMLH6VvaP87PYExoEOwx8veFd4znPk9egTqtlcLBvIfwxASM/640?wx_fmt=png)

找到密码

## 4.68（填空题　1 分）分析服务器检材，服务器上部署的 dsh（DeepSeek Harness）版本号是多少？（答案格式：以实际为准，如1.0.0-1.2）

在opt中不难发现这个dsh的文件夹，其中有package.json文件，DSH 的 package.json 通常是一个 Node.js 项目的项目清单文件，用于记录项目的基本信息、依赖包、运行脚本等。

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8xJNXDpVDZqPJV6diaVs8licOk5TPnWELxtWynhP6KtsBoGx4vBXaE6ZGWqwHQCPbdbXNE0EKXYic7rplWAoicJR5z7tajcl4zMr2o/640?wx_fmt=png)

## 4.69（填空题　1 分）接上题，该dsh配置的 DeepSeek API Key是什么？（答案格式：以实际为准）

先找了一下settings，config等常见的配置文件，发现都没有，于是在dsh这个文件夹中全局搜索api key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8yB585g19BjQnrjPeBy8NW8J8JdUrJCiaJGu2KmMbCxKicZaO5JGYianlOpMtordgPicKyvZzlXuqSHDtK5hicrNuwHb7LQu3NBkxCs/640?wx_fmt=png)

## 4.70（填空题　1 分）接上题，DSH中用户安装的插件共有多少个？（答案格式：如 3）

在dsh文件夹底下啊，有一个插件目录

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8w3dncoGCUzYbSm7mibf6JW49ZB7a5U44DxJVLFyMcKeRxUib7r91ozHpNApc2hJmlrI8FprbN8BQkXhGazddmOoTTYpWHONibMqA/640?wx_fmt=png)

但是，这个很明显不是插件。

DSH 官方架构文档说明，Profile 会记录使用的 bundles、额外安装的插件以及用户自己的配置补丁。默认用户配置目录通常是 ~/.dsh。于是在profiles中找，发现了这个json文件，里面记录了插件。其中@deepseek-ai开头的是自带的，所以就5个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wsVgcLOYLPvdxv8AMOZ7ZZwZ4BdiacUy1Z3C9QNnB77oiaicQQdnH0jwCTbetCGmbXLQP2zXj8JfHykDB0tNgHicE5HZbTW7tibBEw/640?wx_fmt=png)

## 4.71（填空题　1 分）分析服务器检材，该服务器中部署了一个API中转站，该API中转站管理员账号Jelly的登录密码是什么？（答案格式：以实际为准）

前面找错的插件文件夹里就是这个api中转站的信息。同时在/opt底下，发下来一个文件夹教new-api，推测应该就是这个api中转站。

但是里面只有两个文件，应该是env，另一个是docker相关的配置文件，这很奇怪，这个中转站的数据去哪里了？

想到前面做了找luks加密盘的密码，想到内容可能在加密盘中，于是我们打开加密盘，定位到/new-api底下，一眼发现mm这个txt文件

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8xn2snImDd3xK3KL0tdQSS2U2Y8ibibxhGiavg8Goob7eoHtAmsCwAl6kxAeYWQ8eAHXcvNobiczyibMkw2IXufDN2k7Lf6ghrLQqXU/640?wx_fmt=png)

## 4.72（填空题　1 分）接上题，该中转站里启动的模型中哪个模型供应商下的模型最多？（答案格式：TuoJie）

看看能不能在仿真系统中仿真出这个中转站

sudo cryptsetup open /dev/...