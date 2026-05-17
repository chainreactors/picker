---
title: 弱口令到Root Shell  配置正确的重要性
url: https://mp.weixin.qq.com/s/jQ9GGUXsCKJLS2zmIeJ_Uw
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:43.656898
---

# 弱口令到Root Shell  配置正确的重要性

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SPfHPOgCrHpvP0tlpl2941BVgYu9TzDhWwPczKYZUzroYEF9JOuRp32bB20bM9ticoNHdAaUEicWibR5O9o5DCo3clHfL4W0T00OnR9G3ZXnM8/0?wx_fmt=jpeg)

# 弱口令到Root Shell 配置正确的重要性

原创

YMsora
YMsora

YMs0ra的安全漫路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

记一次渗透RCE的过程 非常感谢F0r7yn渗透出的弱密码，让我登进了后台，因为是Eyoucms的模板，

![](https://mmbiz.qpic.cn/mmbiz_jpg/SPfHPOgCrHoRHwNXAULcBFGyE4JDc44cu2TyxRqvicic9VEncicDFp9KkC2xgF48sJe3Sjxjg2jibf7lEdCOhUL7RrSx5pqumuHS19Igdcv8H5M/640?wx_fmt=jpeg&from=appmsg)

并且下发的版本号是1.2.9,虽然是比较老的版本， 传统的文件上传被封死，绕过不了php，白名单过滤

![](https://mmbiz.qpic.cn/mmbiz_jpg/SPfHPOgCrHq7sBJCs8JGnbKibZQEURlrbvbkSVQWxemGAic6BEO3IlJZon1NNQ6DTffeJK3V2SrWQ545Ficv36J3fmcPnBQy1eHrXu7Iuh7ZEQ/640?wx_fmt=jpeg&from=appmsg)

发现有历史遗留问题，那就是file.php对于htm会对php代码进行渲染，

 查看disable\_function以及open\_basedir，

后者是tmp 前者基本所有的命令执行函数都被禁用，

想起PHP版本小于8.5，对于一个issue有些在意https://github.com/php/php-src/issues/21961

竞争绕过open\_basedir，但是对于disable\_function，

我尝试了自带的sqllite扩展，但是loadextension是关闭状态

以及curl的动态加载库等等，都失败了

但是这时agent注意到了FastCGI

nginx的流量是经过FastCGI给php-fpm的，它会监听一个入口

这可以是一个tcp开放端口，也可能是文件的表现形式

在tmp中查找到了sock文件，这时，我还可以执行PHP代码，这就闭环了

 我用

```
stream_socket_client("unix:///tmp/php-cgi-82.sock")
```

去连接这个sock，将open\_basedir和send\_mail的值

```
SCRIPT_FILENAME=/www/wwwroot/www.xxxx.com/public/.target.php
DOCUMENT_ROOT=/www/wwwroot/www.xxxx.com/public
PHP_VALUE=open_basedir=/
PHP_ADMIN_VALUE=sendmail_path=/www/wwwroot/www.xxxx.com/public/xxxx.sh
```

sendmail\_path在被呼出时会默认调用指向的文件，

直接改成要执行的脚本以绕过disable\_function，（其实可以直接改） 然后就拿到了基本的命令执行了，当然用户组还是www，

最后上copy-fail，拿到root，至此了结

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SPfHPOgCrHqnEGA5UdIaMIgRXzPnnCSh042ULM5KKfT02L44y1rmHfdXTK9kwOjfmrdQtueTpakrQ79Vwp4xdABk3GewsqGV8sdJLb8GKps/0?wx_fmt=png)

YMs0ra的安全漫路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SPfHPOgCrHqnEGA5UdIaMIgRXzPnnCSh042ULM5KKfT02L44y1rmHfdXTK9kwOjfmrdQtueTpakrQ79Vwp4xdABk3GewsqGV8sdJLb8GKps/0?wx_fmt=png)

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