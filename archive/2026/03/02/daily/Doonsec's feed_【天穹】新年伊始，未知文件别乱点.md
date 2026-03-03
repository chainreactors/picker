---
title: 【天穹】新年伊始，未知文件别乱点
url: https://mp.weixin.qq.com/s/5SjgZA2srvnSWnNWvbURzg
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:10:56.856692
---

# 【天穹】新年伊始，未知文件别乱点

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QSjGzxHEMdtKY8AdkptdFcsAP7jnSUZIVRCV4x7iaJHtGattytfPCHwQbCs1QYEAfNCoAcwicLZUDKvNHuR5kJWnDPLicN8kngic57H97WIXSSo/0?wx_fmt=jpeg)

# 【天穹】新年伊始，未知文件别乱点

星图实验室
星图实验室

奇安信技术研究院

![]()

在小说阅读器中沉浸阅读

# 一、概述

近期，天穹沙箱团队在常规样本狩猎分析工作中，发现 XRed 家族最新变种—一款基于 Delphi 编写的蠕虫病毒，该样本通过伪装成合法软件、多进程落地执行等手段，试图规避安全检测，并实现对受害主机的持久驻留。

# 二、样本信息

* 样本名: SB360.exe
* SHA1: 0dc1b2aa1b7e628c2c85dfda891683dd13af845a
* 文件类型: EXE
* 文件大小: 5.31 MB
* 家族归属: XRed家族
* 报告链接:

  [天穹沙箱分析报告](https://sandbox.qianxin.com/tq/report/toViewReport.do?rid=c107d81046ee7d61c9d4d8cc0ea7702e&sk=68147171)

# 三、样本分析

![](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdtzcyVuCMkU7aRkMxZCWECf9vGnmgia0WloGBEV6vJ5YgUjFLLsI9pkloCE2xUpMmRNmp5fO4m53AJQpvDnU6OREfTNCXIt59as/640?wx_fmt=png&from=appmsg)

图1 样本进程攻击执行链

样本进程 SB360.exe 执行后释放文件 `._cache_SB360.exe`，并将该文件属性修改为隐藏以降低被用户发现的概率，随后立即执行该文件。同时，样本进程通过创建名为 **Synaptics Pointing Device Driver** 的自启动项建立持久化机制，使 Synaptics.exe 在系统启动时自动运行，如图 2 所示。Synaptics.exe 启动后会访问域名 xred[.]mooo[.]com 和 freedns[.]afraid[.]org 进行网络通信，如图 3 所示。

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdvK830ejVBlQicsicok5IAOznhLgfLBdr42h9zGAA0qUjibJVmYRlTibr7CVu8lCTOaOPyz1u4ZPJicPvTd1D8zEojFTnqRNZbpyIQk/640?wx_fmt=png&from=appmsg)

图2 设置 Synaptics 自启动项

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdvnMw5vOcqTq3BPLKbia9KoCmeic6EqKqFhPtEVU1wArrBLvrE4XRWjAeKaAeicFfuCm5qAPSEXJ3ic9MWMKEibtecueB6k93PjFe40/640?wx_fmt=png&from=appmsg)

图3 Synaptics 访问域名

`._cache_SB360.exe` 进程随后释放 HD\_.\_cache\_SB360.exe 和 svchost.exe 文件，并通过创建系统服务的方式运行 svchost.exe，从而间接执行 HD\_.\_cache\_SB360.exe 文件。同时，该进程还设置 `._cache_SB360.exe` 自身以及 **HD\_ls.exe** 为开机自启动程序，并访问域名 qq678833[.]f08[.]87yun[.]club。如图 4、5、6 所示。

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdtJjKsVRoqZAuTsibGbevO6zUDRk3CWurEA9iaWq5mN7nyUTQEE9iayGnKD60wiaHyHuHwvibg7Ibkmjp6ah8sQicPjZdicGBk859pfks/640?wx_fmt=png&from=appmsg)

图4 设置 .\_cache\_SB360.exe 自启动

![alt text](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdthsjROIZShsS7Gr0t9vHXwbxyP0VTjl6Uv7hDGQic7xWhZQuCnWMD8hXK5n223TMgVjVrVIGiaVC0Y7qn5nVqzPcrnpOoxpxhbg/640?wx_fmt=png&from=appmsg)

图5 设置 HD\_ls.exe 自启动

![alt text](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdsefP0x6nu8kglliaYfYw5Pgp3rdibcCzicCNEwWXlaDKC2wzHgvyLjSYCFznRI1EFuyBTY85ruCP1hAZyDCvqiasC98kl8yMOErwU/640?wx_fmt=png&from=appmsg)

图6 .\_cache\_SB360.exe 访问域名

HD\_.\_cache\_SB360.exe 释放并执行 .\_cache\_HD\_.\_cache\_SB360.exe 文件。.\_cache\_HD\_.\_cache\_SB360.exe 进程进一步释放并执行 HD\_.\_cache\_HD\_.\_cache\_SB360.exe 和 GLk.exe 程序。如图 7 所示。

![alt text](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMduK3Ciba0XseVo7rNmF3ib80eKgS5lLAiazkeYvKR2VUs7CoMH0oKaiaXiaNIm9IgZXH5byfNibEjgYJFlTlYhcR8jGP4vv04gnClDns/640?wx_fmt=png&from=appmsg)

图7 创建子进程

HD\_.\_cache\_HD\_.\_cache\_SB360.exe 进程将自身拷贝到 C:\WINDOWS\System32\Abrst.exe 并创建系统服务，访问域名 5614894156aa[.]e1[.]luyouxia[.]net。如图 8、9、10 所示。

![alt text](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdu0vCnwINAib4OpIG8O8Fic8FOTxZHY47UR3ZTicyibnEJmzAck2LKPoSCWV5CsASeibelkcPxWB5ZdUS6gcibztkJgsibiavhU2p4VIz4/640?wx_fmt=png&from=appmsg)

图8 复制自身

![alt text](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdsBPdqFiaHaAfANibHYibvicRplx7asartDu6Z6Z5fClu89XStByXcC8PL1nzgdx59Z3qbEiboRx9LdUJnYxNwn8xlK8Gia3OPcV1neI/640?wx_fmt=png&from=appmsg)

图9 创建系统服务

![alt text](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMduqsOhxCcw4ON6jnib3t7R2lZV1GOGrlm4PhEhlO4gO65cHHGVaoNSzDbxTRErCJicr85xqJengjuj07O3JLialt86Mk46Jyh1xmY/640?wx_fmt=png&from=appmsg)

图10 Abrst.exe 访问域名

GLk.exe 进程会创建系统服务，并利用系统 **svchost.exe** 加载 53727812.bat(实际为 DLL 文件)以实现持久化驻留，并访问域名 kinh[.]xmcxmr[.]com。如图 11、12 所示。

![alt text](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdsr9UhjhOjb4fqxVCpeDLRJBRs0RDfnhPqf1HDMrw2LVuwrVwAHuH7Qp3RbhG6qRgibZqPTCxCmLTeDLiaZHbGVdUakOtUiaIpX18/640?wx_fmt=png&from=appmsg)

图11 加载模块实现持久化

![alt text](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdvRNyqViaws9S6e6jewJZbUGYbnzoBRgzDbYhaPAqWHcw1EJVXTVBxqkmTaGzpOx8yce5ZskWEOXDtFHVYxQqVfVCaRicxVg8rWc/640?wx_fmt=png&from=appmsg)

图12 GLK.exe 访问域名

沙箱报告进程信息部分展示了样本执行过程释放和创建子进程执行的逻辑关系，如图 13 所示。

![alt text](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMduDmhxbYp8QCmICiaHqVRZV5cGna5TH68eIfMljB8vjtN3EiahYJq7GuQ4n7Kypr8WvqOecmkk7xHMBqPa6YEYWW3QaOLCIkMW3I/640?wx_fmt=png&from=appmsg)

图13 样本进程信息

综上分析，该样本在执行后通过多级释放和执行子文件的方式构建了较为复杂的恶意执行链。SB360.exe 作为初始入口程序，通过释放并执行隐藏文件 .\_cache\_SB360.exe 实现后续恶意模块的加载。同时，攻击者利用伪装为系统驱动组件的自启动项 Synaptics Pointing Device Driver 建立初始持久化机制，并通过 Synaptics.exe 与外部域名建立通信。

随后，恶意程序通过持续释放新的可执行文件（如 HD\_.\_cache\_SB360.exe、.\_cache\_HD\_.\_cache\_SB360.exe、GLk.exe 等）逐级扩展其功能，并通过创建系统服务、设置开机自启动等方式实现多重持久化。同时，样本利用 svchost.exe 加载恶意组件以提高隐蔽性，并通过多个动态域名与外部服务器保持通信，从而实现远程控制或后续载荷的下载执行。

# 四、IOC

**恶意文件（MD5）**

```
7f9f21ed23c68b5452945d6595ba589 SB360.exe95eb3a84be9bd0ae9e970f95df889584 ._cache_SB360.exee6602803d2908eb659e19d7bb39a2a8c svchost.exebc83f5c2166951713d82178e0e8bb5a8 Synaptics.exe
```

**恶意IOC**

```
kinh[.]xmcxmr[.]comxred[.]mooo[.]comqq678833[.]f08[.]87yun[.]club
```

**报告链接：[天穹沙箱分析报告](https://sandbox.qianxin.com/tq/report/toViewReport.do?rid=c107d81046ee7d61c9d4d8cc0ea7702e&sk=68147171)**

天穹智能分析平台**（联系我们申请账号）：https://sandbox.qianxin.com**

天穹智能分析平台持续迭代升级，致力于为每一位样本分析人员打造更高效、更智能、更易用的分析平台——这始终是我们不变的初心与追求。

如果您希望深入了解平台功能，或在使用过程中遇到任何问题，欢迎随时联系我们。您的反馈，是我们进步的重要动力！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lG0evzxL96k3J9EIwMqhiacpDHibsxFTCugUuHF9VUnGG5ceic7dILO41pMNfer7OzCyIviaBYAWAZicicVfocuO8HKw/0?wx_fmt=png)

奇安信技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lG0evzxL96k3J9EIwMqhiacpDHibsxFTCugUuHF9VUnGG5ceic7dILO41pMNfer7OzCyIviaBYAWAZicicVfocuO8HKw/0?wx_fmt=png)

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