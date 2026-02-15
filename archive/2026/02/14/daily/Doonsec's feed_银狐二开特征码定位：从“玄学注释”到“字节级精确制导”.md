---
title: 银狐二开特征码定位：从“玄学注释”到“字节级精确制导”
url: https://mp.weixin.qq.com/s/5ivjJDGyBJ0jdHZH0Twrpg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:23:22.247734
---

# 银狐二开特征码定位：从“玄学注释”到“字节级精确制导”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GEVYW8ofHic1edzDzJ11icBDB8jnCFNAnDxVgYibPNn4SpbmfR1fibE6Tiapv9flSiavsz6icNcokVHoNod8pe2DLh4SbelA0HITFLsichdXlyNdiads/0?wx_fmt=jpeg)

# 银狐二开特征码定位：从“玄学注释”到“字节级精确制导”

原创

老鑫安全
老鑫安全

老鑫安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic3X5bkkRaylEIp01kcMAntDs4V20Nswx2z8xj2U3sXiapJtUFeGszzQibb7kJoM07VLhtaKuuVRpdO9f7xRNFpib41BlAvnuPdZMo/640?wx_fmt=png&from=appmsg "null")

如图，徒弟快过年了还在测试二开的C2，真是太卷了，想起他之前二开银狐，改了很多特征，像经典的以下报毒(Backdoor/Lotok.ei)需要改登录模块

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic0kyQ4lBAhKpAEPKzWaq2QoZCJxFprV57HnmIW8XTkB5Ay45qpk1sBVaOibHO2PRHDl3XFQBgpBnOW6XLYKmI0a9FpJcKJwKYf0/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic12QG43PuSFEngxeZ4Xicj4pA65mpMelSP9SK394cJxicWo0licS6qGHmfjNiclsHsjIsriaE5pDtyR9QBnlJia3ZFmKsRjdJpkIVbhM/640?wx_fmt=png&from=appmsg "null")

聊了几句没啥问题，但是他测哪个地方报毒的特征居然是通过每次注释掉不同代码编译来判断让我有点无语(杀软报“登录模块” → 猜测相关代码 → 注释掉 → 重新编译 → 上传扫描。)每次修改都需**完整编译**，耗时巨大。最大的问题是，你永远不知道是**哪一行、哪一个字节**触发的规则

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic3jccNbMtbXBMJZwW56iaCJfAvR0eyRDib4xE8kruRaibw9icTsGMORxEGmiceDibt6LlAkDM7o90f1LmkCVnqwQ13deH9PJkdWv2Lhc/640?wx_fmt=png&from=appmsg "null")

其实在很早之前也有个师傅特地要在火绒环境下改这个静态特征，当时我是发了一个Virtest给他定位特征码，相比每次通过注释不同代码块来判断报毒位置来说这种工具更为简便，其大概原理也很简单就是不断对半分割文件提交给AV扫描，根据报毒反馈，锁定触发检测的**最小字节集**（往往精确到16字节以内）。

工具实现代码可以参考网络安全领域的C语言基础课：https://www.bilibili.com/video/BV1mAcWzaEW2?spm\_id\_from=333.788.videopod.episodes&vd\_source=d0c5cfc4008c14d0c490e16cf55f5b65&p=14

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic3TxBceURNuapJasg8yOUIPedLKZfGTzicsZLJEqXOOP7jGK54Zibxa4yvjaeSutVSxv8aBfeib2n2JDyLmNbaZ55f9JmlUItc8Zo/640?wx_fmt=png&from=appmsg "null")

不过这个VirTest无法检测其他杀软，比如Defender、AVG、kaspersky等。毕竟年久失修，且只针对特定环境。现在，我们有更强大的开源工具，它们原理相通，但功能更强、适配更广：

所以这里推荐其他定位恶意字节的工具：

https://github.com/dobin/avred

https://github.com/gatariee/gocheck

https://github.com/PACHAKUTlQ/ThreatCheck

在线工具：https://avred.r00ted.ch/upload

其中ThreatCheck还可以编辑config.yaml配置扫描器，比如配置火绒的扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic0y00rrA95QFpgDJNlpcicDjc4heUpBtQ8B59AbHiaY38qM3EaSPYs44zehVwWr3vx8tRrJhvhT5dWBfxQaLn3UCVOiaPaJMXNOPw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

老鑫安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

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