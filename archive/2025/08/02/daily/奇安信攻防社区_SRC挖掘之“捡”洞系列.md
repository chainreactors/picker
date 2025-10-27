---
title: SRC挖掘之“捡”洞系列
url: https://forum.butian.net/share/4474
source: 奇安信攻防社区
date: 2025-08-02
fetch_date: 2025-10-07T00:18:07.329753
---

# SRC挖掘之“捡”洞系列

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

### SRC挖掘之“捡”洞系列

* [渗透测试](https://forum.butian.net/topic/47)

在SRC挖掘中，当输入单引号，出现报错，会不会高兴的跳起来，然后打开sqlmap，level设到最高，以为自己竟然能捡到洞，运气真好，结果却是does not seem to be injectable。

### 前言
在测试过程中接触到一个从没有见过的数据库，不过好在有AI的加持，其次也很幸运地有一个能线上直接用的数据库网站，造就了这次“捡”洞之旅。
### 发现过程
开局一个登录框，挂上burp，先抓个登陆包看看，可以看到跟网址有区别应该是个前后端分离的网站，遇到前后端分离的网站时复制一下数据包的url，去访问一下看是否为springboot搭建的，这个网站运气很好是springboot，使用工具测试看看是不是有泄露，有一个env泄露，env里面通常会有各种key啊，真是让我欢喜。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-05b749b6f8b7804925a627a6340310615dd381df.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-b2f62ef8e97ff2a55514ed4a87329954659f5968.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-428248d079e07faec0765dce2a466ae57787b339.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-50d7ec5c3ee7e0a4ac4c546bf7f83cb46df81a47.png)
打开查看后，只想说一句，梦里啥都有，一点用都没有，怪不得一直留着没关了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-1e08037beaf0d05a266e0a4ad34bee86c88ee646.png)
固定密码进行爆破，没任何结果，一群大佬虎视眈眈，也不会留给你啊。
查看熊猫头，也没什么有用的东西，有一个没见过的网址，访问后，发现是swagger界面。难道这次真掏上了？
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-6ef725b69986b775293f99c606fc7794d970cd24.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-dd646df5976c3b0ef6409ce6117b3d04f36f40de.png)
swagger基本上就是去测试接口，看看是否有未授权，泄露等漏洞。打开接口进行测试，发现没有任何返回，可以看到首先端口不一样，并且访问的网址是本地127.0.0.1。尝试将接口拼到该网址下，发现是有回显的，证明是可以用的，可能是需要其他东西，并没有搞成，所以选择跳过。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-cb12f6b05f151f1ca9a39cdda9d9e861ce60991a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-ac383db23b37570e7752bcbc9d82d6dbf9b71ae5.png)
查看其他接口，发现有些接口是会给一些需要的参数的，直接拼凑进行测试，数据库报错，运气太好了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-56f1769b95c2eafe9b5c0c1da0ac93a7260a0dfa.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e47686b61b728d89801ce25b417f0290dcd75011.png)
仔细查看报错信息，是在3的地方出现了报错，可以看到是成功带入到语句中的，并且可以发现该数据库是clickhouse数据库。这种数据库是列式数据库，与mysql数据库不同，如果感兴趣的话可以看一下这篇文章，讲的还挺详细的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-724165abd9e61409df9a291c6ed23cbd62b32d11.png)
```php
https://mp.weixin.qq.com/s/zAAteksBIvCXaqzCMGqAMw
```
既然带入到数据库了，直接上sqlmap进行测试。结果没有结果。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-18c2c7f5fc60e8275be04a80ec358980567c47c2.png)
#### 测试过程
回到数据包中，参数logstore，会不会是路径呢，输入/tmp/log发包，/报错，删除第一个/后发现本来带入的是tmp/log，但是最后显示出来的只剩/log，前面的tmp没了，难道是tmp对了？将/log删除，此时数据库不再报错，但是显示tmp表不存在。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-a2d8dc3744faebb660b7466420f1db8953ab4f57.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-ac8e17074af93841af978965b4aee1591e5b2860.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-4c4708db4b428d7adb198350ae9ca46706847504.png)
到这先稍微了解一下语法，在clickhouse数据库中,查询表名的语法例子：如果有数据，select \*from default.actors
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-9695dc5aba1d58256389a3b52df2077561ec88e9.png)
如果没有表不存在没有数据，select\* from default.actor1
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-965fa9a8667d306d33c91ba8225fbe30670110ef.png)
对比一下漏洞网站的报错不存在tmp表，大概还原一下查询语句
```php
SELECT \*from apaaslog.tmp WHERE 1 = 1 AND appid = '1' AND tenantname != '' AND receive\_date IN (today(), yesterday()) ORDER BY tenantname ASC
```
在演示网站可以看到也是有log相关的表名的，结合一下该系统的title就是日志管理系统，并且这种数据库大多数是用来做大数据分析的，猜测是否该系统存着该厂商的一些日志，难道这个系统就是类似于某音，根据喜好做分析推送的？
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-0a6bfae176a6c14b8ae4d1eba7ad0260b5546899.png)
想到这回到刚开始发现的/env泄露，应该是给这些企业做分析的。可以看到网站都是以公司名为开头，格式为：公司名.厂商主域.com。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-409d495f07784e9f07f1c7578db8496314826597.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-24a7b6371506e4276f3447d7fbd91b16131800d2.png)
到此想到既然tmp不存在，是不是它使用公司名作为日志文件的呢？将env中的子域名进行收集，使用ai查找关于日志文件的构造，利用脚本直接进行生成日志文件。放入burp中，进行爆破。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-9a7ff9677c2b6a3c0afb5382a3758bf494102681.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-0b880fac972392edc2c6149bf69a23ec8406ef5a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-816db45725ff396a274a593f4c9e5f3755256fd5.png)
发现问题，生成的日志名在爆破过程中显示的是Database test doesn't exist,而不是Table apaaslog.tmp doesn't exist，对比发送的数据一个是tmp，另一个是test.log，最后发现是点的问题，也就是说它会把点前面的识别成数据库，如果我们用一个系统自带的数据库和数据表，这样的话岂不是语句的条件就成立了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-9ddab7d820af9c4943060bbce16acab8cf2198d6.png)
在clickhouse中，system.tables是系统自带的表，直接进行测试，报错显示的是没有相关的列，证明SQL语句是完整的执行了，只不过是前面做筛选的列这个表中没有，庆幸的是爆出了真正的sql语句。其中$$包含的就是数据包的参数。虽然拿到了真正的语句，但是在测试时前面的限制条件我们是无法更改的，所以只能对语句后面做测试，所以还是得找一个满足限制条件的表，只能继续爆破了，并且只要加上点他就会默认点前面是数据库，回想到演示网站中的日志表后缀为\\_log，将点改成\\_重新生成，然后继续爆破。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-a6c80d89057b30c034dc501903ca33882f80616e.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-5ba035df4ea8a4e7c60efebd508ec2757a65a6a7.png)
```php
SELECT DISTINCT tenantcode, tenantname from $system.tables$ WHERE 1 = 1 AND appid = '1' AND tenantname != '' AND receive\_date IN (today(), yesterday()) ORDER BY tenantname ASC
```
成功爆破出一个表
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-8e2fe986ce2facaa6e120b1edd9eafb4b1fa28ab.png)
#### 利用过程
直接访问发现并没有任何信息，在mysql数据库中有注释符--和#用来做注解，但在渗透测试过程中，更多的是用来注释后面要执行的语句，在clickhouse中同样也有--，但是在clickhouse中需要加上分号(;--)，成功返回信息。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-c949d125a507340d486e6f9faa1d5579ce732f36.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-b4dd436f623ed568e889ee66088e0ba3bab212ce.png)
既然可以注释掉后面的where语句，当然也可以添加sql语句进行查询，例如查询数据库。到此算是初步找到了漏洞点，后续就要围绕这个点继续扩大危害。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-3edc6a09c1d6c96ccbf84be47c6c3300fbfe4011.png)
在该数据库中存在一个url函数本意是对向外访问然后将数据插入到数据库，但是在渗透测试里，我们可以把它看成ssrf的利用点，先说一下我的当时的思路，首先利用dnslog可以看到它回显的ip地址，通过查询发现是腾讯云，既然是云上的就查元数据，获取凭证，拿下该数据库，但是不幸的是没有设置cam(类似于阿里云的RAM)，使用到的语句为
```php
select \* from url('http://metadata.tencentyun.com/latest/meta-data/', CSV, 'column1 String, column2 UInt32')
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-5fcc76574a1d3cf2b50b900228f744a5073a99bd.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-1c9db5d1a4d2c8544428d265d4959ebd4e04b20d.png)
到此我们已经确定是存在ssrf的，我们只是想进一步去扩大危害，比较平常的利用方式网上一堆，在这也就不说的，这里我们只针对clickhouse做利用。在clickhouse数据库中有一个system.clusters表放着数据库集群ip以及端口开放情况，通过漏洞点可使用命令select \\* from system.clusters进行查询，就能得到数据库集群的相关信息，这样就可以直接配合url函数对相关ip进行进一步测试了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-01d8b8d1dfb61dbca5b4acd6f430eb5044364a8d.png)
与此同时，clickhouse集群中，有一个专门的端口是用来进行数据查询的，就是8123，使用方式为http://IP:8123?guery=SQL语句，同样也可以配合url函数进行使用,可惜的是这个系统做的权限校验，没办法继续进一步利用，没法将中危利用成高危。
![image.png](https://cdn-yg-zzbm....