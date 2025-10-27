---
title: 原创Paper | 某 T 路由器固件解压缩探秘
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650967463&idx=1&sn=b8d987a17c67c069e23c6eeab1b8ab66&chksm=8079cf95b70e4683bb0c8c15e5dba60cb69548708e0d96d4a5193fd1f5a7f9092afa933d88c9&scene=58&subscene=0#rd
source: Seebug漏洞平台
date: 2023-02-16
fetch_date: 2025-10-04T06:46:28.036934
---

# 原创Paper | 某 T 路由器固件解压缩探秘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccP4RzYiaXsibAZhqoiaEibpDrzNPtha5HcSRTOXyK9tjpkKeFaX8z0Yjy4Q/0?wx_fmt=jpeg)

# 原创Paper | 某 T 路由器固件解压缩探秘

原创

404实验室

知道创宇404实验室

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT09IJjs3wGQbICd50va8zMqfnXZfD5LGdibcuOrtia3P4DpMAVfibZ8J4MsbHt0JW20QL8Wh0SO8zpyA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

作者：sn0w\_xxx@知道创宇404实验室
日期：2023年2月15日

**准备工具**

参考资料

1.某T固件

2.某T路由器

3.ida

4.binwalk

5.xz-5.6.2

6.squashfs-tools

7.010 Editor

**开始分析**

参考资料

* ### **固件初始分析**

1.利用binwalk -Me + 固件名提取固件中的文件系统，发现提取失败

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccF5vz0rzm3MuwqvwONGJtXC1cdr1CLusNpfSA9HNkm0TPWDCTrscjCQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccSrn7PiawtJibsyZib1a2cDrW9eQhfwJqtiafibXPs7J2wOGdiac68UyRuXFg/640?wx_fmt=png)

2.使用binwalk -E + 固件名命令查看固件的熵值如下图，熵值接近于1，说明固件可能被加密或者压缩，因此要想得到固件的文件系统，需要寻找其解密或解压的逻辑

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccwibFKG6A9zOLjIaiaia60a2kYaUCp48HTV8licZ1MmcEPFW9kQ4gzEa6gA/640?wx_fmt=png)

* ### **解压逻辑分析**

1.用户通过浏览器访问192.168.0.1，通过密码验证后可以对路由器进行管理

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccdib6CeJzHF0rymmiaZlNbtm3bAtFkXL9DQTRo8QIms0GD0cGU8dib3QibA/640?wx_fmt=png)

并且通过访问链接http://192.168.0.1/goform/telnet可以开启路由器的telnet服务，

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4icicckyOGhljyRk5qM3PbsaRkmaWkAzzibBSflbd6tric78ykfkt5LwFJlHvg/640?wx_fmt=png)

利用路由器默认账号root，默认密码即可远程连接路由器shell

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccmWjKsvwbrjnU1kZNLGFqr0R6B6b0qOYBgdlkfrTenXFXeMzxGOdVeQ/640?wx_fmt=png)

2.利用netstat -anp命令查看路由器端口存活状态，发现80端口由进程ID为1301的httpd程序占用，推测路由器由httpd程序提供web服务，并在/bin下找到httpd程序

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4icicc1x3oEtAm5USrAB9HZOUDcxOkwzn4Sr7h3qtFRQoHIP9kia1KiaWbmuPQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4icicc1STLiaLeibicibuoRxmFrOo2dgxsL8EibXmneLJUsS3Ndn4tMkmCZuTCzhQ/640?wx_fmt=png)

3.通过路由器自带的shell获得httpd文件，通过对历史路由器固件的httpd程序分析，发现路由器web服务启动后，网站主目录为/var/webroot，

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccQvbSzBqgibibIZmO09mN9Fv58LhYkz9eiad6iaibGUThODG7M0xVmB0wkAA/640?wx_fmt=png)

将/bin/httpd文件拷贝至/var/webroot文件下，

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4icicc5IAXHg57Uq5dtKuOpEuuJibFJgiaSuowl6kNQED8BgCKTa1Bsbaq1SKw/640?wx_fmt=png)

即可通过访问url:192.168.0.1/httpd下载得到

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccWVribk97LApqib1IwibmOngdSua4t7JcD46fazJeH6QafUibw0EhsZUUKg/640?wx_fmt=png)

4.对路由器升级时，或者本地提供固件，或者从官网下载需要升级的固件，通过对固件升级逻辑的分析，可以找到固件的解密或解压逻辑

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4icicciaxrXQVQRLHnRnZ8aqREP3ZyqXtkA9YWj2PZZx5rg6HIJyaFEqDmKfg/640?wx_fmt=png)

使用burpsuite在点击固件升级时进行抓包，发现访问的url是http://192.168.0.1/cgi-bin/upgrade，上面找到路由器一般使用/bin/httpd程序提供web服务，所以需要在httpd程序中寻找固件解密或解压逻辑

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccECfuqwdsy93r9ibeAm5uMZK6HELibQZfibgsWGgpJyfTBRkg4c9tqPqlQ/640?wx_fmt=png)

5.使用ida对httpd程序进行逆向，发现httpd进行三项重要工作，即websopen、websload和webslisten

```
```
int __cdecl main(int argc, const char **argv, const char **envp){...  if ( websOpen(webroot, route) >= 0 )  {    if ( websLoad(v11) >= 0 )    {...        if ( g_lan_ip )        {          memset(v18, 0, sizeof(v18));          sprintf(v18, "http://%s:80,http://127.0.0.1:80", &g_lan_ip);          v8 = (void *)sclone(v18);          v6 = stok(v8, ", \t", v16);        }        else        {          v8 = (void *)sclone("http://*:80,https://*:443");          v6 = stok(v8, ", \t", v16);        }        for ( haystack = (char *)v6; haystack; haystack = (char *)stok(0, ", \t,", v16) )        {          if ( !strstr(haystack, "https") && websListen(haystack) < 0 )            return -1;        }...      }...}
```
```

websopen(webroot="/webroot", uri = "/var/route.txt")函数的作用是初始化web服务器，设置默认ip，端口，注册uri接口以及对应的handler处理函数，

```
```
int __fastcall websOpen(int a1, const char *a2){...  websOsOpen();  websRuntimeOpen();  logOpen();  sub_423E40();  socketOpen();...  if ( websOpenRoute() < 0 )    return -1;  websCgiOpen();  websOptionsOpen();  websActionOpen();  websFileOpen();  if ( websOpenAuth(0) < 0 )    return -1;  initWebDefine();  old_main_init();  websFsOpen();  if ( websLoad(a2) < 0 )    return -1;  dword_5389D8 = hashCreate(268);...  for ( i = off_5294B0; *i; i += 2 )  {    v3 = dword_5389D8;    v4 = i[1];    valueString(v6, *i, 0);    hashEnter(v3, v4, v6[0], v6[1], v6[2], v6[3], 0);  }  return 0;}
```
```

参数webroot="/webroot"目录下是路由器的web资源

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccicbSnian1vK256WTb706Rd4zGiauHicvaaUKccUUfzBKYpnGg7jOgHEoEQ/640?wx_fmt=png)

参数uri ="/var/route.txt"文件中访问路由器web服务时的请求接口uri

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccy0sYhlQeB6CyY2otSbGZ4iahNlfV9iaEictAZyWFK9kqDiaUOC3Rwv8h9w/640?wx_fmt=png)

其中 websCgiOpen()、 websOptionsOpen()、 websActionOpen()函数负责对这些uri进行注册

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4icicckPrMsnxy8n0eFBqmufnXwDQjd3uVaJFgelnwk8ImxzHK25MDxZxvyw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccBmzNCBA0h3nAFG2d3MOekEPYLJOoMpXRHyLFu4xictwia4LMibGn3iacwQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4icicc9C5LQ14Kibgibe2xcqPpdHbgv5Q4hIDDibXoJicdwtkzaPibnzFQ5ATgLZQ/640?wx_fmt=png)

其中cgi-bin的handler函数被写入了old\_main\_init的old\_initWebs()函数中，函数名为webs\_\*\*\*\_CGI\_BIN\_Handler，或者通过字符串查找cgi-bin，查找其引用函数，寻找/cgi-bin/upgrade接口，也可以找到webs\_\*\*\*\_CGI\_BIN\_Handler函数，最终发现用于固件升级的处理函数upgrade(a1, (int)a3, a2, 0)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4icicceHwSz0tpibOFXa9DvzXIvycMrR4Uy3LV4uicwx8mR0iaenUdP4ib34OGYw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccqrmbubLBWOu9ic3q2apFHIQVPWQzxvtf1YIvKYrcgOQGpAqyHYqw1qg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccAiat5dG6oG6J062633xQ8WxCZpwgkjtr87QAznUAEVdAgvA3Q1HImrA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccbC9LWtJic27z2AibEhE3ibDt3RMJHDiaicW1Gic9XfYorDgq3EX8ibnUsGZyA/640?wx_fmt=png)

websload(auth="/auth.txt")函数的作用是根据/auth.txt文件，注册起始用户并赋予用户权限

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0G5lZm70CtDtrE4B8e4iciccy79ec5uVkO9uic6YWibMiceFuZqawRKzwic0AxKMTvicOmNBO9t4zK497FA/640?wx_fmt=png)

webload函数如下：

```
```
int __fastcall websLoad(const char *a1){ ...        else if ( smatch(v15, "user") )        {          v12 = 0;          v11 = 0;          v10 = 0;          while ( 1 )          {            v17 = stok(0, " \t\r\n", v27);            if ( !v17 )              break;            v20 = (const char *)stok(v17, "=", &v28);            if ( smatch(v20, "name") )            {              v10 = v28;            }            else if ( smatch(v20, "password") )            {              v11 = v28;            }            else if ( smatch(v20, "roles") )            {              v12 = v28;            }            else            {              error("Bad user keyword %s", v20);            }          }          if ( !websAddUser(v10, v11, v12) )          {            v9 = -1;            break;          }        }        else        {          if ( !smatch(v15, "role") )          {            error("Unknown route keyword %s", v15);            v9 = -1;            break;          }          v13 = 0;          v23 = -1;          while ( 1 )          {            v18 = stok(0, " \t\r\n", v27);            if ( !v18 )              break;            v21 = stok(v18, "=", &v28);            if ( smatch(v21, "name") )            {              v13 = v28;            }            else if ( smatch(v21, "abilities") )            {              sub_42609C(&v23, v28, 0);            }          }          if ( !websAddRole(v13, v23) )          {            v9 = -1;        ...