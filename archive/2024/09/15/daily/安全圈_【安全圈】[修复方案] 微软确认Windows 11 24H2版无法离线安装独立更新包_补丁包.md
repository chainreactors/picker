---
title: 【安全圈】[修复方案] 微软确认Windows 11 24H2版无法离线安装独立更新包/补丁包
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064389&idx=3&sn=1266912d4c300ee9ce656070ee322533&chksm=f36e66c5c419efd340031b902182e025447945a5cfbfe2696e1bca04d28dd62a7b6fa4e41e9b&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-15
fetch_date: 2025-10-06T18:26:49.146474
---

# 【安全圈】[修复方案] 微软确认Windows 11 24H2版无法离线安装独立更新包/补丁包

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht6LzJblNicxKp9CjJrLp4QlfWjcJ7RyVC4JiardKK3ibKCUdKZEEWjy2tFw/0?wx_fmt=jpeg)

# 【安全圈】[修复方案] 微软确认Windows 11 24H2版无法离线安装独立更新包/补丁包

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

Windows系统

今年 7 月份微软宣布为 Windows 11 24H2 版和 Windows Server 2025 版推出检查点累积更新，这种微软开发的新版更新方式，可以缩减补丁包体积并加快安装速度。

不过这个问题似乎导致目前无法在离线状态下安装累积更新，当用户下载并尝试安装 MSU 格式的安装包时会失败并提示操作不受支持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht61LmibkzDibkgqrnt5qq2zqyW3PjExUyWQVYPy59fLbxibicXCWDqiaD6kYA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht6fibVO7hd5ya9hbf44yC3Mj0iaUZnLmQd9cArfb7f884AiaGrcrqWXxlCQ/640?wx_fmt=png&from=appmsg)

**下面是解决方案：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht63xNU0Hw9SUmfyhibUIiaUcTIvOQcRCHA9qFBAqYjOJbdOmnicm0vp8oXA/640?wx_fmt=png&from=appmsg)

**如果要通过 DISM 命令操作：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht6eBMqLfpT48eCZw3op17qGGBygz4bnJRD3gtJjySw3bneNoylWEfLcA/640?wx_fmt=png&from=appmsg)

具体 WindowsPackage 命令的使用方法请参阅微软的技术支持文档：https://learn.microsoft.com/powershell/module/dism/add-windowspackage?view=windowsserver2022-ps

来源：[修复方案] 微软确认Windows 11 24H2版无法离线安装独立更新包/补丁包 – 蓝点网 (landiannews.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccHv6u9KrSpvq29PNagJll5hNGOzLAbxdyydCGW5fmibrvpP05TOfibDlw/640?wx_fmt=jpeg)[【安全圈】新型 Vo1d 恶意软件曝光，超130万台安卓电视设备已中招](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=1&sn=86872ba5c7fd0a8fb03d84febaa490d2&chksm=f36e6633c419ef2582f41f7358b5a94ec9e1ea409cbd54a4e4038c81e4f7ee545452d86a80ca&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccwgHI6ds7LRyGAxHH65BGRIicoyrib1ADicuTbN0zNqz29mCVgRNC5tw0w/640?wx_fmt=png)[【安全圈】天翼云盘主域名遭微软报毒拉黑 目前Microsoft Edge会自动拦截访问](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=2&sn=9c6331bd04185788e03156e723c86aba&chksm=f36e6633c419ef255b39135c006f3d38b741d9c8a4e855bf8fa5e646b10097ea01536887ee14&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0cc8Victdkjliaiabp79icS3ucppL0Ok6LPGVTGnicLQJ9IPR7Bl4EE5UtcUicA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccT1lic86Mh3JWP1gwibcNKYchKuP7Gq21gKs7LZcQ9volJtyicr2MHdutA/640?wx_fmt=png)

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