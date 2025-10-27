---
title: 【更新】Apache Struts2文件上传漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507565&idx=1&sn=f1eb832586d6ef20bbd6b579dff4956f&chksm=cfcabd79f8bd346f18fe53c9b16c9b7029e5124dffe6fd10d7027af46c8fab5d4f12807425d8&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-12-18
fetch_date: 2025-10-06T19:42:22.638653
---

# 【更新】Apache Struts2文件上传漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSibfONW0ib18vsxvniae0dvDGyNH4YzdjmskGMeKXoCGr0Cr6FzbVsxu5w/0?wx_fmt=jpeg)

# 【更新】Apache Struts2文件上传漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png)

**漏洞概况**

Apache Struts2 是一个开源的 Java Web 应用程序开发框架，旨在帮助开发人员构建灵活、可维护和可扩展的企业级 Web 应用程序。

微步情报局获取到 Apache Struts2 文件上传漏洞情报 CVE-2024-53677 （https://x.threatbook.com/v5/vul/XVE-2024-35895），攻击者成功利用该漏洞可上传任意文件，从而远程执行任意代码，如果系统没有使用FileUploadInterceptor组件，则不受此漏洞影响。

漏洞PoC已公开，建议受影响的客户尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-35895 |
| 漏洞类型 | 远程代码执行 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 使用FileUploadInterceptor组件 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 是 |
| 已知利用行为 | 否 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | Apache软件基金会 - Apache Struts |
| **受影响版本** | 2.0.0 - 2.3.37   2.5.0 - 2.5.33  6.0.0 - 6.3.0.2 |
| **有无修复补丁** | 有 |

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIzLY3S5oy9Hw50kaibjSUHib7dicoRonDVKYuHb3rZtfvLmgh3jMd2CVQk8BKvGtqc0zTxbibyQgV0Rw/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

Apache Struts 已发布安全通告，官方通告链接：

https://cwiki.apache.org/confluence/display/WW/S2-067

请根据官方通告将 Struts 升级至 6.4.0 并使用 ActionFileUploadInterceptor 作为文件上传组件。

## **临时修复方案：**

1. 自查业务是否使用了 FileUploadInterceptor 组件，如果并未使用则不受该漏洞影响。
2. 使用防护类设备对文件上传接口进行防护。
3. 如非必要，避免将资产暴露在互联网。

**微步产品侧支持情况**

微步威胁感知平台TDP通用规则可以检出，检测ID为 S3100120558，模型/规则高于 20230612000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIzLY3S5oy9Hw50kaibjSUHibqx5gwIk8aicnulAcnJmDpjepWLBqM5m9btCvwHCYGbAibaoqqdUxv40w/640?wx_fmt=png&from=appmsg)

- END -

//

**微步漏洞情报订阅服务**

微步提供漏洞情报订阅服务，精准、高效助力企业漏洞运营：

* 提供高价值漏洞情报，具备及时、准确、全面和可操作性，帮助企业高效应对漏洞应急与日常运营难题；
* 可实现对高威胁漏洞提前掌握，以最快的效率解决信息差问题，缩短漏洞运营MTTR；
* 提供漏洞完整的技术细节，更贴近用户漏洞处置的落地；
* 将漏洞与威胁事件库、APT组织和黑产团伙攻击大数据、网络空间测绘等结合，对漏洞的实际风险进行持续动态更新。

扫码在线沟通

↓↓↓

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png)

点此电话咨询

**X漏洞奖励计划**

“X漏洞奖励计划”是微步X情报社区推出的一款针对未公开漏洞的奖励计划，我们鼓励白帽子提交挖掘到的0day漏洞，并给予白帽子可观的奖励。我们期望通过该计划与白帽子共同努力，提升0day防御能力，守护数字世界安全。

活动详情：https://x.threatbook.com/v5/vulReward

预览时标签不可点

修改于

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