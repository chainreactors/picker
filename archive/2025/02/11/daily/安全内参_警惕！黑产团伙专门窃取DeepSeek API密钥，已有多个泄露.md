---
title: 警惕！黑产团伙专门窃取DeepSeek API密钥，已有多个泄露
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513690&idx=1&sn=3b50cd9dc7ff66346b74d2dd708477e1&chksm=ebfaf17adc8d786cd86360d77b7d4cd793ca80b926e82483cd1e764055020cabe39f81bb9839&scene=58&subscene=0#rd
source: 安全内参
date: 2025-02-11
fetch_date: 2025-10-06T20:39:09.501089
---

# 警惕！黑产团伙专门窃取DeepSeek API密钥，已有多个泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7unshVItj0TwgYQiaJT9wiciaGVocfXvFCYP5OvIKICIaBdMzYapBmfvcxvfHYCbS7KSwCMOkePAsreA/0?wx_fmt=jpeg)

# 警惕！黑产团伙专门窃取DeepSeek API密钥，已有多个泄露

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vQ0NWEgFIdmPL2ygumbOpeSey4FcF7K0gIRuLiba7HddMaJRK5jXmRoWJLc5hoHd4AaXdVSE87hkg/640?wx_fmt=jpeg)

**安全研究团队发现，有黑产团伙开始专门窃取云上部署DeepSeek大模型的API密钥，对外以30美元/月售卖使用权限。**

**据悉，这类黑产团伙过去长期窃取OpenAI、AWS、Azure等各类大模型服务的API密钥，对外提供违规生成服务，仅此次研究期间就发现超20亿个token被滥用，给付费用户和平台造成了巨大损失。**

**DeepSeek的最新大模型V3和R1刚发布几天，黑产团队就已经实现API适配支持。目前，研究团队在某个黑产团队的系统中，已经发现了55个疑似被窃取的DeepSeek API密钥。**

前情回顾·**DeepSeek网络威胁态势**

* [破解DeepSeek大模型，揭秘内部运行参数](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513673&idx=1&sn=7a12aa615f1328b3ccd6f00b68d635ab&scene=21#wechat_redirect)
* [警惕！DeepSeek爆火引山寨潮，超两千仿冒域名潜藏风险](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513650&idx=1&sn=dc24fd555056860003945b1591774bf5&scene=21#wechat_redirect)
* [针对DeepSeek的网络攻击再升级：僵尸网络进场 攻击指令激增上百倍](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513623&idx=1&sn=d0d49c0d4b6e85b4dd8aacd8623ca272&scene=21#wechat_redirect)
* [突发！DeepSeek遭大规模恶意攻击](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513606&idx=1&sn=c00cf1c71328532ab314b816e276ebd8&scene=21#wechat_redirect)

安全内参2月10日消息，DeepSeek大模型公开发布仅数周后，复杂的“大模型劫持”（LLMjacking）黑产团伙便已成功盗取访问权限。

大模型劫持与代理劫持、加密劫持类似，都是攻击者为自身利益非法占用他人的计算资源。利用这一攻击手法窃取的API密钥，攻击者可以使用OpenAI、Anthropic等公司提供的流行且昂贵的大模型来生成图像、绕过封禁等，而账单却转嫁给无辜的受害者。

最近，云安全厂商Sysdig的研究人员发现，一些活跃度极高的大模型劫持操作已整合了对DeepSeek开发模型的访问权限。去年12月26日，DeepSeek-V3模型发布，仅几天后，大模型劫持者便成功窃取访问权限。同样，DeepSeek-R1于1月20日发布，而攻击者在次日便已得手。

Sysdig网络安全专家Crystal Morin表示：“这已不再是短暂的趋势。与我们去年5月首次发现这种行为时相比，大模型劫持如今已发展到了全新的阶段。”

**大模型劫持的运作方式**

大规模使用大模型往往会带来高昂的成本。例如，根据Sysdig的粗略估算，若全天候不间断使用GPT-4，账户持有人每月的开销可能会超过50万美元（尽管DeepSeek目前的成本要低得多）。

为了使用这些模型而不承担费用，攻击者会窃取云服务账户的凭据或特定大模型应用的API密钥。随后，他们利用脚本验证这些凭据是否具备访问目标模型的权限。

接下来，攻击者会将这些被盗的身份验证信息整合进“OAI”反向代理（ORP）中。ORP充当用户与大模型之间的桥梁，同时为攻击者提供一定程度的操作隐蔽性。

“ORP”这一术语最早可追溯至2023年4月11日，当时首个相关项目被公开发布。自那以后，该技术被多次分支和修改，新增了更多隐蔽功能。例如，最新版本的ORP已集成密码保护和混淆机制，攻击者可通过禁用浏览器CSS使网站内容不可读，或取消提示记录功能，以隐藏自身的使用痕迹。此外，这些代理还利用Cloudflare隧道技术生成随机的临时域名，以掩盖ORP实际使用的虚拟专用服务器（VPS）或IP地址。

在4chan和Discord等平台上，围绕ORP已形成新的社区。部分用户利用非法获取的大模型访问权限生成NSFW（不适合公开场合）内容、编写各种恶意脚本，甚至只是完成学校作业。而在俄罗斯、伊朗等国家，普通用户则通过ORP绕过ChatGPT的国家级封禁。

**大模型劫持让账户持有者承担高额损失**

最终，总有人要为这些计算资源买单，无论是用于生成不适宜公开浏览的图像，还是用于撰写论文。

ORP的开发者并不希望账单过高，以免异常使用行为引起警觉。因此，他们通常会将计算负载分配到几十甚至上百个不同的账户凭据上。例如，Sysdig记录的某个ORP便整合了55个DeepSeekAPI密钥以及多个其他AI应用的密钥。通过持有多个不同应用的API密钥，ORP能够实现负载均衡，使非法使用尽可能分散。

然而，这一策略并非总能奏效。

Morin回忆道：“我曾与一位推特用户交谈过，他的个人AWS账户因大模型劫持遭到入侵。他平时的AWS月账单大约2美元（主要用于调用大模型撰写电子邮件），但某天早晨醒来，他惊讶地发现短短两三个小时内，账单竟飙升至730美元。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7unshVItj0TwgYQiaJT9wiciaGpbg5zicywb4ASkplcGKHgia2egeQbYor7ogKvpWfiaFFXQx2vCaJ8aQMQ/640?wx_fmt=jpeg&from=appmsg)

没人确切知道这位受害者的AWS凭据是如何被窃取的，但他在毫不知情的情况下，账单已累积至近2万美元。幸运的是，他在AWS账户中启用了成本警报（该功能默认未开启），因此得以及时发现异常活动。

Morin表示：“他随即联系AWS客服询问情况，但对方一开始也无法确定问题所在。最终，他几乎是立刻关闭了自己的账户，但由于费用报告存在延迟，最终账单仍在1万至2万美元之间，这仅仅是半天的使用成本。”

AWS最终为这位受害者免除了账单。但Morin警告道：“只是个人账户被劫持都能产生如此高昂的费用。试想一下，如果这种攻击发生在企业级别，会造成怎样的损失？”

**参考资料：darkreading.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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