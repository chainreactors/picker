---
title: 安全评估必备插件-BurpAPIFinder
url: https://mp.weixin.qq.com/s/ZwyVncT3muay_KTu9h4CAA
source: Doonsec's feed
date: 2026-07-20
fetch_date: 2026-07-21T05:01:46.492512
---

# 安全评估必备插件-BurpAPIFinder

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qvoCyTM5aVKVx1CU9NkuiaxD7txlGWeUgFlDHyy3hDA7b0sMQREiacbJJnC4aGrz6xcsGsE4cNscGLqLypj6f6bHETBT6LLOWiblAb91McjstE/0?wx_fmt=jpeg)

# 安全评估必备插件-BurpAPIFinder

锐鉴安全

![]()

在小说阅读器读本章

去阅读

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

**工具介绍**

攻防演练过程中，我们通常会用浏览器访问一些资产，但很多未授权/敏感信息/越权隐匿在已访问接口的html、JS文件等，通过该BurpAPIFinder插件我们可以：

1、发现通过某接口可以进行未授权/越权获取到所有的账号密码、私钥、凭证。

2、发现通过某接口可以枚举用户信息、密码修改、用户创建接口。

3、发现登录后台网址。

4、发现在html、JS中泄漏账号密码或者云主机的Access Key和SecretKey。

5、自动提取js、html中路径进行访问，也支持自定义父路径访问。

![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVIOjJAqsccWTnor0W8IkzTj8yY56m9fJf4E0iceiaqB1DEPh7vug95icsSVsmicXnAVfLsgaBPemqQGh2b2GX8VZgMJVArpDp9ib88Q/640?wx_fmt=png&from=appmsg)

主要功能

1、提取网站的URL链接和解析JS文件中的URL链接(不单单正则、支持多种模式提取)。

2、前段界面可自行定义敏感关键词、敏感url匹配。

3、界面可配置的开启主动接口探测、敏感信息获取。

4、支持用户自定义父路径重新开发扫描任务。

5、集成主流攻防场景敏感信息泄漏的指纹库。

安装方法

在 Burp Suite → Extender → Add → Java → 选择BurpAPIFinder

.jar

下载方式见文末。

注意：记得星标，才能第一时间接收到文章更新通知！！！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVIvqaH7S6chxxI05Eic8qlMD74bCk5O0mfQzUaGZWbyjKTJoTjweqKZQYxknQ0cxdHILUoibDFq1MXfVkGFfNV2ZHhus9YMZvZDw/640?wx_fmt=png&from=appmsg)

期待你的关注

往期好文推荐

[记一次SRC实战Getshell](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488672&idx=1&sn=262836b82eb5c83b5b7a55f4f3e894e1&scene=21#wechat_redirect)

[武装你的浏览器-Storage Inspector](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488938&idx=1&sn=28b8235768d2da3eb96cc1b9c3a44250&scene=21#wechat_redirect)

[企业SRC必备工具，ByPass WAF](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488868&idx=1&sn=8cab9a7e99d2be64e749f5114c564bad&scene=21#wechat_redirect)

[某众测实战案例，简单拿下零花钱](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488897&idx=1&sn=e9b0a6378601ad7efd8620dfe6fffa10&scene=21#wechat_redirect)

[某TOP高校的高危实战案例](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488888&idx=1&sn=3fe8229c66a7d6c8479507e01a4dceae&scene=21#wechat_redirect)

[记录一次RCE实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488842&idx=1&sn=03e9d8bbee225932739cda6b41b95f04&scene=21#wechat_redirect)

[入门级的赏金获取案例](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488830&idx=1&sn=3adc9509716c56b758af8f6ea7f46136&scene=21#wechat_redirect)

[某985证书站实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488796&idx=1&sn=af6051dfe22f0bdf165d3e79d2891c9a&scene=21#wechat_redirect)

[信息收集工具-DigDeep](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488851&idx=1&sn=b427275a1f6da69fb74caeb9a7b17bc7&scene=21#wechat_redirect)

[分享一个渗透测试必备的POC速查网站](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488716&idx=1&sn=37bfc3a33edd4078d09782ce47b9bdf2&scene=21#wechat_redirect)

[微信小程序Debugger 神器-First](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488707&idx=1&sn=7291bb3c24491b54e3d07e4451dcd21e&scene=21#wechat_redirect)

[专注于各类注入检测的工具-xia\_tan](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488694&idx=1&sn=a077908fb295e64a151d38dc159ed888&scene=21#wechat_redirect)

["细狗",太细了,就该你出洞（干货案例）](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488336&idx=1&sn=4fc12ad7e24012b7ba2789f0113a0df1&scene=21#wechat_redirect)

[记一次对房东xxx的渗透实战，含技巧！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488363&idx=1&sn=ad8a61a8593cd0c07271d1f7150f19ec&scene=21#wechat_redirect)

[JSHunter助你挖掘JS中的漏洞"宝矿"](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488322&idx=1&sn=776feed1b3a99b0c735cddbde1ace82e&scene=21#wechat_redirect)

[分享1个发现隐藏资产的技巧，附实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488233&idx=1&sn=b9b47437e21fc89e0bccb43879dd62c9&scene=21#wechat_redirect)

[从微信扫描登录到账号接管，细节实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488142&idx=1&sn=874e5fcfabd9dda5cccb9506c0b25fb8&scene=21#wechat_redirect)

[Web渗透测试综合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486715&idx=1&sn=1d507a1a89b525e5c1ad4d75d0d9eedc&scene=21#wechat_redirect)

[Java漏洞专项检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487205&idx=1&sn=e0d8353342f7d33fc3ce5bd5e747c861&scene=21#wechat_redirect)

[有趣的Fuzz+BucketTool工具等于双高危！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486814&idx=1&sn=1d114995e1cf5745e824d2018cdbd615&scene=21#wechat_redirect)

下载方式：关注公众号，回复“260720”获取下载链接

![](https://mmbiz.qpic.cn/mmbiz_gif/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlND18ovUTvvzp4MagwzrEIAu6ZHoicVWA2YvfmEgZicxv4tvVibeFB8T7w3A/640?wx_fmt=gif&from=appmsg)

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