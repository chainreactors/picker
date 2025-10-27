---
title: Linux搭建SVN服务器详细教程
url: https://blog.upx8.com/3169
source: 黑海洋 - WIKI
date: 2023-01-10
fetch_date: 2025-10-04T03:27:33.050259
---

# Linux搭建SVN服务器详细教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux搭建SVN服务器详细教程

发布时间:
2023-01-09

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
12385

SVN是subversion的缩写，是一个开放源代码的版本控制系统，通过采用分支管理系统的高效管理，实现最终集中式的管理。

目前很多互联网公司在使用SVN，优点在于使用方便、易于管理。与之对应的分布式的版本控制系统Git则更加灵活。

## 搭建

### 安装SVN

//Ubuntu

        apt-get install subversion

        //Centos

        yum install subversion

查看是否安装成功，可以查看版本。

         svnserve --version

提示版本1.13.0，说明已安装成功。

### 创建版本库目录

创建SVN版本库目录，为后面创建版本库提供存放位置，也是最后启动SVN服务的根目录。

我们在/usr路径下创建svn目录作为版本库目录。

> cd /usr
>
> mkdir svn

所以，将SVN库存放在用户文件目录/usr下比较合理

### 创建SVN版本库

在上一步建立路径基础上，创建版本库，如dev。

cd /usr/svn

svnadmin create dev

创建成功后，可以查看到dev目录下生成的文件。

### 修改SVN配置

进入conf目录，查看需要修改的配置文件。

cd /usr/svn/dev/conf

ls

配置文件：

* authz：权限配置文件，控制读写权限
* passwd：账号密码配置文件
* svnserve.conf：svn服务器配置文件

#### 修改svnserve.conf文件

vim svnserve.conf

![](//imgsrc.baidu.com/imgad/pic/item/800a19d8bc3eb1357bf6a07ee31ea8d3fc1f44c5.jpg)

去掉anon-access、auth-access、password-db、authz-db、realm几项前的注释符号“#”。

配置项含义：

* anon-access = none|read|write 决定非授权用户的访问级别。none 表示无访问权限，read 表示只读，write 表示可读可写，默认为 read。
* auth-access = none|read|write 决定授权用户的访问级别，使用与上面相同的访问级别。默认为 write。
* password-db = filename 指定账号密码数据库文件名。filename 是相对仓库中 conf 目录的位置，也可以设置为绝对路径，默认为passwd。
* authz-db = filename 指定权限配置文件名，filename 是相对仓库中 conf 目录的位置，也可以设置为绝对路径，默认为authz。
* realm = realm-name 指定版本库的认证域，即在登录时提示的认证域名称。若两个版本库的认证域相同，建议使用相同的账号密码数据库文件passwd。

vim passwd

**![](//imgsrc.baidu.com/imgad/pic/item/11dfa9ec8a136327a7c0d5f6d48fa0ec09fac7c2.jpg)**

只需在末尾添加账号和密码，格式 `账号 = 密码`，如`user1 = 123456`，可添加多个。

#### 修改authz文件

vim authz

在根目录下设置user1、user2读写权限：（注意：[/]也是必须的）

![](//imgsrc.baidu.com/imgad/pic/item/d5628535e5dde711b3fb5433e2efce1b9c1661cd.jpg)

如果用户比较多，可以使用groups形式设置分组team1，并在根目录下指定分组@team1的权限：

![](//imgsrc.baidu.com/imgad/pic/item/b2fb43166d224f4af31664d64cf790529922d16c.jpg)

 如果想设置其他用户的权限，可以通过`*`设置，如设置除@team1分组外其他用户只读权限：

[/]

@team1 = rw

\* = r

### 启动SVN服务

执行SVN启动命令，其中参数`-d`表示以守护进程的方式启动， `-r`表示设置的根目录。

```
svnserve -d -r /usr/svn/
```

关闭svn命令：

```
killall svnserve
```

**检测svn端口3690是否已经监听：**

```
netstat -antlp|grep svnserve
netstat -antlp|grep 3690
ps -ef | grep 'svnserve'
```

### 本地访问SVN服务

在windows系统中，安装TortoiseSVN软件，创建一个本地目录，右键选择SVN Checkout测试下，URL填写`svn://IP/dev`，dev替换成你创建的版本库名称。

![](//imgsrc.baidu.com/imgad/pic/item/55fbb2fb43166d229dff0251032309f79152d26f.jpg)![](https://img2022.cnblogs.com/blog/984421/202203/984421-20220317115445160-1002085075.png)

输入passwd配置好的用户。

![](//imgsrc.baidu.com/imgad/pic/item/62d0f703918fa0ecc14c73c8639759ee3c6ddb68.jpg)

Checkout completed，SVN访问成功，这就Nice了~

![](https://img2022.cnblogs.com/blog/984421/202203/984421-20220317115507448-1427171919.png)![](//imgsrc.baidu.com/imgad/pic/item/a9773912b31bb0515caea4ed737adab44bede069.jpg)

# Ubuntu防火墙设置开放端口：3690

**防火墙设置：**[https://blog.upx8.com/3180](https://blog.upx8.com/3180 "https://blog.upx8.com/3180")

开放端口：3690

[取消回复](https://blog.upx8.com/3169#respond-post-3169)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")