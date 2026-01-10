---
title: YunSeeIRs 应急响应工具
url: https://mp.weixin.qq.com/s/8rYikWRmFqVNSb5xpng6zg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:28:08.046571
---

# YunSeeIRs 应急响应工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nNzOrpxNkNObVhYKCdLz426GQlW5m72O8ibSDjwDB4BU5J5Hicl5Yd7AKUKywUG7gUeXwa7ibtuGAiaG0YjEQzBgvg/0?wx_fmt=jpeg)

# YunSeeIRs 应急响应工具

原创

江思澄

云晞科技Sec

![]()

在小说阅读器中沉浸阅读

# YunSeeIRs 应急响应工具v1.1

**原作者：https://github.com/Tokeii0/LovelyERes**

本项目基于 LovelyRes 进行二次开发，在原有架构基础上扩展了多项核心能力。新增流量分析与数据库管理功能，提升系统在应急响应与运维分析场景下的实用性；引入“茉莉花绿”“滑稽”两套主题，完善多主题视觉体系；新增 SFTP 文件上传功能，实现远程文件的安全传输与管理；同时扩展对多家 AI 模型厂商的支持，并统一输出为 Markdown 渲染格式，提升结果展示与可读性。

## 修复

本次版本更新对系统稳定性与交互体验进行了集中修复与优化。已修复命令执行中 `sshd_config` 快捷方式异常、AI 解释功能接口调用失败、仪表盘状态与远程服务器实际状态不一致等问题；解决 AI 输出乱码及输出模态窗口颜色与字体对比度不足的问题；修复部分厂商 Linux 系统下 Docker 容器兼容性异常；优化窗口关闭、最小化、最大化触发区域与图标偏差；同时修复新增服务器后出现的卡顿、闪退以及流量分析模块存在的漏包问题，显著提升系统稳定性与可用性。

## 主题

**浅色**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OzWpYuCBQkfr8BiaBwU7KiaJSFhd1W93XsjTdVRZy5jMUa1lgqZ1PRsIg/640?wx_fmt=png&from=appmsg)

**深色**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OFlKVmDToFgoT7umUB6fPQgAp6kiaWgShURjFUE0uzJeuvu2KzXiaD0DQ/640?wx_fmt=png&from=appmsg)

**樱花粉**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OpQzaT0Yz9pu9DXqX8yMAT19TxOXQiaOC5uvB3icZvAibp1rgAjMpMPDPQ/640?wx_fmt=png&from=appmsg)

**茉莉花绿**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OakB9FZoiaaOb6geNWibSkErvKm2ickm9oibzNgbYefzzemFL7gaETxrRpQ/640?wx_fmt=png&from=appmsg)

**滑稽**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OWdj6Yxm5AWRgzyicuMC7q9cafmIn8AwfPSwax3pplKgRQCkk5tSV7ww/640?wx_fmt=png&from=appmsg)

## 仪表盘

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OCtQ9a0Cl2cPnXfyJXXiaDGhQSIUtRUFGhZ2XM9VjCecp1ExfzvT0Mibw/640?wx_fmt=png&from=appmsg)

## 系统信息

**进程详情**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OKv6Z2t3lu8pqqDqPXicypZ29WzummHoyPPdkaDicMUpgYn9LDd1Vh55w/640?wx_fmt=png&from=appmsg)

**网络详情**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OZA8DskFwfYMeqzD1TegdKnJGg7r15MptxcgIib1DvmXibG2f99u7kt9w/640?wx_fmt=png&from=appmsg)

**系统服务**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72O7ECtrlNh0gNe4gWmRDsx1dsABGr3GbFgodDRMNCNW57rspPNTWia9nQ/640?wx_fmt=png&from=appmsg)

**用户列表**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72ObIWFpnvq4XyRDMVXEVBw1gAViac5ngCPDU3H7PB5HKQqPcuFia3P00pA/640?wx_fmt=png&from=appmsg)

**自启动**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72Ofs3zWjRYQJxhmW4AVM1EVRrrlmnDjnvjTqpYnUx3nibiaPmSVhztBZsw/640?wx_fmt=png&from=appmsg)

**计划任务**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72Ofs3zWjRYQJxhmW4AVM1EVRrrlmnDjnvjTqpYnUx3nibiaPmSVhztBZsw/640?wx_fmt=png&from=appmsg)

**防火墙**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OI8QBictJPC6NCSyJdjVePx6CjgCHoibUIWebibAlJRpCPYSoQicCyVk5yQ/640?wx_fmt=png&from=appmsg)

**AI解释**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72Owbfqxa8Ic8yd3aQGKXp7viaT4CGp5Hf4QHynDdtYb0W37xTSWer5SbA/640?wx_fmt=png&from=appmsg)

## SFTP文件管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OL3eicFVKcCDU5JlcmBdp2I4wibrkuBOQGvtib4RRCg6zjnyunI6kY4ADQ/640?wx_fmt=png&from=appmsg)

**文件上传**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OzM3K0RA4GVN3e0B0Kzyicpf8pW6Lhay6EkpGUiccknmgbzfdAZHzF1CA/640?wx_fmt=png&from=appmsg)

**新建文件**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72Oh2Mf6EFq8RYeA5cZ7ibK1bJtlD4kxq32rZud7FKQgcVEYzeC5L5dc7Q/640?wx_fmt=png&from=appmsg)

**文件智能分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OPAKLwIINuiawERD5RZNwP5TUT3px71MKDub4eLdTeu4t0MXibyzrCeFQ/640?wx_fmt=png&from=appmsg)

**AI智能解析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OlibH8KuTkXBiajftfBQOPQIlLkQBiavgrObR6Rib4F6UvYZV0oluq9nIfQ/640?wx_fmt=png&from=appmsg)

## Docker容器管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OrOPeoScQTqicfANL2YpBiaM6WvXvpUdGF7EstP5c4SrxE4WyMoye1f2Q/640?wx_fmt=png&from=appmsg)

**快捷命令执行**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OocHHAzeAdNP9kMc5b5cHiaT6GSM8g8FB8BChWiaZMZJfLib5osqrbLj0Q/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OuP5IWxPlRyia6bsK7tOeTAvSibibz2Jttk7v9ibO91uUZibF5GLheMJYiaWQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72O7fdEA19cTEdrVD6SMl7kRHjdUDN2HvhSicv6sCQNYCGLZAWoBcDUPXQ/640?wx_fmt=png&from=appmsg)

**快速检测**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OCHicTicU5eRUDThg7ia8kSeXMibh60jd799YIPrw0BJU8cq2JJOraE1LdQ/640?wx_fmt=png&from=appmsg)

**详细检测报告**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72O98XpF8gHoaZPm8psm7PiaLM2J6NdFEKFZClPQgA1Z6jI97t3gJWnia7A/640?wx_fmt=png&from=appmsg)

## **数据库**

**支持多种数据库连接**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OqTVSeZPKPgVKN5mkx13OYXfg1maLLFOPliaU5yqxGwdHiaM6ia2rbqlJg/640?wx_fmt=png&from=appmsg)

**支持对表增删改快捷操作、自定义查询命令、数据库运维快捷指令**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OMuDXNBC2ChyvgkoaRR2hDq5ZaR1o4MUJdbECtM66LWzvp6dbWyerIA/640?wx_fmt=png&from=appmsg)

## 日志审计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72O7x97hprgvRpQkGc9UJu0RbzPB6M20OJ6g4DgF7xwEQ0qfo59CagnTA/640?wx_fmt=png&from=appmsg)

**AI智能解析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OeYAfHWxMcd0iangaeibLfDia4AAdhe5N80IHLL4ANE4fpISN58hkOOdiaQ/640?wx_fmt=png&from=appmsg)

## 流量分析

**网卡选择**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OOfMxOo0ibPncqYDU3OyX3XxEKZu62fEW9Bu9tf6wX7lXT1hw2Ww9Dmw/640?wx_fmt=png&from=appmsg)

**流量捕获**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72Ot7sDbKM2wkvmqJuq5n9ziaSHp7y3vzIYORv3Br3LhzzoqNxcSQ7z8aQ/640?wx_fmt=png&from=appmsg)

## 终端

**命令建议**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OFzcpLJ7ALFMGACJZ6m7ibMd17fTzwft8SvqVIHKl1XrCzQGT1fq6FVg/640?wx_fmt=png&from=appmsg)

## 设置

**字体设置&语种设置**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OPP9PgMNJgt1lDc1Ip2evliaG30mNwUCLjLiac9JBpl34c2Syib18mAufQ/640?wx_fmt=png&from=appmsg)

**AI设置**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNObVhYKCdLz426GQlW5m72OtIic5vHxNQ9hCjjMlFmH9FJM8duZp1vlwcGgnc4icGVVnsIPtLWiaDNxw/640?wx_fmt=png&from=appmsg)

## 下个版本

新增RDP、SMB服务管理【适配Windows】

新增Windows日志分析&AI分析

新增华为、锐捷等厂商的交换机、路由器、防火墙网络设备连接【SSH、Telnet】

**项目链接：https://github.com/achenc1013/YunSeeIRs-lssue**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nNzOrpxNkNOQiaOLicMMFN0n4GLtcibHmWJsEptFGGEWyUCBKvGjHoOibhy4SdsG0qjqSF4mRI6Azguzqicee2Mj0cA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNOexrWpDgDYXpYTLbLrl7RhtCuwTAdmvLKiaF0kN9rgKnvsq0GYhnCY3w34I63n5U9ocibeG87eFCqg/0?wx_fmt=png)

云晞科技Sec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNOexrWpDgDYXpYTLbLrl7RhtCuwTAdmvLKiaF0kN9rgKnvsq0GYhnCY3w34I63n5U9ocibeG87eFCqg/0?wx_fmt=png)

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