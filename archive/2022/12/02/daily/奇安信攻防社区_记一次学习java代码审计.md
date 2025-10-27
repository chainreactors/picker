---
title: 记一次学习java代码审计
url: https://forum.butian.net/share/2034
source: 奇安信攻防社区
date: 2022-12-02
fetch_date: 2025-10-04T00:15:05.694025
---

# 记一次学习java代码审计

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 记一次学习java代码审计

* [渗透测试](https://forum.butian.net/topic/47)

近期学习的代码审计

\*\*前言\*\*
======
企业级进销存管理系统，采用SpringBoot+Shiro+MyBatis+EasyUI构建。
本次是复现以前的漏洞，以下复现都已经修复。
\*\*项目部署流程\*\*
==========
1、命令行进入Mysql后，创建数据库名为jxc，并切换使用该数据库。
2、将项目文件中的/sql/jxc.sql的数据导入到jxc数据库，注意导入路径中应使用正斜杠/。
3、使用IDEA打开本项目，等待Maven自动加载依赖项，如果时间较长需要自行配置Maven加速源。几个现象表明项目部署成功。pom.xml文件无报错，项目代码已编译为class，Run/Debug
Configurations...处显示可以运行。
4、修改src/main/resouces/application.properties 配置文件内容，具体如下图所示：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-6868ed8ab9436278449d4f9ace63f4a3518e5022.png)
5、点击启动Run/Debug Configurations...本项目。
6、项目访问地址如下：
后台地址：<http://127.0.0.1:8888/login.html>
admin/admin123
\*\*验证码绕过\*\*
=========
验证码重复利用，通过对登陆等核心代码进行审计；梳理登陆过程中的逻辑顺序；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-b9a1a24a758845ed882e6520154203348051b960.png)
在39行中对login拦截，并通过42行提交登陆参数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-d3eaf9aa692d0b0c5ccef5eb0169713b79a7cac7.png)
跟着42行login方法，打开login方法，在47及48行中只对验证码做了验证，验证后并未生成新的验证码；这就可以导致验证码进行无限次验证
47行将输入过来的验证码转为大写后和session中的验证做一次对比，48行如果if判断为否返回错误提示。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-d5c63aa652cddf3c5de7251ac8c0c8a06e3db0c0.png)
通过这块代码对比可以发现，验证码并未达到一次一码，只要输入一次正确验证码，可以进行无限次爆破。
因此基本可以判断登陆处存在账号密码爆破。
\*\*sql注入审计\*\*
===========
通过对框架的审计发现使用Mybatis框架；Mybatis框架对sql的处理：
${xx}是直接拼接
{xxx}预处理后拼接
===========
全局搜索${ 查看xml中是否有响应配置;并未发现xml中有相应配置
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-f5330385996d077e02ea5393d44e6bc5f8b1870c.png)
里面都是#{配置
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-f10c22fe1cabda9fa94d8ccf6beee415825e3a96.png)
\*\*这边进行多加分析\*\*
------------
Mybatis 框架
===========
MyBatis 是支持定制化 SQL、存储过程以及高级映射的优秀的持久层框架。
MyBatis 避免了几乎所有的 JDBC 代码和手工设置参数以及抽取结果集。
MyBatis 使用简单的 XML 或注解来配置和映射基本体，
将接口和 Java 的 POJOs(Plain Old Java Objects,普通的 Java对象)映射成数据库中的记录。
审计策略
====
这种一般可以直接黑盒找到，如果只是代码片段快速扫描可控制的参数或者相关的sql关键字查看，可能在一般源码中遇到的不是百度中遇到的那种简单的形式，故把我遇到的一些说一下。
实例：开源的教育平台，这里为控制层（该漏洞已修复）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-4adf015c76b7f84737858deb48d5d489f87d279c.png)
String\[\] aridArr = request.getParameterValues("articelId");
关键代码，代码前台获取到具体参数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-32b85299afd8b568ded1408c039b6b0d60e3c4fd.png)
然后到接口和接口实现类
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-d2863419a82d7e5e48208af3ce3f0db62f11f302.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-93d26de1312e62166fdea184f3192ad652fe5cd7.png)
这里只看最关键的sql部分
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-f626e7d4fc808deeb756bbdcd016cb3b750e55d5.png)
用${}直接拼接，会产生注入，故源头在此处。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-adb9b45f9118e5e32aef45101b87cf02e84db758.png)
in 语句问题
Select \*from news where id in (#{id})，
这样写程序会报错，研发人员将SQL查询语句修改如下：
Select\* from news where id in (${id})，
修改SQL语句之后，程序停止报错，但是可能会产生SQL注入漏洞。
### 1.#和$的区别
1）#{}是预编译处理，$ {}是字符串替换；
2）变量替换后,#{}对应的变量自动加上单引号 ''；变量替换后,${}对应的变量不会加上引号 ''
3）#{} 占位符；${} 拼接符；
4）将传入的数据直接拼接在sq l中。造成sql注入如:whereusername=将传入的数据直接拼接在sql中。造成sql注入如:where username=将传入的数据直接拼接在sql中。造成sql注入如：whereusername={username}，如果传入的值是111,那么解析成sql时的值为where username=111；
如果传入的值是1 and 1=1 ;则解析成的sql为：select id, username, password, role from user where username=1 and 1=1；
### 2.Foreach遍历迭代
入参采用需要查询的字段集合，遇到像如下的sql代码，则无注入。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-91a299c29ea1b0fc78ad715287ecfc4493accec8.png)
在SQL中通常用在 in 这个关键词的后面
foreach元素的属性主要有 item，index，collection，open，separator，close；分别代表：
item表示集合中每一个元素进行迭代时的别名；
index用于表示在迭代过程中，每次迭代到的位置；
open表示该语句以什么开始；
separator表示在每次进行迭代之间以什么符号作为分隔符；
close表示以什么结束；
还有其他几种写法，（传入的参数为list或 Array的时候）原理都是差不多的。
### 3.模糊查询
有时候还会遇到如下SQL的例子;也是没有注入的（已知为mysql）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-785abb786fcba1498af09ae4b61fa440d259784c.png)
这里解释一下为什么要这样写
1)尽量避免采用$的方式，$会导致SQL注入， LIKE '%$name$%'和LIKE concat( '%',$name$,'%') 都会导致SQL注入 ；
2)尽量采用 #的方式，#将传入的数据都当成一个字符串，会对自动传入的数据加一个双引号;更详细的可以查看$和#的区别；
### 4.Select注释的使用
在我们平常的应用中往往需要用到mybatis去操作一些原生的sql，也可以应用到一些复杂的应用场景。
一般情况有两种，如图是第一种较为常见
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-0ceddb3f4c8c29a403168e675c43723f9ed777d3.png)
有时候会出现jdbcType类型可以省略，只需字段的类型对齐好数据库中的字段类型即可。这种也是不存在注入的，虽然用了$，但是在下面标注为int类型，不是字符型，故不存在注入。
第二种就是像我们通常写的xml类似，在注解中使用等相关的标签来实现我们复杂的语句，但是必须在外面一层用标签将sql语句含入进去
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-21a733ff3a2939b3bbf365203929d27c14c0184b.png)
因为sql语句中使用了预编译和模糊查询，故不存在注入。
\*\*xss审计\*\*
=========
在我们审计xss漏洞时，首先要审计是否有xss全局过滤器，对于整套系统来说不可能每个功能点自己搞个xss过滤，一般都是通过全局过滤器来进行过滤；
那么结合代码的框架，我们来看一下过滤器
springboot框架下查看shiro中filter过滤器配置；其中并未发现有xss过滤器配置，基本判断无xss过滤
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-b414e8080607bb1c848e7ed60ef62bffcc2a9814.png)
在基础资料---供应商管理：payload：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-847d772b2d02ea821504da89975618576ce3cdbf.png)
\*\*任意添加用户信息\*\*
============
添加/修改这类能够直接写入数据库数据的操作
在/role目录下的添加用户操作/save
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-ce7bc883a31336081e6925f130d3ee97405f5a18.png)
在save方法中只对用户信息做了校验并直接使用addUser()方法将数据进行了提交，并未对提交次数进行验证，因此存在无限次添加用户信息。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-da270f6d86afe591afdac4297322de5e0c43e2bd.png)
黑盒验证：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-519a0daa4cd2397931b8e794e4d4d7d77348e181.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-b1c6d5c1991608bc6e97bff7a942b2818bb103f8.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2022/12/attach-9c583f1099f46e892e3b4c136397b65fb5efc67b.png)

* 发表于 2022-12-02 09:00:02
* 阅读 ( 10033 )
* 分类：[代码审计](https://forum.butian.net/community/code%20audit)

3 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![fan](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b87b7eda468fed599dbaff7370938104a282eae.png)](https://forum.butian.net/people/3292)

[fan](https://forum.butian.net/people/3292)

4 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![fan](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b87b7eda468fed599dbaff7370938104a282eae.png)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---