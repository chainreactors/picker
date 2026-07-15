---
title: 攻击者利用疑似AI生成的PowerShell脚本映射Active Directory
url: https://mp.weixin.qq.com/s/XZke342ZQEDddGSmhA-ykA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:43:22.704866
---

# 攻击者利用疑似AI生成的PowerShell脚本映射Active Directory

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0KELqq5pMCtPUjDyyu6iaWeMxTiar8mZ103tnxkJrvIBjJ7w9CRFsDMH5BZXrdUStjQUlDF13L0c2xK4iaFXJDmo4JOWA7bTvvSM/0?wx_fmt=jpeg)

# 攻击者利用疑似AI生成的PowerShell脚本映射Active Directory

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1RwDEn6067eGKYmRia8yEcXqpQkf8aZn41yQF3C8UJKV1NKDCDuA8erBpC2l3gEcJKfekjiaWk7yPIpflAwjE4P9QK1D26oWLbE/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX38oKElQt0K84llLUSNl9pDCDLCicKN9Pn5Sx26xZamNxfia86ocY15ibuag6v7pItDs71F6jlzvhybqXWkmIvCh1icyAcuCpoJBRU/640?wx_fmt=jpeg)

Part01

### 从RDP登录到AD数据打包外泄

网络安全研究人员标记了一起入侵事件，其中一名未知威胁行为者利用一个通过AI生成的PowerShell脚本（vibe-coded）对Active Directory（AD）进行枚举。

Huntress研究人员Jevon Ang和Dray Agha表示：“该脚本会寻找域控制器（Domain Controller，DC），映射用户、计算机和域，然后在创建目录并导出多个文件后，最终生成AD\_Report.html来验证枚举尝试的成功程度。”

攻击链涉及威胁行为者使用一组已泄露的凭据，通过远程桌面协议（RDP）访问一台加入域的Windows Server，随后在“C:\ProgramData\”文件夹中部署工具。该事件发生于2026年6月初。

其中包含一个AI生成的payload，用于映射Active Directory环境。这一判断基于多种迹象，例如提示迭代标题、占位符字符串、过度设计的代码（采用了多种方法来寻找域控制器），以及使用青色、绿色、红色和黄色美化控制台输出。

Huntress将该定制PowerShell脚本描述为“高度激进”且“嘈杂”，它采用“五级级联回退机制”来实现侦察与发现。该脚本标题为“100% Working AD Information Gathering Script - FULLY FIXED”，暗示其经过与大型语言模型（LLM）的反复交互。

一旦定位到主域控制器，脚本便会启动数据收集例程，系统性地收集AD用户、计算机、组、组织单位（OU）和信任关系，并将详细信息存储在一个暂存目录中。

约30分钟后，攻击者开始部署s5cmd（一款用于批量文件操作的合法工具）和SharpShares（一款基于C#的网络共享枚举工具），以寻找用户可访问的数据存储库。

在最后阶段，数据被导出为CSV文件、归档并外泄至远程服务器，但在此之前，攻击者还创建了一个HTML文件，以Active Directory资产报告的形式总结了数据窃取情况。

研究人员解释道：“这很可能是LLM‘好心’注入的结果，攻击者只是顺手接受了，而不是有意将其编写到脚本中。”

![文章配图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3GWWT1QiclZZHcWR9rwicGicNcwlESxUtC2ibfibxHSk9OMsI1eCx2zaMOLEAFRFZIXbUDv3zBcG0IibDyhRCOhIoy7nGSQHPJG6vMc/640?wx_fmt=jpeg)

Part02

### AI帮了攻击者什么忙？

这一进展再次表明，威胁行为者正在借助AI模型生成的恶意软件（vibe-coded）来扩充其武器库，即使这种技术的滥用方式并非前所未有。但它的确降低了网络犯罪的门槛，使技术较差的攻击者能够以最少精力开发出功能强大且具备规避能力的工具。

Huntress表示：“底层的攻击链仍然类似于我们多年来见惯的‘打砸抢’战术。这种核心方法一直保持不变，但现在它正被AI有选择地增强。这种混合方法优先考虑攻击性与速度，而非隐蔽性，使威胁行为者能够以前所未有的速度发起极具破坏力的攻击。”

Part03

AI作为战斗力倍增器

Sygnia在上周发布的一份报告中披露，具备AI能力的攻击者并不一定需要新型恶意软件或0Day漏洞，真正的转变在于网络入侵可以比防御方更快、更大规模地协调发动，以至防守方难以遏制。

该事件响应公司表示，他们观察到一次AI辅助的云攻击，在约72小时内从一个大型Amazon Web Services（AWS）环境中的初始访问发展至广泛入侵。评估认为，该活动的最终目标是牟利，攻击者利用对受害者云基础设施的访问权限作为勒索筹码。

Sygnia指出：“威胁行为者反复利用新获取的凭据来重新启动发现、秘密收集、持久化和影响活动。该攻击依赖的是常见的云技术，而非新型恶意软件或0Day漏洞。”

“威胁行为者并未利用单一配置错误；他们串联了应用服务、AWS资源、源代码仓库、CI/CD工作流、运行时组件和数据存储等多个环节的弱点，同时快速执行凭据发现、秘密收集、云枚举、部署管道滥用、运行时修改、数据库访问和运营中断。”

据Sygnia称，攻击者多次尝试在被入侵的主机上建立持久化，通过一个面向互联网的应用的缺陷获取了其中一个AWS账户的访问密钥。每次获得新访问权后，攻击者都会重新进行枚举、收集更多秘密、通过创建访问密钥和IAM用户尝试持久化，并外泄数据。同时，多个攻击者创建的工件被伪装成渗透测试或红队演练。

为进一步向受害者施压，攻击者执行了一系列操作：

* 拒绝访问S3存储桶
* 将ECS服务或容器的最大容量限制为零
* 创建ACL规则以阻止网络访问
* 清空SQS队列

Sygnia指出：“关键在于AI没有引入新的攻击技术——每个被观察到的行为都对应着长期存在的对手行为——而是减少了在复杂环境中实施这些技术所需的时间和精力。”

“威胁行为者反复将新获得的访问权转化为针对性行动。对于每个新访问密钥，攻击者似乎都能迅速判断出关联的权限、可访问的资源以及最有价值的下一步行动。”

参考来源：

Attacker Uses Suspected AI-Generated PowerShell Script to Map Active Directory

https://thehackernews.com/2026/07/attacker-uses-suspected-ai-generated.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3M5qLVTGP6jiaibktDcXOic6E1x1CNbVhdStkk8micFrCq9q4Hp2oH9WnQ229S3ziaeHPACAgicCRKZjic3pV1CTArGRs1KdhccugdUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342454&idx=1&sn=30ae51eba566ed3187493e4e817d3124&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38DqtZUv5FjJ2NibZ3wlLba7jpicoInsIGFnVouGN6kbudJyTf7yhkPM5z8JBrkOVNnialq3PeHX0JzJ9vkBXoUwAdicH70OSf4Wc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3vp7Nh5SN03lJzkelia9oMl3rDgBcDgQuSu66GUobMfu7PibWYZsgcVfAuZ1aAVwMiatGia3JO3kthfNotNqKQC8uiaS9Za2ky2BVI/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0d7KoyEHYsPfbgBgXYQmHS9EgIpOAxfibDrVp8uYPQd3yzGxCrUKcoiajc9NX5KNwMKmib2nnrSsnDa8POob7G5mibuxwMMez0bfI/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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