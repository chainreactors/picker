---
title: 一键挖掘 CVE 工具 AutoCVE
url: https://mp.weixin.qq.com/s/5b4VyBqCsL1vwLyfz5Z0nA
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:40:23.006170
---

# 一键挖掘 CVE 工具 AutoCVE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVmkt0Bm2dU2WddqXJhAeRmfYrJMPSzWqjaxV3d2ympbvISOOY39HskPcJicDjgOBVDBbfGhzf7Pwrb16kSSyaCicewMWFjE6icSMw/0?wx_fmt=jpeg)

# 一键挖掘 CVE 工具 AutoCVE

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 198，阅读大约需 1 分钟

## 前言

一键挖掘 CVE，筛项目、审源码、验漏洞、出报告，全流程自动化

项目地址：https://github.com/larlarua/AutoCVE

![5509bbc9861bd355354e41aa025f0c0c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVm9EZUrfnEhB5MQCGhALViaSYYCct4LADhJwib8oKvFT2IlEtF49nm8xHQnsMwFoVX4FIV4p3tJBuxTJVWfca1FKyDydOL7x5gaU/640?from=appmsg "null")

5509bbc9861bd355354e41aa025f0c0c.png

## docker 安装

```
sudo usermod -aG docker $USER
curl -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.0/docker-compose.prod.cn.yml | docker compose -f - up -d
```

```
http://192.168.23.137:3000

邮箱：demo@example.com
密码：demo123
```

![bcf0db05b4412ae058851d68d2583ca8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnX0w82fhAygh7AJKeicMcjfy3xcRx7VrmdDmqiau5Y0FHEicypyPOjr4DRgicl79Sa5uT8GLXVhcjsAwtWSpJTy0XM2G7UATvjIibg/640?from=appmsg "null")

bcf0db05b4412ae058851d68d2583ca8.png

上传源码
![4e1394ebc6a659ec4d6d9f1b04a60b0e.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkzrBU3UnZ7w6SyTLc6Txv2wdXbRplq4B2VuKUejcGzyicia1bhQA2xasAgq42LAT80Waa3pAPAdqkoXVAJJ1jBuy5TnoYlaicUXw/640?from=appmsg "null")

4e1394ebc6a659ec4d6d9f1b04a60b0e.png

## AutoCVE 使用手册

https://github.com/larlarua/AutoCVE/blob/main/docs/USER\_GUIDE.md

![9c2d07c98a94c6d6ccb288d680090d0a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmia58a6SxTSInH5sqU5OkT3m57NXbDQxKMO9JNfkkic7Bic0a5McLH7CqTjEFgATYmBj8P2Kd03kdr0OFRVSSgDhR4sRgIOlZDto/640?from=appmsg "null")

9c2d07c98a94c6d6ccb288d680090d0a.png

## 核心能力

### 一键完成 CVE 挖掘

实现从项目筛选、仓库导入、审计任务创建、Agent 漏洞挖掘到 CVE 申报报告生成的全流程自动化。用户仅需复制报告内容并提交，即可完成后续 CVE 申请。

### Multi-Agent 协同审计

通过 Orchestrator 统一调度 Recon、Scan、Triage、Finding 和 Verification 等 Agent，协同完成信息收集、工具扫描、误报过滤、漏洞深挖与动态验证。
![cf44a992ddf6de782e267ac83ed6a5c8.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlgRF2ANVaJEbu9CJ1yZG9EMEibr4Qgx9VEnaGCfmPeiaB17qicNu0XpfBSS7ibhfaZSGu512vgicn4oCsiczrjFqU7rA8Jw3pETO8DE/640?from=appmsg "null")

cf44a992ddf6de782e267ac83ed6a5c8.png

![6481482aa8c682591331a7c5b402a190.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmvUFVCwnY4VrnViaUYah0PkhcBbAs3O99Lsofib8Qq2uaItZk89OWlDAL0qyYPLEVXrt9AJtVlcxXhEINqElSJksHEickTmPpq7M/640?from=appmsg "null")

6481482aa8c682591331a7c5b402a190.png

## 总结

项目地址：https://github.com/larlarua/AutoCVE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13)

声明：文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

如有侵权烦请告知，我会立即删除并致歉。谢谢！

文章有疑问的，可以公众号发消息问我，或者留言。我每天都会看的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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