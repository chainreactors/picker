---
title: APP渗透测试之基础环境配置
url: https://mp.weixin.qq.com/s/i2gYi3UckCxHUGxGkpG_RA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:44:11.768700
---

# APP渗透测试之基础环境配置

# APP渗透测试之基础环境配置

原创

流岁金沙
流岁金沙

迷雾光航

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vDS9wSyn9iapoDZFUNJMGXrzeia57FQrVTauXs5h1zPxe7r11zKicAk1uHlSNWhq4tpMibZC3HxwRLBUk7nVKicmeibyKA4uHJnmENydbxTzhq4aA/640?from=appmsg)

APP渗透测试基础环境搭建

一、模拟器搭建APP测试环境

前言: 若是不想使用真机，可以尝试模拟器的方案，但是有些APP可能有模拟器检测，绕过不了的情况就只能用真机了。

**一些工具**

* 模拟器   （雷电模拟器）

* adb    安卓调试工具
* jadx    反编译工具
* frida    动态代码hook工具包
* frida-server   安卓端安装

1、开启root和adb调试

雷电模拟器的设置中即可设置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Jql0Y1qckZRA2mQicJXxsfZm5QBXYYbEYuJOmR9vKaPjfib6ibGX01qMwYVice6Rla1vU7cQy7BzGMA5TlzCP0If2ZbS9fYPibKqmOrcscBmOgPQ/640?from=appmsg)

2、LSPosed框架和Magisk安装

主要用于添加一些LSPosed模块，例如相信证书绕过证书信任问题等

雷电模拟器中使用原版的magisk一直有问题，这里使用大佬二开过的版本，参考链接如下：

https://zhuanlan.zhihu.com/p/1898362870061834749

* LSPosed插件安装

TrustMeAlready：绕过证书安全性检测
Inspeckage：动态分析安卓应用
webview：调试移动端网页

安装好后大概是如下

LSPosed框架，需要从通知栏点进去

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Jql0Y1qckZTAmDgvaugVLwxKicDgBAicB1BTAKicIUvmh5WIicMhiawENXRv9htJzfNXoRgP0h0kKqNJ1c3OiaHnZibfag1pnWFpXUdCVSLOsLZ0Eg/640?from=appmsg)

二开的magisk，注意是一个狐狸头像这个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Jql0Y1qckZQKwl1LAzqO0tVZ7tPrbVXBzHuTaaUH2TMBJfVpTuKzmFp8ml745xNzqgESYovR0xXFQic0PBbf5icsk2IHPOgQAQWEnqOpiagWick/640?from=appmsg)

3、burpsuite证书安装

参考以下链接

https://www.cnblogs.com/rsa64/p/20991868

4、配置burpsuite抓包

直接将apk文件拖入雷电模拟器中即可安装程序

设置wifi代理为burpsuite代理即可进行抓包（需要重启才能生效）

有些APP可能有wifi代理检测、证书是否信任检测等，后面再记录

![](https://mmbiz.qpic.cn/mmbiz_png/Jql0Y1qckZS29o81pTJ4T2DUCJIicfnXFzyh14mRH1GKLsCAQcvW5wv73hbxCMJUckMVRNq2BiaaNtPIhasLfcLb18D6pGc452aqu0MtcCoJ4/640?from=appmsg)

5、安装frida、frida-tools和frida-server

frida对于动态调试很有帮助，可以用来脱壳获取源码，拦截函数修改值，内存修改等操作

参考以下网站即可

https://blog.csdn.net/weixin\_31476015/article/details/161843928

实在不会装的话，直接连接adb后叫AI帮忙装一下就完事了，告别古法装环境的折磨

环境上差不多就是这么多，然后让AI直接帮忙脱壳，分析源码，测试接口，构造参数，等等等

二、真机搭建APP渗透测试环境

直接购置一台经过root的安卓机

安装如上的环境，大差不差，就不赘述了

三、本机的环境配置

* 反编译工具：jadx以及mcp插件，方便AI调用
* 抓包工具：burpsuite、reqable
* AI工具：Claude Code 、 dsh、codex等

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jJ8gG6mVnEFIJS8ZaAC70ibttTmGyY8Ued3BNFEbaVWibAhibYJCfGziaYzHLZiaS0IbmbXX9UXAl3WwuZ6Oxb9AUyw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过