---
title: Active Directory 里的影子管理员：攻击者利用的隐蔽特权路径
url: https://mp.weixin.qq.com/s/S9TrONgH_kiYJlm19jboRA
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:51:20.214478
---

# Active Directory 里的影子管理员：攻击者利用的隐蔽特权路径

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibedk0ib1lDCMnMOZOWOcibvXIZc41jiawtZkjRoX6XLtE0A2BN2So7BqWpUibzmONJJvZqYkqicL4icibrjz7mA9hZVn4G4HOpYE6F8Wo/0?wx_fmt=jpeg)

# Active Directory 里的影子管理员：攻击者利用的隐蔽特权路径

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 在Active Directory环境中，许多看似普通的账户其实拥有等同于域管理员的特权。这些“影子管理员”形成了巨大的安全盲区，而它们的成因往往出人意料，从虚拟化平台管理员到普通的服务台账号都可能在其中扮演关键角色。本文将揭示几种常见的影子管理员路径及其背后的安全逻辑。

## 什么是影子管理员？

如果你负责Active Directory安全，你可能已经花了不少力气去管好Domain Admins组里的那些账号。问题是，攻击者已经不太关心这些明面上的目标了。他们的兴趣转向了那些不在任何特权组里、却在某些间接路径上拥有顶级权限的账户。

这就是影子管理员。这些账号用net group命令查不到，特权访问管理（PAM）工具的报告里也看不到他们。但恶意攻击者只要拿到其中一个，基本上就等于赢了。他们就像潜伏在系统中的隐形管理员，是身份和访问管理工具最常忽略的盲区。

这几年，随着企业数字化转型，问题变得更糟了。工作负载迁到AWS和Azure，身份通过ADFS联合到云端，域控制器在ESXi上跑着虚拟机。一个账号失陷，影响范围早就超出了传统AD的边界。现在一台VMware管理员的主机，可能就是通往你整个AWS环境的跳板。

下面我们看几个实战中经常遇到的例子。这些都是真实的隐患。

## ADFS服务器：身份联合的双刃剑

如果你的公司在用AD Federation Services（ADFS）把身份联合到云服务商，那你应该听说过SolarWinds攻击里用到的“金色SAML”手法。ADFS服务器握着令牌签名证书的私钥，它能生成所有云服务商都认可的SAML断言。

这个服务器要是被拿下，攻击者就能伪造任何联合用户的令牌，包括那些云管理账号。这问题为什么和AD影子管理员有关？

因为它创造了双向的影子管理员路径。

* 从本地方向看：控制了本地的ADFS服务器（作为身份提供者），攻击者就能进入你的整个AWS Organization、Azure订阅和GCP项目。
* 从云端方向看：如果那台ADFS服务器本身是跑在EC2实例或者Azure VM上，或者由某个云端的配置管道管理，那一次云层面的入侵，就能给攻击者开一条回到本地AD的路。

结果就是，任何能管理ADFS服务器或其底层基础设施的人，在效果上都成了你云环境的影子管理员，甚至可能是本地域的影子管理员。这些人通常是服务器运维团队、备份操作员，还有下文要提到的虚拟化团队。他们根本不在任何特权AD组里，却握有关键权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcBviap01ozB5hh2SEWic9crmlicWfwHhyycpARWOpsE0akb99luic2t8ZVJNtgL66TLia4bGHl4MNTibFwLOaVZzLq14IFqEEwnz17Q/640?wx_fmt=png&from=appmsg)

**怎么处理？**把ADFS服务器当作和域控制器同级的Tier 0资产来对待。如果可能，迁移到云原生的认证方案（如无缝SSO或直通身份验证），彻底去掉本地的令牌签名密钥。

## 虚拟化管理员的特权路径

现在很多公司都把域控制器做了虚拟化。从运维角度看，这很合理。但从攻击者角度看，这事就意味深长了。

如果你的域控制器是ESXi上的虚拟机，那么任何能管理这台虚拟机管理程序（hypervisor）的人，都间接控制了这台域控制器。VMware管理员可以做快照，离线提取NTDS.dit文件，访问虚拟控制台，挂载启动盘，甚至克隆整个虚拟机来离线提取凭证。这些权限可能直接关系到域内每个账号的密码哈希。

你可能会想，如果攻击者只有ESXi控制台（VMRC）的访问权限呢？实际上，这通常就够了。有VMRC权限的操作员可以直接看到Windows登录界面，用任意域用户身份登录，然后尝试本地提权。

同样的逻辑适用于每一个虚拟化了的Tier 0资产。包括ADFS服务器、PKI证书颁发机构、Azure AD Connect服务器。如果前面提到的ADFS服务器跑在ESXi上，那么虚拟化管理员可以直接攻陷它，提取令牌签名证书，然后伪造SAML令牌进入你的云环境——全程都无需直接连接AD。

这是一条横跨三个不同管理域（VMware、AD、AWS）的影子管理员攻击链，而这三方团队中的任何一个，通常都看不到完整的路径。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfnJVtYbKUo4JJFLIia6iaBbicxyhCpxdfBvc0dgKKRAG0B0DaEhdnxNIaGlR3uCBS041LW8SNsdUHMfuvyiczQQibVEAzYKibak20og/640?wx_fmt=png&from=appmsg)

**怎么处理？**如果一台虚拟机管理程序承载了Tier 0的虚拟机，那这台管理程序本身就是Tier 0资产。用专门的ESXi主机来跑Tier 0工作负载，把VMRC访问权限限定给Tier 0管理员。

## 服务台权限滥用与ACL问题

在典型的委托模型里，服务台管理员会被授予对AD中计算机账户对象的写入权限。这看起来很合理。服务台人员需要重置机器密码、更新描述、在系统重装时管理属性。

但问题就出在，对计算机账户对象的写入权，包含了修改`msDS-AllowedToActOnBehalfOfOtherIdentity`属性的能力。这个属性控制着基于资源的约束委派（RBCD）。

攻击者如果拿下一个服务台管理员账号，就可以把任何他有写入权限的计算机对象，配置成信任一个由他控制的账号进行委派。之后他就能用S4U2Self和S4U2Proxy来在那台计算机上模拟一个特权用户。如果这个可写的计算机对象碰巧是域控制器，那整个域就沦陷了。

这就是用户账户仅凭过度的权限就成为影子管理员的典型案例。我们经常看到这个模式被ACL权限漂移放大。在最近的一次评估中，我们发现某个委托组对服务账户有GenericAll权限，而那个服务账户又对某个管理组有AddMember权限，同时还有其他组对特权账户有WriteAccountRestrictions权限。单独看每一步都好像说得通，但连在一起，就构成了一条从低权限委托组通往完全域控制的路径。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdgAszRfoOu9jYe6KGpeUnH22ulwKulk6kOM8oia6hhRFYtZI0RLoibZDTEV1qID8zEe8QFAQy1mMkAwGlGJ7JhPNahuk08wuz1Y/640?wx_fmt=png&from=appmsg)

**怎么处理？**移除所有非Tier 0组对DC计算机对象的写入权限。把服务台的委托权限限制在不包含Tier 0或Tier 1机器账户的组织单位（OU）里。

## Azure AD Connect：AD里的影子账户

如果你为目录同步设置了Azure AD Connect，那你肯定见过那些它自动创建的、以“MSOL\_”为前缀的同步账户。这些账户，按照设计，需要DCSync权限——这正是复制域内所有密码哈希所需的权限。

在最近的一次评估里，我们检查DCSync权限时，发现了一个名为`MSOL_EXAMPLE@CONTOSO.LOCAL`的账户。它的密码被设为永不过期，受AdminSDHolder保护，还对多个委托组拥有GenericWrite和GenericAll权限。这个账户就这么放着好几年没人管。

这就是一个拥有敏感权限却缺乏管理的典型账户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdiaU3YBHf0GwB4DNyzlDz4uVzgmnB6nwBKMTJDR8EdriaP9Xq0hZ71e3cewfibzCySxxO5ZEfnECyzXicicnuiaoticTgnbpIJ4siaJibE/640?wx_fmt=png&from=appmsg)

更麻烦的是，Azure AD Connect服务器经常被当作一个中层的应用服务器，而不是Tier 0资产来管理。它通常跑在共享的虚拟化平台上，由管理通用基础设施的团队负责，备份方案也和其他系统混在一起。这些相邻系统中的任何一个，都可能成为通向DCSync和完全域控制的间接路径。

**怎么处理？**把Azure AD Connect服务器当作Tier 0资产。可以考虑迁移到Azure AD云同步，这个方案不需要在域级别配置DCSync账户。

## 了解影子管理员层级与检测

不是所有影子管理员都一样。在安全研究中，一级影子管理员，是指那些对现有管理员账户或域管理员组拥有强大权限的账户，比如能重置域管理员的密码，或者能修改域管理员组的成员。二级影子管理员则是对一级影子管理员有控制权限，从而形成一条传递链。

现实中，大环境里的很多影子管理员都是二级或更深层级的，这让检测变得非常困难，因为没有哪个团队能看到完整的链条。

设想一个场景：Larry是一个二级影子管理员，他对一个服务台账户拥有GenericAll权限。而那个服务台账户，又对域特权组的某个成员拥有WriteOwner权限。无论是Larry自己，还是服务台团队，都没意识到他们已经处于一条能直达域管理员权限的链条里了。

影子管理员检测需要持续审计域内的所有账户和组，不仅要检查直接的组成员关系，还要看权限的完整传递闭包。传统的管理员可见性工具只检查账户是不是某个特权组的成员。它们会漏掉那些通过委派、所有权或其他访问控制路径获得管理员权限的账户。

## 如何识别并降低影子管理员风险

上面这些例子有个共同点：影子管理员路径越来越频繁地跨越不同管理域的边界。你的VMware团队、服务台、云运维团队和身份团队，都在管理着一个互联系统中各自那部分风险，但没有谁清楚自己的权限是如何和其他人的组合在一起的。

这只是我们最近遇到的一部分问题。影子管理员的威胁也不仅限于AD。我们在之前的文章里也提过，一个配置了root权限和基于密码SSH访问的漏洞扫描器账户，也可能在某个被攻陷的主机上被拦截，让你自己的安全工具变成横向移动的跳板。

> 在真实世界里，想在不同层级的用户和组之间干净地划分权限非常困难。权限分配上的人为错误是不可避免的。但每条安全控制措施（或缺失的控制措施）带来的风险，都必须被清楚地认识。没有持续监控，任何用户都可能给自己或他人授予需要域管理员权限的未授权访问，而在有人发现之前，一切可能都太晚了。

**几个关键建议：**

* 只要一个身份存在通往域级别权限的传递路径，那它就是影子管理员，不管它是哪个团队在管。
* 做好内置组的审计——不只“域管理员”和“企业管理员”组，是所有管理组和特权角色。
* 承载或管理Tier 0资产的系统，它自己就是Tier 0：虚拟机管理程序、ADFS服务器、AD Connect服务器都是。
* 联合身份验证基础设施是你的本地域和云端的桥梁。相应地，把它作为你身份安全战略的一部分来加固。
* ACL漂移是持续发生的。一次性的检查不够。投资于特权访问管理和持续的访问管理，以便在未授权变更发生时就能发现。

说实话，如果你在运行AD，那你肯定有影子管理员。问题在于，是你先找到他们，还是恶意攻击者先找到。

---

### 参考资料

[1] https://www.praetorian.com/blog/shadow-admins-active-directory/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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