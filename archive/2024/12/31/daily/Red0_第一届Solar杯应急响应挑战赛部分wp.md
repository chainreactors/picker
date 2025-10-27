---
title: 第一届Solar杯应急响应挑战赛部分wp
url: https://mp.weixin.qq.com/s?__biz=Mzg3NDY3NjcxOA==&mid=2247484526&idx=1&sn=60e771e45abd48baadd70e3aedd7ec24&chksm=cecc6ceff9bbe5f99880391d5517a818630b0141216ef814dbaa7784d0a745542b045406f79b&scene=58&subscene=0#rd
source: Red0
date: 2024-12-31
fetch_date: 2025-10-06T19:41:13.210463
---

# 第一届Solar杯应急响应挑战赛部分wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16B6Kuzb4UI0OjCaxvbRjGgMMNUcmF7nibhibPrSHcTrvC8gG35KBwic6Slg/0?wx_fmt=jpeg)

# 第一届Solar杯应急响应挑战赛部分wp

Red0

Red0

1、题目描述

题目文件：tomcat-wireshark.zip/web新手运维小王的Geoserver遭到了攻击：黑客疑似删除了webshell后门，小王找到了可能是攻击痕迹的文件但不一定是正确的，请帮他排查一下。flag格式 flag{xxxx}

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BHzibJ5sLUGxZH4JvTlBn6zRJMDNhcNKeFJrgViamhc04iaKOibiblAsX2Aw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BsGdaJcFMv7kNEAe2vIRzib8UUka9FQVXwpeemYHlH6FIribb9lciclGvA/640?wx_fmt=png)

2、题目描述

题目文件：tomcat-wireshark.zip/web新手运维小王的Geoserver遭到了攻击：小王拿到了当时被入侵时的流量，其中一个IP有访问webshell的流量，已提取部分放在了两个pcapng中了。请帮他解密该流量。flag格式 flag{xxxx}

E:\应急比赛\【题目】小题+综合题\solar\tomcat-wireshark\web\apache-tomcat-9.0.96\work\Catalina\localhost\ROOT\org\apache\jsp 可以找到明文webshell，看到加密逻辑是aes加密且给出了密钥

flag{sA4hP\_89dFh\_x09tY\_lL4SI4}

aes解密

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BYfmJGpkgRdibAWU53640RfM7Xj1M7c4JSR3zR5uMLRBFeML7fNAyY4A/640?wx_fmt=png)

3、题目描述

题目文件：tomcat-wireshark.zip/web新手运维小王的Geoserver遭到了攻击：小王拿到了当时被入侵时的流量，黑客疑似通过webshell上传了文件，请看看里面是什么。flag格式 flag{xxxx}

解密出来有个包是里传了flag.pdf

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16B6FqyQiczR7dZEUEhrKHJxgaN1ceL9OrmezhHvCLZzChZIcGljJXMLMg/640?wx_fmt=png)

cyberchef直接保存为文件打开

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BJ3BOmYRZucmglPMRibnAia9OajzliaFTXs0CoY1HTwQuk4THcACYgyrEQ/640?wx_fmt=png)

 flag{dD7g\_jk90\_jnVm\_aPkcs}

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BdUK6LVMl2kLLneFJtIuTwCIlkCgpeAibmboicoft3v1DAepoZ97ZJH7w/640?wx_fmt=png)

4、题目描述

题目附件：mssql、mssql题-备份数据库请找到攻击者创建隐藏账户的时间flag格式 如 flag{2024/01/01 00:00:00}

flag{2024/12/16 15:24:21}

windows日志4720

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BX0icpAK9z42ZxicLfDfqXpqiaYWs5ojCIZQ6flicuOaC8akPXhibOn7tdzQ/640?wx_fmt=png)

5、题目描述

题目附件：mssql、mssql题-备份数据库请找到恶意文件的名称flag格式 如 flag{\*.\*}

flag{xmrig.exe}

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BQv76otO2wHkia6tic0A3vWX2SK0nHicX8vF46D8qVUN1ZpA2rAFhJzKIw/640?wx_fmt=png)

6、题目描述

题目附件：mssql、mssql题-备份数据库请找到恶意文件的外联地址flag格式 如 flag{1.1.1.1}

flag{203.107.45.167}

火绒剑监控

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16Bentya5RelHbAl6oa7ibyuTE9ic2ltQnqsvcCO5RQGoA8IIUVCfsrs53A/640?wx_fmt=png)

7、题目描述

题目附件：mssql、mssql题-备份数据库请修复数据库flag格式 如 flag{xxxxx}

flag{E4r5t5y6Mhgur89g}

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BJ1ycvZLo5FSuuEeMDfcw0m9E3sEBsA6fDZRpL31LxqoiamSWmjrAo1g/640?wx_fmt=png)

8、题目描述

题目附件：mssql、mssql题-备份数据库请提交powershell命令中恶意文件的MD5flag格式 如 flag{xxxxx}

flag{d72000ee7388d7d58960db277a91cc40}

powershell日志发现恶意命令，套娃套了两层base64，最后一层base64解密保存为文件算md5

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BsZezREN5jZcfzNoXFB8eSwVfO6777dc1ZFGnqpqvVucyfsQEd4EibmQ/640?wx_fmt=png)

解密

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BzD8rswwhqbUryARAeQkKc7UyKeEPMZE7ArQdG9nvkX6FyNYNia2wIaQ/640?wx_fmt=png)

base转文件算md5

9、题目描述

题目文件：SERVER-2008-20241220-162057请找到rdp连接的跳板地址flag格式 flag{1.1.1.1}

flag{192.168.60.220}

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16B1Gt2cDZ3HRdC6FZHSclDj22oIz9RgEAiccmicN0pGswCRGJX3JsFNUqw/640?wx_fmt=png)

10、题目描述

题目文件：SERVER-2008-20241220-162057请找到攻击者下载黑客工具的IP地址flag格式 flag{1.1.1.1}

flag{155.94.204.67}

vol导出网络连接

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BreicF7S1BPdnJwJ1ibU0rc33Z5f5CdrM0AlqSwPSEggPOfGdGxxPWsxA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BzUDxNoWHphcxMdaiaVhQdriaIekbibU1xaMthUAsHTpqOicjGHHbqPWrnQ/640?wx_fmt=png)

11、题目描述

题目文件：SERVER-2008-20241220-162057攻击者获取的“FusionManager节点操作系统帐户（业务帐户）”的密码是什么flag格式 flag{xxxx}

flag{GalaxManager\_2012}

文件扫描发现有个pass.txt

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BXdBW9g3u4WOmLJEKpGH9LT9tcmonvc8f5tIQZVNGMxb2ofmyjRXEbA/640?wx_fmt=png)

导出查看

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BY5fAbwuqyBNYw7icXTn0rqRYnoSvRbBmHxjjyNrBUD03BI4cCFJFyRw/640?wx_fmt=png)

12、题目描述

题目文件：SERVER-2008-20241220-162057请找到攻击者创建的用户flag格式 flag{xxxx}

flag{ASP.NET}

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BvZdoTR1ysQ25YbT5qPosvUJ1XiaeibpXy8Rn4nS38eicA0Q5wsbP9bNVw/640?wx_fmt=png)

13、题目描述

题目文件：SERVER-2008-20241220-162057请找到攻击者利用跳板rdp登录的时间flag格式 flag{2024/01/01 00:00:00}

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16B4fJ2eJ5cjnVzvPz5G5b7BgMAh616xahM1xSYaE7tS3VewH8SlMZELg/640?wx_fmt=png)

注意要换一下时区，他的是UTC时区，北京时间是UTC+8

flag{2024/12/21 00:15:34 }

14、题目描述

题目文件：SERVER-2008-20241220-162057请找到攻击者创建的用户的密码哈希值flag格式 flag{XXXX}

flag{5ffe97489cbecle08d0c6339ec39416d}}

![](https://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nJlKG6iaiaR8eF4CBxRuHP16BvZdoTR1ysQ25YbT5qPosvUJ1XiaeibpXy8Rn4nS38eicA0Q5wsbP9bNVw/640?wx_fmt=png)

15、题目描述

本题作为签到题,请给出邮服发件顺序。Received: from mail.da4s8gag.com ([140.143.207.229])by newxmmxszc6-1.qq.com (NewMX) with SMTP id 6010A8ADfor ; Thu, 17 Oct 2024 11:24:01 +0800X-QQ-mid: xmmxszc6-1t1729135441tm9qrjq3kX-QQ-XMRINFO: NgToQqU5s31XQ+vYT/V7+uk=Authentication-Results: mx.qq.com; spf=none smtp.mailfrom=;dkim=none; dmarc=none(permerror) header.from=solar.secReceived: from mail.solar.sec (VM-20-3-centos [127.0.0.1])by mail.da4s8gag.com (Postfix) with ESMTP id 2EF0A60264for ; Thu, 17 Oct 2024 11:24:01 +0800 (CST)Date: Thu, 17 Oct 2024 11:24:01 +0800To: hellosolartest@qq.comFrom: 鍏嬪競缃戜俊Subject:xxxxxxxxxxMessage-Id: <20241017112401.032146@mail.solar.sec>X-Mailer: QQMail 2.xXXXXXXXXXXflag格式为flag{domain1|...|domainN}

GPT秒了

flag{mail.solar.sec|mail.da4s8gag.com|newxmmxszc6-1.qq.com}

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nK24yvrc4jXNQJicTsrAhgLtpntRYWavc6kezOKw5RtfVOBibzsf1s7iaCibTgGKgjuPEZQh0gpfuRuFQ/0?wx_fmt=png)

Red0

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9ic0mFdBia4nK24yvrc4jXNQJicTsrAhgLtpntRYWavc6kezOKw5RtfVOBibzsf1s7iaCibTgGKgjuPEZQh0gpfuRuFQ/0?wx_fmt=png)

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