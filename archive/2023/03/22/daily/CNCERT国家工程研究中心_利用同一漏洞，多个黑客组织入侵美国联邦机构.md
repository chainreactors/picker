---
title: 利用同一漏洞，多个黑客组织入侵美国联邦机构
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535631&idx=3&sn=0b028a99a444b67cb78077ecbb7e691b&chksm=fa93facecde473d8e5fa54aee23c72de10a90c674501cdc4b710805611e0163b22275294c5f0&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-22
fetch_date: 2025-10-04T10:16:05.885132
---

# 利用同一漏洞，多个黑客组织入侵美国联邦机构

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kMMYn0L9k9MplexpNL3E3ycWYtmFqX8vIhqaPMnjicrQcybySaf23K4QlX2DfbfksOGpQMRUrnticQ/0?wx_fmt=jpeg)

# 利用同一漏洞，多个黑客组织入侵美国联邦机构

网络安全应急技术国家工程中心

近日，多个威胁行为者，包括一个民族国家组织，利用Progress Telerik中存在三年的严重安全漏洞闯入美国一个未命名的联邦实体。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kMMYn0L9k9MplexpNL3E3y1ibpneXpCMPicFwMzsANEQXCWohf2uUejbiaaSsIQwuf1aw32FtPtmWAQ/640?wx_fmt=jpeg)

该披露来自网络安全和基础设施安全局(CISA)、联邦调查局(FBI)和多州信息共享与分析中心(MS-ISAC)发布的联合咨询。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QmbJGbR2j6wRwlhzQOxOnrzOaOuglhLt3Y9qrNR7ibrXQkiaicMrfibxrcrp3ywWpFg8EOjp0lwuzibeF5FU7a6IJvw/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

“利用此漏洞允许恶意行为者在联邦文职行政部门(FCEB)机构的Microsoft Internet 信息服务(IIS) Web 服务器上成功执行远程代码。”这些机构表示。

从2022年11月到2023年1月初，确定了与数字入侵相关的妥协指标(IoC)。

跟踪为CVE-2019-18935（CVSS分数：9.8），该问题与影响ASP.NET AJAX的Progress Telerik UI的.NET反序列化漏洞有关，如果不打补丁，可能会导致远程代码执行。

在此值得注意的是，CVE-2019-18935之前曾在2020年和2021年被各种威胁参与者滥用的一些最常利用的漏洞中占有一席之地。

CVE-2019-18935与CVE-2017-11317一起，也被追踪为Praying Mantis（又名TG2021）的威胁行为者武器化，以渗透到美国的公共和私人组织网络。

上个月，CISA还将CVE-2017-11357——另一个影响 Telerik UI 的远程代码执行错误——添加到已知被利用漏洞(KEV)目录中，引用了积极利用的证据。

在2022年8月记录的针对FCEB机构的入侵中，据说威胁行为者利用CVE-2019-18935 通过 w3wp.exe 进程上传和执行伪装成 PNG 图像的恶意动态链接库(DLL)文件。

DLL工件旨在收集系统信息、加载额外的库、枚举文件和进程，并将数据泄露回远程服务器。

早在2021年8月就观察到的另一组攻击很可能是由名为XE Group的网络犯罪分子发起的，需要使用上述规避技术来规避检测。

这些DLL文件投放并执行反向（远程）shell实用程序，用于与命令和控制域进行未加密的通信，以投放额外的有效负载，包括用于持久后门访问的ASPX web shell。

Web shell配备了“枚举驱动器；发送、接收和删除文件；以及执行传入的命令”和“包含一个用于轻松浏览系统上的文件、目录或驱动器的界面，并允许用户上传或将文件下载到任何目录。”

为应对此类攻击，建议组织将其 Telerik UI ASP.NET AJAX 实例升级到最新版本，实施网络分段，并对具有特权访问权限的帐户强制实施抗网络钓鱼的多因素身份验证。

原文来源：E安全

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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