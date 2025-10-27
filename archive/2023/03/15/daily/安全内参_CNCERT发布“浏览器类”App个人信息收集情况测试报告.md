---
title: CNCERT发布“浏览器类”App个人信息收集情况测试报告
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247508064&idx=2&sn=5ca0aecc8b6e9c2b8188c6f1b92f1c24&chksm=ebfae740dc8d6e56c9fa1740224995a6f564d9acb638797398d14513f3d8b3596177e6218c5b&scene=58&subscene=0#rd
source: 安全内参
date: 2023-03-15
fetch_date: 2025-10-04T09:36:20.304856
---

# CNCERT发布“浏览器类”App个人信息收集情况测试报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vZ0OWgVoiaC7PicV8xMib4sOBeuxzvh9BJvBaAjOk9MwNibWNkLoEW10AcCPrfdjwXoMvksibueQo11EQ/0?wx_fmt=jpeg)

# CNCERT发布“浏览器类”App个人信息收集情况测试报告

安全内参

**关注我们**

**带你读懂网络安全**

近期，中国网络空间安全协会、国家计算机网络应急技术处理协调中心对“浏览器类”公众大量使用的部分App收集个人信息情况进行了测试。测试情况及结果如下：

**一**

**测试对象**

本次测试选取了19家应用商店⁽¹⁾累计下载量达到1亿次的“浏览器类”App，共计9款，其基本情况如表1。

表1  9款App基本情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHg1Ynp0UoRnGqONLiaEx2b64ny1lByGdbQnyspy8N21zdaQ18JwGLm7A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**二**

**测试方法**

****（一）测试环境****

本次测试选取相同品牌、型号的手机终端，安装相同版本安卓操作系统，分别部署9款App，在相同网络环境下进行同步操作。

****（二）测试场景****

以完成一次互联网信息浏览活动作为测试单元，包括启动App、搜索信息、访问信息3种用户使用场景，以及后台静默应用场景⁽²⁾。

****（三）测试内容****

本次测试包括系统权限调用、个人信息上传、网络上传流量3项内容。

**三**

**测试结果**

****（一）系统权限调用情况****

测试发现，9款App在4种场景下调用了位置、设备信息、剪切板、应用列表、相册5类系统权限，未发现调用麦克风、通讯录等其他权限。

（1）在启动App场景中，调用系统权限种类最多的为悟空浏览器（5类），调用系统权限次数最多的为UC浏览器（88次）。具体情况如表2。

表2  启动App场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHAmTSsA4Gh4JZ907hxOJOLEySFWibI4qAmg1SiaCpTvjz9JQG7TicibY3Eg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（2）在搜索信息场景中，调用系统权限种类最多的为小米浏览器和搜狗浏览器极速版（均为3类），调用系统权限次数最多的为小米浏览器（12次）。具体情况如表3。

表3  搜索信息场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrH1V0z6RcvN9j15PZqvUgOibETrA47fYb18Bf9rQZdWtDReiaL2iaKC6G9w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（3）在访问信息场景中，通过浏览器打开网站时，调用系统权限种类和次数最多的均为悟空浏览器（2类、5次）；通过浏览器下载文件时，调用系统权限次数最多的为UC浏览器和悟空浏览器（均为2次）。具体情况如表4。

表4  访问信息场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHiat4KN175br1icZM6zrhRD1qAPQy2UglhQ6oJRdsMLqgrSiccn7TGgLUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（4）在后台静默场景中，调用系统权限种类最多的为UC浏览器、夸克、360浏览器、悟空浏览器（均为2类），调用系统权限次数最多的为360浏览器（16次）。具体情况如表5。

表5  后台静默场景调用系统权限情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHbWmeNic9iafPzVhibMx9m0MKicpdMFclSla9IzmWqqP4sWb2T2LDUM0PTg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

****（二）个人信息上传情况****

测试发现，9款App上传了4种类型个人信息⁽³⁾：①位置信息，包括经纬度、街道地址、当前连接Wi-Fi MAC地址、当前连接基站信息、周边可用Wi-Fi MAC地址；②唯一设备识别码，包括IMEI（国际移动设备识别码）、Android ID（安卓ID）、OAID（开放匿名设备标识符）、手机MAC地址；③应用列表信息，包括手机上已安装、新安装、新卸载的应用信息；④用户在App内的截图操作信息。

（1）在启动App场景中，个人信息上传种类最多的为UC浏览器（4类）。具体情况如表6。

表6  启动App场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHIJD1tRichtCUofrqVickU8CfudpsJ8QyKBVJJQX1uu2u9w4rIfeDQgug/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（2）在搜索信息场景中，个人信息上传种类最多的为悟空浏览器（2类）。具体情况如表7。

表7   搜索信息场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHFu4iaWl4pV3hOmaibkEE8nmZMd3g7ia9HiaMN7dW5xrv9H5uapmpqWesyw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（3）在访问信息场景中，通过浏览器打开网站时，个人信息上传种类最多的为小米浏览器和悟空浏览器（均为2类）；通过浏览器下载文件时，个人信息上传种类最多的为UC浏览器和360浏览器（均为2类）。具体情况如表8。

表8  访问信息场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHwR6pg1HfAt9jL54V3Z56UTwVSlj0hjgBPp67TW8gtHSibLOqRojlZ6Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

（4）在后台静默场景中，个人信息上传种类最多的为UC浏览器（3类）。具体情况如表9。

表9  后台静默场景个人信息上传情况

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHIq0cyQtuN3og9YDzou0w2FlXBTz60gpa6bJIh7H9TmqXYGnQ7M1ticw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

****（三）网络上传流量情况****

（1）9款App在用户完成一次网站浏览活动（启动App、搜索信息、打开网站）时，上传数据流量平均⁽⁴⁾最多的为悟空浏览器，约为1608KB；平均最少的为小米浏览器，约为472KB。具体情况如图1。

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHlMKOJqTCfFWic2SqKfvCKP3xIicKnJEIRWA5yFExmcrtOENnJiafozibAQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1  完成一次网站浏览活动的平均上传数据流量（单位：KB）

（2）9款App在用户完成一次文件下载活动（启动App、搜索信息、下载文件）时，上传数据流量平均⁽⁵⁾最多的为QQ浏览器，约为1994KB；平均最少的为小米浏览器，约为152KB。具体情况如图2。

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHgaR6kSaSX4vNkSxRkfWIsWKuNjMSUtIABh0UKQZiaarj4gK9YbTrgkg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2  完成一次文件下载活动的平均上传数据流量（单位：KB）

（3）9款App后台静默12小时，上传数据流量平均⁽⁶⁾最多的为UC浏览器，约为2506KB；平均最少的为华为浏览器，约为87KB。具体情况如图3。

![](https://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz66JGFOyQopcpc5SJ7bTtMrHAjVthyfb5B3COY6Tfibst7IBxpLFu7XFOQt4mb2xAKYPb2cUGG0c3hA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图3  后台静默12小时平均上传数据流量（单位：KB）

**注释：**

⁽¹⁾包括华为应用市场、小米应用商店、腾讯应用宝、OPPO软件商店、VIVO应用市场、360手机助手、百度手机助手、豌豆荚手机助手、历趣应用商店、乐商店、魅族应用商店、移动MM商店、太平洋下载、中关村在线、木蚂蚁安卓应用市场、多特软件站、华军软件园、西西软件园、绿色资源网。

⁽²⁾启动App指用户点击浏览器图标启动App至首页加载完毕；搜索信息指用户搜索一个网站或文件，至搜索结果加载完毕；访问信息指用户点击一条搜索结果进行浏览（当搜索结果为一个网页时）或下载（当搜索结果为一个文件时）；后台静默指用户启动浏览器后，直接切换到后台保持静默状态。

⁽³⁾不包含用户访问互联网产生的交互信息。例如，用户浏览银行网站时，可能向网站传输身份证号、银行卡号、取款密码等信息，在此过程中浏览器仅按照网络协议向网站转发数据，本身不收集上述信息。

⁽⁴⁾共重复测试10次。

⁽⁵⁾共重复测试10次。

⁽⁶⁾共重复测试6次。

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