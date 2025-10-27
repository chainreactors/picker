---
title: 玄机应急响应靶场集合WP - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18513230
source: 博客园 - 渗透测试中心
date: 2024-10-30
fetch_date: 2025-10-06T18:52:07.711803
---

# 玄机应急响应靶场集合WP - 渗透测试中心

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

# [玄机应急响应靶场集合WP](https://www.cnblogs.com/backlion/p/18513230 "发布于 2024-10-29 14:53")

## 第一章 应急响应-webshell查杀

简介

```
 靶机账号密码 root xjwebshell
 1.黑客webshell里面的flag flag{xxxxx-xxxx-xxxx-xxxx-xxxx}
 2.黑客使用的什么工具的shell github地址的md5 flag{md5}
 3.黑客隐藏shell的完整路径的md5 flag{md5} 注 : /xxx/xxx/xxx/xxx/xxx.xxx
 4.黑客免杀马完整路径 md5 flag{md5}
```

### 1.黑客webshell里面的flag flag{xxxxx-xxxx-xxxx-xxxx-xxxx}

进去靶机开久了会扣金币，所以一进去把文件dump下来

```
 tar -czvf html.tar.gz ./
```

dump下来之后直接先D盾一把梭先

扫描结果如下

```
 id      级别  大小       CRC        修改时间             文件 (说明)
 --------------------------------------------------------------------------------------------------------------------------------------------
 00001   4     38         FEE1C229   23-08-02 10:52:25    \html\shell.php     『Eval后门 {参数:$_REQUEST[1]}』
 00002   4     808        3F54B485   23-08-02 10:56:39    \html\include\gz.php  『(内藏)Eval后门 {参数:encode($_SESSION[$payloadName],"3c6e0b8a9c15224a")}』
 00003   3     205        D6CF6AC8   23-08-02 16:56:29    \html\wap\top.php   『变量函数[$c($fun)]|可疑文件』
 00004   4     768        3DEFBD91   23-08-02 11:01:06    \html\include\Db\.Mysqli.php  『(内藏)Eval后门 {参数:encode($_SESSION[$payloadName],"3c6e0b8a9c15224a")}』
 --------------------------------------------------------------------------------------------------------------------------------------------
```

有很多，一个一个看在\html\include\gz.php里看到一行注释

```
 //027ccd04-5065-48b6-a32d-77c704a5e26d
```

就是flag了

```
 flag{027ccd04-5065-48b6-a32d-77c704a5e26d}
```

### 2.黑客使用的什么工具的shell github地址的md5 flag{md5}

随便把shell里复制出来一段

```
 $data=encode($data,$key);
     if (isset($_SESSION[$payloadName])){
         $payload=encode($_SESSION[$payloadName],$key);
         if (strpos($payload,"getBasicsInfo")===false){
             $payload=encode($payload,$key);
```

然后直接丢github搜

> 塞不了图片，直接丢github之后左边选code就能看到

看到是哥斯拉

```
 https://github.com/BeichenDream/Godzilla
```

md5一下

```
 flag{39392de3218c333f794befef07ac9257}
```

### 3.黑客隐藏shell的完整路径的md5 flag{md5}注：/xxx/xxx/xxx/xxx/xxx.xxx

隐藏shell我们可以看到d盾扫出来有一个.Mysqli.php的隐藏文件

完整路径就是/var/www/html/include/Db/.Mysqli.php

md5后为flag

```
 flag{aebac0e58cd6c5fad1695ee4d1ac1919}
```

### 4.黑客免杀马完整路径 md5 flag{md5}

至于是不是免杀马

丢杀毒软件看一下

> 塞不了图片，直接丢火绒查杀一下发现有三个都扫出来了，还有一个没扫出来

发现top.php没扫出来，那么就是/var/www/html/wap/top.php了

md5一下之后就是

```
 flag{eeff2eabfd9b7a6d26fc1a53d3f7d1de}
```

## 第一章 应急响应-Linux日志分析

简介

```
 账号root密码linuxrz
 ssh root@IP
 1.有多少IP在爆破主机ssh的root帐号，如果有多个使用","分割
 2.ssh爆破成功登陆的IP是多少，如果有多个使用","分割
 3.爆破用户名字典是什么？如果有多个使用","分割
 4.登陆成功的IP共爆破了多少次
 5.黑客登陆主机后新建了一个后门用户，用户名是多少
```

### 1.有多少IP在爆破主机ssh的root帐号，如果有多个使用","分割

我们先把/var/log里面的日志dump下来

```
 tar -czvf log.tar.gz ./
```

里面找到auth.log.1是放ssh的日志，放到自己虚拟机用正则分析

看有多少ip在爆，直接找登录失败的就行了

```
 cat auth.log.1|grep -a "Failed password for root"
```

输出

```
 Aug  1 07:42:32 linux-rz sshd[7471]: Failed password for root from 192.168.200.32 port 51888 ssh2
 Aug  1 07:47:13 linux-rz sshd[7497]: Failed password for root from 192.168.200.2 port 34703 ssh2
 Aug  1 07:47:18 linux-rz sshd[7499]: Failed password for root from 192.168.200.2 port 46671 ssh2
 Aug  1 07:47:20 linux-rz sshd[7501]: Failed password for root from 192.168.200.2 port 39967 ssh2
 Aug  1 07:47:22 linux-rz sshd[7503]: Failed password for root from 192.168.200.2 port 46647 ssh2
 Aug  1 07:52:59 linux-rz sshd[7606]: Failed password for root from 192.168.200.31 port 40364 ssh2
```

看到就三个ip，那么flag就是

```
 flag{192.168.200.2,192.168.200.31,192.168.200.32}
```

这是ip比较少的情况下，ip比较多的话可以用下面命令

```
 cat auth.log.1 | grep -a "Failed password for root" |awk '{print $11}' |uniq -c
```

输出

```
       1 192.168.200.32
       4 192.168.200.2
       1 192.168.200.31
```

### 2.ssh爆破成功登陆的IP是多少，如果有多个使用","分割

登录成功就找Accepted的字样

```
 cat auth.log.1|grep -a "Accepted "
```

输出

```
 Aug  1 07:47:23 linux-rz sshd[7505]: Accepted password for root from 192.168.200.2 port 46563 ssh2
 Aug  1 07:50:37 linux-rz sshd[7539]: Accepted password for root from 192.168.200.2 port 48070 ssh2
```

就一个192.168.200.2那么flag就是

```
 flag{192.168.200.2}
```

### 3.爆破用户名字典是什么？如果有多个使用","分割

我们看爆破字典，要找验证错误的就是"Failed password"

```
 cat auth.log.1|grep -a "Failed password"
```

输出

```
 Aug  1 07:40:50 linux-rz sshd[7461]: Failed password for invalid user test1 from 192.168.200.35 port 33874 ssh2
 Aug  1 07:41:04 linux-rz sshd[7465]: Failed password for invalid user test2 from 192.168.200.35 port 51640 ssh2
 Aug  1 07:41:13 linux-rz sshd[7468]: Failed password for invalid user test3 from 192.168.200.35 port 48168 ssh2
 Aug  1 07:42:32 linux-rz sshd[7471]: Failed password for root from 192.168.200.32 port 51888 ssh2
 Aug  1 07:46:41 linux-rz sshd[7475]: Failed password for invalid user user from 192.168.200.2 port 36149 ssh2
 Aug  1 07:46:47 linux-rz sshd[7478]: Failed password for invalid user user from 192.168.200.2 port 44425 ssh2
 Aug  1 07:46:50 linux-rz sshd[7480]: Failed password for invalid user user from 192.168.200.2 port 38791 ssh2
 Aug  1 07:46:54 linux-rz sshd[7482]: Failed password for invalid user user from 192.168.200.2 port 37489 ssh2
 Aug  1 07:46:56 linux-rz sshd[7484]: Failed password for invalid user user from 192.168.200.2 port 35575 ssh2
 Aug  1 07:46:59 linux-rz sshd[7486]: Failed password for invalid user hello from 192.168.200.2 port 35833 ssh2
 Aug  1 07:47:02 linux-rz sshd[7489]: Failed password for invalid user hello from 192.168.200.2 port 37653 ssh2
 Aug  1 07:47:04 linux-rz sshd[7491]: Failed password for invalid user hello from 192.168.200.2 port 37917 ssh2
 Aug  1 07:47:08 linux-rz sshd[7493]: Failed password for invalid user hello from 192.168.200.2 port 41957 ssh2
 Aug  1 07:47:10 linux-rz sshd[7495]: Failed password for invalid user hello from 192.168.200.2 port 39685 ssh2
 Aug  1 07:47:13 linux-rz sshd[7497]: Failed password for root from 192.168.200.2 port 34703 ssh2
 Aug  1 07:47:18 linux-rz sshd[7499]: Failed password for root from 192.168.200.2 port 46671 ssh2
 Aug  1 07:47:20 linux-rz sshd[7501]: Failed password for root from 192.168.200.2 port 39967 ssh2
 Aug  1 07:47:22 linux-rz sshd[7503]: Failed password for root from 192.168.200.2 port 46647 ssh2
 Aug  1 07:47:26 linux-rz sshd...