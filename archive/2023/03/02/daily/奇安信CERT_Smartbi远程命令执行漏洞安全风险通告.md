---
title: Smartbi远程命令执行漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497863&idx=1&sn=b1491f0343ff76f15ba2e6269ad8cfbb&chksm=fe79dc1fc90e5509806ac5ec072a93dad754cb32b4742a54150ae000c701447adcb2ad785c41&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2023-03-02
fetch_date: 2025-10-04T08:27:14.211630
---

# Smartbi远程命令执行漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icicQEb8qESTOo4089m2GRQZQA8iao9me772XvfBmAM3Ac5peg2HJjTRYibEZxmKtLiand9640qhttTmg/0?wx_fmt=jpeg)

# Smartbi远程命令执行漏洞安全风险通告

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

Smartbi是广州思迈特软件有限公司旗下的商业智能BI和数据分析品牌，为企业客户提供一站式商业智能解决方案。Smartbi大数据分析产品融合BI定义的所有阶段，对接各种业务数据库、数据仓库和大数据分析平台，进行加工处理、分析挖掘和可视化展现；满足所有用户的各种数据分析应用需求，如大数据分析、可视化分析、探索式分析、复杂报表、应用分享等等。

近日，奇安信CERT监测到Smartbi官方发布安全更新，其中包含**Smartbi 远程命令执行漏洞**。Smartbi大数据分析平台存在远程命令执行漏洞，未经身份认证的远程攻击者利用此漏洞向系统发送恶意数据，可能执行任意命令，导致系统被攻击与控制。**鉴于此产品用量较多，建议客户尽快更新至最新版本。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Smartbi** **远程命令执行漏洞** | | |
| **公开时间** | 2023-02-28 | **更新时间** | 2023-03-01 |
| **CVE****编号** | 暂无 | **其他编号** | QVD-2023-5326 |
| **威胁类型** | 命令执行 | **技术类型** | 命令注入 |
| **厂商** | 广州思迈特软件有限公司 | **产品** | Smartbi |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未公开 |
| **漏洞描述** | Smartbi大数据分析平台存在远程命令执行漏洞，该漏洞为Smartbi DB2 命令执行漏洞的补丁绕过，未经身份认证的远程攻击者利用此漏洞向系统发送恶意数据，可能执行任意命令，导致系统被攻击与控制。 | | |
| **影响版本** | V7 <= Smartbi <= V10.5.8 | | |
| **其他受影响组件** | 无 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Smartbi 远程命令执行漏洞 | | | |
| **CVE****编号** | 暂无 | **其他编号** | | QVD-2023-5326 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 不需要 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 未经身份认证的远程攻击者利用此漏洞向系统发送恶意数据，可能执行任意命令，导致系统被攻击与控制。 | | | |

处置建议

目前 Smartbi官方已发布安全版本修复该漏洞，建议受影响用户尽快进行安全更新。

**自动升级：**

登录后台->右上角系统监控->系统补丁->安装补丁->在线更新

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icicQEb8qESTOo4089m2GRQZYib7sPEIYTVO6H5sz2VXFokgP8vlQHWZXicRKKth5s0tRrvcxBpvLnhA/640?wx_fmt=png)

**手动升级：**

下载补丁->登录后台->右上角系统监控->系统补丁->安装补丁->手动更新

补丁下载地址：https://www.smartbi.com.cn/patchinfo

详情可参考：

https://wiki.smartbi.com.cn/pages/viewpage.action?pageId=50692623

参考资料

[1]https://www.smartbi.com.cn/patchinfo

[2]https://wiki.smartbi.com.cn/pages/viewpage.action?pageId=50692623

时间线

2023年3月1日，奇安信 CERT发布安全风险通告。

点击**阅读原文**

到奇安信NOX-安全监测平台查询更多漏洞详情

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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