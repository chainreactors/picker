---
title: 一口气getshell
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496671&idx=1&sn=806276d964174b1365a75da252de686f&chksm=e8a5f9bcdfd270aa7f209fe0841146bd0a30472575511395e169fb72e47c6179050c6528c23d&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-25
fetch_date: 2025-10-06T19:39:23.710898
---

# 一口气getshell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6tHgVzHooqWMAUQSncX8EtDvJjbFpNuruGBv4s66LGebict94P8p8X9FPAyZMFlt8uQ8FKOxGYSFw/0?wx_fmt=jpeg)

# 一口气getshell

迪哥讲事

以下文章来源于跟着斯叔唠安全
，作者跟着斯叔唠安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM71BddGyNDhcnRiaPT7QXjlY4LPZlr1kjTkctThFFtib9LA/0)

**跟着斯叔唠安全**
.

一个专注于安全资讯分享的家伙

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

1

Start

好久没更新了，又来水文章了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_21@2x.png)

2

Action

故事的最开始是下发了一批ip为主的资产。这玩意儿到手第一步当然是全端口扫描或者fofa，quake，hunter之类的获取资产啦。整理结果的时候发现了一个8848的端口。虽然没扫出来指纹，并且直接访问标题是“404-NOT FOUND”，不过直接告诉我，这里可能是个nacos，果然，通过拼接目录/nacos直接访问到了nacos的系统

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaN9HHLJNwAtQeZLZo1UZbNupJlEB1Z1RKEJrptnSghPfvySCtyMbbjt8egyFkBUdrI48dytRgr0w/640?wx_fmt=png&from=appmsg)

    直接nacos工具一把梭哈

```
https://github.com/charonlight/NacosExploitGUI
```

    问题还不少，先nacos/nacos默认口令登录上去看看有没有可以利用的东西

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaN9HHLJNwAtQeZLZo1UZbNfKmf40ssaLTiaDe6heBtXa2fy9PibiaveuPO6vIYv9WZPBnic0icvy3dLbw/640?wx_fmt=png&from=appmsg)

通过数据库的配置文件账号密码稳稳拿下数据库，刚好是建在公网上的数据库

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaN9HHLJNwAtQeZLZo1UZbNLufULOLnruHepwgZJfPeqWuXnKaCw7NfF0snyvkMWrd6XRB8AfFBBQ/640?wx_fmt=png&from=appmsg)

准备通过数据库看看能不能看到一些能够进一步利用的信息的时候，看到了另一个端口的url

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaN9HHLJNwAtQeZLZo1UZbNlgk24uCaQcmTdTeejwGsCicicARPF9LLHfkYCZFIfYEsK68ibiarDmYPvw/640?wx_fmt=png&from=appmsg)

尝试访问了资源之后，将一个一个目录删掉，发现存在存储桶遍历，不过到目前为止，还是不痛不痒

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaN9HHLJNwAtQeZLZo1UZbNLKCcYRKyg2kMjeIkFMhVRfyf1aF1e5Nx4VnJO9lkiaoM29yd4mibbnwQ/640?wx_fmt=png&from=appmsg)

直接掏出之前文章分享的工具把存储桶里面的文件都爬取下来，没有印象的铁铁可以看这个文章[送上门的高危还有人不知道？](https://mp.weixin.qq.com/s?__biz=MzkzNDI5NjEzMQ==&mid=2247484333&idx=1&sn=9dd0e66ddeeb8cfeed6c89b05d4ced51&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaN9HHLJNwAtQeZLZo1UZbNYtcGlugcHa9ZSN5K4LnPx8z3S9q0Xz02PcxzLYxvH3TFDC5dPyyPzw/640?wx_fmt=png&from=appmsg)

看着没啥内容啊，照旧去筛选文件并访问，一不小心看到了不该看的内容![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaN9HHLJNwAtQeZLZo1UZbNvZ2joHMmOaFzLsOGnleqBlMiaMYOZTicPSfPic2M7kicAdkoa6D1jfVGxQ/640?wx_fmt=png&from=appmsg)

然后就是轻松通过狗运连接ssh就接管了服务器

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaN9HHLJNwAtQeZLZo1UZbNA6Fc2cAZg7bmvMK80ZcvYEoiaCU0ABGz8HftwoMPFILyicK4cInVrQ6g/640?wx_fmt=png&from=appmsg)

3

End

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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