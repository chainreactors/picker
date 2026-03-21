---
title: 【红队思路】360下钓鱼免杀思路
url: https://mp.weixin.qq.com/s/f3S9iwcXppW6kGcA7_R-8A
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T03:59:48.953487
---

# 【红队思路】360下钓鱼免杀思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BvSCMR82FwEStCJYFU5D8zzrRJfNH8rBiaicQGrBj6l0AeP4kcJdHwOd8tSnegfcYiaEW9GHubQ7Le9C9ZTrObCmQ/0?wx_fmt=jpeg)

# 【红队思路】360下钓鱼免杀思路

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器中沉浸阅读

0x01 声明

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担！！！

0x02 前言

钓鱼是一种重要的攻击手段，而使用lnk钓鱼技术则是其中一种具有较强欺骗性和伪装能力的方法。在国内对抗环境中，个人PC以常见杀软和EDR为主，下图为部分国H钓鱼样本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwEStCJYFU5D8zzrRJfNH8rBU2TAXCegvKFGBkwSIlRXn31SGW4TVpbcFwQulLP0AMsxn4HvGjSESQ/640?wx_fmt=png&from=appmsg)

0x03 制作所需

免杀木马+免杀lnk方法。

本文不讲解免杀木马制作，免杀木马由HeavenlyBypassAV圈子版本自动化生成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwEStCJYFU5D8zzrRJfNH8rBeH2qzzME5vDic5GHjqwKeKsTzlJH1yKib32PAal3j459mVibU16fzU71Q/640?wx_fmt=png&from=appmsg)

0x04 钓鱼lnk制作

因为lnk场景存在一定的局限性，需要使用Windows下存在的程序去启动我们的免杀马，白名单程序被滥用，已经被各大杀软及EDR拉黑加入规则库。新的lnk需要我们自行挖掘可用的Windows程序，下面是可用的lnk钓鱼姿势。

```
C:\Windows\System32\rundll32.exe url.dll,FileProtocolHandler 222.exe
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BvSCMR82FwEStCJYFU5D8zzrRJfNH8rBeTPuBAyw4IJGNT9GFcoZlKemQ3cAAvLbeDXpsg2H6YXicrsjxAFibgqQ/640?wx_fmt=jpeg)

0x05 红蓝偶像练习生小圈子

****更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！****

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQUPMMOM5dOInsVxyQnl7dXwicRbmOtUjYmF3W3REiaDbwjxFyxqjPz0icSTicvias0jCY7Dib0pozbaaYQkTiaCLcxVsHYlBp5Lr6EalA/640?wx_fmt=jpeg&from=appmsg)

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版工具-轻松免杀各大杀软
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