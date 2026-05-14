---
title: 【安全圈】Windows 11遭新型BitUnlocker降级攻击：5分钟内可解密加密磁盘
url: https://mp.weixin.qq.com/s/jLv7O743kX1FCGw0QgK77w
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:44:28.824700
---

# 【安全圈】Windows 11遭新型BitUnlocker降级攻击：5分钟内可解密加密磁盘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyF6Eda7AXnA3tvhYgicfEY9PPiciawFajicA5zCpI0wabWc8vZTpOP42evHnWKB1GUwoC6s9ZZhz4pFm1WWC9VFYNiberFkBI4liaA7A/0?wx_fmt=jpeg)

# 【安全圈】Windows 11遭新型BitUnlocker降级攻击：5分钟内可解密加密磁盘

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

一款名为BitUnlocker的新工具曝光了针对微软BitLocker加密的降级攻击手法。攻击者通过利用补丁更新与证书吊销之间的关键时间差，可在5分钟内物理破解已打补丁的Windows 11设备上的加密卷。该攻击源于微软安全测试与攻防研究团队（STORM）发现的四个关键0Day漏洞之一（CVE-2025-48804），已于2025年7月补丁星期二修复。

## 漏洞原理分析

根据Intrinsec研究，该漏洞存在于Windows恢复环境（WinRE）中，涉及系统部署映像（SDI）文件机制。当启动管理器加载SDI引用的合法WIM（Windows映像格式）文件进行完整性验证时，会同时允许将攻击者控制的第二个WIM文件附加到SDI的blob表中。启动管理器虽验证第一个（合法）WIM文件，实际却从包含修改版WinRE镜像的第二个WIM启动，该镜像会在BitLocker卷已解密挂载状态下直接启动cmd.exe。

微软虽在2025年7月通过Windows Update为所有受支持系统提供了修补后的bootmgfw.efi文件，但仅靠补丁无法彻底消除攻击面。

## 攻击技术细节

BitUnlocker攻击得以实现的关键弱点并非补丁缺失，而是未吊销的签名证书。安全启动（Secure Boot）验证的是二进制文件的签名证书而非版本号。在2025年7月修复前用于签署所有启动管理器的旧版Microsoft Windows PCA 2011证书，仍被当前绝大多数设备的Secure Boot数据库信任（除非设备在2026年初之后执行过全新Windows安装）。

这意味着采用PCA 2011签名的补丁前版本bootmgfw.efi，即使存在漏洞仍会被Secure Boot视为完全有效。微软大规模吊销PCA 2011证书将面临重大运营挑战，因其会影响生态系统中大量合法签名的二进制文件。

研究人员基于STORM原始研究和早期"bitpixie"降级漏洞利用成果，开发出可实际运行的PoC，将这些弱点串联成5分钟内完成的攻击链。攻击者仅需物理接触目标工作站、配备U盘或PXE启动服务器，无需专用硬件即可实施攻击。

## 攻击流程与影响范围

攻击步骤如下：

1. 攻击者准备指向篡改SDI的修改版BCD（启动配置数据）文件
2. 通过USB或PXE启动提供旧版存在漏洞的PCA 2011签名启动管理器
3. 目标设备加载补丁前版本的启动管理器（可通过Secure Boot验证）
4. TPM在PCR测量值7和11仍通过PCA 2011证书验证的情况下，静默释放BitLocker卷主密钥（VMK）
5. 最终获得已完全解密挂载OS卷的命令提示符

受影响系统包括：

* 仅配置TPM（无PIN）且Secure Boot仍信任PCA 2011证书的BitLocker设备
* 未完成KB5025885更新迁移（未采用新版Windows UEFI CA 2023证书签名）的系统

具备以下配置的设备可防御此攻击：

* 启用TPM+PIN预启动认证（需用户交互才能解封VMK）
* 已完成KB5025885更新（启动管理器签名迁移至CA 2023证书）

## 缓解措施

安全团队应立即采取以下措施：

* **启用TPM+PIN预启动认证**

  ：最有效的防护措施，可阻止TPM在任何被操控的启动序列中释放VMK
* **部署KB5025885更新**

  ：将启动管理器签名迁移至CA 2023证书并引入吊销控制机制
* **验证启动管理器证书**

  ：挂载EFI分区并使用sigcheck工具确认当前bootmgfw.efi由CA 2023而非PCA 2011签署
* **移除WinRE恢复分区**

  ：对于无法强制执行预启动认证的高安全负载，可最小化此类漏洞的攻击面

目前该PoC已在GitHub公开，企业需尽快审计BitLocker配置并加速CA 2023迁移，以防攻击者将此技术用于针对性入侵。

***END***

阅读推荐

[【安全圈】警惕！你的蓝牙可能正被监听 改一个设置就能有效防护](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=1&sn=80e79d8ca786f2b8a4f2a23fe7d5bad4&scene=21#wechat_redirect)

[【安全圈】谷歌确认黑客利用 AI 生成零日漏洞攻击 可提升攻击速度](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=2&sn=6ddc9b61db17560810d8e2ede885638d&scene=21#wechat_redirect)

[【安全圈】“Crimenetwork” 平台关停后死灰复燃，再遭德国当局捣毁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=3&sn=cde7250ec4d43b997cf6a5e4993a5c93&scene=21#wechat_redirect)

[【安全圈】cPanel新漏洞可能导致文件泄露与远程代码执行](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076342&idx=1&sn=30dee5e2a1337bda6b57e2ae8e2f3e7b&scene=21#wechat_redirect)

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