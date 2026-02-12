---
title: 已修复 | 微信Linux版本远程命令执行漏洞
url: https://mp.weixin.qq.com/s/mgdatlRj_WUUKCW8I0VCzw
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:19:56.528412
---

# 已修复 | 微信Linux版本远程命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKRfkOibMss786PqPwUGjHu4siboRiaqI4mguqRmR09PN8XVEaw2KnV8ORyrCRF8ZQz35agEmw3yebIQ/0?wx_fmt=jpeg)

# 已修复 | 微信Linux版本远程命令执行漏洞

原创

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

漏洞概况

Linux 版微信是腾讯基于 QT 或 Web 技术开发的官方客户端，让 Linux 用户无需通过 Wine 模拟即可在国产操作系统或主流发行版上直接收发消息和文件。

近日，微步情报局监控到微信Linux客户端1click 远程命令执行漏洞已被修复。微步情报局已成功复现。经分析，Linux版本(包括银河麒麟等信创系统)微信中存在一个1click远程命令执行漏洞，攻击者可构造恶意文件名的文件（包括但不限于pdf，doc，xls等文件类型），诱使受害者点击查看，从而造成远程命令执行。（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-3046）

此漏洞无须用户权限，攻击者成功利用此漏洞可远程命令执行。

漏洞处置优先级(VPT)

**综合处置优先级：**高风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-3046 |
| 漏洞类型 | 命令注入 |
| 利用条件评估 | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 否 |
| 对被攻击系统的要求 | Linux操作系统 |
| 利用漏洞的权限要求 | 无须用户权限 |
| 是否需要受害者配合 | 是 |
| 利用情报 | POC是否公开 | 是 |
| 已知利用行为 | 暂无 |

漏洞影响范围

|  |  |
| --- | --- |
| 产品名称 | 深圳市腾讯计算机系统有限公司 | 微信客户端（Linux版本） |
| 受影响版本 | 由于腾讯在服务端做了修复，2026.2.11起所有版本都不受影响 |
| 有无修复补丁 | 有 |

漏洞复现

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMiad16bVVxwVg5t2ib8Fu9dudibjva31PXicibTqM2dvApCOGWDVnRbNmTiaRjGiaiaBWPzFfuVVLnqcGXWN6FNJCDJ54YnGrhviczPGTg/640?wx_fmt=png&from=appmsg)

修复方案

### 官方修复方案

无需更新客户端，微信官方已在服务端修复此漏洞，发送恶意文件会显示发送中断，如下图所示：![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPXDvzBs06iaBAtfy2ib8CcmfVO1jib7XIb7X7ozpasViad90IhG9RFlKLcR2MYicc3V6oxzBnzPib0U84QQyT6AiavmBWNsoXqeLGBSo/640?wx_fmt=png&from=appmsg)

### 临时缓解措施

1. 提升个人安全意识，不点击未知来源文件
2. 禁用微信的文件自动下载功能，防止因误点造成的漏洞利用，配置方式如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEM6GY6S3p5IqiczwY5rviavuXF5ZFsLOiafGkBib46wdcjzx9YIWfFKQju0jcUIPPEXIJmEvvF7cINNBdib8w0U4Z22nHRN1LWibTbvk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOkY1bDneY3bXONLWZicBJK0Q1KIP1qrb5ZJ2ITYJhjd24duOibZibCuhzh4EJ8w19PaiaQlrnRFgkXGGcUMPmsfa2nZDpfNYMlvxs/640?wx_fmt=png&from=appmsg)

微步产品支撑

微步漏洞情报于2026-02-10收录该漏洞。

微步下一代威胁情报平台NGTIP及X情报社区已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

微步终端安全管理平台OneSEC已于2026-02-10支持检测，检测ID：9107利用微信执行代码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEO0qrxLPmgzoGYMfu6JDkbTERia9kx37LsWqNnm5O7w7retkJeRHbl3t2cWejKaibR3hwXgvNdkgvyk9IbyBbrlmicDRP6yLQeQlQ/640?wx_fmt=png&from=appmsg)

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