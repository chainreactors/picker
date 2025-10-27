---
title: Gh0stRAT远控最新攻击样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490589&idx=1&sn=f076c8eb3766c8667ad310bdabfba0e6&chksm=902fb335a7583a238fc945aa122ab97ea2fa9628bd87557d8cab2a2db54dddca354dc744f990&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-20
fetch_date: 2025-10-06T20:35:25.300189
---

# Gh0stRAT远控最新攻击样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTKKb7METBwxnJd0icWIk08x6ibEC1DqwNkEkic4ricXXYCCM4A76tYicwHzA/0?wx_fmt=jpeg)

# Gh0stRAT远控最新攻击样本分析

原创

pandazhengzheng

安全分析与研究

‍

**‍安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

最近几年“银狐”类黑产团伙非常活跃，今年这些黑产团伙会更加活跃，而且仍然会在不断的更新自己的攻击样本，采用各种免杀方式，逃避安全厂商的检测，此前大部分“银狐”黑产团伙使用各种修改版的Gh0st远控做为其攻击武器，远程控制受害者主机之后，进行相关的网络犯罪活动。

近日发现一批疑似新型的Gh0st攻击样本，伪装成各种流行应用网站及其安装程序，诱骗受害者下载安装，该攻击活动非常频繁，笔者对该批攻击样本进行了一些分析。

样本分析

1.样本运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTrbX8icoL8liaOFLsveds7Q9Ziat6PMI7XolWwqSHDhiaVIYtCmib8NW8Ijw/640?wx_fmt=png)

2.在%ProgramData%目录下生成恶意文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTpPxCHJ0HUpowXLd88cZ6pEVT1jeXOcONcbSjpZzyT25gY6sCFzHTsw/640?wx_fmt=png)

3.创建相关的自启动服务，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTicibRhhL0DI0v0lSqVsfC70QK5WsXicjo6aOFwA9ecIkDib9Ub5ZdK8s7g/640?wx_fmt=png)

4.打开恶意程序所在的文件目录，相关恶意程序文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTyY2QX6emcicgnIW5icCP5J5n9oD09Fbw415x5uIkDbXLwicwYm2bgbahQ/640?wx_fmt=png)

5.获取到核心PayLoad，编译时间为2025年1月10日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTaYcexJIAwiaD7oibsXDpPWw7nB5zfJa4zduJ68AG6YVv8C0onEXhkI2Q/640?wx_fmt=png)

6.PayLoad相关代码，与此前Gh0st变种部分特征相匹配，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTMJ4sRAD1mwwmYyXAfWwv7pzUGibBgb4WFI21BU21AxiaE8Ao4yvr17rQ/640?wx_fmt=png)

7.将获取的黑客服务器C2域名信息在威胁情报平台上查询，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTQc8icpuHdrdUOic0tPENia5ibH1hTy1CnZhQZ6refuEr9mtsymUochh0icg/640?wx_fmt=png)

8.另外一个样本在ProgramData目录下生成的恶意文件，与上面类似，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTRXbT6AOYwxxib3da8YUSfGDWoTQHDtr9uBtniaUiaicKQ2k4lHzCh5V8LA/640?wx_fmt=png)

9.展开app-3.11.3目录之后，相关的恶意文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTBibFJrnZaHMOxLYRPfGicic6fNqt4ZtzJU2HzF31PQMS5mLplVTxwNLRw/640?wx_fmt=png)

10.同样会生成相关的自启动服务，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDTiakTLgIA6cqvUzXGVaqvoz5P8tkLWPDOl3aoPhOyhThMe9t4aZXkosQ/640?wx_fmt=png)

11.将获取的黑客服务器C2域名信息在威胁情报平台上查询，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXNsibTDTSYt8zFrHwU8DSDT9BYvxicIFh7UNnTbQCwwF22yl5ZFvPMVn2f5H02SE8uKZ8as8NpGSBg/640?wx_fmt=png)

其他分析过程省略，该批最新的Gh0st变种攻击活动很多，主要伪装成各种流行的应用程序的网站以安装程序进行下载传播，给受害者安装Gh0st远控后门。

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

对高级恶意软件分析和研究感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族，笔者今年打算深度跟踪分析一些全球最顶级的TOP恶意软件家族，这些恶意软件家族都是全球最流行的，也是黑客攻击活动中最常见的恶意软件家族，被广泛应用到各种勒索攻击、黑灰产攻击、APT窃密攻击活动当中以达到攻击目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2rTRBJMYDfYowK8WcvBScfWlJiaYZ5elMdlrREG1LDVODxFQ0Eoy0YLQ/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

‍

预览时标签不可点

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