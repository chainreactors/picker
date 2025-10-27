---
title: 自动化构建全版本安卓GKI内核模块，附代码
url: https://mp.weixin.qq.com/s?__biz=MzU3MTY5MzQxMA==&mid=2247484724&idx=1&sn=15ed88bfb0f44ff63a190e5d3f08d358&chksm=fcdd0539cbaa8c2f4ef8ad5eca410d1eb319b5c06eb655960f7e2265b85e1a7bc7746d902c6b&scene=58&subscene=0#rd
source: 软件安全与逆向分析
date: 2024-11-26
fetch_date: 2025-10-06T19:20:18.090832
---

# 自动化构建全版本安卓GKI内核模块，附代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k9S5z61JPnZc8pZuW1gtypLXIrotHh1f6gapsYEZnx8F5KRr96PA9uA0xhFibOiazScCibCMJ618CEqIbdS99afGw/0?wx_fmt=jpeg)

# 自动化构建全版本安卓GKI内核模块，附代码

原创

非虫

软件安全与逆向分析

在做安卓内核模块ko文件开发时，经常需要在多个GKI内核中测试与编译，这也是安卓系统定制课程中很多学员朋友们的需求。

由于内核模块树外开发需要编译一次GKI源码树，比较耗时，于是我就有了开发一个github action插件的想法，让这些工作全部自动化，经过两天的编码与测试，完成了第一个版本。

项目取名为android-kernel-build-action，目前支持GKI2.0发布的所有内核分支与

android16-6.12的内核与模块编译，理论也支持android-mainline的编译。

使用方法：把需要编译的内核模块的代码，以artifact的方式传上去。

然后调用action来编译。全版本编译如下：

```
build: name:GKIKernelModuleBuild runs-on:ubuntu-22.04 needs:upload-artifact strategy:   matrix:     tag:       -android12-5.10       -android13-5.10       -android13-5.15       -android14-5.15       -android14-6.1       -android15-6.6       -android16-6.12     arch:       -aarch64       -x86_64 steps:   -name:Maximizebuildspace     uses:easimon/maximize-build-space@master     with:       root-reserve-mb:8192       temp-reserve-mb:2048       remove-dotnet:'true'       remove-android:'true'       remove-haskell:'true'       remove-codeql:'true'   -name:CheckoutRepository     uses:actions/checkout@v4   -name:RunGKIKernelBuildAction     uses:./     with:       arch:${{ matrix.arch }}       tag:${{ matrix.tag }}       module-name:hello-ko       module-path:hello-ko
```

编译好后，会在github action的运行日志页面看到产物。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnZc8pZuW1gtypLXIrotHh1fOLEZy29CicnvfVeiaNRwCbdBnAWG9YHnBMdGRJljnL8Ue2qBEwORk8lA/640?wx_fmt=png&from=appmsg)

下载下来后，内核与ko文件一起打包了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnZc8pZuW1gtypLXIrotHh1fjIHu8NlV2hI1nCW0qLq1xaib0zr3CfYkN3xF26YJxCVo1sU2hicdktcg/640?wx_fmt=png&from=appmsg)

这个action用来做内核模块的多版本内核适配应该会有点用处，你说呢？

仓库代码开源地址：https://github.com/feicong/android-kernel-build-action

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

软件安全与逆向分析

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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