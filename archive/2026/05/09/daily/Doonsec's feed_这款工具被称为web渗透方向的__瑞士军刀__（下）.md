---
title: 这款工具被称为web渗透方向的\"瑞士军刀\"（下）
url: https://mp.weixin.qq.com/s/UxWnCk4LswSOGQTDDeM57w
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:34:50.827285
---

# 这款工具被称为web渗透方向的\"瑞士军刀\"（下）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QJTLZsy5trF79TA9uImMpVibhqwojagic0MxeCZlOdgHyXXj8Mg7VqVxVPGRGmVSTLMTt4vz86zpazcxxiacJic4ZXlXmC4FIibbHsTUDOyhdFVs/0?wx_fmt=jpeg)

# 这款工具被称为web渗透方向的"瑞士军刀"（下）

原创

建哥聊安全
建哥聊安全

建哥聊安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# **免责声明：**严格禁止**对任何未授权系统/网络进行扫描、攻击或入侵。 禁止制作/传播恶意程序，禁止参与任何网络犯罪。如擅自将本文实验技术用于非法用途，一切法律后果及责任由行为人独立承担，与作者无关。**

# **Burpsuite配置使用2**

## **实验目的**

掌握Burpsuite的intruder模块的用法，熟悉利用Burpsuite对HTTP登录凭证进行暴力破解的方法和流程。

## **实验环境**

#### **操作机：Kali2018-TS**

（1）操作系统：Kali Linux 2018.4

（2）登录账号密码：操作系统账号root，密码Sangfor!7890

#### **靶机：A-SQLi-Labs**

（1）操作系统：CentOS 7

（2）安装的应用软件：Apache、MySQL(MariaDB)、PHP；DVWA、SQLi-Labs、Webug3.0漏洞网站环境

（3）登录账号密码：操作系统账号root，密码Sangfor!7890

## **实验原理**

BurpSuite（简称Burp）是基于Java开发的Web安全领域的集成工具，被称为信息安全界的瑞士军刀，它包含Proxy、Intruder、Repeater、Decoder、Comparer等多个模块，模块间通过共享相互传递HTTP/HTTPS消息数据包。
其中，Intruder模块在原始请求数据的基础上，通过修改各种请求参数，以获取不同的请求应答。每一次请求中，Intruder通常会携带一个或多个有效攻击载荷（payload)，在不同的位置进行攻击重放，通过应答数据的比对分析来获得需要的特征数据。

## **实验步骤**

#### **本实验的目标是：利用Burpsuite的Intruder模块对DVWA网站（安全级别为High）的“Brute Force”训练关卡的用户名和密码进行暴力破解。**

#### **1．访问DVWA网站，进入“Brute Force”训练关卡**

（1）正常访问DVWA网站

在操作机Kali2018-TS上启动Firefox浏览器，输入以下URL访问靶机上的DVWA网站：

http://[靶机IP]/dvwa/

（注意大小写）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEficqynRX6HTib7LmkRBt0ibQIzaVBYEWrQDoc7JmcQtzu3d8X95icgD5WqpyM6TVvHa5MELQrrExW7ZKecjegLajDN2Yo05UeG1M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHsOeibIczJC8bwAgHcSogV99iakgjBbAzNGtAgD9sdZzTdBRYTROIemMHicFzpVb6jIbWSXKldeuiaJq41Xm54pKYIvAwfGzhHPr8/640?wx_fmt=png&from=appmsg)

输入用户名admin、密码password登录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trF9n2U75WhnztNno5my5licHfVpeNAvCibaXmxoJNkX0WNQydXcGDUh59OdPmgrAZEmGwp3JBdtFHG1Psiaia2sYP2tWTWOR4E1iauo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFibpnb01nRgbWTaFk1u7XicGuNAJbvyPa532MBibjY9AyouurxI6xNJib5CzWZzXfWjl3W26hrHt9xJriasNzicibKqTLlR24n2eD5cM/640?wx_fmt=png&from=appmsg)

（2）在DVWA网站主页左侧菜单中点击“DVWA Security”，将网站安全级别设置为High：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trED84cHsIrqCvdzu4uNIwvnD6zFlrqIoCR0ysDLTvCcJftX51kV6SFHsuzlUs9GgspPpN0dNKmpSptKZeXslpegDEcQgsP9yVw/640?wx_fmt=png&from=appmsg)

（3）在DVWA网站主页左侧菜单中点击“Brute Force”，进入Brute Force训练关卡：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGspibzYibv8hxTy6E1c6wvGia0x7iclywUz0gyia4XGq1WpAgGI4VnyecsJZ6lRYdMdTpa7LKPHSMEllxxf9iaaOiakwuZRsTa1auMgw/640?wx_fmt=png&from=appmsg)

#### **2．启动Burpsuite并进行代理设置**

（1）启动Burpsuite

在操作机Kali2018-TS上启动Burpsuite：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHCY7je0yP9QSLnUjR2D8LK5ohdsq5vrIEfOFayLYYiaXAykS6b39yibCOnkHBZ03m4zL7qL0r5mARLYqMiaTnTF53e16ZQJU8v2M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHiazJwqYAMo4Wnxewf70MdDewdxwHmiavYcxE89202ib4MiamHt3WBUnf8hf0ibOibZHkDrlAurTCzosOYJZkfC5JR2Ndrv8vXtKZ2Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFOxdaQCuibT3bePEuib8tb3pG86twu1oCUEse0xic24tXHxYfPqFCGuWLeicWo6XXgT2e7hWrGFDR7t6O1uWXxeNAzNH2AYCjTqw0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHPW0XunKVbP2DlQz9vEyWhbCtJDrG6DNzq4EsRGnGPQLG3JDRrsWuFvxqoEm2MSuL89GTGxcNcgRoyRjd9VFDqtp5xdicZl1M0/640?wx_fmt=png&from=appmsg)

（2）设置Burpsuite的代理服务端口

在Burpsuite软件界面上选择选项卡“Proxy”->“Options”，在Proxy Listeners模块下，将Burpsuite的代理服务端口设置为8090。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFoASSgopLIKjZJzqH8oRMnbeBK3mSBKdv0iaqBEJZFdg9kWFLoVwp1B3ibleicNT9JXibBbKiakzVribic1ib0sDictee2pzrjC8R6PbfA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFqSHLXC3icibSsdSibGLk3jeNCaIaUppTct9B715ysREswUFrNTDRo20kk7fPrkQy9NOWGtE3jibWF2Vw0o3DdDicicDb6ZshWBee7o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trE35WG1icIJBYOvjjX0GkIxXObiaxKSGjVKs76a0JMZfialEkyxTBVPWPr3ot8bdCC9rqQbsItgbiblnxD1iaPGWvpeJqIoCV2mibBP0/640?wx_fmt=png&from=appmsg)

（3）开启Burpsuite的代理拦截功能

在Burpsuite软件界面上选择选项卡“Proxy”->“Intercept”，将拦截开关按钮的状态设置为“Intercept is on”。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFq0pFewStnXUHTunUsWFQo77sCYE1ZMKO7BiaPjFXwiaCOhWd6ribnKrYNoLsLWMrNqn3AqsicFAERU233Oic7plleRUjcreDFbkDc/640?wx_fmt=png&from=appmsg)

注意：上述设置完成之后，不要关闭Burpsuite！

#### **3．Firefox浏览器代理设置**

在Firefox浏览器界面，点击菜单按钮，选择“Preferences”:

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGPyvyr46tUG56iaia6KEK7L2dGfhgM97CyQibDa9W0x5GPIrLEeaQbkNHCEY81nwRmtoZEl5fTjuKrwj6iajQ9IrmIHD36ibOqS7OA/640?wx_fmt=png&from=appmsg)

在“General”->“Network Proxy”处点击“Settings”按钮：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEWXKS8CO2TaKYRUAaqWPVUQ3phlMrO0biaQT1IHLuKH1TCjGcCVsFZY0mcjlnX8mAyFJ4mD8eutyNicSQFQgOjO31YEm4U9Gv5A/640?wx_fmt=png&from=appmsg)

在此处设置如下图所示的代理参数，并点击“OK”按钮确认：

代理方式：“Manual Proxy configuration”

HTTP Proxy： 127.0.0.1

Port: 8090

选项“Use this proxy server for all protocols”钩选。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEFbiczyhZcmfbchTmGpiaefsntQnBtiaz7icSyibGwm17zd8ndLmluuP5KqPIiaykGuhkWh3cuJVBlGlZW2IibaW76QTs0XeVlgra0do/640?wx_fmt=png&from=appmsg)

#### **4．利用Burpsuite工具拦截HTTP请求包，并发送至Intruder模块**

回到Firefox浏览器显示的DVWA网站“Brute Force”训练关卡界面，输入用户名1、密码1，然后点击Login按钮：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFicFTaQec2Lw6PIggQM8ibNF7ibtRGoFgAy2drHrUK6hiaREHZgMgnK3W6JCM0xxiaclXLsH9RwFNxVsMlyfSSqUicEM1HlP7Bd9Beg/640?wx_fmt=png&from=appmsg)

此时Burpsuite会拦截到HTTP请求包：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHcMH9NcuE4xPRu9lfHggAWicciaXoqPgqPNMfrmGlzCYsQO1vicMgoEeNrTACicNGmIPpskvXUuPJXBwWVaNEx9ThkygHbbic4begk/640?wx_fmt=png&from=appmsg)

将此HTTP请求包全部选中，单击鼠标右键，在弹出的菜单中选择“Send to intruder”，将此报文发送至Intruder模块：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFdOmuof6uZYO1bn4xoysdPAJ2wNZ4M4WyfUVxHAeaaVgFE40RGEhMPLnCLJFsdWpWngZX531b1KhUwDiazO0G78gTLTY8cKMEE/640?wx_fmt=png&from=appmsg)

#### **5．利用Intruder模块进行暴力破解**

（1）进入选项卡“Intruder”->“Positions”，点击右侧的“Clear $”按钮，将默认选中的爆破位置清空：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGWOr46M4f9zefHicXgjoLowasibBh1zUD7Jw2rhszDfCvuCuoVw6Nib0GdNT1W42EW2Uqmg7vN3SrGqayJm2I6PRFopk4iaicTwa4U/640?wx_fmt=png&from=appmsg)

然后按如下方式指定爆破位置，同时将Attack type设置为“Pitchfork”（草叉模式）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHoWWw83n9m4giaydlHTJ2WJxuOL77FENz0nYlZD1ia1f7g3mbeWsJOdC7EEoMkWGkFRgUJqX1icibZNJaHRRIHia3fKs6HpWcrFNXs/640?wx_fmt=png&from=appmsg)

（2）进入选项卡“Intruder”->“Payloads”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFIEUZAKdwfca3XuGXGVepiaX5N7yIAsoDzWl1esjSFJF8mTy3QQw9UGvotpibuNNgXAtAgKficJkajlIUBOY2qxYyXVibPHQzQZNc/640?wx_fmt=png&from=appmsg)

在此选项卡中设置2个payload set（有效载荷集）：

i）第一个payload set选择Custom iterator类型：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFrC3GdeVI2KqrU95UEvV89ibbHauU70xyhJuZETxC8Y6Jaa240LYzQS5GWPrv1PwN9lOt1R1gO1ITMC2uLENibupeGpEHFxH1ibI/640?wx_fmt=png&from=appmsg)

同时配置3个占位：

第1个占位为用户名的集合：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEfXAjkQ2XNFicibJnNkktFCddoTxILelqpaFW5dM2zcQiadFXoObFONTicjlBMM56NolicNV66B9ic3DMOC0icaoxQhzMdJ3R9LRWgk8/640?wx_fmt=png&from=appmsg)

第2个占位为固定字符串：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGdyxiaAtCC89z3w4kesKylZkaiaxVWnulwPFSWd4JfU5WyKhwiaZqbqiamrYfWn8xbBW4j6IAEzr3vZUbibqSlHFia1bibTnaSAjNdmM/640?wx_fmt=png&from=appmsg)

第3个占位为密码的集合：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEoYNkOcdSQH2332o8ulSSsibbq7shLAK8uep16q4iaA5HQeMiaaZZpsRp30fIK6zeqHTkGPEKhH9PxgjMLXSk3omLcH0qib3MUpUo/640?wx_fmt=png&from=appmsg)

同时，在Payload Encoding处，禁用对=和&进行URL编码：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trF5AzlJQxDMqwgmqqR3O78wS3jRjheEAyOSuZC4KEx7TayaVtUQ3RoNEBf8wIBnv315BaZ5cjqQDvYwX25aCDQqNQGOOwtZdia0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trH97kq5fChrBOOUAKA0OxHh9oblqBWWibBXNdSTeh9b9ZMhFQScXCMAh6Z5NZUDDEcEPVZh6z5fcDSA2bFVJLeMQzZMFuf6mibgA/640?wx_fmt=png&from=appmsg)

ii）第二个payload set选择Recursive grep类型：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFUNcD63AIluCsulicSK0Bib1QXciaD7J0THicVfoA2J6XanGmFsGWVz9yz3wLXOJicmA8HN8YPXfOBic2Wh6xo6RDKEPNpTX8PHBbaU/640?wx_fmt=png&from=appmsg)

（3）进入选项卡“Intruder”->“Options”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGfmcia0tsXDbBEERCgucb71...