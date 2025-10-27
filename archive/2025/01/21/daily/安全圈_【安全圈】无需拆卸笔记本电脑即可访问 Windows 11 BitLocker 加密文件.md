---
title: 【安全圈】无需拆卸笔记本电脑即可访问 Windows 11 BitLocker 加密文件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067503&idx=4&sn=17aa39950a2ad339c5c9189715ebc4f2&chksm=f36e7aefc419f3f9cb51bb87bb1f571572cf3b66429795fbd19cc7536069f74aa0232d0c9cc2&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-21
fetch_date: 2025-10-06T20:11:12.283199
---

# 【安全圈】无需拆卸笔记本电脑即可访问 Windows 11 BitLocker 加密文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhBf5lNicbVc7sJQicibeBrdcUWfxjKMvpoMftrqGoRJRL5vYbcuFiaaupE6MBu3F3F8dCuZd9t5ypMLA/0?wx_fmt=jpeg)

# 【安全圈】无需拆卸笔记本电脑即可访问 Windows 11 BitLocker 加密文件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Windows

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhBf5lNicbVc7sJQicibeBrdcUIZcL7icUaQcJDXl1SYGA1RFIy0icZkXGoNKicwRXH2h0X1gYI8FHnzicicw/640?wx_fmt=jpeg&from=appmsg)

研究人员演示了攻击者如何在不实际篡改设备的情况下绕过其保护措施。安全研究员 Thomas Lambertz 在混沌通信大会 (38C3) 上展示了该漏洞，该漏洞被称为“bitpixie”(CVE-2023-21563)。

“bitpixie”漏洞利用对Windows 启动管理器的降级攻击来绕过安全启动。

此漏洞凸显了 Windows 11 上 BitLocker 默认配置中的一个严重缺陷，对依赖它进行数据保护的用户敲响了警钟。

BitLocker 是微软的全盘加密技术，旨在通过加密整个驱动器来保护敏感数据。它依靠安全启动和受信任平台模块 (TPM) 来确保加密密钥仅在启动期间发布给受信任的组件。然而，bitpixie 漏洞利用了此过程中的一个设计缺陷。

“这个漏洞被称为 bitpixie，它依赖于降级 Windows 启动管理器。攻击者只需要插入 LAN 电缆和键盘即可解密磁盘，”Thomas补充道。

## **该漏洞如何发挥作用？**

该漏洞源于 Windows 启动管理器在特定恢复流程中未能从内存中清除加密密钥。攻击者可以通过将引导加载程序降级为较旧的易受攻击的版本来利用此漏洞。此过程涉及：

1. **引导加载程序降级**：使用网络启动（PXE 启动），攻击者加载仍然包含漏洞的过时的 Windows 启动管理器。
2. **触发恢复模式**：降级的引导加载程序启动恢复序列，将卷主密钥 (VMK)（解密受 BitLocker 保护的数据所需的密钥）留在系统内存中。
3. **内存转储**：然后攻击者启动到Linux 环境并使用取证工具从内存中提取 VMK。
4. **解密数据**：有了 VMK，攻击者就可以完全访问加密驱动器。

这种攻击不需要打开笔记本电脑或访问内部组件，因此对于被盗设备来说尤其令人担忧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhBf5lNicbVc7sJQicibeBrdcUNdRIg84iak2YqYYkxm6U4Rs1PicQ7Jq0EFXRPfmB9HweKcQ45BT4UyeA/640?wx_fmt=png&from=appmsg)

bitpixie 漏洞凸显了BitLocker在依赖安全启动和 TPM 进行无人值守解密方面的严重弱点。

虽然这些机制旨在通过在启动过程中自动解锁驱动器来简化用户体验，但它们在被利用时也会产生漏洞。

主要关注点包括：

* **广泛适用性**：该漏洞影响所有使用 BitLocker 默认“设备加密”模式的设备，该模式在许多 Windows 11 系统上默认启用。
* **执行的简易性**：攻击只需要对设备进行物理访问以及键盘和网络连接等基本工具。
* **持续风险**：尽管微软在 2022 年底发布了补丁，但由于安全启动证书撤销的限制，攻击者仍然可以通过引导加载程序降级绕过保护措施。

### **缓解策略**

微软承认，要完全解决这一缺陷确实存在挑战。虽然较新的引导加载程序已经修复了此问题，但由于安全启动无法普遍实施严格的降级保护，旧版本仍然可能被利用。为了降低风险，建议用户实施额外的安全措施：

1. **启用预启动身份验证**：使用预启动 PIN 配置 BitLocker 可确保在没有用户交互的情况下不会自动释放加密密钥。
2. **应用 KB5025885 更新**：此更新引入了额外的安全启动证书并撤销了旧证书，从而减少了降级攻击的风险。
3. **调整 PCR 配置**：更改 TPM 平台配置寄存器 (PCR) 以包含额外测量可以防止未经授权的密钥释放。
4. **禁用网络启动选项**：在 BIOS/UEFI 设置中限制 PXE 启动功能可以阻止主要攻击媒介之一。

像 bitpixie 这样的漏洞持续存在，凸显了基于硬件的安全实施方面存在的更广泛问题。由于固件限制和对制造商更新的依赖，在所有设备上更新安全启动证书是一个缓慢的过程。

微软计划在 2026 年之前推出新的安全启动证书，但这留下了很大的漏洞窗口。

来源：https://cybersecuritynews.com/windows-11-bitlocker-encrypted-files-accessed/

***END***

阅读推荐

[【安全圈】可能对企业产生严重影响：字节跳动飞书海外版Lark也将在美国市场停止运营](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=1&sn=c2d0bb267baf11570d6e3253fa3ff4fe&scene=21#wechat_redirect)

[【安全圈】微软已经修复Microsoft 365在Windows Server 2016/2019上崩溃的问题](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=2&sn=e94b5cb3a624cdca3e6452bf7c79d7a8&scene=21#wechat_redirect)

[【安全圈】FTC 要求通用汽车停止收集和销售驾驶员数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=3&sn=220a3c1eb7166bba53400942dfa9cab1&scene=21#wechat_redirect)

[【安全圈】CL-UNK-0979 利用 Ivanti Connect Secure 中的零日漏洞获取网络访问权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=4&sn=8dc7094933166fceeb2e467f38e23545&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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