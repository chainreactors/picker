---
title: 俄罗斯APT组织关联账号域名与人员身份链分析案例
url: https://mp.weixin.qq.com/s/nKUNnJoFy-XiW3I59Q-QGw
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:50:43.315541
---

# 俄罗斯APT组织关联账号域名与人员身份链分析案例

# 俄罗斯APT组织关联账号域名与人员身份链分析案例

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 2021年，两波大规模邮件活动先后指向俄罗斯FD派支持者，一波夹带个人信息与起诉威胁，一波仿冒智能投票推荐以分裂选票。公开调查沿账号、域名和泄漏数据库逐层回溯，最终把活动背后的人与一家被美国起诉的俄罗斯私营公司Yutek-NN联系起来，相关APT威胁活动跟踪编号为Void Blizzard/Laundry Bear。

# 下文按调查脉络梳理事件经过、技术线索与人员归属，仅做情报分析案例，无任何zz立场。

# 两封邮件的来龙去脉

Alexei Navalny是俄罗斯fd派。2021年初其团队发起Free Navalny运动，动员公众支持其获释，支持者在free[.]navalny[.]com注册登记。

2021年4月，一份含注册者邮箱的数据库被获取并泄漏，记录与其他泄漏数据交叉补充后发布到XSS[.]is论坛，这批数据随后被用于针对库内人员的邮件活动，邮件夹带收件人个人信息和起诉威胁。

2021年9月国家杜马选举前不久，同一泄漏数据库被用于第二波邮件活动，分发虚假的智能投票推荐，用以混淆选民、分裂对立派选票。

# 仿冒域名与一组关联站点

2021年9月投票开始前不久，调查方即对这波大规模邮件活动展开追踪。邮件仿冒合法的智能投票推荐，却替换成另一些候选人。

邮件发自vote@fbkinfo[.]tech，域名刻意仿冒fbk[.]info，后者是Navalny组织反腐基金会FBK的合法域名。fbkinfo[.]tech的WHOIS（域名注册记录）显示注册人姓名为Gennadii Babkov，注册邮箱babkov@protonmail[.]com，调查方未找到该身份真实存在的证据，判断注册信息系伪造。反向WHOIS检索进一步带出一批通过共享注册细节关联的基础设施。

按域名命名、注册关联和已观测内容，其中一组域名被评估用于反Navalny活动，另一组可能支撑一个或多个独立钓鱼活动，完整清单见文末附表。多数域名当时托管的内容和具体用途，调查方并未掌握。

navalny-team[.]com在当时即较为突出，站点托管了一批批评Navalny和FBK的文章，基于Ghost发布平台搭建。调查方尝试用babkov@protonmail[.]com登录站点后台，系统提示该邮箱未关联任何用户账号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqvmI90V3kkhWwpFibmhxjPotZVSYpnUDFt3VFYy32nHuFfyVsHeSWEicUkGiaM3fnWkW6UiaH4Krn4fz9746bCGKyQZFcibmpQaNyk/640?wx_fmt=png)

图1 navalny-team[.]com上的批评性博客页面

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrOoWibqnoa1xGQyL1TzSC3BLNoc4hejiaLJe7icP9zjxQ9mOYRxkuU2icAFNU7QdzYIsmJPompHRJyfUL7gXE6o72sUP3tBqBe9ZA/640?wx_fmt=png)

图2 以babkov@protonmail[.]com尝试登录后台，提示无此账号

# 退订链接里漏出的邮箱

虚假邮件除候选人信息外，版式与合法邮件完全一致。调查方判断，操作者很可能先收到过一封合法推荐邮件，复制其版式和样式，替换候选人细节后再分发欺诈版本。

威胁行为者同时复制了合法邮件的退订链接，且未做修改。该链接指向邮件订阅设置页，页面回显了原始邮件被发送到的地址：evilsocks.dev@gmail[.]com。调查方据此高置信度判断，该邮箱是合法原始邮件的收件地址。在navalny-team[.]com的Ghost后台测试该地址时，确认存在关联账号，支持邮箱由威胁行为者控制这一判断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqy1y8XOtxa9YnaVf77lNfbKdhNv1AibtHiakqzrj6LbaR2uzHxRibnIp2u7tNlCQ30sxBH1xyttANyg5eWeXHC3bPy0ee3Ppy6MM/640?wx_fmt=png)

图3 虚假智能投票邮件界面（俄文界面）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDotzwEtwL4kIF4QwxR520ibjTgIMianbmvqdPBM1xM1fibTA0hf09V1jLzNjd4ASsbblib7SAJdKdiauxYUWrXLn2ictQmgianHXSYJibY/640?wx_fmt=png)

图4 同一邮件的译文对照

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrTtuZu29icVl0xADSL6q6SjLQdI8HSEIez46AIElbEIQ3Hppy3icK8ic656xVoLqsT1qgRW3FyeoYR4ZpWkVzuzC2h15uqZ7aAEQ/640?wx_fmt=png)

图5 退订设置页（俄文界面），页面回显原始收件地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoZlEIkqdCwPP774zmpSKStlicCVM6s4hyFNRsQ1g45hHFgIDRe1EiaFsEkPVGyacmzzVD9ytLXsyQ5avGOyMdw23EjxYmAGsicv0/640?wx_fmt=png)

图6 退订设置页译文对照

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqsWhChvYbJ6Pickhqj4IWJBWYo7kA6ttkb7d2tDduyz9uAKqk1ibaR7XyQtPHPSiaHNVnHiaq820ZspfzmiaAwnFJIZhabrHv5dMts/640?wx_fmt=png)

图7 evilsocks.dev@gmail[.]com在站点后台存在关联账号

# 从邮箱追到GitHub账号

为定位与evilsocks.dev@gmail[.]com关联的人员，调查方由邮箱推导可能的用户名evilsocks.dev和evilsocks，由此找到一个评估为同一威胁行为者运营的GitHub账号github[.]com/EvilSocks。

该邮箱在账号关联的多个Git提交中留下痕迹，例如github[.]com/EvilSocks/avtozak\_help/commit/524993311a904548effe929d457608401bae5277.patch。仓库avtozak\_help创建于一场支持政治犯的线上黑客马拉松，项目是一个Telegram机器人，用于把被非法拘留的活动人士与能够提供协助的志愿者对接。

仓库附有一段发布在YouTube的演示视频，频道名为Evil Socks。视频虽有多帧模糊，但脱敏并不完整，若干帧可见演示者所处位置。依据画面细节，录制地点被地理定位到俄罗斯莫斯科州克拉斯诺戈尔斯克市Krasnogorskiy Bul’var, 8，邮编143401。视频中Telegram用户首字母缩写为БЮ，其中Б应为名字首字母，以Б开头的常见俄语男性名包括Boris（Борис）和Bogdan（Богдан）。

调查方还在讨论2021年4月另一波邮件活动的论坛帖中发现evilsocks.dev的痕迹，帖中邮件头片段显示To头收件人名为evilsocks.dev。调查方认为这是又一次OPSEC（运行安全）失误，行为者可能更换了收件地址，却保留了显示名。原始邮件未能取得，无法直接确认，但邮件头片段中的其他技术细节与4月活动观测到的基础设施和发送模式一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqtL5FAHp8ZuuQicGS4uxoxBFMtpI13oADnsq2UrXxGhb3EK0XMlu6mc986lDWicuRicxK76XwTzwsmrvDVg6tARBUib2GYf2bS2tI/640?wx_fmt=png)

图8 关联的GitHub账号EvilSocks主页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoANLrVPgIXcxofCH39PCia3gHpwiazhBhP4j1kicHkz8cVh54ia1DbAy4cdJdc7uSQrNtrgAhZXdZ3bmb9OVwNzMVps4XGouSQZHI/640?wx_fmt=png)

图9 Git提交记录中暴露的邮箱地址

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDppGpgXzRgAakwwSib8BmI8oic2us2SXOKEia13qYpticTRb81unlDia4nmv29cziaiap6LWjjZ0FBic1MHBC3ibIUCKupGmOph69rpibibgs/640?wx_fmt=png)

图10 演示视频中Telegram分享位置的画面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrgqo2THZGy0ryI8h1VXrNibQNE2Q8eEMlAqbbK1Opb9aNdQibf2tInibHibau98TGmoictRnecpzzPCmQDU1M5X6uBaic8KjLpBicSia8/640?wx_fmt=png)

图11 视频画面在Yandex地图上对应的定位点

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrEeQ9KTC6Gp4PTBByIJC9QOvicVnN3TUaCoh2zA5jx1OuUuQzeWCd5J3FlR810tV109Z2WBZkgmHNbwDyNsOic3Czv7pOZfyhDY/640?wx_fmt=png)

图12 4月活动邮件头片段，收件人显示名为evilsocks.dev

# 泄漏数据库拼出的身份：Anton Listarov

上述调查完成于2021年，当时未能识别EvilSocks别名背后的个人。调查方判断行为者尚未察觉邮箱已经暴露，因此未公开相关发现，预期其继续使用别名后会再留下新的失误。

三年后的2024年，复盘旧调查时，evilsocks.dev@gmail[.]com出现在Alfa-Insurance泄漏数据中，记录内含邮箱所有者的大量个人信息，并将该邮箱关联到Anton Listarov（Антон Александрович Листаров），1987年9月17日出生。

后续CDEK与Sport-Marathon[.]ru泄漏数据与之吻合，Listarov把个人手机号与该邮箱配合使用。另一份泄漏的Delivery Club订单库提供独立印证，Listarov的个人信息曾被用于向Krasnogorskiy Bul’var, 8, Krasnogorsk送餐40余次，正是演示视频地理定位出的地址。多起泄漏还确认Борис（Boris）是Listarov常用别名，与视频中的БЮ缩写吻合。综合这些材料，调查方高置信度判断，evilsocks.dev@gmail[.]com、相关别名以及欺诈性大规模邮件活动背后的人就是Anton Listarov。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDphtCSf8iafScV7WDu2rmxFDHDkyNoLRJxRLh4iaM7gzDia7qndWwB6jPWgFuFXrqZSgict810HtClmAlQ2u1cmPfQdnyX4iboK0zrU/640?wx_fmt=png)

图13 Alfa-Insurance泄漏记录，将邮箱与Anton Listarov关联

据泄漏数据和公开资料，Listarov来自俄罗斯萨马拉，现居莫斯科。其已删除的VK主页和约会网站账号显示，他曾就读于萨马拉大学（СГАУ/SSAU），旧LovePlanet账号用户名为flowerboy，照片中其约18岁；另可对应到vampiro.rastafari@gmail[.]com的Google账号头像，以及MirTesen主页mirtesen[.]ru/people/625909531的头像，照片中其约二十多岁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDo9wz1vazNW4gvQJe3Yq60dd7XoxVpKDcfyGvywfhc0BV0a0GCudlLd7B2yA9e3yE2waCiaFfIZRg9qibDUic0m4jltdOkxfucAkY/640?wx_fmt=png)

图14 已删除VK主页的聚合快照

主页还有 旧LovePlanet账号，用户名flowerboy Google账号头像，MirTesen主页头像，黑鸟不过多展示

泄漏数据显示，他自2018年起供职于俄罗斯紧急情况部信息分析中心IAC EMERCOM，自2020年起供职于Yutek-NN。Listarov在IAC EMERCOM任职期间，该中心副主任是Denis Obrezko，Obrezko为前FSB官员，后因网络间谍活动被美国起诉。

俄罗斯社会基金泄漏记录显示，至少到2025年7月，Listarov已在Yutek-NN任信息系统专家，同一时期Obrezko也在Yutek-NN任信息安全副主任。基于任职重叠，调查方判断两人很可能相识，Obrezko的高级别职务表明其可能是Listarov的主管。

Listarov的一个手机号在他人通讯录中显示为из АП Борис，意为来自AP的Boris。俄语语境中АП（AP）是总统行政办公室Администрация Президента的常用缩写。

# 另一波威胁邮件活动

在虚假智能投票邮件活动前六个月，同一泄漏数据库就被用于一波夹带威胁和个人信息的大规模邮件活动。库内人员先收到一封含数据库本身的邮件，之后又收到一封含个人信息的邮件，后者推测是把泄漏邮箱与公开泄漏数据关联后获得。

部分邮件的收件人显示名包含evilsocks.dev，调查方据此假设同一行为者可能参与其中，对该活动一并展开追踪。邮件发自navalnyfail[.]ru和navalnyfail[.]online，公开WHOIS记录带出更多基础设施。

调研中发现Current Time记者Andrei Soshnikov已对该活动做过详细调查，调查方使用历史WHOIS数据独立验证并复现了其结论。WHOIS溯源找到大量与疑似钓鱼、仿冒活动关联的域名，但除原始evilsocks.dev别名外，没有导向新的身份识别。

Current Time指出一个细节，归属同一行为者的两个域名zasekin[.]press和zasekin[.]space于2021年2月注册，用于仿冒萨马拉本地媒体Zasekin。Zasekin所有者Dmitry Loboyko在接受采访时称，这些域名的注册时间与针对Zasekin的DDoS攻击、以及利用Zasekin合法邮件服务器（推测已被攻陷）发送赞扬Navalny邮件的大规模邮件活动大致同期，表面目的是激起地方当局和警方的政治压力乃至可能的起诉。Loboyko认为这些攻击可能由Mikhail Dudin协助，Dudin是萨马拉FSB前雇员Seleznev在Princip Prava公司的前商业伙伴，但Loboyko本人没有支持该关联的直接证据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDquiaZadCkSGlKC7qab14a18IKblliaMw7iaeU3fY9flmshXSfXxDYAoDmUjwm1MPF0libAlBv9uv9ZXjwOcpwYvECdZrGmG1z2WdI/640?wx_fmt=png)

图18 2021年4月发出的威胁邮件

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDricAicwGIbyjOJP2ImvG1GKBDqnILtpOuWS5bohKmbMrhjfas94eLLOlSSqfLuhF2gJhQof0ApCIoHgc3cJhX6LXUUdFG4vL9Cc/640?wx_fmt=png)

图19 4月活动关联基础设施（Current Time发现，调查方复核绘制）

# 表格元数据里的另一个人：Vyacheslav Zubkov

在追溯free[.]navalny[.]com泄漏数据分发时，Current Time把XSS论坛用户scs识别为针对Navalny支持者泄漏数据库的核心来源。该用户在论坛发布29个数据集，其中28个与Navalny相关组织或支持者有关，一条被删帖中scs承认用其他来源信息补充泄漏数据。唯一与Navalny无关的数据集属于陶里亚蒂一家物业公司，与其他文件不同，它以Excel表格而非CSV分发。

表格元数据显示，文件由名为ckfdf的用户创建，之后由Sin Bit编辑。Current Time把这两个别名追溯到Vyacheslav Zubkov，他是萨马拉州陶里亚蒂人，曾单独或组合使用ckfdf、Sin Bit注册邮箱以及社媒、游戏平台账号。调查方独立验证了两个别名与Zubkov的关联，印证Current Time的识别结论。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoDtqyolhcDHg978FhxyTUAcZl82d8qBCiamwofibaS4lCfuGEObYlVZ0uFRb00O2wtn4vUvYsl5CZmqNOZnhwrZDbP4QhZLplibo/640?wx_fmt=png)

图20 泄漏Excel表格的元数据（原始记录界面）

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDowu7Jtfk5cFAyZibWSNQsY8jhzzq1F6WicRUH9qzbDCLia6YLCo1loXPl5BhicK5dicdf9yhXDOLo0xXf2png9T2RJG3PEoM7SWX7A/640?wx_fmt=png)

图21 元数据译文对照

Vyacheslav Zubkov（Зубков Вячеслав Дмитриевич），1996年12月1日出生，陶里亚蒂人，距萨马拉80公里，现居莫斯科。调查方找到其多个社媒主页，包括一个旧VK账号，VK...