---
title: 洞见RSAC 2024｜UEFI Bootkits，当安全启动不再“安全”
url: https://blog.nsfocus.net/rsac-2024uefi-bootkits/
source: 绿盟科技技术博客
date: 2024-05-25
fetch_date: 2025-10-06T17:17:53.969744
---

# 洞见RSAC 2024｜UEFI Bootkits，当安全启动不再“安全”

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 洞见RSAC 2024｜UEFI Bootkits，当安全启动不再“安全”

### 洞见RSAC 2024｜UEFI Bootkits，当安全启动不再“安全”

[2024-05-24](https://blog.nsfocus.net/rsac-2024uefi-bootkits/ "洞见RSAC 2024｜UEFI Bootkits，当安全启动不再“安全”")[绿盟科技](https://blog.nsfocus.net/author/nsfocuser/ "View all posts by 绿盟科技")

阅读： 5,445

2024年RSA大会上，研究员Martin Smolar分享了有关UEFI安全启动和Bootkits的议题。UEFI安全启动（Secure Boot）旨在确保计算机UEFI固件启动的代码可信，从而保护系统，防止恶意代码在操作系统加载前的启动过程中被加载和执行。此前的系列文章已介绍了安全启动的基本知识[1][2]，而本文将着重讨论安全启动涉及的密钥、潜在的安全漏洞以及加固方法。

## 一、什么是UEFI安全启动？

几十年来，个人电脑一直受到病毒、蠕虫和其他恶意软件的困扰。最早的一些个人电脑病毒是以引导扇区病毒的形式传播的：它们以代码形式存在于软盘的引导扇区中，当用户使用受感染的 DOS 软盘启动计算机时，病毒就会从一台计算机传播到另一台计算机。虽然随着软盘重要性的降低和互联网连接的普及，其他病毒传播方式也逐渐显现，但系统启动前阶段（pre-boot）的恶意软件对黑客来说始终具有吸引力。通过在操作系统内核获得计算机控制权之前执行，恶意软件可以 “隐藏”起来，而一旦操作系统获得控制权，恶意软件就无法“隐藏”起来。因此pre-boot阶段的恶意软件很难被检测到（除非重启到未受影响的应急系统里）。

![](https://blog.nsfocus.net/wp-content/uploads/2024/05/WeChatbe6e2eda688c9fc7e6c2fc0418731117-300x169.png)

图1 UEFI固件的位置

BIOS/UEFI 几乎无法防止启动前的恶意软件；在 BIOS/UEFI启动过程中，系统默认信任boot loader执行的任何程序。直到 2012 年底，大多数的 EFI 实现也是如此。传统的系统启动分为以下几个过程：开启电源——UEFI固件——硬盘中的操作系统（boot loader、内核）。

![](https://blog.nsfocus.net/wp-content/uploads/2024/05/WeChatb64bd4fc841a738659c042df1f474287-300x114.png)

图2 UEFI启动过程

在系统启动过程中，UEFI固件会根据Boot variables 去决定启动顺序，并且执行磁盘ESP分区中的UEFI 应用。如下图所示，攻击者可能修改Boot order以及ESP分区中的二进制文件。

![](https://blog.nsfocus.net/wp-content/uploads/2024/05/WeChatabb3048b9360376f12cd76915ba8dd12-300x161.png)

图3 UEFI潜在攻击点

安全启动旨在为pre-boot过程添加一层保护。开启安全启动后，固件会检查执行的任何 EFI 程序是否存在签名。如果签名不存在或与计算机 NVRAM 中的密钥不一致或被列入 NVRAM 的黑名单，固件就会拒绝执行该程序。一个可信的 EFI boot loader必须以安全的方式继续引导，最终实现一个安全的操作系统。

安全启动中的重要概念是允许签名数据库 (db) 和禁止签名数据库 (dbx)。允许签名数据存储机器固件允许加载的受信任boot loader和 EFI 应用程序的哈希值和证书。禁止签名数据库 (dbx)存储已撤销、受损和不可信任的哈希值和证书。任何使用禁止dbx密钥加载签名代码的尝试，或在哈希值与禁止dbx条目匹配的情况下，都会导致启动失败。对db和dbx的签名，需要用到密钥注册密钥数据库 (KEK)和平台密钥数据库 (PK)。

![](https://blog.nsfocus.net/wp-content/uploads/2024/05/WeChat8563aff166350e761ed65e6a9446e424-300x160.png)

图4 db与dbx

这些密钥用于签署启动加载程序、驱动程序固件运行的其他软件。目前销售的大多数商品 PC 都包含由微软控制的密钥。

![](https://blog.nsfocus.net/wp-content/uploads/2024/05/WeChat37bdc383513edee14f1b063a043912e3-1-300x145.png)

图5 安全启动涉及的密钥

## 二、开启了安全启动的系统就绝对安全吗？

只要是开启了安全启动的系统就绝对安全吗？我们总结了几类涉及UEFI安全启动绕过的漏洞。

内存相关漏洞：2022年1月，研究者发现了名为“baton drop”的安全启动漏洞（CVE-2022-21894）[3]。Windows 启动应用程序允许通过设置“truncatememory”移除包含序列化数据相关的内存块，从而绕过安全启动。Truncatememory BCD 元素将从内存映射中删除指定物理地址以上的所有内存内容。在从内存读取序列化的安全启动策略之前，攻击者会在初始化过程中对每个启动应用程序执行此操作。尽管微软很快修复了此漏洞，但由于受影响的UEFI二进制没有被撤销，“baton drop”攻击在很长的一段时间内仍然可被利用，产生了相关联的漏洞[4]。直到2023年5月，微软才给出处理建议[5]。

![](https://blog.nsfocus.net/wp-content/uploads/2024/05/WeChatad08960d7a232901c21f8df8b6b3056e-300x160.png)

图6 微软修复过程

特权命令、撤销列表相关漏洞：在2020年研究者发现，攻击者可以通过insmod加载一个未被签名的grub module来绕过安全启动[6][7]。微软花费数月才彻底地将此漏洞移除。类似地，UEFI shell中也存在大量的敏感命令，在开启安全启动的设备中，这些命令必须被禁止[8][9]。除此之外，一些第三方的PE也被爆出存在安全风险，他们从硬编码的地址，加载运行任意的UEFI二进制[10]。

![](https://blog.nsfocus.net/wp-content/uploads/2024/05/WeChatdd3bc0c1dceae3a223df33300127cf41-300x148.png)

图7 微软修复涉及撤销相关漏洞的过程

Debug相关漏洞：ESET的研究人员发现某些品牌笔记本的UEFI固件存在安全风险，攻击者可以直接从OS中创建NVRAM变量来关闭UEFI安全启动或者恢复出厂设置[11]。

![](https://blog.nsfocus.net/wp-content/uploads/2024/05/WeChat72ef88616b98251769518a74f32ba5d5-300x109.png)

图8 UEFI安全启动漏洞

## 三、如何控制安全启动的密钥来预防Bootkits？

传统的解决方案，例如“最新版本的系统更新、更新固件、开启安全启动、安装安全防护软件等”往往是不够的。这是由于Bootkits往往需要花费数月的时间去彻底移除，移除可能不彻底，签名过程不透明。因此我们需要尽早地介入，例如可以阻断任何试图修改ESP分区文件的行为，可以通过白名单的方式来实现它。除此以外，还可以自定义安全启动：完全定制化和部分定制化。

完全定制化的安全启动将会移除所有安全启动的密钥，并且只使用用户自己的密钥，所有启动的组件都由客户的密钥签名。完全定制化的安全启动对用户而言，往往很难维护。

而部分定制化的安全启动则允许用户将自己的密钥追加进PK、KEK数据库中，当发现安全漏洞时，用户可以提前一步，将恶意程序的hash写入到dbx中，避免了微软/OEM厂商的漫长的响应。而对于只用Linux的用户而言，还可以将windows UEFI CA从db数据库中移除，进而降低攻击面。

从上述的自定义安全启动可以看出，其实质是重新控制安全启动的密钥。笔者总结了如下益处：

**从默认密钥中移除风险**

理论上，安全启动应能阻止恶意软件运行。但另一方面，攻击者总是有可能诱骗微软签署恶意软件；或者签署的软件可能存在漏洞，比如 2020 年发现的 Boot Hole 漏洞。如果使用默认密钥的 Shim，并且dbx没有进行对应的更新，计算机仍会受到这些威胁的攻击。

**从发行版密钥中移除风险**

与前述情况类似，发行版密钥也有可能被泄露，在这种情况下，攻击者可能会分发使用泄露密钥签名的恶意软件。

**消除对 MOK 的需求**

Shim 和 PreLoader 工具都依赖于机器所有者密钥 (MOK)，MOK 与安全启动密钥类似，但更容易安装。由于更容易安装，它们更容易被社会工程或其他手段滥用。尤其是在管理一系列由其他人使用的台式电脑时，取消 MOK 可以增加安全性。

**测试和开发**

如果想开发自己的启动管理器，可能需要在模拟环境中测试软件的签名版本。不过，使用微软安全启动密钥签署二进制文件的过程烦琐而耗时，因此可能需要用自己的密钥以便自己签署二进制文件。当软件按照预期运行时，就可以将它发送给微软进行签名了。

**解决启动问题**

在双系统的场景中，某些电脑默认只能启动 Windows；尽管可以暂时启动到 Linux，使用 efibootmgr 将 Linux 设置为默认启动加载器，但随后发现自己又启动回 Windows，因为固件一直将 Windows 设置为默认设置。如果 Linux 启动项仍然存在但被 “降级”，那么设置自己的启动密钥就可以解决这一问题，具体方法是从常规安全启动列表中删除微软的密钥，然后将其添加到 MOK 列表中。

## 四、总结

前几年对于 Linux 用户来说，安全启动介于 “无所谓”和 “很麻烦”之间。虽然安全启动有可能提高安全性，但相关安全风险没有受到大家重视。因此，虽然安全启动在理论上有好处，但对于只使用 Linux 的计算机来说，安全启动是否有实际好处还不清楚。随着Bootkits的出现，以及人们愈加重视安全启动以及对应的漏洞所造成的安全风险。由于厂商无法及时地将恶意软件加到撤销列表中，就导致了许多在野漏洞的出现。签署你自己的boot loader以使用自己的密钥可以提供最大的安全性和灵活性。绿盟科技会持续关注安全启动的进展，欢迎感兴趣的读者持续关注。

参考文献

[1] https://mp.weixin.qq.com/s/wucSVNYYeg5d5fQ1I1cnAQ

[2] https://mp.weixin.qq.com/s/showAKatT3TsN11aWRD9GQ

[3] https://nvd.nist.gov/vuln/detail/CVE-2022-21894

[4] https://nvd.nist.gov/vuln/detail/CVE-2023-24932

[5] KB5025885: How to manage the Windows Boot Manager revocations for Secure Boot changes associated with CVE-2023-24932 – Microsoft Support

[6] https://nvd.nist.gov/vuln/detail/CVE-2020-7205

[7] https://nvd.nist.gov/vuln/detail/CVE-2020-26200

[8] https://nvd.nist.gov/vuln/detail/CVE-2022-343010

[9] https://nvd.nist.gov/vuln/detail/CVE-2022-34303

[10] https://nvd.nist.gov/vuln/detail/CVE-2022-34302

[11] https://nvd.nist.gov/vuln/detail/CVE-2022-3431

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/rsac-2024/)

[Next](https://blog.nsfocus.net/weeklyreport202421/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)