---
title: CNCERT发布“地图导航类”App个人信息收集情况测试报告
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247508084&idx=2&sn=f46b7d66fe9f9422755320a72432df4e&chksm=ebfae754dc8d6e42c41b9cb9796eff5f9ba046ea95817bfbff5cf3531ce507f25f0becb3e121&scene=58&subscene=0#rd
source: 安全内参
date: 2023-03-16
fetch_date: 2025-10-04T09:45:24.732881
---

# CNCERT发布“地图导航类”App个人信息收集情况测试报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s0PoAvGEMNzrPrrOMdfXJX2cNgEzmzoSeXXUlrp8jymYNibgDSIIB1iaVv0UPKlJvQql4l3who8n7A/0?wx_fmt=jpeg)

# CNCERT发布“地图导航类”App个人信息收集情况测试报告

安全内参

**关注我们**

**带你读懂网络安全**

近期，中国网络空间安全协会、国家计算机网络应急技术处理协调中心对“地图导航类”公众大量使用的部分App收集个人信息情况进行了测试。测试情况及结果如下：

**一**

**测试对象**

本次测试选取了19家应用商店⁽¹⁾累计下载量达到5000万次的“地图导航类”App，共计3款，其基本情况如表1。

表1  3款App基本情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHYPRYlLlOYmmPH8NdAM7ZK3IS0jJJjA6HiaXN80VaGiaH7KyBtA6tT2GQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**二**

**测试方法**

****（一）测试环境****

本次测试选取相同品牌、型号的手机终端，安装相同版本安卓操作系统，分别部署3款App，在相同网络环境下进行同步操作。

****（二）测试场景****

以完成一次地图导航活动作为测试单元，包括启动App、搜索地点、点击导航3种用户使用场景，以及后台静默应用场景⁽²⁾。

****（三）测试内容****

本次测试包括系统权限调用、个人信息上传、网络上传流量3项内容。

**三**

**测试结果**

****（一）系统权限调用情况****

测试发现，3款App在4种场景下调用了位置、设备信息、麦克风、剪切板、应用列表5类系统权限，未发现调用相机、通讯录等其他权限。

（1）在启动App场景中，调用系统权限种类最多的为高德地图和百度地图（均为3类），调用系统权限次数最多的为百度地图（127次）。具体情况如表2。

表2  启动App场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHFmxFJ5tAJCYxzXdBoTkUlh5l4JichibOuZ16AhTDvtBIqAtEvgDWtXPw/640?wx_fmt=png)

（2）在搜索地点场景中，通过文字输入方式进行搜索时，调用系统权限种类最多的为高德地图和百度地图（均为2类），调用系统权限次数最多的为腾讯地图（123次）；通过语音交互方式进行搜索时，调用系统权限种类最多的为百度地图（4类），调用系统权限次数最多的为腾讯地图（217次）。具体情况如表3。

表3  搜索地点场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHAnsDRictya0hQuAT4tv2ficvognNrq2aib1WAMCFNf4vvwTUmTzCmgfAg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（3）在点击导航场景中，调用系统权限种类最多的为高德地图和百度地图（均为2类），调用系统权限次数最多的为腾讯地图（62次）。具体情况如表4。

表4  点击导航场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHG2icR1dMW9wuoPdLjkVezR9p3VXgmz7jT3Kr6FmYQfOSJ9hqsO7HEwQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（4）在后台静默场景中，3款App调用系统权限种类均为2类，调用系统权限次数最多的为腾讯地图（282次）。具体情况如表5。

表5  后台静默场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHfSYxFhOxjVDdibVwmvN7SO2Sd17fSCN67WCtvJE9QQn1xhRGdFXW4gQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

****（二）个人信息上传情况****

测试发现，3款App上传了5种类型个人信息：①位置信息，包括经纬度、街道地址、当前连接Wi-Fi MAC地址、当前连接基站信息、周边可用基站信息、周边可用Wi-Fi MAC地址；②唯一设备识别码，包括Android ID（安卓ID）、手机MAC地址；③剪切板内容信息，主要是地点分享链接；④应用列表信息，包括手机上已安装、新安装和新卸载的应用信息；⑤地点信息，主要是地点名称，包括文本或语音形式。

（1）在启动App场景中，个人信息上传种类最多的为高德地图和百度地图（均为3类）。具体情况如表6。

表6  启动App场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHWfLA2oXyoT4E29UxjwsFEyUaickicnA2TkaRoyk3vgPp51MlQomENnkw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（2）在搜索地点场景中，通过文字输入方式进行搜索时，个人信息上传种类最多的为高德地图和腾讯地图（均为3类）；通过语音交互方式进行搜索时，个人信息上传种类最多的为百度地图（4类）。具体情况如表7。

表7  搜索地点场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHtVgrmmBN1FL7dYBicFx0YAEPRXxmWYiaqXfFxKAKQVuPiaiccjApJlwKmA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（3）在点击导航场景中，个人信息上传种类最多的为高德地图和百度地图（均为2类）。具体情况如表8。

表8  点击导航场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHfUV7xU5yOkZzWtpvF9JUicCMR2UBCFHQlRqweSgMkzI5yPHPtuBoyPQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（4）在后台静默场景中，个人信息上传种类最多的为高德地图（3类）。具体情况如表9。

表9  后台静默场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHzvQ00Dibv9XsbuWHibfmZLENria96jGYWBREjjib2t1uMjE0EGXXbbykeg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

****（三）网络上传流量情况****

（1）测试发现，3款App在用户通过文字输入方式完成一次地图导航活动（启动App、通过文字输入搜索地点、点击导航）时，上传数据流量平均⁽³⁾最多的为腾讯地图，约为2584KB；平均最少的为百度地图，约为889KB。具体情况如图1。

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHrOZ8F78Hic3JicEQqk43uRFySOyltImzZLqoyazYBzcIFYtoHD5wI6Qg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1  通过文字输入方式完成一次地图导航活动的平均上传数据流量（单位：KB）

（2）测试发现，3款App在用户通过语音交互方式完成一次地图导航活动（启动App、通过语音交互搜索地点、点击导航）时，上传数据流量平均⁽⁴⁾最多的为腾讯地图，约为2242KB；平均最少的为百度地图，约为756KB。具体情况如图2。

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHYZIOglQCjnaCXsoC1COHHd3BUdPOJXVZoRr77P09VKdY13P4y42GJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2  通过语音交互方式完成一次地图导航活动的平均上传数据流量（单位：KB）

（3）测试发现，3款App后台静默12小时，上传数据流量平均⁽⁵⁾最多的为腾讯地图，约为7830KB；平均最少的为高德地图，约为1363KB。具体情况如图3。

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrH5quZcn7Dc36hmNmmrR9GlQibAGwPCzJhSGF3jJ4n5KkEfDL9vica0gEA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图3  后台静默12小时平均上传数据流量（单位：KB）

**注释：**

⁽¹⁾包括华为应用市场、小米应用商店、腾讯应用宝、OPPO软件商店、VIVO应用市场、360手机助手、百度手机助手、豌豆荚手机助手、历趣应用商店、乐商店、魅族应用商店、移动MM商店、太平洋下载、中关村在线、木蚂蚁安卓应用市场、多特软件站、华军软件园、西西软件园、绿色资源网。

⁽²⁾启动App指用户点击图标至主界面加载完成；搜索地点指用户通过文字输入或者语音交互方式搜索特定地点，点击并加载地点详情；点击导航指用户点击导航按钮至导航界面加载完毕；后台静默指用户启动App后，直接将App切换至后台保持静默运行状态。

⁽³⁾共重复测试10次。

⁽⁴⁾共重复测试10次。

⁽⁵⁾共重复测试6次。

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：国家互联网应急中心CNCERT

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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