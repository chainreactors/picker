---
title: 安全厂商警告2000万个OpenAI账号权限遭出售，官方回应
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513699&idx=1&sn=e08bed77ab557ac45630a406e606dd01&chksm=ebfaf143dc8d78557a204ac16c2befded19062d26529da67a721df0db771bd68e243af01f6fc&scene=58&subscene=0#rd
source: 安全内参
date: 2025-02-12
fetch_date: 2025-10-06T20:36:52.001667
---

# 安全厂商警告2000万个OpenAI账号权限遭出售，官方回应

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tP7yISGm4z3PLAIX3BibRWI6fe6GWS2hoMTg3cGYz5iaDtJd0ZvfNt5MibNdYg1x81KgnQIckJuydqQ/0?wx_fmt=jpeg)

# 安全厂商警告2000万个OpenAI账号权限遭出售，官方回应

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tP7yISGm4z3PLAIX3BibRWIu5I574NVK7BrvSmozof5YQZic81qniaK4WLQTTdNhnWCfQK5XicrQPCmg/640?wx_fmt=webp&from=appmsg)

**Malwarebytes实验室称，如果这批代售数据为真，考虑到数据量巨大，攻击者很可能利用系统漏洞或特权账号攻陷了auth0.openai.com子域名；**

**OpenAI发言人表示，它正在认真评估数据泄露报告，但尚未发现其系统受到损害的任何证据。**

前情回顾·**OpenAI网络威胁态势**

* [警惕！黑产团伙专门窃取各类大模型API密钥，已有大量泄露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513690&idx=1&sn=3b50cd9dc7ff66346b74d2dd708477e1&scene=21#wechat_redirect)
* [微软OpenAI云遭滥用：攻击者绕过安全护栏 对外售卖违规内容生成服务](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513487&idx=1&sn=2bb2b3796dd10a13b4a3bf0ae256a199&scene=21#wechat_redirect)
* [向ChatGPT植入恶意“长期记忆”，持续窃取用户输入数据](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512702&idx=1&sn=183b62e899019269d6a0f8da6b16f22b&scene=21#wechat_redirect)
* [OpenAI反复修补未果的ChatGPT数据泄露漏洞是什么？](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510652&idx=1&sn=32aae66d172b998bebb5ec073df3c99c&scene=21#wechat_redirect)

安全内参2月11日消息，网络安全厂商Malwarebytes发文警告称，上周，用户“emirking”在暗网论坛上发帖，兜售2000万个OpenAI用户的登录凭据，并分享了疑似被盗数据的样本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tP7yISGm4z3PLAIX3BibRWIeRpwMaT0h6EM68GszpecnlBcLfDIESicEKB29XUOfcEcZicWITybPPNg/640?wx_fmt=jpeg&from=appmsg)

*图：emirking的帖子*

该帖子的俄语内容翻译如下：

> “当我意识到OpenAI可能会批量验证账号时，我就明白我的密码不可能一直保持隐藏。我掌握了超过2000万个OpenAI账号的访问代码。如果你感兴趣，可以联系我。这是一座宝藏。”

这番话表明，该网络犯罪分子可能掌握了绕过OpenAI平台身份验证系统的访问代码。如此大规模的凭据泄露，似乎不太可能仅通过针对用户的网络钓鱼攻击获取。因此，如果该说法属实，emirking很可能是通过利用系统漏洞或获取管理员凭据，成功攻破了auth0.openai.com子域名。

虽然emirking在该论坛上看似是新注册的用户（其账号创建于2025年1月），但这并不代表什么。他可能曾使用其他网名发帖，并出于安全考虑更换了账号。

由于此次账号出售的暗网论坛BreachForums之前处于离线状态，Malwarebytes表示相关说法尚无法验证，后续将跟进并核实信息。

**官方称未发现系统受损害**

全球数百万用户依赖OpenAI平台，包括ChatGPT及其他GPT集成服务。

此次泄露的凭据，可能能让网络犯罪分子访问用户在OpenAI平台上的敏感信息，包括对话内容和查询数据。这些被盗数据可能被用于精准网络钓鱼攻击和金融欺诈。此外，攻击者还可能利用这些账号滥用OpenAI API，导致受害者为OpenAI的Plus或Pro会员功能支付费用。

然而，同一暗网论坛上的其他用户表示，所发布的凭据无法用于访问被泄露账号的ChatGPT对话记录。

OpenAI发言人表示，它正在认真对待数据泄露报告，但尚未发现其系统受到损害的任何证据。

如果担心自己的凭据可能包含在此次泄露事件中，建议用户可采取以下措施：

* 更改密码。
* 启用多因素认证（MFA）。
* 监控账号是否存在异常活动或未经授权的使用。
* 警惕利用此次泄露数据发动的网络钓鱼攻击。

**参考资料：malwarebytes.com**

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