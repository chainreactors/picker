---
title: 【红队工具】SOAPy--SOCKS5代理与ADWS进攻性交互
url: https://mp.weixin.qq.com/s/DGISHzgE5aUMKZb2u7l6rQ
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:08:24.869940
---

# 【红队工具】SOAPy--SOCKS5代理与ADWS进攻性交互

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQWp7b9UTHOzIjicOuEicL0olWkcfazmfmuuK5v5VhACic1pz78U9IyrGx8JlibMeIRQMZRQeR4upa0PjWBDNPscoia3KocMube6q0q4/0?wx_fmt=jpeg)

# 【红队工具】SOAPy--SOCKS5代理与ADWS进攻性交互

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担！！！

工具介绍

SOAPy 是一款概念验证（PoC）工具，通过 SOCKS5 代理与 Active Directory Web Services（ADWS）进行进攻性交互。

SOAPy 包含了此前未开发的自定义 Python 实现，这些协议是与 ADWS 服务交互所需的一组 Microsoft 协议。这包括但不限于：NNS（.NET NegotiateStream协议）、NMF（.NET 消息帧协议）和 NBFSE（.NET 二进制格式：SOAP 扩展）。

SOAPy最初作为IBM X-Force Red与Jackson Leverett合作的研究项目，重写了FalconForce的SOAPHound用于与ADWS交互的专有Microsoft .NET机制/库，以便通过Linux对红队的SOCKS5代理进行侦察和后利用操作。加入SpecterOps后，我决定继续开发该项目，使其达到运营速度。

SOAPy 用于通过代理与 ADWS 交互，实现潜行侦察进入内部 Active Directory 环境。SOAPy 旨在作为 Active Directory 的 ADWS 导入器使用，然后通过 Matt Creel 的 BOFHound 项目将生成的数据转换为兼容 BloodHound 的 JSON。从BOFHound转换后的JSON可以上传到BloodHound，用于后期处理和攻击路径的可视化。

SOAPy还可以在Active Directory中执行有针对性的后利用操作，这在许多需要规避性LDAP写入操作的评估中非常有用。

这包括以下的商业技巧：

1. servicePrincipalName 为目标 kerberoasting 编写
2. userAccountControl为定向AS-REProasting写作
3. msDs-AllowedToActOnBehalfOfOtherIdentity 用于资源基约束委派（RBCD）攻击
4. msDs-KeyCredentialLink 为影子凭据攻击编写
5. 认证强制原语的DNS记录添加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQXOnhtEm5zqX99rVXlQzbtbfgtibwic2y7AiaoFQK9vL4p42Itw9KQXc9yuqL4JviaYnnhpbvicaDbPibZDAJ4RID5S6VyP8GqEr9UXs/640?wx_fmt=png&from=appmsg)

GitHub地址：

```
https://github.com/logangoins/SOAPy
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

**红蓝偶像练习生小圈子**

**更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQWBtF8n8G0Q2qfYY1ibia316d2wgL8ahMh9EibkrWnczXfFDWV5Y343ALUG25u4rrz03obawnZCHXubM8k9NyrlAUpUydG5nA0m4s/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版工具-轻松免杀各大杀软
* HeBypassAV内部版Patch免杀工具-轻松绕过杀软EDR
* Heavenly自动化红队后渗透工具免杀生成器
* Heavenly白加黑自动化生成免杀工具
* HeavenlyProtectionCS内部CS插件
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass免杀AV
* Frp免杀隧道工具
* 1day和0dayPOC
* lnk钓鱼思路视频讲解
* lnk钓鱼Bypass天擎
* msi钓鱼
* chm钓鱼
* Kill360核晶
* AV对抗-致盲AV（核晶）
* 捆绑免杀360
* Kill火绒
* 火绒6.0内存免杀
* kill-windows Defender

* Defender分离免杀
* Defender知识点
* EDR对抗思路
* 进程注入知识点

* 自启动思路
* **多种维权手法**

* Fscan免杀核晶
* QVM解决思路
* 红队思路-钓鱼环境下小窗口截屏窃取
* 免杀Todesk/向日葵读取工具

* 渗透测试文章思路
* 内网对抗文章思路
* **还有更多红队工具文章！期待您的加入！！！********

******往期推荐**

**[安全天书免杀课来袭｜助力实战免杀钓鱼(文末送福利)](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485167&idx=1&sn=7ab4393e75cf94d13cb79e22b92fb8d0&scene=21#wechat_redirect)**

**[Patch免杀0检测！！！绕过卡巴斯基、360、Defender、火绒等](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485194&idx=1&sn=e29a965863c59bbd26cf4b306d58301a&scene=21#wechat_redirect)**

**[【红队工具】红队内网后渗透CobaltStrike插件更新](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485006&idx=1&sn=e3bcf2070226fcfc93b565ae2c9d85ad&scene=21#wechat_redirect)**

**[全新版本--Heavenly自动化生成白加黑2.0版本](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485067&idx=1&sn=94ac2f5b6b58345bb892da7527352cab&scene=21#wechat_redirect)**

**[绕过360安全卫士实现维权](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485280&idx=1&sn=467194cdf681646597a84e7f08b638bf&scene=21#wechat_redirect)******

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

安全天书

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

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