---
title: URL重定向挖掘技巧，含实战案例
url: https://mp.weixin.qq.com/s/pOOwIFIHOW-B231vPUouEw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:20:31.218394
---

# URL重定向挖掘技巧，含实战案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlND9xQiauqIDNWnQ9JvRZCPZzMULmySBBmacjcKkNBwXvj7IwPHicibyDpicA/0?wx_fmt=jpeg)

# URL重定向挖掘技巧，含实战案例

原创

锐鉴安全
锐鉴安全

锐鉴安全

![]()

在小说阅读器中沉浸阅读

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

不管是企业内部或者SRC，URL重定向漏洞可以说是低成本高收益的一种漏洞，是安全评估比备的一个评估点，为此特分享一期关于URL重定向漏洞的挖掘技巧，详情见实战。

号外号外，免费的睿鉴安全知识库上线了。点击下发链接，福利直达！！

模块介绍

安全知识模块主要会放一些学习材料以及之前个人的一些实战案例，目前已更新资源，含两期案例集合，还在持续上新中，请各位师傅持续关注。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVKwN5JjOXubmpyFsNC938GVwQteESI7kjib1zFMVOz9prUTzuoo67VFkbDqaZu4vs1ly5YZF5llibriafs4oCRYZKLlaJdASpyu9Q/640?wx_fmt=png&from=appmsg)

资源中心主要会放一些个人经常用到的工具，做成了一个集合，目前已发布十几款工具，后续各位师傅可以直接在这里获取到下载链接。一站式获取到你想要的工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVJqmUnlq2icmasHLJ6X1qY9ULUG7EtTXjn0T7MHK7BOb8LBoO3mjJjh0EibWOclvOE1pUjTH0T6l6jWa9at2XYHMnAUgicdNILwMY/640?wx_fmt=png&from=appmsg)

**2**

**实战过程**

话不多说，直接介绍常见URL重定向的漏洞场景。

场景一

Url 重定向是程序员误信了攻击者的输入而将网站重定向到另一个站点，这通常通过 url参数、HTML<meta>刷新标签、DOM 中的 window 对象的 location 属性来实现的很多 Web 网站都是通过在原始 URL 的参数中设置目标 URL 来有意实现用户访问的重定向的。

应用程序通过使用这个参数来告诉浏览器向目标 URL 发送一个 GET 请求。如下。

https://www.baidu.com/?redirect\_to=https://www.Email.com

场景二

HTML<meta>标签和 JavaScript 都可以重定向浏览器。HTML<meta>标签可以告知浏览器刷新网页，并向标签中的 content 属性定义的 URL 发起 GET 请求。

下面是一个例子:

<meta http-equiv=' 'refresh" content="0; ur1=https://www. Baidu. com/">

content 属性定义了浏览器发起 HTTP 请求的两个步骤。

首先，content 属性定义了浏览器在向 URL 发起 HTTP 请求前需要等待的时间，在本例中，这个时间是 0 秒。

其次,content 属性确定了浏览器向其发起 GET 请求的网站中 URL 的参数。

在本例中，这个参数是 https :/ /wWW. Baidu.com.当我们具有控制<meta>标签的 content 属性的能力时,或者通过其他漏洞能够注人他们自己的标签时，就可以利用这种重定向行为。

场景三

JavaScript修改文档对象模型(DOM)中window对象的location属性来实现重定向用户。DOM 是用于 HTML 和 XML 文档的 API.它允许开发者修改网页的结构、风格和内容。因为 location 属性表示了请求将被重定向到哪里，浏览器将立刻解释 JavaScript 脚本并重定向到 指定的 URL。

如下。

window.location = https://www.baidu. com/

window.location.href=https:/www.baidu.com

window.location.replace(htts://ww. baidu.com)

实战案例

01.某里的 src 案例

这是一个购物商城的卖家后台的漏洞，我们在浏览时突然发现一个 get 参数是跳转到货物供应链的站点：

www.xxx.xxx.com/oauta/authurl/?targeturl=www.gongyinglian.xxx.xxx.cn

我们可以看见参数 targeturl?=后面跟着跳转的参数,然后我们将参数修改为www.baidu.com

即可跳转到百度，收获一枚url跳转漏洞，提交平台并获取了赏金。

02.某企鹅 src

场景是对一个视频分享它会生成一个二维码跳转到我们要分享的视频，可我们可以在生成二维码的时候进行抓包导致url跳转漏洞。可以看到下图有个url参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVLzSzeNo3chClAibiay7aUtFiasgkCbaIgw4WGZuGwxqXP0rRXPzDoDG6dTAiaT0D9Z26tSXHvIkWMjp4FvicmFDL1zjJ4M8DwhtREk/640?wx_fmt=png&from=appmsg)

修改该地址为 https://www.baidu.com,修改完成后，刷新该界面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVKt7zoUlcbkyoRI5ThzDNbpT9UZR4CaYlxovHsnYJoB1mibiaSXwNpHSsXeCeHEYIopYnkArPF5qooO0yiaXuP9ptNqG0icTS5uTibE/640?wx_fmt=png&from=appmsg)

手机扫描二维码后跳转至baidu。

![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVLfx13oFYNrXZofqpx644wYWw7FgNOrBNaTQxQX9VFjM11rMvMSO3x0kIlqgAicVctwDHnzmpQz9wvXoBkIonKFqZbMAFg3AxVs/640?wx_fmt=png&from=appmsg)

**3**

**经验总结**

URL重定向的漏洞分享结束了，希望对各位师傅有帮助。

往期好文推荐

[记一次"高危"逻辑漏洞挖掘实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487704&idx=1&sn=f2f296b6870ed8ddbaa6d142c93ea114&scene=21#wechat_redirect)

[安服仔薅洞必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487810&idx=1&sn=6fb51d171d6546386a5bdbda662046f7&scene=21#wechat_redirect)

[记一次SRC支付漏洞实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487822&idx=1&sn=0cfb1fd7754a8bb5fee12d44e450cd53&scene=21#wechat_redirect)

[记一次SRC渗透测试实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487518&idx=1&sn=9d4498c7829a31051be9ba9813d367ec&scene=21#wechat_redirect)

[从微信扫描登录到账号接管，细节实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488142&idx=1&sn=874e5fcfabd9dda5cccb9506c0b25fb8&scene=21#wechat_redirect)

[更新|帆软、用友、泛微、蓝凌等常见OA系统综合漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487310&idx=1&sn=f27b0f1199b3f52b086d1c7dc18685d0&scene=21#wechat_redirect)

[Web渗透测试综合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486715&idx=1&sn=1d507a1a89b525e5c1ad4d75d0d9eedc&scene=21#wechat_redirect)

[Swagger漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487229&idx=1&sn=07acbbae48db8862efe4bb8062056a96&scene=21#wechat_redirect)

[Java漏洞专项检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487205&idx=1&sn=e0d8353342f7d33fc3ce5bd5e747c861&scene=21#wechat_redirect)

[渗透测试集成工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487068&idx=1&sn=e343013c9f5a4f736865236e6dfd4bf0&scene=21#wechat_redirect)

[AntiDebug\_Breaker最新版,Hook必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486930&idx=1&sn=2684c990c45276e6fb23de5c48a1c85a&scene=21#wechat_redirect)

[有趣的Fuzz+BucketTool工具等于双高危！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486814&idx=1&sn=1d114995e1cf5745e824d2018cdbd615&scene=21#wechat_redirect)

[推荐一款资产“自动化”筛选工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486679&idx=1&sn=288fe9f4312c3267c33765cfa9e3ab06&scene=21#wechat_redirect)

[EDU SRC学号、账号等敏感信息收集工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486657&idx=1&sn=847f77601dd94eed5a5b04b5bf8176a1&scene=21#wechat_redirect)

[Jeecg-boot最新漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486651&idx=1&sn=70d0e3d5ac4920684f52a4ee52531854&scene=21#wechat_redirect)

[js.map文件还原组合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486582&idx=1&sn=a08daa5cc01f04b813d827e5d8bf444b&scene=21#wechat_redirect)

[Nacos漏洞检测专项工具,攻防必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486606&idx=1&sn=595219ca87296bd633d89d0e966d40a6&scene=21#wechat_redirect)

[微信公众号，微信小程序，钉钉,飞书等第三方平台接管工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486471&idx=1&sn=1a9ddf83c74be73ab70bbbf202771a19&scene=21#wechat_redirect)

入交流群扫下方二维码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVJPZ5SwuG3vOJxaKLd9l42U3Wic1TTXEkV2ic5gaNywwRnrrVRnBJVrwH3SLOEoJq6oia64VUwgJ7P0F1MtwMIvr6RL1jXSMtjjYQ/640?wx_fmt=png&from=appmsg)

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