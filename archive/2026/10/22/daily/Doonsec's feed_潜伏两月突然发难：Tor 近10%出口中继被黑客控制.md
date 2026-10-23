---
title: 潜伏两月突然发难：Tor 近10%出口中继被黑客控制
url: https://mp.weixin.qq.com/s/KH5vXxyOZ6N6-ZYhoxNpLA
source: Doonsec's feed
date: 2026-10-22
fetch_date: 2026-10-23T06:44:23.354647
---

# 潜伏两月突然发难：Tor 近10%出口中继被黑客控制

# 潜伏两月突然发难：Tor 近10%出口中继被黑客控制

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

十月二日周五早上九点三十五分，Tor网络里突然多出了三百多台“听话”的出口节点。

这些节点不是新上线的志愿者服务器，而是早在两个月前就被攻击者悄悄拿下的中继节点。

此刻它们被统一改写了配置，开始执行一项精心设计的拦截任务：

收割所有通过Tor网络进行的SSH登录密码，同时批量收集未加密的邮件流量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqjDCXuDJTWnyldQtPX5xXBofp2lYRdQTD9icIpDjD8ySF322OrVtuAQmoLGaaZlmHPZA9xkVxmRaaDlLhDaJgo3CqWlAaXricD8/640?wx_fmt=png&from=appmsg)

三天后，当瑞士研究员Kaba的SSH连接撞上host key警告时，这场Tor网络历史上规模最大的节点劫持事件才浮出水面。

# 10%的出口在谁手里

先给不熟悉Tor的读者补个背景。Tor网络由成千上万台志愿者运行的中继组成，用户流量经过三跳加密节点才到达目的地，最后一跳叫做Exit Relay（出口中继）。出口节点是流量离开Tor网络进入公网的最后一站，也是唯一能看到明文内容的节点。

正因为如此，运行出口节点的志愿者一直是被信任的角色，这次攻击者赌的就是这份信任。

Tor网络目前大约有三千台出口中继。被劫持的三百三十三台占到了11%左右，按共识权重计算峰值时占了整个Tor出口容量的7.46%，换句话说，那几天里每十个用Tor的人，就有一个人的流量在经过攻击者控制的服务器。

# 攻击者到底干了什么

整个攻击分两条线并行。

第一条线是SSH中间人攻击。攻击者改写了被劫持节点的torrc配置，打开了22端口也就是SSH默认端口。当用户通过这些节点建立SSH连接时，流量不会到达真正的目标服务器，而是被悄悄重定向到攻击者控制的十二台拦截服务器上。

如果用户是第一次连接，一切看起来都很正常，输入密码就登录了，但密码直接进了攻击者的口袋。

如果用户之前连过这台服务器，OpenSSH会弹出那个著名的警告框：REMOTE HOST IDENTIFICATION HAS CHANGED。这个警告是SSH安全模型的核心防线，它告诉用户对面那个人换了。大多数人看到警告会停下来，但也有人直接忽略，敲下yes继续登录。

一旦用户接受了拦截服务器的host key，攻击者同时做三件事：偷走输入的密码、打开一条到真实服务器的中转连接让会话看起来一切正常、再开第二条连接把Ebury木马安装到登录的服务器上。

注意最后一步，这不是被动嗅探而是主动扩散。每一个粗心的SSH登录，都会让攻击者的僵尸网络多一台服务器。

第二条线是邮件流量收割。攻击者把出口策略改成了一个很巧妙的组合：关闭加密邮件端口也就是993 IMAPS和995 POP3S，保留明文邮件端口也就是110 POP3和143 IMAP。这样一来这些节点上只会走明文邮件流量，加密邮件用户自然会被路由到其他节点。至于为什么要关闭加密邮件端口，公开数据里找不到答案。

# Ebury：潜伏了十七年的OpenSSH后门

这次攻击的核心武器是Ebury。

Ebury是一个针对OpenSSH的Linux后门，最早可以追溯到2009年。ESET在2024年的报告中估计，全球有超过四十万台服务器被Ebury感染，其中至少十万台到2023年底仍然在线。

这次攻击者部署的是Ebury 1.8.3版本，比ESET公开的检测规则还新，连官方检测脚本都认不出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoibvTaNgXmoo6nmhiaIGiaVAugYOG6FVqp1cGYIhlGxyOibhG05MZLdUnFmAJ7QkkicbKUcxqvp9Pj1X6VH8eaF4iaiaXBVGS7y9IrI4/640?wx_fmt=png&from=appmsg)

Ebury的伪装方式非常精妙。它不是一个独立的恶意进程，而是伪装成一个系统库文件：/usr/lib/x86\_64-linux-gnu/libkeyutils.so.1.10.2。系统自带的libkeyutils库原封不动，只是软链接被指向了这个恶意文件。包管理工具验证库文件时看到的是原始文件的校验和，完全查不出问题。

更隐蔽的是Ebury注入到sshd进程内部运行。SSH传输过程是加密的，但sshd必须解密密码才能验证登录，而Ebury就运行在sshd里面，所以每个登录密码都被原封不动地记录下来，连失败尝试都不放过。

后门登录完全绕过日志，没有PAM记录，没有shell history，连sshd的日志级别都被改成了ERROR，只保留最关键的错误信息。

# 两个月前就埋下的钉子

被劫持的节点不是十月二日才被攻破的。Quetzalcoatl中继家族运营者Zimmer的事后复盘显示，攻击者在八月二十八日就已经入侵了他们的管理服务器。

时间线是这样的：八月二十八日凌晨三点十九分，攻击者从185.225.226[.]62这个IP登录了Zimmer的Contabo VPS管理服务器，用的是管理员密码，第一次就成功了，没有任何失败尝试记录。五分钟后拿到root权限，装上Ebury。一个多小时后通过管理服务器作为跳板，又入侵了运行出口节点的Switzerland2服务器，同样装上Ebury。

根因说出来很简单：管理员密码在SSH登录、sudo提权、备份解密三个地方复用，而且明文存在服务器的脚本里，管理服务器还开着密码登录。

但更大的问题是其他五十八个运营者的一百台节点是怎么被攻破的。数据分析显示其中71台托管在FranTech Solutions也就是BuyVM的运营方，而其他地方的九千多台节点里只有13台被波及。Kaba在邮件列表里直接发问：会不会是托管商层面被攻破了？

这个问题至今没有定论。

# 三天的战斗

十月二日早上，Kaba自己的SSH连接撞上了host key警告。他没有忽略，而是用exitmap写了个脚本，逐个测试Tor网络里所有约三千台出口节点，检查每台节点是否返回正确的SSH指纹。

结果发现大约十二台节点直接返回了假指纹，另外三百多台虽然不改指纹，但SSH连接都被重定向到了同一组十二台拦截服务器上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrYianZLsQiadhMiaVBME3IaMS6vib4CpkNnULB6Hb7QzMU4vG0xq7Wu3fzojZZL0w9dPpuiaRNbmgS1XhCUxCMJt4KDZHSRJfV2tMg/640?wx_fmt=png&from=appmsg)

当晚Kaba联系了Tor网络健康团队。对方的回复是：

"We've not seen an attack like that before."

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpMY0xVk0jA53owgyic8ialgpym4fEdeqB5YNUAk5N2GoLnoxNOGbnk8yh6e6qicUiaA7onwzG12prspP0YESmIHzYUcpoiceX9Qur4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr8DA4xVSjma3hokicLITwkWdryUpcZy3iacAic2iaBB1Ib75ASibWg7SoavBIH74JSP0YiasriaMUzr8o9erwyEmDTvMwGiaibAeQ6kbTc/640?wx_fmt=png&from=appmsg)

十月四日周日，健康团队开始通知运营者，同时把受影响节点标记为BadExit。BadExit标记意味着Tor客户端不会再把这些节点当作出口使用。

十月五日周一，攻击者试图重启大量被标记的节点想恢复运作，但BadExit标记生效了，这些节点只能当作中间中继，无法再做拦截。当天所有被感染服务器全部下线，一部分是运营者主动关的，一部分是攻击者自己关的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqIqOUzutPF8dN8LBiaurHxiaLPfOibbRvbQwib7YCDQwrCziceQLfkjFUOFpSVs201F3LXKaMHjib69pBOLU76qJuPBUp5r3aa1RX5w/640?wx_fmt=png&from=appmsg)

从metrics.torproject.org的公开数据可以看到，十月四日出口节点数量出现了一个明显的断崖式下跌，之后一直没有恢复到之前的水平。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpibxvK1Zk4dKJLiav0H3mW67WBvib0hvbDe538nK0UM3nTEWW2coaXBSyrTgBNR66tyxuEeUG1q26W2Jr2ROyvTfGquqia4lse1qM/640?wx_fmt=jpeg)

Tor网络出口节点数量变化，十月四日出现明显断崖

# 普通人需要担心什么

如果在十月一日到十月五日之间通过Tor网络用密码登录过SSH服务器，而且接受了一个陌生的host key警告，那密码很可能已经泄露了。

需要做几件事：立刻改掉那个密码，检查登录过的服务器上有没有Ebury的痕迹。检查方法包括查找可疑的setuid库文件、检查/proc/net/unix里有没有@event-开头的抽象socket、查看ssh.service cgroup里有没有不属于sshd的进程。

如果只是普通Tor用户，不通过SSH登录任何东西，那这次事件对用户没有直接影响。但它暴露了一个问题：Tor网络的安全性依赖于出口节点运营者的自律，而这次攻击证明，即使是有经验的运维人员，也可能在两个月里都没发现自己的服务器已经被植入了后门。

# 留下的问题

这场攻击还有很多未解之谜。攻击者到底是怎么拿到那58个运营者密码的？是FranTech/BuyVM的管理系统被攻破了，还是Ebury之前就已经感染了他们的服务器？

ESET的研究员Marc-Etienne Léveillé提出了一个更令人不安的猜测：全球有四十万台服务器感染过Ebury，Tor中继里很可能还有没被发现的感染者。攻击者可能早就自动化了在Tor中继上部署特殊工具的流程，专门用来抓通过Tor进行SSH登录的用户密码。

Kaba还注意到一个细节：攻击者特意选在周五发动攻击，大概是赌没人愿意为了这事毁掉周末。

Zimmer在复盘的最后写了一句话：

"At the end of the day, relays/bridges need to be treated as highly targeted production machines."

这句话放在这次事件里，分量很重。

Tor网络一直被当作匿名通信的基石，但这次事件暴露了一个底层假设的脆弱性：大家信任出口节点运营者是好人，却没有足够的机制去验证这一点。

Ebury潜伏了十七年，感染了四十万台服务器，而它这次被用在了Tor网络上，一次就拿下了10%的出口节点。如果不是一个研究员碰巧把自己的SSH流量路由到了被劫持的节点上，这场攻击还会持续多久？

教训其实很老套但永远不过时：

禁用SSH密码登录改用密钥认证、管理服务器不要暴露在公网、密码不要到处复用、运行中继的时候把它当作高价值生产机器来对待。

黑鸟打算去买一把硬件密钥。

参考：《How I got over 300 Tor exit nodes removed》

相关阅读：[Tor 匿名网络的“美国印记”：政府招标项目资金占比从53%降到35%](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184312&idx=1&sn=c555fe3244d85515ad22a896402d459b&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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