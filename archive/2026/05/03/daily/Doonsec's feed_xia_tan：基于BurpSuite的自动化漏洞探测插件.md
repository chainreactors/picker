---
title: xia_tan：基于BurpSuite的自动化漏洞探测插件
url: https://mp.weixin.qq.com/s/O5CYKKIsJ4R_QrzgiN0w7w
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:31:07.127928
---

# xia_tan：基于BurpSuite的自动化漏洞探测插件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicJEoLhU0U48WiaYU7fia1NsWaiar0USsZPU48T59forpMJpECR7W5v25wyWTl5NHiaH2kO8etsh1ApvchjwhClhM6jHJ1KwVN0R3PA/0?wx_fmt=jpeg)

# xia\_tan：基于BurpSuite的自动化漏洞探测插件

原创

网安工具库
网安工具库

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[科来抓包：企业级小白可用的流量分析工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487269&idx=1&sn=5ffd4013d8725f181b344501f46c43b3&scene=21#wechat_redirect)

·[网安人的五一活动-集赞免费领六大付费工具！](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487239&idx=1&sn=c6ce3018816376ecd509d17001850677&scene=21#wechat_redirect)

·[Misc-Galaxysail：一站式 CTF Misc 杂项分析工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487238&idx=1&sn=e703c19069376df0616c7fa1f50a014a&scene=21#wechat_redirect)

·[CialloVOL 1.2：便捷好用的轻量化内存取证分析平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487188&idx=1&sn=e79b9644800b6e2a27241243fad4f56f&scene=21#wechat_redirect)

·[近期你还有这些CTF比赛可以参加](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487155&idx=1&sn=8dbf634d2c54d83eb5baa5fcb781b98a&scene=21#wechat_redirect)

·[USB抓包工具：Bus Hound](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487129&idx=1&sn=c837679e94cfa86982879523fcde61ed&scene=21#wechat_redirect)

**背景分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicI8fXnb7wRtIlnbjyyKrww2ibhcwrgPUa0q0AnjjPSGa9VzElG9o6rbdaAJhdPiaPxs0fSgwiaicApicMG37O6Gpm39zkpibFbicBrk8U/640?wx_fmt=png&from=appmsg)

当前`Web`应用安全测试中，`XSS`漏洞、`SQL`注入、`SSTI`模板注入、`NoSQL`注入是高频出现的高危安全风险，传统检测方式依赖人工验证，效率低下，且常规工具易产生大量误报，增加安全测试人员的工作量。`xia_tan`作为一款`BurpSuite`扩展插件，针对上述四类漏洞实现自动化初步探测，采用行级`Jaccard`相似度算法与多步布尔盲注对照算法优化检测逻辑，有效降低漏洞误报率，支持多种数据库与模板引擎覆盖，能够辅助安全测试人员快速完成授权范围内的`Web`漏洞初步筛查，提升安全测试的整体效率。

**安装介绍**

```
●●●

地址：https://github.com/mapl3miss/xia_tan
```

环境依赖配置：

```
●●●

# 安装JDK 1.8及以上版本
# 安装BurpSuite工具
```

项目编译与构建：

```
●●●

# 克隆项目源码
git clone https://github.com/mapl3miss/xia_tan.git
# 进入项目根目录
cd xia_tan
# 执行编译脚本
build.bat
# 编译完成后，插件文件位于build/libs目录下
```

`BurpSuite`插件加载步骤：

```
●●●

# 1. 打开BurpSuite
# 2. 进入Extender模块
# 3. 选择Extensions选项
# 4. 点击Add按钮
# 5. 选择Java类型，加载build/libs目录下的xia_tan-1.0.jar文件
# 6. 加载成功后，BurpSuite界面出现xia_tan标签页
```

功能介绍

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJbv0hURwVVEFgM5NibDdavVxlJBdocRbZPAMJrketchvhib0TGVhsKTDHbx4Lak3GaOSgIkTFvjUYeA5dSibib9czwgDa8CunxdYk/640?wx_fmt=png&from=appmsg)

`xia_tan`插件核心作用为自动化初步探测`Web`应用漏洞，支持检测的漏洞类型包括反射`XSS`、`SQL`注入、`SSTI`模板注入、`NoSQL`注入，插件无明确给出可直接调用的代码，仅通过图形化界面完成操作。

插件具备广泛的适配能力，`SQL`注入检测支持10种数据库，`SSTI`模板注入检测支持20种以上的模板引擎，能够满足多数主流`Web`应用的漏洞检测需求。

插件采用行级`Jaccard`相似度算法进行基础漏洞检测，针对布尔盲注场景采用多步布尔盲注对照算法，通过优化算法逻辑，大幅降低漏洞检测的误报率，提升检测结果可靠性。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJgTAd9iaicMDoovXIBLa8yurmRbCKNpG0jrQkTyOzhS89gI2ujArdSGVfAqmEYkFUnFqq0AObVCSFMkeD9KuicvHt19ibWhicyiaWfg/640?wx_fmt=png&from=appmsg)

插件支持手动扫描与自动扫描两种工作模式，同时支持`Cookie`参数场景下的漏洞探测，支持延时注入检测功能，还可配置域名过滤、路径过滤、参数过滤规则，支持`CUD`接口开关控制，满足多样化的安全测试场景需求。

插件运行后，会在`BurpSuite`的专属标签页内展示漏洞检测结果，安全测试人员可根据结果进行后续的人工验证工作，插件仅用于授权的安全测试场景，不可用于非法攻击行为。

如有想获得更多资源和网安圈交流，可以加入网安工具交流群~

![](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJBL7rS8Y8dicboGtjyjqmHvhGFMPiaeVBo32UsgmVGBPvryOlHrpvNzbENdcYnicBCrHBt52XHZyibCyVRVKGrVulIydoeribj7U8Q/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

网安工具库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

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