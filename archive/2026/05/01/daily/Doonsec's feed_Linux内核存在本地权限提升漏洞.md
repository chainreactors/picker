---
title: Linux内核存在本地权限提升漏洞
url: https://mp.weixin.qq.com/s/f6S9x1G5KL1nP_owZlkfsA
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:55:22.450390
---

# Linux内核存在本地权限提升漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/V1icTKBjMOiasbszLmVgt05UibDflDjIm6tmQUZ1ibKoiaefvYCfDFrL5dqsBM5a7YsnEqNIo5icNPKsIDhMGWgJwax8rH16uqqoibuNgnAiarnJnzQ/0?wx_fmt=jpeg)

# Linux内核存在本地权限提升漏洞

原创

guowei
guowei

网络安全直通车

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V1icTKBjMOiavbiarlwQ3Rc8KxelDz1Zg9t2yvu3HRduWov9uHicbbSRMlRBrb3x3TKA6dSHic5nia3OHgxq04NdgtUkHWAW6OqvoO4IibSGn4xTE8/640?wx_fmt=jpeg)

漏洞概述

漏洞编号：CNTA-2026-0002（CNVD-2026-19044，对应CVE-2026-31431）

发布日期：2026年4月30日

漏洞类型：Linux内核本地权限提升漏洞

危险等级：高危

漏洞详情

Linux内核加密子系统存在逻辑处理缺陷，本地普通权限用户可通过组合AF\_ALG套接字和splice系统调用，向可读文件或SUID程序的页缓存中写入4字节数据，从而篡改setuid等高权限进程，最终获得root权限。

影响范围

受影响系统

默认启用或可加载 algif\_aead 模块的Linux发行版：

Ubuntu 24.04 LTS及以下

Amazon Linux 2023及以下

RedHat Enterprise Linux 10/9/8及以下

SUSE 16及以下

Debian、Arch、Fedora、Rocky、Alma、Oracle等同期内核版本

内核版本范围

受影响提交： commit 72548b093ee3 ≤ version < commit a664bf3d603d

未受影响版本：内核主线7.0+、稳定版6.18.22+、稳定版6.19.12+

高危场景

共享服务器（多租户主机、开发机、跳板机）

Kubernetes和容器集群

CI/CD执行器（GitHub Actions、GitLab Runner、Jenkins等）

处置建议

根本解决方案

立即升级至官方修复版本：https://git.kernel.org/stable/c/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5

临时缓解措施

禁用algif\_aead内核模块

通过seccomp或运行安全策略，阻断容器内AF\_ALG socket创建

重要提醒

漏洞利用代码已公开

安天公司报告已发现漏洞在野利用情况

特别建议云服务器、容器宿主机、多租户环境用户立即采取行动

该漏洞对云计算和容器化环境威胁较大，建议相关管理员优先处理。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/J8AVIknUyQlKATmLAFibRG7DezjkNIEqbwEYR0fRY4WYibs8SZ8CtNC2NZHEu3nicHJx1rVoe96v4XZDpdRJ2aWbQ/0?wx_fmt=png)

网络安全直通车

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/J8AVIknUyQlKATmLAFibRG7DezjkNIEqbwEYR0fRY4WYibs8SZ8CtNC2NZHEu3nicHJx1rVoe96v4XZDpdRJ2aWbQ/0?wx_fmt=png)

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