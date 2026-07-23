---
title: Oracle 2026年7月补丁日多产品高危漏洞安全风险通告
url: https://mp.weixin.qq.com/s/HZm_WSiMvObEbLPlCclcBg
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:09:20.802550
---

# Oracle 2026年7月补丁日多产品高危漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555vChgFsY1yaFGRZTzEUOSQtagGKrlGlWSCEwZ9byIDyEic8gIAiaicqMg8zvWnx8vedzNjzVV1rx9CWtCicBpr3LIALFrlUibyIYX2w/0?wx_fmt=jpeg)

# Oracle 2026年7月补丁日多产品高危漏洞安全风险通告

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Oracle 2026年07月补丁日多产品高危漏洞 | | |
| **影响产品** | Oracle WebLogic Server、MySQL Server等 | | |
| ****公开时间**** | 2026-07-22 | ****影响对象数量级**** | 百万级 |
| **奇安信评级** | **高危** | **利用可能性** | **中** |
| **POC状态** | 未公开 | **在野利用状态** | 未发现 |
| **EXP状态** | 未公开 | **技术细节状态** | 未公开 |
| **危害描述：**攻击者利用这些漏洞，可造成破坏系统完整性或泄露敏感信息等。 | | | |

**01**

**漏洞信息**

**>****>****>****>**

**漏洞描述**

Oracle官方发布了2026年07月的关键安全补丁集合更新CPU（Critical Patch Update），修复了多个漏洞包括 CVE-2026-60315、CVE-2026-60206、CVE-2026-60199 等。其中Oracle MySQL Server X Plugin 拒绝服务漏洞(CVE-2026-60315)、Oracle WebLogic Server 远程代码执行漏洞(CVE-2026-60206)、Oracle WebLogic Server 远程代码执行漏洞(CVE-2026-60199)影响相对较大。奇安信CERT建议客户尽快自查并应用本次关键安全补丁集合（CPU）。

**奇安信CERT建议客户尽快自查并应用本次关键安全补丁集合（CPU）。**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **CVE编号** | **影响组件** | **协议** | **是否远程未授权利用** | **CVSS** | **受影响版本** |
| CVE-2026-60315 | MySQL Server, MySQL Cluster: Server: X Plugin | X Protocol | 是 | 8.2 | MySQL Server:   8.4.0-8.4.10  9.7.0-9.7.1  MySQL Cluster:  8.0.0-8.0.47  8.4.0-8.4.10  9.7.0-9.7.1 |
| CVE-2026-61094 | MySQL Server, MySQL Cluster: Server: Replication | MySQL Protocol | 否 | 7.2 | MySQL Server:  8.4.0-8.4.10  9.7.0-9.7.1  MySQL Cluster:  8.0.0-8.0.47  8.4.0-8.4.10  9.7.0-9.7.1 |
| CVE-2026-60316 | MySQL Server, MySQL Cluster: Server: X Plugin | X Protocol | 否 | 7.2 | MySQL Server:  8.4.0-8.4.10  9.7.0-9.7.1  MySQL Cluster:  8.0.0-8.0.47  8.4.0-8.4.10  9.7.0-9.7.1 |
| CVE-2026-60206 | Oracle WebLogic Server (Core) | SAML | 否 | 9.9 | 12.2.1.4.0 14.1.1.0.0  14.1.2.0.0  15.1.1.0.0 |
| CVE-2026-60199 | Oracle WebLogic Server (Core) | HTTP | 是 | 9.8 | 12.2.1.4.0 14.1.1.0.0  14.1.2.0.0  15.1.1.0.0 |
| CVE-2026-60291 | Oracle WebLogic Server (Core) | HTTP | 是 | 9.8 | 12.2.1.4.0 14.1.1.0.0  14.1.2.0.0  15.1.1.0.0 |
| CVE-2026-60292 | Oracle WebLogic Server (Core) | HTTP | 是 | 9.8 | 12.2.1.4.0 14.1.1.0.0 |

**需注意的是，****目前多个Oracle WebLogic Server版本已停止维护，详情如下：**

**10.3.6.0、11.1.1.9版本最终CPU截止至2021年10月；**

**12.1.3.0版本最终CPU截止至2022年01月。**

**>****>****>****>**

**值得关注漏洞**

本次值得关注的漏洞如下：

**1. Oracle MySQL Server X Plugin 拒绝服务漏洞(CVE-2026-60315)**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 漏洞名称 | Oracle MySQL Server X Plugin 拒绝服务漏洞 | | | | |
| 漏洞类型 | 拒绝服务、信息泄露 | 风险等级 | 高危 | 漏洞ID | CVE-2026-60315 |
| 公开状态 | 未公开 | 在野利用 | 未发现 | | |
| 漏洞描述 | 该漏洞存在于 X Plugin 组件中，由于对特定协议请求的处理存在缺陷，未经身份验证的远程攻击者可通过网络发送特制数据包触发漏洞。成功利用可导致 MySQL Server 或 MySQL Cluster 进程挂起或频繁崩溃，造成完全拒绝服务，同时可能未授权读取数据库中的部分敏感数据。 | | | | |
| 参考链接 | | | | | |
| https://www.oracle.com/security-alerts/cpujul2026.html | | | | | |

**2. Oracle WebLogic Server 远程代码执行漏洞(CVE-2026-60199)**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 漏洞名称 | Oracle WebLogic Server 远程代码执行漏洞 | | | | |
| 漏洞类型 | 代码执行 | 风险等级 | 高危 | 漏洞ID | CVE-2026-60199 |
| 公开状态 | 未公开 | 在野利用 | 未发现 | | |
| 漏洞描述 | 未经身份验证的远程攻击者可通过发送特制的 HTTP 网络请求利用此漏洞。成功利用后，攻击者能够完全控制受影响的 Oracle WebLogic Server 实例，进而执行任意操作、访问敏感数据或中断业务服务，对系统机密性、完整性和可用性造成全面威胁。 | | | | |
| 参考链接 | | | | | |
| https://www.oracle.com/security-alerts/cpujul2026.html | | | | | |

**3. Oracle WebLogic Server 远程代码执行漏洞(CVE-2026-60206)**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 漏洞名称 | Oracle WebLogic Server 远程代码执行漏洞 | | | | |
| 漏洞类型 | 代码执行 | 风险等级 | 高危 | 漏洞ID | CVE-2026-60206 |
| 公开状态 | 未公开 | 在野利用 | 未发现 | | |
| 漏洞描述 | 该漏洞存在于核心组件的 SAML 身份验证处理机制中，由于对用户提供的 SAML 数据验证不充分导致。具有网络访问权限的攻击者可通过发送特制的 SAML 请求触发此漏洞。成功利用可能导致攻击者完全控制服务器，并可能通过范围变更影响与 WebLogic 集成的其他产品，造成机密信息泄露、数据篡改和服务中断等严重后果。 | | | | |
| 参考链接 | | | | | |
| https://www.oracle.com/security-alerts/cpujul2026.html | | | | | |

**02**

**影响范围**

|  |  |
| --- | --- |
| **CVE编号** | **受影响版本** |
| CVE-2026-60315 | 8.4.0 <= Oracle MySQL Server <= 8.4.10 9.7.0 <= Oracle MySQL Server <= 9.7.1  8.0.0 <= Oracle MySQL Cluster <= 8.0.47  8.4.0 <= Oracle MySQL Cluster <= 8.4.10  9.7.0 <= Oracle MySQL Cluster <= 9.7.1 |
| CVE-2026-61094 | 8.4.0 <= Oracle MySQL Server <= 8.4.10 9.7.0 <= Oracle MySQL Server <= 9.7.1  8.0.0 <= Oracle MySQL Cluster <= 8.0.47  8.4.0 <= Oracle MySQL Cluster <= 8.4.10  9.7.0 <= Oracle MySQL Cluster <= 9.7.1 |
| CVE-2026-60316 | 8.4.0 <= Oracle MySQL Server <= 8.4.10 9.7.0 <= Oracle MySQL Server <= 9.7.1  8.0.0 <= Oracle MySQL Cluster <= 8.0.47  8.4.0 <= Oracle MySQL Cluster <= 8.4.10  9.7.0 <= Oracle MySQL Cluster <= 9.7.1 |
| CVE-2026-60206 | Oracle WebLogic Server 12.2.1.4.0 Oracle WebLogic Server 14.1.1.0.0  Oracle WebLogic Server 14.1.2.0.0  Oracle WebLogic Server 15.1.1.0.0 |
| CVE-2026-60199 | Oracle WebLogic Server 12.2.1.4.0 Oracle WebLogic Server 14.1.1.0.0  Oracle WebLogic Server 14.1.2.0.0  Oracle WebLogic Server 15.1.1.0.0 |
| CVE-2026-60291 | Oracle WebLogic Server 12.2.1.4.0 Oracle WebLogic Server 14.1.1.0.0  Oracle WebLogic Server 14.1.2.0.0  Oracle WebLogic Server 15.1.1.0.0 |
| CVE-2026-60292 | Oracle WebLogic Server 12.2.1.4.0 Oracle WebLogic Server 14.1.1.0.0 |

**03**

**处置建议**

**>****>****>****>**

**安全更新**

目前官方已发布补丁，请参考以下链接进行修复：

https://www.oracle.com/security-alerts/cpujul2026.html

**Oracle WebLogic Server升级方式**

1. Oracle WebLogic Server 12c：

参考补丁文件，使用opatch apply 安装补丁

C:\Oracle\Middleware\Oracle\_Home\OPatch>opatch apply 本机补丁地址

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamicayeaSoUMibKlneuCfKpoJTHpVwnB10Rh5wIsotUTZdMUiatKaiak2J7ng/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamicxMK7hPnicmuy1MACuPxhsibQIUmoMUotvDVkLusI6ZibPLKkfEeJQY9aw/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=1)

注：补丁编号请自行更改为新补丁编号。

**若非必须开启，请禁用T3和IIOP协议。**

禁用T3、IIOP协议具体操作步骤如下：

**1.禁用T3：**

进入WebLogic控制台，在base\_domain的配置页面中，进入“安全”选项卡页面，点击“筛选器”，进入连接筛选器配置。

 ![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamic9vBCAcH5dEmhP2u9ZXHibD3ONict0Dg94ZibeTgyLGiapHreQpT8SLrxeg/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=2)

在连接筛选器中输入：WebLogic.security.net.ConnectionFilterImpl，参考以下写法，在连接筛选器规则中配置符合企业实际情况的规则：

127.0.0.1 \* \* allow t3 t3s

本机IP \* \* allow t3 t3s

允许访问的IP \* \* allow t3 t3s

\* \* \* deny t3 t3s

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamicIMOGibMtJFR22sK3tmkapZCO5DBAn7EVRsWaqq9Y9MQwbOxfCmFzx3g/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=3)

连接筛选器规则格式如下：target localAddress localPort action protocols，其中：

target 指定一个或多个要筛选的服务器。

localAddress 可定义服务器的主机地址。(如果指定为一个星号 (\*)，则返回的匹配结果将是所有本地 IP 地址。)

localPort 定义服务器正在监听的端口。(如果指定了星号，则匹配返回的结果将是服务器上所有可用的端口)。

action 指定要执行的操作。(值必须为“allow”或“deny”。)

protocols 是要进行匹配的协议名列表。(必须指定下列其中一个协议：http、https、t3、t3s、giop、giops、dcom 或 ftp。) 如果未定义协议，则所有协议都将与一个规则匹配。

保存后若规则未生效，建议重新启动WebLogic服务（重启WebLogic服务会导致业务中断，建议相关人员评估风险后，再进行操作）。以Windows环境为例，重启服务的步骤如下：

进入域所在目录下的bin目录，在Windows系统中运行stopWebLogic.cmd文件终止WebLogic服务，Linux系统中则运行stopWebLogic.sh文件。

 ![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamiccOeicN9e4taBDDKyn5DXj5fFOzIeKeHZgDJf05Yp8KHOicme6tEqeTMQ/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=4)

待终止脚本执行完成后，再运行startWebLogic.cmd或startWebLogic.sh文件启动WebLogic，即可完成WebLogic服务重启。

**2.禁用IIOP：**

用户可通过关闭IIOP协议阻断针对利用IIOP协议漏洞的攻击，操作如下：

在WebLogic控制台中，选择“服务”->”AdminServer”->”协议”，取消“启用IIOP”的勾选。并重启WebLogic项目，使配置生效。

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic5ctib8wmV2DDbKsfVNPamiccvt6lCYxlRvjI3nvLszFFOszt9TKBrfBPlkcGtNT7uBDRTDB8PxtLw/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=5)

**04**

**参考资料**

[1]https://www.oracle.com/security-alerts/cpujul2026.html

**05**

**时间线**

2026年07月22日，奇安信 CERT发布安全风险通告。

**06**

**漏洞情报服务**

「奇安信漏洞情报平台」重磅上线，诚邀您来体验：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555thlV1AqdGj8NCOFDbIcXAZ6...