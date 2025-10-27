---
title: 关于VMware vCenter Server存在堆溢出漏洞的安全公告
url: https://mp.weixin.qq.com/s?__biz=MzU3ODM2NTg2Mg==&mid=2247495387&idx=1&sn=4b11b67781cc01260f323237f4760f1d&chksm=fd74de12ca03570409b90f05069bcce53813287269fc25f8a73f92667d6a9d85378ee794eb27&scene=58&subscene=0#rd
source: CNVD漏洞平台
date: 2024-10-25
fetch_date: 2025-10-06T18:52:32.830525
---

# 关于VMware vCenter Server存在堆溢出漏洞的安全公告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pMINP9OQkbgPtiaJNGAhKILyJ95GJl8TyUkUxNdwibfVedH3AxgvpcgM0IPFx8zibLicwJVzuABJxK1GZ1oNOGsliaQ/0?wx_fmt=jpeg)

# 关于VMware vCenter Server存在堆溢出漏洞的安全公告

原创

CNVD

CNVD漏洞平台

安全公告编号:CNTA-2024-0018

2024年10月23日，国家信息安全漏洞共享平台（CNVD）收录了VMware vCenter Server堆溢出漏洞（CNVD-2024-41447，对应CVE-2024-38812）。具有网络访问权限的攻击者可利用漏洞远程执行代码，获取服务器控制权限。官方已于10月21日发布安全公告修复该漏洞，CNVD建议受影响的单位和用户安全升级到最新版本。

**一、漏洞情况分析**

VMware vCenter Server是VMware公司提供的一款虚拟化服务器管理平台，用于集中管理和监控VMware vSphere虚拟化环境。

近日，VMware公司发布安全公告修复了VMware vCenter Server堆溢出漏洞。vCenter Server的远程过程调用（DCERPC）协议实现存在堆溢出漏洞，具有vCenter Server网络访问权限的恶意攻击者可利用该漏洞，通过远程发送特制的网络数据包来触发该漏洞，从而执行任意代码，实现对服务器的权限获取和完全控制。

CNVD对该漏洞的综合评级为“高危”。

**二、漏洞影响范围**

漏洞影响的产品和版本：

VMware vCenter Server 8.0 < 8.0 U3d

VMware vCenter Server 8.0 < 8.0 U2e

VMware vCenter Server 7.0 < 7.0 U3t

VMware Cloud Foundation 5.x < 8.0 U3d

VMware Cloud Foundation 5.x < 8.0 U2e

VMware Cloud Foundation 4.x < 7.0 U3t

**三、漏洞处置建议**

目前，VMware公司已发布新版本修复该漏洞，CNVD建议受影响用户升级至最新版本：

VMware vCenter Server 8.0 U3d

VMware vCenter Server 8.0 U2e

VMware vCenter Server 7.0 U3t

VMware Cloud Foundation 5.x 8.0 U3d

VMware Cloud Foundation 5.x 8.0 U2e

VMware Cloud Foundation 4.x 7.0 U3t

官方下载链接及文档地址：

VMware vCenter Server 8.0 U3d：

https://support.broadcom.com/web/ecx/solutiondetails?patchId=5574

https://docs.vmware.com/en/VMware-vSphere/8.0/rn/vsphere-vcenter-server-80u3d-release-notes/index.html

VMware vCenter Server 8.0 U2e：

https://support.broadcom.com/web/ecx/solutiondetails?patchId=5531

https://docs.vmware.com/en/VMware-vSphere/8.0/rn/vsphere-vcenter-server-80u2e-release-notes/index.html

VMware vCenter Server 7.0 U3t：

https://support.broadcom.com/web/ecx/solutiondetails?patchId=5580

https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-vcenter-server-70u3t-release-notes/index.html

Cloud Foundation 5.x/4.x：

https://knowledge.broadcom.com/external/article?legacyId=88287

参考链接：

https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24968

感谢奇安信网神信息技术（北京）股份有限公司为本报告提供的技术支持。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/pMINP9OQkbhv2uDwc7hNMH9gPUUt39C13bYw7EhIhmITpa6692RtN0xDyb4rTiaTpewIpuGUrD1Ckf1lCVStiaRg/0?wx_fmt=png)

CNVD漏洞平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pMINP9OQkbhv2uDwc7hNMH9gPUUt39C13bYw7EhIhmITpa6692RtN0xDyb4rTiaTpewIpuGUrD1Ckf1lCVStiaRg/0?wx_fmt=png)

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