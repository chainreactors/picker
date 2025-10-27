---
title: 【安全圈】App-Bound新工具可绕过谷歌浏览器的 Cookie 加密系统
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065582&idx=3&sn=48b082a9fd35585b2bf9bc37b080418d&chksm=f36e636ec419ea78095e55f2d7ec00e84dd1e8a21a6ed9f100e709fdb4adf38304d960543f1d&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-30
fetch_date: 2025-10-06T18:53:15.172444
---

# 【安全圈】App-Bound新工具可绕过谷歌浏览器的 Cookie 加密系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgSldgotMxiafttMr145kImrvibPqnZBHGwibGkfMJ7Y99bc7PFVpL0W0PayBs47icLrMF0W7hmtMZfXQ/0?wx_fmt=jpeg)

# 【安全圈】App-Bound新工具可绕过谷歌浏览器的 Cookie 加密系统

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgSldgotMxiafttMr145kImrOTSVrllliatX8KUC1VfljUu46cs4eiaM7Afm7yvlNLjl3ZyG3n3pYKtg/640?wx_fmt=jpeg&from=appmsg)

最近，网络安全研究员亚历山大-哈根纳（Alexander Hagenah） 发布了一款工具，该工具名为 “Chrome-App-Bound-Encryption-Decryption ”， 可以绕过谷歌新的应用程序绑定加密 cookie 盗窃防御系统，并从 Chrome 浏览器中提取已保存的凭据。

虽然该工具实现了多个信息窃取者已经在其恶意软件中添加的功能，但它的公开可用性提高了继续在浏览器中存储敏感数据的 Chrome 浏览器用户的风险。

## 谷歌的应用程序绑定加密问题

谷歌在 7 月份推出了应用程序绑定（App-Bound）加密技术（Chrome 127），作为一种新的保护机制，它使用具有系统权限的 Windows 服务对 cookies 进行加密。

其目的是保护敏感信息免受信息窃取恶意软件的攻击，因为恶意软件以登录用户的权限运行，如果不首先获得 SYSTEM 权限，就无法解密窃取的 Cookie，从而可能引起安全软件的警报。

谷歌在 7 月份解释说：由于 App-Bound 服务以系统权限运行，攻击者需要做的不仅仅是诱骗用户运行恶意应用程序。

现在，恶意软件必须获得系统权限，或者向 Chrome 浏览器注入代码，而这是合法软件不应该做的事情。

然而，到了 9 月份，多名信息窃取者找到了绕过新安全功能的方法，并为他们的网络犯罪客户提供了再次从谷歌 Chrome 浏览器中窃取和解密敏感信息的能力。

谷歌当时告诉《BleepingComputer》，信息窃取开发者与谷歌工程师之间的 “猫捉老鼠 ”游戏一直在预料之中，他们从不认为自己的防御机制会刀枪不入。

相反，随着 App-Bound 加密技术的推出，他们希望最终能为逐步建立更完善的系统奠定基础。以下是谷歌当时的回应：

> “正如我们在博客中所说，我们预计这种保护措施将导致攻击者的行为转向更易观察的技术，如注入或内存刮擦。这与我们看到的新行为相吻合。
>
> 我们将继续与操作系统和反病毒软件厂商合作，尝试更可靠地检测这些新型攻击，并不断改进加固防御措施，为用户提供更好的信息窃取保护。- 谷歌发言人

## 旁路工具现已公开

昨天，Hagenah 在 GitHub 上公开了他的 App-Bound 加密旁路工具，并分享了源代码，允许任何人学习和编译该工具。

该工具使用 Chrome 浏览器内部基于 COM 的 IElevator 服务，对存储在 Chrome 浏览器本地状态文件中的 App-Bound 加密密钥进行解密。

该工具提供了一种检索和解密这些密钥的方法，Chrome 浏览器通过 App-Bound Encryption (ABE) 对这些密钥进行保护，以防止未经授权访问 cookie 等安全数据（将来还有可能访问密码和支付信息）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgSldgotMxiafttMr145kImrsicicMVA5qDaXPWJUMtAsVtRLrXTj1icY8aianiark6ANA7FmAhWZr5bUBA/640?wx_fmt=jpeg&from=appmsg)

要使用该工具，用户必须将可执行文件复制到通常位于 C:\Program Files\Google\Chrome\Application 下的 Google Chrome 目录中。该文件夹受保护，因此用户必须首先获得管理员权限才能将可执行文件复制到该文件夹。

不过，这通常很容易实现，因为许多 Windows 用户，尤其是消费者，都使用具有管理权限的账户。

就其对 Chrome 浏览器安全性的实际影响而言，研究人员 g0njxa 告诉 BleepingComputer，Hagenah 的工具展示了一种基本方法，现在大多数信息窃取者已经超越了这种方法，可以从所有版本的谷歌 Chrome 浏览器中窃取 cookies。

eSentire恶意软件分析师Russian Panda也向BleepingComputer证实，Hagenah的方法看起来与谷歌首次在Chrome浏览器中实施App-Bound加密时，信息窃取者所采取的早期绕过方法类似。

Russian Panda 表示，Lumma使用的就是这种方法：通过COM实例化Chrome IElevator接口，访问Chrome的提升服务来解密cookie，但这种方法很容易被发现。

Russian Panda 称他们现在使用间接解密，而不直接与 Chrome 浏览器的提升服务交互。不过，g0njxa 评论说，谷歌仍然没有跟上，因此使用新工具可以轻易窃取存储在 Chrome 浏览器中的用户秘密。

针对该工具的发布，谷歌与 BleepingComputer 分享了以下声明：

这段代码（xaitax 的代码）需要管理员权限，这表明我们已经成功提升了成功实施此类攻击所需的访问量。虽然确实需要管理员权限，但这似乎并没有影响恶意软件的信息窃取行动，在过去六个月里，恶意软件的数量只增不减，它们通过零日漏洞、GitHub 问题的虚假修复，甚至 StackOverflow 上的答案来锁定用户。

参考来源：https://www.bleepingcomputer.com/news/security/new-tool-bypasses-google-chromes-new-cookie-encryption-system/

***END***

阅读推荐

[【安全圈】中方抗议美国中情局企图蛊惑诱骗中方人员投靠](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065566&idx=1&sn=7ca4926cd0ec6f740e5a6c6205c875f4&chksm=f36e635ec419ea487b810b9fa5d34e3b4880c3829945e77330a610f4a6bf0104a645072d6ece&scene=21#wechat_redirect)

[【安全圈】臭名昭著的勒索软件 REvil 四名成员在俄罗斯法院被判处4~6年监禁](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065566&idx=2&sn=bb6585dc09f065aca01a914c286b2428&chksm=f36e635ec419ea48c2fdd806f47f22dade9fb939b9eb60645d63218b24740819493c512fb559&scene=21#wechat_redirect)

[【安全圈】美国超大型数据泄露事件曝光：超1亿人数据被盗](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065566&idx=3&sn=46969e0de80f5f72c83eb444f479f4ed&chksm=f36e635ec419ea4806d6897373bd6333ed859cd10ba15393a815521e4f9e174940849c7da621&scene=21#wechat_redirect)

[【安全圈】因持续技术问题未能解决 微软宣布暂时撤掉Windows 11所有开发虚拟机](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065566&idx=4&sn=2b801b48c3a2637022eda84b8ded4b9b&chksm=f36e635ec419ea48fb3673df944a0a01efd65ec51428521954973b7f681350f5cba836cf2779&scene=21#wechat_redirect)

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