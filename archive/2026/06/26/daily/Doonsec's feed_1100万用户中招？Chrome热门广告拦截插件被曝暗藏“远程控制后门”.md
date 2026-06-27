---
title: 1100万用户中招？Chrome热门广告拦截插件被曝暗藏“远程控制后门”
url: https://mp.weixin.qq.com/s/PffSzJ24j1Kh39I_LpHmdw
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:47:40.620054
---

# 1100万用户中招？Chrome热门广告拦截插件被曝暗藏“远程控制后门”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K31weib7KtichT9qUprWx0lX6ibOBGDZJNcLInpXg9Dr3n9soXrAraibC101brJUuOtDJn6HBk0LCcYav95UvnTYmsa1SVXRJIUCRA/0?wx_fmt=jpeg)

# 1100万用户中招？Chrome热门广告拦截插件被曝暗藏“远程控制后门”

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你手机或电脑上安装的Chrome广告拦截插件，可能正在成为黑客窃取你银行账户、工作邮箱和企业内网数据的“特洛伊木马”。

近日，企业浏览器安全公司Island发布了一份重磅安全报告。报告指出，一款名为 “Adblock for YouTube” 的Chrome扩展程序，虽然表面上只是一个普通的YouTube广告拦截工具，但其代码中竟然暗藏着**可被远程激活的任意JavaScript代码执行能力。**

更令人不寒而栗的是——激活这个“后门”甚至不需要更新插件、不需要通过Chrome应用商店审核、也不会给用户任何可见的提示。只需开发者在其服务器上轻轻改动一个配置，1100万台浏览器就可能在一夜之间沦为攻击者的提款机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0WCMblUXBGIQlcpDEpUMYA6ibkNlFoEicFHGgP4rsJgQjPzdqMNp8B3bXFZ6XewWR9zPaTicuFRg6Sya5KzsloUSGhjLAvSlApxU/640?wx_fmt=png&from=appmsg)

**披着羊皮的“狼”：表面屏蔽广告，背后随时可控**

“Adblock for YouTube”并非无名小卒。自2014年上架Chrome应用商店以来，这款插件已累计超过1100万次安装，拥有37.4万条评价和4.4星的高分，在Chrome商店数十万款扩展中综合排名高居第31位。它还获得了Chrome官方颁发的 “Featured”徽章。

然而，Island的安全研究人员Oleg Zaytsev和Shachar Gritzman在深入分析后发现，这款插件在正常功能之外，内置了一套完整的远程脚本注入架构。

具体来说，该插件每隔24小时就会从外部服务器获取一次配置。除了正常的广告拦截规则外，服务器返回的数据中还包含一个名为 “scriptletsRules” 的字段。该字段可以指定插件内置的某个JavaScript函数以什么参数执行——而其中一个名为“trusted-create-element” 的脚本，可以在当前网页中\*\*创建任意<script>标签并注入任意JavaScript代码。

一旦该功能被激活，注入的代码将与网页本身拥有同等的权限——可以读取页面内容、窃取表单数据、劫持登录会话、模拟用户操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0P8qxu6kqZAQMmR79RVZnmGR0boxhnlwYHmcU3P8ngLD68xLz3gD9QQKb7IxKxSGvGOoRN21ia1vzy6FGnDWUdTCkQ5WeK7TO8/640?wx_fmt=png&from=appmsg)

**致命的权限漏洞：说是“仅限YouTube”，实则跑遍全网**

更令人担忧的是，这款插件声称只拦截YouTube广告，但其在Chrome商店声明的权限范围却是“`<all\_urls>`”——即用户访问的所有网站。

也就是说，它不仅可以读取YouTube页面，还能读取你的电子邮箱、网上银行、企业SaaS系统、内部管理工具、公司内网等一切你通过浏览器访问的网站。

插件内部虽然有一个检查逻辑，试图判断当前页面是否为YouTube——但这个检查只判断URL字符串中是否包含“youtube.com”字样，而不验证域名、框架来源或播放器上下文。

这意味着，攻击者只需构造一个包含“youtube.com”的钓鱼链接，就能轻松绕过限制。例如：

- www.facebook.com/page?ref=youtube.com

- bank.example.com/search?q=youtube.com

- internal.corp.com/redirect?from=youtube.com

研究人员在概念验证中成功演示了：在用户已登录的Salesforce会话中打开一个包含“youtube.com”参数的链接，插件便读取了账户数据并回传至模拟服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0MD8SCU8SwujufMvdoweWwAR8QeGsemBgk7ibYa94HxmEmfpjDg1U15Bjs02o3Bvzm7TBQwNribM1J3XwBicvSgmtPpiahtfFGKicA/640?wx_fmt=png&from=appmsg)

**劣迹斑斑的“前科”：曾植入广告SDK，关联插件已被下架**

报告显示，“Adblock for YouTube”在2018年曾更换过所有权。早期版本曾被发现在代码中植入了名为 “Unistream SDK”的广告注入软件开发工具包——一个本应屏蔽广告的工具，却在向用户页面强行插入广告。该SDK直到2024年6月才被移除。

更值得注意的是，与该插件出自同一开发者或同一生态体系的另外三款广告拦截扩展——“Adblock for Chrome”、“Adblock for You”和“AdBlock Suite” ——已因恶意软件问题被Chrome应用商店下架。

Island的研究人员强调：“问题不在于某一行可疑的代码，而在于多重因素的叠加——一个拥有千万级安装量的扩展具备全网站访问权限、一条远程可控的注入路径、过往的广告注入前科、重大的所有权和代码变更历史，以及多个已被下架的关联插件。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0Kc1jBXB22PJqic5bwGLZkzo1VvlhOOscRfEMfALVeuBRnxT7SIZePZyOU7RbH9gXCdJ4ZFsaqjFnMj0wbAZSFZ3HAgNUbpN90/640?wx_fmt=png&from=appmsg)

**是“沉睡”而非“缺席”：一颗随时可能引爆的定时炸弹**

截至目前，尚未发现攻击者利用这一能力向用户分发恶意代码的实际案例。

坏消息是，这一能力只是“沉睡”，并非“不存在” 。

“激活它只需要一次服务器端配置变更，不需要更新插件，不需要商店审核，用户也看不到任何变化。 ”研究人员警告道。

对于已经安装了该插件的1100万用户来说，这无异于一颗随时可能被远程引爆的定时炸弹。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2L9YjzFBt7iajauG32w3LENlho142NPSlicD2WniaFcYpdeI52rHOh0g3Mlhubf2iawxoiaxVjmtRPTrulu7Sic90jCqBa5GL5DHoIM/640?wx_fmt=png&from=appmsg)

**安全建议：立即自查，果断卸载**

如果你正在使用Chrome浏览器，请立即按以下步骤检查：

1. 在地址栏输入 chrome://extensions 并回车

2. 开启右上角的 “开发者模式”

3. 查看已安装扩展的ID

如果你的扩展列表中出现了 cmedhionkhpnakcndndgjdbohmhepckk 这个ID，说明你正在使用这款存在风险的“Adblock for YouTube”插件——建议立即卸载。

需要提醒的是，Chrome应用商店中存在多款名称相似的广告拦截插件。请务必核对扩展ID，而不要仅凭名称判断。

广告拦截插件因其功能特性，往往被用户和商店审核者“网开一面”，授予比普通扩展更广泛的权限。然而，正是这种“信任的惯性”，让恶意开发者有了可乘之机。

资讯来源：The Hacker News、Island Security Blog、Gigazine、Boannews、Korben、TechNadu

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2L4Biag91BOymErrgXNl6yDMTUYT9Vr9b4YmqNDoycrIczqV1oRVygliaWkKIhBTRZXzntIHiaID9iaSVicJc6c7H5hAoEmUPTM6e4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K0GzlIZaFe8mskP1F4uCtciaJLVL2Rzb5lqmuoJy7TJQcW7LWYrjZqOnu3nHGW18gtGbX4Q21hlaD1eBG4uwTWEDcPlm60tLdzE/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K01LibnpbjF2tgKMEErtUccnibuVWk6FMliaiauZoLJic9N8xb3CYxQFx4h7KU2rFC3mR02GWbcPmRY5fPZib59TehF2CjiaLUwebPtpI/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K0w3fu1y5mcVNKU5Xsyoau2DvomB2djZYc1iaPbgKRfSbGCT9bfPAzA5vqwfr3aGK7QjV2W02Ryiabx3mUsJMw5Jtz8ibOI7BKbDQ/640?wx_fmt=gif&from=appmsg)

**球在看**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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