---
title: “日企”被黑7小时没发现！运维狂点重启，黑客都急了：给你们留了225封信啊
url: https://mp.weixin.qq.com/s/4Kx9lkCYxdulrihc7YPg0Q
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:00:49.677365
---

# “日企”被黑7小时没发现！运维狂点重启，黑客都急了：给你们留了225封信啊

# “日企”被黑7小时没发现！运维狂点重启，黑客都急了：给你们留了225封信啊

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

10月7日凌晨3点，日本软银旗下IDC Frontier（IDCF Cloud）东日本第1区域出大事——tesla、henry、pascal、joule四个可用区虚拟服务器直接趴窝。

黑客后来放话：只用了7分钟，整个区域就变成密文，3.6 PB主存储说没就没。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIpOYBIpUQlQJg7h37XSgWeeBBqWXTXbyfLVg69v9T2PliaLn1DnXqC07e0tjE7khQKhyLJwGlaG56YeOUHalJ5VlSPsC9zNjeM/640?wx_fmt=jpeg)

一、黑客留信，运维却狂点重启

凌晨3点，攻击者在225个数据存储根目录放了"RECOVER-INFO.txt"，随便登一台ESXi就能看见。

结果呢？

IDCF运维在vCenter里反复重启那些永远起不来的虚拟机，整整7小时没找到勒索信。

黑客都看不下去了："225份，你们也能当没看见？"

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicI6BRCTAxbRfGrg0gjoHThgh19ZaiaEYZe75SibOWWJTUrHAqnYhBLn1gYTDWHLqdMV7b2qQFYUNFz31wgPJEUfvEwjFdAWJTGxA/640?wx_fmt=jpeg)

网友评论：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJNP0uibkqiccOk62zsicoo4xuN8Hk05T8tFicicfhG1sGslPgd1TSRRuOcoKwiaV2ibJ1p059qibMJkQh3JiaaC6hlXQLYmGLXwia0Lv80Q/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicINwItkic5hWFJ7TGzOvntIAJDq37icdhs7dkduNrfSl5TmjmoegicibkwgBjaXCoyRM3l13yGIkwCjSN3Wdt38GvMfCukKh1ibLFHQ/640?wx_fmt=jpeg)

二、数字很吓人，但别全信

黑客自报战绩：

239台宿主机、225个数据存储、1.66万+虚拟机磁盘、55万多快照、41.5 PB备份容量全没了。

注意，这些是攻击者口径，IDCF没逐条认。但官方也说了：受影响区域客户数据"难以提取或恢复"，想起来？靠你自己的备份。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJgvcMdkWhbrPGTO9tleaxhgQphAm8nkJicysoTDsEtyrs9k8ibId0NNQb20hYaw8ib3WJlAAqz9RkblYWd7dG56opkwx3zn5VmicQ/640?wx_fmt=jpeg)

官方通告

三、上云不是免死金牌

495家企业+地方政府被拖下水，官网、物流、政务系统全哐当。

IDCF后来切网络、关控制台、拉软银和外部安全公司进场救火。

说白了：

云厂商再大，也不是你不用管备份的理由。同区域快照≠真备份，控制台能登≠系统安全。企业别光"上云"，得把真异地备份+应急演练也带上云。

-- END --

\*本文作者：hacking。文章内容或图片来自网络，如果存有侵权，请留言，第一进行处理。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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