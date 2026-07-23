---
title: 【漏洞复现】Fastjson 1.2.83远程代码执行漏洞
url: https://mp.weixin.qq.com/s/1DDz7VRYfNkmQMPF36xpPA
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:10:11.344961
---

# 【漏洞复现】Fastjson 1.2.83远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0wuPBaVgoOaP4obiahMkqqYGYFvqiawLAWHibVtTnXOtSPzia8icC51ibq9MtV1MNCRcQgEEcTibkVgNFYUsCiawQP13CgrLibtmDu43Shkia3x9wIg9Y/0?wx_fmt=jpeg)

# 【漏洞复现】Fastjson 1.2.83远程代码执行漏洞

数字人才创研院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于禾盾安全应急响应中心
，作者HDSRC

![](https://wx.qlogo.cn/mmhead/kSiaeFj92SMz5Z1EDjRx7VrDnWN2XYkiacEq8P21CqJicADkEojcwhzeKDvaeME7ibRmVHzltAlEpPA/0)

**禾盾安全应急响应中心**
.

禾盾安全应急响应中心，简称HDSRC，致力于发布重要安全漏洞的预警、最新的威胁事件分析与漏洞风险提示、相关威胁情报与安全研究成果共享。

点击上方蓝字关注我们

漏洞预警

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5d6O0HSxyXkoJlmfe0w3ScXV6VhNKNLP8JvkZzicOziaviaSxjKtia1pzPiaT7RYjdTUm8TYGhpY365mIXEzVGucoSA/640?wx_fmt=png&from=appmsg)

01

漏洞基本概述

Vulnerability Overview

![](https://mmbiz.qpic.cn/mmbiz_png/4kcMpxcoP324FB41iaOFjLovYzq48jiayABVZozfrfjNU4hTK3iaTAS71icN9rSUtVqAavoMiagZ3BVyyJlLgxTCiarQ/640?wx_fmt=png)

01

![](https://mmbiz.qpic.cn/mmbiz_png/qiaou2SWwgPxZsPuGUBqvfztY349JahH5gTicMQHkTaziasQOt0sYZP0QicweflsMyu4g1lUGPOrIpDlBwCYibwNjYw/640?wx_fmt=png)

Fastjson是阿里巴巴开源的一款高性能 Java JSON 解析库，以其出色的解析速度和简洁的 API 设计在国内Java生态系统中占据主导地位。

**【风险等级】****极 危**

**【CVE编号】****无**

  2026年7月19日，禾盾安全应急响应中心监测到该漏洞，经分析，攻击者可通过构造包含特定字段的JSON字符串，利用Fastjson的AutoType支持机制加载远程恶意文件，从而在目标服务器上执行任意代码。建议受影响的用户尽快修复，与此同时，请做好资产自查以及预防工作，以免遭受黑客攻击。

02

漏洞影响范围

Vulnerability Impact

![](https://mmbiz.qpic.cn/mmbiz_png/4kcMpxcoP324FB41iaOFjLovYzq48jiayABVZozfrfjNU4hTK3iaTAS71icN9rSUtVqAavoMiagZ3BVyyJlLgxTCiarQ/640?wx_fmt=png)

01

![](https://mmbiz.qpic.cn/mmbiz_png/qiaou2SWwgPxZsPuGUBqvfztY349JahH5gTicMQHkTaziasQOt0sYZP0QicweflsMyu4g1lUGPOrIpDlBwCYibwNjYw/640?wx_fmt=png)

Fastjson 1.2.66-1.2.83

03

漏洞修复方案

Vulnerability Fixes

![](https://mmbiz.qpic.cn/mmbiz_png/4kcMpxcoP324FB41iaOFjLovYzq48jiayABVZozfrfjNU4hTK3iaTAS71icN9rSUtVqAavoMiagZ3BVyyJlLgxTCiarQ/640?wx_fmt=png)

01

![](https://mmbiz.qpic.cn/mmbiz_png/qiaou2SWwgPxZsPuGUBqvfztY349JahH5gTicMQHkTaziasQOt0sYZP0QicweflsMyu4g1lUGPOrIpDlBwCYibwNjYw/640?wx_fmt=png)

目前官方已发布修复版本，建议用户及时确认产品版本，尽快采取修补措施。

  **注：其它建议**

    1.启用安全模式 (SafeMode)，可以完全禁用 AutoType 功能。

    2.Spring Boot 3.2 重写了嵌套 jar Loader，类名与 URL 处理变化，公开链结论需重新验证，不能直接套用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0wuPBaVgoOaamEbZxdjXdnEhswyL3nbgsiaTZWMM3tZ7Cp6tRCb41fPnLI9AwvP7KRpX0EFlSoMCVj4hM2Z9sK2160aXEBuTemE72olaZHuk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0wuPBaVgoOYcibiaUibvByiadoGIwlImegeIzpSWZJpgLrIa7NibHBiaibzkr8iaichvCP8HZgKq7nE47icHjS6AibicGj9khBTFSbNHjb5Csg2sbnibCN2g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0wuPBaVgoOYbVmvcDvTkUvXx9QB5DbnWpMqoeQqhVOVfk6LLiaIPxGzAgRaTW4GqcUo0IsRFcZYKJF8nxyJhzl8gLH9QF5vK0OW5jx5EOBW8/640?wx_fmt=png&from=appmsg)

‍‍‍‍‍‍‍**下载链接：**

```
https://github.com/alibaba/fastjson
```

04

漏洞参考链接

Vulnerability Fixes Link

![](https://mmbiz.qpic.cn/mmbiz_png/4kcMpxcoP324FB41iaOFjLovYzq48jiayABVZozfrfjNU4hTK3iaTAS71icN9rSUtVqAavoMiagZ3BVyyJlLgxTCiarQ/640?wx_fmt=png)

01

![](https://mmbiz.qpic.cn/mmbiz_png/qiaou2SWwgPxZsPuGUBqvfztY349JahH5gTicMQHkTaziasQOt0sYZP0QicweflsMyu4g1lUGPOrIpDlBwCYibwNjYw/640?wx_fmt=png)

```
https://github.com/alibaba/fastjson2
```

05

漏洞时间滚轴

Vulnerability Time

#发现时间#2026年07月19日

#验证时间#2026年07月20日

#通告时间#2026年07月21日

HD

![](https://mmbiz.qpic.cn/mmbiz_png/ibwov0bgAkBeVIILoZgYNTn6rrKD6sSkPVG8nZcwn2QWHibG6AsEyuy9n3XGMuoZIyGCEmvv1ZRnaibXbYkrIP4Hg/640?wx_fmt=png)

禾盾安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f1Ap1TId9Sp8P5te00xOHDe8oCZN6GRlKk24gBLXpsI9gV0pyabsYgkrAhygibQL1VzhABHrUstCyoMHysrBY5g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XCey8HnLC70G2J8ft1vNlFXiaURP3NcPfiaB4KASRaibFGRX73tiaiaKFFxVbDv0UiaGpvxGxAvdr147CIwPrVkw8Qvw/640?wx_fmt=png)

**以技术为驱动，以安全专家为核心，以诚信为本、以专业为先、以坚持为恒，围绕漏洞生态体系打造集漏洞监测、漏洞收集、漏洞挖掘、漏洞分析、漏洞管理、专家响应、漏洞预警、安全服务定制化于一体的漏洞安全一站式服务，帮助客户防患于未然，在降低资产风险的同时，大幅提升客户对漏洞感知、预警、分析等响应能力，为国家、政企客户、用户抢占风险预警处置先机，提升网络安全主动防护能力。**

![](https://mmbiz.qpic.cn/mmbiz_png/ry30yBl2sr8jsWibpdia0ku8mG2eibhcjnIADPzCMXXlsdUXs3KzibJ8Q6q6VCw33WRPxx0xNpI8vyepKOONH1Ij2A/640?wx_fmt=png)

HD

![](https://mmbiz.qpic.cn/mmbiz_png/ibwov0bgAkBeVIILoZgYNTn6rrKD6sSkPVG8nZcwn2QWHibG6AsEyuy9n3XGMuoZIyGCEmvv1ZRnaibXbYkrIP4Hg/640?wx_fmt=png)

获取更多最新情报

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f1Ap1TId9Sp8P5te00xOHDe8oCZN6GRlKk24gBLXpsI9gV0pyabsYgkrAhygibQL1VzhABHrUstCyoMHysrBY5g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XCey8HnLC70G2J8ft1vNlFXiaURP3NcPfiaB4KASRaibFGRX73tiaiaKFFxVbDv0UiaGpvxGxAvdr147CIwPrVkw8Qvw/640?wx_fmt=png)

**建议您订阅「禾盾安全-漏洞情报」服务，及时获取更多漏洞情报详情以及处置建议，让您的单位真正远离漏洞威胁。**

**电话：177-128-77993**

**邮箱：src@hedun.com.cn**

![](https://mmbiz.qpic.cn/mmbiz_png/ry30yBl2sr8jsWibpdia0ku8mG2eibhcjnIADPzCMXXlsdUXs3KzibJ8Q6q6VCw33WRPxx0xNpI8vyepKOONH1Ij2A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5d6O0HSxyXkoJlmfe0w3ScXV6VhNKNLPmYBiaYmk4QgObS8Iicl7vJ6Q685oE8vTNLHFfHefk58InmILibRUJDzGw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/SkPgzibRbCL5X8OKYMB024f1gWFpTuBibMDe5YTnPU2uAuEBUoiaXD3OXnTBfPfGyew6VpxO5dBgFoic9TaRhHouFw/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MPrt2xIEpHTQMv2HqCZUgSSH2diaXwhwzRr9oI1M20ry9YibVaLLqJwfiaibSurbeWsO917R7GiaU8718hLY6vYC9ng/0?wx_fmt=png)

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