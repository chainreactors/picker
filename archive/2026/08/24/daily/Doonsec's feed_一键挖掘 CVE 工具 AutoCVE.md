---
title: 一键挖掘 CVE 工具 AutoCVE
url: https://mp.weixin.qq.com/s/TWMOdRfrBa9xG7gtLwwSpg
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:55:33.830492
---

# 一键挖掘 CVE 工具 AutoCVE

# 一键挖掘 CVE 工具 AutoCVE

larlarua
larlarua

无影安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：本篇文章仅用于技术交流，请勿利用文章内的相关技术从事非法测试，由于传播、利用本公众号无影安全实验室所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号无影安全实验室及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！所有工具安全性自测！！！**VX：smile62157**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把"**无影安全实验室**"设为星标，这样更新文章也能第一时间推送！

![](https://mmbiz.qpic.cn/mmbiz_gif/3GHDOauYyUGbiaHXGx1ib5UxkKzSNtpMzY5tbbGdibG7icBSxlH783x1YTF0icAv8MWrmanB4u5qjyKfmYo1dDf7YbA/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

安全工具

## 0x01 工具介绍

AutoCVE是一款可以一键挖掘 CVE，筛项目、审源码、验漏洞、出报告，全流程自动化的自动化工具。

项目地址：https://github.com/larlarua/AutoCVE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Nuuibh3bDOw41A7TVFJXPyWhPh6XLGdmgB0Ny1Wv2NndwDuviaibaG4A5Hnouc7wX4DLje02EqNp6txDWqMzYic3Tz8iaEb1vS7PIuNamYHsUdsQ/640?wx_fmt=png&from=appmsg)

## 0x02 工具功能

### 一键完成 CVE 挖掘

实现从项目筛选、仓库导入、审计任务创建、Agent 漏洞挖掘到 CVE 申报报告生成的全流程自动化。用户仅需复制报告内容并提交，即可完成后续 CVE 申请。

### Multi-Agent 协同审计

通过 Orchestrator 统一调度 Recon、Scan、Triage、Finding 和 Verification 等 Agent，协同完成信息收集、工具扫描、误报过滤、漏洞深挖与动态验证。
![cf44a992ddf6de782e267ac83ed6a5c8.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlgRF2ANVaJEbu9CJ1yZG9EMEibr4Qgx9VEnaGCfmPeiaB17qicNu0XpfBSS7ibhfaZSGu512vgicn4oCsiczrjFqU7rA8Jw3pETO8DE/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4 "null")![6481482aa8c682591331a7c5b402a190.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmvUFVCwnY4VrnViaUYah0PkhcBbAs3O99Lsofib8Qq2uaItZk89OWlDAL0qyYPLEVXrt9AJtVlcxXhEINqElSJksHEickTmPpq7M/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5 "null")

## 0x03 docker 安装

```
sudo usermod -aG docker $USER
curl -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.0/docker-compose.prod.cn.yml | docker compose -f - up -d
```

```
http://192.168.23.137:3000

邮箱：demo@example.com
密码：demo123
```

![bcf0db05b4412ae058851d68d2583ca8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnX0w82fhAygh7AJKeicMcjfy3xcRx7VrmdDmqiau5Y0FHEicypyPOjr4DRgicl79Sa5uT8GLXVhcjsAwtWSpJTy0XM2G7UATvjIibg/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1 "null")上传源码
![4e1394ebc6a659ec4d6d9f1b04a60b0e.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkzrBU3UnZ7w6SyTLc6Txv2wdXbRplq4B2VuKUejcGzyicia1bhQA2xasAgq42LAT80Waa3pAPAdqkoXVAJJ1jBuy5TnoYlaicUXw/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2 "null")

## 0x03 使用教程

https://github.com/larlarua/AutoCVE/blob/main/docs/USER\_GUIDE.md

![9c2d07c98a94c6d6ccb288d680090d0a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmia58a6SxTSInH5sqU5OkT3m57NXbDQxKMO9JNfkkic7Bic0a5McLH7CqTjEFgATYmBj8P2Kd03kdr0OFRVSSgDhR4sRgIOlZDto/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3 "null")

最后推荐一下内部小密圈，干货满满，物超所值，**内部圈子每增加100人，价格将上涨20元，越早进越优惠！！！**

**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/awCdqJkJFET8apEknf7bc6ZR8CyWIBqmV3L88k03ibsUgLfyzvyvuOjkZUfWm9YsK0phQ3owbjBgbhibnWBicgsXw/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&randomid=ebo9tcn3&tp=webp)**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFESkGMPLLYOibsOdiaYUbUGH2ibd832G0h4stN7iacicE62hCJGle1IuVQbgGDx5v5GXjwUuE23xJNJjgTg/0?wx_fmt=png)

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