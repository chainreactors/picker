---
title: 基于邮箱的域名欺骗攻击（利用解析器绕过访问控制）
url: https://mp.weixin.qq.com/s?__biz=MzkyNzcxNTczNA==&mid=2247486653&idx=1&sn=35430337b92bb7aa32d65c2587448944&chksm=c2229444f5551d5299d4a85c3f46371a373d03b308fc082e1d5c98cd19cce865acd6d716152e&scene=58&subscene=0#rd
source: Beacon Tower Lab
date: 2024-08-16
fetch_date: 2025-10-06T18:04:44.734931
---

# 基于邮箱的域名欺骗攻击（利用解析器绕过访问控制）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8ggFjNVoXAo2FBnleqRPqbvuricPDLJCibYIMgpj8rlKhXjvAxbEmKhfA/0?wx_fmt=jpeg)

# 基于邮箱的域名欺骗攻击（利用解析器绕过访问控制）

原创

烽火台实验室

Beacon Tower Lab

**0x01 前言**

每年blackhat总是会有一些新奇的攻击思路值得大家学习，在2024年blackhat的议题中发现一篇很有意思的文章，作者提出了一套基于邮箱的欺骗攻击思路，利用RFC标准中对SMTP协议中邮箱地址的特性，提供一系列绕过技巧，我们从中挑选一些实用性较高的思路分享。

**0x02 邮箱欺骗**

**1）邮箱地址注释**

在RFC2822规范中规定了邮件数据格式标准，其中3.2.3章节提到可以对消息头中的内容进行注释，邮件地址属于消息头的一部分，也支持注释，注释符是单括号。

```
zhangsan@webray.com.cn  #正常目标收件箱zhangsan(xxxxx)@webray.com.cn  #使用括号进行注释zhangsan(test@gmail.com)@webray.com.cn   #注释中支持任意其它字符zhangsan@(test@gmail.com)webray.com.cn   #支持在任意未知进行注释
```

在上面表格中的邮箱地址是属于添加了注释的邮件地址，本质上都是代表zhangsan@webray.com.cn。可以使用python的smtplib库复现了邮件发送过程中的注释功能，如下所示。

```
import smtplibfrom email.mime.text import MIMETextfrom email.utils import formataddr
#发送邮件def send_mail(html,mails_to,title='xxxxxxx'):    ret=True    mails_to_old=mails_to    mails_to=','.join(mails_to)    try:        my_sender='zhangsan@webray.com.cn'        # 邮件内容        msg=MIMEText(html,'html','utf-8')        # 括号里的对应发件人邮箱昵称、发件人邮箱账号        msg['From']=formataddr(["xxx",my_sender])          # 括号里的对应收件人邮箱昵称、收件人邮箱账号        msg['To'] =formataddr(["xxx",mails_to])        # 邮件的主题                   msg['Subject']=title              # 邮件服务器的SMTP地址                  server=smtplib.SMTP_SSL("smtp.target.cn", 465)          # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码        server.login(my_sender, 'yourpassword')        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件        server.sendmail(my_sender,mails_to_old,msg.as_string())          # 关闭连接        server.quit()         # 如果 try 中的语句没有执行，则会执行下面的 ret=False     except Exception as e:        print('发送邮件错误',e)        ret=False    return ret
if __name__ == '__main__':  send_mail("xxxxxxx", ["zhangsan@(test@gmail.com)webray.com.cn"])
```

*那么这样的邮件欺骗的攻击行为有什么用处呢？*

**恶意邮箱注册（低危）**

攻击者只有一个邮件收件箱，但是通过引入不同的注释符在同一个网站注册多个账号。

**认证与鉴权绕过（高危）**

有的网站只允许特定域名进行注册（或者通过用户注册邮箱提取其域名信息），如果对域名数据的获取逻辑存在问题，则可能导致获取到的域名是属于注释中的域名，导致认证与鉴权绕过漏洞。

**2）邮箱地址编码**

在RFC2047规范中规定了邮件传输协议中邮件头的标准，规范中介绍可以使用多种不同的编码方式对邮件头的值进行编码。如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8ZcgIV7mWH0Sy4xWZvhEcVCukYdp6tbWSmibQ268yMJFOZ3CtnNRsVCw/640?wx_fmt=png&from=appmsg)

其中=?代表编码开始的位置，utf-8代表后续的字符集类型（其它支持的类型包括utf-8、iso-8859-1等），q代表编码方式的简称（其中q代表Q-Encoding,是一种hex编码方式；b代表Base64-Encoding，是base64编码），?=代表编码结束的位置。

通过对邮件地址进行编码提供了另一种邮件地址表示方式，可以使用github的邮箱验证功能来复现这一特性。在github的settings->emails模块中，添加邮箱地址的base64编码后的值，可以在自己的邮箱正常收到github的邮件。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8UzIw76rr4w6sI2oibica4Y9c2u7GbacWGI8JaLPHd5gGJaTemYlWLQdw/640?wx_fmt=png&from=appmsg)

单纯通过对邮箱地址的用户名字段进行编码似乎并不足以产生较大的危害，其灵活性似乎还没有上面邮箱注释的方式高。而且在更多场景下，网站获取邮箱域名是直接获取的邮箱地址的末尾的域名。例如用户输入的邮箱地址是zhangsan@webray.com.cn，网站会获取最后的webray.com.cn来进行校验，判断输入邮箱是否属于允许注册的域名，这样的验证无法通过上面两种方式来绕过。

为了应对上面这种场景，作者提出了一种%00截断的方式，通过邮箱编码结合%00截断可以在输入的邮箱地址末尾添加任意字符。如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8kol1Oco1ibED4b7NjNQibONMQgl7jXw0xHhZrmXeYQdM1QGKLCEmO5Dw/640?wx_fmt=png&from=appmsg)

其中最关键的是在后面添加了=3e（代表右尖括号>）和%00用于截断后面的内容。其中%00可以截断后面的内容应该是属于C语言在字符遍历时的特性，这个很容易理解。前面的右尖括号是什么作用呢？这是因为在SMTP协议头中真实的目的邮箱地址是下面的方式通过左右尖括号的方式来包裹的。

```
RCPT TO:<zhangsan@webray.com.cn>
```

在作者给出的案例中，通过这样的方式可以在github上面认证任意后缀的邮箱地址，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8uBW8uoq3gn5l5QSWeok6DNibEbLAmCYYAtjWUznicAuxBAfumuExbThw/640?wx_fmt=png&from=appmsg)

*那么这样的欺骗攻击有什么用处呢？*

**用于欺骗钓鱼攻击（低危）**

在业务系统中伪造目标内部邮箱域名后缀，增加钓鱼成功率。

**绕过特定域名邮箱注册限制（高危）**

有的重要系统限制了必须是特定域名的邮箱才能注册，通过这样的方式可以绕过系统注册限制。在原文中作者提到有的自建gitlab服务器会限制只允许特定域名后缀的邮箱注册，通过这种方式可以绕过限制，这也应该算是邮箱欺骗攻击的典型应用场景了。

使用github管理员权限登陆，在管理配置中配置允许注册的后缀域名。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8zoLXTZkicY7jVNInH1Vz7d3BRgSibgygciaibID68M4bawq5babPhBF0sg/640?wx_fmt=png&from=appmsg)

配置之后就使用其它域名后缀的邮箱注册，则会返回禁止注册的错误。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8nFzcNOTX7beltxHhrLgNpkcz2V5tWVSFvxdaKBHemCiaibMXmC2KPmKQ/640?wx_fmt=png&from=appmsg)

这个时候可以通过=?utf-8?q?testtest1=40163.com=3e=00?=foo@webray.com.cn对gitlab邮件限制进行欺骗，绕过域名注册限制。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8Y9nMAVI1oziaac7xro491W8M4ibAgD3omF5K41Txpan8Wzq2hLad6DhQ/640?wx_fmt=png&from=appmsg)

**0x0 3实网体验**

基于邮件地址的域名欺骗攻击是一种新型的攻击思路，在特定场景下能产生重要的作用，但是经过笔者实际测试效果似乎并没有那么好：

* 大多数网站对邮件地址有格式校验，不允许在邮件地址中存在特殊字符。
* 我们测试了python的smtplib、php的phpmailer、java的javax.mail.jar三种语言的常见SMTP发邮件的方式，从测试结果上来看三种方式原生均不支持通过编码的方式来定义收件箱地址。原文中也并没有明确当前主流邮件服务器对编码邮件地址的支持情况。
* github仅有老版本受域名欺骗攻击影响，在最新的gitlab上面进行测试，是不允许对邮箱地址进行编码的。使用编码的域名会返回邮件地址错误。

![](https://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeANsdC5fLJ01Ebqaoam8UPz8VB6qYsXph6wJekwBhhS6TBlYia0AAo2B7XPeaGnD7pr1AYpenIZyYZA/640?wx_fmt=png&from=appmsg)

也欢迎大家在实际具体业务中多做尝试，肯定能发现其它利用的思路。

**0x04 参考链接**

```
https://portswigger.net/research/splitting-the-email-atom
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAPuXuLlzxV94SmGrdhm12Xoib8pv5tVryyDTMZPUwvOeXrHV2ygdoKrKJQ1u618rmXbhfhiaw8icr5Lw/0?wx_fmt=png)

Beacon Tower Lab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8E5sfrfkeAPuXuLlzxV94SmGrdhm12Xoib8pv5tVryyDTMZPUwvOeXrHV2ygdoKrKJQ1u618rmXbhfhiaw8icr5Lw/0?wx_fmt=png)

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