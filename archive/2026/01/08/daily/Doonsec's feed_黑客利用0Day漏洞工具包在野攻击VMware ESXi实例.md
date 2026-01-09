---
title: 黑客利用0Day漏洞工具包在野攻击VMware ESXi实例
url: https://mp.weixin.qq.com/s/RkoaOPT2SHSLU1qLHgO-tg
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:29:27.573046
---

# 黑客利用0Day漏洞工具包在野攻击VMware ESXi实例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR394NmBBpZoDqlukekR6EWdYpIJuB1nD9R18R7Qratic7miaMRwEnb9RQT8PkbrGqicJ8FeprficKkTibHw/0?wx_fmt=jpeg)

# 黑客利用0Day漏洞工具包在野攻击VMware ESXi实例

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR394NmBBpZoDqlukekR6EWdYcXo4hNciaIyBg31cpMrrzcblIia2uLK9S8iahH8LYopAMdx0P5LcDAY7A/640?wx_fmt=jpeg&from=appmsg)

网络安全公司Huntress发现黑客正在利用一个0Day漏洞工具包攻击VMware ESXi实例，该工具包通过串联多个漏洞实现虚拟机逃逸。攻击者最初通过被入侵的SonicWall VPN获得初始访问权限。

**Part01**

## ****攻击过程分析****

威胁行为者首先通过SonicWall VPN获得立足点，随后利用被入侵的域管理员账户进行横向移动，先后攻陷备份域控制器和主域控制器。在主域控制器上，攻击者部署了Advanced Port Scanner和ShareFinder等侦察工具，使用WinRAR暂存数据，并修改Windows防火墙规则以阻止外部出站流量，同时允许内部横向移动。

在部署漏洞工具包约20分钟后，攻击者开始执行ESXi漏洞利用程序，Huntress在勒索软件部署前成功阻止了攻击。

**Part02**

## ****MAESTRO漏洞工具包技术细节****

```

```

Huntress将该工具包命名为MAESTRO，其工作原理包括：

* 使用devcon.exe禁用VMware VMCI驱动程序
* 通过KDU加载未签名驱动程序以绕过驱动程序签名强制（DSE）
* 执行核心逃逸操作

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR394NmBBpZoDqlukekR6EWdY8BQdt8ovnlccN4b14cLtXo0zw2ycAIPXgNPHKq5aXXQONLVVmdoPAg/640?wx_fmt=jpeg&from=appmsg)

工具包截图（来源：Huntress）

MyDriver.sys驱动程序通过VMware Guest SDK查询ESXi版本，从支持ESXi 5.1至8.0共155个构建版本的数据表中选择偏移量，通过HGFS（CVE-2025-22226）泄露VMX基址，通过VMCI（CVE-2025-22224）破坏内存，并部署用于沙箱逃逸的shellcode（CVE-2025-22225）。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR394NmBBpZoDqlukekR6EWdY1AHjmuZERu2CpOwNZQU4OcTIibIUWl6TSE8mghzXAzbjwhjbbmadtug/640?wx_fmt=png&from=appmsg)

Shellcode会部署名为VSOCKpuppet的后门程序，该后门劫持ESXi的inetd服务（端口21）以获取root权限，并使用VSOCK进行隐蔽的虚拟机-宿主机通信，这种通信方式对网络监控工具不可见。

**Part03**

## ****攻击溯源与防御建议****

```

```

PDB路径显示该工具包在简体中文环境中开发，如"全版本逃逸--交付"的路径名称，时间戳为2024年2月，比Broadcom在2025年3月4日发布的VMSA-2025-0004安全公告早了一年多。2023年11月的client.exe PDB表明该工具采用模块化设计，被篡改的VMware驱动程序引用了"XLab"。Huntress高度确信攻击者来自中文环境，基于资源文件和0Day漏洞获取能力。

防御建议：

* 及时为ESXi打补丁，已停止支持的版本无法获得修复
* 使用"lsof -a"命令监控ESXi主机的VSOCK进程
* 警惕KDU等BYOD加载器
* 加强VPN安全防护
* 防火墙规则变更和未签名驱动程序都是系统被入侵的信号
* VSOCK后门可绕过入侵检测系统（IDS）

此次事件凸显了虚拟机监控程序面临的持续威胁，攻击者通过驱动程序恢复和配置清理保持隐蔽性。随着针对ESXi的勒索软件攻击增加，企业必须加强虚拟化环境的安全防护。

**参考来源：**

Hackers Exploiting VMware ESXi Instances in the Wild Using zero-day Exploit Toolkit

https://cybersecuritynews.com/vmware-esxi-exploited-toolkit/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39H4eicalbOEwZ1t8X3mSSZssMSDW4LkuO5g3W31c7ibGVXTlUPk3BqrUoic8Rqt25DJOCygq1FzABicw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651333596&idx=1&sn=a5f1d8decaf400a24f3b9e74a3a357e1&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLq7T2qZrtcsoq5PRQ2cjDU1HUaakGzExOsSIU2Quxiasf7W9ibLiaEsmWA/640?wx_fmt=png&from=appmsg)

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