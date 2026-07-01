---
title: Kali Linux 2026.2 发布，新增 9 个工具并优化虚拟机启动设置
url: https://mp.weixin.qq.com/s/Gm8RxE-qo3yKOP134Lvcug
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:16.630820
---

# Kali Linux 2026.2 发布，新增 9 个工具并优化虚拟机启动设置

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTFtQFZVI2QmUaz9JmBCVle1F7XOpDxJQ1JgYwzsWgkXxZpKqaXZvlkDCWDQewlYFmGbssA17iaqsOKFDc4LTAibzdAoUFH55p6s/0?wx_fmt=jpeg)

# Kali Linux 2026.2 发布，新增 9 个工具并优化虚拟机启动设置

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Kali Linux 团队于 2026 年第二季度末按计划正式发布了 Kali Linux 2026.2，带来了一系列引人注目的桌面环境升级、基础架构优化、虚拟机性能增强以及九款面向渗透测试人员和安全研究人员的全新工具。

此次更新将两大桌面环境升级至最新版本。GNOME 50 带来了显著的文件管理器优化、缩略图和图标加载速度优化、更低的内存占用、重新设计的辅助功能首选项窗口，以及在文档查看器应用程序中直接添加文档注释的功能。

KDE Plasma 6.6 注重可访问性和易用性，引入了新的屏幕键盘、通过 Spectacle 屏幕截图实用程序实现的 OCR 文本提取、色觉支持选项，并采用了标准化的“减少动态效果”设置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibQt4DuoianC90FZskcd27D0FenMofhnowAjoTkicgjexP7qL3PhlL1EcTibb1d3W1t4uFQvNWRibp7gahog8GGLx58WMHu5Cdnia0Lg/640?wx_fmt=png&from=appmsg)![]()![]()

KDE Plasma 6.6（来源：Kali）

2026.2 版本的核心更新之一，是对虚拟机环境下图形固件的处理机制进行全面重构。此前，Kali 预构建镜像内置了英伟达、AMD、英特尔显卡的图形固件，相关文件占用近 300 兆存储空间，同时将初始化内存盘（initrd）体积膨胀至约 200 兆，这也是系统启动缓慢的直接诱因。

2026.2 版本中，预制虚拟机镜像不再内置显卡固件；安装程序现在可识别虚拟机环境，并据此跳过显卡固件的安装流程。优化后初始化内存盘（initrd）精简至 60 MB，使用 QEMU 虚拟机用户模式的开机速度提升约两倍（耗时缩短至原先三分之一）。物理机裸机用户不受任何影响，系统仍会预装全套显卡固件。

Kali 2026.2 弃用了长期使用的 /etc/apt/sources.list 文件，转而采用新的 deb822 风格格式，位于 /etc/apt/sources.list.d/kali.sources 。

从 2026.2 版本开始，多个软件包已更新为使用统一的辅助脚本，现在可以一致地处理以下所有操作：

管理服务——干净利落地启动和停止它。

检查是否已在运行——防止意外双重启动。

显示服务状态——每次输出都清晰易懂。

显示默认凭据——无需再翻阅文档。

显示访问详情 — 对于基于 Web UI 的工具，将显示 URL 并自动在浏览器中打开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibS7XzK5LQBUmjdpRmOMnTeib4wtnm4QEQ6ggg42hOxRrp4NyrlxclGXbhNWECmTSBM91cZy7lRWEj7zUJ029snJAzuQx22PQuWM/640?wx_fmt=png&from=appmsg)![]()![]()

Helper Scripts (来源: Kali)

新安装的系统将自动使用新格式，而现有安装的系统将继续运行，但 APT 最终会提醒用户进行迁移。这使得 Kali 与 Debian 和 Ubuntu 衍生发行版正在进行的更改保持一致。

Kali 2026.2 搭载 Linux 内核 6.19，这是为了避免与 Debian 系统中 NVIDIA DKMS 驱动程序在内核 7.0 下出现的兼容性问题。想要体验最新版 7.0 内核的用户可以通过 kali-experimental 软件仓库进行选择。

此外，此版本还包含一些破坏性更新，需要重启系统，特别是针对 polkit（以避免以 root 用户身份运行 GUI 应用程序时出现故障）和 xrdp/xorgxrdp v0.10（与 Hyper-V 增强会话模式用户相关）。

Kali 2026.2 扩展了其工具集 ，在网络存储库中新增了九个工具：

* arsenal-ng — 基于 Go 语言的命令库，包含 200 多个网络安全速查表
* hydra-gtk — 为快速网络登录破解程序重新添加了 GTK+ GUI
* legba — 多协议凭证暴力破解器和密码喷洒器
* oletools — 用于分析 MS OLE2 文件和 Office 文档的工具包
* penelope — 功能强大的后渗透 shell 处理程序
* shell-gpt — 基于人工智能的 LLM 命令行生产力工具
* tailscale——安全连接平台
* tookie-osint — 用于社交媒体账户发现的开源情报工具
* uro——用于网络爬虫和渗透测试的 URL 清理工具

移动端方面，NetHunter 应用现已实现秒开，同时修复了自定义命令与容器环境（chroot）管理相关漏洞。本次更新一项标志性成果是适配 Qcacld-3.0 的无线注入补丁，该补丁让一加 7/9、POCO X3 Pro、红米 Note 10、三星 A73、小米 Mi A3 等多款设备均支持 WiFi 数据包注入功能。

NetHunter Pro 的全新裸机支持已扩展到 20 多款其他设备，涵盖 Google Pixel、Sony Xperia、Samsung 和 Xiaomi 系列产品。

用户可以通过 sudo apt update && sudo apt full-upgrade 升级现有的 Kali 安装，或者从 kali.org 下载新的镜像。

END

推荐阅读

[两伙黑客同时潜伏一家企业，用的全是合法工具](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493551&idx=1&sn=76a4fa489992d4c6577981b0dedbad84&scene=21#wechat_redirect)

2026-06-28

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTwtOsdXCavibRiaWuIc6GLpJ6cC8Sxw37GqOSctZpicLWfgQT94f1fVManbic4m22Iw1r53I4HkTIlw4a8ymH1JWrn9RibJQFL4hvM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493551&idx=1&sn=76a4fa489992d4c6577981b0dedbad84&scene=21#wechat_redirect)

[美国水务系统频遭黑客攻击，为何中国很少发生？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493543&idx=1&sn=4a93a012083d5160b92489a71c9428ec&scene=21#wechat_redirect)

2026-06-27

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTkqkPAfxxeiad7rWK5ic4Rq9NkMsfys95JDyCYCu2Wqy6OFgf5JCRL2DZApUTYRJLzB3qdl4E1iaSpJRnbicWAu6IDUpThWzydxLw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493543&idx=1&sn=4a93a012083d5160b92489a71c9428ec&scene=21#wechat_redirect)

[网站自动跳转"小黄网"？鄂尔多斯一煤矿企业栽了，被网信办立案处罚！](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493537&idx=1&sn=58dc126018002f3c8ba2bdb26797c16d&scene=21#wechat_redirect)

2026-06-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibRnRP1e3dAgYPaaicYMPbKaAArbc2Ov1NY0jJ9lu7JPLvVcszEaiaY9EbfByThDBEdODD3nWOE5LdZXls7wZt8lmM6sZAotByDbs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493537&idx=1&sn=58dc126018002f3c8ba2bdb26797c16d&scene=21#wechat_redirect)

[高考填志愿，网安专业还值得报吗？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493531&idx=1&sn=b4d6d1d50b6fbb69539aef8852c1a5af&scene=21#wechat_redirect)

2026-06-19

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibSHBtPknVjZMJibVT3jiaw5Sict2ibLCYqVAxmWEcjI0tdDRfWXmkaMljOV87n957DatC2UtSibjOjbSotbJfKKS3bAcysp15NGl67U/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493531&idx=1&sn=b4d6d1d50b6fbb69539aef8852c1a5af&scene=21#wechat_redirect)

[LockBit勒索病毒的前世今生和应对策略](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493531&idx=2&sn=bdc4d137e79f6199aafc61720ef61ec1&scene=21#wechat_redirect)

2026-06-19

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1aGlsMrkTiaz1icibiahYNheLOLjnicF1n7vIuyyMWZgAnOV0RCXmuLJI8OPGrvZhhIia8N2LibFPqyuiampw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493531&idx=2&sn=bdc4d137e79f6199aafc61720ef61ec1&scene=21#wechat_redirect)

[2026年，网络安全公司该怎么活？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493524&idx=1&sn=c99d8a56e9d2d29232f9ad5b152eed0f&scene=21#wechat_redirect)

2026-06-18

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTrOUOVZZ5qHgXhIxOe4yRmXLfFt80cPEMF9bXk1Hsyziaia16uriaMdzianhGZaVHU4Er6MWcPn7oyr7Ey7W46FX0RJlzicGLahQds/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493524&idx=1&sn=c99d8a56e9d2d29232f9ad5b152eed0f&scene=21#wechat_redirect)

[2026年，传统安全产品创业，还有出路吗？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493519&idx=1&sn=1f564d76914744f830776049ee058413&scene=21#wechat_redirect)

2026-06-17

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibRfIBnHj0qsYcWmfiaOz0QwsUDicGcHkmmLGMmWQOlo4vdJISuRib8u2ciaEnB3sG9C738LBu1GicPUjXeDVJCvCFlWvP7FK1Aq9erg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493519&idx=1&sn=1f564d76914744f830776049ee058413&scene=21#wechat_redirect)

[小白入门 | 渗透测试系统Kali安装全过程](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493514&idx=1&sn=e914183bdcc6d69da342e74bcdf226aa&scene=21#wechat_redirect)

2026-06-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTAaR3nHZuRYiaIMN0aJhicbZM9ic8WH5n88xVUib2m4oTR07pvPNzIHDibAIyibvqZnWvWxM93yKYoqkfKHRiaQnicnw0LZ6w05BeEsibk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493514&idx=1&sn=e914183bdcc6d69da342e74bcdf226aa&scene=21#wechat_redirect)

[小白入门 | 社会工程学模拟工具setoolkit](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493514&idx=2&sn=37331fdc6657fedf80f91283a8a6c952&scene=21#wechat_redirect)

2026-06-16

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibRj8Hiaw5UPCuHnAjqXY8ibHPbdG7ia7OfRXpXcgt7lSZD2oGSCIkSIqk9ee8c3wbLMu8eFicREt6lO3Rcdq9daibcaKTlY19IFqzpg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493514&idx=2&sn=37331fdc6657fedf80f91283a8a6c952&scene=21#wechat_redirect)

[没有安全数据积累，就别谈AI赋能网络安全](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493261&idx=1&sn=2cdc303a546c6b59ce790f346e53d993&scene=21#wechat_redirect)

2026-06-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibSYZ2Q6oYKyVAgvgCPsQLLRjvicmybAjun0NibJVxpJ3oibRewaIPvLEu1DC6EYH7N7Y9Pqg8Xkmuich14BoPLPWx6ia88k5Xk5CdsQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493261&idx=1&sn=2cdc303a546c6b59ce790f346e53d993&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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