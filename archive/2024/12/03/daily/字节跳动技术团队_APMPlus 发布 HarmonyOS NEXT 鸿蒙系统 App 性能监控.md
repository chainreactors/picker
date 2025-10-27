---
title: APMPlus 发布 HarmonyOS NEXT 鸿蒙系统 App 性能监控
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512088&idx=2&sn=bca17e72d31a7fe0cb80e0a409fc9ebb&chksm=e9d37bfadea4f2ec98b6bdb41b069451e5114176b0d37cb74e0e34a462c295a3b478ad916a5e&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-12-03
fetch_date: 2025-10-06T19:40:32.283189
---

# APMPlus 发布 HarmonyOS NEXT 鸿蒙系统 App 性能监控

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiaKnG8I4DiaspborgW0GibQw4UwkLuLP2UicdxuguHHOqOMFbISzsUiaT9V7zp1L8ox5aJQQlheu5UKPw/0?wx_fmt=jpeg)

# APMPlus 发布 HarmonyOS NEXT 鸿蒙系统 App 性能监控

字节跳动技术团队

***新品发布：APMPlus 鸿蒙星河版***

APMPlus（火山引擎应用性能监控全链路版 App 监控）全新推出 HarmonyOS NEXT “鸿蒙星河版”App 性能监控服务，致力于为鸿蒙星河版 APP 用户提供优质的使用体验。我们积极携手鸿蒙星河版生态建设，更是荣幸地成为 DevEco Studio Partner SDK 专区首款 Performance Monitoring 类型 SDK。在此，我们诚邀对鸿蒙星河版 App 性能监控有诉求的企业接入并使用我们的服务。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBqfzomiaI77ZLNyics1SS1s2jEzcpwLFn5zoR5DkFKwKklJav6XKpPMwA/640?wx_fmt=png&from=appmsg)

***极致体验：APMPlus 鸿蒙接入***

APMPlus SDK 可以通过 OHPM 一行命令即可轻松集成，感兴趣的朋友可以查看具体的接入文档：https://www.volcengine.com/docs/6431/1256322

```
ohpm i @volcengine/apmplus@latest
```

```
APMPlus.init(this.context);
APMPlus.setDeviceId("device_id");//可选，设备device_id，不返回会使用内部内置默认device_idAPMPlus.setUserId("user_id");//可选，用户标识，没有默认值。
let builder = new APMPlusBuilder("AppID", "AppToken");//必填builder.debug = true;//可选，测试阶段配置有输出日志builder.channel = "volcengine";//可选，渠道builder.startMonitor = true;//可选，是否开启启动监控builder.netMonitor = true;//可选，是否开启网络监控 后续需要使用HttpMonitor进行监控builder.logRecovery = true;//可选，是否开启自定义Vlog打点回捞能力builder.versionCode = BuildProfile.VERSION_CODE;//可选，应用versionCodebuilder.versionName = BuildProfile.VERSION_NAME;//可选，应用versionNameAPMPlus.start(builder);
```

***重磅上线：APMPlus 鸿蒙应用性能监控***

APMPlus 鸿蒙应用性能监控独树一帜，目前已实现并上线的功能包括：JS 崩溃检测、AppFreeze 监控、Native 崩溃监控、启动耗时、网络监控、自定义事件打点、自定义 JS 错误、自定义日志回捞。我们立足于用户需求，提供了自定义看板、异常报警、单点查询、SDK 上报配置等便捷高效的功能，致力于满足您在业务运营过程中关于用户体验的核心诉求。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZB89IJLibJ1eHXhSXVdOcLEwnWHibd8Qgr0dqWnlZ6xhaoXB045q5RTWNg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dO3QMhRwich9UDhgWN4icpfZ1q5aPM9GkjGGV9JBI9hmTmCt8xcMJ0kmmtzrPoJmluibxLffvX6JO3DQ/640?wx_fmt=png&from=appmsg)

我们后续计划持续为您增强和拓展更多功能，包括卡顿监控、内存监控、磁盘监控等。

**稳定性监控**

实现对 JS 崩溃、Native 崩溃和 AppFreeze 的异常监控，以及不会造成闪退的自定义异常上报，线上问题分析与线下复现崩溃问题给予同样丰富的信息。

* 问题聚合：溃型数据根据堆栈特征聚合成不同的 Issue，方便问题分配与跟踪解决进度。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBt3jB7JJ7YalLdR2TfeI2ibDV9y7Y9PAcW35WfA9El9iaKu1py0u7aibow/640?wx_fmt=png&from=appmsg)

* 堆栈还原：支持自动上传符号表，关联崩溃事件，对混淆堆栈进行解析，定位崩溃文件与行号。

![](https://mmbiz.qpic.cn/mmbiz_jpg/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZB5vWmCLVlkuyMYQ5JyHUgyhZXyJsSsdZTnDvU4ERvsZ0E73Lp4VGnDQ/640?wx_fmt=jpeg)

* 问题分布：支持多维度的问题筛选与聚合分析，堆栈无从下手时，可以尝试聚合分析寻找共性来打开思路。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBxgffwwAGMTd59Ta0jNMMBCHz2teF5uWZQxdh8fIxEfkWw8rCZicArvQ/640?wx_fmt=png&from=appmsg)

* 跟踪日志：支持崩溃时进程 HiLog 日志收集，崩溃原因很可能就隐藏在一行行流水日志中。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBicOzUKy0hzSF0KPicLqWyH9jUkDpmZLWdAwEtXIRQoUj4sicibVoyZ2jOg/640?wx_fmt=png&from=appmsg)

* Freeze Info：AppFreeze 类型的异常数据，支持分析 FaultLog，获取 Freeze Info 信息。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBDLg8viau7EcFvJ9mHGTEjtF9qzjVCeSsIaLlIXYwv244AoBZQZ5OVbQ/640?wx_fmt=png&from=appmsg)

* Tombstone：Native 崩溃支持生成 tombstone 格式的文件，方便参考 Android 生态对 Native 崩溃问题进行分析。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBRBj6CibE4sZ3OicBkcYx9zQCxq9fEx7hanOAF4nl70e2IPjupK9OmgqQ/640?wx_fmt=png&from=appmsg)

* 崩溃日志：支持收集系统 FaultLoger 提供的崩溃信息，可以从 FaultLog 中发掘鸿蒙官方对异常问题的分析思路。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBUbeET1RxTSye97ZZyuEogS8MDNkwJicPwViazLmYa8bLgRCXib61icuYow/640?wx_fmt=png&from=appmsg)

* Native 信息：支持崩溃时环境信息的收集与智能解析，辅助分析资源泄漏等疑难问题。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBkBCkyHY1r9m5AI1e2Z3RbFh7q8icAVpt2rzldxM0arica7sRT9DpI3IA/640?wx_fmt=png&from=appmsg)

**性能监控**

* **启动监控**

启动监控可以监控鸿蒙应用启动阶段的总耗时和阶段耗时。默认数据为鸿蒙系统 HiAppEvent 返回的启动监控数据，SDK 也支持业务自定义启动结束点和自定义节点耗时监控。平台可以有效明确启动总耗时，以及具体在哪个阶段耗时严重。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBKEFRMicBYUibdR4gMicGXkOmFdEDxT3JavpWoO18BkHxIqVGkCw4e0BkA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBQibXjYu0chJ5NGlUCecUoo3peXk38nsfW0bZNQ42d8Deg1aGJz8q41Q/640?wx_fmt=png&from=appmsg)

* **网络监控**

网络监控支持对系统网络库 import http from '@ohos.net.http' 的网络请求进行监控。可以监控 Http 网络请求的成功率和各阶段耗时，有效指导网络优化方向。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBbKs1HL6s9t3dVjx5dCcMVFm8iaOEV6Q02BvhpyQxkv8QCkuv17IdUaQ/640?wx_fmt=png&from=appmsg)

网络详情支持分析每次 Http 请求的成功失败以及 DNS / TCP / SSL /发送时间/等待时间/接收时间各阶段耗时分析。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBjWEH58GrKyPrcupABrYXLjQbicw0kjmdbN4BIxo2AOFibn8tliaYDGPxg/640?wx_fmt=png&from=appmsg)

针对网络错误平台可以有效进行分析并根据错误类型进行分类，查看不同网络错误类型的错误占比和趋势。例如最常见的域名解析失败和 404。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBibqzBBuvL8C4eew4DUYybgpXwzXr8Gb7gqCqyCfukoadyraiaPbNgicicw/640?wx_fmt=png&from=appmsg)

**自定义打点**

* **自定义事件打点**

平台除了有自带的性能稳定性指标外，也支持业务通过 SDK 上报自定义指标，进行指标观测和维度分析，有效扩展了业务的监控范围。例如监控某次图片加载是否成功，某次广告播放是否失败。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBDfd0IxeOU3VxPFflQu1S0icFCQeUaumvr71GicnDCPJyBHQsficM499Ag/640?wx_fmt=png&from=appmsg)

* **自定义日志回捞**

针对单点问题分析，平台提供自定义日志的能力。可以通过回捞，用户反馈按钮主动上报，崩溃时上报来获取自定义日志分析用户问题。日志文件在本地加密、压缩保存，利用系统 mmap 机制保证日志写入的效率并保证数据不丢失。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBdVFib8y7H6AVZyV5y4c5l3qc0YF3ZHBrCCyVR0D1SeDIGicZb6csLAPw/640?wx_fmt=png&from=appmsg)

查看回捞获取的日志辅助分析问题。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBYj9rN7lIrZRLbYdhnibYA5P1anFrlDuphKt6k9sibvAFexNiaoEnMLGgg/640?wx_fmt=png&from=appmsg)

**平台能力**

* **自定义看板**

自定义看板支持业务根据自身诉求灵活配置指标的不同图表展示形式。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBibkbY22OGvrmNAldE0D1r46FNGSll2Q3dGT7lbqXuicZwkR5rcVrSiaQg/640?wx_fmt=png&from=appmsg)

* **日志查询**

日志查询可以根据 DID 和 UserID 单点查询由 App 监控采集到的所有性能稳定性以及自定义数据，辅助分析单个用户反馈的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBRmZQGSmxOMwCWxWibgYcFdbO7sMLRU6jFbBpbloqfr1KdSVed3yxzxg/640?wx_fmt=png&from=appmsg)

* **报警管理**

平台支持针对崩溃和事件等指标可以设置报警任务，在数据满足报警策略后，会通过配置的报警方式进行报警通知。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZB1e1wws5Diciaa1BSzawG9PXXY1U3jATv1cZyUPA8jXRSJaqY01VpZn1A/640?wx_fmt=png&from=appmsg)

* **SDK 上报配置**

SDK 上报配置功能支持按照业务需要来配置 SDK 功能是否开启，采样和阈值。崩溃异常数据不支持采样，其他数据都可以通过采样进行配置，业务可以通过降低采样来降低成本。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBopkvWGyXCiahtg3KU5EqMHff1feBRkptL41nfkcrnLoLQcdK2UfB6BA/640?wx_fmt=png&from=appmsg)

***致力服务：APMPlus 产品平台***

火山引擎应用性能监控全链路版，为您提供针对 **Android、iOS、鸿蒙、Web、PC****、****服务端**等多种平台的应用性能监控服务。我们致力于助力团队优化产品，打造完美的用户体验。通过对海量数据的聚合分析，我们能够协助您发现并处理多类异常，妥善应对各类问题。此外，平台具备包括异常分析、多维度分析、自定义上报、单点日志查询等众多丰富功能，以满足您的需求。我们对内服务的大型应用包括**抖音、今日头条**等，对外也为**作业帮、Keep**等优秀企业提供了服务。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dO3QMhRwich9UDhgWN4icpfZ1Oja71gjF3oMhKrWgpPtQVhCgTOy27EKOQT7k8YBDHV6tcZ3fNqDTFQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBRLbgxseic2K0c6OwEBaOKeSCRJ7WDXM58IxVEF8wzRQ2F4naErZicknw/640?wx_fmt=png&from=appmsg)

至此，火山引擎应用性能监控全链路版已开启全新的**企业助力行动**，我们满怀诚意地邀请您**免费试用**。期待您的加入，一起感受我们的产品，共同打造卓越的应用体验！点击链接，立即使用。

![](https://mmbiz.qpic.cn/mmbiz_png/x1nibL49E8dMwZ3Pc3IPiaAQ9WuSLEic9ZBZs7ObPWVaicibQE6DRGpdibhd7KYp1ohVowe0UgKbLWR30r5l7TwJgiazg/640?wx_fmt=png&from=appmsg)

火山引擎依托字节跳动内部大规模技术实践，推出了应用性能监控全链路版（APMPlus）、托管 Prometheus（VMP）、云监控等可观测产品，致力于为用户提供全面、智能、高效、易用且安全的全栈可观测解决方案。欢迎咨询了解。

🔗 **相关链接**

**APMPlus：**www.volcengine.com/product/apmplus

**VMP：**www.volcengine.com/product/prometheus

**云监控：**www.volcengine.com/product/cloudmonitor

![](https://mmbiz.qpic.cn/mmbiz_gif/x1nibL49E8dPs3JB0eVGibDel9wN3B6fQrSwo6SPMP3oF0zCnRQGFysE02rWJqzLurRJgaU3mJhyp92pktHNVHuw/640?wx_fmt=gif)

**了解更多产品信息**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队...