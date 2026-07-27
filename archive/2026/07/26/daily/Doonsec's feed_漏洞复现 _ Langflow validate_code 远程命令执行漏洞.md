---
title: 漏洞复现 | Langflow validate_code 远程命令执行漏洞
url: https://mp.weixin.qq.com/s/Oa9pVBMLUSGOzg0kV9y4tw
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:41:18.090162
---

# 漏洞复现 | Langflow validate_code 远程命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yIciaKAicYtoocP0tUIblsCbmoJicwibOw5cDMOzN8icPdv0BSuXX4vs9C45via8L5RibRs3qfUHuwBfiakfaa338sjNef9AjTU0VVlLRk9jkXkup5Q/0?wx_fmt=jpeg)

# 漏洞复现 | Langflow validate\_code 远程命令执行漏洞

实战安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

|  |
| --- |
| 本文仅用于技术学习和安全研究，请勿使用本文所提供的内容及相关技术从事非法活动，由于传播和利用此文所提供的内容或工具而造成任何直接或间接的损失后果，均由使用者本人承担，所产生一切不良后果与文章作者及本账号无关。如内容有争议或侵权，请私信我们！我们会立即删除并致歉。谢谢！ |

1

**漏洞描述**

Langflow 是目前最流行的低代码 AI 工作流构建平台，支持拖拽式可视化界面，可接入 OpenAI、Anthropic、Azure 等主流大模型，并集成 Pinecone、Milvus 等向量数据库，被大量企业用于构建 RAG 应用、Agent 工作流和 MCP 工具服务。Langflow /api/v1/validate/code 接口存在远程命令执行漏洞。攻击者可通过构造恶意的请求，利用该漏洞在目标服务器上执行任意命令，从而可能导致服务器被完全控制、敏感数据泄露等严重后果。

2

**影响版本**

Langflow

3

**测绘语法**

fofa语法

```
product="LOGSPACE-LangFlow"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtoqOzQ4ppVu1tSCsbX1zpViaAql2w2LcMrY5pbvwFzlXIpdb11tDIDkFdsJPMnpFdTGUnRaZllxLiaXzdiaueZdA4ibxdgpFtz7cQ14/640?wx_fmt=png&from=appmsg)

4

**漏洞复现**

获取access\_token

![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtopgv38DdyFcj42LmDRPFMW048jv7K2qMkdIGHXqmCVOBhtlBewwdibrjMzlhdoMgNwKN5wSW3ayDcvueaTmibGLuk5xp1XUlOg24/640?wx_fmt=png&from=appmsg)

执行命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtoqrEPrOaDibbIE6v73WLh0TsB2UC8Y3fh7bIxtfuRkh8WzzJGp7WC6wfGP2TFLLpWX1z0UAvo1a5l2azy7YeeyUxibT9AxmAiaFbc/640?wx_fmt=png&from=appmsg)

5

**检测POC**

nuclei

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtooJdcIhA6SJtP5o5OpG4PVibzibNwDojAezEh0mwt6DjVTGW3xXpCdaZbmyCRl8XfQ6oBVc8f0vkkc9l3eMUqLZ5w5NLe7tUMnaI/640?wx_fmt=png&from=appmsg)

afrog

![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtorHzNiaHzTJggq7zK4fDhiaf0FGbtCSuIfprs9icKad0bEOc9iaCVlgAHybs6E6aGcuy8DibgYLGic4NELQfWN8ZALIFhohoELwHzvd0/640?wx_fmt=png&from=appmsg)

6

**漏洞修复**

1、建议联系厂商打补丁或升级版本。

2、增加Web应用防火墙防护。

3、关闭互联网暴露面或接口设置访问权限。

7

**内部圈子**

**现在已更新POC数量 2450+（中危以上）**

🔥 **1day/Nday 漏洞实战圈上线** 🔥

还在到处找公开漏洞 POC？

这里专注整合全网公开1day/Nday漏洞POC和复现，一站式解决你的痛点！

🔍 圈子福利

✅ 整合全网 1day/Nday 漏洞POC，附带复现步骤，新手也能快速上手

✅ 每周更新 7-15 个POC测试脚本，经过实测验证，到手就能用

✅ 完美适配 Nuclei/Afrog 扫描工具，脚本无需额外修改，即拿即用

✅ 临时福利：免费 FOFA 高级会员查询，无需账号也能高效资产测绘

✅ 专属权益：提供指纹识别库，指纹库持续更新

💡 适合对象

渗透测试🔹攻防演练🔹安全运维🔹企业自查🔹SRC漏洞挖掘

⚠️ 重要提醒

仅限授权范围内的合法安全测试，严禁用于未授权攻击行为！

本服务为虚拟资源服务，一经购买概不退款，请按需谨慎购买！

目前圈子已满200人，价格由66.9调整为69.9元（交个朋友啦），250人后调整为71.9元。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yIciaKAicYtooOcDoeEYZtETDFQ4rjVvy92CZjibia4I6kmdiakLGDf8DbibXuyXo44ic8YGePNBib59bWUHegCYsgPATaVUw8r11f9B7uzwfczOyt4/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF11icZP3IFHQ3V3ayPqKCuRxbljuSc8zianApHibibJQzEG3qXvkW76uWBjvYrGNTZOmcvXTl5K8ely0g/0?wx_fmt=png)

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