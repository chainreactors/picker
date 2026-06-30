---
title: Pedit COW：通过投毒缓存二进制，获得根权限
url: https://mp.weixin.qq.com/s/mkb-yDks0W8U499S791Qlw
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:08:18.539769
---

# Pedit COW：通过投毒缓存二进制，获得根权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfXukoPhAowLQQXbibwKOnnPvBdAEql4YZBnBAIqMC3NFqCWWLmzQN6gaDYRT3ewzB9r71sBysqe0BSel5k2P5iajPia8ibiatCeFwxo/0?wx_fmt=jpeg)

# Pedit COW：通过投毒缓存二进制，获得根权限

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

**Linux****内核流量控制子系统中存在一个被称为 “pedit COW” 的漏洞CVE-2026-46331，可能导致本地非特权用户在受影响系统上获取 root 权限。**

该漏洞是数据包编辑动作 (act\_pedit) 中的一个越界写入漏洞，会破坏共享的页缓存内存。该漏洞在6月16日获得CVE编号后一天内，公开的可利用代码就已出现。Red Hat 将该漏洞评级为“重要”。

该利用代码不触碰磁盘上的文件，而是会在内存中污染 setuid root 二进制文件（/bin/su）的缓存副本，注入一段小载荷，然后以 root 身份运行该被篡改的镜像。当 root shell 已经打开时，文件完整性检查仍然显示一切正常。

利用该漏洞需要两个条件，即act\_pedit 可被加载，且非特权用户命名空间处于开启状态，从而为攻击者提供触发漏洞所需的命名空间本地网络能力（CAP\_NET\_ADMIN）。该漏洞在 RHEL 和 Debian 目标系统上进行了测试，均满足这两个条件。

**漏洞工作原理**

Linux 的流量控制工具可以使用名为 pedit 的动作来改写传输中的数据包头部。负责此功能的内核函数 tcf\_pedit\_act()，本应在编辑数据前制作一份私有副本，即标准的写时复制模式。但该函数只检查了一次可写范围，且是在最终偏移量确定之前检查，部分编辑键只有在运行时才能解析其偏移量。当这种情况发生时，写入操作会落到私有复制区域之外，导致内核修改的是共享的页缓存页面，而非私有副本。如果该页面属于某个已缓存文件，则该文件的内存镜像就会被破坏。

这种模式并不陌生。Dirty Pipe、Copy Fail、DirtyClone 和 Dirty Frag 都有相似的结构：内核快速路径写入了一个它并不独占的页面，而页缓存承担了后果。该漏洞模式的新颖之处在于入口点。非特权用户可以在用户命名空间内部配置 tc 动作，这为他们提供了利用漏洞所需的 CAP\_NET\_ADMIN 能力。

**受影响系统**

披露 PoC 的作者报告称，在 RHEL 10 和 Debian 13（trixie）上可实现从非特权到 root 的利用，这些系统默认开启了非特权用户命名空间。Ubuntu 24.04 需要通过仍允许用户命名空间的 AppArmor 配置文件来路由执行。Ubuntu 26.04 默认阻止了该路径，因为其 AppArmor 配置文件限制了非特权用户命名空间，尽管底层内核仍然存在漏洞。

各厂商的修复方案有所不同：

* Debian 已通过其安全渠道修复了 trixie。Debian 11 和 12 仍被列为易受攻击。
* Ubuntu表示受支持版本18.04 至 26.04 均易受攻击。
* Red Hat 列出 RHEL 8、9 和 10 受影响；RHEL 7 未列入公告。

**应对措施**

安装修复后的内核并重启。优先处理那些“本地用户”并不等同于“可信用户”的系统：多租户主机、CI/CD 运行环境、Kubernetes 节点、构建工作节点，以及共享的研究或实验室机器。

如果暂时无法修复，可采取两种缓解措施阻断利用链。在不需要 tc pedit 规则的系统上，检查该模块是否在使用中（lsmod | grep act\_pedit），然后阻止加载：

echo 'install act\_pedit /bin/true' | sudo tee /etc/modprobe.d/disable-act\_pedit.conf

或者，禁用非特权用户命名空间（RHEL 上设置 user.max\_user\_namespaces=0，Debian/Ubuntu 上设置 kernel.unprivileged\_userns\_clone=0）。这样做虽然能移除利用漏洞所需的命名空间本地能力，但会破坏无根容器、部分 CI 沙箱以及沙箱化浏览器的运行。因此应首先先进行测试。

由于该写入操作的目标是缓存内存，因此文件完整性检查可能无法发现该操作。清理页缓存（echo 3 > /proc/sys/vm/drop\_caches）可以清除被污染的内存镜像，但对攻击者已经打开的 root shell 无能为力。用户应将该主机视为已被攻陷。

该修复方案于五月底就已提交到 netdev 邮件列表，当时被描述为常规的数据损坏补丁。该漏洞可被利用的细节在公开邮件列表中存在了数周，但一直没有 CVE 编号，也没有安全警告。CVE 编号在修复方案于 6 月 16 日合并时分配，而武器化的 PoC 代码在一天之内随之出现。对于内核页缓存损坏类漏洞而言，等待扫描器规则更新实在太慢。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[漏洞Dirty COW：影响Linux系统以及安卓设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485656&idx=2&sn=7f74dd9aba0b235b8d3b3d2330a6b413&scene=21#wechat_redirect)

[Ubunntu 高危漏洞可导致攻击者获得根权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525508&idx=1&sn=2833d5727c1faf94104890b325bb6d75&scene=21#wechat_redirect)

[数百万台Exim 服务器被曝严重缺陷，可导致攻击者以根权限远程执行命令](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247490811&idx=3&sn=4ec2274061c40fd69a4aa5003515ca5d&scene=21#wechat_redirect)

[最新软件供应链事件概览：Red Hat npm 包遭劫持；投毒 Claude Code；OpenAI Codex 认证令牌被盗](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526178&idx=1&sn=17c22b5b9c9011ac7e14bc24b3c1e6ee&scene=21#wechat_redirect)

[Axios npm 包遭投毒，发动供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525629&idx=2&sn=b076315a014fe06f2a8b6eeec62f33c2&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/06/new-linux-pedit-cow-exploit-enables.html

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