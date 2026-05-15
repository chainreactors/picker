---
title: Windows 11遭新型BitUnlocker降级攻击，5分钟内可解密加密磁盘
url: https://mp.weixin.qq.com/s/IdPUuR5PyeqluHd0EfaOAw
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:50:25.891106
---

# Windows 11遭新型BitUnlocker降级攻击，5分钟内可解密加密磁盘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1gygY6AUabW1wF6ibMtxWzicMjYpqjSK5nh9w9kh8fCZz2uK9eJ6ZuWJ7wq5s5rD1m8V3A1zqGsMIHibw3927W0VztE0dUZUyOJ8/0?wx_fmt=jpeg)

# Windows 11遭新型BitUnlocker降级攻击，5分钟内可解密加密磁盘

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0E4FicvvJ7FCOGQyJrWtXzp4hHM6iaKypn478phWe9ZnNRRT4YibbrD8mHYv55cwfZq1spRy65Ho9ic1gvPxCZC8Jht6BRnpLgphQ/640?wx_fmt=png&from=appmsg)

一款名为BitUnlocker的新工具曝光了针对微软BitLocker加密的降级攻击手法。攻击者利用补丁更新与证书吊销之间的关键时间差，可在5分钟内物理破解已打补丁的Windows 11设备上的加密卷。该攻击源于微软安全测试与攻防研究团队（STORM）发现的四个关键0Day漏洞之一（CVE-2025-48804），该漏洞已于2025年7月补丁星期二修复。

**Part01**

## ****漏洞原理分析****

根据Intrinsec的研究，该漏洞存在于Windows恢复环境（WinRE）中，涉及系统部署映像（SDI）文件机制。当启动管理器加载SDI引用的合法WIM（Windows映像格式）文件进行完整性验证时，会同时允许将攻击者控制的第二个WIM文件附加到SDI的blob表中。启动管理器虽然验证了第一个（合法）WIM文件，但实际却从包含修改版WinRE镜像的第二个WIM启动，该镜像会在BitLocker卷已解密挂载的状态下直接启动cmd.exe。

微软虽在2025年7月通过Windows Update为所有受支持系统提供了修补后的bootmgfw.efi文件，但仅靠补丁无法彻底消除攻击面。

**Part02**

## ****攻击技术细节****

BitUnlocker攻击得以实现的关键弱点并非补丁缺失，而是未吊销的签名证书。安全启动（Secure Boot）验证的是二进制文件的签名证书，而非版本号。在2025年7月修复前用于签署所有启动管理器的旧版Microsoft Windows PCA 2011证书，至今仍被绝大多数设备的Secure Boot数据库信任（除非设备在2026年初之后执行过全新Windows安装）。

这意味着采用PCA 2011签名的补丁前版本bootmgfw.efi，即使存在漏洞，仍会被Secure Boot视为完全有效。微软若大规模吊销PCA 2011证书，将面临重大运营挑战，因为该证书还签发了生态系统中大量其他合法二进制文件。

研究人员基于STORM的原始研究和早期的“bitpixie”降级漏洞利用成果，开发出可实际运行的PoC，将这些弱点串联成一条5分钟内即可完成的攻击链。攻击者仅需物理接触目标工作站，配备U盘或PXE启动服务器，无需专用硬件即可实施攻击。

**Part03**

## ****攻击流程与影响范围****

攻击步骤如下：

1. 攻击者准备指向篡改SDI的修改版BCD（启动配置数据）文件。
2. 通过USB或PXE启动，提供旧版存在漏洞的PCA 2011签名启动管理器。
3. 目标设备加载补丁前版本的启动管理器（可通过Secure Boot验证）。
4. TPM在PCR测量值7和11仍通过PCA 2011证书验证的情况下，静默释放BitLocker卷主密钥（VMK）。
5. 最终获得一个已完全解密挂载的OS卷的命令提示符。

受影响系统包括：

* 仅配置TPM（无PIN）且Secure Boot仍信任PCA 2011证书的BitLocker设备。
* 未完成KB5025885更新迁移（未采用新版Windows UEFI CA 2023证书签名）的系统。

具备以下配置的设备可防御此攻击：

* 启用TPM+PIN预启动认证（需要用户交互才能解封VMK）。
* 已完成KB5025885更新（启动管理器签名已迁移至CA 2023证书）。

**Part04**

## ****缓解措施****

安全团队应立即采取以下措施：

* 启用TPM+PIN预启动认证：最有效的防护措施，可阻止TPM在任何被操控的启动序列中释放VMK。
* 部署KB5025885更新：将启动管理器签名迁移至CA 2023证书并引入吊销控制机制。
* 验证启动管理器证书：挂载EFI分区，使用sigcheck工具确认当前bootmgfw.efi由CA 2023而非PCA 2011签署。
* 移除WinRE恢复分区：对于无法强制执行预启动认证的高安全负载，可最小化此类漏洞的攻击面。

目前该PoC已在GitHub公开，企业需尽快审计BitLocker配置并加速CA 2023迁移，以防攻击者将此技术用于针对性入侵。

**参考来源：**

New BitUnlocker Downgrade Attack on Windows 11 Allows Access to Encrypted Disks in 5 Minutes

https://www.freebuf.com/articles/system/480862.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2WOichlYJst28QicxZVpXP1ibeVdB4iawibWIFgqV6Ry4LzdhyQbspxEr3NAqQviatF6AoAYMl0qboYWSzKwjM7zPSKtD3ncv5joxpM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337950&idx=1&sn=12d64571335d50c1b93389447dfb8ef1&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ibzbO8hNu1jchaRibLfz5ZHmRibzmT7nmjUqZSAswml2TEozpdNFMZw8N1ShpFef0a2bibN2crXGM5BZhMQjgAbAOY0DN1yjl1Cc/640?wx_fmt=png&from=appmsg)

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