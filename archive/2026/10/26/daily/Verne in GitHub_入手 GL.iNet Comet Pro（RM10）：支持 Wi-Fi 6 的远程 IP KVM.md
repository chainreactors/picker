---
title: 入手 GL.iNet Comet Pro（RM10）：支持 Wi-Fi 6 的远程 IP KVM
url: https://blog.einverne.info/post/2026/10/gl-inet-comet-pro-rm10-ip-kvm.html
source: Verne in GitHub
date: 2026-10-26
fetch_date: 2026-10-27T07:04:22.110101
---

# 入手 GL.iNet Comet Pro（RM10）：支持 Wi-Fi 6 的远程 IP KVM

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# 入手 GL.iNet Comet Pro（RM10）：支持 Wi-Fi 6 的远程 IP KVM 给 Homelab 补上 BIOS 级别的远程控制

Posted on 10/26/2026
, Last modified on 10/26/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-10-26-gl-inet-comet-pro-rm10-ip-kvm.md)

家里的 [[Homelab]] 一直是一台 4 盘位的小主机跑 [[Proxmox VE]]，上面跑着 Ubuntu 虚拟机、一堆 Docker 服务和下载机。平时远程管理全靠 SSH 加 [[Tailscale]]，只要系统还活着基本没什么问题。真正让我不放心的是系统起不来的时候：升级内核后卡在启动界面、改网卡配置时手滑导致网络没起来、BIOS 被重置后不再从正确的硬盘启动，这时候 SSH 连不上，Tailscale 也不会在线，人不在家就只能干等。最近正好赶上一波促销，我入手了 [[GL.iNet]] 的 Comet Pro（型号 GL-RM10）远程 [[IP KVM]]，叠加各种限时优惠之后实际支付 590.76 元，算是把 Homelab 远程管理的最后一块短板补上了。

![GL.iNet Comet Pro 远程 IP KVM](https://pic.einverne.info/images/2026-10-26-09-38-40-glinet-comet-pro-ip-kvm.png)

## 远程桌面解决不了的问题

我们平时用的 [[AnyDesk]]、[[TeamViewer]]、[[RDP]]、VNC 这类远程桌面工具，本质上都是跑在操作系统里的一个程序，系统没启动、卡死或者网络配置坏了，它们也就跟着失效。服务器厂商的解决办法是在主板上放一颗独立的 BMC 芯片，也就是常说的 [[IPMI]]、iDRAC、iLO，不管操作系统是什么状态都能远程看到画面、按电源键。但我们在家里用的迷你主机、NAS 小主机、旧台式机几乎都没有这个东西。

IP KVM 就是把 BMC 做成了一个外挂的小盒子。它通过 HDMI 采集目标电脑的画面，通过 USB 模拟键盘鼠标，再把这些信号经网络传到浏览器里，于是开机自检、BIOS/UEFI 设置、系统安装界面都能远程看到并操作，和坐在机器前面没什么区别。对 Homelab 来说，这意味着即使宿主机彻底起不来，也能在外面进 BIOS 改启动顺序，或者挂一个 ISO 重装系统。

几年前想要这个能力，基本只有 [[PiKVM]] 一个选择，要么买树莓派加采集模块自己 DIY，要么买 V4 Mini 这样的成品，价格在 275 美元左右。2024 年之后情况变了，[[JetKVM]] 在 Kickstarter 上众筹爆火，Sipeed 推出了 [[NanoKVM]]，GL.iNet 也做了 Comet 系列，消费级 IP KVM 的价格被拉到了 100 美元上下，这也是我开始认真考虑买一台的原因。

## 为什么选了 Comet Pro

GL.iNet 的 Comet 系列目前有好几款：入门的 Comet（GL-RM1）、带 PoE 的 Comet PoE（GL-RM1PE）、本文的主角 Comet Pro（GL-RM10），以及走 5G 网络的 Comet 5G（GL-RM10RC）。Comet Pro 是其中配置最完整的一款，相比入门款多了双频 Wi-Fi 6、2.22 英寸触摸屏和 HDMI 直通输出，存储从 8GB 提升到 32GB eMMC，处理器也从 Cortex-A7 换成了四核 Cortex-A53 加 1GB 内存。它在 2025 年 8 月上 Kickstarter 众筹，同年 12 月开始发货。

让我下决心的其实是价格。Comet Pro 官方定价 179.99 美元，亚马逊上平时的折扣价也在 145～160 美元，而我这次 590.76 元到手，按现在的汇率折合 80 多美元，不到官方定价的一半，基本和 JetKVM、Comet 入门款是一个价位。同样的钱能拿到 Wi-Fi 6、32GB 存储和 HDMI 直通，就没有太多犹豫的理由了。下面是我购买前整理的几款主流方案对比：

| 产品 | 参考价（美元） | 采集规格 | 网络 | 特点 |
| --- | --- | --- | --- | --- |
| GL.iNet Comet Pro（GL-RM10） | 179.99（我实付 590.76 元） | 4K@30，带 HDMI 直通 | 千兆有线 + 双频 Wi-Fi 6 | 触摸屏，32GB eMMC，A53 + 1GB 内存 |
| GL.iNet Comet（GL-RM1） | 约 80～90 | 最高 2K | 千兆有线 | 小巧便宜，8GB 存储 |
| [[JetKVM]] | 约 69～100 | 1080p@60 | 百兆有线 | 完全开源，单核 A7 + 256MB 内存 |
| [[NanoKVM]] Pro | 约 155 | 4K@45 | 有线 / Wi-Fi | 采集规格最高，安全口碑有争议 |
| [[PiKVM]] V4 Mini | 约 275 | 1920x1200@60 | 千兆有线 | 生态最成熟，功能最全 |

如果按原价买，我大概率会选 JetKVM，毕竟便宜一半而且完全开源。但在价格拉平之后，Comet Pro 的硬件余量明显更大，A53 加 1GB 内存跑 Web 界面和视频编码都更从容，再加上 GL.iNet 做路由器多年，固件更新和售后相对靠谱，所以选它是比较自然的结果。

## 无线连接到底解决了什么

Comet Pro 最大的卖点是双频 Wi-Fi 6，官方称它是第一款同时支持 2.4GHz 和 5GHz 的桌面 KVM。不过这里要先说清楚它的边界：Wi-Fi 只是替代了 KVM 到路由器的那根网线，KVM 到被控电脑的 HDMI 线和 USB 线还是少不了，所以它不是「无线控制电脑」，而是「KVM 本身可以无线联网」。理解了这一点再看它的价值，主要体现在机器所在的位置没有网口，或者交换机口已经插满的场景，Comet Pro 可以直接放在机器旁边，不用为它再拉一根线。

配置过程也因此简单了不少。设备通电后在触摸屏上直接选择 Wi-Fi、输入密码，屏幕上就会显示分配到的 IP，用浏览器打开这个地址就能开始初始化，全程不需要先插网线或者去路由器后台找设备。远程画面用的是 H.264 硬件编码，局域网内官方标称延迟 30～60ms，网络一般的时候也可以从 4K@30 切到 1080p@60，这点码率对 Wi-Fi 6 来说绰绰有余。

不过有一个容易被忽略的坑：KVM 自己也要依赖网络才能被访问到。如果你的软路由（比如 OpenWrt、iKuai）是跑在 PVE 的虚拟机里，那么 PVE 宿主机挂掉的同时家里的网络也一起断了，KVM 不管是有线还是无线都连不上，形成一个循环依赖。这种情况下要么让 KVM 连到一台独立的主路由上，要么接受「宿主机挂了只能等回家」的现实。

## 板载存储与虚拟媒体

32GB eMMC 是我比较看重的另一点。IP KVM 的虚拟媒体功能可以把上传的 ISO 挂载成一个 U 盘给被控电脑，远程重装系统就靠它。Proxmox VE 的安装镜像只有一两 GB，Windows 11 镜像也就 5～7GB，32GB 的空间足够同时放好几个常用镜像，需要的时候直接挂载，不用每次重新上传。入门款 Comet 只有 8GB，放一个 Windows 镜像就去掉了一大半。

除了装系统，这块存储也可以当成一个临时的文件中转站。比如被控机器网络坏了，需要把一个修好的网卡驱动或者配置文件送进去，就可以先传到 KVM 上，再以 U 盘的形式挂给目标机器，绕过它自己已经瘫痪的网络。

## 触摸屏、直通与软件生态

HDMI 直通（Loop Out）是我之前没太在意、但仔细想想很实用的功能。被控电脑的画面同时输出给 KVM 和本地显示器，机器旁边有人用的时候完全不受影响，不需要被控电脑额外拿出一个视频输出口。机身上的 2.22 英寸触摸屏不显示被控电脑的画面，主要用来查看 IP、连接 Wi-Fi、开关云服务，还可以设置一个 4 位 PIN 锁住屏幕，防止别人随手改设置。

软件方面，Comet Pro 的固件叫 GLKVM，核心守护进程 KVMD 是 PiKVM 的衍生项目，以 GPL-3.0 协议开源在 GitHub 的 gl-inet/glkvm 仓库里。GL.iNet 在上面套了一层 Vue 写的新界面，原版 PiKVM 的 Web UI 其实也打包在固件里，只是在 nginx 配置中被注释掉了，习惯 PiKVM 界面的话可以手动切回去。远程访问有几种方式可以选：官方的 GLKVM Cloud、开源可自托管的 glkvm-cloud、Apps Center 里内置的 [[Tailscale]]，以及 [[ZeroTier]] 和 [[NetBird]]。我自己一直在用 Tailscale 组网（之前写过一篇 [Tailscale 简单使用](https://blog.einverne.info/post/2022/04/tailscale-usage.html)），所以会直接用内置的 Tailscale，不打算依赖官方云。

## 部署计划与需要注意的地方

我的计划是把它接到跑 PVE 的宿主机上，作为整台 Homelab 的兜底方案。连接方式本身很简单，包装里电源适配器、两根 HDMI 线、USB-C 线和网线都有，基本不需要额外买线：

1. 用 USB-C 线连接 Comet Pro 和宿主机，负责键鼠模拟和虚拟媒体
2. HDMI 线从宿主机接到 Comet Pro 的 HDMI IN，本地如果还要用显示器就接到 HDMI OUT
3. 在触摸屏上连接 Wi-Fi，浏览器打开显示的 IP，设置管理员密码并开启两步验证
4. 在 Apps Center 里启用 Tailscale，加入自己的 tailnet

购买前翻文档和评测时，整理了几个比较容易踩的坑。第一是供电，Comet Pro 可以从被控电脑的 USB 口取电，但电脑关机或进入睡眠（S3/S4）时 USB 可能断电，KVM 也会跟着掉线，所以最好用单独的电源适配器供电，或者在 BIOS 里打开 USB 待机供电。第二是显示输出，不少电脑只在主显示输出上显示 BIOS 画面，多显示器的机器要把 KVM 接在主输出上；如果被控电脑只有 USB-C 视频输出，还要确认这个口支持 DP Alt Mode。

第三是远程开机。Comet Pro 内置了 [[Wake on LAN]]，但前提是宿主机的 BIOS 和网卡都开启了 WOL，PVE 里也要确认网卡配置没有把它关掉。对完全断电关机的机器，官方提供了 ATX 控制板（接主板的电源和复位针脚）和 Fingerbot（一个物理按开机键的小机械臂），都通过 Comet Pro 的 USB-A 口连接。很多迷你主机主板上根本没有 ATX 针脚可接，这时候 Fingerbot 反而更通用。还有一个更便宜的思路是在 BIOS 里打开「来电自动开机」（Restore on AC Power Loss），再配合一个智能插座断电再上电，也能实现远程开机。

第四也是最重要的一点是安全。IP KVM 等于拿到了这台机器的物理控制权，能进 BIOS、能挂载 ISO、能输入任意按键，一旦被别人登录进来，后果比 SSH 密码泄露严重得多。NanoKVM 之前就因为默认密码、硬编码密钥、未说明的麦克风等问题被反复报道过，虽然后来大部分都修了，但足以说明这类设备出问题的代价。我的原则是绝不把 KVM 的 Web 界面直接暴露到公网，只通过 Tailscale 访问，同时开启两步验证、改掉默认密码，并保持固件更新。

## 需要接受的妥协

Comet Pro 也不是没有短板。名字叫 Pro 却不支持 PoE，想要一根网线供电只能退回 Comet PoE；4K 只有 30FPS，日常操作没问题，但别指望用它看流畅的 4K 画面；存储也没有 microSD 或 USB 3 扩展，32GB 就是全部。另外它只能控制一台电脑，如果要管理多台机器，要么每台配一个，要么再加一个 KVM 切换器，到这个规模可能就该考虑带 BMC 的服务器主板了。

还有就是 ATX 控制板和 Fingerbot 都要另外购买，如果宿主机完全不支持 WOL，又没有 ATX 针脚，那远程开机这件事还得再多花一点钱。早期评测里也有提到音频和麦克风偶尔需要重启才能恢复，好在 GL.iNet 的固件更新还算频繁，这类问题基本随着版本迭代慢慢被修复了。

## 最后

像 [Proxmox VE 8 升级到 9](https://blog.einverne.info/post/2026/08/upgrade-proxmox-ve-8-to-9.html) 这种需要重启宿主机的操作，最怕的就是重启之后机器没回来，而人又不在旁边。有了 Comet Pro 之后，最坏的情况也只是远程进 BIOS 或者挂 ISO 重装，心理负担会小很多，这才是 IP KVM 真正的价值：它平时几乎用不上，但关键时刻能让你不用跑回家。

对我来说，590.76 元的价格让 Comet Pro 从一个「有点贵的高端款」变成了「同价位里配置最完整的选择」，Wi-Fi 6、32GB 存储和 HDMI 直通都是实打实的加分项。如果你的 Homelab 也是没有 IPMI 的迷你主机或者自组装机器，又正好遇到不错的折扣，很值得考虑。等实际用一段时间后，我再写一篇聊聊日常使用的体验，包括 Tailscale 远程访问的延迟、虚拟媒体重装系统的流程，以及原版 PiKVM 界面怎么切回去。

## Related Posts

* [Proxmox VE 8 升级到 9 的完整流程与避坑清单](/post/2026/08/upgrade-proxmox-ve-8-to-9.html) - 08/21/2026
* [把 Android 手机当成 USB 无线网卡：以及那些被低估的安卓妙用](/post/2026/08/android-phone-as-usb-network-adapter-and-more.html) - 08/21/2026

---

* [← Previous（前一篇）](/post/2026/10/daidai-panel-mcp.html "呆呆面板 MCP 配置教程：让 Claude、Cursor 用自然语言管理定时任务")
* [Archive（目录）](/archive.html)
* Next（后一篇） →

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/10/gl-inet-comet-pro-rm10-ip-kvm.html)评论。

* [产品体验 249](/categories.html#产品体验)

* [gl-inet 1](/tags.html#gl-inet)
* [comet-pro 1](/tags.html#comet-pro)
* [gl-rm10 1](/tags.html#gl-rm10)
* [ip-kvm 1](/tags.html#ip-kvm)
* [kvm-over-ip 1](/tags.html#kvm-over-ip)
* [homelab 8](/tags.html#homelab)
* [remote-management 1](/tags.html#remote-management)
* [out-of-band 1](/tags.html#out-of-band)
* [wifi-6 1](/tags.html#wifi-6)
* [tailscale 8](/tags.html#tailscale)
* [proxmox-ve 12](/tags.html#proxmox-ve)
* [pikvm 1](/tags.html#pikvm)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").