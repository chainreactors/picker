---
title: 基于邮箱的域名欺骗攻击（利用解析器绕过访问控制）
url: https://www.4hou.com/posts/ArNz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-27
fetch_date: 2025-10-06T18:02:46.475899
---

# 基于邮箱的域名欺骗攻击（利用解析器绕过访问控制）

基于邮箱的域名欺骗攻击（利用解析器绕过访问控制） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 基于邮箱的域名欺骗攻击（利用解析器绕过访问控制）

盛邦安全
[行业](https://www.4hou.com/category/industry)
2024-08-26 10:14:28

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)61754

收藏

导语：基于邮箱的域名欺骗攻击（利用解析器绕过访问控制）

**0x01 前言**

每年blackhat总是会有一些新奇的攻击思路值得大家学习，在2024年blackhat的议题中发现一篇很有意思的文章，作者提出了一套基于邮箱的欺骗攻击思路，利用RFC标准中对SMTP协议中邮箱地址的特性，提供一系列绕过技巧，我们从中挑选一些实用性较高的思路分享。

**0x02 邮箱欺骗**

**1）邮箱地址注释**

在RFC2822规范中规定了邮件数据格式标准，其中3.2.3章节提到可以对消息头中的内容进行注释，邮件地址属于消息头的一部分，也支持注释，注释符是单括号。

```
zhangsan@webray.com.cn  #正常目标收件箱
zhangsan(xxxxx)@webray.com.cn  #使用括号进行注释
zhangsan(test@gmail.com)@webray.com.cn   #注释中支持任意其它字符
zhangsan@(test@gmail.com)webray.com.cn   #支持在任意未知进行注释
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

![QQ截图20240816100628.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723774246151546.png "1723773988102798.png")

其中=?代表编码开始的位置，utf-8代表后续的字符集类型（其它支持的类型包括utf-8、iso-8859-1等），q代表编码方式的简称（其中q代表Q-Encoding,是一种hex编码方式；b代表Base64-Encoding，是base64编码），?=代表编码结束的位置。

通过对邮件地址进行编码提供了另一种邮件地址表示方式，可以使用github的邮箱验证功能来复现这一特性。在github的settings->emails模块中，添加邮箱地址的base64编码后的值，可以在自己的邮箱正常收到github的邮件。

![QQ截图20240816100613.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723774246732968.png "1723774003205234.png")

单纯通过对邮箱地址的用户名字段进行编码似乎并不足以产生较大的危害，其灵活性似乎还没有上面邮箱注释的方式高。而且在更多场景下，网站获取邮箱域名是直接获取的邮箱地址的末尾的域名。例如用户输入的邮箱地址是zhangsan@webray.com.cn，网站会获取最后的webray.com.cn来进行校验，判断输入邮箱是否属于允许注册的域名，这样的验证无法通过上面两种方式来绕过。

为了应对上面这种场景，作者提出了一种%00截断的方式，通过邮箱编码结合%00截断可以在输入的邮箱地址末尾添加任意字符。如下图所示。

![QQ截图20240816100620.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723774247205442.png "1723774020119551.png")

其中最关键的是在后面添加了=3e（代表右尖括号>）和%00用于截断后面的内容。其中%00可以截断后面的内容应该是属于C语言在字符遍历时的特性，这个很容易理解。前面的右尖括号是什么作用呢？这是因为在SMTP协议头中真实的目的邮箱地址是下面的方式通过左右尖括号的方式来包裹的。

```
RCPT TO:
```

在作者给出的案例中，通过这样的方式可以在github上面认证任意后缀的邮箱地址，如下图所示。

![QQ截图20240816100728.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723774248184822.png "1723774066140851.png")

*那么这样的欺骗攻击有什么用处呢？*

**用于欺骗钓鱼攻击（低危）**

在业务系统中伪造目标内部邮箱域名后缀，增加钓鱼成功率。

**绕过特定域名邮箱注册限制（高危）**

有的重要系统限制了必须是特定域名的邮箱才能注册，通过这样的方式可以绕过系统注册限制。在原文中作者提到有的自建gitlab服务器会限制只允许特定域名后缀的邮箱注册，通过这种方式可以绕过限制，这也应该算是邮箱欺骗攻击的典型应用场景了。

使用github管理员权限登陆，在管理配置中配置允许注册的后缀域名。

![QQ截图20240816100736.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723774248166697.png "1723774081943768.png")

配置之后就使用其它域名后缀的邮箱注册，则会返回禁止注册的错误。

![QQ截图20240816100827.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723774249125424.png "1723774122112666.png")

这个时候可以通过=?utf-8?q?testtest1=40163.com=3e=00?=foo@webray.com.cn对gitlab邮件限制进行欺骗，绕过域名注册限制。

![QQ截图20240816100900.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723774249503859.png "1723774150602163.png")

**0x03 实网体验**

基于邮件地址的域名欺骗攻击是一种新型的攻击思路，在特定场景下能产生重要的作用，但是经过笔者实际测试效果似乎并没有那么好：

* 大多数网站对邮件地址有格式校验，不允许在邮件地址中存在特殊字符。
* 我们测试了python的smtplib、php的phpmailer、java的javax.mail.jar三种语言的常见SMTP发邮件的方式，从测试结果上来看三种方式原生均不支持通过编码的方式来定义收件箱地址。原文中也并没有明确当前主流邮件服务器对编码邮件地址的支持情况。
* github仅有老版本受域名欺骗攻击影响，在最新的gitlab上面进行测试，是不允许对邮箱地址进行编码的。使用编码的域名会返回邮件地址错误。

![QQ截图20240816100929.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723774250149715.png "1723774180753200.png")

也欢迎大家在实际具体业务中多做尝试，肯定能发现其它利用的思路。

**0x04 参考链接**

```
https://portswigger.net/research/splitting-the-email-atom
```

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?G8Gqy7tA)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/9ZO4)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https:/...