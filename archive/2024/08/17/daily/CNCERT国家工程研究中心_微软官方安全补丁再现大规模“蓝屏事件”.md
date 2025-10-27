---
title: 微软官方安全补丁再现大规模“蓝屏事件”
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546480&idx=1&sn=9a0bd2c4ba0b2ed09421374a2d344864&chksm=fa9380b1cde409a7d57d280890dd3e626d0619150efab4c57907a70ca1d3d4fafbef166889d2&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-17
fetch_date: 2025-10-06T18:06:25.855048
---

# 微软官方安全补丁再现大规模“蓝屏事件”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mtuibGC6AGcr19Ew2NzEUWBMrLX3jx35Iria8BrGdMvB958m12xjdfU6xAibo0vVwPnrWRicKZdYfIaQ/0?wx_fmt=jpeg)

# 微软官方安全补丁再现大规模“蓝屏事件”

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mtuibGC6AGcr19Ew2NzEUWBwCfbWFmypgQTxOEnjrFOz0mAr14wQhiakiaJO7BT4tU8EYDJRf5tAPYA/640?wx_fmt=png&from=appmsg)

当CrowdStrike正忙于应付“全球最大规模蓝屏事件”的客户集体诉讼时，微软公司本周发布的一个BitLocker安全补丁再次触发“蓝屏”事件。不过这次“蓝屏”不是“蓝屏死机”，而是重启到Bitlocker的蓝色恢复界面。

对于很多刚刚经历CrowdStrike事件惊魂未定的CIO和CISO们来说，微软官方“蓝屏补丁”事件不仅仅是伤口上撒盐，更可能是彻底摧毁对IT服务商信心的“最后一根稻草”。

**“官方蓝屏补丁”**

微软的Windows驱动器加密工具BitLocker在两次“蓝屏事件”中都扮演了重要角色。在CrowdStrike的安全更新导致的全球最大规模IT系统崩溃事件中，使用BitLocker加密驱动器的用户在恢复系统时需要手动输入BitLocker密钥，这大大拖延了系统恢复的时间。

在本周微软的“蓝屏事件”中，BitLocker的角色从“反串”晋升到了主角。事件起因是微软在修复BitLocker安全漏洞的过程中，由于固件兼容性问题导致部分设备进入BitLocker恢复模式（下图），导致大量用户必须输入恢复密钥才能正常启动系统。这迫使微软撤回该补丁并建议用户实施BitLocker安全漏洞的手动缓解措施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvabxpvibsgbD93DmqpibXjkVfSicEZ0micIXmfejkhu8KkIk3F64MniahLga9CKZpkEYevJZDib8HBxsC6Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

微软安全更新导致设备重启到Bitlocker恢复界面

BitLocker是Windows的一个安全功能，通过加密存储驱动器来防止数据泄露或被盗。通常情况下，只有在用户更换硬件或TPM（受信任平台模块）更新等事件后，系统才会进入BitLocker恢复模式。而此次微软补丁导致触发恢复模式，显然属于程序bug而非“功能特色”，并迅速引起了业界广泛关注。

该“蓝屏补丁”影响多个Windows客户端和服务器平台，涵盖Windows 10、Windows 11以及多版本的Windows Server，具体如下：

* 客户端系统：Windows 11 23H2、22H2、21H2；Windows 10 22H2、21H2。
* 服务器系统：Windows Server 2022、2019、2016、2012 R2、2012、2008 R2、2008

**此前已发生多次安全更新事故**

类似的的安全更新问题在2022年8月的KB5012170更新中也曾出现，当时Secure Boot DBX（禁止签名数据库）的更新触发了0x800f0922错误，导致部分设备进入BitLocker恢复模式。而在2023年4月，微软再次修复了另一个导致BitLocker加密错误的问题，该问题在一些管理环境中被标记为报告错误，但并未影响驱动器加密本身。

在本月的补丁星期二，微软还修复了7月Windows安全更新引发的BitLocker恢复问题。然而，微软并未透露导致该问题的根本原因，也未详细说明是如何修复的。

**不可撤销的缓解措施**

由于补丁与设备固件不兼容导致部分设备进入BitLocker恢复模式，微软最终决定撤回该修复补丁（CVE-2024-38058）。

但由于该漏洞极为严重（攻击者可能通过物理访问目标设备绕过BitLocker设备加密功能，从而访问加密数据），微软在8月的安全更新中正式禁用了该补丁，并建议用户通过KB5025885公告中的手动缓解措施保护系统和数据。

微软给出的手动缓解措施包括一个四阶段的操作流程，需要重启设备多次。需要格外留神的是，应用这些缓解措施后，启用了安全启动（Secure Boot）的设备将无法移除该缓解措施，即使重新格式化磁盘也无济于事。

微软提醒用户，在实施这些缓解措施之前，应充分测试并了解所有可能的影响，因为一旦实施，撤销将变得非常困难。

**安全补丁不可随意“敏捷”**

虽然微软总是建议用户安装最新更新，但此次“蓝屏事件”再次提醒我们，安全补丁的兼容性和系统恢复问题仍是未来安全更新中的一大挑战。

对于企业和用户来说，最重要的是及时了解和跟进安全更新，同时在部署补丁和实施缓解措施时，不可盲目置信（即便是主流厂商），必须进行充分的测试和评估，以确保系统稳定性与安全性的平衡。

此外，CrowdStrike和微软相继曝出“蓝屏事件”，表明在网络安全产品的QA和测试环节生搬硬套敏捷方法往往会产生严重的安全隐患。

正如一位安全人士对该事件的点评：

“这就是所谓的敏捷。微软的产品曾经很成功，因为他们有更多的QA而不是开发。然后，他们在开发Bing时改变了QA方法，并认为找到了最佳实践（将Bing看作成功的衡量标准）”

“将开发和测试结合起来的敏捷方法，以“组合工程”的名义（首先在Bing团队中使用）大肆宣传。在Bing，创建程序化测试的任务被甩给开发人员，而不是专门的测试人员。QA仍然存在并且仍然很重要，但（安全产品）需要执行的是最终用户风格的“真实世界”测试，而不仅仅是程序化自动化测试。”

**参考链接：**

https://support.microsoft.com/en-us/topic/kb5025885-how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023-24932-41a975df-beb2-40c1-99a3-b3ff139f832d

https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-bitlocker-security-fix-advises-manual-mitigation/

原文来源：GoUpSec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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