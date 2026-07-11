---
title: 勒索软件用上了微软签名的恶意驱动：GodDamn把你的EDR变成了瞎子
url: https://mp.weixin.qq.com/s/uy_WuNXvXl2i4RrIa9VjGg
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:58:58.793526
---

# 勒索软件用上了微软签名的恶意驱动：GodDamn把你的EDR变成了瞎子

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/757fvrbk7obPbSxdfbfyFbtYoCA7q4atibndWtyQdHKlnVKL2BdxkaiabRWDCfFlbIqoV9D4X3bI5zCE4uuanvrQcBysrJ6X4rJ9OTTGZ1BYo/0?wx_fmt=jpeg)

# 勒索软件用上了微软签名的恶意驱动：GodDamn把你的EDR变成了瞎子

安世加

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**新闻**

*News Today*

7月9日，Symantec威胁猎手团队发布了一份报告，披露了一个叫GodDamn的勒索软件家族——这个名字听着像是骂人，但对安全团队来说确实值得骂一句。因为这个勒索软件做了一件让很多防守者心里发毛的事：它用了一个携带微软合法签名的恶意内核驱动，在攻击开始之前先把你的EDR和杀毒软件变成"瞎子"。

这不是一个全新冒出来的团伙。Symantec追踪的开发者代号叫Hyadina，这个人在勒索软件圈子里已经干了四年了。2022年3月他推出了Monster，用Delphi写的，只盯32位Windows。2024年6月换了个壳叫Beast，加了Linux和ESXi支持，还多语言包括中文——说明他把目标池子扩大了。到了2026年，再换名GodDamn，这次最大的升级就是PoisonX驱动。

PoisonX不是一个普通的BYOVD攻击。 所谓BYOVD（Bring Your Own Vulnerable Driver），通常是攻击者拿一个已有合法用途但有漏洞的老驱动来利用——比如RTCore64.sys那种被各个勒索团伙反复薅的。PoisonX不一样，它看起来是专门为恶意目的编写的驱动，但它的开发者居然成功拿到了微软的签名。这意味着Windows会自动加载它，不会有任何弹窗或警告。一个内核级驱动拿着微软的签字准入证，然后开始杀安全进程、剥离安全工具的权限、篡改内核事件通知机制——你的EDR进程还在跑，但它已经收不到任何事件了。活着，但什么都看不见。

在Symantec调查的那次实际入侵里，攻击链是这样走的：

5月29日，攻击者在组织内一台机器的Music文件夹里放了一个AnyDesk——这不是正常安装目录，说明攻击者已经通过某种方式拿到了初始访问权限（具体入口不明）。第二天，在另一台主机上部署了防御规避工具：一个伪装成Symantec产品的symantec.exe，它把PoisonX驱动以g11.sys的名字丢进了系统驱动存储区。同一台主机上还出现了一个凭证收割工具包，放在用户目录的子文件夹里，里面有14个工具——Mimikatz加上一整套NirSoft密码恢复工具（WebBrowserPassView、ChromePass、PasswordFox、MailPassView、SniffPass等），覆盖浏览器、Windows凭据管理器、域缓存凭证、VNC会话、邮件客户端、Wi-Fi配置和实时网络流量。还有NetScan用来扫描可达主机。这套组合跟Hyadina四年前Monster时代用的几乎一模一样——工具没换，但规避手法升级了。

然后攻击者停了两天。6月1日开始横向移动，用PsExec推命令到远程主机。命令链都经过psexesvc.exe → services.exe → wininit.exe，典型PsExec痕迹。他们先关掉Windows Defender实时监控，再用窃取的凭证挂载管理共享访问相邻系统。每到一个新主机，就配置AnyDesk无人值守访问：创建专用配置目录、关闭交互确认弹窗、通过管道直接输入远程访问密码，还注册了两个自启动Windows服务确保重启后存活。有些机器上甚至用预部署的PowerShell脚本来批量安装AnyDesk，说明他们有标准化的部署流程。安装完AnyDesk后杀掉进程、短暂等待、重启机器。到6月2日结束时，这套部署流程已经在至少10台主机上重复执行完毕。

6月3日，勒索软件在一个独立网络段上线，二进制文件名叫encrypter-windows-gui-x86.exe，出现在用户Downloads和Music文件夹里。加密后的文件有的用.God8Damn后缀，但这次攻击中用的是受害者组织的名字做扩展名——这种做法比较少见，可能是为了让受害者更容易识别这是针对自己的攻击。勒索信让受害者通过邮件或qTox加密聊天联系。

从5月29日首次活动到6月3日加密，中间有四天空窗期。这段时间大概率在做数据窃取和进一步侦察。

这件事值得关注的不是又一个勒索软件换了名字，而是两个趋势叠加：

第一，恶意驱动拿到了微软签名。PoisonX今年初被发现时就已经被用来杀CrowdStrike Falcon服务了，现在它不只是The Gentlemen勒索团伙的GentleKiller工具里的组件，还被GodDamn直接纳入标准攻击流程。如果一个专门为恶意目的编写的驱动能通过微软的签名审核，那整个BYOVD防御思路——"盯住已知有漏洞的合法驱动列表"——就不够了，因为你还得面对"看起来合法但实际是恶意的"这一类。微软的驱动签名审核机制需要加强，但这不是企业安全团队能控制的，你能控制的是怎么在自己的环境里应对。

第二，勒索团伙的防御规避正在系统化、工业化。Hyadina的套路四年没大变——AnyDesk+NirSoft凭证收割+PsExec横向移动，这套"标准配置"已经熟练到可以批量部署了。但每一次换壳都在升级规避能力：Beast阶段已经加入杀进程和关杀毒的工具，GodDamn则直接上内核驱动致盲EDR。这意味着传统的"发现勒索软件加密行为再响应"越来越来不及，因为你被致盲之后根本看不到加密行为发生。

对防守者来说，有几件事值得马上想想：AnyDesk这类远程访问工具是不是该限制到白名单配置，不允许随便往Music文件夹里丢一个就开始跑？内核驱动的安装行为是不是该纳入重点监控——特别是g11.sys这个名字？PsExec的命令链特征（psexesvc.exe → services.exe → wininit.exe）在你的SIEM里有告警规则吗？14个NirSoft工具同时出现在一台机器上这种"购物清单"式的异常，你的EDR能不能在它们落地的时候就拦住而不是等到加密才发现？

这件事还在发展。PoisonX驱动被多个勒索团伙共用说明它可能是一个正在流通的"EDR杀手"商品化工具，后续可能会有更多团伙接入。对于企业安全团队来说，内核级的防御致盲不再是理论风险，而是已经在实战中出现了——你得确保你的EDR在被致盲之前能看到异常，或者在被致盲之后还有备用检测手段。

来源：Symantec Threat Hunter Team报告

本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！

安世加为出海企业提供SOC 2、ISO 27001、PCI DSS、TrustE认证咨询服务（点击图片可详细查看）

[![](https://mmbiz.qpic.cn/mmbiz_jpg/757fvrbk7oZSh9smTw5WbkMwgALz0Zhibs9CJYo8oLfVJ5Rc3pajxytbl3lpI3HklY8otH7KVUib4Xj0nD6HeeAQDWqcwnPtZSYR8D2vXiaypI/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247540448&idx=1&sn=165f2bc3b3233827b2c601a32073aca8&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

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