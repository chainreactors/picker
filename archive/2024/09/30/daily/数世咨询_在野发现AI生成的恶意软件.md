---
title: 在野发现AI生成的恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247518455&idx=1&sn=3c3314233a3682deeda4b4f1eec09c96&chksm=c144fa4af633735cb7fa5f1e39ba1a84f7caff8a4b9b58330961d188a5c919de8952a31138aa&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-09-30
fetch_date: 2025-10-06T18:25:22.438863
---

# 在野发现AI生成的恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqpQibsUYk6ZIjR0FpC2gs4Qrst3fRbjRpa3SfS4fAcqpLAl22VBZHcUe0r1r59cy6wibFavWbIQlN8Q/0?wx_fmt=jpeg)

# 在野发现AI生成的恶意软件

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqpQibsUYk6ZIjR0FpC2gs4QrwHE1nTicibZKKk4KRAE9mIjrvLgSELWurk6VcSbko1zqVHxfYRzh23Aw/640?wx_fmt=jpeg&from=appmsg)

HP最近拦截了一封电子邮件，其中包含由人工智能（AI）生成的投放器传递的标准恶意软件。在投放器中使用生成式AI的方式，这标志完全由人工智能创造的恶意软件有了明显的进化。

2024年6月，惠普公司发现了一封带有常见发票主题诱饵和加密 HTML 附件的钓鱼邮件。这种钓鱼邮件并不稀奇，但值得注意的是其中的加密方式。通常，网络钓鱼者会将恶意软件隐藏在附件中，而在这个案例中，攻击者在附件的JavaScript代码里嵌入了解密密钥。HP的首席威胁研究员Patrick Schlapfer解释说：“攻击者将AES解密密钥嵌入到了附件的JavaScript代码内，这很不寻常，因此我们对此进行了深入研究。”现在，惠普公布了他们的发现。

解密后的附件启动后呈现为一个网站界面，但实际上隐藏了VBScript和AsyncRAT信息窃取程序。VBScript是信息窃取程序的加载器，它向Windows注册表写入多个变量，并在用户目录中投放JavaScript文件，该文件随后作为计划任务执行。此外，还会创建一个PowerShell脚本，通过这一系列操作最终触发AsyncRAT恶意软件的运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqpQibsUYk6ZIjR0FpC2gs4Qrjq3OOqSpgOpQCktdicZFon6lo0cawxTdE7YSPkzZelVf7EQS4Hm7ichA/640?wx_fmt=png&from=appmsg)

所有这些都是相当标准的，但有一个方面有所不同。Schlapfer补充说：“VBScript代码结构清晰，每个重要命令都有注释，这还不寻常”。恶意软件通常不会包含注释，而这份脚本不仅包含注释还是用法语编写的，这在恶意软件中很少见。这些线索让研究人员认为，这个脚本可能不是由人类编写的，而是由生成式AI（gen-AI）编写的。

为了验证这一理论，研究人员使用了自己的Gen-AI来编写脚本，其结构和注释与发现的投放器软件非常相似。虽然结果不是绝对证据，但研究者们有信心认为这种恶意软件是由Gen-AI产生的。

不过，这事还是有点蹊跷。脚本为什么没有被进行混淆处理？为什么不删除这些注释？加密也是借助AI实现的吗？答案或许隐藏在公众对AI威胁的普遍看法中——它为新手恶意攻击者降低了技术门槛。

“通常情况下，” Schlapfer 的联合首席威胁研究员Alex Holland解释道，“当我们评估一次攻击时，我们会考察攻击者所需的技能和资源。在这次事件中，需要的资源非常少，Payload（恶意软件）AsyncRAT是公开可获取的，HTML传送也不需要任何编程知识。除了一个控制信息窃取器的C&C服务器外，没有其他基础设施。这种恶意软件本身很简单，也没有经过混淆处理。简而言之，这是一次低级别的攻击。”

这一结论增强了可能是新手使用生成式人工智能发动攻击的可能性，并且可能正是因为其新手原因，AI生成的脚本才没有混淆并进行了充分的注释。但即使没有这些注释，也几乎无法判断脚本是AI生成还是人工编写的。

这引发了一个新的问题。如果我们设想这种恶意软件是由一位新手制造的，并且在其中留下了使用AI技术的痕迹，那么可以推测，更为经验丰富的黑客在使用AI技术时可能会更加谨慎，从而减少留下此类线索的可能性。然而，实际上，这种情况也难以被检测和证实。

Holland表示：“我们知道AI技术可以被用来制造恶意软件，但目前还未有确凿的证据来证实这一点。现在我们有了一个数据点，它告诉我们攻击者正在攻击活动中使用AI。这表明，随着技术的进步，犯罪分子已经开始利用AI创造出更为复杂和有效的攻击手段。”

Holland补充说：“我认为很难预测这需要多长时间，”“但是考虑到生成式人工智能技术的快速发展，这不是一个长期趋势。如果非要我给出一个时间的话，我认为未来几年内这种情况肯定会发生。”

我们或许该向1956年的电影《人体异形》（Invasion of the Body Snatchers）致歉，因为现在恐怕得说一句：“它们已经在这里了！下一个就轮到你！下一个就轮到你！”

\* 本文为陈发明编译，原文地址：https://www.securityweek.com/ai-generated-malware-found-in-the-wild/
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqXZatwW85WHD0ggOUzguusylfEicp7y64ic36rtZXpLGPKXds2NvBpuExtgAMicK0LB71waZTVKfpPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513359&idx=1&sn=2f3bd51b24862de02cca6078688bafeb&chksm=c144c7b2f6334ea415adac810ce4803cdb3cd5e5ba194ff394b7278ebbb48cc830c8d405427a&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqpQibsUYk6ZIjR0FpC2gs4QrQ6j0fsNFxg3rs8icO2Bt4EQuyEG9ibKfTEeBNfKjSaCjWySF60ORvqtA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247510027&idx=1&sn=d8563f0675986bfebd75ce0860aa9f01&chksm=c144dab6f63353a0aa5c8493a054f37c49031e7201783afd3b346704201dfebf17935e275b4c&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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