---
title: EDRStartupHinder可阻断Windows 11启动时的杀毒软件与EDR服务
url: https://mp.weixin.qq.com/s/9Odd_8dSuaQIOdumOMQGqQ
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:29:29.729784
---

# EDRStartupHinder可阻断Windows 11启动时的杀毒软件与EDR服务

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR383C7pgG0CK9dk0C3ZMfp7t9buYdvUibvn7x0A6uFPW61XQ5zz8Jso4gZdOWA9q3S4XH0LdreqONjw/0?wx_fmt=jpeg)

# EDRStartupHinder可阻断Windows 11启动时的杀毒软件与EDR服务

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR383C7pgG0CK9dk0C3ZMfp7tH1FVJk1M067Mrp7GHZ8JLngDXZbmKAbnlGYD5kFsLRkr1R6YfmaAYw/640?wx_fmt=jpeg&from=appmsg)

以开发EDR-Freeze和EDR-Redir等EDR规避工具闻名的安全研究员TwoSevenOneT，本周发布了EDRStartupHinder工具。该工具通过Windows Bindlink重定向关键的System32 DLL，在Windows 11 25H2系统的Windows Defender上演示了如何阻断杀毒软件和EDR服务的启动。

**Part01**

## ****杀毒软件与EDR的运行机制****

杀毒软件和EDR服务虽然以标准Windows服务形式运行，但通过内核驱动提供增强保护。它们以SYSTEM权限运行，开机自动启动，并采用受保护进程轻量级（PPL）机制防止用户模式篡改。用户模式的配置更改会失效，除非使用EDR-Freeze等高级技术，否则无法修改这些进程。

**Part02**

## ******当前解决方案******

由于Microsoft Defender默认启用，用户需前往安全中心临时关闭防护才能完成激活。操作完成后应立即恢复防护措施。必须特别强调：操作时需极度警惕域名准确性。若在关闭防护时误执行钓鱼脚本，系统将完全暴露于恶意软件威胁之下，可能导致灾难性数据泄露或其他安全事件。

**Part03**

## ******Bindlink启动阻断技术******

此前EDR-Redir等技术在服务启动后重定向EDR文件夹，但已被厂商防御。EDRStartupHinder通过针对所有进程（包括EDR）必需的System32目录实现先发制人。

![EDRStartupHinder Tool](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR383C7pgG0CK9dk0C3ZMfp7tcP8XDMgOzkzqzaDQZiaTR05vE7frb1yXds3nEhGyuxibl8vCXdvA8z7g/640?wx_fmt=jpeg&from=appmsg)

具体步骤包括：

* 创建更高优先级的服务
* 通过Bindlink将核心DLL重定向到未签名的"损坏"副本
* 利用PPL机制使EDR在加载失败时崩溃
* 终止后清理痕迹

服务优先级参考BYOVD研究，检查注册表项HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\ServiceGroupOrder。目标DLL需避开KnownDLLs预加载列表（可通过Process Monitor识别）。

**Part04**

## ******工具参数与实战演示******

该工具GitHub版本包含以下参数：

* OriginalLib（System32 DLL路径）
* FakeLib（副本位置）
* ServiceName/Group（优先级）
* EDRProcess（目标进程如MsMpEng.exe）

工具会破坏FakeLib的PE头签名，注册为服务后动态监控EDR启动并应用/移除Bindlink。用户需使用Process Explorer分析启动日志确定EDR特定DLL和服务组。

在Windows 11 25H2测试环境中，针对Defender引擎MsMpEng.exe和启动加载的msvcp\_win.dll，使用TDI服务组优先级的命令示例：

```
EDRStartupHinder.exe msvcp_win.dll C:\TMP\FakeLib DusmSVC-01 TDI MsMpEng.exe
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR383C7pgG0CK9dk0C3ZMfp7tIeMccSdJeOBQN6ghZzcs2fsBhvS7nb7BC9GjUKOiaP6a0DTHYsE2nAA/640?wx_fmt=jpeg&from=appmsg)

重启后服务优先激活并重定向DLL，受PPL保护的MsMpEng.exe会拒绝未签名DLL并自我终止。

**Part05**

## ******防御建议******

系统管理员应监控：

* bindlink.dll使用情况
* 高优先级组中的可疑服务
* System32目录异常

纵深防御措施包括：

* 扩展KnownDLLs列表
* 加强签名验证审计
* 启用minifilter日志记录

厂商需强化DLL依赖关系和启动顺序防护。该技术证明Windows机制对红队是把双刃剑，实验室测试中可有效对抗Defender和未具名商业EDR/杀毒软件。

**参考来源：**

New EDRStartupHinder Tool blocks antivirus and EDR services at startup on Windows 11 25H2 Defender

https://cybersecuritynews.com/edrstartuphinder-tool/

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