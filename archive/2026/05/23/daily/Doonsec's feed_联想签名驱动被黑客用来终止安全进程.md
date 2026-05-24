---
title: 联想签名驱动被黑客用来终止安全进程
url: https://mp.weixin.qq.com/s/4Wb5HYz757Dy7eJMstA-mA
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:47.690002
---

# 联想签名驱动被黑客用来终止安全进程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3ukyRwN8CVU3DemEFsca520UdicrZWHEBS9qPBWLLic1LRgO3ZB8RBOvQ9vqJelKWcgp7IZn5Gu5fkWHSEMUkxMLOOORofXM0icg/0?wx_fmt=jpeg)

# 联想签名驱动被黑客用来终止安全进程

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0fJTX3LuBCib5ibbwDEAAYI3ecGbazgxY8hNI2BsPa2Dic2Hf4BE9m7jZD9yfBe5mZCM0ktmkBL1KeHHXrUhYZ03CcgLMicqw4URQ/640?wx_fmt=jpeg&from=appmsg)

安全研究人员发现，黑客可利用联想公司合法签名的驱动程序BootRepair.sys强制终止安全进程，这揭示了一种危险的BYOVD（自带漏洞驱动）攻击载体，可绕过端点防护机制。

**Part01**

## 驱动漏洞技术分析

安全专家Jehad Abudagga对联想PC Manager工具配套的BootRepair.sys驱动进行分析后发现，该驱动可在内核层面终止任意进程。该驱动具有联想有效数字签名，分析时在VirusTotal平台零检出，使其成为隐蔽攻击的理想选择。

![VirusTotal检测结果（来源：Jehad Abudagga）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0RwSviaoXZKhia6fdZXKQNG8gynN0ibsora5WAmKYrYlhdrzkAjfKgeNEtVe5Iez54JZH5J90bBlic1btDkAcfpaLs4s4LDm9XO1c/640?wx_fmt=jpeg&from=appmsg)

逆向工程显示该驱动存在多项安全缺陷：

* 创建的\Device\::BootRepair设备对象未设置安全DACL，允许低权限用户交互
* 通过\DosDevices\BootRepair符号链接向用户态程序暴露设备接口
* 处理IRP\_MJ\_CREATE请求时未实施访问控制检查，任何用户均可获取驱动句柄

**Part02**

## **攻击实现机制**

IOCTL处理程序分析表明，驱动暴露的0x222014控制码可接收4字节输入缓冲区，其中包含传递给内部例程的进程PID。该功能通过Windows内核API ZwTerminateProcess终止指定进程，使攻击者能关闭包括安全防护服务在内的任意进程。

![进程终止功能实现（来源：Jehad Abudagga）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3pA5iaN1V1mmGLo4TR66q96Gs5FTr5KhtF7Vs6h1FVMicz8KRb2guYXzP3knXI1icRGMxNibBl59Cermv1d1xTnYITJQwvkLcicg6c/640?wx_fmt=jpeg&from=appmsg)

漏洞支持两种攻击场景：

* 系统已存在该驱动时，低权限攻击者可直接终止杀毒/EDR进程
* 驱动未部署时，攻击者可将其作为BYOVD攻击组件加载入内核，在渗透后工具执行前关闭防护

PoC演示显示，加载驱动后连CrowdStrike Falcon传感器等受保护进程也可被终止。

![CrowdStrike进程被终止（来源：Jehad Abudagga）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2qe6YcbCeJDYkOcSRFFXSdcdIGvZEHrgBxRJn4SHXL8jHibiboL6rkXwWzgZvftpCCCf6mAfShLzUtXsLH4ZPhyicPUTEwaySjT0/640?wx_fmt=jpeg&from=appmsg)

**Part03**

## **安全防护建议**

当Bandizip.exe启动后，攻击进入DLL劫持阶段。攻击者将恶意DLL"ark\_x86.dll"与合法可执行文件置于同一隐藏目录，利用Windows正常的DLL搜索顺序加载攻击者控制的库而非可信系统副本。该DLL中的"CreateArk"导出函数会执行多项反调试检查和解密例程，最终在内存中解包运行Cobalt Strike信标，而不会在磁盘留下传统可执行文件。

该事件凸显BYOVD攻击威胁升级——攻击者正滥用受信任的签名驱动破坏端点防护。由于驱动具有合法签名且初始零检出，可规避依赖签名信任的传统防护措施。建议企业采取以下措施：

* 使用微软推荐驱动黑名单拦截已知漏洞驱动
* 监控可疑驱动加载及内核级行为
* 限制未签名/未批准驱动的加载权限
* 部署能检测合法驱动滥用的EDR防护

![终止CrowdStrike后运行mimikatz（来源：Jehad Abudagga）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2TREzhTDhY60qjiaibPo6EyoPKL6AMA30sHSDVmMg17xwMibwqhFjzTne20z0x3F6sRmm8IGLqM8fwB7hKQM2zMHb2fQHB2v7JoQ/640?wx_fmt=jpeg&from=appmsg)

随着攻击者持续滥用可信组件，主动的驱动控制与行为检测仍是防护现代端点的关键。

|
|  |

**参考来源：**

Hackers Can Weaponize Lenovo Driver to Terminate EDR Processes

https://cybersecuritynews.com/lenovo-driver-terminate-edr-processes/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0TPDSBGWyOrBX6roghTcfJ7S0Uk6LPc6NiazIJCibS6wTdC64AxlpIAv3YZ2LoZFsJy3UHwic3ohlaRGRMZkKBW03QD5AMj5yuicM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338385&idx=1&sn=a442efc5bf8726e3e4239bc246e2976b&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2A30nW87bmYJO7PWcHicOLnjA5DRaqykn6a3r9Nvg2PUTX1XkGuXcekoXza0aIXeq8O4ZwnhjLdFba5NEv5NQetNb0KjM9Mnb8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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