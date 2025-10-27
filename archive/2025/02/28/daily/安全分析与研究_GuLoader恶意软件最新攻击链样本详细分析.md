---
title: GuLoader恶意软件最新攻击链样本详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490797&idx=1&sn=f454227e2ef591427376bad3a05a6b26&chksm=902fb3c5a7583ad37df74f272610ce55a3f4fb02e9e9b5e3c6ba03c22979ad02a84daddc3ed1&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-28
fetch_date: 2025-10-06T20:38:00.060739
---

# GuLoader恶意软件最新攻击链样本详细分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eFibWjTSTDAFO0NypLibOCxnuDAP46tcKsSCTZHLIic3bWoFsA2LDVibgjA/0?wx_fmt=jpeg)

# GuLoader恶意软件最新攻击链样本详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/news/16842

先知社区 作者：熊猫正正

笔者最近逛malware-traffic-analysis网站，发现DBatLoader/GuLoader恶意软件最新攻击链样本，比较有意思，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eMycdXFv5GJfMw6uom4wVsvF7JlyJGzXDOJyp3icPQA4hib7rozSuZT2A/640?wx_fmt=png)

从该网站下载样本之后，对该最新攻击链样本进行了详细分析，分享出来供大家参考学习。

样本分析

1.初始样本是一个包含CVE-2017-0199漏洞的XLS文件，解析OLE里面的流数据，包含一个URL链接，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eicKvf2fuwwzckBKGFMI7lIv9an9aFWWF1I6exGahzQg3TmzzO3bibhhQ/640?wx_fmt=png)

2.由于漏洞，会自动连接下载URL，URL跳转到另外一个URL链接，并下载对应的HTA恶意脚本文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5evBDXN577mPyMSTl1HzkJ68mmYhb6j7JnohIa4l9XnV8tgEZQzMc0Bw/640?wx_fmt=png)

3.下载的HTA恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eJyBUh0ZGWj4pqId4icic1icicRzqhnK1Bcic9iarMsgesaJGv4gn3suP6DLw/640?wx_fmt=png)

4.恶意脚本执行之后，会调用PowerShell执行恶意脚本，恶意脚本的内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eYJZ8Nscq1GvwmIFu6FicaOibStVKTkcGOlpVLAnFr0N5sQibld1jsEdJQ/640?wx_fmt=png)

5.解密PowerShell脚本里面的加密数据，解密之后，该恶意脚本会从远程服务器下载另外一个VBS恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eORiaKw9DPV8PzQeVhFVH9hyY1ufPt7Hjpc6lR14ASq1zpjfxKXzicegQ/640?wx_fmt=png)

6.下载的VBS脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eSItgEcwictHnpHiaPiaKKNLqxzySTjQ4T6yibaPoeXC3S0aRfZsMPGM5BQ/640?wx_fmt=png)

7.解密里面的加密数据代码，解密之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5enOqoicib4y83VndIkRRofw4E0vYiay9ukjVbcp8k4eJJep1znw4JWY4aA/640?wx_fmt=png)

8.解密之后的PowerShell脚本，会从远程服务器下载一个JPG图片，然后解密里面的加密数据，并加载执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5ezzO4AVpsdZkzVrEbjsNM0WhC9purWNU7HoRbw9zOB0xBJYz60LgboQ/640?wx_fmt=png)

9.JPG图片中包含的加密数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eRye9BaNkOjicV7GNdgpjMOPudjn9LkxTI0IYia7Ngia9JgWhiaQRxoD5Cw/640?wx_fmt=png)

10.解密该数据之后是一个PayLoad，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5efW7l4E8dL0wPczfSC1lIODSzmI4cnBxm0bHmSBT5DLhzNypHtCef8w/640?wx_fmt=png)

11.该PayLoad是一个NET程序，样本编译时间为2024年12月13日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eQUhzWhWdiaBiclWHhLXstwNhmtxppRglbOehDQl7fDDaSb5pHIrfZ1Jw/640?wx_fmt=png)

12.通过分析为一个TaskSchedular程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eibLvAXjhiaQ7LDqJicVhJ2IpzSJlaYlcVTicFPdicxcZxFXibw5UodzKQF9Q/640?wx_fmt=png)

开源代码地址：https://github.com/dahall/taskscheduler

13.从远程服务器上下载相关的恶意代码，并加载执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5e59iaRPaVXyh8aRsKo8kWfAGGiaOC3HpKUYNvPvn5oNbkic15tAwFQDPaw/640?wx_fmt=png)

14.通过VIA函数加载下载回来的恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eYNbxvVj9806CicWMThqRwQ9ekyGsn6sC7127TCDic1mnCeYTG9PaZFuw/640?wx_fmt=png)

15.解密远程下载的恶意代码，为一个PayLoad程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5edJLYpoJnicr69BEJP4mftttoEyicpKnialMh1zibH6XlEAjmlrGJNp9K8Q/640?wx_fmt=png)

16.解密出来的PayLoad对受害者主机进行屏幕记录，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5e5J1QM2WWv3OhH9CmJKsO4z36Ag0AJGt6na2JY4qLX9MOiaoAwo62hTQ/640?wx_fmt=png)

17.屏幕截取记录过程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eicnByLNV8bt3Hma28MoCwiaYdmoOiar7Hj8ZZnTOpJs7WQFozKrnUA5Tg/640?wx_fmt=png)

18.获取主机相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eicw7dZxicYCG3qNtCnibWYxyUlEIhic0WtcJGfRZz9RiahicS5MFBOMWAPwg/640?wx_fmt=png)

19.进行键盘记录操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5elBHP032AuyWwpL0tHm0HUZdwrjUmvWNyFiaGd7biaaZSIHGMjNWPbibPA/640?wx_fmt=png)

20.关闭进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5ebVgMVg9BW5PAq5eKJCzORL6pJNkKm1DXKmDl9VeRiafNzLlAwvQQLrA/640?wx_fmt=png)

21.上传受害者信息，到远程FTP服务器，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5ekAKicOOY9BtfR03wQoqnSP03XZEEsC4PqE52O0HZdmlSianQY3fXHhKw/640?wx_fmt=png)

22.上传到远程FTP服务器过程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eDaXoAxj9Fznfw3IfPJicpIrDdqWePXE2CcgMuibiaP52yyW9TrHicmQhvg/640?wx_fmt=png)

23.远程FTP服务器地址ftp://ftp.horeca-bucuresti.ro，FTP远程服务器的用户名和密码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5ezawDtyXey7DtYdOoIZXyeDLwDB8B4vDBaU74cqwrYmoRjcuaVBLePg/640?wx_fmt=png)

24.盗取Thunderbird数据库信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5eowKibrywAWCwfLk4ButL4IYJm3Np5enS61AoYk7xkTNz9Gr0sIwBdow/640?wx_fmt=png)

25.盗取UCBrowser浏览器的登录用户信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5epMuibUia7ewpibdouKl9JXrrhXBToSbfEtWUfdWHeFheNbKYsq76JDVSA/640?wx_fmt=png)

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVEV0cgQqibgjtRzMwEvUD5erXxiafXLY7WfnicHF8Akj64OcJMKPCrB793l8tvknJ8d906ywAdtibU3w/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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