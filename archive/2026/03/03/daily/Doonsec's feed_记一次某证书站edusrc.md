---
title: 记一次某证书站edusrc
url: https://mp.weixin.qq.com/s/2YliuA_UFayeeS-_xjOBpA
source: Doonsec's feed
date: 2026-03-03
fetch_date: 2026-03-04T04:01:26.930377
---

# 记一次某证书站edusrc

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhg24XSxqCpekrAnucRqC5t7kexC4pcH2XX1k4DVkribkURj8DDx0owGhSgIB29KKULO4riajnXiaV8PIpPErXXejzSLryY4auT08E/0?wx_fmt=jpeg)

# 记一次某证书站edusrc

魔术师
魔术师

B1acktide安全团队

![]()

在小说阅读器中沉浸阅读

我有天由于心情好，突然想去挖一下edu，正好知道某高校出了证书，于是开始当牛马挖一下洞

该学校域名还挺多，通过我不断信息收集，发现某网页

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhh5cJic7xrU9pEicMB9LOAY2Q9a3z2pDIszJtQ4R3zEH0ibib6IpDGoqZGfXA5uiaSzAkicgsLQxNOfhF9IweoHPMmC682DZkUkyFXl8/640?wx_fmt=jpeg)

通过bp抓包，发现某处含有sql注入漏洞先观察数据包

![](https://mmbiz.qpic.cn/mmbiz_jpg/fE13Qb8uKhhwEhE3hckz5mMtK3hqtYDdeD2kOyOBYGu6zoDxjanExSOhqslxSW9KaEC5MA8EdAJNIAdTLWLOk96wXqrnMlHP7wxdKrTec8Y/640?wx_fmt=jpeg)

分析{"tablename":"screenimg","cols":["\*"],"values":["type = 1"],"order":"id asc"}

API接受JSON格式的查询参数（tablename，values，order）values参数直接包含SQL条件片段（"type = 1"）

如果后端未充分验证和过滤，攻击者可构造恶意输入

而且API似乎允许直接查询数据库表，这里就可能缺乏适当的权限验证机制，我们可以试着通过修改tablename等的值去试着访问一些敏感表

于是我们三个都修改试一下，构造sql语句进行测试，尝试获取全部表{"tablename":"information\_schema.tables","cols":["\*"],"values":["1=1"],"order":"table\_name asc"}

![](https://mmbiz.qpic.cn/mmbiz_jpg/fE13Qb8uKhgRfExzSB6sR8icWW6uve723ubovAPFcgAiaOtGdqJia3YSmzgKX1EoeJ77kjwdJqZsL3kMqTYNsujSHTh51xlmfDWykaia0sm1yR8/640?wx_fmt=jpeg)

谁知道直接就出来了，震惊了，赶紧提交了，后续就不搞了，点到就行，提交就行，最后也就高危拿到

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhiaCKqn3kFtVABnAQ3CJvPgxTPVJSnqQtX5uYXplq3p3Hfn9MicuvPjrIWuYZGCiatlxO2nASmicgk7lbV5ibc3SPKpzibPDATNxxC3E/640?wx_fmt=jpeg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

B1acktide安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

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