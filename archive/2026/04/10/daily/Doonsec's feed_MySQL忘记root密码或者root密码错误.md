---
title: MySQL忘记root密码或者root密码错误
url: https://mp.weixin.qq.com/s/QtLkAo3HBvWA4fb7MiZqRA
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:20:39.254740
---

# MySQL忘记root密码或者root密码错误

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/V1icTKBjMOiasxZVeSJQJhcKeqT5AMBg9cjkicJHC5Q98hX8TEQLcmgbcmhTYxoBjyJzaiafQ6fY10ovrsElN7SmyKwkDa6LicuAMZaINLVC9DrU/0?wx_fmt=jpeg)

# MySQL忘记root密码或者root密码错误

原创

guowei
guowei

网络安全直通车

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 说明：有的同学安装了MySQL之后用root密码登录不上（先检查一下复制的密码对不对，有没有多了空格冒号之类的）。

如果提示access denied for user root，就是密码错误。这个时候需要修改root密码，为了方便输入，可以修改成一个比较简单的密码。

适用版本：MySQL 5.7。

8.0看这个：https://www.jb51.net/article/145464.htm

# 1、配置跳过权限验证

没有密码无法登录，先配置跳过权限验证，不校验登录密码。

Windows环境下MySQL Server的配置文件为my.ini，一般在 MySQL 的安装目录下。

例如：`C:\ProgramData\MySQL\MySQL Server 5.7`

(Linux的配置文件是`/etc/my.cnf`，同样适用)

在配置文件中加一行`skip-grant-tables`

```
[mysqld]
skip-grant-tables
```

# 2、重启数据库服务

在服务中重启：

# 3、修改密码

使用mysql命令登录，使用以下密码修改密码。

命令行连接到服务端（也可以用Navicat，空密码登陆）：

```
mysql -uroot;
use mysql;
```

执行以下SQL：
`update user set authentication_string=password('123456') where Host='localhost' and User='root';`

# 4、还原配置

密码修改成功了，后面还是需要用密码登录。

修改以后，在配置文件my.ini中去掉skip-grant-tables，重启数据库服务。
再使用 `mysql -uroot -p123456` 登录。

# 5、修改密码安全限制

否则不能使用简单密码。

永久修改：
MySQL默认的配置文件：my.ini
(Linux的配置文件是`/etc/my.cnf`，同样适用)

```
validate_password_policy=0
validate_password_length=1
```

# 6、授权远程访问

连接到数据库以后

```
grant all privileges on *.* to 'root'@'%' identified by '123456';
flush privileges;
```

实测mysqld –skip-grant-tables这样的命令行，在mysql8中无法成功启动，而且测试了该参数放在ini文件里面也同样无法启动

MySQL的密码是存放在user表里面的，修改密码其实就是修改表中记录。

重置的思路是是想办法不用密码进入系统，然后用数据库命令修改表user中的密码记录。

查了下，MySQL5系统在网上建议的方法是以–skip-grant-tables参数启动mysql服务，该参数指示在启动时不加载授权表，因此启动成功后root用户可以空密码登陆

> mysqld –skip-grant-tables

登陆之后可以用

> UPDATE user SET authentication\_string=” WHERE user='root';

这类命令设置密码或者将密码置空。

但是，实测mysqld –skip-grant-tables这样的命令行，在mysql8中无法成功启动，而且测试了该参数放在ini文件里面也同样无法启动

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V1icTKBjMOiavu7H5zJC1O6g9TmuJ97NLzDIS2YvrZQpuA73bV4SQAAqiaZlXpITsjcOltqn0QKkJwb9ic0FnflFklCrPMjy1m3GTc73lPuFSSs/640?wx_fmt=jpeg&from=appmsg)

**MySQL8系统密码重置的两个思路**

两条思路，或者用–init-file参数在服务启动时加载并运行修改密码的命令文件，该命令一旦执行，服务启动后密码即已经清除或者重置，启动服务后即可以空密码或指定密码登入。

或者继续研究–skip-grant-tables命令行参数下服务不能启动的原因，解决问题，然后启动服务后以空密码登入，手工输入命令，执行清除或者重置mysql.user表中的密码记录字段。

推荐使用前者。

具体操作流程如下：

**方法一:利用–init-file参数解决**

该参数指定服务启动时先执行一个包含sql命令文件，因此，只需要将重置密码的命令写在该文件中，以此参数指定启动时执行该命令，启动完成即可重置系统密码了。

第一步，关掉系统服务

> net stop mysql

第二步，创建一个文本文件，内含一条密码修改命令

> ALTER USER ‘root'@'localhost' IDENTIFIED BY ”;

第三步：命令行方式启动服务器，指定启动时执行上述的密码修改命令文件

> mysqld –init-file=d:mysqlc.txt –console

具体操作截图

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V1icTKBjMOiasXP04ic4CELQfFN5cCdrygOVib0N9NL7FLxR8sqFHY1EK0cYkB1CjAoZr0cicJia8TxXAsYsX91IibRzSytnmZvusPqJaHWHAZCm3k/640?wx_fmt=jpeg&from=appmsg)

**方法二，想办法让–skip-grant-tables参数用起来**

同方法一，先关掉系统服务

实测，在mysql8系统下，用mysqld –console –skip-grant-tables –shared-memory可以无密码启动服务

![](https://mmbiz.qpic.cn/mmbiz_jpg/V1icTKBjMOiauC94YooqfeibFzicHpykibwaQXdOT7n9KHkI0fXvXzkGY2voiaTiaDKORlTtYk2uP6bg2vVLnlszr69f607WnKkjlqECqJAt91dXRk/640?wx_fmt=jpeg&from=appmsg)

服务启动后，以空密码登入系统

> mysql.exe -u root

然后执行sql命令将root用户密码设置为空

> UPDATE mysql.user SET authentication\_string=” WHERE user='root' and host='localhost';

具体操作截图

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V1icTKBjMOiasKuibu5OfJJM58edetcbVqhytibYzNzVMQmP8lOlPpA9lR08p2UNCvmNhB10xrKDI8SPibhicGicFgv89QfqpdIGqusYymvRRkNv0M/640?wx_fmt=jpeg&from=appmsg)

MySQL8的一些特性导致老方法重置不大管用了，建议使用–init-file参数解决，实测安全可靠。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/J8AVIknUyQlKATmLAFibRG7DezjkNIEqbwEYR0fRY4WYibs8SZ8CtNC2NZHEu3nicHJx1rVoe96v4XZDpdRJ2aWbQ/0?wx_fmt=png)

网络安全直通车

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/J8AVIknUyQlKATmLAFibRG7DezjkNIEqbwEYR0fRY4WYibs8SZ8CtNC2NZHEu3nicHJx1rVoe96v4XZDpdRJ2aWbQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过