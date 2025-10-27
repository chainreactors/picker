---
title: 新型手法｜Telegram 假 Safeguard 骗局
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500978&idx=1&sn=8d502d81ee56971fac26b35e70b49081&chksm=fddeba35caa9332370f3eb036a88298138c4c0b3affab16a89684c8be0ea352075d9efbc6119&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-01-19
fetch_date: 2025-10-06T20:08:57.903939
---

# 新型手法｜Telegram 假 Safeguard 骗局

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZyJfY56xnOhWFIfhic0evH8p6vsVzOibOPFrj7Aqiaocg82gFsBXeq1ricQ/0?wx_fmt=jpeg)

# 新型手法｜Telegram 假 Safeguard 骗局

原创

慢雾安全团队

慢雾科技

近期，我们收到很多受害者的求助信息，均与 Telegram 上的“假 Safeguard”骗局有关。由于许多用户对这类攻击方式不了解，往往在遇到这种骗局时警惕性不够，无论是新手，还是经验丰富的玩家都很可能上当，本文将深入剖析这一骗局的攻击方式，并提供有效的防范建议，帮助用户保护资产免受损失。

###

### **骗局分析**

此类骗局主要分为两种，一种是盗取 Telegram 账号，骗子通过诱导用户输入手机号、验证码，甚至 Two-Step Verification 密码来窃取其 Telegram 账号，另一种是往用户电脑植入木马，也是近期出现较多的手法，本文将重点讨论第二种方式。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZibCtUjNl2tOaaUgZedZ0szOHicwUqqRcC0T0dUxPZcCMUf0gEvykzqNw/640?wx_fmt=png&from=appmsg)

在某些热度较高的代币空投活动中，用户的 FOMO 情绪正上头时，在 Telegram 上看到下图 Channel 界面，肯定就去点击 Tap to verify 了：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZfac6RnIJtAxwugFrial0dYa7GG83IEdiaFFRyLiaXwSZreLuW7WwH49BQ/640?wx_fmt=jpeg&from=appmsg)

点击 Tap to verify 后会打开一个假冒的 Safeguard bot，表面上显示正在进行验证，这个验证窗口极短，给人一种紧迫感，迫使用户继续操作。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZwXYoclv94CMxg474ic4XdKkvxuOCsfmpgQUXUKHcI8ictXibSBibNhoxUQ/640?wx_fmt=jpeg&from=appmsg)

继续点击，结果“假装”显示验证不通过，最终让用户手动验证的提示界面出现了：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZNgG3F5fhQozjfr9VicHFRsq7H1ogH2dNNhL9KGmfLKnCa8udbibpASgA/640?wx_fmt=jpeg&from=appmsg)

骗子很贴心的配置了 Step1, Step2, Step3，此时用户的剪贴板里已经有恶意代码了，只要用户没真的按照这几个 Step 去操作就不会有问题：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZF6SQookME5eYrSdxdpCiaz7OORstaN3kvonOUrcu2LcMJo6XgNDbSNg/640?wx_fmt=png&from=appmsg)

但如果用户乖乖地按照这几个 Step 去操作，电脑就会中病毒。

再举一个例子 —— 攻击者冒充 KOL 并使用恶意机器人进行验证引导运行 Powershell 恶意代码。诈骗者创建假冒 KOL 的 X 账号，然后他们在评论区附上 Telegram 链接，邀请用户加入“独家” Telegram 群组以获得投资信息。例如 @BTW0205 的评论区出现的 Scam account，许多用户会在评论区看到“令人兴奋的消息”：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZfseabQSF4K5aS9rBxemZV8ndyryKoYvHoFicO4jcd1oJWdSkia38cJxA/640?wx_fmt=jpeg&from=appmsg)

然后进入了对应的 Telegram Channel，引导用户验证。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZVViaNpTQhIfyUbN5vEf02RorYlEmbiarQCGvAXvtnwxPFdmgf2s4OXzA/640?wx_fmt=jpeg&from=appmsg)

当用户点击验证时，出现了一个假的 Safeguard，跟上述过程类似，出现了 Step1, Step2, Step3 引导做验证操作。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZMOzToVBZfV7gk0zmGFQ0bIqVCXM4LdmVicMoGugCoeGMwEDxUeGJOag/640?wx_fmt=jpeg&from=appmsg)

此时用户的剪切板已经偷偷地被植入了恶意代码内容。如果用户真的按指南打开了运行框，并 Ctrl + V 把恶意代码内容粘贴进运行框里，此时的状态就如下图，在运行框里并看不到全部内容，一大片空白的前面是 Telegram 字样及恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZOGeljeq0jEIYrMFMnyQVHQFPgOdLXsctdFQpyoouuPfuuTPknQicOdQ/640?wx_fmt=jpeg&from=appmsg)

这些恶意代码通常是 Powershell 指令，执行后会悄无声息地下载更复杂的恶意代码，最终使电脑感染远程控制木马（如 Remcos）。一旦电脑被木马控制，黑客便能远程窃取电脑中的钱包文件、助记词、私钥、密码等敏感信息，甚至进行资产盗窃。（PS. 关于“假 Safeguard” 木马行为可以参考慢雾区白帽 Jose 的分析，指路：https://jose.wang/2025/01/17/%E4%BC%AASafeguard%E7%97%85%E6%AF%92%E5%88%86%E6%9E%90/）

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZpOJib4zdLgqU8CkKwnRwCkwhezJJq1K6aWwDGuicER7ictVRF6Kepf3Uw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZ65FPVTz6mByV43TDQanTzDONjBB57u9TFeMOdjonyLSxltZeRasAWg/640?wx_fmt=jpeg&from=appmsg)

以太坊基金会账号 @ethereumfndn 评论区也曾被这种骗局污染，这种骗局呈现出大范围撒网收割模式。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZXuZcUVvTCEzBLVaRYQOVuHIqqPUk94m0E4LJMiaPWXyIycjhC6Us7eQ/640?wx_fmt=png&from=appmsg)

###

最新的如 Trump 的 X 评论区也被这种骗局污染：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYX9CmacBAlOAibiacEHiaE1j1GyEdzhiawrIYvO7C8pTTwticXyNyic9dSrPX1QQsTRQF4cRWpHYZnS8tg/640?wx_fmt=png&from=appmsg)

### 如果你是手机上打开的，骗局会一步步拿到你的 Telegram 权限，发现及时的话，需要尽快在 Telegram 设置里的 Privacy and Security -> Active sessions -> Terminate all other sessions，然后加上或修改 Two-Step Verification。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZKLxTueM6Nmbqicv7LC2icF9DyK3pFdic7cWk2y5rloXJfnoELTsfqcafw/640?wx_fmt=png&from=appmsg)

如果你不是 Windows 电脑，而是 Mac 电脑，也一样有类似的方式来诱导你电脑中毒。套路类似，当在 Telegram 里出现下图时，你的剪切板已经被偷偷地植入了恶意代码内容。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZKpBjBODFJC5Jk0kxNQlMiaDowlQtibBowica29aiasxCMAjAA2m5icVbjNw/640?wx_fmt=jpeg&from=appmsg)

此时还没出现风险，但如果你按照给出的步骤去做，就会出现下图的后果：

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZbiafiaw0NfTCgGkVUwAGm4f086qX8DJhV6wxuicicrtr8zIhlMDqAHJOCA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZFOZ1f8rF9WySBsLvU2VliaqUYZpHnGD0O9rjnehYuFkMCbmUZvA6JlQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZuTtSeuprluXiafP3BYl4wt1cdbKxxARbXX5LQRRj8dDEibEcpOiaKna4w/640?wx_fmt=jpeg&from=appmsg)

### **MistTrack 分析**

我们选取几个黑客地址，使用链上追踪和反洗钱平台 MistTrack 进行分析。

Solana 黑客地址：

HVJGvGZpREPQZBTScZMBMmVzwiaVNN2MfSWLgeP6CrzV

2v1DUcjyNBerUcYcmjrDZNpxfFuQ2Nj28kZ9mea3T36W

D8TnJAXML7gEzUdGhY5T7aNfQQXxfr8k5huC6s11ea5R

根据 MistTrack 的分析，以上三个黑客地址目前共获利超 120 万美金，包括 SOL 和多个 SPL Token。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZicjGAQ5FnuQbBPPuFzA37dJRX1G5W8Jyf6J9PAu3IibPMZlv2yqnENibQ/640?wx_fmt=png&from=appmsg)

黑客首先会将大部分 SPL Token 兑换为 SOL：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZTJ0YG5KUOLBjLibdBicBia5BaXyBXpkRhcjHKXxGWnflAb9b34ZteWOtw/640?wx_fmt=png&from=appmsg)

再将 SOL 分散转移到多个地址，且黑客地址还与 Binance、Huobi、FixedFloat 平台存在交互：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZ68LUvUPl6lJo6eUu4hzlPfajfVM5K07aJMFrW6ep5jkzIHN309wByQ/640?wx_fmt=png&from=appmsg)

另外，目前地址 HVJGvGZpREPQZBTScZMBMmVzwiaVNN2MfSWLgeP6CrzV 仍有 1,169.73 SOL 和价值超 1 万美金的 Token 余额。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZDwN8MtgKzUokdoU0ic5NMicWMu7JWAj3kjCTQkNOnKBfD7hudFRHjVmw/640?wx_fmt=png&from=appmsg)

我们再分析其中一个 Ethereum 黑客地址 0x21b681c98ebc32a9c6696003fc4050f63bc8b2c6，该地址首笔交易时间为 2025 年 1 月，涉及多条链，目前余额约 13 万美元。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZZYTEIE0Nic9ZzT59hU27BcX9Tmxib5v6Zvq3tBkKtVPfQD9SspZgW8Zg/640?wx_fmt=png&from=appmsg)

该地址将 ETH 转到多个平台如：ChangeNOW, eXch, Cryptomus.com：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZuwgeVZgBDpxTibZXicqw9sZffl35r2Nz5ZHHm6kyE9ibGFs9spibXr3rXjlbbxDBOU9OJNfrEzkNcGw/640?wx_fmt=png&from=appmsg)

**如何防范**

如果你的电脑中招了，需要立即这样做：

1. 这台电脑用过的钱包、资金都及时转移，不要认为扩展钱包带密码就没事；

2. 各个浏览器保存的密码或登陆过的账号，密码或 2FA 都尽可能进行修改；

3. 电脑上的其他账号，如 Telegram 等，能改都改。

你就做最极端假设就行，反正电脑中毒了，你的电脑对于骗子来说就是透明的。所以逆向思维，如果你是骗子，完全控制了一台在 Web3/Crypto 世界活跃的电脑，会做些什么。最后，电脑重要资料备份后，可以重装，但重装后最好安装国际知名的杀毒软件，如 AVG、Bitdefender、Kaspersky 等，全盘杀毒下，处理完毕就问题不大了。

**总结**

假 Safeguard 骗局已经发展成一种成熟的黑客攻击模式，从仿冒评论引流到植入木马病毒，再到窃取资产的全过程都隐蔽且高效。随着攻击手段的日益精细化，用户需要更加警惕网络上的各类诱导性链接和操作步骤，通过提高警觉、加强防护、及时发现并处理潜在威胁，才能有效防范这类骗局的侵害。

**往期回顾**

[MistTrack：区块链安全与合规利器，守护全球用户](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500938&idx=1&sn=f3fbf87c17d8588e73bcd53e3607447e&scene=21#wechat_redirect)

[探讨 Poseidon 延展性攻击，可影响零知识证明应用的安全性](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500936&idx=1&sn=433dc45041abe0603c4c00d7a3db7ced&scene=21#wechat_redirect)

[以小博大 —— UniLend 被黑事件分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500933&idx=1&sn=3f6f83f296e51b2befe35efb58807026&scene=21#wechat_redirect)

[慢雾：演员王星被骗事件相关聊天截图调查](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500907&idx=1&sn=1e629e1d6e96b48b3c5962aadba90a92&scene=21#wechat_redirect)

[2024 区块链安全与反洗钱年度报告解读之反洗钱态势和数据](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500849&idx=1&sn=a4c8a7404ac4c33d52ec625858d74fc6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaa3Th7YiamUUBwq1Iiby9N9lWh3tKP2MVjM6L3UxtTnuUy6iaegsOP2IrqZYsIBM2v3XgC5O2JTbY5g/640?wx_fmt=png&from=appmsg)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.z...