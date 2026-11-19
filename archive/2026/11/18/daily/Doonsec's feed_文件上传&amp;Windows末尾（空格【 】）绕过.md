---
title: 文件上传&amp;Windows末尾（空格【 】）绕过
url: https://mp.weixin.qq.com/s/lwC7_ibDnxeoCUlpXf1pmw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:42:15.452347
---

# 文件上传&amp;Windows末尾（空格【 】）绕过

# 文件上传&Windows末尾（空格【 】）绕过

原创

建哥聊安全
建哥聊安全

建哥聊安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 后缀名检测与绕过之Windows特性（空格【 】）绕过

# 实验目的

通过本实验，掌握文件上传服务端检测中的后缀名的检测原理以及绕过方法。

# 实验环境

* 操作机：Win10用户名：Administrator密码：Aa123!7890
* 靶机：Apache + PHP
* 实验地址：http://ip/upfile/2/upload4.html

# 实验原理

文件上传从客户端进行检测显然是防护不足的，一些特殊的文件命名方式在Windows下是不被允许的，利用Burp Suite工具抓包修改后缀名，绕过服务端的验证后上传文件，Windows会自动去掉后面添加的。注：此方法只适应于Windows，因为Unix/Linux系统没有这个特性。

# 实验步骤

1、登录操作机，打开浏览器，输入实验地址：http://ip/upfile/2/upload4.html

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGaE69zfCZEwlenrfQjS8McmDojrkpheHH1xP8rreNQLibqtFtiarOY2HZpsLN3tzX9FaWxnSJyNEmOyTW84T8Y5SpqfhJW9gCJg/640?wx_fmt=png&from=appmsg)

2、在操作机上准备要上传的文件（脚本文件），比如新建info.php文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trG7nP5sXbWM7BGadtibjPYNFP6iaZqRKoibKxBia9I5lAuRBMKgFMHWiaE4H2C4moflib5FuBjVY1yPK8vFF5EVBz13T4DB7IH0JyMW8/640?wx_fmt=png&from=appmsg)

3、点击“选择文件”按钮，选中要上传的文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHG8aKnnCCu7iaH6D6JWscQ6IkX5ibhIeibqHKt7cicFMGiaWq2bolja0jks98FcystW3hbiaxYj6kiaNiciankFxZq9C364icwib4ibMQFAMk/640?wx_fmt=png&from=appmsg)

4、点击“submit”按钮，文件上传失败，此文件不允许上传

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFpdD8XnmHQNNZ0rV0xcoN7qhjsO0PbFS0RHvHyJEVIXEtzJKIXPiccphbB0mrxTWYic4KmiaWfBlbDw19yBvrkKTmjj7BIBKa7Pg/640?wx_fmt=png&from=appmsg)

5、尝试利用大小写绕过，将脚本文件info.php更改为info.pHp，以及尝试寻找黑名单列表之外可允许上传的文件后缀名进行绕过，将脚本文件info.php更改为info.php3或者info.phtml，再次选择脚本文件上传，依然失败，此文件不允许上传

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEN23hViaRPK5WaVtjRn7ug3vWXJDWeMmgcl6U7gdlvDlDvStDwOK4PcEleVoibR3ems9libcpDrjGRUxpfs4W0X268UHmCoCMicEo/640?wx_fmt=png&from=appmsg)

6、打开桌面的的“Burp”文件夹，双击“BURP.cmd”启动Burp Suite抓包工具

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFyALcMQVYLuyc2mtYjQdfywRHL0NM5cz1qRDNPqiakWiaUbP0ic8ZyLRrSU4ZjMopwwib9WKVe17hibbVyz3cxkzVjCfY1lq0R4sib0/640?wx_fmt=png&from=appmsg)

7、切换到“Proxy”代理模块的“Options”，查看Bp的代理

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFgfPxMmPMQ4tt0yGmOL14dqm1G8h2wYbCKhrfygXezSCweWkH53ejibFg90f8rklelfXfibWp0KQzkOgAL1zuIQG8JKvUjX7cko/640?wx_fmt=png&from=appmsg)

8、切换到浏览器，选择火狐插件中的代理（配置浏览器的的代理），与Bp的代理一致

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHMSF7HC0MpJ8tibhGQceYX8diarH7bVvs6vgicOziaBotWibYmblic8aA1aLh5lS6RPJkAl0YwRFcN0vaTcibkK3PibyteeuQcRKLZnDA/640?wx_fmt=png&from=appmsg)

9、点击“submit”按钮，再次上传文件，Bp成功抓取数据包

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFLrY0Uh8HDYpvfgCpicAgnQLpjjv8QpD1oGmoe6jrygZibJw5RCDrLiafJXo3to6IVSbYicelRdPXa8DtuYwOU85ZRQ25argPs1Hg/640?wx_fmt=png&from=appmsg)

10、利用Windows特性，给文件名加“.”绕过服务端后缀名的检测，将数据包中的后缀名info.php改为info.php.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEsuOCNfE0BaoTwPNjWEuL5ts8vMLic6rHW6793RzReT4M77n2LicVEdwydZEgOicibfwMfibhE0qJey63h0gxd21LmJdOBNAw1Tdiac/640?wx_fmt=png&from=appmsg)

11、点击“Forward”，转发数据包，切换到浏览器，依然上传失败，后缀名不允许“.”出现

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trED2SyTB8TXHarkx4y4AINCEupny9ZEXJOEzTtVxzpmufogicwdTicU5591Egicd1UUvWofh3G1xMfDuzZb0gDhDeqOxPoVTtR6mE/640?wx_fmt=png&from=appmsg)

12、关闭浏览器代理，重新选择脚本文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFKa81edfB6ehYPrbsL90olyTA4Dff47n1Nwb2sCwcqFbdZGlgt1adTic5GoQD4R63FwqzBJ6jMttRo1xUEhvkMrUo7IBm8ENE0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEsibNibicZjDKxUSCmrCdQ3xr3qzTzL5tomXDPwvsZtnGgTOoQyEfYK3Pewd38POAa8sPTKSI36VZO5fjuiaaA29DibMyiaDzxDuLgo/640?wx_fmt=png&from=appmsg)

13、再次打开浏览器代理，点击“submit”按钮，上传文件并抓取数据包

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHQgwFk8wa2gpnedfJDpvKWgYaRw3ahtDdCW5uGULItibgsyicMjcUCLwuYWL01fmricHfOoic6D1AGnp2nB0UcGPnicC9BfPIiaNAF4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFf0qpq2TH04yIRd4GSjBHbXHkf9FR1bcElXx7b6RySS0SefcwhXvicD7VlvYsY2zEjCibpJm3xeMgyAOictVqIYL4m3Kgwh4oXok/640?wx_fmt=png&from=appmsg)

14、利用Windows特性，给文件名加“（空格）”绕过服务端后缀名的检测，将数据包中的后缀名info.php改为info.php

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFpGWVZa8eKlG9W65zGPHAtIKb1SK0DkUSkygOeGbV7ksPLsoCC8te8bWwofmRDLN6BP8VFXX9N6vJ3mUXSSMicBfzsQRa4x7Zw/640?wx_fmt=png&from=appmsg)

15、点击“Forward”，转发数据包，切换到浏览器，脚本文件成功上传

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHJWblUvlfowPJGuuFr8sSjADZJTzoIOq3jxVhKlTLSERQAEJdW9wClhW6JMGu3SUtVTP9BTkhiadpibVMYjfZgbztGtDXOoDc3w/640?wx_fmt=png&from=appmsg)

16、关闭浏览器代理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGoUHqYslbiaTpjIicBja1Vmfiaw45lkfokMr7tW8CzR5lF1oKPSyjkUk8d3uorMkauMTOich1mIOj0ZdeFzXrjiauicDBK8vDNmNnE8/640?wx_fmt=png&from=appmsg)

17、访问http://ip/upfile/2/upload/info.php （访问http://ip/upfile/2/upload/info.php也可以），上传的脚本文件成功解析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEHstzicNjYulV9ona6n1YNrwgMh1YEQJE68U5X2WJjMebONHCZXjN6mAJAumibicldRgrA9h15Jpdicwt2aMh3ialBhvI25MYcgssw/640?wx_fmt=png&from=appmsg)

# 实验总结

掌握文件上传的服务端检测中的后缀名检测原理，“【 】”在Windows下是不被允许的，利用Burp Suite抓包在文件后缀名处添加“【 】”，绕过服务端的验证后上传文件，Windows会自动去掉后面添加的空格（【 】）。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过