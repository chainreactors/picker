---
title: 2024年CVE漏洞数量激增38%：2024年CVE漏洞数据全景分析
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjAxNjc5OQ==&mid=2247484106&idx=1&sn=f398b5755112251a67ba7163915a09b7&chksm=c006ca3af771432c0af0c5d10250b43373383a354df878b38e50aa2bf42603c9ec05fe68cfa3&scene=58&subscene=0#rd
source: RedTeam
date: 2025-02-16
fetch_date: 2025-10-06T20:37:25.852676
---

# 2024年CVE漏洞数量激增38%：2024年CVE漏洞数据全景分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk4CA8RbTEaGn42pBjo0eSR4SNKzODvXU1BaDxpjSzoL3wDIK8WCafP6vYLIxe4uia5qAiaYTke51SrQ/0?wx_fmt=jpeg)

# 2024年CVE漏洞数量激增38%：2024年CVE漏洞数据全景分析

原创

tonghuaroot

RedTeam

## 摘要

2024年CVE漏洞数量激增38%，开源项目与WordPress插件成重灾区，周二发布量最高，平均CVSS评分6.67，前五大CNA贡献近44%漏洞。

### **要点总结**

1. **CVE数量暴涨**：2024 年发布了 40009 个 CVE，比 2023 年（28818）增长 38%，开源项目与 WordPress 插件成漏洞重灾区。
2. **漏洞严重性分化**：平均 CVSS 评分降至 6.67，仍有231个“满分”漏洞威胁关键系统。
3. **时间规律显著**：5 月为漏洞发布高峰，占全年 12.5%，周二单日占比超 24%。
4. **责任主体集中**：前 5 大 CNA 贡献近 44% 的 CVE，凸显开源生态安全治理挑战。
5. **新兴技术风险**：AI相关漏洞讨论升温，分类标准亟待完善。

## 前言

2024年，CVE数据呈现出前所未有的增长，本文结合关键统计数据与行业趋势，解析年度漏洞生态。

### CVEs 统计概况

2024 年结束时，共发布了 40009 个 CVE，比 2023 年发布的 28818 个CVE增长了 38% 以上。

* 平均每天发布 108 个CVE。
* 5 月发布的 CVE 数量最多，共发布了 5010 个，占全年 CVE 的 12.5%。
* 星期二成为发布最多 CVE 的日子，发布了 9706 个，占全年 CVE 的 24.3%。
* 5月3日是发布 CVE 最多的一天，达到了 824个。

### 按月分布的CVEs

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk4CA8RbTEaGn42pBjo0eSR4bibbdQaHLQ181nIElVbv27fsmvIse4U9rBaroxlolcDAuibsFjKfC2qQ/640?wx_fmt=png&from=appmsg)

image

| 月份 | CVEs | 占比 |
| --- | --- | --- |
| 一月 | 2593 | 6.5% |
| 二月 | 2778 | 6.9% |
| 三月 | 3310 | 8.3% |
| 四月 | 3622 | 9.1% |
| 五月 | 5010 | 12.5% |
| 六月 | 3080 | 7.7% |
| 七月 | 3124 | 7.8% |
| 八月 | 2900 | 7.2% |
| 九月 | 2522 | 6.3% |
| 十月 | 3573 | 8.9% |
| 十一月 | 4058 | 10.1% |
| 十二月 | 3439 | 8.6% |

### 按星期几分布的CVEs

| 星期 | CVEs | 占比 |
| --- | --- | --- |
| 星期一 | 6449 | 16.1% |
| 星期二 | 9706 | 24.3% |
| 星期三 | 7143 | 17.9% |
| 星期四 | 6321 | 15.8% |
| 星期五 | 7100 | 17.7% |
| 星期六 | 1858 | 4.6% |
| 星期天 | 1432 | 3.6% |

### 前10个CVE发布日

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk4CA8RbTEaGn42pBjo0eSR4mQjKPoribRlGVUOLmNX7HdIzo46He4ZibeHkK5grWFUWCniaG56ibs6APw/640?wx_fmt=png&from=appmsg)

image

| 日期 | CVEs |
| --- | --- |
| 5/3/24 | 845 |
| 5/14/24 | 824 |
| 7/9/24 | 471 |
| 5/21/24 | 436 |
| 10/21/24 | 436 |
| 11/22/24 | 385 |
| 4/9/24 | 384 |
| 11/19/24 | 383 |
| 12/12/24 | 341 |
| 11/12/24 | 333 |

### CVE增长趋势

自2017年以来，CVE发布数量连续第七年创下新高，2024年共发布40009个CVE，同比增长了38.83%。这意味着15.32%的CVE是去年发布的。

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk4CA8RbTEaGn42pBjo0eSR425T3WricsVBry5HutH80ibiac04TEl6secrbDuRMAN9cOpdpF7seG5r9g/640?wx_fmt=png&from=appmsg)

image

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk4CA8RbTEaGn42pBjo0eSR4szA3UvmI588WSU8IcW7jwopM3KJLLLjl7RSJ5GwHxPE52icCROpjm8Q/640?wx_fmt=png&from=appmsg)

image

### CVE CVSS评分

通用漏洞评分系统（CVSS）提供了一种捕捉漏洞关键特征并生成数值评分的方式，评分范围从0.0到10.0，反映其严重性。

* 今年的CVSS平均分为6.67。
* 总共有231个漏洞获得了10.0分。
* CVE-2024-2365是今年发布的CVSS最低分漏洞，得分为1.6。

### CPE

通用平台枚举（CPE）是用于IT系统、软件和软件包的系统命名规范，有助于识别CVE中列出的易受攻击软件。

* 今年共记录了19807个不同的CPE，其中最常见的是 `cpe:2.3:o:linux:linux_kernel:*:*:*:*:*:*:*:*`，共被引用了8093次。
* CVE-2024-20433，这个漏洞与Cisco IOS软件和Cisco IOS XE软件的资源预留协议（RSVP）功能有关，具有最多的CPE记录，达到了2,434个唯一的受影响配置。

### CNA

CVE编号授权机构（CNA）包括软件供应商、开源项目、协调中心、漏洞悬赏服务提供商、托管服务和研究小组，CVE计划授权它们为漏洞分配CVE ID并在其指定的覆盖范围内发布CVE记录。

* 共有433个CNA，在今年发布了至少一个CVE。
* 去年发布最多CVE的前五个CNA为：

+ Patchstack：4,566个（11.41%）
+ Kernel.org：4,325个（10.81%）
+ Wordfence：3,525个（8.81%）
+ VulDB：2,936个（7.34%）
+ Github：2,121个（5.3%）

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk4CA8RbTEaGn42pBjo0eSR47kMn9BJhO67icuEPgEG9TSrvYYWMocbs5R3Cq1XZc4LClmoNETKdWjQ/640?wx_fmt=png&from=appmsg)

image

### CWE

CWE是一个由社区开发的软件和硬件弱点类型列表，作为安全工具的共同语言、基准，并为识别、缓解和预防弱点提供基础。

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk4CA8RbTEaGn42pBjo0eSR4zlJbn6LzZVJcDb62jPoxM8BibL9MYribzSHnWUKMLXJvgDYRL9kEysaw/640?wx_fmt=png&from=appmsg)

image

* 今年有237个CWE被分配给CVE，其中CWE-79是分配最多的，达到了6,227次，占所有CVE的15.56%。
* NVD 没有分配 CWE（NVD-CWE-noinfo或Missing\_Data）的CVE有6292个，占比为15.73%。

注：695 个被拒绝的 CVE 在今年的数据集中被移除。

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk4CA8RbTEaGn42pBjo0eSR42yuvVYjb7xr0vojTbo0wNj9ZibEnm3vrF1r9y2DyY4XpT1ibJk2ET4Xg/640?wx_fmt=png&from=appmsg)

image

以上内容编译自 jerrygamblin

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

RedTeam

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

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