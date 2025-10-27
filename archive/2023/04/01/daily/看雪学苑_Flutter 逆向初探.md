---
title: Flutter 逆向初探
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458500574&idx=1&sn=06344a7d18a72530077fbc8f93a40d8f&chksm=b18e8d5486f904424874d7308e840523ebfb2db20811d99e4b0249d42fa8e38c4e80c3f622c6&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-04-01
fetch_date: 2025-10-04T11:22:33.875020
---

# Flutter 逆向初探

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ETRoCScGHH55IwbOU6syQibzm2Gfj9wsZKIibYcHxjUKWbwmek8dqrahLPEfF74icOj4Ko29L4xRZdg/0?wx_fmt=jpeg)

# Flutter 逆向初探

Mr\_Holiday[译]

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ETRoCScGHH55IwbOU6syQibGE5Eeh6A5PHKK2uUDLS1PlibqC2rxwtrfpPCFwPcAMSA367icsZv8tHQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：Mr\_Holiday[译]

最近看了很多flutter逆向绕过SSL验证的文章，发现有些细节比较模糊，新接触flutter的师傅们可能不太理解，所以搜到原文进行翻译加上自己的理解，简单梳理了下整个方法和逻辑。

#

#

```
一

Flutter简介
```

Flutter是Google构建在开源的Dart VM之上，使用Dart语言开发的移动应用开发框架，可以帮助开发者使用一套Dart代码就能快速在移动iOS 、Android上构建高质量的原生用户界面，同时还支持开发Web和桌面应用。

#

#

```
二

Flutter特征
```

在逆向分析前，我们首先要确定测试目标是否用Flutter开发的。当使用Flutter构建Android APP时，lib文件夹下的每个受支持的架构下会出现两个库：libapp.so和libflutter.so，如下图所示。如果出现这两个特殊的库，那可以判定这个APP是有部分或全部使用Flutter开发的。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg80C5vgryUzkTfLS32FseAEiclj5CJGrK49EP5JibAAXoHSH6oGUibzXgmg/640?wx_fmt=jpeg)

#

#

```
三

逆向Flutter解决HTTPS抓包问题
```

应用市场上有些APP核心的业务逻辑代码使用了Flutter开发，实际测试过程中发现无法使用Burpsuite、Charles等工具拦截相关的请求数据包。这是因为Dart使用Mozilla的NSS库生成并编译自己的Keystore，导致我们不能通过将代理CA添加到系统CA存储的方式来绕过SSL验证。

我们可以通过一个小实验复现上面提到的场景，目标APP主页面包括了三个按钮：HTTP Request, HTTPS Request and Pinned Request，分别用来测试拦截三种类型的请求。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8IZJnq6cKGKHstDF3ADpoBcCuahkQImM75bPMGKzleOQxbKW6Z4P1Vw/640?wx_fmt=jpeg)
其中的HTTP和HTTPS是通过HTTPClient类的getUrl方式发送指定请求，Pinned Request是通过使用Dio包执行SSLPinning，发送HTTPS请求并验证证书。主要的实现逻辑如下所示:
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8WuBSv0pRRInyWibsibb6zpPAexAbLtrNugEMuljrZneewYlZPYOqbNmw/640?wx_fmt=jpeg)
首先像抓包Android APP一样拦截Flutter的请求包，但会发现三种请求都无法被拦截，因为Flutter APP默认情况下不使用系统的代理设置，所以可以使用Drony + BurpSuite，将手机上的目标APP的流量都重定向到Drony自身，再转发到BurpSuite上。发现只能拦截到HTTP请求，如下图所示。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8rZibMv4e0SzDD47F9Ymy02IPwf19r7cEia5DOVBjZpQGX54SQxwy23JA/640?wx_fmt=jpeg)
发送HTTPS和HTTPS (Pinned) 请求失败，可以用logcat看到相关报错信息，这部分我们之后分析：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8ANWuLbsjdldCl2KVkiaj9BW201ZZFUW4KwmPuichhzpfJHbP0GYicVxpw/640?wx_fmt=jpeg)
接下来就是通过逆向来绕过证书链校验，目前有两种方法可以解决这类场景：

1) 使用reFlutter开源逆向分析工具；

2) 使用Frida脚本hook libflutter.so中的函数。

**1. 使用reFlutter开源逆向分析工具**

reFlutter框架使用了已编译且重新封装的Flutter库来帮助广大研究人员对Flutter APP进行逆向工程分析，通过socket.cc可以执行流量拦截和监控。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8kl4z4VBRloKb8SAv4VI2ibrxLO7wNOYK5b3jawkiaFYgb5nn1wy085Hg/640?wx_fmt=jpeg)
首先PC端命令行安装reFlutter：pip3 install reflutter。装完输入命令：reflutter flutter\_ssl\_pinning\_bypass\_lab\_android.apk。选择[1]流量监控和拦截，输入PC端的IP地址后，将获取到release.RE.apk，但此apk尚未签名，需要我们手动签名。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8t4TtgUm2NhtLqbB1cBolvboUEqNmP4icb0GsrbIkGB8akj8Wic6YlvDQ/640?wx_fmt=jpeg)
通过MT管理器或者uber-apk-signer jar签名，这里使用后者。输入命令：java -jar uber-apk-signer-1.2.1.jar --apk release.RE.apk。然后将重签名的apk安装到真机或者模拟器上。

下一步我们需要按照之前reFlutter的提示，设置BurpSuite的代理，端口为8083，绑定所有地址，并且勾选支持不可见代理，使非代理意识的客户端直接连接到侦听器。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8hEGRSicEHOO6ckPuicN6vpia01mNPdoClcQ9m4VoQKg9mrvo8jUfhf3Qg/640?wx_fmt=jpeg)
设置Drony的wifi代理主机名端口和BurpSuite一致。

完成以上步骤，点击Flutter APP的三种请求按钮，发现Burpsuite已经拦截到HTTPS请求和Pinned HTTPS请求。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8QqiaMAZtVzS3SsZE8iaNrmPMIZgbp77bTXQY1mjeWVYsNcUUGs3ns1gA/640?wx_fmt=jpeg)
使用reFlutter框架拦截HTTPS流量比较简单易上手，但是存在一个很大的弊端，就是需要重打包app，导致它的局限性较大，因为现在的应用市场很多Flutter APP是做了防二次打包的，虽然可以直接替换私有目录的libflutter.so，但需要root，很多APP也会检测root。对于这些防护倒是可以使用frida框架绕过签名校验和root代码，但这样也增加了攻击成本。

**2. 使用Frida脚本hook libflutter.so中的函数**

当无法拦截HTTPS请求时，我们通过logcat查看日志发现错误被触发的位置是[handshake.cc:393]，而Handshake.cc是BoringSSL库的一部分，包含执行证书验证的逻辑。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg89ZV6wTqF2zu6Wscc1FvxJKR1j9G69g668HbVS2u76ibxShVgmiaep9aw/640?wx_fmt=jpeg)
因为BoringSSL是开源的，很容易就可以查到如下所示的393行代码段，其中的ret指的是SSL校验结果（验证通过是ssl\_verify\_ok），这段代码表示如果结果是ssl\_verify\_invalid，则报错提醒。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8xv1JT7ye4DIicLJ09AQBF1nYKmhb2jKw3oQHQTUvYC1HzjXLK4BgmRw/640?wx_fmt=jpeg)
这个判断逻辑是处于ssl\_verify\_peer\_cert函数中的，这个函数最后会return ret。那么如果直接hook这个函数修改ret的值为ssl\_verify\_ok可以绕过SSL验证吗？答案是否定的。因为最有可能采用的代码路径是，注册了一个自定义验证回调，使得368行返回true，而在第369行执行的回调返回ssl\_verify\_invalid。然后代码跳转到392行，ret变量赋值为ssl\_verify\_invalid，因此在ssl\_verify\_peer\_cert函数return ret之前就会显示警报（393-394行）。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8pxMIl73Q0vsrUwSveuFsuQMiaN3r92YpUFIdccAC0yz8WpCVOiawcRHA/640?wx_fmt=jpeg)
继续观察上下文环境寻找更好hook的函数，发现Handshake.cc的386行代码段是验证链的方法的实际部分。这行的session\_verify\_cert\_chain函数实际是在ssl\_x509.cc的第361行定义，此函数返回布尔值类型，如果hook这个函数，修改返回值为true，则386行的ret为ssl\_verify\_ok。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8FNplI8omBiaQCS8DVK5ejdw6FYrUic6f6nUVclbAYJQmYwtMXSdCFI5Q/640?wx_fmt=jpeg)
锁定hook的目标函数后，我们现在需要在libflutter.so中找到它。找到session\_verify\_cert\_chain函数唯一性的特征方便后续IDA中定位该函数，如[ssl\_client]或[ssl\_server]。将libflutter.so导入IDA，使用Search -> Find Strings搜索关键词[ssl\_client]，发现有4处交叉引用。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8nlR3QLiaYbm9PNCDuVMPJfFTKnhKrG5cVViauk7JRJgwthyMJvPh47fQ/640?wx_fmt=jpeg)
第二处和第三处都是Function sub\_3B1834中的，跳转到函数调用位置。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8jVO6nAPfEbHu5D8DDHWBCWPnVMZvMwPsVHaPLxJjjpsicl1VEdy7ajQ/640?wx_fmt=jpeg)
F5检查是不是目标函数，点击sub\_7F4B14，查看代码逻辑与ssl\_x509.cc中389行一致，确定是目标。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8H5BtcW9ibTpaqwibOw1t0J4PrrXCq7icpNQwsiaHGvYLMHkKxX068zkKew/640?wx_fmt=jpeg)
这时我们计算这个函数与其中一个导出函数的偏移量，并将它hook。可以复制函数的前10个以上的字节，之后利用frida编写的脚本检查该模式出现的频率。如果它只发生一次，说明找到了函数，可以hook它。首先在IDA中的Options->General->Number of opcode bytes 设置为4，定位到sub\_3B1834起始位置，复制前10个以上的字节。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8H9gSTFvZmXu0iaj7z2J8xiciaO4hUIiccHXibhxxSMGxOPouD714BqdxSXA/640?wx_fmt=jpeg)

接下来就是编写frida的脚本，使用之前复制的字节定位，在运行时使用Interceptor将返回值更改为1 (true)，这样就实现了绕过证书链检查拦截HTTPS和HTTPS(Pinned)的请求，代码如下所示。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8YuVwybibhLlMOFr3dPxRwdzREGaaoz9uG7kiaBgrn9QN2KPjXuucBeeg/640?wx_fmt=jpeg)
其中注释说明的地址要add 0x01是因为在32位ARM上, 对于ARM函数, 此地址的最低有效位必须设置为0, 对于Thumb函数, 此地址必须设置为1。因为我们这里hook的libflutter.so是64位的，地址不需要再加1。

使用frida命令frida -U -l XXX.js -f com.xxx.xxx --no-pause执行脚本，发送HTTP/HTTPS/HTTPS (Pinned)三种请求，终端打印绕过证书链检查的日志。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8oQQGMpdibjCQcCdQxUn3gf3NAqFKRTwm9e4hrh2v4OPeDKC5CAUY5Dw/640?wx_fmt=jpeg)
Flutter客户端界面显示请求成功。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg82qGy2bxDDiau582ruGUsnt8hicXKJyqbvBToMVaXWpL8n6OAS18g0akg/640?wx_fmt=jpeg)
并且Burpsuite也可以拦截所有请求。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg87K3nGTj5Y5x9cQib5pia270JuhQQDpiaxNmUZ98aB131N0iaBqWNwzrRFQ/640?wx_fmt=jpeg)
如果将hook目标函数的前10多个字节找到规律部分使用通配符代替，上面的脚本会适用于大多数的Flutter APP，有兴趣的师傅们可以自己试试。

#

#

# **参考**

# *https://l33t-en0ugh.gitbook.io/infosec/android-pentesting/bypass-ssl-pinning-for-flutter-apps-using-reflutter-framework*

# *https://blog.nviso.eu/2020/05/20/intercepting-flutter-traffic-on-android-x64/*

# *https://blog.nviso.eu/2022/08/18/intercept-flutter-traffic-on-ios-and-android-http-https-dio-pinning/*

# *https://github.com/google/boringssl/blob/master/ssl/ssl\_x509.cc*

# *https://github.com/google/boringssl/blob/master/ssl/handshake.cc*

# *https://github.com/google/boringssl/blob/master/include/openssl/err.h*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8kh90ib9zV56eG288aia2Mc371jUbqMbpSTOojWwgnTNJk8rPVObFmzvA/640?wx_fmt=png)

**看雪ID：Mr\_Holiday**

https://bbs.kanxue.com/user-home-971971.htm

\*本文由看雪论坛 Mr\_Holiday 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FJjl92zYviaHbyrEZEZzyZFOjibI9RsDgTicPv5dSuE7FmbcRjV9sn7Y7qDnx1icFuO45cIj22DLEZDQ/640?wx_fmt=png)](http://mp.weix...