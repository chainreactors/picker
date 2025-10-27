---
title: 【安全圈】大蜘蛛发现针对安卓机顶盒的Android.Vo1d病毒 感染超过130万台设备
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064389&idx=4&sn=45061c2de3db8adc3b2ffb67dcfae3cc&chksm=f36e66c5c419efd3a666da7de1773238df54749b1afae2551d4af0dae3f1e62e9d969b4fe88a&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-15
fetch_date: 2025-10-06T18:26:50.112973
---

# 【安全圈】大蜘蛛发现针对安卓机顶盒的Android.Vo1d病毒 感染超过130万台设备

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht6l2nFGUznyE59FCR6CiaGsHdq9L2wia6IckbYqtItre7b2cd4IvLa5ibVg/0?wx_fmt=jpeg)

# 【安全圈】大蜘蛛发现针对安卓机顶盒的Android.Vo1d病毒 感染超过130万台设备

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

系统病毒

网络安全公司大蜘蛛 (Dr.Web) 在最新发布的博客中提到有一款针对安卓机顶盒的恶意软件正在广泛传播，该恶意软件被命名为 Android.Vo1d，在全球 197 个国家或地区中感染超过 130 万台设备。

该事件自 2024 年 8 月开始，当时大蜘蛛接到多个用户反馈称该安全软件检测到设备系统文件分区发现变化，**该问题主要出现在以下型号和固件版本中：**

* 设备名称：R4 系统版本：Android 7.1.2 构建版本：R4 Build/NHG47K
* 设备名称：TV BOX 系统版本：Android 12.1 构建版本：TV BOX Build/NHG47K
* 设备名称：KJ-SMART4KVIP 系统版本：Android 10.1 构建版本：SJ-SMART4KVIP Build/NHG47K

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht6nSoNOicSW5mte9nWyR9jjtagtiaj7sMxBicrMkdCrWZciaCWIcTpbJC7kg/640?wx_fmt=png&from=appmsg)

**大蜘蛛进行分析后发现所有出现异常的设备的系统分区都出现了四个新文件：**

* /system/xbin/vo1d
* /system/xbin/wd
* /system/bin/debuggerd
* /system/bin/debuggerd\_real

其中 vo1d 和 wd 文件是木马程序组件，基于这个名称大蜘蛛将该病毒命名为 Android.Vo1d 的原因，至于黑客选择的名字也有迷惑性，其故意将 void 中的 i 改成 1，可能是用来迷惑某些用户让用户误以为这是正常文件。

黑客使用 install-recovery.sh 脚本在系统启动时运行病毒并且具有 root 权限，因此可以在这些安卓机顶盒上执行任意操作。

**统计表明此次攻击似乎没有针对特定区域的特点，感染数量最多的国家或地区分别是：**

* 巴西
* 摩洛哥
* 巴基斯坦
* 沙特阿拉伯
* 俄罗斯
* 阿根廷
* 厄瓜多尔
* 突尼斯
* 马来西亚
* 阿尔及利亚
* 印度尼西亚

目前还不清楚该病毒通过何种方式进行广泛传播，但这些安卓机顶盒运行的多数都是过期的老旧安卓版本，这些版本无法获得安全更新因此现有漏洞可以被利用。

大蜘蛛安卓版现已将 Android.Vo1d 添加到定义更新中，如果大蜘蛛具有 root 访问权限则可以清除病毒，如果没有 root 权限可能也无法彻底删除病毒。

来源：大蜘蛛发现针对安卓机顶盒的Android.Vo1d病毒 感染超过130万台设备 – 蓝点网 (landiannews.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccHv6u9KrSpvq29PNagJll5hNGOzLAbxdyydCGW5fmibrvpP05TOfibDlw/640?wx_fmt=jpeg)[【安全圈】新型 Vo1d 恶意软件曝光，超130万台安卓电视设备已中招](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=1&sn=86872ba5c7fd0a8fb03d84febaa490d2&chksm=f36e6633c419ef2582f41f7358b5a94ec9e1ea409cbd54a4e4038c81e4f7ee545452d86a80ca&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccwgHI6ds7LRyGAxHH65BGRIicoyrib1ADicuTbN0zNqz29mCVgRNC5tw0w/640?wx_fmt=png)[【安全圈】天翼云盘主域名遭微软报毒拉黑 目前Microsoft Edge会自动拦截访问](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=2&sn=9c6331bd04185788e03156e723c86aba&chksm=f36e6633c419ef255b39135c006f3d38b741d9c8a4e855bf8fa5e646b10097ea01536887ee14&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0cc8Victdkjliaiabp79icS3ucppL0Ok6LPGVTGnicLQJ9IPR7Bl4EE5UtcUicA/640?wx_fmt=png)[【安全圈】网络安全软硬件开发商飞塔(Fortinet)泄露约440GB客户相关的数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=3&sn=f978ad9b352ecb4006ea727e1d181157&chksm=f36e6633c419ef2503fda40defd9a7dbec8f80967a704f4e9c017c684beff17192e2ce836029&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccT1lic86Mh3JWP1gwibcNKYchKuP7Gq21gKs7LZcQ9volJtyicr2MHdutA/640?wx_fmt=png)[【安全圈】Windows 11 22H2版将在下月结束支持 微软从10月8日起开始强制更新](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=4&sn=463256c6b4a84c7f835c4ac8d4e9add2&chksm=f36e6633c419ef2584a9d72c9ee174a113221b71c6bf04386e34a5a1be07a81daef4426f791e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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