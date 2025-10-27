---
title: PHP代码审计之taocms
url: https://buaq.net/go-146695.html
source: unSafe.sh - 不安全
date: 2023-01-26
fetch_date: 2025-10-04T04:50:02.817915
---

# PHP代码审计之taocms

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/fd5dbacbb18e9b6cef8b59151e52b666.jpg)

PHP代码审计之taocms

首先我们来分析该系统的路由信息，以及如何进行参数的构造。该系统有两个路由，一是前台功能点路由，二后台功能点路由，但两个路由代码类似只不过后台路由添加了s
*2023-1-25 17:32:0
Author: [xz.aliyun.com(查看原文)](/jump-146695.htm)
阅读量:34
收藏*

---

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125163732-825f3950-9c8b-1.png)

该系统有两个路由，一是前台功能点路由，二后台功能点路由，但两个路由代码类似只不过后台路由添
加了session校验，我们先来看看前台路由是怎么构造的。
前台路由放在api.php文件中。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230125163843-ad3b0de8-9c8b-1.png)
 **在common.php中22行代码处中调用\_\_autoload() 魔术方法来加载 Model 文件夹下的功能代码，方便后续路由的调用。在代码30行去除 get\_magic\_quotes\_gpc() 方法对特殊字符加载的反斜杠，这可能是为了代码的兼容性。**

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164106-0275df18-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164114-06c0ee28-9c8c-1.png)

代码5、6两行传入两个参数 ctrl 、 action ,第7行代码其实就是将 action 传过来的参数首字母转换为
大写，因为类名首字母都是大写的，第8行判断该类是否为 Api 或 Comment。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164140-16a66250-9c8c-1.png)

后台路由代码 admin.php 文件与前台路由代码基本类似，只是在上面添加了session校验，检测是否为
登录状态。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164151-1ccf2afe-9c8c-1.png)

## 1.任意文件读取/下载

通过上面的路由信息我们知道功能点文件存放在Model文件夹下，我们去翻找Model文件夹发现
file.php 文件也就是File这个类下存在一个 download() 方法。
在这个类中的第85行代码处，我们一目了然的看到了 file\_get\_contents() 函数，看到这个函数想要
利用，我们会下意思的想到两个点：第一该函数的参数是否可控；第二该函数是没有回显的，如果想要
利用是需要使用 echo 等函数配合。我们只需要查看这里file\_get\_contents() 中参数是否可控就可以了。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164216-2c1a64f6-9c8c-1.png)

### 漏洞复现：

由于在上面我们已经分析过路由的构造，所以我们可以不用特意去找功能点就能构造出利用路由。
在路由中 action 传入的是我们要实例化的类名 file ， ctrl 则对应我们需要调用的方法 download 。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164232-358a9380-9c8c-1.png)

## 2.任意文件上传

首先我们去创建一个.php后缀的文件

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164250-40030f68-9c8c-1.png)

通过这里我们发现 executeupload() 方法中调用了Upload类下的 upload() 方法，这里的上传主要调
用了upload()方法，我们主要去看下他是如何进行过滤的。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164303-48378e2a-9c8c-1.png)

在该方法的最上面定义了 $upext 变量，这里包含了可以上传的后缀名，也就是白名单，大致看了这些
后缀没有可利用的。然后下面通过 $\_FILES 接收上传文件，通过 pathinfo() 获取上传文件名。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164321-5286e4de-9c8c-1.png)

关键在于代码106行通过 [extension] 获取后缀名，然后到代码107行进行正则匹配如果上传的文件名
不在 $upext 白名单中，则返回下面的提示信息。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164339-5d7c1008-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164346-61d67030-9c8c-1.png)

这里上传是走不通的，但是在上传的右边有一个创建文件的功能点，我们发现这里竟然没有限制可以上
传任意文件，

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164354-66a593a2-9c8c-1.png)

在 create() 方法中，首先接收文件名 name ，然后通过 isdir 来判断创建的是目录还是文件，然后分别做不同的操作进行创建。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164416-735f47e6-9c8c-1.png)

然后我们在看看他是如何进行文件写入的，其实下面的功能点就可以直接写入文件内容，
![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164431-7c357296-9c8c-1.png)

其实这里写入内容的代码也在 File 这个类中，在 save() 方法中只是对该文件是否具有写入权限进行判
断，就直接将内容写入到文件中。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164444-84667c9e-9c8c-1.png)

### 漏洞复现：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164457-8b9d7986-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164516-96f688e0-9c8c-1.png)

## 3.mysql日志文件getshell

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164529-9eaf6a84-9c8c-1.png)

在Sql类下的 excute() 方法，依旧的简洁明了。通过14行传入 $sqltext 参数也就是我们的SQL语句，
在15行实例化 Dbclass 类调用其中 query() 方法直接执行SQL语句。最后18行将我们SQL语句结果进行
打印输出。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164540-a58e8a88-9c8c-1.png)

### 漏洞复现：

MySQL日志文件getshell
Mysql 5.6.34版本以后无法通过into outfile、into dumpfile进行文件写入
我们通过日志文件写shell即可
set global general\_log = on;
set global general\_log\_file = '网站绝对路径';
![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164550-aba29c0c-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164559-b0ceba26-9c8c-1.png)

## 4.通过修改配置文件getshell

在后台有这么一个 网站设置 功能点,大致一看这里的内容和config.php文件中内容是一致的
首先我们去查看代码该功能点代码，这里调用 upload() 方法，第53行直接判断config.php是否可写，
然后通过POST接收参数，但是这里参数值会被57行代码处的 safeword() 方法进行过滤，跟进该方法看
看是如何对输入内容进行过滤的。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164612-b8750eec-9c8c-1.png)

在 safeword() 方法中需要传入两个参数，一个是需要过滤的字符串，另一个参数则决定走哪个case。
上面没有给出第二个参数则直接走默认level,也就是154行下面的代码，在155行判断了数据库类型是否
为 Sqlite 是的话执行Sqlite的过滤代码，如果不是则走158行的else，，调用 Base::\_addslashs() 方
法,跟进该方法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164625-c02af35e-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164632-c4bc50fc-9c8c-1.png)

将传入的字符通过 addslashes() 函数将特殊字符添加反斜杠，无法绕过限制。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164643-caf2ef8a-9c8c-1.png)

所以我们只能走上面的if条件，这里只要数据库为 Sqlite ，下面的单引号会被替换为两个单引号(当时以
为将单引号替换为双引号了)，而这个替换方式是可以被绕过的。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164651-cfb7c342-9c8c-1.png)

然后我们返回 upload() 方法的第60行，直接将过滤后的内容通过 file\_put\_contents() 写入到
config.php中。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164658-d42351a8-9c8c-1.png)

通过分析源码，我们知道输入的单引号会替换为两个双引号，如果我们输入 \' 这样在替换为两个双
引号的时候第一个双引号前会有一个反斜杠，那么我们就可以闭合前面的双引号，我们的PHP代码就能
逃逸出来。我们的payload可以构造为：
\');@eval($\_REQUEST[1]);/\*

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164710-db3e4d12-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164720-e0e7e2a0-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164731-e7f58296-9c8c-1.png)

## 5.缓存文件getshell

我们在搜索危险函数的时候发现一处很有可能getshell的地方，我们先看这里的$arrayData是否可控。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164745-f00d96d0-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164758-f7a098fc-9c8c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164807-fd3b45b4-9c8c-1.png)

这里代码37行的 $o 也就是对应代码49行的 $cat 数组中的内容是从数据库中 cms\_category 表中获取的。那么如果这里表中的内容是我们可以控制的那么就能写入任意内容。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164827-0949d5fa-9c8d-1.png)

我们去看下该表中的内容

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164841-112b1ad6-9c8d-1.png)

从数据内容可以看出这里的功能点其实就是 管理栏目 中的内容，这里就可以添加内容。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125164856-1a6bf0fc-9c8d-1.png)

这里通过 columsdata() 接收参数，然后通过 add\_one() 进行数据插入这里还是通过 safeword() 进行数据的过滤的，但是这里的 safeword() 方法在后续并没有起到过滤的效果。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125165012-4768cc7e-9c8d-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125165020-4c3c6d1e-9c8d-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125165027-50842fec-9c8d-1.png)

通过搜索该文件可以发现有好几处包含了该模板文件，所以我们这里就可以通过写入缓存文件getshell。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125165041-58adfda6-9c8d-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125165048-5ce758e0-9c8d-1.png)

cat\_array.inc 文件内容如下

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125165055-618a8ebc-9c8d-1.png)

然后我们访问刚才包含该文件的路由

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125165103-662a6956-9c8d-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125165112-6b3d1db2-9c8d-1.png)

## 6.sql注入

直接先进入admin.php和index.php

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125170321-1e2ba73a-9c8f-1.png)

可以通过函数名和语义分析出是根据一些变量或者一些路径来渲染，加载模板文件，随后回显到前端。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230125170338-27e33964-9c8f-1.png)

再看admin.php，发现存在action参数和ctrl参数。
发现有两个方法，class\_exists和method\_exists，这两个函数是判断是否存在类和方法的，接下if内的语句判断，指导action是类名，ctrl是函数名，有点像路由

![](https://xzfile.aliyuncs.com/me...