---
title: 虚假中文版Telegram钓鱼样本详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489156&idx=1&sn=bcc5360565bfdcf676d223630677fe47&chksm=902fb9aca75830baab92b78ff6b6218c191f803ed05f07958398058e4a09a139249f03cbae27&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-10-19
fetch_date: 2025-10-06T18:53:04.672229
---

# 虚假中文版Telegram钓鱼样本详细分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qHDibn4hnXzJbpvAUmo71hEFGAPPmNy0RwbiaNLxnRArG02eGibTp7jdibg/0?wx_fmt=jpeg)

# 虚假中文版Telegram钓鱼样本详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/15863

先知社区 作者：熊猫正正

最近笔者发现一个虚假中文版Telegram钓鱼样本，对该样本母体加载程序进行了详细分析，分享出来供大家参考学习，不要从非官方网站下载安装应用，不然很容易中招。

详细分析

1.样本伪装为Telegram中文版安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qRSEusS744PKOnfQ2eHZCEjqxgXRQic2RmOcLibOtakekjXSClMajb79w/640?wx_fmt=png)

2.解析出安装程序的安装脚本，安装完成之后，会启动目录下的loFsoirtplugLaer.exe程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4q5iaRuLJ0l56oWjdic6pqdYF1wEBh8kDice1WRnRRZ5eyucfJxZaeOAYfw/640?wx_fmt=png)

3.安装完成之后，对应的安装目录文件结构，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qYf6DU4YeUyRuObuKiaL7kZibZHQGT2NKma4rmME10L0okv0nH8HECZUw/640?wx_fmt=png)

4.通过白+黑的方式，利用loFsoirtplugLaer.exe加载恶意模块python36.dll，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qJgibt37rRUnrR2Q6lay9HIUdibrjLUhBNAEAjrRKR3N2SweciaAfEiaOsg/640?wx_fmt=png)

5.恶意模块的数字签名信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qdaeGvo0pWXqa8cZ3707N5hHJIibkksN5BJPOXvpCe5pv8qwTAAib9CUw/640?wx_fmt=png)

6.检测是否存在调试器，反调试操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qSTgDpB6IsdgF1axPvKrZzsSOn1icNqVY1S1vAprSuPckqnpzewt7NIw/640?wx_fmt=png)

7.查询进程信息，反调试操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4q1Qfyxjrp77lPX9529ZibkEHZAdzBwlRKjoq5ziahY8U7ic0rklw6Awq6g/640?wx_fmt=png)

8.通过Sleep、主机内存信息、CPU信息进行反虚拟机操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4q2AOxiboBib61AfdciaLsdk18ibckBMtqRpOkfPGYfiaNxzwA0liblCB9ibt1Q/640?wx_fmt=png)

9.分配相应的内存空间，然后进行相关操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qEGbfDcXg5vAWgibB7fC4Ahx2ZtrYTibgESgKyAJ4kzMlybMADRVQSg2A/640?wx_fmt=png)

10.将加密的数据拷贝到内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qz8iciasOtPiarjcHVicE50KVe4A56Uj2tuZmt7vx9iakNDxFpv7BG36BX3w/640?wx_fmt=png)

11.拷贝完成之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qq9n8NtPYtaFoJ2k92hEvxFRm3NrN5cCicXOqek8av2e1ia7fkVJ0Vwgw/640?wx_fmt=png)

12.异或3A解密加密的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qibuc9wrDl2oibiaYCKFkx7DJITfwbXJ5aTI03MGA7IrDE0VXTufVibftFg/640?wx_fmt=png)

13.解密完成之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qUTRrdSia04JVGv4wkmS5VHXD6rBInvegEnhzhagHNEO3S3KClbtEqhg/640?wx_fmt=png)

14.解密出来的PayLoad导出函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qRzYgTIUDjpbtNXz0e49F8sJ8jhSXFic0GYT957UUbDwvepVFn6p0yIA/640?wx_fmt=png)

15.分配内存空间，将解密出来的PayLoad加载到新分配的内存空间当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qImHniakHME0ewsUPjsSaFAYZmYY8y5XAojJXhemBz407pxia7DUXPkOg/640?wx_fmt=png)

16.执行PayLoad的导出函数run，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qYpib0BpyY5awSo6HnfkjtREguibHsOUZPLVQia7icicpGzw4AhT6F1g99jw/640?wx_fmt=png)

17.判断是否为管理员权限，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qTmhMxAfu0ImbnGRhIo7SVvUjXU0u8HYoYic7n6c66IgeUMESdsWR83A/640?wx_fmt=png)

18.遍历系统中火绒剑、360等安全软件，然后调用驱动，对抗安全软件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qe8ic9QGTEdBmA1qicQ3qWNvcxcggoVkERic2nRIXEU9rSQg8yopmI4gaQ/640?wx_fmt=png)

19.获取本地网络信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qgZQd81s8KUewz1JanNMoFW76qiaXw98f3PnArNOhp5Sc8CEEvJg1lIQ/640?wx_fmt=png)

20.禁用主机网络接口，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qeiafZmNplR12YspZzburWiaa93lXKxCV48MicrsCJAYmcbLXN651gOkVQ/640?wx_fmt=png)

21.在C:\Windows\Temp目录下生成相应的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qcTPp1zm1PK9PpLSEtWIyQHOkIee42RA4wIGTFHEgEibY5DkTCg4KHXA/640?wx_fmt=png)

22.生成的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qiauEK1QNfClzAsOoGDkm52SsohcEic4Su3ibHkgMbkIdsgoUpuZpoXEOQ/640?wx_fmt=png)

23.将生成的文件拷贝到对应的C盘目录下，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qjicsxadWMMWZkYrnaoLfJvo8vWOlL4HG4DPFJczafboVo680ak0W6Sw/640?wx_fmt=png)

24.拷贝之后生成的文件信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qRjic1fUqhj3jnXcjBwLAA5TVv7qeaUkw0gdvVUB4wGJjCKM5es6nu5w/640?wx_fmt=png)

25.然后重新启动网络接口，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qX5mZQdwfv1qaIibRA4fxkvlhYa1qM8XPYUichbjrOZUUMicfDx4uO8MMQ/640?wx_fmt=png)

26.采用白+黑的方式加载恶意模块lum\_sdk32.dll，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qibiabXrS0fROiaefamZ48AntLfWyVI8Y8krYPKcDKEq3hDokqLJayOjsw/640?wx_fmt=png)

27.恶意模块的数字签名信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qsjiciaKPct0LO0iaq9Cd8wYkIGhaiceq7kiaenkSf4pcuGapicEFXXAK1Ekg/640?wx_fmt=png)

28.读取同目录下的文件lum\_sdk32.dll.dat，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qWWZgqLTunl7IeMWkrJNO2Z5eWkyG0JaKfacLTQs7BfoRm1PAfIDMMg/640?wx_fmt=png)

29.将文件中ShellCode代码读取到内存当中，然后调用执行ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qVsd5vgj012ibn7FuaxRbibsYTxgY9UCHBuKVvb2BrcuYsa8D0ia8icY2eQ/640?wx_fmt=png)

30.将ShellCode中加密的数据拷贝到分配的内存，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qNAkCtYaUlMibjNN4446ibj1SUQbficOK5cWAF70gO5pP6j1055H5wU8lw/640?wx_fmt=png)

31.然后异或解密加密的数据，解密之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qpVx3kqSpaicVZOQ8iaI6nK8eHTl4DDIPZjqhnVHxOB5dtMv6ffxUiaIcQ/640?wx_fmt=png)

32.解密出来的PayLoad使用UPX加壳，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qYAMWGXEkeTPvicCMFH0qSoLr0LYv2GXrHKZMMFkoiawCnjfkJ8icl7ZGg/640?wx_fmt=png)

33.执行PayLoad的导出函数run，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qtTVElGS2Lf2Q00mY4EkFxBicfzK0q57N5NicGUZpQYlodeib3c8q60UNA/640?wx_fmt=png)

安装对应的服务进行持久化操作，到此该钓鱼样本母体加载程序就分析完了，应该是某个黑产组织的攻击样本，对受害者进行远控窃密攻击活动。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVe2TA390xPFyPys6ZUnb4qlt5nKiaj2EibTibXSSnyUv1mdfGcaLtNQ6yKicoicxJ0uwhPGbUWPiaUWNOA/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，而且非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

安全分析与研究，专注于全球恶意软件的分析与研究，追踪全球黑客组织攻击活动，欢迎大家持续关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUhMH31lHL5cAbC7FmAV8CpZXC7f6VQtQZNhJbCRRv6YeGO31wpHol0276ydPN5FNd9icELbHl5sdQ/640?wx_fmt=jpeg)

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