---
title: 合法终端管理软件遭滥用：疑似银狐攻击事件分析与溯源
url: https://mp.weixin.qq.com/s/0GdXqw59lsZPL6JTeG-v8Q
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:48:31.676552
---

# 合法终端管理软件遭滥用：疑似银狐攻击事件分析与溯源

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mVOy0n0uJdjsneCDic6hgrMH6RkncCuvrkicyq8YvZaImmjiacRlnOkANLJ46GOlOJHcDLnMIldCvqLLAdYju39eibk4Yu3xojRmbGYYAa1dK90/0?wx_fmt=jpeg)

# 合法终端管理软件遭滥用：疑似银狐攻击事件分析与溯源

原创

知道创宇
知道创宇

知道创宇

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**一、事件概述**

近期，我们在客户现场应急响应中排查到一起新型攻击事件。攻击者伪造常用工具安装包诱导执行，随即部署一款带有合法数字签名的终端管理软件。经技术溯源确认，该程序具备主机信息收集、远程控制等完整恶意能力，其 C2 基础设施与 “银狐” 高度关联。由于合法数字签名的天然 “免杀” 特性，该恶意程序可轻易绕过主流杀毒软件检测，实现隐蔽入侵与长期控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdgibibh9jZS1mNsVVIdibyaRPu0UgCbxA2foeoQQYUWNcOhmrlgNLmsXGachTDV7yJdWoYsNrruPT9ib7LDy8W8ULyicgTPiaiagbvX8w/640?wx_fmt=png&from=appmsg)

**银狐简介**

银狐（别名：游蛇、谷堕大盗）是自2022年底起持续活跃的黑产远控木马家族，其以东南亚为核心活动大本营。早期安全圈将其界定为黑产团伙，随着其核心武器Gh0stRAT的源码在互联网上广泛泄露与传播，任何具备基础技术能力的攻击者均可获取该源码并进行二次修改、定制，进而利用其发起恶意攻击。基于此，安全行业逐渐将其重新定义为一个“去中心化”的黑产工具集合。该木马家族主要活跃于中文互联网场景，攻击范围覆盖金融、证券、能源等多个关键行业，目前已成为国内影响范围最广、传播最为流行的黑产攻击工具之一。

**二、事件背景**

**2.1 初始发现**

事件起因系客户方员工反馈其工作电脑出现鼠标不受控制的异常现象。经初步测试，已排除硬件故障可能。安全人员后续排查分析时，在主机中发现一款可疑安装包，该程序伪装为常用工具软件，运行后会静默安装合法终端管理软件。

利用 RMM（远程监控与管理）工具实施攻击已成为常见攻击手法。典型案例包括中东 APT 组织 MuddyWater，曾多次借助 ScreenConnect、AnyDesk 等工具发起攻击活动。此外，TeamViewer、Quick Assist 等主流 RMM 工具也曾被不同程度的滥用。

**2.2 样本拓线**

通过对终端管理软件的拓展分析，我们找到了一批利用相同RMM进行攻击的安装包，同时还发现了下载该安装包的前一阶段脚本，详细见样本分析章节。

**三、样本分析**

**3.1 初始阶段**

攻击者使用的初始载荷为一个VBS脚本，该脚本经过简单的混淆处理，主要功能是下载并执行MSI安装包。

**3.1.1 规避技术**

脚本采用多种简单的混淆手段试图规避检测，同时，注释中大量的中文暗示了作者可能为中文使用者：

字符串分割拼接

![](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdhBRtWHOI2AkRlTREqJ9ibPxlxtSZSNSZClqrMhGVRuWSu2WVubpItD3kl3IsGcPMJPJNdljYpM35DMHYCVCnNSo9lyBIOiawoao/640?wx_fmt=png&from=appmsg)

文件伪装

将系统自带提供下载功能的工具复制到工作目录并重命名为常见系统文件名，可在一定程度上规避常规的可疑下载规则检测。

![](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdiacOEAmL39YEVmTw593beuJwPBcTIkzCr2VReZNYzgS3hJE2icK086eNMmE2bv8maZTGbJDWLEicccseaYLpM8RErfU9wiaYq185A/640?wx_fmt=png&from=appmsg)

**3.1.2 下载逻辑**

脚本内置多种下载方式，依次尝试直到成功：

![](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdiaRfiaV9zT9M3CKfJbREG6ccNhZNRXBfPywtCvh0cbmGAic0lE5qq0onoOtZGxmXwThUNOK6tcHfFrThfE7CMgicgN9iblWkibgmko4/640?wx_fmt=png&from=appmsg)

下载地址为：

hxxps://fawanyoufa.s3.us-west-004.backblazeb2.com/VibeCheck.msi

backblazeb2[.]com为国外的云存储服务，大部分流量设备会将该域置为白名单，攻击者利用这一特性来保证载荷在下载阶段不会被拦截。

**3.1.3 安装执行**

下载完成后，脚本以管理员权限静默安装MSI包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdjiayMhsQlhhEx69PicJ95E9OxuQQsIDjtWoUUdqBicwcPjp81z1yR7R7SfoPOwBGib5RYBEfQsbic9dyuDtg8TqmqxRpQoqvLWHrTY/640?wx_fmt=png&from=appmsg)

**3.2 MSI安装包分析**

下载的MSI安装包经分析，其主体是一个终端管理软件。MSI中包含了一个NSIS安装程序（client.exe）和配置文件(server.cfg)：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdhsEd2vMR6wiawlo8AnQYU3Rtib2Md10vxIlibpiaPobz5RjvyzrMTaFnHq72degNBPqS7bfN49na0v3exSbt33dZ0R9R7MpVYYIe0/640?wx_fmt=png&from=appmsg)

NSIS安装包中指定了安装完成后的运行流程，使用nsExec::ExecToLog运行"NSec.exe -ip"，随后再运行"instrap.exe"：

![](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdiajDvicZyoK6xWDrZYDcgdBfmhmyScCF7VDXPIcw5lGvE3wBaH8deJofYc7rgCexWvMGKQ1C6KcNTvaY8cNBQgOk0nSsEb6ibyzo/640?wx_fmt=png&from=appmsg)

**3.2.1 软件信息**

该软件具有有效的数字签名，攻击者利用合法签名软件作为攻击工具，可绕过部分安全产品的检测，同时降低用户警觉性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdjczvicbz8cn8X5qgGMvtLTaTy0iajAxPH8fjwsHV0ypHvyEZEq1y3UzyNFrLcniaLjPLf6reianvB0mMuO7b4tZNp2MAiaVD9F8qTU/640?wx_fmt=png&from=appmsg)

软件的版本为3.7.84，从时间上来看该版本为2024年3月后发布。

![](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdiaPg4tB2MbOHKjS8HIqTKWE7Ew1I8bvqI4sfZ9J4mCBmibByUTH3ry1PNwINeS1c9ZB7egmlzCEdaKAYYAAy203aGPRicKA4fk2k/640?wx_fmt=png&from=appmsg)

**3.2.2 功能分析**

该终端管理软件具备以下功能：

信息收集

* 主机基础信息（主机名、IP地址、操作系统版本）
* 硬件信息（CPU、内存、磁盘）
* 已安装软件列表
* 网络配置信息
* 用户账户信息

远程控制

* 远程桌面控制
* 远程文件管理
* 进程管理
* 系统服务管理
* 注册表操作

这些功能本身是终端管理软件的正常功能，但在攻击场景下被滥用于恶意目的。通过对软件包的测试，我们发现上述server.cfg中的ip地址正是RMM运行后使用的外联地址：

![](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdjBqvHU7glvks36NlHRMFrxHgomaTdiccSwDFu63QaQRMKBOo8N9T6gLZloKuoia7jILuT7IjmFuzx1Yib5AHUMSAezmLtcJIwqr4/640?wx_fmt=png&from=appmsg)

**四、溯源分析**

**4.1 样本关联**

通过对样本的深入分析，我们发现了一批同类型的MSI安装包，这些样本具有以下共同特征：

* 使用相同的分发基础设施
* 均包含带签名的终端管理软件
* 相同的加载运行方式

**4.2 C2基础设施关联**

通过对回连地址的溯源分析可发现，该地址与银狐（SilverFox）过往攻击活动存在明确关联。本次样本所使用的远程 IP 地址（202.79.165.130），曾于 2026 年 3 月被用于分发 ValleyRAT。该远控木马为银狐组织常用武器 WinOS 的变种，在中文互联网环境中常被伪装成各类常用工具进行传播扩散。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdhmrd3PIZRz7mbe2487uTaEREbXByUdYKfwJhufDvywicDRgZeXRGNrrEgESW4xich0Cic0B1vX2iaEO3uYfEnHkv36crPysicY09vo/640?wx_fmt=png&from=appmsg)

无独有偶，2025 年已有安全情报[1]披露，银狐组织曾利用本次事件同款 RMM 软件中的驱动程序漏洞实现强杀任意进程，以此达到免杀对抗目的。该漏洞于 2026 年初被正式编号为 CVE-2025-68947。由此可推断，银狐攻击者已完整掌握该软件的运行组件，并对其开展了深度逆向与漏洞挖掘。

事实上，该 RMM 软件并非首次被滥用于恶意攻击。早在 2020 年，国内多家安全厂商就已公开披露过该工具被黑产团伙滥用的相关案例[2]。

**五、总结**

本次攻击事件中，攻击者创新性地将带有合法数字签名的终端管理软件作为核心攻击武器，清晰展现了“Living off the Land”（寄生在合法环境）的攻击理念。

攻击者通过对合法工具进行武器化改造，既能够借助合法签名绕过传统安全产品的静态检测机制，又能依托终端管理软件本身具备的远程控制、进程管理等原生功能，实现对目标主机的完整控制、持久化驻留及后续横向移动，攻击隐蔽性与危害性大幅提升。

该事件再次为政企单位及安全行业敲响警钟，核心警示如下：

1.合法软件可被恶意滥用为攻击载体：

传统依赖数字签名校验的安全检测模式已难以应对新型攻击手法，安全产品需实现从“静态签名校验”向“动态行为分析”的转变，重点监控合法软件的异常操作（如静默安装、非授权远程连接、异常进程调用等），构建全方位的行为检测体系。

2.用户安全意识是网络安全的最后一道防线：

此类攻击的初始入口多与钓鱼诱导相关，防范此类攻击并非单一部门的职责，需推动全员安全意识提升，加强钓鱼邮件、可疑安装包的识别培训，引导员工养成“不随意点击陌生链接、不安装来源不明软件”的安全习惯，形成全员参与的安全防护闭环。

**六、IOC指标**

**6.1 文件指标**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdg2emtpU5caiaZbFERWJgFVU8ErYar6zsznyxvdpzmcR6PeDzoZwvc6Olcx5CjgmmNuicSHIlj1M9V1sbO2Hj0asoyHp3LDBibKWI/640?wx_fmt=png&from=appmsg)

**6.2 网络指标**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdhKzfKuS5U7yejGzWsI5nnIZKbAIgnQGnh2asfFV70rpAjA5PVsE27B6q6g5gnNdAv3drt0WZpJctADEELkibaGWNByCxdmtka8/640?wx_fmt=png&from=appmsg)

**七、防护建议**

**7.1 终端防护**

1.软件来源验证：仅从官方渠道下载软件，验证发布者签名

2.权限管理：限制普通用户的软件安装权限

3.行为监控：监控msiexec静默安装、异常进程创建等行为

**7.2 网络防护**

1.流量监控：监测异常外联行为，特别是向云存储服务的请求

2.域名过滤：对未知或可疑域名进行访问控制

3.SSL解密：对加密流量进行检测分析

**7.3 安全意识**

1.提高员工对钓鱼攻击的识别能力

2.不随意执行来源不明的安装包

3.发现异常及时上报安全团队

**7.4 边界威胁防护**

部署知道创宇自研威胁情报网关产品，结合本次银狐事件溯源成果及全域威胁情报能力，构建从情报生成、实时检测、自动阻断的全流程主动防御闭环。实战效果已通过内部验证与客户场景双重检验。

1.精准掌握：银狐攻击核心指纹特征

2.情报实时匹配：基于全域威胁情报库，对银狐相关情报实现识别命中

3.自动阻断与联动响应协同处置，将威胁有效拦截于网络边界

![](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdhmmrWWGvKhdkk9NkWr3197LRpbLGQZSTtR9D0xXj7a7vm5QHRzrPaGkR8om9NaIUDj3FRw8CfXbVygyTOOP2F9g2VCv0opLCo/640?wx_fmt=png&from=appmsg)

*参考链接：*

1.https://blog.csdn.net/qq\_40827990/article/details/148997201

2.https://www.anquanke.com/post/id/197266

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Oan15mBs7fOYe1ETMicrrK5eEreO2UU1sxFQL4Eebn6tthroecicEQrsbZ8qRzV2xMGpvCyU3lWjJwASBPD5QpBg/0?wx_fmt=png)

知道创宇

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Oan15mBs7fOYe1ETMicrrK5eEreO2UU1sxFQL4Eebn6tthroecicEQrsbZ8qRzV2xMGpvCyU3lWjJwASBPD5QpBg/0?wx_fmt=png)

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