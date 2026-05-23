---
title: 入门级的赏金获取案例
url: https://mp.weixin.qq.com/s/UnvS_Pi7IgJ1jao2pMqiZg
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:38:01.789699
---

# 入门级的赏金获取案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qvoCyTM5aVKpiaAtq5czd5ZWDQ8QwkbdpdvqocOQYbWibPUg2D8qqNy3kQBPJGuert2qDiaTeOiaXdwbkjtQjibgfEn2yjecERGVEk7GibkCiczQBM/0?wx_fmt=jpeg)

# 入门级的赏金获取案例

原创

信安魔方
信安魔方

锐鉴安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

z

go。

部分X

dian'ji'weigweiID

，

zai

cizhi'cizhici

s

“证书站的未授权漏洞，忆校园青春[阅edu证书站的未授权漏洞，忆校园青春](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486254&idx=1&sn=993cd82bceba042301a009c28ca2d251&scene=21#wechat_redirect)

点击蓝字 关注我  共筑信息安全

￼

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任！

1

背景

本次实战的案例，源于某高校的人脸采集系统，听着都感觉危害很大，因为全是敏感信息，如身份证、人脸等，拿到就是高危漏洞。从无账号到登录系统，靠的就是fuzz，详细的过程见实战过程。

2

实战过程

通过一系列的信息收集，高校的人脸采集系统引起了作者注意，为什么？因为有敏感信息。

连Hunter、Fofa都没索引到这个系统，作者靠灯塔拿到了，灯塔确实好使，关键还免费，需要的师傅可以文末获取下载链接！

系统的首页如下图，可以看到，只用一个登录按钮。

￼

看下findsomething，也没有找到“注册”功能相关的关键字，同时也跑了下接口，并无接口未授权问题。

￼

本次案例的关键操作来了，首先抓包观察下登录系统的数据包情况，随意输入账号密码，点击登录。

￼

可以看到登录的数据包中有个login关键字，秉着试试的心态！

作者将login改为register，惊喜时刻，注册账号成功。

￼

使用注册成功的账号登录系统。

￼

可以看到获取到了身份凭证。

￼

登录到了个人信息首页。

￼

任意用户注册账号漏洞拿下，这个fuzz操作确实有点妙。都登录系统，肯定得把全量的功能测一遍，一般可以测试sql注入、越权、文件上传等漏洞。

co

**点击蓝字 关注我  共筑信息安全**

![](https://mmbiz.qpic.cn/mmbiz_png/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlNDd8O4wJKfGhV48dQHTMk8icXxCBI5BKxPqWQOfwFWxPtG2e8iazqUssJg/640?wx_fmt=png&from=appmsg)

**免责声明：**请勿利用文章内的相关信息、工具从事非法测试，由于传播、利用此文所提供的信息、工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任！

**1**

**背景**

近期在做一些zhognce项目，大部分的精力都搭进去了，所以更新的会慢一些，不得不说，有钱的项目就是难一点，但也不是完全不可能搞钱。

本期分享一个实战案例，也是入门级的，并拿到了赏金，其实跟平时的测试大差不差，相信各位师傅能接到项目，也是能轻松获取赏金。

详细过程见实战部分。

**2**

**实战**

通过某zhongce项目给的资产清单，首先找到了一个注册的页面，为某商城的入口。输入手机号和验证码，默认注册，并登录系统。

![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVKudsrZABovPos84de7XpL00dVxmjeSyuPCuVTbOq7xCztUibQSSN338O5f2ZAyw7q8EyajqF3nwrHuk59MSa1ZibofFgkic86kKs/640?wx_fmt=png&from=appmsg)

直接注册账号，进入商城的首页。

![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVLy08obzVxo3ScD1zhfcBYdhMgUttlhkfuNyBXjvra0JOhmq0BYnicd8r7GeEO4Z8ZBibnEB87W3cUL4jxEicZW7cDZcBKbVguibRM/640?wx_fmt=png&from=appmsg)

点击进入某个商品的页面。

![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVKQm6KpwYTbRL1DWiao6nqib8EXibaOIcu7c328viaDz7iaLeOywnAOvOpCgFDxU3gAzMOcicKGib9FDPy4WslhKvKOmDZoZuKSib63eqw/640?wx_fmt=png&from=appmsg)

看下商品的情况，可以看到有个评论区。就是这个评论区，简单拿下一个漏洞，其他什么支付类的漏洞都没测，就拿下了，可以说相当的高效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVJu39GTdpQ7a225Ird9BhBaHmhYPR5u5orUCBePwxpTBibGh6wQvzdk7mw9NomIL9oja5NxH4TfMEgwT4hYGKElCgaX3TqNN1R4/640?wx_fmt=png&from=appmsg)

可以看到，买过此产品的用户的评论，前端都是打码脱敏的，真的是脱敏吗？有遇到类似场景的师傅不要被欺骗了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVKic2Bytqp6zTXjPX9eyz8oUEYYgneviaKiaicELX6kIYBYOr6ZnqLziboBAdKZ6P2zZibmvQ1iaW6buWNJq8ucah4QfticIEg6wDu3UL8/640?wx_fmt=png&from=appmsg)

必须回到Burp，看下数据包的情况。就是个伪脱敏，该商品的5W家用户的信息泄露。仅仅是此商品的。

![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVIkBNIEia12r5sgukddXgib3mPkicfuX4bcNma8ssfWmDJ3cgJfafGoaXfDlby66O7BC0NLQbUV1K4icdVvuqBiaY3MkMsAxxsBCKbM/640?wx_fmt=png&from=appmsg)

翻了下其他产品，约8款，8\*5约等于40w用户的信息。虽然不是三要素，但被有意图的人拿到了，会存在一些其他问题，具体啥问题就不说了。最终该厂商也是收了洞，给了些许赏金。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVL8nFVMFZhbM5vY63lYI9VyP6H5sA72LHgfP4e3SmDb8thFW3c0EsYhb0Gywz1YPlDhhqMHwDZAn3QnM0fJruia8rYVmAK7awm8/640?wx_fmt=png&from=appmsg)

本次分享结束，希望对你有帮助。

往期好文推荐

[分享一个渗透测试必备的POC速查网站](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488716&idx=1&sn=37bfc3a33edd4078d09782ce47b9bdf2&scene=21#wechat_redirect)

[不受限的资源调用漏洞实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488810&idx=1&sn=2a75dd51546c21fa25ac1ae14c9f24fb&scene=21#wechat_redirect)

[武装你的浏览器-AegisScope](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488779&idx=1&sn=9ad247cf823e1a75baa29993a7b59ba3&scene=21#wechat_redirect)

[某985证书站实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488796&idx=1&sn=af6051dfe22f0bdf165d3e79d2891c9a&scene=21#wechat_redirect)

[记一次差1分10分的实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488771&idx=1&sn=b60e68083cb0d1dfa0826b753c8847ed&scene=21#wechat_redirect)

[微信小程序Debugger 神器-First](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488707&idx=1&sn=7291bb3c24491b54e3d07e4451dcd21e&scene=21#wechat_redirect)

[基于攻防演练场景的信息收集工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488656&idx=1&sn=d1f4aeb5b74214bf79bdb0116f0efc7c&scene=21#wechat_redirect)

[OneScan\_TX插件，出洞神器](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488726&idx=1&sn=f6b449aa5e34dfeac533f0e34fe92a7c&scene=21#wechat_redirect)

[记一次SRC实战Getshell](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488672&idx=1&sn=262836b82eb5c83b5b7a55f4f3e894e1&scene=21#wechat_redirect)

[XXE\SSRF\XSS全家桶实战案例](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488615&idx=1&sn=81ba367b5962295e50dbc2b335fd4d59&scene=21#wechat_redirect)

[WEB安全评估工具-FLUX](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488646&idx=1&sn=b28066918da5c7b6b4a32cd2bcf58e2c&scene=21#wechat_redirect)

[武装你的浏览器-信息收集](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488461&idx=1&sn=330b3bacf6d1cbad8f3fa1f50d2cd159&scene=21#wechat_redirect)

[武装你的浏览器-漏洞检测](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488515&idx=1&sn=dbd723fea089a06385d61685c3a90189&scene=21#wechat_redirect)

[武装你的浏览器器-Webpack\_extract](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488526&idx=1&sn=b30d224548e609162996602f2ec5af42&scene=21#wechat_redirect)

[通过SSO认证绕过，艰难“拿证”实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488451&idx=1&sn=1e8f509e558f429a5a2e1bbe7ba6f777&scene=21#wechat_redirect)

[SRC通用案例，第三方接口调用缺陷](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488481&idx=1&sn=2dd2432375ca933ef9b1a39a7706d150&scene=21#wechat_redirect)

[记一次对房东xxx的渗透实战，含技巧！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488363&idx=1&sn=ad8a61a8593cd0c07271d1f7150f19ec&scene=21#wechat_redirect)

["细狗",太细了,就该你出洞（干货案例）](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488336&idx=1&sn=4fc12ad7e24012b7ba2789f0113a0df1&scene=21#wechat_redirect)

[记一次SRC渗透测试实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487518&idx=1&sn=9d4498c7829a31051be9ba9813d367ec&scene=21#wechat_redirect)

[从微信扫描登录到账号接管，细节实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488142&idx=1&sn=874e5fcfabd9dda5cccb9506c0b25fb8&scene=21#wechat_redirect)

[更新|帆软、用友、泛微、蓝凌等常见OA系统综合漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487310&idx=1&sn=f27b0f1199b3f52b086d1c7dc18685d0&scene=21#wechat_redirect)

[Web渗透测试综合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486715&idx=1&sn=1d507a1a89b525e5c1ad4d75d0d9eedc&scene=21#wechat_redirect)

[Java漏洞专项检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487205&idx=1&sn=e0d8353342f7d33fc3ce5bd5e747c861&scene=21#wechat_redirect)

[有趣的Fuzz+BucketTool工具等于双高危！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486814&idx=1&sn=1d114995e1cf5745e824d2018cdbd615&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlND18ovUTvvzp4MagwzrEIAu6ZHoicVWA2YvfmEgZicxv4tvVibeFB8T7w3A/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RLTNmn7FBP7M1kgcoDU768ibicXsxGLOicXwxev9pSGqXnhyeUoMLdBzsial7AQibmYvao9JmGeaf9cQUZuTO6ibo6fg/0?wx_fmt=png)

锐鉴安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RLTNmn7FBP7M1kgcoDU768ibicXsxGLOicXwxev9pSGqXnhyeUoMLdBzsial7AQibmYvao9JmGeaf9cQUZuTO6ibo6fg/0?wx_fmt=png)

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