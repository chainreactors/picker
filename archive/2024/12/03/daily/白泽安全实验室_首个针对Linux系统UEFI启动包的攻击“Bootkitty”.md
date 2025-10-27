---
title: 首个针对Linux系统UEFI启动包的攻击“Bootkitty”
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492447&idx=1&sn=7ad7e9784b90e878e1eaea54e8808d58&chksm=e90dc975de7a4063c3c5669473d59be264150198926429a2bbf98182d73a6aef53f20e720bc4&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-12-03
fetch_date: 2025-10-06T19:42:57.958574
---

# 首个针对Linux系统UEFI启动包的攻击“Bootkitty”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 首个针对Linux系统UEFI启动包的攻击“Bootkitty”

BaizeSec

白泽安全实验室

**一、事件概述**

随着UEFI威胁领域的不断演变，ESET研究人员最近披露了一个重大发现——首个针对Linux系统UEFI启动包的攻击Bootkitty。这一发现打破了现代UEFI启动包仅针对Windows系统的固有观念，为Linux系统安全敲响了警钟。Bootkitty是一个UEFI启动包，其主要目标是禁用内核的签名验证功能，并通过Linux初始化进程预加载两个未知的ELF二进制文件。ESET研究人员在事件分析中发现了一个可能相关的未签名内核模块，该模块被命名为“BCDropper”，它会部署了一个ELF程序，负责加载另一个在事件分析期间未知的内核模块。Bootkitty于2024年11月被上传至VirusTotal，初步分析确认这是由其创建者命名的Bootkitty UEFI启动包，并且是首个针对Linux的UEFI启动包，特别是针对几个Ubuntu版本。Bootkitty通过自签名证书签名，因此无法在启用了UEFI Secure Boot的系统上运行，除非攻击者的证书已被安装。Bootkitty旨在无论是否启用UEFI Secure Boot，都能无缝启动Linux内核，因为它在内存中修补了负责完整性验证的必要功能，这是在执行GRUB之前进行的。bootkit.efi包含的许多特征迹象表明，这更像是一个概念验证，而不是活跃攻击者的具体攻击实施工作。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPvfd9ZWvnxOnKkHpyv3lCEQlvqFvO9xtoYMVpNVvgeuOsHw1QN9hGyr4rxpUic8FfbibqsrfsIl0eA/640?wx_fmt=png&from=appmsg)

图 1 Bootkitty执行流程图

**二、技术分析过程细节描述：**

**（1）Bootkitty的执行与GRUB引导程序的篡改：**

Bootkitty首先检查UEFI Secure Boot的状态，如果启用，则挂钩UEFI认证协议中的两个函数，修改它们的输出以绕过安全检查。Bootkitty加载合法的GRUB引导程序，并在GRUB的内存中挂钩和篡改代码，包括修改启动PE图像的start\_image函数，以及禁用GRUB的签名验证机制。

**（2）Linux内核图像解压挂钩：**

Bootkitty挂钩了GRUB模块中的zstd\_decompress\_dctx函数，该函数负责解压Linux内核图像。挂钩函数在执行原始解压功能之前，恢复原始解压函数的字节。

**（3）对解压后的Linux内核图像的修补：**

Bootkitty在内核解压并位于内存中未执行时，对其进行硬编码偏移的修补。这包括重写内核版本和Linux横幅字符串，挂钩module\_sig\_check函数，并修补指向init进程的第一个环境变量的指针/地址。

**（4）BCDropper和BCObserver的发现：**

研究人员还发现了一个可能相关的未签名内核模块BCDropper，它部署了一个名为BCObserver的ELF程序，负责加载另一个未知的内核模块。

**三、事件影响与改善措施**

Bootkitty在系统中留下了痕迹，包括修改内核版本和Linux横幅字符串。为了清除Bootkitty，一个简单的补救措施是将合法的/EFI/ubuntu/grubx64-real.efi文件移回其原始位置，即/EFI/ubuntu/grubx64.efi。尽管Bootkitty目前并不代表对大多数Linux系统构成实际威胁，但它强调了为潜在的未来威胁做好准备的必要性。研究人员建议用户确保启用UEFI Secure Boot，保持系统固件和操作系统的最新状态，并更新UEFI撤销列表。

参考链接：

https://www.welivesecurity.com/en/eset-research/bootkitty-analyzing-first-uefi-bootkit-linux/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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