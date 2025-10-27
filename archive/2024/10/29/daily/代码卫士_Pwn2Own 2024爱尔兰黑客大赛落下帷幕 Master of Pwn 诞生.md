---
title: Pwn2Own 2024爱尔兰黑客大赛落下帷幕 Master of Pwn 诞生
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521303&idx=1&sn=741af621329dcd54f31bdaa6d93a7347&chksm=ea94a57ddde32c6bc1de5d890d7c66d24412921260f5c1eecf49caefd86f6ffbf17e92b17ba3&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-29
fetch_date: 2025-10-06T18:51:24.405608
---

# Pwn2Own 2024爱尔兰黑客大赛落下帷幕 Master of Pwn 诞生

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTgicnicddUYKiaW0UuECmnFcFAALZOic876rqFiblXxE7icqJBqGrGMNqHACUrrCv5RApW5dlnQpBBdnbA/0?wx_fmt=jpeg)

# Pwn2Own 2024爱尔兰黑客大赛落下帷幕 Master of Pwn 诞生

ZDI

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTgicnicddUYKiaW0UuECmnFcFC8ChDdfC58iajZLXGWNl47licTcCsqnVztMbTyBVM4PA8PcjZaHwCkxg/640?wx_fmt=gif&from=appmsg)

**为期四天的Pwn2Own 爱尔兰黑客大赛落下帷幕。主办方ZDI为所发现的70多个唯一0day共颁发1066625美元的赏金。这是第四次总赏金超过100万美元的大赛。最终，Viettel Cyber Security 团队以33个积分点和205000美元的赏金拔得头筹。如下是对各团队每天的比赛情况概述。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTgicnicddUYKiaW0UuECmnFcFbCY8EyLpia15UJ5BCsjMLbMHHEjwPIe2xIClsWcOFbBrDRkNf4Wz0ug/640?wx_fmt=jpeg&from=appmsg)

**第一天比赛情况**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTgicnicddUYKiaW0UuECmnFcFmg65JlicHcg5icWFgjDJ4nhbKsA0iaepMIiceYeIuLluJycDfRWpRdCxicQ/640?wx_fmt=gif&from=appmsg)

|  |  |  |
| --- | --- | --- |
| **战绩** | **战队** | **战况** |
| 成功+成功+成功 | Viettel Cyber Security | （1）   Phudq和namnp 使用基于栈的缓冲区溢出和一个不可信指针解引用漏洞，成功利用   Lorex 2K WiFi摄像头，赢得3万美元赏金和3个积分点。  （2）   组合4个漏洞（2个是路由器类，2个是NAS类），实现从   QNAP QHora-322到 TrueNAS MiniX。组合利用SQL注入和缺失认证的/被暴露的函数漏洞最终为他们赢得5万美元赏金和10个积分点。  （3）   @dungnm、@dungdm 和@tunglth 使用基于堆的缓冲溢出成功利用 Synology TC500，获得3万美元赏金和3个积分点。 |
| 失败 | Can Acar | 该研究员未能在规定时间内完成对 Synology   TC500 摄像头的利用。 |
| 成功+失败+失败+失败+失败 | Summoning Team | （1）   Sina Kheirkhah 利用9个不同漏洞成功实现从   QNAP Qhora-322 到 TrueNAS Mini X，最终赢得10万美元赏金和10个积分点。  （2）   无法在规定时间内在 QNAP TS-464上执行利用。  （3）   未能在规定时间内，在 Synology BeeStation BST150-4T上成功实施利用。  （4）   未能在规定时间内使其 Synology DiskStation DS1823xs+利用成功运行。  （5）   未能在规定时间内使其 Lorex 2K Indoor WiFi 的利用起作用。 |
| 成功+成功 | RET2 Systems | （1）   Jack Dates 使用一个OOB 写，成功利用   Sonos Era 300扬声器，最终获得6万美元赏金和6个积分点。  （2）   利用一个OOB 写在   Synology DiskStation DS1823xs+ 上获得一个 shell 和修改登录页面，获得2万美元赏金和4个积分点。 |
| 成功 | Team Neodyme | 通过一个基于栈的缓冲溢出漏洞，成功利用 HP   Color LaserJet Pro MFP 3301fdw 打印机，最终赢得2万美元赏金和2个积分点。 |
| 成功+失败+退出 | PHP Hooligans/Midnight   Blue | （1）   通过一个漏洞成功利用 Canon imageCLASS MF656Cdw 打印机，最终获得2万美元赏金和2个积分点。  （2）   未能在规定时间内，使其 Lorex 2K Indoor WiFi 摄像头的利用起作用。  （3）   退出对“监控”类别中 Synology TC500 摄像头的利用尝试。 |
| 撞洞+成功 | Synacktiv | （1）   虽然通过2个漏洞成功利用   Lorex 摄像头，但其中一个是此次比赛中已使用过的漏洞，不过仍然获得11250美元的赏金和2.25个积分点。  （2）   组合利用3个不同漏洞，成功利用   Ubiquiti AI Bullet。所有漏洞都是唯一的，因此获得1.5万美元赏金和3个积分点。 |
| 成功 | ExLuck（@pivik\_） | 组合利用4个漏洞（其中一个是证书认证不当，另一个是硬编码密钥），成功利用   QNAP TS-464 NAS 设备，最终获得40000美金赏金和4个积分点。 |
| 失败 | DEVCORE Internship Program | YingMuo 未能在规定时间内，使其对 Canon imageCLASS MF656Cdw 的利用起作用。 |
| 成功 | STEALIEN Inc. | 研究员Bongeun Koo、Dohyun Kim、Junyong Choi、Wonbeen Im、Juhyeop Lee、Juyeong Lee、GuckHyeon Jin、Jongmin Kim，组合利用多个漏洞构成攻击链，成功利用 Ubiquity AI   Bullet，获得3万美元赏金和3个积分点。 |
| 成功 | Rapid7 | Ryan Emmons 和 Stephen   Fewer 利用参数分隔符中和不当漏洞成功利用 Synology DiskStation DS   1823xs+，且它还适用于其他 Synology 设备。他们获得4万美元赏金和4个积分点。 |
| 失败 | InfoSect | 该团队未能在规定时间内，成功实施 Synology   TC500 摄像头的利用。 |
| 成功 | Josh Foote | 利用一个基于栈的缓冲溢出漏洞，成功利用 Lorex   2K WiFi 摄像头，获得1.5万美元赏金和3个积分点。 |

**第二天比赛情况**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTgicnicddUYKiaW0UuECmnFcFmg65JlicHcg5icWFgjDJ4nhbKsA0iaepMIiceYeIuLluJycDfRWpRdCxicQ/640?wx_fmt=gif&from=appmsg)

|  |  |  |
| --- | --- | --- |
| **战绩** | **战队** | **战况** |
| 成功 | ANHTUND | Pham Tuan Son和 ExLuck   (@ExLuck99)使用一个基于栈的溢出漏洞，成功利用 Canon imageCLASS MF656Cdw   打印机，获得1万美元赏金和2个积分点。 |
| 成功 | NCC Group | Ken Gannon 利用5个不同漏洞（其中一个是路径遍历）获得一个shell并在三星 Galaxy S24上安装了一款app，获得5万美元赏金和5个积分点。 |
| 成功+成功 | Viettel Cyber Security | （1）   Dungdm 通过一个UAF漏洞利用   Sonos Era 300，获得3万美元赏金和6个积分点。  （2）   该团队使用一个类型混淆漏洞，成功利用 HP Color LaserJet Pro MFP 3301fdw，获得1万美元赏金和2个积分点。 |
| 撞洞 | Tenable Group | 通过一个基于栈的缓冲溢出漏洞，成功利用 Lorex   2K摄像头，不过由于该漏洞已在大赛中使用过，最终获得3750美元赏金和1.5个积分点。 |
| 失败+成功+成功 | DEVCORE Research Team | （1）   @d3vc0r3和@nella17未能及时完成   SOHO Smashup，虽然打入路由器但未能弹出打印机。  （2）   YingMuo 通过一个参数注入和SQL漏洞在   QNAP TS-464 NAS 上获得root shell，获得2万美元赏金和4个积分点。  （3）   NiNi 通过加密签名验证不当漏洞利用 AeoTec Smart Home Hub，获得4万美元赏金和4个积分点。 |
| 失败 | Rapid7 | Ryan Emmons和Stephen   Fewer未能在规定时间内在 Lorex 2K摄像头上实施利用。 |
| 成功+撞洞 | InfoSect | （1）   该团队通过一个基于堆的缓冲溢出漏洞接管了 Sonos Era 300扬声器，共获得3万美元赏金和6个积分点。  （2）   成功在 Lorex   摄像头上获得shell，但其中一个漏洞是此前已知的。结果获得3750美元和1.5个积分点。 |
| 成功+成功 | Team Cluck | （1）   Chris Anastasio   和 Fabius Watson 通过两个漏洞（包括一个 CLRF 注入）组成漏洞链，成功利用   QNAP TS-464 NAS设备，共获得2万美元赏金和4个积分点。  （2）   利用一个证书验证不当漏洞利用 Synology DiskStation，获得2万美元赏金和4个积分点。 |
| 失败 | Cody Gallagher 和 Charlie   Waters | 未能在规定时间内，使其 Sonos Era 300的利用起作用。 |
| 成功 | PHP Hooligans/Midnight   Blue | 通过一个命令注入漏洞在 Synology   BeeStation BST 150-4T上成功执行代码，共获得4万美元赏金和4个积分点。 |
| 撞洞 | Reverse\_Tactics | Corentin BAYET 通过三个漏洞从 QNAP   QHora-322 进入 QNAP TS-464，不过其中1个漏洞为此前已知，不过仍获得41750美元和8.5个积分点。 |
| 失败 | Summoning Team | 研究员 Sina Kheirkhah 未能在规定时间内成功运行   TrueNAS Mini X 的利用。 |
| 失败+成功/撞洞 | Neodyme 团队 | （1）   未能在规定时间内，成功运行 Lexmark CX331adwe 打印机的利用。  （2）   利用四个漏洞（含一个基于栈的缓冲溢出漏洞）成功演示对SOHO Smashup的利用，但其中一个漏洞是此前已知。结果获得21875美元赏金和8.75个积分点。 |
| 撞洞 | Synacktiv 团队 | 成功利用 Synology Beestation，但由于其中一个漏洞是此前已用漏洞，因此获得1万美元赏金和2个积分点。 |
| 撞洞 | Compass Security | 在 Ubiquiti AI Bullet 利用中撞洞，不过仍获得3750美元和1.5个积分点。 |

**第三天比赛情况**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTgicnicddUYKiaW0UuECmnFcFmg65JlicHcg5icWFgjDJ4nhbKsA0iaepMIiceYeIuLluJycDfRWpRdCxicQ/640?wx_fmt=gif&from=appmsg)

|  |  |  |
| --- | --- | --- |
| **战绩** | **战队** | **战果** |
| 成功+成功+撞洞+失败 | Viettel Cyber Security | （1）   Ha The Long 和 Ha Anh   Hoang 通过一个命令注入漏洞，利用 QNAP TS-464 NAS设备，共获得1万美元赏金和4个积分点。  （2）   通过一个类型混淆漏洞成功利用 Lexmark CX221adwe 打印机，获得2万美元赏金和2个积分点。  （3）   Namnp 和 tunglth所用的栈缓冲区溢出漏洞虽然接管了   Canon 打印机但为大赛此前所用，因此获得5000美元赏金和1个积分点。  （4）   未能在规定时间内成功实施针对 Ubiquiti AI Bullet利用。 |
| 失败 | Summoning Team | Sina Kheirkhah 和 Enrique   Castillo 未能在规定时间内在 Uiquiti AI Bullet 上成功执行利用。 |
| 成功 | DEVCORE Research Team | Pumpkin Chang 和 Orange   Tsai组合利用一个 CRLF 注入、一个认证绕过和一个SQL注入成功利用   Synology BeeStation，获得2万美元赏金和4个积分点。 |
| 成功 | PHP Hooligans/Midnight   Blue | 通过一个OOB 写和一个内存损坏漏洞成功从   QNAP QHora-322 进入 Lexmark 打印机，成功打印出自己的“现金”。这次成功的   SOHO Smashup 为他们赢得2.5万美元赏金和10个积分点。 |
| 撞洞 | STEALIEN Inc. | 成功弹出 Lorex 摄像头，不过其中一个漏洞此前已用于比赛，获得3750美元赏金和1.5个积分点。 |
| 成功 | Team Smoking Barrels | 通过一个不受保护的主要频道漏洞利用 Synology   BeeStation 实现代码执行，获得1万美元赏金和4个积分点。 |
| 成功 | Computest Sector 7 | Daan Keuper、Thijs   AIkemade和Khaled Nassar 组合利用4个漏洞（其中一个是命令注入，另外一个是路径遍历），成功从   QNAP QHora-322 到TrueNAS MiniX，获得2.5万美元赏金和10个积分点。 |
| 失败 | ANHTUD | ExLuck 未能在规定时间内完成 SOHO Smashup，虽然成功打入 Synology 路由器但未能成功跳转到   Canon 打印机。 |

**第四天比赛情况**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTgicnicddUYKiaW0UuECmnFcFmg65JlicHcg5icWFgjDJ4nhbKsA0iaepMIiceYeIuLluJycDfRWpRdCxicQ/640?wx_fmt=gif&from=appmsg)

|  |  |  |
| --- | --- | --- |
| **战绩** | **战队** | **战况** |
| 撞洞 | Team Smoking Barrels | 通过2个漏洞成功利用 True NAS X，但为大赛此前已用漏洞，不过仍然获得2万美元赏金和2个积分点。 |
| 成功/撞洞 | Team Cluck | Chris Anastasio 和 Fabius   Watson 组合利用6个漏洞成功从 QNAP   QHora-322 进入 Lexmark CX331adwe，但其中1个此前出现在大赛中，不过仍然获得2.3万美元赏金和9.25个积分点。 |
| 撞洞 | Viettel Cyber Security | 通过2个漏洞利用 TrueNAS MiniX，不过撞洞，仍然获得2万美元赏金和2个积分点。 |
| 成功 | PHP Hooligans/Midnight   Blue | 通过一个整数溢出漏洞利用 Lexmark 打印机，获得1万美元赏金和2个积分点。 |

    Viettel Cyber Security 团队最终以20500美元的赏金和33个积分点的战绩独占鳌头。Team Cluck、PHP Hooligans / Midnight Blue、DEVCORE 和 Neodyme 分列第二、三、四、五位。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[黑客在思科商店注入恶意JS，窃取信用卡和凭据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=3&sn=ca7a392b964011a90f44ef9b56046155&chksm=ea94a0c1dde329d7b3357897b0d476fbdcccdb403a0341d564f40687a51b08c0f26ca20939a6&scene=21#wechat_redirect)

[思科修复已有 PoC 的根提权漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=1&sn=00f735c28afb0e6cc70f919cade9dc5c&chksm=ea94a0c1dde329d7537d32cf0cc038587d8e6da619b0dc82fb99bb8917e432ece7028a7dd65c&scene=21#wechat_redirect)

[思科：注意这些已达生命周期IP电话中的RCE 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=2&sn=bad61fd4a7dd0064d77...