---
title: 从一次有趣的漏洞分析到一个有趣的php后门
url: https://www.secpulse.com/archives/195883.html
source: 安全脉搏
date: 2023-02-16
fetch_date: 2025-10-04T06:45:06.321784
---

# 从一次有趣的漏洞分析到一个有趣的php后门

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 从一次有趣的漏洞分析到一个有趣的php后门

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-15

8,241

1. 1. 起因

事情的起因很有趣，前几天我正对着电脑发呆的时候，突然有个安全交流群的群友来找我交流一个问题

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431700.png "null")

{width="5.7625in" height="4.3694444444444445in"}

大概的意思就是，他在挖SRC的时候，发现一处资产存在目录遍历漏洞，它通过这个漏洞，找到目标资产使用了一个名为phpmailer的中间件（应该类似于中间件吧），问我有没有办法利用，我查了一下这个组件的漏洞信息。最新的洞似乎截止到6.5.0版本以前

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431702.png "null")

{width="5.763194444444444in" height="1.14375in"}

很不幸，群友这个版本是6.5.1，刚好就不能利用了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431703.png "null")

{width="5.763194444444444in" height="3.3048611111111112in"}

找不到符合版本的洞没关系，抱着学习的心态，我还是看了一下它的历史漏洞成因，不看不知道，看了之后就学到一些好玩的新知识了，这也就是为什么会有这篇文章的原因。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431705.png "null")

{width="5.7659722222222225in" height="1.3611111111111112in"}

1. 1. CVE-2016-10033的简单分析

CVE-2016-10033是Phpmailer出现过的最经典的的漏洞，在本文正式开始之前，我们先来简单分析一下这个漏洞。读者可以到：

https://github.com/opsxcq/exploit-CVE-2016-10033/blob/master/src/class.phpmailer.php

看到phpmailer的代码。这里先开门见山地说，漏洞的成因其实就在mail()函数的第五个参数，只要控制了第五个参数，我们就能进行RCE、文件读取等操作。因此我们先追溯mail()函数：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431706.png "null")

{width="5.763194444444444in" height="2.325in"}

因此我们可以先定位到mailPassthru()这一方法，可以看到，这个方法内部就使用了mail()，maill的第五个参数也就是mailPassthru()的第五个参数。

因此，我们再查看有没有别的地方使用了mailPassthru()，可以找到这个maillSend()方法中使用了mailPassthru()方法，并且第五个参数$params是来自于当前类中的Sender属性

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431707.png "null")

{width="5.760416666666667in" height="3.076388888888889in"}

那我们回溯Sender属性，看看有什么地方可以控制Sender属性。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431710.png "null")

{width="5.767361111111111in" height="3.3194444444444446in"}

这里可以看到，setFrom方法当中，就可以对Sender属性进行赋值

当然，这个漏洞还有一个重点就是对validateAddress()这一方法的绕过，这也是CVE-2016-10033的精彩部分。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431711.png "null")

{width="5.768055555555556in" height="0.8743055555555556in"}

但是它和本文的重点不符，所以我们就不深入分析这块，感兴趣的读者可以拓展阅读：

https://paper.seebug.org/161/

既然知道了Sender这个关键属性是怎么赋值的，接下来我们继续分析mailSend()方法的调用链，可以找到postSend()方法

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-16764317111.png "null")

{width="5.763194444444444in" height="3.8673611111111112in"}

继续看postSend()，最终可以找到send()方法

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431713.png "null")

{width="5.7659722222222225in" height="2.7041666666666666in"}

自此，整个漏洞的传参流程我们就已经分析完了。大体上来说，只要我们用setFrom()方法对Sender属性赋值，再调用send()方法。那么Sender属性的值就会进入到mail()函数的第五个参数中，从而实现RCE。看到这想必很多读者已经对开篇提到的这个mail()函数的第五个参数提起兴趣了，为什么控制了它就能实现RCE呢？这就要提到php 中 mail()函数的实现原理了。

1. 1. 有趣的mail()

mail()函数是php定义的用来发送邮件的函数，其支持的参数如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431714.png "null")

{width="5.759027777777778in" height="3.8534722222222224in"}

为什么一个发送邮件的函数能造成RCE？前人的安研经验已经告诉了我们答案。Php的mail()函数，其底层其实是调用了linux下的sendmail命令。由于sendmail支持一些有趣的参数，这就会造成更大的危害。

①日志写入导致的RCE

接着上面提到的内容来说，我们首先要介绍的是sendmaill的X和O参数，其效果分别为：

**-X logfile ：指定一个文件来记录邮件发送的详细日志**。

-O option=value ：临时设置一个邮件储存的临时位置。

看到这大部分读者应该马上能反应过来，我们能指定文件来储存邮件发送的日志，那不就可以写日志getshell了吗？事实也的确如此。了解这个信息之后，我们再回过头看mail()函数支持的第五个参数：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431715.png "null")

{width="5.590277777777778in" height="0.5833333333333334in"}

没错，我们可以用这个第五个参数来控制sendmail的额外参数，那我们控制X的参数值不就拿下了？我们可以使用如下demo进行测试：

```
<?php

$to = 'La2uR1te@b.c';

$subject = '<?php system("whoami"); ?>'; //你想执行的任意php代码

$message = '<?php system("ls ./"); ?>';//同上

$headers = '';

$addtionparam = '-f La2uR1te@1 -OQueueDirectory=/tmp/
-X/var/www/html/1.php';

//假设我们已知目标站点绝对路径

mail($to, $subject, $message, $headers, $param);

?>
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-16764317151.png "null")

{width="5.7625in" height="1.3444444444444446in"}

比如我在自己的服务器上运行如下代码，我们假设网站根目录是/root/，我们运行一下上述代码看看会发生什么。（在复现的时候确保你已经安装过sendmail，不然没用）。

运行完之后，我们在root目录下确实发现了一个名为testmail.php的文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431716.png "null")

{width="5.7652777777777775in" height="2.129861111111111in"}

我们看看它的内容是什么：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431717.png "null")

{width="5.767361111111111in" height="2.2958333333333334in"}

其实他的内容很多，就是日志文件。但是看箭头指的地方，毫无疑问，我们的代码已经被成功写入了。这时候如果我们再用php来执行这个testmail.php，注意看前后的区别

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-16764317171.png "null")

{width="5.138888888888889in" height="1.1319444444444444in"}

当前用户就是root，当前目录下只有testmail.php和test.php，毫无疑问，我们的恶意代码已经被成功执行了。

综上，如果我们知道目标网站的绝对路径、目标网站是linux环境并且php底层使用sendmail进行发送邮件（默认），那么就可以使用mail()函数来执行写入日志文件的GETSHELL。

②读取配置文件导致的任意文件读取

这个函数好玩的地方不止于此，它还可以用于任意文件读取。我们修改一下上面的demo

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195883-1676431718.png "null")

{width="5.761111111111111in...