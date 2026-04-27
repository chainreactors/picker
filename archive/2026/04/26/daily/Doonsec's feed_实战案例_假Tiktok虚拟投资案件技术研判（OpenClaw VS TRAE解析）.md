---
title: 实战案例:假Tiktok虚拟投资案件技术研判（OpenClaw VS TRAE解析）
url: https://mp.weixin.qq.com/s/TGYNZumfVTuIdN_1F-dIzA
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:03:20.445069
---

# 实战案例:假Tiktok虚拟投资案件技术研判（OpenClaw VS TRAE解析）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/b34oV9VTkcGYCHzwha8QxK1OW9E6tbYQJczS2omNcu2OKhNhoGic4RnxROOZvgeRraTeyKoX7fjgL7k01a5qBibE2IEOVXX0jq6KeJl2f5s0o/0?wx_fmt=jpeg)

# 实战案例:假Tiktok虚拟投资案件技术研判（OpenClaw VS TRAE解析）

原创

小谢
小谢

小谢取证

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字“小谢取证”一起玩耍

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/b34oV9VTkcGWXxcbdcbwD2sHKzmfEJnzTLzC6IFTAmH2cfPVoMQce6A7sia3H5icicLhJgOeib6OE24ZLB5v5hGgQibjPdHgf98kicI2RILHvfq0g/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFuK99RxictiavoXCjyVor9RKKxZWWTQ5LXLxlZUauUJsGL428uscoZW3ibbmXpfCveYy8p9YuUvZ3MMIQTC7cb6yZnC4Ckh3kPbE/640?wx_fmt=png&from=appmsg)

  在新历26年的年初碰到一个实际案件的场景：
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFibpzGyVibADNiaYNqyDFtddq7xrEUoY1pRiblYEAFfsRKqAANgkQAPjSGVQ3f9LfJ0cibdTe16IGcntr9EDp5ibCKpTribdwoTlGr2U/640?wx_fmt=png)

  搜索了相关一下报道，确实有不少受害者被假的Tiktok诈骗的报道。而且几起案件被骗的金额还比较大。报道都是防范此类的诈骗，但缺少对其进行技术分析的文章。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcET3qjLzPAtz5TUMeB8VTgD01DLVFDtrK0Z4MU99hluOw9nOZzUcbtHDJ4xpLjjtcmSlcNrwZT2HicN2ETzWZd8UKBbrhKY1waQ/640?wx_fmt=png)

  包括这周五在山东授课，也有取证专家刚刚碰到，案件还在侦办当中，与小谢共同探讨如何溯源。看来从去年开始到今年，这类案件还一直频繁发生。
  刚开始看到，一想到如果去判断一个APK是不是官方的Toktok，只要在官网上下载的apk与假的TikTok的哈希值进行比对，肯定是不同的，但是需求是要看看假的TikTok里面有没有夹带私货，到底被改了哪些地方。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGqyYTAGTfUGau5lrovJs0sez0JDgXCGwxBuib5l8TVZmV8RIwqpYPQSib0htibkfD7q1TqJiciazMQydUODgKYs5yd6R1KyE1RcRjo/640?wx_fmt=png)

  但是，疑惑的是假的TikTok和官网正版的TikTok包名和签名证书一致，甚至连文件大小是一致的。我们说，一般打包一个APK，需要包名，但包名又具有唯一性，两个不一样的APK不可能一致呀。那会不会就是他们在官方的TikTok上做了手脚。待会我们可以看看OpenClaw和TRAE给我们的分析。他们这样做的主要目的是过软件商店和手机的白名单，这样受害者在下载假的TikTok的时候将没有任何的风险提示。

  在电子数据司法鉴定中，有一个项目为软件相似性鉴定，主要用到的以下两个工具进行相似性的检验（如果需要这两个工具，在文末有）。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGHrAb57a7XL0MmGVRQDQiaGTic91FvJgjLIx3CWDibckeAuXlcu8yapNQFlmc5ZtVMic4ZWlmbPWc26GPIiaUQoPlzN7lkW6PEAjJY/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGt4Yicg2w9whEjRQQQyf1sayKTZwMpiciapfy4Nl5R1aSpxxbfGauPnEOLmoXKCcNokhzhNbOTBrDJa6QLwe1WtWvibW9qG4Ca600/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFApLTuAz2vPzXZOjQLccSficsibia1iagqtUt9VdiabL9efSSQIzrC7GQfmuoBWxvgJ9EmrFs1FCVbXRztAhsfbBsxAA0JXEm28M1I/640?wx_fmt=png&from=appmsg)

  但是对于没有逆向基础的人来说是非常不友好的，首先不知道如何反编译，对APK文件如何处理，其次即使是反编译成功之后，源码也不懂得看。

  所以基于这个痛点，这篇文章就引入了OpenClaw和TRAE来帮我们解析这个APK，通过可视化界面与自然语言交互，让我们零基础的一线侦办人员也能快速定位代码的修改点且能够溯源到假的TikTok所通联的服务器地址。
  这篇文章就以OpenClaw和TRAE分别对这个假TikTok进行反编译分析，来一场PK，看谁的效果会更好些。

一、先来展示OpenClaw的部分。

  具体的搭建文章可以参考：

   [OpenClaw在警务当中的应用 打造你的警虾！（附详细搭建流程）](https://mp.weixin.qq.com/s?__biz=Mzg4MTcyMTc5Nw==&mid=2247491213&idx=1&sn=1666bb3690398b6be479bfe7ea555c29&scene=21#wechat_redirect)
  如果大家觉得这样搭建还是挺麻烦的，也可以在评论区留言“5分钟搭建龙虾”，如果大家比较需要这种比较简单无门槛的搭建，下期小谢可以出一期“5分钟快速养活一只OpenClaw”，纯图形化界面安装在Windows计算机上且无需任何的命令安装。

实操过程：
  1.先启动OpenClaw：openclaw gateway run
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEicEB5K9Go08JIbQemwY9Iu72YPLibHneicaLlRDUFNRX4q5FU1bicLia5wyJcrrzhQm1nYJtkqccXzXpDLicuLHYbGLct3XFzLaEB4/640?wx_fmt=png)

  2.在飞书界面上传APK文件，让他帮我们分析这个APK，为了公平性，和TRAE进行对比，我们输入相同的提示词给他：

  帮我解析TikTok.apk，这是一个假的Tiktok，我的目标是找出这个假的Tiktok的apk文件反编译后修改的代码在哪里，为什么和官方的tiktok的包名和证书签名是一致的，实现的技术是什么，核心代码在哪里体现。同时也要溯源这个假的Tiktok的通联地址是什么或者其他能够调证的值。

  不过很遗憾，在飞书上的OpenClaw给了我这样一个回答：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHnm0fCUDVAQLC30a3jjOD6pTrugRR3MwjP7JyOClChicZyoCfo3aGLLet4PDxQxPsDoxDt0TIJNkDftka7qTMcKtJ2kGOPyfXQ/640?wx_fmt=png)

  有可能是APK文件过大，毕竟这个假的TikTok有几百M的大小。也有可能飞书在上传文件的大小做了一些限制。
  问了一下师兄，也是碰到这样的问题，果断切换TRAE。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGZeUfrtH86grveG9mOAE8pkjbjTEShvx0iaMwSMsEEeVngkljOqwoFYhwD44wPWd8SatVoeXOFcGUyDbDn0rXD6BP7HnE4ich1g/640?wx_fmt=png)

二、再来展示TRAE的部分。

  Trae这边可以不用像之前装MCP Sever，也可以参考之前装MCP Server的文章：

[电子数据取证之使用Trae进行APP逆向分析](https://mp.weixin.qq.com/s?__biz=Mzg4MTcyMTc5Nw==&mid=2247490159&idx=1&sn=8e5dac59dfe6a8edbadc08c970ea2570&scene=21#wechat_redirect)

  但这次需要添加一些apk逆向专属的技能即可。如何给TRAE添加技能可以参考文章：

[给Trae装上skills，让Trae自动取证服务器的数据！](https://mp.weixin.qq.com/s?__biz=Mzg4MTcyMTc5Nw==&mid=2247491386&idx=1&sn=4a6d3c0bed239a1a185cada8716ff42b&scene=21#wechat_redirect)
  只需要在.trae的文件夹中添加以下几个skills即可（如果需要APK逆向的SKILLS技能，在文末有）：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcH2qj4TGtndj4AM4fanibsMZrCN7GXz8QCc4DRibhYAVoicI5icdjPS1TmV6401n2NSpn51xpiccqViaE4PX6b7sic6vziavnVb9tYOONU/640?wx_fmt=png&from=appmsg)

  按照上述文章教程添加上述的skills好后，我们使用国际版的TRAE，用的是GPT5.4的模型来问他。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFJmCMXkFZRlY6sKA8cqxoWPKXoTTkbHD4fk0zfKB0ltzXImLCWQnpoV0P8hTxfaKRMO05226V7A7FOSnzTRgibPNxjWeWSiaJx4/640?wx_fmt=png)

我们可以看到TRAE配合GPT5.4和SKILLS将它分为了五个任务:

1.定位并确认 TikTok.apk 样本、基础元数据与可用分析入口

2.分析 Manifest、签名与包名伪装机制，判断为何与官方看似一致

3.定位被修改的核心代码、主要实现技术与恶意模块

4.提取通联地址、域名、IP、证书与其他可调证 IOC

5.整理具备证据链的取证结论与后续调证建议

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHB15BY5FR6nUFLFIpm6e9k2jMa1BOL90ffrbJ1f68NfRWxqicm08Zt4kgUByy4n1Bq2jN5sHAJib5Siby2NOeIMK1qPw0fyRUyic4/640?wx_fmt=png)

  再测评一下完成的时间共花了13分钟，可以说所花费的时间比一位专业的APP逆向专家的时间还要快。所以我们当前还是要善于利用和学会运用AI解决我们工作和生活当中的一些问题，提高工作效率和生活质量，ALL IN AI！

以下为所花费时间的展示:
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcH8jgN0nDiaHKxiaWdIBXibBAMuo5PPMTrQQT9yBgT1WjyDQzia0SraBFsFzcT6nL5ceoNmiaKUruTlpKN4395URI6bI0x7nvnyaicjA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHUZdUNMW55GfyvbhTyzR0f1PK0ercOtablm258MufeYPPhAnsPD4rpJm6hxTbZygHXibb5LMGtLdyHMccefzvpTbn4MgicFFDPY/640?wx_fmt=png)

最后呈现以一下来自TRAE的解析报告：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGm7D0ib8kp7nnMQHKT6ZARTUaa8ibFdbHRl1JvuZxU37ebMYNySxS4d9ia9FOZfQb79WsZbCll7910P9OxOLNN9nbpnbBicaT8V7o/640?wx_fmt=png&from=appmsg)

  甚至，我们可以让TRAE帮我们落查反编译出来的通联服务器地址：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHOdt5sibSzeWWLCL5RHYKEelgkB3nwNQC833Il4sF7gT1784JzfF17pAqpxYBmKboKfiam1O8YSI0d9EegyrUcPB6EXLjOQy2yc/640?wx_fmt=png)

  最后出来的结论：
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcF0DgABAAdYp8PjMRHV4B0T9sLbrHMTMaibXJhHH40aWwvsnyyymswqYoMOUuAM849PhjJlMtUsmMNfmsNtuXlHy1q042WzDHGI/640?wx_fmt=png)

  我们可以继续让TRAE帮我们溯源，看能否挖掘到更多的线索。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcG2ib4XicuTStHxGglPSptvDicml0ovh6WvokmXKV4WXEJd0XPdLQqgunYicAwsXbC5rmpIRr0Qnh8wdKbPUoib26x4U3IicHiawlhJ5A/640?wx_fmt=png)

  给出了下一步可以尝试做的方法：
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFFicuaSUE8qwicvhRiabKQrodzFzWXMIWsEicIK8xyUk2Me7Zicibsb3bz5juZw3XXSneGmY7srbNUMAaHKK1dOWJshY9UZFlZrtkX4/640?wx_fmt=png)

 TRAE最后给出的总结及预防被骗的方法：

\*\*为什么很多人会被骗\*\*

- 它不是一个“全新陌生诈骗 App”，而是伪装成大家熟悉的 `TikTok`，界面、入口、账号信息都看起来很真，受害者天然会放松警惕。

- 这个样本会在正常 `TikTok` 页面里偷偷加出“店铺中心、商品、订单”这类按钮，让人误以为这是平台官方新增功能，不像普通诈骗页面那么突兀。

- 它会直接读取当前登录的 TikTok 账号信息，比如昵称、UID、头像，再带到假商城页面里，页面因此显得“和自己账号绑定了”，信任感很强。

- 真正的商城内容不是写死在 App 里，而是由远端服务器动态下发。诈骗方可以随时改页面、改话术、改收款方式、改客服链接，今天是刷单，明天就能变成充值返利、跨境电商代运营、提现解冻。

- 页面很可能把客服、邀请码、钱包地址、订单状态这些内容都放在远端 H5 里，再配合 `WhatsApp`、`Telegram` 外跳，把受害者迅速带离正规平台环境，进入骗子可控的话术场。

- 对普通用户来说，它“像真 App、像真商城、像真客服、像真订单”，被骗不是因为受害者笨，而是因为这个 App 专门在伪造“官方感”和“可信感”。

\*\*它最容易骗到人的几个点\*\*

- `熟悉感`：看起来就是 TikTok，不像陌生博彩或贷款软件。

- `账号绑定感`：页面里出现自己的头像、昵称、ID，容易让人觉得“这一定是真的”。

- `官方功能感`：按钮直接长在原页面里，像平台内部商城，不像广告跳转。

- `收益诱导`：常见套路是“开店赚钱、代运营分成、充值返利、做任务提现吗”，先给小利，再诱导大额转账。

- `客服施压`：通过 Telegram、WhatsApp 一对一催促，制造“名额有限、订单超时、账户冻结、必须补单/解冻”的紧迫感。

- `加密货币收款`：一旦让你转 `USDT` 或扫链上地址，追回难度会非常高。

\*\*普通人怎么预防被骗\*\*

- 不要因为图标、包名、页面像官方，就默认它是真的。`像 TikTok` 不等于 `真 TikTok`。

- 只从官方应用商店或官网安装 App，不装别人发来的安装包，不点“企业包”“内测包”“特殊版本”。

- 任何平台如果突然出现“做任务、代运营、充值返利、垫资抢单、解冻提现”，先当诈骗看。

- 只要对方要求你转 `USDT`、虚拟币、境外卡、个人二维码、陌生对公账户，风险都极高。

- 只要对方把你往 `WhatsApp`、`Telegram`、私人聊天群里引导，脱离平台内沟通，就要立刻警惕。

- 不相信“先小额返利、后大额投入”的模式。诈骗最常见的就是先给甜头，再逐步加码。

- 遇到“账户冻结、信用分不足、缴保证金、补单解锁、提现前先充值”，基本可以直接判定为诈骗。

- 对家人尤其是年轻兼职人群、宝妈、待业者和老年人，要重点提醒“刷单、电商代运营、海外商城、短视频带货代开店”这些高发话术。

\*\*如果已经接触过这类 App\*\*

- 立刻停止转账，不再继续补钱“解冻”。

- 立刻卸载可疑 App，并修改 TikTok、邮箱、手机号、支付工具密码。

- 检查手机里是否还有来源不明的 App、辅助功能授权、悬浮窗权限、无障碍权限。

- 保留证据：安装包、聊天记录、转账记录、钱包地址、收款账号、客服账号、网页链接、截图。

- 如果涉及虚拟币，尽快记录 `钱包地址、交易哈希、时间、金额、平台账号`，这对后续报案很关键。

- 尽快报警，并同步联系银行、交易所、平台客服做冻结或风险登记。

\*\*一句话总结\*\*

- 这个 App 能骗到很多人，不是靠“技术炫酷”，而是靠“伪装成你信任的平台 + 用你的真实账号信息包装假商城 + 把你引到骗子控制的客服和收款链路里”。

- 最有效的预防方法，就是记住一个原则：`凡是让你离开正规平台、去私聊、去充值、去转 USDT、去补单解冻的，默认就是诈骗。`

  本文章当中所有...