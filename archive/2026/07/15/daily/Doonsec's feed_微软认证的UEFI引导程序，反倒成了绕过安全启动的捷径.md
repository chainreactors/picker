---
title: 微软认证的UEFI引导程序，反倒成了绕过安全启动的捷径
url: https://mp.weixin.qq.com/s/j0E951MGgS3fuTLyVjeb-g
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:56:26.915075
---

# 微软认证的UEFI引导程序，反倒成了绕过安全启动的捷径

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDq8vkicricV3lMpzbHcRSrONdNnfBUJW0vy79IWesXsJ73EgguE4lf5rQRpVdomqCfAqTyblkUaQJ1OIHcXfGflUTSaPeXL3ia8to/0?wx_fmt=jpeg)

# 微软认证的UEFI引导程序，反倒成了绕过安全启动的捷径

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](https://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

最近网络安全厂商 ESET 的研究团队披露了一项潜藏多年的底层安全风险。11 个版本停留在 0.9 及更早的 UEFI shim 引导程序，因为持有微软官方颁发的有效数字签名，至今可以在绝大多数开启 UEFI Secure Boot (安全启动) 的设备上绕过安全校验，在系统启动前执行任意未受信任的代码。本次漏洞整体分配了两个 CVE 编号，分别为 CVE-2026-8863 和 CVE-2026-10797，覆盖所有上报的问题程序。

无论设备安装的是 Windows 还是 Linux 系统，只要固件信任微软的 Microsoft Corporation UEFI CA 2011 第三方证书，就可能受到影响。攻击者利用这些有漏洞的引导程序，可以轻易部署 Bootkitty、HybridPetya 或是 BlackLotus 这类 UEFI 级别的启动恶意程序，哪怕设备完整开启了安全启动也无法阻挡。

好在这一隐患已经通过正规的协调披露流程得到修复。ESET 研究团队在 2026 年 2 月就将完整的漏洞细节和验证样本提交给 CERT/CC 协调中心，原本计划在 5 月补丁日发布修复，最终调整到 2026 年 6 月 9 日的微软月度补丁日同步公开。当天微软将这 11 个存在风险的引导程序哈希加入了 UEFI 禁止启动列表 dbx，从固件层面封堵了这条攻击路径。

要理解这次漏洞的影响，我们得先从 UEFI Secure Boot (安全启动) 的基本逻辑说起。

现在的电脑早已淘汰了传统的 BIOS 固件，改用 UEFI (统一可扩展固件接口) 来完成开机自检和系统引导。安全启动是 UEFI 自带的核心安全机制，它的作用是在电脑开机时，校验每一个要运行的启动程序是否合法，防止恶意程序在系统加载前就悄悄运行。

校验的规则很简单，固件里存着两份名单。一份叫 db，是允许启动的白名单，记录了受信任的证书和程序哈希。另一份叫 dbx，是禁止启动的黑名单，记录了被吊销的证书和有漏洞的程序哈希。一个启动程序要想运行，必须同时满足在白名单里，同时不在黑名单里。

![Figure 1. UEFI Secure Boot simplified scheme](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrXeibq6ibJhYRAqA4QbhcTbqQiaU0QB74LhbyWJnBicLJNjIsSB6W32ibVVljSAtdS9q1IZjnotLmDZu9NpxiaQfoObMh6JRlmjGqQE/640?wx_fmt=png&from=appmsg)

为了让用户买到电脑就能正常用，绝大多数品牌的电脑出厂时，都会在 db 列表里预装微软的两套 UEFI 证书。一套用来给 Windows 自己的启动程序签名，另一套就是 Microsoft Corporation UEFI CA 2011，专门给第三方的 UEFI 程序签名，比如 Linux 引导程序、系统恢复工具、磁盘加密软件等等。只要是拿这个证书签过名的程序，在几乎所有消费级 UEFI 电脑上都会被默认信任。

可以说，微软手握的这张第三方签名证书，是整个 UEFI 生态里最核心的信任锚点。

既然微软可以直接给程序签名，为什么还会出现 shim 这个中间层？这就要说到 Linux 生态的特殊性。

Windows 是单一厂商维护的系统，启动程序版本少更新慢，每次找微软签名都没问题。但 Linux 发行版数量众多，每个发行版都有自己的引导程序和内核，更新也非常频繁。如果每一次版本更新都要提交给微软签名，流程繁琐效率极低，根本不现实。

于是社区就设计出了 shim 这个极简的第一阶段引导程序。微软只需要对 shim 做一次审核和签名，shim 内部会嵌入对应 Linux 发行版自己的厂商证书。开机时固件先验证 shim 的微软签名，验证通过后，再由 shim 用自己带的厂商证书，去验证第二阶段的 GRUB2 引导程序，最后再由 GRUB2 验证 Linux 内核。

![Figure 2. Simplified UEFI boot flow on Linux systems](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqjZUYsj2Vq0ep4UxiaXa6ffnkSt8xxZMyBZVbJvXclXV7sA2bupP532RWz8kbiaGVqQENB5KVwjkshzE6hyRBttPrkaniapzIxicQ/640?wx_fmt=png&from=appmsg)

这样一来，Linux 厂商更新引导程序和内核时，只用自己的厂商密钥签名就行，不用每次都找微软。整条信任链环环相扣，既兼容了安全启动机制，又保留了 Linux 生态的灵活性。

除了厂商证书，shim 还支持用户自己管理的 Machine Owner Key (机器所有者密钥) 简称 MOK。用户可以把自己的密钥加进 MOK 白名单 MokList，用来加载自己编译的内核或者第三方驱动，对应的黑名单则叫 MokListX。修改这两份列表都需要物理接触设备并在启动时操作，普通远程攻击很难篡改。

![Figure 3. Simplified UEFI boot flow on Linux systems (with Machine Owner Key)](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDponOhOHclAxAxhEFuQJVlrvFFyuxqLjdG0ILKYF4kibWxC0vCvYckdueiapuqeDg060xC0w4R12hs1BlyV7NQpW50m7wqVavSbM/640?wx_fmt=png&from=appmsg)

这次被发现的 11 个 shim 都有一个共同点，版本都在 0.9 及以下，发布时间早，后续没人跟进维护和吊销，就这么一直留在微软的信任白名单里。它们能被用来绕过安全启动，不只是因为一两个单独的漏洞，而是整个攻击面层层叠加的结果。

每个 shim 都会信任一批用对应厂商证书签名的第二阶段程序，其中最常见的就是 GRUB2 引导程序。这些老旧 shim 配套的 GRUB2 版本同样古老，积累了大量公开的安全漏洞，其中最典型的就是早年的 BootHole 漏洞。

比如本次报告里提到的 Oracle Linux 旧版 shim，它信任的 GRUB2 存在 CVE-2015-5281 漏洞。攻击者可以直接通过 GRUB2 的 multiboot2 命令，加载一个完全没有签名的自定义程序并执行。整个过程不需要利用内存损坏漏洞，不需要构造 ROP 链，也不需要复杂的逆向分析，只需要写一个符合格式的程序就能完成攻击。

更关键的是，这种攻击不需要目标设备原本就安装了对应的 Linux 发行版。攻击者只要能访问到电脑的 EFI 系统分区 ESP，把有漏洞的 shim 和 GRUB2 文件复制进去，下次开机就能触发。只要设备信任微软的第三方证书，不管装的是什么系统，这条攻击路径都成立。

随着漏洞越来越多，社区给 shim 加了很多新的安全机制来提升吊销效率，但这些机制在老旧版本的 shim 上统统不生效。

首先是 MOK 黑名单 MokListX 的校验。MOK 白名单从 shim 0.3 版本就有了，但黑名单的强制校验直到 0.9 版本才正式加入。也就是说 0.9 之前的 shim，只会读取 MOK 白名单，完全无视黑名单的存在。

举个实际场景，企业给内网所有设备都加了自定义 MOK 密钥来签名内部工具，后来发现这批工具存在漏洞，管理员就把旧密钥加进了 MokListX 黑名单，再换上新的密钥和工具。正常来说旧程序已经不能运行了，但如果攻击者把 0.9 版本之前的 shim 放进设备里，旧 shim 根本不会读取黑名单，旧密钥签发的漏洞程序就能照常运行，攻击者可以直接执行任意代码或是植入启动恶意程序。

另一个失效的机制是 Secure Boot Advanced Targeting (安全启动高级靶向机制) 简称 SBAT。这是 shim 从 15.3 版本开始支持的功能，它会在程序里写入组件版本号，固件里存着最低安全版本要求，只要版本低于要求就直接拒绝运行。相比一个个添加程序哈希到 dbx，用版本号批量吊销效率高得多，还能节省固件的存储空间。

![Figure 4. Latest SBAT revocations in the shim repository](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrP3RLGUu6iaRBAIcfmGymxIrdvXDvSIcrlHhyRru1vd9VGnmm71gGYqKdnuZdIldfqLG2y6F856yibmH2g61EoVibWwuic7icGE7zg/640?wx_fmt=png&from=appmsg)

但 15.3 之前的 shim 根本不认识 SBAT 规则，也不会读取对应的版本信息。攻击者只要拿一个旧版 shim，搭配一个已经被 SBAT 吊销的有漏洞 GRUB2，就能绕开所有基于版本的安全限制，正常加载并利用漏洞。

除了配套程序的问题，旧版 shim 自身也存在已经修复了十年却一直没分配 CVE 编号的漏洞。这个漏洞在本次报告中正式被分配为 CVE-2026-10797。

漏洞的原理出在签名长度的校验上。一个带 Authenticode 签名的 PE 文件，会在两个不同的位置记录签名的长度。一个在 PE 头的数据目录里，另一个在封装签名的 WIN\_CERTIFICATE 结构里。在有漏洞的旧版 shim 中，吊销检查和签名校验读取的不是同一个位置的数值。

攻击者可以篡改第二阶段引导程序里 WIN\_CERTIFICATE 结构的长度值，让 shim 的吊销检查功能去比对错误的签名数据，误以为这个程序的证书没有被吊销。简单来说，哪怕对应的签名证书已经被加进了 dbx 或是 MokListX，旧 shim 也检测不出来，依然会正常加载程序。

当然这个漏洞也有局限，它只能绕过基于证书的吊销，无法绕过基于程序哈希的吊销，而且被篡改的程序必须是被 shim 内置证书信任的。

有人可能会注意到，这次涉及的 Microsoft Corporation UEFI CA 2011 证书，有效期到 2026 年 6 月 27 日就已经截止了。用过期证书签的程序，难道还能正常运行吗？

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpIEnTHbFSLNLIP1zotiaVVUPVjt5rVGO9wZrTgW24crj2KGVBlHjEEFkl0Y4djKnRlmibXnplBoLWS0J4cvgFIMGOvJiaRt7vnA8/640?wx_fmt=png&from=appmsg)

答案是肯定的。在 UEFI 安全启动的校验逻辑里，证书的过期时间不会影响验证结果。只要证书还在白名单 db 里，同时没有被加入黑名单 dbx，哪怕证书过期很久，用它合法签发的程序依然会被固件信任。这也是为什么微软会一直用这张证书接收签名申请，直到它正式过期的原因。

所以指望证书过期自动解决老旧程序的风险，是完全不现实的。想要彻底禁用有漏洞的程序，只能主动把它的哈希或者对应证书加进 dbx 黑名单。

针对这批有漏洞的 shim，微软已经在 2026 年 6 月 9 日的月度补丁中，将对应 11 个程序的哈希值更新到了 dbx 吊销列表里。正常开启自动更新的 Windows 设备会自动收到这份吊销数据，Linux 设备则可以通过 Linux Vendor Firmware Service 获取更新。

如果你想手动确认自己的 Windows 设备是否已经应用了这批吊销，可以用管理员权限打开 PowerShell，运行下面这段代码。如果输出 “All hashes revoked in dbx!” 就说明所有漏洞程序都已经被禁用。

```
$hashes = 'AE75F0D82BA3DF824FBFC69340CC3B4D66C598373B1AB54CDB6C8BFD83A6B961','7B2A3F5C96F95BD8086CE54B0825E300F9C8F11FE3401BB631B3215C8DE9EB10','EB86FA1386FE6E4533B8B938DCC1250616D2F1C14C15E2FCF80834A161018A0A','FD23D6E57DE6F4E1F9D7118DA1C5F31A8AF6BE5E5D9E8170F9493447268D50C5','A0DE9333442C1BF9349A460141AE5E80F911955C6506040FA3D021BF6C1AE3E4','95B6D71FC0C0F8C5E1533A37AEF92CF6B0C961E2CC612A97117FA6759CE5FC06','236A9CB0D71951C36398A32EB660CE2CD4A52CCFA7CF751CC6A35D9DE549E19B','5E594C448760A3135B1A3A83E07A4F2E6FBE49414EF2C7CAB1CBA77F284FA63B','8A964D5F8373948D20A1D4296FB92E545DAD4617A0C810F3B934B53D98AE8963','410260B1B6F5AF5FBEEB9EA3220658435E876CB3247126EE907A437F312DB373','96275DFD6282A522B011177EE049296952AC794832091F937FBBF92869028629' $dbx = [BitConverter]::ToString((Get-SecureBootUEFI dbx).Bytes) -replace '-'$notRevoked = $hashes | Where-Object { $dbx -notmatch $_ }if ($notRevoked) {    $notRevoked | ForEach-Object { "Hash not revoked: $_" }} else {    "All hashes revoked in dbx!"}
```

Linux 用户可以使用 uefi-dbx-audit 脚本检查当前的吊销状态，及时通过固件更新服务安装最新的 dbx 补丁。

另外需要说明的是，Windows 11 的 Secured-core 安全核心电脑默认禁用了第三方 UEFI 证书信任，受本次漏洞的影响相对更小。

这次发现的 11 个有漏洞的 shim，只是浮出水面的冰山一角。

真正的问题在于，早期的 shim 签名流程没有公开的记录和统一的审核。直到 2017 年社区推出 shim-review 仓库，所有提交给微软签名的 shim 才会经过公开审核并留下记录。在那之前有多少厂商提交过 shim，有多少版本还在信任列表里，没有人能给出准确的数字。

没有完整的清单，就没法系统性地排查和吊销所有存在风险的老旧程序。这些被遗忘在角落里的合法签名程序，就像一把把没有登记在册的钥匙，随时可能被攻击者拿来绕开安全启动的大门。

值得庆幸的是整个生态正在往好的方向发展。SBAT 这类按版本吊销的机制大幅提升了漏洞修复的效率，公开审核流程也让新的 shim 越来越规范。但我们也要看到，除了 shim 之外，还有大量第三方 UEFI 工具和诊断程序也持有微软的签名，它们同样可能存在老旧版本无人维护的问题，过去几年也已经多次曝出类似的安全启动绕过漏洞。

底层安全的防线，从来都不是靠某一次补丁就能一劳永逸的。整个第三方 UEFI 签名生态的透明度，还有很长的路要走。

参考链接：

https://www.welivesecurity.com/en/eset-research/forgotten-uefi-shims-undermining-secure-boot/

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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