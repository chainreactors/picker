---
title: Oracle 2025年1月补丁日多产品高危漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247502951&idx=2&sn=21655dd26fe10def4a6c6546fdf240d4&chksm=fe79e8ffc90e61e9fd1b2697f079954e6002507bd3d9fe45bf9331fc3c21481d0b14887ce263&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2025-01-23
fetch_date: 2025-10-06T20:10:51.489119
---

# Oracle 2025年1月补丁日多产品高危漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48ZcqRNwqXAyadStHBiaDD5bibpdLd4YcoBZARiaW8vts7ekSqm3YQqY60iaN6h56a3ll6JojlSfMiajYQ/0?wx_fmt=jpeg)

# Oracle 2025年1月补丁日多产品高危漏洞安全风险通告

奇安信 CERT

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Oracle 2025年1月补丁日多产品高危漏洞 | | |
| **影响产品** | Oracle WebLogic Server、MySQL Server等 | | |
| ****公开时间**** | 2025-01-22 | ****影响对象数量级**** | 百万级 |
| **奇安信评级** | **高危** | **利用可能性** | **中** |
| **POC状态** | 未公开 | **在野利用状态** | 未发现 |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**攻击者利用这些漏洞，可造成破坏系统完整性或泄露敏感信息等。 | | | |

**01**

**漏洞信息**

**>****>****>****>**

**漏洞描述**

Oracle官方发布了2025年1月的关键安全补丁集合更新CPU（Critical Patch Update），修复了多个漏洞包括CVE-2025-21535、CVE-2025-21549、CVE-2025-21521等。其中**Oracle WebLogic Server T3/IIOP远程命令执行漏洞(CVE-2025-21535)、MySQL Server 线程池组件拒绝服务漏洞(CVE-2025-21521)**影响相对较大。

**奇安信CERT建议客户尽快自查并应用本次关键安全补丁集合（CPU）。**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **CVE编号** | **影响组件** | **协议** | **是否远程未授权利用** | **CVSS** | **受影响版本** |
| CVE-2025-21535 | Oracle WebLogic Server  (Core) | T3/IIOP | 是 | 9.8 | 12.2.1.4.0,  14.1.1.0.0 |
| CVE-2025-21549 | Oracle WebLogic Server  (Core) | HTTP/2 | 是 | 7.5 | 14.1.1.0.0 |
| CVE-2025-21521 | MySQL Server:Server: Thread Pooling | MySQL   Protocol | 是 | 7.5 | 8.0.39 and prior,   8.4.2 and prior,   9.0.1 and prior |
| CVE-2025-21500 | MySQL Server:Server: Optimizer | MySQL   Protocol | 否 | 6.5 | 8.0.40 and prior,   8.4.3 and prior,   9.1.0 and prior |
| CVE-2025-21501 | MySQL Server:Server: Optimizer | MySQL   Protocol | 否 | 6.5 | 8.0.40 and prior,   8.4.3 and prior,   9.1.0 and prior |
| CVE-2025-21518 | MySQL Server:Server: Optimizer | MySQL   Protocol | 否 | 6.5 | 8.0.40 and prior,   8.4.3 and prior,   9.1.0 and prior |
| CVE-2025-21566 | MySQL Server:Server: Optimizer | MySQL   Protocol | 否 | 6.5 | 9.1.0 and prior |

**需注意的是，****目前多个Oracle WebLogic Server版本已停止维护，详情如下：**

**10.3.6.0、11.1.1.9版本最终CPU截止至2021年10月；**

**12.1.3.0版本最终CPU截止至2022年01月。**

**>****>****>****>**

**值得关注漏洞**

本次值得关注的漏洞如下：

**1. Oracle WebLogic Server T3/IIOP远程命令执行漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 漏洞名称 | Oracle WebLogic Server T3/IIOP远程命令执行漏洞 | | | | |
| 漏洞类型 | 命令执行 | 风险等级 | 高危 | 漏洞ID | CVE-2025-21535 |
| 公开状态 | 未公开 | 在野利用 | 未发现 | | |
| 漏洞描述 | Oracle WebLogic Server 中存在命令执行漏洞。未经身份验证的攻击者可以通过T3或IIOP协议通过网络访问来破坏Oracle WebLogic Server。成功的攻击可能导致攻击者完全接管Oracle WebLogic Server。 | | | | |
| 参考链接 | | | | | |
| https://www.oracle.com/security-alerts/cpujan2025.html | | | | | |

**2. MySQL Server 线程池组件拒绝服务漏洞**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 漏洞名称 | MySQL Server 线程池组件拒绝服务漏洞 | | | | |
| 漏洞类型 | 拒绝服务 | 风险等级 | 高危 | 漏洞ID | CVE-2025-21521 |
| 公开状态 | 未公开 | 在野利用 | 未发现 | | |
| 漏洞描述 | 该漏洞存在于 MySQL Server 的线程池组件中。攻击者可以通过网络利用该漏洞，无需身份验证或用户交互。成功利用该漏洞可能导致 MySQL Server 挂起或频繁崩溃，从而完全拒绝服务。 | | | | |
| 参考链接 | | | | | |
| https://www.oracle.com/security-alerts/cpujan2025.html | | | | | |

**02**

**影响范围**

|  |  |
| --- | --- |
| **CVE编号** | **受影响版本** |
| CVE-2025-21535 | Oracle WebLogic Server 12.2.1.4.0  Oracle WebLogic Server 14.1.1.0.0 |
| CVE-2025-21549 | Oracle WebLogic Server 14.1.1.0.0 |
| CVE-2025-21521 | Oracle MySQL Server <= 8.0.39  Oracle MySQL Server <= 8.4.2  Oracle MySQL Server <= 9.0.1 |
| CVE-2025-21500 | Oracle MySQL Server <= 8.0.40  Oracle MySQL Server <= 8.4.3  Oracle MySQL Server <= 9.1.0 |
| CVE-2025-21501 | Oracle MySQL Server <= 8.0.40  Oracle MySQL Server <= 8.4.3  Oracle MySQL Server <= 9.1.0 |
| CVE-2025-21518 | Oracle MySQL Server <= 8.0.40  Oracle MySQL Server <= 8.4.3  Oracle MySQL Server <= 9.1.0 |
| CVE-2025-21566 | Oracle MySQL Server <= 9.1.0 |

**03**

**处置建议**

**>****>****>****>**

**安全更新**

目前官方已发布补丁，请参考以下链接进行修复：

https://www.oracle.com/security-alerts/cpujan2025.html

**Oracle WebLogic Server升级方式**

1. Oracle WebLogic Server 12c：

参考补丁文件，使用opatch apply 安装补丁

C:\Oracle\Middleware\Oracle\_Home\OPatch>opatch apply 本机补丁地址

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamicayeaSoUMibKlneuCfKpoJTHpVwnB10Rh5wIsotUTZdMUiatKaiak2J7ng/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamicxMK7hPnicmuy1MACuPxhsibQIUmoMUotvDVkLusI6ZibPLKkfEeJQY9aw/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

注：补丁编号请自行更改为新补丁编号。

**若非必须开启，请禁用T3和IIOP协议。**

禁用T3、IIOP协议具体操作步骤如下：

**1.禁用T3：**

进入WebLogic控制台，在base\_domain的配置页面中，进入“安全”选项卡页面，点击“筛选器”，进入连接筛选器配置。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamic9vBCAcH5dEmhP2u9ZXHibD3ONict0Dg94ZibeTgyLGiapHreQpT8SLrxeg/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

在连接筛选器中输入：WebLogic.security.net.ConnectionFilterImpl，参考以下写法，在连接筛选器规则中配置符合企业实际情况的规则：

127.0.0.1 \* \* allow t3 t3s

本机IP \* \* allow t3 t3s

允许访问的IP \* \* allow t3 t3s

\* \* \* deny t3 t3s

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamicIMOGibMtJFR22sK3tmkapZCO5DBAn7EVRsWaqq9Y9MQwbOxfCmFzx3g/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

连接筛选器规则格式如下：target localAddress localPort action protocols，其中：

target 指定一个或多个要筛选的服务器。

localAddress 可定义服务器的主机地址。(如果指定为一个星号 (\*)，则返回的匹配结果将是所有本地 IP 地址。)

localPort 定义服务器正在监听的端口。(如果指定了星号，则匹配返回的结果将是服务器上所有可用的端口)。

action 指定要执行的操作。(值必须为“allow”或“deny”。)

protocols 是要进行匹配的协议名列表。(必须指定下列其中一个协议：http、https、t3、t3s、giop、giops、dcom 或 ftp。) 如果未定义协议，则所有协议都将与一个规则匹配。

保存后若规则未生效，建议重新启动WebLogic服务（重启WebLogic服务会导致业务中断，建议相关人员评估风险后，再进行操作）。以Windows环境为例，重启服务的步骤如下：

进入域所在目录下的bin目录，在Windows系统中运行stopWebLogic.cmd文件终止WebLogic服务，Linux系统中则运行stopWebLogic.sh文件。

 ![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamiccOeicN9e4taBDDKyn5DXj5fFOzIeKeHZgDJf05Yp8KHOicme6tEqeTMQ/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

待终止脚本执行完成后，再运行startWebLogic.cmd或startWebLogic.sh文件启动WebLogic，即可完成WebLogic服务重启。

**2.禁用IIOP：**

用户可通过关闭IIOP协议阻断针对利用IIOP协议漏洞的攻击，操作如下：

在WebLogic控制台中，选择“服务”->”AdminServer”->”协议”，取消“启用IIOP”的勾选。并重启WebLogic项目，使配置生效。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamiccvt6lCYxlRvjI3nvLszFFOszt9TKBrfBPlkcGtNT7uBDRTDB8PxtLw/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

**04**

**参考资料**

[1]https://www.oracle.com/security-alerts/cpujan2025.html

**05**

**时间线**

2025年1月22日，奇安信 CERT发布安全风险通告。

**06**

**漏洞情报服务**

奇安信ALPHA威胁分析平台已支持漏洞情报订阅服务：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icvtfpU85HMgqgQaWBcvFdZZmoic7vD8p42wrTeAdC0cg22eL2YQKBnrWG5Qo5PlLNMrXb6sSK7NnQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic9MrG2xydb7ibvlliaJy5hSRNiczgXkCbn5Ca7F9ND19ZMa62TRibWNYwy5icTIZTh91gtp9CNt30tKQQ/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

点击↓**阅读原文**，到**ALPHA威胁分析平台**订阅更多漏洞信息。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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