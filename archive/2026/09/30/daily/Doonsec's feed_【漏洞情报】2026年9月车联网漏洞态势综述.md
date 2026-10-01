---
title: 【漏洞情报】2026年9月车联网漏洞态势综述
url: https://mp.weixin.qq.com/s/dVPfaeLA9zvAtwbb6b9now
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:58:26.657698
---

# 【漏洞情报】2026年9月车联网漏洞态势综述

# 【漏洞情报】2026年9月车联网漏洞态势综述

原创

太初众测
太初众测

太初众测

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**【漏洞情报】**

**2026年9月**

**车联网漏洞态势综述**

**车联网安全漏洞情报**

**月度推送**

本月共收录车联网相关漏洞 47 条，严重与高危合计占比 53%。联网车载终端风险集中暴露：Botslab G980H 行车记录仪单日集中披露 14 个漏洞，lwIP 协议栈 MQTT 组件披露可远程利用的严重越界写入漏洞，建议相关单位及时排查处置。

![](https://mmbiz.qpic.cn/mmbiz_png/ounUznLmib99ktdS7QHnAe7BKBwfZSZHcibQT6Sp1icNSibVGBQpx6e9tCjAx8tAmHm6wiax6wAJuba1yt3aWWAt7mdHTuGH3o5IM3FPCds9fjUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/ounUznLmib9icIXl4LdfAnBklKiaibDchcVsOtnp4kt89ofPSZVofQ70kHrnyP98IB5y1LMtPSKaWxlk7ArnDH7xGIu4sQViaTD5hr2iaZvvmNfnY/640?wx_fmt=gif&from=appmsg)

**一、本月漏洞综述**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ounUznLmib99oFP2NAlMxx4QhPvf9xa78ckv9ykFSqVeYCJ7VKjk2e6zaM7MF9WW2Qyz9hlwibHJnYmdzVD8zEibicXxBTXIqONY9PNh6L7pD6U/640?wx_fmt=png&from=appmsg)

2026 年 9 月，车联网漏洞情报平台共收录车联网相关公开漏洞 47 条（均为 CVE 编号漏洞）。按危害等级统计

：严重（Critical）4 条、高危（High）21 条、中危（Medium）16 条、低危（Low）6 条，严重与高危漏洞合计占比 53%。其中 43 条已公布官方 CVSS 评分，平均得分 7.05 分，整体危害水平较高；其余 4 条为 Linux 内核瑞萨驱动漏洞，官方暂未发布评分（NVD 待分析），已如实标注。本期数据经 NVD、CVE.org 官方漏洞库交叉核验。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ounUznLmib98lvxmtRPDrQFIoKhBjWoLxLkQicLbCfbXQHVgAR9OkEJyKtmQWG1Fr4DqhxdsKoyjVqc7IsT4y5r2L6gIKQBRX2b7HFEw918BI/640?wx_fmt=png&from=appmsg)

图 1  危害等级分布

![](https://mmbiz.qpic.cn/mmbiz_png/ounUznLmib982dcrwausotUibkqcUVFboQezyJ1lLQqBnKylWArW73ia7H1s0cxAYrC26n2AGXxGzwjGsZuD3126iaQn7tHRUGEfvjhpEHO1skw/640?wx_fmt=png&from=appmsg)

图 2  2026 年 9 月每日新增车联网漏洞趋势

从披露节奏看，本月漏洞呈多批次集中披露特征：9月 24 日单日新增 15 条，为全月峰值，其中 14 条来自 Botslab G980H 行车记录仪的集中披露；9 月 10 日新增 7 条，含博世 Sensortec 传感器 SDK 集中披露的 5 条缓冲区溢出类漏洞；9 月 18 日新增 7 条，含 Bransys ELD 电子记录设备硬编码凭证漏洞 3 条、gPTP 时间同步协议栈漏洞 2 条；9 月 17 日新增 5 条；9 月 4 日、11 日、14 日、28 日、29 日分别新增 2 条，9 月 7 日、9 日、22 日分别新增 1 条。从影响领域看，车载及充电专用系统（12 条）、内核/驱动（9 条）、Wi-Fi/无线（7 条）为主要受影响面，另有移动/Android、蓝牙、Web/应用各 2 条。

![](https://mmbiz.qpic.cn/mmbiz_png/ounUznLmib9ibWzW4XRFRHE7hBP0TwGDEpAwrhUWbsXyQ8b0fcict4fsL0Jq5BykFibBCJlyEHxYAB2SyGCqBgmib9zzw8u9mxy7oylU5ia9Mzjpg/640?wx_fmt=png&from=appmsg)

图 3  漏洞涉及技术领域分布（单条漏洞可涉及多个领域）

**二、重点漏洞分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ounUznLmib98U4nrnIkwYuzRAEAccriciakbLHp3libIib1TI6VyakG1rNJjOy0vOpk95HAuqziciaCoSJic9icChev1IYvicMddWt76hryMjSjMa4mB0/640?wx_fmt=png&from=appmsg)

**!**

**一）联网车载终端**

**>>联网车载终端：Botslab G980H 行车记录仪单日集中披露 14 个漏洞**

**风险等级：严重 ｜ 涉及 CVE-2026-75558 ~ CVE-2026-88956 共 14 个漏洞 ｜ 最高 CVSS 9.2**

9 月 24 日，Botslab G980H 行车记录仪集中披露 14 个固件漏洞，覆盖认证、会话管理、传输加密与固件更新等多个环节：固件更新验证不足（CVE-2026-81630，CVSS 9.2，严重）——更新流程经未受保护的连接获取固件，且仅依赖固件自带的完整性值而非可信密码学校验，网络可达、无需认证，攻击者需能向设备更新流程提供固件方可利用；会话管理缺陷（CVE-2026-82566，8.7）与会话授权绕过（CVE-2026-84399，8.7）使已认证状态在连接终止后仍保持有效，认证值重放漏洞（CVE-2026-77967，8.6）允许攻击者复用截获的认证值，三者均面向同一无线覆盖范围内的邻近网络攻击者；另有硬编码 root 密码（CVE-2026-79959，7.0）、UART 接口 root 账户无认证（CVE-2026-88956，7.0）、HTTP 服务器路径遍历（CVE-2026-82708，7.1）、HTTP/RTSP 明文传输敏感信息（CVE-2026-82585，7.1）、会话标识符可预测（CVE-2026-85496，7.7）、WiFi 密码可预测（CVE-2026-88761）、WiFi 凭据硬编码密钥（CVE-2026-75558）、蓝牙未认证访问（CVE-2026-84403）、诊断日志敏感信息泄露（CVE-2026-82716）与命令处理越界写入（CVE-2026-87118）。

**风险分析**

硬编码凭据与缺失认证使设备的认证门槛形同虚设，固件更新验证不足则为植入恶意固件留下通道；行车记录仪持续记录位置与影像，数据敏感性高。使用该设备的车辆用户应尽快升级固件并修改默认 WiFi 密码。与之关联，本月还披露行车记录仪云平台云存储桶权限配置错误漏洞（CVE-2026-94204，CVSS 8.7），存储桶被配置为公开可读，用户记录与行车数据可被任意访问；以及 Bransys ELD 电子记录设备硬编码 MQTT 凭证漏洞 3 条（CVE-2026-86520，CVSS 8.7；CVE-2026-86689，CVSS 8.2，凭证明文传输；CVE-2026-77960），可读取接入受影响 MQTT 代理的在营车辆实时数据。

**!**

**二）基础组件与平台软件**

**>>基础组件与平台软件：lwIP 协议栈与车辆管理系统披露严重漏洞**

广泛应用于嵌入式与车载网络设备的 lwIP TCP/IP 协议栈披露 MQTT 组件越界写入漏洞（CVE-2026-87121，CVSS 9.3，严重），网络可达、无需认证、无需用户交互，可能导致攻击者在设备上获得完整代码执行能力。Joomla 车辆管理器扩展（Vehicle Manager 免费版 6.5.8 之前版本）披露未授权 SQL 注入漏洞（CVE-2026-101108，CVSS 9.3，严重），前端匿名可达的排序参数未过滤，攻击者可远程注入任意 SQL。此外：Traccar GPS 追踪系统权限接口 SQL 注入（CVE-2026-52851，高危）；LubeLogger 车辆维护追踪系统文件上传路径穿越（CVE-2026-62278，CVSS 8.1，需认证）与记录复制越权访问（CVE-2026-62279，CVSS 7.1，需认证）；SJRC GPS 追踪器 inetd 服务信息泄露（CVE-2026-52482，CVSS 7.5）；DetaWix 移动门户敏感信息泄露（CVE-2026-86450，CVSS 7.5）；code-projects 车辆管理系统 SQL 注入（CVE-2026-85516，CVSS 6.9）与数据库备份文件信息泄露（CVE-2026-85517），后者利用代码已公开。

**风险分析**

lwIP 被大量车载通信模块与充电桩固件集成，漏洞影响面随供应链放大；车辆管理与追踪平台漏洞则直接威胁运营数据与车辆位置信息安全。建议相关厂商盘点 lwIP MQTT 组件使用情况并跟踪上游修复。

**!**

**三）联网车载终端**

**芯片、内核与传感器：博世传感器 SDK 与瑞萨驱动集群**

博世 Sensortec 于 9 月 10 日集中披露 5 个传感器 SDK 漏洞：BHI385 传感器 API 栈缓冲区溢出（CVE-2026-42805，CVSS 8.4，本地攻击者可利用）、COINES\_SDK 桥接协议解码器堆缓冲区溢出（CVE-2026-42807，CVSS 8.0，邻近网络攻击者需用户交互方可利用）、BHI360 传感器 API 栈缓冲区溢出（CVE-2026-42804，CVSS 7.6，需物理接触设备）及 2 个中危漏洞（CVE-2026-42806、CVE-2026-42808）。

Linux 内核方面，瑞萨（Renesas）驱动集群披露 6 个漏洞：I3C 驱动释放后使用（CVE-2026-80950，CVSS 7.8）与 RCAR-Gen2 PHY 驱动双重释放（CVE-2026-90288，CVSS 7.4）——需要指出的是，二者早期被部分情报源标注为低危，经 NVD 核验实为高危，建议相关单位以官方定级为准评估风险；另有 4 个漏洞（CVE-2026-89728、CVE-2026-93072、CVE-2026-90124、CVE-2026-93276）官方暂未发布评分（NVD 待分析）。瑞萨 R-Car 系列芯片广泛应用于车载座舱与网关，相关驱动缺陷可被本地低权限攻击者利用提权。

此外：车辆运动规划系统 EGO-Planner-v2 披露过期轨迹数据处理不当漏洞（CVE-2026-71640，CVSS 9.1，严重），重规划管线对过期轨迹数据处理不当可导致不安全的车辆运动，该漏洞早期被部分情报源标注为低危，经 NVD 核验实为严重，建议以官方定级为准；gPTP 时间同步协议栈披露 2 个越界读取漏洞（Linux 内核 CVE-2026-16514、Zephyr RTOS CVE-2026-16512），车载以太网时间同步面临畸形报文风险；联发科相机中间件双重释放漏洞（CVE-2026-20510）可致本地提权；三星 Exynos 系列处理器披露 2 个拒绝服务漏洞（CVE-2024-53922、CVE-2023-37366）。

![](https://mmbiz.qpic.cn/mmbiz_png/ounUznLmib99ZVCCaoxib7SZKicDIvmG12gj3Oicu71yllTBaqDCEc3NyQ9n4R8rrwiaUkWcM5Hz3gJtYd3XMKjXU1onB9ibKHV5tnxE6AB4DV47w/640?wx_fmt=png&from=appmsg)

图 4  主要漏洞类型分布

**!**

**四）本月重点漏洞清单**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ounUznLmib9ibUicJbQxbnoicc96IW2T9vPW4MuZK6qhYQIia08GSUV974RZbFwmbibYeLdKiaiaanI9MibPBzBM6hdfLiba3k0iaGsBNwcJXl19lLgEQY/640?wx_fmt=png&from=appmsg)

**三、在野利用风险研判**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ounUznLmib9ibHSXiaHzCzHnsoXC4d6wO9xZTllTe0PHGDEictpSFXDbMmJX5K4P5bLaFNhxXTiarIJJ2V8xx6mTJkg8Bic12XM2dWJM3DFuhSTic8/640?wx_fmt=png&from=appmsg)

**●EPSS 利用概率**：本批漏洞 EPSS 评分最高为 0.63%（CVE-2026-71640），已返回数据的 45 条均低于 1%，暂未出现利用概率显著升高的个体；其余 2 条（CVE-2026-86450、CVE-2026-94204）因披露时间较新暂无 EPSS 数据。[EPSS（Exploit Prediction Scoring System）数据来自 FIRST.org API，数据日期 2026-09-29，表示漏洞未来 30 天内被利用的预测概率。]

**●CISA KEV 目录：**经核查，47 条漏洞均未被收录至 CISA 已知被利用漏洞目录，目前无公开在野利用证据。[CISA KEV（Known Exploited Vulnerabilities）目录版本 2026.09.29，核查日期 2026-09-30。]

**综合研判：**当前处于"漏洞已公开、攻击利用尚未规模化"的处置窗口期。考虑到本月严重漏洞集中于联网车载终端与基础协议栈组件，且部分漏洞利用代码已公开（如 CVE-2026-85517），此类漏洞从披露到被扫描利用的周期通常仅为数周，建议相关单位抓紧完成排查修复，避免窗口期后被动应对。

**四、安全建议**

![](https://mmbiz.qpic.cn/mmbiz_png/ounUznLmib9ic0swtDAmMNXicx8KoNnib0UvWTM72s7FDoS7Zbx8pGvXlfHicnt1xd82EN3uCNyoXMRmPBx9HMVpvOhaXorIKWs59ujJrRhlw3nk/640?wx_fmt=png&from=appmsg)

**01**

**车辆用户及充电用户**

●使用 Botslab G980H 等联网行车记录仪的用户，应至官方渠道核查并升级固件，同时修改设备默认 WiFi 密码；蓝牙、WiFi 等无线功能在不使用时建议关闭。

●车机系统与车载设备推送固件或 OTA 安全更新时尽快安装；避免在不可信公共 WiFi 环境下使用车载联网服务。

●发现车辆异常联网行为（如未知热点连接、异常流量）时及时联系厂商售后核查。

**02**

**车企、充电运营商及零部件厂商**

●终端固件整改：行车记录仪、ELD 等联网终端厂商应建立固件签名与安全更新机制，移除硬编码账户与硬编码密钥，关闭 UART 等调试接口的出厂无认证访问。

●组件与驱动修复：盘点 lwIP MQTT、Open1722 等开源组件的使用情况并跟踪上游修复；采用瑞萨 R-Car 平台的产品关注内核驱动补丁并纳入 OTA 排期。

●云平台权限审计：对云存储桶、MQTT 代理等云端资产开展权限配置专项审计，杜绝公开可读与硬编码凭证接入。

●平台应用加固：车辆管理与追踪平台运营方应对 SQL 注入、路径穿越、越权访问类漏洞开展自查，及时升级第三方扩展与框架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ounUznLmib9ictcsiciaojvy8V6HkVcKgRadFIuiamag25AADEdibSFc0UVQsvYicibia3sGnXamDibibopQxgftAicRdhg2ZgOA2PpgU4a1EoaRNmQsQiaE/640?wx_fmt=png&from=appmsg)

扫码查看9月漏洞数据

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ounUznLmib99gbibgfGGZO9OuvAHcbXw3MyGmLZKtJayGjEB6fSt9Qj6mqt682R6KRUOibibETicsULZ3nIYFclEa8SLttT5aicph5dyRNXMdkAAU/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ounUznLmib99f1AlqBA4jiak8pptkeGDFK9a9GoUjicDITH8R37eo2nPxsg7MNJ7FNib1lYN5Iw0jpZKOSBicyHzfV5ZsFaNsehk6tian9ZNbJuEg/0?wx_fmt=png)

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