---
title: 可任意文件读取，警惕Solr身份绕过形成的漏洞利用链
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507329&idx=1&sn=0a2cf458a45cbd59b0416309a4bcfdf5&chksm=cfcabe95f8bd37833e6a5024c97259be35a8948851b49eaafd4184990e41bb88b853159f0a9b&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-10-31
fetch_date: 2025-10-06T18:54:19.546539
---

# 可任意文件读取，警惕Solr身份绕过形成的漏洞利用链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMLwp5eBIVgfZHMicVu1wDPOAiceSGxJLmGEGwcL4U0bvQ2ada6Tm9Ay0ibeicvwBiaMtoYt7mdG7j5GePw/0?wx_fmt=jpeg)

# 可任意文件读取，警惕Solr身份绕过形成的漏洞利用链

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**漏洞概况**

Apache Solr是一个基于Apache Lucene的开源企业搜索平台。它提供快速可靠的搜索，分布式索引，复制和负载平衡查询，自动故障转移和恢复，集中化配置以及其他功能。

微步情报局于近日获取到Apache Solr 身份认证绕过漏洞情报（https://x.threatbook.com/v5/vul/XVE-2024-29630，CVE编号CVE-2024-45216）。在以集群模式启动的Solr实例中，攻击者能够通过在任何Solr URL API 路径的末尾添加一个伪造的路由，绕过身份认证机制，访问任意API。

由于此漏洞影响版本范围较广，所以可结合Solr历史漏洞形成组合利用链。微步情报局已实现任意文件读取的组合利用，目前不排除可结合其他漏洞实现RCE。

该漏洞利用较为简单且 PoC 已公开，建议尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-29630 |
| 漏洞类型 | 身份鉴别错误 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 以集群方式启动Solr |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 是 |
| 已知利用行为 | 否 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | Apache软件基金会 - Apache Solr |
| **受影响版本** | 5.3.0 ≤ version < 8.11.4  9.0.0 ≤ version < 9.7.0 |
| **影响范围** | 万级 |
| **有无修复补丁** | 有 |

前往X情报社区资产测绘查看影响资产详情：

https://x.threatbook.com/v5/survey?q=app%3D%22solr%22

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLwp5eBIVgfZHMicVu1wDPOAe0Rlia8KGZvbGVrXWIib9SnPfAhibhia70XG21eUNoQV5ECG9YnI5RbZmQ/640?wx_fmt=png&from=appmsg)

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLwp5eBIVgfZHMicVu1wDPOAn4X7XUha1iaxono9tcia9AsyibjSkQFuctCMibvOu7QYALxjW9FjX2mib0g/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

厂商已修复此漏洞，可通过以下链接下载最新版本：

https://solr.apache.org/security.html#cve-2024-45216-apache-solr-authentication-bypass-possible-using-a-fake-url-path-ending

## **临时修复方案：**

* 避免将Solr实例暴露于互联网上
* 使用防护类设备进行防护，拦截URL中带有 “:/admin/info/key” 特征的请求

**微步产品侧支持情况**

微步威胁感知平台TDP已支持检测，检测ID为S3100156199 ，模型/规则高于20241030000000 可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLwp5eBIVgfZHMicVu1wDPOAXBltRwPCBXmAfHDt9yTHK5K0HxC4yuNicKwodGYBaiaibWVhAVCqPicbjQ/640?wx_fmt=png&from=appmsg)

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