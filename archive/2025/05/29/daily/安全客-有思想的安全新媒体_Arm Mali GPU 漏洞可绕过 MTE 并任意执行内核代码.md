---
title: Arm Mali GPU 漏洞可绕过 MTE 并任意执行内核代码
url: https://www.anquanke.com/post/id/307898
source: 安全客-有思想的安全新媒体
date: 2025-05-29
fetch_date: 2025-10-06T22:25:31.438108
---

# Arm Mali GPU 漏洞可绕过 MTE 并任意执行内核代码

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Arm Mali GPU 漏洞可绕过 MTE 并任意执行内核代码

阅读量**118077**

发布时间 : 2025-05-28 13:36:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta ，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/arm-mali-gpu-vulnerability-let-bypass-mte/>

译文仅供参考，具体内容表达以及含义原文为准。

安全研究人员发现了Arm的Mali GPU驱动程序中的一个关键漏洞,该漏洞允许恶意Android应用程序绕过内存标记扩展(MTE)保护并实现任意内核代码执行。

该漏洞名为CVE-2025-0072,对使用命令流前端(CSF)架构(包括Google的Pixel 7,8和9系列智能手机)配备更新Arm Mali GPU的设备构成重大威胁。

安全专家Man Yue Mo的研究于2024年12月12日向Arm报告了这个问题。

遵循负责任的披露做法,Arm解决了2025年5月2日公开发布的马里驱动程序版本r54p0中的漏洞,随后包含在Android的2025年5月安全更新中。

攻击向量涉及通过命令队列利用 Mali GPU 和 userland 应用程序之间的通信机制,特别是针对驱动程序中的 kbase\_queue 对象实现。

[GitHub分析师指出](https://github.blog/security/vulnerability-research/bypassing-mte-with-cve-2025-0072/),这个漏洞遵循了MTE旁路技术的关注模式,基于Mo之前发表的关于CVE-2023-6241的类似研究。

此漏洞的影响超出了典型的内存损坏问题,因为它表明,基于硬件的安全功能(如MTE)可以通过精心制作的驱动程序级漏洞来规避。

Mo成功在启用了内核MTE的Pixel 8设备上开发并测试了该漏洞,表明该漏洞会影响现实世界的部署,其中MTE正在积极防止内存安全违规。

利用技术以创建无页后使用条件为中心,允许攻击者重用已释放的内存页面作为 GPU 上下文的页表全局目录 (PGD)。

这种方法可以操纵GPU内存管理结构,最终提供任意内核代码执行的途径。

漏洞的重要性不仅在于其损害设备安全性的能力,还在于其演示了现代硬件安全扩展可以通过复杂的驱动程序级攻击系统地绕过。

###

### **技术开发机制**

CVE-2025-0072的核心在于操纵马里GPU驱动程序中的CSF队列绑定和不绑定进程。

该漏洞利用了 kbase\_queue 对象在队列绑定操作期间管理内存分配的设计缺陷。

当使用 KBASE\_IOCTL\_CS\_QUE\_BIND ioctl 创建并绑定到 kbase\_queue\_group 时,驱动程序分配 GPU 内存页面并将其地址存储在 quael->phys 字段中。

关键缺陷在队列终止和重新绑定过程中出现。

当使用 KBASE\_IOCTL\_CS\_QUE\_QUE\_GROUP\_TERMINATE ioctl 终止 kbase\_queue\_group 时,清理过程调用 kbase\_csf\_term\_descheduled\_queue\_group,它解绑定关联的队列并重置其 queange->group。

这种不绑定操作为相同的 kbase\_queue 绑定到不同的 kbase\_queue\_group 创造了机会,[触发了第二个内存分配](https://cybersecuritynews.com/apple-xnu-kernel-vulnerability-let-attackers-escalate-privileges/),覆盖原始 queange->phys 地址。

利用序列涉及通过以下过程创建页面使用后无条件:首先,攻击者创建并将 kbase\_queue 绑定到 kbase\_queue\_group,将 [GPU](https://cybersecuritynews.com/nvidia-gpu-display-driver-vulnerabilities-2/) 内存页面映射到用户空间。

```
void kbase_csf_free_command_stream_user_pages(struct kbase_context *kctx, struct kbase_queue *queue)
{
    kernel_unmap_user_io_pages(kctx, queue);
    kbase_mem_pool_free_pages(&kctx->mem_pools.small[KBASE_MEM_GROUP_CSF_IO],
        KBASEP_NUM_CS_USER_IO_PAGES, queue->phys, true, false);
}
```

这种无用后状态使攻击者能够操纵已释放的内存页面,并可能将它们重用为页表结构,最终实现任意内核代码执行,同时通过用户空间内存映射绕过MTE保护,从而规避内核级去义检查。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/arm-mali-gpu-vulnerability-let-bypass-mte/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307898](/post/id/307898)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/arm-mali-gpu-vulnerability-let-bypass-mte/)

如若转载,请注明出处： <https://cybersecuritynews.com/arm-mali-gpu-vulnerability-let-bypass-mte/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)