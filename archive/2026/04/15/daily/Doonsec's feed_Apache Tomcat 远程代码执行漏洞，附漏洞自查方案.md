---
title: Apache Tomcat 远程代码执行漏洞，附漏洞自查方案
url: https://mp.weixin.qq.com/s/-42YuZv_nyDrzMx2xaf_mw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:51:17.944086
---

# Apache Tomcat 远程代码执行漏洞，附漏洞自查方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKRfkOibMss786PqPwUGjHu4siboRiaqI4mguqRmR09PN8XVEaw2KnV8ORyrCRF8ZQz35agEmw3yebIQ/0?wx_fmt=jpeg)

# Apache Tomcat 远程代码执行漏洞，附漏洞自查方案

原创

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

漏洞概况

Apache Tomcat是一款开源的Java Servlet容器和Web服务器，广泛用于部署和运行Java Web应用。

近日，Apache Tomcat官方发布通告，修复了Apache Tomcat 远程代码执行漏洞（CVE-2026-34486）。微步情报局已成功复现。经分析，该漏洞源于针对CVE-2026-29146的修复引入了回归缺陷。在消息解密失败后，未能正确终止消息处理流程，而是继续调用 super.messageReceived(msg)，导致攻击者构造的未加密或加密错误的恶意消息能够绕过加密保护，直接进入 Tribes 集群的反序列化流程，若服务器类路径中存在可利用的反序列化链，则可实现远程代码执行。（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-12886）

此漏洞利用条件较为苛刻，建议用户通过如下方案自查：
1. 优先排查Tomcat版本
2. 集群状态和EncryptIntercepto排查：检查是否启用了 Tribes 集群并开启EncryptInterceptor，此组件默认不开启，可自查配置文件(默认路径$CATALINA\_HOME/conf/server.xml)中是否存在集群配置关键字(如："SimpleTcpCluster")和EncryptInterceptor关键字(如："**encryptionKey=")**

3. 检查集群端口（Tribes Receiver 端口）开放情况

建议受此漏洞影响用户尽快修复。

漏洞处置优先级(VPT)

**综合处置优先级：**中风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-12886 |
| CVE编号 | CVE-2026-34486 |
| 漏洞类型 | 远程命令执行 |
| 利用条件评估 | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 否 |
| 对被攻击系统的要求 | 1.启用Tribes集群功能 2.攻击者能够访问集群端口(默认于4000开放) 3.集群通信配置EncryptInterceptor 拦截器 4.目标服务器的Java类路径中存在可利用的反序列化链 |
| 利用漏洞的权限要求 | 无须用户权限 |
| 是否需要受害者配合 | 否 |
| 利用情报 | POC是否公开 | 否 |
| 已知利用行为 | 暂无 |

漏洞影响范围

|  |  |
| --- | --- |
| 产品名称 | Apache Tomcat |
| 受影响版本 | 9.0.116  10.1.53  11.0.20 |
| 有无修复补丁 | 有 |

漏洞复现

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEOaV0NwKH9UYDqiakLtyDKdJjoctOQSxg0Acc5Z5saOONQPicnN46n7P165rjgOg1ZicZJWB1wncIVCMjeb4iaNevoMlwLqS9VdJKM/640?wx_fmt=png&from=appmsg)

修复方案

### 官方修复方案

官方已发布修复方案，请访问链接下载：
https://tomcat.apache.org/download-90.cgi
https://tomcat.apache.org/download-101.cgi
https://tomcat.apache.org/download-110.cgi

### 临时缓解措施

网络层面严格限制Tomcat集群通信端口的访问来源。

微步产品支撑

微步漏洞情报于2026-04-10收录该漏洞。

微步下一代威胁情报平台NGTIP及X情报社区已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

微步威胁感知平台TDP、微步威胁防御系统OneSIG Java反序列化攻击的通用规则默认可检出。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEP5Ph6XbJXKtO3iaEsWrOian4mOjUYLuyeRzIx7TukgnFWh57icXd9KRmcZnsQ0gRVUpztCSL0E1DWMEM4eW9njneGXT5lGxPapkA/640?wx_fmt=png&from=appmsg)

- END -

**微步漏洞情报订阅服务**

微步提供漏洞情报订阅服务，精准、高效助力企业漏洞运营：

* 提供高价值漏洞情报，具备及时、准确、全面和可操作性，帮助企业高效应对漏洞应急与日常运营难题；
* 可实现对高威胁漏洞提前掌握，以最快的效率解决信息差问题，缩短漏洞运营MTTR；
* 提供漏洞完整的技术细节，更贴近用户漏洞处置的落地；
* 将漏洞与威胁事件库、APT组织和黑产团伙攻击大数据、网络空间测绘等结合，对漏洞的实际风险进行持续动态更新。

扫码在线沟通

↓↓↓

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点此电话咨询

**X漏洞奖励计划**

“X漏洞奖励计划”是微步X情报社区推出的一款针对未公开漏洞的奖励计划，我们鼓励白帽子提交挖掘到的0day漏洞，并给予白帽子可观的奖励。我们期望通过该计划与白帽子共同努力，提升0day防御能力，守护数字世界安全。

活动详情：https://x.threatbook.com/v5/vulReward

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

微步在线研究响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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