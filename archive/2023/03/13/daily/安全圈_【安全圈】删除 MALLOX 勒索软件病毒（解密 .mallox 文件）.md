---
title: 【安全圈】删除 MALLOX 勒索软件病毒（解密 .mallox 文件）
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031340&idx=2&sn=41e7044d4c411a2e716463f69d7fc4f7&chksm=f36fe52cc4186c3a2f7354656a4646628d239bd3430f43d64a2fcbd82307dd19d6b19d80fd41&scene=58&subscene=0#rd
source: 安全圈
date: 2023-03-13
fetch_date: 2025-10-04T09:25:36.932568
---

# 【安全圈】删除 MALLOX 勒索软件病毒（解密 .mallox 文件）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicIwMQ1S6mAj6gyAtBxjEWc4nDh23Gk3ibwsPIvPhMAfgibLhFpqcjN8AQ/0?wx_fmt=jpeg)

# 【安全圈】删除 MALLOX 勒索软件病毒（解密 .mallox 文件）

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg)

**关键词**

勒索软件

**Mallox 勒索软件说明**

**Mallox 勒索软件（也称为 FARGO 或 TargetCompany）是一种高度活跃的分布式计算机病毒**，主要针对未受保护的 MS-SQL 服务器，但也可以通过恶意电子邮件附件感染计算机。该恶意软件的主要目标是加密目标系统上的所有文件，**将 .mallox 扩展名附加**到每个文件名，并删除要求支付赎金的注释。该勒索软件有多个版本，勒索字条的名称各不相同。我们分析过的一些示例删除了名为**RECOVERY INFORMATION.txt 或 FILE RECOVERY.txt**的注释。

为了说明文件在计算机攻击期间如何重命名，请参见以下示例：**以前名为 1.jpg、2.png 和 3.docx 的文件将重命名为 1.jpg.mallox、2.png.mallox、3.docx.mallox**.

该恶意软件还运行额外的进程来停止各种服务和程序，以便加密与其关联的文件。这个勒索软件的另一个值得注意的细节是它会停止与 GPS 相关的程序，这可能意味着该病毒可能以从事关键基础设施部门工作的组织为目标。

该勒索软件还会窃取有关计算机的信息并将其发送到其命令与控制服务器。该恶意软件的早期版本还声称有一个数据泄露网站，犯罪分子会在该网站上上传受害公司的名称，并威胁如果受害者拒绝支付赎金，就会发布窃取的数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicpH51Viaq1ibEYoGpdejoicu2R2UnWvQWzxyAFK9zJBo9Rc3G4CNruYYjA/640?wx_fmt=jpeg)

赎金记录概述

恢复信息.txt

Mallox 勒索软件的最新样本释放了一个名为 RECOVERY INFORMATION.TXT 的勒索字条，其中包含有关如何从网络犯罪分子那里获取解密工具的信息。该注释指示向提供的电子邮件地址发送电子邮件：**mallox.israel@mailfence.com****或 mallox@tutanota.com**。有趣的是， BOZON ransomware ransom note中也使用了后者的电子邮件。

该说明随后解释说，计算机用户在通过电子邮件与犯罪分子联系时应包括赎金说明中提供的个人 ID 字符串以及一些加密文件。他们承诺对部分文件进行解密，并告知全数据解密服务的价格。但是，该说明提到不应发送任何有价值的文件进行测试解密。

文件恢复.txt

其他 Mallox 勒索软件样本丢弃了**FILE RECOVERY.txt**文件，其中包含的信息略有不同。与前面的示例不同，此赎金票据要求安装 TOR 浏览器并通过提供的 .onion 网站联系网络犯罪分子。为了登录门户，用户必须指定赎金票据中提供的私钥。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicFdTclF1lHnyVicYY76rNMEeFFaaWL8WahKzJqjqo0U0DJx1a5KWaEXg/640?wx_fmt=jpeg)

该网站包含一个聊天窗口和信息面板，其中包括客户信息（受害者 ID、文件重量、硬盘大小、博客链接、测试解密状态）、付款详情（解密工具价格、支付金额和日期）最后一笔交易）。最后，还有一个空间可以直接链接到要被网络罪犯解密的文件，同时还有一个文件大小不能超过 3MB 的通知。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevic3MicP4aZ8Ax8BicddrJI82LAnicYcRnkUiavXEuIGziaavWeucDUje3icULg/640?wx_fmt=jpeg)

我们的研究表明，犯罪分子通常会为 Mallox 文件解密工具索要 1000 美元、2000 美元或更多的钱。如**果您已受到此恶意软件的影响，我们强烈建议您使用INTEGO Antivirus等**专业软件移除 MALLOX 勒索软件病毒。请随意使用文章下方提供的删除说明作为指导。此外，您可能需要下载R**ESTORO，**这是修复 Windows 操作系统文件病毒损坏的好工具。

**M****ALLOX 勒索软件病毒清除指南**

##### 步骤 1. 以带网络连接的安全模式启动 Windows

在尝试删除病毒之前，您必须**以带网络连接的安全模式**启动计算机。首先，关闭您的电脑。然后按电源按钮再次启动它并立即开始以 1 秒的间隔重复按键盘上的F8按钮。这将启动“高级启动选项”菜单。

1. 使用键盘上的箭头键向下导航到“带网络连接的安全模式”选项，然后按Enter 键。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevickR37oWKs1MVuFKShbu9jcvibMOtTLic9qnfJB4wyThpvsic5nwbfjvKjw/640?wx_fmt=jpeg)

##### 步骤 2. 删除与病毒相关的文件

现在，您可以搜索并删除 MALLOX 勒索软件病毒文件。很难识别属于勒索软件病毒的文件和注册表项，此外，恶意软件创建者往往会反复重命名和更改它们。因此，卸载此类计算机病毒的最简单方法是使用可靠的恶意软件清除程序。此外，我们建议尝试结合使用**INTEGO Antivirus**（删除恶意软件并实时保护您的 PC）和**RESTORO**（修复病毒对 Windows 操作系统文件造成的损坏）

**方法二：使用系统还原**

1. 关闭您的电脑。按电源按钮再次启动它，并立即开始以 1 秒的间隔重复按键盘上的F8按钮。您将看到高级启动选项菜单。
2. 使用键盘上的箭头键，向下导航到带命令提示符选项的安全模式，然后按Enter 键。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevic0WCbIHyic15Ggxcsjwjx153myAUvIibNQqg9gxtnRt5DdJ9UoGNu5G3g/640?wx_fmt=jpeg)

##### 骤 2. 启动系统还原过程

1. 等到系统加载并出现命令提示符。
2. 键入cd restore并按Enter，然后键入rstrui.exe并按Enter。或者您可以在命令提示符中键入%systemroot%system32restorerstrui.exe并按Enter。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicTRicTrhd5syEtkFCB6aMW36g2tJonj4MJg2KPpQt0yDtGmRKse1WgYg/640?wx_fmt=jpeg)

1. 这将启动系统还原窗口。单击下一步，然后选择过去创建的系统还原点。选择一个在勒索软件感染之前创建的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicIboL3rm3utOicoRoSxNZUkGg5GJjxcoOGMfdYgx4DBxtzllDC61SBFA/640?wx_fmt=jpeg)

1. 单击系统还原过程。

还原系统后，我们建议使用防病毒或反恶意软件扫描系统。在大多数情况下，不会留下任何恶意软件，但仔细检查也无妨。此外，我们强烈建议您查看我们的专家提供的勒索软件预防指南，以保护您的 PC 将来免受类似病毒的侵害。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFHibf3ZAicuClNcV7HhVGBuOIWU8T01j8cLWMOpR8icprkLkdSPgjALNzA/640?wx_fmt=jpeg)

[【安全圈】“帮信罪”正式成为我国第三大罪名，大量学生涉案](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=1&sn=fff4bbbf1ca96280bf5794293e1e3288&chksm=f36fe558c4186c4ee4c48bcd624b01cf312a57f6c3dab75118e4936afbf05c45ae61a7361b79&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFnib6B33c71phvzw56Tb9sibaPu7GMicI0yJSoYKSXQ6y5etN704yXfSibQ/640?wx_fmt=jpeg)

[【安全圈】可绕过 UAC，微软 Win10 / Win11 系统中发现高危漏洞：可安装执行恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=2&sn=8cb3a0990860352ef0335b43b556dc4b&chksm=f36fe558c4186c4e66969bb745657d7543dc5e5f0a05b8777fbd8612e77288657f8e4fd9521e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFHVD4HNSdHNvdsnjc12fI6FMtBhWK1NfgNvQmhMb2zXRBUDlQZe1Iww/640?wx_fmt=jpeg)

[【安全圈】已对 Linux 服务器发起攻击，针对 Win10 / Win11 的勒索软件 IceFire 出现新变种](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=3&sn=bd432c9dc0e56d5a649853c38afbb35f&chksm=f36fe558c4186c4edb19d958a91a31a116849adfc5c67934ff96a6e0d0723fcde9ef62d1ed70&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFfL4qFa1Wx5XAe7SkFqoqic8Hqv6S3gZTYfIWC9AauDQUVVfZia6kiaR9g/640?wx_fmt=jpeg)

[【安全圈】被指与谷歌形成“双头垄断”，苹果辩称英国监管机构已无权发起调查](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=4&sn=7448fdfd960f1f740ac53593c365dedc&chksm=f36fe558c4186c4e4b69ab3de74151c60ade89dd81141d8b01ad591e326a775787b9db4b3387&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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