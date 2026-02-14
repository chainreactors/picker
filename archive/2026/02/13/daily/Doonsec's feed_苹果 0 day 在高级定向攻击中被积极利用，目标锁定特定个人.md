---
title: 苹果 0 day 在高级定向攻击中被积极利用，目标锁定特定个人
url: https://mp.weixin.qq.com/s/KwwxzsIfeWeBPIwk1e0I2A
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:04:52.522264
---

# 苹果 0 day 在高级定向攻击中被积极利用，目标锁定特定个人

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnvQSVulYQicJ4UIKFz2qPR46tUS8z70JL5MEJibXrNdptA4ic93QQprK4hxrpzVLT4iaYu4oKlnhrBWvOwzGZhia4SGeNvKDSTp5nmc/0?wx_fmt=jpeg)

# 苹果 0 day 在高级定向攻击中被积极利用，目标锁定特定个人

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnue7h1jIkXcz7WDJk0bnRq0bf8vpic9K5xicacGspbU98eHoEMz3WIg1ZIMqa5PTGkR08UjMpYgiaS0HJnqdOeMgPU1tUHLObaTMg/640?wx_fmt=jpeg&from=appmsg)

苹果公司于2026年2月11日发布iOS 26.3和iPadOS 26.3系统更新，修复了**40余个安全漏洞**，其中包括一个在**dyld组件中被积极利用的关键零日漏洞**（CVE-2026-20700），该漏洞已被用于针对特定个人的**高度复杂定向攻击**。

### 漏洞技术细节

1. **漏洞本质与影响**

* CVE-2026-20700是dyld组件中的**内存损坏漏洞**，由谷歌威胁分析小组(TAG)发现，允许攻击者在获得**内存写入权限**后执行**任意代码**
* dyld作为苹果**动态链接编辑器**，负责iOS、macOS等平台**动态库的加载与链接**，此漏洞源于**不当的状态管理**，导致内存损坏进而引发代码执行
* 苹果指出该漏洞是"针对特定目标个人的极端复杂攻击"的一部分，与2025年12月修复的CVE-2025-14174和CVE-2025-43529漏洞相关联

2. **攻击链分析**

* 攻击链可能始于**鱼叉式钓鱼邮件**或**零点击漏洞**，先获取内存写入权限
* 攻击者随后**利用dyld漏洞实现持久化或权限提升**，绕过**指针认证码(PAC)**和**KASLR**等防护机制
* 此方法可**安装持久化间谍软件**，用于**数据外泄**，目标包括**记者、活动人士**等高价值个人，与**飞马(Pegasus)**等国家级间谍软件活动模式一致

3. **修复与影响范围**

* 苹果通过"**改进状态管理**"修复漏洞，可能增强了dyld内存分配和链接阶段的验证
* 受影响设备包括**iPhone 11+**、**最新iPad Pro**、**Air**和**mini**系列，全球**数亿设备面临风险**
* 本次更新共修复**37+个漏洞**，涵盖**Accessibility**(锁屏信息泄露)、**内核**(root权限提升)、**WebKit**(拒绝服务/崩溃)和**Sandbox**(逃逸)等关键组件

### 防御建议

1. **用户行动指南**

* **立即更新**：通过"设置 > 通用 > 软件更新"安装最新系统版本
* **禁用不必要的功能**：如iPhone镜像(修复了UI问题CVE-2026-20640)
* **启用锁定模式**：高风险用户应开启此模式以增强安全性

2. **企业级防护措施**

* **实施MDM策略**：强制执行设备更新和安全配置
* **监控异常活动**：通过Apple Unified Logging监控设备行为
* **配置应用控制**：使用AppLocker或Windows Defender应用控制限制.scr文件执行
* **建立RMM白名单**：严格管控远程管理软件安装，阻止未经授权的工具

### 安全态势评估

这是苹果**2026年首个被积极利用的零日漏洞**，延续了2025年修复**7个零日漏洞**的趋势，表明**高级威胁持续存在**。虽然目前攻击主要针对**特定个人**，但随着补丁普及率不足，**漏洞可能被更广泛利用**。网络安全专业人员应密切关注**CISA KEV目录**，及时获取安全更新信息，并考虑实施**硬件级防御**以应对日益复杂的内存损坏攻击。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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