---
title: 【漏洞通告】Oracle WebLogic Server远程代码执行与拒绝服务漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzk0MjE3ODkxNg==&mid=2247488946&idx=1&sn=64c5620996cc0710ef9e2507f0fc0365&chksm=c2c642b9f5b1cbaf3667d5aae3b668b4e34e0cd89d95893a59c258488748706a1a17b3cd727e&scene=58&subscene=0#rd
source: 绿盟科技CERT
date: 2025-01-23
fetch_date: 2025-10-06T20:10:48.627179
---

# 【漏洞通告】Oracle WebLogic Server远程代码执行与拒绝服务漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VvfsuOanecqWKmFAib2YIsj4ibRLo7W31Oicsoay6AFicjicJsbib41szogFhh8S4xjDL55WYkN3AF7hBPWXzIO1ygBQ/0?wx_fmt=jpeg)

# 【漏洞通告】Oracle WebLogic Server远程代码执行与拒绝服务漏洞

原创

NS-CERT

绿盟科技CERT

**通告编号:NS-2025-0006**

2025-01-22

|  |  |
| --- | --- |
| **TA****G：** | **Oracle WebLogic、CVE-2025-21535、CVE-2025-21549** |
| **漏洞危害：** | **攻击者利用此次漏洞，可实现远程代码执行与拒绝服务。** |
| **版本：** | **1.0** |

**1**

**漏洞概述**

近日，绿盟科技CERT监测到Oracle发布安全公告，其中修复了Oracle WebLogic Server远程代码执行和拒绝服务漏洞，请相关用户尽快采取措施进行防护。

CVE-2025-21535：当T3/IIOP协议开启时，未经身份验证的攻击者通过T3/IIOP协议向服务器发送特制的请求，可实现在目标系统上执行任意代码，导致服务器被远程接管。CVSS评分9.8。

CVE-2025-21549：由于HTTP/2协议的设计缺陷，未经身份验证的攻击者可通过向WebLogic Server发送特制的数据包，导致服务器宕机或频繁崩溃。CVSS评分7.5。

Oracle WebLogic Server是一款企业级Java应用服务器，用于部署、运行和管理基于Java的Web应用程序和企业应用程序。它广泛应用于企业中间件环境，是Oracle Fusion Middleware技术堆栈的核心组件之一。

参考链接：

https://www.oracle.com/security-alerts/cpujan2025.html

**SEE MORE →**

**2****影响范围**

**受影响版本：**

CVE-2025-21535：

* Weblogic 12.2.1.4.0
* Weblogic 14.1.1.0.0

CVE-2025-21549：

* Oracle WebLogic Server 14.1.1.0.0

注：上述为目前Oracle官方仍支持维护的影响范围，10.3.6.0、11.1.1.9、12.1.3.0等多个WebLogic Server版本已停止维护；

**3****漏洞检测**

**3.1 本地检测**

用户可使用如下命令对WebLogic版本和补丁安装的情况进行排查。

|  |
| --- |
| $ cd /Oracle/Middleware/wlserver\_10.3/server/lib $ java -cp weblogic.jar   weblogic.version |

在显示结果中，如果没有补丁安装的信息，则说明存在风险，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecqWKmFAib2YIsj4ibRLo7W31OvLib7IVKQNXmTict5go79pO2l1UrGraeON4rFXBKsSxWGR0qaj9FNbvA/640?wx_fmt=png&from=appmsg)

**3.2 T3协议探测**

Nmap工具提供了WebLogic T3协议的扫描脚本，可探测开启T3服务的WebLogic主机。命令如下：

|  |
| --- |
| nmap -n -v -Pn   –sV [主机或网段地址] -p7001,7002 --script=weblogic-t3-info.nse |

如下图红框所示，目标开启了T3协议且WebLogic版本在受影响范围之内，如果相关人员没有安装官方的安全补丁，则存在漏洞风险。

**![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecqWKmFAib2YIsj4ibRLo7W31Oiahwu4j1fWt5Gicc2nOibvzY42RQN1ibvza6QxiccibpojJ0Eic2GR0rAXWFg/640?wx_fmt=png&from=appmsg)**

**4****漏洞防护**

**4.1 补丁更新**

目前Oracle已发布补丁修复了上述漏洞，请用户参考官方通告及时下载受影响产品更新补丁，并参照补丁安装包中的readme文件进行安装更新，以保证长期有效的防护。

注：Oracle官方补丁需要用户持有正版软件的许可账号，使用该账号登陆https://support.oracle.com后，可以下载最新补丁。

**4.2 临时防护措施**

如果用户暂时无法安装更新补丁，可通过下列措施对高危漏洞进行临时防护。

**4.2.1 限制T3协议访问**

用户可通过控制T3协议的访问来临时阻断针对利用T3协议漏洞的攻击。WebLogic Server提供了名为weblogic.security.net.ConnectionFilterImpl 的默认连接筛选器，此连接筛选器接受所有传入连接，可通过此连接筛选器配置规则，对T3及T3s协议进行访问控制，详细操作步骤如下：

1. 进入WebLogic控制台，在base\_domain的配置页面中，进入“安全”选项卡页面，点击“筛选器”，进入连接筛选器配置。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecqWKmFAib2YIsj4ibRLo7W31O46wPKk2vm0UsBmBBu12m69c6gYibx9QEbSSuOq1B5EAOYTREkF9GwCw/640?wx_fmt=png&from=appmsg)

2. 在连接筛选器中输入：weblogic.security.net.ConnectionFilterImpl，参考以下写法，在连接筛选器规则中配置符合企业实际情况的规则：

|  |
| --- |
| 127.0.0.1 \* \* allow t3 t3s  本机IP \*\* allow t3 t3s  允许访问的IP  \* \* allow t3 t3s    \* \* \* deny t3 t3s |

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecqWKmFAib2YIsj4ibRLo7W31Ox8NFdHgKjOHRicJ8YfTz2HUM5JsniaklXHNHQibfoxQGBzj7Wt9hOleFw/640?wx_fmt=png&from=appmsg)

|  |
| --- |
| 连接筛选器规则格式如下：target   localAddress localPort action protocols，其中：  ·                  target 指定一个或多个要筛选的服务器。  ·                  localAddress 可定义服务器的主机地址。(如果指定为一个星号 (\*)，则返回的匹配结果将是所有本地 IP 地址。)  ·                  localPort 定义服务器正在监听的端口。(如果指定了星号，则匹配返回的结果将是服务器上所有可用的端口)。  ·                  action 指定要执行的操作。(值必须为“allow”或“deny”。)  ·                  protocols 是要进行匹配的协议名列表。(必须指定下列其中一个协议：http、https、t3、t3s、giop、giops、dcom 或 ftp。) 如果未定义协议，则所有协议都将与一个规则匹配。 |

3. 保存后若规则未生效，建议重新启动WebLogic服务（重启WebLogic服务会导致业务中断，建议相关人员评估风险后，再进行操作）。以Windows环境为例，重启服务的步骤如下：

进入域所在目录下的bin目录，在Windows系统中运行stopWebLogic.cmd文件终止WebLogic服务，Linux系统中则运行stopWebLogic.sh文件。

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecqWKmFAib2YIsj4ibRLo7W31OIMcTb0d3p5WD6icgeVKW10Xq7kTyMfXqg4F4DCztibYoqrtuLa5G0L7A/640?wx_fmt=png&from=appmsg)

待终止脚本执行完成后，再运行startWebLogic.cmd或startWebLogic.sh文件启动WebLogic，即可完成WebLogic服务重启。

**4.2.2 禁用IIOP协议**

用户可通过关闭IIOP协议阻断针对利用IIOP协议漏洞的攻击，操作如下：

在WebLogic控制台中，选择“服务”->“AdminServer”->“协议”，取消“启用IIOP”的勾选。并重启WebLogic项目，使配置生效。

**![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecqWKmFAib2YIsj4ibRLo7W31Ozt0EJpAcNjEicXaCymxZiaabBcS5g8vmUmv4PI53ueqYRJvfrgHhNPVg/640?wx_fmt=png&from=appmsg)**

**END**

![](https://mmbiz.qpic.cn/mmbiz_png/qR4ORTNELImFwJM2rh6GKbnrurdFA28jJ8chUPyC1U6aW3jhenqEiaXkmeGVmfOnvAJy8j3My901JQ7emHaicYzA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qR4ORTNELImFwJM2rh6GKbnrurdFA28jib7icfic0lJJHh3eLRpIXiaia08KqOSEibBsz64vlOH9aqicu3lmjccEeAFWQ/640?wx_fmt=jpeg)

**声明**

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qR4ORTNELImFwJM2rh6GKbnrurdFA28jib7icfic0lJJHh3eLRpIXiaia08KqOSEibBsz64vlOH9aqicu3lmjccEeAFWQ/640?wx_fmt=jpeg)

**绿盟科技CERT**∣微信公众号

![](https://mmbiz.qpic.cn/mmbiz_jpg/VvfsuOanecqWKmFAib2YIsj4ibRLo7W31OQqqdnOW05T7icOtGmgcgXDY8A9ouHnRBM2bC1TfcK39LGeQkxn6xibQg/640?wx_fmt=jpeg&from=appmsg "绿盟科技CERT公众号.jpg")

![](https://mmbiz.qpic.cn/mmbiz/Hu8hctxHqSW0nSJn8p8OHVEQwHicSwTibFJMBE650AxdzfISoeY8woe2QsgCINIBrccBOOUft2HuU0GsNQWibSG7g/640?wx_fmt=png)

长按识别二维码，关注网络安全威胁信息

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoicvhEy80SjuIeB8aHInNEXXaMDSZpHyeWx4Aer9yLmHDvnjTFT44XkicnIAuF0AiaicLA6ZKFiaXCCicg/0?wx_fmt=png)

绿盟科技CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoicvhEy80SjuIeB8aHInNEXXaMDSZpHyeWx4Aer9yLmHDvnjTFT44XkicnIAuF0AiaicLA6ZKFiaXCCicg/0?wx_fmt=png)

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