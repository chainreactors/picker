---
title: 【勒索预警】用友 BIP 高级版疑似0day已被rox勒索病毒利用（附IOC）
url: https://mp.weixin.qq.com/s/LnMzZYU9Qi1y31467GX9bg
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:44:21.799137
---

# 【勒索预警】用友 BIP 高级版疑似0day已被rox勒索病毒利用（附IOC）

# 【勒索预警】用友 BIP 高级版疑似0day已被rox勒索病毒利用（附IOC）

原创

州弟学安全
州弟学安全

solar应急响应团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/DxUXemrrntp3gibjPSCHmSEpdPDqfBcXT5e151v5AJSbV5JtaALLzQe0I1Jibbet7rTia8icjmgo5r4hpY3IMpYPIw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

## 写在前面

本文首发于**Solar应急响应团队「州弟学安全（徐龙州）」**，转载请务必注明出处。

Solar应急响应团队由思而听（山东）网络科技有限公司组建，长期专注勒索病毒应急响应、攻击溯源与数据恢复，为遭遇突发勒索事件的企业提供7×24小时突发危机干预通道。如企业正在遭受勒索攻击，可通过应急响应.cn（**https://solarsecurity.cn/****）**或应急响应.com（****https://www.solarert.com/**）**联系我们。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbAVSXyxtemt8X15KYfricSaOU7A0BndYXDjo9F8KTeAOxhJPDNFYIM8P80Nia7lXpiaeHqKsOchw4uiau0L1ialvYznxzavTiccpsoI/640?wx_fmt=png&from=appmsg)

应急响应.cn平台Weaxor勒索家族特征查询，标注家族名称、加密后缀、勒索信样式等关键字段

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQaIlme9x9oS2sRZbokibfXAfdLdJwzKnznPU0u3sgXyRj9vI39xGFibQF1ZCiadnbo4gx7yrVX2Zs9CQAYoshMiadtR4DnT6IPmicmU/640?wx_fmt=png&from=appmsg)

应急响应.com平台Weaxor勒索家族特征查询，标注家族名称、加密后缀、勒索信样式等关键字段

自今年6月以来，我们持续跟进weax勒索病毒在国内的多起攻击事件。近期，该家族已将加密文件后缀改为 `.rox`。在此前发布的畅捷通T+案例中，我们已对这一变化作出预警：

[【勒索预警】首发，weax勒索病毒针对用友畅捷通T+应用0day攻击溯源全流程（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247514452&idx=1&sn=d867ab55ab867712051db21537d641ef&scene=21#wechat_redirect)

围绕tellyouthepass（sorry勒索病毒）、weaxor等相关勒索家族，我们也持续发布过溯源分析。建议结合以下文章阅读，了解其攻击手法的延续与变化：

[【全网首发】Weax与Sorry勒索病毒席卷全国中小企业，深度还原全链路攻击，疑似黑客利用AI挖掘管家婆0day漏洞](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247510579&idx=1&sn=c8ddda3466a9fc0b75f1121ad96b24c4&scene=21#wechat_redirect)

[【勒索预警】某ERP曝0day漏洞致Weax勒索病毒在国内爆发，波及资产近4万台（合并修订版）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247511937&idx=1&sn=0b2a89e4a0ab893a71eea71c15d14305&scene=21#wechat_redirect)

[【勒索预警】警惕！Weax勒索病毒改用国内IP发起0day攻击，某地产ERP遭加密，完整溯源复盘（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247512969&idx=1&sn=bc8ace54cffcaf17252e7c8da0ecb05d&scene=21#wechat_redirect)

[【勒索预警】快转发！某财务ERP曝最新0day，Weax勒索病毒携杭州代理IP再次爆发，全网同类资产超十万，完整溯源复盘（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247513584&idx=1&sn=fa69a8b7da95745e00e2eab6b51e3372&scene=21#wechat_redirect)

[【勒索预警】万字溯源分析，weax勒索病毒利用国内代理IP对某ERP使用通杀0day攻击勒索，影响资产近4万（附IOC）](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247514230&idx=1&sn=3840a5b7d9b816623db17acb8a609894&scene=21#wechat_redirect)

本次案例的入侵入口指向用友 BIP 高级版 `sprmonitorservlet` 接口的Java原生反序列化漏洞。

通过日志分析，10月17日，攻击者利用该漏洞上传第一枚WebShell；18日早上8点，再次上传一枚采用加密通信的木马；18日20时起，我们处置和接到的相关案例中，互联网暴露的用友 BIP 高级版陆续出现勒索中招情况。

此前，我们曾推测勒索家族可能借助AI辅助挖掘0day。本案呈现出先打点、再验证、后加密的时间衔接，且前后使用了两套攻击基础设施，使“漏洞详情或已控目标权限在不同人员之间流转”的可能性进一步上升。但这一判断仍属推测，后文会列明依据和证据边界。

**阅读说明**：按照惯例，本文不公开受害单位信息，只分享主服务器的溯源过程与攻击者思路。为避免攻击代码被滥用，本文不公开完整PoC及可直接利用的载荷，相关技术细节以说明原理和辅助排查为限。

## 一、事件概述

2026年10月18日20时36分，某企业用友 BIP 高级版主服务器开始被批量加密，共150,411个文件被追加 `.rox` 后缀，业务中断。加密器落地前，主服务器已分别于10月17日凌晨和10月18日上午出现两轮漏洞利用与WebShell落地记录。

用友 BIP 高级版运行于Java环境，正常情况下主要留下应用日志。本次现场未部署安全设备，也没有中间件访问日志，应用日志又只记录异常堆栈，不记录请求URI、来源IP和POST请求体，因此无法直接还原完整攻击请求。

本次分析以应用日志中的异常时间为起点，与Windows PowerShell事件日志、文件时间和系统痕迹逐条对齐，最终还原出三轮漏洞利用、两枚WebShell落地及勒索加密的过程。下文仅围绕主服务器展开，时间均为北京时间。

## 二、详细溯源过程

### 2.1 10月17日05:02，首次异常与漏洞试探

10月17日05:02:59，主服务器 `fw-log.log` 首次记录 `####sprmonitorServlet Exception`，异常类型为 `java.io.EOFException`，调用位置位于 `ObjectInputStream` 读取序列化流头阶段。

这类异常说明接口收到了不完整或不符合预期的序列化数据。结合38秒后出现的完整利用异常判断，该请求更符合正式利用前的试探特征。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQbicQnarSVgKv3kWggNlDKVcG3Z9ffhjVlriaZvboc1LI1By40XGjPibS4vqQOiaN45Txn1tNxqibYZG6LOo5nicEyA5QvCrpiad7XTCg/640?wx_fmt=png&from=appmsg)

主服务器首次出现 `sprmonitorServlet` 异常，时间为10月17日05:02:59

### 2.2 10月17日05:03，第一枚WebShell落地

05:03:37，应用日志出现 `####requestEntry Exception`。堆栈显示，`Hashtable` 在原生反序列化过程中触发 `JtaTransactionManager.readObject`，随后向 `rmi://8.130.77.216:1099/x` 发起JNDI查找，对端返回 `javax.el.ELProcessor` 对象。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZIia5Rkdiaucl5Vy2SumwsgpY5qKVkg9bpxBaPbRibEU51ztQnw9bXMdTHwlIaUpdfFDofwRCa6lDQOzbPnjHXXTNehHyn0UbcpI/640?wx_fmt=png&from=appmsg)

应用日志记录JNDI回连地址及 `ELProcessor` 返回对象，与后续命令执行时间相接

仅1秒后，Windows事件日志记录PowerShell执行。命令先从Java进程路径推导应用目录，失败时再遍历多组常见安装路径，随后从 `8.130.77.216:18888` 下载 `ncsync.jsp`，写入 `webapps/nc_web` 目录，并将落地结果编码后回传。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQakBzE3rOByPFJ72MZXialel3BEGBDdhj5BUXibIkbCFUIMdRFoMU0wympoVicgvia6xq2gP1dLBLv5xuprp3Iq5ibzJRiadFTbGEAa8/640?wx_fmt=png&from=appmsg)

10月17日05:03:38，主服务器执行PowerShell，下载并落地 `ncsync.jsp`

对 `ncsync.jsp` 分析发现，该文件通过自定义 `ClassLoader` 加载内嵌的Base64类字节码，再反射注册 `/ncsync` 内存Servlet。其字节码包含密码验证、Windows与Linux命令执行分支，属于跨平台命令执行型WebShell。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQapxduuabxEwLlqLTxoUdaNcXYWU6kKCyEJODUUFZwhvMS7BfrpLFK0GAL3tLWwyyHlcHM6LZibiatQiaMwe5JviaY6SgZFMRHaJpo/640?wx_fmt=png&from=appmsg)

`ncsync.jsp` 内嵌Base64类字节码，运行时加载并注册内存Servlet

文件检索结果与事件日志相互印证，`ncsync.jsp` 的修改时间为10月17日05:03，大小为7 KB。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQbDooYoiboG7xG2akXMmtDCmcMwFYUOA7kjejwzXFyAWbI7uLogaDj9VUNsmm8OAR9ZzgeJwClzNsicxia4Y6SlzOiapRBqH8cauz4/640?wx_fmt=png&from=appmsg)

文件检索确认 `ncsync.jsp` 已落入应用目录，时间为10月17日05:03。

### 2.3 第一阶段基础设施

`8.130.77.216` 归属内蒙古乌兰察布阿里云数据中心。在本次攻击中，该地址的1099端口承担RMI服务，18888端口用于分发WebShell和接收落地回执。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYt2tPqSQprb0qZbRTEqTUjLz0YXEcevo0WBAWYFX5yjJgjscO9ZibG76oYtVGzaxePEzjciaRW8m45qPSMNw4cO2bjsXicgpMqBo/640?wx_fmt=png&from=appmsg)

`8.130.77.216` 的归属查询结果

资产测绘显示，该地址的8000、8080端口曾分别出现 `SimpleHTTPServer` 与 `BaseHTTPServer` 服务特征，均为Python 3.12.3。这类轻量服务与攻击中直接下载文件、接收落地回执的方式相吻合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQY5uJB8mRYyo3XPcyfBOLxh2KWAhMD9aY5aL8ZlOiaPUgWm80b2CuZC1YwWk2Q5alU84tFia0gfjEaMErmvNZPGb4nWRyGv0NECo/640?wx_fmt=png&from=appmsg)

该IP部分端口呈现Python HTTP服务特征

### 2.4 10月18日08:15，第二枚WebShell落地

距首次利用约27小时后，服务器于08:15:34再次出现同型异常。JNDI回连地址仍为 `rmi://8.130.77.216:1099/x`，说明同一基础设施再次通过该漏洞执行了攻击载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZcicLRviaWjqapShuXaFoXI27azjW9HsI220Blx0Sa5RvmMvtbKR1Oiah7pbhNgKwCIpcgVKgcOa0y3L5kYMrSicK0LTbN2PUlyH0/640?wx_fmt=png&from=appmsg)

10月18日08:15:34，同一RMI地址再次出现在应用日志中

08:15:35，主服务器再次执行落地命令。脚本逻辑与前一日基本一致，仅将下载文件替换为 `gzms.jsp`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQaKiatxF66Pneuq0ib8U5tpGYpZHHcxKuvR8rLgx5ucgZgg6afEiavkAibicFzqz0RFibZ79w1olN0icp8x4ZUxGUQiaDHWnobRMfiaUoics/640?wx_fmt=png&from=appmsg)

主服务器于10月18日08:15:35执行 `gzms.jsp` 落地命令

文件检索显示，`gzms.jsp` 的修改时间为08:15，大小为22 KB。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZFKtDLCIiaV2cvJCFvoulA9gKfRmPfUCWic7NXDWKBDNOibdjq2EDjicAMYjVePoBn8Uk1TA8P1cUDyN0sQt1YNCvV0UAqv2BWv34/640?wx_fmt=png&from=appmsg)

文件检索确认 `gzms.jsp` 的落地时间与事件日志一致

第二枚WebShell沿用相同的类加载骨架，但内嵌类为 `AES_BASE64`，注册路径为 `/gzsync`，通信内容经AES加密后再进行Base64编码。两枚WebShell共用连接密码 `ncw3b2026`，由同一地址分发，落地脚本也高度一致，可以确认前两轮利用属于同一套自动化工具链。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQaDdynf6ykPCvQ5465ibtDdqAGBN5HlYd1JAribdS2JF3o9ETmg5rvVowIw4Ah4oCLlysZLUZJFnrNDGdHGSZPxBNvCZycsgBBDw/640?wx_fmt=png&from=appmsg)

`gzms.jsp` 采用加密通信，结构较第一枚WebShell更为复杂

### 2.5 10月18日20:34，漏洞入口再次出现

20:34:59，应用日志第三次出现同型反序列化异常，但RMI地址变为 `rmi://192.151.233.247:1099/x`。漏洞入口和利用链未变，攻击基础设施已经切换。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQY35OpYjiaB3DZdGu5uF5ibRyRI8msia6un4JThjMQj6ajzaov9c23vj6dLicFRAmACXEEIyyWsBJcHzzmjNsAXXRv2uCaWgSRMKDo/640?wx_fmt=png&from=appmsg)

20:34:59，RMI回连地址切换为 `192.151.233.247`

20:35:00，主服务器执行一段混淆PowerShell。还原后可见两组关键处理：一组整数逐字节减129，恢复以IEX开头的下载执行内容；另一组整数减23，恢复 `System.Management.Automation.ScriptBlock`，再调用 `ScriptBlock.Create` 在内存中执行脚本块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYpnBuLCLKxUZYgBUFz5BBibiaHlBRYoa5C398HgXwgxYic3p5qcvhSpkJ1qCvib5CTsAETDcOL12q7WFT9nMuiaBvG2jiatkJdb3AicY/640?wx_fmt=png&from=appmsg)

主服务器于20:35:00执行混淆PowerShell，事件ID为4104

脚本还使用 `Update service mesh routing table` 作为注释，并将变量命名为 `$Timestamp`、`$LogFile`、`$ConfigPath` 等常见运维名称，以增加人工识别难度。还原后的下载地址指向 `192.151.233.246:20469`。

威胁情报显示，`192.151.233.246` 位于中国香港，带有恶意及漏洞利用相关标记。该地址与本轮RMI服务器 `192.151.233.247` 处于同一网段，分别承担载荷分发和漏洞利用回连。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQb9ibvsRrxVMAr3y3IknY9oc3JfCsYTVHKPxZOazPQSiaLj3qQocpBB7HKB1pKPorW6V7Fvia...