---
title: 武装你的浏览器器-Webpack_extract
url: https://mp.weixin.qq.com/s/aorwPvXv3_ugeiRaN6uPEQ
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:35:33.212729
---

# 武装你的浏览器器-Webpack_extract

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qvoCyTM5aVIRVeaAIJ9ov1joibdsGUpZ4uek1RcNKUPCdnVOwIpsj8M6wgghJKjf10VawdcvrgZIicynYggXNLwOUS1ktTFiaCpNhnxjRoH5tE/0?wx_fmt=jpeg)

# 武装你的浏览器-Webpack\_extract

锐鉴安全

![]()

在小说阅读器中沉浸阅读

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

**免责声明：**请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息、工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任！

**1**

**背景**

分享一款从浏览器侧搞定webpack异步加载js的工具，可以是实现全量文件js文件拉取，并完成分析及结果导出，在浏览器中直接完成信息收集工作。

要的就是简单高效出洞工具，推荐下载。

**2**

**工具介绍**

定位：协助红队人员快速的信息收集，一键自动加载js，一键自动化分析js。

语言：JS开发

功能：一条龙服务，有发现存在Webpack需要读取的js文件，点击提取映射并且可以获取映射js文件，并且支持一键自动加载js、一键分析js。

调用： 脚本借用了HaE内容提取脚本，可以分析异步加载的js文件中的敏感信息，如sfz、手机号、url、token、邮箱等信息。

支持环境：Chrome。

亮点：本工具已多次在攻防、SRC挖掘场景中出货。

使用方法：

1、提取js映射

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVJks4UrA6a6reLzvlRn696Hno0rYxgmwMLLuE6yySK8833heJ5daqjB1jxZ9S3j88FIWexQno76zYM4OMhalibuLQProcetIPaU/640?wx_fmt=png&from=appmsg)

2、一键加载

![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVLjOiahD6uYLXl7CZiamdULdRGdu1KLn41U12BLNIczA8UBickBZSFmkD8HuKXzGCiaY3HRtFBMfXsTpHEZ645iaEcc0Q1tCcFLibib5M/640?wx_fmt=png&from=appmsg)

3、一键分析

分析完成后，自动下载结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVLYS5uicuZ8VoeiaGZBJdRvO9WibZhbbsr0jiawPzoYkS3ib4tSQdBNUFfDa1AeTbPXjO4bqHqEFKcNKZ1ATcZ1mPmSpHv8joQRRCT0/640?wx_fmt=png&from=appmsg)

工具的使用方法：

1、下载以上插件，下载方式见文末；

2、进入浏览器扩展程序-》管理扩展程序；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVLWe0tgQkNsR3hpI8JaUlwNqhEQuHcBz6q9Mu7tic2QXrsW6fDPjk1YV6SzOqGIAO8OgaYcCMZgh76u3YZaHX5go3OYUFxHPbQ4/640?wx_fmt=png&from=appmsg)

3、加载解压后的包。

![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVKQXPDsFxOl9TJkBibVVruKFnpMdVlK5CCTibfxnic2U7QJ6kic3pxpWqhJsicsxDMgib7Nkjgdib12KMStTZo1yBGeSILT1fr5zQ5lG8/640?wx_fmt=png&from=appmsg)

往期好文推荐

[武装你的浏览器-信息收集](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488461&idx=1&sn=330b3bacf6d1cbad8f3fa1f50d2cd159&scene=21#wechat_redirect)

["细狗",太细了,就该你出洞（干货案例）](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488336&idx=1&sn=4fc12ad7e24012b7ba2789f0113a0df1&scene=21#wechat_redirect)

[SRC之实名绑定绕过实战！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488420&idx=1&sn=4e7b4fcff88f7ce347f3bd6241c978f1&scene=21#wechat_redirect)

[SRC通用案例，第三方接口调用缺陷](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488481&idx=1&sn=2dd2432375ca933ef9b1a39a7706d150&scene=21#wechat_redirect)

[记一次对房东xxx的渗透实战，含技巧！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488363&idx=1&sn=ad8a61a8593cd0c07271d1f7150f19ec&scene=21#wechat_redirect)

[通过SSO认证绕过，艰难“拿证”实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488451&idx=1&sn=1e8f509e558f429a5a2e1bbe7ba6f777&scene=21#wechat_redirect)

[JSHunter助你挖掘JS中的漏洞"宝矿"](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488322&idx=1&sn=776feed1b3a99b0c735cddbde1ace82e&scene=21#wechat_redirect)

[分享1个发现隐藏资产的技巧，附实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488233&idx=1&sn=b9b47437e21fc89e0bccb43879dd62c9&scene=21#wechat_redirect)

[更新-大佬的SRC思路，等你来GET](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488407&idx=1&sn=17a9d299d47f8d19735b28ce29995f9f&scene=21#wechat_redirect)

[SRC必备的SSRF插件](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488266&idx=1&sn=34a7dd1fa98025f74cd200438b2c095a&scene=21#wechat_redirect)

[记一次SRC渗透测试实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487518&idx=1&sn=9d4498c7829a31051be9ba9813d367ec&scene=21#wechat_redirect)

[从微信扫描登录到账号接管，细节实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488142&idx=1&sn=874e5fcfabd9dda5cccb9506c0b25fb8&scene=21#wechat_redirect)

[更新|帆软、用友、泛微、蓝凌等常见OA系统综合漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487310&idx=1&sn=f27b0f1199b3f52b086d1c7dc18685d0&scene=21#wechat_redirect)

[Web渗透测试综合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486715&idx=1&sn=1d507a1a89b525e5c1ad4d75d0d9eedc&scene=21#wechat_redirect)

[Swagger漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487229&idx=1&sn=07acbbae48db8862efe4bb8062056a96&scene=21#wechat_redirect)

[Java漏洞专项检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487205&idx=1&sn=e0d8353342f7d33fc3ce5bd5e747c861&scene=21#wechat_redirect)

[有趣的Fuzz+BucketTool工具等于双高危！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486814&idx=1&sn=1d114995e1cf5745e824d2018cdbd615&scene=21#wechat_redirect)

[推荐一款资产“自动化”筛选工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486679&idx=1&sn=288fe9f4312c3267c33765cfa9e3ab06&scene=21#wechat_redirect)

[Jeecg-boot最新漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486651&idx=1&sn=70d0e3d5ac4920684f52a4ee52531854&scene=21#wechat_redirect)

[Nacos漏洞检测专项工具,攻防必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486606&idx=1&sn=595219ca87296bd633d89d0e966d40a6&scene=21#wechat_redirect)

入交流群扫下方二维码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVJPZ5SwuG3vOJxaKLd9l42U3Wic1TTXEkV2ic5gaNywwRnrrVRnBJVrwH3SLOEoJq6oia64VUwgJ7P0F1MtwMIvr6RL1jXSMtjjYQ/640?wx_fmt=png&from=appmsg)

号外：进入下方小程序，获取其他资源。

下载方式：关注公众号，回复“260323”获取下载链接。

![](https://mmbiz.qpic.cn/mmbiz_gif/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlND18ovUTvvzp4MagwzrEIAu6ZHoicVWA2YvfmEgZicxv4tvVibeFB8T7w3A/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

修改于

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