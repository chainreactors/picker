---
title: ssh有-J参数指定跳板机
url: https://blog.nsfocus.net/ssh/
source: 绿盟科技技术博客
date: 2024-11-30
fetch_date: 2025-10-06T19:16:17.530038
---

# ssh有-J参数指定跳板机

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# ssh有-J参数指定跳板机

### ssh有-J参数指定跳板机

[2024-11-29](https://blog.nsfocus.net/ssh/ "ssh有-J参数指定跳板机")[绿盟科技](https://blog.nsfocus.net/author/nsfocuser/ "View all posts by 绿盟科技")

阅读： 2,325

ssh后来新增-J参数，可指定跳板机，相当于内置端口转发。-J可指定多个跳板，用逗号分隔。有了-J，若中间用跳板机，不再需要单用-L搞端口转发，不再需要多条命令组合，可合并成一条命令。Win10自带ssh，也支持-J。

比如这种场景，从A->B->C-D，后三者均为sshd，现在想搞SSH Tunnel，最终出口是D，考虑如下命令:

ssh -CfNgT24 -D ip\_a:port\_a user\_d@ip\_d -p port\_d -J user\_b@ip\_b:port\_b,user\_c@ip\_c:port\_c

在此过程中根据提示依次输入pass\_b、pass\_c、pass\_d，之后A机侦听”ip\_a:port\_a”，将之当作SOCKS5代理即可。若A是Windows，建议不用-f参数，否则将来无法Ctrl-C打断，只能Process Explorer杀。

若D只支持公私钥登录，考虑如下命令:

ssh -CfNgT24 -D ip\_a:port\_a -i priv\_d user\_d@ip\_d -p port\_d -J user\_b@ip\_b:port\_b,user\_c@ip\_c:port\_c

上述部分参数简介:

-C Requests compression of all data
-f Requests ssh to go to background just before command execution.
-N Do not execute a remote command
-g Allows remote hosts to connect to local forwarded ports
-T Disable pseudo-terminal allocation
-4 Forces ssh to use IPv4 addresses only

现代ssh可能没有”-2″参数了，默认就是协议版本2。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/weeklyreport202447/)

[Next](https://blog.nsfocus.net/llvm-pass/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)