---
title: 一夜之间TB数据归零，群晖NAS勒索潮爆发，这3件事情今晚就要做
url: https://mp.weixin.qq.com/s/dppPDEVSX_UHde1baF6Llw
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:45:12.009462
---

# 一夜之间TB数据归零，群晖NAS勒索潮爆发，这3件事情今晚就要做

# 一夜之间TB数据归零，群晖NAS勒索潮爆发，这3件事情今晚就要做

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

热点事件预计阅读 4 分钟 · 共 1254 字

一夜之间TB数据归零，群晖NAS勒索潮爆发，这3件事情今晚就要做

10月28日多平台爆发 · 持续追踪

#群晖NAS#勒索病毒#数据安全

READING PATH

阅读路线

6 个章节

01

一夜之间，文件全变

-

02

是0day还是1day？

-

03

三个用数据换来的教训

-

04

现在就可以做三件事

-

05

黄金一小时这样处置

-

06

写在最后

01

一夜之间，文件全变

文件全变了.L0CK3D

凌晨5点多，有群友在技术群里只留下三个字：中毒了。

打开他的共享文件夹，几十年的照片、文档、`Datasheet`，文件名还在，后面全多了一串后缀——.L0CK3D。每个目录下还躺着一封勒索信，开头一行写着：`C3RB3R INSTRUCTIONS`。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzOiaNVCwOoBoYMOfhaBQMM2OkSJ75PAl5JiaDKwTicvbbrKBIeSK8QwOvGDiay71lsiafUFeL2aIzeVcZyWs27uX0U3lNeq0YPvwvA/640?wx_fmt=png&from=appmsg)

这不是个案。**10月28日早上开始，B站、小红书、Linux.do、什么值得买，四个社区同时冒出同一批求助帖**；海外的Reddit和BleepingComputer上也是哀嚎一片。有人一夜痛失9TB收藏，有人配齐了RAID 6加每日自动备份的六年老机器，照样被一锅端。

据360反勒索团队分析，动手的是老牌勒索家族Cerber的Linux变种，安全圈暂称其为**C3RB3R**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxAET4W0pDnkI3npdRaiahquM8KNWEibwNcYp9SMmJRNWnkDB6kgKnK5rkoJthxVetEBiaiavUa15aYEGnVCaSYRUXHRC6TdYfYdIQ/640?wx_fmt=png&from=appmsg)

赎金明码标价：**0.085个比特币，五天不付翻倍**。更瘆人的是，对方的暗网站点已经做成了全自动流水线——上传一个1MB以内的加密文件免费试解密，证明"我真能解"，付款6次确认后自动放行解密器，全程不靠人工。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxrTPLsNM2Mc4GvFhDqJTV02Vu4mbNH9P3x1wCtTgYME56CL3YuE16aRgqVU0ewHicDx7bhv8EZkIr9IfKiaOmd87hWxSfOicic2fQ/640?wx_fmt=png&from=appmsg)

消息传开后，群里第一句话都是：**群晖爆0day了？**

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfx9rGV1K9YjhCErRH1KfOHUb5zoPfgrG02hFDfJHXhjrcWKXZR9ZqAjDB8l1iavBcaa90oFoyZhgNTic22h7BeuDbmNytTQ7ozNI/640?wx_fmt=png&from=appmsg)

02

是0day还是1day？

先别急着下结论

确实有跑着最新版DSM 7.4.1的设备中招，但**"最新版被攻击"不等于"最新版有0day"**。

360团队的报告认为，这次攻击利用的是9月就已经披露、评分高达CVSS 9.8的两个高危漏洞，属于典型的1day攻击——补丁早就出了，只是大量设备一直没更新。Solar应急响应团队的说法更谨慎：入侵入口仍在溯源，不排除DSM本体、套件、Docker容器或凭据泄露等多种可能。

官方公告

群晖 SA-26:14 已更新

10月29日推送安全更新

#PHP2Shell#10个套件受影响

"PHP2Shell"漏洞（CVE-2026-109618、CVE-2026-109619）会影响 **Web Station、WordPress、phpMyAdmin、Calendar、Mail Station** 等10个常用套件。  换句话说，不管入口是哪一个，官方的修复动作已经跟上，**现在最不该做的事就是干等**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfwkBH6FBdHKIEYxl3vvmathSt7salsiaCVcDCgDOeLfkypia9TxYEgAMG3yGHDzAqsPac4ZPzgN4KTM3on7A7HHVkD7VGLqibqzO0/640?wx_fmt=png&from=appmsg)

03

三个用数据换来的教训

01

RAID 不是备份

`RAID 1`、`RAID 6`防的是"硬盘坏了"，防不了"文件被加密"。加密发生在文件系统层面，两块盘只是完美同步了一份密文。拔下盘插到电脑上，读出来照样是加密文件。

02

改密码、开2FA、禁SSH：防的是大门，不是小路

如果局域网里一台电脑中了钓鱼邮件，病毒读出本机保存的NAS账号密码，直接走正常共享协议加密文件——你大门修得再牢也没用。

03

暴露公网 = 赌运气

这次受害用户的唯一共同点，就是设备都能从外网直接访问。

NAS暴露在公网上，本质上是在赌运气

04

现在就可以做三件事

还没中招

SELF-CHECK

立即自查清单

1

关公网

关掉所有不必要的公网暴露，远程访问改走VPN或Tailscale这类组网工具

2

打补丁

把DSM和所有套件更新到最新版，尤其检查有没有装着受影响的PHP依赖套件

3

离线备份

给最重要的数据留一份离线备份——放在一块不通电、不联网的硬盘上，勒索软件够不着的那种

05

黄金一小时这样处置

已经中招

EMERGENCY

发现 .L0CK3D 后的第一小时

1

拔网线

立刻物理断网，停掉一切备份和同步服务，防止密文覆盖干净备份

2

别乱动

千万不要重启、不要恢复出厂、不要格式化——有受害者靠保留内存现场，成功抢回了三分之一的数据

3

翻快照

去快照中心找加密发生前的快照，这是成批救回数据最现实的希望

💡 部分加密密钥可能仍驻留在内存中，重启即永久丢失——那是数据恢复最后的窗口。

06

写在最后

把这篇文章转给你身边还在用NAS的朋友吧。你多转一次，可能就少一台`NAS`归零。

SHARE

你的NAS是怎么连外网的？

评论区聊聊，给其他人提个醒

感谢你的阅读

转发给还在用NAS的朋友，可能就救回一台

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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