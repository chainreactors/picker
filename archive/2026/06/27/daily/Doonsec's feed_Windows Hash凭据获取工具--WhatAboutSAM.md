---
title: Windows Hash凭据获取工具--WhatAboutSAM
url: https://mp.weixin.qq.com/s/aJpQfKrhELPYqv3rG3tcwQ
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:11:21.510111
---

# Windows Hash凭据获取工具--WhatAboutSAM

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQW0O5mw6B1Gn95vhCyTu2l7rz5KNC4f3rtvIkD3UibaPsWRFXhOEWWABXXDZiawQMEM0icsahMt3wQ0FpKGML1Ivo1Vf5ATdzhM4Q/0?wx_fmt=jpeg)

# Windows Hash凭据获取工具--WhatAboutSAM

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

WhatAboutSAM 是我定制的 Windows SAM 转储器。它可以直接从实时注册表读取SAM材料，也可以读取通过影子快照显示的离线蜂巢。实时注册表方法需要系统权限，而影子快照方法只需提升管理员上下文，因为它从VSS快照读取SAM和系统蜂箱。

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQUiagr5kGfCK0lDQskBnQrpE09WPPZf7bl2ROaYoRuVUVIFSicsGMJGWrw6ASD3fUiaY8tc6jqvTvo1UOwK6LC7qrvt4qXiadG3qtw/640?wx_fmt=png&from=appmsg)

GitHub地址：

```
https://github.com/PeterGabaldon/WhatAboutSAM
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

**红蓝偶像练习生小圈子**

**更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满400人，欢迎各位进圈子交流学习！**

![](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQVofynIQUX0S8glkJ1BQ04xHoTicVZsMgGoTGnpzOA3exRvPhMcMGTXgEgR4S1KBV5yQ0QTqvw3xbFm7EFS4vxgYnkiaKiaAVImyI/640?wx_fmt=jpeg&from=appmsg)

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

**[绕过360安全卫士实现维权](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485280&idx=1&sn=467194cdf681646597a84e7f08b638bf&scene=21#wechat_redirect)**

**[免杀更新--Heavenly自动化生成白加黑3.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485679&idx=1&sn=991c111e2627ec8835dc13b8bc919eb3&scene=21#wechat_redirect)******

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