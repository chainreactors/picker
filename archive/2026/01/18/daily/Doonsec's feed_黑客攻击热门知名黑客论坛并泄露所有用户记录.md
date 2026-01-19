---
title: 黑客攻击热门知名黑客论坛并泄露所有用户记录
url: https://mp.weixin.qq.com/s/FBLu9zMY1piyVdadUwqNWA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:44:18.275944
---

# 黑客攻击热门知名黑客论坛并泄露所有用户记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eCL9rXDTWqSicA3mutEGpgibgSoOeE8QT1JbkedmlUQRqesrA5feayTV9zHF7wtUnFVHUyOdEfhSXibz8Iunw4d8w/0?wx_fmt=jpeg)

# 黑客攻击热门知名黑客论坛并泄露所有用户记录

河南等级保护测评

![]()

在小说阅读器中沉浸阅读

以下文章来源于豫说网数安
，作者铸盾安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM59AUe157CquBULm3Sn1mS0bZLHRaoSOicaicgKiaq5h5rsQ/0)

**豫说网数安**
.

网络安全人人有责，贯彻网络安全为人民，网络安全靠人民。网络安全和信息化是相辅相成的。安全是发展的前提，发展是安全的保障，安全和发展要同步推进。

![](https://mmbiz.qpic.cn/mmbiz_png/eCL9rXDTWqSicA3mutEGpgibgSoOeE8QT12TkUkRaJB5ib6Mb1oVrFWUyxYt4fmGnKiaNhMv1M9IlaXqcdOUOW85hg/640?wx_fmt=png&from=appmsg)

网络犯罪地下世界发生戏剧性转变，一位名为“James”的神秘黑客泄露了 BreachForums 的完整用户数据库，BreachForums 是一个臭名昭著的暗网论坛，是窃取数据交易和黑客讨论的中心。

*此次数据泄露事件于 2026 年 1 月 9 日通过shinyhunte.rs*网站宣布，泄露了超过 323,986 名用户的元数据，其中包括管理员、版主和普通成员，这可能会使许多人面临执法部门的审查。

这一事件凸显了网络犯罪分子最终成为自身漏洞受害者的讽刺之处。

## **BreachForums 数据泄露**

BreachForums 于 2022 年成立，是 RaidForums 的继任者。RaidForums 因涉嫌数据贩运而被美国当局查封。

该论坛由MyBB 软件提供支持，促进了泄露数据集、黑客工具和非法服务的销售，尽管屡次遭到关闭，但这些服务通常通过 DDoS-Guard 和 Tor 镜像托管。

关键的干扰事件包括 2023 年创始人 Conor Fitzpatrick 被捕，他被判处 20 年监管释放，以及 2024 年域名被查封，但很快就被运营商ShinyHunters收回。

ShinyHunters 与 Scattered LAPSUS Hunters 等组织有关联，多次重启网站，在 2025 年 6 月法国警方逮捕其成员以及美国联邦调查局查封勒索网站后仍然幸存。该论坛的韧性依赖于频繁更换域名和在暗网上的存在，但 MyBB 的底层缺陷最终导致了它的覆灭。

从“hcclmafd2jnkwmfufmybbusers”表中导出的 MySQL 数据库泄露了 ShinyHunters、Hollow 和 IntelBroker 等知名账户的用户名、哈希密码（Argon2）、电子邮件、IP 地址、注册日期和 PGP 密钥。

分析显示，管理员 (4)，超级版主 (3)，版主 (6)，用户来源遍布美国（占比最大）、德国、荷兰、法国、土耳其、英国以及摩洛哥和埃及等中东和北非地区。

![](https://mmbiz.qpic.cn/mmbiz_jpg/eCL9rXDTWqSicA3mutEGpgibgSoOeE8QT1Gt6ftJC2S29SX4AqSzVlDc3YqCMjqKY1uXAWtndTV6ia3uTSwhMVMiaw/640?wx_fmt=jpeg&from=appmsg)

附件图片中的截图显示了 shinyhunte.rs 页面，页面上有一篇题为“末日：詹姆斯的故事”的宣言，以及一个显示用户所在国家/地区的饼图，其中美国用户数量占主导地位。詹姆斯声称，此次安全漏洞源于一个网络应用程序的漏洞或配置错误，使得犯罪分子的避风港变成了他们的累赘。

![](https://mmbiz.qpic.cn/mmbiz_jpg/eCL9rXDTWqSicA3mutEGpgibgSoOeE8QT1YtAVgDElsGHibwPLicOAtW0Iic2Tronw9RlMgZBBCp1fbAFJJrn9zwTXg/640?wx_fmt=jpeg&from=appmsg)

在“末日”的旗帜下，詹姆斯将自己描绘成一个超越世代的“捕食者”，吹嘘自己渗透了谷歌、微软、联邦调查局、国家安全局等机构。

他点名道姓地指认了多里安·达利（Kams）、纳赫尔·奥赫达（INDRA）、阿里·阿布西（Kernel）等涉嫌组织成员，以及Prosox/Kuroish的创始人，并誓言要让他们因背叛更高目标而垮台。詹姆斯在面向法国读者的讲话中，将自己塑造成这些他曾经指导过的“孩子”的保护者，并将他们与反法活动联系起来。

该文本将黑客传说与关于权力、邪恶和救赎的哲学论述融合在一起，呼应了过去的地下宣言。

这种自作自受的举动暴露了暗网网站上的明文风险，在全球打击行动的背景下，加剧了逮捕威胁。受害者面临个人信息泄露的风险，而执法部门则在“The Com”网络中获得了有关 ShinyHunters 衍生项目的线索。Resecurity分享了用于分析的数据包，并警告称，针对 Salesforce 等公司的敲诈勒索活动将受到更广泛的冲击。

正如詹姆斯所言“无处可藏”，BreachForums 事件说明了网络犯罪的脆弱性，捕食者最终会被更强大的捕食者吞噬。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sNicKB84ZxoERdyt2icMobIJOJ7gZ6EE7A5Lu91AicvWMVsCUpMGUVic1PkJD8nJULlZG3XyRDzTNpQbVsfyFBLYeg/0?wx_fmt=png)

河南等级保护测评

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sNicKB84ZxoERdyt2icMobIJOJ7gZ6EE7A5Lu91AicvWMVsCUpMGUVic1PkJD8nJULlZG3XyRDzTNpQbVsfyFBLYeg/0?wx_fmt=png)

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