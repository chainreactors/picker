---
title: 字节跳动云工作负载安全防护平台：一套方案覆盖主机、容器、K8s、Serverless 全场景
url: https://mp.weixin.qq.com/s/Lj0q81sbRJdESRh63MNURQ
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T07:01:09.406403
---

# 字节跳动云工作负载安全防护平台：一套方案覆盖主机、容器、K8s、Serverless 全场景

# 字节跳动云工作负载安全防护平台：一套方案覆盖主机、容器、K8s、Serverless 全场景

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全规范声明：本文仅做技术分享，请严格遵守当地法律法规，将相关技术用于正当安全防护场景。

## 重点导读概述

Elkeid 是字节跳动开源的云工作负载保护平台，核心技术架构覆盖主机层、容器层、K8s 集群层、Serverless 层。该项目源于字节跳动内部安全运营实践，核心组件经过海量业务数据验证。

## 重点导读架构

![架构图](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Up4SkB5HVhbrl707OWWNalnqfbMtfDFq0NuoUburJNzicsJh7kGBTemOssJRbADcOYhGVVU8jl5MnmMJqa0lYd285grrM8jmZicI/640?from=appmsg)

架构图

## 重点导读主机端能力

### PART 01Agent

Linux 用户态代理程序，负责管理各类插件组件，与 Elkeid Server 建立通信通道，实现配置下发、任务执行、数据上报等核心功能。

### PART 02Driver

Linux 内核模块，部署于系统内核层，采集内核态运行时数据，支持容器运行时识别，可检测常见 Rootkit 行为特征。

### PART 03RASP

运行时应用自保护探针，支持 CPython、Golang、JVM、NodeJS、PHP 多语言运行时环境，采用动态注入机制，无需业务重启即可实现运行时安全防护。

### PART 04Agent 插件列表

| 插件名称 | 功能描述 |
| --- | --- |
| Driver Plugin | 管理 Elkeid Driver，处理驱动层采集数据 |
| Collector Plugin | 采集主机资产信息、用户列表、计划任务、包管理信息 |
| Journal Watcher | 监控 systemd 日志，采集 SSH 相关日志 |
| Scanner Plugin | 基于 Yara 规则进行静态恶意文件检测 |
| RASP Plugin | 管理 RASP 探针，处理运行时采集数据 |
| Baseline Plugin | 基于基线检查策略进行安全风险识别 |

## 重点导读后端服务能力

### PART 05AgentCenter

代理中心组件，负责与终端 Agent 建立通信连接，接收并处理 Agent 上报数据，执行 Agent 升级、配置修改、任务下发等管理操作。

### PART 06ServiceDiscovery

服务发现组件，后台各服务组件向其注册并同步服务信息，确保各服务实例相互可见，实现服务间直接通信。

### PART 07Manager

管理平面组件，提供后台整体管理功能，暴露查询与管理 API 接口。

### PART 08Console

Web 控制台前端，提供可视化安全运营界面。

### PART 09HUB

规则引擎，支持与外部系统联动对接，实现检测规则扩展。

## 重点导读功能支持

| 功能模块 | 社区版 |
| --- | --- |
| Linux 运行时数据采集 | 支持 |
| RASP 探针 | 支持 |
| K8s Audit Log 采集 | 支持 |
| Agent 控制平面 | 支持 |
| 主机状态详情 | 支持 |
| 资产采集 | 支持 |
| 容器集群资产采集 | 支持 |
| 告警白名单 | 支持 |
| 病毒扫描 | 支持 |
| 插件管理 | 支持 |
| 系统监控 | 支持 |

## 重点导读前端展示

**安全概览**

![安全概览](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UrYib96jibmJ4GTLcIf1RUicvYkAfKS0oJicCVoJ5oVHIjFGRHHdpX8Alc4eaXbuzJ6swNJqhPDkWGtzsgBBRNfmN9O1HbJzicXibr6M/640?from=appmsg)

安全概览

**K8s 安全告警列表**

![K8s安全告警](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Ur6JQsLEPLmX9mQQCsHDXkusxqrmAasKlDybU0X5D3PLlCL1ibT7aHXx8gd0k0mDjhulMPgSRutLCrAniaNeWibEKYGApeyK3nKEQ/640?from=appmsg)

K8s安全告警

**K8s 工作负载信息**

![K8s工作负载](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uouz3YeIevIOZibdpX1TlX6RpclJPztnRbJDib6QaXryeUiciblHRbV2hIJJMfNkDk7diaCsj1uOLns0Qiciae92eqze4IprqCrUCrjp0/640?from=appmsg)

K8s工作负载

**主机概览**

![主机概览](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrWQZavxvExNmb334Ht6MaRG2DzFZMREabuwAia5UclKuTS78Q8wKvp9D1uouJl4QybMUmkjg9WBTpbl8DabHdFR9hWaPCb1jvU/640?from=appmsg)

主机概览

**资产指纹**

![资产指纹](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqKvL8DFxTmMRiaMoQTYbt9faVqm9ufDlzsaVicAcQAkSaHdTibbktuvVwEvIwKpJNiccGGhiarykydAE7CXttFtqRqJ9ibib28NnX2ak/640?from=appmsg)

资产指纹

**安全告警**

![安全告警](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UpmU0wMZTjkhiaSKx57MsfR6LKe25ya9cupsOaqKAgbsUmRWP4RuUMbnBX5iaeYF05UmYUzYtwrg1NGQ3NjUMc30mx4fHZNnY4WQ/640?from=appmsg)

安全告警

**漏洞信息**

![漏洞信息](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UoorSFRKYZHF84SGxpR7BLf2UkaxGQIedDHicnrTt4LOfHLiaThZbpqkRA2vYtuLw8OKVwibRGOn4O6KuCHGFYkvx69N64GWMeccI/640?from=appmsg)

漏洞信息

**基线检查**

![基线检查](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uo8XBOs0QNophiaKN7zVeZGW0EmmZIJzknjTlCSvA3mFppgsqJzMTTMwYrIIgWBVahD5vEcTAaeEGkKtJuhRpnibAVAn8Rg4hKME/640?from=appmsg)

基线检查

**病毒扫描**

![病毒扫描](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqsS6BU35VwJePSicq5j5Rf0ZPaVOqNlqQXYa4fVn2m5V1k5bv7awCELyrYQRVicNu8y7r49aJxGicDI0d31DXdLet7zHHjw5lGSY/640?from=appmsg)

病毒扫描

**后端监控**

![后端监控](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqg18sYoLVaJJOIGXGNStYxUGJbxRUQH3BMtk6k0Z1gP4UI7bQzlHxLukJ1vmkhlibKGhwualhebzBEMOryib2micckDAsuXibiaicOc/640?from=appmsg)

后端监控

**后端服务监控**

![后端服务监控](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UqANvZE1XJte4zWa7CbzjDqmicW2EjpOkn4ykSgCK0rN9ibRFjKOjicicQIvcm8ZlT3KuibWKibxaq3V8xELkSDOMmCk9ib7C9YOibicRFo/640?from=appmsg)

后端服务监控

## 重点导读快速部署

项目提供 Elkeidup 工具实现快速部署，具体操作可参考项目文档。

## 重点导读开源协议

| 组件 | 协议 |
| --- | --- |
| Driver | GPLv2 |
| RASP | Apache-2.0 |
| Agent | Apache-2.0 |
| Server | Apache-2.0 |
| Console | Elkeid License |
| HUB | Elkeid License |

本公众号非项目作者，仅做技术分享。

本文介绍的项目开源地址如下：

```
https://github.com/bytedance/Elkeid
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UoRzdW8ClQCm22PzIMibib4tUA2aVS9XMftg9UKf2vbiaef0JHgicib51F0Ss8TiaJnyELqwMJn47stpCtDqFPe6RnT9NT6jUm4iaaUNk/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UplpgMKh41r9D2ssibD1DhA6UHTWGZf5bzQwdL2lNpOKBJ4qsKpy1dpZTeKN7W4DG8g3SibibWSXseFpjsEH1UhbdpzuPGqmiaFBUo/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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