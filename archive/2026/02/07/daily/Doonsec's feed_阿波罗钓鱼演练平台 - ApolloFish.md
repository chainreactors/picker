---
title: 阿波罗钓鱼演练平台 - ApolloFish
url: https://mp.weixin.qq.com/s/594IEHbXMW-P1tvQejmJVg
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:31:05.390519
---

# 阿波罗钓鱼演练平台 - ApolloFish

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj57d8A4QS7YIS9SJFI91YhTnja3nUjDYyibrQAhia9Y0gLLMzkDulN9RZj1OwjsdfonHgxtSUpJ08XS2BuMaGCsAJaHPfEuudtySk/0?wx_fmt=jpeg)

# 阿波罗钓鱼演练平台 - ApolloFish

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

## 平台介绍

### 背景

在数字化浪潮下，钓鱼攻击已成为企业网络安全的主要威胁之一。仿冒网页、恶意邮件等钓鱼手段层出不穷，一旦员工不慎中招，可能导致企业核心数据泄露、系统瘫痪、财产损失等严重后果。在此背景下，阿波罗钓鱼演练平台(ApolloFish)应运而生，平台以“实战演练赋能安全意识提升”为核心目标，通过模拟真实的网页钓鱼、邮箱钓鱼场景，帮助企业精准检验员工安全防护能力，系统性强化全员安全意识，筑牢企业网络安全第一道防线。

### 平台价值

为企业安全意识提升赋能

1. 实战化演练，贴近真实攻击场景：摒弃传统说教式安全培训的弊端，以1:1还原真实钓鱼攻击的演练模式，让员工在沉浸式体验中直观感受钓鱼攻击的隐蔽性和危害性，深刻认识到安全防护的重要性。
2. 精准化评估，定位安全防护短板：通过全流程行为数据追踪和多维度分析，生成企业全员安全意识评估报告，清晰呈现各部门、各层级员工的安全防护能力差异，为企业制定针对性的安全培训计划提供数据支撑。
3. 个性化培训，提升培训实效：基于演练结果精准推送个性化培训内容，实现“因材施教”，让员工快速掌握与自身岗位相关的钓鱼攻击识别技巧，提升培训的针对性和实效性。
4. 全流程管控，简化演练管理难度：平台提供从演练场景配置、演练发起、过程监控到报告生成、培训跟进的全流程可视化管理功能，操作简单便捷，无需专业的安全技术团队即可完成演练组织，大幅降低企业安全演练的管理成本和技术门槛。

## 使用说明

### 部署方式

阿波罗钓鱼演练平台 优势：

* [\*] 无需Docker环境
* [\*] 无需复杂的依赖环境
* [\*] 支持跨平台运行

下载地址：https://github.com/safe1024/apollofish/releases
阿波罗钓鱼演练平台支持多系统运行，支持x86架构和arm架构。
若您是Windows，且CPU是Intel、AMD，请下载：ApolloFish\_windows\_amd64.exe
若您是Windows，且CPU是骁龙、联发科，请下载：ApolloFish\_windows\_arm.exe

若您是Macbook/Mac mini/Mac Studio，且CPU是Intel，请下载：ApolloFish\_mac\_amd64
若您是Macbook/Mac mini/Mac Studio，且CPU是M系列，请下载：ApolloFish\_mac\_arm

若您是Linux或基于Linux内核的国产信创系统，且CPU是Intel、AMD、海光系列，请下载：ApolloFish\_linux\_amd64
若您是Linux或基于Linux内核的国产信创系统，且CPU是鲲鹏系列，请下载：ApolloFish\_linux\_arm

### 运行命令

命令行执行，例如:

./ApolloFish\_v1.0.0\_windows\_amd64.exe

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEBbEI1iaAsU5tPs7r7WhPmicVAU42H9Kv0lFmZNdgj3yUwZGh7nl1049RYSu1KJyWJyv9BAtfoqesQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

首次运行，会在同目录下生成config.yaml文件，并随机生成后台路径、登录账号、登录密码。请前往config.yaml文件中查看。

```
panel:    path: 76cd36b08d6a11c2237f7be87075ce43    port: 3333    username: 9bqz38hz    password: ky9je64t
```

使用浏览器访问平台后台，访问路径: http://127.0.0.1:{panel.port}/{panel.path}/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEBbEI1iaAsU5tPs7r7WhPmicMmrEicaNECSPYoKGFArmvt8YdpibsgCZAvhs7aoWjkfgw3YtDia2NHq1Q/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9JPpNb7icHgEBbEI1iaAsU5tPs7r7WhPmicX2S7lOB75icYN6Ricb6BE8NqJBuGF4uF5CEJl2s0kxADa3bYR5eBxS0Q/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

项目地址

https://github.com/safe1024/apollofish

![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1)

**今日福利**

为了帮助大家早日习得网络安全核心知识，快速入行网络安全圈，给大家整理了一套***【2026最新网安资料】***网络安全工程师必备技能资料包（文末一键领取），内容有多详实丰富看下图！

Web安全👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFBODrmsTGnPTOibdIT9B5eFLTHVIgWzYafxGAesmYnfzrz52xwV3Bjhw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

渗透测试👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVKWl2cLRTq7x9haKJerUZNO0YMhiaO8ibN1jjV0qxNLEvRKMfR90eNjQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

安全面试题👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFgrmaDLaYT1yV5lst9tKC72QrYjd5I8IN7kcOZIZSfQJJz8MdX6a1uA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

代码审计👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFxmUkTNP1iagssZL5zkjID8hibpZsRCj1OnEb4x7ZYWqpiaymSjc8O7vSQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

红队笔记👇

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAkcvc41LgmeFn1B18QpgBZFVZS1mB4MKAo4FoMBGyVSzq38ZXEKJCjZVaTsFtLE7tIJ3zbRWF5xeA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

入门视频👇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgxtiaXGtk7loXV41e8AXiaORJMhqFbrtcfHvJWTia6ME2oSI9msVYJu79uCicb7foufuibEHaVg32XnWw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

以上所有资料获取请扫码

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAmQO922RsJH8oNVNo28hujdEqkbnrZTKI5IXibkbQGT3Es1s6wruZu9giczEsvg0Qr6G06ldEuVGFPg/640?wx_fmt=png&from=appmsg)

识别上方二维码

备注：***2026安全合集***

100%免费领取

（是扫码领取，不是在公众号后台回复，别看错了哦）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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