---
title: 搭建个人的贾维斯——openclaw
url: https://mp.weixin.qq.com/s/6vKNnF-fK1850mzw3GcXjQ
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:03:42.609673
---

# 搭建个人的贾维斯——openclaw

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ptxZESUjfTGzLhOYFO7pbtRaSCCQga93BTv6ZgY6deVyibH05aV09cAfVGmpjBnExtLMH5z3OB4dcZnQyrtHDyW2r5SGuqdXWJZVmmRWibgHQ/0?wx_fmt=jpeg)

# 搭建个人的贾维斯——openclaw

原创

【白】
【白】

白安全组

![]()

在小说阅读器中沉浸阅读

**前言**

是一套把 AI 能力变成“可运维、可诊断、可长期运行”的本地/服务器工具链：说白了就是可以让我们实现像贾维斯一样，一个指令帮我们做很多事情，比如整理邮件，工作流，关注某个行业最新的信息并且整理在什么时间发送到我们的微信上等等。

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTHnIjKrsBtib25Nuq0fv9UDQGFTvYDcgzbef6IiarbYhSWD6tZBnoH7OK8Biad85F7qSdoFQmHEOiaDn2DfQSCYtiazlNc3GbGE7Ribk/640?wx_fmt=png&from=appmsg)

那么对于安全人员来说可以做什么呢

一次引导把服务装成后台 daemon，适合 7×24 的安全自动化任务（告警分析/流量研判/报告生成等）

当你把它接进安全流程（比如 SOC 辅助分析、工单自动总结、情报归档），最重要的是稳定和可追踪

关注当前最新的一些漏洞情况，整理poc或者exp等等

# 安装

安装目前三大平台都支持，这里主要写Windows和Linux

## Linux快速安装

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

## Windows安装（使用powershell安装）

```
iwr -useb https://openclaw.ai/install.ps1 | iex
```

这里以Linux为例，安装好之后我们校验可以使用下面的命令：

```
curl -fsSL https://openclaw.ai/install.sh | bash -s -- --help
```

随后会出现帮助手册

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTFicrThtVPVCYa7azGkqjNBtMvAmF7fk6ZJwQV1xibszRxyvus2966JFRfGADTZLzuerU95ia3FJnm1F8ceFaErVta4SLicRbGzVEs/640?wx_fmt=png&from=appmsg)

具体使用方式可以参考官网：

https://docs.openclaw.ai/install

# 腾讯云搭建

参考文章

https://cloud.tencent.com/document/product/1291/128042

开通云桌面之后，我们创建购买云桌面实例

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTGgAj2v1oHe1soPpqDda2WibC3Cn8Fr2gicoaibbJERHrUSoSl7LXp3I7CrOlw1ibggG18rJlrhqOCVhnDVJ6FKOHh4gXGscWia4ibZ4/640?wx_fmt=png&from=appmsg)

然后利用桌面实例进行，建议选择按时收费，一个月钱也不少

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

白安全组

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

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