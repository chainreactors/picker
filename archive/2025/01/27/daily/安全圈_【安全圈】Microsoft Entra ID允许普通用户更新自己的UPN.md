---
title: 【安全圈】Microsoft Entra ID允许普通用户更新自己的UPN
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067622&idx=2&sn=a56656b05bfd9f42f777c577cffe85e3&chksm=f36e7b66c419f2708526e2e4cf320f327b2b10e54589e7f1f7332c0aaab95c830b6fe1e99286&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-27
fetch_date: 2025-10-06T20:08:45.635531
---

# 【安全圈】Microsoft Entra ID允许普通用户更新自己的UPN

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno5ZlQwTHISfKUkWh7MD3uoFIbJnqsPS2D6aj7NGEG8kVUkCuFUfRTOww/0?wx_fmt=jpeg)

# 【安全圈】Microsoft Entra ID允许普通用户更新自己的UPN

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

微软

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno5ZicpPxaklqyV8Kld4MyeSAjicjUywicwLcURWnxP5e3moZia7fJ1jqF6xg/640?wx_fmt=jpeg&from=appmsg)

微软允许非特权用户在Entra ID中更新自己的用户主体名称 (UPN) ，这引发了对安全和管理监督的担忧。

测试正式，普通用户可以通过Entra管理中心进入账户属性页面，直接编辑自己的UPN。也可以通过Microsoft Graph PowerShell SDK进行类似的更新，这两种接口都依赖于Microsoft Graph Users API。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno5Yt66N5YNZOEWLPQIVwXfwicE0SN8hQGDlnTvC7iaTTCMZrXC8zibbJyiaw/640?wx_fmt=jpeg&from=appmsg)Eric Hammond Entra帐户的属性

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno505lIGVj1q3pic3JMSiazR7XiaZqgmKoag4w5DibYb4WMdGZsnQdkibpL8YQ/640?wx_fmt=jpeg&from=appmsg)使用Microsoft Graph PowerShell SDK更新用户主体名称

作为访问微软服务的关键标识符，此前，UPN的更新通常仅限于管理员，但现在任何用户都可以修改自己的UPN。很难理解为何会有组织会故意允许用户修改如此重要的属性。

## 安全风险与应对措施

允许用户修改UPN带来了诸多安全风险。由于Entra ID与Exchange Online之间的双写同步，更改UPN会自动更新Exchange Online中的主SMTP地址。旧的主SMTP地址将保留为代理地址，以确保电子邮件传递的连续性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno5OqbdS2Pxy9HqbdwIThPKNb3alxeiaPcRtMjhBneyxVS4pfZaStUsOLw/640?wx_fmt=jpeg&from=appmsg)更新用户主体名称和照片后的帐户属性

用户可以暂时更改UPN以冒充他人（如CEO@domain.com），获取该邮箱地址的访问权限，然后再恢复为原来的UPN。如果管理员没有积极监控审核日志，这种更改可能会被忽视。

此外，撤销UPN更改并不会自动删除在此过程中创建的额外邮件代理地址，如果管理员未明确处理，这可能会导致进一步的复杂情况或滥用。

对此功能感到担忧的组织可以采取措施限制用户访问：

* 限制对 Entra 管理中心的访问：管理员可以配置设置以阻止非管理用户访问 Entra 管理中心。虽然这并不能完全防止具有低级角色（例如报告阅读者）的用户进行更改，但可以减少随意访问。
* 保护 Microsoft Graph PowerShell SDK：默认情况下，任何用户都可以使用 Connect-MgGraph cmdlet 连接到 Microsoft Graph PowerShell SDK 。管理员可以通过限制相关企业应用程序的设置来保护此功能。如果没有适当的权限，尝试连接的用户将遇到 AADSTS50105 错误。

微软启用这一功能的原因尚不清楚。虽然微软通常会基于特定用例实施更改，但尚未提供允许无特权用户修改其UPN等基本属性的明确理由。这让IT管理员感到困惑，并担心潜在的滥用行为。

## 微软的行动与回应

截至2025年1月24日14:00 UTC，微软已采取措施阻止用户更新自己UPN。当用户尝试进行此类操作时，Entra管理中心现在会显示一条通知，限制此功能。

在微软对此变更的更多信息公布之前，建议组织实施控制措施以降低风险。阻止用户访问 Entra 管理中心和 Microsoft Graph PowerShell SDK 是维护安全的明智之举。

来源：https://cybersecuritynews.com/microsoft-accidently-allow-unprivileged-users-to-change-their-user-principal-names-in-entra-id/

***END***

阅读推荐

[【安全圈】2000余名网红遭信息“开盒” 嫌疑人获利几十万元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067606&idx=1&sn=06c7d132a1649380a5b7629742f5d3f7&scene=21#wechat_redirect)

[【安全圈】微软 Win10 / Win11 新威胁：RID 劫持可提权至管理员控制你的 PC](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067606&idx=2&sn=efa053f9e1755bb17193b5a5868fb8ce&scene=21#wechat_redirect)

[【安全圈】新的 Cleo 零日 RCE 漏洞在数据盗窃攻击中被利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067606&idx=3&sn=6473d53d9a207bfac9888ca3a543bbf8&scene=21#wechat_redirect)

[【安全圈】新的 UEFI 安全启动漏洞使系统暴露于 bootkit](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067606&idx=4&sn=e8ae1a9dfb9fb649575b0d8a5414a82d&scene=21#wechat_redirect)

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