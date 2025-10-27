---
title: CNCERT发布“网上购物类”App个人信息收集情况测试报告
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507682&idx=2&sn=f8460a013308fb2b2d673390a73646b8&chksm=ebfa99c2dc8d10d4d13f0cc4104b8fbaa8e9b4dc4a5ecb5873d6a59ab47c0c378e2914f7757c&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-02-03
fetch_date: 2025-10-04T05:35:14.004040
---

# CNCERT发布“网上购物类”App个人信息收集情况测试报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sAmVQQC8HeiaEzOAibJEliad0P8zvCRjnhF48v0Xe6pflXZUgtVC300nDSEe1ibu1IhFUX1jJUTymLNA/0?wx_fmt=jpeg)

# CNCERT发布“网上购物类”App个人信息收集情况测试报告

CNCERT

安全内参

近期，中国网络空间安全协会、国家计算机网络应急技术处理协调中心对“网上购物类”公众大量使用的部分App收集个人信息情况进行了测试。测试情况及结果如下：

**一**

**测试对象**

本次测试选取了19家应用商店⁽¹⁾累计下载量排名前10位的“网上购物类”App。10款App基本情况如表1。

表1  10款App基本情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflT3gL69jUNvicJSSssQ7R4iaqAm9ibiakMlX7ABibSoic797jVHibBSsUtBhnAg/640?wx_fmt=png)

**二**

**测试方法**

****（一）测试环境****

本次测试选取相同品牌、型号的手机终端，安装相同版本安卓操作系统，分别部署10款App，在相同网络环境下进行同步操作。

****（二）测试场景****

以完成一次网上购物活动作为测试单元，包括启动App、搜索商品、购物下单3种用户使用场景，以及后台静默应用场景⁽²⁾。

****（三）测试内容****

本次测试包括系统权限调用、个人信息上传、网络上传流量3项内容。

**三**

**测试结果**

****（一）系统权限调用情况****

测试发现，10款App在4种场景下调用了位置、设备信息、剪切板、应用列表4类系统权限，未发现调用相机、麦克风、通讯录等其他权限。

在启动App场景中，调用系统权限种类最多的为拼多多（4类），调用系统权限次数最多的为苏宁易购（357次）。具体情况如表2。

表2  启动App场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflT9hiaKRpUydsIGlPTEicGhjprX6np6SokPjUeC4JxdHYC0ALib6O9lpo7A/640?wx_fmt=png)

在搜索商品场景中，调用系统权限种类最多的为淘宝（3类），调用系统权限次数最多的为苏宁易购（152次）。具体情况如表3。

表3  搜索商品场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflTQ5Befl1Y9lLlzRk8ibSZgleVnGk9tFyic4uVHBxAOvPC0AmDUxUAk4BQ/640?wx_fmt=png)

在购物下单场景中，调用系统权限种类最多的为手机天猫（3类），调用系统权限次数最多的为苏宁易购（255次）。具体情况如表4。

表4  购物下单场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflT6ONgoMicdYsbMZ1QMdybSdBetPFZYeZ7xF28dpuvM0Lcsy8XMfjOQaQ/640?wx_fmt=png)

在后台静默场景中，调用系统权限种类最多的为拼多多（4类），调用系统权限次数最多的为苏宁易购（1199次）。具体情况如表5。

表5  后台静默场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflTm8nItX6WhOJDRLX29pQVVpsr96G5NjnYSIlUHCtx4rWoU0D0GhCqeA/640?wx_fmt=png)

****（二）个人信息上传情况****

测试发现，10款App上传了6种类型个人信息：①位置信息，包括经纬度、街道地址、当前连接WiFi MAC地址、当前连接基站信息、周边可用WiFi MAC地址等；②唯一设备识别码，包括IMEI（国际移动设备识别码）、IMSI（SIM卡国际移动用户识别码）、Android ID（安卓ID）、OAID（开放匿名设备标识符）、手机MAC地址等；③剪切板内容信息，包括商品分享链接、最近复制的文本等；④应用列表信息，包括手机上已安装、正在运行、新安装和新卸载的应用信息等；⑤购物信息，包括商品搜索词、订单信息等；⑥登录信息，包括用户ID、登录状态等。

在启动App场景中，个人信息上传种类最多的为拼多多（4类）。具体情况如表6。

表6  启动App场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflTfzhoPrn1ibyuIfib2fFGo9BOyDS1TZcPFRuelrbpzTibrtPXNcerk7PqQ/640?wx_fmt=png)

在搜索商品场景中，个人信息上传种类最多的为拼多多和手机天猫（均为4类）。具体情况如表7。

表7  搜索商品场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflTlRrTU2FdgQRN467zQ1pzvfwBFwGgXssOfOESJ85WwQsbPC8qASZCUQ/640?wx_fmt=png)

在购物下单场景中，个人信息上传种类最多的为淘宝、京东、苏宁易购（均为4类）。具体情况如表8。

表8  购物下单场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflTUqdrTOvK0ZPC97d1ZnTLDqBsUib2KK1NNLajFB6hPpegpjWd2aHcfwQ/640?wx_fmt=png)

在后台静默场景中，个人信息上传种类最多的为拼多多（3类）。具体情况如表9。

表9  后台静默场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflTS1Afo1AAR2eiaKehcE5Ebicib0n8bgoIxiby6jrNicP3icPibD1kb7E2kqTew/640?wx_fmt=png)

****（三）网络上传流量情况****

测试发现，10款App在用户完成一次网上购物活动（启动App、搜索商品、购物下单）时，上传数据流量平均⁽³⁾最多的为苏宁易购，约为653KB；平均最少的为荣耀亲选，约为115KB。具体情况如图1。

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflTG1bibViaZkJcalWSVIez0AYwknogXrLPBT3Z375yQ7Xafp4vuwiboRagg/640?wx_fmt=png)

图1  完成一次网上购物活动平均上传数据流量（单位：KB）

测试发现，10款App后台静默12小时，上传数据流量平均⁽⁴⁾最多的为手机天猫，约为92KB；平均最少的为唯品会，约为1.4KB。具体情况如图2。

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz67nLE91rSI1QWvom8A4QflTQicD6eiaqMKJLpAlHNmGQN72oqoh6h9WXGNHo5oshskdDDNm7bUWqkjQ/640?wx_fmt=png)

图2  后台静默12小时平均上传数据流量（单位：KB）

**注释：**

⁽¹⁾包括华为应用市场、小米应用商店、腾讯应用宝、OPPO软件商店、VIVO应用市场、360手机助手、百度手机助手、豌豆荚手机助手、历趣应用商店、乐商店、魅族应用商店、移动MM商店、太平洋下载、中关村在线、木蚂蚁安卓应用市场、多特软件站、华军软件园、西西软件园、绿色资源网。

⁽²⁾启动App指用户点击图标至主界面加载完成；搜索商品指用户选中搜索框，输入搜索词，点击搜索并选择第一项搜索结果；购物下单指用户点击购买按钮，选择收货地址，提交订单至确认付款页面；后台静默指用户将App切换至后台保持静默运行状态。

⁽³⁾共重复测试24次。

⁽⁴⁾共重复测试7次。

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