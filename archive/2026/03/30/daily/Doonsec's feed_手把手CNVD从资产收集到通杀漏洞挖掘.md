---
title: 手把手CNVD从资产收集到通杀漏洞挖掘
url: https://mp.weixin.qq.com/s/RVb-ai_ZrfWTyWdY6jjl0g
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:00.734268
---

# 手把手CNVD从资产收集到通杀漏洞挖掘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QWKuviak37V1a6JlB6CPx4LKjqLoF8sxlSwEsW0OedxS0OoBDibAg5xn333GOqaXGsJhiboXcy0PjaRDXDviaOMlrjMTnibFbicaeClY/0?wx_fmt=jpeg)

# 手把手CNVD从资产收集到通杀漏洞挖掘

原创

神农Sec
神农Sec

神农Sec

![]()

在小说阅读器中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

01

0x1 手把手CNVD从资产收集到通杀漏洞挖掘

## 0x1 前言

### 1、CNVD平台介绍

国家信息安全漏洞共享平台（China National Vulnerability Database，简称CNVD）是由国家计算机网络应急技术处理协调中心（中文简称国家互联网应急中心，英文简称CNCERT）联合国内重要信息系统单位、基础电信运营商、网络安全厂商、软件厂商和互联网企业建立的国家网络安全漏洞库。

CNVD官方网站：https://www.cnvd.org.cn/

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXXiaNItZMzxCQWe4a5eDFvoqmwyOFctS2ic0c6NVypicVz4csWk1ZjZKbmI2BH8aM9I0ceAk0iczFW5vO5pOEmVg03uQSZzVTKfDk/640?wx_fmt=png&from=appmsg)

img

### 2、CNVD证书发放规则

**归档漏洞的证书颁发条件为：**

**1、事件型**

事件型漏洞必须是三大运营商（移动、联通、电信）的中高危漏洞，或者党政机关、重要行业单位、科研院所、重要企事业单位（如：中央国有大型企业、部委直属事业单位等）的高危事件型漏洞才会颁发原创漏洞证书。

**2、通用型**

这里我们主要介绍通用型漏洞证书获取方式，通用型发证要求为中高危漏洞且漏洞评分不小于4.0（这里说白了就是低危不发证），通用型证书获取方式需要满足两个条件：

* 1）需要给出漏洞证明案例至少十起（例如：一个建站平台下的十个网站都存在SQL注入，你就需要提供这十个网站的URL，具体漏洞复现方式需要在你上传的doc文件中至少详细复现3~5个，剩下的只需要将URL附上即可）。
* 2）发现的漏洞相应的公司规模要以及注册资金要相应比较多，反之可能提交的漏洞会被打下来（CNVD要求公司的实缴资金必须不小于五千万）。

## 0x2 信息收集——github

### 简介

在漏洞挖掘的过程前期我们进行信息收集，`github和码云`搜索相关的信息，代码库，运气好的话可以在库中发现一些重要配置如数据库用户密码等。

这里先给师傅们分享一下**手工github搜索语法**:

```
in:name baidu              #标题搜索含有关键字baidu
in:descripton baidu         #仓库描述搜索含有关键字
in:readme baidu             #Readme文件搜素含有关键字
stars:>3000 baidu           #stars数量大于3000的搜索关键字
stars:1000..3000 baidu      #stars数量大于1000小于3000的搜索关键字
forks:>1000 baidu           #forks数量大于1000的搜索关键字
forks:1000..3000 baidu      #forks数量大于1000小于3000的搜索关键字
size:>=5000 baidu           #指定仓库大于5000k(5M)的搜索关键字
pushed:>2019-02-12 baidu    #发布时间大于2019-02-12的搜索关键字
created:>2019-02-12 baidu   #创建时间大于2019-02-12的搜索关键字
user:name                  #用户名搜素
license:apache-2.0 baidu    #明确仓库的 LICENSE 搜索关键字
language:java baidu         #在java语言的代码中搜索关键字
user:baidu in:name baidu     #组合搜索,用户名baidu的标题含有baidu的
等等..
```

然后再给师傅们分享下**github官方文档**： `GitHub检索文档`

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWVQNEE3HPAHzDhgGXRThSXI4cZXFvIeFtwZAjOLSkn0WFhPC9WsW1IjkEdFnWlyCUpUrUJTMX1nBM4xKj5lyqKQZYVUSaOnsE/640?wx_fmt=png&from=appmsg)

img

### 自动化工具——GitDorker

`GitDorker工具下载``GitDorker`是一款github自动信息收集工具，它利用 GitHub 搜索 API 和作者从各种来源编译的大量 GitHub dorks 列表，以提供给定搜索查询的 github 上存储的敏感信息的概述。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWCZHw3C2X624TyfcGnoNQgM49ibcAfS4Vic49TqfaCgCtms1TgfjWAticOIOjCyLbZdyBfybHQxVKgzkyIIKmG1FoPuw4HLtWgrg/640?wx_fmt=png&from=appmsg)

img

**挖掘泄漏方法:** 可以从域名开始找比如: `xxx.com` 我们就使用`github.com` 等平台等搜索语法对包含`xxx.com`进行搜索，再一一进行逐个排查或者直接使用上方等自动化工具，直接跑也可以。

**高危案例:**

某某某.com 存在敏感信息泄露，数据库用户名密码等泄露

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUlxhg7ia0btic496SiaxRDoCw6cDFpBvLCic0DliclBHLh21eW3dfNVP1icic5buH2zH76bdSYhhAytK0xuTKLKcL3UTbC3dXcFdpBRs/640?wx_fmt=png&from=appmsg)

img

通过查看库内文件找到了 数据库配置等信息

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUicV17dvLuxbu7gNYdXywYewjM8ibNMrQPLLicm5R9j50ib4icntKThOK4c2JaUz30pR7mNut9xOiaeX4VQ7mJgWXzWHeOvn2QCLoeg/640?wx_fmt=png&from=appmsg)

img

## 0x3 资产收集

首先这里我先确定这个公司的资产信息，可以使用网上一些免费的企业查询在线网站，比如爱企查、企查查、风鸟等在线免费的企业信息查询网站。

下面可以看到该公司的基本信息以及重要的注册资本资金，但是现在对于要拿漏洞证书的通用型漏洞来说，需要实缴资本大于5000万，下面这个公司就符合。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXXgxfGJfH1DibhUicxTABDlMP9moHj3vBBa2BibYorj5rA6oiabAorxym5cxnfsvYLyBzlQUWicSiab2D9TB33RXTyjp2icdDKh225JY/640?wx_fmt=png&from=appmsg)

img

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QU1SnJv2CE9hJcGwRrzNia2wQiaJiawHHd3IYnAHE3r6zJ2u91Xotrog7g7TU1qwjoL8McUCdfSfIYOCqIOtNBHO71HjyicHbq4Njw/640?wx_fmt=png&from=appmsg)

img

像这里面的系统都是可以进行测试的，一般都是可以利用空间搜素引擎进行检索，然后去挨个找漏洞，找到了就可以再去利用搜素引擎进行检索关键字进行模糊匹配，然后打个通杀漏洞，就可以拿到CNVD漏洞证书了。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUYS6LAfvJiaGHrKeEIXQr48oEBn9D7HJTuLr6MqzlF2UCEnTuwrY2ZSPciaMgGibvWzQXdEMyLnWBoZP4X74LKB9BZW5Rm2Ruazw/640?wx_fmt=png&from=appmsg)

img

### FOFA检索

下面就是利用FOFA进行检索目标网站了，这里利用空间引擎进行检索的时候，很容易打偏，因为资产网站很多，所以检索语法需要进行多测试，对关键字进行模糊匹配

下面直接检索**仓库管理系统**

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUzqqiayQYnqb9RJ8AgC3o1Lk5icWRfo2fgG7KYjSmqhYaMCnWWnLmOjicc54QEc4LN3b36p7KoNaWzZO5gC6u2JM2b1rv5S0hiae0/640?wx_fmt=png&from=appmsg)

img

这里需要主要的是这里FOFA还给我们整理了icon图标，可以找对应的icon，然后也是同一系统，然后也是可以打一个通杀的

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXRXDibupC62jZXzoAFGGhXnoMzjFKJyKZXnvh2xC3X0R4cz9iaiajy3LLBsKiaH0ZMYaDV1G9iaS3vfugF5J7KsUzyFcY4ujlHkUmQ/640?wx_fmt=png&from=appmsg)

img

也可以利用FOFA检索出来的系统名称进行一个漏洞测试，测试出来都是一个系统，也是很大概率会碰倒通杀漏洞的，提交CNVD也是可以拿到一个漏洞报送证书的

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QW3zjqMySwE2F531gzb9qfwCKmZLK1TT8wu2rSFJOYVlHfCZnbP9ASpAygjQJMQNiaXzDo591c5P7ofeAfv5iad9eFKAtmyTibWPc/640?wx_fmt=png&from=appmsg)

img

下面就检索有关**Vue**相关的icon网站

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVRzsk0XSQqegxlf5dE8DF8VJsFT1mVthKiaxRufx3DCGxNKJI91PjiaOoGbMd298kRefEshWxqLexqjfRLJpsmXU6gyLibpXamKY/640?wx_fmt=png&from=appmsg)

img

vue是一个用于创建用户界面的开源JavaScript框架，也是一个创建单页应用的Web应用框架。他的图标长这样，绿色的一个V，如果以后看到这样一个图标，这就是vue框架了：

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWQQ9yn5DLWx66MnS1sVbhIFPMYaWWhrrLdIvoHGoZ91amBlWbbbsTNzHtoavTbJBQZzYHVgBx0z7jfEFcMJVjLTo8C32byjrg/640?wx_fmt=png&from=appmsg)

img

## 0x4 漏洞猎杀

### 漏洞一：弱口令漏洞

这里随便点开一个网站，然后进行测试

这里可以看到里面有管理员登录，那么看到账号密码登录框以及管管理员登录，首先就要尝试下弱口令以及尝试下sql万能密码，看看能不能进去。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXicpj3oicDT91BfstduxjmeONyCKPl5ayAcjfRmkJO5yk1VJgmFwqoB4PSGEE8U4B4shaj63Liciawf1260FzfSO7ngR7YDNibRUtY/640?wx_fmt=png&from=appmsg)

img

这里我还是运气蛮好的，直接弱口令admin:admin就直接登录进去了

进去以后，那么就可以尝试在网站后台进行测试其他的漏洞了

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWtfCWb1zHXXxnCnRkClWfJkVzC223cPGWyVwmf1iauxia2IZiaV1Va3EAQ1MlmpoS2MwOlC8sKqV8EXiaboHUAibc4FYqJ7HXeibU2s/640?wx_fmt=png&from=appmsg)

img

### 漏洞二：垂直越权漏洞

然后师傅们可以退出登录后台页面，来到开始的登录页面

可以看到这里有管理员登录、学生登录以及还可以注册学生，那么我们这里是不是可以尝试打一个垂直越权呢？

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWlT1hTx5lYfAmq7d5e5sWuich37nE89N0ro2iajibpjEdPSJm6xy19OzXnP1Cn9FyvT3mUKLvck4KEeM553tFoNSdBxibN9jBmsHk/640?wx_fmt=png&from=appmsg)

img

接下来我们先注册一个学生用户，前面我们已经把这个网站的管理员账号密码给弄出来了

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVLg4EcHFnFM2ZbtB2T8jQ4IQozibkvT6IuYBLTQVH6iaiczeBPgVV4b9nXsicNZw5QPpeh9A40lgGBdYYbNTzJh3fp6QZf1AXHQ9k/640?wx_fmt=png&from=appmsg)

img

然后先拿学生账号去登录，再利用bp抓包，看看登录成功和登录失败的返回包的区别

可以看到下面是登录成功的数据包，记录下这个登录成功的返回包code为0，且有token值

```
{
"code":0,
"token":"1u40ivkgvpvtc1dd2l663zdu249e132z"
}
```

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXyXSEibcSKwwLQHnsOchCSwuuzRXBsmwia1w2VthXTCx0Esmer1nmEiaa7I68yjIKVKoLtysoPEtl4xnRF35wO2DVEy4djnrN4Rc/640?wx_fmt=png&from=appmsg)

img

然后下面再使用管理员的账号密码去登录，且是利用bp看他的登录失败的数据包

然后再使用bp的Comparer功能去对比两个数据包

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVefysDBibnqD9KpiaG4BgQtx8xwFicwmLhibBJBUWACVuK9fo0JzboGYyj0Njs3dWCbFFAYBQcoWfib6PO56Iy4niaKZpmISkHJLMao/640?wx_fmt=png&from=appmsg)

img

可以看到利用admin管理员登录失败的数据包如下，看到这个数据包，师傅们可以尝试改下msg，里面的内容改成succes，以及把code里面的内容改成0试试。

```
{
"msg":"账号或密码不正确",
"code":500
}
```

下面是学生用户登录成功和管理员登录失败的数据包对比如下：

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWLehN9VicmibhfFUCQmV9tliaRuSAUSSicWMNOrFbqOaa1xXWaDVJrVDbw3AfF9bic1ULsEjM2PcVpViaT269bPTV07mciaaIRibx7ibvc/640?wx_fmt=png&from=appmsg)

img

```
管理员数据包：POST /users/login?username=admin&password=12345 HTTP/1.1

普通学生用户数据包：POST /xuesheng/login?username=pass&password=123456 HTTP/1.1
```

直接先抓管理员登录失败的数据包，然后修改请求包

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVvyU7wvue1xcMNx3GAbexnVc6fADT47Xcw79Utz7VibXFaPRia2ZmBemA92xicfvfHb4AvXicGTibTxVmxpXnMuqibJsj5YJt2zticm4/640?wx_fmt=png&from=appmsg)

img

然后再使用学生用户登录成功的数据包，发送下数据包，更新...