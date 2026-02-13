---
title: 重磅发布，睿鉴安全知识库小程序上线了！
url: https://mp.weixin.qq.com/s/iRMZFVcCC5UmtbszzYn5Cg
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:14:26.261939
---

# 重磅发布，睿鉴安全知识库小程序上线了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlND9xQiauqIDNWnQ9JvRZCPZzMULmySBBmacjcKkNBwXvj7IwPHicibyDpicA/0?wx_fmt=jpeg)

# 重磅发布，睿鉴安全知识库小程序上线了！

原创

锐鉴安全
锐鉴安全

锐鉴安全

![]()

在小说阅读器中沉浸阅读

g'weigweiID

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

为了更好的将相关的网络安全资源分享给大家，联合多个师傅，在小程序上搭建了一个知识库“睿鉴安全知识库”，目前是免费。

目前涵盖了网络安全知识，安全工具、资源中心等三个模块。主要功能如下图，希望各位师傅在 春节归乡途中不孤独。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVLbSOBtWRx7yZrd6E3SwSSfI7biaMdbQ6ribtdD4kd5pnhXYXBcHV4ic5G6tXqck0aV7ldQHvG0ViaiahO35otzxHyZ97b6SVN1lhFE/640?wx_fmt=png&from=appmsg)

高铁上信号不好时,打开睿鉴安全知识库,无需复杂加载,就能浏览分类清晰的网络安全知识库,从基础防护技巧到进阶漏洞分析,图文并茂易理解，十几个小时的旅途转瞬即逝，到站就多学一个实用知识点！

春节宅家想补短板的话，打开睿鉴安全知识库整合了海量安全学习资料、工具安装包不用再全网到处找资源,一键就能获取。

模块介绍

安全知识模块主要会放一些学习材料以及之前个人的一些实战案例，目前还在持续上新中，请各位师傅持续关注。

资源中心主要会放一些个人经常用到的工具，做成了一个集合，后续各位师傅可以直接在这里获取到下载链接。一站式获取到你想要的工具。

工具模块的话，目前没放什么功能，后续会根据实际的情况，进一步优化。

彩蛋，后续会发布个人近期开发的安全工具！！请持续关注哦。

赶快去试用获取你想要的资源吧！！

往期好文推荐

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

[经典的前端鉴权绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487869&idx=1&sn=33bb92121a1a4ca9bea2adcf4945e9ba&scene=21#wechat_redirect)

[安服仔薅洞必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487810&idx=1&sn=6fb51d171d6546386a5bdbda662046f7&scene=21#wechat_redirect)

[记一次SRC支付漏洞实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487822&idx=1&sn=0cfb1fd7754a8bb5fee12d44e450cd53&scene=21#wechat_redirect)

[记一次"高危"逻辑漏洞挖掘实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487704&idx=1&sn=f2f296b6870ed8ddbaa6d142c93ea114&scene=21#wechat_redirect)

[记一次SRC渗透测试实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487518&idx=1&sn=9d4498c7829a31051be9ba9813d367ec&scene=21#wechat_redirect)

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