---
title: 浅谈SQL注入手工测试思路
url: https://www.anquanke.com/post/id/313692
source: 安全客-有思想的安全新媒体
date: 2025-12-11
fetch_date: 2025-12-12T03:20:46.533732
---

# 浅谈SQL注入手工测试思路

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 浅谈SQL注入手工测试思路

阅读量**19156**

发布时间 : 2025-12-11 15:14:59

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

# 浅谈SQL注入手工测试思路

作者：The0dy[@360SRC](https://github.com/360SRC "@360SRC")

## 一、 前言

​ SQL 注入（SQL Injection）作为一种历史悠久却依然高发的漏洞，始终是 Web 应用面临的核心威胁之一。尽管现代 Web 开发框架已内置诸多安全防护机制，自动化扫描工具也能高效排查部分常见注入点，但复杂的业务逻辑、自定义的查询语句以及多样化的过滤规则，仍可能让自动化工具 “失察”。此时，手工测试凭借其灵活性、针对性强的优势，成为挖掘深层 SQL 注入漏洞、验证漏洞可利用性的关键手段。

## 二、 测试思路

​ 常规检测中，在参数中插入单引号、双引号或括号等特殊字符，若无任何变化 → 通常表明当前参数不存在SQL注入漏洞（输入被安全处理或无法触发异常）；出现异常报错（如数据库错误信息） → 可能存在未过滤的注入点，需进一步验证漏洞；返回拦截页面（如WAF提示） → 说明存在防御机制但可被绕过，需尝试特殊绕过手法（如注释符替换、编码变形等）。

### (一) 单引号闭合注入类

根据测试与分析报告，单引号闭合的 SQL 注入成为最常见且占比最高的注入类型，主要由以下两个核心原因驱动：

1. **数据库设计规范**：多数数据库系统（如 MySQL、PostgreSQL、SQL Server）默认将**单引号作为字符串常量的标准界定符**。例如，SQL 语句中字符串值必须被单引号包裹（如 `WHERE username='input'`），若输入未过滤的单引号，会破坏语句结构并可能引发注入漏洞。
2. **开发实践习惯**： 在 PHP、Python 等后端语言中，开发者常通过**字符串拼接**构造 SQL 查询（如 `"SELECT * FROM users WHERE name='" + user_input + "'"`）。若 `user_input` 含恶意单引号（如 `admin' OR 1=1--`），将闭合原语句并附加恶意代码，导致注入成功。

![image-20251208155139753]()

​ 例如以下单引号闭合注入案例：

​ 在接口的startTime和endTime参数中输入单引号存在报错。

![image-20251208155218144]()

​ 输入两个单引号，返回正常，这种情况存在sql注入概率就比较大了。

![image-20251208155246290]()

​ 通过嵌套子查询，like 等方式绕过限制，构造出payload：

![image-20251208155301261]()

​ 在 SQL 注入测试中，优先检测单引号闭合是提高效率的关键，但同时也需覆盖双引号、数字型、括号等其他闭合方式，确保测试的全面性。

### (二) order by 参数注入

​ 在 SQL 中，ORDER BY 后面跟着的用户输入参数无法直接通过预编译处理，导致直接拼接用户输入到 ORDER BY 子句，会引发严重的 SQL 注入风险。例如：

#### 1. 注入恶意排序逻辑

​ 用户输入：id; SELECT database()—

​ 拼接后的 SQL：SELECT \* FROM users ORDER BY id; SELECT database()—

#### 2. 注入子查询进行盲注

​ 用户输入：id DESC, (SELECT database())

​ 拼接后的 SQL：SELECT \* FROM users ORDER BY id DESC, (SELECT database())

​ 涉及 SQL 注入风险的排序参数（如 sort、orderby、orderid 等），可通过在参数值后追加 ,0 和 ,1 的方式测试响应差异，以初步判断是否存在 ORDER BY 注入漏洞。如下：

![image-20251208155609254]()

​ 例如，在orderType参数输入,0报错

![image-20251208155627402]()

​ 输入,1正常返回

![image-20251208155645834]()

​ 在mysql数据库中，当order by索引为0，不存在时就会报错，根据这个思路在相关功能处可进行尝试。由于 ORDER BY 子句无法预编译，常通过注入 CASE WHEN 表达式来实现 布尔盲注 或 结果控制。

![image-20251208155714415]()

## 三、 常用的函数

### (一) 注用户函数

​ 如user()、current\_user、system\_user()、session\_user()，有的数据库则为user。

### (二) 逻辑判断函数

​ 下面是最原始的函数用法，后续可以根据实际情况去改变返回的东西

```
 1、case when 1=1 then 1 else 2 end -->如果1=1则返回1,否则返回2。
```

​ 2、if(1=1,1,1) —>1=1返回1，否则返回2。

​ 3、IFNULL(1,500) —>前面不为null就返回1，为null返回500。

​ 4、NULLIF(5,10) —>如果相等返回为null，否则返回5。

​ 5、decode(1,1,1,2) —>orcale还可以使用decode函数，前面两个1相等则返回1，否则返回2。

​ 其他更多函数使用方法可以自己去看官方文档。

​ 例如NULLIF,当两个相等时返回false：

![image-20251208160327933]()

​ 不等时返回true

![image-20251208160339412]()

### (三) 截取函数

​ 存在length(user())，len(user)，substr(str,pos,len)，substring()，mid()，right(str,length)，ascii(str)，ord(str)，lpad(str1,len,str2)，rpad(str1,len,str2)，instr (root,r)，position(‘r’ in ‘root’)，ltrim()和rtrim()，insert(str,len,x,new)，strcmp (str1,str2)等。

​ 关于trim这个函数用的比较少，这里简单说下思路。

​ trim(leading ‘b’ from ‘abcd’)：移除abcd句首的b，但是abcd并不以b为句首开头，所以会返回abcd。

​ trim(leading ‘a’ from ‘abcd’) ：则会返回bcd。

​ 那我们的注入语句为：id=1’and trim(leading ‘b’ from user())=trim(leading ‘c’ from user()) or ‘a’=’b，因为user第一位不是b也不是c，所以返回的字符串是一样的，返回为true，假如第一位是b那他就会返回false了。

![image-20251208160802042]()

## 四、 总结

​ 现在的SQL注入是需要大量的探测和fuzz才会暴露出来。自动化工具虽能覆盖基础场景，但面对自定义过滤规则、业务逻辑耦合的复杂注入点，往往难以突破。手工测试需结合参数特性 —— 如时间型参数的盲注延时、排序参数的语法变形、字符串参数的编码绕过，通过多轮.payload 构造与结果比对，才能挖掘出深层漏洞。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**360安全应急响应中心**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313692](/post/id/313692)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [SQL注入](/tag/SQL%E6%B3%A8%E5%85%A5)
* [审计](/tag/%E5%AE%A1%E8%AE%A1)

**+1**0赞

收藏

![](https://p2.ssl.qhmsg.com/dm/200_200_100/t01b5d8fecc4d01072b.jpg)360安全应急响应中心

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhmsg.com/dm/200_200_100/t01b5d8fecc4d01072b.jpg)](/member.html?memberId=122586)

[360安全应急响应中心](/member.html?memberId=122586)

360安全应急响应中心（360 Security Response Center，简称360SRC）是360公司致力于保障产品及业务安全，促进白帽专家合作与交流的平台。诚邀白帽专家向我们反馈360产品安全漏洞、威胁情报，共筑数字安全基石，保障数亿用户业务和产品的安全。

* 文章
* **70**

* 粉丝
* **15**

### TA的文章

* ##### [VMP的手动分析和AI还原](/post/id/313690)

  2025-12-11 15:15:32
* ##### [浅谈SQL注入手工测试思路](/post/id/313692)

  2025-12-11 15:14:59
* ##### [360SRC年终冲榜丨敢AI，就请上场！](/post/id/313386)

  2025-11-26 12:32:59
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47
* ##### [诚邀莅临|三六零天御·亚马逊云科技安全合规沙龙](/post/id/308420)

  2025-06-13 14:18:45

### 相关文章

* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [Stealth Falcon 在复杂的网络间谍活动中利用新的零日漏洞 (CVE-2025-33053)](/post/id/308352)

  2025-06-11 16:12:52

### 热门推荐

文章目录

* [一、 前言](#h2-0)
* [二、 测试思路](#h2-1)
  + [(一) 单引号闭合注入类](#h3-2)
  + [(二) order by 参数注入](#h3-3)
* [三、 常用的函数](#h2-4)
  + [(一) 注用户函数](#h3-5)
  + [(二) 逻辑判断函数](#h3-6)
  + [(三) 截取函数](#h3-7)
* [四、 总结](#h2-8)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)