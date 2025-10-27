---
title: Linux爆出9.9分高危安全漏洞 暂无漏洞补丁且已存在十多年
url: https://mp.weixin.qq.com/s?__biz=MzUyMDQ4OTkyMg==&mid=2247542901&idx=2&sn=2133da115eacf4e2a0d2e2c9206b1cff&chksm=f9ebf6d8ce9c7fce557fe7aca4c1671c15110094e6d07863cda92cecefef7aac440653b8ccba&scene=58&subscene=0#rd
source: 安全419
date: 2024-10-01
fetch_date: 2025-10-06T18:53:54.716653
---

# Linux爆出9.9分高危安全漏洞 暂无漏洞补丁且已存在十多年

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9lmiax2vemgj17fLZbd1n9LkibUlM1iayUvuryydLaT6G4B2TPiaibRusGnRxYQ28iazPQQjibvUZlUbMMICkibMFgqPuQ/0?wx_fmt=jpeg)

# Linux爆出9.9分高危安全漏洞 暂无漏洞补丁且已存在十多年

原创

安全419

安全419

据外媒报道，最近一名叫Simone Margaritelli研究人员在Twitter/X上发出警告，称在Linux系统中发现了一个严重的安全漏洞。并表示这是一个影响所有Linux系统的CVSS 9.9级漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/9lmiax2vemgj17fLZbd1n9LkibUlM1iayUvFADeOmuNiaVUIhiaTuVzW9CGLzsmLkG1krs9KlCYpe9JUVria9Z4FHrRA/640?wx_fmt=png&from=appmsg)

实际上，我们注意到，该Linux系统的安全漏洞，涉及到Common Unix Printing System（CUPS）。这个漏洞允许远程攻击者在满足特定条件下执行命令。CUPS是一个在Linux和其他类Unix系统中广泛使用的开源打印系统。漏洞主要存在于CUPS的cups-browsed守护进程中，该进程用于自动安装在本地网络上发现的打印机。

这里的诡异之处在于，这个传入请求可以包含作为IPP打印机驱动程序信息来源的任意URL。该IPP数据没有经过过滤，从而允许攻击者上传任意信息并创建文件。最糟糕的是，foomatic-rip驱动程序包含一个功能，即在打印过程中运行shell命令。

虽然这个漏洞的CVSS评分为9.9，但实际上它需要用户与恶意打印机进行交互，比如发送打印任务，才能触发代码执行。这意味着，如果用户的系统没有连接到互联网，或者没有启用cups-browsed服务，那么这个漏洞就不会被利用。但是，该漏洞已然引起了广泛关注，目前已有超过100,000个系统暴露了UDP端口631和cups-browsed服务到互联网。

目前，虽然没有针对这个漏洞的补丁，但是有一些缓解措施可以采取。用户可以禁用或移除cups-browsed服务，更新CUPS安装，以便在安全更新可用时引入安全更新，或者阻止对UDP端口631的访问，并考虑关闭DNS-SD。

此外，Red Hat已发布通知，提供了检查系统是否存在此问题的方法，并提醒用户不要将CUPS暴露到互联网。

**用户可执行以下命令来检查自身的Linux系统是否收到这个漏洞的影响：**

**bash**

sudo systemctl status cups-browsed

如果输出显示“631/udp open|filtered ipp”，则可能需要采取行动。可以使用nmap工具来远程检查机器是否暴露了这个服务：

**bash**

sudo nmap -sU -p 631 -v ip.address.of.machine

目前已经有概念验证（PoC）的代码泄露，因此建议用户检查并关闭任何暴露此服务的系统。

![](https://mmbiz.qpic.cn/mmbiz_png/9lmiax2vemgj17fLZbd1n9LkibUlM1iayUvYJiaSUd6LibWoChltvGcPsE3CsWWj8ku9gwLBNzAByofenJZdOOEhJ0A/640?wx_fmt=png&from=appmsg)

需要注意的是，这个漏洞并不是新发现的，它已经存在了十多年，影响几乎所有的GNU/Linux发行版。目前还没有修复补丁，但是可以通过上述措施来缓解风险。

编译来源：

https://hackaday.com/2024/09/27/this-week-in-security-password-sanity-tank-hacking-and-the-mystery-9-9/

END

![](https://mmbiz.qpic.cn/mmbiz_gif/9lmiax2vemgjicH5zTglS9tytC3OUDlpYyJFBXrv87TJ3PhhPumxFRRia7EepckKLTqxXvPwM4lq2yib0PYISe68ibQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

‍

![](https://mmbiz.qpic.cn/mmbiz_jpg/9lmiax2vemgjicH5zTglS9tytC3OUDlpYy1duzA8wmNQEXnvvicpfPb1iag5qpx3dBic5Qic3xcia2aWNQrpaiabyRCRxw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**粉丝福利群开放啦**

加安全419好友进群

红包/书籍/礼品等不定期派送

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9lmiax2vemgjbNkVoWyr9NsuPKE7ibX2icPJeKt6P9Rrhp4MbsoTXtsJcCr1ZAVdiaraqIibU7F3wJRyymBicbRk4Xsg/0?wx_fmt=png)

安全419

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9lmiax2vemgjbNkVoWyr9NsuPKE7ibX2icPJeKt6P9Rrhp4MbsoTXtsJcCr1ZAVdiaraqIibU7F3wJRyymBicbRk4Xsg/0?wx_fmt=png)

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