---
title: 【安全圈】卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064335&idx=1&sn=58b373211bd4c559c7a5438c7028763d&chksm=f36e660fc419ef19209d749f3d05c2f0c992ef5a7c5af76624fb52ec5d4fcf65e86883226729&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-12
fetch_date: 2025-10-06T18:29:15.281105
---

# 【安全圈】卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSnBZJibNUDIujEpVry75T6efcjAxUibPlhzUNCbpbszDXtKFIykgwlibaA/0?wx_fmt=jpeg)

# 【安全圈】卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

勒索软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSxabjiaWtIOJqwLpNen8epZicv4yTDibFbrZpiaia0l7tkVSjIOnXPzZogdg/640?wx_fmt=jpeg&from=appmsg)

近期，RansomHub 勒索组织一直通过利用卡巴斯基的合法工具 TDSSKiller 来禁用目标系统上的端点检测和响应 (EDR) 服务。

在攻破防御系统后，RansomHub 又部署了 LaZagne 凭证采集工具，试图从各种应用程序数据库中提取有助于在网络上横向移动的登录信息。

## 在勒索软件攻击中滥用 TDSSKiller

卡巴斯基创建的 TDSSKiller 是一种可以扫描系统是否存在 rootkit 和 bootkit 的工具，这两种恶意软件特别难以检测，而且可以躲避标准的安全工具。

EDR代理是更先进的解决方案，它们至少部分在内核级别上运行，以便监控和控制如文件访问、进程创建和网络连接等低级系统活动，从而提供针对勒索软件等威胁的实时保护。

网络安全公司 Malwarebytes 报告称，他们最近观察到 RansomHub 勒索组织滥用 TDSSKiller，使用命令行脚本或批处理文件与内核级服务交互，从而禁用机器上运行的 Malwarebytes 反恶意软件服务（MBAMService）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSrvb7aZWzD26ibfGq4eJEFxBsQTicNxYhvTicWmLlIm0SbhjZkkSJiaeumQ/640?wx_fmt=jpeg&from=appmsg)

TDSSKiller 支持的命令参数  来源：Malwarebytes

该合法工具是在侦察和权限升级阶段之后使用的，并使用动态生成的文件名（'{89BCFDFB-BBAF-4631-9E8C-P98AB539AC}.exe'）从临时目录（'C:\Users\<User>\AppData\Local\Temp\' ）执行。

作为一个签署了有效证书的合法工具，TDSSKiller 不存在 RansomHub 的攻击被安全解决方案标记或阻止的风险。

接下来，RansomHub 会使用 LaZagne 工具提取存储在数据库中的凭据。在 Malwarebytes 调查的此次攻击事件中，该工具生成了 60 次文件写入，这些文件可能是被盗凭证的日志。删除文件的操作可能是攻击者试图掩盖其在系统中的活动的结果。

## 防御 TDSSKiller

大多数安全工具都能直接标记LaZagne为恶意软件，因此检测它并不复杂。但如果利用TDSSKiller来禁用安全防护，LaZagne的活动就可能隐蔽起来。TDSSKiller本身处于一个灰色地带，一些安全工具，包括Malwarebytes的ThreatDown，将其归类为“RiskWare”，这可能向用户暗示了潜在的风险。

为了安全起见，建议启用EDR解决方案中的防篡改保护功能，以防止攻击者利用类似TDSSKiller的工具来禁用安全措施。同时，通过监控“-dcsvc”这一禁用或删除服务的参数，以及TDSSKiller的执行情况，可以更有效地检测和阻断恶意行为。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckLPdj78V4glicW8B5l0wYOEZDiaUNPm6kFmfU1qSpspg793icvkdGzG1bw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljUASPgGc31ibGFF8QlWO2bDVRTmG60tLcehoiaraLcyb9sHGOuavM5GxCJMTSegsHe0rNJzoDG9Cww/640?wx_fmt=jpeg&from=appmsg)[【安全圈】美国一 AI 公司因非法收集面部数据被罚超 3000 万欧元](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=2&sn=1a2768fa4fc1c00cdb0d5257c8f13ab0&chksm=f36e6679c419ef6f6aabf549f51379c2bdefb5b3097e8d633c0b1971d029fc37b4b0f41e6637&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckwO49EEhAmZlicZuPyaMTV5V0Ot6L28ujkfcMaic2GwicQtMLqtcgJhymw/640?wx_fmt=jpeg)[【安全圈】McAfee 识别出 280 多个虚假安卓应用，可能会窃取加密货币钱包](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=3&sn=779efcc08939bdd90510ded9e796ed50&chksm=f36e6679c419ef6f32af6ed70d1c1bc2cf9c6ec712a4762d0fbf5fab5a13b9ec9c822a19b1d6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckGjKj87HLbicfdk2VICtNmbsstdWXUibE5L8tO1tM7K4x5iavP9AVefLUg/640?wx_fmt=jpeg)[【安全圈】黑客背刺同行，向对方发送信息窃取软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=4&sn=0aa1c34198f22da1fad88f018223ddf9&chksm=f36e6679c419ef6f6509c94daed8b8325067c714e4eb88049e1be19548527e03aa43c500eb0a&scene=21#wechat_redirect)

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