---
title: ssh有-J参数指定跳板机
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247487754&idx=1&sn=058b4ddbd21e8ed9aca3dbada175879b&chksm=fab2d235cdc55b232684393f3513765e62e116c18ee16485fe8cbd860c664de8650eab807de4&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2024-11-30
fetch_date: 2025-10-06T19:16:43.264421
---

# ssh有-J参数指定跳板机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPP6jPiaylKggGHgBF4cWhQ4uDZvxfQWLGELXkfQwPuQQ6xqO0TRfGmuMmibeiccHVJl5ZiaBgNn1DUuNg/0?wx_fmt=jpeg)

# ssh有-J参数指定跳板机

原创

沈沉舟

青衣十三楼飞花堂

```
创建: 2024-11-28 11:46
https://scz.617.cn/unix/202411281146.txt
```

ssh后来新增-J参数，可指定跳板机，相当于内置端口转发。-J可指定多个跳板，用逗号分隔。有了-J，若中间用跳板机，不再需要单用-L搞端口转发，不再需要多条命令组合，可合并成一条命令。Win10自带ssh，也支持-J。

比如这种场景，从A->B->C->D，后三者均为sshd，现在想搞SSH Tunnel，最终出口是D，考虑如下命令:

```
ssh -CfNgT24 -D ip_a:port_a user_d@ip_d -p port_d -J user_b@ip_b:port_b,user_c@ip_c:port_c
```

在此过程中根据提示依次输入pass\_b、pass\_c、pass\_d，之后A机侦听"ip\_a:port\_a"，将之当作SOCKS5代理即可。若A是Windows，建议不用-f参数，否则将来无法Ctrl-C打断，只能Process Explorer杀。

若D只支持公私钥登录，考虑如下命令:

```
ssh -CfNgT24 -D ip_a:port_a -i priv_d user_d@ip_d -p port_d -J user_b@ip_b:port_b,user_c@ip_c:port_c
```

上述部分参数简介:

```
-C  Requests compression of all data
-f  Requests ssh to go to background just before command execution.
-N  Do not execute a remote command
-g  Allows remote hosts to connect to local forwarded ports
-T  Disable pseudo-terminal allocation
-4  Forces ssh to use IPv4 addresses only
```

现代ssh可能没有"-2"参数了，默认就是协议版本2。

早些年架SSH Tunnel，若有级联、套娃之类的需求，只能多条命令组合，非常臃肿，有-J后，一条命令完事儿。坏事做尽的人，想必第一时刻发现-J登场，TA们有这种强需求。我们善良之辈，没这种强需求，近日ZZ向我提及，才知晓ssh进步如斯。此外，在寡妇王眼皮子底下，SSH Tunnel并非稳定信道，所以上述信息亦非暗示什么。仅仅FYI。

预览时标签不可点

个人观点，仅供参考

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

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