---
title: 网传BT面板突遭黑产批量攻击
url: https://mp.weixin.qq.com/s/FGGVzzNyif9nD71D99hZJA
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:28:53.541061
---

# 网传BT面板突遭黑产批量攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OzSjTuNHyE4oPl6BFbp632rR1xgVHaJtr0YQE8npkHNAGKpte2cuzcxh3mWvSiby1ROYbwug0O9PYc77ialC5qbLDG8G4g83Dy9Q/0?wx_fmt=jpeg)

# 网传BT面板突遭黑产批量攻击

原创

DATADOG
DATADOG

表哥带我

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/pxKqYxJWy7MwqgqlfAHibBF3z5SG1jQ33gAZpcpSzNrDOcWqOwsflg9dtktFJDmQDp8S0zibEmjILNJGcxK9bAjA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

> ❝
>
> 由于传播、利用本公众号"表哥带我"所提供的信息而造成的任何直接或者间接的后果及损失,均由使用者本人负责。本文选材源于DATADOG。

据**DATADOG实验室于2026年2月4日发布的报告**显示识别出大量React2Shell漏洞利用相关的攻击活动,该攻击活动旨在利用恶意的NGINX配置劫持网络流量。

![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OxDkNFQ5aRBl9WGIaYteicE2zUwP8ISnaM3lN2k9PES01B4jGHC1OmPjy2iaUd4dKlfw3u6y49eJ7Zj8XOlpmRECAEBjicrC2X4UU/640?wx_fmt=png&from=appmsg)

根据报告内容，攻击活动实际上发生在**2025年12月**，Datadog Security Labs是在**2026年2月4日**才发布详细分析报告，属于事后披露和深度技术分析，而非实时预警，应当是被部分公众号误解了发生时间。

**报告指出宝塔面板**及**NGINX服务器**成为主要攻击目标，黑客通过攻击篡改服务器配置，将网站流量劫持至非法博彩网站。

该黑客活动面向亚洲顶级域名(.in、.id、.pe、.bd、.th)、云上托管的一些基础设施(Baota Panel)以及政府和教育类顶级域名(.edu,.gov)等目标。

![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OwYMye2UTknEe8Zw7RtA1g5Yu7liaCLhmCnJIic6m4M0x4hbUaLLlb6ia1E24kMl0V4YYicApM2opPeepxO2zVh59SKWZ8IoPhEAN4/640?wx_fmt=png&from=appmsg)

根据该实验室的调查发现，黑客利用React2Shell漏洞(CVE-2025-55182)获得的初始访问权限。

在调查过程中发现了攻击者用于自动向 NGINX 注入恶意配置的多个 shell 脚本。根据这些工具包脚本中的模板逻辑,恶意配置通常遵循以下所述结构。

![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OwANPybXOrtpTV0nNbXcacBtQerUcefHhwMiaamkUMkfBGWpEBmiaPPTBd4yDJ1MPzGsBYIN3BugVe25aby6c1MuZmNaZXHsCTqs/640?wx_fmt=png&from=appmsg)

在这种情况下,路径变量和`proxy_pass`恶意配置中的指令是动态识别的,并根据攻击者成功劫持的特定域名进行替换。

下表显示了哪些TLD和路径对将被发送到攻击者的代理域中:

| 模板 | 顶级域名 | 路径 | 代理域名 |
| --- | --- | --- | --- |
| TH | .edu,.gov,.vn,.th | pg “pgslot” “老虎\*” “游戏” "\*场" "实时播放" | th.cogicpt.org |
| 在 | .in,.id,.pe,.bd | pg “pgslot” “老虎\*” “游戏” "\*场" "实时播放" | ide.hashbank8.com |
| COM | \* | 帮助“新闻”页面“博客”关于“支持”“信息” | xzz.pier46.com |

zx.sh是 NGINX 注入工具包的第一阶段

![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OxSclDcD0bGibywoDsd3rYvssYNm6ZlHPvxA4EyP3xIuYMPmBR0mEpOsY9pKt8mhoeAiayG46FXfNP3j8m6nD7qfft8xkK35KUAU/640?wx_fmt=png&from=appmsg)

bt.sh通过输入特定的配置文件路径来针对Baota(BT)管理面板环境:/www/server/panel/vhost/nginx。

识别目标后,脚本会先检查配置文件是否用于任何先前的恶意代理域,然后继续进行注入。配置文件使用`server_name`变量(包含完整域名),可动态选择注入模板。此选择基于顶级域(TLD),并包含基于硬编码路径变量的随机选择路径。

4zdh.sh脚本采用的输出和错误处理技术比bt.sh更广泛。

该脚本针对常见的 Nginx 配置位置,例如`/etc/nginx/sites-enabled`,`/etc/nginx/conf.d`并且`/etc/nginx/sites-available`除了寻找宝塔管理面板外。

![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6Oz7Z6PTBurFqJ1pSmG0J4O3riak4gxSl18KkrzNbhlUC0EvNebKF5Dbz0w3DUUXicOXQK110GsCC2Rha1eBx7acHicwrHgnF6ywhg/640?wx_fmt=png&from=appmsg)

报告指出建议升级React至19.2.1+或Next.js至15.5.7+；审计NGINX配置目录，删除陌生proxy\_pass指令；修改宝塔默认端口，启用二次验证；对/etc/nginx/\*\*实施文件完整性监控；限制服务器与境外IP通信。

其他阅读：

[字节海外中国籍员工直呼扎心](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486910&idx=1&sn=c3f6e0a16c5cf6b912ffbdf807ac207f&scene=21#wechat_redirect)

[【吃瓜】某三中监控被“黑客入侵”放片](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486901&idx=1&sn=b7587007a77c0ef9341b3caf59ed4546&scene=21#wechat_redirect)

[服务器爆满，下单奶茶被千问“拉黑”](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486901&idx=2&sn=7782806dfe8dd3eaaa183c3c7db8f933&scene=21#wechat_redirect)

[【吃瓜】下头X为了千问助力脸都不要了](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486875&idx=1&sn=16ee18913d27f0aea8e8915b345b0d8c&scene=21#wechat_redirect)

[快手出现大量低俗内容被罚1.191亿](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486856&idx=1&sn=085ac8766a9c925a030939d7750b7427&scene=21#wechat_redirect)

[用泄露的爱泼斯坦邮箱拿下微软365个人版](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486848&idx=1&sn=ea2645950f190e264ecc7092d5381690&scene=21#wechat_redirect)

[【AI大战】继豆包后阿里送出30亿免单卡](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486827&idx=1&sn=6ba4b631c6820330e29a5731340b6440&scene=21#wechat_redirect)

[【吃瓜】秒挖高危洞的手机黑客临幸补天6群](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486810&idx=1&sn=93f5ef59db2f2957c00aa2a2551a60a4&scene=21#wechat_redirect)

[网传海角社区泄露1570万条用户数据](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486775&idx=2&sn=0460974909d1d3c15de929de44d69bc8&scene=21#wechat_redirect)

[【吃瓜】Telegram大量用户数据泄露](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486552&idx=1&sn=6e3fe989d90dcefc461261763bb1f100&scene=21#wechat_redirect)

[Notepad++遇国家级APT投毒定向百万设备](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486743&idx=1&sn=c9b0e8ed68b2a53e723f3e4453b2c9e4&scene=21#wechat_redirect)

[停用一批境外厂商的网络安全软件](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486732&idx=1&sn=ae325fcd6eb6eeda8ff2bb108d365852&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PQ94TF6vc1lVW4vKDb0TEXvWoTCrRtywEIMeOruhjDclgAvFjr3Dd84iaI0LqTJ4CAODAnwm447cw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

**左侧长按加入**

**吃瓜交流群**

动态入群二维码

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PW1JR7KU1wRqvaNyp3ESh9m1FzIau0Uqvh7DDnryFJCzq3u7sc2J8wAtOffybvhBgkQW1CfJs9sg/0?wx_fmt=png)

表哥带我

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pxKqYxJWy7PW1JR7KU1wRqvaNyp3ESh9m1FzIau0Uqvh7DDnryFJCzq3u7sc2J8wAtOffybvhBgkQW1CfJs9sg/0?wx_fmt=png)

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