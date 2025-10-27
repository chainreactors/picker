---
title: VMware vRealize Log Insight多个高危漏洞通告
url: https://mp.weixin.qq.com/s?__biz=MzU5MjEzOTM3NA==&mid=2247491787&idx=1&sn=b6e6f73d94e17797f797784791e0d0cd&chksm=fe26e5cac9516cdc7ad4831086fc1426f42ff432a3f66e19a00b1c5365b7446e1131b0f09833&scene=58&subscene=0#rd
source: 三六零CERT
date: 2023-01-31
fetch_date: 2025-10-04T05:14:30.183367
---

# VMware vRealize Log Insight多个高危漏洞通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96fmcWbeMEnsPkcBicAyQdlBcwSDHByjEjLdgEaGWRAmVvOxyRUjhCzvWklrHdcXcS7GFn3bcqeFwtA/0?wx_fmt=png)

# VMware vRealize Log Insight多个高危漏洞通告

原创

360CERT

三六零CERT

**赶紧点击上方话题进行订阅吧！**

报告编号：B6-2023-013001

报告来源：360CERT

报告作者：360CERT

更新日期：2023-01-30

1

漏洞简述

2023年01月30日，360CERT监测发现`VMware官方`发布了`VMware vRealize Log Insight`的风险通告，漏洞编号为`CVE-2022-31706,CVE-2022-31704，CVE-2022-31710，CVE-2022-31711`，漏洞等级：`高危`，漏洞评分：`9.8`。

vRealize Log lnsight 提供了高度可扩展的异构日志管理功能，它具有多个可在其中执行操作的直观仪表盘、完善的分析功能和范围更广的第三方延展性。VMware vRealize Log Insight 提供集中式日志管理、深度运维可见性和智能分析 (sysin)，从基础架构到跨本地部署和私有云环境的应用，都能提供更好的故障排除和更高的安全性。

对此，360CERT建议广大用户及时将`VMware vRealize Log Insight`升级到最新版本。与此同时，请做好资产自查以及预防工作，以免遭受黑客攻击。

2

风险等级

360CERT对该漏洞的评定结果如下

| 评定方式 | 等级 |
| --- | --- |
| 威胁等级 | 高危 |
| 影响面 | 广泛 |
| 攻击者价值 | 高 |
| 利用难度 | 低 |
| 360CERT评分 | 9.8 |

3

漏洞详情

### CVE-2022-31706: VMware vRealize Log Insight目录遍历漏洞

CVE: CVE-2022-31706

组件: vRealize Log Insight

漏洞类型: 目录遍历

影响: 代码执行

简述: 该漏洞存在于vRealize Log Insight中，是一个目录遍历漏洞。未经身份验证的攻击者可以通过组合利用CVE-2022-31706、CVE-2022-31704将恶意文件写入服务器，从而导致远程代码执行。

### CVE-2022-31704: VMware vRealize Log Insight访问控制漏洞

CVE: CVE-2022-31704

组件: vRealize Log Insight

漏洞类型: 代码执行

影响: 服务器接管

简述: 该漏洞存在于vRealize Log Insight中，是一个访问控制漏洞。未经身份验证的攻击者可以通过组合利用CVE-2022-31706、CVE-2022-31704将恶意文件写入服务器，从而导致远程代码执行。

### CVE-2022-31710: VMware vRealize Log Insight 反序列化漏洞

CVE: CVE-2022-31710

组件: vRealize Log Insight

漏洞类型: 反序列化

影响: 拒绝服务

简述: 该漏洞存在于vRealize Log Insight中，是一个反序列化漏洞。未经身份验证的攻击者可以远程触发不可信数据的反序列化，这可能导致拒绝服务。

### CVE-2022-31711: VMware vRealize Log Insight信息泄露漏洞

CVE: CVE-2022-31711

组件: vRealize Log Insight

漏洞类型: 信息泄露

影响: 敏感数据泄漏

简述: 该漏洞存在于vRealize Log Insight中，是一个信息泄露漏洞。攻击者可以在未经身份验证的情况下远程收集敏感会话和应用程序信息。

4

影响版本

| 组件 | 影响版本 | 安全版本 |
| --- | --- | --- |
| VMware vRealize Log Insight | 8.x < 8.10.2 | 8.x >= 8.10.2 |
| VMware Cloud Foundation (VMware vRealize Log Insight) | 3.x | - |
| VMware Cloud Foundation (VMware vRealize Log Insight) | 4.x | - |

5

修复建议

### 通用修补建议

根据`影响版本`中的信息，排查并升级到`安全版本`。

#### VMware vRealize Log Insight

下载链接：*https://docs.vmware.com/en/vRealize-Log-Insight/8.10.2/rn/vrealize-log-insight-8102-release-notes/index.html*

#### VMware Cloud Foundation (VMware vRealize Log Insight)

参考链接：*https://kb.vmware.com/s/article/90668*

### 临时修补建议

可参考VMware官方给出的修复方案：

*https://kb.vmware.com/s/article/90635*

6

产品侧解决方案

若想了解更多产品信息或有相关业务需求，可移步至http://360.net。

### 360企业安全云

用户可以通过安装360安全卫士并进行全盘杀毒来维护计算机安全。360CERT建议广大用户使用360安全卫士定期对设备进行安全检测，以做好资产自查以及防护工作。

![](https://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96dfXnnIZzibDwWWss5AEEHH2bPxzkTWpWDIib2iclPyjLm7xDjAr3iaGGVqkia7KcFIKgLRS2przd3KsVw/640)

### 360威胁情报平台（TIP）

360威胁情报平台（TIP）一款构建全面情报管理、赋能、评价、分享能力的新一代本地化情报平台。可以用来增强对关键威胁的检测；可以自动化识别报警中的重点事件；还可以提供情报分析、外部攻击面管理、行业威胁情报等高阶能力，帮助组织全面应对数字时代的安全风险。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ic3Rgfdm96dfXnnIZzibDwWWss5AEEHH2jAKh3qqa2YIqPUfZNNssqFSq3xL6pjeTuTrjvF82D1IS1Asuw9KqGA/640)

### 360安全分析响应平台

360安全大脑的安全分析响应平台通过网络流量检测、多传感器数据融合关联分析手段，对该类漏洞的利用进行实时检测和阻断，请用户联系相关产品区域负责人获取对应产品。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ic3Rgfdm96eZuuPLhqHNsNqvIqiaeibiaSnG76OsuLsFhKJN8lPMZXqNhhzSL0VkEicmHHia78A8qCDjbMrKce0GVeQ/640)

### 360本地安全大脑

360本地安全大脑是将360云端安全大脑核心能力本地化部署的一套开放式全场景安全运营平台，实现安全态势、监控、分析、溯源、研判、响应、管理的智能化安全运营赋能。360本地安全大脑已支持对相关漏洞利用的检测，请及时更新网络神经元（探针）规则和本地安全大脑关联分析规则，做好防护。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ic3Rgfdm96dfXnnIZzibDwWWss5AEEHH2Sr4ZMnHibodT61ZTb189xlWg8qqhVL3Mc7nKXSE0Y7xL9HohhGYo3nA/640)

7

时间线

**2023-01-24** VMware官方发布通告

**2023-01-30** 360CERT发布通告

8

参考链接

1.*https://www.vmware.com/security/advisories/VMSA-2023-0001.html*

9

特制报告相关说明

一直以来，360CERT对全球重要网络安全事件进行快速通报、应急响应。为更好地为政企用户提供最新漏洞以及信息安全事件的安全通告服务，现360CERT推出了安全通告特制版报告订阅服务，以便用户做资料留存、传阅研究与查询验证。

今后特制报告将不再提供公开下载，用户可扫描下方二维码进行服务订阅。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ic3Rgfdm96dGuACWTa4BQzhoMl3chI7Tdch7TU5O21ECnPYAkbzMTfjcuvslias51NRldtrfia2XCvoI05Q91X8Q/640?wx_fmt=jpeg)

往期推荐

01

[2022年勒索病毒流行态势报告](http://mp.weixin.qq.com/s?__biz=MzU5MjEzOTM3NA==&mid=2247491771&idx=1&sn=220399a6a63b60869f8555753b0ca38e&chksm=fe26e5bac9516cacdd0e2b2105c3ec66272abbd33ec923a463f4d95073953ef4e2397c35f762&scene=21#wechat_redirect)

02

[CVE-2023-21839：Oracle WebLogic Server 远程代码执行漏洞通告](http://mp.weixin.qq.com/s?__biz=MzU5MjEzOTM3NA==&mid=2247491768&idx=1&sn=522a1c2a2b080255adb748ac54afa6ac&chksm=fe26e5b9c9516cafa272589c07fc294edd76d51e933ce63b451fd46f40d52171dbebf67e9496&scene=21#wechat_redirect)

03

[2023-01 补丁日: Oracle多个产品漏洞安全风险通告](http://mp.weixin.qq.com/s?__biz=MzU5MjEzOTM3NA==&mid=2247491768&idx=2&sn=cd6ba0802a47bc1446eea686d4d1a2e1&chksm=fe26e5b9c9516caffd97886c53782732c1729d1b57a7bd14afeb9c9a18211051a64928e9b0a6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96fDEiaYRAwzeORXyPTzIZEicJEJchzE6NNx8UKdqTdwDHNIYmwsIK7JlquzGrjaQS7ssnemOGtsTvYw/640?wx_fmt=png)

360CERT

https://cert.360.cn/

进入官网查看更多资讯

长按扫码关注我们

![](https://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96fDEiaYRAwzeORXyPTzIZEicJJ6oj5eUnvicLHzb45xcpgT8bhs83yg8VQjlRo8Av3jvfEv1NNMfHvRA/640 "微信公众号二维码.jpg")

![](https://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96fDEiaYRAwzeORXyPTzIZEicJLRf9N0If8jPYhCicZ5sao1dWa48hVm5xpUskBUnDMYmvTJHpsWTmBsw/640?wx_fmt=png)

点击在看，进行分享

![](https://mmbiz.qpic.cn/mmbiz_gif/Ic3Rgfdm96fDEiaYRAwzeORXyPTzIZEicJX2oU8HWWic5QdjaCkRHBK3anwULoleLibhW5SnibSGWCF1fjkYS5ia8JPg/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96ehiaKaNLl4R2jEAKbwYWArdHJBHLPsfvia7icjTiaGrgEvu6D11iaH6NLKSibIZxPSaiaiaQE0O5WfrpicKcQ/0?wx_fmt=png)

三六零CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96ehiaKaNLl4R2jEAKbwYWArdHJBHLPsfvia7icjTiaGrgEvu6D11iaH6NLKSibIZxPSaiaiaQE0O5WfrpicKcQ/0?wx_fmt=png)

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