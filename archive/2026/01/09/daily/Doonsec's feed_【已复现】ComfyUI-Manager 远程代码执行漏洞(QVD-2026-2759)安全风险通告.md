---
title: 【已复现】ComfyUI-Manager 远程代码执行漏洞(QVD-2026-2759)安全风险通告
url: https://mp.weixin.qq.com/s/h2G0STVzVlsv43n_Nw1s7w
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:23:30.855596
---

# 【已复现】ComfyUI-Manager 远程代码执行漏洞(QVD-2026-2759)安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48A2VmYMwjaouRlWRB9MibCuu9bGsmzIRkrpcIOdOUicg5hicNFcc1kiaXeOybTk6JNcicjNsHZu9PU8lQ/0?wx_fmt=jpeg)

# 【已复现】ComfyUI-Manager 远程代码执行漏洞(QVD-2026-2759)安全风险通告

奇安信 CERT

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | ComfyUI-Manager 远程代码执行漏洞 | | |
| **漏洞编号** | QVD-2026-2759 | | |
| ****公开时间**** | 2026-01-09 | ****影响量级**** | 十万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **9.8** |
| **威胁类型** | 代码执行 | **利用可能性** | ****高**** |
| **POC状态** | **未公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **未公开** | **技术细节状态** | **未公开** |
| **危害描述：**攻击者无需认证即可远程控制运行中 ComfyUI 的服务器，造成数据泄露、服务瘫痪或横向移动等严重后果。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

ComfyUI 是一款基于节点式工作流的 Stable Diffusion 图形界面工具，广泛用于 AI 图像生成领域。它通过可视化拖拽方式构建复杂推理流程，支持自定义模型、插件和脚本扩展。ComfyUI-Manager 是其官方扩展组件管理器，负责安装、更新和管理自定义节点、模型及启动脚本，是 ComfyUI 生态中的核心辅助模块。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复ComfyUI-Manager 远程代码执行漏洞(QVD-2026-2759)，默认暴露 Web API 接口用于在线修改配置项，且未对用户输入中的 \r\n 做过滤，导致攻击者可向配置文件中注入恶意换行内容；通过将 security\_level 等关键配置项篡改为 weak，进一步结合插件自带的 Git URL 安装功能，可在服务器上执行任意代码。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

ComfyUI-Manager < v3.39.2

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现ComfyUI-Manager 远程代码执行漏洞(QVD-2026-2759)，截图如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48A2VmYMwjaouRlWRB9MibCubAATTeR3Qls9tn7tsCGvH2fnzjdSuLSsJZkkgiauaRuurodiaXghiaMag/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48A2VmYMwjaouRlWRB9MibCu0wq3Yq7YfyuCrNROiachmstE3EykwQELelQShXLF2XvHSLb74ibt5DsA/640?wx_fmt=jpeg&from=appmsg)

**04**

**受影响资产情况**

奇安信鹰图资产测绘平台数据显示，ComfyUI-Manager 远程代码执行漏洞(QVD-2026-2759)关联的国内风险资产总数为28968个，关联IP总数为3719个。国内风险资产分布情况如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icooYBZackl2a6Ftbm3BHud2WibDQ7pgpyEPfk8jBWzzG4xqWZY279YNPreonBHHyesbS7aO8pxYTA/640?wx_fmt=png&from=appmsg)

ComfyUI-Manager 远程代码执行漏洞(QVD-2026-2759)关联的全球风险资产总数为105029个，关联IP总数为46117个。全球风险资产分布情况如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icooYBZackl2a6Ftbm3BHudZaKibSibKysywdIxS5fgRIkKPiauGzXsoog6kntf4yrED5XqQElolicJRg/640?wx_fmt=png&from=appmsg)

**05**

**处置建议**

**>****>****>****>**

**安全更新**

官方已发布安全补丁，请及时更新至最新版本：

ComfyUI-Manager >= v3.39.2

同时升级ComfyUI >= v0.3.76，以启用“系统用户保护API”。

下载地址：

https://github.com/Comfy-Org/ComfyUI-Manager

**06**

**参考资料**

[1]https://github.com/Comfy-Org/ComfyUI-Manager/commit/f4fa394e0f03b013f1068c96cff168ad10bd0410

**07**

**时间线**

2026年01月09日，奇安信 CERT发布安全风险通告。

**08**

**漏洞情报服务**

奇安信ALPHA威胁分析平台已支持漏洞情报订阅服务：

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BY9IJ0MPzeiashvK2XLpdl3XtTtCD91h0jS26fqvuWpEMXgmXa85qLkoA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=3 "漏洞订阅上线.png")

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=4)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=5 "CERT LOGO.png")

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