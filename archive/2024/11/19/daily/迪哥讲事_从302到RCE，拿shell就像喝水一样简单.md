---
title: 从302到RCE，拿shell就像喝水一样简单
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496368&idx=1&sn=776d5575867f08de6b73d3b5ba545171&chksm=e8a5f8d3dfd271c579aa9dade1e836ea3788b9505ea767b835216a7b0b616ff932f766ae7e3c&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-19
fetch_date: 2025-10-06T19:19:25.397031
---

# 从302到RCE，拿shell就像喝水一样简单

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj5X3AkXG5DDnicnlQFZBwVb6xNYotic4LVvfDA90VTHh5EjJxib2b31fRq4GdDvaSk7w7yMwUiaWa705w/0?wx_fmt=jpeg)

# 从302到RCE，拿shell就像喝水一样简单

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

从前两天《[从404到RCE](http://mp.weixin.qq.com/s?__biz=MzkzNDI5NjEzMQ==&mid=2247484218&idx=1&sn=744a1df0c116bf5257da1d5001de1172&chksm=c2be2c16f5c9a500ddc9068cfc8e039c77d79e8dbc88b3324a30f5870cf1517678643619fd82&scene=21#wechat_redirect)》的文章反馈来看，大家很喜欢看这个系列嘛（还没看过的铁汁可以点击链接查阅哦），刚好最近项目上又碰到一个比较有意思的网站，顺手也给记录了下来。

2

Action

故事的开始总是那么的普通，老生常谈的开局一个登录框。什么？还有人不会测试登录框？快去参考参考斯叔之前的文章：[抛开day不谈，为什么同样一个站你挖不到洞，别人却能咔咔上分？](http://mp.weixin.qq.com/s?__biz=MzkzNDI5NjEzMQ==&mid=2247483975&idx=1&sn=25603630eb190bc7b66f5769003861f1&chksm=c2be2d6bf5c9a47de40a142e20d145be38ee90d4a148f44bd32d0ac1600916da892e34aaaaf8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8Me21EaeV5xzs3FqzmekDANE9YSibfkWxGGUic6Tibn9h8UuJQL8kqrVuPg/640?wx_fmt=png&from=appmsg)

    简单识别了一下指纹情况，只有shiro，但是没跑出来key，刚燃起来的火焰又被浇灭了

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8Mtt8EPt8ibBUtrPhHZZlNjEF42o7Al7iaLyEbvb20NZia5R04IcTVFeniaQ/640?wx_fmt=png&from=appmsg)

    试了弱口令也无果，JS里面也没翻到什么有价值的内容。偶然瞥到了url栏里面的/xxx/admin/login（/xxx指代一级目录），你说会不会存在未授权的后台页面呢？试了一下访问/xxx/admin/home，emmm不行，302跳转回了登录框

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8MIczYlCVCcQffiabFO0VCicGPefW1reticicbdsaesiaGc0zCjzTG38E49Hg/640?wx_fmt=png&from=appmsg)

    看似走头无路，但是汇总一下目前已知的一些信息来看。。。首先网站是用了shiro的……嗯？shiro？谁说shiro只有爆key反序列化漏洞？还有权限绕过诶，试了一下权限绕过的poc：/xxx/;/admin/home，成了！

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8MAP6l2ch0tKcaNvj2ribAMwlSIvYvQfKAYZWyAticGibXbsvXoxFqRibvXA/640?wx_fmt=png&from=appmsg)

    但是光是这个漏洞还不够呀，不得行啊，不能辅助rce这就是个垃圾洞，看看还能不能继续深入。翻了一下home页面加载的js文件，没啥能利用的接口呀，那咋办？没啥好办法，只能使用fuzz大法了，burp导入密码本，开扫！

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8MeJPVbicALI9D9K1KdYVY2tVaZOMgibVicc60Ud7BjRiaqKhj53xxvrQ4qQ/640?wx_fmt=png&from=appmsg)

    功夫不负有心人，还真让我扫到了一个目录/xxx/;/admin/content，有数据！感觉有戏。

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8MicDJo9nZ1tkibGS7SluhQWQBRycECrISicLjkGZ0ZZjPQFhY2Olvue1SQ/640?wx_fmt=png&from=appmsg)

    不过目前都是在burp里面访问这些资源，如何在浏览器里面自动的让url添加/;/呢？我们只需要在burp的代理模块里面按照下图的步骤添加一个规则，这时候经过burp的代理流量就会自动将匹配到一级目录/xxx/后面添加;/实现自动的shiro权限绕过了

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8Ml3JvicrnduZs1PQ8DmCm0PWhUTpM4iblfErpmpyjmOtxvxkBtSOzDJEA/640?wx_fmt=png&from=appmsg)

    随机点了一个标题的查看功能点

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8MgHEZexyOHKPEbrwic39bHcP8oMibjKfcyvTAUjfntE0U5h2n4EKCjjJA/640?wx_fmt=png&from=appmsg)

    有上传点![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8MItuc7LEp2KLUUqqHdwZ2IPlYHYoNWnNialRicmbIiataLeg880mTPB1WA/640?wx_fmt=png&from=appmsg)

    经过测试，共有三个上传的接口，分别是/uploadImage，/uploadPicture以及/uploadVideo，其中前两个是白名单校验，不能上传非图片后缀的文件，最后一个能上传jsp（提示上传成功），但是不返回文件路径。

    得盲猜文件路径了啊，有点难搞。不过当我回头分析/uploadImage接口的时候发现了一件事情，它是返回路径的，它告诉我文件保存在了/xxx/xx/res/images目录下面的

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8MG0cNfYguWh3U0khcyECx4lL4zM24anWw4pAIkFibicib0dv9slyc9oIQw/640?wx_fmt=png&from=appmsg)

    有没有一种可能，，/uploadVideo也是在/res目录下的？为了防止资源目录下可能不解析webshell文件，我特地在文件名处增加../跳跃到上一级目录，这样webshell的地址就在/xxx/xx/res/1.jsp了，上传成功

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8MMRKiavl6OBPHEnRNibiaOTKvib0ldUYSWSy4yrGtF94cTp4QqcGYncxibWg/640?wx_fmt=png&from=appmsg)

    访问一下/xxx/xx/res/1.jsp，成了！

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaOw6lthMj8PPTGzibQzvSVv0oMAibC50CYcNYyoMw2mvKL0f5XmPSpaJhagntSdr6YxBvOVlDL4AFQ/640?wx_fmt=png&from=appmsg)

    上传的马子是无害的自删除马子，访问后自动把自己删除掉

```
<%out.print("f7098ef4b298e771722e3935f309eb6e");new java.io.File(application.getRealPath(request.getServletPath())).delete();%>
```

    一不小心又shell了。

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24Ubia8oiavG1E6r9CuRsniaEib8M9nPTJ167CUuvjfLUqoXJVk0HoYxlkNoBjEzjr6YVich3vPDTfLeN14w/640?wx_fmt=png&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

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