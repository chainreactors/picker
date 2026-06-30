---
title: DirtyClone: Linux 内核新漏洞，通过克隆的数据包获得根权限
url: https://mp.weixin.qq.com/s/voZerzkRD8Kp8JZQJKWR1g
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:08:20.894201
---

# DirtyClone: Linux 内核新漏洞，通过克隆的数据包获得根权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfXd5XGicBIDuKWHqjUeY8V0YH5W59AKY3DicCRInDgIOvCsAJh1flKw7pjyKY76HAFaM75HZAuM2wrVUiaRia9RyTIIiaCPHfRc7rRY/0?wx_fmt=jpeg)

# DirtyClone: Linux 内核新漏洞，通过克隆的数据包获得根权限

Swati Khandelwal
Swati Khandelwal

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**DirtyClone****（CVE-2026-43503，CVSS评分8.8）是 DirtyFrag 家族中一个新的 Linux 内核权限提升漏洞。JFrog 安全研究团队于 6 月 25 日发布了一份针对该漏洞的可用利用指南，是该变种首次公开演示。**

该漏洞可导致本地用户通过克隆的网络数据包破坏文件支持的内存，获取 root 权限。该漏洞的补丁于 5 月 21 日合入主线；如果用户的内核尚未包含该补丁，应立即更新。

当内核在内部复制网络数据包时，两个辅助函数会丢弃一个用于标记与磁盘上某个文件共享的数据包内存的安全标记，而缺失的标志就是该漏洞的根源。攻击者将诸如 /usr/bin/su 等特权二进制文件加载到内存中，将这些内存页挂载到一个网络数据包中，并强制内核对其进行克隆。克隆后的数据包会经过攻击者控制的 IPsec 隧道，在解密步骤中，攻击者选定的字节会覆写该二进制文件中用于登录验证的检查代码。之后任何人再运行 su 命令时，它就会直接交出 root 权限。

磁盘上的文件从未改变。修改仅存在于内核的内存副本中，因此文件完整性检查工具无法发现，攻击不会留下审计痕迹，重启系统才能恢复原始二进制文件。而等有人想到要去检查时，攻击者早已拿到了 root 权限。利用该漏洞需要 CAP\_NET\_ADMIN 权限来配置回环 IPsec 隧道。非特权用户命名空间在 Debian 和 Fedora 尚默认启用，因此本地用户可以在新的命名空间内部获取该能力。

Ubuntu 24.04 及更高版本通过 AppArmor 限制了命名空间的创建，从而阻止了默认的利用路径。页缓存在主机级别是共享的，因此在命名空间内部所做的修改会影响机器上的所有进程。

受影响系统包括多租户服务器、CI 运行环境、容器主机，以及允许不可信用户创建命名空间的 Kubernetes 集群。JFrog 已在采用默认命名空间配置的 Debian、Ubuntu 和 Fedora 系统上确认了该利用的有效性。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVoXAibXH4RcY35aauVGz071ict2kw4fyo4nUOrS70N7vC1YNhRtT32QD1eYS9iaCSXbtfsaicibYqB4eDoLAaxqqxLsQhYNjVZtshY/640?wx_fmt=gif&from=appmsg)

**共享片段标志位丢失的问题仍未根除**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfV3Y4Dpn5qbiaJ18IyerHC8kaH9JibqcSWcjDUarpWWibiaZA9P7o5ku3wibPd450ibVdUGdCBR3CfslPqMuibe1Kc6TxZRnwfKPxCaFg/640?wx_fmt=gif&from=appmsg)

这是近期第四个具有相同失败模式的权限提升漏洞：文件支持的内存被当作数据包数据处理，然后一个原地网络操作直接写入本该执行复制操作的位置。其它三个如下：

* Copy Fail（CVE-2026-31431）于四月下旬最先出现，利用 algif\_aead 模块实现四字节的页缓存写入。
* DirtyFrag（CVE-2026-43284 和 CVE-2026-43500）于 5 月 7 日紧随其后，串联 IPsec ESP 和 RxRPC 路径实现完整的写入原语。
* Fragnesia（CVE-2026-46300）于 5 月 13 日出现，通过 skb\_try\_coalesce() 中一个丢弃标志的漏洞绕过了 DirtyFrag 的补丁。

虽然每个修复方案都关闭了一条代码路径，却又留下了其它路径。DirtyClone 已演示的利用核心围绕 \_\_pskb\_copy\_fclone()，而 skb\_shift() 同样受影响；更广泛的 CVE 修复覆盖了其他可能丢失相同标志的片段传输辅助函数。根本问题不在于某个坏的辅助函数。而是一个契约问题：每一条移动 skb 片段的代码路径，都必须不折不扣地每次都保留共享片段标志位。内核的零拷贝网络允许文件支持的内存作为数据包数据使用，而链中任何位置只要有一个标志被丢弃，就会将性能优化变成写入原语。每个变种都找到了一条未遵守该契约的路径。

原始 DirtyFrag 的研究者 Hyunwoo Kim 已于 5 月 16 日提交了一个更广泛的多站点补丁，覆盖了其余几个片段传输辅助函数。综合修复方案于 5 月 21 日合入（提交 48f6a5356a33），5 月 23 日分配了 CVE-2026-43503，并于 5 月 24 日在 Linux v7.1-rc5 中发布。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVrEKmbBnp4gX96lxdibiafIz8fJwlhDNUoJgjOaQzQUQS3FxRHl9eRmalp2T16BWVRU1pMUmG2MFxhwia8a8SUvzCNAOyppOrs0c/640?wx_fmt=gif&from=appmsg)

**应对措施**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfW6l3J9BpBLHbW5Ko4hOBUCIia00GNIdGIlyVG7e0DiabgRIG6zQr0XiatibgsYPO2xaia7B1IPeuP90z6rb90OLCCvo6w60iaqFX2aQ/640?wx_fmt=gif&from=appmsg)

安装所用发行版提供的内核更新。该修复方案已在上游 v7.1-rc5 中落地，并已向后移植到稳定版和 LTS 分支。Ubuntu、Debian 和 SUSE 已发布安全公告；Red Hat 在 Bugzilla 中有对应的跟踪条目。

如果无法立即修复，可采取两种临时措施可以减少攻击面。限制非特权用户命名空间：在 Debian 和 Ubuntu 上，设置 kernel.unprivileged\_userns\_clone=0（其它发行版使用不同的机制）。或者，将 esp4、esp6 和 rxrpc 内核模块加入黑名单，但这会破坏 IPsec 和 AFS 功能，且仅在这些功能是可加载模块而非编译进内核时才有效。这两种都只是临时控制措施，而非修复方案。

DirtyFrag 这一类漏洞很可能还会继续出现。任何在移动片段描述符时未能传递共享片段标志位的函数，都可能成为一个新的 CVE 漏洞，因此审计工作应覆盖在片段传输过程中触及 skb\_shinfo()->flags 的每一条路径。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Dirty Frag 可被用于获得Linux所有主流发行版本的 root 权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525959&idx=2&sn=da57a54e174c45c1b0df30db368b79b8&scene=21#wechat_redirect)

[脏凭据 (DirtyCred)：已存在8年的Linux内核提权漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513659&idx=1&sn=f519e177177bc04c8fe5154fbd6457fd&scene=21#wechat_redirect)

[Snapd 被曝 Dirty\_Sock 漏洞，可用于获取Linux 系统 root 权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489215&idx=1&sn=ac16399c9556fac6cb81a887482b46d7&scene=21#wechat_redirect)

[漏洞Dirty COW：影响Linux系统以及安卓设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485656&idx=2&sn=7f74dd9aba0b235b8d3b3d2330a6b413&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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