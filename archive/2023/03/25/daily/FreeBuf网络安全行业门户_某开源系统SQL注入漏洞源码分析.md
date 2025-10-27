---
title: 某开源系统SQL注入漏洞源码分析
url: https://www.freebuf.com/articles/web/361423.html
source: FreeBuf网络安全行业门户
date: 2023-03-25
fetch_date: 2025-10-04T10:37:16.780688
---

# 某开源系统SQL注入漏洞源码分析

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

某开源系统SQL注入漏洞源码分析

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

某开源系统SQL注入漏洞源码分析

2023-03-24 09:53:26

所属地 北京

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## ****1. 简介****

大家好，我是观宇战队Di@m1racl3，今天给大家分享一个针对某开源系统SQL注入漏洞源码分析的案例，该开源系统是使用PHP + MySQL开发的一款专业开源项目管理软件，功能丰富，集产品管理、项目管理、测试管理、人员管理、发布管理、事务管理等功能于一体。由于操作简洁高效，统计报表丰富多样，软件架构拓展灵活，所以被很多企业广泛应用。因此也成为广大安全爱好者研究的重点对象。

## ****2.**** ****漏洞概述****

该开源系统对输入的account参数内容未做过滤校验，直接将其拼接到SQL查询语句中，导致SQL注入漏洞。

## ****3. 漏洞影响版本****

开源版：16.5，16.5beta1

企业版：6.5，6.5beta1

旗舰版：3.0，3.0beta1

## ****4. 代码审计分析****

### ****4.1**** ****系统介绍****

#### ****4********.1.1**** ****系统架构简介****

在进行源代码分析前，首先学习一下该系统的目录结构。该系统基于b/s架构开发，支持MVC（Model-View-Controller）软件架构模式，把软件系统分为三个基本部分：

模型（Model）：实现程序的功能、数据管理和数据库设计，对数据库的增删改查可以放在这一层。

控制器（Controller）：负责转发用户请求，对请求进行处理，组织各种业务逻辑，准备数据。

视图（View）：负责渲染数据，图形界面设计，通过HTML方式呈现给用户。

#### ****4.1.2**** ****系统运行方式简介****

（1）通过apache服务将请求转交给\xxx\www\index.php，通过它来进行资源调度。

（2）index.php加载框架文件，初始化应用，解析URI请求，得到请求对应的模块名、方法和参数。比如如果有一个URL为：http://<ip:port>/xxx/testcase-browse-1.html，则模块名为testcase，方法名为browse，参数为1。

（3）然后加载相应模块的control方法和model方法，最后渲染view文件呈献给用户。

#### ****4.1.3**** ****系统数据库操作简介****

该系统中数据库的操作是通过数据库的对象类DAO来实现的，定义在\lib\dao\dao.class.php中，系统启动时会自动生成$this->dao对象，可以在control、model以及view层直接使用$this->dao来执行各种数据库操作，查询数据库使用fetch系列方法，增删改相关方法使用exec方法。

如查询所有数据，使用如下示例代码，这里使用fetchAll方法来实现：

```
$this->dao->select('*')->from(TABLE_CASE)->where('deleted')->eq(0)->fetchAll('id');
```

插入数据使用如下示例代码，使用exec方法来实现：

```
$this->dao->insert(TABLE_CASE)->data($case)->autoCheck()->exec();
```

### ****4.2**** ****系统目录结构介绍****

在官网下载源码包，解压后可以看到整个目录结构，如下图所示：![](https://image.3001.net/images/20230323/1679566020_641c24c4e3bb7f2025137.png!small)

图4.1 系统目录结构

```
api是接口目录
bin存放系统的一些命令行脚本
config存放系统运行的主配置文件和数据配置文件
db存放历次升级的数据库脚本和完整的建库脚本
doc存放系统相关的文档
framework是框架的核心目录，里面包含了router、control、model和helper的核心文件
lib存放常用的类文件，如html、js和css类、数据库DAO类、数据验证fixer类等
module存放具体的功能模块，每个模块一个目录
sdk存放PHP sdk类
tmp存放运行时的临时文件，如运行日志等
www存放各种样式表文件、js文件、图片文件以及该项目管理系统的入口程序index.php
```

模块目录结构如下图所示：

![](https://image.3001.net/images/20230324/1679620159_641cf83f44f7bd863297b.jpg!small)

图4.2 模块目录结构

```
config.php为该模块的配置文件，可以用来存放专门针对这个模块的配置，也可以覆盖全局性的配置
lang:存放各种语言的文件，比如中文存为zh-cn.php，英语存为en.php，繁体存为zh-tw.php
control.php为这个模块对应的控制器类文件
model.php为这个模块对应的业务逻辑类文件
view存放的各个方法的视图文件，比如index.html.php是index方法的模板文件
```

### ****4.3**** ****系统代码调用流程介绍****

如果是下载一键安装包，启动后首先从htdocs/index.php页面进入，在点击开源版后，后台自动转到登录界面，入口为xxx/www/index.php，在该文件中，加载框架包，然后创建各种实例，并初始化各种路径、主配置、链接数据库等，解析URL请求也在该文件中，由parseRequest函数来实现。

![](https://image.3001.net/images/20230324/1679621477_641cfd65beb76b2e6a46e.jpg!small)

图4.3 htdocs/index.php页面

![](https://image.3001.net/images/20230324/1679621495_641cfd77a77c1a31bcf76.jpg!small)

图4.4 登录界面

这里如果在启动界面上勾选了启用Apache用户访问验证选项的话，会出现一个登录界面，不能进入上图所示的界面，这里把该选项取消即可。

![](https://image.3001.net/images/20230324/1679620214_641cf876f04f9923b9015.jpg!small)

图4.5 启用Apache用户访问验证截图

![](https://image.3001.net/images/20230324/1679621521_641cfd91574857c416141.jpg!small)

图4.6 取消Apache用户访问验证

在URL解析完成后，就使用loadModule函数加载模块，根据解析出的模块以及方法找到对应的模块以及方法进行初始化和调用，index.php关键代码如下：

```
//加载框架包
include '../framework/router.class.php';
include '../framework/control.class.php';
include '../framework/model.class.php';
include '../framework/helper.class.php';

//创建app实例
$app = router::createApp('pms', dirname(dirname(__FILE__)), 'router');

//启动app
$common = $app->loadCommon();
...

//解析URL请求
$app->parseRequest();
//加载模块
$app->loadModule();
```

loadModule函数关键代码如下：

```
/*
* 创建control类的实例。
* Create a instance of the control.
**/
$module = new $className();
if(!method_exists($module, $methodName)) $this->triggerError("the module $moduleName has no $methodName method", __FILE__, __LINE__, $exit = true);
$this->control = $module;
...
/* 调用该方法   Call the method. */
call_user_func_array(array($module, $methodName), $this->params);
```

### ****4.4**** ****漏洞原理分析****

入口分析发现登录界面的URL为http://127.0.0.1/xxx/user-login-L3plbnRhby8=.html，根据4.1.1中介绍的，模块为user，方法为login，因此找到对应的模块和方法，参数为L3plbnRhby8=。

![](https://image.3001.net/images/20230324/1679621547_641cfdab3c0b8d713ded7.jpg!small)

图4.7 登录界面URL图示

分析源码中user模块control中login方法代码和model中login方法。分析发现在control中，首先判断该账号是否已经登录，如果已经登录则跳过登录阶段，如果没有登录，则从POST或者GET请求中获取账号密码，然后从account两端删除空白字符和其他预定义字符，并且检测该账号是否被锁定，如果锁定就返回失败，respone参数为返回结果，最后通过send函数返回给用户。如果没锁定，则继续往下执行，代码如下：

![](https://image.3001.net/images/20230324/1679620266_641cf8aa949a612d44fa9.jpg!small)

图4.8 登录源码

接着调用user模块model中的identify函数进行账号验证。跟进identify函数，首先会判断账号密码是否为空，然后使用DAO查询数据库中存储的用户名为我们输入的用户名的数据，如果该用户存在，则record中存储的就是该用户的数据，如果用户不存在，则record为空，源代码如下所示。

![](https://image.3001.net/images/20230324/1679620280_641cf8b87b1b1e7ec4f0c.jpg!small)

图4.9 用户名不存在record为false

![](https://image.3001.net/images/20230324/1679620295_641cf8c7ee32983c984df.jpg!small)

图4.10 用户名存在record不为false

![](https://image.3001.net/images/20230324/1679620310_641cf8d6a63a2cf0be229.jpg!small)

图4.11 identify函数源码解析

分析发现，只有在数据库中查询数据时，record不为false可以进入密码校验，如果record为false，即该用户不存在，则直接登录失败。截止目前，登录过程中account的数据库操作过程分析完毕。登录过程中使用DAO进行数据查询代码为：

```
//查询数据库中存储的用户名为输入用户的数据
$record = $this->dao->select('*')->from(TABLE_USER)
    ->where('account')->eq($account)
    ->beginIF(strlen($password) <
32)->andWhere('password')->eq(md5($password))->fi()
    ->andWhere('deleted')->eq(0)
    ->fetch();
```

使用漏洞验证POC调试发现，该查询sql语句为：

```
"SELECT * FROM `zt_user` wHeRe account  = 'admin\' AND (SELECT 1337 FROM (SELECT(SLEEP(5)))a)-- b' AND  deleted  = '0'"
```

![](https://image.3001.net/images/20230324/1679620330_641cf8eaa405bf4222f6e.jpg!small)

图4.12 登录验证启用了字符转义

输入的单引号被转义了，调试时并没有在此处发现任何延迟，因此注入点不在此代码中。我们知道，造成SQL注入的原因一般为，在构造SQL语句时没有过滤传入的参数，直接将其拼接，而这里对输入的参数进行了转义，需要找到直接拼接SQL语句的地方。

通过在源码里全局查找，发现在framework/base/router.class.php中存在如下代码：

![](https://image.3001.net/images/20230324/1679620347_641cf8fb89d0ee4ff28e0.jpg!small)

图4.13 serVision函数源码分析

分析发现在系统入口www/index.php中，每次登录请求都会调用createApp函数，而该函数调用就会调用router.class.php中的构造函数，setVision函数就在构造函数中，因此每次登录操作都会调用该函数。

![](https://image.3001.net/images/20230324/1679620365_641cf90d8cb789ef33a17.jpg!small)

图4.14 index.php中createApp函数

![](https://image.3001.net/images/20230324/1679620383_641cf91f12f7ba7538d9f.jpg!small)

图4.15 router.class.php中的构造函数

在setVision函数下断点，调试发现无法直接获取该sql语句，于是修改一下代码如下所示：

![](https://image.3001.net/images/20230324/1679620404_641cf9340320a9d98e0ff.jpg!small)

图4.16 修改获取sql语句代码

继续调试得到导致SQL注入的语句为：

```
"SELECT * FROM `zt_config` WHERE owner = 'admin' AND (SELECT 1337 FROM (SELECT(SLEEP(5)))a)-- b' AND `key` = 'vision' LIMIT 1"
```

![](https://image.3001.net/images/20230324/1679620420_641cf9447c5e25247724b.jpg!small)

图4.17 setVision函数拼接的sql语句

单步跟踪，在query函数处会存在延迟响应，即存在延迟注入。

## ****5. 漏洞复现****

在官网下载16.5版本一键安装包。

![](https://image.3001.net/images/20230324/1679621579_641cfdcb7fcdfc4150a78.jpg!small)

图5.1 安装包下载

双击解压，得到xampp目录，进入该目录，双击start.exe，启动该系统， 然后访问首页。

![](https://image.3001.net/images/20230324/1679621595_641cfddbd428ecc4c55a1.jpg!small)

图5.2 启动截图

![](https://image.3001.net/images/20230324/1679621612_641cfdecac5d818e0948d.jpg!small)

图5.3 登录界面

随便输入用户名和密码，然后使用burp抓包，测试延迟注入结果如下图所示。测试payload为：

```
admin' AN...