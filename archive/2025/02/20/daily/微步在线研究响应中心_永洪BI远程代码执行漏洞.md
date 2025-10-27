---
title: 永洪BI远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507692&idx=1&sn=7311ec648e06da0783dc83eec9aba48f&chksm=cfcabdf8f8bd34ee59ae8a8d4d1d23ee9224edae49635d0a8ac5b4a6c828c18248f443cc9aad&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2025-02-20
fetch_date: 2025-10-06T20:35:17.837745
---

# 永洪BI远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSibfONW0ib18vsxvniae0dvDGyNH4YzdjmskGMeKXoCGr0Cr6FzbVsxu5w/0?wx_fmt=jpeg)

# 永洪BI远程代码执行漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png)

**漏洞概况**

永洪BI是一款由北京永洪商智科技有限公司开发的企业级商业智能软件。旨在帮助企业通过数据分析和可视化，提升决策效率和数据驱动的业务洞察能力。永洪BI提供了从数据准备、数据分析到数据可视化的一站式解决方案，适用于多种行业和应用场景。

微步情报局通过X漏洞奖励计划获取到永洪BI远程代码执行漏洞情报（https://x.threatbook.com/v5/vul/XVE-2025-0235），攻击者可利用该漏洞绕过身份认证验证，进入后台写入WebShell，进而获取服务器权限，利用难度较低，建议受影响的用户尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：****高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2025-0235 |
| 漏洞类型 | 远程代码执行 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 默认配置 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 否 |
| 已知利用行为 | 否 |

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | 北京永洪商智科技有限公司 - 永洪BI (Z-Suite) |
| **受影响版本** | version < 10.2.4 |
| **有无修复补丁** | 有 |

前往X情报社区资产测绘查看影响资产详情：

https://x.threatbook.com/v5/survey?q=app%3D%22%E6%B0%B8%E6%B4%AABI%22

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJUl6vIy7ibZm5DuQW8F9bNXFvW9pHeWPRB7J0uUESMLt6sUnIUB1PQYbSmQyt84dfwkrstWxCopZw/640?wx_fmt=png&from=appmsg)

**漏洞复现**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJUl6vIy7ibZm5DuQW8F9bNXdVDexTN5kFH5VRFectEztzx0L7sdOcVCia8g0XXGonJfM2SgSbKgcgg/640?wx_fmt=png&from=appmsg)

**修复方案**

**官方修复方案：**

厂商反馈已于10.2.4版本修复此漏洞，建议联系永洪售后（https://www.yonghongtech.com/help/Z-Suite/10.2/ch）更新至10.2.4及以上版本。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJUl6vIy7ibZm5DuQW8F9bNXVn3bwckiaAxYibNRhpYEqq6Ad4yLT123uwAvibNHNGPr5fORr7uCAtqeQ/640?wx_fmt=png&from=appmsg)

## **临时修复方案：**

##

1. 使用防护类设备进行防护，限制访问/bi/Viewer路径，拦截可疑的文件上传操作。
2. 如非必要，避免将资产暴露在互联网。

**微步产品侧支持情况**

微步威胁感知平台TDP 已支持检测，检测ID：S3100158190、S3100158191，模型/规则高于20250113000000可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJUl6vIy7ibZm5DuQW8F9bNXAGHfhBhwh3MwHwUgjLkvaSL6b1kicfk0avibibAPURjRsRQ7F8k8BJ9pA/640?wx_fmt=png&from=appmsg)

微步威胁防御系统OneSIG已支持防护，规则ID为：3000008724。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMJUl6vIy7ibZm5DuQW8F9bNXS52WWZZRNuBnq5e5OtH1V0ZoW1WyTEIhNUQDIeF4qod4xEENpsD2dA/640?wx_fmt=png&from=appmsg)

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