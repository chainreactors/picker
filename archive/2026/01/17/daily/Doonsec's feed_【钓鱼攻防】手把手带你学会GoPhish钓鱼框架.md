---
title: 【钓鱼攻防】手把手带你学会GoPhish钓鱼框架
url: https://mp.weixin.qq.com/s/q8zU9scFq-L4I-YA-7A8rQ
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:34:04.051026
---

# 【钓鱼攻防】手把手带你学会GoPhish钓鱼框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/v94hWOZcBpxf5ujLrIwurOt7k2PHrAOyJRyhBDFQeYrKic1DL3rEpMA4MVpqqVzP47D8x11X9kOUicOre8VIwgXQ/0?wx_fmt=jpeg)

# 【钓鱼攻防】手把手带你学会GoPhish钓鱼框架

原创

平凡安全
平凡安全

平凡安全

![]()

在小说阅读器中沉浸阅读

**「**蝴蝶再美，终究飞不过沧海**」**

## **「前言」**

网络安全技术学习，承认⾃⼰的弱点不是丑事，只有对原理了然于⼼，才能突破更多的限制。

拥有快速学习能力的安全研究员，是不能有短板的，有的只能是大量的标准板和几块长板。

知识⾯，决定看到的攻击⾯有多⼴；知识链，决定发动的杀伤链有多深。

## **「快速搭建平台Gophish」**

推荐使用Gophish开源项目搭建测试平台，伪造钓鱼页面、发送钓鱼邮件、统计测试效果。

下载安装Gophish

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCKsdqwulA7OQ3ABK8MAMIJciaXUxibpc63jbOkAh2C13KnHDZiakRMyJTg/640?wx_fmt=png&from=appmsg)

解压

修改配置文件：

若需要远程访问后台管理界面，将listen\_url修改为0.0.0.0:3333，端口可自定义。（这项主要针对于部署在服务器上，因为一般的Linux服务器都不会安装可视化桌面，因此需要本地远程访问部署在服务器上的gophish后台）

如果仅通过本地访问，保持127.0.0.1:3333即可

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCw9G1eZibTYiccGx5pqw3s9o2JPCYlKw19o1g8rhoCTzibZqAbVovOogag/640?wx_fmt=png&from=appmsg)

后台运行，目前环境即搭建完成。

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCgz9ctjuibaBSBbchbE0ibqPnzHSODAuFfvCyxkW77g95FYwbOwa170Aw/640?wx_fmt=png&from=appmsg)

访问

可能会提示证书不正确，依次点击高级—继续转到页面，输入默认账密进行登录。

也有可能不是默认密码，在vps启动./gophish之后，会在命令行中给出一个临时密码：

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCp2Whf3TE71SNRcHeuH2k85HqVEY6d0Xe4se1R7mj0ql4eS631OHicKA/640?wx_fmt=png&from=appmsg)

用临时密码登录之后再设置新的密码。

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOC3bia9Gmxlib2X1wf7Av0htIiaN8gAXGEfWkicTsfwaRdfSC4rkfhsBxHEg/640?wx_fmt=png&from=appmsg)

## **「Sending Profiles」**

这个是用来设置发件人的邮箱的

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCaOgrtBRAvHZofv7KWNWDKa6XE9KajEOTLeeZqJx3oiaOz173QmMrsnA/640?wx_fmt=png&from=appmsg)

配置完成后点击send test email来检测配置是否成功

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCWVjAdIG1tr9J6PibZvuAqLz8AShYFN0jQfiaZOWktlwT9g5GCbhchib6g/640?wx_fmt=png&from=appmsg)

某邮箱有授权码机制，所以我们要先进行授权码的获取

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCCtOLnIVuOfcXCLy1HAGZClicUQJNXnh0eXNJiahyniceicHNz0q1GdWSzQ/640?wx_fmt=png&from=appmsg)

某邮箱配置授权码

怎么获取授权码？

先进入设置－》帐户页面找到入口，按照以下流程操作。

（1）点击“开启”

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCL5lTGvHrKQUTiayMY6Ohsm3RZqQQLstOUXtNaHHtiaJsK3O90kic74CbQ/640?wx_fmt=png&from=appmsg)

点击生成授权码

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCy9tI4GwL96hTRgVRITDte82pc5SsQKU9IvA0aEDjKmjc2YVictP6AvA/640?wx_fmt=png&from=appmsg)

将授权码替换password

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCNkzB1BRNYicUibMFobmTMsnNj4uZffcCduARYtJEdI5DbLTibicicWxQoicg/640?wx_fmt=png&from=appmsg)

收到邮件

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOC9pKCFHMyQlJthM8icspQQlL9yR8ib9Dnxbevtqr9xL2T4AH1wN0wdKdA/640?wx_fmt=png&from=appmsg)

python发送测试邮件

效果如下

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOC0Yy4KTDHDZWhSyhAqxv00MibZph433RocRyk75r2maDBSybTUAEdeZQ/640?wx_fmt=png&from=appmsg)

## **「Landing Pages」**

点击New Page新建页面

**「Name:」**

Name 是用于为当前新建的钓鱼页面命名，可以简单命名

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOClWDwq1tlsAy5jNYXGVNiaRXzRF32uwMMJ7wKeu3HsgGwJ0LMbSEYA6w/640?wx_fmt=png&from=appmsg)

**「Import Site:」**

点击Import Site后，填写被伪造网站的URL，再点击Import，即可通过互联网自动抓取被伪造网站的前端代码

这里以伪造XX大学电子邮箱登录界面为例，在Import Site中填写：https://mail.rdyx0.cn/，并点击import

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCTPjJGibUIWIhjsAvPndOpML6hDd1hYibymykCUiaECKDaUcfpjnxqqZFw/640?wx_fmt=png&from=appmsg)

**「内容编辑框：」**

绝大多数情况下，它更偏向于用来辅助第一种方法，即对导入的页面进行源码修改以及预览。删掉蓝色字体。

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCD4uHFYyQsdshmEukwnSkdOkvicxg6ibFmDzMqlicGlEibAib6pj1HnMvrOQ/640?wx_fmt=png&from=appmsg)

由于编码的不同，通常直接通过Import Site导入的网站，其中文部分多少存在乱码现象，这时候就需要查看源码并手动修改过来

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCBeF8LYrMk3dSLOxkEibk7HwYpV5Jop57wGwf7TicUQM8ZY2ZuVeSeSdg/640?wx_fmt=png&from=appmsg)

**「（重点）Capture Submitted Data:」**

当勾选了Capture Submitted Data后，页面会多出一个Capture Passwords的选项，显然是捕获密码。通常，可以选择勾选上以验证账号的可用性。如果仅仅是测试并统计受害用户是否提交数据而不泄露账号隐私，则可以不用勾选

（一般来说，当一个登录页面提交的表单数据与数据库中不一致时，登录页面的URL会被添加上一个出错参数，以提示用户账号或密码出错，所以在Redirect to中，最好填写带出错参数的URL）

因此，令此处的Redirect to的值为：

```
https://mail.rdyx0.cn/login.php?vid=16xxxx486
```

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOClciaWebpND7jusf89uMFFJ6j2DDw7RcHYKwpv06MnKGHQBxRNpib18QQ/640?wx_fmt=png&from=appmsg)

填写好以上参数，点击Save Page，即可保存编辑好的钓鱼页面

## **「Email Templates」**

完成了邮箱配置之后，就可以使用gophish发送邮件了。所以，接下来需要去编写钓鱼邮件的内容

点击New Template新建钓鱼邮件模板，依次介绍填写各个字段

**「Name:」**

同样的，这个字段是对当前新建的钓鱼邮件模板进行命名。可以简单的命名为

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCseb2CeywTJOv9bcTicJWjpC9G0Ujziaq931SJZ5y6XDIlhPFxfSaFfhg/640?wx_fmt=png&from=appmsg)

**「Import Email:」**

gophish为编辑邮件内容提供了两种方式，第一种就是Import Email

用户可以先在自己的邮箱系统中设计好钓鱼邮件，然后发送给自己或其他伙伴，收到设计好的邮件后，打开并选择导出为email文件或者显示邮件原文

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCbNjtdHjpCclJjCT5c0DO4JPkRaG37a19kVc2dLsyA3hre54PoKibYgA/640?wx_fmt=png&from=appmsg)

然后将内容复制到gophish的Import Email中，即可将设计好的钓鱼邮件导入

需要注意，在点击Import之前需要勾选上Change Links to Point to Landing Page，该功能实现了当创建钓鱼事件后，会将邮件中的超链接自动转变为钓鱼网站的URL

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCokDjzVh2J4Gb7vgiapcG99UicXH6dJiaTCgicAYdQHDNXjicAHr6J2V8D7A/640?wx_fmt=png&from=appmsg)

**「Subject:」**

Subject 是邮件的主题，通常为了提高邮件的真实性，需要自己去编造一个吸引人的主题。这里简单填写

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCkWkRt7nmibq801npictibxud2NGxbGVTeXcPnjbbQ3m9RIKWymghla8jg/640?wx_fmt=png&from=appmsg)

**「Add Tracking Image:」**

Add Tracking Image 是在钓鱼邮件末添加一个跟踪图像，用来跟踪受害用户是否打开了收到的钓鱼邮件。默认情况下是勾选的，如果不勾选就无法跟踪到受害用户是否打开了钓鱼邮件

（注：跟踪受害用户是否点击钓鱼链接以及捕捉提交数据不受其影响）

Add Files:

Add Files 是在发送的邮件中添加附件，一是可以添加相关文件提高邮件真实性，二是可以配合免杀木马诱导受害用户下载并打开

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCic6kEOjZpCCKBNssCic565aYZWn9KiaPYyx7ibcPkHmxfnfJIAfFIAyK9A/640?wx_fmt=png&from=appmsg)

当填写完以上字段后，点击Save Template，就能保存当前编辑好的钓鱼邮件模板

## **「Users & Groups」**

当完成上面三个功能的内容编辑，钓鱼准备工作就已经完成了80%，Users & Groups 的作用是将钓鱼的目标邮箱导入gophish中准备发送

点击New Group新建一个钓鱼的目标用户组

**「Name:」**

Name 是为当前新建的用户组命名，这里简单命名

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCQFAC4YxULfRfRdiaKmKgPwmaaCDQJujn42IGlg2xy5zTZoS092eHlYQ/640?wx_fmt=png&from=appmsg)

**「Bulk Import Users:」**

Bulk Import Users是批量导入用户邮箱，它通过上传符合特定模板的CSV文件来批量导入目标用户邮箱

点击旁边灰色字体的Download CSV Template可以下载特定的CSV模板文件。其中，模板文件的Email是必填项，其余的Frist Name 、Last Name、Position可选填

**「Add:」**

除了批量导入目标用户的邮箱，gophish也提供了单个邮箱的导入方法，这对于开始钓鱼前，钓鱼组内部测试十分方便，不需要繁琐的文件上传，直接填写Email即可，同样其余的Frist Name 、Last Name、Position可选填

编辑好目标用户的邮箱后，点击Save Changes即可保存编辑好的目标邮箱保存在gophish中

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCSQia2g1gO1R63ib6eI8UAeY7zQRLO7XibcOiaynwMc5ibTtnlSpec6NpHMA/640?wx_fmt=png&from=appmsg)

## **「Campaigns」**

Campaigns 的作用是将上述四个功能Sending Profiles 、Email Templates 、Landing Pages 、Users & Groups联系起来，并创建钓鱼事件

在Campaigns中，可以新建钓鱼事件，并选择编辑好的钓鱼邮件模板，钓鱼页面，通过配置好的发件邮箱，将钓鱼邮件发送给目标用户组内的所有用户

点击New Campaign新建一个钓鱼事件

**「Name:」**

Name 是为新建的钓鱼事件进行命名，这里简单命名

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCwKJ1O9nX0aLGBWpMZ2oXwOORgibsTTFcY9JtdymydicQmpUYTfU0WOvw/640?wx_fmt=png&from=appmsg)

**「Email Template:」**

Email Template 即钓鱼邮件模板，这里选择刚刚上面编辑好的钓鱼邮件模板

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCDtxoJ2FhuKeCZ36LawV4SurHolQoQFJYmOertZ01tc7AhMOYbvw4AQ/640?wx_fmt=png&from=appmsg)

**「Landing Page:」**

Landing Page 即钓鱼页面，这里选择刚刚上面编辑好的名为钓鱼页面的XX邮箱登录页面的钓鱼页面

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpyAHibhe6hFSnJicdOLh3nlOCNbpfESIcSic3S6e7iciccrROjMsJA3t3UGKOjaNUILktwY00hKsNhz7ag/640?wx_fmt=png&from=appmsg)

**「（重点）URL:」**

URL 是用来替换选定钓鱼邮件模板中超链接的值，该值指向部署了选定钓鱼页面的url网址（这里比较绕，下面具体解释一下，看完解释再来理解这句话）

简单来说，这里的URL需要填写当前运行gophish脚本主机的ip。

因为启动gophish后，gophish默认监听了3333和80端口，其中3333端口是后台管理系统，而80端口就是用来部署钓鱼页面的。

当URL填写了http://主机IP/，并成功创建了当前的钓鱼事件后。gophish...