---
title: 【网安技术面】面试题高频V2版
url: https://mp.weixin.qq.com/s/FSEPuNwLreLQTi54vu3GPg
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:29:21.747316
---

# 【网安技术面】面试题高频V2版

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SV67dJYwaXM3gNoI2FD8JlJpv0yYhoS0lpuwq9w4QU1iaUxgEynSKqsiaXvVyibVibIWfUHjJ3rwLiaUta6HAukkEFFRC1XT3iaD426NYFePmmSSU/0?wx_fmt=jpeg)

# 【网安技术面】面试题高频V2版

原创

繁星01
繁星01

安全君呀

![]()

在小说阅读器中沉浸阅读

点击上方蓝色文字关注↑↑↑↑↑

将安全君呀设为"星标⭐️"

第一时间收到文章更新

**声明: 安全君呀 公众号文章中的技术只做研究之用,禁止用来从事非法用途,如有使用文章中的技术从事非法活动,一切后果由使用者自负,与本公众号无关。**

文章声明：本篇文章内容部分选取网络，如有侵权，请告知删除。

![](https://mmbiz.qpic.cn/mmbiz_png/SV67dJYwaXOysm8QEyA70SyNPy11TbCozeczPkevibmZ1DXQo7Tns43aamZuz6LuAgHkLgFy3jibdh1PibbTA0dbARkjwJE47swicBWBqgTdjtQ/640?from=appmsg&wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/SV67dJYwaXMcm1sf3rSaeWYJE8ypiaaEJxQIMzEFDCL1aW4X3GCsTSUfrHPaZ9kST9z866e1X40hK7Licez5zbenfSCYAr9QKG4DzFiaEEFYLM/640?from=appmsg&wx_fmt=gif)

**前言**

**致每一位正在路上的网安人：**

      网络安全是一个"手比嘴重要"的领域，但面试往往是进入这个领域的第一道门槛。

**0****1**

**Linux 常用的命令**

##

       文件操作（cat显示文件内容、ls显示目录）、网络管理（ifconfig查看IP、netstat查看端口、ping检测连通）、系统信息（whoami查看当前用户、ps查看进程）、文本搜索（grep搜索字符串）以及任务调度（crontab检查定时任务）等核心场景。

**0****2**

**Cookies 和 session 区别**

     Cookie 和 Session 都是客户端与服务器之间保持状态的解决方案

1，存储的位置不同

cookie：存放在客户端，session：存放在服务端。Session 存储的数据比较安全；

2，存储的数据类型不同

两者都是 key-value 的结构，但针对 value 的类型是有差异的，cookie：value 只能是字符串类型，session：value 是 Object 类型；

3，存储的数据大小限制不同

cookie：大小受浏览器的限制，很多是是 4K 的大小， session：理论上受当前内存的限制；

4，生命周期的控制

cookie 的生命周期当浏览器关闭的时候，就消亡了

(1)cookie 的生命周期是累计的，从创建时，就开始计时，20 分钟后，cookie 生命周期结束，

(2)session 的生命周期是间隔的，从创建时，开始计时如在 20 分钟，没有访问 session，那么 session 生命周期被销毁

session 的工作原理？

session 的工作原理是客户端登录完成之后，服务器会创建对应的 session，session 创建完之后，会把 session 的 id 发送给客户端，客户端再存储到浏览器中。这样客户端每次访问服务器时，都会带着 sessionid，服务器拿到 sessionid 之后，在内存找到与之对应的 session ，这样就可以正常工作了。

**0****3**

**Linux 中 PHP 环境**

**Linux 中 PHP 环境，**

**已知**

**disable\_functions=exec,passthrupopen,proc\_open,shell\_exec,system, 请写出两种有可能实现任意命令执行的方式？**

在Linux中，如果`disable_functions`禁用了一些常用的执行外部命令的函数，如`exec`、`passthru`、`proc_open`、`shell_exec`和`system`，那么直接执行任意命令执行（Arbitrary Command Execution，ACE）将会受到限制。然而，攻击者可能会寻找其他方法来绕过这些限制。以下是两种可能绕过这些限制的方法：

1. **利用PHP的反序列化漏洞**

   ： 如果应用程序存在反序列化漏洞，攻击者可能会利用这个漏洞来执行任意代码。例如，如果应用程序反序列化了来自不可信源的PHP对象，攻击者可以构造恶意的PHP对象，其中包含`__destruct`、`__wakeup`或其他魔术方法中的恶意代码。

```
<?php
  // 假设攻击者能够控制$serializedData变量
  $serializedData = 'O:3:"Cmd":2:{s:5:"cmd";s:11:"id;whoami";}';
$object = unserialize($serializedData);
// 如果Cmd类中存在__destruct方法，并且可以执行命令，那么whoami命令将被执行
```

2. **利用PHP的输入/输出流**

   ： PHP提供了多种输入/输出流，这些流可能被用来执行系统命令。例如，如果应用程序使用了`fopen`函数来打开远程文件，并且没有正确地过滤输入，攻击者可能会利用这一点来执行命令。

```
<?php
  // 假设攻击者能够控制$remoteFile变量
  $remoteFile = "php://filter/read=convert.base64-encode/resource=/dev/urandom|base64_decode|sh";
$output = fopen($remoteFile, 'r');
// 如果应用程序没有正确处理这个流，攻击者可能会执行命令
```

请注意，这些方法并不是直接绕过`disable_functions`的限制，而是利用应用程序中的其他漏洞来实现任意命令执行。在实际环境中，攻击者可能会结合多种技术来绕过安全限制。

作为防御措施，开发者应该采取以下措施：

* 避免反序列化不可信的数据。
* 对所有用户输入进行严格的验证和清理。
* 使用安全的编程实践，避免使用不安全的函数。
* 定期更新和打补丁，以修复已知的安全漏洞。
* 使用Web应用防火墙（WAF）来检测和阻止恶意请求。

请记住，安全是一个持续的过程，需要不断地评估和改进。在生产环境中，应该采取多层次的安全措施来保护应用程序。

**0****4**

**常见的中间件**

• **IIS**：PUT漏洞、短文件名猜解、远程代码执行、解析漏洞

• **Apache**：解析漏洞、目录遍历

• **Nginx**：文件解析、目录遍历、CRLF注入、目录穿越

• **Tomcat**：远程代码执行、war后门文件部署

• **JBoss**：反序列化漏洞、war后门文件部署

• **WebLogic**：反序列化漏洞、SSRF任意文件上传、war后门文件部署

• **Apache Shiro：**反序列化漏洞、 Shiro rememberMe（Shiro-550）、Shiro Padding Oracle Attack(Shiro-721)

**0****5**

**蚁剑/菜刀/C刀/冰蝎的相同与不相同之处**

相同：都是用来连接 WebShell 的工具

不同：相比于其他三款，冰蝎有**流量动态加密**。

**0****6**

**Linux 提权有哪些方法**

• Linux 内核漏洞提权

• 低权限用户目录下可被 Root 权限用户调用的脚本提权（SUID）

• 环境变了劫持高权限程序提权

• sudoer 配置文件错误提权

![](https://mmbiz.qpic.cn/mmbiz_gif/vnT4hbaLoX74JddnOszb8qDbTibKeA0BQ13ibicLXNFgfgtQ5k4caRXSLwFibjclTYPvMkciaBachkzMHIse79n0Bdw/640?wx_fmt=gif)

**Tips**

**欢迎大家在下面点赞评论加关注，让我们一起在网安之路越走越远！！！**

**长按****扫描****下方二维码加关注，了解更多网安知识哦！**

![qrcode_for_gh_ecd196afad79_344.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/SV67dJYwaXPIyVSAHRD6CR9hGmW2OxL9XjWcQS7JRTMaJicADML0vzFB3cgqJwcNibibwusCPnDlvjz6sibib9bSqLDtdGib1ITIib8kcFXgtlutX0/640?from=appmsg&wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/SV67dJYwaXNoMgTSQ2TPPMlNO9ib1zwmMkgsoLuVoHiaXFO5PLSuV5mQ1Sj85mq7xyT6wRickuAxic1uYs7FROz2qrMXmX9K9wpXKfenicCibypNk/640?from=appmsg&wx_fmt=gif)

**END**

![图片](https://mmbiz.qpic.cn/mmbiz_gif/cv7xkU9cPaX1dqtBQs6CcuBcVruKFIXQKHnK0iaQY1lRENrqAp2dD2piaqJcyPic3WYTicIjCXDNDCZvicxfvqEUSFQ/640?from=appmsg&wx_fmt=gif#imgIndex=8)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Jr5xjApHb7ECMbxmswyNk1wRx7dW46N9cxxnJcucpV1RPmI4hgjKtIc1j00ZyfBxdAa4r28cfge3qjiaTNHPWEg/0?wx_fmt=png)

安全君呀

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Jr5xjApHb7ECMbxmswyNk1wRx7dW46N9cxxnJcucpV1RPmI4hgjKtIc1j00ZyfBxdAa4r28cfge3qjiaTNHPWEg/0?wx_fmt=png)

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