---
title: Google Earth 实景三维数据下载实战
url: https://mp.weixin.qq.com/s/vzRcyt0AKGm2ZaDJisdIuQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:52.591734
---

# Google Earth 实景三维数据下载实战

# Google Earth 实景三维数据下载实战

原创

mapxiaotu
mapxiaotu

空天感知

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# Google三维实景数据下载的完整可用链路

Google Earth上有比较丰富的世界上部分国家地区的三维实景数据，不管是做各种试验还是用在课题上，效果都还挺好。

但google的数据基本只能在线浏览，或者使用付费API调用，google杜绝本地下载使用。

我搭了一个下载服务，后端通过解析Google实景数据的API，就可以方便的根据区域下载三维成果了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPthSoK8qdgff23QjMK6qxGINZh6zM9L1dD0reUOaf9Jmze8Z7frTvIkR6eLLFRibvnW2ia4QiclrMQTL80NFiceCHtcnraYduwCkGU/640?wx_fmt=webp&from=appmsg)

旧金山市中心 0.2 km²、18 级细节，35.9 万三角面，ZIP 包 218 MB。级别拉到 21 级只框一栋楼，能拿到 1770 个节点、457 MB 的单体建筑模型。

## 三维数据解析思路

Google Earth 的三维实景内部，是将整个地球当成一个立方体不断八等分，目标下载区域对应树上的一批节点，每个节点挂一份网格加一张贴图。

下载，就是把这棵树上落在这块范围内的节点全摘下来，拼成一张网格。

## 下载服务使用

页面设计的比较简单粗暴，框选区域执行下载即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cemuAg1hRPtbVWZtHWVAgPA3cj1638RPrvZSCESbQwhiaq8ibHEG8Epfw81a8KLIk3WkLKnBVDlxt6ecrcK5fwYwUXLJFN0T3X9bBoBx8C374/640?wx_fmt=webp&from=appmsg)

下完点「下载 ZIP」，解压得到 model.obj + model.mtl + 贴图，Blender 里 File → Import → Wavefront 直接导。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPsxtFxGVQqGqEZsKAsjkq8ezZlsqOM9I7AEFfbTuIhKLm6I6vI94LKD4ic0qOKyP6AY4NU894bnk288AJ7n1Ojohibic79scGKf78/640?wx_fmt=webp&from=appmsg)

Blender视口

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPsXicvxYlvxM6kxKicNrdv3QHETE50NtLQGKTTUX16RZAm2RPHW90GFQ4nibwYZxo88ICtlWX2hV2rJAbhJE4ySrI7wCZ5ic111qOY/640?wx_fmt=webp&from=appmsg)

Blender渲染

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPtXJEK9Ng8icnssodmfWE3SXC8jicXTYJSJj1l5WvTKIalcKInYMr7o8b4BumH4xicXPSwCR1Saj4BW27EtWbbtdnNmhD1MGpR5lY/640?wx_fmt=webp&from=appmsg)

白模

换成法线着色能看清几何密度：街道高差、建筑退台、裙房和天桥都是独立建模的。

## 一些不足

细节上来讲，Google上生产的数据还是有部分缺陷，但瑕不掩瑜。

覆盖不均匀。核心区能下得很深，郊区、山区、新地块可能停在浅层甚至没有节点，模型上就是几个洞——上面视口截图里中部偏下那几处就是。

建筑侧面纹理是从航拍图硬投影的，近看会拉伸会糊，屋顶才是精修区。鸟瞰、场景底、体量分析够用；贴脸镜头或精确立面还得自己补。

输出是局部坐标下的居中缩放模型，不带经纬度。要放回 GIS 或按真实米制对齐，得自己反算那套变换。

很早之前跟部分从事QB工作的公司聊过，他们都是专门有人来逆向写这些下载程序，抓取Google的数据。从前看着异常复杂神秘的工作，而今在AI的支撑下，似乎也能被常人所掌握了。

有数据抓取相关需求可以联系文末微信合作～

`往期推荐：`

[让AI“读懂”12000+景SAR影像：开源SAR平台重大更新，接入大模型你也可以实现以文搜图](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247488734&idx=1&sn=d045ef3e00551d2562e24413dab1bfe2&scene=21#wechat_redirect)

[也说遥感共性产品，行业需要什么样的遥感产品？](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486926&idx=1&sn=66ad7dc53a491a5c9068e6b4684cbb03&scene=21#wechat_redirect)

[看水利部水利遥感星座战略布局，机遇与挑战并存](http://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486470&idx=1&sn=8cac97764abc7e9245f86848dd08e2ca&chksm=ea6d9db9dd1a14af59370e49bcf8ee8e5ba2da77d1b5658589b68c6d649ff302627d446d071e&scene=21#wechat_redirect)

[Umbra开源雷达影像下载工具开发实践](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486877&idx=1&sn=15bb7e1fa63a69c07bf78df5e668758a&scene=21#wechat_redirect)

[NASA与微软联合推出“Earth Copilot”，“智能助手“或成为行业产品标配](http://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486590&idx=1&sn=869ed4f61721ebc13009dd121b105b90&chksm=ea6d9dc1dd1a14d7146f6faee440b3c3e6526d673c10f990d3f7d633b45350eec0f51aae7e4f&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjdEW9c30onjJcgk6LHVj8znEw3pAFsRY0RgWLfXfGOVGNfqjsgmQxVALISuFh3ovbrUZbOEyX49Q/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

笔者长期从事人工智能、遥感、大模型等业务

欢迎添加微信交流

（微信号：mapxiaotu）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ObyhaySm97WZNjpySwibqk7H5ntMHKzv68D9ES1ajKEoa99iaKyw0UHfrzyqxcAe0RgoS61lwXicia92djIK593Atg/0?wx_fmt=png)

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