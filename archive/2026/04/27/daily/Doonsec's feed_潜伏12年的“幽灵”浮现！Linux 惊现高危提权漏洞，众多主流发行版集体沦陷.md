---
title: 潜伏12年的“幽灵”浮现！Linux 惊现高危提权漏洞，众多主流发行版集体沦陷
url: https://mp.weixin.qq.com/s/rISt6k5t53l3ksz4wV_f4g
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:24:33.157622
---

# 潜伏12年的“幽灵”浮现！Linux 惊现高危提权漏洞，众多主流发行版集体沦陷

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquPAiaQjkJEc5Jd4f2dJO1KZxm1HdyDQcLM0Oeglhkl8YYMbZJXUIaSxmPXPHTE8PHqCzUIQ8WDGpbEicib1EqvnaKaCweicpFa73K0/0?wx_fmt=jpeg)

# 潜伏12年的“幽灵”浮现！Linux 惊现高危提权漏洞，众多主流发行版集体沦陷

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

对于全球无数 Linux 服务器和桌面用户来说，这几天可能要捏把汗了。德国电信（Telekom Security）红队最近扔下了一颗重磅炸弹——一个被称为 **Pack2TheRoot** 的 Linux 高危权限提升漏洞（CVE-2026-41651，CVSS 评分高达 8.8）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquOmCGG7djIbEYVSvwlQDuuZghvGn7n7MJzLSx1via6dJ1MxfLt3UPJSIbia8CwUYkSicFm2pGRqicGibu5Xls5FgjfJTV4sXYdsBwAQ/640?wx_fmt=png&from=appmsg)

这个漏洞有多猛？简单来说：**只要你有任何本地非特权用户的访问权限，就能在几秒钟内静默拿下系统的至高 Root 权限**。

今天，我们就来扒一扒这个让无数运维彻夜难眠的底层缺陷。

### 💣 一、 何方神圣？直击漏洞核心

这次出事的不是别人，正是 Linux 世界里那个无处不在的“大管家”——**PackageKit**。

它是一个跨发行版的软件包管理抽象层，不管是 Debian、Ubuntu、Fedora 还是 Red Hat，绝大多数主流发行版都默认装着它。可以说，它是 Linux 生态的基石之一。

**漏洞的本质，就是一道形同虚设的“门禁”。**

德国电信的安全研究员发现，在特定条件下，本地非特权用户可以直接欺骗 PackageKit 守护进程，无需任何密码验证，就能随意安装或删除系统级软件包。这相当于你把钥匙插在门上，还贴了张纸条写着“随便进”。

更可怕的是，这个缺陷跨越了 **PackageKit 1.0.2 到 1.3.4 的几乎所有版本**，也就是说，这道敞开的“大门”已经默默敞开了整整 **12 年**！

### 🎯 二、 伤敌一千？不，是直接“蓝军屠榜”

如果一个漏洞能被红队（攻击方）视为珍宝，那它对防守方来说绝对是个噩梦。Pack2TheRoot 的实战价值极高：

1. **默认即中招，覆盖面极广**

   研究员在 Ubuntu (18.04 ~ 26.04)、Debian、Rocky Linux、Fedora 等众多默认安装环境中均成功复现。只要你的系统跑着 PackageKit，基本就是“躺枪”状态。
2. **企业服务器的“阿喀琉斯之踵”**

   PackageKit 同时也是著名服务器管理面板 **Cockpit** 的可选依赖。这意味着，那些运行着 Red Hat Enterprise Linux (RHEL) 等企业级系统的核心服务器，只要开启了相关功能，同样暴露在危险之中。
3. **稳定、快速、无情**

   据披露，目前已有成熟的概念验证（PoC）代码，利用过程只需几秒且极度稳定。虽然 PoC 暂未公开，但在黑产手里，这绝对是把趁手的“提权利刃”。

### 🛡️ 三、 亡羊补牢：自查与防御指南

看到这里，你是不是想赶紧看看自己的服务器有没有中招？由于 PackageKit 往往是按需激活（D-Bus activation）的，光看进程列表可能不准。你可以通过以下命令快速自查：

* **Debian/Ubuntu 系：**`dpkg -l | grep -i packagekit`
* **RedHat/CentOS 系：**`rpm -qa | grep -i packagekit`
* **检查运行状态：**`systemctl status packagekit`或 `pkmon`

**好消息是，补丁已经火速安排上了！**

PackageKit 官方已于 2026年4月22日发布了修复版本 **1.3.5**。各大主流发行版的软件源也正在陆续推送更新。

**💡 强烈建议：**

如果你是系统管理员，**请立刻、马上**着手更新你们的补丁策略。特别是那些暴露在公网、且运行着 Cockpit 的服务器，这是黑客眼中的“超级肥羊”，优先级必须拉满！

此外，防守方还可以通过监控日志中的特定断言失败特征（`pk-transaction.c:514`）来捕捉潜在的攻击试探行为。

### ✍️ 结语

Pack2TheRoot 再次给我们敲响了警钟：即便是最基础、最底层的系统组件，也可能隐藏着足以颠覆整个防御体系的巨洞。安全是一场永无止境的猫鼠游戏。

别等服务器被挂马、数据被清空才追悔莫及。今晚就检查一下你们的 Linux 集群吧！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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