---
title: Windows应急响应综合工具
url: https://mp.weixin.qq.com/s/xVkusYiTGV0PWcH_1E-q5g
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:33:15.953516
---

# Windows应急响应综合工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qkajCoyKpkCpwMpKNBtlialwia2Zf2br9SGuOAUvIJDrOfxLiaibQ4ESIJV6IDGj3j6Hel9MHy75hDs39y8TfYBxbon4XGIxurWnQYuLXMAwZEA/0?wx_fmt=jpeg)

# Windows应急响应综合工具

原创

一个努力的学渣
一个努力的学渣

一个努力的学渣

![]()

在小说阅读器中沉浸阅读

免责声明

本文只做学术研究使用，不可对真实未授权网站使用，如若非法他用，与平台和本文作者无关，需自行负责！

本文涉及的工具排名不分先后，每款都要自己的特色，根据自身情况去使用！

前言

本文涉及的工具：本文只写了windows综合工具，肯定还有更多优秀的工具，如Docker应急、勒索应急、内存马应急等专项应急项目未涉及，后续有时间写

* WindowsBaselineAssistant
* BlueTeamTools

* Hawkeye(鹰眼)
* DarkArk
* WG-Win-Check
* ATool
* FindAll
* Golin
* Windows\_Log
* Baseline-check
* 火绒
* TaskExplorer
* unhide
* BlueTeamTools

windows基线检查加固

* 项目地址：https://github.com/DeEpinGh0st/WindowsBaselineAssistant
* 工具用途：windows加固
* 功能：可一键加固，可自定义规则加固，如等保2.0标准/加固脚本+AI优化=自定义规则

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkB6DQicAbdsF2xnSKiaxc0HkPzn7C99uTiaqdbVPGJGFWOia7TLsXQzJvOUmQLjs3ic37DwarzmiaUG3ODtxUTiaAuduNtaqA4yo9M9hA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDMe64HgBOFPhicpbQ5G5uMcDNHSjQeFeU5mAfO5uHkFcrPRClfgpQd0nRnAPgmPEwTqU2ULtP0GYsN5bb48kPq6iccgcLicunUm0/640?wx_fmt=png&from=appmsg)

BlueTeamTools

* 项目地址：https://github.com/ChinaRan0/BlueTeamTools
* 用途：蓝队综合工具箱
* 功能：蓝队大多数功能都有，比较火，做过蓝队的应该都知道，这里不细说了

+ 常用工具
+ 资产梳理
+ 流量分析
+ 应急响应
+ 日志分析
+ 逆向分析
+ 上传应急
+ 蓝队思路图
+ 安装文档
+ 临时笔记

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkByoMjYHFNbs2OTetZ8dyLibrsJy3mkF9oEGldtSibyoicFfeicS9hUnvwFqIOJl8GsP5jJF21uhhVuaC8oGGVwpo6SMS0rkEwrc9s/640?wx_fmt=png&from=appmsg)

Hawkeye(鹰眼)

* 项目地址：https://github.com/mir1ce/Hawkeye
* 工具用途：Windows安全分析工具，需管理员身份运行
* 功能：

+ 进程信息：该功能能够查看当前主机所有的进程信息包含进程名称、父进程pid、父进程名称、进程创建时间、可执行文件路径、MD5等关键信息，点击相关进程后能够查看当前进程加载的DLL模块信息，并且右键支持进程信息复制以及文件跳转等功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDhw79mGygqeKYHUQLGnmD9Q5JuyVthQRicJYHmLDHbHXk9KYibIL6CN0fKmkFUFgQTR0OX5nNICLMM0yyuorJyYpicNJYianY68fY/640?wx_fmt=png&from=appmsg)

+ 外联助手：旨在发现异常外连后，通过外连ip及时发现相关程序进程以及常见维持项信息，方便进行快速的分析处置的工作

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkC9iaibB9G9GCqobNBiajMicibYlBUCsQsNZPYMWf9mPjIsAlzuRX0TXJ4RFic3P4kqVc1fa9NIhCQn68d5A3WYYpmHR2MdiaAsWr6NBk/640?wx_fmt=png&from=appmsg)

+ Beacon扫描：该功能会遍历当前系统进程信息，并且找出CobaltStrike加载的进程，并解析相关信息

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkARS6fKqoFeP5IRjVK6MN6SbgoW0XLsqWq7t0wcevEFjgrb5un3ib2fZyib9dQDapMoOuWbfiaOO6MaCk5lKiaOlCicFfk96DA4FJV8/640?wx_fmt=png&from=appmsg)

+ 主机信息：

- 用户信息：会标识当前系统存在的隐藏账户，并进行提示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCuxwuk0V38myPBAS3odhib5PsjHRxN8tC5icdu0pc7iadBHHZ2fMlJD5Hx72QKDfJ1BPia33O728LwBhl3hY0YyxwRWZAlhpKGCDA/640?wx_fmt=png&from=appmsg)

- 计划任务：会检索当前系统存在的计划任务信息，并且调用yara扫描模块，检索是否存在恶意程序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCtJWV0xRic1VYArfO9iaNXMhyV9yM6Mk4kKYbARico5ry8J7W0mbJbWC36nHianZoO8ttadF7D3KFSeXPUwwVywqQz36zbPWmHicEk/640?wx_fmt=png&from=appmsg)

- 服务信息、启动项、镜像劫持：也会展示相关信息，并调用yara扫描模块，对这些常见维持项进行扫描

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDxj1ll24wzRQ1JicM6P9jLVzpDulV8DR86Qjwd7cSlXzakfFDEZlUb8rPiaX1qppa1BAE0ZyUpJIf8YDLkfvzItY4cfFDvmk0icM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDCm1LRnpo9gWGib54ricaF19sICRhxLwPvicwnroGNCMGo1hd9GPF9BVDFWoNtAAAVkedVfVx9ibveOW7NdibKtN0BylcWgCjS8oww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCWibtet4pjAe52htWj4TXhicQWESJ5pXickyaHxwFPQoKWYKIic4NPnGP95zR6cjQnjlExXiaPJ1RhPMfzMgqvtl3ibYdsuY4Q7TZg8/640?wx_fmt=png&from=appmsg)

* 日志分析：涵盖常见Windows应急分析过程中，常见的Windows事件，如登录成功、登录失败、RDP登录、RDP连接、服务创建、用户创建、sqlserver日志以及powershell日志等信息

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDNkibkzUU6HdfYEMsngzcwfN8YYbTj0iaGdYiabrORMia3cYXLYdxJP7qoMLhkUOCaiccP2mml3ibQ6ocjpqia9WWZs5Eng1TNgHiaeAU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkAL5P1xmNic9xEQPwicWzPZK18xlDrIDOibpTkkHibHY385CwQz8roDrbBYozAX5obX0GXKEkUzibwdVTt7lC8jMWXo4Y7R72TTibUpw/640?wx_fmt=png&from=appmsg)

* 进程扫描：采用了yara扫描的功能，能够对当前系统进程进行扫描，发现异常风险。若发现异常进程，会将相关信息打印在告警日志面板

+ 该功能采用了elastic security的yara规则，在HawkEye同级目录下的rules文件夹中，用户可以将自己编写的yara规则放在该目录下，文件后缀为.yara，如果在其他目录下放有yara规则，程序提供了输入框，可以根据相关规则路径，进行引入

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBibQDUJBHBF8VTpx1F4Ry4YqCF92zTgKW2yhGTsPTbweb4Cj9kNbsNTZ6YAIibghFmmnBsqKMNYuJiaPBqZeAL5kdKu0ibPgVw3ds/640?wx_fmt=png&from=appmsg)

* 活动痕迹：主机会采集当前系统Prefetch文件、UserAssit以及Recent文件夹相关信息进行展示，方便用户分析主机实现时攻击者通过RDP进行操作的相关记录

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDxHeqPnQfrrib6YPWSC15wYHu5FL786R3xicNw4TeAejTnSfRiaq1pdDibqfK8TPfS8scvLE6mFMmyID0KFnJXdtlAnSSpiaXfvjqM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDLQAmkibfnEaebhE21JwibicOliatyT3N1SkoRLaKwGc0d9B3AJTEPtPOjOWPpo8wSIicyk6icM86YmSKgPLNCic6icfUCKPbzkZKXThY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkA3MCkxzat1n4vJvBndtricwS6xibyAw1J7xYVEtvZ4fx7ns7A4OTKv683RUYjKO0SoyaceyzQwjyB0931aOQ5wSx5iaohnqItkmU/640?wx_fmt=png&from=appmsg)

* 威胁检索：该功能会对当前主机内存进行字符串检索，常用于异常域名外连的使用场景，方便快速定位可疑进程

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCDNBydibn1zJzwMWy61Hqo1kqMJmhBAE5T6fAxL7HiciaZDqqCyxcEzMGdfjLHVgmBPb4XRWROW9wYhAibibLTCqyc4Fic7ySKS45zQ/640?wx_fmt=png&from=appmsg)

DarkArk

* 项目地址：https://github.com/baiyies/DarkArk
* 工具用途：APK
* 功能：

+ 进程列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAjmNAicVuqBgyeIWkYyyrG6zkQAPk2IBlcly0uh2KVnjf7lst9XZeGAueXjfR3k9hwZgw5ozXayoWjFBq5eftNcRhzIqmS7f0c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDZoiaU8sOyvUBnP1Xiay4CGL51FFODaIn32EMdyF5kjjx1qhtSm7pkDX1kc8b4aQf6yia0KsS6K4TT4iayicrLGcMiaIWbIzAib4Xfnw/640?wx_fmt=png&from=appmsg)

+ 内核层：

- 驱动模块

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkA1TDABh0NfL7IHiaibMj2InawoEaiaAruhP0whlnyGkeM9w109LhicqKLibRUNCfHSNOoCT1VY3dylBKRXqiaPfMAckQwlicDnJqNmGU/640?wx_fmt=png&from=appmsg)

- 驱动对象

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkC1rSmUZ4As4CxkFsMeKT9UIUiaCpDlHnibm5ia1FbQMibMB6mgXatwAx2O4VKP0FwZIk2UGWXPFHv3DvE4RpYPj1K3fWRqTjhY9dI/640?wx_fmt=png&from=appmsg)

- 系统线程

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCwNcWqplRKXyhfByfCjXvhIibuCdiaGEFvceZ9SBLWS33t4pIUSujTO1MibTUXURNtc1mRmgV1UDln1EL2h39sbsib7DdicnAZTB3k/640?wx_fmt=png&from=appmsg)

- 系统回调

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBRZjBib2vdH53tGTFcsrjzI1jNBjo9djjpKibZzjIMkjkP3S8D3rdAdFMD74bViaTaWu7rDpOnFkIe2XQIYFBKnjKliaMkz7or0EQ/640?wx_fmt=png&from=appmsg)

- MiniFilter

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCIUX55OxBOVmtXqpTCJ7PvZhJibFrAOicYIfuPhYjWhxaicXJg68190Zlu3pMgWljKib1qJqLpbGQ4bhukV0bOAEdMAsV8icxcWr9E/640?wx_fmt=png&from=appmsg)

- SSDT

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAG9mYRxyCXvtJKN7ApCJyGTw1P04pDlDxSja7eAgXA1VraWTibqaakT8tE8YvEOjVTvypPmp894uWhKTjjp3t96b9ucxO4pHYk/640?wx_fmt=png&from=appmsg)

- ShadowSSDT

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBEoCs5wnhGsYFSRX5ynxPPMfGmwDRN9pp2WxtSVUCibPDWicyLt2uwibklysVRsiauJSSImALPOouZutycGoqCdCc9e9fK6r27Gaw/640?wx_fmt=png&from=appmsg)

- 关键指针

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCvfgxYrptUsydJw9KicJwEVrnV7Ckz8L1VyEfAibrPEsvqrxvOoZya5BanYCTicaYmEp2vy43TeoNhqUXAL7u9wbtVZp3Oo6Gic3s/640?wx_fmt=png&from=appmsg)

+ 驱动痕迹：

- PiDDBCache

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkAyjbbRKNsHfd4renRL4HfMCmQKQLO1bFHSGDicD73Ilvafic5yx7RIk4U6aGxGDib5mn2Z4qwJIibepmGjzH96KyqhxQFPYvlwqZs/640?wx_fmt=png&from=appmsg)

- MmUnloadedDrivers

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCckfULia5HrpjmZib82ayicGabHlmKqYY3qBod51FhXqSVVmZ39CkXu5owbYJBszD3JNzMhHDw2jJQpiahhKcF4dwiakpKqUtyfWMU/640?wx_fmt=png&from=appmsg)

- CiHashBucket

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDaP7ezuERoWQTDy8fBibRDUC3up0U5zSMSyAbGj8jlRw9SUcCRo8TVApv2DxrwtgUIE5iauje6wnGVuJaM5HGQHo0RAnia8tO7TQ/640?wx_fmt=png&from=appmsg)

- WdFilter：蓝屏

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkA0O420vm1yp37icI7rq8zKdULOBthoKn16Hciata313WehiaWSe7ictL4TP3thJKUvmnunmAQEUVcSNt0gFsCxGdXfY3QVSSKRfqE/640?wx_fmt=png&from=appmsg)

+ 窗口列表

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkAfcpLMiaFjpO4LUnRBlLjpmsCFbxg9UnVM1Y1kXqjH84vbrMG0ZubNSXicuiaIiahdvVwPibsmV2zWgddvYaaiamzHnSfT9MnQt6Is8/640?wx_fmt=png&from=appmsg)

+ 网络组件：

- 网络连接
...