---
title: Linux恶意软件自动化分析开源沙箱
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490656&idx=1&sn=f15e7959caf5f0e404b6abe35e5afe91&chksm=902fb348a7583a5e7fd0e9a9070584036e06a5534a2b06c7186e68fc41d169556b10b7012ba4&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-24
fetch_date: 2025-10-06T20:36:28.142001
---

# Linux恶意软件自动化分析开源沙箱

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVxlHibSicyJ0YGTzjaf49DicPMI70X1cOASU66EwtH9ibPTLHzBGNwkbPvFbfvwSmsWI5ia0DQx2yyA1A/0?wx_fmt=jpeg)

# Linux恶意软件自动化分析开源沙箱

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

Linux平台上的恶意软件在最近几年都呈现爆发式增长状态，目前在Linux平台上主流的恶意软件包含：挖矿、勒索、RootKit后门、远控后门、僵尸网络等类型的恶意软件家族，分享一些开源的Linux沙箱项目，有兴趣可以自己去实践一下，提升Linux样本的分析效率。

[《基于Linux的僵尸网络构建器，构建高级隐秘僵尸网络负载》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490259&idx=1&sn=c08c2bd9abcefc046bac145ca7cbfe50&scene=21#wechat_redirect)

[《针对一款开源跨平台Linux远控样本的分析》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490489&idx=1&sn=e3f9b98799f83408765ecfd1ad180d55&scene=21#wechat_redirect)

[《Linux数字取证工具与常用命令汇总》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490135&idx=1&sn=f03af96e5629aec61e50ba56fc831114&scene=21#wechat_redirect)

[《UEFI BootKit学习路线与资料分享》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490058&idx=1&sn=8c80dfb3d169392af3a7821398c50637&scene=21#wechat_redirect)

[《盘点全球主流Linux平台的勒索病毒》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489981&idx=1&sn=f92b58bb6a06cfb2d3596dee93f226ab&scene=21#wechat_redirect)

[《Linux UEFI BootKit样本分析》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489681&idx=1&sn=db979eeea2772c3628882e836b8b6c59&scene=21#wechat_redirect)

[《服务器被黑，安装Linux RootKit木马》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247487497&idx=1&sn=53b293cfd25fa88d494b67fd181af498&scene=21#wechat_redirect)

[《Linux版Black Basta勒索病毒针对VMware ESXi服务器》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247487404&idx=1&sn=53a4d2c22acd4edb719d9af1e0f85115&scene=21#wechat_redirect)

[《深度分析一款新型Linux勒索病毒》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247487280&idx=1&sn=6eb2dc3d0b686158e5ce0862cfb2dcd0&scene=21#wechat_redirect)

[《Sodinokibi(REvil)勒索病毒最新变种，攻击Linux平台》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247487064&idx=1&sn=93f788d51b39e7b0e561415f57865cf6&scene=21#wechat_redirect)

[《黑客利用F5 BIG-IP漏洞传播Linux挖矿病毒》](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247486812&idx=1&sn=4a15da8eb901dc78ac95c7afb7e4c002&scene=21#wechat_redirect)

开源沙箱

Linux沙箱

Sandbox for automated Linux malware analysis

https://github.com/danieluhricek/LiSa

Linux malware analysis based on Cuckoo Sandbox

https://github.com/0x71/cuckoo-linux

HaboMalHunter is a sub-project of Habo Malware Analysis System

https://github.com/Tencent/HaboMalHunter

Limon

https://github.com/monnappa22/Limon

IoT Malware Similarity Analysis Platform

https://github.com/mucoze/Umay

Linux Malware Detection (LMD) docker image

https://github.com/Bessonov/docker-linux-malware-detect-monitor

static malware analysis and report tool open source version for linux

https://github.com/zengrx/S.M.A.R.T

An easy to setup Cuckoo environment for GNU/Linux malware analysis

https://github.com/ShellCode33/LinuxMalwareHuntingBox

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

对恶意样本分析感兴趣的，但是没有基础的读者，可以学习笔者的《恶意软件分析基础教程》，基本上是从零基础开始入门恶意软件分析。

[1.汇编语言基础知识必备](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490098&idx=1&sn=ed0be305f2c8c9de0fff326bc45f1ce9&scene=21#wechat_redirect)

[2.恶意样本分析环境搭建](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490186&idx=1&sn=dbccef63b6ad18308eec7ebf88455def&scene=21#wechat_redirect)

[3.恶意样本静态分析-上](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490311&idx=1&sn=3ddb48128acc2772763bd99ba4cf850a&scene=21#wechat_redirect)

[4.恶意样本静态分析-下](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490352&idx=1&sn=7a485e1264bc2f1a221a0822e46ac1c3&scene=21#wechat_redirect)

[5.恶意样本动态分析-上](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490380&idx=1&sn=eab7072e40253f683bc6d1c2e68ac8c7&scene=21#wechat_redirect)

[6.恶意样本动态分析-下](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490447&idx=1&sn=c7cf5c60d80febdcde3d62e977e3b04b&scene=21#wechat_redirect)

[7.恶意样本反调试反分析](https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490541&idx=1&sn=c69072f45da7f28ba4f9d3b1d36842f0&scene=21#wechat_redirect)

对高级恶意软件分析和研究感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族，笔者今年打算深度跟踪分析一些全球最顶级的TOP恶意软件家族，这些恶意软件家族都是全球最流行的，也是黑客攻击活动中最常见的恶意软件家族，被广泛应用到各种勒索攻击、黑灰产攻击、APT窃密攻击活动当中以达到攻击目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVibz1lILTxQIJaB6DqPOSAUghodibssAyprGx5CIumn6vluNfuuF4ia4DU6d2WbGFbFcqO98hgWyuyA/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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