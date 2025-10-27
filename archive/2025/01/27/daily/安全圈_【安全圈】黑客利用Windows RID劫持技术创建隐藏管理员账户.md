---
title: 【安全圈】黑客利用Windows RID劫持技术创建隐藏管理员账户
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067622&idx=3&sn=ad95819ae6f36cb189f9da9618fff556&chksm=f36e7b66c419f270b763f53a6b467d57fb473ad42b2f070ef2b5ef85e28fe5a6a216883110c8&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-27
fetch_date: 2025-10-06T20:08:47.336394
---

# 【安全圈】黑客利用Windows RID劫持技术创建隐藏管理员账户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno5kXkCTIyk2RbCt5xjlKrLChgcGaa1tMntga4T8AnEmzj9wfMsiaB5vSA/0?wx_fmt=jpeg)

# 【安全圈】黑客利用Windows RID劫持技术创建隐藏管理员账户

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno5mIIB3sicgibjLUcI2ib78ADMwMUIqnQ749QSNOVsQUIrCRn67joAMYstA/640?wx_fmt=jpeg&from=appmsg)

一个来自朝鲜的黑客组织正在使用一种名为RID劫持的技术，该技术可以欺骗Windows系统，使其将低权限账户视为具有管理员权限的账户。

黑客使用了一个自定义的恶意文件和一个开源工具来进行劫持攻击。这两种工具都可以执行攻击，但韩国网络安全公司AhnLab的研究人员表示，它们之间存在一些差异。

## RID劫持的工作原理

在Windows系统中，相对标识符（RID）是安全标识符（SID）的一部分，SID是分配给每个用户账户的唯一标识符，用于区分不同的账户。

RID可以取不同的值来表示账户的访问级别，例如“500”表示管理员账户，“501”表示来宾账户，“1000”表示普通用户，“512”表示域管理员组。

当攻击者修改低权限账户的RID，使其与管理员账户的RID值匹配时，就会发生RID劫持，Windows系统会授予该账户提升的权限。

然而，执行这种攻击需要访问SAM注册表，因此黑客首先需要入侵系统并获得SYSTEM权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno5EyMPoduQ6JK74vcqrBLoc2qYS8Lm3KSUictmR0gW6njVjof6VBicNotw/640?wx_fmt=jpeg&from=appmsg)RID劫持过程 来源：ASEC

## Andariel攻击

AhnLab的安全情报中心ASEC的研究人员将此次攻击归因于Andariel威胁组织，该组织与朝鲜的Lazarus黑客组织有关联。

攻击始于Andariel通过利用漏洞在目标系统上获得SYSTEM权限。

黑客使用PsExec和JuicyPotato等工具启动SYSTEM级别的命令提示符，从而实现初始权限提升。

尽管SYSTEM权限是Windows系统中的最高权限，但它不允许远程访问，无法与图形用户界面（GUI）应用程序交互，且非常容易被检测到，并且无法在系统重启后保持持久性。

为了解决这些问题，Andariel首先使用“net user”命令创建一个隐藏的低权限本地用户，并在命令末尾添加“`”字符。

通过这种方式，攻击者确保该账户无法通过“net user”命令显示，只能在SAM注册表中识别。然后，他们执行RID劫持，将该账户的权限提升为管理员。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhseqppXia1pWNYkQB1BMno5xROuKbQ7KvYicsdFRxB1emAqBNFuVAEY9LEc3LlrUUrmPn5LS6RPQgw/640?wx_fmt=jpeg&from=appmsg)Windows系统上的隐藏Andariel账户 来源：AhnLab

据研究人员称，Andariel将其账户添加到远程桌面用户组和管理员组中。

这种RID劫持是通过修改安全账户管理器（SAM）注册表实现的。朝鲜黑客使用自定义恶意软件和开源工具来执行这些更改。

尽管SYSTEM权限可以直接创建管理员账户，但根据安全设置的不同，可能会受到某些限制。提升普通账户的权限则更加隐蔽，更难被检测和阻止。

Andariel还试图通过导出修改后的注册表设置、删除密钥和恶意账户，然后从保存的备份中重新注册来掩盖其踪迹，从而在不出现在系统日志中的情况下重新激活账户。

## 如何防范RID劫持攻击

为了降低RID劫持攻击的风险，系统管理员应使用本地安全机构（LSA）子系统服务来检查登录尝试和密码更改，并防止未经授权的访问和对SAM注册表的更改。

此外，建议限制PsExec、JuicyPotato等工具的执行，禁用来宾账户，并为所有现有账户（即使是低权限账户）启用多因素认证。

值得注意的是，RID劫持技术早在2018年就已经被公开，当时安全研究员Sebastián Castro在DerbyCon 8上将其作为一种Windows系统的持久化技术进行了演示。

通过以上分析，我们可以看到，RID劫持是一种隐蔽且危险的攻击手段，系统管理员应采取多种措施来防范此类攻击，确保系统的安全性。

参考来源：Hackers use Windows RID hijacking to create hidden admin account

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