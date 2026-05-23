---
title: 工具推荐 | 基于Xposed / Lsposed的主动调用抽取壳脱壳工具
url: https://mp.weixin.qq.com/s/My-694sFZCpYibyFOeHsPg
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:33:12.201022
---

# 工具推荐 | 基于Xposed / Lsposed的主动调用抽取壳脱壳工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVl2AecLE3tYJfE2l7iaRiagJhtIib9YvhHtZhejVEs9VpicWRnQJRcTs4te3MJK4ZBLQN13gpD5icXwrGZdSu01hZJ8Kv5VUMhlHqno/0?wx_fmt=jpeg)

# 工具推荐 | 基于Xposed / Lsposed的主动调用抽取壳脱壳工具

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 457，阅读大约需 3 分钟

## 前言

**应用场景**：可以应对未对 Lsposed 设置有效检测的大部分的企业抽取壳和免费壳的 Dex 加固

项目地址：https://github.com/J5now/JDex2

![01bbe812bfc6a86d471e4b86860371ba.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlTMhkyHInSEf4qLYcasEI19P5oxic0kA0tc9jmjklecpAo1libm5mHQ7hOgKLSQvA0W43Il4bjWStyic88ebdiaXPjDYLsojTNAjc/640?from=appmsg "null")

01bbe812bfc6a86d471e4b86860371ba.png

官方介绍：https://bbs.kanxue.com/thread-290669.htm

作者在看雪的这篇文章里写得很详细，推荐去看。

**局限性**

* • 高度依赖于 Lsposed 的隐蔽性，如果 Lsposed 被检测则会直接闪退无法进行脱壳

## 快速使用

release 中下载 apk，Android 9.0+ 安装使用。

```
adb install JDex2_V1.6.apk
```

![04c06e97f92863e2d30f59951f37741e.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnf1HqTeveDfMyrEGibjuJkvibwwk2h6Lq0ibrE8sHF1OChX9Asz4hnXP5neCrAMG6GIM4MCka4ITsHe8ibu0wQNxRJklb73paaLqE/640?from=appmsg "null")

04c06e97f92863e2d30f59951f37741e.png

* • targetApp：目标 APP 包名
* • targetClass：指定要脱的壳的包路径 com.xxx（不设置可能会导致 JNI 引用过多，通常建议以 App 的包名前两层作为筛选）
* • blackListClass：填写某些导致 App 崩溃的类，如果崩溃则需要通过 JDex2 Debugger 的日志对某些类或者包进行筛选（由于写到本地性能开销过大所以没有写）
* • Debugger：输出完成主动调用的类列表（tag~=JDex2 Debugger）
* • Hook：使用 Hook 方式脱壳（不推荐使用）
* • innerClassesFilter：由于可能导致 JNI 引用数量过多，可以尝试关闭对内部类的主动调用，但是对某些壳，脱出来的匿名类依旧是空的，按需开启，建议使用黑名单过滤而不是本配置
* • invokeConstructors：是否进行主动调用脱壳
* • lazyDump：用于在筛选出导致闪退类的大致范围之后通过白名单进行主动调用筛选时，降低主动调用速度，以便更快的找到导致闪退的类/包

在 Lsposed 中启动模块，并勾选需要脱壳的 APP

![2ed99fa4fccc72b05e62af3157f4c5c0.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn7SCQHcT6r4EWS6aibPulLaicdjRxxo7HtbHd0JEwGrpIdxtBRk3v7MZj39cuPSafn76uMOkeyuicdBnfY1P2Pl2CoLcvq2SRsvQ/640?from=appmsg "null")

2ed99fa4fccc72b05e62af3157f4c5c0.png

dump 后的 dex 位于/sdcard/Android/data/包名/dumpDex/下
![1c34f371a1acaed48191e229cddf55a9.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVn1QvtFpMNbIM1JQfXtkygrn3bSFDsSkW5GAa2vVwkprHD6KicYnd00yyWBhicRokY19nzq6BRnZrB8e3AumXACZI5gJJiciaIBygc/640?from=appmsg "null")

1c34f371a1acaed48191e229cddf55a9.png

## 总结

工具高度依赖于 Lsposed 的隐蔽性，如果 Lsposed 被检测则会直接闪退无法进行脱壳。
项目地址：https://github.com/J5now/JDex2
官方介绍：https://bbs.kanxue.com/thread-290669.htm

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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