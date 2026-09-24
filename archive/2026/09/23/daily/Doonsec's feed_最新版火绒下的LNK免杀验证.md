---
title: 最新版火绒下的LNK免杀验证
url: https://mp.weixin.qq.com/s/KyloFKJlRmfqSkf7ZzZddQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:57:07.083256
---

# 最新版火绒下的LNK免杀验证

# 最新版火绒下的LNK免杀验证

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担！！！

测试环境

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQXzyibQJ862wAQqWHMGBDsk5dUWcIia1g4IWesHCcb7seI1XQCDbXiaH4zc5jnjmsor3p7mMLtxDUVfLGNnzZAvjtl7699Py40zus/640?wx_fmt=png&from=appmsg)

事情起因

日常做LNK测试发现，解压后LNK文件直接被火绒落地秒杀，看起来火绒又加新规则了。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUQpGZ8Qiceab0GUpttT3DzswPiaOBj6hrE7xvbw7AIIMKNsZRXyCzI5SefXY4oabpqBuVuSqoLgL6RsKl5osmQjnce5h8WAFV8s/640?wx_fmt=png&from=appmsg)

如上图，可以看到落地就被秒了，火绒落地秒的情况，多半就是字符串查杀，查杀了lnk中的某部分信息！

目标命令行测试

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQX5D6AmHeLxnfqGRuRaVuxRhQqPuCCiaPr8EyuUicc3wicguPf2vicHz7wd2HUWtGglMTaJXtib7rBu5CVJUA06DZ7LNQvRWW44vXDE/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQWXtvrNKibXdab3oNaTDnfx6Q2jXibotuHRluXUPaTEyVrJoc0JKo0O8jtLXPC0CO66oY9Sib08tmLcuzYS111jvYOldNwhzw0oJ0/640?wx_fmt=png&from=appmsg)

```
C:\Windows\System32\rundll32.exe url.dll,FileProtocolHandler "1.exe"
```

测试验证还是被查杀，直接把url.dll,FileProtocolHandler "1.exe"内容删除，再次测试！

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQVdF53UzFibplia5JdMrpEyN4ricompvVCn51zYJBz6FIs9CVCBzOaGZ5Nqyk3BSoH9bbJynLdOwVJtBnJPSXKh9xf4RiaGia3c6p3A/640?wx_fmt=png&from=appmsg)

如上图，还是被杀，换个思路：使用正常文件的LNK替换命令行参数，确认下是否命令行参数查杀。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQW1mruff3m6SC9YJGSbwGamdyiaQsjYpgmKXd9Teo6Riawwmgc02ticxBKyXScYCgw2AOF3onpUw4ytVYibibNMFoicPibibOm8Nhvj30s/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQW2YPKicyRtHRWqIO2XT4fXpSlXPq3nwich6kU5A8Ihf1DPFqWsgv79qbnaUKP3r4mic1p1Fv5AZ9Cthy0Qic1DmoQxgJKC8fejdFQ/640?wx_fmt=png&from=appmsg)

没被查杀，排除目标中的命令行问题，那问题猜测是LNK本身的信息导致被查杀的，修改自动解析PDF图标看看，很大概率是这个问题。

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQW1VL4kdGsYWVt7oNVXY8PJ4xlPCw9OicZWGiayMFTufuYvgNBurWqSZEDnjB6HdY6GicvTst8Qn4AuAUfQJ6KRkAHbHSuhBc2TNg/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUyjxpVjHFtv6fDvk6uwDb6cvdHWyWzo6bq9BZ2avWX1UICnicWOK5MnQiaMfvKEGz05xTKDV0JzPK8CLeF58EAzv7m9f8X8Jcb0/640?wx_fmt=png&from=appmsg)

确实是因为改PDF造成的。

（反转）发现组合规则

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQXw7T8uOI9jUgVUXJPTOPaUf4KZ3Xpx4SmibUs48yP5qHf6Rfd53PUFwicstKDdictRTD7EiaKicknUSIn7lMGocFm3o6UN5k4SE4C8/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQWID6sYhCsoKFYRwzK0GWbed6FDe8tbGEo0OQSrNtRe8vyeraSIgicK898iaUib2B6Nltkh9N0xJMdRUWGj5MMvZXrckv7ytN558A/640?wx_fmt=png&from=appmsg)

如上图二进制查看同样是1.pdf，但是没有杀，我把目标改成rundll32呢？

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQVhxlU0Frctdw0Yxz3UgYYQS3BrteB7mGf3N8G5Xttic1PXXzoBxOkvCvkbtLE5pKqobTG6yES7cvyribTH5oopL8AalBrVMYJgI/640?wx_fmt=png&from=appmsg)

改完就被杀了，那么初步判断是pdf后缀自解析图标+rundll32调用就查杀，看来是用得人太多了呢。

总结绕过

简单粗暴的方法就是不用rundll32了，用其他exe。

```
C:\Windows\explorer.exe "1.exe"
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQXaficHLvibxd00FY82qyzZOzrOy3XdJNy5FxPSs7PtjGuhsuiaAPJRrAWup1cUniabod8MgBBWVwDOj5jzfGyO8MqCZpYfd4sKQQE/640?wx_fmt=png&from=appmsg)

**红蓝偶像练习生小圈子**

**更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满400人，欢迎各位进圈子交流学习！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQXm0N3QQT1byMjhzMvPx3RqYswWyvlOTqPbxMWYiawjx8h7EJwTTDrE5Wp4CytmjG2dYtIGjAJMCSicXoY1N8nOcFE2a0oqNwWnE/640?wx_fmt=jpeg&from=appmsg)

****圈子目前更新相关技术文章：****

************* HeavenlyBypassAV内部版工具-轻松免杀各大杀软
* HeBypassAV内部版Patch免杀工具-轻松绕过杀软EDR
* Heavenly自动化红队后渗透工具免杀生成器
* Heavenly白加黑自动化生成免杀工具
* HeavenlyProtectionCS内部CS插件
* Heavenly专版Linux免杀工具
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
* **还有更多红队工具文章！期待您的加入！！！**********

**往期推荐**

**********[安全天书免杀课来袭｜助力实战免杀钓鱼(文末送福利)](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485167&idx=1&sn=7ab4393e75cf94d13cb79e22b92fb8d0&scene=21#wechat_redirect)**

**[【红队工具】攻防后渗透工具自动化免杀！！！](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485305&idx=1&sn=3b4c50d0f88a753089767db5304b6626&scene=21#wechat_redirect)**

**[【红队工具】红队内网后渗透CobaltStrike插件更新](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485006&idx=1&sn=e3bcf2070226fcfc93b565ae2c9d85ad&scene=21#wechat_redirect)**

**[免杀更新--Heavenly自动化生成白加黑3.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485679&idx=1&sn=991c111e2627ec8835dc13b8bc919eb3&scene=21#wechat_redirect)**

**[绕过360安全卫士实现维权](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485280&idx=1&sn=467194cdf681646597a84e7f08b638bf&scene=21#wechat_redirect)**************

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