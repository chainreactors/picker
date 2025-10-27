---
title: APIFinderPlus API挖掘项目开源公测
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247489735&idx=1&sn=75382a87c35b3de0c7f9a88ef127af4a&chksm=fad4c5d0cda34cc6b0a1d75a694c35a7032016e8633c0804c2f5914cd53fd9a9f1d4f0c2b139&scene=58&subscene=0#rd
source: NOVASEC
date: 2024-10-10
fetch_date: 2025-10-06T18:54:04.892025
---

# APIFinderPlus API挖掘项目开源公测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/toroKEibicmZCXDKLtq3R7icicTVxUljDOnTuF5RK35aG77Jy0iaZ5F1dcoLbnialfM02Il5Fy2gczCGdKsqFo8VSo6A/0?wx_fmt=jpeg)

# APIFinderPlus API挖掘项目开源公测

原创

酒零

NOVASEC

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZDxicuqPkFfjdG2kcyzCXrXf0zrlDGZOnCofnEffxJaK5EDWfvZprrvHVAGSxiaSeXibS6GerhEAsLjw/640?wx_fmt=png)

***△△△点击上方“蓝字”关注我******们了解更多精彩***

**0x00 前言**

**免责声明：继续阅读文章视为您已同意[**[**NOVASEC免责声明**](http://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247489726&idx=1&sn=e5459d91f53caf90e76c6558dc8b4ac9&chksm=fad4c5a9cda34cbf0d02c24383827a906e7d08d5694d452a0cc18988f130abab371735ee1843&scene=21#wechat_redirect)**].**

前段时间开放内测的APIFinderPlus插件经过内测似乎没有得到什么功能上的建议，功能似乎已经完善,考虑开源项目收集更多建议.

致谢项目原始开发大佬@Shaun

致谢项目开发这几个月的实测大佬 @LiuYuChi @WangYiRan

使用说明略显繁杂，更多的按钮功能可以鼠标悬浮提示.

**0x01 APIFinderPlus:**

目标是成为当下最完善的API挖掘工具，实现自动提取响应敏感信息、URI信息，并且对URI进行自动|手动递归检查。

```
https://github.com/winezer0/APIFinderPlus
```

功能介绍：

做最全面的API挖掘工具、 减少手动拼接Path的提取测试、 补充无法自动处理的操作、

1、支持 响应 信息中的敏感信息、URL、URI提取.

2、支持 自动基于 已知路径信息 计算PATH 对应的实际URL.

3、支持 自动访问 挖掘出来的URL信息 进行递归式的信息提取.

4、支持 对webpack的js的简单格式的拼接提取 （限制格式，但准确度高）

欢迎大家Star.

**0X02 其他说明**

当前插件可以通过【当前路径拼接】和【有效路径计算】，计算出可能的API路径。

**当前路径拼接：**直接拼接当前文件路径和提取结果，适用于部分场景，在部分场景下存在限制

举例：

```
有效路径：http://www.baidu.com/aaa/xxx.js提取路径：/bbb计算结果：http://www.baidu.com/aaa/bbb
```

**有效路径计算：**基于有效路径和带目录的提取路径进行计算，适用于部分场景,在部分场景下存在限制

举例：

```
有效路径：http://www.baidu.com/aaa/xxx提取路径：aaa/bbb计算结果：http://www.baidu.com/aaa/bbb
```

**手动指定场景：**

对于更多复杂的场景，如（前后端分离）已知有效路径，但是有效路径不是当前域名的，可以调用右键功能 手动指定有效路径，为当前提取API结果进行指定根URL的拼接。

举例：

```
提取路径：aaa/bbb指定路径：http://api.baidu.com/aaa/xxx计算结果：http://api.baidu.com/aaa/bbb
```

**通过 CONF\_DEFAULT\_PERFORMANCE 进行关键配置：**

```
分段正则处理的大小："maxPatterChunkSizeDefault=20000",（默认5w以下即可,通过缩小处理内容节省内存占用）
最大保留的响应体大小： "maxStoreRespBodyLenDefault=1200000",（保留的响应体会在内容中限制,可能会导致显示卡顿）
执行线程间隔时间/秒:"monitorExecutorIntervalsDefault=4",（定时执行挖掘任务的时间频率,4线程电脑可改为2(秒)）
有效路径记录功能:"autoRecordPathIsOpenDefault=true",（建议开启,未开启就无法动态计算API)
动态有效路径筛选："dynamicPathFilterIsOpenDefault=false",（在当网站任何不存在的路径都是200响应时开启）
根据有效路径筛选计算API："autoPathsToUrlsIsOpenDefault=false",（建议开启,未开启就无法动态计算API)
自动递归访问URL："autoRecursiveIsOpenDefault=false",（一般不需要开启,可以右键手动调用）
监听Proxy模块传入的流量："proxyListenIsOpenDefault=false",（一般需要开启,也可以右键转发报文到插件中）
自动刷新未访问URL ："autoRefreshUnvisitedIsOpenDefault=false",（数据库中有记录提取/计算的API是否已经访问过）（一般不需要开启,可以右键手动调用）
自动刷新UI表格："autoRefreshUiIsOpenDefault=false",（UI内容是定时从数据库提取更新的）（一般需要开启,也可以点击刷新按钮手动调用）
强制解码Unicode Json编码："forceDecodeUnicodeDefault=true"（部分场景的中文、斜杠转义,会导致正则提取失败）（建议开启）
```

配置修改后如果需要持久话需要点击功能按钮进行保存，下次重新加载插件会进行导入。

**0X03 总结**

在功能上目前程序基本已经覆盖API挖掘的常见方面，可以说是目前最全面的API挖掘工具。

部分场景由于JS混淆、前后端问题目前无法完整实现自动化。

前端API挖掘大部分情况是徒劳无功的，如果没有发现有效的结果，可能是正常的情况、也有可能是功能实现上的不足。

希望大家能够提供功能、开发建议。

![](https://mmbiz.qpic.cn/mmbiz_gif/icZfUh6Tsbv0xAFjs5qQlsFCCmymOS3Vq8v6OSKDP0pw3aoCD4OTqojr5NMysBOcoMehddw6JUqYXVuurThNLsQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

END

如您有任何投稿、问题、需求、建议

请NOVASEC公众号后台留言！

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCP3AeicSCQAYIOvxVDSRUxpiadmBKZ8gtggx02BmG1WwCqoM23l72qV8AiabXSRKjGmk8S1HS1nTjXw/640?wx_fmt=png)

或添加 NOVASEC 联系人

![](https://mmbiz.qpic.cn/mmbiz_jpg/toroKEibicmZD7m4f7uBkNfCG8BjypNEukN0Ht6Ha0XsryrmS5PAmaVeyzb3JzsH5ibx6DmpHq9e8agwMkccrwNSQ/640?wx_fmt=jpeg "微信图片_20201214143605.jpg")

感谢您对我们的支持、点赞和关注

加入我们与萌新一起成长吧！

**本团队任何技术及文件仅用于学习分享，请勿用于任何违法活动，感谢大家的支持！！**

预览时标签不可点

个人观点，仅供参考

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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